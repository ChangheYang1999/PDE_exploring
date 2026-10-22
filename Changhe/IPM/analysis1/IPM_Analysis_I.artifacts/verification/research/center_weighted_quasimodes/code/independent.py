"""Literal significands, fmpq polynomials, exact Fourier symbols, iv enclosures."""
import sys,json,hashlib,re
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import fmpq as Q,fmpq_poly as P
from mpmath import iv
iv.dps=220;sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/center_weighted_quasimodes';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def literal(s):
 m=re.fullmatch(r'(-?)0x([0-9a-f]+)\.([0-9a-f]+)p([+-]?[0-9]+)',s);assert m
 sign,integer,fraction,exp=m.groups();n=int(integer+fraction,16)*(-1 if sign else 1);e=int(exp)-4*len(fraction)
 return Q(n*(1<<e)) if e>=0 else Q(n,1<<(-e))
def iq(q):q=F(str(q));return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def pair(x):
 def f(v):
  s,m,e,bc=v;assert bc>=0;return F((-1 if s else 1)*m)*F(2)**e
 return {'lower_exact':str(f(x._mpi_[0])),'upper_exact':str(f(x._mpi_[1]))}
def zero(p):assert not p;return '0'

def run():
 inp=load(E/'inputs.json');raw=load(ROOT/'data_exact/modal_v2.json');assert sha(ROOT/'data_exact/modal_v2.json')==inp['input_sha256']
 vals={k:literal(raw['scalars_hex'][k]) for k in ['k','L']};k=vals['k'];assert 0<k<Q(1,2) and vals['L']>0
 ell=1/k;aa=1-2*ell;bb=4*ell-1;d=6*ell-2;pp=(8*ell-3)/d;qq=(4*ell-1)/d
 vals.update(ell=ell,c=3*ell-1,alpha=aa,beta=bb,p=pp,q=qq,axis_H1_squared_error_exponent_p=2*pp-1,axis_H1_squared_error_exponent_q=2*qq-1)
 assert pp+qq==2 and aa*pp+bb*qq==1 and 1<pp<Q(3,2) and Q(1,2)<qq<1
 t=P([0,1]);pn=8*t-3;qn=4*t-1;dn=6*t-2;a=1-2*t;b=4*t-1
 identities={'p_plus_q_2':zero(pn+qn-2*dn),'alpha_p_beta_q_1':zero(a*pn+b*qn-dn),'angular_cos2_coefficient':zero(2*a*dn+(b-a)*qn-dn),'angular_sin2_coefficient':zero(2*b*dn-(b-a)*pn-dn),'p_minus_1':zero(pn-dn-(2*t-1)),'three_halves_minus_p':zero(Q(3,2)*dn-pn-t),'q_minus_half':zero(qn-dn/2-t),'one_minus_q':zero(dn-qn-(2*t-1))}
 # Symbol numerator equalities on an independent rational grid, supplemented by full symbolic coefficient identities.
 # Let z=xi_x/xi_y. Then M1=z/(z^2+1), M2=-z^2/(z^2+1).
 z=P([0,1]);n1=z;n2=-z*z;den=z*z+1
 symbol={'divergence_numerator':zero(z*n1+n2),'curl_plus_dx_numerator':zero(z*n2-n1+z*den),'squared_symbol_norm_relation':zero(n1*n1+n2*n2-z*z*den)}
 for xx,yy in [(1,0),(0,1),(-3,7),(17,-5),(2,2)]:
  x=Q(xx);y=Q(yy);r2=x*x+y*y;m1=x*y/r2;m2=-x*x/r2
  assert x*m1+y*m2==0 and x*m2-y*m1==-x and m1*m1+m2*m2==x*x/r2<=1
 powers={'critical_center_degree2':Q(4-6+1),'center_error_degree3':Q(6-6+1),'far_nonlocal_product':2*k-6-2*k-3+1,'far_density':2*k-2*k-3+1,'Hfivehalves_squared_scaling':Q(6-5),'Fourier_C1_integrability_at_infinity':Q(1+2-5)}
 enclosures={n:pair(iq(v)) for n,v in vals.items()};enclosures['dyadic_Hfivehalves_triangle_sum']=pair(1/(1-iv.exp(-iv.ln(2)/2)))
 old=load(E/'compute.json');assert old['status']=='PASS_CENTER_QUASIMODE_EXACT_ALGEBRA_AND_ARB_INPUT_CHECKS_REQUIRES_SECOND_PATH_AND_REVIEW' and old['source_sha256']==sha(D/'code/compute.py') and old['inputs_sha256']==sha(E/'inputs.json')
 assert old['values_exact']=={n:str(v) for n,v in vals.items()} and old['formal_polynomial_identities']==identities and old['radial_and_fourier_powers_exact']=={n:str(v) for n,v in powers.items()}
 assert old['strain_integration_coefficients_exact']=={'F1_coefficient_after_parts':'0','F3_coefficient_after_parts':'1','radial_bump_factor':'1/4'}
 for name in vals:
  exact=F(str(vals[name]));A=old['arb512'][name];B=enclosures[name]
  assert F(A['lower_exact'])<=exact<=F(A['upper_exact']) and F(B['lower_exact'])<=exact<=F(B['upper_exact'])
 for name in enclosures:
  A=old['arb512'][name];B=enclosures[name];assert max(F(A['lower_exact']),F(B['lower_exact']))<=min(F(A['upper_exact']),F(B['upper_exact']))
 for n,h in old['parent_files'].items():assert sha(ROOT/n)==h
 return {'values_exact':{n:str(v) for n,v in vals.items()},'formal_polynomial_identities':identities,'exact_fourier_symbol_identities':symbol,'exact_fourier_grid_checks':5,'radial_and_fourier_powers_exact':{n:str(v) for n,v in powers.items()},'iv220':enclosures,'scalar_pair_count':len(enclosures),'rational_scalar_containment_checks':2*len(vals),'parent_pin_count':len(old['parent_files']),'compute_sha256':sha(E/'compute.json')}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();out=run();out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_CENTER_QUASIMODE_ALGEBRA_SYMBOL_AND_IV_CHECKS_REQUIRES_ACTUAL_REVIEW','source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),**out}
 with (E/'independent.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ['utc','status','scalar_pair_count','rational_scalar_containment_checks','parent_pin_count']}))
