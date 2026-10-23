from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,math
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/closing_endpoint_audit';V=R/'verification';checks=[];bindings={};values=[];point_checks=0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();a=sha(p)
 if h is not None:ck('binding '+str(p),a==h)
 bindings[str(p)]=a;return p.read_bytes()
def fields(p):
 x,y,g,gx,gy,v1,v2=[F(str(p[k]))for k in ['x','y','rho','rho_x','rho_y','U1','U2']];ell=F(5,2);a=(ell*x+v1)*gx;b=(ell*y+v2)*gy;r=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
 return dict(R=r,abs_R=abs(r),Nf=nf,Nv=nv,R_Nf=abs(r)/nf if nf else None,R_Nv=abs(r)/nv if nv else None)
def close(a,b,tol=F('1e-90')):
 if a is None or b is None:return a is None and b is None
 a,b=F(str(a)),F(str(b));return abs(a-b)<=tol*max(1,abs(a),abs(b))
for v,want in [(0,F(3,2)),(1,F(5,2))]:
 z=fields(dict(x=0,y=1,rho=1,rho_x=0,rho_y=1,U1=0,U2=v));ck('manufactured primary ell5/2 residual '+str(v),z['R']==want and z['Nf']==want+2)
ck('undefined manufacture',fields(dict(x=0,y=0,rho=0,rho_x=0,rho_y=0,U1=0,U2=0))['R_Nf']is None)
ck('precision comparison manufactures',close(F(1),F(1)+F('1e-91'))and not close(F(1),F(1)+F('1e-89')))
for p in [__file__,R/'PRIMARY_RECORD_CHECK_PROOF.md',R/'ENDPOINT_MATRIX_DRAFT.md']:bind(p)
compare=json.loads(bind('research/smooth_N44_refinement_audit/verification/THREE_RESOLUTIONS.json'));ck('comparison status',compare['status']=='CONFIRMED_FINITE_COMPARISON')
for p,h in compare['manifest'].items():bind(p,h)
bind('independent_code/compare_smooth_three_resolutions.py',compare['code_sha256'])
for row,n in zip(compare['rows'],[36,40,44]):
 base=Path(f'research/smooth_N{n}_refinement_audit');s=json.loads(bind(base/'verification/SUMMARY.json'));bind(base/'PROOF.md',s['proof_sha256'])
 for p,h in s['manifest'].items():bind(p,h)
 bind(s['source'],s['source_sha256']);ck('coefficient identity '+str(n),row['source']==s['source']and row['sha256']==s['source_sha256'])
 args=s['solver_arguments'];ck('same budget and settings '+str(n),{k:v for k,v in args.items()if k not in ['radial','angular','tag']}==compare['common_arguments']and args['max_nfev']==s['solver']['nfev']==1000 and s['solver']['solver_status']==0 and args['radial']==n and args['angular']==n-4)
 a=F(s['exact_center']['a_exact']);delta=F(s['exact_center']['Delta_exact']);ck('nonzero saved center data '+str(n),a!=0 and delta!=0 and row['a']==float(a)and row['Delta']==float(delta)and row['ell']==2.5)
 points={}
 for path in s['manifest']:
  if 'smooth_mp_inverse/'not in path:continue
  d=json.loads(bind(path,s['manifest'][path]));ck('MP precision source '+path,d['source_sha256']==s['source_sha256']and [q['digits']for q in d['rows']]==[75,110])
  for p in d['rows'][-1]['points']:
   key=(float(p['x']),float(p['y']));calc=fields(p)
   for name,q in calc.items():ck('exact decimal transcription '+str((n,key,name)),close(q,p[name]));point_checks+=1
   if key in points:ck('consistent repeated MP point '+str((n,key)),all(close(points[key][k],p[k])for k in calc))
   points[key]=p
 ck('retained point union count '+str(n),len(points)==row['MP_point_count']==s['MP_union_points'])
 for name in ['R_Nf','R_Nv']:
  peak=max((p for p in points.values()if p[name]is not None),key=lambda p:F(p[name]));stored=row['MP_selected_maxima'][name]
  ck('selected maximum '+str((n,name)),stored==s['MP_selected_maxima'][name]and F(stored[name])==F(peak[name])and (float(stored['x']),float(stored['y']))==(float(peak['x']),float(peak['y'])))
 for extent in row['extents']:
  pts=[p for p in points.values()if float(p['radius'])<=extent['rmax']];ck('extent counts '+str((n,extent['rmax'])),len(pts)==extent['selected_points'])
  for name in ['abs_R','R_Nf','R_Nv']:
   peak=max((p for p in pts if p[name]is not None),key=lambda p:F(p[name]));ck('extent maximum '+str((n,extent['rmax'],name)),F(peak[name])==F(extent['maxima'][name][name]))
 ck('three extents '+str(n),[e['rmax']for e in row['extents']]==[100,10000,100000000])
 for j in row['jets']:
  source=next(q for q in s['jets_by_degree']if q['degree']==j['degree']);ck('jet tensor transcription '+str((n,j['degree'])),j['R_tensor']==source['R']['derivative_frobenius']and j['rho_tensor']==source['rho']['derivative_frobenius'])
 values.append(dict(N=n,a=float(a),Delta=float(delta),Rf=float(row['MP_selected_maxima']['R_Nf']['R_Nf']),Rv=float(row['MP_selected_maxima']['R_Nv']['R_Nv']),abs_R_r100=float(row['extents'][0]['maxima']['abs_R']['abs_R']),R_degree11=next(q['R_tensor']for q in row['jets']if q['degree']==11),rho_degree11=next(q['rho_tensor']for q in row['jets']if q['degree']==11),selected_points=len(points)))
for aa,bb,ch in zip(values,values[1:],compare['changes']):
 ck('relative changes '+str((aa['N'],bb['N'])),abs((bb['a']/aa['a']-1)-ch['relative_a'])<1e-15 and abs((bb['Rf']/aa['Rf']-1)-ch['relative_NF'])<1e-15)
ck('observed nonmonotone Rf',values[0]['Rf']>values[1]['Rf']<values[2]['Rf'])
ck('observed moving invariant slope',values[0]['a']>values[1]['a']>values[2]['a'])
ck('observed growing degree11 residual tensor',values[0]['R_degree11']<values[1]['R_degree11']<values[2]['R_degree11'])
critical=json.loads(bind('research/smooth_N44_refinement_audit/verification/critical_points/SUMMARY.json'));ck('critical finite audit status',critical['status']=='CONFIRMED_FINITE_SEARCH'and len(critical['checks'])==133 and all(q['passed']for q in critical['checks']))
for p,h in bindings.items():ck('final stable '+Path(p).name,sha(p)==h)
out=dict(status='PASS_CLOSING_PRIMARY_FINITE_RECORDS_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),decimal_scalar_checks=point_checks,checks=checks,bindings=bindings,values=values,scope='Saved primary records rebound, decimal transcriptions and finite maxima checked. No new inverse calculation, error enclosure, exactness or limiting inference.')
(V/'PRIMARY_RECORD_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','decimal_scalar_checks','values']},indent=2))
