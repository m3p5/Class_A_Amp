from math import *

def closest_resistor(r,series='E24',mode='closest'):
    if r<=0:
        return 0.0

    e12_bases=[1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
    e24_bases=[
        1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
        3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1
    ]

    bases=e12_bases if series.upper()=='E12' else e24_bases

    order=floor(log(r,10))
    
    candidates=[]
    for o in [order-1, order, order+1]:
        for b in bases:
            val=round(b*(10**o),1 if o<=1 else 0)
            if val>0:
                candidates.append(val)

    candidates=sorted(set(candidates))

    if mode=='next_higher':
        quals=[c for c in candidates if c>=r]
        if quals:
            return min(quals)
        else:
            return candidates[-1] if candidates else r
    else:
        return min(candidates,key=lambda c:abs(c-r))
