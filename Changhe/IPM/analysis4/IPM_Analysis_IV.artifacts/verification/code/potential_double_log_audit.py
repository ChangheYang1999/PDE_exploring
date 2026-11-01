"""Check the zero-degree logarithmic potential by Cartesian differentiation."""
from datetime import datetime, timezone
from pathlib import Path
from hashlib import sha256
import json
from laurent_log_audit import Q,Poly,L,parse
C=L(Q(0),0,[Poly([]),Poly([Q(1,4)]),Poly([Q(1,4)])])
lap=C.X().X()-C.Y().Y()
F=lap.Y()
G=C.X().Y().scale(-1)
expected_f=parse(Q(-3),{'1':['1']})
expected_g=parse(Q(-2),{'2':['0','-1/2']})
assert (F-expected_f).zero()
assert (G-expected_g).zero()
assert (G.X().X().scale(-1)+G.Y().Y()-F.X()).zero()
source=Path('research/21_logarithmic_data_audit/sources/lead_exact_log_data.json')
kappa=Q(json.loads(source.read_text())['density']['9']['1'][0])
assert kappa
out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
         code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
         cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
         potential_constant_log_coefficients=['0','1/4','1/4'],density={'1':['1']},stream={'2':['0','-1/2']},
         density_identity=True,stream_identity=True,poisson_identity=True,
         exact_reference=str(source),exact_reference_sha256=sha256(source.read_bytes()).hexdigest(),
         delta_4_9_sin1_kappa9=str(kappa),required_t2_constant_coefficient=str(kappa/4))
Path('research/39_potential_double_log/verification/identities.json').write_text(json.dumps(out,indent=2)+'\n')
print('All three Cartesian identities passed; kappa9 is nonzero.')
