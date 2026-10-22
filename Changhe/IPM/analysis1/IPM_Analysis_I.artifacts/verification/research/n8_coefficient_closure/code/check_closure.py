"""Exact rational and two directed-engine source coefficient closure."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_coefficient_closure';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
files={};counts={'frozen_dependency_pins':0,'exact_scalar_identities':0,'engine_strict_inequalities':0}
def pin(p):
 p=B/p;files[str(p.relative_to(B))]=sha(p);return p
expected={'n8_density_hessian':'c590ba0d354b26595bd1131f68ca87bbc9875c9d248b4cf5fdf71344ef6e01ca','n8_velocity_hessian':'8a35f9cb43b241bd7a880b03aa8fcfdc01806a2517f50dbea99530e03a2455d5'}
verdicts={}
for name,h in expected.items():
 p=pin('research/'+name+'/evidence/verdict.json');assert sha(p)==h
 v=json.loads(p.read_text());verdicts[name]=v
 for f,h0 in v['files'].items():assert sha(B/f)==h0,f;counts['frozen_dependency_pins']+=1
 assert F(v['disc_radius_exact'])==F(99,2000)
 assert v['counts']['cells']==13 and v['counts']['angular_radial_boxes']==8320
v=json.loads(pin('research/n8_velocity_hessian/evidence/moment_inputs.json').read_text())
r=json.loads(pin('research/n8_density_hessian/evidence/density_inputs.json').read_text())
for key in ['source_header','source_center_bracket_exact','delta_exact','theta_max_exact','ntheta','radial_subdivisions','cells']:assert v[key]==r[key],key
assert r['source_center_bracket_exact']==['4841405518533377/562949953421312','4841405518533711/562949953421312']
assert F(r['delta_exact'])==F(33,2000)
M=F(verdicts['n8_velocity_hessian']['bound_exact']);H=F(verdicts['n8_density_hessian']['bound_exact']);delta=F(33,2000);kappa=F(1687,500)
C=F(417,10)*M+3*H;Emax=delta*C;gap=kappa-Emax;K=1/gap
assert M==F(743,2500) and H==F(5059,10000)
assert (C,Emax,gap,K)==(F(695547,50000),F(22953051,100000000),F(314446949,100000000),F(100000000,314446949));counts['exact_scalar_identities']+=4
assert 0<Emax<kappa/2 and C<F(3374,33) and K<F(3181,10000)
assert 100000000*10000 < 3181*314446949

def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
engine={}
for name,convert in [('arb512',aa),('iv180',ii)]:
 # Different arithmetic grouping; neither starts from the exact final fraction.
 if name=='arb512':cc=convert(F(417,10))*convert(M)+3*convert(H);ee=convert(delta)*cc
 else:ee=(convert(417)*convert(M)+convert(30)*convert(H))*convert(F(33,20000));cc=ee/convert(delta)
 gg=convert(kappa)-ee;kk=1/gg
 assert ee<convert(kappa/2) and cc<convert(F(3374,33)) and gg>0 and kk<convert(F(3181,10000));counts['engine_strict_inequalities']+=4
 if name=='arb512':assert cc.contains(aa(C)) and ee.contains(aa(Emax)) and gg.contains(aa(gap)) and kk.contains(aa(K))
 else:
  for x,q in [(cc,C),(ee,Emax),(gg,gap),(kk,K)]:assert x.a<=convert(q).b and x.b>=convert(q).a
 engine[name]={'C':str(cc),'E':str(ee),'gap':str(gg),'K':str(kk)}
for p in [D/'PROOF.md',E/'proof_first.json',Path(__file__)]:files[str(p.relative_to(B))]=sha(p)
assert json.loads((E/'proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md')
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_SOURCE_COEFFICIENT_CLOSURE','exact':{'M_V_upper':str(M),'M_rho_upper':str(H),'delta':str(delta),'C_V_upper':str(C),'E_upper':str(Emax),'kappa':str(kappa),'kappa_minus_E_lower':str(gap),'K_1_upper':str(K),'K_1_decimal_ceiling':'3181/10000'},'counts':counts,'engines':engine,'scope':'The coefficient smallness condition only, for the normalized modal_v2 trial and exact source bracket; all other local hypotheses remain explicit. No tighter N8v2 producer bound is used.','files':dict(sorted(files.items()))}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
