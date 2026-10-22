"""Independent interval complex recurrence for the interior angular witness."""
from fractions import Fraction as Q
from mpmath import iv

def decode(s):
 neg=s.startswith('-');s=s.lstrip('+-');man,ex=s.split('p');whole,fract=man[2:].split('.');v=Q(int(whole+fract,16),16**len(fract))*Q(2)**int(ex)
 return -v if neg else v

def evaluate(p):
 iv.dps=180
 def a(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
 def f(t):
  sg,man,e,bc=t
  assert int(bc)>=0, 'nonfinite interval endpoint'
  return Q(-int(man) if sg else int(man))*Q(2)**int(e)
 def box(v):return {'lower_exact':str(f(v._mpi_[0])),'upper_exact':str(f(v._mpi_[1])),'display':str(v)}
 beta=[decode(s) for s in p['beta_hex']];co=[decode(s) for s in p['modal_A0_hex']];T=sum(map(decode,p['chebyshev_hex']),Q(0));k=Q(p['k']);pp=6+2*k/(2-k)
 th=iv.pi/4;root=(iv.cos(2*th),iv.sin(2*th));re=iv.mpf(1);im=iv.mpf(0);B=iv.mpf(0);C=iv.mpf(0)
 for m in range(max(len(beta),len(co))):
  if m<len(beta):B+=a(beta[m])*re
  if m<len(co):C+=a(co[m])*re
  re,im=re*root[0]-im*root[1],re*root[1]+im*root[0]
 zlo=Q(p['z_iv_bracket']['lower_exact_dyadic']);zhi=Q(p['z_iv_bracket']['upper_exact_dyadic']);z=iv.mpf([a(zlo).a,a(zhi).b])
 ct=iv.cos(th);st=iv.sin(th);L=a(p['L']);angular=ct**2*st
 tx=angular*(L**a(3-k))*iv.exp(B)*iv.exp(a(T)*(ct**a(pp-2))*st**2)
 tm=angular*(iv.exp(a(p['tplus']))**a(3-k))*(C+z)
 # F(0) is evaluated with theta=pi/2 directly rather than an alternating exact sum.
 Bb=sum((a(b)*iv.cos(m*iv.pi) for m,b in enumerate(beta)),iv.mpf(0));Df=(L**a(3-k))*iv.exp(Bb)*a(T)
 return {'method':'iv180 interval complex-root recurrence, split exponentials and independent integer-hex decoder','values':{k:box(v) for k,v in {'T1':a(T),'p':a(pp),'ThetaX':tx,'ThetaM':tm,'Delta':tx-tm,'D_F0':Df,'z':z}.items()},'counts':{'beta':len(beta),'outer':len(co),'chebyshev':6,'complex_recurrence_steps':260}}
