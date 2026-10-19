"""Build final study tables from archived numerical records."""
import json
import re
import sys
from pathlib import Path
import numpy as np

names=["c4_centre","c4_r1","c4_r2"]
stage=sys.argv[1]
out=[]
def add(s=""):
    out.append(s+"\n")
def table(headers,rows):
    add("| "+" | ".join(headers)+" |")
    add("| "+" | ".join(["---"]*len(headers))+" |")
    for row in rows:
        add("| "+" | ".join(str(v) for v in row)+" |")
    add()
def fmt(x):
    return f"{x:.10g}"

if stage=="resolution":
    ms=[json.loads(Path(n+"_metrics.json").read_text()) for n in names]
    ss=[json.loads(Path(n+"_scan.json").read_text()) for n in names]
    add("\n## Step 3 completed: three nested trial spaces")
    add()
    add("For every numerical entry in this section, sources are "
        "`NAME_metrics.json`, `NAME_scan.json`, and the archived "
        "`NAME_chunkN.json` records, where NAME is one of the table column names. "
        "Commands: `timeout 540 bash bounded.sh python3 export_fit.py NAME`, "
        "`timeout 540 bash bounded.sh python3 metrics.py NAME`, and "
        "`timeout 540 bash bounded.sh python3 quick_scan.py NAME_shape.npz 10240 384`. "
        "The exports use 8192 radial points, 384 angular intervals, and shape "
        "outer radius 10000, with fixed saved L. Common scans use shape radius "
        "1000 on 10240 radial points and 384 angular intervals. Full optimizer "
        "commands are recorded with each chunk.")
    add()
    rows=[]
    for key,label in [("degree","radial functions per angular mode"),
                      ("angular","highest angular index"),
                      ("cl_stored","fitted c_l"),("cl","export c_l"),
                      ("xstar","x*"),("hP","h(P)"),("mu1","w'(P)"),
                      ("inverse_c","c from inverse"),("target_c","3 fitted c_l - 1"),
                      ("c_discrepancy","inverse c - target c")]:
        rows.append([label]+[fmt(m[key]) for m in ms])
    for key in ("alpha","beta","delta","gamma","E","D2","E_relative","D2_relative"):
        rows.append([key]+[fmt(s["centre_fixed_scale"][key]) for s in ss])
    table(["quantity"]+names,rows)
    add("The source condition is fitted on the fitting grid; its independently "
        "reevaluated defect is shown above. Inverse c is compared with the "
        "stored fitted c_l, not with the c_l recomputed from that same inverse. "
        "The D14 coefficients use the saved physical scale, through the "
        "centre_fixed_scale entries of the scan JSON files.")
    add()
    rows=[]
    for n in names:
        files=sorted((p for p in Path(".").glob(n+"_chunk*.json")
                      if re.fullmatch(re.escape(n)+r"_chunk\d+\.json",p.name)),
                     key=lambda p:int(re.search(r"chunk(\d+)",p.name)[1]))
        recent=[json.loads(p.read_text()) for p in files[-2:]]
        for p,d in zip(files[-2:],recent):
            change=1-(d["final_norm"]/d["initial_norm"])**2
            rows.append([n,p.name,fmt(d["initial_norm"]),fmt(d["final_norm"]),
                         f"{100*d['change']:.6g}%",f"{100*change:.6g}%"])
    table(["fit","chunk record","start norm","end norm","norm reduction",
           "squared-objective reduction"],rows)
    add("All final stopping decisions use two consecutive completed chunks "
        "with less than 1% reduction of the squared objective. This is an "
        "operational test for the documented inexact solver; no claim of a "
        "global minimum or of exact nonlinear stationarity follows.")
    add()
    rows=[]
    for m in ms:
        d=m["D9"];i=d["integral"][-1]
        rows.append([m["name"],fmt(i["integral"]),fmt(i["target"]),
                     fmt(i["relative_defect"]),
                     fmt(max(abs(q["relative"]) for q in d["nonlocal"])),
                     fmt(m["D10"]["q"]),fmt(m["D10"]["target"]),
                     fmt(m["D10"]["relative"])])
    table(["fit","D9 integral","D9 target","D9 relative defect",
           "D9 max sampled nonlocal defect","D10 q","D10 target","D10 relative defect"],rows)
    add("D9 uses 16, 32, and 64 point Gauss quadrature on each spline interval. "
        "All three values, plus differential axis checks, are in each metrics "
        "JSON. The nonlocal maximum above covers the seven listed evaluation "
        "points, not the continuum. D10 uses the supplied weighted identity "
        "with its modal tail correction.")
    add()
    rows=[]
    for m in ms:
        d=m["D9"];t=list(m["T3"].values())[-1]
        rows.append([m["name"],fmt(d["divergence_max"]),
                     fmt(d["a2prime_plus_3b3_max_relative"]),
                     fmt(d["a2prime_plus_3b3_max_absolute"]),
                     fmt(d["hprime_minus_2a2_plus_gprime_max_relative"]),
                     fmt(d["hprime_minus_2a2_plus_gprime_max_absolute"]),
                     fmt(t["max_T1_relative_away_from_source"]),
                     fmt(t["max_T1_absolute"])])
    table(["fit","max |w'+h-2cl|","a2'+3b3 max relative","max absolute",
           "h'-2a2+g' max relative","max absolute","T1 max relative to 0.99x*",
           "T1 max absolute to x*"],rows)
    add("Differential D9 values use differentiated cubic interpolants of "
        "the exported velocity jets. Their interpolation error is included "
        "in these numbers; they are not independent bounds for the analytic "
        "modal identities. T1 is shown both in absolute units through x* "
        "and with a relative normalization restricted to x <= 0.99x*.")
    add()
    for normalization in ("flux","N4"):
        add(f"### {normalization} residual by physical band and angle strip")
        add()
        add("Every cell is **maximum / RMS** over the indicated log-polar "
            "samples, including analytic transverse limits at the axes. "
            "Flux means |R|/(|W1 rho_x|+|W2 rho_y|+|rho|); N4 means "
            "|R|/(|rho|+|X·grad rho|+|U·grad rho|). The outer physical radius "
            "is 10000 L (approximately 76520). These are sampled values, "
            "not rigorous pointwise bounds. The smallest sampled physical "
            "radius is 1e-4 L (approximately 0.0007652); the inner disk is "
            "not covered by these sampled maxima. The strips are theta < 0.05, "
            "0.05 <= theta <= pi/2-0.05, and theta > pi/2-0.05.")
        add()
        rows=[]
        for key in ms[0]["bands"]:
            a,b=("max","rms") if normalization=="flux" else ("N4_max","N4_rms")
            rows.append([key]+[f"{m['bands'][key][a]:.7g} / "
                                f"{m['bands'][key][b]:.7g}" for m in ms])
        table(["band / theta strip"]+names,rows)
    rows=[]
    for m in ms:
        for interval,t in m["T3"].items():
            rows.append([m["name"],interval,fmt(t["max_relative"]),
                         fmt(t["rms_relative"]),fmt(t["max_absolute"]),fmt(t["x_max"])])
    add("### Cubic axis transport")
    add()
    add("T3 = w G3' + (3h-1)G3 + A2 G1' + B3W G1. Its relative defect is "
        "the absolute sum divided by the sum of absolute values of these "
        "four terms. G3 and G3' are evaluated analytically from the trial; "
        "velocity jets come from the modal export and spline interpolation.")
    add()
    table(["fit","physical interval","max relative","RMS relative",
           "max absolute","x at max relative"],rows)
    add("The large relative T1 value at x* in the JSON is a degenerate "
        "normalization: its two terms vanish for exact source data. It "
        "must not be read as an order-one absolute defect.")
    add()
    rows=[]
    for j,x in enumerate(ms[0]["w"]["x"]):
        vs=[m["w"]["values"][j] for m in ms]
        rows.append([str(x)]+[f"{v:.12f}" for v in vs]+
                    [f"{vs[1]-vs[0]:+.12e}",f"{vs[2]-vs[1]:+.12e}"])
    add("### Axis velocity")
    add()
    add("Values are printed to 12 decimal places as requested. This formatting "
        "does not assert 12-place accuracy. All use the same interpolation "
        "w(x)=x S(x²) of the modal field exports.")
    add()
    table(["x"]+names+["r1 - centre","r2 - r1"],rows)
elif stage=="finite":
    add("\n## Step 4 completed: finite-part diagnostics")
    add()
    add("Commands for each NAME: `timeout 540 bash bounded.sh bash assess.sh "
        "NAME_fields.npz NAME`, `timeout 540 bash bounded.sh python3 "
        "finite_parts.py NAME`, and `timeout 540 bash bounded.sh python3 "
        "b3_ibp.py NAME_fields.npz mu1only`. Sources: `NAME_assess.log`, "
        "`NAME_b3_wonly.json`, `NAME_b3_wonly.log`, `NAME_b3_ibp.log`, and "
        "`NAME_metrics.json`. No field data are used from discarded probes.")
    add()
    rows=[];d13rows=[];raw={}
    for n in names:
        a=json.loads(Path(n+"_b3_wonly.json").read_text())
        text=Path(n+"_b3_ibp.log").read_text()
        vals=[float(v) for v in re.findall(r"\sibp\s+([-+0-9.eE]+)\s+near-0",text)]
        if len(vals)!=16:
            raise ValueError((n,"expected 16 IBP variants",len(vals)))
        m=json.loads(Path(n+"_metrics.json").read_text())
        rows.append([n,f"[{a['minimum']:.8g}, {a['maximum']:.8g}]",
                     fmt(a["spread"]),f"[{min(vals):.5f}, {max(vals):.5f}]",
                     f"{max(vals)-min(vals):.5f}",fmt(m["B3_ansatz_natural"])])
        log=Path(n+"_assess.log").read_text()
        lines=[l for l in log.splitlines() if l.startswith("s1, s2")]
        d13rows.extend([[n,l] for l in lines])
        raw[n]=dict(wonly=a,ibp_printed_values=vals,
                    ibp_min=min(vals),ibp_max=max(vals),
                    ansatz_natural=m["B3_ansatz_natural"],D13_printed_lines=lines)
    Path("finite_parts_summary.json").write_text(json.dumps(raw,indent=2))
    table(["fit","w-only LS range","LS spread","IBP range","IBP spread",
           "trial singular coefficient"],rows)
    add("All B3 entries are divided by the natural unit x*^(2-p3), "
        "p3=6+2/A. The first estimator covers delta=0.4,0.5 and every integer "
        "degree 8 through 14. The IBP range covers xc/x*=0.3,0.4, "
        "xlo/x*=0.03,0.05, degrees 7,9 and Jacobi orders 40,80. The supplied "
        "IBP script prints five decimals; its table is not more accurate "
        "than that. These spreads are sensitivity diagnostics, not error bars.")
    add()
    add("The mu1only option replaces A in the reconstructed axis equation by "
        "A_g(x)=A+(w'(x*)-A)(x/x*)² to regularize the endpoint. Its size is "
        "printed in each log. Thus agreement is conditional on this small "
        "regularization as well as spline differentiation, cutoff treatment, "
        "and finite-part extrapolation. The actual trial fails T3 at a much "
        "larger level than its ordinary 2D residual. No compatibility or "
        "regularity conclusion is drawn from the B3 estimates.")
    add()
    add("### D13 independent partition checks")
    add()
    add("These are the unchanged supplied D13 script's printed results. "
        "It evaluates four circular-PV partitions using interpolation of H, "
        "numerical quadrature, and a leading tail closure. The supplied SPEC "
        "labels D13 as a referee claim with rederivation pending; this report "
        "uses it as a requested numerical diagnostic and does not establish it.")
    add()
    table(["fit","D13 output line"],d13rows)
else:
    raise ValueError(stage)

with open("REPORT.md","a") as f:
    f.writelines(out)
print("Appended",stage)
