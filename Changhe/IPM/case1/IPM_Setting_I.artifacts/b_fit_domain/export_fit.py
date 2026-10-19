"""Single-pass modal-grid export with exact density-axis derivatives."""
import json
import sys
from pathlib import Path
from diagnose import diagnostic

name=sys.argv[1]
nr=int(sys.argv[2]) if len(sys.argv)>2 else 8192
nt=int(sys.argv[3]) if len(sys.argv)>3 else 384
shape=name+"_shape.npz"
fields=name+"_fields.npz"
result=diagnostic(shape,nr,nt,10000.,export=fields,tail="two-term")
Path(name+"_diagnostic.json").write_text(json.dumps(result,indent=2))
print(json.dumps({k:result[k] for k in ("cl","cl_stored","c_V1","c_rho3",
                                      "roots_xaxis","residuals","weighted_identity")},indent=2))
