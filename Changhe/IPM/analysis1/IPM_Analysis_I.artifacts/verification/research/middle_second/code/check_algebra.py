"""Independent exact oracles for production quantization/convolution/remainders."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib
from mpmath import iv
import cell_iv as c

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enclosed(x,target):lo,hi=c.ends(x);assert lo<=target<=hi

def run():
 Q=16;P=512;base=33;den=2**(2*P);data=c.setup(F(1,5),F(7),Q,P)
 checks=defaultdict(int)
 # Small exact trigonometric products, with terms at the maximum mode/degree.
 V={(0,0):F(3,5),(1,7):F(-2,3),(260,16):F(1,7)}
 D={(0,16):F(-4,5),(1,0):F(2,7),(260,16):F(3,11)}
 def models(src):
  out=[([iv.mpf(0)]*17,iv.mpf(0)) for j in range(261)]
  for (j,l),v in src.items():out[j][0][l]=c.iq(v)
  return out
 for vk,dk,kind in [('velocity_cos','density_sin','cos_sin'),('velocity_sin','density_cos','sin_cos')]:
  ve=c.angular(models(V),vk,Q,P);de=c.angular(models(D),dk,Q,P);mc,rc=c.convolve(ve,de);exact=defaultdict(F)
  for (j,l),v in V.items():
   m=2*j+2
   for (n,d),value in D.items():
    nu=2*n+1
    frequencies=(nu+m,nu-m) if kind=='cos_sin' else (m+nu,m-nu)
    for freq in frequencies:exact[abs(freq),l+d]+=(1 if freq>0 else -1)*v*value/2
  for slot in range(1044):
   freq=2*(slot-522)+1
   for l in range(33):
    target=(1 if freq>0 else -1)*exact[abs(freq),l]
    mi,ri=int(mc[slot*base+l]),int(rc[slot*base+l]);assert ri>=0
    assert F(mi-ri,den)<=target<=F(mi+ri,den),(kind,slot,l);checks['integer_convolution_all_degrees_and_mirrors']+=1
 # Outward quantization, including the separate 2P scale used by Lin.
 for q in [F(-7,3),F(-1,2**600),F(0),F(1,3),F(2**1020+1,2**600)]:
  for prec in [512,1024]:
   x=c.iq(q);mi,ri=c.quant(x,prec);assert F(mi-ri,2**prec)<=q<=F(mi+ri,2**prec);checks['quantization']=checks['quantization']+1
 # Expand Bernstein basis functions back into powers, an independent matrix oracle.
 for degree in range(Q+1):
  bs=[F(row[degree],math.factorial(Q)) for row in data['matrix']]
  actual=[F(0)]*17
  for j,bj in enumerate(bs):
   for l in range(Q-j+1):actual[j+l]+=bj*math.comb(Q,j)*math.comb(Q-j,l)*(-1)**l
  expected=[F(math.comb(degree,l)*2**l*(-1)**(degree-l)) if l<=degree else F(0) for l in range(17)]
  assert actual==expected;checks['Bernstein_basis_coefficients']+=17
  p=[0]*17;p[degree]=1
  assert c.bernstein_max(p,[0]*17,data['matrix'])==math.factorial(Q);checks['known_monomial_maxima']+=1
 # Production polynomial truncation and the complete product error radius.
 ops=c.model_ops(F(0),F(1,7),Q);mul=ops['multiply'];p=[iv.mpf(0)]*17;p[-1]=iv.mpf(1)
 pol,rem=mul((p,iv.mpf(0)),(p,iv.mpf(0)));assert all(c.ends(v)==(0,0) for v in pol) and c.ends(rem)==(1,1);checks['degree32_tail']=1
 x=([iv.mpf(2)]+[iv.mpf(0)]*16,iv.mpf(3));y=([iv.mpf(-5)]+[iv.mpf(0)]*16,iv.mpf(7))
 pol,rem=mul(x,y);assert c.ends(pol[0])==(-10,-10) and c.ends(rem)==(50,50);checks['product_error_radius_attained']=1
 def value(p,v):return sum((x*c.iq(v**j) for j,x in enumerate(p)),iv.mpf(0))
 def error_check(actual,model,v):
  p,r=model;lo,hi=c.ends(actual-value(p,v));bound=max(abs(lo),abs(hi));assert bound<=c.ends(r)[0],(str(bound),str(r));checks['sampled_remainder_enclosures']+=1
 # Non-polynomial exp models, including negative exponents and nonzero centers.
 for tc,h,lam in [(F(0),F(1,7),F(3)),(F(-5,7),F(1,100),F(-3))]:
  ops=c.model_ops(tc,h,Q);coef=[iv.mpf(2),iv.mpf(-1),iv.mpf(3)];tm=ops['exp_poly'](coef,lam)
  for v in [F(-1),F(-1,3),F(0),F(1,5),F(1)]:
   actual=iv.exp(c.iq(lam*(tc+h*v)))*(2-c.iq(v)+3*c.iq(v*v));error_check(actual,tm,v)
  p1=ops['exp_poly']([iv.mpf(1)],F(2));p2=ops['exp_poly']([iv.mpf(1)],F(3));tm=ops['multiply'](p1,p2)
  for v in [F(-1),F(0),F(1)]:error_check(iv.exp(c.iq(5*(tc+h*v))),tm,v)
 # Non-polynomial ODE solutions, zero forcing and a nonzero g_Q case.
 h=F(1,7)
 for lam in [F(-12),F(12)]:
  tm=c.closed_ode(iv.mpf(1),lam,1,[iv.mpf(0)],h,Q)
  for v in [F(-1),F(-1,2),F(1,2),F(1)]:error_check(iv.exp(c.iq(lam*h*v)),tm,v)
 lam=F(2);ell=lam*h;g=[iv.mpf(0)]*17;g[-1]=iv.mpf(1);tm=c.closed_ode(iv.mpf(1),lam,-1,g,h,Q)
 for v in [F(-1),F(-1,2),F(1,2),F(1)]:
  poly=[iv.mpf(0)]*17;poly[-1]=iv.mpf(1)
  integ=c.integrate_exp_poly(poly,abs(v),-ell if v>0 else ell)
  if v<0:integ=-integ
  actual=iv.exp(c.iq(ell*v))*(1-c.iq(h)*integ);error_check(actual,tm,v)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ALGEBRA_AND_REMAINDER_CONTRACTS','checks':dict(checks),'source_sha256':sha(Path(__file__)),'cell_iv_sha256':sha(Path(c.__file__)),'iv_dps':iv.dps,'mpmath_version':c.mpmath.__version__,'python_flint_version':c.flint.__version__}
 E=c.BASE/'research/middle_second/evidence';out=E/'algebra_contracts.json';tmp=out.with_suffix('.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
 print(json.dumps(result),flush=True)
if __name__=='__main__':run()
