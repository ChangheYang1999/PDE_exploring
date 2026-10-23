"""Own Cartesian density jets at all actual exported nodes. No inverse runs."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter();checks=[];bindings={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p).resolve().relative_to(Path.cwd());z=sha(p);ck('binding '+str(p),h is None or h==z);bindings[str(p)]=z;return p
try:
 for p in [Path(__file__),R/'ACTUAL_JET_STAGE_PROOF.md',V/'PROVENANCE_INPUTS.json',V/'JET_PROVENANCE_INPUTS.json',V/'TRANSITIVE_JET_INPUTS.json']+[Path('independent_code')/s for s in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','node_export_arithmetic_strict.py','node_export_arithmetic.py','scalar_mp_hydrostatic_density.py']]:bind(p)
 for name,count in [('ADMISSION.json',4721),('MANUFACTURES_EXPANDED.json',717),('SUPPLEMENT_CHECKS.json',421),('HIGH_BASIS_CHECKS.json',182),('PARTITION_CHECKS.json',881)]:
  p=bind(V/name);a=json.loads(p.read_text());ck('complete gates '+name,a['status'].startswith('PASS')and a['count']==len(a['checks'])==count and all(z['passed']for z in a['checks']))
  for p,h in a['bindings'].items():bind(p,h)
 for name in ['JET_PROVENANCE_INPUTS.json','TRANSITIVE_JET_INPUTS.json']:
  for z in json.loads((V/name).read_text())['entries']:bind(z['frozen'],z['sha256']);ck('two static reads '+z['frozen'],z['two_reads_identical'])
 src=json.loads((V/'PROVENANCE_INPUTS.json').read_text());state=bind(src['state']['frozen'],'4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01');export=bind(V/'source_nodes_maps.npz','071b990c7a9ee3a91faeca5a1cc8c7d9ef6ef478f41ccd591fbe1ad5575d42d7')
 # All local imports occur after their input/code bindings.
 import numpy as np
 import torch
 from fractions import Fraction as F
 from q_local_checkpoint import QLocalCheckpoint
 from independent_hydrostatic import CartesianQJet
 from node_export_arithmetic_strict import residual,exact
 torch.set_num_threads(1)
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state)
 with np.load(export,allow_pickle=False)as f:d={k:f[k]for k in f.files}
 x,y=d['X'],d['Y'];rad=np.hypot(x,y);own=CartesianQJet(q).jet(x,y);producer=np.column_stack([d[k]for k in ['g','gx','gy']]);ck('candidate finite shape',own.shape==(2304,4)and np.isfinite(own).all());ck('exact candidate dimensions',q.N==96 and q.M==24 and q.cl==2 and q.kappa==2 and q.L==1)
 absolute=abs(own[:,:3]-producer);scale=np.maximum(abs(own[:,:3]),abs(producer));floored=absolute/np.maximum(scale,1e-5);pure=np.divide(absolute,scale,out=np.zeros_like(scale),where=scale!=0);zeros=(scale==0);ck('relative finite and zero counted',np.isfinite(pure).all()and np.all(absolute[zeros]==0))
 maxima=[];witness=set([2136,2160]);regions=[('r<.1',rad<.1),('.1<=r<1',(rad>=.1)&(rad<1)),('1<=r<100',(rad>=1)&(rad<100)),('r>=100',rad>=100)];ck('radial partition covers exactly',np.all(sum(mask.astype(int)for _,mask in regions)==1))
 for j,name in enumerate(['g','gx','gy']):
  for metric,arr in [('absolute',absolute),('floored',floored),('pure_relative',pure)]:
   i=int(np.argmax(arr[:,j]));witness.add(i);maxima.append(dict(component=name,metric=metric,index=i,x=float(x[i]),y=float(y[i]),radius=float(rad[i]),value=float(arr[i,j]),own=float(own[i,j]),producer=float(producer[i,j]),both_zero=bool(zeros[i,j])))
 for ir in [0,47,95]:
  for ia in [0,11,23]:witness.add(ir*24+ia)
 witness=sorted(witness);ck('deterministic witness count',len(witness)==len(set(witness))and all(0<=i<2304 for i in witness))
 rm=np.empty((2304,3));rp=np.empty((2304,3));dj=np.empty(2304)
 for i in range(2304):
  j=own[i,:3];jp=producer[i];vm=[d['V1_map'][i],d['V2_map'][i]];a=residual(j,vm,2,x[i],y[i]);b=residual(jp,vm,2,x[i],y[i]);want=(2*exact(x[i])+exact(vm[0]))*(exact(j[1])-exact(jp[1]))+(2*exact(y[i])+exact(vm[1]))*(exact(j[2])-exact(jp[2]))-exact(j[0])+exact(jp[0]);ck('exact fixed-map jet identity '+str(i),a['R']-b['R']==want);rm[i]=[float(a[k])for k in ['R','Nf','Nv']];rp[i]=[float(b[k])for k in ['R','Nf','Nv']];dj[i]=float(want)
 summaries=[]
 for label,mask in regions:
  ids=np.flatnonzero(mask);row=dict(region=label,count=len(ids),metrics={})
  for who,rr in [('own_jet_exported_map',rm),('producer_jet_exported_map',rp)]:
   out={}
   for key,z in [('absR',abs(rr[:,0])),('absR_over_Nf',np.divide(abs(rr[:,0]),rr[:,1],out=np.full(2304,np.nan),where=rr[:,1]!=0)),('absR_over_Nv',np.divide(abs(rr[:,0]),rr[:,2],out=np.full(2304,np.nan),where=rr[:,2]!=0))]:
    valid=ids[np.isfinite(z[ids])];i=int(valid[np.argmax(z[valid])])if len(valid)else None;out[key]=dict(value=float(z[i])if i is not None else None,index=i,x=float(x[i])if i is not None else None,y=float(y[i])if i is not None else None,defined_count=len(valid),undefined_count=len(ids)-len(valid))
   row['metrics'][who]=out
  summaries.append(row)
 path=V/'actual_node_jets.npz';np.savez_compressed(path,X=x,Y=y,own_jet=own,producer_jet=producer,absolute_difference=absolute,floored_difference=floored,pure_relative_difference=pure,both_zero=zeros,own_jet_map_residual=rm,producer_jet_map_residual=rp,exact_jet_residual_difference=dj);bind(path)
 for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
 out=dict(status='PASS_ACTUAL_NODE_JETS_AND_EXACT_FIXED_MAP_ARITHMETIC',started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,maxima=maxima,mp_witness_indices=witness,source_both_zero_count=[int(z)for z in zeros.sum(axis=0)],radial_residual_summaries=summaries,scope='Finite2304-node jets and fixed exported-map arithmetic only. Independent inverse/MP witness stage pending. No producer code executed; historical map authentication open; primary unresolved.')
 (V/'ACTUAL_JETS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['elapsed_monotonic_seconds']);print(json.dumps(maxima,indent=2));print('witness',witness)
except Exception:
 (V/'ACTUAL_JETS_FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,bindings=bindings,traceback=traceback.format_exc()),indent=2)+'\n');raise
