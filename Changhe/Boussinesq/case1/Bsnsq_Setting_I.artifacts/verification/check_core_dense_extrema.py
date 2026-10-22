"""Raw scalar MP differentiation at FD-sample extrema and regional witnesses."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,csv,json,hashlib,os,time,resource
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import mpmath as mp
import numpy as np
from checked_core_source import bind
from core_generating_mp import from_data
from raw_generating_mp import fields,differentiate
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
def serial(x):
 if isinstance(x,mp.mpf):return mp.nstr(x,155)
 if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x

def inverse(G,x,y,guess,dps):
 e=guess
 for it in range(12):
  err=differentiate(G,x,e,1,0)-y
  if abs(err)/abs(y)<mp.mpf(10)**(-(dps-20)):return e,err,it+1
  A=differentiate(G,x,e,1,1)
  if A<=0:raise ArithmeticError('nonpositive raw derivative')
  e-=err/A
  if e*y<=0:raise ArithmeticError('raw Newton left correct half-axis')
 raise ArithmeticError('raw inverse relative convergence failed')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('root');args=ap.parse_args();root=Path(args.root);fd=root/'physical_fd';out=fd/'raw_followup';assert (out/'PROOF.md').exists()
 d,binding=bind(root/'center_with_core/input.json');summary=json.loads((fd/'audit.json').read_text());assert summary['status']=='PASS_FINITE_EVALUATION'
 assert summary['source_binding']['source_sha256']==binding['source_sha256']
 assert sha(fd/'points.csv')==summary['points_csv_sha256']
 for f,h in summary['hashes'].items():assert sha(f)==h
 with (fd/'points.csv').open() as f:rows=list(csv.DictReader(f))
 assert len(rows)==summary['completed_points']==10000
 reasons={}
 def add(i,reason):reasons.setdefault(int(i),[]).append(reason)
 for k,v in summary['maxima'].items():add(v['index'],'global_'+k)
 primary=set(reasons)
 for reg,vals in summary['regions'].items():
  for k in ['q','q2','R','D','step_q2_difference']:add(vals[k]['index'],'band'+reg+'_'+k)
 for i in np.random.default_rng(202610210522).choice(len(rows),12,replace=False):add(i,'extra_seed202610210522')
 repeat=primary|set(sorted(reasons)[::max(1,len(reasons)//12)])
 files=[Path(__file__),fd/'points.csv',fd/'audit.json',out/'PROOF.md',root/'center_with_core/input.json',Path('code/core_generating_mp.py'),Path('code/raw_generating_mp.py'),Path('code/checked_core_source.py')]
 report={'start_utc':now(),'status':'OPEN','source_binding':binding,'selected':reasons,'repeat130':sorted(repeat),'rows':[],'precision':[],'hashes':{str(p):sha(p) for p in files},'scope':'Finite raw differentiation at selected points; neither numerical error interval nor regional supremum.'}
 def save():(out/'checks.json').write_text(json.dumps(serial(report),indent=2)+'\n')
 maxima={};base={};start=time.monotonic()
 for dps,indices in [(90,sorted(reasons)),(130,sorted(repeat))]:
  with mp.workdps(dps):
   G,a=from_data(d)
   for index in indices:
    row=rows[index];assert int(row['index'])==index;x,y=mp.mpf(row['x']),mp.mpf(row['y']);e,err,it=inverse(G,x,y,mp.mpf(row['eta']),dps)
    raw,terms,groups,dterms=fields(G,a,x,e)
    results={}
    mapping={'q':'prompt_ratio','q2':'grouped_ratio','R':'R','D':'D','N':'N','N2':'N2','Omega':'Omega','Omega_x':'Omega_x','Omega_y':'Omega_y'}
    for step in ['coarse','fine']:
     errors={}
     for key,rawkey in mapping.items():
      truth=raw[rawkey];s=row[step+'_'+key]
      if truth is None or not s:
       assert truth is None and not s;errors[key]={'undefined':True};continue
      value=mp.mpf(s);error=abs(value-truth)
      errors[key]={'absolute':error,'relative':error/abs(truth) if truth else None}
      k=step+'_'+key
      if k not in maxima or error>mp.mpf(maxima[k]['absolute']):maxima[k]={'absolute':serial(error),'index':index,'dps':dps}
     results[step]=errors
    entry={'index':index,'dps':dps,'x':row['x'],'physical_y':row['y'],'eta':e,'inverse_absolute_y_defect':abs(err),'inverse_relative_y_defect':abs(err)/abs(y),'inverse_iterations':it,'fields':raw,'terms':terms,'groups':groups,'differences':results}
    report['rows'].append(serial(entry));report['max_absolute_errors']=maxima;save()
    if dps==90:base[index]=serial(raw)
    else:
     diffs={}
     for key,v in raw.items():
      old=base[index][key]
      if v is None:assert old is None;continue
      delta=abs(mp.mpf(old)-v);relative=delta/abs(v) if v else None
      diffs[key]={'absolute':delta,'relative':relative}
      # Algebraic regrouping errors vanish only in exact arithmetic; their
      # sizes reflect the two working precisions, not physical observables.
      if key in ['regrouping_error','desingularized_regrouping_error']:continue
      assert (relative if relative is not None else delta)<mp.mpf('1e-55'),(index,key,delta,relative)
     report['precision'].append(serial({'index':index,'errors':diffs}));save()
    for step in ['coarse','fine']:
     for key in ['q','q2']:assert results[step][key]['absolute']<mp.mpf('1e-8'),(index,dps,step,key,results[step][key])
    print(now(),'point',index,'dps',dps,'qerr',mp.nstr(results['fine']['q']['absolute'],8),'q2err',mp.nstr(results['fine']['q2']['absolute'],8),flush=True)
 report.update(status='PASS_FINITE_RAW_CHECK',end_utc=now(),seconds=time.monotonic()-start);save();print('PASS',len(reasons),'points',len(repeat),'repeats',report['seconds'],flush=True)
if __name__=='__main__':main()
