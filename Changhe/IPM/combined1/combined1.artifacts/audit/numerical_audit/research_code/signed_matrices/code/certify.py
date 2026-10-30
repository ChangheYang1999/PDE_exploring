"""Adaptive full-plane positivity for two explicitly specified signed matrices."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,json,sys,time
from flint import fmpq,arb,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/global_matrices/code'))
from cover import ranges,eigen,endpoints,checktree,add,ar,digest
BASE=ROOT/'research/signed_matrices'

def matrices(data,kind):
 fields={k:{(i,j):fmpq(v) for i,j,v in rows} for k,rows in data['polynomials'].items()}
 out={(label,j):{} for label in ['a','b','q'] for j in range(7)}
 constant=fmpq(2,25) if kind=='L2' else fmpq(1,10)
 for label in ['a','b']:out[label,0]={(0,0):constant}
 terms=([('a','chi22',-1),('a','chi04',-1),('q','chi31',fmpq(1,2)),('q','chi13',fmpq(1,2))]
        if kind=='L2' else [('a','chi04',-1),('b','chi22',-1),('q','chi13',1)])
 for j in range(6):
  for label,key,factor in terms:out[label,j+1]=add(out[label,j+1],fields[f'{key}_{j}'],factor)
 return out

def run(kind,bits,seconds):
 ctx.prec=bits;start=time.monotonic()
 datafile=ROOT/'research/global_matrices/data/independent_d2_polynomials.json.gz'
 with gzip.open(datafile,'rt') as f:data=json.load(f)
 raw=matrices(data,kind);nt=max(i for A in raw.values() for i,j in A);nz=max(j for A in raw.values() for i,j in A)
 P={}
 for key,A in raw.items():
  M=arb_mat(nt+1,nz+1)
  for (i,j),v in A.items():M[i,j]=ar(v)
  P[key]=M
 codehash=digest(__file__);sourcehash=digest(datafile);coverfile=ROOT/'research/global_matrices/data/nb_d2_exact.M1.correlated.json'
 target=BASE/f'verification/d2_{kind}_{bits}.json'
 if target.exists():
  state=json.loads(target.read_text());assert state['code_sha256']==codehash and state['source_sha256']==sourcehash
  queue=state['pending'];accepted=state['accepted'];failures=state['inconclusive'];elapsed=state['total_elapsed_seconds']
 else:
  old=json.loads(coverfile.read_text());queue=[r['path'] for r in old['accepted']];accepted=[];failures=[];elapsed=0
 checktree(set(queue+[r['path'] for r in accepted]))
 delta=fmpq(data['delta']);print('prepared',kind,nt,nz,'accepted',len(accepted),'pending',len(queue),flush=True)
 count=0
 while queue and time.monotonic()-start<seconds:
  path=queue.pop(0);a,b,c,d=endpoints(path)
  plain,improved=ranges(P,nt,nz,a,b,c,d,delta);bound=eigen(plain,c,d)
  if improved is not None:bound=bound.max(eigen(improved,c,d))
  if bound>=0:
   accepted.append({'path':path,'bound':bound.str(70),'pass':True})
  else:
   failures.append({'path':path,'bound':bound.str(30)})
   if len(path)>=36:
    queue.insert(0,path);print('depth limit; no conclusion',path,flush=True);break
   children=('t','T') if b-a>=(d-c)/2 else ('z','Z')
   queue.extend([path+x for x in children])
  count+=1
  leaves=queue+[r['path'] for r in accepted];assert len(set(leaves))==len(leaves);checktree(set(leaves))
  state={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'d2','kind':kind,
         'target':'A+(2/25)I>=0' if kind=='L2' else 'I-sym Du+A >=(9/10)I',
         'precision_bits':bits,'source_sha256':sourcehash,'code_sha256':codehash,'initial_cover_sha256':digest(coverfile),
         'enclosure_code_sha256':digest(ROOT/'research/global_matrices/code/cover.py'),
         'accepted':accepted,'pending':queue,'inconclusive':failures,'complete_partition':True,'all_pass':not queue,
         'total_elapsed_seconds':elapsed+time.monotonic()-start}
  if not queue and kind=='L2':
   kfile=ROOT/'research/background_sobolev/verification/d2.json';kd=json.loads(kfile.read_text())
   margin=ar(fmpq(data['cl']))+1-ar(fmpq(2,25))-arb(kd['gradient_identity_conditional_HS_upper'])
   state['signed_rate_lower']=margin.str(70);state['signed_rate_at_least_two']=bool(margin>=2);state['HS_source_sha256']=digest(kfile)
  temp=target.with_suffix('.pending');temp.write_text(json.dumps(state,indent=2)+'\n');temp.replace(target)
  print('cell',count,path,'pass',bool(bound>=0),'bound',bound.str(10),'pending',len(queue),'seconds',time.monotonic()-start,flush=True)
 print('stage done accepted',len(accepted),'pending',len(queue),'stage seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('kind',choices=['L2','M1']);p.add_argument('--bits',type=int,default=768);p.add_argument('--seconds',type=int,default=460)
 a=p.parse_args();run(a.kind,a.bits,a.seconds)
