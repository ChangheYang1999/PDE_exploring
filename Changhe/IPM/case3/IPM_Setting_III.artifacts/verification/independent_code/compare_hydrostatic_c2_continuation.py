"""Result 238: compare frozen states at identical points; no producer evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, math, re
ROOT=Path('research/hydrostatic_c2_continuation_audit');V=ROOT/'verification'
OLD=Path('research/hydrostatic_c2_resolved_audit/verification')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
def read(p):return json.loads(p.read_text())
a=read(OLD/'hsG_c2.0_N128_log.json');b=read(V/'hsG_c2.0_N128_log_cont.json')
sa=next(s for s in read(OLD/'SUMMARY.json')['states'] if s['tag']==a['tag']);sb=read(V/'SUMMARY.json')['states'][0]
for name,p,n in [('old',OLD/'SUMMARY.json',246),('new',V/'SUMMARY.json',134)]:
 s=read(p);check(name+' summary PASS',s['status']=='PASS' and s['count']==n and all(c['passed'] for c in s['checks']))
check('distinct input hashes',a['source_sha256']!=b['source_sha256'])
for name,v,st in [('old',OLD,a),('new',V,b)]:
 check(name+' frozen checkpoint hash',sha(v/(st['tag']+'.pt'))==st['source_sha256'])
 check(name+' raw done',st['status']=='DONE')
check('same physical point document',read(OLD/'POINTS.json')==read(V/'POINTS.json'))
check('same sizes exponents',[(s['N'],s['M'],s['c'])for s in [sa,sb]]==[(128,32,2.0)]*2)
regions=[('tiny',0.,.01),('inner',.01,.1),('core',.1,1.),('annulus',1.,100.),('far',100.,float('inf')),('extent10',0.,10.),('extent100',0.,100.),('extent10000',0.,10000.000001)]
def recompute(rows,c,label):
 out=[];errors=[];zero=True
 for r in rows:
  x,y,g,gx,gy,u,v=(r[k] for k in ['x','y','g','gx','gy','V1','V2'])
  X=(c*x+u)*gx;Y=(c*y+v)*gy
  R=X+Y-g;nf=abs(X)+abs(Y)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(u*gx+v*gy)
  z=dict(x=x,y=y,g=g,V1=u,V2=v,R=R,Nf=nf,Nv=nv,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None)
  for k in ['R','Nf','Nv','R_Nf','R_Nv']:
   if z[k] is None:zero &= r[k] is None
   else:errors.append(abs(z[k]-r[k])/(1+abs(z[k])))
  out.append(z)
 check(label+' raw residual denominator audit',max(errors)<1e-14,max(errors));check(label+' undefined ratios retained',zero)
 return out
levels=[]
for i,(la,lb) in enumerate(zip(a['levels'],b['levels'])):
 check(str(i)+' same quadrature',all(la[k]==lb[k] for k in ['order','tail_order','split','inner_scale']))
 A=recompute(la['points'],sa['c'],str(i)+' old');B=recompute(lb['points'],sb['c'],str(i)+' new')
 check(str(i)+' identical 774 point order',len(A)==len(B)==774 and [(z['x'],z['y'])for z in A]==[(z['x'],z['y'])for z in B])
 report={}
 for reg,lo,hi in regions:
  pairs=[(x,y)for x,y in zip(A,B)if lo<=math.hypot(x['x'],x['y'])<hi]
  zz={'count':len(pairs),'undefined_Nf':sum(x['Nf']==y['Nf']==0 for x,y in pairs),'maxima':{},'maximum_pointwise_changes':{}}
  for key in ['R','R_Nf','R_Nv']:
   candidates=[(x,y)for x,y in pairs if x[key]is not None and y[key]is not None]
   x=max((x for x,y in candidates),key=lambda r:abs(r[key]));y=max((y for x,y in candidates),key=lambda r:abs(r[key]))
   zz['maxima'][key]=dict(before=x,after=y,ratio=abs(y[key]/x[key])if x[key]else None)
   if i==2:
    check(reg+' old maximum '+key,math.isclose(abs(x[key]),abs(sa['final_regions'][reg][key][key]),rel_tol=1e-13,abs_tol=1e-15))
    check(reg+' new maximum '+key,math.isclose(abs(y[key]),abs(sb['final_regions'][reg][key][key]),rel_tol=1e-13,abs_tol=1e-15))
  for key in ['g','V1','V2','R','R_Nf','R_Nv']:
   pairs2=[(x,y)for x,y in pairs if x[key]is not None and y[key]is not None]
   x,y=max(pairs2,key=lambda xy:abs(xy[1][key]-xy[0][key]))
   zz['maximum_pointwise_changes'][key]=dict(x=x['x'],y=x['y'],before=x[key],after=y[key],change=y[key]-x[key])
  report[reg]=zz
 levels.append(dict(order=la['order'],tail_order=la['tail_order'],split=la['split'],regions=report))
log=(V/'producer_run.log').read_text();res=json.loads(next(x[len('# RESULT '):]for x in log.splitlines()if x.startswith('# RESULT ')))
check('producer log source tag and start',res['tag']==b['tag'] and res['start']=='runs/hsG_c2.0_N128_log.pt')
it=[]
for line in log.splitlines():
 m=re.search(r'it (\d+): \|F\|2 ([\deE+.-]+) \|F\|max ([\deE+.-]+)',line)
 if m:it.append((int(m[1]),float(m[2]),float(m[3])))
check('120 recorded continuation iterations',[r[0] for r in it]==list(range(120)))
check('finite node objective',res['nodes_F2']>0 and res['nodes_Fmax']>0)
late=[r for r in it if r[0]>=104]
producer=dict(result=res,first=it[0],last=it[-1],relative_decrease_last_15_steps=(late[0][1]-late[-1][1])/late[0][1],scope='Recorded producer optimizer objectives only; independently computed grid residuals above.')
constants={}
for key in ['a','cH','delta','b','e','E','axis_cubic_residual']:
 constants[key]={'before':sa[key],'after':sb[key],'change':sb[key]-sa[key]}
for key in sa['far']['values']:
 constants[key]={'before':sa['far']['values'][key],'after':sb['far']['values'][key]}
constants['Cp_K']={'before':sa['cusp']['Cp_K'],'after':sb['cusp']['Cp_K']}
check('nonzero raw far limits',all(abs(float(s['far']['values']['r2']))>7 for s in [sa,sb]))
check('empirical maximum rises all metrics',all(levels[-1]['regions']['extent10000']['maxima'][k]['ratio']>1 for k in ['R','R_Nf','R_Nv']))
files=[ROOT/'COMPARISON_PROOF.md',Path(__file__),OLD/'SUMMARY.json',V/'SUMMARY.json',OLD/(a['tag']+'.json'),V/(b['tag']+'.json'),V/'producer_run.log']
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,levels=levels,constants=constants,producer=producer,hashes={str(p):sha(p)for p in files},scope='Finite same-coordinate comparison of two auxiliary hydrostatic trials. Not a full IPM candidate, continuum error bound, or exclusion theorem.')
(V/'COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],out['count']);print([c for c in checks if not c['passed']])
print(json.dumps({k:q['ratio']for k,q in levels[-1]['regions']['extent10000']['maxima'].items()}));print('last15',producer['relative_decrease_last_15_steps'])
if out['status']!='PASS':raise SystemExit(1)
