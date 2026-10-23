"""Light independent finite-part manufacture and frozen revision checks."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
import sympy as S
import mpmath as mp
r=Path('research/sec378_text_audit');v=r/'verification/v2';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
out={'status':'RUNNING','start_utc':utc(),'proof_sha256':sha(r/'V2_PROOF.md'),'code_sha256':sha(__file__),'checks':[],'gaussian':[]}
def save():(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
 out['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
 if not ok:out['status']='FAILED';save();raise AssertionError(name)
def zero(name,e):check(name,S.factor(e)==0)
p,z,nu,beta=S.symbols('p z nu beta',positive=True);a=(1+p)/2;n=a*p;s=p-1/a;q=n+p-1
zero('axis coefficient',(1/p-1/s)/a-1/(n*(1-n)))
for j in range(6):
 # Canonical integral response to a local b'' monomial, excluding the global cusp coefficient.
 coeff=(1/(p-2*j)+1/(2*j-s))/a
 zero('Euler inverse on smooth local monomial '+str(j),a*a*(2*j-p)*(2*j-s)*coeff+1)
zero('correction root m',nu/a-(p+beta/a).subs(beta,nu-n))
zero('correction root k',(nu-1)/a-(p+(beta-1)/a).subs(beta,nu-n))
zero('correction root r',2*(1-nu)/(1-p)-(p+2-beta/(1-a)).subs(beta,nu-n))
zero('recessive exponent',5+2*p+s-(3+3*p+2*p/(p+1)))
zero('counterexample b second derivative',S.diff(S.cos(z*z),z,2)+2*S.sin(z*z)+4*z*z*S.cos(z*z))
for path in [r/'verification/CHECKS.json',Path('research/hydrostatic_inner_layer_audit/verification/CHECKS.json'),Path('research/hydrostatic_inner_layer_audit/verification/FOLLOWUP_CHECKS.json')]:
 d=json.loads(path.read_text());check('prior independent dependency '+str(path),d['status']=='DONE' and all(c['passed'] for c in d['checks']),{'sha256':sha(path),'count':len(d['checks'])})
for row in json.loads((v/'INPUTS.json').read_text())['inputs']:check('frozen source '+row['source'],sha(row['frozen'])==row['sha256'])
mp.mp.dps=75
for pp in [mp.mpf('.1'),mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),mp.mpf('.9')]:
 aa=(1+pp)/2;ss=pp-1/aa;nn=aa*pp
 def integrand(u):
  if not u:return 6/(2-pp)
  t=u**(1/(2-pp));tt=t*t
  return (4*mp.exp(-tt)-2*mp.expm1(-tt)/tt)/(2-pp)
 lower=mp.quad(integrand,[0,mp.mpf('.2'),1]);upper=mp.quad(lambda t:t**(-pp-1)*(4*t*t-2)*mp.exp(-t*t),[1,2,4,mp.inf]);finite=lower+upper+2/pp
 gamma=2*mp.gamma(1-pp/2)-mp.gamma(-pp/2);err=abs(finite-gamma);check('Gaussian convergent finitepart p='+str(pp),err<mp.mpf('1e-60'),mp.nstr(err,12))
 def raw(zz):return 2*mp.gammainc(1-pp/2,zz*zz,mp.inf)-mp.gammainc(-pp/2,zz*zz,mp.inf)
 def val(zz):
  low=2*mp.gammainc(1-ss/2,0,zz*zz)-mp.gammainc(-ss/2,0,zz*zz)
  return (-gamma*zz**pp+zz**pp*raw(zz)+zz**ss*low)/aa
 rows=[]
 for zz in [mp.mpf('.1'),mp.mpf('.05'),mp.mpf('.025')]:
  scaled=(raw(zz)+2*zz**(-pp)/pp-gamma)/zz**(2-pp);want=-6/(2-pp)
  check('finitepart rate and sign '+str((pp,zz)),abs(scaled-want)<mp.mpf('.06'),mp.nstr(scaled,15));rows.append({'z':str(zz),'scaled_error':mp.nstr(scaled,30)})
 zz=mp.mpf('.0001');value=val(zz);axis=-2/(nn*(1-nn));coeff=6*(1/(pp-2)+1/(2-ss))/aa
 check('smooth manufactured axis curvature '+str(pp),abs((value-axis)/zz**2-coeff)<mp.mpf('2e-7'))
 out['gaussian'].append({'p':str(pp),'F_integral':mp.nstr(finite,60),'F_gamma':mp.nstr(gamma,60),'cusp_cancelling_Cp':mp.nstr(-gamma/aa,60),'rates':rows})
body=(v/'body.txt').read_text();app=(v/'app.txt').read_text()
for name,needle,txt in [('local scope','This is not a complete remainder estimate',body),('earlier outer order','y^{mu (p - 1)}',body),('finitepart identity','F = -mu C_p(Theta)',app),('first resonance','sqrt(5) - 2',app),('second resonance','sqrt(17) - 3',app),('bounded qualifier missing','every bounded solution',body),('derivative growth missing','For even h, smooth at z = 0 and O(z^p)',body),('fit repair still missing','about 1e-8 for the even and 1e-5 for the odd coefficients',app),('global scope','Nothing here shows that solutions',body)]:
 check('frozen text '+name,needle in txt)
fit=json.loads((r/'verification/CHECKS.json').read_text())['printed_fits'];out['inherited_exact_fit_errors']=fit
check('v2 exact oldfit exceeds1e-8',fit['max_even_absolute_discrepancy']>1e-8)
check('v2 exact oldfit exceeds1e-5',fit['max_odd_absolute_discrepancy']>1e-5)
producer=(v/'producer_chk_layer3.txt').read_text();check('producer approximate A failure visible','quad (approx small-t part) 14969.756' in producer)
out.update(status='DONE',finished_utc=utc(),count=len(out['checks']));save();print(json.dumps({'status':'DONE','count':out['count']}))
