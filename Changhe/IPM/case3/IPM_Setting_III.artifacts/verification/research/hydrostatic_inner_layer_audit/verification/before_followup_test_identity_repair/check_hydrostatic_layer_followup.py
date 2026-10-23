"""Independent checks of the written result215 follow-up; no producer imports."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import mpmath as mp
root=Path('research/hydrostatic_inner_layer_audit')
utc=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
out={'status':'RUNNING','start_utc':utc(),'pid':os.getpid(),'proof_sha256':sha(root/'FOLLOWUP_PROOF.md'),'code_sha256':sha(__file__),'checks':[],'numeric':[]}
def save(): (root/'verification/FOLLOWUP_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
    out['checks'].append({'name':name,'passed':bool(ok),'evidence':evidence})
    if not ok:
        out['status']='FAILED';save();raise AssertionError(name)
def zero(name,e): check(name,S.factor(e)==0)
p,z,x,y,K,Q,L,eps=S.symbols('p z x y K Q L eps',positive=True)
a=(1+p)/2;h=a*p;q=h+p-1;s=p-1/a;D=(1-p)/p;A=D/2;lam=4*p*p*K/((p+1)**2*(1-p))
T=lambda f:z*S.diff(f,z)
b=S.Function('b')(z)
P=lambda f,roots:T(T(T(f)))-sum(roots)*T(T(f))+sum(roots[i]*roots[j] for i in range(3) for j in range(i+1,3))*T(f)-S.prod(roots)*f
v=A*((p+2)*b-T(b))/(p*K)
equation=P(b,[p,s,p+2])-2*lam*S.diff(b,z,2)
H=(S.diff(b,z)+a*a*z*(T(v)-p*v))/(a*(s+1))
zero('horizontal differential identity modulo leading ODE',S.diff(H,z)-a*(T(v)-p*v)+a*A*equation/((s+1)*p*K*z))
zero('b0 transport relation',A*(p+2)/(p*K)-(1-h)/(p*p*K))
zero('axis curvature relation',-a*a*p*s-h*(1-h))
zero('positive gamma argument',1/(p+1)-p/2-(1-p)*(p+2)/(2*(p+1)))
zero('special s=-1',(s+1).subs(p,S.sqrt(2)-1))
t=S.symbols('t');poly=(t-p)*(t-s)*(t-p-2)
zero('logarithm polynomial derivative',S.diff(poly,t).subs(t,p)+2/a)
zero('necessary logarithm coefficient',(-a*lam*(p+1)*(p+2))*S.diff(poly,t).subs(t,p)-2*lam*(p+1)*(p+2))
m=p+eps/a;n=m-1/a;fast=p+2-eps/(1-a)
for label,beta,star,cinv in [('base',p-1,S.sqrt(5)-2,S.sqrt(5)+2),('self',h-1,(S.sqrt(17)-3)/4,(S.sqrt(17)+3)/2)]:
    zero(label+' resonance root',(m+1).subs(eps,beta).subs(p,star))
    zero(label+' reciprocal',1/star-cinv)
    for name,expr,want in zip(('m','n','fast'),(m,n,fast),((-S.Rational(1,6),-S.Rational(3,2),S.Rational(9,2)) if label=='base' else (-S.Rational(1,3),-S.Rational(5,3),S.Integer(5)))):
        zero(label+' c2 '+name,expr.subs(eps,beta).subs(p,S.Rational(1,2))-want)
zero('self resonance polynomial',(m+1).subs(eps,h-1)-(2*p*p+3*p-1)/(p+1))
# Derive sources directly in physical coordinates for independent monomial inputs.
for pr in [S.Rational(1,3),S.Rational(1,2),S.Rational(3,4)]:
    ar=(pr+1)/2;hr=ar*pr;qr=hr+pr-1;dr=2*pr-1
    zr=x/y**ar;BQr=K*Q/((1-pr)*((1-pr)/pr));aQr=Q/(pr*(1-pr))
    bg=BQr*y**dr+Q*x*x*y**(pr-2)/2
    for j in [0,1,2,4]:
        br=z**j;vr=2-z+3*z*z;HH=z+z**3
        u=y**qr*br.subs(z,zr);V2=y**hr*vr.subs(z,zr);V1=y**(hr+ar-1)*HH.subs(z,zr)
        direct=(-Q*x*y**(pr-1)/(1-pr))*S.diff(u,x)+aQr*y**pr*S.diff(u,y)+V2*S.diff(bg,y)+V1*S.diff(bg,x)
        F=-Q*z*S.diff(br,z)/(1-pr)+aQr*(qr*br-ar*z*S.diff(br,z))+vr*(dr*BQr+(pr-2)*Q*z*z/2)+Q*z*HH
        zero(f'physical base source p={pr} j={j}',S.expand_power_base((direct-y**(qr+pr-1)*F.subs(z,zr)).subs(x,z*y**ar),force=True))
        directself=V1*S.diff(u,x)+V2*S.diff(u,y)
        FN=HH*S.diff(br,z)+vr*(qr*br-ar*z*S.diff(br,z))
        zero(f'physical self source p={pr} j={j}',S.expand_power_base((directself-y**(qr+hr-1)*FN.subs(z,zr)).subs(x,z*y**ar),force=True))
F=S.Function('F')(z);B=S.Function('B')(z);W=(-F-A*(T(B)-fast*B))/(p*K)
zero('inhomogeneous eliminated sign',S.diff(B,z,2)+a*a*(T(T(W))-(m+n)*T(W)+m*n*W)+a*a*A/(p*K)*(P(B,[m,n,fast])-2*lam*S.diff(B,z,2)+(T(T(F))-(m+n)*T(F)+m*n*F)/A))
save()
mp.mp.dps=75
ps=[mp.mpf('.01'),mp.mpf('.2'),mp.mpf(1)/3,mp.sqrt(2)-1,mp.mpf('.5'),mp.mpf('.75'),mp.mpf('.99')]
def conn(aa,bb,ll,j):
    other=1-j
    return mp.gamma(bb[0])*mp.gamma(bb[1])*mp.gamma(aa[other]-aa[j])*mp.rgamma(aa[other])*mp.rgamma(bb[0]-aa[j])*mp.rgamma(bb[1]-aa[j])*ll**(-aa[j])
for pr in ps:
    ar=(1+pr)/2;hr=ar*pr;sr=pr-1/ar;dd=1/(1+pr);ll=4*pr*pr/((1+pr)**2*(1-pr))
    aa=[-pr/2,(1-pr)/2];bb=[1-dd,mp.mpf(2)]
    aa2=[aa[0]+dd,aa[1]+dd];bb2=[1+dd,2+dd]
    E1,O1=[conn(aa,bb,ll,j) for j in (0,1)];E2,O2=[conn(aa2,bb2,ll,j) for j in (0,1)]
    exact=mp.gamma(dd-pr/2)*mp.gamma((1+pr)/2)*ll**(pr/2)/(mp.sqrt(mp.pi)*mp.gamma(2+pr/2)*mp.gamma(dd))
    err=abs(E1-O1*E2/O2-exact)/(1+abs(exact))
    check('axis gamma positive identity '+str(pr),err<mp.mpf('1e-65'),mp.nstr(err,10))
    check('axis gamma strictly positive '+str(pr),exact>0)
    for beta in (pr-1,hr-1):
        mm=pr+beta/ar;nn=mm-1/ar;tt=pr+2-beta/(1-ar)
        check('correction gamma endpoint signs '+str((pr,beta)),(-nn/2)>0 and (1+tt)/2>0 and -2<mm<1)
    out['numeric'].append({'p':mp.nstr(pr,65),'axis_factor':mp.nstr(exact,50),'relative_identity_error':mp.nstr(err,10)})
# A fully independent Gaussian manufacture of the horizontal and vertical inverses.
for pr in [mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.8')]:
    ar=(1+pr)/2;hr=ar*pr;sr=pr-1/ar
    def IH(zz): return zz**(sr+1)/ar*mp.gammainc(-sr/2,0,zz*zz)
    def IV(zz):
        return (zz**pr*(2*mp.gammainc(1-pr/2,zz*zz,mp.inf)-mp.gammainc(-pr/2,zz*zz,mp.inf))+zz**sr*(2*mp.gammainc(1-sr/2,0,zz*zz)-mp.gammainc(-sr/2,0,zz*zz)))/ar
    for zz in [mp.mpf('.2'),mp.mpf(1),mp.mpf(3)]:
        physical=2*zz/(1-hr)*mp.quad(lambda u:mp.exp(-zz*zz*u**(2*ar/(1-hr))),[0,mp.mpf('.25'),1])
        check('Gaussian horizontal physical inverse '+str((pr,zz)),abs(physical-IH(zz))<mp.mpf('1e-60'))
        defect=mp.diff(IH,zz)-ar*(zz*mp.diff(IV,zz)-pr*IV(zz))
        check('Gaussian canonical incompressibility '+str((pr,zz)),abs(defect)<mp.mpf('1e-60'),mp.nstr(defect,8))
        relation=-2*zz*mp.exp(-zz*zz)+ar*(zz*mp.diff(IH,zz)-(sr+1)*IH(zz))
        check('Gaussian horizontal integrated identity '+str((pr,zz)),abs(relation)<mp.mpf('1e-60'))
for label,pr in [('base',mp.sqrt(5)-2),('self',(mp.sqrt(17)-3)/4)]:
    ar=(1+pr)/2;hr=ar*pr;beta=pr-1 if label=='base' else hr-1
    mm=pr+beta/ar;nn=mm-1/ar;tt=pr+2-beta/(1-ar)
    residue=mp.rgamma(-nn/2)*mp.rgamma((1+mm)/2)*mp.rgamma((1+tt)/2)
    check(label+' exact resonance vanishing reciprocal gamma',abs(residue)<mp.mpf('1e-70'))
    for direction in [-1,1]:
        perturb=pr+direction*mp.mpf('1e-6');ap=(1+perturb)/2;hp=ap*perturb;ep=perturb-1 if label=='base' else hp-1
        mm2=perturb+ep/ap;nn2=mm2-1/ap;tt2=perturb+2-ep/(1-ap)
        res2=mp.rgamma(-nn2/2)*mp.rgamma((1+mm2)/2)*mp.rgamma((1+tt2)/2)
        check(label+' perturbed connection nonzero '+str(direction),abs(res2)>mp.mpf('1e-12'))
out['status']='DONE';out['finished_utc']=utc();out['count']=len(out['checks']);save()
print(json.dumps({'status':out['status'],'checks':out['count'],'finished_utc':out['finished_utc']}))
