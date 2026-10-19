"""Single-pass modal-grid export with exact density-axis derivatives.
Fit-convention version (lead, 2026-10-18; VERIFY_REPORT G64 (b)): inverse domain and two-term closure at the shape's
stored R_shape (as in the fit), not at 1e4 shape units."""
import json
import sys
from pathlib import Path
from diagnose import diagnostic

name=sys.argv[1]
nr=int(sys.argv[2]) if len(sys.argv)>2 else 8192
nt=int(sys.argv[3]) if len(sys.argv)>3 else 384
shape=name+"_shape.npz"
fields=name+"_fields.npz"
import numpy as np
with np.load(shape) as _z:
    Rsh=float(_z["R_shape"]) if "R_shape" in _z else 1000.
result=diagnostic(shape,nr,nt,Rsh,export=fields,tail="two-term")
result["R_inverse_shape_units"]=Rsh
Path(name+"_diagnostic.json").write_text(json.dumps(result,indent=2))
print(json.dumps({k:result[k] for k in ("cl","cl_stored","c_V1","c_rho3",
                                      "roots_xaxis","residuals","weighted_identity")},indent=2))
