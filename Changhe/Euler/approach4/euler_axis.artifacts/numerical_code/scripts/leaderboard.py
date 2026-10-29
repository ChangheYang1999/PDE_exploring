"""Aggregate runs/*/result.json into PARAMETER_SWEEP.csv (every finished job) and CANDIDATE_LEADERBOARD.csv (ranked).

Ranking key (until the SPEC 6.1 holdout rho metric with pressure is attached by validate.py): the maximum over the
two reduced equations of the holdout relative RMS residual (rel_Rq_inner, rel_Reta_inner), then the scaled exterior
residuals.  Entries with swirl ratio below 0.02 or |q|max below 1e-3 are flagged 'swirl-free' and ranked last.
Usage: python3 scripts/leaderboard.py [--top 30]
"""
import csv, glob, json, os, sys, math, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIELDS = ["rank", "job_id", "branch", "stage", "cl", "alpha", "free_cl", "family", "seed", "init_extra", "gauge", "shift", "s1_constraint",
          "z0", "optimizer", "status", "n_iter", "elapsed_s", "nx", "D", "nmax", "shells", "ball_radial", "emax", "cost", "rel_Rq", "rel_Reta", "Rq_in_rms", "Reta_in_rms",
          "Rq_in_max", "Reta_in_max", "ext_scaled_q_rms", "ext_scaled_eta_rms", "swirl_ratio", "q_max", "eta_max", "tail_F2", "tail_Ftheta2",
          "tail_swirl_frac", "q0_origin", "Uz0", "vort_max", "vort_max_R", "axis_Rq_max", "axis_Reta_max", "ifc_dphi_max", "L_to_reporting",
          "rho_max_spec", "rho_M_max", "s_core_spec", "s_far_spec", "a_eff", "n_axis_zeros", "n_offaxis_zeros", "swirl_max_defect", "elliptic_rel_diff", "flag", "finished"]


def row_of(r):
    rep = r.get("report", {})
    cfg = r.get("cfg", {})
    ini = r.get("init") or {}
    t = rep.get("tail", {})
    ifc = rep.get("interfaces", [])
    rel = max(rep.get("rel_Rq_inner", float("nan")), rep.get("rel_Reta_inner", float("nan")))
    flag = ""
    sc = (r.get("validation") or {}).get("s_core")
    if (sc is not None and sc < 0.02) or (sc is None and rep.get("swirl_ratio_inner", 0) < 0.02) or rep.get("max_abs_q_inner", 0) < 1e-3:
        flag = "swirl-free"
    if not math.isfinite(rel):
        flag = (flag + ";nan").strip(";")
    vst = (r.get("validation") or {}).get("status")
    if vst and vst != "ok":
        flag = (flag + ";" + ("invalid" if vst.startswith("invalid") else "degenerate-shells")).strip(";")
    st = r.get("stage_status", [])
    return dict(job_id=r["job_id"], branch=r.get("branch"), stage=r.get("stage"), cl=r.get("cl"), alpha=r.get("alpha"), free_cl=cfg.get("free_cl"),
                family=ini.get("family") if ini else ("transfer" if r.get("from_state") else ""), seed=ini.get("seed"), init_extra=json.dumps(ini.get("extra", {})),
                gauge=cfg.get("gauge"), shift=cfg.get("scale_power_shift"), s1_constraint=cfg.get("s1_constraint"), z0=(r.get("s1") or {}).get("z0"),
                optimizer="+".join(s["name"] for s in r.get("optimizer", [])), status="/".join(s["status"] for s in st), n_iter=r.get("n_iter"),
                elapsed_s=round(r.get("elapsed_s", 0), 1), nx=r.get("nx"), D=cfg.get("D"), nmax=cfg.get("nmax"), shells=json.dumps(cfg.get("shells")),
                ball_radial=cfg.get("ball_radial", "cheb"), emax=cfg.get("emax"),
                cost=r.get("cost"), rel_Rq=rep.get("rel_Rq_inner"), rel_Reta=rep.get("rel_Reta_inner"),
                Rq_in_rms=rep.get("Rq_inner", {}).get("rms"), Reta_in_rms=rep.get("Reta_inner", {}).get("rms"),
                Rq_in_max=rep.get("Rq_inner", {}).get("max"), Reta_in_max=rep.get("Reta_inner", {}).get("max"),
                ext_scaled_q_rms=rep.get("Rq_ext_scaled", {}).get("rms"), ext_scaled_eta_rms=rep.get("Reta_ext_scaled", {}).get("rms"),
                swirl_ratio=rep.get("swirl_ratio_inner"), q_max=rep.get("max_abs_q_inner"), eta_max=rep.get("max_abs_eta_inner"),
                tail_F2=t.get("int_F2"), tail_Ftheta2=t.get("int_Ftheta2"), tail_swirl_frac=t.get("swirl_fraction"),
                q0_origin=rep.get("origin", {}).get("q0"), Uz0=rep.get("origin", {}).get("Uz0"), vort_max=rep.get("vorticity_max"), vort_max_R=rep.get("vorticity_max_R"),
                axis_Rq_max=rep.get("axis", {}).get("Rq", {}).get("max"), axis_Reta_max=rep.get("axis", {}).get("Reta", {}).get("max"),
                ifc_dphi_max=max([d["dphi"] / max(d["phi_scale"], 1e-300) for d in ifc], default=float("nan")), L_to_reporting=r.get("L_to_reporting_gauge"),
                rho_max_spec=(r.get("validation") or {}).get("rho_max"), rho_M_max=(r.get("validation") or {}).get("rho_M_max"),
                s_core_spec=(r.get("validation") or {}).get("s_core"), s_far_spec=(r.get("validation") or {}).get("s_far"), a_eff=(r.get("validation") or {}).get("a_eff"),
                n_axis_zeros=(r.get("validation") or {}).get("n_axis_zeros"), n_offaxis_zeros=(r.get("validation") or {}).get("n_offaxis_zeros"),
                swirl_max_defect=(r.get("validation") or {}).get("swirl_max_defect"), elliptic_rel_diff=(r.get("validation") or {}).get("elliptic_max_rel_diff_phi"),
                flag=flag, finished=r.get("finished"), _rel=rel)


def main():
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 40
    rows = []
    for f in glob.glob(os.path.join(ROOT, "runs", "*", "result.json")):
        if os.path.basename(os.path.dirname(f)).startswith("zz_"):
            continue
        try:
            rows.append(row_of(json.load(open(f))))
        except Exception as ex:
            print("skip", f, ex)
    all_have_rho = len(rows) > 0 and all(r.get("rho_max_spec") is not None and math.isfinite(r["rho_max_spec"]) for r in rows)
    def key(r):
        # consistent ranking: SPEC rho_max only once every finished job carries it; otherwise the holdout relative residual
        primary = r["rho_max_spec"] if all_have_rho else r["_rel"]
        return (1 if r["flag"] else 0, primary if (primary is not None and math.isfinite(primary)) else 1e300)
    rows.sort(key=key)
    for i, r in enumerate(rows):
        r["rank"] = i + 1
    with open(os.path.join(ROOT, "PARAMETER_SWEEP.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader()
        for r in sorted(rows, key=lambda r: r["job_id"]):
            w.writerow(r)
    with open(os.path.join(ROOT, "CANDIDATE_LEADERBOARD.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader()
        for r in rows[:top]:
            w.writerow(r)
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {len(rows)} finished jobs; top {min(top, len(rows))} written; ranked by {'SPEC rho_max' if all_have_rho else 'holdout relative residual (validation incomplete)'}")
    for r in rows[:15]:
        print(f"{r['rank']:3d} {r['job_id'][:60]:60s} cl={r['cl']:.3f} rel(q,eta)=({r['rel_Rq']:.2e},{r['rel_Reta']:.2e}) swirl={r['swirl_ratio']:.3f} "
              f"qmax={r['q_max']:.2e} ext_eta={r['ext_scaled_eta_rms']:.1e} rho={r['rho_max_spec']} z0={r['z0']} {r['status']} {r['flag']}")


if __name__ == "__main__":
    main()
