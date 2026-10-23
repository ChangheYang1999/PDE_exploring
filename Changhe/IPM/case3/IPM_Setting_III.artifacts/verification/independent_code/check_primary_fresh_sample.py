from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/primary_fresh_sample';V=R/'verification';C=V/'candidate';checks=[];bindings={};outrows=[]
keys=['x','y','radius','rho','psi','U1','U2','rho_x','rho_y','R','abs_R','Nf','Nv','R_Nf','R_Nv']
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable read '+str(p),p.read_bytes()==b)
 if h is not None:ck('binding '+str(p),a==h)
 bindings[str(p)]=a;return b
def fields(p):
 x,y,g,gx,gy,u,v=[F(str(p[k]))for k in ['x','y','rho','rho_x','rho_y','U1','U2']];a=(F(5,2)*x+u)*gx;b=(F(5,2)*y+v)*gy;r=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(u*gx+v*gy)
 return dict(R=r,abs_R=abs(r),Nf=nf,Nv=nv,R_Nf=abs(r)/nf if nf else None,R_Nv=abs(r)/nv if nv else None)
def diff(a,b):
 if a is None or b is None:
  if a is not None or b is not None:raise ValueError('undefined mismatch')
  return F(0)
 a,b=F(a),F(b);return abs(a-b)/max(1,abs(a),abs(b))
def key(p):return tuple(float(p[k]).hex()for k in ['x','y'])
ck('manufacture affine residual',fields(dict(x=0,y=1,rho=1,rho_x=0,rho_y=1,U1=0,U2=0))['R']==F(3,2))
ck('manufacture undefined',fields(dict(x=0,y=0,rho=0,rho_x=0,rho_y=0,U1=0,U2=0))['R_Nf']is None)
ck('manufacture Nv sharp bound',fields(dict(x=1,y=0,rho=0,rho_x=1,rho_y=0,U1=0,U2=0))['R_Nv']==F(5,2))
ck('manufacture exact extent boundary',F(60)**2+F(80)**2==100**2)
ck('manufacture exact scaled comparison',diff('1e100','1.000000000000001e100')==F(1,1000000000000001))
if sys.argv[1:]==['--manufacture']:
 out=dict(status='PASS_FRESH_ARITHMETIC_MANUFACTURES',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(V/'ARITHMETIC_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));raise SystemExit
if sys.argv[1:]:raise RuntimeError('unknown args')
if (V/'CHECKS.json').exists():raise FileExistsError('CHECKS exists')
for p in [__file__,R/'PROOF.md',R/'DESIGN_REVIEW_RESOLUTION.md',ROOT/'runs/launch_336.sh',V/'JOB.json']:bind(p)
am=json.loads(bind(V/'ARITHMETIC_MANUFACTURES.json'));ck('prospective arithmetic gate',am['status']=='PASS_FRESH_ARITHMETIC_MANUFACTURES' and am['checker_sha256']==bindings[str(Path(__file__).resolve())] and am['count']==5 and all(c['passed']for c in am['checks']))
inp=json.loads(bind(V/'INPUTS.json'));ck('101 prospective distinct inputs',inp['status']=='FROZEN_PROSPECTIVE101_SAMPLE' and len(inp['points'])==101 and len({tuple(p['hex'])for p in inp['points']})==101)
for p,h in inp['bindings'].items():bind(p,h)
done=json.loads(bind(C/'COMPLETE.json'));ck('completed all state precision rows',done['status']=='COMPLETE_PRIMARY_FRESH_MP_SAMPLE'and[(r['N'],r['digits'])for r in done['rows']]==[(n,d)for n in [36,40,44]for d in [75,110]])
for p,h in done['bindings'].items():bind(p,h)
ck('prospective inputs and checker precede evaluation',datetime.fromisoformat(inp['utc'])<datetime.fromisoformat(done['started_utc']) and datetime.fromisoformat(am['utc'])<datetime.fromisoformat(done['started_utc']))
bind(V/'IMPORT_PREPARATION.json');ex=json.loads(bind(V/'JOB_EXIT.json'));ck('wrapper exit0',ex['returncode']==0)
ck('memory cap recorded',all(0<x<=14*1024**3 for x in done['memory_limits_bytes']))
ck('single thread nice19 recorded',done['nice']==19 and all(v=='1'for v in done['environment'].values()))
old=json.loads(bind(ROOT/'research/primary_common_mp_sample/verification/CHECKS.json'))
data={(r['N'],r['digits']):json.loads(bind(r['path'],r['sha256']))for r in done['rows']}
geom=[tuple(F.from_float(float.fromhex(v))for v in p['hex'])for p in inp['points']];r2=[x*x+y*y for x,y in geom]
groups=['log_polar','near_horizontal','near_vertical','exact_axes'];ck('group counts',[sum(p['group']==g for p in inp['points'])for g in groups]==[64,16,16,5])
for n in [36,40,44]:
 a,b=data[n,75],data[n,110];ck('point counts '+str(n),len(a['points'])==len(b['points'])==101);ck('center precision equality '+str(n),all(a[k]==b[k]for k in ['a_exact','c_exact','delta_exact','p_exact']));ref=next(r for r in inp['states']if r['N']==n);ck('state identity '+str(n),a['source_sha256']==b['source_sha256']==ref['source_sha256']);prior=next(r for r in old['rows']if r['N']==n);ck('old center and source identity '+str(n),all(b[k]==prior[k]for k in ['a_exact','c_exact','delta_exact','p_exact','source_sha256']))
 checked=[];pmax=F(0);rmax=F(0);pwhere=None
 for i,(pa,pb)in enumerate(zip(a['points'],b['points'])):
  ck('same binary64 coordinates '+str((n,i)),key(pa)==key(pb)==tuple(inp['points'][i]['hex']))
  for k in keys:
   d=diff(pa[k],pb[k])
   if d>pmax:pmax=d;pwhere=dict(index=i,field=k)
  ck('precision '+str((n,i)),max(diff(pa[k],pb[k])for k in keys)<=F('1e-65'))
  rr=F(pb['radius']);raderr=abs(rr*rr-r2[i])/max(1,rr*rr,r2[i]);rmax=max(rmax,raderr);ck('squared radius '+str((n,i)),raderr<=F('1e-100'))
  f=fields(pb)
  for k,z in f.items():ck('exact decimal residual '+str((n,i,k)),diff(z,pb[k])<=F('1e-90'))
  ck('triangle inequalities '+str((n,i)),abs(f['R'])<=f['Nf']and abs(f['R'])<=F(5,2)*f['Nv']);checked.append(f)
  if geom[i][1]==0:ck('horizontal exact symmetry '+str((n,i)),f['R']==f['Nf']==f['Nv']==0 and f['R_Nf']is None and f['R_Nv']is None)
 def maxima(ids):
  out=dict(points=len(ids),undefined_Nf=sum(checked[i]['R_Nf']is None for i in ids),undefined_Nv=sum(checked[i]['R_Nv']is None for i in ids),maxima={})
  for k in ['abs_R','R_Nf','R_Nv']:
   valid=[i for i in ids if checked[i][k]is not None]
   if not valid:out['maxima'][k]=None;continue
   i=max(valid,key=lambda j:checked[j][k]);out['maxima'][k]=dict(index=i,x=b['points'][i]['x'],y=b['points'][i]['y'],radius=b['points'][i]['radius'],value=float(checked[i][k]),displayed_fields={z:b['points'][i][z]for z in ['R','abs_R','Nf','Nv','R_Nf','R_Nv']})
  return out
 allmax=maxima(list(range(101)));ck('three undefined points '+str(n),allmax['undefined_Nf']==allmax['undefined_Nv']==3)
 comparisons={}
 for k in ['abs_R','R_Nf','R_Nv']:
  newmax=allmax['maxima'][k];oldmax=prior['all']['maxima'][k];nv=F(newmax['displayed_fields'][k]);ov=F(oldmax['displayed_fields'][k]);comparisons[k]=dict(old51=oldmax['value'],fresh101=newmax['value'],larger_sample='fresh101'if nv>ov else'old51',union_max_displayed=float(max(nv,ov)),scope='different finite point sets, no continuum supremum or trend')
 outrows.append(dict(N=n,source_sha256=ref['source_sha256'],a_exact=b['a_exact'],c_exact=b['c_exact'],delta_exact=b['delta_exact'],p_exact=b['p_exact'],max_scaled_precision_difference=float(pmax),precision_where=pwhere,max_scaled_squared_radius_difference=float(rmax),all=allmax,groups=[dict(group=g,**maxima([i for i,p in enumerate(inp['points'])if p['group']==g]))for g in groups],extents=[dict(radius=str(e),**maxima([i for i,z in enumerate(r2)if z<=e*e]))for e in map(F,['1','100','1e4','1e8','1e12'])],old51_comparison=comparisons))
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_PRIMARY_FRESH_SAMPLE_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,rows=outrows,scope='Prospectively frozen stratified finite sample of three saved primary fields. Exact decimal arithmetic and empirical multiprecision stability, no inverse enclosure, independent domain runs, continuum supremum or limiting conclusion.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
for row in outrows:print(json.dumps(dict(N=row['N'],max_scaled_precision_difference=row['max_scaled_precision_difference'],all_maxima={k:v['value']if v else None for k,v in row['all']['maxima'].items()},extents=[dict(radius=e['radius'],points=e['points'])for e in row['extents']])) )
