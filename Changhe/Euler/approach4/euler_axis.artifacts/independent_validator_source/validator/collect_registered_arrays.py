"""Check the retained arrays of a complete independent native validation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path);args=ap.parse_args();args.directory=args.directory.resolve();out=args.directory/'array_collection.json';assert not out.exists();start=time.perf_counter();cpu=time.process_time()
checks=[]
def check(name,value):
 checks.append(dict(name=name,passed=bool(value)))
 if not value:raise AssertionError(name)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def close(a,b):return bool(np.isclose(a,b,rtol=3e-13,atol=1e-300))
def rms(a,w):
 if a.ndim==2:a=np.linalg.norm(a,axis=1)
 return float(np.sqrt(np.dot(w,a*a)/np.sum(w)))
d=json.loads((args.directory/'summary.json').read_text());p=args.directory/'registered';s=json.loads((p/'summary.json').read_text());tail=json.loads((args.directory/'tail.json').read_text());pre=json.loads((args.directory/'preflight.json').read_text())
for doc in [s,tail,pre]:
 for rel,h in doc['source_sha256'].items():check('source '+rel,sha(ROOT/rel)==h)
for name,h in pre['input_sha256'].items():check('input '+name,sha(Path(pre['input_paths'][name]))==h)
check('complete shell set',s['complete_required_shell_set']and len(s['rows'])==57)
check('native independent evaluator',s['evaluator']=='native spherical derivative operators with an exact-polynomial origin patch')
check('same candidate',s['candidate_sha256']==pre['input_sha256']['coeffs.npz']==tail['input_sha256'])
check('parameters',s['nradial']==8 and s['nangle']==64 and s['nrandom']==256)
with np.load(p/'arrays.npz',allow_pickle=False)as z:arrays={k:z[k]for k in z.files}
check('684 arrays',len(arrays)==684)
for key,a in arrays.items():check('finite float64 '+key,a.dtype==np.float64 and np.isfinite(a).all())
per_eq={};allrho=[];allm=[];swirl=[]
for row in s['rows']:
 prefix=f"{row['shell_index']}_{row['set']}_";w=arrays[prefix+'weights'];check('positive weights '+prefix,np.all(w>0));equations=row['metrics']['equations']
 for eq,key,component in [('M_vector','M',None),('M_r','M',0),('M_theta','M',1),('M_z','M',2),('q','q_residual',None),('eta','eta_residual',None),('div','divergence',None),('ell','elliptic',None)]:
  a=arrays[prefix+key];a=a[:,component]if component is not None else a;m=equations[eq];rr=rms(a,w);v=np.linalg.norm(a,axis=1)if a.ndim==2 else np.abs(a);maximum=float(np.max(v))
  check(prefix+eq+' rms',close(rr,m['rms']));check(prefix+eq+' maximum',close(maximum,m['maximum']))
  location=dict(shell=row['shell_index'],point_set=row['set']);per_eq.setdefault(eq,{})
  for metric,value in [('rho',m['rho']),('m',m['m']),('rms',rr),('maximum',maximum)]:
   if value is not None and (metric not in per_eq[eq]or value>per_eq[eq][metric]['value']):per_eq[eq][metric]=dict(value=value,**location)
  if m['denominator']>0:
   check(prefix+eq+' rho ratio',close(rr/m['denominator'],m['rho']));check(prefix+eq+' m ratio',close(maximum/m['denominator'],m['m']))
   if eq!='M_vector':allrho.append((m['rho'],dict(shell_index=row['shell_index'],set=row['set'],equation=eq)));allm.append((m['m'],dict(shell_index=row['shell_index'],set=row['set'],equation=eq)))
  else:check(prefix+eq+' undefined',m['rho']is None and m['m']is None)
 if row['shell_index']==0:
  U=arrays[prefix+'U'];swirl.append(dict(point_set=row['set'],velocity_rms=rms(U,w),swirl_velocity_rms=rms(U[:,1],w),swirl_fraction=rms(U[:,1],w)/rms(U,w)))
rho=max(allrho,key=lambda t:t[0]);mm=max(allm,key=lambda t:t[0]);agg=s['aggregate']
check('maximum rho',close(rho[0],agg['rho_max'])and rho[1]==agg['rho_max_at']);check('maximum m',close(mm[0],agg['m_max'])and mm[1]==agg['m_max_at']);check('driver agreement',agg==d['aggregate']);check('A1 failed',agg['rho_max']>1e-6 and not agg['A1_measured_pass']);check('A2 failed',agg['m_max']>1e-4 and not agg['A2_measured_pass'])
result=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',check_count=len(checks),all_passed=all(x['passed']for x in checks),candidate_sha256=s['candidate_sha256'],completed_utc=s['completed_utc'],aggregate=agg,per_equation=per_eq,core_swirl=swirl,gauge=s['gauge'],core={k:v for k,v in s['core'].items()if k in ['a_eff','max_vorticity','maximum_point_r_z','global_maximum_proved']},interfaces=d['interface_summary'],tail_correction=tail['correction_relative_to_Euler'],pressure_parameters=s['pressure_parameters'],input_sha256={str(f.relative_to(ROOT)):sha(f)for f in [args.directory/'summary.json',args.directory/'preflight.json',args.directory/'tail.json',p/'summary.json',p/'arrays.npz',Path(__file__)]},checks=checks,wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,scope='Retained float64 arrays, hashes, metric arithmetic and selectors checked. The registered residuals fail. Pressure refinement, identities and second representation remain separate checks.')
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ['checks','input_sha256']},indent=2))
