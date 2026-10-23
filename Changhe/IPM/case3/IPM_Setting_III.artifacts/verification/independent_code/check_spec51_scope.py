from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,difflib
R=Path('research/spec50_consistency_audit');V=R/'verification'/'v51';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda s:' '.join(s.split())
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
for x in json.loads((V/'INPUTS.json').read_text())['files']:ck('frozen '+Path(x['frozen']).name,sha(x['frozen'])==x['sha256'])
ck('v51hash',sha(V/'SPEC_v51.md')=='9bde2eb239e5d7be2eefeb17b5940c93bdca56abe0a82b79c1ae3ac0303f2a62')
a=(R/'verification'/'SPEC_v50.md').read_text();b=(V/'SPEC_v51.md').read_text()
g43=b[b.index(' (G43)'):b.index(' (G44)')];g44=b[b.index(' (G44)'):b.index('## CHANGELOG')];cl=b[b.index('- v51'):b.index('- v50')]
oldprefix=a[:a.index(' (G43)')].replace('Version v50, 2026-10-21T15:53Z','Version v51, 2026-10-21T16:13Z',1)
ck('entireprefixexceptversion',oldprefix==b[:b.index(' (G43)')]);ck('entireoldchangelog',a[a.index('- v50'):]==b[b.index('- v50'):])
for phrase in ['0 < t < 1','C > 0','H(0) = 0',"H'(0) != 0",'1 < P <= 2','nonempty open interval of y > 0','equality at single points is not excluded','each expansion finite, degrees unbounded','no degree-uniform residual bound','NOT a NO endpoint']:
 ck('theorem repaired '+phrase,phrase in flat(g43))
ck('degenerate C0 explanation remains','C = 0 gives G = 0 and the claim fails'in g43)
t=F(1,2);w=1-t*t;y=t/w**2;G=t/w;Gy=(1+t*t)*w/(1+3*t*t)
ck('C0 noncoordinate',0*t/w**2==0);ck('singleton equality',F(7,5)*y*Gy==G);ck('singletonpositive',y>0)
for phrase in ['100 <= y <= 1e12','.0761','.00326','.00344','.000311','96 -> 128 -> 160','continuation of the capped 128 state raises it slightly','not converged']:
 ck('G44 repaired '+phrase,phrase in flat(g44))
ck('complete search ambiguity remains','complete axis search'in flat(g44))
d=json.loads((V/'axis_SUMMARY.json').read_text());ck('axisgate',d['status']=='PASS'and d['count']==332 and all(x['passed']for x in d['checks']));v=[F(s['maxima']['12']['R_Nf']['R_Nf'])for s in d['states']]
ck('two resolutions128between96and160',v[0]>max(v[1:3])>min(v[1:3])>v[3]);ck('continued128rises',v[2]>v[1],float(v[2]/v[1]-1))
ck('axis scope not exhaustive','root completeness and plane supremum OPEN'in d['scope'])
for phrase in ['63 saved converged states','within 5e-6 relative','table to its displayed precision','4.0000 to the displayed precision','not exactly 4','UNRESOLVED']:
 ck('history repaired '+phrase,phrase in flat(cl))
ck('wrong attribution249','checker 249 repairs of 16:07Z'in flat(cl))
g=json.loads((V/'v50_CHECKS.json').read_text());ck('prior v50 audit35',g['status']=='PASS'and g['count']==35)
A=a.splitlines(True);B=b.splitlines(True);ops=[x for x in difflib.SequenceMatcher(a=A,b=B,autojunk=False).get_opcodes()if x[0]!='equal'];rev=B[:]
for o,l,h,k,m in reversed(ops):rev[k:m]=A[l:h]
ck('exactbyte reverse',''.join(rev)==a)
(V/'CHANGES.json').write_text(json.dumps([dict(op=o,old_lines=[l,h],new_lines=[k,m],old=''.join(A[l:h]),new=''.join(B[k:m]))for o,l,h,k,m in ops],indent=2)+'\n')
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,verdict='REPAIRS_REQUIRED',proof_sha256=sha(R/'V51_PROOF.md'),driver_sha256=sha(__file__),repairs=['Replace C=0 explanation by C=0 does not parametrize positive y.','Replace complete axis search by finite axis search using the complete inverse; no root completeness or certified suprema.','Changelog16:07 scope repairs are result250, not249.'])
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
