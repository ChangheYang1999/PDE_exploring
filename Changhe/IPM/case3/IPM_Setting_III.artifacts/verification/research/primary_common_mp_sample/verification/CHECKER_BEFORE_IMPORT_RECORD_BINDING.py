from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/primary_common_mp_sample';V=R/'verification';C=V/'candidate';checks=[];bindings={};outrows=[]
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
ck('manufacture Nv bound attained',fields(dict(x=1,y=0,rho=0,rho_x=1,rho_y=0,U1=0,U2=0))['R_Nv']==F(5,2))
ck('manufacture 60-80-100 boundary',F(60)**2+F(80)**2==100**2)
for p in [__file__,R/'PROOF.md',R/'ARITHMETIC_PROOF.md',R/'RESOURCE_CHECK_PROOF.md',ROOT/'runs/launch_334.sh',V/'JOB.json']:bind(p)
inp=json.loads(bind(V/'INPUTS.json'));ck('51 common inputs',len(inp['points'])==51 and len({tuple(p['hex'])for p in inp['points']})==51)
for p,h in inp['bindings'].items():bind(p,h)
done=json.loads(bind(C/'COMPLETE.json'));ck('completed all state/precision rows',done['status']=='COMPLETE_PRIMARY_COMMON_MP_SAMPLE'and[(r['N'],r['digits'])for r in done['rows']]==[(n,d)for n in [36,40,44]for d in [75,110]])
for p,h in done['bindings'].items():bind(p,h)
exit_record=json.loads(bind(V/'JOB_EXIT.json'));ck('wrapper exit0',exit_record['returncode']==0)
ck('memory cap recorded',all(0<x<=14*1024**3 for x in done['memory_limits_bytes']))
ck('single-thread nice19 recorded',done['nice']==19 and all(v=='1'for v in done['environment'].values()))
data={(r['N'],r['digits']):json.loads(bind(r['path'],r['sha256']))for r in done['rows']}
geom=[tuple(F.from_float(float.fromhex(v))for v in p['hex'])for p in inp['points']];r2=[x*x+y*y for x,y in geom]
for n in [36,40,44]:
 a,b=data[n,75],data[n,110];ck('point counts '+str(n),len(a['points'])==len(b['points'])==51);ck('center precision equality '+str(n),all(a[k]==b[k]for k in ['a_exact','c_exact','delta_exact','p_exact']));ref=next(r for r in inp['states']if r['N']==n);ck('state identity '+str(n),a['source_sha256']==b['source_sha256']==ref['source_sha256'])
 checked=[];pmax=F(0);rmax=F(0)
 for i,(pa,pb)in enumerate(zip(a['points'],b['points'])):
  ck('common coordinate '+str((n,i)),key(pa)==key(pb)==tuple(inp['points'][i]['hex']));ds=[diff(pa[k],pb[k])for k in keys];pmax=max(pmax,*ds);ck('precision '+str((n,i)),max(ds)<=F('1e-65'))
  rr=F(pb['radius']);raderr=abs(rr*rr-r2[i])/max(1,rr*rr,r2[i]);rmax=max(rmax,raderr);ck('squared radius '+str((n,i)),raderr<=F('1e-100'))
  f=fields(pb)
  for k,z in f.items():ck('exact finite residual '+str((n,i,k)),diff(z,pb[k])<=F('1e-90'))
  ck('triangle inequalities '+str((n,i)),abs(f['R'])<=f['Nf']and abs(f['R'])<=F(5,2)*f['Nv']);checked.append(f)
 lookup={key(p):p for p in b['points']};oldmap={};matches=0;strings=0;repeat=0;oldmax=F(0)
 s=json.loads(bind(f'research/smooth_N{n}_refinement_audit/verification/SUMMARY.json'))
 for p,h in s['manifest'].items():
  if 'smooth_mp_inverse/'not in p:continue
  old=json.loads(bind(p,h))
  for pt in old['rows'][-1]['points']:
   k=key(pt);new=lookup[k];ds=[diff(pt[z],new[z])for z in keys];oldmax=max(oldmax,*ds);ck('original point agreement '+str((n,matches)),max(ds)<=F('1e-90'));matches+=1;strings+=all(pt[z]==new[z]for z in keys)
   if k in oldmap:
    ck('repeated original all fields '+str((n,repeat)),all(diff(oldmap[k][z],pt[z])<=F('1e-90')for z in keys));repeat+=1
   oldmap[k]=pt
 def maxima(ids):
  out=dict(points=len(ids),undefined_Nf=sum(checked[i]['R_Nf']is None for i in ids),undefined_Nv=sum(checked[i]['R_Nv']is None for i in ids),maxima={})
  for k in ['abs_R','R_Nf','R_Nv']:
   valid=[i for i in ids if checked[i][k]is not None]
   if not valid:out['maxima'][k]=None;continue
   i=max(valid,key=lambda i:checked[i][k]);out['maxima'][k]=dict(index=i,x=b['points'][i]['x'],y=b['points'][i]['y'],radius=b['points'][i]['radius'],value=float(checked[i][k]),displayed_fields={z:b['points'][i][z]for z in ['R','abs_R','Nf','Nv','R_Nf','R_Nv']})
  return out
 regions=[]
 for label,lo,hi in [('origin',None,F(0)),('core',F(0),F('0.01')),('subunit',F('0.01'),F(1)),('annulus',F(1),F(10000)),('far',F(10000),None)]:
  ids=[i for i,z in enumerate(r2)if (z==0 if label=='origin'else z>0 and(lo is None or z>=lo)and(hi is None or z<hi))];regions.append(dict(region=label,**maxima(ids)))
 outrows.append(dict(N=n,source_sha256=ref['source_sha256'],a_exact=b['a_exact'],c_exact=b['c_exact'],delta_exact=b['delta_exact'],p_exact=b['p_exact'],max_scaled_precision_difference=float(pmax),max_scaled_squared_radius_difference=float(rmax),original_matches=matches,original_all_fields_string_equal=strings,original_repeated_matches=repeat,max_scaled_original_difference=float(oldmax),all=maxima(list(range(51))),regions=regions,extents=[dict(radius=str(e),**maxima([i for i,z in enumerate(r2)if z<=e*e]))for e in map(F,['100','1e4','1e8','1e12','1e250'])]))
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_PRIMARY_COMMON_MP_SAMPLE_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,rows=outrows,scope='Exact decimal arithmetic and source-linked common51-point multiprecision evaluation of three saved primary fields. Same finite a posteriori set, no independent domain runs, uniform error enclosure or limiting claim.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
for row in outrows:print(json.dumps(dict(N=row['N'],max_scaled_precision_difference=row['max_scaled_precision_difference'],original_matches=row['original_matches'],original_all_fields_string_equal=row['original_all_fields_string_equal'],original_repeated_matches=row['original_repeated_matches'],all_maxima={k:v['value']if v else None for k,v in row['all']['maxima'].items()})))
