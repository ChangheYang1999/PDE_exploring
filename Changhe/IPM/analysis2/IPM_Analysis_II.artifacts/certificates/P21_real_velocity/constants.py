"""Exact real angular comparison and original-state radius audit."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,hashlib
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'source_audit'))
import recover_state as rec
rec.HERE=HERE;rec.COPY=Path('case4/IPM_case4.artifacts')
c,coeff,record=rec.read_state(131)
ctx.prec=512
sigma=Q(11,5);d=Q(4,9)
def A(n):return n*(n-2+sigma)/((n-2)*(n-sigma))
def D(n):return 1+sigma/(n+2)
def diag(n):return Q(5,8)+D(1)**2/8 if n==1 else Q(1,4)+(A(n)**2+D(n)**2)/8
def edge(n):return (A(n)+D(n-2))/8
row1=diag(1)+10*edge(3)
row3=diag(3)+edge(3)/10+edge(5)/20
row5=diag(5)+20*edge(5)+edge(7)
assert row1<Q(75,4) and row3<Q(75,4) and row5<14
assert diag(5)<2 and edge(7)<1
assert Q(75,4)<Q(169,9)
assert 4*7**7*100**9 <59**9*9**9
assert Q(59,100)**2*(Q(99,4)**2+Q(132,65)**2)/2<Q(21,2)**2
assert 14000**9<2**124
rational=Q(2,5)-(22+Q(23,2)*186+sigma*282)/14000
assert rational==Q(14093,70000) and rational>Q(1,5)
num=lambda x:arb(Q(x).numerator)/Q(x).denominator
M=num(d/2)*num((2-d)/d)**num(1-d/2)
real=M*((num(Q(99,4))**2+num(Q(132,65))**2)/2).sqrt()
assert real<num(Q(21,2))
C=22+(1+num(Q(21,2)))*186+num(sigma)*(9*22+2*22+56/arb(2).sqrt())
margin=num(Q(2,5))-C/(arb(2)**num(Q(124,9)))
assert margin>num(Q(1,5))
old=BASE/'17_weight_radius/verification/decay_radius.json';od=json.loads(old.read_text())
assert od['canonical_sha256']==record['canonical_serialization_sha256']
assert od['source_json_sha256']==record['source_json_sha256']
target={'C_rho':186,'C_U':22,'C_DU':22,'C_D2U':56}
for k,v in target.items():
 assert arb(od['local_bounds'][k])<v and arb(od['exterior_bounds'][k])<v
files=[HERE.parent/'PROOF.md',old,BASE/'17_weight_radius/verification/decay_radius.py',BASE/'14_homogeneous_weight/REGULARIZED_PROOF.md',BASE/'07_weighted/RADIAL_COMMUTATOR_PROOF.md',BASE/'07_weighted/LOW_INVERSE_PROOF.md',BASE/'17_weight_radius/PROOF.md',BASE/'18_fractional_constants/PROOF.md',BASE/'source_audit/recover_state.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED exact arithmetic; analytic proof required','precision_bits':ctx.prec,'source_sha256':record['source_json_sha256'],'canonical_sha256':record['canonical_serialization_sha256'],'rows':{str(k):str(v) for k,v in [(1,row1),(3,row3),(5,row5)]},'row3_decimal':num(row3).str(60),'real_velocity_bound':'13/3','real_commutator_bound':real.str(60),'commutator_rounded':'21/2','coefficient_tuple':target,'radius':'2^31','low_margin':margin.str(60),'rational_low_margin':str(rational),'low_bilinear_bound':'3640/3','dependencies':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
