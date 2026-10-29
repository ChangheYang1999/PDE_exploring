# Independent lead cross-check of topic 91 (local axis-root certificate for critical/L0 near z ~ 0.062 reporting).
# Own polynomial construction (explicit Legendre sum and sympy chebyshevt, not the verifier's expand_ball or recurrence),
# own enclosure method (mean-value form with mpmath interval arithmetic, not the translated-polynomial bound).
# Reads the verifier's frozen files read-only; writes only checks/topic91_check_output.json.
import json, hashlib, time
from fractions import Fraction as Fr
from math import factorial
import numpy as np, sympy as sp, mpmath
from mpmath import iv
V='independent_validation/'
A_='axisymmetric_euler_24h/'
inp=json.load(open(V+'research/near_axis_stagnation/data/inputs.json'))
out={}; ok=[]
def chk(name,cond,**kw):
    ok.append((name,bool(cond))); out[name]=dict(passed=bool(cond),**{k:str(v) for k,v in kw.items()})
for key,p in inp['paths'].items():
    chk('sha256 '+key, hashlib.sha256(open(V+p,'rb').read()).hexdigest()==inp['sha256'][key])
d=np.load(V+inp['paths']['coefficients'],allow_pickle=False); meta=json.loads(str(d['meta_json']))
el=meta['elements'][0]; Rb=sp.Rational(Fr(float(el['Rhi']))); cl=sp.Rational(Fr(float(meta['cl'])))
chk('c_l = 1/2', cl==sp.Rational(1,2))
s,z=sp.symbols('s z')
def solid(n):  # R^n P_n(z/R), R^2 = s + z^2, explicit sum
    return sp.expand(sum(sp.Rational((-1)**m*factorial(2*n-2*m),2**n*factorial(m)*factorial(n-m)*factorial(n-2*m))
                         *z**(n-2*m)*(s+z**2)**m for m in range(n//2+1)))
x=sp.Symbol('x')
def poly(key):
    tot=0
    for (n,k),v in zip(el['labels'],d[key+'_el0']):
        n=int(n); k=int(k)
        T=sp.chebyshevt(k,x).subs(x,2*(s+z**2)/Rb**2-1)
        tot+=sp.Rational(Fr(float(v)))*solid(n)/Rb**n*T
    return sp.Poly(sp.expand(tot),s,z)
t0=time.time()
phi=poly('phi'); q=poly('q')
out['expand_seconds']=time.time()-t0
# numeric cross-check of the construction at two points against scipy special functions
from scipy.special import eval_legendre, eval_chebyt
for (sv,zv) in [(0.01,0.25),(0.2,-0.3)]:
    R=np.sqrt(sv+zv*zv); val=sum(float(v)*(R/float(Rb))**int(n)*eval_legendre(int(n),zv/R)*eval_chebyt(int(k),2*R*R/float(Rb)**2-1)
                                 for (n,k),v in zip(el['labels'],d['phi_el0']))
    chk('construction vs scipy at s=%g z=%g'%(sv,zv), abs(val-float(phi.eval({s:sv,z:zv})))<1e-11*max(1,abs(val)), diff=abs(val-float(phi.eval({s:sv,z:zv}))))
L=sp.Rational(Fr(float(json.load(open(V+inp['paths']['geometry']))['gauge']['dilation_L'])))
c=sp.Rational(Fr(inp['box']['z_center_working'])); S=sp.Rational(Fr(inp['box']['s_max_working'])); Z=sp.Rational(Fr(inp['box']['z_halfwidth_working']))
chk('box inside ball', S+(abs(c)+Z)**2<Rb**2)
A=sp.Poly(cl-phi.diff(z).as_expr(),s,z)
As=A.diff(s); Az=A.diff(z)
A0=A.eval({s:0,z:c})
iv.prec=200
def ivpoly(P,sI,zI):
    tot=iv.mpf(0)
    for (i,j),v in P.terms():
        tot+=iv.mpf(sp.Rational(v).p)/iv.mpf(sp.Rational(v).q)*sI**i*zI**j
    return tot
def ivr(r): r=sp.Rational(r); return iv.mpf(r.p)/iv.mpf(r.q)
sI=iv.mpf([0,ivr(S).b]); zI=iv.mpf([ivr(c-Z).a,ivr(c+Z).b]); dz=iv.mpf([-ivr(Z).b,ivr(Z).b])
encl=ivr(A0)+ivpoly(As,sI,zI)*sI+ivpoly(Az,sI,zI)*dz
chk('A > 0 on the rectangle (mean-value interval form)', encl.a>0, lower=encl.a, upper=encl.b)
chk('A < 3 c_l/2 on the rectangle', encl.b<ivr(3*cl/2).a)
qencl=ivr(q.eval({s:0,z:c}))+ivpoly(q.diff(s),sI,zI)*sI+ivpoly(q.diff(z),sI,zI)*dz
chk('q > 0 on the rectangle', qencl.a>0, lower=qencl.a, upper=qencl.b)
B=lambda zz: cl*zz+2*phi.eval({s:0,z:zz})
bl=B(c-Z); br=B(c+Z)
chk('B(c - Z) < 0 exact', bl<0, value=float(bl)); chk('B(c + Z) > 0 exact', br>0, value=float(br))
inv=json.load(open(V+inp['paths']['inventory']))['detected_roots']
o=[p for p in inv if 0<p['r']<1e-5][0]
pr=sp.Rational(Fr(o['r']))/L; pz=sp.Rational(Fr(o['z']))/L
chk('alleged off-axis point inside rectangle', pr**2<=S and abs(pz-c)<=Z)
Wr_rep=L*pr*A.eval({s:pr**2,z:pz})   # reporting W_r = L * working W_r at the corresponding point (velocity scales by L)
chk('W_r > 0 exactly at the alleged off-axis point', Wr_rep>0, reporting_Wr=float(Wr_rep), working_Wr=float(pr*A.eval({s:pr**2,z:pz})))
out['A_axis_center']=float(A0)
out['all_passed']=all(v for _,v in ok); out['n_checks']=len(ok)
json.dump(out,open('author_checks/topic91_check_output.json','w'),indent=1)
print(json.dumps(out,indent=1))
