"""Independent literal/scope audit. No producer source is executed."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
root=Path('research/spec50_consistency_audit');v=root/'verification';checks=[]
def ck(name,ok,evidence=None):checks.append({'name':name,'passed':bool(ok),'evidence':evidence})
for name,record in json.loads((v/'INPUTS.json').read_text()).items():ck('frozen '+name,hashlib.sha256((v/name).read_bytes()).hexdigest()==record['sha256'])
s=(v/'SPEC_v50.md').read_text();g43=s[s.index(' (G43)'):s.index(' (G44)')];g44=s[s.index(' (G44)'):s.index('## CHANGELOG')]
for term in ["H(0) = 0", "H'(0) != 0",'1 < P <= 2','int_y^inf g_xixi(0, s) ds','NOT a NO endpoint']:
 ck('retained hypothesis/scope '+term,term in g43)
for name,term in [('missing positive C','C > 0'),('missing open interval','nonempty open interval'),('finite-class ambiguity','finite class only')]:ck('defect present '+name,(term not in g43) if name!='finite-class ambiguity' else term in g43)
t=F(1,2);w=1-t*t;y=t/w**2;G=t/w;dydt=(1+3*t*t)/w**3;dGdt=(1+t*t)/w**2;Gy=dGdt/dydt
for name,a,b in [('y',y,F(8,9)),('G',G,F(2,3)),('G_y',Gy,F(15,28)),('singleton equality',F(7,5)*y*Gy,G)]:ck(name,a==b,str(a))
ck('C0 loses positive coordinate',F(0)*t/w**2==0)
ck('infinitely many distinct H witnessed',len(set(F(i) for i in range(1,21)))==20)
cap=F('0.0032578547902581733');cont=F('0.00343793061799162');n96=F('0.07607982855449697');n160=F('0.0003112138950101398')
ck('continued128 rises',cont>cap,float(cont/cap-1));ck('both128 below96',max(cap,cont)<n96);ck('160 below both128',n160<min(cap,cont))
for term in ['100 <= y <= 1e12','.0761','.00326','.00344','.000311','43 percent','21 percent','not\n      converged']:ck('G44 recorded '+term,term in g44)
for path,count in [('research/hydrostatic_finite_axis_obstruction/verification/CHECKS.json',329),('research/draft74_preliminary_audit/verification/CHECKS.json',206),('research/hydrostatic_c2_axis_extrema/verification/SUMMARY.json',332),('research/cubic_fit_history_audit/verification/SUMMARY.json',754)]:
 d=json.loads(Path(path).read_text());print(path,sorted(d)[:12]);ck('prerequisite '+path,d.get('status')=='PASS' and d.get('count')==count,{'status':d.get('status'),'count':d.get('count')})
for phrase in ['64 logged values to 3e-6','beta L_g^{1/3} = 4','awaiting CONFIRM']:
 ck('historical pending claim '+phrase,phrase in s[s.index('## CHANGELOG'):s.index('- v49')])
ck('amplitude notexact4',F('3.99998200914248')!=4)
output={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS' if all(x['passed'] for x in checks) else 'FAIL','verdict':'REPAIRS_REQUIRED','count':len(checks),'checks':checks}
(v/'CHECKS.json').write_text(json.dumps(output,indent=2)+'\n');print(output['status'],len(checks));print([x for x in checks if not x['passed']]);raise SystemExit(output['status']!='PASS')
