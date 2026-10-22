"""Export only reconstructing parameters, retaining exact binary64 data as hex."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import numpy as np
BASE = Path(__file__).resolve().parents[3]
SOURCE = Path('PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz')
raw=SOURCE.read_bytes()
assert hashlib.md5(raw).hexdigest()=='15f8095f7e79dbfa0c50d75e5fe8997a'
with np.load(SOURCE,allow_pickle=False) as z:
    data={
        'schema':'ipm-x3-exact-binary64-v1',
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'source':str(SOURCE), 'source_sha256':hashlib.sha256(raw).hexdigest(),
        'scalars_hex':{n:float(z[n]).hex() for n in ['L','k','c_l','c','origin_radius','R_shape']},
        'integers':{n:int(z[n]) for n in ['degree','angular','singular','spline_order','tail_terms']},
        'z_hex':[float(v).hex() for v in z['z']],
        'spline_knots_hex':[float(v).hex() for v in z['spline_knots']],
        'names':z['names'].tolist(),
        'interpretation':'Hex strings are exact dyadic inputs. Mathematical held exponent may be defined as 1/k; stored c_l is separately retained. No rounded field arrays or optimizer residuals are inputs.'}
    assert float.fromhex(data['z_hex'][0])==float(z['k'])
out=BASE/'data_exact/x3.json'
out.write_text(json.dumps(data,separators=(',',':'))+'\n')
manifest={'utc':data['created_utc'],'json_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_sha256':data['source_sha256'],'bytes':out.stat().st_size}
(BASE/'research/canonical_inverse/evidence/data_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest))
