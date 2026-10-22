"""Authenticate the two prior row majorants and exact first-row corollary."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/row_one_local';ctx.prec=256;iv.dps=100
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
def ir(q):return iv.mpf(q.numerator)/q.denominator
old=B/'research/tail_local_modes/evidence/verdict.json';v=json.loads(old.read_text());assert v['status']=='CONFIRMED_FINITE_MODE_LOCAL_VELOCITY_AND_ALL_ADMISSIBLE_T_HIGHER_TAIL_SOURCE_DEFECT'
pins=dict(v['files'])
for f,h in pins.items():assert sha(B/f)==h,f
A=json.loads((B/'research/tail_local_modes/evidence/arb.json').read_text());I=json.loads((B/'research/tail_local_modes/evidence/iv.json').read_text());assert A['exact']=={k:x for k,x in I['exact'].items() if k in A['exact']}
k=F(A['exact']['k']);a1=2*k-1;assert k*(a1/k-1)/(1-k)==-1
assert k/(1-k)>0 and I['exact']['T']=='3000' and I['exact']['R']=='9'
ceil=['1.523891e-12','5.139245e-13','1.184002e-13','1.590300e-14'];bounds={};checks=0
for j,c in enumerate(ceil):
 vals=[]
 for tag,res in [('Arb512_finite',A),('iv180_geometric',I)]:
  x=res['values'][f'row1_j{j}'];lo,hi=F(x['lower_exact']),F(x['upper_exact']);assert 0<lo<=hi<F(c)
  assert ar(F(c)-hi).lower()>0 and ir(F(c)-hi).a>0;checks+=1
  vals.append({'method':tag,'lower_exact':str(lo),'upper_exact':str(hi),'ceiling_minus_upper_exact':str(F(c)-hi)})
 assert F(vals[0]['upper_exact'])<F(vals[1]['lower_exact']);bounds[str(j)]=vals
Rb=I['values']['R_b'];L=I['values']['L'];assert F(Rb['lower_exact'])>F('3412.96685816')>3000 and F(L['upper_exact'])<F(Rb['lower_exact']) and F(L['lower_exact'])>1
margin=F('6.70197e-7')-F('30.0230')*F(ceil[0]);assert margin>F('6.7015e-7')>F('6.70e-7') and F(ceil[1])<F(ceil[0])
ma=ar(F('6.70197e-7'))-ar(F('30.0230'))*ar(F(ceil[0]));mi=ir(F('6.70197e-7'))-ir(F('30.0230'))*ir(F(ceil[0]));assert ma.lower()>ar(F('6.7015e-7')).upper() and mi.a>ir(F('6.7015e-7')).b
pf=D/'evidence/proof_first.json';assert json.loads(pf.read_text())['sha256']==sha(D/'PROOF.md')
for p in [old,D/'PROOF.md',pf,Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FIRST_ROW_COROLLARY_REQUIRES_REVIEW','prior_pins':len(v['files']),'strict_row_ceiling_checks':checks,'strict_component_C3_ceilings':ceil,'bounds':bounds,'exact_defect_lower_margin':str(margin),'arb_defect_margin':str(ma),'iv_defect_margin':str(mi),'strict_source_derivative_lower':'6.7015e-7','pins':pins,'scope':'Exact identity of105 and first compensated row of106; reused two audited114 majorants, new exact scalar corollary. No surrounding exclusion or endpoint.'}
(D/'evidence/audit.json').write_text(json.dumps(o,indent=2)+'\n');print(o['utc'],o['status'],o['prior_pins'],str(margin))
