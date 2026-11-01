"""Independent conditional diagnostics, with explicit reset-state provenance."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import gzip,json,pickle,sys,time,math,shutil,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,ctx
from stream_precision_audit import unpack
from certified_initial_majorants import pack
ROOT=Path('research/189_reset350_conditional_audit')

def main():
 start=time.monotonic();ctx.prec=768;zero=arb(0);lg=arb(10).log();text=lambda v:v.str(40,radius=True)
 source=Path('../a4-num/ckpt/log_sin1_c3_N350.pkl');raw=source.read_bytes();digest=sha256(raw).hexdigest();size=len(raw);state=pickle.loads(raw);del raw
 assert (state['A'],state['B'],state['ring'],state['prec'])==('2','3','arb',512) and max(state['f'])==350
 selected={key:{n:state[key][n] for n in [348,349,350]} for key in ['f','g']}
 selected.update(A='2',B='3',ring='arb',prec=512,source_sha256=digest,scope='Conditional on loaded midpoint arrays through329; no inherited uncertainty included')
 raw=pickle.dumps(selected,protocol=4);compressed=gzip.compress(raw,compresslevel=6,mtime=0)
 used=sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file());assert used+len(compressed)<2990000000 and shutil.disk_usage('.').free>20000000000
 (ROOT/'verification/selected.pkl.gz').write_bytes(compressed)
 manifest=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),source=str(source),source_sha256=digest,source_bytes=size,selected_orders=[348,349,350],selected_raw_sha256=sha256(raw).hexdigest(),selected_raw_bytes=len(raw),archive_sha256=sha256(compressed).hexdigest(),archive_bytes=len(compressed),source_maximum_order=350)
 (ROOT/'verification/input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');del selected,raw,compressed
 peerpath=Path('../a4-num/notes/stream_ratio_modes_341_350.json');peerraw=peerpath.read_bytes();peer=json.loads(peerraw)['orders'];(ROOT/'sources/peer_mode_shares.json').write_bytes(peerraw)
 for name in ['tprofile_350.txt','bands_350.txt']:(ROOT/'sources'/name).write_bytes(Path('../a4-num/notes',name).read_bytes())
 rows=[];norms={};poisson=canonical=count=comparisons=0;decoded350=None
 for n in range(324,351):
  decoded={};row=dict(n=n,fields={})
  for field in ['f','g']:
   cols=[[arb(*unpack(v)) for v in col] for col in state[field][n]];decoded[field]=cols;column=[sum(map(abs,c),zero) for c in cols];total=sum(column,zero);norms[field,n]=total;count+=sum(map(len,cols))
   facts=[arb(math.factorial(q))*v for q,v in enumerate(column)];win=max(range(len(facts)),key=lambda q:float((facts[q]/column[0]).mid()))
   assert all(facts[win]>v for q,v in enumerate(facts) if q!=win)
   row['fields'][field]=dict(norm=pack(total),log10_norm=text(total.log()/lg),relative_radius=text(total.rad()/abs(total.mid())),degree=len(cols)-1,factorial_maximizer=win,factorial_log10_ratio=text((facts[win]/column[0]).log()/lg))
  ratio=norms['g',n]/norms['f',n];row['log10_N_over_M']=text(ratio.log()/lg)
  if n>=348:
   FF,GG=decoded['f'],decoded['g'];P=arb(2)-arb(2*n)/3
   def get(A,q,j):return A[q][j] if 0<=q<len(A) and 0<=j<len(A[q]) else zero
   local=0;res=zero;scale=zero
   for q in range(max(len(FF),len(GG))):
    assert get(GG,q,0).is_zero()
    for j in range(1,max(max(map(len,FF)),max(map(len,GG)))+1):
     lhs=(4*j*j-P*P)*get(GG,q,j)-2*P*(q+1)*get(GG,q+1,j)-(q+1)*(q+2)*get(GG,q+2,j)
     rhs=((P-2*j)*get(FF,q,j-1)+(q+1)*get(FF,q+1,j-1)+(P+2*j)*get(FF,q,j)+(q+1)*get(FF,q+1,j))/2
     assert (lhs-rhs).contains(0),(n,q,j);res+=abs(lhs-rhs);scale+=abs(lhs)+abs(rhs);local+=1
     if q==0 and 3*(2+2*j)==2*n:assert get(GG,0,j).is_zero();canonical+=1
   poisson+=local;row['poisson']=dict(coefficients=local,relative_residual=text(res/scale))
  if n>=341:
   P3=6-2*n;shift={};Gcol={};Fnear=zero
   for q,col in enumerate(decoded['g']):
    Gcol[q]=sum(map(abs,col),zero)
    for j,v in enumerate(col):
     if not j:continue
     distance=min(abs(P3+6*j),abs(P3-6*j));key=str(F(distance,3)) if distance<=12 else 'far';shift[key]=shift.get(key,zero)+abs(v)
   for col in decoded['f']:
    for j,v in enumerate(col):
     if abs(abs(P3)-3*(2*j+1))<=4:Fnear+=abs(v)
   shares={k:v/norms['g',n] for k,v in shift.items()};old=peer[str(n)]
   def check(v,w,tol='5e-12'):
    nonlocal comparisons
    assert v.overlaps(arb(str(w),tol)),(n,text(v),w);comparisons+=1
   check(norms['f',n].log()/lg,old['log10M']);check(norms['g',n].log()/lg,old['log10N']);check(ratio.log()/lg,old['log10ratio'])
   for k,v in old['stream_share_by_shift'].items():check(shares[k],v,'5e-15')
   check(Gcol[0]/norms['g',n],old['stream_col0_share'],'5e-15');check(Fnear/norms['f',n],old['density_near_share'],'5e-15')
   row['shares']=dict(stream_by_shift={k:text(v) for k,v in shares.items()},stream_column0=text(Gcol[0]/norms['g',n]),density_near=text(Fnear/norms['f',n]))
  rows.append(row)
  if n==350:decoded350=decoded
  if n>=348:print(json.dumps(dict(n=n,poisson=row['poisson'],log10_N_over_M=row['log10_N_over_M'])),flush=True)
 # 27-order slopes are computed from the current stored arrays. Earlier rows
 # are loaded midpoint values and later rows are their conditional continuation.
 center=337;den=sum((n-center)**2 for n in range(324,351));slopes={f:text(sum(((n-center)*norms[f,n].log()/lg for n in range(324,351)),zero)/den) for f in ['f','g']}
 evaluations=[]
 for t in [20,-20,40,-40]:
  row=dict(t=t,fields={})
  for field,cols in decoded350.items():
   vals=[];M=max(map(len,cols));column=[sum(map(abs,c),zero) for c in cols]
   for j in range(M):
    acc=zero
    for col in reversed(cols):acc=acc*t+(col[j] if j<len(col) else zero)
    vals.append(acc)
   norm=sum(map(abs,vals),zero);absolute=sum((v*abs(t)**q for q,v in enumerate(column)),zero)
   row['fields'][field]=dict(norm=pack(norm),log10_norm=text(norm.log()/lg),log10_radius_sum=text(sum((v.rad() for v in vals),zero).log()/lg),cancellation_decades=text((absolute/norm).log()/lg))
  evaluations.append(row)
 bands=[]
 for q in [0,1,10,20,40,60,74]:
  row=dict(q=q,fields={})
  for field,offset in [('f',4),('g',2)]:
   col=decoded350[field][q];total=sum(map(abs,col),zero);parts=[zero,zero,zero]
   for j,v in enumerate(col):
    distance=abs(3*(2*j+offset)-700)
    bucket=(0 if distance<=6 else 2) if q==0 else (0 if 4*distance<=3*q else 1 if distance<=3*q else 2)
    parts[bucket]+=abs(v)
   row['fields'][field]=[text(v/total) for v in parts]
  bands.append(row)
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,scope='Conditional finite arithmetic for the loaded midpoint continuation. No inherited329 uncertainty or nonlinear high-order check.',source_sha256=digest,selected_manifest='input_manifest.json',bits=768,norm_coefficient_positions=count,poisson_coefficients=poisson,canonical_constants=canonical,peer_rounding_comparisons=comparisons,rows=rows,slopes_324_350=slopes,t_evaluations=evaluations,bands350=bands,actual_elapsed_s=time.monotonic()-start)
 (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
 for name in ['reset350_conditional_audit.py','stream_precision_audit.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
 print(json.dumps({k:v for k,v in result.items() if k not in ['rows','t_evaluations','bands350']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as e:
  d=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)])
  (ROOT/'verification/FAILURE.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d),flush=True);raise SystemExit(1)
