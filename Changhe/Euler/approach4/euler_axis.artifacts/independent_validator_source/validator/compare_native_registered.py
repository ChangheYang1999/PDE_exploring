#!/usr/bin/env python3
"""Compare native-derivative registered data with a frozen Taylor evaluation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser();p.add_argument('--reference',type=Path,required=True);p.add_argument('--native',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--partial',action='store_true');a=p.parse_args()
 if a.output.exists() or not a.output.resolve().is_relative_to(ROOT.parent):raise ValueError('fresh output in lane required')
 start=time.perf_counter();ref=a.reference/'summary.json';new=a.native/('progress.json' if a.partial else 'summary.json');x=json.loads(ref.read_text());y=json.loads(new.read_text());inputs=[ref,new,a.reference/'metadata.json',a.native/'metadata.json',a.reference/'geometry.json',a.native/'geometry.json'];mx=json.loads(inputs[2].read_text());my=json.loads(inputs[3].read_text());gx=json.loads(inputs[4].read_text());gy=json.loads(inputs[5].read_text());checks=[];numeric=[];arrays=[];missing=[]
 def check(name,ok,**extra):checks.append(dict(name=name,passed=bool(ok),**extra))
 check('candidate_hash',mx['candidate_sha256']==my['candidate_sha256']);check('registered_parameters',mx['parameters']==my['parameters'])
 def walk(v,w,path):
  if isinstance(v,bool):check(path,v==w);return
  if isinstance(v,(int,float)):
   error=abs(v-w);scale=max(1.,abs(v),abs(w));numeric.append(dict(path=path,absolute_error=error,scaled_error=error/scale));check(path,error<=2e-8*scale);return
  if isinstance(v,dict):
   for key in v:
    if key in w:walk(v[key],w[key],path+'/'+str(key))
    else:missing.append(path+'/'+str(key))
   return
  if isinstance(v,list):
   check(path+'/length',len(v)==len(w))
   for i,(vv,ww) in enumerate(zip(v,w)):walk(vv,ww,path+'/'+str(i))
   return
  check(path,v==w)
 walk(gx,gy,'geometry');oldrows={(r['shell_index'],r['set']):r for r in x['rows']}
 for row in y['rows']:
  key=(row['shell_index'],row['set']);check('row_present_'+str(key),key in oldrows)
  if key in oldrows:walk(oldrows[key],row,'row_'+str(key))
 if not a.partial:
  check('row_count',len(x['rows'])==len(y['rows']));walk(x['aggregate'],y['aggregate'],'aggregate');check('complete',y['complete_required_shell_set'])
 oldnpz=a.reference/'arrays.npz';newnpz=a.native/(y['arrays_file'] if a.partial else 'arrays.npz');inputs.extend([oldnpz,newnpz])
 with np.load(oldnpz,allow_pickle=False) as u,np.load(newnpz,allow_pickle=False) as v:
  if not a.partial:check('array_keys',set(u.files)==set(v.files))
  for key in v.files:
   check(key+'/present',key in u.files)
   if key not in u.files:continue
   old=u[key];new=v[key];check(key+'/shape_dtype',old.shape==new.shape and old.dtype==new.dtype)
   if old.shape!=new.shape:continue
   error=float(np.max(np.abs(old-new)));scale=max(1.,float(np.max(np.abs(old))),float(np.max(np.abs(new))));arrays.append(dict(key=key,shape=list(old.shape),absolute_error=error,scaled_error=error/scale));check(key+'/values',error<=2e-8*scale and np.all(np.isfinite(new)))
 # Earlier reference records have extra diagnostic Boolean flags; disclose those omissions.
 result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,partial=a.partial,reference=str(a.reference),native=str(a.native),candidate_sha256=mx['candidate_sha256'],rows=len(y['rows']),arrays_compared=len(arrays),checks=len(checks),all_pass=all(r['passed'] for r in checks),failures=[r for r in checks if not r['passed']],missing_reference_fields=missing,max_numeric_scaled_error=max((r['scaled_error'] for r in numeric),default=0),max_array_scaled_error=max((r['scaled_error'] for r in arrays),default=0),numeric=numeric,arrays=arrays,source_sha256=sha256(Path(__file__)),inputs_sha256={str(p):sha256(p) for p in inputs},scope='Comparison of two derivative implementations for the same field and same registered pressure algorithm; tolerance2e-8. Partial records do not establish full-grid reproduction.')
 atomic_json(a.output,result);print(json.dumps({k:result[k] for k in ['completed_utc','wall_seconds','partial','rows','arrays_compared','checks','all_pass','failures','max_numeric_scaled_error','max_array_scaled_error']}),flush=True)
if __name__=='__main__':main()
