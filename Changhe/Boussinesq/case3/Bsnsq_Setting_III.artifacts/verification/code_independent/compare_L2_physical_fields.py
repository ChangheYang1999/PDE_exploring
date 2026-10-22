"""Independent field-distance diagnostics, not NUM code or a PDE residual test."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,sys
import numpy as np
from r2_state_values import R2State
root=Path('verification/L2_physical_continuity_20261021T1239Z');root.mkdir(exist_ok=True);arc=root/'archives';arc.mkdir(exist_ok=True)
started=datetime.now(timezone.utc).isoformat();t0=time.monotonic()
if (root/'inputs.json').exists() and '--refreeze' not in sys.argv:
 inputs=json.loads((root/'inputs.json').read_text());names=inputs['accepted_states'];secants=inputs['secants'];records=inputs['archives']
 for rec in records:
  assert hashlib.sha256(Path(rec['frozen']).read_bytes()).hexdigest()==rec['sha256'],'Frozen archive hash mismatch'
 claimed=json.loads((root/'fieldcont_L2B24.json').read_text())
else:
 names=['blamL2B24_beta3.088','blamL2B24_beta3.09']+['blamL2B24b_beta'+s for s in ['3.0925','3.095','3.1','3.105','3.11','3.12','3.14']]
 source=Path('../numerics/runs');records=[];secants={}
 for name in names:
  secants[name]=[p.stem for p in sorted(source.glob(name+'_sec[0-9].npz'))]
  for label in [name]+secants[name]:
   p=source/(label+'.npz');b=p.read_bytes();h=hashlib.sha256(b).hexdigest();(arc/p.name).write_bytes(b)
   assert hashlib.sha256(p.read_bytes()).hexdigest()==h,'Source changed during freeze'
   records.append({'name':label,'source':str(p),'frozen':str(arc/p.name),'sha256':h,'bytes':len(b),'accepted_stage':label==name})
 report=Path('../numerics/NUM_REPORT.md');(root/'NUM_REPORT_snapshot.md').write_bytes(report.read_bytes())
 p=source/'fieldcont_L2B24.json';(root/p.name).write_bytes(p.read_bytes());claimed=json.loads(p.read_text())
 inputs={'accepted_states':names,'secants':secants,'archives':records,'grid':{'radial_log10_min':-6,'radial_log10_max':8,'radial_count':129,'extra_radii':[0,1,10000,1000000],'angular_resolutions':[96,256],'angular_fractional_offset':0.371,'include_exact_axes':True},'denominator':'old angular max, plus symmetric max; 0/0=0 and positive/0=infinity; no floor','scope':'Finite physical field samples, not PDE/inverse or branch certification'}
 (root/'inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
radii=np.unique(np.r_[0.,np.geomspace(1e-6,1e8,129),1.,1e4,1e6]);states={rec['name']:R2State(rec['frozen']) for rec in records}
fields=('F','G','Theta','Omega')
meta={}
for name,s in states.items():
 seed=s.seed_field;seed_geom={key:s.meta.get('seed_'+key,s.meta.get(key)) for key in ['L','K','Nt','deg','grade','rmap']}
 meta[name]={'beta':s.beta,'beta_basis':s.bb,'lambda':float(s.meta.get('lam',0)),'source_mode':s.forcing_schema,'seed_beta':s.meta.get('beta_seed'),'seed_geometry':seed_geom,'seed_coefficients_sha256':hashlib.sha256(seed.rawG.tobytes()).hexdigest() if seed is not None else None,'a0':s.center()['F']['value'],'stored_accepted':s.meta.get('continuation_accepted'),'stored_converged':s.meta.get('converged')}
def ratios(n,d):
 n=np.asarray(n,dtype=np.longdouble);d=np.asarray(d,dtype=np.longdouble)
 a=np.full(n.shape,np.inf,dtype=np.longdouble);np.divide(n,d,out=a,where=d!=0);a[(d==0)&(n==0)]=0
 return np.asarray(a,dtype=float)
def samples(na):
 phi=2*np.pi*(np.arange(na)+.371)/na;c=np.r_[np.cos(phi),1.,0.,-1.,0.];ss=np.r_[np.sin(phi),0.,1.,0.,-1.]
 x=radii[:,None]*c[None,:];y=radii[:,None]*ss[None,:]
 out={};finite=True
 for name,s in states.items():
  F=s.divided(x,y,'F');G=s.divided(x,y,'G');out[name]={'F':F,'G':G,'Theta':x*x*F,'Omega':x*G}
  finite=finite and all(np.isfinite(a).all() for a in out[name].values())
 assert finite
 return out,na+4
def pair(label1,label2,vals,category):
 a,b=vals[label1],vals[label2];m1,m2=meta[label1],meta[label2]
 ans={'first':label1,'second':label2,'category':category,'dbeta':m2['beta']-m1['beta'],'dlambda':m2['lambda']-m1['lambda'],'fields':{}}
 for key in fields:
  aa=np.max(np.abs(a[key]),axis=1);bb=np.max(np.abs(b[key]),axis=1);dd=np.max(np.abs(b[key]-a[key]),axis=1);rel=ratios(dd,aa);sym=ratios(dd,np.maximum(aa,bb));k=int(np.argmax(rel))
  d={'old_relative_max':float(rel[k]),'radius_at_old_relative_max':float(radii[k]),'symmetric_relative_max':float(np.max(sym)),'absolute_max':float(np.max(dd)),'old_relative_by_radius':rel.tolist(),'absolute_by_radius':dd.tolist(),'old_amplitude_by_radius':aa.tolist(),'new_amplitude_by_radius':bb.tolist(),'subnormal_denominators':int(np.sum((aa>0)&(aa<np.finfo(float).tiny))),'zero_denominators':int(np.sum(aa==0)),'zero_over_zero':int(np.sum((aa==0)&(dd==0))),'positive_over_zero':int(np.sum((aa==0)&(dd>0)))}
  for r in [0.,1.,1e4,1e6,1e8]:
   k=int(np.flatnonzero(radii==r)[0]);d['at_r'+str(r)]={'old_relative':float(rel[k]),'symmetric_relative':float(sym[k]),'absolute':float(dd[k])}
  ans['fields'][key]=d
 return ans
runs=[]
for na in [96,256]:
 vals,nangles=samples(na);pairs=[]
 for a,b in zip(names[:-1],names[1:]):pairs.append(pair(a,b,vals,'successive_accepted'))
 pairs.append(pair(names[0],names[-1],vals,'first_last'))
 pairs.append(pair(names[0],names[-2],vals,'reported_first_last'))
 for name,labels in secants.items():
  for a,b in zip(labels[:-1],labels[1:]):pairs.append(pair(a,b,vals,'successive_secant'))
  if labels:pairs.append(pair(labels[-1],name,vals,'last_secant_to_accepted'))
 run={'angular_count':nangles,'radial_count':len(radii),'point_count':len(radii)*nangles,'radii':radii.tolist(),'pairs':pairs}
 # Compare the numerical lane's published scalar values, without using its code.
 comp=[]
 for old in claimed['rows']:
  hit=next(p for p in pairs if p['first']==old['s1'] and p['second']==old['s2'])
  row={'first':old['s1'],'second':old['s2'],'fields':{}}
  for k in ['F','G']:
   ix=np.flatnonzero((radii>=.01)&(radii<=1e6));q=np.array(hit['fields'][k]['old_relative_by_radius']);j=ix[np.argmax(q[ix])]
   v=float(q[j]);r1=hit['fields'][k]['at_r1.0']['old_relative'];r4=hit['fields'][k]['at_r10000.0']['old_relative']
   row['fields'][k]={'max_relative_our_radial_window':v,'radius_at_max':float(radii[j]),'reported_max_relative':old[k+'_max_rel'],'difference':v-old[k+'_max_rel'],'r1_difference':r1-old[k+'_rel_r1'],'r1e4_difference':r4-old[k+'_rel_r1e4']}
  comp.append(row)
 run['reported_value_comparison']=comp;runs.append(run);del vals
# Counterexample to no-root inference, computed exactly at three rational points.
from fractions import Fraction as Q
nodes=[Q(0),Q(1)];m=lambda t:-1+32*t*t*(t-1)*(t-1)
controls=[{'beta':str(t),'value':str(m(t))} for t in [Q(0),Q(1,2),Q(1)]]
assert m(Q(0))<0 and m(Q(1))<0 and m(Q(1,2))>0
summary={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'input_sha256':hashlib.sha256((root/'inputs.json').read_bytes()).hexdigest(),'metadata':meta,'exact_scalar_counterexample_control':controls,'all_arrays_finite':True,'runs':runs}
(root/'results.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
print(json.dumps({'started_utc':started,'ended_utc':summary['ended_utc'],'elapsed_seconds':summary['elapsed_seconds'],'archives':len(records),'accepted':len(names),'points':[r['point_count'] for r in runs],'pairs':[len(r['pairs']) for r in runs],'all_arrays_finite':True},indent=2))
for p in runs[-1]['pairs']:
 if p['category']=='successive_accepted':print(p['first'],p['second'],p['dbeta'],p['fields']['F']['at_r1000000.0']['old_relative'],p['fields']['G']['at_r1000000.0']['old_relative'])
