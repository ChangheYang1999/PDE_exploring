"""Independent manufactured condition check, no producer imports."""
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
import json,hashlib
R=Path('research/hydrostatic_cusp_row_audit');V=R/'verification';mp.mp.dps=130
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];rows=[]
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
for pf in [0.25,1/3,0.75]:
 p=mp.mpf(pf);a=(p-1)/2
 for t0 in [10,100,1000,10000,100000,1000000,10**8,10**10]:
  t=mp.mpf(t0);h=lambda z:z*(1+z*z)**a;H=[h(t),mp.diff(h,t),mp.diff(h,t,2)];parts=[p*(p-1)*H[0],-2*(p-1)*t*H[1],t*t*H[2]]
  q=2*a*t*(1+t*t)**(a-1)+4*a*(a-1)*t*(1+t*t)**(a-2);qe=mp.fsum(parts);check(str(pf)+' '+str(t0)+' exact Euler identity',abs(q-qe)<mp.mpf('1e-100')*abs(q))
  ff=[float(z)for z in H];tt=float(t0);qd=pf*(pf-1)*ff[0]-2*(pf-1)*tt*ff[1]+tt*tt*ff[2]
  aa=(pf-1)/2;stable=2*aa*tt*(1+tt*tt)**(aa-1)+4*aa*(aa-1)*tt*(1+tt*tt)**(aa-2)
  cond=mp.fsum(abs(z)for z in parts)/abs(q);ratio=cond/(4*p*t*t)
  check(str(pf)+' '+str(t0)+' direct curvature stable',abs(mp.mpf(stable)-q)/abs(q)<mp.mpf('2e-14'))
  if t0>=10000:check(str(pf)+' '+str(t0)+' condition asymptotic',abs(ratio-1)<mp.mpf('1e-7'))
  rows.append(dict(p_binary=str(pf),t=t0,exact=mp.nstr(q,45),euler_double=qd,stable_double=stable,relative_euler_error=float(abs(mp.mpf(qd)-q)/abs(q)),relative_stable_error=float(abs(mp.mpf(stable)-q)/abs(q)),condition=float(cond),condition_over_4pt2=float(ratio)))
check('Euler formula fails severely for manufacture',max(r['relative_euler_error']for r in rows)>1)
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,proof_sha256=sha(R/'STABILITY_PROOF.md'),driver_sha256=sha(__file__),scope='Manufactured sensitivity of Euler cancellation; not an executed test of producer code.')
(V/'EULER_STABILITY.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([(r['p_binary'],r['t'],r['relative_euler_error'])for r in rows if r['t']>=100000]);print([c for c in checks if not c['passed']])
if out['status']!='PASS':raise SystemExit(1)
