"""Result287 finite represented-data scope, no inverse evaluation."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,math,itertools
import numpy as np
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];bindings={};started=datetime.now(timezone.utc).isoformat()
def ck(n,b):
 checks.append({'name':n,'passed':bool(b)})
 if not b:raise AssertionError(n)
def read(name):
 p=V/name;bindings[str(p)]=sha(p);return json.loads(p.read_text())
run=read('RUN.json');ad=read('ADAPTIVE.json');sens=read('MP_SENSITIVITY.json');bridge=read('ARITHMETIC_BRIDGE.json');summary=read('SUMMARY.json');ads=read('ADAPTIVE_SUMMARY.json');mpj=read('MP_JETS.json')
for name,g in [('run',run),('adaptive',ad),('sensitivity',sens),('bridge',bridge),('summary',summary),('adaptive summary',ads),('MP',mpj)]:
 ck(name+' PASS',g['status']=='PASS' and all(x['passed'] for x in g['checks']))
 for p,h in g.get('source_sha256',{}).items():
  ck('source '+p,sha(p)==h);bindings[p]=h
 for p,h in g.get('bindings',{}).items():ck('bound '+p,sha(p)==h);bindings[p]=h
pts=np.load(V/'POINTS.npz')['points'];bindings[str(V/'POINTS.npz')]=sha(V/'POINTS.npz')
radii=np.logspace(-3,6,37);nominal=np.repeat(radii,9);ck('same nominal recipe',np.array_equal(nominal,pts[:,2]));ck('integer shape',pts.shape==(333,4))
source=(V/'producer_definition_static.py').read_text();ck('source nominal masks',all(s in source for s in ['r = np.logspace(-3, 6, 37)','Rr = Rg.reshape(-1)','m = (Rr >= lo) & (Rr < hi)']))
bounds=[.1,1.,100.,1e4];boundary=[]
for b in bounds:
 ix=np.flatnonzero(nominal==b).tolist();ck('nine boundary '+str(b),len(ix)==9)
 boundary.append({'boundary':b,'verifier_hex':float(pts[ix[0],2]).hex(),'locally_reconstructed_producer_definition_hex':float(nominal[ix[0]]).hex(),'producer_actual_execution_hex':None,'indices':ix})
intervals=[(0,.1),(.1,1),(1,100),(100,1e4),(1e4,1e6+1)]
fixed={};adaptive={};raw={};params={}
for state in run['states']:
 lev=state['levels'][-1];ck('fixed array '+state['tag'],sha(lev['path'])==lev['sha256']);bindings[lev['path']]=lev['sha256'];z=dict(np.load(lev['path']));raw[state['tag']]=z;params[state['tag']]=state['c'];fixed[state['tag']]={i:{k:F.from_float(float(z[k][i])) if np.isfinite(z[k][i]) else None for k in ['Rh','Rf','Rv','Rbound']} for i in range(333)}
for state in ad['states']:adaptive[state['tag']]={p['index']:{k:F.from_float(float(p[k])) if p[k] is not None else None for k in ['Rh','Rf','Rv','Rbound']} for p in state['points']}
for row in sens['rows']:
 for dest,key in [(fixed,'MPjet_fixedV'),(adaptive,'MPjet_adaptiveV')]:dest[row['tag']][row['index']]={k:F(row['four_records'][key][k]) if row['four_records'][key][k] is not None else None for k in ['Rh','Rf','Rv','Rbound']}
def region_indices(region,bits=(0,0,0,0)):
 lo,hi=intervals[region];r=nominal.copy()
 for b,shift in zip(bounds,bits):
  if shift:r[r==b]=np.nextafter(b,-np.inf)
 return set(np.flatnonzero((lo<=r)&(r<hi)).tolist())
def rank(data,key,indices):
 rows=[(i,abs(d[key]) if key=='Rh' else d[key]) for i,d in data.items() if i in indices and d[key] is not None]
 return sorted(rows,key=lambda t:(-t[1],t[0]))
def record_rank(ranked):
 i,a=ranked[0];j,b=ranked[1] if len(ranked)>1 else (None,None)
 return {'index':i,'value':str(a),'value_float':float(a),'runner_up_index':j,'runner_up_value':str(b) if b is not None else None,'gap':str(a-b) if b is not None else None,'gap_float':float(a-b) if b is not None else None}
def excess(value,center,half):
 return ((value-(center+half)) if value>center+half else (value-(center-half)) if value<center-half else F(0))/abs(center)
tokens=[]
for old in sens['tokens']:
 tag=old['tag'];k=old['metric'];reg=old['region'];indices=region_indices(reg);fr=rank(fixed[tag],k,indices);ar=rank(adaptive[tag],k,indices);ff=fr[0][1];aa=ar[0][1]
 ck('reconstruct token '+str(len(tokens)),ff==F(old['partially_corrected_fixed_value']) and aa==F(old['partially_corrected_adaptive_value']) and fr[0][0]==old['fixed_index'] and ar[0][0]==old['adaptive_index'])
 center=F(old['printed']);half=F(old['half_width']);ef=excess(ff,center,half);ea=excess(aa,center,half);basepair=[abs(ff-center)<=half,abs(aa-center)<=half]
 scenarios=[]
 for bits in itertools.product([0,1],repeat=4):
  ii=region_indices(reg,bits);rr=rank(fixed[tag],k,ii);ss=rank(adaptive[tag],k,ii)
  pair=[abs(rr[0][1]-center)<=half,abs(ss[0][1]-center)<=half]
  scenarios.append({'lower_boundary_bits':list(bits),'fixed_value':float(rr[0][1]),'fixed_index':rr[0][0],'adaptive_subset_value':float(ss[0][1]),'adaptive_index':ss[0][0],'interval_membership_pair':pair,'changes_pair':pair!=basepair})
 near=max(abs(ef),abs(ea))<F('1e-3')
 tokens.append({k:old[k] for k in ['version','source','tag','region','metric','printed','half_width','verdict']}|{'fixed_indices':sorted(i for i in fixed[tag] if i in indices),'adaptive_indices':sorted(i for i in adaptive[tag] if i in indices),'MP_substituted_indices':[q['index'] for q in sens['rows'] if q['tag']==tag and q['index'] in indices],'fixed':record_rank(fr),'adaptive':record_rank(ar),'signed_relative_excess_fixed':str(ef),'signed_relative_excess_adaptive':str(ea),'relative_excess_float':[float(ef),float(ea)],'rounding_description':'inside or on interval' if ef==ea==0 else 'near-rounding-endpoint discrepancy (<1e-3)' if near else 'larger rounding discrepancy (>=1e-3)','vertical_axis_maximum':[bool(pts[fr[0][0],0]==0),bool(pts[ar[0][0],0]==0)],'region_boundary_maximum':[bool(pts[fr[0][0],2] in bounds),bool(pts[ar[0][0],2] in bounds)],'counterfactual_masks':scenarios,'unexported_producer_mask_comparison':'OPEN' if any(s['changes_pair'] for s in scenarios) else 'unchanged under these16 whole-ring assignments; producer run not recovered'})
ck('187 tokens and295adaptivepoints',len(tokens)==187 and sum(map(len,adaptive.values()))==295)
bridgerows=[]
for row in bridge['exact_bridges']:
 tag=row['tag'];i=row['index'];z=raw[tag];x,y=map(lambda t:F.from_float(float(t)),pts[i,:2]);g,gx,gy=map(lambda t:F.from_float(float(t)),z['jets'][i,:3]);u,v=map(lambda t:F.from_float(float(t)),z['velocity'][i]);c=F.from_float(float(params[tag]));T=abs(c*x*gx)+abs(u*gx)+abs(c*y*gy)+abs(v*gy)+abs(g)
 orig=next(q for state in ad['states'] if state['tag']==tag for q in state['points'] if q['index']==i)
 ratios={k:float(abs(F(val))/T) if T else None for k,val in row['exact'].items()};bridgerows.append({'tag':tag,'index':i,'region':next(k for k,(lo,hi) in enumerate(intervals) if lo<=nominal[i]<hi),'T':str(T),'absolute_over_T':ratios,'adaptive_estimated_error':orig['estimated_error'],'velocity_difference':[float(orig['V'][k]-z['velocity'][i,k]) for k in range(2)]})
regionbridge=[{'region':reg,'points':sum(x['region']==reg for x in bridgerows),'maximum_contribution_over_T':{k:max((x['absolute_over_T'][k] for x in bridgerows if x['region']==reg and x['absolute_over_T'][k] is not None),default=None) for k in bridge['exact_bridges'][0]['exact']}} for reg in range(5)]
q=bridge['exceptional_probe'][0];gxx=F(q['jets'][-1][3]);gxx_double=F.from_float(float(raw[q['tag']]['jets'][q['index'],3]));rel=abs(gxx_double-gxx)/abs(gxx);exception={'relative_gxx_error':float(rel),'multiple_of_64_epsilon':float(rel/F.from_float(float(64*np.finfo(float).eps))),'scope':'one local point; no propagated inverse error'}
provenance={}
for f in ['ADAPTIVE.json','ADAPTIVE_SUMMARY.json','MP_JETS.json','MP_SENSITIVITY.json','ARITHMETIC_BRIDGE.json']:
 p=V/f;g=json.loads(p.read_text());provenance[f]={'sha256':sha(p),'bytes':p.stat().st_size,'actual_keys':list(g),'started_utc':g.get('started_utc'),'updated_utc':g.get('updated_utc'),'finished_utc':g.get('finished_utc')}
for p in [Path(__file__),R/'NUMERICAL_REVIEW_RESOLUTION_PROOF.md',V/'producer_definition_static.py',V/'OPUS_NUMERICAL_REQUEST.txt',Path('independent_code/audit_common_residual_adaptive.py'),Path('independent_code/audit_common_residual_mp_jets.py')]:bindings[str(p)]=sha(p)
for name,g,driver in [('adaptive',ad,'independent_code/audit_common_residual_adaptive.py'),('MP',mpj,'independent_code/audit_common_residual_mp_jets.py')]:
 ck(name+' driver unchanged',g['driver_sha256']==sha(driver));ck(name+' final checkpoint timestamp',g['started_utc']<g['finished_utc']<=g['updated_utc'])
out={'status':'PASS_SCOPED_FINITE_ARRAYS','started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'count':len(checks),'checks':checks,'bindings':bindings,'tokens':tokens,'boundaries':boundary,'bridge_by_region':regionbridge,'bridge_witnesses':bridgerows,'exceptional_probe_ratio':exception,'raw_gate_provenance':provenance,'prior_request_projection_note':'token_results and controlled_rows were request-only aliases; largest_scalar_array_differences was a request-only projection. Original raw gate files unchanged by this checker. Their timestamps describe executing checkpoint writers, not post-run additions.','scope':'Finite represented values only. Quadrature-rule sensitivity conditional on shared binary64 jet. True inverse error OPEN; primary full-plane UNRESOLVED.'}
(V/'FINAL_SCOPE_CHECKS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print(out['status'],out['count']);print('boundary sensitive',sum(t['unexported_producer_mask_comparison']=='OPEN' for t in tokens));print('exception',exception)
print('refuted descriptions',{v:{d:sum(t['version']==v and t['verdict']=='REFUTED' and t['rounding_description']==d for t in tokens) for d in ['near-rounding-endpoint discrepancy (<1e-3)','larger rounding discrepancy (>=1e-3)']} for v in ['original_q3','revision153']})
