import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_high_band';U=B/'research/saved_image_row_functionals'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
pins={};records=[]
for name in ['c2gram2_M24_s16_o32_p4_H1m_NJ1_rowsH1q.json','c2gram2_M24_s16_o40_p4_H1m_NJ1_rowsH1q.json','c2gram2_M24_s8_p4_H1m_NJ1_rowsH1q.json']:
 p=B.parent/'ipmA-num/runs/c2'/name;h=sha(p);data=p.read_bytes();assert sha(p)==hashlib.sha256(data).hexdigest()==h
 target=D/'sources'/name
 with target.open('xb') as f:f.write(data)
 x=json.loads(data);v=x['sections']['Fminus']['sigma_small5'];assert len(v)==5 and all(isinstance(a,float) and a>0 for a in v)
 records.append({'source':str(target.relative_to(B)),'metadata':{k:x[k] for k in ['Mh','stride','Mout','ppc','Ne','NJ','rows_mode']},'n_kept':x['sections']['Fminus']['n_kept'],'small5_exact':[str(Fraction(a)) for a in v]});pins[str(target.relative_to(B))]=h
for p in [U/'data_exact/selected_arrays.json.gz',U/'evidence/verdict.json',U/'PROOF.md',U/'POSTREVIEW_ADJUDICATION.md',D/'PROOF.md',Path(__file__)]+list((U/'sources').glob('c2gram2_M24_s16_o40_p4_H1m_NJ1_rows*q_vec.npz')):pins[str(p.relative_to(B))]=sha(p)
assert sha(U/'evidence/verdict.json')=='c85730f5cf9563fcf176ebe0b223ed5529b583eccb07b59c1d46328839c170df'
with (D/'data_exact/summaries.json').open('x') as f:json.dump(records,f,indent=2);f.write('\n')
pins[str((D/'data_exact/summaries.json').relative_to(B))]=sha(D/'data_exact/summaries.json')
x={'utc':datetime.now(timezone.utc).isoformat(),'status':'CAPTURED_LITERAL_INPUTS','files':dict(sorted(pins.items()))}
with (D/'data_exact/manifest.json').open('x') as f:json.dump(x,f,indent=2);f.write('\n')
print(json.dumps({'utc':x['utc'],'sources':len(pins),'summary_scalars':15}))
