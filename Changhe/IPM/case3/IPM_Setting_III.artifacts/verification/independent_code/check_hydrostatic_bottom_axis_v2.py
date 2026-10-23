"""Result204 transcription and added negative-axis countercheck after standalone proof."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib
import numpy as np
import sympy as s
r=Path('research/hydrostatic_bottom_axis_v2_audit/verification');checks=[]
def ck(name,ok,detail=None):checks.append(dict(name=name,pass_=bool(ok),detail=detail))
b=(r/'body_v2.txt').read_text();a=(r/'app_v2.txt').read_text();o=(r/'body_v1.txt').read_text();q=(r/'app_v1.txt').read_text()
for row in json.loads((r/'INPUTS.json').read_text())['files']:ck('frozen hash '+row['name'],hashlib.sha256((r/row['name']).read_bytes()).hexdigest()==row['sha256'])
prior=json.loads((r/'checks202.json').read_text());ck('prior112 independent checks all passed',prior['pass_count']==112 and prior['fail_count']==0)
body_phrases=['let h be C^1 on {y >= 0} and b continuous there with a continuous partial derivative b_y','an open ball N','At a positive vertical-axis point','with v > 0 and G\' > 0','the roots, as |eta| -> inf','For the frozen linearization of the evolution in xi at a positive axis point','expected local dimension zero','a local slice for the dilation would have an isolated zero in (k, c)','this heuristic gives no global discreteness or selection statement for c']
app_phrases=['no derivative b_xi is needed or asserted','on a neighbourhood of its closure','M and N_0 below are finite','for j >= 1, and d/2 for j = 0','Rouche\'s theorem shows','G_*\'(y) >= c_1 (1 + |y|)^{p-1} on R','for integers m >= 1, the set S_m','every integer n >= 1','C\' = max(C\'\', C\'\'/gamma)','no corresponding bound for H_xi is used','P . T(P) >= |P|^2/2','C(P) e^{tau/2}','no mode with lambda = 0 is lost','At a positive axis point (v > 0, G\' > 0)','On the compact arc arctan(1) <= th <= arctan(2) of the unit circle','homogeneity and parity propagate the strict signs']
for z in body_phrases:ck('body repair '+z,z in b)
for z in app_phrases:ck('appendix repair '+z,z in a)
ck('all displayed body equations byte-identical',[z for z in b.splitlines()if z.startswith('@@')]==[z for z in o.splitlines()if z.startswith('@@')])
ck('all displayed appendix equations byte-identical',[z for z in a.splitlines()if z.startswith('@@')]==[z for z in q.splitlines()if z.startswith('@@')])
ck('old unbounded cone lower bound removed','bounded below by positive constants'not in a)
for phrase in ['Whether a C^inf or C^2 solution is determined by k is not known','Whether the series for G_* itself diverges is not decided','The domain of this map, its differentiability and any contraction property are not established','none of (a)-(e) establishes existence or nonexistence']:
 ck('scope retained '+phrase,phrase in b and phrase in o)
# Independent direct determinant and exact local triple, without importing the lead checker.
x,y,c,la,eta=s.symbols('x y c la eta',real=True);g=y;h=(c-1)*x;bb=y
ck('manufactured local h_y=g_x',s.diff(h,y)==s.diff(g,x))
ck('manufactured local b_y=c-h_x',s.diff(bb,y)==c-s.diff(h,x))
ck('manufactured local transport',s.expand((c*x+h)*s.diff(g,x)+bb*s.diff(g,y)-g)==0)
mat=s.Matrix([[y*la+s.I*(2*c-1)*x*eta-1,0,1],[-s.I*eta,la,0],[0,s.I*eta,la]])
ck('positive-axis determinant',s.expand(mat.det().subs({x:0,y:1})-(la**3-la**2+eta**2))==0)
ck('negative-axis determinant',s.expand(mat.det().subs({x:0,y:-1})-(-la**3-la**2+eta**2))==0)
roots=[]
for side,target in ((1,.5),(-1,1.)):
 errors=[]
 for t in (10.,100.,1000.,10000.):
  rr=np.roots([side,-1/t,0,1]);maximum=float(max(rr.real));err=abs(maximum-target);errors.append(err);roots.append(dict(y=side,t=t,scaled_max_real=maximum,error=err))
 ck('axis scaled maximal real converges '+str(side),all(errors[i+1]<errors[i]for i in range(3))and errors[-1]<4e-5,errors)
ck('external review explicitly not Opus', 'Opus' in (r/'external_hostile_review.md').read_text() and 'credential' in (r/'external_hostile_review.md').read_text().lower())
ledger=[]
for tag,old,new in [('body',o,b),('appendix',q,a)]:
 words1=old.split();words2=new.split();blocks=[];reverse=[]
 for op,i,j,k,l in difflib.SequenceMatcher(None,words1,words2,autojunk=False).get_opcodes():
  reverse.extend(words2[k:l]if op=='equal'else words1[i:j])
  if op!='equal':blocks.append(dict(old=' '.join(words1[i:j]),new=' '.join(words2[k:l]),old_word_span=[i,j],new_word_span=[k,l]))
 ck(tag+' reverse changes recover complete previous source',reverse==words1)
 ledger.append(dict(document=tag,blocks=blocks))
(r/'ALL_CHANGES.json').write_text(json.dumps(ledger,indent=2)+'\n')
out=dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,root_countercheck=roots,pass_count=sum(t['pass_']for t in checks),fail_count=sum(not t['pass_']for t in checks),verdict='CONFIRMED within the stated scopes if all checks pass. Local proof, genericity and formal symbol only; no decisive endpoint.')
(r/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['pass_count'],'PASS',out['fail_count'],'FAIL',[(z['document'],len(z['blocks']))for z in ledger])
for t in checks:
 if not t['pass_']:print('FAIL',t)
if out['fail_count']:raise SystemExit(1)
