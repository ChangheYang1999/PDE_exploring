"""Exact revised text and endpoint checks; result209 PROOF.md."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
import sympy as sp
import mpmath as mp
r=Path('research/hydrostatic_second_compatibility_v2_audit/verification');checks=[]
norm=lambda s:' '.join(s.split())
def ck(n,v,detail=None):checks.append(dict(name=n,pass_=bool(v),detail=detail))
bs={k:(r/(k+'.txt')).read_text()for k in ['body_v1','body_v2','app_v1','app_v2']}
for name,want in [('body_v2','c1a900ccece186442f6da48c159d7fa01fd5c4eaadc02f3fa7560af3c83ef372'),('app_v2','d73ea0a78db3b4b918e3b46542fae2b4813655a0eacfbf19da4d78ac70d4e809')]:ck(name+'exactsha',hashlib.sha256(bs[name].encode()).hexdigest()==want)
for name in ['body','app']:
 old=[l for l in bs[name+'_v1'].splitlines()if l.startswith('@@')];new=[l for l in bs[name+'_v2'].splitlines()if l.startswith('@@')];ck(name+' all displayed equations unchanged',old==new,len(old))
b=norm(bs['body_v2']);a=norm(bs['app_v2']);h=(r/'hostile_review.md').read_text()
for phrase in ['the statements about f_{3p-2} defined by (1) proved','the expansion that leads to (1) formal','with V[f]','smooth on R^2 minus the origin','0 < d < 1','a nonzero axis curvature of f_d makes its unmatched lower velocity integral diverge','matching to a core must in general be included','no hydrostatic solution is constructed','expansions with angular layers or other matching are not excluded']:
 ck('bodyscope '+phrase,phrase in b)
for phrase in ['For the smooth streams constructed below','the chart W_* is used only through (A2) and (A3)','a smooth odd extension through s = 0','for j = 1, 2, 3 (a bound on W\' alone would not suffice)','with the corresponding differentiated expansion and no constant term','Smoothness of V follows from the explicit local stream formulas above','the positive axis limits follow from the W_0 component','normalization f(0, 1) = 1','relative discrepancies below 1e-9; this is a numerical check']:
 ck('appendixrepair '+phrase,phrase in a)
ck('hostileOpusattemptnotcredited','no Opus review was obtained'in h)
s,p=sp.symbols('s p',positive=True);W=sp.Function('W')(s);F=sp.Function('F')(s)
vp=s*sp.diff(W,s)-(p+1)*W
ck('V2_yformula',sp.simplify(sp.diff(vp,s)-(s*sp.diff(W,s,2)-p*sp.diff(W,s)))==0)
ck('V2_yyformula',sp.simplify(sp.diff(vp,s,2)-((1-p)*sp.diff(W,s,2)+s*sp.diff(W,s,3)))==0)
wp=s**(p-1)*sp.sin(s*s)
ck('weakboundcounterexampleexact',sp.simplify(s*sp.diff(wp,s)-p*wp-(2*s**(p+1)*sp.cos(s*s)-s**(p-1)*sp.sin(s*s)))==0)
# Distinct nonpositive-degree axis divergences, with an exact lower cutoff.
e=sp.symbols('e',positive=True)
for d in [sp.Integer(0),-sp.Rational(1,3),-sp.Integer(1)]:
 val=sp.integrate(s**(d-1),(s,e,1));ck('lowerinverseaxisdivergence d='+str(d),sp.limit(val,e,0,dir='+')==sp.oo)
with mp.workdps(50):
 for p in [mp.mpf('.6'),mp.mpf('.75'),mp.mpf('.9')]:
  C=1/(p+2);W0=lambda s:C*s*(1+s*s)**((p-1)/2)
  for j in [1,2,3]:
   lead=C*mp.fprod(p-k for k in range(j));value=mp.diff(W0,mp.mpf('1e5'),j)/mp.mpf('1e5')**(p-j)
   ck('constructedstreamderivtail '+str(p)+' j'+str(j),abs(value-lead)<mp.mpf('1e-8'),mp.nstr(abs(value-lead),12))
  for delta in [mp.mpf('.001'),mp.mpf('.1')]:
   K=(1-p)*(p+2)/2;axis=3*C*delta/(K+delta)
   ck('strictnormalizedhorizontalaxis '+str(p)+' '+str(delta),axis>0 and p>0)
# Every word change is already manually read and retained in this immutable ledger.
c=json.loads((r/'ALL_WORD_CHANGES.json').read_text());ck('sixbodytwentythreeappwordblocks',len(c['body'])==6 and len(c['app'])==23)
ck('previous205allchecksPASS',json.loads((r/'prior205_checks.json').read_text())['fail_count']==0)
out=dict(utc=datetime.now(timezone.utc).isoformat(),checks=checks,pass_count=sum(c['pass_']for c in checks),fail_count=sum(not c['pass_']for c in checks),verdict='CONFIRMED v2 exact text if allchecksPASS. The general-W and numericalwording repairs supersede205 blanketconfirmation.')
(r/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['pass_count'],'PASS',out['fail_count'],'FAIL')
for t in checks:
 if not t['pass_']:print('FAIL',t)
if out['fail_count']:raise SystemExit(1)
