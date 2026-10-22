"""Optional small source records requested by the accepted actual-model followup."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1];p=B/'research/forcing_series_operands/code/regenerate.py';t=ast.parse(p.read_text());wanted={'dth','trig1','inv_fact','cos_b','sin_b'};records=[];seen=set()
for n in ast.walk(t):
 if isinstance(n,ast.Assign):
  ids={z.id for a in n.targets for z in ast.walk(a) if isinstance(z,ast.Name)}
  if ids&wanted:records.append({'lineno':n.lineno,'column':n.col_offset,'body':ast.unparse(n)});seen|=ids&wanted
assert seen==wanted
geo=json.loads((B/'research/localized_forcing/evidence/geometry_arb.json').read_text());rows=json.loads((B/'research/forcing_series_operands/evidence/blocks.json').read_text());assert len(rows)==832 and all(r['w']==geo['w_up'] for r in rows)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_OPTIONAL_CONVENTION_RECORDS','generator_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'assignments':records,'all832width_equalities':True,'scope':'Optional records supplement the already accepted convention binding. No new analytic assertion.'};(D/'evidence/convention_supplement.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(records))
