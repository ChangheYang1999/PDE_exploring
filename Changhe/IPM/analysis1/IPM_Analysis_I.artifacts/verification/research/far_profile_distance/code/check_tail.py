"""Run both independent finite interval methods; nonzero witness fails closed."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys
assert not sys.flags.optimize
sys.dont_write_bytecode=True
B=Path(__file__).resolve().parents[3];D=B/'research/far_profile_distance'
import engine_arb,engine_iv
p=json.loads((D/'source/parameters.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for f,h in p['files'].items():assert sha(B/f)==h,f
for f,h in p['modal_dependency_pins'].items():assert sha(B/f)==h,f
outputs={'arb512':engine_arb.evaluate(p),'iv180':engine_iv.evaluate(p)}
for eng,o in outputs.items():
 for key,v in o['values'].items():assert Q(v['lower_exact'])<=Q(v['upper_exact']),key
 lo=Q(o['values']['Delta']['lower_exact']);hi=Q(o['values']['Delta']['upper_exact']);assert lo>0 or hi<0, (eng,'inconclusive witness')
 for key,(lower,upper) in p['public_strict_enclosures'].items():
  assert Q(lower)<Q(o['values'][key]['lower_exact'])<=Q(o['values'][key]['upper_exact'])<Q(upper),(eng,key)
 assert Q(o['values']['D_F0']['lower_exact'])>0
 assert 6<Q(o['values']['p']['lower_exact'])<=Q(o['values']['p']['upper_exact'])<7
 assert Q(o['values']['T1']['lower_exact'])>0
 assert Q(o['values']['z']['lower_exact'])<Q(o['values']['z']['upper_exact'])<0
files=[D/'PROOF.md',D/'ADDENDUM.md',D/'PUBLICATION.md',D/'source/parameters.json']+sorted((D/'code').glob('*.py'))
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_INDEPENDENT_NONZERO_TAIL_WITNESSES','outputs':outputs,'files':{str(f.relative_to(B)):sha(f) for f in files},'source_pins':p['files'],'dependency_pins':p['modal_dependency_pins'],'public_strict_enclosures':p['public_strict_enclosures'],'scope':'Leading-tail values at theta=pi/4 and exact nonanalytic coefficient, not finite-radius residual or PDE exclusion'}
(D/'evidence/checks.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'utc':r['utc'],'status':r['status'],'display_only':{e:{k:v['display'] for k,v in o['values'].items()} for e,o in outputs.items()}}))
