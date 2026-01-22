from ti_system import *
from BIASDEFA import compute_bias

while True:
    disp_clr()
    print("Class A Amp Bias Optimizer v2.0")
    example=int(input("Run Ward J. Helms' example\n(1=Yes, 0=No)? "))
    
    if example==1:
        p={
            'Vcc':30.0,
            'deltaIcQ':0.20,
            'TAmin':0.0,
            'TAmax':70.0,
            'Tjmax':150.0,
            'PDmax':0.36,
            'I1':0.001,
            'deltaVBE':0.1,
            'VBEmin':0.54,
            'VBEmax':0.74,
            'hFEmin':100.0,
            'hFEmax':600.0
        }
    else:
        p={}
        p['Vcc']=float(input("Vcc (V): "))
        p['deltaIcQ']=float(input("Delta IcQ (%): "))/100
        p['TAmin']=float(input("TAmin (°C): "))
        p['TAmax']=float(input("TAmax (°C): "))
        p['Tjmax']=float(input("Tjmax (°C): "))
        p['PDmax']=float(input("PDmax (W): "))
        p['I1']=float(input("I1 (A): "))
        p['deltaVBE']=float(input("Delta Vbe (V): "))
        p['VBEmin']=float(input("VBEmin (V): "))
        p['VBEmax']=float(input("VBEmax (V): "))
        p['hFEmin']=float(input("hFEmin: "))
        p['hFEmax']=float(input("hFEmax: "))

    result=compute_bias(p)

    disp_clr()
    print("Optimized Values:")
    print("R1  = {} Ohms".format(int(result['R1'])))
    print("R2  = {} Ohms".format(int(result['R2'])))
    print("RE  = {} Ohms".format(int(result['RE'])))
    print("RL  = {} Ohms".format(int(result['RLn'])))
    print("IcQ = {:.1f} mA".format(round(1000*result['IcQ'],1)))
    print("Ic range = {:.1f} - {:.1f} mA".format(round(1000*result['Ic_min'],1),round(1000*result['Ic_max'],1)))
    print("Min gain = {:.1f} dB".format(round(result['Ap_dB'],1)))
    print("Min Ps   = {:.1f} mW".format(round(result['Ps_mW'],1)))
    print("Max Tj   = {:.1f} °C".format(round(result['Tmax'],1)))

    again=int(input("Run again (1=Yes, 0=No)? "))
    if again!=1:
        disp_clr()
        print("Goodbye!")
        break
