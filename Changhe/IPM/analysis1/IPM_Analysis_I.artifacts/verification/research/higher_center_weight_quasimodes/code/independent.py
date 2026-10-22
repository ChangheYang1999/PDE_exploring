"""Sympy identities, addition formulas, literal hex integers, and mpmath interval checks."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,sys
import sympy as S
from mpmath import iv
sys.dont_write_bytecode=True;iv.dps=220
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/higher_center_weight_quasimodes';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def literal(s):
 z=re.fullmatch(r'(-?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?\d+)',s);assert z
 sign,whole,frac,exp=z.groups();n=int(whole+frac,16)*(-1 if sign else 1);e=int(exp)-4*len(frac)
 return Q(n)*Q(2)**e
def pair(a):
 def f(z):sign,m,e,bc=z;assert bc>=0;return Q((-1 if sign else 1)*m)*Q(2)**e
 return {'lower_exact':str(f(a._mpi_[0])),'upper_exact':str(f(a._mpi_[1]))}
def iq(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def zero(v):assert S.expand(v)==0;return '0'
def run():
 x=load(E/'inputs.json');a=load(E/'compute.json');raw=load(ROOT/'data_exact/modal_v2.json');assert sha(ROOT/'data_exact/modal_v2.json')==x['modal_input_sha256']
 k0=literal(raw['scalars_hex']['k']);L=literal(raw['scalars_hex']['L']);assert 0<k0<Q(1,2) and L>0
 ell0=1/k0;aa=1-2*ell0;bb=4*ell0-1;dd=6*ell0-2
 vals={'k':k0,'L':L,'ell':ell0,'alpha':aa,'beta':bb,'d':dd,'p2':(8*ell0-3)/dd,'q2':(4*ell0-1)/dd,'p_increment_per_m':(4*ell0-1)/dd,'q_increment_per_m':(2*ell0-1)/dd}
 assert vals['p2']>1 and vals['q2']>Q(1,2) and vals['p_increment_per_m']>0 and vals['q_increment_per_m']>0
 ell,m,n,k=S.symbols('ell m n k');alpha=1-2*ell;beta=4*ell-1;d=6*ell-2;pn=beta*m-1;qn=1-alpha*m
 ids={'p_plus_q_m':zero(pn+qn-m*d),'alpha_p_beta_q_one':zero(alpha*pn+beta*qn-d),'angular_cos_squared_coefficient':zero(m*alpha+qn-1),'angular_sin_squared_coefficient':zero(m*beta-pn-1),'p_increment_from_m2':zero(pn-(8*ell-3)-(m-2)*(4*ell-1)),'q_increment_from_m2':zero(qn-(4*ell-1)-(m-2)*(2*ell-1)),'green_lower_mode_cancellation':zero(-(1-n)-(n-1)),'green_upper_mode_numerator':zero(-(1-n)+(n+1)-2*n),'far_weight_exponent':zero(-2*m-2+2*(m-k-S.Rational(1,2))+2*k+3),'center_background_square_exponent':zero(6-2*m-2+1-(5-2*m))}
 s=m+S.Rational(1,2)
 exprs={'critical_center_radial':2*m-2*m-2+1,'corrected_center_error_radial':2*m+2-2*m-2+1,'far_nonlocal_radial':2*k-6-2*k-3+1,'Sobolev_scaled_square':2*m+2-2*s,'Fourier_C_m_minus_1_radial':2*m-2-2*s+1}
 powers={name:str(S.expand(v)) for name,v in exprs.items()}
 t=S.symbols('theta',real=True)
 trig=[S.cos(t)*S.sin((n-1)*t)-(S.sin(n*t)+S.sin((n-2)*t))/2,S.sin(t)*S.cos((n-1)*t)-(S.sin(n*t)-S.sin((n-2)*t))/2,S.cos(t)*S.sin((n+1)*t)-(S.sin((n+2)*t)+S.sin(n*t))/2,S.sin(t)*S.cos((n+1)*t)-(S.sin((n+2)*t)-S.sin(n*t))/2]
 for expr in trig:assert S.trigsimp(S.expand_trig(expr))==0
 proj={'-1':{'derivative_source_coefficient':'1/2','density_source_coefficient_divided_by_n_plus_shift':'-1/2'},'1':{'derivative_source_coefficient':'1/2','density_source_coefficient_divided_by_n_plus_shift':'1/2'}}
 assert a['source_sha256']==sha(D/'code/compute.py') and a['inputs_sha256']==sha(E/'inputs.json')
 assert a['values_exact']=={n:str(v) for n,v in vals.items()} and a['formal_polynomial_identities']==ids and a['formal_radial_Fourier_powers']==powers and a['formal_frequency_projection']==proj
 enclosures={name:pair(iq(q)) for name,q in vals.items()}
 for name,q in vals.items():
  A=a['arb512'][name];B=enclosures[name]
  assert Q(A['lower_exact'])<=q<=Q(A['upper_exact']) and Q(B['lower_exact'])<=q<=Q(B['upper_exact'])
  assert max(Q(A['lower_exact']),Q(B['lower_exact']))<=min(Q(A['upper_exact']),Q(B['upper_exact']))
 pins={}
 for path,want in x['parents'].items():
  v=load(ROOT/path);assert sha(ROOT/path)==want['sha256'] and v['status']==want['status'];pins[path]=want['sha256']
  for name,h in v['files'].items():assert sha(ROOT/name)==h and (name not in pins or pins[name]==h);pins[name]=h
 assert dict(sorted(pins.items()))==a['parent_files']
 # Additional exact identity refutes an overstatement in the theorem review: the cubic rank term cancels affine velocity.
 xx,yy,sigma=S.symbols('x y sigma');rho3=xx**2*yy
 cancel=S.expand(-sigma*xx*S.diff(rho3,xx)+sigma*yy*S.diff(rho3,yy)+sigma*(xx*S.diff(rho3,xx)+yy*S.diff(rho3,yy))/3);assert cancel==0
 return {'values_exact':{n:str(v) for n,v in vals.items()},'formal_polynomial_identities':ids,'formal_radial_Fourier_powers':powers,'formal_frequency_projection':proj,'full_angle_addition_identities':4,'iv220':enclosures,'rational_scalar_containment_checks':20,'interval_pair_checks':10,'parent_pin_count':len(pins),'compute_sha256':sha(E/'compute.json'),'additional_cubic_affine_plus_rank_identity':str(cancel),'scope':'Independent algebra and input audit only. No finite test of Gram invertibility, an operator spectrum or any infinite sequence.'}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();r=run();out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_HIGHER_CENTER_ALGEBRA_TRIG_IV_AND_PARENT_PINS_REQUIRES_REVIEW','source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),**r}
 with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
 print({k:out[k] for k in ['utc','status','full_angle_addition_identities','rational_scalar_containment_checks','interval_pair_checks','parent_pin_count','additional_cubic_affine_plus_rank_identity']})
