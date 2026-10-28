"""Exact-rational final aggregation, using both independently computed tail bounds."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,math
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
paths={k:TOP/'evidence'/v for k,v in {'journal':'journal_audit.json','replay':'replay.json','inner':'inner_replay.json'}.items()}
j=json.loads(paths['journal'].read_text());r=json.loads(paths['replay'].read_text());i=json.loads(paths['inner'].read_text())
assert j['status']=='JOURNAL_AUDIT_PASS' and j['coverage_end']=='20' and j['leaf_count']==1860
run=LANE/'proofs/134_residual_green_taylor/evidence/production_28'
original=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert sha(original)==j['source_sha256']
assert sha(run/'metadata.json')==j['metadata_sha256']
assert sha(run/'leaves.jsonl')==j['journal_sha256']
assert sha(TOP/'code/audit.py')==j['checker_sha256']
meta=json.loads((run/'metadata.json').read_text())
assert sha(LANE/'proofs/134_residual_green_taylor/code/integrate.py')==meta['code_sha256']
assert sha(LANE/'proofs/134_residual_green_taylor/PROOF.md')==meta['proof_sha256']
assert j['arithmetic_checks']==3720 and r['bits']==640 and r['degree']==36
assert len(r['rows'])==13 and len({x['leaf_id'] for x in r['rows']})==13
assert all(x['overlap']=='PASS' and x['replay']['center_overlap']=='PASS' and x['replay']['velocity_derivative_overlap']=='PASS' for x in r['rows'])
assert i['bits']==640 and i['source_sha256']==j['source_sha256']
old=Q(i['saved']['energy_upper']['upper_exact']);new=Q(i['fresh']['energy_upper']['upper_exact'])
extra=max(Q(0),new-old)
# Distinct upper estimates need not overlap. Retain the larger exact endpoint.
lo=Q(j['final_norm']['energy_lower_exact']);hi=Q(j['final_norm']['energy_upper_exact'])+extra
assert Q(604911,100)**2<lo and hi<Q(860142,100)**2
assert extra<Q(1,10**140)
now=datetime.now(timezone.utc).isoformat()
out={'date':now,'status':'CONFIRMED','norm':'Y = E G direct sum L2_P(|x|^(-17/2) max(1,r)^(29/4) dX)','strict_norm_lower':'6049.11','strict_norm_upper':'8601.42','energy_lower_exact':str(lo),'energy_upper_exact':str(hi),'source_sha256':j['source_sha256'],'journal_sha256':j['journal_sha256'],'metadata_sha256':j['metadata_sha256'],'base_interval_count':j['base_interval_count'],'leaf_count':j['leaf_count'],'branch_counts':j['branch_counts'],'replayed_leaf_count':13,'replay_bits':640,'replay_degree':36,'inner_tail_upper_exact':str(max(old,new)),'inner_tail_enlargement_exact':str(extra),'inner_tail_enlargement_less_than':'1e-140','input_hashes':{k:sha(v) for k,v in paths.items()},'finalizer_sha256':sha(Path(__file__)),'scope':'Exact normalized modal trial, full angular target and full radial line. No inverse constant or nonlinear existence claim.'}
(TOP/'evidence/final_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('_exact')},indent=2))
