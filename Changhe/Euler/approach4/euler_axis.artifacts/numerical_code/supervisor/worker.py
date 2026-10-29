"""One campaign job: build the problem, initialize, optimize with checkpoints, write diagnostics.

Usage: python3 supervisor/worker.py <job.json> [--run-dir runs/<job_id>]
Exit codes: 0 finished; 3 interrupted (SIGTERM/SIGINT or shift time limit; checkpoint written, resumable); 1 error.

Job JSON keys:
  job_id, cfg (axi.problem.Config fields), init {family, seed, scale_core, amp_core, swirl_amp, tail_ratio, extra{}},
  from_state (optional path to a .pt with x and cfg of a parent run: transferred onto the new basis by least squares),
  optimizer: list of stages [{"name": "lm"|"lbfgs", "max_iter": int, "time_limit": s, ...}],
  ckpt_seconds (default 300), gauge_from_seed (bool: set cfg.gauge_target to the seed's gauge integral),
  export_candidate (bool), tags, branch, stage, priority, max_retries.
Checkpoints are atomic (write tmp, fsync, os.replace).  The heartbeat file is touched every optimizer iteration.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import signal
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))

import numpy as np
import torch

from axi.problem import Problem, Config
from axi.init import make_init
from axi import lm, diagnostics

torch.set_default_dtype(torch.float64)
STOP = {"flag": False, "reason": ""}


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def atomic_save(obj, path):
    tmp = path + ".tmp"
    torch.save(obj, tmp)
    with open(tmp, "rb") as f:
        os.fsync(f.fileno())
    os.replace(tmp, path)


def atomic_json(obj, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1, default=float)
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def _sig(signum, frame):
    STOP["flag"] = True
    STOP["reason"] = f"signal {signum}"


def transfer_state(parent, prob):
    """Least-squares transfer of a parent state (dict with x, cfg) onto prob's basis (all elements)."""
    pprob, xp = Problem.from_state(parent, device="cpu")      # parent's FINAL c_l and exponents
    x = torch.zeros(prob.nx, dtype=torch.float64)
    for i, e in enumerate(prob.elements):
        ph, qq = pprob.eval_all(xp, e.R, e.mu)
        for (cols, off, y) in ((prob.cols_phi[i], prob.off_phi, ph[(0, 0)].numpy()), (prob.cols_q[i], prob.off_q, qq[(0, 0)].numpy())):
            A0 = e.B[(0, 0)][:, cols]
            if e.kind == "exterior":
                wts = 1.0 / (np.abs(y).max(initial=0) * 1e-3 + np.abs(y) + 1e-300)
                cs = np.max(np.abs(A0 * wts[:, None]), axis=0); cs[cs == 0] = 1.0
                c, *_ = np.linalg.lstsq((A0 * wts[:, None]) / cs, y * wts, rcond=None); c = c / cs
            else:
                c, *_ = np.linalg.lstsq(A0, y, rcond=None)
            x[off[i]:off[i + 1]] = torch.tensor(c)
    if prob.ix_cl is not None:
        x[prob.ix_cl] = prob.cl
    if prob.ix_z0 is not None:
        z0p = pprob.z0_of(xp)
        x[prob.ix_z0] = z0p if z0p is not None else prob.cfg.z0_init
    return x.to(prob.device)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("job")
    ap.add_argument("--run-dir", default=None)
    ap.add_argument("--device", default=None)
    args = ap.parse_args()
    job = json.load(open(args.job))
    jid = job["job_id"]
    run_dir = args.run_dir or os.path.join(ROOT, "runs", jid)
    os.makedirs(run_dir, exist_ok=True)
    logf = open(os.path.join(run_dir, "log.txt"), "a")

    def log(msg):
        line = f"{now()} {msg}"
        logf.write(line + "\n"); logf.flush()
        print(line, flush=True)

    signal.signal(signal.SIGTERM, _sig)
    signal.signal(signal.SIGINT, _sig)
    dev = args.device or ("cuda" if (os.environ.get("CUDA_VISIBLE_DEVICES", "") != "" and torch.cuda.is_available()) else "cpu")
    if dev == "cpu":
        torch.set_num_threads(max(1, int(os.environ.get("OMP_NUM_THREADS", "1"))))
    log(f"job {jid} start pid {os.getpid()} device {dev} CUDA_VISIBLE_DEVICES={os.environ.get('CUDA_VISIBLE_DEVICES')}")
    hb_path = os.path.join(run_dir, "heartbeat.json")
    ckpt_path = os.path.join(run_dir, "checkpoint.pt")
    final_path = os.path.join(run_dir, "final.pt")
    result_path = os.path.join(run_dir, "result.json")
    ckpt_seconds = float(job.get("ckpt_seconds", 300))
    t_job0 = time.time()
    try:
        cfg = Config.from_json(job["cfg"])
        prob = Problem(cfg, device=dev)
        torch.manual_seed(int(job.get("init", {}).get("seed", 0)))
        atomic_json(dict(job=job, problem=prob.describe(), start=now(), pid=os.getpid()), os.path.join(run_dir, "job_resolved.json"))
        stages = job["optimizer"]
        state = None
        if os.path.exists(ckpt_path):
            state = torch.load(ckpt_path, weights_only=False, map_location="cpu")
            x = state["x"].to(dev)
            stage_idx = state["stage_idx"]
            opt_state = state.get("opt_state", {})
            history = state.get("history", [])
            elapsed_prev = state.get("elapsed", 0.0)
            if "gauge_target" in state:
                prob.cfg.gauge_target = state["gauge_target"]
            if "row_scale" in state:
                prob.cfg.w_q, prob.cfg.w_eta = state["row_scale"]
            log(f"resumed from checkpoint: stage {stage_idx} it {opt_state.get('it', 0)} cost {state.get('cost')} elapsed {elapsed_prev:.0f}s")
        else:
            ini = job.get("init", {})
            if job.get("from_state"):
                parent = torch.load(job["from_state"], weights_only=False, map_location="cpu")
                x = transfer_state(parent, prob)
                if "gauge_target" in parent:
                    prob.cfg.gauge_target = float(parent["gauge_target"])
                if "row_scale" in parent and not job.get("auto_row_scale", True):
                    prob.cfg.w_q, prob.cfg.w_eta = parent["row_scale"]
                log(f"initialized by transfer from {job['from_state']}")
            else:
                x = make_init(prob, ini.get("family", "gauss_core"), int(ini.get("seed", 0)),
                              scale_core=float(ini.get("scale_core", 1.0)), amp_core=float(ini.get("amp_core", 1.0)),
                              swirl_amp=float(ini.get("swirl_amp", 1.0)), tail_ratio=float(ini.get("tail_ratio", 1.0)),
                              extra=ini.get("extra", {}))
                log(f"initialized family {ini.get('family')} seed {ini.get('seed')} extra {ini.get('extra', {})}")
            if job.get("gauge_from_seed"):
                cphi, cq, _ = prob.split(x)
                prob.cfg.gauge_target = float(prob.gauge_integral(cphi[-1], cq[-1], prob.alpha))
                log(f"working gauge target set from seed: {prob.cfg.gauge_target:.6e}")
            if job.get("auto_row_scale", True):
                # row scaling: divide the PDE rows of each equation by the norm of its weighted linear term at the seed,
                # so that both equations start at O(1) relative size against the interface, gauge and S1 rows
                from axi import ops
                cphi, cq, _ = prob.split(x)
                rq, re = [], []
                for i in range(prob.nel):
                    phi, q = prob.fields_at(i, cphi[i], cq[i]); sq, se = prob.scales(prob.G[i], prob.alpha, i)
                    eta = ops.eta_and_grad(phi, prob.G[i])[(0, 0)]
                    rq.append(prob.wnode[i] * sq * q[(0, 0)]); re.append(prob.wnode[i] * se * (1 + prob.cl) * eta)
                Aq = float(torch.sqrt(torch.sum(torch.cat(rq) ** 2))); Ae = float(torch.sqrt(torch.sum(torch.cat(re) ** 2)))
                if Aq > 0 and Ae > 0:
                    prob.cfg.w_q = cfg.w_q / Aq; prob.cfg.w_eta = cfg.w_eta / Ae
                log(f"auto row scale: w_q {prob.cfg.w_q:.4e} w_eta {prob.cfg.w_eta:.4e} (seed linear-term norms {Aq:.3e}, {Ae:.3e})")
            b0 = prob.cost_breakdown(x)
            log("initial cost breakdown " + json.dumps({k: f"{v:.3e}" for k, v in b0.items()}))
            stage_idx = 0
            opt_state = {}
            history = []
            elapsed_prev = 0.0
            r0 = prob.residual(x)
            log(f"initial cost {0.5 * float(r0 @ r0):.6e} nx {prob.nx} rows {prob.n_rows} z0 {prob.z0_of(x)}")
        last_ckpt = time.time()
        shift_limit = float(job.get("wall_limit", 5.5 * 3600))

        def save_ckpt(xc, st_idx, ost, hist, cost, tag="checkpoint"):
            atomic_save(dict(x=xc.detach().cpu(), cfg=cfg.to_json(), stage_idx=st_idx, opt_state=ost, history=hist, cost=cost,
                             gauge_target=prob.cfg.gauge_target, row_scale=(prob.cfg.w_q, prob.cfg.w_eta), time=now(),
                             elapsed=elapsed_prev + time.time() - t_job0, job_id=jid),
                        ckpt_path if tag == "checkpoint" else final_path)

        status_all = []
        for si in range(stage_idx, len(stages)):
            st = stages[si]
            name = st["name"]
            cur_state = opt_state if si == stage_idx else {}
            hist_stage = []

            def cb(xc, rec, hist, _si=si, _name=name):
                nonlocal last_ckpt
                atomic_json(dict(time=now(), it=rec.get("it"), cost=rec.get("cost"), stage=_si, name=_name, pid=os.getpid()), hb_path)
                if time.time() - last_ckpt > ckpt_seconds:
                    save_ckpt(xc, _si, dict(it=rec.get("it"), lam=rec.get("lam"), history=hist), history + hist, rec.get("cost"))
                    last_ckpt = time.time()
                    log(f"checkpoint stage {_si} it {rec.get('it')} cost {rec.get('cost'):.6e}")
                if STOP["flag"] or (time.time() - t_job0 > shift_limit):
                    if not STOP["flag"]:
                        STOP["reason"] = "wall_limit"
                    save_ckpt(xc, _si, dict(it=rec.get("it"), lam=rec.get("lam"), history=hist), history + hist, rec.get("cost"))
                    log(f"interrupted ({STOP['reason']}): checkpoint written at stage {_si} it {rec.get('it')}")
                    raise lm.Stop()

            log(f"stage {si} {name} {json.dumps({k: v for k, v in st.items() if k != 'name'})} resume_state {bool(cur_state)}")
            if name == "lm":
                res = lm.lm_solve(prob, x, max_iter=int(st.get("max_iter", 300)), lam0=float(cur_state.get("lam", st.get("lam0", 1e-2))),
                                  ftol=float(st.get("ftol", 1e-12)), xtol=float(st.get("xtol", 1e-14)), time_limit=st.get("time_limit"),
                                  callback=cb, state=cur_state, log=(lambda m: log(m)) if st.get("verbose", True) else None,
                                  cl_bounds=cfg.cl_bounds)
            elif name == "homotopy":
                # continuation in the forcing from the seed (exact solution of the forced system) to the unforced equations
                if "x_seed" in cur_state:
                    x_seed = cur_state["x_seed"].to(dev)
                else:
                    x_seed = x.detach().clone()
                prob.r_offset = None
                r_seed = prob.residual(x_seed).detach().clone()
                hstate = dict(t=cur_state.get("t", 0.0), dt=cur_state.get("dt", float(st.get("dt0", 0.1))), path=cur_state.get("path", []))

                def cb_h(xc, rec, path, _si=si):
                    nonlocal last_ckpt
                    atomic_json(dict(time=now(), it=rec.get("it"), cost=rec.get("cost"), stage=_si, name="homotopy", t=rec.get("t"), pid=os.getpid()), hb_path)
                    ost = dict(t=rec["t"], dt=rec["dt"], path=path, x_seed=x_seed.cpu())
                    if time.time() - last_ckpt > ckpt_seconds:
                        save_ckpt(xc, _si, ost, history, rec.get("cost")); last_ckpt = time.time()
                        log(f"checkpoint homotopy t={rec['t']:.5f} cost {rec['cost']:.3e}")
                    if STOP["flag"] or (time.time() - t_job0 > shift_limit):
                        if not STOP["flag"]:
                            STOP["reason"] = "wall_limit"
                        save_ckpt(xc, _si, ost, history, rec.get("cost"))
                        log(f"interrupted ({STOP['reason']}): checkpoint written at homotopy t={rec['t']:.5f}")
                        raise lm.Stop()

                res = lm.homotopy_solve(prob, x, r_seed, dt0=float(st.get("dt0", 0.1)), dt_min=float(st.get("dt_min", 1e-3)),
                                        max_iter_step=int(st.get("max_iter_step", 300)), tol_rel=float(st.get("tol_rel", 1e-10)),
                                        time_limit=st.get("time_limit"), callback=cb_h, state=hstate, log=(lambda m: log(m)), cl_bounds=cfg.cl_bounds)
                res["history"] = [dict(h, t=None) for h in res["history"]]
                status_all.append(dict(stage=si, name=name, status=res["status"], t_reached=res["t"], n_steps=len(res["path"]), path=res["path"]))
                log(f"homotopy finished: status {res['status']} t={res['t']:.5f} cost {res['cost']:.3e} steps {len(res['path'])}")
                atomic_json(dict(path=res["path"], status=res["status"], t=res["t"]), os.path.join(run_dir, "homotopy_path.json"))
                x = res["x"]; history = history + res["history"]
                if res["status"] == "stopped":
                    sys.exit(3)
                opt_state = {}
                save_ckpt(x, si + 1, {}, history, res["cost"]); last_ckpt = time.time()
                continue
            elif name == "varpro":
                # variable projection: q slaved to phi by the hard-pinned linear solve, outer LM on phi and the scalars (lead note 25 item 5 (b))
                vp = lm.VarProProblem(prob, full=bool(st.get("full", True)), trunc_rel=float(st.get("trunc_rel", 1e-4)))
                vp.x_full = x.detach().clone()
                y0 = x[vp.outer].detach().clone()
                log(f"varpro: {len(vp.inner)} inner rows, {len(vp.outer)} outer unknowns, full reduced Jacobian {vp.full}, trunc_rel {vp.trunc_rel:g}, solver {st.get('solver', 'qr')}")
                res = lm.lm_solve(vp, y0, max_iter=int(st.get("max_iter", 300)), lam0=float(cur_state.get("lam", st.get("lam0", 1e-2))),
                                  ftol=float(st.get("ftol", 1e-12)), xtol=float(st.get("xtol", 1e-14)), time_limit=st.get("time_limit"),
                                  callback=(lambda yc, rec, hist: cb(vp.embed(yc), rec, hist)), state=cur_state,
                                  log=(lambda m: log(m + f" | q-floor {vp.last_q_floor:.2e} dropped {vp.last_n_dropped}")) if st.get("verbose", True) else None, cl_bounds=cfg.cl_bounds,
                                  solver=st.get("solver", "chol"))
                res["x"] = vp.embed(res["x"], vp.solve_q(res["x"]))
            elif name == "lbfgs":
                res = lm.lbfgs_solve(prob, x, max_iter=int(st.get("max_iter", 300)), history_size=int(st.get("history_size", 50)),
                                     time_limit=st.get("time_limit"), callback=cb, log=(lambda m: log(m)) if st.get("verbose", True) else None)
            else:
                raise ValueError(name)
            x = res["x"]
            history = history + [dict(stage=si, name=name, **h) for h in res["history"]]
            status_all.append(dict(stage=si, name=name, status=res["status"], it=res["it"], cost=res["cost"]))
            log(f"stage {si} {name} done: status {res['status']} it {res['it']} cost {res['cost']:.6e}")
            if res["status"] == "stopped":
                sys.exit(3)
            opt_state = {}
            save_ckpt(x, si + 1, {}, history, res["cost"])
            last_ckpt = time.time()
        # final diagnostics (in the physical variables q = A qhat if amp_param)
        r = prob.residual(x)
        cost = 0.5 * float(r @ r)
        x_hat, cfg_hat = x.detach().clone(), cfg
        amp = prob.amp_of(x)
        if cfg.amp_param:
            x_phys, cfg_phys = prob.to_physical(x)
            prob_phys = Problem(cfg_phys, device=dev)
            prob_phys.cfg.gauge_target = prob.cfg.gauge_target; prob_phys.cfg.w_q = prob.cfg.w_q; prob_phys.cfg.w_eta = prob.cfg.w_eta
            log(f"amp_param: A = {amp:.6e}; converting to physical variables for diagnostics")
            prob, x, cfg = prob_phys, x_phys, cfg_phys
        rep = diagnostics.report(prob, x)
        cphi, cq, _ = prob.split(x)
        full, sw, pol = prob.tail_integrals(cphi[-1].to(dev), cq[-1].to(dev), prob.alpha)
        # conversion factor to the reporting gauge int |F|^2 dS = 1: F_L = L^(1+alpha) F, so L = full^(-1/(2(1+alpha)))
        Lrep = full ** (-1.0 / (2 * (1 + prob.alpha))) if full > 0 else float("nan")
        s1 = None
        if cfg.s1_constraint:
            res_s1, _ = prob.s1_residual_and_jac(x)
            s1 = dict(z0=prob.z0_of(x), rows=(res_s1 / cfg.w_s1).tolist())
        point_defects = None
        if prob.Jpt.shape[0]:
            pd = (prob.Jpt @ x.to(prob.device) - prob.bpt).detach().cpu().numpy()
            npr = len(cfg.point_rows)
            wts = np.array([float(pr.get("weight", 100.0)) for pr in cfg.point_rows]) if npr else np.zeros(0)
            point_defects = dict(point_rows=[dict(field=pr["field"], der=pr["der"], r=pr["r"], z=pr["z"], defect=float(pd[j] / wts[j])) for j, pr in enumerate(cfg.point_rows)],
                                 axis_rows_max_abs=(float(np.max(np.abs(pd[npr:]))) / cfg.w_axis_q if len(pd) > npr else None))
        elapsed = elapsed_prev + time.time() - t_job0
        val = None
        if job.get("validate", True):
            try:
                from axi import validate as _val
                t_v = time.time()
                val_full = _val.validate(prob, x)
                try:
                    val_full["stagnation"] = _val.stagnation(prob, x)
                except Exception:
                    val_full["stagnation"] = dict(error=traceback.format_exc()[-500:])
                val_full["elapsed_s"] = time.time() - t_v
                atomic_json(val_full, os.path.join(run_dir, "validation.json"))
                val = {k: val_full[k] for k in ("rho_max", "m_max", "rho_M_max", "rho_reduced_max", "a_eff", "s_core", "s_far", "Omega_max", "rho_max_by_eq", "status", "n_degenerate")}
                stg = val_full.get("stagnation", {})
                val["n_axis_zeros"] = len(stg.get("axis_zeros", [])); val["n_offaxis_zeros"] = len(stg.get("offaxis_zeros", []))
                val["swirl_max_defect"] = (stg.get("swirl_max") or {}).get("defect")
                val["elliptic_max_rel_diff_phi"] = (val_full.get("elliptic") or {}).get("max_rel_diff_phi")
                log("validation: " + _val.summary_line(val_full) + f" ({val_full['elapsed_s']:.0f}s)")
            except Exception:
                log("validation failed:\n" + traceback.format_exc())
        b1 = prob.cost_breakdown(x)
        result = dict(job_id=jid, branch=job.get("branch"), cost_breakdown=b1, validation=val, swirl_amplitude_A=amp, amp_param=cfg_hat.amp_param, row_scale=[prob.cfg.w_q, prob.cfg.w_eta], stage=job.get("stage"), tags=job.get("tags", []), cfg=json.loads(cfg.to_json()),
                      init=job.get("init"), from_state=job.get("from_state"), optimizer=stages, stage_status=status_all,
                      cost=cost, rms_weighted=math.sqrt(2 * cost / r.shape[0]), n_iter=len(history), elapsed_s=elapsed,
                      cl=prob.cl_of(x), alpha=prob.alpha, nx=prob.nx, n_rows=prob.n_rows, gauge_target=prob.cfg.gauge_target,
                      L_to_reporting_gauge=Lrep, tail_int_F2=full, tail_int_Ftheta2=sw, s1=s1, point_row_defects=point_defects, report=rep, finished=now(),
                      device=str(dev), gpu=os.environ.get("CUDA_VISIBLE_DEVICES"), hostname=os.uname().nodename)
        atomic_save(dict(x=x.detach().cpu(), cfg=cfg.to_json(), history=history, cost=cost, gauge_target=prob.cfg.gauge_target,
                         row_scale=(prob.cfg.w_q, prob.cfg.w_eta), x_hat=x_hat.cpu(), cfg_hat=cfg_hat.to_json(), swirl_amplitude_A=amp,
                         result_summary={k: v for k, v in result.items() if k != "report"}, time=now(), job_id=jid), final_path)
        atomic_json(result, result_path)
        log(f"finished: cost {cost:.6e} {diagnostics.summarize(rep)}")
        if os.path.exists(ckpt_path):
            os.remove(ckpt_path)
        sys.exit(0)
    except SystemExit:
        raise
    except Exception:
        log("ERROR\n" + traceback.format_exc())
        atomic_json(dict(job_id=jid, error=traceback.format_exc(), time=now()), os.path.join(run_dir, "error.json"))
        sys.exit(1)


if __name__ == "__main__":
    main()
