"""Exact multivariate coefficient dictionaries and Arb; analytic claims stay in PROOF.md."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,fmpq,ctx
sys.dont_write_bytecode=True;ctx.prec=512
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/higher_center_weight_quasimodes';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def trim(p):return {t:Q(v) for t,v in p.items() if v}
def c(v):return trim({(0,0,0,0):Q(v)})
def var(i):t=[0]*4;t[i]=1;return {tuple(t):Q(1)}
def add(a,b):
 r=dict(a)
 for t,v in b.items():r[t]=r.get(t,Q(0))+v
 return trim(r)
def scale(a,v):return trim({t:v*z for t,z in a.items()})
def neg(a):return scale(a,-1)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 r={}
 for t,u in a.items():
  for s,v in b.items():
   z=tuple(ti+si for ti,si in zip(t,s));r[z]=r.get(z,Q(0))+u*v
 return trim(r)
def constant(p):assert not p or set(p)=={(0,0,0,0)};return str(p.get((0,0,0,0),Q(0)))
def projection(shift):
 # Imaginary-unit coefficients of sin((n+shift)theta), sin(theta), and real cosines.
 sinl={(1,shift):Q(-1,2),(-1,-shift):Q(1,2)};cost={(0,1):Q(1,2),(0,-1):Q(1,2)}
 sint={(0,1):Q(-1,2),(0,-1):Q(1,2)};cosl={(1,shift):Q(1,2),(-1,-shift):Q(1,2)}
 def product(a,b):
  out={}
  for x,u in a.items():
   for y,v in b.items():
    z=(x[0]+y[0],x[1]+y[1]);out[z]=out.get(z,Q(0))+u*v
  return out
 A=product(cost,sinl);B=product(sint,cosl)
 assert A[(1,0)]==Q(-1,4) and A[(-1,0)]==Q(1,4)
 expected=Q(-1,4) if shift==-1 else Q(1,4)
 assert B[(1,0)]==expected and B[(-1,0)]==-expected
 return {'derivative_source_coefficient':str(A[(1,0)]/Q(-1,2)),'density_source_coefficient_divided_by_n_plus_shift':str(-B[(1,0)]/Q(-1,2))}
def pair(a):
 def f(v):m,e=v.man_exp();return Q(int(m))*Q(2)**int(e)
 assert a.is_finite();return {'lower_exact':str(f(a.lower())),'upper_exact':str(f(a.upper()))}
def run():
 inp=load(E/'inputs.json');raw=load(ROOT/'data_exact/modal_v2.json');assert sha(ROOT/'data_exact/modal_v2.json')==inp['modal_input_sha256']
 k=Q(float.fromhex(raw['scalars_hex']['k']));L=Q(float.fromhex(raw['scalars_hex']['L']));assert 0<k<Q(1,2) and L>0
 ell=1/k;aa=1-2*ell;bb=4*ell-1;dd=bb-aa
 vals={'k':k,'L':L,'ell':ell,'alpha':aa,'beta':bb,'d':dd,'p2':(2*bb-1)/dd,'q2':(1-2*aa)/dd,'p_increment_per_m':bb/dd,'q_increment_per_m':-aa/dd}
 assert vals['p2']>1 and vals['q2']>Q(1,2) and vals['p_increment_per_m']>0 and vals['q_increment_per_m']>0
 ellp,m,n,kp=[var(i) for i in range(4)];one=c(1);a=sub(one,scale(ellp,2));b=sub(scale(ellp,4),one);d=sub(b,a);pn=sub(mul(b,m),one);qn=sub(one,mul(a,m))
 identities={
 'p_plus_q_m':sub(add(pn,qn),mul(m,d)),
 'alpha_p_beta_q_one':sub(add(mul(a,pn),mul(b,qn)),d),
 'angular_cos_squared_coefficient':sub(add(mul(m,a),qn),one),
 'angular_sin_squared_coefficient':sub(sub(mul(m,b),pn),one),
 'p_increment_from_m2':sub(sub(pn,sub(scale(b,2),one)),mul(sub(m,c(2)),b)),
 'q_increment_from_m2':sub(sub(qn,sub(one,scale(a,2))),mul(sub(m,c(2)),neg(a))),
 'green_lower_mode_cancellation':sub(sub(n,one),sub(n,one)),
 'green_upper_mode_numerator':sub(add(sub(n,one),add(n,one)),scale(n,2)),
 'far_weight_exponent':sub(add(neg(add(scale(m,2),c(2))),scale(sub(sub(m,kp),c(Q(1,2))),2)),sub(neg(scale(kp,2)),c(3))),
 'center_background_square_exponent':sub(add(sub(c(6),add(scale(m,2),c(2))),one),sub(c(5),scale(m,2)))}
 assert all(not p for p in identities.values())
 s=add(m,c(Q(1,2)))
 powers={
 'critical_center_radial':add(sub(scale(m,2),add(scale(m,2),c(2))),one),
 'corrected_center_error_radial':add(sub(scale(add(m,one),2),add(scale(m,2),c(2))),one),
 'far_nonlocal_radial':add(add(scale(sub(kp,c(3)),2),sub(neg(scale(kp,2)),c(3))),one),
 'Sobolev_scaled_square':sub(add(scale(m,2),c(2)),scale(s,2)),
 'Fourier_C_m_minus_1_radial':add(sub(scale(sub(m,one),2),scale(s,2)),one)}
 powers={key:constant(v) for key,v in powers.items()};assert list(map(Q,powers.values()))==list(map(Q,[-1,1,-8,1,-2]))
 proj={str(j):projection(j) for j in [-1,1]};assert proj=={'-1':{'derivative_source_coefficient':'1/2','density_source_coefficient_divided_by_n_plus_shift':'-1/2'},'1':{'derivative_source_coefficient':'1/2','density_source_coefficient_divided_by_n_plus_shift':'1/2'}}
 pins={}
 for path,want in inp['parents'].items():
  v=load(ROOT/path);assert sha(ROOT/path)==want['sha256'] and v['status']==want['status'];pins[path]=want['sha256']
  for name,h in v['files'].items():assert sha(ROOT/name)==h and (name not in pins or pins[name]==h);pins[name]=h
 enclosures={n:pair(arb(fmpq(v.numerator,v.denominator))) for n,v in vals.items()}
 return {'values_exact':{n:str(v) for n,v in vals.items()},'formal_polynomial_identities':{n:'0' for n in identities},'formal_radial_Fourier_powers':powers,'formal_frequency_projection':proj,'arb512':enclosures,'parent_files':dict(sorted(pins.items())),'scope':'Finite algebra and accepted-background inputs only. Positive Gram invertibility, Taylor cancellation and all norm claims are analytic proofs, not finite tests.'}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();r=run();out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_HIGHER_CENTER_EXACT_ALGEBRA_AND_ARB_INPUTS_REQUIRES_SECOND_PATH_AND_REVIEW','source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),**r}
 with (E/'compute.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
 print({k:out[k] for k in ['utc','status','formal_polynomial_identities','formal_radial_Fourier_powers','formal_frequency_projection']})
