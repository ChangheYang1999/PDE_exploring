"""Interval Fourier mass partitions by exact Poisson shift at orders300..320."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from flint import arb,ctx
from stream_precision_audit import unpack
import gzip,json,pickle,time,sys
sys.dont_write_bytecode=True
start=time.monotonic();ctx.prec=640
path=Path('research/82_weighted_loss_criterion/update_N320_20261031T083718Z/verification/input_checkpoint.pkl.gz')
raw=gzip.decompress(path.read_bytes());digest=sha256(raw).hexdigest()
assert digest=='fd3f2e353f1901b50426a25177e238be3854c3008e3a3add4458eb94faca1b90'
state=pickle.loads(raw);del raw
peerpath=Path('../a4-num/notes/stream_ratio_modes_300_320.json');peerraw=peerpath.read_bytes();peer=json.loads(peerraw)['orders']
root=Path('research/75_diagonal_mass/verification')/('mode_shares_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
zero=arb(0);l10=arb(10).log();text=lambda v:v.str(34,radius=True)
rows=[];counts=0;comparisons=0;norms={};near={}
def check(value,reported,eps='8e-13'):
 global comparisons
 assert value.overlaps(arb(str(reported),eps)),(text(value),reported)
 comparisons+=1
for n in range(300,321):
 byshift={};bycol={};nearcol={};M=zero;Fnear=zero;Fcols={};P3=6-2*n
 for q,col in enumerate(state['g'][n]):
  for j,packed in enumerate(col):
   v=abs(arb(*unpack(packed)));counts+=1
   if not j:assert v==0;continue
   distance=min(abs(P3+6*j),abs(P3-6*j))
   key=str(Fraction(distance,3)) if distance<=12 else 'far'
   byshift[key]=byshift.get(key,zero)+v;bycol[q]=bycol.get(q,zero)+v
   if distance<=2:nearcol[q]=nearcol.get(q,zero)+v
 N=sum(byshift.values(),zero);norms[n]=N;near[n]=sum(nearcol.values(),zero)
 assert (N-sum(bycol.values(),zero)).contains(0)
 for q,col in enumerate(state['f'][n]):
  total=zero
  for j,packed in enumerate(col):
   v=abs(arb(*unpack(packed)));counts+=1;total+=v
   if abs(abs(P3)-3*(2*j+1))<=4:Fnear+=v
  Fcols[q]=total;M+=total
 shares={key:value/N for key,value in byshift.items()}
 assert sum(shares.values(),zero).contains(1)
 old=peer[str(n)];check(N.log()/l10,old['log10N']);check(M.log()/l10,old['log10M']);check((N/M).log()/l10,old['log10ratio'])
 for key,reported in old['stream_share_by_shift'].items():check(shares[key],reported,'5e-15')
 check(bycol[0]/N,old['stream_col0_share'],'5e-15');check(Fnear/M,old['density_near_share'],'5e-15')
 winner=max(bycol,key=lambda q:float(bycol[q].log().mid()));assert winner==old['stream_col_argmax']
 winner_cert=all(bycol[winner]>v for q,v in bycol.items() if q!=winner);assert winner_cert
 for q,reported in old['stream_log10_col'].items():check(bycol[int(q)].log()/l10,reported)
 for q,reported in old['density_log10_col'].items():check(Fcols[int(q)].log()/l10,reported)
 for q,reported in old['stream_near_by_col_log10'].items():check(nearcol[int(q)].log()/l10,reported)
 rows.append(dict(n=n,log10_N=text(N.log()/l10),log10_M=text(M.log()/l10),log10_N_over_M=text((N/M).log()/l10),stream_share_by_shift={key:text(v) for key,v in shares.items()},column0_share=text(bycol[0]/N),density_near_share=text(Fnear/M),strict_plain_column_winner=winner,all_peer_roundings_compatible=True))
changes=[]
for n in [311,314,317,320]:
 previous=n-1
 changes.append(dict(n=n,previous=previous,N_ratio=text(norms[n]/norms[previous]),near_increment_over_previous_total=text((near[n]-near[previous])/norms[previous]),complement_increment_over_previous_total=text(((norms[n]-near[n])-(norms[previous]-near[previous]))/norms[previous]),near_increases=bool(near[n]>near[previous]),complement_decreases=bool(norms[n]-near[n]<norms[previous]-near[previous])))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),input_path=str(path),input_sha256=digest,peer_input_path=str(peerpath),peer_input_sha256=sha256(peerraw).hexdigest(),precision_bits=640,coefficient_count=counts,rounded_comparisons=comparisons,rows=rows,adjacent_changes=changes,actual_elapsed_s=time.monotonic()-start,scope='Finite interval partitions and compatibility with rounded midpoint reports; no monotone or asymptotic concentration claim.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/peer_mode_shares.json').write_bytes(peerraw)
for name in ['stream_mode_share_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps(dict(output=str(root),**{key:value for key,value in result.items() if key!='rows'})),flush=True)
