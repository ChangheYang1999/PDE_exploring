"""Exact source-branch classification and prior trial-file linkage."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,math,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1]
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def q(x):assert math.isfinite(x);return Q.from_float(float(x))
rpath=B/'research/forcing_angular_reduction/evidence/regeneration.json';vpath=B/'research/forcing_angular_reduction/evidence/verdict.json';v=read(vpath);assert v['status']=='CONFIRMED_REGENERATED_ANGULAR_REDUCTIONS_ONLY'
pins=dict(v['files']);assert len(pins)==179
for p,h in pins.items():assert sha(B/p)==h,p
assert pins[str(rpath.relative_to(B))]==sha(rpath)
r=read(rpath);g=read(D/'evidence/source_geometry.json')
for name in ['green','trial']:
 x=g['external_inputs'][name];assert r['pins'][x['path']]==x['sha256']==sha(Path(x['path']))
raw=read(D/'source/runs/forcing/v22_p9_merged.json');ri,ro=Q(231,8000),Q(297,8000);counts={k:0 for k in ['inside','transition','straddle']};checks=0;sourcechecks=0
for row in raw['cells']:
 d0,d1=q(row['dmin']),q(row['dmax']);assert d0<=d1 and d1>=0 and d0<ro
 have=row['series'] is not None
 expect='inside' if d1<=ri else ('transition' if have and d0>=ri and d1<=ro else 'straddle')
 assert row['regime']==expect,(row,expect);checks+=1;counts[expect]+=1
 s0,s1=map(q,row['sigma']);assert s0<=(d0-ri)/(ro-ri) and (d1-ri)/(ro-ri)<=s1
 source='inside' if s1<=0 else ('transition' if have and s0>=0 and s1<=1 else 'straddle')
 assert source==expect;sourcechecks+=1
assert counts=={'inside':26079,'transition':16502,'straddle':1368} and checks==sourcechecks==43949
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_V22_EXACT_REGIMES_AND_PRIOR_TRIAL_LINKAGE',direct_regime_checks=checks,source_sigma_branch_checks=sourcechecks,classifications=counts,prior_pins_rehashed=len(pins),prior_verdict_sha256=sha(vpath),regeneration_sha256=sha(rpath),external_inputs=g['external_inputs'],data_sha256=sha(D/'source/runs/forcing/v22_p9_merged.json'),code_sha256=sha(Path(__file__)),geometry_trial_dependence='NONE: the cover uses canonical radial endpoints, source bracket and polar subdivision; no trial coefficient',pins=pins,scope='Exact finite branch/provenance checks; no physical residual jets or historical source execution.')
(D/'evidence/provenance_supplement.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],checks,'rows',len(pins),'pins')
