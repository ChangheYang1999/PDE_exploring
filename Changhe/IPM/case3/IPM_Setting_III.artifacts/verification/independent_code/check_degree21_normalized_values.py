from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from exact_degree21 import decode,prim,divexact,h,degree,univ,shifted
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';checks=[];rows=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def evalpoly(co,z):
 v=F(0)
 for c in co:v=v*z+c
 return v
for index,aa,b,L,expected_e,expected_der in [(4,4,8,2,[F(35,88),F(6425,15488)],F(71745,15488)),(7,2,6,3,[F(2,11),F(273,968),F(1285,10648)],F(165445,21296))]:
 eta=F(23);fixed=eta-1;single=-eta;power=[F(L)]+[-(fixed**k+aa*single**k)/b for k in range(1,L+1)];co=[F(1)]
 for k in range(1,L+1):co.append(-(power[k]+sum(co[j]*power[k-j]for j in range(1,k)))/k)
 es=[(-1)**k*co[k]/fixed**k for k in range(1,L+1)];der=evalpoly(co,eta)+(eta-single)*evalpoly([(L-j)*co[j]for j in range(L)],eta);norm=der/fixed**L
 ck(str(index)+' singleton',single/fixed==F(-23,22));ck(str(index)+' elementary values',es==expected_e,list(map(str,es)));ck(str(index)+' derivative',norm==expected_der,str(norm));ck(str(index)+' original derivative',der==(F(71745,32)if index==4 else F(165445,2)),str(der));rows.append(dict(index=index,single=str(single/fixed),elementary=list(map(str,es)),derivative=str(norm)))
a,b=F(6),F(4);T=F(2);z=F(23,22);K=T*T+(a+b)*(1+2*z)*T*T+2*(a-b)**2*z*T+2*(a+b)**2*z*z*T*T+4*(a-b)**2*z*z*(T*(a+b)-a*b);ck('two-pair n1 K',K==F(114804,121),str(K));ck('strict fromn2',10*4>24);ck('not strict n1',not(10*2>24))
p=V/'external/certificate_13.json';d=json.loads(p.read_text())['certificate']['regular'];full=prim(decode(d['common_resultant']));core=divexact(full,(h-21)**12);co=univ(core);sh=shifted(co,23);ck('core exact product',full==(h-21)**12*core);ck('core primitive',prim(core)==core);ck('degrees10290',degree(full,2)==102 and degree(core,2)==90);ck('core all shifted positive',all(v>0 for v in sh));ck('source full coefficient match',univ(full)==list(map(int,d['common_positivity']['coefficients_eta_ascending'])))
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,normalized=rows,core_coefficients=list(map(str,co)),core_shifted_coefficients=list(map(str,sh)),proof_sha256=sha(R/'NORMALIZED_VALUES_PROOF.md'),driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),source_sha256=sha(p),scope='Exact normalized illustrations and core convention only; outer identity gates separate.')
(V/'NORMALIZED_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
