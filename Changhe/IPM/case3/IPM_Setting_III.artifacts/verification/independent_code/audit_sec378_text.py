"""Claim arithmetic and independent symbolic checks of frozen sec378v1."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']: os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
import sympy as S
r=Path('research/sec378_text_audit');utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
out={'status':'RUNNING','start_utc':utc(),'proof_sha256':sha(r/'PROOF.md'),'code_sha256':sha(__file__),'checks':[]}
def save():(r/'verification/CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
 out['checks'].append({'name':name,'passed':bool(ok),'evidence':evidence})
 if not ok:out['status']='FAILED';save();raise AssertionError(name)
def zero(name,e):check(name,S.factor(e)==0)
p,z,y,x,K,Q,w=S.symbols('p z y x K Q w',positive=True)
a=(p+1)/2;n=a*p;q=n+p-1;s=p-1/a;c=1/p;D=c-1
zero('q formula',q-(p*p+3*p-2)/2)
zero('s formula',s-(p+2)*(p-1)/(p+1))
zero('density inverse exponent',q-2*a-n+2)
zero('smoothness weak bound1',(n-2*a)-(p-2)-(1-p)*(2-p)/2)
zero('smoothness weak bound2',(n-2*a)-(n-2)-(1-p))
zero('q above p-1',q-p+1-n)
zero('q below d2',2*p-1-q-p*(1-p)/2)
zero('n above d2',n-2*p+1-(1-p)*(2-p)/2)
zero('p above n',p-n-p*(1-p)/2)
zero('velocity below p',p-(1+s)-(1-p)/(p+1))
zero('velocity above d2',1+s-(2*p-1)-p*(1-p)/(p+1))
zero('density below d2',2*p-1-(p+s)-(1-p)/(p+1))
zero('density above d3',p+s-(3*p-2)-p*(1-p)/(p+1))
zero('density transport denominator',c*(p+s)-1-c*s)
zero('layer second outer mode degree',q+(1-a)*s-p-s)
zero('velocity mode physical degree',n+(1-a)*s-1-s)
zero('first outer cusp exponent',a*p+p-1-q)
zero('third infinity mode degree',q-a*(p+2)+2)
for pr,expected in [(S.Rational(1,2),[-S.Rational(1,8),S.Rational(1,6),-S.Rational(1,3)]),(S.Rational(1,3),[-S.Rational(4,9),-S.Rational(1,6),-S.Rational(5,6)])]:
 for name,expr,target in zip(['q','1+s','p+s'],[q,1+s,p+s],expected):zero(f'c={1/pr} '+name,expr.subs(p,pr)-target)
# Compact-angular inverse counterexample, with exact endpoint-compatible polynomial manufacture.
d=2*p-1;F=(w-1)**4*(2-w)**4
operator=d*(d-1)*F-2*(d-1)*w*S.diff(F,w)+w*w*S.diff(F,w,2)
integral=S.integrate(w*operator,(w,1,2));moment=S.integrate(w*F,(w,1,2))
zero('manufactured compact angular inverse identity',integral-(d+1)*(d+2)*moment)
check('manufactured moment positive',moment>0,str(moment))
for k in [0,1,2,3]:
 for endpoint in [1,2]:zero(f'manufacture endpoint derivative{k} at{endpoint}',S.diff(F,w,k).subs(w,endpoint))
zero('intermediate velocity power',a*d-n-a*(p-1))
zero('intermediate power exceeds claimed',a*(p-1)-(p-1)-(1-p)**2/2)
for pr in [S.Rational(1,10),S.Rational(1,3),S.Rational(1,2),S.Rational(9,10)]:
 check('nonzero canonical angular counterexample '+str(pr),integral.subs(p,pr)>0)
 check('missing order earlier than claimed '+str(pr),(a*(p-1)-(p-1)).subs(p,pr)>0)
# Freeze the exact printed producer fits without executing its code.
source=Path('../analysis/runs/chk_layer2.txt');data=source.read_bytes();(r/'verification/producer_chk_layer2.txt').write_bytes(data);out['producer_log_sha256']=sha(source)
rows=[]
for line in data.decode().splitlines():
 mt=re.search(r'sol (\d+) even fit/gamma (\S+) (\S+)  odd fit/gamma (\S+) (\S+)',line)
 if mt:
  j,ef,eg,of,og=mt.groups();ef,eg,of,og=map(float,[ef,eg,of,og]);rows.append({'branch':int(j),'even_fit':ef,'even_gamma':eg,'odd_fit':of,'odd_gamma':og,'even_abs_difference':abs(ef-eg),'odd_abs_difference':abs(of-og)})
check('ten printed fit pairs',len(rows)==10)
maxe=max(t['even_abs_difference'] for t in rows);maxo=max(t['odd_abs_difference'] for t in rows)
check('even claimed precision too optimistic',maxe>1e-7,maxe)
check('even repaired rounded maximum',maxe<5e-7,maxe)
check('odd repaired rounded maximum',maxo<6e-5,maxo)
out['printed_fits']={'rows':rows,'max_even_absolute_discrepancy':maxe,'max_odd_absolute_discrepancy':maxo}
body=(r/'verification/body.txt').read_text();app=(r/'verification/app.txt').read_text()
for name,needle,txt in [('body total remainder','terms not kept are smaller by a factor O(y^{p - 1})',body),('appendix unspecified completion','the products with f_s and V_s, smaller by O(y^{p - 1})',app),('checks precision','to\nabout 1e-8 for the even and 1e-5 for the odd coefficients',app),('scope leading','leading inner order only',body),('no endpoint','neither that solutions have such layers, nor existence, nor nonexistence',body)]:
 check('frozen text anchor '+name,needle in txt)
for name in ['CHECKS.json','FOLLOWUP_CHECKS.json']:
 f=Path('research/hydrostatic_inner_layer_audit/verification')/name;dct=json.loads(f.read_text());check('own dependency done '+name,dct['status']=='DONE' and all(t['passed'] for t in dct['checks']));out[name+'_sha256']=sha(f)
out['status']='DONE';out['finished_utc']=utc();out['count']=len(out['checks']);save();print(json.dumps({'status':out['status'],'count':out['count'],'max_even_fit_discrepancy':maxe,'max_odd_fit_discrepancy':maxo}))
