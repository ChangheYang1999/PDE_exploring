"""Append fixed-density quadrature and closure sensitivity."""
import json
from pathlib import Path
import numpy as np

name="c4_r2"
base=json.loads(Path(name+"_metrics.json").read_text())
rows=[]
sources=sorted(Path(".").glob(name+"_quadrature_*.json"))
with open("REPORT.md","a") as f:
    f.write("\n## Fixed-density quadrature and closure sensitivity\n\n")
    f.write("These runs reevaluate the final saved density and saved L; they do "
            "not refit its coefficients. Commands are `timeout 540 bash bounded.sh "
            "python3 quadrature_check.py c4_r2 NR NT R TAIL`, with arguments in "
            "the table. Each output is `c4_r2_quadrature_NR_NT_R_TAIL.json`. "
            "No additional field exports are retained. The 7169/8193/9217 radial "
            "grids on R=1000/10000/100000 have nearly equal logarithmic spacing. "
            "The 480-angle run separately checks angular quadrature. "
            "Residual maxima below use the supplied N4 normalization.\n\n")
    f.write("| NR | NT | R shape | tail | inverse c - fitted target | "
            "x* | h(P) | annulus N4 max | max change in five w samples |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")
    for p in sources:
        d=json.loads(p.read_text());q=d["roots_xaxis"][0]
        dw=np.array(d["axis_velocity_samples"]["w"])-np.array(base["w"]["values"])
        f.write(f"| {d['nr']} | {d['nt']} | {d['R_shape']:.0f} | {d['tail']} | "
                f"{d['c_V1']-base['target_c']:.9g} | {q['x']:.11g} | "
                f"{q['mu2']:.11g} | {d['residuals']['annulus']['pointwise']:.9g} | "
                f"{np.max(np.abs(dw)):.9g} |\n")
        rows.append(dict(file=p.name,w_change=dw.tolist()))
    f.write("\nVelocity differences relative to the retained 8192 × 384 export "
            "are recorded at x=0.15,0.5,1.5,4,8 in `quadrature_w_changes.json`. "
            "These are observed sensitivity estimates, not validated error bounds. "
            "They do not provide an independent nonlinear solver comparison.\n")
Path("quadrature_w_changes.json").write_text(json.dumps(rows,indent=2))
print("Quadrature sensitivity appended.")
