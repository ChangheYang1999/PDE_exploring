"""Direct interval norm audit; the source's diagnostic flag does not remove balls."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,pickle,gzip,sys,time,shutil,subprocess,math
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ctx.prec=640;start=time.monotonic();z=arb(0);l10=arb(10).log()
text=lambda v:v.str(36,radius=True)
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('research/138_post_tolerance_enclosures/verification')/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root.mkdir(exist_ok=True);(root/'sources').mkdir(exist_ok=True)
assert shutil.disk_usage('.').free>20*10**9
source=Path('../a4-num/ckpt/log_sin1_c3_p512.pkl');raw=source.read_bytes();digest=sha256(raw).hexdigest();rawsize=len(raw);state=pickle.loads(raw);del raw
assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512)
N=min(max(state['f']),340);assert N>=332 and N<=max(state['g'])
selected={key:{n:state[key][n] for n in range(331,N+1)} for key in ['f','g']}
selected.update(A='2',B='3',ring='arb',prec=512,original_checkpoint_sha256=digest)
sraw=pickle.dumps(selected,protocol=4);packed=gzip.compress(sraw,compresslevel=1,mtime=0)
used=int(subprocess.run(['du','-s','-B1','.'],capture_output=True,text=True,check=True).stdout.split()[0]);existing=(root/'selected_checkpoint.pkl.gz');credit=existing.stat().st_size if existing.exists() else 0;assert used+len(packed)-credit<2_980_000_000
archive=root/'selected_checkpoint.pkl.gz'
if archive.exists():assert archive.read_bytes()==packed,'Live source changed; use the retained archive rather than overwriting it'
else:archive.write_bytes(packed)
assert gzip.decompress(archive.read_bytes())==sraw
manifest=dict(frozen_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source_path=str(source),source_maximum_order=max(state['f']),source_raw_sha256=digest,source_raw_bytes=rawsize,selected_orders=list(range(331,N+1)),selected_raw_bytes=len(sraw),selected_raw_sha256=sha256(sraw).hexdigest(),archive_path=str(archive),archive_bytes=len(packed),archive_sha256=sha256(packed).hexdigest())
(root/'input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');del selected,sraw,packed
for name in ['logff.py','ffcore.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('../a4-num/code',name).read_bytes())
(root/'sources/num_note_1031.md').write_text(Path('../a4-num/NOTES_FOR_TEAM.md').read_text().split('## 2026-10-31T10:01Z')[0])
rows=[];norms={};counts=0;poisson=0;canonical=0
for n in range(300,N+1):
 row=dict(n=n,fields={});decoded={}
 for field in ['f','g']:
  cols=[[arb(*unpack(v)) for v in col] for col in state[field][n]];decoded[field]=cols
  column_norms=[sum(map(abs,col),z) for col in cols];total=sum(column_norms,z);assert total>0
  counts+=sum(map(len,cols));norms[field,n]=total
  unresolved=0;maxrel=z;exactzero=0;nonzero=0
  if n>=331:
   for col in cols:
    for v in col:
     if v.is_zero():exactzero+=1;continue
     nonzero+=1
     if v.contains(0):unresolved+=1
     if v.mid()!=0:
      rel=v.rad()/abs(v.mid())
      if rel>maxrel:maxrel=rel
  facts=[arb(math.factorial(q))*cn for q,cn in enumerate(column_norms)]
  win=max(range(len(facts)),key=lambda q:float((facts[q]/column_norms[0]).mid()))
  row['fields'][field]=dict(norm=text(total),log10_norm=text(total.log()/l10),norm_relative_radius=text(total.rad()/abs(total.mid())),degree=len(cols)-1,coefficient_count=sum(map(len,cols)),individual_precision_checked=n>=331,unresolved_individuals=unresolved if n>=331 else None,exact_zero_individuals=exactzero if n>=331 else None,nonzero_ball_positions=nonzero if n>=331 else None,max_individual_relative_radius=text(maxrel) if n>=331 else None,factorial_maximizer=win,factorial_maximizer_strict=all(bool(facts[win]>v) for j,v in enumerate(facts) if j!=win),factorial_maximum_log10_ratio=text((facts[win]/column_norms[0]).log()/l10))
 ratio=norms['g',n]/norms['f',n];row.update(N_over_M=text(ratio),log10_N_over_M=text(ratio.log()/l10),ratio_above_one=bool(ratio>1),ratio_above_034=bool(ratio>arb(34)/100))
 if n>=331:
  F=decoded['f'];G=decoded['g'];P=arb(2)-arb(2*n)/3
  def get(A,q,j):return A[q][j] if 0<=q<len(A) and 0<=j<len(A[q]) else z
  pc=cc=0;resnorm=z;lhsnorm=z;rhsnorm=z
  for col in G:assert col[0].is_zero()
  for q in range(max(len(F),len(G))):
   for j in range(1,max(max(map(len,F)),max(map(len,G)))+1):
    m=2*j;lhs=(m*m-P*P)*get(G,q,j)-2*P*(q+1)*get(G,q+1,j)-(q+1)*(q+2)*get(G,q+2,j)
    rhs=((P-m)*get(F,q,j-1)+(q+1)*get(F,q+1,j-1)+(P+m)*get(F,q,j)+(q+1)*get(F,q+1,j))/2
    err=lhs-rhs;assert err.contains(0),(n,q,j,text(err));pc+=1;resnorm+=abs(err);lhsnorm+=abs(lhs);rhsnorm+=abs(rhs)
    if q==0 and 3*(2+m)==2*n:assert get(G,0,j).is_zero();cc+=1
  poisson+=pc;canonical+=cc;row['poisson']=dict(checked_coefficients=pc,canonical_constants=cc,all_contain_zero=True,relative_residual=text(resnorm/(lhsnorm+rhsnorm)))
 rows.append(row)
 if n>=331:print(json.dumps(row),flush=True)
slopes=[]
for end in [326,332,338,340]:
 if end>N:continue
 begin=end-26;center=(begin+end)//2;den=sum((n-center)**2 for n in range(begin,end+1));record=dict(start=begin,end=end)
 for field in ['f','g']:
  value=sum(((n-center)*norms[field,n].log()/l10 for n in range(begin,end+1)),z)/den
  record[field+'_slope']=text(value)
 slopes.append(record)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),input_manifest='input_manifest.json',maximum_order=N,all_checks_pass=True,arithmetic_bits=640,norm_coefficient_count=counts,poisson_coefficient_count=poisson,canonical_constant_count=canonical,rows=rows,slopes=slopes,actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['post_tolerance_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()};(root/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(dict(output=str(root),maximum_order=N,all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'],poisson_coefficient_count=poisson,slopes=slopes)),flush=True)
