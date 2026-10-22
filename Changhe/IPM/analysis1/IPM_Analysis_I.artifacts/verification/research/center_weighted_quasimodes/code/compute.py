"""Exact polynomial-dictionary identities, dyadic input, Arb enclosures."""
import sys,os,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
ctx.prec=512;sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/center_weighted_quasimodes';E=D/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def clean(a):return {n:F(q) for n,q in a.items() if q}
def add(a,b):
 d=dict(a)
 for n,q in b.items():d[n]=d.get(n,F(0))+q
 return clean(d)
def neg(a):return {n:-q for n,q in a.items()}
def mul(a,b):
 d={}
 for n,q in a.items():
  for m,r in b.items():d[n+m]=d.get(n+m,F(0))+q*r
 return clean(d)
def scale(a,q):return clean({n:q*v for n,v in a.items()})
def sub(a,b):return add(a,neg(b))
def pair(x):
 def f(z):
  m,e=z.man_exp();return F(int(m))*F(2)**int(e)
 assert x.is_finite();return {'lower_exact':str(f(x.lower())),'upper_exact':str(f(x.upper()))}
def aq(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))

def run():
 inp=load(E/'inputs.json');assert sha(ROOT/'data_exact/modal_v2.json')==inp['input_sha256']
 raw=load(ROOT/'data_exact/modal_v2.json');assert inp['scalars_hex']=={k:raw['scalars_hex'][k] for k in ['k','L']}
 k=F(float.fromhex(raw['scalars_hex']['k']));L=F(float.fromhex(raw['scalars_hex']['L']));assert 0<k<F(1,2) and L>0
 ell=1/k;alpha=1-2*ell;beta=4*ell-1;den=6*ell-2;p=(8*ell-3)/den;q=(4*ell-1)/den
 assert ell>2 and p+q==2 and alpha*p+beta*q==1 and 1<p<F(3,2) and F(1,2)<q<1
 assert 2*alpha+(beta-alpha)*q==1 and 2*beta-(beta-alpha)*p==1
 vals={'k':k,'L':L,'ell':ell,'c':3*ell-1,'alpha':alpha,'beta':beta,'p':p,'q':q,'axis_H1_squared_error_exponent_p':2*p-1,'axis_H1_squared_error_exponent_q':2*q-1}
 X={1:F(1)};one={0:F(1)};pn=sub(scale(X,8),scale(one,3));qn=sub(scale(X,4),one);dn=sub(scale(X,6),scale(one,2));aa=sub(one,scale(X,2));bb=sub(scale(X,4),one)
 identities={
  'p_plus_q_2':sub(add(pn,qn),scale(dn,2)),
  'alpha_p_beta_q_1':sub(add(mul(aa,pn),mul(bb,qn)),dn),
  'angular_cos2_coefficient':sub(add(scale(mul(aa,dn),2),mul(sub(bb,aa),qn)),dn),
  'angular_sin2_coefficient':sub(sub(scale(mul(bb,dn),2),mul(sub(bb,aa),pn)),dn),
  'p_minus_1':sub(sub(pn,dn),sub(scale(X,2),one)),
  'three_halves_minus_p':sub(sub(scale(dn,F(3,2)),pn),X),
  'q_minus_half':sub(sub(qn,scale(dn,F(1,2))),X),
  'one_minus_q':sub(sub(dn,qn),sub(scale(X,2),one))}
 assert all(v=={} for v in identities.values())
 # Independently stated powers include planar measure r dr.
 powers={'critical_center_degree2':2*F(2)-6+1,'center_error_degree3':2*F(3)-6+1,'far_nonlocal_product':2*(k-3)-(2*k+3)+1,'far_density':2*k-(2*k+3)+1,'Hfivehalves_squared_scaling':2*(2+F(2,2)-F(5,2)),'Fourier_C1_integrability_at_infinity':(2-1)+2-2*F(5,2)}
 assert list(powers.values())==list(map(F,[-1,1,-8,-2,1,-2]))
 strain={'F1_coefficient_after_parts':(F(1)-1)/4,'F3_coefficient_after_parts':(F(1)+3)/4,'radial_bump_factor':F(1,4)};assert strain['F1_coefficient_after_parts']==0 and strain['F3_coefficient_after_parts']==1
 enclosures={n:pair(aq(v)) for n,v in vals.items()};geo=pair(1/(1-1/arb(2).sqrt()));enclosures['dyadic_Hfivehalves_triangle_sum']=geo
 pins={}
 for n,h in inp['parents'].items():
  assert sha(ROOT/n)==h;pins[n]=h;v=load(ROOT/n)
  if n.endswith('modal_graph_scaling/evidence/verdict.json'):
   assert v['status']=='CONFIRMED_ACTUAL_MODAL_GRAPH_SCALING_AND_NONZERO_IMAGE';children=v['files']
  else:assert v['verdict']=='CONFIRMED';children=v['source_and_evidence_sha256']
  for pth,h2 in children.items():assert sha(ROOT/pth)==h2 and (pth not in pins or pins[pth]==h2);pins[pth]=h2
 return {'values_exact':{n:str(v) for n,v in vals.items()},'formal_polynomial_identities':{n:'0' for n in identities},'radial_and_fourier_powers_exact':{n:str(v) for n,v in powers.items()},'strain_integration_coefficients_exact':{n:str(v) for n,v in strain.items()},'arb512':enclosures,'parent_files':dict(sorted(pins.items()))}
if __name__=='__main__':
 start=datetime.now(timezone.utc).isoformat();out=run();out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CENTER_QUASIMODE_EXACT_ALGEBRA_AND_ARB_INPUT_CHECKS_REQUIRES_SECOND_PATH_AND_REVIEW','source_sha256':sha(Path(__file__)),'inputs_sha256':sha(E/'inputs.json'),**out}
 with (E/'compute.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ['utc','status','values_exact','radial_and_fourier_powers_exact']}))
