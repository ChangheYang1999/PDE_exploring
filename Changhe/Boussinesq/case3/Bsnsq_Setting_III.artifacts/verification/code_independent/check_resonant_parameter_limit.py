"""Packet97 high-precision parameter-limit checks and exact manufactured family.
Full proof precedes this code. Independent physical radial integrals test the velocity.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,time,hashlib
import mpmath as mp
mp.mp.dps=65
root=Path('research/97_nonresonant_to_log_limit/verification')
start=time.monotonic()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'precision_decimal_digits':mp.mp.dps,'scope':'Numerical parameter-limit checks, not interval certification or B2 profiles.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'constant_and_tail':[],'physical_inverse':[],'exact_zero_constant_family':[]}

def constants(coeff,b,L):
 alpha=L*L*coeff[2] if len(coeff)>2 else mp.mpf(0)
 cb=-b*L*L/2*sum(a/(j+1-b) for j,a in enumerate(coeff))
 c3=mp.mpf(0)
 for j,a in enumerate(coeff):
  c3+=a*L*L*([mp.mpf(3)/4,mp.mpf(3)/2,mp.mpf(1)/4+mp.log(L)/2][j] if j<3 else -mp.mpf(3)/(2*(j-2)))
 return cb,c3,alpha

def physical_velocity(coeff,b,L,r,theta):
 # Direct integration of the source moments, independent of the moment constants.
 def q(t):
  z=(1+t*t/(L*L))**(-1/(2*b))
  return t*z**(b+1)*sum(a*z**j for j,a in enumerate(coeff))
 cuts=[0,r/4,r/2,r]
 J0=mp.quad(q,cuts)
 J2=mp.quad(lambda t:t*t*q(t),cuts)
 pr=(J2/(r*r)-J0)/2
 dp=(-J2/(r*r)-J0)/2
 cs=mp.cos(theta);sn=mp.sin(theta)
 # Stream = p cos(theta), velocity = (-Psi_y,Psi_x).
 return ((pr-dp)*cs*sn,pr*sn*sn+dp*cs*cs)

def floatlist(v):return [float(a) for a in v]
polys=[('constant',[1]),('resonant',[0,0,1]),('mixed',[1,1,-Q(2,5),Q(7,10),0,-Q(1,5)])]
for label,coef in polys:
 coeff=[mp.mpf(a.numerator)/a.denominator if isinstance(a,Q) else mp.mpf(a) for a in coef]
 for L in [mp.mpf('0.6'),mp.mpf('1'),mp.mpf('1.7')]:
  last_const=None;last_tail=None
  for ds in ['0.1','0.01','0.001','0.000001','0.0000000001']:
   delta=mp.mpf(ds);b=3-delta;eps=delta/b
   cb,c3,alpha=constants(coeff,b,L)
   ren=cb+alpha/(2*eps);target=c3-alpha*(mp.mpf(1)/4+mp.log(L)/2)
   err=abs(ren-target);worst=mp.mpf(0)
   for r in [mp.mpf('.2'),mp.mpf(1),mp.mpf(5),mp.mpf(50),mp.mpf(1000)]:
    for theta in [mp.mpf(0),mp.mpf('.37'),mp.pi/2,mp.mpf('2.1')]:
     cs=mp.cos(theta);sn=mp.sin(theta);fac=alpha*(L/r)**eps/(2-eps)
     combined=(fac*cs*sn,cb+fac/eps-fac*cs*cs)
     limit=(alpha*cs*sn/2,c3-alpha*mp.log(r)/2-alpha*cs*cs/2)
     worst=max(worst,max(abs(a-c) for a,c in zip(combined,limit)))
   row={'polynomial':label,'L':float(L),'delta':ds,'C_b':float(cb),'C3':float(c3),'alpha':float(alpha),'renormalized_constant_error':float(err),'max_tail_vector_error':float(worst)}
   out['constant_and_tail'].append(row)
   if delta<=mp.mpf('.001'):
    if last_tail is not None:assert worst<=last_tail+mp.mpf("1e-40")
    # The pure z² renormalized constant is identically zero; its rounding noise need not decrease.
    last_const=err;last_tail=worst
   if ds=='0.0000000001':assert err<mp.mpf('1e-8') and worst<mp.mpf('1e-7')
  print('tail',label,float(L),float(err),float(worst),flush=True)
 # Full centered inverse at a fixed L is integrated directly, not reconstructed from tails.
 L=mp.mpf('1.3');points=[(mp.mpf('.17'),mp.mpf('.31')),(mp.mpf('1.3'),mp.mpf('-1.2')),(mp.mpf('8.4'),mp.mpf('2.1'))]
 base=[physical_velocity(coeff,mp.mpf(3),L,*p) for p in points]
 for ds in ['0.1','0.001','0.000001']:
  delta=mp.mpf(ds);vals=[physical_velocity(coeff,3-delta,L,*p) for p in points]
  err=max(abs(a-c) for v,w in zip(vals,base) for a,c in zip(v,w))
  out['physical_inverse'].append({'polynomial':label,'L':float(L),'delta':ds,'points_r_theta':[floatlist(p) for p in points],'velocities':[floatlist(v) for v in vals],'beta3_velocities':[floatlist(v) for v in base],'max_error':float(err)})
 print('physical',label,float(err),flush=True)
for b in [Q(5,2),Q(29,10),Q(299,100),Q(2999,1000)]:
 for L in [Q(1),Q(17,10)]:
  d=(3-b)/(b-1)
  cb=b*L*L/(2*(b-1))-d*b*L*L/(2*(3-b))
  alpha=L*L*d;eps=(3-b)/b
  assert cb==0
  out['exact_zero_constant_family'].append({'b':str(b),'L':str(L),'coefficient_d':str(d),'C_b_exact':str(cb),'alpha_b':str(alpha),'alpha_over_2epsilon':str(alpha/(2*eps)),'C3_exact':str(3*L*L/4)})
# Independent radial antiderivative versus direct moment integral at b=3, including logarithm.
# This cross-check addresses the sign and scale used in the preceding physical inverse.
radial=[]
for j in range(6):
 for b in [mp.mpf('2.5'),mp.mpf('2.999'),mp.mpf(3)]:
  L=mp.mpf('1.7');r=mp.mpf('4.3');a=(b+1+j)/(2*b);u=1+r*r/(L*L)
  primitive=L*L/2*(mp.log(u) if a==1 else mp.expm1((1-a)*mp.log(u))/(1-a))
  integral=mp.quad(lambda t:t*(1+t*t/(L*L))**(-a),[0,r/3,r])
  err=abs(primitive-integral)
  assert err<mp.mpf('1e-55')
  radial.append({'j':j,'b':str(b),'error':str(err)})
out['radial_antiderivative_checks']=radial
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'parameter_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
