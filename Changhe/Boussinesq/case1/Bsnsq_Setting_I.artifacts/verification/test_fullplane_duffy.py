"""Manufacture checks for the independent mixed-quadrant full-plane inverse.

Tests inverse signs, slow algebraic tails, both axes, source-chart Jacobian,
compactification scales/powers, and center strain. No Boussinesq solution claim.
"""
from pathlib import Path
import datetime,hashlib,json,math,time
import numpy as np
import mpmath as mp
import sympy as sy
from fullplane_duffy import folded_direct,folded_rational,integrate_velocity,integrate_center_strain
ROOT=Path.cwd();OUT=ROOT/'candidate_audits/mixed_quadrant_inverse/manufactured';OUT.mkdir(parents=True,exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
report=dict(start_utc=now(),sources={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in[Path(__file__),Path('code/fullplane_duffy.py')]},rows=[],algebra={})
store=lambda:(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n')

def source(kind,chart):
    def call(x,e):
        y=e if chart=='identity' else e+e**3;A=np.ones_like(e) if chart=='identity' else 1+3*e**2;s=x*x+y*y
        if kind=='gaussian':O=-2*x*y*(12-4*s)*np.exp(-s)
        else:
            p=1/6;O=-8*p*x*y*(3+(2-p)*s)*(1+s)**(-p-2)
        return dict(y=y,A=A,Omega=O)
    return call


def exact_U(kind,x,y):
    s=x*x+y*y
    if kind=='gaussian':f=np.exp(-s);fp=-f
    else:p=1/6;f=(1+s)**(-p);fp=-p*(1+s)**(-p-1)
    return np.array([2*x*(f+2*y*y*fp),-2*y*(f+2*x*x*fp)])


def main():
    a,b,x,y=sy.symbols('a b x y',real=True);R=a*a+b*b+x*x+y*y
    D=sy.prod((a-s*x)**2+(b-t*y)**2 for s in[-1,1] for t in[-1,1])
    # Use exact polynomial numerator identities rather than floating samples.
    den=lambda s,t:(a-s*x)**2+(b-t*y)**2
    num1=sy.expand(sum(s*t*(b-t*y)*sy.prod(den(ss,tt) for ss in[-1,1] for tt in[-1,1] if(ss,tt)!=(s,t)) for s in[-1,1] for t in[-1,1]))
    num2=sy.expand(sum(-s*t*(a-s*x)*sy.prod(den(ss,tt) for ss in[-1,1] for tt in[-1,1] if(ss,tt)!=(s,t)) for s in[-1,1] for t in[-1,1]))
    report['algebra']['kernel_num1']=bool(sy.expand(num1-8*a*x*y*(4*R*b*b-R*R-4*b*b*y*y+4*a*a*x*x))==0)
    report['algebra']['kernel_num2']=bool(sy.expand(num2-8*b*x*y*(R*R-4*R*a*a-4*b*b*y*y+4*a*a*x*x))==0)
    p=sy.symbols('p',positive=True);r=x*x+y*y;psi=-2*x*y*(1+r)**(-p);O=-8*p*x*y*(3+(2-p)*r)*(1+r)**(-p-2)
    report['algebra']['manufactured_poisson']=bool(sy.simplify(-sy.diff(psi,x,2)-sy.diff(psi,y,2)-O)==0)
    mp.mp.dps=80;kr=[]
    for xx,yy in[(.2,.4),(1e2,3e2),(1e6,3e6),(1e12,3e12),(1e30,3e30)]:
        aa,bb=mp.mpf('.7'),mp.mpf('1.2');mx,my=mp.mpf(xx),mp.mpf(yy);truth=[mp.mpf(0),mp.mpf(0)]
        for s in[-1,1]:
            for t in[-1,1]:
                dx,dy=aa-s*mx,bb-t*my;dd=dx*dx+dy*dy;truth[0]+=s*t*dy/dd/(2*mp.pi);truth[1]-=s*t*dx/dd/(2*mp.pi)
        direct=folded_direct(.7,1.2,np.array([xx]),np.array([yy]))[0];rational=folded_rational(.7,1.2,np.array([xx]),np.array([yy]))[0]
        err=lambda z:[float(abs(mp.mpf(str(z[i]))-truth[i])/abs(truth[i])) for i in range(2)]
        kr.append(dict(x=xx,y=yy,direct_relative=err(direct),rational_relative=err(rational)))
    report['kernel_mp']=kr;store()
    # Powers3 make the slow r^-1/3 tail more accessible to the quadrature.
    configs=[dict(n=n,scales=(1.,1.),powers=(3.,3.)) for n in[6,10,16,24]]
    configs+=[dict(n=24,scales=sc,powers=(3.,3.)) for sc in[(.3,.7),(3.,2.)]]
    targets=[(.7,1.2),(0.,1.3),(1.5,0.),(4.2,3.1)]
    for kind,chart in[('gaussian','identity'),('algebraic','identity'),('algebraic','cubic')]:
        f=source(kind,chart)
        for conf in configs:
            for a,b in targets:
                e=b if chart=='identity' else float(mp.findroot(lambda z:z+z**3-b,(0,max(1,b))))
                start=time.monotonic();v=integrate_velocity(f,(a,b),e,**conf)
                truth=exact_U(kind,a,b);error=np.asarray(v['U'])-truth
                report['rows'].append(dict(kind=kind,chart=chart,target=[a,b],eta=e,**v,expected_U=truth.tolist(),absolute_error=abs(error).tolist(),scaled_error=(abs(error)/(1+abs(truth))).tolist(),seconds=time.monotonic()-start))
                store()
            st=integrate_center_strain(f,**conf);report['rows'].append(dict(kind=kind,chart=chart,kind_of_check='center_strain',**st,expected_c=-2.,absolute_error=abs(st['c']+2)));store()
    finest=[r for r in report['rows'] if r['n']==24]
    report['gates']=dict(algebra=all(report['algebra'].values()),mp_far_rational=max(max(r['rational_relative']) for r in kr)<1e-12,
                         finest_velocity=max(max(r['scaled_error']) for r in finest if 'scaled_error'in r)<1e-5,
                         finest_strain=max(r['absolute_error'] for r in finest if r.get('kind_of_check')=='center_strain')<1e-5)
    report['all_pass']=all(report['gates'].values());report['end_utc']=now();store();print(json.dumps(dict(end=report['end_utc'],gates=report['gates'],all_pass=report['all_pass'])),flush=True)

if __name__=='__main__':main()
