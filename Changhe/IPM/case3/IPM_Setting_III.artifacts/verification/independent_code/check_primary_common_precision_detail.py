from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_common_mp_sample';V=R/'verification';bindings={};checks=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('bind '+str(p),b==p.read_bytes()and(h is None or a==h));bindings[str(p)]=a;return b
def read(p):return json.loads(bind(p))
def diff(a,b):
 if a is None or b is None:ck('undefined match',a is None and b is None);return F(0)
 a,b=F(a),F(b);return abs(a-b)/max(F(1),abs(a),abs(b))
for p in [__file__,R/'PRECISION_DETAIL_PROOF.md']:bind(p)
c=read(V/'CHECKS.json');inp=read(V/'INPUTS.json')
for p,h in c['bindings'].items():bind(p,h)
ck('main1910',c['count']==len(c['checks'])==1910 and all(x['passed']for x in c['checks']))
fields=['x','y','radius','rho','psi','U1','U2','rho_x','rho_y','R','abs_R','Nf','Nv','R_Nf','R_Nv']
rows=[];fresh={};far_ratios=[]
for state in inp['states']:
 n=state['N'];fresh[n]={d:read(V/f'candidate/N{n}_d{d}.json')for d in [75,110]};a=fresh[n][75]['points'];b=fresh[n][110]['points'];detail={}
 for k in fields:
  dd=[diff(u[k],v[k])for u,v in zip(a,b)];idx=max(range(51),key=dd.__getitem__);detail[k]=dict(scaled_difference=float(dd[idx]),exact=str(dd[idx]),index=idx)
 p=F(fresh[n][110]['p_exact']);d=F(5,2)*p-1;lead=d/(2+d);ck('stored exponent defect '+str(n),d==F(1,2**54));ck('leading ratio distinct from 2^-55 '+str(n),lead!=F(1,2**55))
 f=b[-1];rho=F(f['rho']);tr=[(F(5,2)*F(f['x'])+F(f['U1']))*F(f['rho_x']),(F(5,2)*F(f['y'])+F(f['U2']))*F(f['rho_y'])]
 ck('far positive component transports '+str(n),rho>0 and all(x>0 for x in tr))
 ratio=F(f['R_Nf']);far_ratios.append(f['R_Nf'])
 rows.append(dict(N=n,per_field=detail,attaining_global_fields=[k for k in fields if detail[k]['exact']==str(max(F(v['exact'])for v in detail.values()))],far=dict(d=str(d),leading=str(lead),minus_2m55=str(lead-F(1,2**55)),stored_ratio=f['R_Nf'],stored_minus_leading=str(ratio-lead),absolute_stored_minus_leading=float(abs(ratio-lead)))))
ck('far displayed ratios match across states',len(set(far_ratios))==1)
original=[];reference_pairs=0
for p,h in inp['bindings'].items():
 if Path(p).name!='diagnostic.json':continue
 j=json.loads(bind(p,h));ck('old precision order '+p,[z['digits']for z in j['rows']]==[75,110]);n=next(s['N']for s in inp['states']if s['source_sha256']==j['source_sha256']);coords=json.loads(bind(j['points_file'],j['points_sha256']));matches=0
 # coordinates stored as an ordinary list of [x,y] pairs.
 ck('original coordinate count '+p,len(coords)==len(j['rows'][0]['points'])==len(j['rows'][1]['points']))
 for i,xy in enumerate(coords):
  hx=[float(x).hex()for x in xy];idx=next(k for k,z in enumerate(inp['points'])if z['hex']==hx)
  for oldrow in j['rows']:
   nowrow=fresh[n][oldrow['digits']]['points'][idx];oldpt=oldrow['points'][i]
   ck('old matched all15fieldstrings '+str((p,i,oldrow['digits'])),all(oldpt[k]==nowrow[k]for k in fields));matches+=1;reference_pairs+=1
 original.append(dict(file=p,N=n,precision_order=[75,110],point_count=len(coords),matched_reference_precision_pairs=matches))
ck('six original manifests and194 pairs',len(original)==6 and reference_pairs==194)
source_counts=[]
for n in [36,40,44]:source_counts.append(dict(N=n,unique_points=sum(any(a['N']==n for a in p['source_records'])for p in inp['points']),references=sum(sum(a['N']==n for a in p['source_records'])for p in inp['points'])))
for p,h in bindings.items():ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS334_PRECISION_DETAIL_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,rows=rows,original_files=original,reference_precision_pairs=reference_pairs,source_counts=source_counts,scope='Finite component precision and same-implementation reproducibility. Leading ratio is not an exact finite-radius identity or2^-55. No direction or amount of sampling bias is inferred.')
(V/'PRECISION_DETAIL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','reference_precision_pairs','source_counts']}));print(json.dumps([dict(N=r['N'],maxfields=r['attaining_global_fields'],physical_maxima={k:r['per_field'][k]['scaled_difference']for k in ['rho','psi','U1','U2','rho_x','rho_y','R','Nf','Nv','R_Nf','R_Nv']},far_discrepancy=r['far']['absolute_stored_minus_leading'])for r in rows]))
