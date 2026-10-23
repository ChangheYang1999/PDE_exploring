"""Independent verification of the exact v4 edits and exceptional horizontal coefficient."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
import sympy as S
import mpmath as mp
r=Path('research/sec378_text_audit');v=r/'verification/v4';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
out={'status':'RUNNING','start_utc':utc(),'proof_sha256':sha(r/'V4_PROOF.md'),'code_sha256':sha(__file__),'checks':[]}
def save():(v/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,ok,evidence=None):
 out['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
 if not ok:out['status']='FAILED';save();raise AssertionError(name)
def zero(name,e):check(name,S.factor(e)==0)
p,z=S.symbols('p z',positive=True);a=(1+p)/2;n=a*p;q=n+p-1;s=p-1/a
zero('higher cusp relative order',a*(p+2)+p-3-q-p+1)
zero('unbalanced smooth gap',q-(3*p-2)-(1-p)*(2-p)/2)
zero('unbalanced smooth enters earlier',-(1-p)*(2-p)/2-(p-1)-p*(1-p)/2)
zero('bottom slow velocity',n-a*s-1)
zero('bottom remainder exponent',n-a*(p-2)-p-1)
zero('moment integration boundary infinity',p-s-2-(1/a-2))
zero('special half gamma argument',p/(p+1)-(1-p)/2-(s+1)/2)
zero('vertical line exponent',n-2*a-n+p+1)
star=S.sqrt(2)-1
zero('special zero',s.subs(p,star)+1)
zero('special hypergeometric cancellation',(p/(p+1)-(1-p)/2).subs(p,star))
# Derivative identity checked independently in the defining convergent series.
for j in range(7):zero('confluent derivative series '+str(j),(p-2*j)*S.rf(-p/2,j)-p*S.rf(1-p/2,j))
for pr in [S.Rational(1,10),S.Rational(1,3),S.Rational(1,2),S.Rational(9,10)]:
 check('both horizontal endpoint inequalities '+str(pr),(-s).subs(p,pr)>0 and(p-s-2).subs(p,pr)<0)
for entry in json.loads((v/'INPUTS.json').read_text())['sources']:check('frozen hash '+entry['source'],sha(entry['frozen'])==entry['sha256'])
mp.mp.dps=90
pp=mp.sqrt(2)-1;aa=(1+pp)/2;dd=1/(1+pp);a1=-pp/2;a2=(1-pp)/2;b1=pp/(1+pp)
for KK,CC in [(mp.mpf(1),mp.mpf(1)),(mp.mpf('.3'),mp.mpf(-2)),(mp.mpf(4),mp.mpf('.2'))]:
 ll=4*pp*pp*KK/((pp+1)**2*(1-pp));HH=pp*KK*CC/(1/pp-1)
 closed=-HH*pp/(2*aa)*ll**((pp-1)/2)*mp.gamma((1-pp)/2)*mp.sqrt(mp.pi)/(mp.gamma(1-pp/2)*mp.gamma((3+pp)/2))
 O2=mp.gamma(1+dd)*mp.gamma(2+dd)*mp.gamma(-mp.mpf('.5'))*mp.rgamma(a1+dd)*mp.rgamma(1-a2)*mp.rgamma(2-a2)*ll**(-(a2+dd))
 ratio=mp.gamma(b1)*mp.gamma(2)*mp.gamma(-mp.mpf('.5'))*ll**(-a2)/(2*mp.gamma(a1)*mp.gamma(2-a2))
 connected=CC*(pp+3)*ratio/(2*O2)
 check('special B independent gamma identity '+str((KK,CC)),abs(connected-closed)<mp.mpf('1e-75'),mp.nstr(abs(connected-closed),15))
 check('special B nonzero sign '+str((KK,CC)),closed*CC<0,mp.nstr(closed,50))
 for zz in [mp.mpf('.2'),mp.mpf(1),mp.mpf(3)]:
  direct=mp.diff(lambda zz:HH*zz**pp*mp.hyp1f1(-pp/2,2,-ll/zz**2),zz)
  formula=HH*pp*zz**(pp-1)*mp.hyp1f1(1-pp/2,2,-ll/zz**2)
  check('special derivative identity '+str((KK,CC,zz)),abs(direct-formula)<mp.mpf('1e-75'))
  check('special derivative strict sign '+str((KK,CC,zz)),formula*CC>0)
body=(v/'body.txt').read_text();app=(v/'app.txt').read_text();compact=lambda t:' '.join(t.split())
for name,needle,txt in [('bounded','bounded at z = 0',body),('derivative hypothesis',"h'' = O(z^{p - 2})",body),('moment scope','for the displayed leading layer and f_p',body),('completion scope','this says nothing about the outer and core terms not constructed here',body),('allowed degrees','The matching allows in the outer region',body),('local bounds','In the near-axis region r ~ y',body),('nonzero horizontal','the horizontal term B sgn(xi) remains',body),('Barnesprefactor','Gamma(b_1) Gamma(b_2)/(Gamma(a_1) Gamma(a_2)) times (1/(2 pi i))',app),('Barnescontour','the contour is not a vertical line',app),('corrected fit','4.1e-7 for the even and 5.4e-5 for the odd coefficients (absolute)',app),('exact root zero','the exact zero follows from the Gamma formula',app),('notationH',"H'' + mu^2 (th - m)(th - l) W = 0",app),('no endpoint','nor existence, nor nonexistence',body)]:check('v4 repair '+name,compact(needle) in compact(txt))
fits=json.loads((r/'verification/CHECKS.json').read_text())['printed_fits'];check('repaired exactfit bounds',fits['max_even_absolute_discrepancy']<4.1e-7 and fits['max_odd_absolute_discrepancy']<5.4e-5)
raw=(v/'external_results.txt').read_text();odes=[mp.mpf(a)for a in re.findall(r'ODE absolute residual = (\S+)',raw)];ints=[abs(mp.mpf(a))for a in re.findall(r'canonical integral discrepancy = (\S+)',raw)]
check('external five residualrows',len(odes)==5 and len(ints)==5)
check('external reportedODEbounds',max(odes)<mp.mpf('1.2e-55'),mp.nstr(max(odes),15))
check('external reportedcanonicalbounds',max(ints)<mp.mpf('1.4e-30'),mp.nstr(max(ints),15))
check('external Opus limitation recorded','Opus 5.5 collaboration was unavailable' in (v/'external_answer.md').read_text())
for f in [r/'verification/v2/CHECKS.json',Path('research/hydrostatic_inner_layer_audit/verification/FOLLOWUP_CHECKS.json')]:
 d=json.loads(f.read_text());check('own dependency '+str(f),d['status']=='DONE' and all(x['passed']for x in d['checks']),{'sha256':sha(f),'count':len(d['checks'])})
out.update(status='DONE',finished_utc=utc(),count=len(out['checks']));save();print(json.dumps({'status':'DONE','count':out['count']}))
