"""Audit serialized result241 outputs independently of its extrema selectors."""
from pathlib import Path
from datetime import datetime,timezone
import gzip,hashlib,json,decimal
from decimal import Decimal as D
ROOT=Path('research/hydrostatic_c2_axis_extrema');OUT=ROOT/'verification'
decimal.getcontext().prec=100
checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def close(a,b,tol='1e-65'):return abs(D(a)-D(b))<=D(tol)*(1+abs(D(b)))
def f(p,k):return D(str(p[k]))
def point(p):
 y,G,G1,G2,k,V=(f(p,v)for v in ['y','G','G1','G2','k','V']);T=(2*y+V)*G1;R=T-G;R1=(1+k)*G1+(2*y+V)*G2
 Nf=abs(T)+abs(G);Nv=abs(G)+abs(y*G1)+abs(V*G1);sign=0 if V==0 else(1 if V>0 else -1)
 nv1=(2+sign*k)*G1+(y+sign*V)*G2
 expected=dict(R=R,R1=R1,Nf=Nf,Nv=Nv,R_Nf=abs(R)/Nf,R_Nv=abs(R)/Nv,stationary=R1*G-R*G1,stationary_Nv=R1*Nv-R*nv1)
 return all(close(p[a],b)for a,b in expected.items()),G>0 and G1>0 and T>0
z=json.loads((OUT/'CHECKS.json').read_text());ck('raw gate PASS',z['status']=='PASS'and all(c['passed']for c in z['checks']))
ck('raw driver hash',z['driver_sha256']==sha('independent_code/search_hydrostatic_c2_axis_extrema.py'))
inputs=json.loads((OUT/'INPUTS.json').read_text());ck('input manifest hash',z['inputs_sha256']==sha(OUT/'INPUTS.json'))
for p in inputs['files']:ck('input '+p['path'],sha(p['path'])==p['sha256'])
for p,h in inputs['source_sha256'].items():ck('dependency '+p,sha(p)==h)
rows=[]
for state in z['states']:
 tag=state['tag'];p=Path(state['path']);ck(tag+' output hash',sha(p)==state['sha256']);s=json.loads(p.read_text())
 pp=OUT/(tag+'.P.json.gz');ck(tag+' compressed polynomial hash',sha(pp)==s['polynomial_gzip_sha256']);ck(tag+' decoded polynomial hash',hashlib.sha256(gzip.decompress(pp.read_bytes())).hexdigest()==s['polynomial_decoded_sha256'])
 ck(tag+' precision increased',s['high_dps']==s['dps']+60)
 boundary=[v['point']for v in s['higher_precision']if v['key']=='boundary'];maxes=[]
 for scan in s['scans']:
  n=scan['panels'];points=scan['points']+[r['point']for r in scan['roots']]+s['old_axis_samples']+s['crosschecks']+boundary
  ok=[point(p)for p in points];ck(tag+f' {n} all scalar identities',all(a for a,b in ok));ck(tag+f' {n} all sign hypotheses',all(b for a,b in ok))
  ck(tag+f' {n} sample count',len(scan['points'])==n+1)
  ck(tag+f' {n} endpoints',f(scan['points'][0],'y')==100 and f(scan['points'][-1],'y')==D('1e12'))
  for j,r in enumerate(scan['roots']):
   l,h=map(D,r['refined_log10']);fl,fr=map(D,r['refined_sign_values']);bl,bh=map(D,r['bracket_log10']);y=f(r['point'],'y')
   ck(tag+f' {n} root{j} bracket',bl<=l<=h<=bh and h-l<D('1e-26') and fl*fr<=0 and abs(y.log10()-(l+h)/2)<D('1e-65'))
  mm={}
  for edge in ['4','6','8','12']:
   eligible=[p for p in points if f(p,'y')<=D(10)**int(edge)]
   mm[edge]={}
   for field in ['R','R_Nf','R_Nv']:
    best=max(eligible,key=lambda p:abs(f(p,field)));stored=scan['maxima'][edge][field]
    ck(tag+f' {n} max {edge} {field}',close(abs(f(best,field)),abs(f(stored,field))))
    mm[edge][field]={a:str(f(best,a))for a in ['y','R','R_Nf','R_Nv','G','G1','V','Nf','Nv']}
  maxes.append(mm)
 for field in ['R','R_Nf','R_Nv']:
  for edge in ['4','6','8','12']:ck(tag+' stable maximum '+edge+field,close(abs(D(maxes[0][edge][field][field])),abs(D(maxes[1][edge][field][field])),'1e-26'))
 inventory={}
 for key in ['R1','stationary','stationary_Nv','V']:
  lists=[sorted([r for r in scan['roots']if r['key']==key],key=lambda r:f(r['point'],'y'))for scan in s['scans']]
  same=len(lists[0])==len(lists[1]);err=max([abs((f(a['point'],'y')/f(b['point'],'y')).log10())for a,b in zip(*lists)]+[D(0)])
  ck(tag+' inventory '+key,same and err<D('1e-26'),dict(counts=list(map(len,lists)),log10_location_difference=str(err)))
  inventory[key]=dict(coarse=len(lists[0]),fine=len(lists[1]),maximum_log10_location_difference=str(err))
 errors=[D(v)for h in s['higher_precision']for v in h['relative_errors'].values()];ck(tag+' higher precision witnesses',max(errors)<D('1e-68'))
 for h in s['higher_precision']:ck(tag+' witness scalar identities '+h['key']+h['point']['y'],point(h['point'])[0])
 ratios={field:str(abs(D(maxes[-1]['12'][field][field]))/abs(f(s['old_grid_maxima'][field],field)))for field in ['R','R_Nf','R_Nv']}
 r2=D(s['r2']);ck(tag+' nonzero exact asymptotic coefficient',r2!=0)
 rows.append(dict(tag=tag,source_sha256=s['source_sha256'],dps=s['dps'],raw_axis_limit=str(r2),absolute_limit_lower_bound=str(abs(r2)),maxima=maxes[-1],old_grid_maxima=s['old_grid_maxima'],ratios_to_old_grid=ratios,inventory=inventory,max_precision_witness_error=str(max(errors))))
res=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,states=rows,raw_count=z['count'],source_sha256=sha(__file__),proof_sha256=sha(ROOT/'SUMMARY_PROOF.md'),raw_gate_sha256=sha(OUT/'CHECKS.json'),scope='Sampled positive-axis maxima for100<=y<=1e12; root completeness and plane supremum OPEN.')
(OUT/'SUMMARY.json').write_text(json.dumps(res,indent=2)+'\n');print(res['status'],res['count'])
for c in checks:
 if not c['passed']:print(c)
for r in rows:
 print(r['tag'],{k:(v[k],v['y'])for k,v in r['maxima']['12'].items()},r['ratios_to_old_grid'])
if res['status']!='PASS':raise SystemExit(1)
