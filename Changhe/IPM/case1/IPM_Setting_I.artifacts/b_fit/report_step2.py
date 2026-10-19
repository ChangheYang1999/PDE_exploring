"""Record the two separate, equally budgeted local-refinement probes."""
import json
from pathlib import Path

names=["c4_centre","c4_radialtest","c4_angulartest"]
d={n:json.loads(Path(n+"_scan.json").read_text()) for n in names}
lines=["\n## Step 2: separate refinement probes\n",
       "Both probes start from the same centre-corrected shape. The radial probe "
       "inserts the 15 midpoint knots in 0.25 < q < 0.325; the angular probe "
       "adds 20 zero-initialized angular functions. Each probe receives one "
       "250-iteration inexact Gauss–Newton step. These short probes are not "
       "claimed to be stagnated fits. Commands and complete optimizer records "
       "are in the preceding chunk entries.\n",
       "Transfer commands: `timeout 540 bash bounded.sh python3 refine.py "
       "c4_centre_shape.npz c4_radialtest_shape.npz radial` and the corresponding "
       "`c4_angulartest_shape.npz angular` command. Transfer errors are in "
       "`c4_radialtest_transfer.json` and `c4_angulartest_transfer.json`. "
       "Comparison commands: `timeout 540 bash bounded.sh python3 quick_scan.py "
       "NAME_shape.npz`; sources: `NAME_scan.json`, for the three names below. "
       "All scans use 2560 radial points and 640 angular intervals.\n",
       "| shape | objective after chunk | near-P flux max | near-P flux RMS | "
       "near-P N4 max | physical r at flux max | theta at max |\n",
       "| --- | --- | --- | --- | --- | --- | --- |\n"]
for n in names:
    run=json.loads(Path(n+"_shape.npz.run.json").read_text())
    b=d[n]["bands"]["2<=r<=10/all"]
    lines.append(f"| {n} | {run['final_norm']:.9g} | {b['max']:.9g} | "
                 f"{b['rms']:.9g} | {b['N4_max']:.9g} | {b['r_max']:.9g} | "
                 f"{b['theta_max']:.9g} |\n")
lines += ["\nSigned radial profiles on 6.5 < r < 10.5 are stored in each scan JSON. "
          "The following counts include small oscillations and are descriptive, "
          "not measures of regularity.\n",
          "| shape | theta | max absolute flux ratio | sign changes |\n",
          "| --- | --- | --- | --- |\n"]
for n in names:
    for p in d[n]["near_P_profiles"]:
        lines.append(f"| {n} | {p['theta']:.6g} | {p['max']:.9g} | "
                     f"{p['sign_changes']} |\n")
lines += ["\nThe input's quoted 3.3e-5 near-source scale matches the N4 denominator "
          "much more closely than the Cartesian-flux denominator requested here. "
          "The common-grid starting flux maximum is 1.2668065e-4. The centre "
          "correction does not cause that normalization difference.\n"]
with open("REPORT.md","a") as f:
    f.writelines(lines)
print("Step 2 probe tables appended.")
