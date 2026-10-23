"""Independent finite arithmetic auditor. Imports no trial reconstruction module."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,gzip,math,re,sys,time,traceback
import numpy as np
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';C=V/'candidate_inverse';M=V/'candidate_mp_inverse'
checks=[];bindings={};start=time.perf_counter();outputs={};identity_count=0
CN=['V1','V2','Phi','dV2dy','tailV1','tailV2'];MN=['Jx','Jxx','Ix_outer','Ixx_outer','Ix_tail','Ixx_tail']
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=str(p)
 if p in bindings:
  if h is not None and h!=bindings[p]:ck('inconsistent duplicate binding '+p,False)
  return Path(p)
 q=hashlib.sha256(Path(p).read_bytes()).hexdigest()
 ck('binding '+p,(h is None or h==q)and(p not in bindings or bindings[p]==q));bindings[p]=q;return Path(p)
def deps(d):
 for p,h in d.get('bindings',{}).items():bind(p,h)
def f(z):return F.from_float(float(z))
def frac(z):return F(z)
def one_round_equal(a,b):return (math.isnan(a)and math.isnan(b))or a==b

def fields(x,y,j,v):
 g,gx,gy=j[:3];u=(2*x+v[0])*gx;w=(2*y+v[1])*gy;r=u+w-g
 nf=abs(u)+abs(w)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v[0]*gx+v[1]*gy)
 return [r,nf,nv,abs(r)/nf if nf else None,abs(r)/nv if nv else None]
def diff_terms(x,y,j,v,jp,w):
 rr=fields(x,y,j,v)[0];rp=fields(x,y,jp,w)[0]
 a=sum((v[k]-w[k])*j[k+1]for k in range(2));b=(2*x+w[0])*(j[1]-jp[1])+(2*y+w[1])*(j[2]-jp[2])-(j[0]-jp[0])
 aa=sum((v[k]-w[k])*jp[k+1]for k in range(2));bb=(2*x+v[0])*(j[1]-jp[1])+(2*y+v[1])*(j[2]-jp[2])-(j[0]-jp[0])
 ck('exact two jet identity',rr-rp==a+b==aa+bb)
 return [rr,rp,a,b,rr-rp,fields(x,y,j,v)[1],aa,bb]
def compare(low,high,double,floor,threshold):
 n=len(low);w=len(low[0]);pm=[];dm=[];zc=[0]*w;nc=[0]*w;fail=[]
 for k in range(w):
  bestp=F(-1);bestd=F(-1)
  for i in range(n):
   lo,hi,dd=low[i][k],high[i][k],double[i][k];a=abs(hi-lo);q=a/max(abs(hi),floor);ad=abs(hi-dd);den=max(abs(hi),abs(dd));qd=ad/den if den else F(0)
   if hi==0:zc[k]+=1
   if abs(hi)<floor:nc[k]+=1
   if q>threshold:fail.append([i,k,str(q)])
   if q>bestp:bestp=q;p=dict(component=k,index=i,relative=str(q),absolute=str(a))
   if qd>bestd:bestd=qd;d=dict(component=k,index=i,relative=str(qd),absolute=str(ad),both_zero=not bool(den))
  pm.append(p);dm.append(d)
 return dict(precision_maxima=pm,double_pure_relative_maxima=dm,zero_counts=zc,nearzero_counts=nc,precision_failed_entries=fail,precision_diagnostic_passed=not fail,count=n,floor=str(floor),threshold=str(threshold))

def chunks(folder,total,width,digits,expected_bindings):
 out=[];paths=sorted(folder.glob('chunk_*.json.gz'));ck('chunk files nonempty '+str(folder),bool(paths))
 for p in paths:
  bind(p);d=json.loads(gzip.decompress(p.read_bytes()));ck('exact chunk binding schema '+str(p),d['bindings']==expected_bindings);deps(dict(bindings={k:v for k,v in d['bindings'].items()if k!='selected_indices'}))
  ck('chunk schema '+str(p),d['schema']=='FINITE_MP_DECIMALS_V1'and d['total']==total and d['width']==width and d['digits']==digits and d['chunk_size']==64 and d['start']==len(out)and d['stop']==min(total,len(out)+64)and len(d['rows'])==d['stop']-d['start'])
  ck('chunk name '+str(p),p.name==f"chunk_{d['start']:07d}.json.gz")
  ck('chunk digest '+str(p),hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest()==d['rows_sha256'])
  for row in d['rows']:
   ck('row shape',len(row)==width)
   valid=all(isinstance(t,str)and len(t)<=2048 and re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',t)and ('e'not in t.lower()or abs(int(t.lower().split('e')[1]))<=1000)for t in row)
   ck('finite serialized decimals',valid);out.append([F(t)for t in row])
 ck('complete chunk interval '+str(folder),len(out)==total);return out

def moments(rows,node,weight,phase):
 pos=[F(0)for _ in MN];neg=pos.copy()
 for ds,t,w,ph in zip(rows,node,weight,phase):
  for k in range(2):
   ind=2*ph+k;z=w*ds[k]*(t if ph==0 else 1)
   if z>=0:pos[ind]+=z
   else:neg[ind]+=z
 return [a+b for a,b in zip(pos,neg)],(pos,neg)
def components(mm,y):
 return [-mm[2]-mm[4],mm[1]+y*(mm[3]+mm[5]),mm[0]+y*(mm[2]+mm[4]),mm[3]+mm[5],-mm[4],y*mm[5]]
def ledger(mm,pn,y):
 def item(p,n):
  return dict(positive=str(p),negative=str(n),total=str(p+n),sum_absolute=str(p-n),cancellation_ratio=str((p-n)/abs(p+n))if p+n else None)
 terms=[[(2,-1),(4,-1)],[(1,1),(3,y),(5,y)],[(0,1),(2,y),(4,y)],[(3,1),(5,1)],[(4,-1)],[(5,y)]]
 cs=[]
 for ts in terms:
  p=n=F(0)
  for i,a in ts:
   if a>=0:p+=a*pn[0][i];n+=a*pn[1][i]
   else:p+=a*pn[1][i];n+=a*pn[0][i]
  cs.append(item(p,n))
 ck('all component ledger totals',[F(z['total'])for z in cs]==components(mm,y))
 return dict(moments={k:item(a,b)for k,a,b in zip(MN,*pn)},components=dict(zip(CN,cs)))
try:
 bind(__file__);bind(R/'FINAL_FINITE_INVERSE_PROOF.md');bind(R/'FINAL_SELECTION_CORRECTION_PROOF.md');bind(R/'FINAL_CHUNK_SCHEMA_CORRECTION_PROOF.md');ck('assertions enabled',sys.flags.optimize==0)
 # Hand computed finite-sum manufacture, including both sign groups and zero-result behavior.
 mm,pn=moments([[F(2),F(-3)],[F(-4),F(5)],[F(6),F(-7)]],[F(3),F(4),F(5)],[F(2),F(3),F(4)],[0,1,2])
 ck('manufactured six moments',mm==list(map(F,[12,-18,-12,15,24,-28])))
 ck('manufactured six components',components(mm,F(2))==list(map(F,[-12,-44,36,-13,-24,-56])))
 ll=ledger(mm,pn,F(2));ck('manufactured cancellation',ll['components']['V1']['cancellation_ratio']=='3');ck('manufactured signed groups',ll['components']['V1']['positive']=='12'and ll['components']['V1']['negative']=='-24')
 zz=compare([[F(0)],[F(1)]],[[F(0)],[F(1)]],[[F(0)],[F(2)]],F(1,100),F(1,1000));ck('manufactured zeros maxima',zz['zero_counts']==[1]and zz['nearzero_counts']==[1]and zz['double_pure_relative_maxima'][0]['index']==1 and zz['double_pure_relative_maxima'][0]['relative']=='1/2')
 rules=json.loads(bind(C/'RULES_COMPLETE.json','1fefa11e0b74986a7d5d1a703dc7c6de5011241d6fc826ee2ba51699301b6816').read_text());mp=json.loads(bind(M/'MP_COMPLETE.json').read_text())
 for label,d,st in [('rules',rules,'COMPLETE_FINITE_RULES_REQUIRES_LOCAL_MP_INTEGRAND_MP_AND_FINAL_REVIEW'),('mp',mp,'COMPLETE_FINITE_MP_SENSITIVITY_REQUIRES_FINAL_REVIEW')]:
  ck(label+' completed',d['status']==st and d['count']==len(d['checks'])and all(z['passed']for z in d['checks']));deps(d)
  for p,h in d['artifacts'].items():bind(p,h)
 jets=np.load(bind(V/'actual_node_jets.npz'),allow_pickle=False);export=np.load(bind(V/'source_nodes_maps.npz','071b990c7a9ee3a91faeca5a1cc8c7d9ef6ef478f41ccd591fbe1ad5575d42d7'),allow_pickle=False)
 X=jets['X'];Y=jets['Y'];J=[[f(z)for z in row]for row in jets['own_jet']];JP=[[f(z)for z in row]for row in jets['producer_jet']]
 ck('positive admitted coordinates',len(X)==2304 and np.all(X>0)and np.all(Y>0)and np.array_equal(X,export['X'])and np.array_equal(Y,export['Y']))
 W=[[[f(export['V1_'+k][i]),f(export['V2_'+k][i])]for i in range(2304)]for k in ['map','ref']]
 arrays={};exact={};vel={}
 for tag,expected in [('A',2304),('B',2304),('C',30)]:
  z=np.load(C/(tag+'.npz'),allow_pickle=False);arrays[tag]=z;ids=list(map(int,z['indices']));man=json.loads(str(z['manifest']));deps(man)
  ck(tag+' completion manifest',man['status']=='COMPLETE'and man['completed']==man['total']==expected and len(ids)==expected)
  ck(tag+' unique ordered indices',len(set(ids))==expected and ids==sorted(ids));exact[tag]={};vel[tag]={}
  for q,i in enumerate(ids):
   x,y=f(X[i]),f(Y[i]);vv=list(map(f,z['velocity'][q]));rr=fields(x,y,J[i],vv);exact[tag][i]=rr;vel[tag][i]=vv
   ck(tag+' residual operands '+str(i),all(one_round_equal(float(a)if a is not None else float('nan'),float(b))for a,b in zip(rr,z['residual'][q])))
   for k in range(2):
    terms=diff_terms(x,y,J[i],vv,JP[i],W[k][i]);identity_count+=2
    ck(tag+' decomposition '+str((i,k)),all(float(a)==float(b)for a,b in zip(terms,z['decomposition'][q,k])))
  print('ROWS',tag,expected,datetime.now(timezone.utc).isoformat(),flush=True)
 ck('identity count',identity_count==rules['exact_identity_count']==18552)
 # Regional maxima of each pointwise ratio, using the stored once-rounded fields.
 regions=[('r<.1',0,.1),('.1<=r<1',.1,1),('1<=r<100',1,100),('r>=100',100,float('inf'))];rad=np.hypot(X,Y);summaries={}
 for tag in ['A','B']:
  ss=[];z=arrays[tag]
  for name,lo,hi in regions:
   ids=np.where((rad>=lo)&(rad<hi))[0];metrics={}
   for label,k in [('absR',0),('Rf',3),('Rv',4)]:
    vals=np.abs(z['residual'][ids,k]);ok=np.isfinite(vals);j=int(np.argmax(np.where(ok,vals,-np.inf)));i=int(ids[j]);metrics[label]=dict(index=i,value=float(vals[j]),x=float(X[i]),y=float(Y[i]),defined_count=int(ok.sum()),undefined_count=int((~ok).sum()))
   ss.append(dict(region=name,count=len(ids),metrics=metrics))
  ck('regional table '+tag,ss==rules['summaries'][tag]);summaries[tag]=ss
 stability=[]
 for rec in rules['stability']:
  i=rec['index'];rs=[exact[t][i][0]for t in ['A','B','C']];s=max(rs)-min(rs);d=max(abs(sum((vel[t][i][k]-W[0][i][k])*J[i][k+1]for k in range(2)))for t in ['A','B','C']);nf=exact['B'][i][1];rb=exact['B'][i][0]
  flag=nf>0 and s<=nf/F(10**8)and(s<=d/100 if d else s==0)
  ck('stability exact '+str(i),[str(s),str(d),str(nf)]==rec['exact_operands']and flag==rec['empirical_stable'])
  ratios={'spread_over_abs_R_B':s/abs(rb)if rb else None,'spread_over_velocity_term':s/d if d else None,'spread_over_Nf_B':s/nf if nf else None}
  for k,z in ratios.items():ck('stability ratio '+str((i,k)),(float(z)if z is not None else None)==rec[k])
  stability.append(dict(index=i,x=float(X[i]),y=float(Y[i]),S=str(s),D=str(d),Nf=str(nf),**{k:str(z)if z is not None else None for k,z in ratios.items()},empirical_stable=flag))
 outputs['regional_summaries']=summaries;outputs['stability']=stability;outputs['stability_maxima']={k:max(stability,key=lambda z:F(z[k])if z[k]is not None else F(-1))for k in ['S','spread_over_abs_R_B','spread_over_velocity_term','spread_over_Nf_B']}
 lc=json.loads(bind(M/'LOCAL_COMPLETE.json').read_text());deps(lc);ids=lc['indices'];ck('declared local selection',ids==mp['local_indices']==list(map(int,arrays['C']['indices'])))
 oldmp=json.loads(bind(V/'ACTUAL_MP_JETS.json').read_text());oldids=[z['index']for z in oldmp['rows']];ck('thirteen new targets complement prior17',len(oldids)==17 and set(oldids)<=set(ids)and sorted(set(ids)-set(oldids))==rules['new_local_mp_indices'])
 l72=chunks(M/'local_72',len(ids),4,72,dict(mp['bindings'],selected_indices=json.dumps(ids)));l108=chunks(M/'local_108',len(ids),4,108,dict(mp['bindings'],selected_indices=json.dumps(ids)))
 ck('local summary actual rows',l72==[[F(z)for z in row]for row in lc['rows72']]and l108==[[F(z)for z in row]for row in lc['rows108']])
 outputs['local']={}
 for name,low,high,dd in [('local',l72,l108,[J[i]for i in ids]),('producer',[r[:3]for r in l72],[r[:3]for r in l108],[JP[i]for i in ids])]:
  cc=compare(low,high,dd,F(1,10**60),F(1,10**52))
  for k,z in cc.items():ck(name+' diagnostic '+k,z==lc[name][k])
  for key in ['precision_maxima','double_pure_relative_maxima']:
   for rr in cc[key]:rr['export_index']=ids[rr['index']];rr['x']=float(X[rr['export_index']]);rr['y']=float(Y[rr['export_index']]);rr['relative_float']=float(F(rr['relative']));rr['absolute_float']=float(F(rr['absolute']))
  outputs['local'][name]=cc
 outputs['witnesses']=[]
 ck('declared integrand selection',mp['integrand_indices']==rules['mp_integrand_indices']==[455,1139,1240,1944,2280])
 for i in mp['integrand_indices']:
  gg=np.load(bind(M/f'geometry_{i}.npz'),allow_pickle=False);gd=json.loads(str(gg['manifest']));deps(gd);ww=json.loads(bind(M/f'witness_{i}.json').read_text())
  for p,h in ww['geometry'].items():bind(p,h)
  ck('geometry target '+str(i),float(gg['x'])==X[i]and float(gg['y'])==Y[i]and ww['index']==i and ww['x']==X[i]and ww['y']==Y[i])
  n=len(gg['node']);ck('geometry finite positive '+str(i),np.isfinite(gg['node']).all()and np.isfinite(gg['weight']).all()and np.all(gg['node']>0)and np.all(gg['weight']>0)and set(map(int,gg['phase']))=={0,1,2})
  bb=arrays['B'];ref=[bb['velocity'][i,0],bb['velocity'][i,1],bb['Phi'][i],bb['dV2dy'][i],*bb['tail_velocity'][i]]
  ck('same B geometry outputs '+str(i),np.array_equal(gg['reference'],ref)and np.array_equal(gg['metadata'],bb['metadata'][i]))
  a72=chunks(M/f'integrand_{i}_72',n,2,72,ww['geometry']);a108=chunks(M/f'integrand_{i}_108',n,2,108,ww['geometry']);ds=[[f(z)for z in row]for row in gg['derivatives']]
  cc=compare(a72,a108,ds,F(1,10**80),F(1,10**48))
  for key in ['precision_maxima','double_pure_relative_maxima']:
   for rr in cc[key]:rr['phase']=int(gg['phase'][rr['index']]);rr['physical_y']=float(gg['node'][rr['index']])
  for k,z in cc.items():ck('integrand diagnostic '+str((i,k)),z==ww['integrand'][k])
  allmom={};allcomp={};led={};nodes=list(map(f,gg['node']));weights=list(map(f,gg['weight']));phases=list(map(int,gg['phase']));y=f(Y[i])
  for name,rows in [('D',ds),('M72',a72),('M108',a108)]:
   mm,pn=moments(rows,nodes,weights,phases);allmom[name]=mm;allcomp[name]=components(mm,y);led[name]=ledger(mm,pn,y)
   ck('recomputed exact moments '+str((i,name)),dict(zip(MN,map(str,mm)))==ww['moments'][name])
  for k,name in enumerate(CN):
   b=f(ref[k]);d=allcomp['D'][k];m72=allcomp['M72'][k];m108=allcomp['M108'][k];expected=dict(component=name,total=str(m108-b),integrand=str(m108-d),finite_arithmetic=str(d-b),precision_change=str(m108-m72),B=str(b),D=str(d),M72=str(m72),M108=str(m108))
   ck('exact component decomposition '+str((i,name)),expected==ww['components'][k]and m108-b==(m108-d)+(d-b))
  rr=ww['residual_change'];changes={k:sum(F(ww['components'][j][k])*J[i][j+1]for j in range(2))for k in ['total','integrand','finite_arithmetic']};nf=f(bb['residual'][i,1]);ck('held gradient identity '+str(i),changes['total']==changes['integrand']+changes['finite_arithmetic'])
  ck('held gradient recorded '+str(i),all(str(z)==rr[k]for k,z in changes.items())and nf>0 and str(nf)==rr['B_Nf_stored_float']and str(changes['total']/nf)==rr['total_over_B_Nf'])
  for key in ['precision_maxima','double_pure_relative_maxima']:
   for rr2 in cc[key]:rr2['relative_float']=float(F(rr2['relative']));rr2['absolute_float']=float(F(rr2['absolute']))
  outputs['witnesses'].append(dict(index=i,x=float(X[i]),y=float(Y[i]),nodes=n,integrand=cc,ledgers=led,components=ww['components'],residual_change=rr))
  print('EXACT_WITNESS',i,n,datetime.now(timezone.utc).isoformat(),flush=True)
 ck('all empirical flags',all(z['empirical_stable']for z in stability)and mp['precision_diagnostics_passed'])
 ck('MP bookkeeping counts',mp['exact_component_identity_count']==30 and mp['exact_residual_identity_count']==5 and mp['bookkeeping_identity_count']==35)
 for p,h in list(bindings.items()):ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
 status='PASS_FINITE_RECOMPUTATION_REQUIRES_ACTUAL_REVIEW'
except Exception:
 status='FAIL';error=traceback.format_exc();print(error,flush=True)
out=dict(status=status,utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,count=len(checks),checks=checks,bindings=bindings,exact_two_jet_identity_count=identity_count,outputs=outputs,scope='Exact finite stored-operand checks; all inverse error enclosures and primary IPM endpoint OPEN.')
if status=='FAIL':out['error']=error
(V/'FINAL_SUMMARY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(status,len(checks),out['elapsed_seconds'],flush=True)
if status=='FAIL':raise SystemExit(1)
