"""Exact cover audit and higher precision original-data replay."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime,timezone
import json,gzip,hashlib,time
from flint import arb,ctx
import refine as R
ctx.prec=640;ctx.threads=1
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lo(r):return F(r['lower_exact'])
def hi(r):return F(r['upper_exact'])
def emit(**v):print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),**v}),flush=True)
t0=time.monotonic();path=TOP/'evidence/refinement.json.gz'
with gzip.open(path,'rt') as f:out=json.load(f)
basepath=LANE/'proofs/68_independent_global_coefficients/evidence/full.json'
base=json.loads(basepath.read_text());records=base['records']
baseaudit=json.loads((basepath.parent/'audit.json').read_text());ends=json.loads((basepath.parent/'ends.json').read_text())
assert baseaudit['status']=='PASS' and baseaudit['full_result_sha256']==sha(basepath)
assert baseaudit['ends_sha256']==sha(basepath.parent/'ends.json')
assert out['base_sha256']==sha(basepath) and out['cache_sha256']==sha(R.G.CACHE)
assert out['script_sha256']==sha(TOP/'code/refine.py') and out['proof_sha256']==sha(TOP/'PROOF.md')
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert out['input_sha256']==sha(source)
assert out['status']=='COMPUTED_PENDING_AUDIT' and out['unresolved_count']==0 and out['bits']==512
assert F(out['target'])==F(5,2);target=F(5,2)
selected=[i for i,r in enumerate(records) if min(lo(r[k]) for k in ('ma_lower','mr_lower'))<target]
preserved=sorted(set(range(len(records)))-set(selected))
assert selected==out['selected_radial_indices'] and preserved==out['preserved_radial_indices']
assert out['roots']==[[i,j] for i in selected for j in range(128)]
children=defaultdict(list);values={};maxdepth=0
for ix,r in enumerate(out['leaves']):
 assert r['verdict']=='ACCEPTED' and 0<=r['depth']<=14
 for key in ('ma_lower','mr_lower'):assert target<=lo(r[key])<=hi(r[key])
 i,j=r['root'];assert i in selected and 0<=j<128
 l,u,a,b=[F(r[k]) for k in ('t0','t1','a0','a1')]
 root=records[i];L=F(root['left_exact']);U=F(root['right_exact']);A=F(j,256);B=F(j+1,256)
 assert L<=l<u<=U and A<=a<b<=B
 children[(i,j)].append((l,u,a,b,ix))
 values[ix]=(lo(r['ma_lower']),lo(r['mr_lower']))
 maxdepth=max(maxdepth,r['depth'])
assert len(children)==len(out['roots'])
for (i,j),boxes in children.items():
 root=records[i];L=F(root['left_exact']);U=F(root['right_exact']);A=F(j,256);B=F(j+1,256)
 assert sum(((u-l)*(b-a) for l,u,a,b,_ in boxes),F(0))==(U-L)*(B-A)
 for x in range(len(boxes)):
  l,u,a,b,_=boxes[x]
  for ll,uu,aa,bb,_ in boxes[x+1:]:assert not(max(l,ll)<min(u,uu) and max(a,aa)<min(b,bb))
for key in ('ma_lower','mr_lower'):
 assert lo(out[key])==min(lo(r[key]) for r in out['leaves'])
 for side in ('inner','outer'):assert lo(ends[side][key])>=target
minimum={key:min([lo(out[key]),lo(ends['inner'][key]),lo(ends['outer'][key])]+[lo(records[i][key]) for i in preserved]) for key in ('ma_lower','mr_lower')}
emit(stage='exact_cover_passed',selected=len(selected),preserved=len(preserved),roots=len(children),leaves=len(out['leaves']),maxdepth=maxdepth,seconds=time.monotonic()-t0)
# Replay the weakest 40 leaves of each margin, all deepest-level leaves up to
# 32 and 24 deterministic spread leaves. These checks do not replace the
# enclosures of the complete accepted 512-bit run.
replay=set(sorted(values,key=lambda i:values[i][0])[:40]+sorted(values,key=lambda i:values[i][1])[:40])
replay.update([i for i,r in enumerate(out['leaves']) if r['depth']==maxdepth][:32])
replay.update((len(out['leaves'])-1)*j//23 for j in range(24))
c=R.Context();replayed=[]
for count,ix in enumerate(sorted(replay),1):
 r=out['leaves'][ix];i,j=r['root'];l,u,a,b=[F(r[k]) for k in ('t0','t1','a0','a1')]
 c.ranges.clear();c.rows.clear()
 ma,mr=c.ang.bounds(c.radial(records[i]['label'],l,u),l,u,a,b,c.ell)
 assert ma>=R.aa(target) and mr>=R.aa(target)
 replayed.append({'index':ix,'root':[i,j],'ma_lower':R.rec(ma),'mr_lower':R.rec(mr)})
 if count%20==0:emit(stage='replay',done=count,total=len(replay),seconds=time.monotonic()-t0)
result={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','safe_global_lower':'5/2','source_sha256':sha(source),
 'base_result_sha256':sha(basepath),'base_audit_sha256':sha(basepath.parent/'audit.json'),'ends_sha256':sha(basepath.parent/'ends.json'),
 'full_result_sha256':sha(path),'script_sha256':sha(Path(__file__)),'proof_sha256':sha(TOP/'PROOF.md'),
 'selected_radial_cells':len(selected),'preserved_radial_cells':len(preserved),'root_partitions_checked':len(children),
 'accepted_terminal_leaves':len(out['leaves']),'maximum_depth':maxdepth,'unresolved':0,
 'global_lower_exact':{k:str(v) for k,v in minimum.items()},'global_lower_diagnostic':{k:float(v) for k,v in minimum.items()},
 'precision_bits_replay':640,'representative_replays':replayed,'seconds':time.monotonic()-t0,
 'scope':'Both global full-plane energy margins are at least 5/2 for the exact normalized modal profile. No inverse assertion.'}
(TOP/'evidence/audit.json').write_text(json.dumps(result,indent=2)+'\n');emit(stage='finished',status='PASS',seconds=time.monotonic()-t0)
