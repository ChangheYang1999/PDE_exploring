"""Exact endpoint and dependency-manifest audit of the selected Green checks."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/modal_green/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dyad(v):return F.from_float(float.fromhex(v))
p=E/'selected_boundaries.json';r=json.loads(p.read_text())
for key,path,want in [('input_sha256','data_exact/modal_v2.json','57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'),('moments_source_sha256','research/exponential_moments/code/moments.py','6f9aa03d5f7f4f2dff22e5bc8319a861148313e96d89991c16ee979dfdf0489c'),('scalar_input_sha256','research/modal_repair/evidence/independent_gauss_iv.json','0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a')]:assert r[key]==sha(BASE/path)==want
assert r['code_sha256']==sha(BASE/'research/modal_green/code/check_boundaries.py')
assert sha(BASE/'research/canonical_inverse/code/exact_audit.py')=='331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42'
assert r['green_sha256']=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'
keys=set();count=0
for row in r['comparisons']:
 lo,hi=F(row['independent']['lower_exact']),F(row['independent']['upper_exact']);mid,rad=dyad(row['exported_mid_hex']),dyad(row['exported_rad_hex']);assert rad>=0 and mid-rad<=lo<=hi<=mid+rad
 key=(row['array'],row['boundary_index'],row['stream_index_n']);assert key not in keys;keys.add(key);assert row['verdict']=='CONTAINED';count+=1
assert keys=={(a,b,n) for a in ('A','B') for b in r['selected_boundary_indices'] for n in r['mode_indices']}
assert count==180 and r['all_exported_boundary_enclosures_checked']==7810 and r['counts']=={'CONTAINED':180,'OVERLAP_ONLY':0,'DISJOINT':0}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED selected180 Green entries','result_sha256':sha(p),'audit_source_sha256':sha(__file__),'calculation_source_sha256':r['code_sha256'],'compared_artifact_sha256':r['green_sha256'],'counts':r['counts'],'mode_indices':r['mode_indices'],'boundary_indices':r['selected_boundary_indices'],'method':'Recomputed exact dyadic/Fraction endpoint containments and set coverage; dependency hashes bound to accepted exact Cox, moment and scalar certificates. Source method independently reviewed. The original computation hashed the read-only full Green artifact both before and after.','scope':'Only the named180 entries and all7810 boundary abscissa enclosures are confirmed; no assertion for untested Green entries, modal residual products or inverse bounds.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
