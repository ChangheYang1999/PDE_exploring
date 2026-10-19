"""Fixed-shape checks without an additional field export."""
import json
import sys
from pathlib import Path
from diagnose import diagnostic

name=sys.argv[1]
nr=int(sys.argv[2]);nt=int(sys.argv[3])
R=float(sys.argv[4]) if len(sys.argv)>4 else 10000.
tail=sys.argv[5] if len(sys.argv)>5 else "two-term"
result=diagnostic(name+"_shape.npz",nr,nt,R,tail=tail)
output=f"{name}_quadrature_{nr}_{nt}_{R:g}_{tail}.json"
Path(output).write_text(json.dumps(result,indent=2))
print(json.dumps({k:result[k] for k in
                  ("nr","nt","R_shape","tail","cl","c_V1","roots_xaxis",
                   "axis_velocity_samples","residuals")},indent=2))
