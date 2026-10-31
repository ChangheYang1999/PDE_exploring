#!/usr/bin/env python
"""6.3 (a) record v1 (lead 2026-10-29T17:50:42Z item 3, 17:55:21Z items 2 and 3, 18:22:07Z items 1 to 4; verifier V405): one JSON per state with the
registered SPEC 6.3 (a) exclusion quantities, the 6.3 (b) flag quantities, and their comparison with the lineage start reference, computed with the
end-state battery (the worker's battery functions: spec_diagnostics on the training and holdout grids, the half-offset family and spheres, the
located |Omega| maxima, the core-resolution sets of v1.21 (b)) on the state's own parameters and quadrature, plus three add-ons the worker record lacks:
  rho_P^max (lead 18:22:07Z item 1): rho_P(k) = RMS_k(Lap P + f) / (RMS_k(Lap P) + RMS_k(f)) over the holdout shells, f = tr(DU^2) the pressure
             source (-Lap P = f is the equation the solver represents; the registered Euler3 form). Lap P is formed from the solver's own
             spherical-harmonic coefficients P_lm(r), dP_lm/dr at the holdout radii and a centred finite difference of dP_lm/dr across evaluation
             radii r (1 +- eps) (independent Green evaluations), so the identity Lap P = -f is not used in the check. Registered value: the full
             source on the holdout grid; the value with the source projected onto the solver's angular modes (l <= Lf) is reported beside it.
             Accuracy rule: (a) code test, the same construction applied to P_lm(r) = r^l exp(-r^2/a^2) (closed-form Laplacian) on the state's own
             holdout radii and modes, relative error of Lap P per shell (a = R0 and a = 64 R0); (b) the ladder eps, 2 eps, 4 eps with the largest
             change of rho_P^max. rho_P is cleared only if rho_P^max + max((a) error, (b) change) <= 1e-3; if the (a) error or the (b) change exceeds
             1e-4, rho_P is OPEN (not cleared, not an exclusion).
  G5 at the state: validation/gates.py run_case(sections=('G5',)) on the saved state (G5 (a) spatial differences of U against DU, (b) divergences,
             (c) second part, the pressure source consistency). The 50-digit angular-table test of G5 (c) first part is a property of the code
             established in the validation chains and is not repeated per state.
  N6 and the radial coefficients (lead 18:22:07Z item 2): per block (A, C, B, D, E), the energy fraction of the top max(1, round(0.2 Nk)) radial modes
             (3 of 16; 1 of 4); the 6.3 (b) flag is raised if any block's fraction exceeds twice its start value; a block whose start fraction is below
             1e-14 is OPEN (end value written). The angular-degree part (top 20 per cent of the degrees present in the block) is reported, not flagged.
             The top-two coefficient flag (last two radial coefficients over the block maximum above 0.1) is evaluated in every block.
Modes:  start <job json> --tag <tag>   : the lineage's initial state as its first FREE run began (the worker's own load_start_state with the job's
             configuration and seed, then pivot, geometry, phase alignment and the constraint maps as in run_job), then the SAME F-gauge projection the
             worker applies to its reported end states (coefficients divided by the far-field norm sqrt(tail_norm2)); the raw start is saved beside
             it with its far-field norm (<tag>_state_raw.pt), the projected state as <tag>_state.pt; the full battery runs on the projected state.
        end <run dir> --tag <tag> [--full] [--start-ref <record.json>] [--segment-start <record.json>] : the end state of a run (the worker's
             runs/<run>/starts/start_000.pt, already F-projected). The run record (results.jsonl start_result) must name that file as its zfile and
             carry the state's parameters, else the run is REFUSED. Without --full the battery fields are read from the run record (that IS the
             end-state battery on the state's own parameters and quadrature; file, sha256, parameters and vector hash recorded); with --full they are
             recomputed AND compared with the record (lead 18:22:07Z item 4: 1e-10 relative, flags exactly). --start-ref gives the lineage start
             reference (a record of this script) for the ratios of (b), (g) and 6.3 (b); --segment-start a record reported beside it.
Decisions (SPEC 6.3 (a) with 5.3, 5.4, 6.2; lead 17:50:42Z item 3 (a) to (g), 17:55:21Z item 2, 18:22:07Z): see judge(). Every required item needs a
finite value with a valid denominator; otherwise it is listed under 'open' (unknown is never read as false) and registered_clearance_6_3a is false.
Numerics, not a proof. Usage:
       python validation/record_63a.py start <job.json> --tag P1_start [--device cuda:0]
       python validation/record_63a.py end runs/<run> --tag cont1_s3_end --start-ref /abs/validation/records_63a/P1_start.json [--full] [--device cuda:0]
v10 (2026-10-29T20:0xZ; V435, V437): a start-reference record separates reference-data validity from end clearance: its open items that depend on a reference (the (b) and (g) ratios, N6, a_eff, r_tail, the run-path omega item) are listed under open_not_applicable, the remaining open items under open, reference_data_valid is true when no exclusion is raised and open is empty, and registered_clearance_6_3a is false with the note that a start reference is a denominator record, never an end candidate. v9 (8a567eceeae0ddf8) kept as record_63a.py.v9_8a567ece.
v9 (2026-10-29T19:5xZ): end mode compares the run record's zfile with the saved end state by real paths resolved against the run's own experiment directory (the v8 comparison used paths relative to the frozen copy and refused every end state when run through run_frozen); nothing else changed. v8 (cbd0d1353b8a4887) kept as record_63a.py.v8_cbd0d135.
v8 (2026-10-29T19:5xZ; lead 19:35:33Z items 1 (a) to (f) and 2): judge() requires the construction degrees to be exactly range(Lf + 1), the construction shells to be the battery's shells with the same edges and a_k recomputed from them (sqrt(max(lo, hi/64) hi), 1e-12), the pressure shell edges equal to the battery's; every detailed ladder entry's eps equal to its key and the summary equal to the detailed base; the G5 group keys exactly the registered groups and every G5 pass field a genuine bool; the expected spectral inventory equal to the active blocks of the recorded layout; a missing or unrecognized pressure status, or one disagreeing with the recomputed decision, gives OPEN; the norms and absolute maxima of the battery finite and non-negative. decide_record() holds the per-reference loop for the wrapper. v7 (b15aa985fba0107f) kept as record_63a.py.v7_b15aa985.
v7 (2026-10-29T19:2xZ; V422): judge() binds every pressure quantity to the arrays: the ladder's first value equals the shell maximum, every ladder entry carries its finite shell array with a consistent maximum, the ladder keys are exactly eps, 2 eps, 4 eps with eps 1e-3, the construction test is recomputed from its per-shell per-degree errors (every shell and every degree present, finite, non-negative, max <= 1e-4, no skipped entry, eps_test 1e-4); G5 (a), (b), (c) are recomputed from the recorded numbers against the limits; the expected block inventory is required (no fallback); the start reference's norm fields must be consistent (F_norm_projected^2 = F_norm2_projected = F_norm2 from the coefficients to 1e-12). v6 (5f99c9e06896fc35) kept as record_63a.py.v6_5f99c9e0.
v6 (2026-10-29T19:1xZ; lead 19:09:20Z item 1 (c), V421): the construction test evaluates P_lm = (r/a_k)^l exp(-(r/a_k)^2) (the constant a_k^l divides out of e_k; no overflow at the outer shells for the pressure degrees); the core-ball centre convention a_k = sqrt((b/64) b) = b/8 (HoldoutGrid.rmid) is stated in the record. v5 (8c372940984cd0b4) kept as record_63a.py.v5_8c372940.
v5 (2026-10-29T19:1xZ; lead 19:02:50Z items 1 and 2; V416): the (a) construction test is the per-shell, per-degree test of 19:02:50Z item 1 (a) (P_lm = r^l exp(-r^2/a_k^2), a_k the geometric centre radius of shell k, m = 0 and m = l where present, eps_test 1e-4, e_k per shell and degree, pass if max <= 1e-4 with no shell skipped); the decision rule of 19:02:50Z item 1 (Delta = |rho(2 eps) - rho(eps)|; cleared if (a) passes, all finite, Delta <= 1e-4 and rho(eps) + Delta <= 1e-3; exclusion if (a) passes, Delta <= 1e-4 and rho(eps) - Delta > 1e-3; OPEN otherwise), recomputed in judge() from the shell arrays and ladder values (non-negative, nonzero shell count, maxima consistent); F-gauge tolerance 1e-8 on F_norm2 from the coefficients (19:02:50Z item 2); FIXED states (coefficients only) take c_l, omega from the configuration and the vector length is checked (V416). v4 (9470d3eb614e2c05) kept as record_63a.py.v4_9470d3eb.
v4 (2026-10-29T19:0xZ; lead 18:49:47Z items 1 (b), (e), 3 and 5, 18:51:10Z; V412): gauge test |F_norm2 - 1| <= 1e-12 with F_norm2 from the coefficients of the state the battery uses (start and end); several --start-ref records (F2 states against the F2 start and the S01 state): an item raised against any reference counts; the source domain of each core a_max weight is written; the code test adds the rational decaying pressure s^l (1 + s^2)^(-q), q = (l + 4)/2 (V412) and a variant weighted by the state's own modal amplitudes max_r |P_lm|, plus a finer ladder (1e-4, 2e-4, 4e-4) as information; the registered (a) error stays the Gaussian unit-weight test until the lead registers another; compare_batteries requires both sides nonempty. v3 (54046b890ee7b244) kept as record_63a.py.v3_54046b89.
v3 (2026-10-29T18:5xZ; V411 items 1 to 4): the rho_P decision is recomputed in judge() from the finite quantities with complete shell coverage of the code test (scales a = R0 2^j, j = -4..10 step 2); F-gauge norm of the state and of the start reference within F_norm_tol of 1 required, F_projected only when the projection was applied, start reference must be marked; compare_batteries treats missing values as disagreement and requires finite numbers and genuine booleans; G5 combined pass recomputed from the component booleans; expected active-block inventory for the spectra with OPEN on each invalid ratio. v2 (41f71bbc955e5eb9) kept as record_63a.py.v2_41f71bbc.
v2 (2026-10-29T18:4xZ; V405 items 1 to 5, lead 18:22:07Z items 1 to 4): R0-based vorticity-radius limit; finiteness and denominators; F-gauge projected
start reference with the raw start kept; end-mode binding; rho_P accuracy rule (code test + ladder); per-block N6 with the angular-degree part;
--full comparison table. v1 (da7aecb6036754c1) kept as record_63a.py.v1_da7aecb6."""
import sys, os, json, time, math, hashlib, argparse, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from src.equations.fields import Model, alpha_of
from src.equations import residuals as res
from src.pressure.poisson_sh import PressureSolver
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
from src.validation.spec_diagnostics import spec_diagnostics, tier_S
from src.validation.holdout import HoldoutGrid, half_offset_edges, sphere_diagnostics, exchange_radii, two_family_summary
from src.validation.diagnostics import candidate_diagnostics
from src.validation.critical_points import local_maxima_omega
from src.validation.core_resolution import core_resolution
from validation.gates import Case, run_case, code_hashes
_spec = importlib.util.spec_from_file_location("worker_d6", os.path.join(ROOT, "scripts", "worker_d6.py")); W = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(W)

VERSION = "v10"
REF_DEPENDENT_PREFIXES = ("(b) ", "(g) ", "N6 radial part", "a_eff decreasing", "r_tail increasing", "omega decreasing monotonically")
G5A_GROUPS = ["near_origin(r<=0.1R0)", "core_intermediate", "far(r>256R0)"]
G5B_KEYS = ["U", "U_c", "U_w"]
NONNEG_FIELDS = ("N_core", "N_F", "e_core", "e_F", "max_U", "U_L2_r_lt_1", "rho_u_max", "rho_u_max_holdout", "a_max_core", "a_max_core_upper", "a_eff", "r_tail", "r_core", "F_norm2_from_coefficients", "located_max_abs_Omega", "sigma_u_max", "a_max", "a_max_half")
PROV_START = "computed now (full battery of this script, on the F-projected start reference)"
PROV_FULL = "computed now (--full) and compared with the worker's end-of-run battery (results.jsonl start_result)"
OUT_DIR = os.path.join(ROOT, "validation", "records_63a")
TH = dict(N_core=1e-2, N_F=1e-2, e_core=1e-4, e_F=1e-4, collapse_ratio=0.1, saturation_edge=0.002, omega_lo=1e-3, omega_hi=1e3, near_edge=0.02, rho_P=1e-3, rho_P_accuracy_open=1e-4,
          a_max_factor=2.0, G5a=5e-7, G5b=1e-10, G5c=1e-12, omega_flag=1e-2, omega_decrease_factor=10.0, a_eff_factor=2.0, top2_ratio=0.1, N6_factor=2.0, N6_start_floor=1e-14,
          r_vorticity_max_octaves=8, r_tail_factor=4.0, full_compare_rel=1e-10, F_norm2_tol=1e-8, eps_test=1e-4)
BATTERY_NUMERIC_FIELDS = ("c_l", "omega", "N_core", "e_core", "N_F", "e_F", "max_U", "r_core", "r_tail", "rho_u_max", "rho_u_max_holdout", "lambda_max_S", "U_L2_r_lt_1", "a_max", "a_max_half",
                          "sigma_u_max", "sigma_Om", "r_peak_Omega", "N_core_holdout", "e_core_holdout", "located_max_r", "located_max_abs_Omega", "a_eff", "r_star", "core_doubling_change_max",
                          "core_ball_over_a_eff", "a_max_core", "a_max_core_upper", "sigma_u_max_core", "F_norm2")
BATTERY_FLAG_FIELDS = ("tier_S", "tier_S_holdout", "core_resolved")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def log(msg):
    print(f"{now()} {msg}", flush=True)


def fin(x):
    """finite float or None (V405 item 2: unknown is never read as a value)."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def pos(x):
    """finite positive float (a valid denominator) or None."""
    v = fin(x)
    return v if (v is not None and v > 0) else None


# ----------------------------------------------------------------------------------------------------------------------------- add-ons
def spectra(model, zf):
    """Per block (lead 18:22:07Z item 2; V411 item 4: the expected active blocks are those of the model layout with at least two radial functions): energy fraction of the top max(1, round(0.2 Nk)) radial Chebyshev modes (N6 radial part), the energy fraction of the
    top 20 per cent of the angular degrees present in the block (reported only), and the last-one / last-two coefficient ratios to the block maximum."""
    dd = model.unpack_all(zf); l_arr = model.l_arr.to(zf.device); per = {}
    expected = [nm for nm, nk in model.layout if nk >= 2]
    for nm in ("A", "C", "B", "D", "E"):
        arr = dd.get(nm)
        if arr is None or arr.numel() == 0 or arr.shape[0] < 2:
            if nm in expected:
                per[nm] = dict(n_k=None, top_fraction=None, last2_over_max=None, note="expected active block without coefficients")
            continue
        nk = int(arr.shape[0]); ntop = max(1, int(round(0.2 * nk))); k0 = nk - ntop
        e_k = (arr ** 2).sum(1); tot = float(e_k.sum())
        e_q = (arr ** 2).sum(0); present = sorted(set(l_arr[e_q > 0].tolist()))
        ang = None
        if present:
            nd = max(1, int(round(0.2 * len(present)))); top_deg = present[len(present) - nd:]
            mask = torch.zeros_like(e_q, dtype=torch.bool)
            for dg in top_deg:
                mask |= (l_arr == dg)
            ang = dict(degrees_present=present, top_degrees=top_deg, fraction=(float(e_q[mask].sum()) / tot if tot > 0 else None))
        mx = float(arr.abs().max()); last = float(arr[-1].abs().max()); last2 = float(arr[-2:].abs().max())
        per[nm] = dict(n_k=nk, top_modes=ntop, top_modes_from_k=k0, top_fraction=(float(e_k[k0:].sum()) / tot if tot > 0 else None), block_energy=tot,
                       last_over_max=(last / mx if mx > 0 else None), last2_over_max=(last2 / mx if mx > 0 else None), angular_top20=ang,
                       energy_per_k=[float(v) / tot if tot > 0 else None for v in e_k.cpu().numpy()])
    return dict(definition="per block: energy fraction of the top max(1, round(0.2 Nk)) radial Chebyshev modes (3 of 16; 1 of 4), summed over the angular modes (N6 radial part; flagged against twice "
                           "its start value); energy fraction of the top 20 per cent of the angular degrees present in the block (reported, not flagged); last-one and last-two radial coefficient "
                           "ratios to the block maximum (flag if last2_over_max > 0.1 in any block)", expected_blocks=expected, layout=[list(x) for x in model.layout], per_block=per)


def lap_code_test(ps, holdout, model, eps_list, scales, weights=None, kind="gaussian"):
    """Lead 18:22:07Z item 1 (a): the Laplacian construction (centred difference of dP_lm/dr across r(1 +- eps), the radial operator, the solver's synthesis) applied to
    P_lm(r) = r^l exp(-r^2/a^2) in every mode of the solver, whose Laplacian is (4 r^2/a^4 - (4 l + 6)/a^2) r^l exp(-r^2/a^2) Y_lm; relative error per shell."""
    em = holdout.model; r = em.r[:, None]; pl = ps.pl[None, :]
    wq = (weights[None, :] if weights is not None else torch.ones_like(pl))
    out = {}
    for a in scales:
        if kind == "gaussian":                                                  # P_lm = r^l exp(-r^2/a^2): Lap = (4 r^2/a^4 - (4 l + 6)/a^2) P
            def g(rr):
                return wq * torch.exp(pl * torch.log(rr) - (rr / a) ** 2)
            def dg(rr):
                return g(rr) * (pl / rr - 2 * rr / a ** 2)
            P = g(r); exact_lm = (4 * r ** 2 / a ** 4 - (4 * pl + 6) / a ** 2) * P
        else:                                                                   # V412: P_lm = s^l (1 + s^2)^(-q), s = r/a, q = (l + 4)/2: Lap = (1/a^2) s^l (1+s^2)^(-q-2) [ -2q(2l+3)(1+s^2) + 4q(q+1) s^2 ] (algebraic tail stays visible)
            q = (pl + 4.0) / 2.0
            def g(rr):
                s_ = rr / a
                return wq * torch.exp(pl * torch.log(s_) - q * torch.log1p(s_ ** 2))
            def dg(rr):
                s_ = rr / a
                return g(rr) * (pl / rr - 2 * q * s_ / (a * (1 + s_ ** 2)))
            s_ = r / a; P = g(r)
            exact_lm = P / (a ** 2) * (-2 * q * (2 * pl + 3) * (1 + s_ ** 2) + 4 * q * (q + 1) * s_ ** 2) / (1 + s_ ** 2) ** 2
        exact = exact_lm @ ps.A0p.T; rms_ex = holdout.rms(exact)
        res_a = {}
        for eps in eps_list:
            d2 = (dg(r * (1 + eps)) - dg(r * (1 - eps))) / (2 * eps * r)
            num = (d2 + 2 * dg(r) / r - pl * (pl + 1) * P / (r * r)) @ ps.A0p.T
            rms_err = holdout.rms(num - exact); mx = max(rms_ex) if rms_ex else 0.0
            rel = [(e / x if (x > 1e-300 * mx and x > 0) else None) for e, x in zip(rms_err, rms_ex)]
            res_a[f"{eps:.0e}"] = dict(rel_error_per_shell=rel, max_rel_error=max([v for v in rel if v is not None] or [None]), shells_evaluated=sum(1 for v in rel if v is not None))
        out[f"a={a:.6g}"] = dict(scale=a, rms_exact_per_shell=rms_ex, per_eps=res_a)
    worst = max([v["max_rel_error"] for s in out.values() for v in s["per_eps"].values() if v["max_rel_error"] is not None] or [None])
    nsh = holdout.n; covered = [False] * nsh
    for s_ in out.values():
        for v in s_["per_eps"].values():
            for k, e in enumerate(v["rel_error_per_shell"]):
                covered[k] = covered[k] or (e is not None)
    return dict(kind=kind, weighted=(weights is not None), tests=out, max_rel_error=worst, shells_covered=covered, coverage_complete=bool(all(covered)), n_shells=nsh, scales=list(scales), definition="P_lm(r) = r^l exp(-r^2/a^2) in all solver modes (unit coefficients), a in the listed scales; the same difference, operator and synthesis as the state's Lap P; shells where the exact field underflows are not evaluated")


def construction_test(ps, holdout, eps_test):
    """Lead 19:02:50Z item 1 (a): for every holdout shell k (a_k = geometric centre radius of the shell) and every pressure degree l of the solver's expansion,
    P_lm(r) = r^l exp(-r^2/a_k^2) in the modes (l, 0) and (l, l) where present, through the same construction (centred difference of dP_lm/dr at r(1 +- eps_test),
    radial operator, the solver's synthesis); e_{k,l} = RMS_k(Lap_code P - Lap_exact P) / RMS_k(Lap_exact P). Pass if max e <= 1e-4 with no shell skipped."""
    em = holdout.model; r = em.r[:, None]; pl = ps.pl; pm = ps.pm
    degrees = sorted(set(int(v) for v in pl.tolist())); per = {}; worst = None; skipped = []
    for k in range(holdout.n):
        a_, b_ = holdout.edges[k]; a_k = math.sqrt(max(a_, b_ / 64.0) * b_)                  # geometric centre radius (the core ball uses b/64 as its inner radius, as HoldoutGrid.rmid)
        mask_k = holdout.masks[k]; row = {}
        for l in degrees:
            cols = [q for q in range(pl.numel()) if int(pl[q]) == l and (int(pm[q]) == 0 or int(pm[q]) == l)]
            if not cols:
                continue
            A = ps.A0p[:, cols]; plq = pl[cols][None, :]
            def g(rr):                                                           # (r/a_k)^l exp(-(r/a_k)^2): the factor a_k^-l divides out of e_k and keeps the modal values finite (lead 19:09:20Z (c), V421)
                return torch.exp(plq * torch.log(rr / a_k) - (rr / a_k) ** 2)
            def dg(rr):
                return g(rr) * (plq / rr - 2 * rr / a_k ** 2)
            P = g(r); exact = ((4 * r ** 2 / a_k ** 4 - (4 * plq + 6) / a_k ** 2) * P) @ A.T
            d2 = (dg(r * (1 + eps_test)) - dg(r * (1 - eps_test))) / (2 * eps_test * r)
            num = (d2 + 2 * dg(r) / r - plq * (plq + 1) * P / (r * r)) @ A.T
            w = holdout.w_ang[None, :]
            def rms_k(X):
                pn = ((X ** 2) * w).sum(1)
                return float(((pn[mask_k] * holdout.w_vol[mask_k]).sum() / holdout.w_vol[mask_k].sum()).sqrt())
            den = rms_k(exact); e = (rms_k(num - exact) / den) if (den > 0 and math.isfinite(den)) else None
            row[str(l)] = e
            if e is None or not math.isfinite(e):
                skipped.append((k, l))
            elif worst is None or e > worst:
                worst = e
        per[str(k)] = dict(shell=[a_, b_], a_k=a_k, e_by_degree=row, max_e=max([v for v in row.values() if v is not None] or [None]))
    passed = bool(worst is not None and not skipped and worst <= TH["rho_P_accuracy_open"])
    return dict(eps_test=eps_test, degrees=degrees, modes="m = 0 and m = l where present (parity)", per_shell=per, max_e=worst, skipped=skipped, passed=passed, limit=TH["rho_P_accuracy_open"],
                pressure="P_lm(r) = (r/a_k)^l exp(-(r/a_k)^2), Laplacian (4 r^2/a_k^4 - (4 l + 6)/a_k^2) P_lm; a_k = sqrt(r_lo r_hi) for a shell, and for the core ball [0, b] the HoldoutGrid.rmid convention sqrt((b/64) b) = b/8",
                rule="lead 19:02:50Z item 1 (a): pass if max e_{k,l} <= 1e-4 over all shells and degrees with no shell skipped; a skipped or underflowing shell makes (a) OPEN; expected size about (eps_test (l + 2))^2 / 6")


def poisson_residual(model, zf, holdout, c_l, omega, eps=1e-3):
    """rho_P per holdout shell (module docstring) with the eps, 2 eps, 4 eps ladder and the closed-form code test."""
    t0 = time.time(); dev = model.r.device; em = holdout.model
    ps = holdout.pressure_solver(model, c_l, omega)
    f_src = res.pressure_source(model.fields_grid(zf, need_vort=False)["GU"])                       # the source on the training nodes (as in production)
    P, gradP, Plm, dPlm = ps.solve(f_src)
    r = em.r[:, None]; pl = ps.pl[None, :]
    L = model.L; Lx = getattr(model, "L_ext", L); ntheta = 2 * Lx + 12; nphi = 4 * Lx + 18
    def dP_at(scale):
        Ms = Model(L=L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=(em.r * scale).detach().cpu().numpy(), ntheta=ntheta, nphi=nphi,
                   c_l=model.c_l0, omega=model.omega0, free_params=model.free_params, channels=model.channels, device=dev, phi0=math.pi / (2 * nphi))
        pss = PressureSolver(model, p0=2 * alpha_of(float(c_l)) + 2, omega=float(omega), c_l=float(c_l), eval_model=Ms)
        _, _, Plm_s, dPlm_s = pss.solve(f_src)
        del pss, Ms
        if dev.type == "cuda":
            torch.cuda.empty_cache()
        return Plm_s, dPlm_s
    GUe = em.fields_grid(zf, need_vort=False)["GU"]; f_eval = res.pressure_source(GUe)            # the full source tr(DU^2) on the holdout grid
    w = em.grid.w
    gram = ps.A0p.T @ (w[:, None] * ps.A0p); gram_defect = float((gram - torch.eye(gram.shape[0], device=dev)).abs().max())
    f_proj = ((f_eval * w[None, :]) @ ps.A0p) @ ps.A0p.T                                          # projection onto the solver's modes (l <= Lf, parity)
    synth_check = float((Plm @ ps.A0p.T - P).abs().max() / P.abs().max().clamp_min(1e-300))
    rms = holdout.rms
    rf, rfp = rms(f_eval), rms(f_proj); rtr = rms(f_eval - f_proj)
    def ratio(a, b, c):
        return [None if not ((y + z_) > 0) else x / (y + z_) for x, y, z_ in zip(a, b, c)]
    ladder = {}; laps = {}
    for e in (eps, 2 * eps, 4 * eps):
        _, dPp = dP_at(1 + e); _, dPm = dP_at(1 - e)
        d2 = (dPp - dPm) / (2 * e * r)
        lap = (d2 + 2 * dPlm / r - pl * (pl + 1) * Plm / (r * r)) @ ps.A0p.T                       # Lap P on the holdout grid (Ne, Na)
        laps[e] = lap; rl = rms(lap)
        rho = ratio(rms(lap + f_eval), rl, rf); rho_p = ratio(rms(lap + f_proj), rl, rfp)
        ladder[f"{e:.0e}"] = dict(eps=e, rho_P_max=max([v for v in rho if v is not None] or [None]), rho_P_shells=rho, rho_P_proj_max=max([v for v in rho_p if v is not None] or [None]), rho_P_proj_shells=rho_p,
                                  rms_lap_P=rl, rms_residual=rms(lap + f_eval), rms_residual_proj=rms(lap + f_proj))
    keys = [f"{e:.0e}" for e in (eps, 2 * eps, 4 * eps)]
    vals = [ladder[k]["rho_P_max"] for k in keys]
    changes = [abs(b - a_) if (a_ is not None and b is not None) else None for a_, b in zip(vals[:-1], vals[1:])]
    change_max = max([c for c in changes if c is not None] or [None])
    test = construction_test(ps, holdout, TH["eps_test"])                                  # (a) of 19:02:50Z item 1: per shell and degree, eps_test 1e-4
    amp = Plm.abs().max(dim=0).values.clamp_min(1e-300); amp = amp / amp.max()
    tests_info = dict(modal_amplitude_profile=dict(l=[int(v) for v in ps.pl.tolist()], amplitude_normalized=[float(v) for v in amp.tolist()]),
                      gaussian_unit_old_rule=lap_code_test(ps, holdout, model, [eps], [float(model.R0), 64.0 * float(model.R0)]),
                      note="information only: the superseded test of 18:22:07Z (V412) at eps and the state's modal amplitude profile")
    base = ladder[keys[0]]
    rp = fin(base["rho_P_max"]); r2 = fin(ladder[keys[1]]["rho_P_max"]); r4 = fin(ladder[keys[2]]["rho_P_max"])
    delta = abs(r2 - rp) if (rp is not None and r2 is not None) else None; delta4 = abs(r4 - r2) if (r2 is not None and r4 is not None) else None
    ratio_changes = (delta4 / delta) if (delta and delta4 is not None) else None
    err_a = fin(test["max_e"])
    if not test["passed"] or rp is None or delta is None or delta4 is None or any(fin(v) is None for v in base["rho_P_shells"]):
        status = "OPEN: construction test not passed, or a quantity not finite"
    elif delta > TH["rho_P_accuracy_open"]:
        status = f"OPEN: ladder change Delta {delta:.2e} above {TH['rho_P_accuracy_open']:.0e}"
    elif rp + delta <= TH["rho_P"]:
        status = "cleared"
    elif rp - delta > TH["rho_P"]:
        status = "exclusion: rho_P_max(eps) - Delta above 1e-3"
    else:
        status = "OPEN: rho_P_max within Delta of the threshold"
    chg_b = delta; change_max = delta
    out = dict(rho_P_max=base["rho_P_max"], rho_P_shells=base["rho_P_shells"], rho_P_proj_max=base["rho_P_proj_max"], rho_P_proj_shells=base["rho_P_proj_shells"], rms_lap_P=base["rms_lap_P"],
               rms_residual=base["rms_residual"], rms_residual_proj=base["rms_residual_proj"], rms_f=rf, rms_f_proj=rfp, source_truncation_rel=[a_ / b if b > 0 else None for a_, b in zip(rtr, rf)],
               shell_edges=holdout.edges, n_shells=holdout.n, eps=eps, ladder=ladder, ladder_rho_P_max=dict(zip(keys, vals)), ladder_changes=changes, ladder_max_change=change_max, delta=delta, delta_4eps=delta4, ratio_successive_changes=ratio_changes,
               construction_test=test, construction_test_passed=test["passed"], construction_test_max_e=test["max_e"], code_test=None, code_test_max_rel_error=None,
               code_tests_information=tests_info, code_test_coverage_complete=(not test["skipped"]), code_test_note="a construction test on a known pressure (difference, operator, synthesis); it does not bound the error of the state's own Lap P, whose only error indication is the ladder change (lead 18:22:07Z item 1 rule applied as fixed)",
               accuracy_margin=(max(err_a, chg_b) if (err_a is not None and chg_b is not None) else None), rho_P_max_plus_margin=((rp + max(err_a, chg_b)) if (err_a is not None and chg_b is not None and rp is not None) else None),
               status=status, Lf=int(ps.Lf), n_modes=len(ps.pmodes), gram_defect_eval_grid=gram_defect, synthesis_check_rel=synth_check, chain_precision=ps.chain_precision,
               grid=dict(n_radii=int(em.r.numel()), ntheta=ntheta, nphi=nphi),
               definition="rho_P(k) = RMS_k(Lap P + f) / (RMS_k(Lap P) + RMS_k(f)), f = tr(DU^2) the pressure source on the holdout grid (-Lap P = f), holdout shells with exact quadrature; "
                          "Lap P = sum_q [P_q'' + 2 P_q'/r - l(l+1) P_q/r^2] Y_q with P_q, P_q' from the solver at the holdout radii and P_q'' by the centred difference of P_q' between the "
                          "radii r(1+eps) and r(1-eps) (independent Green evaluations); rho_P_proj uses the source projected onto the solver's angular modes; registered value: full source at eps",
               rule="lead 19:02:50Z item 1: (a) construction test per shell and degree passes (max e <= 1e-4, no shell skipped); Delta = |rho(2 eps) - rho(eps)|; cleared if all finite, Delta <= 1e-4 and rho(eps) + Delta <= 1e-3; exclusion if Delta <= 1e-4 and rho(eps) - Delta > 1e-3; OPEN otherwise; an empirical accuracy gate, not a bound", seconds=time.time() - t0)
    log(f"  rho_P: max {rp} (projected source {base['rho_P_proj_max']}); ladder {vals}; Delta {delta}; Delta(4eps) {delta4}; ratio {ratio_changes}; construction test max e {test['max_e']} passed {test['passed']} skipped {len(test['skipped'])}; gram defect {gram_defect:.1e}; status {status}; {out['seconds']:.0f} s")
    return out


def g5_at_state(state_path, device, tag):
    """validation/gates.py G5 (a), (b) and (c) second part at the saved state (own parameters)."""
    t0 = time.time()
    case = Case(f"63a_{tag}", device, start=state_path)
    out = run_case(case, quick=True, sections=("G5",))
    g5 = out["G5"]
    c_rel = fin(g5["G5c_source_consistency_rel"]); g5c_pass = (c_rel <= TH["G5c"]) if c_rel is not None else None
    a_, b_ = g5.get("G5a_PASS"), g5.get("G5b_PASS")
    g5_pass = (bool(a_) and bool(b_) and bool(g5c_pass)) if (isinstance(a_, bool) and isinstance(b_, bool) and g5c_pass is not None) else None
    rec = dict(G5a_PASS=a_, G5a_best_rel_per_group=g5["G5a_spatial_FD_vs_DU_best_rel_per_group"], G5b_PASS=b_, G5b_div_rel_max=g5["G5b_div_rel_max"],
               G5c_source_consistency_rel=g5["G5c_source_consistency_rel"], G5c_second_part_PASS=g5c_pass, G5_pass=g5_pass,
               points=len(g5["points"]), seed=g5["seed"], field=out["field"], pair=out["pair"], own_parameters=out["own_parameters"], harness="validation/gates.py run_case(sections=('G5',), quick=True)",
               harness_sha256=sha(os.path.join(ROOT, "validation", "gates.py")), limits=dict(G5a=TH["G5a"], G5b=TH["G5b"], G5c=TH["G5c"]),
               scope="G5 (a) spatial differences of U against DU at fixed coefficients and parameters, (b) div U and div U_p, (c) second part (source consistency); the 50-digit angular-table test of (c) first part is a code property established in the validation chains, not repeated here",
               seconds=time.time() - t0)
    log(f"  G5: a {a_} b {b_} c2 {g5c_pass} ({g5['G5c_source_consistency_rel']:.1e}); pass {g5_pass}; {rec['seconds']:.0f} s")
    return rec


# ----------------------------------------------------------------------------------------------------------------------------- battery
def gauge_norm(prob, model, zf):
    aT, aS, c_l, om = model.unpack(zf)
    return float(prob.tail_norm2(aT, aS, c_l, om).clamp_min(0).sqrt())


def gauge_norm2(prob, model, zf):
    """F_norm2 = int_S2 |F|^2 from the coefficients of the state (lead 18:49:47Z item 1 (b))."""
    aT, aS, c_l, om = model.unpack(zf)
    return float(prob.tail_norm2(aT, aS, c_l, om))


def full_battery(prob, model, zf, cfg):
    """The worker's end-state battery items that carry the 6.3 quantities (finish_start, variable names kept). Returns (fields, holdout)."""
    T = {}; t = time.time(); c_l, omega = (float(zf[-2]), float(zf[-1])) if model.free_params else (float(cfg["c_l"]), float(cfg["omega"]))
    diag = candidate_diagnostics(prob, zf); T["candidate_diagnostics"] = time.time() - t; t = time.time()
    sd = spec_diagnostics(prob, zf); tS, tS_checks = tier_S(sd); T["spec_diagnostics_training"] = time.time() - t; t = time.time()
    holdout = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
    sdh = spec_diagnostics(prob, zf, holdout=holdout); tSh, tSh_checks = tier_S(sdh); T["spec_diagnostics_holdout"] = time.time() - t; t = time.time()
    r_max_h = float(model.r.max())
    holdout_half = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, r_max_h))
    sdh_half = spec_diagnostics(prob, zf, holdout=holdout_half, extras=False)
    sph = sphere_diagnostics(prob, zf, exchange_radii(model.R0, model.R0 * 2.0 ** -6, r_max_h))
    tf = two_family_summary(sdh, sdh_half, sph); T["half_offset_and_spheres"] = time.time() - t; t = time.time()
    mx = local_maxima_omega(model, zf, c_l, omega); T["local_maxima_omega"] = time.time() - t; t = time.time()
    if mx:
        tSh, tSh_checks = tier_S(sdh, located_lambda_max=mx[0].get("lambda_max_S"))
    guh = sdh["guards"]; corer = None
    if mx:
        maxOm = max([guh["N2_max_abs_Omega"]] + [m_["abs_Omega"] for m_ in mx])
        ystar = mx[max(range(len(mx)), key=lambda i: mx[i]["abs_Omega"])]["y"]
        corer = core_resolution(prob, zf, c_l, omega, ystar, guh["N4_max_U"], maxOm, core_ball_radius=sdh["shells"]["edges"][0][1])
    T["core_resolution"] = time.time() - t
    g = sd["global_"]; n = sd["nonaxi"]; gu = sd["guards"]
    st = tf.get("structure") or sdh.get("structure") or {}
    B = dict(c_l=c_l, omega=omega, R0=float(model.R0), N_core=n["N_core"], e_core=n["e_core"], N_F=n["N_F"], e_F=n["e_F"], max_U=gu["N4_max_U"], r_core=gu["N4_r_core"], r_tail=gu["N5_r_tail"],
             rho_u_max=g["rho_u_max"], rho_u_max_holdout=sdh["global_"]["rho_u_max"], lambda_max_S=gu["N2_lambda_max_S"], tier_S=bool(tS), tier_S_holdout=bool(tSh),
             tier_S_checks=tS_checks, tier_S_checks_holdout=tSh_checks, U_L2_r_lt_1=st.get("U_L2_r_lt_1"), U_L2_r_lt_1_training=(sd.get("structure") or {}).get("U_L2_r_lt_1"),
             a_max=tf.get("a_max_std"), a_max_half=tf.get("a_max_half"), sigma_u_max=tf.get("sigma_u_max_std"), sigma_Om=tf.get("sigma_Om"),
             r_at_Omega_max_grid=diag["strain"]["r_at_Omega_max"], r_peak_Omega=diag["core"]["r_peak_Omega"], N_core_holdout=sdh["nonaxi"]["N_core"], e_core_holdout=sdh["nonaxi"]["e_core"],
             located_max_r=(mx[0]["r"] if mx else None), located_max_abs_Omega=(mx[0]["abs_Omega"] if mx else None), n_local_maxima=len(mx),
             holdout_edges=holdout.edges, innermost_resolved_shell=holdout.edges[0], gauge=cfg.get("gauge", "F") or "F", F_norm2=(sd.get("global_integrals") or {}).get("F_norm2"), F_norm_check=gauge_norm(prob, model, zf),
             F_norm2_from_coefficients=gauge_norm2(prob, model, zf))
    if corer is not None and "a_eff" in corer:
        srcs_c = {"dyadic shells (a_max_std)": B["a_max"], "half-offset shells (a_max_half)": B["a_max_half"], "core ball, weight at the centre (a_max_added_centre)": corer["a_max_added_centre"]}
        srcs_u = {"dyadic shells (a_max_std)": B["a_max"], "half-offset shells (a_max_half)": B["a_max_half"], "core ball, weight at the outer radius (a_max_added_upper)": corer["a_max_added_upper"]}
        B["a_max_core_source"] = max((k for k in srcs_c if srcs_c[k] is not None), key=lambda k: srcs_c[k]); B["a_max_core_upper_source"] = max((k for k in srcs_u if srcs_u[k] is not None), key=lambda k: srcs_u[k])
        B["a_max_core_candidates"] = dict(centre=srcs_c, upper=srcs_u, core_balls=corer.get("balls"))
        B.update(a_eff=corer["a_eff"], r_star=corer["r_star"], core_resolved=bool(corer["core_resolved"]), core_doubling_change_max=corer["max_doubling_rel_change"], core_ball_over_a_eff=corer["core_ball_over_a_eff"],
                 a_max_core=max([v for v in (B["a_max"], B["a_max_half"], corer["a_max_added_centre"]) if v is not None]),
                 a_max_core_upper=max([v for v in (B["a_max"], B["a_max_half"], corer["a_max_added_upper"]) if v is not None]),
                 sigma_u_max_core=max([v for v in (B["sigma_u_max"], tf.get("sigma_u_max_half"), corer["sigma_u_max_added"]) if v is not None]))
    else:
        B.update(a_eff=None, core_resolved=None, a_max_core=None, a_max_core_upper=None, core_note="no located |Omega| maximum: the core-resolution sets were not evaluated (as in the worker)")
    B["seconds_per_item"] = T; B["battery_seconds"] = sum(T.values())
    log("  battery: " + ", ".join(f"{k} {v:.0f} s" for k, v in T.items()) + f"; N_core {B['N_core']:.3f} N_F {B['N_F']:.3f} e_core {B['e_core']:.3f} e_F {B['e_F']:.4f} max_U {B['max_U']:.4f} U_L2 {B['U_L2_r_lt_1']} a_max_core {B['a_max_core']} / {B['a_max_core_upper']} core_resolved {B['core_resolved']} rho_u_max {B['rho_u_max']:.4e} F_norm {B['F_norm_check']:.12f}")
    return B, holdout


def battery_from_record(rec, model, cfg, prob, zf):
    """The same fields read from the worker's end-of-run record (start_result of results.jsonl)."""
    st = rec.get("structure") or {}
    holdout = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
    pf = rec.get("params_final") or {}
    B = dict(c_l=pf.get("c_l", rec.get("c_l")), omega=pf.get("omega", rec.get("omega")), R0=float(model.R0),
             N_core=rec.get("N_core"), e_core=rec.get("e_core"), N_F=rec.get("N_F"), e_F=rec.get("e_F"), max_U=rec.get("max_U"), r_core=rec.get("r_core"), r_tail=rec.get("r_tail"),
             rho_u_max=rec.get("rho_u_max"), rho_u_max_holdout=rec.get("rho_u_max_holdout"), lambda_max_S=rec.get("lambda_max_S"), tier_S=rec.get("tier_S"), tier_S_holdout=rec.get("tier_S_holdout"),
             U_L2_r_lt_1=st.get("U_L2_r_lt_1"), a_max=rec.get("a_max"), a_max_half=rec.get("a_max_half"), sigma_u_max=rec.get("sigma_u_max"), sigma_Om=rec.get("sigma_Om"),
             r_peak_Omega=rec.get("r_peak_Omega"), N_core_holdout=rec.get("N_core_holdout"), e_core_holdout=rec.get("e_core_holdout"),
             located_max_r=rec.get("located_max_r"), located_max_abs_Omega=rec.get("located_max_abs_Omega"), n_local_maxima=None,
             a_eff=rec.get("a_eff"), r_star=rec.get("r_star"), core_resolved=rec.get("core_resolved"), core_doubling_change_max=rec.get("core_doubling_change_max"), core_ball_over_a_eff=rec.get("core_ball_over_a_eff"),
             a_max_core=rec.get("a_max_core"), a_max_core_upper=rec.get("a_max_core_upper"), sigma_u_max_core=rec.get("sigma_u_max_core"),
             holdout_edges=holdout.edges, innermost_resolved_shell=holdout.edges[0], gauge=rec.get("gauge", "F"), F_norm2=rec.get("F_norm2"), F_norm_check=gauge_norm(prob, model, zf),
             F_norm2_from_coefficients=gauge_norm2(prob, model, zf), battery_set=rec.get("battery_set"), t_battery_s=rec.get("t_battery_s"))
    return B, holdout


def compare_batteries(B_rec, B_full):
    rows = {}; agree = bool(B_rec) and bool(B_full)                            # lead 18:49:47Z item 1 (e): both sides nonempty
    for k in BATTERY_NUMERIC_FIELDS:
        a_, b_ = fin(B_rec.get(k)), fin(B_full.get(k))
        if a_ is None or b_ is None:                                           # V411 item 3: a missing or non-finite value on either side is a disagreement (missing equals missing is not agreement)
            rows[k] = dict(record=B_rec.get(k), recomputed=B_full.get(k), agree=False, note="missing or not finite"); agree = False; continue
        rel = abs(a_ - b_) / max(abs(a_), abs(b_), 1e-300); ok = rel <= TH["full_compare_rel"]
        rows[k] = dict(record=a_, recomputed=b_, rel_diff=rel, agree=ok); agree = agree and ok
    for k in BATTERY_FLAG_FIELDS:
        va, vb = B_rec.get(k), B_full.get(k)
        ok = isinstance(va, bool) and isinstance(vb, bool) and (va == vb); rows[k] = dict(record=va, recomputed=vb, agree=ok, note=(None if ok else "flags must be genuine booleans and equal")); agree = agree and ok
    return dict(rule="lead 18:22:07Z item 4: every battery field read from the run record against the recomputed value, 1e-10 relative; flags exactly; V411 item 3: missing or non-finite values and non-boolean flags disagree", all_agree=bool(agree and len(rows) == len(BATTERY_NUMERIC_FIELDS) + len(BATTERY_FLAG_FIELDS)), fields=rows,
                disagreeing=[k for k, v in rows.items() if v["agree"] is False])


# ----------------------------------------------------------------------------------------------------------------------------- run path (6.3 (b) run-based items, 5.3 counter)
def run_path(rec):
    tr = rec.get("trajectory") or []
    acc = [t for t in tr if t.get("accepted")]
    om = [fin(t["omega"]) for t in acc if fin(t.get("omega")) is not None]; cl = [fin(t["c_l"]) for t in acc if fin(t.get("c_l")) is not None]
    p0 = rec.get("params_initial") or {}
    if fin(p0.get("omega")) is not None and fin(p0.get("c_l")) is not None:
        om = [fin(p0["omega"])] + om; cl = [fin(p0["c_l"])] + cl
    def sat(c, w):
        return (min(c - 0.4, 0.5 - c) < TH["saturation_edge"]) or (w < TH["omega_lo"]) or (w > TH["omega_hi"])
    cnt = 0
    for c, w in zip(reversed(cl), reversed(om)):
        if sat(c, w):
            cnt += 1
        else:
            break
    mono = bool(len(om) > 1 and all(b <= a for a, b in zip(om[:-1], om[1:])))
    ok = bool(om) and om[0] > 0
    return dict(n_accepted=len(acc), n_omega_values=len(om), omega_first=om[0] if om else None, omega_last=om[-1] if om else None, omega_min=min(om) if om else None, omega_max=max(om) if om else None,
                omega_monotone_decreasing=(mono if ok else None), omega_last_over_first=(om[-1] / om[0] if ok else None),
                omega_tenfold_monotone_decrease=((mono and om[-1] / om[0] < 1.0 / TH["omega_decrease_factor"]) if ok else None),
                saturation_consecutive_flags_at_end=(cnt if om else None), saturation_stop=rec.get("saturation_stop"), stop_reason=rec.get("stop_reason") or rec.get("status"),
                c_l_min=min(cl) if cl else None, c_l_max=max(cl) if cl else None)


# ----------------------------------------------------------------------------------------------------------------------------- judgement
def judge(B, G5, RP, SP, path, ref, ref_tag, state=None):
    ex = []; fl = []; open_ = []; state = state or {}
    def add(lst, item, value, limit, raised, note=None, rule=None):
        if raised is None:
            open_.append(item + (f" [{note}]" if note else ""))
        lst.append(dict(item=item, value=value, limit=limit, raised=(None if raised is None else bool(raised)), note=note, rule=rule))
    refb = (ref or {}).get("battery") if ref else None
    refs = ((ref or {}).get("spectra") or {}).get("per_block") if ref else None
    # gauge and reference validity (V411 item 2): finite F-gauge norm within F_norm_tol of 1 for the state and the start reference, gauge F, reference marked and projected
    nf2 = fin(B.get("F_norm2_from_coefficients")); gauge_ok = (B.get("gauge") == "F")
    g_ok = (nf2 is not None and abs(nf2 - 1.0) <= TH["F_norm2_tol"] and gauge_ok and state.get("F_projected") is True)
    add(ex, f"(gauge) |F_norm2 - 1| <= {TH['F_norm2_tol']:.0e} from the coefficients of the state the battery uses (gauge F; required for comparability, not an exclusion)", dict(F_norm2=nf2, gauge=B.get("gauge"), F_projected=state.get("F_projected")), TH["F_norm2_tol"],
        (False if g_ok else None), note=(None if g_ok else "state not in the F-gauge within tolerance, gauge not F, or projection not applied"), rule="lead 18:49:47Z item 1 (b) (from the coefficients), tolerance 1e-8 accepted 19:02:50Z item 2; V411 item 2")
    if ref is not None:
        rnf2 = fin((refb or {}).get("F_norm2_from_coefficients")); rst = ref.get("state") or {}
        fnp, fn2p = fin(rst.get("F_norm_projected")), fin(rst.get("F_norm2_projected"))
        norms_consistent = (fnp is not None and fn2p is not None and rnf2 is not None and abs(fnp * fnp - fn2p) <= 1e-12 * max(1.0, fn2p) and abs(fn2p - rnf2) <= 1e-12 * max(1.0, rnf2))   # V422: the norm fields agree with each other
        r_ok = (ref.get("is_start_reference") is True and rst.get("F_projected") is True and rnf2 is not None and abs(rnf2 - 1.0) <= TH["F_norm2_tol"] and (refb or {}).get("gauge") == "F" and fin(rst.get("F_norm_raw")) is not None and norms_consistent)
        add(ex, "(gauge) start reference marked, projected, carrying both norms and within 1e-12 of the F-gauge (required for the ratios, not an exclusion)", dict(tag=ref_tag, is_start_reference=ref.get("is_start_reference"), F_projected=rst.get("F_projected"), F_norm2=rnf2, F_norm_raw=rst.get("F_norm_raw"), F_norm_projected=rst.get("F_norm_projected"), gauge=(refb or {}).get("gauge")), TH["F_norm2_tol"],
            (False if r_ok else None), note=(None if r_ok else "start reference not marked, not projected, norms missing, or not within tolerance of the F-gauge"), rule="lead 18:49:47Z item 1 (b); 19:02:50Z item 2; V411 item 2")
        if not r_ok:
            refb = None                                                         # an invalid reference gives no ratios: the ratio items become OPEN below
    badf = [k for k in NONNEG_FIELDS if k in B and B.get(k) is not None and (fin(B.get(k)) is None or fin(B.get(k)) < 0)]
    missf = [k for k in NONNEG_FIELDS[:12] if B.get(k) is None]
    if badf or missf:
        open_.append(f"battery: norms or maxima not finite/non-negative {badf}; missing {missf}")                   # lead 19:35:33Z (f)
    # (a) Tier S nontriviality warnings
    for k in ("N_core", "N_F", "e_core", "e_F"):
        v = fin(B.get(k))
        add(ex, f"(a) {k} < {TH[k]:.0e}", B.get(k), TH[k], None if v is None else v < TH[k], note=(None if v is not None else "value missing or not finite"), rule="6.3 (a): Tier S nontriviality warning (collapse toward axisymmetry)")
    # (b) collapse of the core: max|U| and ||U||_L2(|y|<1), F-gauge, ratio to the F-projected start reference
    for k, lab in (("max_U", "max|U|"), ("U_L2_r_lt_1", "||U||_L2(|y|<1)")):
        v = fin(B.get(k)); r0 = pos((refb or {}).get(k)) if refb else None
        if v is None:
            add(ex, f"(b) {lab} / start < {TH['collapse_ratio']}", dict(state=B.get(k), start=(refb or {}).get(k)), TH["collapse_ratio"], None, note="state value missing or not finite")
        elif r0 is None:
            add(ex, f"(b) {lab} / start < {TH['collapse_ratio']}", dict(state=v, start=(refb or {}).get(k)), TH["collapse_ratio"], None, note="start reference missing or not a valid denominator")
        else:
            rat = v / r0
            add(ex, f"(b) {lab} / start < {TH['collapse_ratio']}", dict(state=v, start=r0, ratio=rat, start_reference=ref_tag), TH["collapse_ratio"], rat < TH["collapse_ratio"], rule="6.3 (a): collapse of the core toward zero velocity (F-gauge; start reference F-projected)")
    # (c) saturation flag of 5.3 at the state and the run's consecutive counter
    c, w = fin(B.get("c_l")), fin(B.get("omega"))
    if c is None or w is None:
        add(ex, "(c) 5.3 saturation flag at the state", dict(c_l=B.get("c_l"), omega=B.get("omega")), None, None, note="parameters missing"); m = None
    else:
        m = min(c - 0.4, 0.5 - c); satf = (m < TH["saturation_edge"]) or (w < TH["omega_lo"]) or (w > TH["omega_hi"])
        add(ex, "(c) 5.3 saturation flag at the state", dict(min_cl_distance=m, omega=w, consecutive_flags_at_end=(path or {}).get("saturation_consecutive_flags_at_end"), saturation_stop=(path or {}).get("saturation_stop")),
            dict(cl_distance=TH["saturation_edge"], omega=[TH["omega_lo"], TH["omega_hi"]]), satf, rule="5.3")
    # (d) near-edge label of 5.4 (excluded here: v1.21 (d) evidence OPEN, 6.2)
    add(ex, "(d) 5.4 near-edge label (min(c_l - 0.4, 0.5 - c_l) < 0.02)", m, TH["near_edge"], None if m is None else m < TH["near_edge"], note=(None if m is not None else "parameters missing"), rule="6.3 (a) with 6.2: the v1.21 (d) evidence is OPEN here, so the label excludes")
    # (e) core resolved (v1.21 (c))
    cr = B.get("core_resolved")
    add(ex, "(e) core unresolved (v1.21 (c))", cr, True, (not cr) if isinstance(cr, bool) else None, note=(None if isinstance(cr, bool) else "core_resolved not evaluated"), rule="6.3 (a): core_resolved false excludes")
    # (f) rho_P^max with the accuracy rule (V411 item 1: the decision is recomputed here from the finite quantities, the status string is not trusted), and G5
    RP = RP or {}
    shells = RP.get("rho_P_shells") or []; nsh = RP.get("n_shells")
    def arr_ok(a_):
        return isinstance(a_, list) and isinstance(nsh, int) and nsh > 0 and len(a_) == nsh and all(fin(v) is not None and fin(v) >= 0 for v in a_)
    shells_ok = arr_ok(shells)
    rp_arr = max(fin(v) for v in shells) if shells_ok else None; rp_rec = fin(RP.get("rho_P_max"))
    rp = rp_arr if (rp_arr is not None and rp_rec is not None and abs(rp_arr - rp_rec) <= 1e-12 * max(1.0, abs(rp_arr))) else None   # V416: the maximum must agree with the array
    eps0 = fin(RP.get("eps")); keys_exp = [f"{e:.0e}" for e in (1e-3, 2e-3, 4e-3)]
    ladder = RP.get("ladder") or {}; lad_ok = (eps0 == 1e-3 and isinstance(ladder, dict) and sorted(ladder) == sorted(keys_exp))
    lv = []
    if lad_ok:
        for k_ in keys_exp:                                                       # V422: every ladder entry carries its finite shell array and a consistent maximum
            ent = ladder.get(k_) or {}; sh_ = ent.get("rho_P_shells")
            if not arr_ok(sh_) or fin(ent.get("rho_P_max")) is None or abs(max(fin(v) for v in sh_) - fin(ent["rho_P_max"])) > 1e-12 * max(1.0, fin(ent["rho_P_max"])):
                lad_ok = False; break
            lv.append(fin(ent["rho_P_max"]))
        if lad_ok and (rp is None or abs(lv[0] - rp) > 1e-12 * max(1.0, rp)):
            lad_ok = False                                                        # V422: the ladder's base value is the reported maximum
    delta = abs(lv[1] - lv[0]) if lad_ok else None; delta4 = abs(lv[2] - lv[1]) if lad_ok else None
    d_rec = fin(RP.get("delta")); delta_ok = (delta is not None and d_rec is not None and abs(delta - d_rec) <= 1e-12 * max(1.0, delta))
    if lad_ok:
        for k_ in keys_exp:                                                       # lead 19:35:33Z (b): each detailed entry's eps equals its key; the summary equals the detailed base
            if fin((ladder.get(k_) or {}).get("eps")) is None or abs(fin(ladder[k_]["eps"]) - float(k_)) > 1e-12 * float(k_):
                lad_ok = False
        summ = RP.get("ladder_rho_P_max")
        if isinstance(summ, dict) and (sorted(summ) != sorted(keys_exp) or any(fin(summ.get(k_)) is None or abs(fin(summ[k_]) - fin(ladder[k_]["rho_P_max"])) > 1e-12 * max(1.0, fin(ladder[k_]["rho_P_max"])) for k_ in keys_exp)):
            lad_ok = False
    edges_b = B.get("holdout_edges"); edges_p = RP.get("shell_edges")
    def edges_equal(a_, b_):
        try:
            return isinstance(a_, list) and isinstance(b_, list) and len(a_) == len(b_) and all(abs(float(x[0]) - float(y[0])) <= 1e-12 * max(1.0, abs(float(y[0]))) and abs(float(x[1]) - float(y[1])) <= 1e-12 * max(1.0, abs(float(y[1]))) for x, y in zip(a_, b_))
        except Exception:
            return False
    ct = RP.get("construction_test") or {}; ct_e = fin(ct.get("max_e"))
    per_sh = ct.get("per_shell") or {}; degs = ct.get("degrees") or []; ct_vals = []
    Lf = RP.get("Lf")
    ct_complete = (fin(ct.get("eps_test")) == TH["eps_test"] and isinstance(per_sh, dict) and isinstance(nsh, int) and len(per_sh) == nsh and isinstance(degs, list) and isinstance(Lf, int)
                   and degs == list(range(Lf + 1)) and not ct.get("skipped") and edges_equal(edges_p, edges_b) and isinstance(edges_b, list) and len(edges_b) == nsh)   # lead 19:35:33Z (a)
    if ct_complete:
        for k_ in range(nsh):
            ent = per_sh.get(str(k_)) or {}; row = ent.get("e_by_degree") or {}
            lo_, hi_ = float(edges_b[k_][0]), float(edges_b[k_][1]); a_k = math.sqrt(max(lo_, hi_ / 64.0) * hi_)     # the registered convention (19:35:33Z item 2)
            if not edges_equal([ent.get("shell")], [edges_b[k_]]) or fin(ent.get("a_k")) is None or abs(fin(ent["a_k"]) - a_k) > 1e-12 * a_k or sorted(int(x) for x in row) != degs:
                ct_complete = False; break
            for l_ in degs:
                v = fin(row.get(str(l_)))
                if v is None or v < 0:
                    ct_complete = False; break
                ct_vals.append(v)
            if not ct_complete:
                break
    ct_max = max(ct_vals) if (ct_complete and ct_vals) else None
    ct_pass = (ct_complete and ct_max is not None and ct_max <= TH["rho_P_accuracy_open"] and ct.get("passed") is True and ct_e is not None and abs(ct_e - ct_max) <= 1e-12 * max(1.0, ct_max))   # V422: recomputed from the per-shell per-degree errors
    err_a = ct_max; chg_b = delta; cov_ok = ct_complete
    if rp is None or not shells_ok or not lad_ok or not delta_ok or not ct_pass or delta4 is None:
        st_ = "OPEN: construction test not passed or skipped shells, or rho_P_max, a shell value, the ladder values or Delta not finite/consistent"; raised_rp = None
    elif delta > TH["rho_P_accuracy_open"]:
        st_ = f"OPEN: ladder change Delta {delta:.2e} above {TH['rho_P_accuracy_open']:.0e}"; raised_rp = None
    elif rp + delta <= TH["rho_P"]:
        st_ = "cleared"; raised_rp = False
    elif rp - delta > TH["rho_P"]:
        st_ = "exclusion: rho_P_max(eps) - Delta above 1e-3"; raised_rp = True
    else:
        st_ = "OPEN: rho_P_max within Delta of the threshold"; raised_rp = None
    st_rec = RP.get("status")
    if not isinstance(st_rec, str) or not st_rec.startswith(("cleared", "exclusion", "OPEN")):
        st_ = f"OPEN: pressure status missing or unrecognized ({st_rec!r})"; raised_rp = None            # lead 19:35:33Z (e)
    elif raised_rp is not None and not st_rec.startswith("cleared" if raised_rp is False else "exclusion"):
        st_ = f"OPEN: the recorded status {st_rec!r} disagrees with the recomputed decision {st_!r}"; raised_rp = None
    add(ex, f"(f) rho_P_max(eps) - Delta > {TH['rho_P']:.0e} (lead 19:02:50Z item 1 rule)", dict(rho_P_max=rp, delta=delta, delta_4eps=delta4, ratio_successive_changes=(delta4 / delta if (delta and delta4 is not None) else None), construction_test_max_e_recomputed=ct_max, construction_test_max_e_in_record=ct_e,
                                                                                     construction_test_passed_in_record=ct.get("passed"), construction_test_complete=ct_complete, construction_test_skipped=ct.get("skipped"), rho_P_proj_max=(RP or {}).get("rho_P_proj_max"), status=st_, status_in_record=(RP or {}).get("status"), shells_valid=shells_ok, ladder_valid=lad_ok), TH["rho_P"], raised_rp,
        note=(st_ if raised_rp is None else None), rule="6.3 (a) pressure consistency; lead 19:02:50Z item 1: empirical accuracy gate, not a bound")
    G5 = G5 or {}
    ga = G5.get("G5a_best_rel_per_group") or {}; gb = G5.get("G5b_div_rel_max") or {}; gc = fin(G5.get("G5c_source_consistency_rel"))
    ga_vals = [fin(v) for v in ga.values()] if isinstance(ga, dict) and ga else []; gb_vals = [fin(v) for v in gb.values()] if isinstance(gb, dict) and gb else []
    a_num = (all(v is not None and v >= 0 for v in ga_vals) and max(ga_vals) <= TH["G5a"]) if ga_vals else None          # V422: (a), (b), (c) recomputed from the recorded numbers
    b_num = (all(v is not None and v >= 0 for v in gb_vals) and max(gb_vals) <= TH["G5b"]) if gb_vals else None
    c_num = (gc >= 0 and gc <= TH["G5c"]) if gc is not None else None
    comps = [G5.get("G5a_PASS"), G5.get("G5b_PASS"), G5.get("G5c_second_part_PASS")]
    keys_ok = (isinstance(ga, dict) and sorted(ga) == sorted(G5A_GROUPS) and isinstance(gb, dict) and sorted(gb) == sorted(G5B_KEYS))     # lead 19:35:33Z (c): exactly the registered groups
    comps_ok = keys_ok and isinstance(G5.get("G5_pass"), bool) and all(isinstance(c_, bool) for c_ in comps) and None not in (a_num, b_num, c_num) and comps == [a_num, b_num, c_num]
    g5p = (a_num and b_num and c_num) if comps_ok else None
    g5_consistent = (g5p == G5.get("G5_pass")) if g5p is not None else None
    add(ex, "(f) G5 at the state fails", dict(G5a=comps[0], G5b=comps[1], G5c_second_part=comps[2], combined_in_record=(G5 or {}).get("G5_pass"), combined_recomputed=g5p, consistent=g5_consistent, error=(G5 or {}).get("error")), True,
        (not g5p) if (isinstance(g5p, bool) and g5_consistent) else None, note=(None if (isinstance(g5p, bool) and g5_consistent) else "G5 at the state not run, a component not a boolean, or the combined value inconsistent"), rule="6.3 (a): G5 (a), (b), (c) second part at the state")
    # (g) rho_u^max below start and a_max on the core-resolved sets above 2 x start (either weight; lead 17:55:21Z item 2)
    ru, ac, au = fin(B.get("rho_u_max")), fin(B.get("a_max_core")), fin(B.get("a_max_core_upper"))
    ru0, ac0, au0 = (pos((refb or {}).get("rho_u_max")), pos((refb or {}).get("a_max_core")), pos((refb or {}).get("a_max_core_upper"))) if refb else (None, None, None)
    vals = dict(rho_u_max=ru, rho_u_max_start=ru0, a_max_core=ac, a_max_core_start=ac0, a_max_core_upper=au, a_max_core_upper_start=au0, start_reference=ref_tag)
    if None in (ru, ac, au):
        add(ex, "(g) rho_u_max below start and a_max_core (either weight) above 2 x start", vals, TH["a_max_factor"], None, note="state values missing (rho_u_max, a_max_core, a_max_core_upper)")
    elif None in (ru0, ac0, au0):
        add(ex, "(g) rho_u_max below start and a_max_core (either weight) above 2 x start", vals, TH["a_max_factor"], None, note="start reference values missing or not valid denominators")
    else:
        vals.update(rho_u_decreased=ru < ru0, ratio_centre=ac / ac0, ratio_upper=au / au0)
        add(ex, "(g) rho_u_max below start and a_max_core (either weight) above 2 x start", vals, TH["a_max_factor"], (ru < ru0) and (ac > TH["a_max_factor"] * ac0 or au > TH["a_max_factor"] * au0),
            rule="6.3 (a) with v1.21 (b), v1.22 (c); lead 17:55:21Z item 2: either core weight above 2 x its start value while rho_u^max is below its start value")
    # 6.3 (b) flags
    add(fl, f"omega < {TH['omega_flag']}", w, TH["omega_flag"], None if w is None else w < TH["omega_flag"], note=(None if w is not None else "omega missing"))
    if path is None:
        add(fl, "omega decreasing monotonically by more than a factor 10 during the run", None, TH["omega_decrease_factor"], None, note="start reference: no run path (not applicable)")
    else:
        td = path.get("omega_tenfold_monotone_decrease")
        add(fl, "omega decreasing monotonically by more than a factor 10 during the run", dict(first=path["omega_first"], last=path["omega_last"], monotone=path["omega_monotone_decreasing"], last_over_first=path["omega_last_over_first"]), TH["omega_decrease_factor"],
            td if isinstance(td, bool) else None, note=(None if isinstance(td, bool) else "omega path missing"))
    ae, ae0 = fin(B.get("a_eff")), (pos((refb or {}).get("a_eff")) if refb else None)
    add(fl, "a_eff decreasing by more than a factor 2 (ratio to the start reference)", dict(state=ae, start=ae0, ratio=(ae / ae0 if (ae is not None and ae0) else None)), TH["a_eff_factor"],
        (ae < ae0 / TH["a_eff_factor"]) if (ae is not None and ae0) else None, note=(None if (ae is not None and ae0) else "a_eff at the state or a valid start value missing"))
    per = SP.get("per_block") or {}; expected = SP.get("expected_blocks"); layout = SP.get("layout")
    active = [str(x[0]) for x in layout if isinstance(x, (list, tuple)) and len(x) == 2 and isinstance(x[1], int) and x[1] >= 2] if isinstance(layout, list) else None
    if not isinstance(expected, list) or not expected or active is None or expected != active:                    # lead 19:35:33Z (d): the inventory equals the active blocks of the recorded layout
        open_.append(f"spectra: expected active-block inventory missing or not equal to the active blocks of the recorded layout ({expected} vs {active})"); expected = []
    missing_blocks = [nm for nm in expected if nm not in per]
    for nm in expected:                                                               # V411 item 4: every expected active block needs a finite last-two ratio, else OPEN for that block
        x = fin((per.get(nm) or {}).get("last2_over_max"))
        add(fl, f"top two radial coefficients of block {nm} above 0.1 of the block maximum", dict(block=nm, last2_over_max=x, n_k=(per.get(nm) or {}).get("n_k")), TH["top2_ratio"],
            None if x is None else x > TH["top2_ratio"], note=(None if x is not None else "ratio missing or not finite for an expected active block"))
    if missing_blocks:
        open_.append("spectra: expected active blocks without entries " + str(missing_blocks))
    for nm in expected:
        v = per.get(nm) or {}
        x = fin(v.get("top_fraction")); x0 = fin((refs or {}).get(nm, {}).get("top_fraction")) if refs else None
        if x is None:
            add(fl, f"N6 radial part, block {nm}: top {v.get('top_modes')} of {v.get('n_k')} modes above twice its start value", dict(state=None), TH["N6_factor"], None, note="state fraction missing or not finite")
        elif x0 is None:
            add(fl, f"N6 radial part, block {nm}: top {v['top_modes']} of {v['n_k']} modes above twice its start value", dict(state=x, start=None), TH["N6_factor"], None, note="start reference value missing")
        elif x0 < TH["N6_start_floor"]:
            add(fl, f"N6 radial part, block {nm}: top {v['top_modes']} of {v['n_k']} modes above twice its start value", dict(state=x, start=x0), TH["N6_factor"], None, note="start fraction below 1e-14: no defined ratio (lead 18:22:07Z item 2)")
        else:
            add(fl, f"N6 radial part, block {nm}: top {v['top_modes']} of {v['n_k']} modes above twice its start value", dict(state=x, start=x0, ratio=x / x0), TH["N6_factor"], x > TH["N6_factor"] * x0)
    R0 = fin(B.get("R0")); lo = fin((B.get("innermost_resolved_shell") or [None, None])[1])
    rv = fin(B.get("located_max_r")); src = "located |Omega| maximum (critical-point search)"
    if rv is None:
        rv = fin(B.get("r_at_Omega_max_grid")); src = "grid maximum of |Omega| (training grid)"
    hi = (2.0 ** TH["r_vorticity_max_octaves"]) * R0 if R0 is not None else None
    add(fl, "vorticity maximum at radius above 2^8 R0 or inside the innermost resolved shell", dict(r=rv, source=(src if rv is not None else None), innermost_shell_outer_edge=lo, R0=R0, limit_high=hi), dict(low=lo, high=hi),
        None if (rv is None or lo is None or hi is None) else (rv > hi or rv < lo), note=(None if (rv is not None and lo is not None and hi is not None) else "vorticity maximum location, R0 or shell edge missing"))
    rt, rt0 = fin(B.get("r_tail")), (pos((refb or {}).get("r_tail")) if refb else None)
    add(fl, "r_tail increasing by more than a factor 4 (ratio to the start reference)", dict(state=rt, start=rt0, ratio=(rt / rt0 if (rt is not None and rt0) else None)), TH["r_tail_factor"],
        (rt > TH["r_tail_factor"] * rt0) if (rt is not None and rt0) else None, note=(None if (rt is not None and rt0) else "r_tail at the state or a valid start value missing"))
    any_ex = any(e["raised"] is True for e in ex); any_fl = any(f["raised"] is True for f in fl)
    undecided = sorted(set(open_))
    return ex, fl, undecided, any_ex, any_fl


def decide_record(B, G5, RP, SP, path, refs, state):
    """The decision on a record's components against its start references (an item raised against ANY reference counts; the open items carry the reference tag).
    Used by main() and by the wrapper scripts/r63a_decide.py (lead 19:35:33Z item 1 (g))."""
    if refs:
        ex = []; fl = []; open_ = []; any_ex = False; any_fl = False
        for rf_ in refs:
            e_, f_, o_, ae_, af_ = judge(B, G5, RP, SP, path, rf_, rf_.get("tag"), state=state)
            for it_ in e_ + f_:
                it_["reference"] = rf_.get("tag")
            ex += e_; fl += f_; open_ = sorted(set(open_) | set(f"[{rf_.get('tag')}] {o}" for o in o_)); any_ex = any_ex or ae_; any_fl = any_fl or af_
        return ex, fl, open_, any_ex, any_fl
    return judge(B, G5, RP, SP, path, None, None, state=state)


def ref_summary(ref, path):
    b = ref.get("battery") or {}
    return dict(path=os.path.relpath(path, ROOT), sha256=sha(path), tag=ref.get("tag"), version=ref.get("version"), tool_sha256=ref.get("script_sha256"), is_start_reference=ref.get("is_start_reference"), c_l=b.get("c_l"), omega=b.get("omega"),
                gauge_projected=(ref.get("state") or {}).get("F_projected"), F_norm2_from_coefficients=b.get("F_norm2_from_coefficients"), values=dict(max_U=b.get("max_U"), U_L2_r_lt_1=b.get("U_L2_r_lt_1"), rho_u_max=b.get("rho_u_max"), a_max_core=b.get("a_max_core"),
                                                                                     a_max_core_upper=b.get("a_max_core_upper"), a_eff=b.get("a_eff"), r_tail=b.get("r_tail"),
                                                                                     N6_per_block={k: v.get("top_fraction") for k, v in ((ref.get("spectra") or {}).get("per_block") or {}).items()}))


# ----------------------------------------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["start", "end"]); ap.add_argument("source"); ap.add_argument("--tag", required=True)
    ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--full", action="store_true")
    ap.add_argument("--start-ref", action="append", default=None, help="start-reference record(s); repeatable (lead 18:49:47Z item 3: F2 states against the F2 start and the S01 state)"); ap.add_argument("--segment-start", default=None); ap.add_argument("--eps", type=float, default=1e-3)
    ap.add_argument("--is-start-reference", action="store_true", help="mark the record as a lineage start reference (default for mode start)")
    a = ap.parse_args()
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, f"{a.tag}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    dev = torch.device(a.device); t_all = time.time()
    ref_paths = list(a.start_ref or []); refs = [json.load(open(rp_)) for rp_ in ref_paths]
    seg = json.load(open(a.segment_start)) if a.segment_start else None
    for rf_ in refs:
        if not rf_.get("is_start_reference"):
            log(f"  NOTE: the --start-ref record {rf_.get('tag')} is not marked as a start reference")
    state = dict(mode=a.mode)
    if a.mode == "start":
        job = json.load(open(a.source)); cfg = job["config"]
        model, prob = W.build(cfg, dev)
        rng = np.random.default_rng(int(cfg.get("seed", 0)) * 1000003 + 0)                        # run_job: rng_seed = seed * 1000003 + idx, idx 0
        zf, meta = W.load_start_state(cfg, model, prob, dev, log, rng)
        prob.pivot = prob.choose_pivot(zf)
        if model.free_params:
            prob.ensure_geometry(zf)
        zf = prob.phase_align(zf)
        tc = TailConstraints(model) if cfg.get("tail_constraints", True) else None; pm = ParamMap(free=bool(model.free_params))
        to_full = (lambda zo: tc.expand(pm.expand(zo))) if tc is not None else (lambda zo: pm.expand(zo))
        to_opt = (lambda z_: pm.reduce(tc.reduce(z_))) if tc is not None else (lambda z_: pm.reduce(z_))
        z_opt = to_opt(zf); z_raw = to_full(z_opt)
        nF_raw = gauge_norm(prob, model, z_raw)
        zf = z_raw.clone()
        if math.isfinite(nF_raw) and nF_raw > 1e-8:                                                 # the worker's F-gauge projection of its reported end states (worker_d6 'exact F-gauge projection')
            zf[: model.n_coef] = zf[: model.n_coef] / nF_raw
        nF_proj = gauge_norm(prob, model, zf); projected = bool(math.isfinite(nF_raw) and nF_raw > 1e-8); nF2_proj = gauge_norm2(prob, model, zf)
        meta = {k: v for k, v in meta.items() if not hasattr(v, "shape")}
        state_path = os.path.join(OUT_DIR, f"{a.tag}_state.pt"); raw_path = os.path.join(OUT_DIR, f"{a.tag}_state_raw.pt")
        common = dict(config=cfg, free_params=bool(model.free_params), meta=meta, job_file=os.path.abspath(a.source), job_sha256=sha(a.source), ts=now())
        torch.save(dict(z=z_raw.detach().cpu(), F_norm=nF_raw, kind="6.3 (a) record start reference, RAW: the lineage's initial state as its first FREE run began (worker load_start_state, pivot, geometry, phase alignment, constraint maps as in run_job), before the F-gauge projection", **common), raw_path)
        torch.save(dict(z=zf.detach().cpu(), F_norm=nF_proj, F_norm_raw=nF_raw, kind="6.3 (a) record start reference, F-PROJECTED: the raw start with the coefficients divided by its far-field norm (the worker's projection of reported end states); the battery and all ratios use this state", **common), state_path)
        state.update(source=os.path.abspath(a.source), job_id=job.get("job_id"), job_sha256=sha(a.source), state_file=os.path.relpath(state_path, ROOT), state_sha256=sha(state_path), raw_state_file=os.path.relpath(raw_path, ROOT),
                     raw_state_sha256=sha(raw_path), F_norm_raw=nF_raw, F_norm_projected=nF_proj, F_norm2_projected=nF2_proj, F_projected=projected, init_meta=meta, start_file=cfg.get("init_from"),
                     start_file_sha256=(sha(cfg["init_from"]) if cfg.get("init_from") and os.path.isfile(cfg["init_from"]) else None),
                     description="lineage start reference: the initial state of the first FREE run (job configuration and seed), F-gauge projected as the worker projects its reported end states; raw state kept beside it")
        log(f"  start reference: raw far-field norm {nF_raw:.12f}; projected {nF_proj:.12f}; projection applied {projected}")
        rec_run = None; is_ref = True
    else:
        run_dir = os.path.abspath(a.source); sp = os.path.join(run_dir, "starts", "start_000.pt"); rp = os.path.join(run_dir, "results.jsonl")
        S = torch.load(sp, map_location="cpu", weights_only=False); cfg = S["config"]
        rows = [json.loads(l) for l in open(rp) if l.strip()]; rec_run = [r for r in rows if r.get("kind") == "start_result"][-1]
        exp_dir = os.path.dirname(os.path.dirname(run_dir))                          # the experiment directory the run belongs to (zfile is relative to it)
        zabs = os.path.realpath(os.path.join(exp_dir, rec_run.get("zfile") or "")); sabs = os.path.realpath(sp)
        zrel = os.path.relpath(zabs, exp_dir); srel = os.path.relpath(sabs, exp_dir)
        if not rec_run.get("zfile") or zabs != sabs:
            raise SystemExit(f"REFUSED: the run record's zfile {rec_run.get('zfile')!r} is not the saved end state {srel} (V405 item 3)")
        model, prob = W.build(cfg, dev)
        zf = S["z"].to(dev)
        pf = rec_run.get("params_final") or {}
        for key, idx in (("c_l", -2), ("omega", -1)):
            v = fin(pf.get(key)); zv = float(zf[idx]) if model.free_params else float(cfg[key])
            if v is None or abs(v - zv) > 1e-12 * max(1.0, abs(zv)):
                raise SystemExit(f"REFUSED: the run record's params_final {key} {pf.get(key)} does not match the saved end state {zv!r} (V405 item 3)")
        if rec_run.get("iterations") is not None and S.get("iterations") is not None and int(rec_run["iterations"]) != int(S["iterations"]):
            raise SystemExit(f"REFUSED: iterations differ between the run record ({rec_run['iterations']}) and the saved end state ({S['iterations']})")
        prob.pivot = S.get("pivot") or prob.choose_pivot(zf)
        if model.free_params:
            prob.ensure_geometry(zf)
        state_path = sp
        state.update(source=run_dir, job_id=rec_run.get("job_id"), state_file=srel, state_sha256=sha(sp), run_record=os.path.relpath(rp, ROOT), run_record_sha256=sha(rp), run_record_ts=rec_run.get("ts"),
                     run_record_zfile=zrel, iterations=rec_run.get("iterations"), stop_reason=rec_run.get("stop_reason") or rec_run.get("status"), label=rec_run.get("label"),
                     params_initial=rec_run.get("params_initial"), params_final=pf, F_projected=bool(abs(gauge_norm2(prob, model, zf) - 1.0) <= TH["F_norm2_tol"]), F_norm_check=gauge_norm(prob, model, zf), F_norm2_from_coefficients=gauge_norm2(prob, model, zf),
                     binding="the run record names this state file as its zfile, its params_final equal the saved parameters to 1e-12 relative, and its iteration count equals the saved one",
                     description="end state of the run (the worker's start_000.pt, F-gauge projected by the worker)")
        is_ref = a.is_start_reference
    if int(zf.numel()) != int(model.n_z):
        raise SystemExit(f"REFUSED: the state vector has {zf.numel()} entries, the model expects {model.n_z} (V416)")
    c_l, omega = (float(zf[-2]), float(zf[-1])) if model.free_params else (float(cfg["c_l"]), float(cfg["omega"]))   # V416: FIXED vectors carry coefficients only
    state.update(c_l=c_l, omega=omega, free_params=bool(model.free_params), z_sha256=hashlib.sha256(zf.detach().cpu().numpy().tobytes()).hexdigest(), n_z=int(zf.numel()), R0=float(model.R0))
    log(f"{a.mode} {a.tag}: state at (c_l, omega) = ({c_l:.6f}, {omega:.6f}), n_z {zf.numel()}, R0 {float(model.R0)}, device {dev}")
    # battery
    compare = None
    if a.mode == "start":
        B, holdout = full_battery(prob, model, zf, cfg); prov = dict(source=PROV_START, items=list(B["seconds_per_item"]))
    elif a.full:
        B, holdout = full_battery(prob, model, zf, cfg)
        B_rec, _ = battery_from_record(rec_run, model, cfg, prob, zf); compare = compare_batteries(B_rec, B)
        prov = dict(source=PROV_FULL, file=state["run_record"], sha256=state["run_record_sha256"], items=list(B["seconds_per_item"]))
        log(f"  --full comparison with the run record: all agree {compare['all_agree']}; disagreeing {compare['disagreeing']}")
    else:
        B, holdout = battery_from_record(rec_run, model, cfg, prob, zf)
        prov = dict(source="the worker's end-of-run battery (results.jsonl start_result), battery_set " + str(rec_run.get("battery_set")), file=state["run_record"], sha256=state["run_record_sha256"],
                    t_battery_s=rec_run.get("t_battery_s"), bound_to=dict(state_file=state["state_file"], state_sha256=state["state_sha256"], z_sha256=state["z_sha256"], params_final=state["params_final"]))
    if dev.type == "cuda":
        torch.cuda.empty_cache()
    # add-ons
    SP = spectra(model, zf)
    try:
        RP = poisson_residual(model, zf, holdout, c_l, omega, eps=a.eps)
    except Exception as e:
        log(f"  rho_P failed: {e!r}"); RP = dict(error=repr(e), status="OPEN: rho_P computation failed")
    if dev.type == "cuda":
        torch.cuda.empty_cache()
    try:
        G5 = g5_at_state(state_path, dev, a.tag)
    except Exception as e:
        log(f"  G5 failed: {e!r}"); G5 = dict(error=repr(e))
    path = run_path(rec_run) if rec_run is not None else None
    ex, fl, open_, any_ex, any_fl = decide_record(B, G5, RP, SP, path, refs, state)      # lead 18:49:47Z item 3: an item raised against ANY reference counts
    open_na = []
    if is_ref:                                                                                # V435 / V437: a start reference has no reference of its own; those items are inapplicable, not open
        open_na = [o for o in open_ if o.startswith(REF_DEPENDENT_PREFIXES)]; open_ = [o for o in open_ if not o.startswith(REF_DEPENDENT_PREFIXES)]
    reference_data_valid = bool(is_ref and not any_ex and not open_)
    rec = dict(kind="6.3 (a) record v1", version=VERSION, tag=a.tag, is_start_reference=bool(is_ref), state=state, battery=B, battery_provenance=prov, battery_vs_record=compare, spectra=SP, rho_P=RP, G5=G5, run_path=path,
               start_reference=([ref_summary(rf_, rp_) for rf_, rp_ in zip(refs, ref_paths)] if refs else None), segment_start=(ref_summary(seg, a.segment_start) if seg else None),
               exclusions_6_3a=ex, flags_6_3b=fl, any_exclusion=bool(any_ex), any_flag=bool(any_fl), open=open_, open_not_applicable=open_na, reference_data_valid=(reference_data_valid if is_ref else None),
               registered_clearance_6_3a=(False if is_ref else bool(not any_ex and not open_)),
               clearance_note=(("start reference: a denominator record, never an end candidate; reference data " + ("valid" if reference_data_valid else "NOT valid: " + ("exclusion raised" if any_ex else "open items " + "; ".join(open_)))) if is_ref else
                               ("no 6.3 (a) exclusion is raised on the registered fields and no item is open" if (not any_ex and not open_) else
                                ("an exclusion is raised: the state is diagnostic only (6.3 (a))" if any_ex else "clearance NOT established: open items " + "; ".join(open_)))),
               thresholds=TH, rules="SPEC 6.3 (a) (with 5.3, 5.4, 6.2, v1.21 (b), (c), v1.22 (c)) and 6.3 (b); lead 2026-10-29T17:50:42Z item 3 (a) to (g), 17:55:21Z item 2 (a_max core weights), 18:22:07Z items 1 to 4 (rho_P accuracy rule, per-block N6, F-projected start reference, --full comparison); V405; flags are cleared only by a dated lead note with the verifier's concurrence",
               sources=code_hashes(), script_sha256=sha(os.path.abspath(__file__)), worker_sha256=sha(os.path.join(ROOT, "scripts", "worker_d6.py")), gates_sha256=sha(os.path.join(ROOT, "validation", "gates.py")),
               launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None),
               device=str(dev), gpu=(torch.cuda.get_device_name(dev) if dev.type == "cuda" else None), torch=torch.__version__, seconds=time.time() - t_all, ts=now())
    with open(out_path, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    log(f"{a.tag}: exclusions raised {[e['item'] for e in ex if e['raised']]}; flags raised {[f['item'] for f in fl if f['raised']]}; open {open_}; not applicable {len(open_na)}; registered clearance {rec['registered_clearance_6_3a']}; reference data valid {rec['reference_data_valid']}; {rec['seconds']:.0f} s")
    print("DONE", out_path, sha(out_path)[:16])


if __name__ == "__main__":
    main()
