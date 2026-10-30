from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction as Q
import json
R=Path(__file__).resolve().parents[3];B=R/'research/candidate017_dyadic_preparation';sha=lambda p:sha256(p.read_bytes()).hexdigest()
paths=['verification/result.json','verification/bound_production_v01_start.json','verification/bound_production_v01_result.json','PROOF.md','DEPENDENCY_PROOF.md','code/check.py','code/run_bound.py','code/check_acceptance.py'];inputs={str((B/p).relative_to(R)):sha(B/p) for p in paths}
out=json.loads((B/paths[0]).read_text());start=json.loads((B/paths[1]).read_text());bound=json.loads((B/paths[2]).read_text())
assert bound['result_sha256']==sha(B/paths[0]) and bound['start_sha256']==sha(B/paths[1]) and bound['all_before_hashes_unchanged']
for mapping in [out['inputs'],start['sources'],start['earlier_mode_records'],bound['final_modes']]:
 for p,h in mapping.items():assert sha(R/p)==h;inputs[p]=h
modes=[]
for p,h in bound['final_modes'].items():
 x=json.loads((R/p).read_text());assert x['Cartesian_polar_equal'] and x['mixed_derivatives_equal'];assert len(x['weights'])==2
 assert all(w['accuracy_bits']>150 for w in x['weights'])
 assert all(d['exact_reconstruction'] for d in x['decompositions'])
 assert all(Q(e['diagonal_integrability_margin'])>0 for e in x['endpoints'])
 if '007-' in p:assert len(x['polynomial_calibration'])==6 and all(x['polynomial_calibration'].values()) and all(w['accepted007_energy_overlap'] for w in x['weights'])
 modes.append({'path':p,'mode':x['mode'],'branches':len(x['endpoints']),'crosspairs':x['pairs'],'groups':x['group_count'],'min_accuracy_bits':min(w['accuracy_bits'] for w in x['weights'])})
z=out['results']['C1-N1-017-legqs50-quot013'];assert z['conditional_all_seven_excluded'] and len(z['seven_cells'])==7 and all(c['excluded'] for c in z['seven_cells'])
assert set(z['peer_comparisons'])=={'1/4','7/4'} and all(c['containing_display'] for c in z['peer_comparisons'].values())
floor=min(Q(c['strict_ratio_floor']) for c in z['seven_cells']);assert floor>1
record={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'source_count':len(inputs),'mode_checks':modes,'norms':z['norms'],'minimum_strict_ratio_floor':str(floor),'minimum_strict_ratio_floor_decimal':str(float(floor)),'seven_cell_gaps':[c['gap'] for c in z['seven_cells']],'scope':'CONFIRMED N4-389 two complete projected norms, two N3 squared displays and conditional seven-cell exclusion. Five other N3 endpoint values not reproduced. No full norm upper bound or existence.','foreign_code_executed':False}
with (B/'verification/acceptance_v01.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(record['utc'],len(inputs),'sources','strict_min_ratio',floor,'mode_checks',modes,sha(B/'verification/acceptance_v01.json'))
