from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
import mpmath as mp
from negative_slope_dictionary import dictionary,functionals,affine,start,evaluate,residual
R=Path('research/negative_slope_independent_trials');V=R/'verification';mp.mp.dps=55;checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(name,got,want,tol=2e-10):
    if isinstance(want,bool): error=0 if bool(got)==want else 1;passed=error==0
    else: error=float(abs(mp.mpf(float(got))-mp.mpf(want))/(1+abs(mp.mpf(want))));passed=math.isfinite(error) and error<tol
    checks.append(dict(name=name,passed=passed,error=error,tolerance=tol))
def direct_green(n,beta,r,k):
    f=lambda s:s**n*(1+s*s)**(-beta)
    fp=lambda s:n*s**(n-1)*(1+s*s)**(-beta)-2*beta*s**(n+1)*(1+s*s)**(-beta-1)
    q=(lambda s:(fp(s)-n*f(s)/s)/2) if k==n+1 else (lambda s:(fp(s)+n*f(s)/s)/2)
    inner=mp.quad(lambda s:s**(k+1)*q(s),[0,r])
    outer=mp.quad(lambda s:s**(1-k)*q(s),[r,max(r,mp.mpf(1)),mp.inf])
    return (r**(-k)*inner+r**k*outer)/(2*k)
def independent_psi(n,beta,x,y):
    r=mp.sqrt(x*x+y*y);th=mp.atan2(y,x)
    # Independent arbitrary-precision stream; derivatives taken in Cartesian coordinates.
    A=mp.hyp2f1(beta,n+1,n+2,-r*r)*r**(2*n+2)/(2*(n+1))
    ans=-A*r**(-n-1)*mp.sin((n+1)*th)/2
    if n>=3:ans+=r**(n-1)*(1+r*r)**(1-beta)*mp.sin((n-1)*th)/(4*(beta-1))
    return ans
for pp in [Fraction(1,2),Fraction(2,3),Fraction(1,3)]:
    rows=dictionary(pp,6,5,5);base,T,k,s,c=affine(rows,pp)
    ck(f'{pp} unique pairs',len({(z['n'],z['beta']) for z in rows})==len(rows),True)
    ck(f'{pp} affine gauge',np.max(np.abs(k@T)),0)
    ck(f'{pp} affine base',k@base,-1)
    ck(f'{pp} affine slope',np.max(abs(s@T-np.eye(1,T.shape[1],0)[0])),0)
    for aa in [-4,-16,-64]:
        z=start(rows,pp,aa);a=base+T@z
        ck(f'{pp} start{aa} slope',s@a,aa);ck(f'{pp} start{aa} center',c@a,1-1/float(pp));ck(f'{pp} start{aa} K',k@a,-1)
    # Entire realistic dictionary over a much wider range than training.
    rr=np.geomspace(1e-5,1e5,75);th=.417+np.arange(75)*.007
    fs=evaluate(rows,rr*np.cos(th),rr*np.sin(th));ck(f'{pp} finite whole dictionary',all(np.isfinite(v).all() for v in fs.values()),True)
    for n,j,ell in [(1,0,0),(1,3,1),(3,0,0),(3,2,2),(7,1,1),(11,4,4)]:
        beta=(n-pp)/2+j+ell*(1-pp)/2;bm=mp.mpf(beta.numerator)/beta.denominator
        row=dict(n=n,beta=str(beta));tag=f'p{pp}n{n}j{j}l{ell}'
        for rf in [.03,.7,4,40]:
            r=mp.mpf(str(rf));theta=mp.mpf('.63');x=r*mp.cos(theta);y=r*mp.sin(theta)
            fs=evaluate([row],[float(x)],[float(y)])
            ps=lambda xx,yy:independent_psi(n,bm,xx,yy)
            density=lambda xx,yy:mp.im((xx+1j*yy)**n)*(1+xx*xx+yy*yy)**(-bm)
            target={'rho':density(x,y),'dx':mp.diff(lambda xx:density(xx,y),x),'dy':mp.diff(lambda yy:density(x,yy),y),'psi':ps(x,y),'ux':-mp.diff(lambda yy:ps(x,yy),y),'uy':mp.diff(lambda xx:ps(xx,y),x)}
            for key in fs:ck(tag+f'r{rf} {key}',fs[key][0,0],target[key],3e-9)
            poisson=-mp.diff(lambda xx:ps(xx,y),x,2)-mp.diff(lambda yy:ps(x,yy),y,2)
            ck(tag+f'r{rf} poisson',float(poisson),target['dx'],1e-12)
            if rf in [.7,4]:
                green=direct_green(n,bm,r,n+1)*mp.sin((n+1)*theta)
                if n>=3:green+=direct_green(n,bm,r,n-1)*mp.sin((n-1)*theta)
                ck(tag+f'r{rf} complete source Green',float(green),target['psi'],1e-12)
        # Small Cartesian derivative of the complete stream, no constrained center row.
        expected=mp.mpf(-1)/4 if n==1 else 1/(2*(bm-1)) if n==3 else 0
        eps=mp.mpf('1e-8');ck(tag+' center limit',float(independent_psi(n,bm,eps,eps)/(eps*eps)),expected,1e-11)
    # Independent central difference of the nonlinear finite residual map.
    rows=dictionary(pp,3,3,2);base,T,k,s,c=affine(rows,pp);z=start(rows,pp,-4)
    rr=np.geomspace(.002,100,39);th=np.linspace(.03,1.54,39);x=rr*np.cos(th);y=rr*np.sin(th)
    fs=evaluate(rows,x,y);a=base+T@z;rr0,_,_,jac,_=residual(fs,a,x,y,1/float(pp))
    for seed in range(3):
        d=np.random.default_rng(seed).normal(size=len(z));h=2e-5
        rp=residual(fs,base+T@(z+h*d),x,y,1/float(pp))[0];rm=residual(fs,base+T@(z-h*d),x,y,1/float(pp))[0]
        ck(f'{pp} jacobian direction{seed}',np.max(abs((rp-rm)/(2*h)-jac@T@d)),0,1e-7)
    xm=evaluate(rows,-x,y);ym=evaluate(rows,x,-y)
    for key,sx,sy in [('rho',1,-1),('dx',-1,-1),('dy',1,1),('ux',-1,1),('uy',1,-1),('psi',-1,-1)]:
        ck(f'{pp} parityx{key}',np.max(abs(xm[key]-sx*fs[key])),0,1e-8);ck(f'{pp} parityy{key}',np.max(abs(ym[key]-sy*fs[key])),0,1e-8)
# Regression for the observed refined-dictionary far-field failure and switch.
for pp in [Fraction(1,2),Fraction(2,3),Fraction(1,3)]:
    refined=dictionary(pp,6,6,4);rr=np.geomspace(1e-5,1e7,97)
    ff=evaluate(refined,rr*np.cos(.63),rr*np.sin(.63));ck(f'{pp} refined finite to1e7',all(np.isfinite(v).all()for v in ff.values()),True)
    for n in [1,3,7,11]:
        for j in [0,5]:
            for ell in [0,3]:
                beta=(n-pp)/2+j+ell*(1-pp)/2;bm=mp.mpf(beta.numerator)/beta.denominator;row=dict(n=n,beta=str(beta))
                for rf in [7.99,8,8.01,1e3,1e5,1e7]:
                    r=mp.mpf(str(rf));theta=mp.mpf('.63');x=r*mp.cos(theta);y=r*mp.sin(theta);fs=evaluate([row],[float(x)],[float(y)])
                    ps=lambda xx,yy:independent_psi(n,bm,xx,yy)
                    density=lambda xx,yy:mp.im((xx+1j*yy)**n)*(1+xx*xx+yy*yy)**(-bm)
                    targets={'rho':density(x,y),'dx':mp.diff(lambda xx:density(xx,y),x),'dy':mp.diff(lambda yy:density(x,yy),y),'psi':ps(x,y),'ux':-mp.diff(lambda yy:ps(x,yy),y),'uy':mp.diff(lambda xx:ps(xx,y),x)}
                    for key in fs:ck(f'far regression{pp}n{n}j{j}l{ell}r{rf} {key}',fs[key][0,0],targets[key],3e-9)
reviews={}
for name,complete in [('opus_review',False),('opus_followup',False),('opus_dictionary_review',True),('opus_dictionary_clarification',True)]:
    d=V/name;m=json.loads((d/'metadata.json').read_text());payload=json.loads((d/'response.json').read_text())
    ck(name+'actual model',m['returned_model']==payload['model']=='claude-opus-5-5',True)
    ck(name+'completion',m['stop_reason']=='end_turn',complete)
    reviews[name]={p.name:sha(p) for p in d.iterdir() if p.is_file()}
out=dict(status='PASS'if all(z['passed'] for z in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,reviews=reviews,proof_sha256=sha(R/'PROOF.md'),addendum_sha256=sha(R/'DICTIONARY_ADDENDUM.md'),far_repair_proof_sha256=sha(R/'FAR_EVALUATOR_REPAIR_PROOF.md'),module_sha256=sha(Path('independent_code/negative_slope_dictionary.py')),driver_sha256=sha(Path(__file__)))
(V/'DICTIONARY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([z for z in checks if not z['passed']])
if out['status']!='PASS':raise SystemExit(1)
