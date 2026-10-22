"""Exact output audit; no new convolution or residual norm ceiling.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_repair';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
o=load(E/'inputs.json');assert o['status']=='PASS_TWO_EXACT_INPUT_EXPONENT_AND_ANGULAR_IDENTITY_AUDITS';files={}
for f,h in o['files'].items():assert sha(B/f)==h,f;files[f]=h
plan=load(D/'source/plan.json');assert sha(Path(plan['source_archive']))==plan['source_archive_sha256']
A=o['outputs']['exact_json'];N=o['outputs']['exact_npz'];assert A['exact']==N['exact']
assert A['counts']=={'distinct_exponent_pairs':55,'normalization_zero_join_jets':7,'ordered_product_checks':242,'mode_denominator_and_outer_integrability_checks':6003,'Laurent_force_basis_checks':1827,'angular_primitive_multiplier_checks':1566,'factor_polynomial_identities':2}
assert N['counts']=={'distinct_exponent_pairs':55,'surviving_ordered_products':100,'factored_mode_denominators':4437,'original_Aout_entries':2600,'original_knots_entries':1573}
x=A['exact'];k=F(x['k']);bo=F(x['bo']);powers=[F(v) for v in x['all_original_exponents']]
# Independent integer coefficients of k for the ten pure density powers.
coeff=[(1,0),(2,-1),(3,-2),(4,-3),(5,-4),(6,-5),(1,-2),(2,-3),(3,-4),(1,-4)]
ex=[a*k+b for a,b in coeff]+[3-bo];assert ex==powers
assert len(set(ex))==11 and 4*k<1 and k>0 and bo>120
for key,(a,b) in {'a1':(2,-1),'a2':(3,-2),'d':(1,-2),'a3':(4,-3)}.items():assert F(x[key])==a*k+b
assert x['norm_decay_exponents']==[str(k-1),str(2*k-2),'-2']
endpoints=0
for key,(lo,hi) in o['strict_public_exponent_intervals'].items():assert F(lo)<F(x[key])<F(hi);endpoints+=2
remaining=ex[:6]+ex[7:];table=[]
for i,v in enumerate(remaining):
 for j,w in enumerate(remaining):
  a=v+w-1
  if i==j==0:role='canceled_first';assert a==2*k-1
  elif i+j==1 and min(i,j)==0:role='canceled_second';assert a==3*k-2
  else:role='remainder';assert a<=4*k-3
  assert a!=k-2;table.append((i,j,str(a),role))
assert N['product_table_sha256']==hashlib.sha256(json.dumps(table,sort_keys=True).encode()).hexdigest()
assert N['product_witnesses']==[list(table[i]) for i in (0,1,2,10,11,12,98,99)]
# Independent exact check of every possibly resonant exponent against integers.
resonance=0
for a,limit in [(v,261) for v in ex]+[(2*k-1,522),(3*k-2,783),(k-2,261)]:
 b=a+1
 for n in range(1,limit+1):assert b!=2*n and b!=-2*n;resonance+=1
assert resonance==4437
# Reconstruct the exact Beta moments by integrating the expanded polynomial.
bpoly={}
for i in range(9):
 for j in range(9):
  c=math.comb(8,i)*(-1)**(8-i)*math.comb(8,j)*2**(8-j)*(-1)**j
  bpoly[i+j]=bpoly.get(i+j,0)+c
moment=[sum(F(c)*(F(2)**(n+m+1)-1)/(n+m+1) for n,c in bpoly.items()) for m in (0,1)]
assert moment==[F(math.factorial(8)**2,math.factorial(17)),F(3,2)*F(math.factorial(8)**2,math.factorial(17))]
transition=load(B/'research/normalized_tail_repair/source/transition.json')
# Parse the pinned schema explicitly, avoiding an unchecked optional comparison.
raw=transition['coefficients_low_to_high']
assert [F(c) for c in raw]==[F(bpoly.get(i,0)) for i in range(17)]
# Re-execution reproduces the entire Laurent signature and saved input result.
import audit_from_json as J,audit_from_npz as P
j=J.evaluate();p=P.evaluate();p.pop('outer_exact');p.pop('knots_exact');tab=p.pop('product_table')
p['product_table_sha256']=hashlib.sha256(json.dumps(tab,sort_keys=True).encode()).hexdigest();p['product_witnesses']=[list(tab[i]) for i in (0,1,2,10,11,12,98,99)]
assert j==A and p==N
for f in [E/'inputs.json',D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json']+list((D/'code').glob('*.py'))+list((D/'source').glob('*.json')):files[str(f.relative_to(B))]=sha(f)
pf=load(E/'proof_first.json');assert pf['sha256']==sha(D/'PROOF.md')
assert datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(o['utc'])
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_OUTPUT_REPLAY_EXPONENTS_RESONANCES_AND_BETA_MOMENTS','counts':{'original_Aout_entries':2600,'original_knots_entries':1573,'strict_public_endpoints':endpoints,'distinct_pairs_per_input_method':55,'independent_nonresonance_checks':resonance,'surviving_product_rows':100,'exact_beta_moments':2,'exact_transition_coefficients':17,'complete_input_replays':2},'beta_moments_exact':[str(v) for v in moment],'source_archive':{'path':plan['source_archive'],'sha256':plan['source_archive_sha256']},'files':dict(sorted(files.items())),'scope':'Exact finite data and symbolic input conditions. Analytic bounds are proved in PROOF plus mandatory ADDENDUM. No unevaluated angular norm or residual ceiling is certified.'}
(E/'audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':out['counts']}))
