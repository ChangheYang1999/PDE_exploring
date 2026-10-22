"""Retain exact scalar inputs and read-only provenance; no certificate inference."""
import os,sys
sys.dont_write_bytecode=True
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,re
import numpy as np
D=Path(__file__).resolve().parents[1];ROOT=D.parents[1];NUM=ROOT.parent/'ipmA-num'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,z):p.write_text(json.dumps(z,indent=2,allow_nan=False)+'\n')
assert json.loads((D/'evidence/proof_first.json').read_text())['sha256']==sha(D/'PROOF.md')
assert not (D/'evidence/inputs.json').exists()
origins={}
for name in ['src/r2_tails.py','runs/r2_tails.json','runs/cert_tail.json','runs/cert_inner_tail.json','runs/variants_summary.json','NUM_REPORT.md']:
 src=NUM/name;dest=D/'sources'/src.name;data=src.read_bytes();dest.write_bytes(data)
 origins[str(dest.relative_to(ROOT))]={'original_path':str(src),'sha256':hashlib.sha256(data).hexdigest()}
trial=NUM/'data/trial_v2_h0.008.npz';before=sha(trial)
with np.load(trial,allow_pickle=False) as f:
 scalars={n:str(F.from_float(float(f[n]))) for n in ['k','L']};scalars['a']=str(F.from_float(float(f['knots'][0])));scalars['b']=str(F.from_float(float(f['knots'][-1])))
assert sha(trial)==before
assert scalars=={'k':'1615536043799051/9007199254740992','L':'8614738245908811/1125899906842624','a':'-685794559684773/140737488355328','b':'2289893859708677/281474976710656'}
def ball(s):
 m=re.fullmatch(r'\[\s*([-0-9.eE+]+)\s*\+/-\s*([-0-9.eE+]+)\s*\]',s);assert m,s
 c,r=map(F,m.groups());assert r>=0;return c-r,c+r
outer=json.loads((D/'sources/cert_tail.json').read_text());inner=json.loads((D/'sources/cert_inner_tail.json').read_text());stored=json.loads((D/'sources/r2_tails.json').read_text())
rows=json.loads((D/'sources/variants_summary.json').read_text());selected=[r for r in rows if r['tag']==''];assert len(selected)==1;s=selected[0]
ci=ball(inner['bound_W_over_m'])[1];co=ball(outer['tail_bound_weighted'])[1];assert ci>0 and co>0
finite={n:str(F.from_float(s[n]['L2'])) for n in ['middle','outer','inner']}
report=(D/'sources/NUM_REPORT.md').read_text();assert 'C_out = 1.75412e-6' in report and '2.13842e-6 gives at most' in report
x={'utc':datetime.now(timezone.utc).isoformat(),'status':'EXACT_SCALAR_INPUTS_ONLY_PHYSICAL_MAJORANTS_ASSUMED','scalars':scalars,'outer_offset':'17','inner_offset':'-5','C_i_exact':str(ci),'C_o_exact':str(co),'reported_enlarged_C_i':'2.13842e-6','reported_enlarged_C_o':'1.75412e-6','finite_binary64_upper_inputs':finite,'finite_sum_exact':str(sum(map(F,finite.values()),F(0))),'stored_printed_balls':{k:v for k,v in stored.items() if isinstance(v,str) and v.startswith('[')},'endpoint_labels':{k:stored[k] for k in ['outer_tail_sq_upper_endpoint','inner_tail_sq_upper_endpoint','total_R2_upper_endpoint']},'report_tail_ceilings':{'outer':'6.504e-16','inner':'3.819e-20'},'report_whole_ceiling':'6.2899e-4','report_summary_short_values':{'outer':'6.5e-16','inner':'3.8e-20'},'literal_archive':{'path':str(trial),'sha256':before},'source_snapshots':origins,'scope':'Scalar conditional arithmetic for the stored modal trial. This neither certifies the tail majorants nor the finite-region integrals nor a canonical normalization change.'}
write(D/'evidence/inputs.json',x);print(json.dumps({'utc':x['utc'],'status':x['status'],'sha256':sha(D/'evidence/inputs.json'),'source_snapshots':len(origins)}))
