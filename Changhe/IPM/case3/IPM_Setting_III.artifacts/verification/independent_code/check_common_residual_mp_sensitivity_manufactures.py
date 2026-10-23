"""Run only the two manufactured-test blocks from the queued summary driver."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import ast, hashlib, json
import mpmath as mp
source=Path('independent_code/summarize_common_residual_mp_sensitivity.py')
root=Path('research/hydrostatic_common_residual_audit')
tree=ast.parse(source.read_text()); checks=[]
chosen=[t for t in tree.body if isinstance(t,ast.FunctionDef)and t.name in ['ck','metric','verdict']]
body=next(t for t in tree.body if isinstance(t,ast.Try)).body
assert isinstance(body[0],ast.With)and isinstance(body[1],ast.For)
chosen+=body[:2]
ns={'mp':mp,'F':F,'checks':checks}
exec(compile(ast.Module(body=chosen,type_ignores=[]),str(source),'exec'),ns)
assert len(checks)==9 and all(c['passed']for c in checks)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'count':len(checks),'checks':checks,'source_sha256':{str(source):sha(source)},'driver_sha256':sha(__file__),'proof_sha256':sha(root/'MP_SENSITIVITY_MANUFACTURE_PROOF.md'),'scope':'Nine manufactured arithmetic/reporting tests only. Candidate MP summary unexecuted.'}
(root/'verification/MP_SENSITIVITY_MANUFACTURES.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(checks),out['utc'])
