from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/numerics_v07_audit'
publication=BASE/'source/numerics_v07.md'
raw=ROOT/'research/candidate_audits/data/C1-N1-014-pairB-from007/d2w_j7_n4_E2bal_pairB_cpu_m16_exact.json'
H=lambda p:sha256(p.read_bytes()).hexdigest()
assert H(publication)=='8fb65706ecd07ff52be92b0604483c0b02a19ac8de483bc755c3b967d8661c33'
assert H(raw)=='8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746'
meta=json.loads(raw.read_text())['meta'];pairs=meta['pair_k'];probes=[[21,522],[23,523],[25,524]]
assert len(pairs)==102 and all(p in pairs for p in probes) and meta['wpair']==10**12
notes=BASE/'source/N1_NOTES_0530.md'
assert 'concentrated near r about 1' in notes.read_text()
c=Q(4076476460239181,2251799813685248);gamma=1/c;p1=1+gamma
assert p1==(3+gamma-(1-gamma))/2 and p1>0
profiles=[{'m':m,'p_exact':str(p1),'log_derivative_numerator_in_r2':[str(2*m),str(2*p1)],'both_numerator_coefficients_positive':True,'normalized_amplitude_at_r1':str(Q(1,2**m)),'normalized_amplitude_at_r_sqrt_m':str(Q(m,m+1)**m)} for m in [17,18,19]]
rows=[]
for lam in [Q(1,10**6),Q(1,10**4)]:
 x=1/(1+lam);residual=1-x
 assert (1+lam)*x==1 and residual==lam/(1+lam)>0 and 0<x<1
 rows.append({'lambda':str(lam),'unique_damped_solution':str(x),'damped_residual':str(residual),'undamped_solution':'1','undamped_optimal_residual':'0','both_positive_residual_and_norm_below_undamped':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(ROOT)):H(p) for p in [publication,raw,notes,Path(__file__),BASE/'PROOF.md']},'exact_scalar_counterexamples':rows,'bare_radial_profile_monotonicity':profiles,'bare_radial_profile_concentrated_near_r1':'REFUTED; derivative positive for all r>0','candidate014_row_count':len(pairs),'candidate014_design_probes':probes,'uniform_pairing_weight':meta['wpair'],'universal_damped_floor_inference':'REFUTED by exact scalar example','two_positive_damping_values_bracket_undamped':'REFUTED by exact scalar example','actual_IPM_span_optimum':'OPEN','uniform_IPM_family_floor':'OPEN','014_listed_probes_held_out':'REFUTED by exact snapshot metadata','frozen_probe_necessary_test_valid_regardless_of_selection':True}
with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],'counterexamples',len(rows),'metadata probes',len(probes))
