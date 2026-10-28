"""Resumable orchestration of the unchanged independent norm evaluator.

No leaf formula is changed. Each invocation stops within its explicit time
budget; complete output is written only after all leaves have been checked.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,time
from flint import arb,arb_mat,ctx
import recheck_norms as core
from recheck_fast import A,endpoints,tree
p=Path(__file__).resolve().parent
sha=lambda f:sha256(f.read_bytes()).hexdigest()

def main(args):
 ctx.prec=640;start=time.monotonic();src=p/args.file;cert=json.loads(src.read_text());assert cert['status']=='COMPLETE';name=cert['name'];pp=p/f'{name}.polynomials.json';ee=p/f'{name}.derivatives.json';d=json.loads(pp.read_text());e=json.loads(ee.read_text());assert cert['source_sha256']==sha(pp) and cert['derivatives_sha256']==sha(ee);delta=F(d['delta']);assert delta>F(4,9)
 bindings={'primary_sha256':sha(src),'polynomials_sha256':sha(pp),'derivatives_sha256':sha(ee),'core_code_sha256':sha(p/'recheck_norms.py'),'driver_code_sha256':sha(Path(__file__)),'restriction_code_sha256':sha(p/'recheck_fast.py')}
 paths={v['path'] for v in cert['accepted']};assert len(paths)==len(cert['accepted']);tree(paths);rows=[];previous=0;parent=None;partial=src.with_name(src.stem+'.recheck.partial.json')
 if args.resume:
  old=json.loads(partial.read_text());assert old['status']=='INCOMPLETE';assert all(old[k]==v for k,v in bindings.items());rows=old['rows'];previous=old['cumulative_seconds'];parent=sha(partial)
  assert [v['path'] for v in rows]==[v['path'] for v in cert['accepted'][:len(rows)]]
  assert all(v['pass'] and all(arb(z)<=1 for z in v['ratios'].values()) for v in rows)
 S,labels=core.make_fields(d,e,cert['kind']);nt=max(i for q in S.values() for i,k in q);nz=max(k for q in S.values() for i,k in q);P={}
 for key,poly in S.items():
  mm=arb_mat(nt+1,nz+1)
  for (i,k),v in poly.items():mm[i,k]=A(v)
  P[key]=mm
 def record(complete=False):
  out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE' if complete else 'INCOMPLETE','all_pass':bool(complete),'precision_bits':ctx.prec,**bindings,'rows':rows,'leaves':len(rows),'total_leaves':len(paths),'seconds':time.monotonic()-start,'cumulative_seconds':previous+time.monotonic()-start,'previous_partial_sha256':parent}
  dest=src.with_name(src.stem+'.recheck.json') if complete else partial;dest.write_text(json.dumps(out,indent=2)+'\n');return out
 for row in cert['accepted'][len(rows):]:
  if time.monotonic()-start>=args.seconds:break
  a,b,c,z=endpoints(row['path']);assert list(map(str,[a,b]))==row['t'] and list(map(str,[c,z]))==row['z'];vals=core.upper_fields(P,nt,nz,a,b,c,z,delta,labels);rat=core.ratios(vals,cert['kind'],a,b,c,z,delta);assert all(v<=1 for v in rat.values()),(row['path'],rat);rows.append({'path':row['path'],'ratios':{k:v.str(85) for k,v in rat.items()},'pass':True})
  if len(rows)%10==0:record();print(len(rows),'PASS',time.monotonic()-start,flush=True)
 complete=len(rows)==len(paths);out=record(complete);print(out['utc'],out['status'],len(rows),'of',len(paths),out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('file');ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--resume',action='store_true');main(ap.parse_args())
