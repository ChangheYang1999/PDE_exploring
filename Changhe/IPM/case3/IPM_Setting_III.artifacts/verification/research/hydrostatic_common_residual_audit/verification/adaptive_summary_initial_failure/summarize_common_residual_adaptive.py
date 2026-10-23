"""Result287: all fixed/adaptive witnesses and exact displayed intervals."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,math,traceback
import numpy as np
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];witnesses=[];tokens=[];eps=np.finfo(float).eps;start=utc();regions=[(0,.1),(.1,1),(1,100),(100,1e4),(1e4,1e6+1)]
def ck(name,b,e=None):
 checks.append(dict(name=name,passed=bool(b),evidence=e))
 if not b:raise AssertionError((name,e))
def save(status):
 out=dict(status=status,started_utc=start,finished_utc=utc(),count=len(checks),checks=checks,witnesses=witnesses,tokens=tokens,source_sha256={str(p):sha(p)for p in [V/'RUN.json',V/'SUMMARY.json',V/'ADAPTIVE.json',V/'INPUTS.json',V/'POINTS.npz']},proof_sha256=sha(R/'ADAPTIVE_SUMMARY_PROOF.md'),driver_sha256=sha(__file__),review_proof_sha256=sha(R/'MP_REVIEW_RESOLUTION.md'),scope='Empirical finite-sample numerical comparison, not a rigorous error enclosure; no full-plane endpoint.')
 (V/'ADAPTIVE_SUMMARY.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
try:
 run=json.loads((V/'RUN.json').read_text());s=json.loads((V/'SUMMARY.json').read_text());a=json.loads((V/'ADAPTIVE.json').read_text());inp=json.loads((V/'INPUTS.json').read_text())
 for label,b,driver,proof in [('run',run,'audit_hydrostatic_common_residuals.py','verification/EXECUTED_BASE_PROTOCOL.md'),('summary',s,'summarize_hydrostatic_common_residuals.py','SUMMARY_PROOF.md'),('adaptive',a,'audit_common_residual_adaptive.py','ADAPTIVE_PROOF.md')]:
  ck(label+' complete',b['status']=='PASS'and all(t['passed']for t in b['checks']));ck(label+' driver',b['driver_sha256']==sha(Path('independent_code')/driver));ck(label+' proof',b['proof_sha256']==sha(R/proof))
 for key,file in [('summary_sha256','SUMMARY.json'),('run_sha256','RUN.json'),('input_sha256','INPUTS.json'),('points_sha256','POINTS.npz')]:ck('adaptive binding '+key,a[key]==sha(V/file))
 for file,h in s['source_sha256'].items():ck('summary source '+file,sha(file)==h)
 ck('review correction binding',s['review_proof_sha256']==sha(R/'REVIEW_RESOLUTION_PROOF.md'));ck('adaptive module',a['module_sha256']==sha('independent_code/adaptive_hydrostatic_velocity.py'))
 for item in inp['files']+[i[k]for i in inp['states']for k in ['state','export']]:ck('input '+item['path'],sha(item['path'])==item['sha256'])
 for m in a['manufactures']:
  ck('adaptive manufacture '+m['path'],sha(m['path'])==m['sha256']);b=json.loads(Path(m['path']).read_text());ck('adaptive manufacture PASS '+m['path'],b['status']=='PASS'and all(t['passed']for t in b['checks'])and b['module_sha256']==a['module_sha256'])
 ck('exact selection provenance',a['selection']==s['witnesses'])
 pts=np.load(V/'POINTS.npz')['points'];fixed={};ad={}
 for state in run['states']:
  last=state['levels'][-1];ck('fixed raw hash '+state['tag'],sha(last['path'])==last['sha256']);fixed[state['tag']]=dict(np.load(last['path']));ff=fixed[state['tag']];ck('fixed schema '+state['tag'],ff['jets'].shape==(333,4)and ff['velocity'].shape==(333,2));previous=state['levels'][-2];ck('previous raw hash '+state['tag'],sha(previous['path'])==previous['sha256']);prior=dict(np.load(previous['path']));ref=next(z for z in s['refinements']if z['tag']==state['tag']and z['orders']==[48,64]);
  for k,(lo,hi)in enumerate(regions):
   mask=(pts[:,2]>=lo)&(pts[:,2]<hi);ck('pointwise Rh sensitivity '+state['tag']+str(k),float(np.max(abs(ff['Rh']-prior['Rh'])[mask]))==ref['regions'][k]['absolute_Rh'])
   for metric in ['Rf','Rv','Rbound']:
    valid=mask&np.isfinite(ff[metric])&np.isfinite(prior[metric]);ck('pointwise '+metric+' sensitivity '+state['tag']+str(k),float(np.max(abs(ff[metric]-prior[metric])[valid]))==ref['regions'][k][metric])
 for state in a['states']:
  tag=state['tag'];p=state['p'];c=state['c'];ff=fixed[tag];items={z['index']:z for z in state['points']};ad[tag]=items;selection=next(z['indices']for z in s['witnesses']if z['tag']==tag);ck(tag+' exact pointset',sorted(items)==selection and len(items)==len(state['points']));ck(tag+' complete',state['status']=='DONE')
  for i,z in items.items():
   x,y,r,j=pts[i];ck(tag+' coordinate '+str(i),[z['x'],z['y'],z['radius'],z['angle_index']]==[x,y,r,int(j)]);g,gx,gy=z['jet'][:3];u,v=z['V'];aa=(c*x+u)*gx;bb=(c*y+v)*gy;rh=math.fsum([aa,bb,-g]);nf=abs(aa)+abs(bb)+abs(g);nv=abs(g)+abs(math.fsum([x*gx,y*gy]))+abs(math.fsum([u*gx,v*gy]));nb=math.hypot(c*x+u,c*y+v)*math.hypot(gx,gy)+abs(g);raw=dict(Rh=rh,Nf=nf,Nv=nv,Nbound=nb);T=abs(c*x*gx)+abs(u*gx)+abs(c*y*gy)+abs(v*gy)+abs(g);S=abs(g)+abs(x*gx)+abs(y*gy)+abs(u*gx)+abs(v*gy);B=(abs(c*x)+abs(u)+abs(c*y)+abs(v))*math.hypot(gx,gy)+abs(g);scales=dict(Rh=T,Nf=T,Nv=S,Nbound=B)
   ck(tag+' scalar raw '+str(i),all(abs(raw[k]-z[k])<=128*eps*max(scales[k],np.finfo(float).tiny)for k in raw));ck(tag+' shared analytic jet '+str(i),np.allclose(z['jet'],ff['jets'][i],rtol=64*eps,atol=1e-300));ck(tag+' warningfree '+str(i),not z['messages']);dv=np.array(z['V'])-ff['velocity'][i];w=dict(tag=tag,index=i,region=next(k for k,(lo,hi)in enumerate(regions)if lo<=r<hi),velocity_difference=list(map(float,dv)),weighted_velocity_difference=float(np.hypot(*dv)/(1+r)**p),absolute_Rh_difference=abs(z['Rh']-float(ff['Rh'][i])),estimated_error=z['estimated_error'],ratios={})
   for ratio,den in [('Rf','Nf'),('Rv','Nv'),('Rbound','Nbound')]:
    own=abs(rh)/raw[den]if raw[den]>0 else None;ck(tag+' ratio '+ratio+str(i),(own is None and z[ratio]is None)or(own is not None and z[ratio]is not None and abs(own-z[ratio])<=512*eps*(T+own*scales[den])/raw[den]));w['ratios'][ratio]=abs(own-float(ff[ratio][i]))if own is not None else None
   witnesses.append(w)
 for original in s['comparisons']:
  tag=original['tag'];region=original['region'];key=original['metric'];items=ad[tag];chosen=[z for z in items.values()if regions[region][0]<=z['radius']<regions[region][1]];ck(tag+f' adaptive includes {region}{key} fixedmax',original['index']in items);valid=[z for z in chosen if z[key]is not None];ck(tag+f' nonempty subset {region}{key}',bool(valid));z=max(valid,key=lambda z:abs(z[key])if key=='Rh'else z[key]);val=abs(z[key])if key=='Rh'else z[key];center=F(original['printed']);half=F(original['rounding_half_width']);af=F.from_float(val)-center;ff=F.from_float(original['value'])-center;agree=abs(af)<=half;delta=max([w['absolute_Rh_difference']if key=='Rh'else w['ratios'][key]for w in witnesses if w['tag']==tag and w['region']==region and(key=='Rh'or w['ratios'][key]is not None)])
  fixed_change=next(q['regions'][region]['absolute_Rh'if key=='Rh'else key]for q in s['refinements']if q['tag']==tag and q['orders']==[48,64]);empirical=max(delta,fixed_change);min_distance=min(abs(abs(af)-half),abs(abs(ff)-half));same_side=(af>half and ff>half)or(af< -half and ff< -half);stable=min_distance>10*F.from_float(empirical)
  verdict='CONFIRMED'if agree and original['agrees']and stable else'REFUTED'if not agree and not original['agrees']and same_side and stable else'OPEN';tokens.append(dict(**original,coverage='Fixed rules cover the333 reporting points; adaptive covers a selected subset containing the fixed maximizer and its grid neighbors. No continuum bound.',classification_scope='Sampled numerical reproduction with a tenfold observed-sensitivity reporting margin, not an enclosure.',adaptive_value=val,adaptive_index=z['index'],adaptive_subset_count=len(valid),adaptive_agrees=agree,adaptive_signed_difference=str(af),observed_fixed_adaptive_change=delta,observed_fixed_rule_change=fixed_change,empirical_sensitivity=empirical,minimum_rounding_margin=str(min_distance),verdict=verdict,adaptive_corrected=format(val,'.'+str(len(original['printed'].split('e')[0].split('.')[1]))+'e')))
 ck('all70 tokens',len(tokens)==70);ck('all7 states',len(ad)==7);save('PASS');print('PASS',len(checks),'witnesses',len(witnesses),'verdicts',{k:sum(t['verdict']==k for t in tokens)for k in ['CONFIRMED','REFUTED','OPEN']},utc())
 for t in tokens:
  if t['verdict']!='CONFIRMED':print(t['verdict'],t['tag'],t['region'],t['metric'],t['printed'],t['adaptive_value'],t['adaptive_corrected'],t['empirical_sensitivity'])
except Exception:
 save('FAIL');(V/'adaptive_summary_traceback.txt').write_text(traceback.format_exc());raise
