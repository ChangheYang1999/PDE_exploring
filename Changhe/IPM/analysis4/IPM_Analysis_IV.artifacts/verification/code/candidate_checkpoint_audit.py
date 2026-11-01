"""Independent exact-dyadic audit of the pure Candidate007 checkpoint."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,gzip,io,json,pickle,sys,time,shutil,subprocess
sys.dont_write_bytecode=True
from flint import arb,fmpq,ctx
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('--checkpoint',default='../a4-num/ckpt/c007_p2048.pkl');ap.add_argument('--freeze',action='store_true');a=ap.parse_args()
start=time.monotonic();now=datetime.now(timezone.utc);ctx.prec=2304
assert shutil.disk_usage('.').free>20*10**9
path=Path(a.checkpoint);raw=path.read_bytes();digest=sha256(raw).hexdigest();state=pickle.loads(raw)
N=max(state['f']);assert state['ring']=='arb' and state['prec']==2048
root=Path('research/91_candidate_checkpoint_audit/verification')/('N'+str(N)+'_'+now.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
if a.freeze:
 frozen=root/'input_checkpoint.pkl.gz'
 buffer=io.BytesIO()
 with gzip.GzipFile(fileobj=buffer,mode='wb',compresslevel=1,filename='input_checkpoint.pkl') as f:f.write(raw)
 compressed=buffer.getvalue();buffer.close()
 used=int(subprocess.run(['du','-s','-B1','.'],capture_output=True,text=True,check=True).stdout.split()[0])
 assert used+len(compressed)<2_985_000_000,('lane disk limit reserve',used,len(compressed))
 frozen.write_bytes(compressed);del compressed
 input_path=frozen
else:input_path=path
result=dict(checked_at_utc=now.isoformat(timespec='seconds'),input_path=str(input_path),original_checkpoint_path=str(path),checkpoint_sha256=digest,checkpoint_bytes=len(raw),maximum_order=N,precision_bits=2304,source_precision_bits=2048)
del raw
text=lambda x:x.str(40,radius=True)
def endpoint_q(x):
 m,e=x.man_exp();m=fmpq(int(m));e=int(e)
 return m*2**e if e>=0 else m/fmpq(2**(-e))
def contains_exact_q(x,q):return endpoint_q(x.lower())<=q<=endpoint_q(x.upper())
profile_path=Path('research/02_candidate007/data/leading_exact.json');profile_raw=profile_path.read_bytes();profile=json.loads(profile_raw)
cq=fmpq(profile['c']);dq=fmpq(profile['delta']);c=arb(cq);delta=arb(dq)
assert state['delta_exact']==str(dq)
for key,q in [('c_l_pack',cq),('delta_pack',dq)]:assert contains_exact_q(arb(*unpack(state[key])),q)
for j,packed in enumerate(state['f'][1]):assert contains_exact_q(arb(*unpack(packed)),fmpq(profile['density'].get(str(2*j+1),'0')))
assert len(state['f'][1])==10
result.update(exact_parameter_and_leading_profile_checks=12,leading_profile_path=str(profile_path),leading_profile_sha256=sha256(profile_raw).hexdigest(),c_exact=str(cq),delta_exact=str(dq),fields={})
fields={};L10=arb(10).log();full_max=arb(0);full_location=None
for field in ['f','g']:
 fields[field]={};maxrel=arb(0);maxlocation=None;uncertain=0;count=0;rows=[]
 for n,packed in sorted(state[field].items()):
  vals=[];S=arb(0);T=arb(0);orderrel=arb(0);orderloc=None;orderuncertain=0
  for j,z in enumerate(packed):
   mid,rad=unpack(z);vals.append(arb(mid,rad));S+=abs(mid);T+=rad;count+=1
   if mid!=0:
    rel=rad/abs(mid)
    if rel>orderrel:orderrel,orderloc=rel,j
    if rel>maxrel:maxrel,maxlocation=rel,[n,j]
   elif rad!=0:uncertain+=1;orderuncertain+=1
  norm=sum(map(abs,vals),arb(0));l2=sum((v*v for v in vals),arb(0)).sqrt()
  assert norm>0 and l2>0
  lognorm=norm.log()/L10;logl2=l2.log()/L10
  row=dict(n=n,coefficient_count=len(vals),maximum_individual_relative_radius=text(orderrel),maximum_location=orderloc,uncertain_zero_midpoints=orderuncertain,
   all_coefficients_resolved=not orderuncertain and bool(orderrel<1),l1_norm=text(norm),log10_l1_norm=text(lognorm),l1_root=text((norm.log()/n).exp()),
   log10_l2_norm=text(logl2),l2_root=text((l2.log()/n).exp()),wiener_relative_radius=text(T/S))
  if field=='f':
   metadata=state['stats'].get(n,{})
   row['reported_log10_l1_difference']=abs(float(lognorm.mid())-metadata['log10_l1']) if 'log10_l1' in metadata else None
   row['reported_log10_l2_difference']=abs(float(logl2.mid())-metadata['log10_l2']) if 'log10_l2' in metadata else None
  rows.append(row);fields[field][n]=vals
  if n%100==0:print(json.dumps(dict(stage='decode',field=field,n=n,elapsed_s=time.monotonic()-start)),flush=True)
 result['fields'][field]=dict(coefficient_count=count,maximum_individual_relative_radius=text(maxrel),maximum_location=maxlocation,uncertain_zero_midpoints=uncertain,
  all_coefficients_resolved=not uncertain and bool(maxrel<1),rows=rows)
 if maxrel>full_max:full_max,full_location=maxrel,[field,*maxlocation]
# Differentiate the elliptic equation, rather than reproducing the inverse routine.
poisson=[];total=0;canonical=0
for n in range(1,N+1):
 F=fields['f'][n];G=fields['g'][n];P=2-n*delta;Pq=2-n*dq
 assert G[0].is_zero();canonical+=1
 assert len(F)<=10*n and len(G)<=10*n+1
 residual=arb(0);baseline=arb(0);fail=[];mind=None
 for j in range(1,max(len(F)+1,len(G))):
  m=2*j;den=fmpq(m*m)-Pq*Pq;assert den!=0
  if mind is None or abs(den)<mind:mind=abs(den)
  lhs=(m*m-P*P)*(G[j] if j<len(G) else arb(0))
  rhs=((P-m)*(F[j-1] if j-1<len(F) else arb(0))+(P+m)*(F[j] if j<len(F) else arb(0)))/2
  r=lhs-rhs;total+=1;residual+=abs(r);baseline+=abs(lhs)+abs(rhs)
  if not r.contains(0):fail.append(j)
 assert not fail,(n,fail[:5])
 poisson.append(dict(n=n,checked_coefficients=max(len(F),len(G)-1),failure_count=0,relative_residual=text(residual/baseline) if baseline>0 else None,minimum_exact_absolute_denominator=str(mind)))
 if n%100==0:print(json.dumps(dict(stage='poisson',n=n,elapsed_s=time.monotonic()-start)),flush=True)
result.update(poisson_checked_coefficients=total,canonical_zero_modes=canonical,poisson_all_residuals_contain_zero=True,poisson_rows=poisson,
 scope='Finite coefficient precision, exact input inclusion and differential Poisson consistency. No convergence or nonlinear completeness is inferred.',actual_elapsed_s=time.monotonic()-start)
for name in ['candidate_checkpoint_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),**{k:v for k,v in result.items() if k not in ['fields','poisson_rows']},brief={field:{k:v for k,v in rec.items() if k!='rows'} for field,rec in result['fields'].items()})),flush=True)
for field in ['f','g']:
 for row in result['fields'][field]['rows']:
  if row['n'] in [100,200,233,300,350,383,400,N]:print(json.dumps(dict(field=field,**row)),flush=True)
