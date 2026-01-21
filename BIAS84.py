from math import *
from ti_system import *

while True:
    disp_clr()
    print("Class A Amp Bias Optimizer v1.1")

    example=int(input("Run Ward J. Helms' example\n(1=Yes, 0=No)? "))

    if example==0:
        Vcc=float(input("Vcc (V): "))
        deltaIcQ=float(input("Delta IcQ (%): "))/100
        TAmin=float(input("TAmin (°C): "))
        TAmax=float(input("TAmax (°C): "))
        Tjmax=float(input("Tjmax (°C): "))
        PDmax=float(input("PDmax (W): "))
        I1=float(input("I1 (A): "))
        deltaVBE=float(input("Delta Vbe (V): "))
        VBEmin=float(input("VBEmin (V): "))
        VBEmax=float(input("VBEmax (V): "))
        hFEmin=float(input("hFEmin: "))
        hFEmax=float(input("hFEmax: "))
    else:
        Vcc=30.0
        deltaIcQ=0.2
        TAmin=0.0
        TAmax=70.0
        Tjmax=150.0
        PDmax=0.36
        I1=0.001
        deltaVBE=0.1
        VBEmin=0.54
        VBEmax=0.74
        hFEmin=100.0
        hFEmax=600.0

    temp_coeff=-0.0022
    thetaJA=(Tjmax-25)/PDmax
    RLn=thetaJA*Vcc**2/(4.4*(Tjmax-TAmax))
    RE=0.1*RLn

    iteration=1
    max_iterations=10
    tolerance=0.005

    while iteration<max_iterations:

        IcQ=Vcc/(2*(RLn+RE))
        Ic_max=IcQ*(1+deltaIcQ)
        Ic_min=IcQ*(1-deltaIcQ)
        
        VCEmax=Vcc-Ic_max*(RLn+RE)
        Tmax=thetaJA*IcQ*(Vcc-(RLn+RE)*IcQ)+TAmax

        if Tmax>Tjmax:
            RL*=1.1
            continue

        VBEx=VBEmin+deltaVBE*log(Ic_max/I1,10)+temp_coeff*(Tmax-25)
        VCEmin=Vcc-Ic_min*(RLn+RE)
        
        Tmin=thetaJA*Ic_min*(Vcc-(RLn+RE)*Ic_min)+TAmin
        VBEn=VBEmax+deltaVBE*log(Ic_min/I1,10)+temp_coeff*(Tmin-25)
        
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
        print("Iteration: {:.0f}  ({:.1f}%)".format(iteration,100*delta))
        print("RL       = {:.0f} Ohms".format(round(10*RLn+1)/10))
        print("IcQ      = {:.1f} mA".format(1000*IcQ))
        print("Ic range = {:.1f} - {:.1f} mA".format(1000*Ic_min,1000*Ic_max))
        print("Tmax     = {:.1f} °C".format(Tmax))
        print("VBEx     = {:.3f} V".format(VBEx))
        print("Tmin     = {:.1f} °C".format(Tmin))
        print("VBEn     = {:.3f} V".format(VBEn))
        print("REn+1    = {:.1f} Ohms".format(round(10*RE)/10))
        print("Press any key to continue...")
        wait_key()

        standard_values=[820,910,1000,1100,1200]
        RLn=min([v for v in standard_values if v>=RLn],default=RLn)

        if delta<tolerance:
            break

        iteration+=1

    IcQ=Vcc/(2*(RLn+RE))
    Ic_max=IcQ*(1+deltaIcQ)
    Ic_min=IcQ*(1-deltaIcQ)

    Tmax=thetaJA*IcQ*(Vcc-(RLn+RE)*IcQ)+TAmax
    VBEx=VBEmin+deltaVBE*log(Ic_max/I1,10)+temp_coeff*(Tmax-25)

    Tmin=thetaJA*Ic_min*(Vcc-(RLn+RE)*Ic_min)+TAmin
    VBEn=VBEmax+deltaVBE*log(Ic_min/I1,10)+temp_coeff*(Tmin-25)

    numer=hFEmax*hFEmin*(RE*(Ic_max-Ic_min)+(VBEx-VBEn))
    denom=hFEmax*Ic_min-hFEmin*Ic_max
    RB=numer/denom
    Vbb=VBEn+Ic_min*((RB/hFEmin)+RE)

    if Vbb>=Vcc or Vbb<=0:
        Vbb=Vcc/2

    R1=RB*Vcc/Vbb
    R2=RB*Vcc/(Vcc-Vbb)

    if RE==0.0 or (RB+hFEmin*RE)==0.0:
        Ap_dB=0.0
    else:
        Ap=(RB*RLn*hFEmin)/(RE*(RB+hFEmin*RE))
        Ap_dB=10*log(Ap,10)

    Ps1=(Vcc**2)*RLn*(1-deltaIcQ)**2
    Ps2=(8*(RLn+RE)**2)
    Ps_mW=1000*Ps1/Ps2

    disp_clr()
    print("Optimzed Values:")
    print("R1  = {:.0f} Ohms".format(round(R1)))
    print("R2  = {:.0f} Ohms".format(round(R2)))
    print("RE  = {:.0f} Ohms".format(round(RE)))
    print("RL  = {:.0f} Ohms".format(round(10*RLn+1)/10))
    print("IcQ = {:.1f} mA".format(1000*IcQ))
    print("Ic range = {:.1f} - {:.1f} mA".format(1000*Ic_min,1000*Ic_max))
    print("Min gain = {:.1f} dB".format(Ap_dB))
    print("Min Ps   = {:.1f} mW".format(Ps_mW))
    print("Max Tj   = {:.1f} °C".format(Tmax))

    again=int(input("Run again (1=Yes, 0=No)? "))
    if again!=1:
        disp_clr()
        print("Goodbye!")
        break
