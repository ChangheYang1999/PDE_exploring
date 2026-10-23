from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/closing_endpoint_audit';V=R/'verification';checks=[];bindings={};records=[];fields=['x','y','radius','rho','psi','U1','U2','rho_x','rho_y','R','abs_R','Nf','Nv','R_Nf','R_Nv']
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable read '+str(p),p.read_bytes()==b)
 if h is not None:ck('binding '+str(p),a==h)
 bindings[str(p)]=a;return b
def diff(a,b):
 if a is None or b is None:
  if a is not None or b is not None:raise ValueError('undefined mismatch')
  return F(0)
 a,b=F(a),F(b);return abs(a-b)/max(1,abs(a),abs(b))
def key(p):return float(p['x']).hex(),float(p['y']).hex()
def pair(a,b,label):
 ck('same binary64 point '+label,key(a)==key(b));ds={k:diff(a[k],b[k])for k in fields};ck('75/110 scaled agreement '+label,max(ds.values())<=F('1e-65'));return max(ds.values())
ck('manufactured exact 3-4-5 extent',F(3)**2+F(4)**2==F(5)**2)
ck('manufactured near-boundary distinction',(F(3)+F('1e-100'))**2+F(4)**2>F(5)**2)
ck('manufactured precision scaling',diff('1e100','1.0000000000000000000000000000000000000000000000000000000000000000000000001e100')<F('1e-65'))
ck('manufactured undefined equality',diff(None,None)==0)
try:diff(None,'0')
except ValueError:ck('manufactured undefined mismatch',True)
else:ck('manufactured undefined mismatch',False)
for p in [__file__,R/'PRIMARY_PRECISION_RADIUS_PROOF.md',R/'ENDPOINT_MATRIX.md']:bind(p)
old=json.loads(bind(V/'PRIMARY_RECORD_CHECKS.json'));ck('prior807 passing',old['count']==807 and all(c['passed']for c in old['checks']))
for p,h in old['bindings'].items():bind(p,h)
for n in [36,40,44]:
 s=json.loads(bind(f'research/smooth_N{n}_refinement_audit/verification/SUMMARY.json'));union={};dmax=F(0);radiusmax=F(0);pairs=0;membership=[];extras=[]
 for path in s['manifest']:
  if 'smooth_mp_inverse/'not in path:continue
  d=json.loads(bind(path,s['manifest'][path]));inputs=json.loads(bind(d['points_file'],d['points_sha256']));bind(d['input'],d['input_sha256']);ck('row counts '+path,[r['digits']for r in d['rows']]==[75,110]and all(len(r['points'])==len(inputs)for r in d['rows']))
  for a,b,xy in zip(d['rows'][0]['points'],d['rows'][1]['points'],inputs):
   label=str((n,key(b)));xy=tuple(float(v)for v in xy);ck('original binary64 coordinates '+label,key(b)==tuple(v.hex()for v in xy));dmax=max(dmax,pair(a,b,label));pairs+=1
   x,y=map(F.from_float,xy);r2=x*x+y*y;rr=F(b['radius']);err=abs(rr*rr-r2)/max(1,abs(rr*rr),r2);radiusmax=max(radiusmax,err);ck('squared MP radius '+label,err<=F('1e-100'))
   union[key(b)]=(b,r2)
 for k,(p,r2)in union.items():
  for extent in [100,10000,100000000]:
   exact=r2<=F(extent)**2;oldmask=float(p['radius'])<=extent
   if exact!=oldmask:membership.append(dict(point=list(k),extent=extent,exact=exact,old_float_radius=oldmask))
  if r2>F(100000000)**2:extras.append({k:p[k]for k in ['x','y','radius','abs_R','R_Nf','R_Nv']})
 records.append(dict(N=n,pairs=pairs,union=len(union),max_scaled_precision_difference=float(dmax),max_scaled_squared_radius_difference=float(radiusmax),membership_disagreements=membership,extreme_points=extras,extent_counts=[dict(extent=e,exact_count=sum(r2<=F(e)**2 for p,r2 in union.values()),old_count=sum(float(p['radius'])<=e for p,r2 in union.values()))for e in [100,10000,100000000]]))
cp=ROOT/'research/smooth_N44_refinement_audit/verification/critical_points';s=json.loads(bind(cp/'SUMMARY.json'));raw=json.loads(bind(cp/'AUDIT.json',s['audit_sha256']));ck('all three critical states',len(raw['states'])==len(s['rows'])==3 and raw['status']=='DONE')
bind('research/smooth_N44_refinement_audit/CRITICAL_POINT_PROOF.md',raw['proof_sha256']);bind('independent_code/audit_smooth_critical_points.py',raw['code_sha256'])
for p,h in raw['implementation_sha256'].items():bind(p,h)
crit=[]
for n,a,b in zip([36,40,44],raw['states'],s['rows']):
 ck('critical state identity '+str(n),a['tag']==b['tag']==f'common1000_moments_cl2.5_N{n}M{n-4}'and a['source_sha256']==b['source_sha256']and a['status']=='DONE');bind(a['source'],a['source_sha256']);bind(a['exact_input'],a['exact_input_sha256'])
 for k in ['origin','grids','axis_roots']:ck('critical summary direct record '+str((n,k)),a[k]==b[k])
 ck('critical three meshes and inverse refinement '+str(n),[(g['radial'],g['angular'],g['inverse_order'])for g in a['grids']]==[(129,95,128),(257,159,128),(513,287,128),(513,287,192)])
 peak=F(0)
 for i,rec in enumerate(a['MP']):
  ck('two critical MP evaluations '+str((n,i)),len(rec['evaluations'])==2);peak=max(peak,pair(*rec['evaluations'],str(('critical',n,i))))
 ck('five selected critical witnesses '+str(n),len(a['MP'])==len(b['MP'])==5)
 crit.append(dict(N=n,witnesses=len(a['MP']),max_scaled_precision_difference=float(peak),origin=a['origin'],axis_sampled_brackets=sum(len(z['brackets'])for z in a['axis_roots']),interior_attempts=len(a['interior_attempts'])))
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_CLOSING_PRIMARY_PRECISION_AND_RADIUS_RECORDS_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,records=records,critical=crit,scope='Finite saved precision agreement, exact input-coordinate extent checks, and all-three-state critical source linkage. No new inverse run, error enclosure, critical completeness, or primary endpoint.')
(V/'PRIMARY_PRECISION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','critical']},indent=2))
for d in records:print(json.dumps({k:d[k]for k in ['N','pairs','union','max_scaled_precision_difference','max_scaled_squared_radius_difference','membership_disagreements','extent_counts']}))
