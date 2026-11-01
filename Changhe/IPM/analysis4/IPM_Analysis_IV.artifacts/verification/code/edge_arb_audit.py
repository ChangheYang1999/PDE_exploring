"""Independent exact-input, precision, norm and Poisson checks for edge runs."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from flint import arb,fmpq,ctx
from stream_precision_audit import unpack
import argparse,gzip,json,pickle,time,math,sys,shutil,subprocess
sys.dont_write_bytecode=True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('K',type=int,choices=[1,3]);ap.add_argument('--max-order',type=int,default=300);a=ap.parse_args()
 start=time.monotonic();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 header_path=Path(f'../a4-num/logs/log23_edge{a.K}_p1024.jsonl')
 header_text=header_path.open().readline();header_data=json.loads(header_text)
 assert header_data['edge_only_min_ij_le']==a.K and header_data['delta']=='2/3' and header_data['prec']==1024
 root=Path('research/102_edge_recurrence_reference/verification')/f'arb_edge{a.K}_{stamp}';root.mkdir();(root/'sources').mkdir()
 src=Path(f'../a4-num/ckpt/log23_edge{a.K}_p1024.pkl');raw=src.read_bytes();digest=sha256(raw).hexdigest();size=len(raw);state=pickle.loads(raw)
 assert (state['ring'],state['prec'],state['A'],state['B'])==('arb',1024,'2','3')
 N=min(a.max_order,max(state['f']));ctx.prec=1152
 frozen=root/'input_checkpoint.pkl.gz'
 assert shutil.disk_usage('.').free>20*10**9
 compressed=gzip.compress(raw,compresslevel=3,mtime=0)
 used=int(subprocess.run(['du','-s','-B1','.'],capture_output=True,text=True,check=True).stdout.split()[0])
 assert used+len(compressed)<2_985_000_000,('lane disk reserve',used,len(compressed))
 frozen.write_bytes(compressed)
 del compressed
 del raw
 refp=Path('research/102_edge_recurrence_reference/verification/exact_reference.json');ref=json.loads(refp.read_text())['variants'][str(a.K)]['rows'];refs={r['n']:r for r in ref}
 zero=arb(0);l10=arb(10).log();text=lambda x:x.str(34,radius=True)
 counts={'balls':0,'exact_positions':0,'poisson_coefficients':0,'resonant_constants':0};rows=[];maxrel={'f':zero,'g':zero};loc={};uncertain={'f':0,'g':0};poisson_fail=[];exact_fail=[]
 def get(cols,k,j):return cols[k][j] if 0<=k<len(cols) and 0<=j<len(cols[k]) else zero
 for n in range(1,N+1):
  fields={};norms={};row={'n':n};P=arb(2)-arb(2*n)/3
  for field,label in [('f','density'),('g','stream')]:
   cols=[];cns=[];ore=zero;unz=0
   for k,packedcol in enumerate(state[field][n]):
    col=[]
    for j,v in enumerate(packedcol):
     mid,rad=unpack(v);x=arb(mid,rad);col.append(x);counts['balls']+=1
     if mid!=0:
      rel=rad/abs(mid)
      if rel>ore:ore=rel
      if rel>maxrel[field]:maxrel[field]=rel;loc[field]=[n,k,j]
     elif rad!=0:unz+=1
    cols.append(col);cns.append(sum(map(abs,col),zero))
   uncertain[field]+=unz;norm=sum(cns,zero);norms[field]=norm;fields[field]=cols
   vals=[(arb(math.factorial(k)).log()/l10+cn.log()/l10-cns[0].log()/l10,k) for k,cn in enumerate(cns) if k and cn>0]
   winner=max(vals,key=lambda v:float(v[0].mid())) if vals else None
   row[label]={'degree':max(k for k,col in enumerate(cols) if any(x!=0 for x in col)),'log10_norm':text(norm.log()/l10),'root':text((norm.log()/n).exp()),'maximum_individual_relative_radius':text(ore),'uncertain_zeros':unz,'all_coefficients_resolved':not unz and bool(ore<1),'column_log10_norms':[text(cn.log()/l10) if cn>0 else None for cn in cns]}
   if winner:
    win,k=winner;row[label].update(factorial_max=text(win),factorial_argmax=k,strict_max=all(bool(win>other) for other,j in vals if j!=k),all_nonconstant_factorial_columns_smaller=all(bool(other<0) for other,j in vals))
   if n in refs:
    exact={(int(k),int(m)):fmpq(v) for k,col in refs[n][label].items() for m,v in col.items()}
    keys=set(exact)|{(k,2*j+(field=='f')) for k,col in enumerate(cols) for j in range(len(col))}
    for k,m in keys:
     j=(m-(field=='f'))//2;x=get(cols,k,j);counts['exact_positions']+=1
     if not x.contains(exact.get((k,m),fmpq(0))):exact_fail.append([field,n,k,m])
  F,G=fields['f'],fields['g'];pc=0;pr=zero;scale=zero
  assert all(row[0]==0 for row in G)
  for k in range(max(len(F),len(G))):
   for j in range(1,max(max(map(len,F)),max(map(len,G)))+1):
    m=2*j
    lhs=(m*m-P*P)*get(G,k,j)-2*P*(k+1)*get(G,k+1,j)-(k+1)*(k+2)*get(G,k+2,j)
    rhs=((P-m)*get(F,k,j-1)+(k+1)*get(F,k+1,j-1)+(P+m)*get(F,k,j)+(k+1)*get(F,k+1,j))/2
    err=lhs-rhs;pc+=1;pr+=abs(err);scale+=abs(lhs)+abs(rhs)
    if not err.contains(0):poisson_fail.append([n,k,j,text(err)])
    if k==0 and 3*(2+m)==2*n:
     counts['resonant_constants']+=1
     assert get(G,0,j)==0
  counts['poisson_coefficients']+=pc;row.update(poisson_relative_residual=text(pr/scale),log10_N_over_M=text((norms['g']/norms['f']).log()/l10));rows.append(row)
  assert not exact_fail and not poisson_fail,(exact_fail[:3],poisson_fail[:3])
  if n%30==0 or n==N:print(json.dumps({'K':a.K,'n':n,'elapsed_s':time.monotonic()-start,'counts':counts}),flush=True)
 slopes={}
 for n in sorted({100,150,200,250,300,N}):
  if n>N or n<27:continue
  mid=n-13;den=sum((i-mid)**2 for i in range(n-26,n+1))
  slopes[n]={label:text(sum((arb(rows[i-1][label]['log10_norm'])*(i-mid) for i in range(n-26,n+1)),zero)/den) for label in ['density','stream']}
 result={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'K':a.K,'maximum_order':N,'source_maximum_order':max(state['f']),'source_path':str(src),'source_sha256':digest,'source_bytes':size,'frozen_checkpoint':str(frozen),'arithmetic':'1152-bit Arb from exact dyadic1024-bit source enclosures','counts':counts,'maximum_individual_relative_radius':{f:text(v) for f,v in maxrel.items()},'maximum_locations':loc,'uncertain_zeros':uncertain,'exact_failures':exact_fail,'poisson_failures':poisson_fail,'slopes_27':slopes,'rows':rows,'scope':'Finite precision, norm, exact low-order and all-order Poisson audit. High-order nonlinear convolution is separate. No all-order growth claim.','actual_elapsed_s':time.monotonic()-start}
 (root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
 hashes={}
 for name in ['edge_arb_audit.py','stream_precision_audit.py']:
  data=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(data);hashes[name]=sha256(data).hexdigest()
 for name in ['logff.py','ffcore.py']:
  data=Path('../a4-num/code',name).read_bytes();(root/'sources'/('peer_'+name+'.txt')).write_bytes(data);hashes['peer_'+name]=sha256(data).hexdigest()
 (root/'sources/run_header.json').write_text(header_text)
 (root/'MANIFEST.json').write_text(json.dumps({'created_at_utc':result['checked_at_utc'],'source_sha256':digest,'source_bytes':size,'checkpoint_gzip_sha256':sha256(frozen.read_bytes()).hexdigest(),'checks_sha256':sha256((root/'checks.json').read_bytes()).hexdigest(),'source_hashes':hashes},indent=2)+'\n')
 print(json.dumps({'output':str(root),**{k:v for k,v in result.items() if k!='rows'},'last_row':rows[-1]}),flush=True)
if __name__=='__main__':main()
