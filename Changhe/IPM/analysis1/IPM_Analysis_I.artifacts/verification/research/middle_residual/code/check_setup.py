"""Cross-check fast moments and extracted cell core before the full middle run."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from fast_moments import phi_values,aa
B=Path(__file__).resolve().parents[3];E=B/'research/middle_residual/evidence'
sys.path.insert(0,str(B/'research/exponential_moments/code'))
from moments import phi
ctx.prec=384;ctx.threads=1
count=0;acc=100000
for z in [F(0),F(1,10**8),F(-1,10**8),F(1,1000),F(-1,1000),F(1,2),F(-1,2),F(21,2),F(-21,2)]:
 ph=phi_values(z)
 for j,v in enumerate(ph):assert v.overlaps(phi(j,aa(z),128));count+=1;acc=min(acc,v.rel_accuracy_bits())
import cell_core as c
samples=json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text());old=json.loads((B/'research/residual_cells/evidence/q16_result.json').read_text());pub=json.loads((B/'research/residual_samples/evidence/published_residual_snapshot.json').read_text(),parse_float=F);tr=json.loads((B/'data_exact/modal_v2.json').read_text());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')];knots=sorted(set(F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']));checks=[]
for row in samples['samples']:
 if row['cell'] not in (0,4125):continue
 r=c.bound_cell(row,k,L,knots,pub,Q=16);o=next(v for v in old['cells'] if v['cell']==row['cell']);assert r['W_upper_exact']==o['W_upper_exact'] and r['W_over_m_upper_exact']==o['W_over_m_upper_exact'];checks.append(row['cell'])
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','fast_vs_Taylor_moment_checks':count,'minimum_fast_accuracy_bits':acc,'extracted_cell_exact_equality':checks,'hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).parent/'fast_moments.py',Path(__file__).parent/'cell_core.py',Path(__file__).parent/'modal_setup.py']}}
(E/'setup_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
