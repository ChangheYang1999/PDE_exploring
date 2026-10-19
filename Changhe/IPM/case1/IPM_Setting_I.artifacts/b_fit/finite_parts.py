"""Save unrounded requested w-only estimator variants."""
import sys,json,runpy
from pathlib import Path
import numpy as np

name=sys.argv[1]
sys.argv=["b3_wonly_export.py",name+"_fields.npz"]
ns=runpy.run_path(str(Path("b3_wonly_export.py").resolve()))
rows=[]
for delta in (.4,.5):
    for degree in range(8,15):
        value,fit,odd=ns["fp_ls"](ns["d_w"],delta,degree)
        rows.append(dict(delta=delta,degree=degree,value=value,fit=fit,odd=odd))
values=np.array([r["value"] for r in rows])
result=dict(method="supplied b3_wonly_export.py",rows=rows,
            minimum=float(values.min()),maximum=float(values.max()),
            median=float(np.median(values)),spread=float(np.ptp(values)))
Path(name+"_b3_wonly.json").write_text(json.dumps(result,indent=2))
print("REQUESTED VARIANTS",json.dumps(result,indent=2))
