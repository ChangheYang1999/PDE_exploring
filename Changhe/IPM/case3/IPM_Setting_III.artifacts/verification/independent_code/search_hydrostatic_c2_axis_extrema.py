"""Result241: complete elementary inverse, exact coefficients and analytic extrema."""
from pathlib import Path
from datetime import datetime,timezone
from math import comb
import gzip,hashlib,json,os,sys,time
import gmpy2
import mpmath as mp
from hydrostatic_p2_elementary_axis import Axis,rational_polynomial
from hydrostatic_core_moment import exactmp,guard
sys.set_int_max_str_digits(0)
Q=gmpy2.mpq; Z=gmpy2.mpz
ROOT=Path('research/hydrostatic_c2_axis_extrema');OUT=ROOT/'verification';OUT.mkdir(exist_ok=True)
checks=[];states=[];started=datetime.now(timezone.utc).isoformat();start=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def stamp():return datetime.now(timezone.utc).isoformat()
def dump(p,o):p.write_text(json.dumps(o,indent=2)+'\n')
def serial(o):
 if isinstance(o,dict):return {k:serial(v)for k,v in o.items()}
 if isinstance(o,(list,tuple)):return [serial(v)for v in o]
 if isinstance(o,mp.mpf):return mp.nstr(o,80)
 return o
def poly(k):
 out=[Q(0)]*max(2,2*len(k)-4)
 if len(k)>2:out[1]=-3*k[2]
 for j in range(3,len(k)):
  for m in range(j-2):
   v=k[j]*((-1)**m*comb(j-3,m))
   out[2*m+1]+=v/(2*m+1);out[2*m+3]+=3*v/(2*m+3)
 while len(out)>1 and out[-1]==0:out.pop()
 return out
keys=['R1','stationary','stationary_Nv','V']
def enrich(axis,y):
 a=axis.evaluate(y);sgn=mp.sign(a['V'])
 nv1=(2+sgn*a['k'])*a['G1']+(a['y']+sgn*a['V'])*a['G2']
 a['stationary_Nv']=a['R1']*a['Nv']-a['R']*nv1
 a['positive_G1']=bool(a['G1']>0)
 return a
def scan(axis,n):
 logs=[mp.mpf(2)+mp.mpf(10)*i/n for i in range(n+1)]
 points=[enrich(axis,mp.power(10,u)) for u in logs]
 roots=[]
 for key in keys:
  for i in range(n):
   a=points[i][key];b=points[i+1][key]
   if not a*b<0:continue
   left,right=logs[i],logs[i+1];lo,hi=left,right;fl,fr=a,b
   for unused in range(90):
    mid=(lo+hi)/2;fm=enrich(axis,mp.power(10,mid))[key]
    if fm==0:lo=hi=mid;fl=fr=fm;break
    if fl*fm<0:hi=mid;fr=fm
    else:lo=mid;fl=fm
   p=enrich(axis,mp.power(10,(lo+hi)/2))
   roots.append(dict(key=key,bracket_log10=[left,right],refined_log10=[lo,hi],refined_sign_values=[fl,fr],point=p))
 return points,roots

def main():
 gp=Path('research/hydrostatic_p2_elementary_axis/verification/GATE.json');g=json.loads(gp.read_text())
 ck('elementary manufacture1124',g['status']=='PASS'and g['count']==1124 and all(x['passed']for x in g['checks']))
 ck('elementary source unchanged',g['module_sha256']==sha('independent_code/hydrostatic_p2_elementary_axis.py'))
 cg=Path('research/hydrostatic_p2_elementary_axis/verification/COORDINATE_GATE.json');co=json.loads(cg.read_text())
 ck('coordinate regression1106',co['status']=='PASS'and co['count']==1106 and all(x['passed']for x in co['checks']))
 ck('coordinate source unchanged',co['module_sha256']==sha('independent_code/hydrostatic_p2_elementary_axis.py'))
 for k in [[0,1],[0,3,7],[0,-2,5,3,0,-1],[0,Q(1,7),Q(-5,11),Q(13,17),Q(1,9)]]:
  got=poly(list(map(Q,k)));want=rational_polynomial([str(v)for v in k]);ck('GMP exact fixture '+str(k),[str(v)for v in got]==[str(v)for v in want])
 sources=[('hydrostatic_c2_resolved_audit','hsG_c2.0_N96_log'),('hydrostatic_c2_resolved_audit','hsG_c2.0_N128_log'),('hydrostatic_c2_continuation_audit','hsG_c2.0_N128_log_cont'),('hydrostatic_c2_resolved_160_audit','hsG_c2.0_N160_log')]
 provenance=[]
 for dirname,tag in sources:
  base=Path('research')/dirname/'verification';ps=[base/(tag+'.polynomials.json'),base/'SUMMARY.json',base/(tag+'.json')]
  provenance.extend(dict(path=str(p),sha256=sha(p))for p in ps)
 dump(OUT/'INPUTS.json',dict(utc=stamp(),files=provenance,source_sha256={p:sha(p)for p in [__file__,'independent_code/hydrostatic_p2_elementary_axis.py','independent_code/hydrostatic_core_moment.py']},proof_sha256=sha(ROOT/'PROOF.md'),manufacture_gate_sha256=sha(gp),coordinate_gate_sha256=sha(cg)))
 for dirname,tag in sources:
  print(stamp(),tag,'START',flush=True)
  base=Path('research')/dirname/'verification';summary=json.loads((base/'SUMMARY.json').read_text());s=next(a for a in summary['states'] if a['tag']==tag)
  ck(tag+' previous summary',summary['status']=='PASS'and all(c['passed']for c in summary['checks']))
  z=json.loads((base/(tag+'.polynomials.json')).read_text());q=lambda p:Q(Z(p[0]),Z(p[1]));k=list(map(q,z['k_w']));H=list(map(q,z['H_w']));L=q(z['L']);C=L/4
  ck(tag+' exact P2',q(z['P'])==2);ck(tag+' zero constants',k[0]==H[0]==0)
  P=poly(k);encoded=json.dumps({'P_t':[[str(p.numerator),str(p.denominator)]for p in P]},separators=(',',':')).encode();compressed=gzip.compress(encoded,compresslevel=6,mtime=0)
  pp=OUT/(tag+'.P.json.gz');pp.write_bytes(compressed)
  dps=max(160,guard(k)+100,guard(H)+100,guard(P)+100);mp.mp.dps=dps
  axis=Axis(exactmp(C),list(map(exactmp,H)),list(map(exactmp,k)),list(map(exactmp,P)))
  cross=[]
  for old in s['axis_points']:
   y=mp.mpf(old['y'])
   if not mp.mpf(100)<=y<=mp.mpf('1e12'):continue
   p=enrich(axis,y)
   for a,b in [('G','g'),('G1','gy'),('V','V2'),('R','R'),('Nf','Nf')]:
    e=abs(p[a]-mp.mpf(old[b]))/(1+abs(p[a]));ck(tag+' prior axis '+old['y']+' '+a,e<mp.mpf('1e-68'),mp.nstr(e,10))
   cross.append(p)
  raw=json.loads((base/(tag+'.json')).read_text());sample=[]
  for old in raw['levels'][-1]['points']:
   if old['y']<100 or abs(old['x'])>1e-10:continue
   p=enrich(axis,mp.mpf(str(old['y'])));sample.append(p)
   for a,b in [('G','g'),('G1','gy'),('V','V2'),('R','R'),('R_Nf','R_Nf'),('R_Nv','R_Nv')]:
    e=abs(p[a]-mp.mpf(str(old[b])))/(1+abs(p[a]));ck(tag+' prior double '+str(old['y'])+' '+a,e<mp.mpf('1e-9'),mp.nstr(e,10))
  scans=[]
  for n in [320,640]:
   print(stamp(),tag,'SCAN',n,'dps',dps,flush=True);points,roots=scan(axis,n)
   allp=points+[r['point']for r in roots]+sample+cross
   for edge in [4,6,8,12]:allp.append(enrich(axis,mp.power(10,edge)))
   ck(tag+f' n{n} positive G and transport',all(p['positive_denominator']for p in allp))
   ck(tag+f' n{n} positive G1',all(p['positive_G1']for p in allp))
   for j,r in enumerate(roots):
    lo,hi=r['refined_log10'];fl,fr=r['refined_sign_values'];ck(tag+f' n{n} root{j} computed signs',fl*fr<=0 and hi-lo<mp.mpf('1e-26'))
   maxima={}
   for edge in [4,6,8,12]:
    eligible=[p for p in allp if p['y']<=mp.power(10,edge)]
    maxima[str(edge)]={key:max(eligible,key=lambda p:abs(p[key]))for key in ['R','R_Nf','R_Nv']}
   scans.append(dict(panels=n,points=points,roots=roots,maxima=maxima))
  a,b=scans;inventory={}
  for key in keys:
   aa=[r for r in a['roots']if r['key']==key];bb=[r for r in b['roots']if r['key']==key]
   inventory[key]=dict(coarse=len(aa),fine=len(bb),same_count=len(aa)==len(bb),maximum_log_location_change=max([abs(mp.log10(x['point']['y']/y['point']['y']))for x,y in zip(aa,bb)]+[mp.mpf(0)]))
  witnesses=b['roots']+[dict(key='boundary',point=enrich(axis,mp.power(10,edge)))for edge in [2,4,6,8,12]]
  mp.mp.dps=dps+60;higher=Axis(exactmp(C),list(map(exactmp,H)),list(map(exactmp,k)),list(map(exactmp,P)))
  high=[]
  for j,w in enumerate(witnesses):
   p=w['point'];q=enrich(higher,p['y']);error={key:abs(p[key]-q[key])/(1+abs(q[key]))for key in ['G','G1','G2','V','k','R','R1','Nf','Nv','R_Nf','R_Nv']}
   ck(tag+f' high precision witness{j}',max(error.values())<mp.mpf('1e-68'),{k:mp.nstr(v,12)for k,v in error.items()});high.append(dict(key=w['key'],point=q,relative_errors=error))
  result=dict(tag=tag,dps=dps,high_dps=dps+60,source_sha256=s['source_sha256'],polynomial_gzip_sha256=sha(pp),polynomial_decoded_sha256=hashlib.sha256(encoded).hexdigest(),r2=s['far']['values']['r2'],old_grid_maxima=s['levels'][-1]['regions']['extent10000'],crosschecks=cross,old_axis_samples=sample,scans=scans,inventory=inventory,higher_precision=high)
  dump(OUT/(tag+'.json'),serial(result));states.append(dict(tag=tag,path=str(OUT/(tag+'.json')),sha256=sha(OUT/(tag+'.json')),dps=dps,inventory=serial(inventory),maxima=serial(b['maxima']),r2=result['r2']))
  dump(OUT/'PIPELINE.json',dict(status='RUNNING',started=started,utc=stamp(),pid=os.getpid(),states=states));print(stamp(),tag,'DONE',flush=True)
 result=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=stamp(),started=started,seconds=time.monotonic()-start,count=len(checks),checks=checks,states=states,proof_sha256=sha(ROOT/'PROOF.md'),driver_sha256=sha(__file__),inputs_sha256=sha(OUT/'INPUTS.json'),scope='Finite scans and computed brackets, not a rigorous global maximum or an IPM existence result.')
 dump(OUT/'CHECKS.json',result);dump(OUT/'PIPELINE.json',dict(status='DONE',utc=stamp(),gate=result['status'],states=states));print(result['status'],result['count'],flush=True)
 if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
