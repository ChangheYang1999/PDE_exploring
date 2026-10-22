"""Finalize only the scoped modal-scalar claim, keeping original evidence immutable."""
import json, hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from flint import arb, ctx
BASE=Path(__file__).resolve().parents[3]
ctx.prec=384
E=BASE/'research/modal_repair/evidence'
a=json.loads((E/'scalar_result.json').read_text())
b=json.loads((E/'independent_gauss_iv.json').read_text())
def sha(p):return hashlib.sha256((BASE/p).read_bytes()).hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def dyad(v):
 m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def first(v):
 v=arb(v['lower']).union(arb(v['upper']));return dyad(v.lower()),dyad(v.upper())
def second(v):return F(v['lower_exact_dyadic']),F(v['upper_exact_dyadic'])
checks={
 'data_exact/modal_v2.json':a['input_json_sha256'],
 'research/modal_repair/code/certify_scalar.py':a['script_sha256'],
 'research/modal_repair/code/independent_gauss_iv.py':b['script_sha256'],
 'research/exponential_moments/code/moments.py':a['moments_source_sha256'],
 'research/canonical_inverse/code/exact_audit.py':a['exact_Cox_source_sha256']}
for p,s in checks.items():assert sha(p)==s,p
oldmom=json.loads((BASE/'research/exponential_moments/evidence/actual_spline_audit.json').read_text())
oldcox=json.loads((BASE/'research/canonical_inverse/evidence/exact_audit.json').read_text())
assert oldmom['moment_library_sha256']==a['moments_source_sha256']
assert oldcox['script_sha256']==a['exact_Cox_source_sha256']
d=json.loads((BASE/'data_exact/modal_v2.json').read_text());k=exact(d['scalars_hex']['k']);bo=exact(d['scalars_hex']['bo'])
assert d['degree']==7 and d['arrays']['S']['shape'][0]>=4
pairs=d['outer_jl'];assert pairs[0]==[0,0] and len(set(map(tuple,pairs)))==len(pairs)
assert all(type(j) is int and type(l) is int and j>=0 and l>=0 for j,l in pairs)
alphas=[k-3-j*(1-k)-2*l for j,l in pairs]
assert alphas[0]+bo>0 and all(v<-2 for v in alphas) and all(v<=2*k-4 for v in alphas[1:])
public={
 'c_before_scalar_repair':['15.7260878319246786225638146971829','15.7260878319246786225638146971831'],
 'normalization_slope':['3386927.8387444893284459954233595','3386927.8387444893284459954233596'],
 'A00_correction':['-1.198605236453734890460334164888e-20','-1.198605236453734890460334164887e-20'],
 'exact_joins_cost_in_factor_norm':['4.075508828278320539267774194175e-10','4.075508828278320539267774194177e-10'],
 'scalar_correction_cost_in_factor_norm':['3.561661131767958722977145216913e-13','3.561661131767958722977145216915e-13'],
 'total_exactification_cost_common_endpoints':['4.079070489410088497990751339392e-10','4.079070489410088497990751339394e-10']}
for name,(lo,hi) in public.items():
 al,ah=first(a[name]);bl,bh=second(b['values'][name]);assert max(al,bl)<=min(ah,bh)
 assert F(lo)<=min(al,bl) and max(ah,bh)<=F(hi),name
assert F(public['total_exactification_cost_common_endpoints'][1])<F('4.080e-10')
review=json.loads((BASE/'notes/reviews/modal_scalar_final_audit_metadata.json').read_text())
assert review['actual_response_model']=='claude-opus-5-5'
files=list(checks)+['research/modal_repair/evidence/scalar_result.json','research/modal_repair/evidence/independent_gauss_iv.json','research/modal_repair/PROOF.md','research/exponential_moments/PROOF.md','research/exponential_moments/evidence/actual_spline_audit.json','research/canonical_inverse/evidence/exact_audit.json','notes/reviews/modal_scalar_final_audit_response.md','notes/reviews/modal_scalar_final_audit_metadata.json','research/modal_repair/code/final_audit.py']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','scope':'Exact common-knot-endpoint modal six-jet repair, canonical scalar normalization, and total weighted factor cost below 4.080e-10 relative to the literal modal formula with the same endpoints. Not a distance to X3 and not a stationary profile proof.','public_decimal_enclosures':public,'input_and_source_hashes_verified':True,'prior_moment_and_Cox_audit_hashes_match':True,'additional_exact_input_conditions':'PASS','independence':'Cox polynomials plus Arb moments versus derivative coefficients, de Boor, and mpmath.iv Gaussian derivative remainders. Closed-form join, slope, cost formulas and input are shared and proved analytically.','trusted_dependencies':'Python exact integer/Fraction arithmetic; python-flint/Arb and mpmath.iv outward arithmetic implementations. Neither library implementation is formally verified in this project.','actual_second_model':review['actual_response_model'],'source_and_evidence_sha256':{p:sha(p) for p in files}}
(E/'audit_verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'verdict':out['verdict'],'public_total_cost_upper':public['total_exactification_cost_common_endpoints'][1]}))
