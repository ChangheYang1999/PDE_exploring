"""Independent finite arithmetic audit. No candidate/producer arithmetic imports."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,sys,json,hashlib,time,traceback,math,csv
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
if sys.flags.optimize:raise SystemExit('optimized Python prohibited for verification')
sys.set_int_max_str_digits(1000000)
import numpy as np
import larger_node_independent_arithmetic as ar
R=Path('research/hydrostatic_larger_node_audit');BASE=R/'verification'
RULES={'A':dict(order=48,tail_order=160,split=64.,inner=.125,partition='dyadic'),'B':dict(order=64,tail_order=192,split=128.,inner=.125,partition='dyadic'),'C':dict(order=88,tail_order=256,split=512.,inner=.125,partition='ratio')}
SHAPES={'velocity':(2,),'Phi':(),'dV2dy':(),'tail_velocity':(2,),'metadata':(10,),'residual':(5,)}
META=['R_split','inner_panels','outer_panels','inner_nodes','outer_nodes','tail_nodes','minimum_panel_width','rounded_endpoint_nodes','x_axis_imposed','y_axis_imposed']
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');t.replace(p)
def arrays(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
def six(a,i):return list(map(ar.f,np.r_[a['velocity'][i],a['Phi'][i],a['dV2dy'][i],a['tail_velocity'][i]]))
class Audit:
 def __init__(self,V,fixture):self.V=V;self.fixture=fixture;self.bindings={};self.aliases={};self.checks=[];self.scalars=0;self.outputs={}
 def ck(self,name,b,e=None):
  self.checks.append(dict(name=name,passed=bool(b),evidence=e))
  if not b:raise AssertionError((name,e))
 def scalar(self,b,where):
  self.scalars+=1
  if not b:raise ArithmeticError(where)
 def bind(self,p,h=None):
  p=str(p);z=sha(p);alias=str(Path(p).resolve());self.ck('binding '+p,(h is None or h==z)and(p not in self.bindings or self.bindings[p]==z)and(alias not in self.aliases or self.aliases[alias]==z));self.bindings[p]=z;self.aliases[alias]=z;return Path(p)
 def json(self,p,h=None):return json.loads(self.bind(p,h).read_text())
 def gate(self,p,status):
  d=self.json(p);self.ck('semantic gate '+str(p),d['status']==status and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']))
  for p,h in d.get('bindings',{}).items():self.bind(p,h)
  return d
 def artifact(self,p,manifest):
  self.ck('listed artifact '+str(p),str(p)in manifest);return self.bind(p,manifest[str(p)])
 def load_snapshot(self,p,tag,label,ids,xy,jets,artifacts):
  a=arrays(self.artifact(p,artifacts));self.ck('snapshot members '+tag+label,set(a)==set(SHAPES)|{'indices','xy','jets','manifest'})
  m=json.loads(str(a['manifest']));n=len(ids)
  self.ck('snapshot complete '+tag+label,m['schema']=='LARGER_NODE_V1'and m['label']==tag+'_'+label and m['rule']==RULES[label]and m['status']=='COMPLETE'and type(m['completed'])is int and m['completed']==m['total']==n)
  for p,h in m['bindings'].items():self.bind(p,h)
  self.ck('snapshot indices and targets '+tag+label,a['indices'].dtype==np.dtype('int64')and np.array_equal(a['indices'],ids)and np.array_equal(a['xy'],xy[ids])and np.array_equal(a['jets'],jets[ids]))
  for k,shape in SHAPES.items():
   self.ck('snapshot shape '+tag+label+k,a[k].dtype==np.dtype('float64')and a[k].shape==(n,)+shape)
   if k!='residual':self.ck('snapshot finite '+tag+label+k,np.isfinite(a[k]).all())
  before=self.scalars
  for pos,i in enumerate(ids):
   exact=ar.residual(*map(ar.f,xy[i]),list(map(ar.f,jets[i])),list(map(ar.f,a['velocity'][pos])))
   for k,(q,z)in enumerate(zip(exact,a['residual'][pos])):
    self.scalar(ar.same_round(q,z),('rounded arithmetic',tag,label,int(i),k))
    if k in [1,2]:self.scalar(q>=0 and(q==0 or z>0),('denominator representation',tag,label,int(i),k))
  self.ck('independent all-row arithmetic '+tag+label,True,dict(rows=n,scalar_assertions=self.scalars-before));return a
 def check_selection(self,s,xy,j,B,sums):
  reasons={}
  def add(i,text):
   if i is not None:reasons.setdefault(str(int(i)),[]).append(text)
  for row in sums:
   for key,item in row['metrics'].items():add(item['index'],'B '+row['region']+' '+key)
  for k in range(2):add(np.argmax(abs(B['velocity'][:,k])),'absolute V'+str(k+1))
  add(np.argmax(abs(j[:,3])),'absolute gxx')
  proxies=[int(i)for i,reasons0 in s['reasons'].items()if 'five-point gxx proxy'in reasons0]
  self.ck('one provenance-backed FD proxy',len(proxies)==1)
  add(proxies[0],'five-point gxx proxy')
  for k in [1,2,6]:
   add(np.argmax(B['metadata'][:,k]),'metadata maximum '+str(k));add(np.argmin(B['metadata'][:,k]),'metadata minimum '+str(k))
  for i in [0,len(xy)//2,len(xy)-1]:add(i,'deterministic endpoint/middle')
  self.ck('reconstructed selection apart from proxy provenance',s['indices']==sorted(map(int,reasons))and s['reasons']==reasons)
  rr=np.hypot(xy[:,0],xy[:,1]);expected={str(i):float(max(1,rr[i])*2**-10/rr[i])for i in s['indices']}
  self.ck('selected finite-difference step metadata',s['selected_h_over_r']==expected and s['proxy_step']=='2^-10 max(1,r)')
 def spreads(self,xy,j,ids,A,B,C,declared):
  out=[];self.ck('selected comparison coverage',len(declared)==len(ids))
  for pos,i in enumerate(ids):
   vv=[six(A,pos),six(B,i),six(C,pos)];rs=[ar.residual(*map(ar.f,xy[i]),list(map(ar.f,j[i])),v)[0]for v in vv];nf=ar.residual(*map(ar.f,xy[i]),list(map(ar.f,j[i])),vv[1])[1];S=max(rs)-min(rs);base=abs(rs[1]);pairs=[];allpairs=[]
   for k in range(6):
    for a,b in [(0,1),(2,1),(2,0)]:
     q=dict(component=k+1,pair=[a,b],**ar.discrepancy(vv[a][k],vv[b][k]));allpairs.append(q)
     if k<2:pairs.append(q)
   d=dict(rule_order=['A','B','C'],R=list(map(str,rs)),spread=str(S),B_Nf=str(nf),spread_over_abs_B_R=str(S/base)if base else None,spread_over_B_Nf=str(S/nf)if nf else None,zero_B_R=not bool(base),zero_B_Nf=not bool(nf),empirical_pass=bool(S<=base/100 and S<=nf/10**8)if base and nf else None,components=pairs,index=i,x=float(xy[i,0]),y=float(xy[i,1]))
   self.scalar(d==declared[pos],('selected exact comparison',i));d['all_six_component_pairs']=allpairs;out.append(d)
  return out
 def run(self):
  V=self.V;C=V/'candidate';O=V/'mp'
  for p in [__file__,ar.__file__,R/'FINAL_ARITHMETIC_PROOF.md',R/'FINAL_DIAGNOSTIC_ORDER_PROOF.md',R/'FINAL_CHECKER_ASSEMBLY_PROOF.md',R/'FINAL_DESIGN_REVIEW_RESOLUTION_PROOF.md',R/'FINAL_GEOMETRY_DTYPE_CORRECTION_PROOF.md']:self.bind(p)
  self.gate(BASE/'FINAL_ARITHMETIC_MANUFACTURES.json','PASS_INDEPENDENT_FINITE_ARITHMETIC_MANUFACTURES')
  if not self.fixture:
   self.gate(BASE/'FINAL_CHECKER_MANUFACTURES.json','PASS_SYNTHETIC_INTEGRATED_LARGER_NODE_FINAL_CHECKER')
   self.gate(BASE/'OPTIMIZATION_MANUFACTURES.json','PASS_OPTIMIZATION_REFUSAL')
   self.bind(R/'FINAL_INTEGER_LIMIT_AND_ADMISSION_PROOF.md','e67f08a66bb529832900fe2a65faa5072edd03e25e9d9bc9f1d88eae608e868e')
   self.bind(BASE/'center_review_schema_failure/FAILURE.json','10264ab22de1c1aacecc9082e925e52ac8ad24044739afb953358a1b9070feef')
   self.bind(BASE/'center_review_schema_failure/check_larger_node_center_reuse.py','55bf90cb392eb5e8b8e04e4a426d7b8c1410efc32407f2a52fc3668eddd840ac')
   for fn in ['JOB.json','MP_JOB.json']:
    self.ck('required heavy job record '+fn,(V/fn).is_file())
    job=self.json(V/fn);p=Path('/proc')/str(job['pid'])
    if p.exists():
     stat=(p/'stat').read_text().rsplit(') ',1)[1].split()[0];cmd=(p/'cmdline').read_bytes();self.ck('heavy process ceased '+fn,stat=='Z'or not any(s in cmd for s in [b'run_larger_node_audit.py',b'launch_larger_node_mp.py',b'run_larger_node_mp.py']))
  inp=self.json(V/'INPUTS.json');states=inp['states'];expected=[(2,1)]if self.fixture else[(224,56),(192,48)]
  self.ck('exact input state order',[(s['N'],s['M'])for s in states]==expected)
  for s in states:self.bind(s['path'],s['sha256'])
  candidate=self.gate(C/'COMPLETE.json','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW')
  for p,h in candidate['artifacts'].items():self.bind(p,h)
  self.ck('candidate source sequence',[s['source']for s in candidate['results']]==states)
  mpout=self.gate(O/'COMPLETE.json','COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT')
  self.ck('MP synthetic fence',mpout['synthetic_only']is self.fixture)
  for p,h in mpout['artifacts'].items():self.bind(p,h)
  self.ck('MP binds same candidate completion',mpout['bindings'][str(C/'COMPLETE.json')]==sha(C/'COMPLETE.json'))
  execution=mpout['execution_admission'];ad=self.json(execution['path'],execution['sha256']);self.ck('exact admission record',ad==execution['record'])
  policy=self.json(ad['policy_path'],ad['policy_sha256']);ret=self.json(Path(execution['path']).with_suffix('.result.json'))
  self.ck('wrapper completed successfully',ret['child_returncode']==0 and ret['wrapper_pid']==ad['wrapper_pid']and all(ret[k]==v for k,v in ad.items()))
  self.ck('stable process policy',policy['schema']=='IPM318_MP_POLICY_V1'and policy['synthetic_only']is self.fixture and policy['nice']==19 and policy['memory_limit_bytes']==14*1024**3 and policy['timeout_seconds']==(180 if self.fixture else 14400))
  self.bind('independent_code/run_larger_node_mp.py',policy['driver_sha256']);self.bind('independent_code/launch_larger_node_mp.py',policy['wrapper_sha256'])
  self.ck('numeric versions recorded',all(isinstance(mpout['versions'][k],str)and mpout['versions'][k]for k in ['python','numpy','torch','mpmath','numeric_pickle']))
  self.ck('MP state coverage',[(s['N'],s['M'])for s in mpout['results']]==expected)
  results=[];regional_csv=[]
  for st,ms in zip(candidate['results'],mpout['results']):
   N=st['N'];tag='N'+str(N);n=N*st['M'];self.ck('state completed file '+tag,self.json(self.artifact(C/(tag+'_COMPLETE.json'),candidate['artifacts']))==st)
   d=arrays(self.artifact(C/(tag+'_targets.npz'),candidate['artifacts']));self.ck('target schema '+tag,set(d)=={'xy','jets'}and d['xy'].shape==(n,2)and d['jets'].shape==(n,4)and all(a.dtype==np.dtype('float64')and np.isfinite(a).all()for a in d.values())and(d['xy']>0).all());xy,j=d['xy'],d['jets']
   sel=self.json(self.artifact(C/(tag+'_SELECTION.json'),candidate['artifacts']));ids=sel['indices'];self.ck('selected indices '+tag,ids==st['selected']['indices']==st['local_mp_indices']==sorted(set(ids))and all(type(i)is int and 0<=i<n for i in ids))
   B=self.load_snapshot(C/(tag+'_B.npz'),tag,'B',list(range(n)),xy,j,candidate['artifacts']);A=self.load_snapshot(C/(tag+'_A.npz'),tag,'A',ids,xy,j,candidate['artifacts']);CC=self.load_snapshot(C/(tag+'_C.npz'),tag,'C',ids,xy,j,candidate['artifacts'])
   sums=ar.summarize(xy,B['residual']);self.ck('all regional summaries '+tag,sums==st['region_summaries']);self.check_selection(sel,xy,j,B,sums)
   self.ck('selection bound to exact arrays '+tag,sel['B_sha256']==sha(C/(tag+'_B.npz'))and sel['target_sha256']==sha(C/(tag+'_targets.npz')))
   comp=self.spreads(xy,j,ids,A,B,CC,st['comparisons']);self.ck('metadata columns '+tag,st['metadata_columns']==META)
   valid=[i for i in range(n)if math.isfinite(B['residual'][i,3])];witness=max(valid,key=lambda i:float(B['residual'][i,3]));self.ck('first global Rf witness '+tag,st['integrand_mp_indices']==[witness]and[w['index']for w in ms['witnesses']]==[witness]and ms['B_Rf_undefined_count']==n-len(valid))
   local=ms['local'];self.ck('local MP coverage '+tag,local['indices']==ids and local==self.json(self.artifact(O/(tag+'_LOCAL_COMPLETE.json'),mpout['artifacts'])))
   lb=local['chunk_bindings'];self.ck('local chunk binding metadata '+tag,lb['state_N']==str(N)and json.loads(lb['selected_indices'])==ids)
   for p,h in lb.items():
    if p not in ['state_N','selected_indices']:self.bind(p,h)
   def mpbind(p):return self.artifact(p,mpout['artifacts'])
   lr={dg:ar.read_chunks(O/(tag+'_local_'+str(dg)),len(ids),4,dg,lb,mpbind)for dg in [72,108]}
   self.ck('local decimal rows equal chunks '+tag,all(lr[dg]==[list(map(ar.decimal,row))for row in local['rows'+str(dg)]]for dg in [72,108]))
   ld=[[ar.f(z)for z in j[i]]for i in ids];lcmp=ar.compare(lr[72],lr[108],ld,F('1e-60'),F('1e-50'));self.ck('independent local precision comparison '+tag,lcmp=={k:v for k,v in local['comparison'].items()if k!='scope'} and local['comparison']['scope']=='Finite recorded decimal comparisons, not certified errors.')
   bz=[sum(row[k]==dd[k]==0 for row,dd in zip(lr[108],ld))for k in range(4)];self.ck('local both-zero undefined counts '+tag,bz==local['both_zero_counts'])
   locs={key:[dict(z,original_index=ids[z['index']],x=float(xy[ids[z['index']],0]),y=float(xy[ids[z['index']],1]))for z in lcmp[key]]for key in ['precision_maxima','double_pure_relative_maxima']};self.ck('local maximizing locations '+tag,locs==local['locations'])
   localfailed=[dict(original_index=ids[a],component=b,scaled=c,x=float(xy[ids[a],0]),y=float(xy[ids[a],1]))for a,b,c in lcmp['precision_failed_entries']];wout=[]
   for w in ms['witnesses']:
    index=w['index'];xx,yy=map(ar.f,xy[index]);self.ck('witness serialized complete '+tag,w==self.json(self.artifact(O/(tag+'_witness_'+str(index)+'.json'),mpout['artifacts'])))
    self.ck('witness coordinates '+tag,ar.f(w['x'])==xx and ar.f(w['y'])==yy)
    gp=self.artifact(w['geometry'],mpout['artifacts']);g=arrays(gp);gm=json.loads(str(g['manifest']));self.ck('geometry exact manifest '+tag,gm==dict(N=N,index=index,bindings=mpout['bindings'],rule=RULES['B']))
    self.ck('geometry fields '+tag,set(g)=={'node','weight','phase','derivatives','reference','metadata','manifest','x','y'} and g['x'].shape==g['y'].shape==() and ar.f(g['x'])==xx and ar.f(g['y'])==yy)
    total=len(g['node']);self.ck('geometry dimensions '+tag,total==w['nodes']and g['weight'].shape==g['phase'].shape==(total,)and g['derivatives'].shape==(total,2)and g['reference'].shape==(6,)and g['metadata'].shape==(10,))
    self.ck('geometry dtypes '+tag,g['phase'].dtype==np.dtype('int8')and all(z.dtype==np.dtype('float64')for k,z in g.items()if k not in ['phase','manifest']))
    sets=[set(g['node'][g['phase']==k])for k in range(3)];self.ck('disjoint phase nodes '+tag,all(not sets[a]&sets[b]for a,b in [(0,1),(0,2),(1,2)]))
    self.ck('geometry finite positive '+tag,all(np.isfinite(a).all()for k,a in g.items()if k!='manifest')and(g['node']>0).all()and(g['weight']>0).all()and set(g['phase'])=={0,1,2}and np.all(np.diff(g['phase'])>=0))
    self.ck('geometry B replay reference '+tag,g['reference'].tobytes()==np.r_[B['velocity'][index],B['Phi'][index],B['dV2dy'][index],B['tail_velocity'][index]].tobytes()and g['metadata'].tobytes()==B['metadata'][index].tobytes())
    gb=w['geometry_bindings'];self.ck('geometry chunk binding '+tag,gb==dict(mpout['bindings'],**{str(gp):sha(gp)}))
    rows={dg:ar.read_chunks(O/(tag+'_integrand_'+str(index)+'_'+str(dg)),total,2,dg,gb,mpbind)for dg in [72,108]};dd=[[ar.f(z)for z in row]for row in g['derivatives']];icmp=ar.compare(rows[72],rows[108],dd,F('1e-80'),F('1e-50'))
    for key in ['precision_maxima','double_pure_relative_maxima']:
     for z in icmp[key]:z.update(phase=int(g['phase'][z['index']]),physical_y=float(g['node'][z['index']]))
    self.ck('independent integrand precision comparison '+tag,icmp=={k:v for k,v in w['integrand'].items()if k!='scope'} and w['integrand']['scope']=='Finite recorded decimal comparisons, not certified errors.')
    bzero=[sum(row[k]==old[k]==0 for row,old in zip(rows[108],dd))for k in range(2)];self.ck('integrand both-zero undefined counts '+tag,bzero==w['both_zero_counts'])
    fl=[dict(node=a,component=b,scaled=c,phase=int(g['phase'][a]),physical_y=float(g['node'][a]),target=index)for a,b,c in icmp['precision_failed_entries']];self.ck('failed integrand locations '+tag,fl==w['failed_locations'])
    ns=list(map(ar.f,g['node']));ws=list(map(ar.f,g['weight']));ph=list(map(int,g['phase']));mom={};comps={};ledgers={}
    for key,rr in [('D',dd),('M72',rows[72]),('M108',rows[108])]:
     mm,positive,negative=ar.moments(rr,ns,ws,ph);mom[key]=dict(zip(ar.MOMENTS,map(str,mm)));comps[key]=ar.components(mm,yy);ledgers[key]=ar.ledgers(mm,positive,negative,yy)
    self.ck('six independent exact moments '+tag,mom==w['moments']);self.ck('independent signed moment/component ledgers '+tag,ledgers==w['ledgers'])
    bref=six(B,index);parts=[]
    for k,name in enumerate(ar.COMPONENTS):
     totalc=comps['M108'][k]-bref[k];dj=comps['M108'][k]-comps['D'][k];da=comps['D'][k]-bref[k];self.scalar(totalc==dj+da,('component identity',N,index,k));parts.append(dict(component=name,B=str(bref[k]),D=str(comps['D'][k]),M72=str(comps['M72'][k]),M108=str(comps['M108'][k]),total=str(totalc),integrand=str(dj),finite_arithmetic=str(da),precision_change=str(comps['M108'][k]-comps['M72'][k])))
    self.ck('six exact component decompositions '+tag,parts==w['components'])
    jj=list(map(ar.f,j[index]));jp=lr[108][ids.index(index)];change=sum((comps['M108'][k]-bref[k])*jj[k+1]for k in range(2));ij=sum((comps['M108'][k]-comps['D'][k])*jj[k+1]for k in range(2));ia=sum((comps['D'][k]-bref[k])*jj[k+1]for k in range(2));nf=ar.f(B['residual'][index,1]);self.ck('positive stored witness Nf '+tag,nf>0)
    cr=dict(total=str(change),integrand=str(ij),finite_arithmetic=str(ia),stored_B_Nf=str(nf),total_over_stored_B_Nf=str(change/nf));fc=ar.four(xx,yy,jj,jp,bref,comps['M108']);self.ck('exact residual change and cross identity '+tag,cr==w['residual_change']and fc==w['four_combinations']and change==ij+ia==F(fc['R01'])-F(fc['R00']))
    wout.append(dict(index=index,x=float(xx),y=float(yy),nodes=total,precision_diagnostic_passed=icmp['precision_diagnostic_passed'],both_zero_counts=bzero,failed_locations=fl,components=parts,residual_change=cr,four_combinations=fc))
   for region in sums:
    for metric,z in region['metrics'].items():
     if z['index']is not None:regional_csv.append(dict(N=N,region=region['region'],metric=metric,index=z['index'],x=z['x'],y=z['y'],value=z['value'],R=z['fields'][0],Nf=z['fields'][1],Nv=z['fields'][2],Rf=z['fields'][3],Rv=z['fields'][4]))
   results.append(dict(N=N,M=st['M'],source=st['source'],points=n,regional_summaries=sums,selected_count=len(ids),selected_comparisons=comp,local_comparison=lcmp,local_locations=locs,local_failed_locations=localfailed,local_both_zero_counts=bz,witnesses=wout,FD_selector_scope='Argmax only backed by frozen executed selection code; absent full FD array is not independently recomputed',producer_raw_Fmax=st.get('producer_solver_nodes_Fmax'),producer_raw_Fmax_scope='Producer metadata only, not independently authenticated historical residual'))
  precision=all(s['local_comparison']['precision_diagnostic_passed']and all(w['precision_diagnostic_passed']for w in s['witnesses'])for s in results);self.ck('overall MP diagnostic flag',precision==mpout['precision_diagnostics_passed'])
  self.outputs=dict(states=results,precision_diagnostics_passed=precision,region_maxima_csv=regional_csv,scope='Exact finite-array arithmetic and selected MP checks. No integral error enclosure, historical map authentication, continuum claim or primary IPM endpoint.')
  if not self.fixture:
   center=self.gate(V/'CENTER_REUSE_CHECKS.json','PASS_EXACT_CENTER_REUSE');self.ck('center source coverage',[(r['N'],r['state_sha256'])for r in center['results']]==[(r['N'],r['source']['sha256'])for r in results]);self.outputs['center_evidence_scope']='224 completed exact source and semantic summary;192 additionally named polynomial application equalities. Both source hashes and exact defining coefficients bound.';self.outputs['center_comparisons']=[dict(z,B_core_max=st['regional_summaries'][0]['metrics']['Rf']['value'],B_core_to_center_limit=(float(ar.f(st['regional_summaries'][0]['metrics']['Rf']['value'])/F(z['core_axis_limit_exact']))if st['regional_summaries'][0]['metrics']['Rf']['value']is not None and F(z['core_axis_limit_exact'])else None))for z,st in zip(center['results'],results)]
  for p,h in list(self.bindings.items()):self.scalar(sha(p)==h,('stable binding',p))
  self.ck('all final bindings remain current',True,len(self.bindings))
  return self.outputs

def main():
 fixture=len(sys.argv)>1
 if fixture:
  if not(len(sys.argv)==3 and sys.argv[1]=='--fixture'):raise ValueError('explicit fixture flag')
  V=Path(sys.argv[2]);V.resolve().relative_to((BASE/'mp_driver_manufactures').resolve())
 else:V=BASE
 target=V/'FINAL_ARITHMETIC_CHECKS.json';a=Audit(V,fixture);started=now();tick=time.monotonic()
 if target.exists():target.rename(V/('FINAL_ARITHMETIC_CHECKS_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json'))
 try:
  a.run();status='PASS_SYNTHETIC_FINAL_ARITHMETIC'if fixture else'PASS_FINITE_LARGER_NODE_ARITHMETIC_REQUIRES_FINAL_REVIEW'
 except Exception:
  status='FAIL';a.outputs['error']=traceback.format_exc();print(a.outputs['error'],flush=True)
 out=dict(status=status,integer_string_limit=sys.get_int_max_str_digits(),python_flags=repr(sys.flags),synthetic_only=fixture,started_utc=started,finished_utc=now(),elapsed_seconds=time.monotonic()-tick,count=len(a.checks),scalar_assertion_count=a.scalars,checks=a.checks,bindings=a.bindings,outputs=a.outputs);write(target,out);print(status,len(a.checks),a.scalars,out['elapsed_seconds'],flush=True)
 if status=='FAIL':raise SystemExit(1)
if __name__=='__main__':main()
