from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/weighted_l2_tail_display_repair';E=D/'evidence';NUM=ROOT.parent/'ipmA-num'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
parent='research/weighted_l2_tail_reduction/evidence/verdict.json';assert sha(ROOT/parent)=='c1ad9aff752b39c98ea3b127606d7e8b096051878d3047ec44681f1411e19688';v=load(ROOT/parent)
for n,h in v['files'].items():assert sha(ROOT/n)==h,n
snap={}
for name,rel in [('r2_tails_v2.py','src/r2_tails.py'),('r2_tails_v2.json','runs/r2_tails.json'),('NUM_REPORT.md','NUM_REPORT.md')]:
 source=NUM/rel;dest=D/'sources'/name;b=source.read_bytes()
 with dest.open('xb') as f:f.write(b)
 assert source.read_bytes()==b
 snap[str(dest.relative_to(ROOT))]={'original_path':str(source),'sha256':sha(dest)}
x=load(ROOT/'research/weighted_l2_tail_reduction/evidence/inputs.json');y=load(D/'sources/r2_tails_v2.json');assert y['tag']==''
report=(D/'sources/NUM_REPORT.md').read_text()
assert 'add up to at most 3.9563e-7' in report and 'sum of the raw L2 pieces is <= 3.95619e-7' in report
assert '4.9727e-9 (middle) + 3.9065e-7 (outer) + 3.4826e-16 (inner) <= 3.9562e-7' not in report
labels={n:y[n] for n in ['inner_tail_sq_upper_endpoint','outer_tail_sq_upper_endpoint','finite_sq_upper_endpoint','finite_R2_upper_endpoint','total_R2_upper_endpoint']}
out={'utc':datetime.now(timezone.utc).isoformat(),'parent_path':parent,'parent_sha256':sha(ROOT/parent),'parent_status':v['status'],'parent_files':v['files'],'snapshots':snap,'scalars':x['scalars'],'C_i_exact':x['C_i_exact'],'C_o_exact':x['C_o_exact'],'finite_inputs_exact':x['finite_binary64_upper_inputs'],'finite_sum_exact':x['finite_sum_exact'],'labels':labels,'report':{'finite_raw_ceiling':'3.95619e-7','finite_printed_terms':['4.9727e-9','3.9065e-7','3.4826e-16'],'finite_printed_sum_ceiling':'3.9563e-7','enlarged_C_i':'2.13842e-6','enlarged_C_o':'1.75412e-6','inner_tail_ceiling':'3.819e-20','outer_tail_ceiling':'6.504e-16','whole_ceiling':'6.2899e-4'},'scope':'Saved scalar/display repair only; no physical premise discharged.'}
with (E/'inputs.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],labels,len(v['files']))
