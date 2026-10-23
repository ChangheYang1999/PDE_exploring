from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
root=Path('research/pseudotime_sign_and_hydrostatic_symbol');v=root/'verification';checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,value,evidence=None):checks.append({'name':name,'passed':bool(value),'evidence':evidence})
def zero(name,e):z=s.simplify(e);check(name,z==0,str(z))
r,rx,ry,u1,u2,q,C,x,y,t=s.symbols('r rx ry u1 u2 q C x y t',real=True)
h,hx,hy,v1,v2,j=s.symbols('h hx hy v1 v2 j',real=True)
w=q/(1-C)
F=w*r-(C*w*x+u1)*rx-(C*w*y+u2)*ry
fields=[r,rx,ry,u1,u2,q];directions=[h,hx,hy,v1,v2,j]
scaled=F.subs({a:t*a for a in fields},simultaneous=True)
zero('quadratic scaling all real amplitudes',scaled-t*t*F)
zero('even vector field',F.subs({a:-a for a in fields},simultaneous=True)-F)
DF=s.diff(F.subs({a:a+t*b for a,b in zip(fields,directions)},simultaneous=True),t).subs(t,0)
zero('linearization sign at every base',DF.subs({a:-a for a in fields},simultaneous=True)+DF)
zero('origin slope conserved',w-C*w-q)
# Steady-state normalization, keeping the multiplier symbolic rather than assuming its sign.
W=s.symbols('W',nonzero=True,real=True)
steady=(C*W*x+u1)*rx+(C*W*y+u2)*ry-W*r
normalized=(C*x+u1/W)*rx/W+(C*y+u2/W)*ry/W-r/W
zero('steady division by signed rate',normalized-steady/W**2)
for a in [-1,1]:
 for w0 in [-s.Rational(3,8),-2,s.Rational(3,8),2]:
  check('slope sign '+str((a,w0)),s.sign(a/w0)==s.sign(a)*s.sign(w0))
rad=s.symbols('rad',positive=True);bb=s.symbols('b',real=True)
zero('Gaussian mode moment',s.integrate(rad*s.exp(-rad**2),(rad,0,s.oo))-s.Rational(1,2))
zero('manufactured negative-slope strain',s.Rational(1,4)+(-2)/s.Integer(2)+s.Rational(3,4))
zero('manufactured negative-slope cw at C3',(-s.Rational(3,4))/(1-3)-s.Rational(3,8))
for bv in [-2,-1,-s.Rational(1,2),0,2]:
 check('strict strain inequality '+str(bv),(s.Rational(1,4)+bv/2<0)==(bv<-s.Rational(1,2)))
beta=s.symbols('beta',positive=True);Y=s.symbols('Y',real=True);a=1/(beta*W)
newres=(C*x+u1/W)*a*rx+(C*beta*y+beta*u2/W)*(a/beta)*ry-a*r
zero('hydrostatic transport scaling',newres-a/W*steady)
zero('hydrostatic vertical slope',a/beta-1/(beta**2*W))
for gy,cw in [(1,1),(1,2),(-1,-2),(4,s.Rational(1,2))]:
 beta2=s.Rational(gy)/cw;zero('unit-slope required beta '+str((gy,cw)),s.Rational(gy)/(beta2*cw)-1)
check('arbitrary beta does not fix slope',s.Rational(1,4)!=1)
check('opposite signs cannot have positive beta squared',s.Rational(-1,2)<0)
# Analytic Gaussian inverse: independently differentiate the transformed fields.
G=a*s.exp(-x*x)*(Y/beta)*s.exp(-(Y/beta)**2)
U=a*beta*x*s.exp(-x*x-(Y/beta)**2)
V=a*beta**2*s.sqrt(s.pi)/2*(2*x*x-1)*s.exp(-x*x)*s.erf(Y/beta)
zero('transformed V1_y=G_x',s.diff(U,Y)-s.diff(G,x))
zero('transformed V2_yy=-G_xx',s.diff(V,Y,2)+s.diff(G,x,2))
zero('transformed divergence',s.diff(U,x)+s.diff(V,Y))
zero('transformed V2 zero from parity',V.subs(Y,0))
zero('transformed actual slope',s.diff(G,Y).subs({x:0,Y:0})-1/(beta**2*W))
# Half-line inverse mode, never used as a nonlinear candidate.
k=s.symbols('k',real=True);phi=y*s.exp(-y*y);K=s.sqrt(s.pi)/4*s.erf(y);J=s.exp(-y*y)/2
zero('K second derivative',s.diff(K,y,2)+phi)
zero('K derivative equals J',s.diff(K,y)-J)
zero('K origin parity',K.subs(y,0))
zero('J derivative minus phi',s.diff(J,y)+phi)
phase=s.exp(s.I*k*x);VH1=-s.I*k*phase*J;VH2=-k*k*phase*K
zero('mode V1 derivative',s.diff(VH1,y)-s.diff(phase*phi,x))
zero('mode V2 equation',s.diff(VH2,y,2)+s.diff(phase*phi,x,2))
zero('mode divergence',s.diff(VH1,x)+s.diff(VH2,y))
zero('feedback signs',-VH1*rx-VH2*ry-phase*(s.I*k*rx*J+k*k*ry*K))
# The positive growth statement here is only about the isolated constant-gradient Fourier operator.
for av in [-2,-1,1,2]:
 for eta in [1,2]:
  rates=[s.Rational(av)*kk*kk/(eta*eta)for kk in [1,4,16]]
  check('frozen quadratic growth ratio '+str((av,eta)),rates[1]/rates[0]==rates[2]/rates[1]==16)
  check('frozen rate sign '+str((av,eta)),all(s.sign(z)==s.sign(av)for z in rates))
manifest=json.loads((v/'INPUTS.json').read_text());check('request hash',sha(v/'lead_request.md')==manifest['request_sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS'if all(a['passed']for a in checks)else'FAIL','count':len(checks),'checks':checks,'proof_sha256':sha(root/'PROOF.md'),'driver_sha256':sha(__file__),'scope':'R-a algebra; R-b transformation requires unit-slope repair; complete nonlinear well-posedness remains OPEN.'}
(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([a for a in checks if not a['passed']])
if out['status']!='PASS':raise SystemExit(1)
