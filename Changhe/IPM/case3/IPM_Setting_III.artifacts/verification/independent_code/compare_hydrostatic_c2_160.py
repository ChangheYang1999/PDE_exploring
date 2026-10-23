from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
V=Path('research/hydrostatic_c2_resolved_160_audit/verification');checks=[];rows=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
sources=[('hydrostatic_c2_resolved_audit','hsG_c2.0_N96_log'),('hydrostatic_c2_resolved_audit','hsG_c2.0_N128_log'),('hydrostatic_c2_continuation_audit','hsG_c2.0_N128_log_cont'),('hydrostatic_c2_resolved_160_audit','hsG_c2.0_N160_log')]
coord=None
for dirname,tag in sources:
 base=Path('research')/dirname/'verification';summary=json.loads((base/'SUMMARY.json').read_text());state=next(s for s in summary['states']if s['tag']==tag);raw=json.loads((base/(tag+'.json')).read_text())
 ck(tag+' summary gate',summary['status']=='PASS'and all(c['passed']for c in summary['checks']))
 p=raw['levels'][-1]['points'];here=[(a['x'],a['y'])for a in p]
 if coord is None:coord=here
 ck(tag+' identical774points',here==coord and len(here)==774)
 chosen=[a for a in p if a['x']**2+a['y']**2<10000.000001**2]
 maxima={k:max((a for a in chosen if a[k] is not None),key=lambda a:abs(a[k])) for k in ['R','R_Nf','R_Nv']}
 for k in maxima:ck(tag+' recomputed maximum '+k,maxima[k]==state['levels'][-1]['regions']['extent10000'][k])
 ck(tag+' nonzero center defect',state['delta']!=0 and state['a']!=0)
 f=state['far']['values'];ck(tag+' exact intended exponent',float(f['cp_minus1'])==0)
 ck(tag+' nonzero raw axis limit',abs(float(f['r2']))>0.4)
 rows.append(dict(tag=tag,source_sha256=state['source_sha256'],summary_sha256=sha(base/'SUMMARY.json'),raw_sha256=sha(base/(tag+'.json')),delta=state['delta'],b=state['b'],E=state['E'],Q=f['Q'],B_log=f['B_log'],Cp_K=state['cusp']['Cp_K'],r2=f['r2'],maxima={k:abs(maxima[k][k])for k in maxima}))
ratios={rows[i]['tag']:{k:rows[-1]['maxima'][k]/rows[i]['maxima'][k]for k in ['R','R_Nf','R_Nv']}for i in range(3)}
z=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,N160_to_prior_ratios=ratios,proof_sha256=sha(V.parent/'COMPARISON_PROOF.md'),driver_sha256=sha(__file__))
(V/'COMPARISON.json').write_text(json.dumps(z,indent=2)+'\n');print(z['status'],z['count']);print(json.dumps(ratios));print([c for c in checks if not c['passed']])
if z['status']!='PASS':raise SystemExit(1)
