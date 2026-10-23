"""Rerun current verifier arithmetic manufactures without replacing historical gate."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import check_residual_fraction_arithmetic as a
started=datetime.now(timezone.utc).isoformat();a.main('manufactures');assert len(a.checks)==30 and all(x['passed'] for x in a.checks)
for p in [Path(__file__),a.R/'CLOSURE_CORRECTION_PROOF.md']:a.bind(p)
out={'status':'PASS','started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'count':30,'checks':a.checks,'bindings':a.bindings,'scope':'Current-driver hand-derived manufactures only; historical gate preserved'}
(a.V/'FRACTION_MANUFACTURES_FINAL.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['count'])
