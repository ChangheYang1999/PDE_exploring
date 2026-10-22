"""Two exact far-axis certificates from independently imported core-aware JSON.

These are fixed-file applications of results57,68,69. No fitter code.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import argparse,json
import mpmath as mp
from core_generating_mp import sha
from analytic_far_mp import load_far
ap=argparse.ArgumentParser();ap.add_argument('root');args=ap.parse_args();root=Path(args.root)
out=root/'far_axes_exact';out.mkdir(exist_ok=True)
data=json.loads((root/'center_with_core/input.json').read_text())
if F(data['alpha'])!=3:raise ValueError('alpha3 only')
if sha(data['source'])!=data['source_sha256']:raise ValueError('source changed')
c=[[F(q) for q in row] for row in data['outer']];s,a=F(data['s']),F(data['a'])
now=lambda:datetime.now(timezone.utc).isoformat()
def weights(n,d,end):
    if end==0:
        return (F((-1)**n),F(-2*(-1)**n*n*n),F(4*(-1)**n*n*n*(n*n-1),3))[d]
    return (F(1),F(2*n*n),F(4*n*n*(n*n-1),3))[d]
def endpoint(end):
    return {(i,j):sum((q*weights(n,i,0)*weights(k,j,end) for n,row in enumerate(c) for k,q in enumerate(row)),F(0)) for i,j in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]}
def horizontal(p):
    p00,p01,p10,p11,p20,p21=[p[k] for k in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]]
    h=5*p00/3
    if h<=0:raise ArithmeticError('nonpositive local horizontal limiting chart')
    A=-p10/h;B=(p10*p01/h**4-p11/h**3)/s**2;g=2*A/9-6*B
    k0=(3*p10+p20)/2;k1=(3*p11+p21)/2
    L=-2*k0+4*p10*p10/(3*h);M=(-2*k1+14*p10*p11/(3*h)-4*p10*p10*p01/h**2)/s**2
    C1=L/h;D1=-L*p01/(s*s*h**4)+M/h**3
    return [-2*C1/9+6*D1,4*A*g/3,2*A*g/3],2/(3*h),F(1)
def vertical(p):
    p0,p0w,p1,p1w,p2,p2w=[p[k] for k in [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]]
    h=p0/s**2;j=s**4*(p0-p0w)/3
    if h<=0:raise ArithmeticError('nonpositive local vertical limiting chart')
    b=p1/s;c=s**5*(p1-2*p1w)/6;k0=(3*p1+p2)/2;k1=(3*p1w+p2w)/2
    L=-2*k0+2*b*b/(3*h);M=2*s**6*k1/3+2*b*c/(3*h)+2*b*b*j/h**2;d0=2*b*j/h-c
    return [-2*L/9+6*h*h*M-6*h*L*j,-4*b*b/(27*h)-4*b*d0*h,-8*b*b/(27*h)-8*b*d0*h],2*j*h,s*s*p0**3
N=100;elo=sum((F(3**k,factorial(k)) for k in range(N+1)),F(0));ehi=elo+F(3**(N+1),factorial(N+1))/(1-F(3,N+2))
c1=((1-1/elo)/3,(1-1/ehi)/3);c1sq=tuple(v*v for v in c1)
def serial(v):return {'lo':str(v[0]),'hi':str(v[1]),'display':[float(x) for x in v]}
def scale(v,c):return tuple(sorted(q*c for q in v))
def absolute(v):return (F(0) if v[0]<=0<=v[1] else min(map(abs,v)),max(map(abs,v)))
report={'utc':now(),'source_sha256':data['source_sha256'],'input_sha256':sha(root/'center_with_core/input.json'),'script_sha256':sha(__file__),'exp3':serial((elo,ehi)),'rows':[],
        'scope':'Exact local limiting-chart coefficient identities. Global candidate interpretation requires a separate positive global chart. Patches contribute no far coefficients. No finite-radius or supremum bound.'}
req=[]
for end,name,fn in [(0,'horizontal',horizontal),(1,'vertical',vertical)]:
    p=endpoint(end);terms,slope,pref=fn(p)
    val=scale(c1sq,sum(terms));force=a*slope;val=(val[0]+force,val[1]+force)
    den=scale(c1sq,sum(map(abs,terms)));den=(den[0]+abs(force),den[1]+abs(force))
    if den[0]<=0:raise ArithmeticError('zero denominator')
    av=absolute(val);ratio=(av[0]/den[1],av[1]/den[0]);Cd=scale(val,1/pref)
    target=scale(c1sq,-sum(terms)/slope) if slope else None
    req.append(target)
    row={'axis':name,'endpoint_data':{str(k):str(v) for k,v in p.items()},'Q123_c1_squared_factors':[str(q) for q in terms],'forcing_slope':str(slope),'positive_prefactor_denominator':str(pref),'C_div_xy':serial(Cd),'N20_div_xy':serial(scale(den,1/pref)),'grouped_ratio':serial(ratio),'required_amplitude':serial(target) if target else None,'nonzero_coefficient':Cd[0]*Cd[1]>0,'ratio_exceeds_1e_minus_6':ratio[0]>F(1,10**6)}
    mp.mp.dps=150;far=load_far(data['source']).section(F(end))
    for key,iv in [('C_div_xy',Cd),('grouped_div_ratio',ratio)]:
        lo,hi=[mp.mpf(x.numerator)/x.denominator for x in iv]
        if not lo<=far[key]<=hi:raise ArithmeticError(('independent MP mismatch',name,key))
    row['independent_MP150']='diagnostic agreement inside both exact intervals; no MP rounding certificate'
    report['rows'].append(row)
    print(name,'Cdiv',row['C_div_xy']['display'],'ratio',row['grouped_ratio']['display'],'a_required',row['required_amplitude']['display'] if target else None,flush=True)
report['amplitude_intervals_disjoint']=bool(all(req) and (req[0][1]<req[1][0] or req[1][1]<req[0][0]))
chart=root/'chart_certificate/replay.json'
if chart.exists():
    cr=json.loads(chart.read_text())
    if cr['status']!='CONFIRMED' or cr['pinned_source_sha256']!=data['source_sha256'] or cr['manufacture_mode'] or F(cr['delta'])<=0:raise ValueError('chart mismatch')
    for f,digest in cr['hashes'].items():
        if sha(f)!=digest:raise ValueError('chart dependency changed')
    report['global_chart']={'status':'CONFIRMED','replay_sha256':sha(chart),'delta':cr['delta']}
else:report['global_chart']={'status':'OPEN'}
report['end_utc']=now();(out/'certificate.json').write_text(json.dumps(report,indent=2)+'\n')
