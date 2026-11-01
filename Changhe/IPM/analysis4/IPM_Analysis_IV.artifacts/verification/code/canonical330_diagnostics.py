"""Independent ball t-evaluations, diagonal partitions and mode shares near order330."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import argparse,json,pickle,re,time,sys
sys.dont_write_bytecode=True
from flint import arb,ctx
from read_checkpoint_archive import read_bytes
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('checkpoint');a=ap.parse_args();start=time.monotonic();ctx.prec=640
raw=read_bytes(a.checkpoint);digest=sha256(raw).hexdigest();state=pickle.loads(raw);del raw;assert max(state['f'])>=330
root=Path('research/75_diagonal_mass/verification')/('canonical330_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'));(root/'sources').mkdir(parents=True)
peer={}
for name in ['bands_330.txt','tprofile_330.txt','stream_ratio_modes_321_330.json']:
 p=Path('../a4-num/notes')/name;peer[name]=p.read_text();(root/'sources'/name).write_text(peer[name])
z=arb(0);l10=arb(10).log();text=lambda v:v.str(36,radius=True);checks=[]
def check(value,reported,tolerance,tag):
 target=arb(str(reported));tol=arb(tolerance)
 overlap=value.overlaps(arb(target,tol));contained=bool(abs(value-target)<tol)
 assert overlap,(tag,text(value),reported)
 checks.append(dict(tag=tag,reported=str(reported),tolerance=tolerance,compatible=True,enclosure_inside_rounding_bin=contained))
# Read source table columns, not a reimplementation of the source evaluator.
tprinted={}
for line in peer['tprofile_330.txt'].splitlines():
 parts=line.split()
 if parts and parts[0]=='330':tprinted[int(float(parts[1]))]=parts[2:]
bprinted={}
for line in peer['bands_330.txt'].splitlines():
 parts=line.split('|')
 if len(parts)==3 and parts[0].strip().isdigit():bprinted[int(parts[0])]=[parts[1].split(),parts[2].split()[:3]]
profiles=[];bands=[]
for fi,field in enumerate(['f','g']):
 cols=[[arb(*unpack(v)) for v in col] for col in state[field][330]];colnorm=[sum(map(abs,col),z) for col in cols]
 for t in [-40,-20,0,20,40]:
  values=[z]*max(map(len,cols));absolute=z
  for q in range(len(cols)-1,-1,-1):
   values=[v*t+(cols[q][j] if j<len(cols[q]) else z) for j,v in enumerate(values)];absolute=absolute*abs(t)+colnorm[q]
  norm=sum(map(abs,values),z);assert norm>0
  log=norm.log()/l10;cancel=(absolute/norm).log()/l10;rad=sum((v.rad() for v in values),z)
  if t in tprinted:
   row=tprinted[t];check(log,row[0 if field=='f' else 4],'0.00005',f'{field}:t{t}:lognorm')
   if field=='f':check(colnorm[0].log()/l10,row[2],'0.00005',f'f:t{t}:c0');check(cancel,row[3],'0.005',f'f:t{t}:cancel')
  profiles.append(dict(field=field,t=t,log10_norm=text(log),log10_absolute_sum=text(absolute.log()/l10),log10_cancellation=text(cancel),norm_relative_radius=text(norm.rad()/abs(norm.mid())),log10_sum_coefficient_radii=text(rad.log()/l10)))
 for q,printed in bprinted.items():
  total=colnorm[q];parts=[z,z,z];offset=4 if field=='f' else 2
  for j,v in enumerate(cols[q]):
   distance=abs(3*(2*j+offset)-660)
   idx=(0 if distance<=6 else 2) if q==0 else (0 if 4*distance<=3*q else 1 if distance<=3*q else 2)
   parts[idx]+=abs(v)
  shares=[v/total for v in parts];assert sum(shares,z).contains(1)
  for idx,val in enumerate(shares):check(val,printed[fi][idx],'0.0005',f'{field}:q{q}:band{idx}')
  bands.append(dict(field=field,q=q,shares=list(map(text,shares))))
modepeer=json.loads(peer['stream_ratio_modes_321_330.json'])['orders'];mode_rows=[];count=0
for n in range(321,331):
 P3=6-2*n;byshift={};bycol={};nearcol={};Fcols={};Fnear=z
 for q,col in enumerate(state['g'][n]):
  for j,packed in enumerate(col):
   v=abs(arb(*unpack(packed)));count+=1
   if not j:assert v.is_zero();continue
   dist=min(abs(P3+6*j),abs(P3-6*j));key=str(Fraction(dist,3)) if dist<=12 else 'far'
   byshift[key]=byshift.get(key,z)+v;bycol[q]=bycol.get(q,z)+v
   if dist<=2:nearcol[q]=nearcol.get(q,z)+v
 N=sum(byshift.values(),z)
 for q,col in enumerate(state['f'][n]):
  total=z
  for j,packed in enumerate(col):
   v=abs(arb(*unpack(packed)));count+=1;total+=v
   if abs(abs(P3)-3*(2*j+1))<=4:Fnear+=v
  Fcols[q]=total
 M=sum(Fcols.values(),z);old=modepeer[str(n)];shares={k:v/N for k,v in byshift.items()}
 for v,k in [(N.log()/l10,'log10N'),(M.log()/l10,'log10M'),((N/M).log()/l10,'log10ratio')]:check(v,old[k],'8e-13',f'n{n}:{k}')
 for k,v in old['stream_share_by_shift'].items():check(shares[k],v,'5e-15',f'n{n}:shift{k}')
 check(bycol[0]/N,old['stream_col0_share'],'5e-15',f'n{n}:stream_col0');check(Fnear/M,old['density_near_share'],'5e-15',f'n{n}:density_near')
 winner=max(bycol,key=lambda k:float(bycol[k].mid()));assert winner==old['stream_col_argmax'];strict=all(bool(bycol[winner]>v) for k,v in bycol.items() if k!=winner)
 for source,mapping in [('stream_log10_col',bycol),('density_log10_col',Fcols),('stream_near_by_col_log10',nearcol)]:
  for q,v in old[source].items():check(mapping[int(q)].log()/l10,v,'8e-13',f'n{n}:{source}:{q}')
 mode_rows.append(dict(n=n,log10_N=text(N.log()/l10),log10_M=text(M.log()/l10),N_over_M=text(N/M),stream_shares={k:text(v) for k,v in shares.items()},winner=winner,winner_strictly_certified=strict))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),checkpoint_path=a.checkpoint,checkpoint_sha256=digest,all_checks_pass=True,profiles=profiles,bands=bands,mode_rows=mode_rows,mode_coefficient_count=count,comparisons=checks,compatible_comparisons=len(checks),rounding_bins_containing_full_enclosure=sum(c['enclosure_inside_rounding_bin'] for c in checks),actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['canonical330_diagnostics.py','stream_precision_audit.py','read_checkpoint_archive.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()};(root/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(dict(output=str(root),all_checks_pass=True,profiles=profiles,bands=bands,mode_coefficient_count=count,compatible_comparisons=len(checks),full_enclosure_bins=result['rounding_bins_containing_full_enclosure'],actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
