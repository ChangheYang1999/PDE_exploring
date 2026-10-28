#!/usr/bin/env python
"""Enqueue continuation/refinement jobs from saved starts (exact embedding into a larger basis), e.g. the 2x2 experiment
(fixed/free parameters x current/refined basis). Usage:
  enqueue_continuation.py --src runs/<job>/starts/start_000.pt --tag c1 --L 10 --Nk 24 [--free] [--priority 10] [--sigmaZ 1] [--far 4096,16384,65536] [--channels 6,6,6]"""
import sys, os, json, time, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
from scripts.enqueue_stage1 import enqueue
ap = argparse.ArgumentParser()
ap.add_argument("--src", required=True); ap.add_argument("--tag", required=True); ap.add_argument("--L", type=int, required=True); ap.add_argument("--Nk", type=int, required=True)
ap.add_argument("--Nr", type=int, default=None); ap.add_argument("--free", action="store_true"); ap.add_argument("--priority", type=int, default=10)
ap.add_argument("--sigmaZ", type=float, default=None); ap.add_argument("--far", default="4096,16384,65536"); ap.add_argument("--channels", default=None)
ap.add_argument("--max_iter", type=int, default=300); ap.add_argument("--perturb", type=float, default=0.0); ap.add_argument("--formulation", default="mom")
ap.add_argument("--time_limit", type=float, default=7200); ap.add_argument("--nl_den", default="nl", help="nl (T4+T5) or all5 (five-term denominator) or all5far")
ap.add_argument("--chdeg", default=None, help="channel angular degrees LB,LD,LE (SPEC 4.4 closure: 2L+3,2L+2,L); default: all L")
ap.add_argument("--R1", type=float, default=None, help="core damping radius of the B/D/E channels in units of R0 (default R0)")
ap.add_argument("--exclusive", action="store_true", help="force one job per GPU (memory rule)"); ap.add_argument("--chunk", type=int, default=None)
ap.add_argument("--suffix", default="", help="appended to the job id")
ap.add_argument("--c_l", type=float, default=None, help="override c_l (fixed-parameter scan from a warm start, SPEC 11c V3)")
ap.add_argument("--omega", type=float, default=None, help="override omega")
ap.add_argument("--m_parity", default=None, help="override the azimuthal parity of the target basis (even -> all for the odd-m test)")
ap.add_argument("--perturb_m", type=int, default=None); ap.add_argument("--perturb_m_rel", type=float, default=0.0)
ap.add_argument("--max_retries", type=int, default=6); ap.add_argument("--far_lambda", type=float, default=None, help="all5far far-imbalance weight (default 1e-2)")
ap.add_argument("--closure_lambda", type=float, default=None, help="weight of the closure rows G_carried - G_required (0 = off)")
ap.add_argument("--fsw", type=float, default=None, help="S7 (a): continuation row on the mean-swirl fraction of the tail (target value)")
ap.add_argument("--fsw_weight", type=float, default=None); ap.add_argument("--boost_e_core", type=float, default=None, help="S7 (b)/(c): scale the m != 0 content so that the core eddy energy fraction reaches this value")
ap.add_argument("--nu", type=float, default=None, help="S8: artificial viscosity (R^nu = R_u - nu Delta U); the job is labelled a viscous continuation, never an Euler candidate")
ap.add_argument("--pin_c_l", type=float, default=None, help="S8 with --free: row pinning c_l at this value while omega moves")
ap.add_argument("--balance_lambda", type=float, default=None, help="S9: weight of the scalar rows lambda E_ren and lambda H_tot/int|h| (d64)")
ap.add_argument("--core_pin", default=None, help="S8 core nontriviality row: 'auto' pins the core RMS of U at the start state's value")
ap.add_argument("--nonaxi_pin", default=None, help="S9b guard rows: 'auto' pins e_core and e_F at the start state's values")
ap.add_argument("--nonaxi_r_tail", type=float, default=None, help="S9d: e_core shell-set cutoff (lower edge <= r_tail) frozen from Z0, used with numeric --nonaxi_pin e_core,e_F")
ap.add_argument("--both_weight", type=float, default=None, help="S10: weight of the vorticity rows in the 'both' formulation (--formulation both)")
ap.add_argument("--jtj_blocks", type=int, default=None, help="split-column J^T J accumulation with this many column blocks (memory J/blocks, time (blocks+1)/2; L10 with SPEC channels)")
ap.add_argument("--lm_only", action="store_true", help="solver validation: run the LM and save its output, skip the diagnostics battery (never a ranked state)")
ap.add_argument("--lam0", type=float, default=None, help="initial Marquardt parameter (default 1e-2)")
ap.add_argument("--radial_lambda_w", type=float, default=None, help="S12: weight w of the sphere rows on the radial-lambda part of the momentum residual (lead 11:27Z)")
ap.add_argument("--refresh_block", type=int, default=None, help="safeguarded lagged-target refresh (lead d128 CV 4): freeze the closure target and the nonlinear weights for blocks of N accepted iterations (default off)")
ap.add_argument("--refresh_backtrack", action="store_true", help="with --refresh_block: restore the previous block boundary when the merit function rose")
ap.add_argument("--ftol", type=float, default=1e-7, help="LM stop: one accepted step with relative cost decrease below this value ends the run (default 1e-7, the production value since Stage I; 1e-10 to run a rung to its iteration budget)")
a = ap.parse_args()
S = torch.load(os.path.join(ROOT, a.src) if not os.path.isabs(a.src) else a.src, map_location="cpu", weights_only=False); cfg = S["config"]
c_l_t = a.c_l if a.c_l is not None else cfg["c_l"]; om_t = a.omega if a.omega is not None else cfg["omega"]
job_id = f"{a.tag}_L{a.L}_cl{c_l_t:.2f}_om{om_t:+.1f}{'_free' if a.free else '_fixed'}{'_both%g' % a.both_weight if (a.formulation == 'both' and a.both_weight is not None) else ('_both' if a.formulation == 'both' else '')}{'_AVnu%.0e' % a.nu if a.nu else ''}{'_bal%g' % a.balance_lambda if a.balance_lambda else ''}{'_corepin' if a.core_pin else ''}{'_naxpin' if a.nonaxi_pin else ''}{'_rl%g' % a.radial_lambda_w if a.radial_lambda_w else ''}{a.suffix}"
c = dict(L=a.L, Nk=a.Nk, Nr=(a.Nr or 3 * a.Nk), m_parity=(a.m_parity or cfg.get("m_parity", "even")), R0=cfg.get("R0", 1.0), formulation=a.formulation, c_l=c_l_t, omega=om_t,
         free_params=a.free, n_starts=1, seed=0, max_iter=a.max_iter, init_from=os.path.relpath(S and (os.path.join(ROOT, a.src) if not os.path.isabs(a.src) else a.src), ROOT) if False else (a.src if os.path.isabs(a.src) else os.path.join(ROOT, a.src)),
         perturb=a.perturb, nl_weighting=True, sigmaZ=a.sigmaZ, far_radii=[float(v) for v in a.far.split(",")] if a.far else None,
         time_limit_per_start=a.time_limit, chunk=(256 if a.free else 512), threads=1, ftol=a.ftol, families=["init_from"],
         tail_constraints=True, sigmaZ_ramp_iters=(60 if a.sigmaZ else 0), nl_denominator=a.nl_den)   # v5 defaults: exact tail-moment constraints, Sigma_Z target ramp
if a.channels:
    nb, nd, ne = [int(v) for v in a.channels.split(",")]; c["channels"] = dict(NkB=nb, NkD=nd, NkE=ne, core_damp=2)
    if a.chdeg:
        LB, LD, LE = [int(v) for v in a.chdeg.split(",")]; c["channels"].update(LB=LB, LD=LD, LE=LE)
    if a.R1 is not None:
        c["channels"]["R1"] = a.R1 * c["R0"]
if a.chunk:
    c["chunk"] = a.chunk
if a.closure_lambda is not None:
    c["closure_lambda"] = a.closure_lambda
if a.refresh_block:
    c["refresh_block"] = int(a.refresh_block); c["refresh_backtrack"] = bool(a.refresh_backtrack)
if a.far_lambda is not None:
    c["far_lambda"] = a.far_lambda
if a.perturb_m is not None:
    c["perturb_m"] = a.perturb_m; c["perturb_m_rel"] = a.perturb_m_rel
if a.fsw is not None:
    c["fsw"] = a.fsw
if a.fsw_weight is not None:
    c["fsw_weight"] = a.fsw_weight
if a.boost_e_core is not None:
    c["boost_e_core"] = a.boost_e_core
if a.nu is not None:
    c["nu"] = a.nu
if a.pin_c_l is not None:
    c["pin_c_l"] = a.pin_c_l
if a.balance_lambda is not None:
    c["balance_lambda"] = a.balance_lambda
if a.core_pin is not None:
    c["core_pin"] = a.core_pin if a.core_pin == "auto" else float(a.core_pin)          # S9d: numeric pin frozen from Z0
if a.nonaxi_pin is not None:
    c["nonaxi_pin"] = a.nonaxi_pin if a.nonaxi_pin == "auto" else [float(v) for v in a.nonaxi_pin.split(",")]   # 'e_core,e_F' numeric pins frozen from Z0
if a.nonaxi_r_tail is not None:
    c["nonaxi_r_tail"] = a.nonaxi_r_tail
if a.both_weight is not None:
    c["both_weight"] = a.both_weight
if a.radial_lambda_w is not None:
    c["radial_lambda_w"] = a.radial_lambda_w
if a.jtj_blocks is not None:
    c["jtj_blocks"] = a.jtj_blocks
if a.lm_only:
    c["lm_only"] = True
if a.lam0 is not None:
    c["lam0"] = a.lam0
ok = enqueue(dict(job_id=job_id, type="continuation", stage="I", priority=a.priority, max_retries=a.max_retries, config=c,
                  exclusive=(a.L >= 8 or a.exclusive or bool(a.chdeg)), note=f"continuation of {a.src} (holdout rho_u {((S.get('spec_diag_holdout') or {}).get('global_') or {}).get('rho_u_max')})"))
print(("enqueued " if ok else "exists: ") + job_id)
