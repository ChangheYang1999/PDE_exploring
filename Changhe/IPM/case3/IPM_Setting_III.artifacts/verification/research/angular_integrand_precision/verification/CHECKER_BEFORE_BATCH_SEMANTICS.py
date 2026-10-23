"""Independent exact rational recomputation of result333 frozen operand records."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,gzip,hashlib,re,sys
import numpy as np
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_integrand_precision';V=R/'verification';C=V/'candidate';checks=[];bindings={};nscalar=0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest()
 if p.read_bytes()!=b or(h is not None and h!=a):raise AssertionError('unstable binding '+str(p))
 bindings[str(p)]=a;return b
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError(n)
def ex(a):return F(float(a))
def decimal(s):
 if not isinstance(s,str)or len(s)>2048 or re.fullmatch(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?',s)is None:raise ValueError('invalid decimal')
 if 'e'in s.lower()and abs(int(s.lower().split('e')[1]))>1000:raise ValueError('decimal exponent')
 return F(s)
def load(p):
 with np.load(p,allow_pickle=False)as z:return {k:z[k]for k in z.files}
def fields(x,y,j,v):
 a=(2*x+v[0])*j[1];b=(2*y+v[1])*j[2];r=a+b-j[0];nf=abs(a)+abs(b)+abs(j[0]);nv=abs(j[0])+abs(x*j[1]+y*j[2])+abs(v[0]*j[1]+v[1]*j[2])
 if not(abs(r)<=nf and abs(r)<=2*nv and(nf!=0 or r==0)and(nv!=0 or r==0)):raise AssertionError('finite bound')
 return dict(R=r,Nf=nf,Nv=nv,Rf=abs(r)/nf if nf else None,Rv=abs(r)/nv if nv else None)
def serial(d):return {k:str(a)if a is not None else None for k,a in d.items()}
def moment(weights,values):return sum((a*b for a,b in zip(weights,values)),F(0))
def components(g,rows):
 w2=list(map(ex,g['w2']));wt=list(map(ex,g['wt']));cols=list(zip(*rows));out={'V1':-moment(wt,cols[0])}
 for e,k in enumerate([1,2,3]):out['V2_'+str(e)]=moment(w2,cols[k]);out['tail_'+str(e)]=moment(wt,cols[k])
 return out
def read_chunks(directory,total,digits,width,expected_bindings,artifacts):
 directory=Path(directory).resolve();expected=[directory/f'chunk_{i:07d}.json.gz'for i in range(0,total,64)];ck('chunk filenames '+str(directory),set(directory.glob('chunk_*.json.gz'))==set(expected));rows=[]
 for start,p in zip(range(0,total,64),expected):
  ck('listed chunk '+str(p),str(p)in artifacts);d=json.loads(gzip.decompress(bind(p,artifacts[str(p)])));stop=min(start+64,total)
  signature=dict(schema='FINITE_MP_DECIMALS_V1',total=total,digits=digits,width=width,chunk_size=64,bindings=expected_bindings)
  ck('exact chunk schema '+str(p),set(d)==set(signature)|{'start','stop','rows','rows_sha256'}and all(d[k]==v for k,v in signature.items())and type(d['start'])is int and d['start']==start and type(d['stop'])is int and d['stop']==stop and len(d['rows'])==stop-start and all(isinstance(row,list)and len(row)==width for row in d['rows']))
  ck('row digest '+str(p),hashlib.sha256(json.dumps(d['rows'],separators=(',',':'),ensure_ascii=True).encode()).hexdigest()==d['rows_sha256']);rows.extend([[decimal(v)for v in row]for row in d['rows']])
 ck('complete rows '+str(directory),len(rows)==total);return rows
def precision(a,b,label):
 global nscalar
 ck('matching precision shape '+label,len(a)==len(b)and all(len(u)==len(v)for u,v in zip(a,b)))
 maxima=[dict(abs_change=F(0),abs_index=None,pure_relative=F(0),relative_index=None,both_zero=0,failures=[])for _ in a[0]]
 for i,(u,v)in enumerate(zip(a,b)):
  for k,(x,y)in enumerate(zip(u,v)):
   nscalar+=1;delta=abs(y-x);scale=max(abs(x),abs(y));m=maxima[k]
   if m['abs_index']is None or delta>m['abs_change']:m['abs_change']=delta;m['abs_index']=i
   if scale:
    rel=delta/scale
    if m['relative_index']is None or rel>m['pure_relative']:m['pure_relative']=rel;m['relative_index']=i
   else:m['both_zero']+=1
   if delta>F('1e-60')+F('1e-50')*scale:m['failures'].append(i)
 out=[]
 for k,m in enumerate(maxima):out.append(dict(component=k,max_absolute_change=float(m['abs_change']),argmax_absolute=m['abs_index'],max_pure_relative_change=float(m['pure_relative'])if m['relative_index']is not None else None,argmax_relative=m['relative_index'],both_zero=m['both_zero'],failed_indices=m['failures']))
 return dict(tolerance='1e-60+1e-50*maxabs',passed=all(not m['failures']for m in maxima),components=out)
# Manufactures before candidate reads.
ck('finite exact moment',moment([F(1,3),F(2,5)],[F(-2),F(7)])==F(32,15))
for x,y,j,v,want in [(0,1,[1,0,1],[0,0],(1,3,2)),(0,1,[1,0,1],[0,1],(2,4,3)),(0,0,[0,0,0],[0,0],(0,0,0)),(1,0,[0,1,0],[0,0],(2,2,1))]:
 z=fields(F(x),F(y),list(map(F,j)),list(map(F,v)));ck('exact residual manufacture '+str((x,y,j,v)),(z['R'],z['Nf'],z['Nv'])==want)
ck('Rv can attain2',fields(F(1),F(0),[F(0),F(1),F(0)],[F(0),F(0)])['Rv']==2)
ck('undefined zero ratio',fields(F(0),F(0),[F(0)]*3,[F(0)]*2)['Rf']is None)
for j,v,dj,dv in [([1,2,3],[4,5],[6,7,8],[9,10]),([0,0,1],[0,1],[2,-3,4],[-5,6])]:
 j,v,dj,dv=[list(map(F,a))for a in [j,v,dj,dv]];jm=[a+b for a,b in zip(j,dj)];vm=[a+b for a,b in zip(v,dv)];rr=lambda a,b:fields(F(2),F(-3),a,b)['R']
 ck('manufactured four-combination identity '+str(j),rr(jm,vm)-rr(j,v)==rr(jm,v)-rr(j,v)+rr(j,vm)-rr(j,v)+sum(dv[k]*dj[k+1]for k in range(2)))
for raw in ['nan','1e1001','1/2',' 1']:
 try:decimal(raw);rejected=False
 except ValueError:rejected=True
 ck('invalid decimal refused '+raw,rejected)
for p in [__file__,R/'PROOF.md',R/'ARITHMETIC_PROOF.md',V/'JOB.json']:bind(p)
c=json.loads(bind(C/'COMPLETE.json'));ck('candidate completed',c['status']=='COMPLETE_SELECTED_ANGULAR_MP_REQUIRES_EXACT_CHECK_AND_REVIEW'and c['count']==len(c['checks'])and all(a['passed']for a in c['checks']))
exit=json.loads(bind(V/'JOB_EXIT.json'));ck('worker exit0',exit['returncode']==0)
for p,h in {**c['bindings'],**c['artifacts']}.items():bind(p,h)
ck('actual module origins',c['module_paths']=={n:str(ROOT/'independent_code'/(n+'.py'))for n in ['angular_evaluator_sensitivity','node_export_inverse_stage','independent_hydrostatic','q_local_checkpoint','q_checkpoint_reader','scalar_mp_hydrostatic_density','node_export_mp_chunks']})
ck('exact witness order',[(s['radius'],s['index'])for s in c['records']]==[(3,254),(30,254)])
records=[]
for state in c['records']:
 radius=state['radius'];gp=Path(state['geometry']).resolve();ck('listed geometry '+str(radius),str(gp)in c['artifacts']);g=load(gp);n=state['nodes'];x,y=ex(state['x']),ex(state['y']);jd=list(map(ex,g['local_jet']));rows={};local={}
 ck('geometry shapes '+str(radius),g['node'].shape==(n,)and g['double_integrands'].shape==(n,4)and g['reference_velocity'].shape==(3,2)and np.array_equal(g['eps'],[0.,1e-5,1e-6])and ex(g['x'])==x and ex(g['y'])==y)
 ck('ordered precisions '+str(radius),[a['digits']for a in state['precisions']]==[72,108])
 for pp in state['precisions']:
  digits=pp['digits'];ck('observed precision '+str((radius,digits)),pp['observed_dps']==dict(local=[digits],integrands=[digits]));gb=dict(c['bindings']);gb[str(gp)]=sha(gp);ck('chunk source and geometry binding '+str((radius,digits)),pp['chunk_bindings']==gb and pp['row_count']==n and Path(pp['integrand_directory']).resolve()==C/('R'+str(radius)+'_integrands_'+str(digits)))
  rows[digits]=read_chunks(pp['integrand_directory'],n,digits,4,gb,c['artifacts']);ll=read_chunks(C/('R'+str(radius)+'_local_'+str(digits)),1,digits,4,gb,c['artifacts']);ck('local manifest decimals '+str((radius,digits)),ll==[[decimal(z)for z in row]for row in pp['local_rows']]);local[digits]=ll[0]
 pd=precision(rows[72],rows[108],'integrands '+str(radius));pl=precision([local[72]],[local[108]],'local '+str(radius));dd=[[ex(a)for a in row]for row in g['double_integrands']];comps={'D':components(g,dd),'M72':components(g,rows[72]),'M108':components(g,rows[108])};B={'V1':ex(g['reference_velocity'][0,0])}
 for e in range(3):B['V2_'+str(e)]=ex(g['reference_velocity'][e,1]);B['tail_'+str(e)]=ex(g['reference_tail'][e])
 ledger={}
 for name in B:
  b=B[name];d=comps['D'][name];m=comps['M108'][name];ck('exact finite integral decomposition '+str((radius,name)),m-b==(m-d)+(d-b));ledger[name]=serial(dict(B=b,D=d,M72=comps['M72'][name],M108=m,total=m-b,integrand_change=m-d,finite_arithmetic=d-b,precision_change=m-comps['M72'][name]))
 rr=[]
 for e in range(3):
  bv=[B['V1'],B['V2_'+str(e)]];mv=[comps['M108']['V1'],comps['M108']['V2_'+str(e)]];dv=[comps['D']['V1'],comps['D']['V2_'+str(e)]];jm=local[108]
  ff={'DD':fields(x,y,jd,bv),'MD':fields(x,y,jm,bv),'DM':fields(x,y,jd,mv),'MM':fields(x,y,jm,mv)};r00,r10,r01,r11=[ff[k]['R']for k in ['DD','MD','DM','MM']];cross=sum((mv[k]-bv[k])*(jm[k+1]-jd[k+1])for k in range(2));inv_integrand=sum((mv[k]-dv[k])*jd[k+1]for k in range(2));inv_arithmetic=sum((dv[k]-bv[k])*jd[k+1]for k in range(2))
  ck('exact four-combination identity '+str((radius,e)),r11-r00==(r10-r00)+(r01-r00)+cross and r01-r00==inv_integrand+inv_arithmetic)
  nf=ff['DD']['Nf'];decomp=dict(total=r11-r00,local=r10-r00,inverse=r01-r00,cross=cross,inverse_integrand=inv_integrand,inverse_arithmetic=inv_arithmetic)
  rr.append(dict(epsilon=float(g['eps'][e]),fields={k:serial(z)for k,z in ff.items()},decomposition=serial(decomp),fixed_Nf_D=serial({k:a/nf if nf else None for k,a in decomp.items()})))
 records.append(dict(radius=radius,index=254,nodes=n,local_MP_minus_double=[str(a-b)for a,b in zip(local[108],jd)],local_MP_pure_relative=[str(abs(a-b)/max(abs(a),abs(b)))if max(abs(a),abs(b))else None for a,b in zip(local[108],jd)],precision_integrands=pd,precision_local=pl,component_ledger=ledger,residual_records=rr))
for p,h in bindings.items():ck('final stable '+Path(p).name,sha(p)==h)
out=dict(status='PASS_SELECTED_ANGULAR_MP_FINITE_ARITHMETIC_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),precision_scalar_pairs=nscalar,checks=checks,bindings=bindings,records=records,precision_diagnostics_passed=all(s['precision_integrands']['passed']and s['precision_local']['passed']for s in records),scope='Exact identities of finite operands, empirical72/108 precision comparisons on2 selected targets and their frozen nodes only. No enclosure, continuum derivative or primary endpoint.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','precision_scalar_pairs','precision_diagnostics_passed']},indent=2))
