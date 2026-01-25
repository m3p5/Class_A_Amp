from math import *
from ti_system import *
from BIASDEFB import closest_resistor

def compute_bias(p):
    deltaIcQ=p['deltaIcQ']
    temp_coeff=-0.0022
    thetaJA=(p['Tjmax']-25)/p['PDmax']
    RLn=thetaJA*p['Vcc']**2/(4.4*(p['Tjmax']-p['TAmax']))
    RE=0.1*RLn

    iteration=1
    max_iterations=10
    tolerance=0.005

    while iteration<max_iterations:
        IcQ=p['Vcc']/(2*(RLn+RE))
        Ic_max=IcQ*(1+deltaIcQ)
        Ic_min=IcQ*(1-deltaIcQ)
        
        VCEmax=p['Vcc']-Ic_max*(RLn+RE)
        Tmax=thetaJA*Ic_max*(p['Vcc']-(RLn+RE)*Ic_max)+p['TAmax']

        if Tmax>p['Tjmax']:
            RLn*=1.1
            iteration+=1
            continue

        VBEx=p['VBEmin']+p['deltaVBE']*log(Ic_max/p['I1'],10)+temp_coeff*(Tmax-25)
        VCEmin=p['Vcc']-Ic_min*(RLn+RE)
        
        Tmin=thetaJA*Ic_min*(p['Vcc']-(RLn+RE)*Ic_min)+p['TAmin']
        VBEn=p['VBEmax']+p['deltaVBE']*log(Ic_min/p['I1'],10)+temp_coeff*(Tmin-25)
        
        REnew=-2*(VBEx-VBEn)/(Ic_max-Ic_min)
        
        if REnew<0:
            REnew=0.0
            RLn*=1.1

        if RE>0:
            delta=abs(REnew-RE)/RE
        else:
            delta=1.0

        RE=REnew

        disp_clr()
        print("Iteration: {}  ({:.1f}%)".format(iteration,round(100*delta,1)))
        print("RL       = {} Ohms".format(int(RLn+0.5)))
        print("IcQ      = {:.1f} mA".format(round(1000*IcQ,1)))
        print("Ic range = {:.1f} - {:.1f} mA".format(round(1000*Ic_min,1),round(1000*Ic_max,1)))
        print("Tmax     = {:.1f} °C".format(round(Tmax,1)))
        print("VBEx     = {:.3f} V".format(round(VBEx,1)))
        print("Tmin     = {:.1f} °C".format(round(Tmin,1)))
        print("VBEn     = {:.3f} V".format(round(VBEn,3)))
        print("REn+1    = {:.1f} Ohms".format(round(REnew,1)))
        print("Press any key to continue...")
        wait_key()

        RLn=closest_resistor(RLn,mode='next_higher')

        if delta<tolerance:
            break

        iteration+=1

    RE=closest_resistor(RE,mode='next_higher')

    IcQ=p['Vcc']/(2*(RLn+RE))
    Ic_max=IcQ*(1+deltaIcQ)
    Ic_min=IcQ*(1-deltaIcQ)

    Tmax=thetaJA*Ic_max*(p['Vcc']-(RLn+RE)*Ic_max)+p['TAmax']
    VBEx=p['VBEmin']+p['deltaVBE']*log(Ic_max/p['I1'],10)+temp_coeff*(Tmax-25)

    Tmin=thetaJA*Ic_min*(p['Vcc']-(RLn+RE)*Ic_min)+p['TAmin']
    VBEn=p['VBEmax']+p['deltaVBE']*log(Ic_min/p['I1'],10)+temp_coeff*(Tmin-25)

    numer=p['hFEmax']*p['hFEmin']*(RE*(Ic_max-Ic_min)+(VBEx-VBEn))
    denom=p['hFEmax']*Ic_min-p['hFEmin']*Ic_max
    RB=numer/denom if abs(denom)>1e-8 else 100000.0
    Vbb=VBEn+Ic_min*((RB/p['hFEmin'])+RE)

    if Vbb>=p['Vcc'] or Vbb<=0:
        Vbb=p['Vcc']/2

    R1=RB*p['Vcc']/Vbb
    R2=RB*p['Vcc']/(p['Vcc']-Vbb)

    R1=closest_resistor(R1)
    R2=closest_resistor(R2)

    if RE==0.0 or (RB+p['hFEmin']*RE)==0.0:
        Ap_dB=0.0
    else:
        Ap=(RB*RLn*p['hFEmin'])/(RE*(RB+p['hFEmin']*RE))
        Ap_dB=10*log(Ap,10)

    Ps1=(p['Vcc']**2)*RLn*(1-deltaIcQ)**2
    Ps2=(8*(RLn+RE)**2)
    Ps_mW=1000*Ps1/Ps2

    return {
        'R1':R1,
        'R2':R2,
        'RE':RE,
        'RLn':RLn,
        'IcQ':IcQ,
        'Ic_min':Ic_min,
        'Ic_max':Ic_max,
        'Ap_dB':Ap_dB,
        'Ps_mW':Ps_mW,
        'Tmax':Tmax
    }
    