"""Bind dynamic own-module closure before and after an unchanged checker run."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from types import ModuleType
import importlib.util,json,sys,time
R=Path(__file__).resolve().parents[3];B=R/'research/joint_scaled_dyadic016'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def save(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def main():
 started=time.monotonic();kind='calibration' if '--calibration-only' in sys.argv else 'production';out=B/'verification';index=1
 while (out/f'bound_{kind}_v{index:02d}_start.json').exists():index+=1
 prefix=out/f'bound_{kind}_v{index:02d}';spec=importlib.util.spec_from_file_location('dyadic016_bound_checker',B/'code/check.py');C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
 todo=[C]+list(sys.modules.values());seen=set();paths=set();edges=[]
 while todo:
  m=todo.pop()
  if not isinstance(m,ModuleType) or id(m) in seen:continue
  seen.add(id(m));p=getattr(m,'__file__',None)
  if not p:continue
  p=Path(p).resolve()
  if not p.is_relative_to(R) or p.suffix!='.py':continue
  paths.add(p)
  for name,value in vars(m).items():
   if isinstance(value,ModuleType):
    todo.append(value);vp=getattr(value,'__file__',None)
    if vp and Path(vp).resolve().is_relative_to(R):edges.append({'from':str(p.relative_to(R)),'name':name,'to':str(Path(vp).resolve().relative_to(R))})
 expected=['research/rational_pole_moments/code/moments.py','research/factored_pole_moments/code/moments.py','research/successor_dyadic_probes/code/check.py','research/successor_weak_probes/code/check.py','research/joint_scaled_factored_weak/code/weak.py','research/joint_scaled_factored_weak/code/fields_joint.py','research/whole_plane_norms/code/norms.py']
 assert all(R/p in paths for p in expected)
 paths|={B/'PROOF.md',B/'DEPENDENCY_PROOF.md',Path(__file__).resolve()};before={str(p.relative_to(R)):sha(p) for p in sorted(paths)}
 historical={str(p.relative_to(R)):sha(p) for p in sorted(out.glob('C1-N1-*/mode_*.json'))}
 if (out/'calibration.json').exists():historical[str((out/'calibration.json').relative_to(R))]=sha(out/'calibration.json')
 # These two moment sources were source-bound in the accepted original016 weak test.
 earlier=R/'research/scaled_factored_weak/verification/C1-N1-016-legqs25-quot013_n019_K01800.json';old=json.loads(earlier.read_text());links={}
 for rel in expected[:2]:assert before[rel]==old['inputs'][rel];links[rel]=before[rel]
 before[str(earlier.relative_to(R))]=sha(earlier)
 first={'utc':now(),'kind':kind,'arguments':sys.argv[1:],'sources':before,'module_edges':edges,'earlier_mode_records':historical,'accepted_moment_source_links':links,'initial_calibration_scope':'Initial unwrapped attempt lacks before-run hashes for dynamic entry scripts; retained unchanged code and evidence are linked retrospectively, actual016 is wrapped from start'}
 save(Path(str(prefix)+'_start.json'),first);print(now(),'BOUND_START',kind,'own_sources',len(before),flush=True)
 C.main()
 assert all(sha(R/p)==h for p,h in before.items()) and all(sha(R/p)==h for p,h in historical.items())
 rp=out/('calibration.json' if kind=='calibration' else 'result.json');record=json.loads(rp.read_text())
 assert all(sha(R/p)==h for p,h in record['inputs'].items())
 result={'utc':now(),'kind':kind,'start_sha256':sha(Path(str(prefix)+'_start.json')),'result':str(rp.relative_to(R)),'result_sha256':sha(rp),'all_before_hashes_unchanged':True,'source_count':len(before),'final_modes':{str(p.relative_to(R)):sha(p) for p in sorted(out.glob('C1-N1-*/mode_*.json'))},'elapsed_seconds':time.monotonic()-started,'verdict':'CONFIRMED own dynamic source closure and unchanged checked records; numerical verdict is in the bound result'}
 save(Path(str(prefix)+'_result.json'),result);print(now(),'BOUND_DONE',sha(Path(str(prefix)+'_result.json')),flush=True)
if __name__=='__main__':main()
