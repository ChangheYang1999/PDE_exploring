"""Real-space kernel validation of the independently derived radial mode constants."""
from pathlib import Path
import sys,json,math
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse'/'code'))
from realspace import velocity

def field(x,y):return x*x*y*np.exp(-x*x-y*y)
def modes(r):
    S=r*r/16;T=0.;Sp=r/8;Tp=0.
    for n in range(40):
        b=(-1.)**n/math.factorial(n)
        power=2*n+4
        sn=-b*(n+2)/(8*(n+1)*(n+3))*r**power
        tn=-b/(16*(n+4))*r**power
        S+=sn;T+=tn;Sp+=power*sn/r;Tp+=power*tn/r
    return S,T,Sp,Tp

def analytic(x,y):
    r=np.hypot(x,y);t=np.arctan2(y,x)
    S,T,Sp,Tp=modes(r)
    ur=-(2*S*np.cos(2*t)+4*T*np.cos(4*t))/r
    ut=Sp*np.sin(2*t)+Tp*np.sin(4*t)
    return np.array([ur*np.cos(t)-ut*np.sin(t),ur*np.sin(t)+ut*np.cos(t)])
rows=[]
for nang in (512,1024):
    for x,y in ((.2,0.),(.1,0.),(.05,0.),(.02,0.),(.2,.1),(.1,.05),(.05,.025),(.02,.01)):
        u,_=velocity(field,(x,y),nang=nang,order=16,panel=.2,rmin=1e-9,rmax=32.)
        ex=analytic(x,y)
        row={'nang':nang,'point':[x,y],'kernel':u.tolist(),'radial_series':ex.tolist(),'max_error':float(np.max(np.abs(u-ex)))}
        if y==0:row['cubic_axis_coefficient']=(float(u[0])+x/8)/x**3
        rows.append(row);print(json.dumps(row),flush=True)
result={'status':'floating manufactured tests, not interval certificates','max_error':max(t['max_error'] for t in rows),'expected_axis_cubic_coefficient':11/48,'rows':rows}
p=Path(__file__).resolve().parents[1]/'verification'/'gaussian.json';p.write_text(json.dumps(result,indent=2)+'\n')
assert result['max_error']<2e-13
