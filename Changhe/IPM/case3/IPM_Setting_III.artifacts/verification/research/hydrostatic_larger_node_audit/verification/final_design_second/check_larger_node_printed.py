"""Independent printed-decimal comparison. No producer or inverse imports."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import re,json,hashlib,sys,math,time,traceback
if sys.flags.optimize:raise SystemExit('optimized Python prohibited for verification')
import numpy as np
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification'
NUM=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def interval(s):
 if not isinstance(s,str)or not re.fullmatch(NUM,s):raise ValueError('printed decimal syntax')
 bits=re.split('[eE]',s);mant=bits[0];e=int(bits[1])if len(bits)==2 else 0
 if abs(e)>1000:raise ValueError('printed decimal exponent')
 d=len(mant.split('.')[1])if '.'in mant else 0;h=F(10)**(e-d);q=F(s)
 return dict(token=s,mid=str(q),step=str(h),lower=str(q-h/2),upper=str(q+h/2))
def inside(q,d):return F(d['lower'])<=q<=F(d['upper'])
def parse(text):
 lines=text.splitlines()
 if len(lines)!=6:raise ValueError('exact table line coverage')
 m=re.fullmatch(r'hsG_c2\.0_N(\d+)_log\.pt (\d+)x(\d+) c=2\.0: solver node \|F\|max \(maps\) ('+NUM+r');  resolved evaluator \(32, 10x16, 400, q=2\); rows: M collocation angles AT THE SAME NODES \((\d+) points\):',lines[0])
 if not m:raise ValueError('table header')
 n,n2,angular,count=map(int,[m[1],m[2],m[3],m[5]])
 if n!=n2 or n*angular!=count:raise ValueError('node count')
 rows=[]
 pattern=r'   r in \[('+NUM+r'), ('+NUM+r')\): max \|R_h\| ('+NUM+r')   max \|R_h\|/N_f ('+NUM+r')   max N_f ('+NUM+r')   median \|R_h\|/N_f ('+NUM+r')'
 for line,(lo,hi) in zip(lines[1:5],[(F(0),F('.1')),(F('.1'),F(1)),(F(1),F(100)),(F(100),F('1e300'))]):
  m=re.fullmatch(pattern,line)
  if not m or F(m[1])!=lo or F(m[2])!=hi:raise ValueError('ordered region row')
  rows.append(dict(lower=str(lo),upper=str(hi),**{key:interval(m[k])for key,k in [('absR',3),('Rf',4),('maxNf',5),('medianRf',6)]}))
 m=re.fullmatch(r'   argmax \|R_h\|/N_f at \(x, y\) = \(('+NUM+r'), ('+NUM+r')\), r = ('+NUM+r'), theta = ('+NUM+r') deg; R_h ('+NUM+r'), N_f ('+NUM+r')',lines[5])
 if not m:raise ValueError('argmax row')
 return dict(N=n,M=angular,count=count,solver_Fmax=interval(re.fullmatch(r'.* \(maps\) ('+NUM+r');.*',lines[0])[1]),rows=rows,argmax={k:interval(m[j])for k,j in [('x',1),('y',2),('r',3),('theta_degrees',4),('R',5),('Nf',6)]})
def matching(xy,arg):
 return [i for i,(x,y)in enumerate(xy)if all(inside(F(float(q)),arg[k])for k,q in [('x',x),('y',y),('r',math.hypot(x,y)),('theta_degrees',math.degrees(math.atan2(y,x)))])]
def descriptive(v,printed):
 den=F(printed['mid'])
 return dict(B_exact=str(v)if v is not None else None,B_float=float(v)if v is not None else None,producer_printed=printed,B_to_printed_midpoint=float(v/den)if v is not None and den else None,B_in_printed_rounding_interval=inside(v,printed)if v is not None else None)
def finite_values(ids,rr,region):
 vals=sorted(F(float(rr[i,3]))for i in ids if math.isfinite(rr[i,3]));mid=len(vals)//2;median=((vals[mid]+vals[mid-1])/2 if len(vals)%2==0 else vals[mid])if vals else None
 values={k:(F(float(region['metrics'][k]['value']))if region['metrics'][k]['value']is not None else None)for k in ['absR','Rf']}
 values.update(maxNf=max((F(float(rr[i,1]))for i in ids),default=None),medianRf=median)
 return values,len(vals),len(ids)-len(vals)
def main():
 checks=[];bindings={};outputs={};start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();fixture=len(sys.argv)>1
 def ck(n,b,e=None):
  checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:raise AssertionError((n,e))
 def bind(p,h=None):
  p=str(p);v=sha(p);ck('binding '+p,(h is None or h==v)and(p not in bindings or bindings[p]==v));bindings[p]=v;return Path(p)
 target=V/('PRINTED_MANUFACTURES.json'if fixture else'PRINTED_COMPARISON_CHECKS.json')
 try:
  for p in [__file__,R/'PRINTED_COMPARISON_PROOF.md',R/'FINAL_DESIGN_REVIEW_RESOLUTION_PROOF.md']:bind(p)
  if fixture:
   ck('explicit fixture flag',sys.argv==[sys.argv[0],'--manufactures'])
   for token,mid,step in [('1.805e-06',F(1805,10**9),F(1,10**9)),('-4.313e-09',-F(4313,10**12),F(1,10**12)),('.94',F(47,50),F(1,100)),('1.00e+2',F(100),F(1)),('0',F(0),F(1))]:
    q=interval(token);ck('exact interval '+token,F(q['mid'])==mid and F(q['step'])==step and F(q['lower'])==mid-step/2 and F(q['upper'])==mid+step/2);ck('closed endpoints '+token,inside(mid-step/2,q)and inside(mid+step/2,q)and not inside(mid+step,q))
   for token in ['NaN','Inf','1/2','1e1001','1.2junk','']:
    try:interval(token)
    except ValueError:ck('malformed rejected '+token,True)
    else:raise AssertionError(('accepted malformed',token))
   for n in [224,192]:
    p=bind(V/('producer_hs_node_check_c2_N'+str(n)+'.txt'));t=p.read_text();d=parse(t);ck('actual printed schema '+str(n),d['N']==n and d['M']==n//4)
    for bad in [t+'extra\n',t.replace('AT THE SAME NODES','other nodes'),t.replace('r in [0.1, 1)','r in [0.2, 1)'),t.replace(str(n*(n//4))+' points','1 points')]:
     try:parse(bad)
     except ValueError:ck('bad table rejected '+str(n),True)
     else:raise AssertionError('malformed table admitted')
   xy=np.array([[1.,1.],[2.,2.]]);arg={k:interval(s)for k,s in [('x','1.0'),('y','1.0'),('r','1.41'),('theta_degrees','45.0')]};ck('simultaneous matching',matching(xy,arg)==[0]);arg['theta_degrees']=interval('44.0');ck('contradictory coordinates',matching(xy,arg)==[])
   ck('zero printed midpoint descriptive',descriptive(F(1),interval('0'))['B_to_printed_midpoint']is None)
   ck('undefined B descriptive',descriptive(None,interval('1.0'))['B_in_printed_rounding_interval']is None)
   empty=dict(metrics={'absR':dict(value=None),'Rf':dict(value=None)})
   values,defined,undefined=finite_values([],np.empty((0,5)),empty);ck('empty region descriptive',all(v is None for v in values.values())and defined==undefined==0)
   zerorr=np.array([[0.,0.,0.,np.nan,np.nan]]);zero=dict(metrics={'absR':dict(value=0.),'Rf':dict(value=None)})
   values,defined,undefined=finite_values([0],zerorr,zero);ck('all undefined median descriptive',values==dict(absR=F(0),Rf=None,maxNf=F(0),medianRf=None)and defined==0 and undefined==1)
   status='PASS_PRINTED_INTERVAL_MANUFACTURES'
  else:
   d=json.loads(bind(V/'FINAL_ARITHMETIC_CHECKS.json').read_text());ck('final arithmetic gate',d['status']=='PASS_FINITE_LARGER_NODE_ARITHMETIC_REQUIRES_FINAL_REVIEW'and d['count']==len(d['checks'])and all(z['passed']for z in d['checks'])and not d['synthetic_only'])
   for p,h in d['bindings'].items():bind(p,h)
   m=json.loads(bind(V/'PRINTED_MANUFACTURES.json').read_text());ck('printed manufacture gate',m['status']=='PASS_PRINTED_INTERVAL_MANUFACTURES'and m['count']==len(m['checks'])and all(z['passed']for z in m['checks']))
   for p,h in m['bindings'].items():bind(p,h)
   results=[]
   for st in d['outputs']['states']:
    n=st['N'];pt=bind(V/('producer_hs_node_check_c2_N'+str(n)+'.txt'));p=parse(pt.read_text());ck('state printed identity '+str(n),(p['N'],p['M'],p['count'])==(n,st['M'],st['points']))
    with np.load(bind(V/'candidate'/('N'+str(n)+'_B.npz')),allow_pickle=False)as z:xy=z['xy'];rr=z['residual']
    radius=np.hypot(xy[:,0],xy[:,1]);rows=[]
    for region,printed in zip(st['regional_summaries'],p['rows']):
     ids=[i for i,r in enumerate(radius)if F(printed['lower'])<=F(float(r))<F(printed['upper'])];ck('finite region count '+str((n,region['region'])),len(ids)==region['count']);values,defined,undefined=finite_values(ids,rr,region)
     comparisons={k:descriptive(v,printed[k])for k,v in values.items()}
     rows.append(dict(region=region['region'],count=len(ids),median_defined_count=defined,median_undefined_count=undefined,metrics=comparisons))
    matches=matching(xy,p['argmax']);results.append(dict(N=n,M=st['M'],source=st['source'],rows=rows,producer_argmax=p['argmax'],printed_argmax_geometrically_compatible=bool(matches),compatible_node_indices=matches,B_at_compatible_nodes=[dict(index=i,fields=list(map(float,rr[i])))for i in matches],raw_solver_Fmax_metadata=p['solver_Fmax']))
   outputs=dict(states=results,scope='Printed-rounding intervals only; independent B comparisons use different finite rules and derivatives. Historical argmax and map residual unverified; no exact integral bounds.',median_convention='Undefined entries excluded and counted; empty set null. Exact rational mean of central pair, rounded once only for display');status='PASS_FINITE_PRINTED_COMPARISONS'
  for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
 except Exception:
  status='FAIL';outputs['error']=traceback.format_exc();print(outputs['error'])
 out=dict(status=status,python_flags=repr(sys.flags),synthetic_only=fixture,started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,count=len(checks),checks=checks,bindings=bindings,outputs=outputs);target.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(status,len(checks))
 if status=='FAIL':raise SystemExit(1)
if __name__=='__main__':main()
