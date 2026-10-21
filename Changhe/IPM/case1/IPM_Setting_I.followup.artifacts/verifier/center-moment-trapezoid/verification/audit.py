from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
from flint import arb,ctx
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root.parent/'exact-data/code'))
from nodal_input import load
ctx.prec=256
p=root/'verification/certificates.json';o=json.loads(p.read_text())
assert o['complete'] and o['precision_bits']==256 and len(o['rows'])==6
for d in o['dependencies']:
 assert hashlib.sha256(Path(d['file']).read_bytes()).hexdigest()==d['sha256'],d
rows=[]
for r in o['rows']:
 a,b,pars,sha=load(Path(r['exact_json']))
 assert sha==r['json_sha256'] and a['source_sha256']==r['source_sha256']
 assert hashlib.sha256(Path(r['source']).read_bytes()).hexdigest()==r['source_sha256']
 assert (b[0]==1).all()
 c,old,defect=[arb(r[k]) for k in ('c','first_method_c','self_consistency_ball')]
 assert c.is_finite() and old.is_finite() and defect.is_finite()
 assert c.overlaps(old) and not defect.contains(0)
 n,d=float(pars['c_l']).as_integer_ratio();cl=arb(n)/d
 assert (3*cl-1-c).overlaps(defect)
 n,d=float(pars['L']).as_integer_ratio();L=arb(n)/d
 bound=L*L/(1-1/cl)*2*arb(r['strip_bound'])/((arb(r['J'])/4).exp()-1)
 assert bound.overlaps(arb(r['quadrature_remainder']))
 rows.append({'source':r['source'],'source_sha256':r['source_sha256'],'all_hashes_match':True,'old_new_overlap':True,'defect_excludes_zero':True,'strip_bound_reproduced_from_saved_M':True})
audit={'date':datetime.now(timezone.utc).isoformat(),'certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'proof_sha256':o['dependencies'][1]['sha256'],'code_sha256':o['dependencies'][0]['sha256'],'rows':rows,'verdict':'CONFIRMED for six exact represented canonical center moments; no off-center certificate'}
(root/'verification/audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps(audit,indent=2))
