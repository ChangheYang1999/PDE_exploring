from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time,re
B=Path(__file__).resolve().parents[1];t=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for n,h in m['inputs'].items():assert sha(B/n)==h,n
text=(B/'source/theory_v07.md').read_text();assert sha(B/'source/theory_v07.md')=='42eb222a38caadac911cffc261287892a9f18f60888f211f3e028f560508b320'
assert len(text.splitlines())==710
rows=m['appendix_entries'];assert len(rows)==65
for row in rows:
 if row['binding']!='unresolved historical mutable version':assert sha(B/row['frozen_path'])==row['publication_sha256']
ratios=[]
for candidate,d,lower in [('007','0.004769166867',['1257','1673','10.43']),('021','0.001864696854799172',['491.6','654.3','4.078']),('022','0.00135251075726327',['356.5','474.6','2.958'])]:
 for c,l in zip(['0.000003793','0.0000028496','25/54684'],lower):
  exact=Q(d)/Q(c);assert exact>Q(l);ratios.append({'candidate':candidate,'exact':str(exact),'printed_lower':l})
assert 'if K = 0 the majorant' in text
assert 'sharp enough to evade NC-T-UNIV-E' in text
assert 'except at\n  011' in text
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'proof_sha256':sha(B/'PROOF.md'),'manifest_sha256':sha(B/'data/manifest.json'),'code_sha256':sha(Path(__file__)),'publication_sha256':sha(B/'source/theory_v07.md'),'appendix_count':len(rows),'unresolved_historical':[x['path'] for x in rows if x['binding']=='unresolved historical mutable version'],'ratios':ratios,'verdict':'CONFIRMED mathematical content with three explicit status/scope repairs','foreign_code_executed':False,'new_integrals':False}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
