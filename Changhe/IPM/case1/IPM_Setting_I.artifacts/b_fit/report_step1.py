import json
from pathlib import Path

before=json.loads(Path("c4_start_scan.json").read_text())
after=json.loads(Path("c4_centre_scan.json").read_text())
bm=json.loads(Path("c4_start_metrics.json").read_text())
am=json.loads(Path("c4_centre_metrics.json").read_text())
with Path("REPORT.md").open("a") as f:
    f.write("\n## Step 1 completed: centre rows and full diagnostics\n\n")
    f.write("Canonical velocity scans use one common 2560 × 640 grid and shape radius 1000. "
            "Commands: `timeout 540 bash bounded.sh python3 quick_scan.py c4_start_shape.npz` and "
            "`timeout 540 bash bounded.sh python3 quick_scan.py c4_centre_shape.npz`. "
            "Sources: `c4_start_scan.json`, `c4_centre_scan.json`. "
            "The field export additionally extends to shape radius 10000 at fixed saved L. "
            "Commands: `timeout 540 bash bounded.sh python3 export_fit.py c4_centre`, "
            "`timeout 540 bash bounded.sh python3 metrics.py c4_centre`; files: "
            "`c4_centre_fields.npz`, `c4_centre_diagnostic.json`, `c4_centre_metrics.json`. "
            "Baseline axis command: `timeout 540 bash bounded.sh python3 metrics.py c4_start "
            "final_candidate.npz`; "
            "source: `c4_start_metrics.json`.\n\n")
    f.write("| common-grid quantity | before | after |\n| --- | --- | --- |\n")
    for key in ("cl","xstar","hP"):
        f.write(f"| {key} | {before[key]:.12g} | {after[key]:.12g} |\n")
    for key in ("alpha","beta","delta","gamma","E","D2","E_relative","D2_relative"):
        f.write(f"| {key} | {before['centre'][key]:.12g} | {after['centre'][key]:.12g} |\n")
    f.write("\nThe origin radius remains 0.02: both explicit D14 rows can be met without "
            "changing the multiplier radius. No 0.05 or 0.1 radius comparison was triggered.\n\n")
    f.write("The following Cartesian-flux ratios use |R|/(|W1 rho_x|+|W2 rho_y|+|rho|), "
            "with analytic transverse limits on the axes. RMS is an unweighted log-polar sample RMS.\n\n")
    f.write("| physical band | before max | before RMS | after max | after RMS |\n"
            "| --- | --- | --- | --- | --- |\n")
    for key in before["bands"]:
        if key.endswith("/all"):
            b=before["bands"][key];a=after["bands"][key]
            f.write(f"| {key[:-4]} | {b['max']:.8g} | {b['rms']:.8g} | {a['max']:.8g} | {a['rms']:.8g} |\n")
    f.write("\n| axis T3 interval | before max relative | after max relative | after x at max | after max absolute |\n"
            "| --- | --- | --- | --- | --- |\n")
    b=next(v for k,v in bm["T3"].items() if k.startswith("[0.01,"))
    a=next(v for k,v in am["T3"].items() if k.startswith("[0.01,"))
    f.write(f"| [0.01, 0.5] | {b['max_relative']:.8g} | {a['max_relative']:.8g} | {a['x_max']:.8g} | {a['max_absolute']:.8g} |\n")
    f.write("\nT3 uses the exact trial G3 derivative and the modal velocity jets, interpolated from "
            "the field export; it is divided by the sum of the absolute values of its four displayed "
            "terms in SPEC D12. This remains a numerical, derivative-sensitive diagnostic.\n\n")
    f.write("The last two base chunks are checked separately against the <1% objective-change "
            "criterion. This is operational stagnation for the documented inexact solver, not "
            "a certificate of a nonlinear stationary point. The storage rewrite passed the "
            "original-versus-compact tensor and adjoint checks: command "
            "`timeout 540 bash bounded.sh python3 verify_centre.py --start`, evidence "
            "`centre/verification/tensor_derivative.json` and `start_tensor.json`.\n")
print("Step 1 tables appended.")
