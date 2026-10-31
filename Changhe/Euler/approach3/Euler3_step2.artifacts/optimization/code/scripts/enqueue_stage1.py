#!/usr/bin/env python
"""Enqueue the Stage I multi-start sweep: fixed-parameter LM starts over the (c_l, omega) grid with diverse seed
families at the lowest ladder level, plus a few free-parameter jobs. Idempotent per job_id."""
import sys, os, json, time, itertools, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue")

def enqueue(job, overwrite=False):
    for d in ["pending", "running", "done", "failed"]:
        p = os.path.join(Q, d, job["job_id"] + ".json")
        if os.path.exists(p) and not overwrite:
            return False
    job.setdefault("created", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    tmp = os.path.join(Q, "pending", job["job_id"] + ".json.tmp")
    json.dump(job, open(tmp, "w"), indent=1); os.replace(tmp, tmp[:-4])
    return True

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=6); ap.add_argument("--Nk", type=int, default=16)
    ap.add_argument("--n_starts", type=int, default=6); ap.add_argument("--max_iter", type=int, default=150)
    ap.add_argument("--formulation", default="vort"); ap.add_argument("--priority", type=int, default=10)
    ap.add_argument("--tag", default="s1a"); ap.add_argument("--m_parity", default="even")
    ap.add_argument("--cl", default="0.41,0.43,0.45,0.47,0.49"); ap.add_argument("--om", default="0.1,0.3,1,3,10,-0.3,-3")
    ap.add_argument("--families", default="random,tail,nonaxi,poloidal,toroidal,random")
    ap.add_argument("--time_limit_per_start", type=float, default=1500); ap.add_argument("--ftol", type=float, default=1e-5)
    ap.add_argument("--nlw", action="store_true"); ap.add_argument("--efrac", type=float, default=None); ap.add_argument("--optimizer", default="lm")
    ap.add_argument("--free", action="store_true"); ap.add_argument("--R0", type=float, default=1.0); ap.add_argument("--seed_base", type=int, default=1000)
    ap.add_argument("--Nr", type=int, default=None, help="radial nodes (default 2.5 Nk for mom/both, 1.5 Nk for vort)")
    ap.add_argument("--channels", default=None, help="e.g. 6,6,6 for NkB,NkD,NkE")
    ap.add_argument("--sigmaZ", type=float, default=None, help="total-stretching constraint target (exact profile: 1)")
    ap.add_argument("--gauge", default="F", help="F (SPEC 6.1) or Z (enstrophy gauge, SPEC 11 v1.5 iii)")
    ap.add_argument("--exclusive", action="store_true", help="job needs a whole GPU (both slots)")
    ap.add_argument("--far", default=None, help="far anchoring radii in units of R0, e.g. 4096,16384,65536")
    ap.add_argument("--nl_den", default="nl", help="nl, all5, all5far or split"); ap.add_argument("--tail_constraints", action="store_true")
    ap.add_argument("--chunk", type=int, default=None); ap.add_argument("--max_retries", type=int, default=2)
    a = ap.parse_args()
    n = 0
    for i, (cl, om) in enumerate(itertools.product([float(x) for x in a.cl.split(",")], [float(x) for x in a.om.split(",")])):
        job_id = f"{a.tag}_L{a.L}_cl{cl:.2f}_om{om:+.1f}"
        cfg = dict(L=a.L, Nk=a.Nk, m_parity=a.m_parity, R0=a.R0, formulation=a.formulation, c_l=cl, omega=om, free_params=a.free,
                   n_starts=a.n_starts, seed=a.seed_base + i, max_iter=a.max_iter, families=a.families.split(","),
                   time_limit_per_start=a.time_limit_per_start, chunk=(256 if a.free else 512), threads=1, ftol=a.ftol,
                   nl_weighting=a.nlw, efrac=a.efrac, optimizer=a.optimizer, sigmaZ=a.sigmaZ, gauge=a.gauge,
                   far_radii=([float(v) for v in a.far.split(",")] if a.far else None), nl_denominator=a.nl_den, tail_constraints=a.tail_constraints,
                   Nr=(a.Nr if a.Nr else (int(round(2.5 * a.Nk)) if a.formulation in ("mom", "both") else None)))
        if a.channels:
            nb, nd, ne = [int(v) for v in a.channels.split(",")]
            cfg["channels"] = dict(NkB=nb, NkD=nd, NkE=ne, core_damp=2)
        if a.chunk:
            cfg["chunk"] = a.chunk
        n += enqueue(dict(job_id=job_id, type="multistart", stage="I", priority=a.priority, max_retries=a.max_retries, config=cfg, exclusive=a.exclusive))
    print(f"enqueued {n} jobs")
