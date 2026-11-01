"""Independent exact inputs, low-order Cartesian recursion and interval profile diagnostics."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,pickle,sys,time
sys.dont_write_bytecode=True
from flint import arb,fmpq,ctx
from stream_precision_audit import unpack
from laurent_log_audit import L,parse,Q,Poly
ctx.prec=640
start=time.monotonic();stamp=datetime.now(timezone.utc)
root=Path('research/96_profile_family_audit/verification')/stamp.strftime('%Y%m%dT%H%M%SZ');root.mkdir();(root/'sources').mkdir()
basepath=Path('research/02_candidate007/data/leading_exact.json');raw=basepath.read_bytes();base=json.loads(raw);cq=fmpq(base['c']);dq=fmpq(base['delta']);gamma=1-dq
cases=[]
for K in [1,2,3,5,9]:
 coeff=[fmpq(1)]
 for k in range(1,K+1):coeff.append(coeff[-1]*(2*k-1-gamma)/(2*k+1+gamma))
 cases.append((f'shear_K{K}_c007_p512',coeff,dict(family='shear',K=K)))
for idx,mul in [(1,'1/2'),(1,'3/4'),(1,'5/4'),(1,'3/2'),(2,'1/2'),(2,'3/2')]:
 coeff=[fmpq(base['density'].get(str(2*k+1),'0')) for k in range(10)];coeff[idx]*=fmpq(mul)
 cases.append((f'pert007_a{idx}x{mul.replace("/","_")}_p512',coeff,dict(family='perturbation',index=idx,factor=mul)))
text=lambda x:x.str(32,radius=True)
def endpoint(x):
 m,e=x.man_exp();return fmpq(int(m))*fmpq(2)**int(e)
def included(x,q):return endpoint(x.lower())<=q<=endpoint(x.upper())
def exact_small(coeff,N=4):
 F={};G={};XF={};YF={};XG={};YG={}
 for n in range(1,N+1):
  q=1-n*dq
  if n==1:A=parse(q,{str(2*k+1):[str(v)] for k,v in enumerate(coeff) if v})
  else:
   A=L(q,0,[])
   for i in range(1,n):A=A+XG[i]*YF[n-i]-YG[i]*XF[n-i]
   A=A.scale(1/((n-1)*(cq-1)))
  F[n]=A;XF[n]=A.X();YF[n]=A.Y();H=XF[n];P=q+1;vals=[]
  for idx,v in enumerate(H.a[0].coeffs()):
   m=idx-H.M;den=m*m-P*P
   assert den!=0
   vals.append(v/den)
  B=L(P,H.M,[Poly(vals)]);G[n]=B;XG[n]=B.X();YG[n]=B.Y()
 return F,G
summary=dict(checked_at_utc=stamp.isoformat(timespec='seconds'),precision_bits=640,source_precision_bits=512,leading_profile_sha256=sha256(raw).hexdigest(),cases=[])
for tag,coeff,meta in cases:
 t0=time.monotonic();path=Path('../a4-num/ckpt')/(tag+'.pkl');raw=path.read_bytes();digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw
 assert state['ring']=='arb' and state['prec']==512 and state['delta_exact']==str(dq)
 for key,q in [('c_l_pack',cq),('delta_pack',dq)]:assert included(arb(*unpack(state[key])),q)
 assert len(state['f'][1])==len(coeff)
 for packed,q in zip(state['f'][1],coeff):assert included(arb(*unpack(packed)),q)
 if meta['family']=='shear':
  peerpath=Path('../a4-num/notes')/f'shear_family_K{meta["K"]}.json';peerc=[fmpq(v) for v in json.loads(peerpath.read_text())];assert peerc==coeff
 exact=exact_small(coeff);exact_count=0;low={}
 for field,E in zip(['f','g'],exact):
  low[field]={}
  for n,A in E.items():
   vals={};parity=1 if field=='f' else 0
   for j,z in enumerate(state[field][n]):
    m=2*j+parity;v=2*A.a[0][A.M+m] if A.M+m>=0 else fmpq(0)
    assert included(arb(*unpack(z)),v),(tag,field,n,j)
    exact_count+=1
    if v:vals[str(m)]=str(v)
   low[field][str(n)]=vals
 rows=[];total_coeff=0;poisson_count=0;maxrel=arb(0);maxrel_loc=None;zero_uncertain=0;containing_zero=0;norms={};maxres=arb(0)
 N=max(state['f']);L10=arb(10).log()
 for n in range(1,N+1):
  decoded={};row=dict(n=n)
  for field in ['f','g']:
   vals=[];rad=arb(0);midnorm=arb(0)
   for j,z in enumerate(state[field][n]):
    m,r=unpack(z);v=arb(m,r);vals.append(v);total_coeff+=1;rad+=r;midnorm+=abs(m)
    if r != 0 and v.contains(0):containing_zero+=1
    if m != 0:
     rel=r/abs(m)
     if rel>maxrel:maxrel,maxrel_loc=rel,[field,n,j]
    elif r != 0:zero_uncertain+=1
   decoded[field]=vals;norm=sum(map(abs,vals),arb(0));l2=sum((v*v for v in vals),arb(0)).sqrt();assert norm>0 and l2>0
   row[field]=dict(log10_l1=text(norm.log()/L10),l1_root=text((norm.log()/n).exp()),log10_l2=text(l2.log()/L10),l2_root=text((l2.log()/n).exp()),relative_norm_radius=text(rad/midnorm))
   if field=='f':norms[n]=l2
  F,G=decoded['f'],decoded['g'];Pq=2-n*dq;P=arb(Pq);res=arb(0);dennorm=arb(0);assert G[0].is_zero()
  for j in range(1,max(len(F)+1,len(G))):
   m=2*j;assert m*m-Pq*Pq!=0
   lhs=(m*m-P*P)*(G[j] if j<len(G) else arb(0));rhs=((P-m)*(F[j-1] if j-1<len(F) else arb(0))+(P+m)*(F[j] if j<len(F) else arb(0)))/2
   e=lhs-rhs;assert e.contains(0),(tag,n,j);poisson_count+=1;res+=abs(e);dennorm+=abs(lhs)+abs(rhs)
  rel=res/dennorm if dennorm>0 else arb(0)
  if rel.upper()>maxres:maxres=rel.upper()
  rows.append(row)
 selected={field:{str(n):state[field][n] for n in [1,2,3,4,100,N-10,N] if n in state[field]} for field in ['f','g']}
 (root/(tag+'_selected.json')).write_text(json.dumps(dict(checkpoint_sha256=digest,**selected))+'\n')
 (root/(tag+'_exact_low.json')).write_text(json.dumps(low)+'\n')
 result=dict(tag=tag,**meta,checkpoint_path=str(path),checkpoint_sha256=digest,maximum_order=N,exact_input_coefficients=[str(v) for v in coeff],exact_low_order_inclusions=exact_count,coefficient_count=total_coeff,maximum_individual_relative_radius=text(maxrel),maximum_location=maxrel_loc,uncertain_zero_midpoints=zero_uncertain,nonexact_balls_containing_zero=containing_zero,poisson_coefficient_checks=poisson_count,maximum_relative_poisson_residual=text(maxres),smoothed_ten_step_l2_ratio=text(((norms[N]/norms[N-10]).log()/10).exp()),rows=rows,actual_elapsed_s=time.monotonic()-t0)
 (root/(tag+'.json')).write_text(json.dumps(result,indent=2)+'\n');summary['cases'].append({k:v for k,v in result.items() if k not in ['rows','exact_input_coefficients']});summary['actual_elapsed_s']=time.monotonic()-start
 (root/'checks.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(dict(tag=tag,N=N,low_checks=exact_count,coefficient_count=total_coeff,poisson_checks=poisson_count,uncertain_zero_midpoints=zero_uncertain,last=rows[-1],smooth=result['smoothed_ten_step_l2_ratio'],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
for name in ['profile_family_audit.py','stream_precision_audit.py','laurent_log_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
summary['complete']=True;summary['actual_elapsed_s']=time.monotonic()-start;(root/'checks.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(dict(output_directory=str(root),complete=True,actual_elapsed_s=summary['actual_elapsed_s'])),flush=True)
