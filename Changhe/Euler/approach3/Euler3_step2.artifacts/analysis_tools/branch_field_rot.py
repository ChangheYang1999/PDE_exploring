#!/usr/bin/env python
"""Lead diagnostic: the field part of the branch identity (SPEC 6.5 norm, 8.6 rule) minimized over rotations about the z axis.

The equations are invariant under rotation about the z axis, and the production phase gauge (Problem.phase_align) fixes the
rotation by the largest m != 0 tail pair of each run (Problem.choose_pivot), so two states can carry different phase pivots, and
a pivot of degree m leaves a residual ambiguity of 2 pi / m. The registered distance d(a, b) of the producer tool
(scripts/branch_distance.py v6, reused here unchanged for the grid, the shells and the RMS) compares the two fields as saved.
This tool also computes, for state a rotated by gamma with the exact coefficient rotation of phase_align,
  d_ab(gamma) = max_j RMS_j(U_a(gamma) - U_b) / RMS_j(U_b),  d_ba(gamma) = max_j RMS_j(U_a(gamma) - U_b) / RMS_j(U_a(gamma)),
and reports min over gamma of max(d_ab, d_ba). Scan: n_scan equally spaced gamma on one period 2 pi / g (g = gcd of the m values
present), then golden-section refinement around the best scan point. The rotated field is evaluated directly with
fields_grid at each gamma (no linearity assumption). Also reports each state's pivot (choose_pivot) and its phase defect.
Information for the lead; it does not change the registered rule. Numerics, not a proof.
Usage: python tools/branch_field_rot.py <state a .pt> <state b .pt> --tag <tag> [--n-per-shell 6] [--n-scan 90]
Output: artifacts/branch_field/<tag>_rot.json (never overwritten)."""
import sys, os, json, time, math, hashlib, argparse
ROOT = "<optimization tree>"   # producer code, imported read only
OUT = "<analysis tree>/artifacts/branch_field"
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.validation.holdout import HoldoutGrid
from branch_field_lead import load_state, tail_norm2, sha


def rotate(model, z, gamma):
    """the exact rotation of Problem.phase_align by an arbitrary angle gamma (same formula and convention)."""
    d = model.unpack_all(z)
    m = model.m_arr.to(z.dtype)
    cm, sm = torch.cos(m * gamma), torch.sin(m * gamma)
    sign = model.tw_sign; partner = model.partner
    def rot(a):
        return a * cm[None, :] + sign[None, :] * a[:, partner] * sm[None, :]
    extra = {k: rot(d[k]) for k in ("B", "D", "E") if d[k].numel() > 0}
    return model.pack(rot(d["A"]), rot(d["C"]), d["c_l"], d["omega"], extra=extra)


def pivot_info(model, z):
    try:
        from src.optimization.problem import Problem
        from validation.gates import PROD
        prob = Problem(model, **PROD)
        pv = prob.choose_pivot(z)
        if pv is None:
            return None
        d = model.unpack_all(z); q = pv["q"]
        arr = d["A"] if pv["pot"] == "T" else d["C"]
        ac, as_ = float(arr[:, q].sum()), float(arr[:, q + 1].sum())
        l, mm, t = model.modes[q]
        return dict(pot=pv["pot"], q=int(q), l=int(l), m=int(mm), amp=float(pv["amp"]), tail_cos_sum=ac, tail_sin_sum=as_,
                    phase_defect=abs(as_) / max(math.hypot(ac, as_), 1e-300))
    except Exception as e:
        return dict(error=repr(e))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--tag", required=True)
    ap.add_argument("--n-per-shell", type=int, default=6); ap.add_argument("--n-scan", type=int, default=90)
    ap.add_argument("--jmin", type=int, default=-4); ap.add_argument("--jmax", type=int, default=8)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, f"{a.tag}_rot.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time(); dev = torch.device("cpu")
    ma, za, ia = load_state(a.a, dev); mb, zb, ib = load_state(a.b, dev)
    assert (ma.L, ma.Nk, float(ma.R0)) == (mb.L, mb.Nk, float(mb.R0))
    assert [tuple(q) for q in ma.modes] == [tuple(q) for q in mb.modes], "different mode sets"
    for info, m_, z_ in ((ia, ma, za), (ib, mb, zb)):
        n2 = tail_norm2(m_, z_); info["F_norm2_from_coefficients"] = n2
        info["pivot"] = pivot_info(m_, z_)
    R0 = float(ma.R0)
    edges = [(R0 * 2.0 ** j, R0 * 2.0 ** (j + 1)) for j in range(a.jmin, a.jmax + 1)]
    Ha = HoldoutGrid(ma, r_core=R0, n_per_shell=a.n_per_shell, edges=edges)
    Hb = HoldoutGrid(mb, r_core=R0, n_per_shell=a.n_per_shell, edges=edges)
    assert torch.equal(Ha.model.r, Hb.model.r) and torch.equal(Ha.model.grid.n, Hb.model.grid.n) and torch.equal(Ha.w_vol, Hb.w_vol)
    ms = sorted(set(int(v) for v in ma.m_arr.tolist() if int(v) != 0))
    g = 0
    for v in ms:
        g = math.gcd(g, v)
    period = 2.0 * math.pi / g
    with torch.no_grad():
        Ub = Hb.model.fields_grid(zb, need_vort=False)["U"]
        rms_b = Ha.rms(Ub)
        def dist(gamma):
            Ua = Ha.model.fields_grid(rotate(ma, za, gamma), need_vort=False)["U"]
            rd = Ha.rms(Ua - Ub); ra = Ha.rms(Ua)
            dab = max(x / y for x, y in zip(rd, rms_b)); dba = max(x / y for x, y in zip(rd, ra))
            return max(dab, dba), dab, dba, rd, ra
        t1 = time.time(); d0 = dist(0.0); t_eval = time.time() - t1
        # check: the rotation is exact on the coefficients (rotating by gamma then -gamma returns z)
        zz = rotate(ma, rotate(ma, za, 0.7), -0.7); rot_roundtrip = float((zz - za).abs().max())
        scan = []
        for k in range(a.n_scan):
            gam = period * k / a.n_scan
            v = dist(gam); scan.append((gam, v[0], v[1], v[2]))
        kb = min(range(len(scan)), key=lambda k: scan[k][1])
        lo, hi = scan[kb][0] - period / a.n_scan, scan[kb][0] + period / a.n_scan
        phi = (math.sqrt(5) - 1) / 2
        x1, x2 = hi - phi * (hi - lo), lo + phi * (hi - lo); f1, f2 = dist(x1)[0], dist(x2)[0]
        for _ in range(30):
            if f1 < f2:
                hi, x2, f2 = x2, x1, f1; x1 = hi - phi * (hi - lo); f1 = dist(x1)[0]
            else:
                lo, x1, f1 = x1, x2, f2; x2 = lo + phi * (hi - lo); f2 = dist(x2)[0]
        gbest = 0.5 * (lo + hi); vb = dist(gbest)
    shells = [dict(j=j, rms_diff=d_, rms_Ua=x_, rms_Ub=y_, ratio_ab=d_ / y_, ratio_ba=d_ / x_) for j, d_, x_, y_ in zip(range(a.jmin, a.jmax + 1), vb[3], vb[4], rms_b)]
    rec = dict(kind="lead diagnostic: SPEC 6.5 field distance minimized over rotations about the z axis (information; registered rule unchanged)",
               tag=a.tag, a=ia, b=ib, m_values=ms, gcd_m=g, period=period, n_scan=a.n_scan, seconds_per_eval=t_eval, rotation_roundtrip_maxabs=rot_roundtrip,
               d_at_gamma0=dict(d_max=d0[0], d_ab=d0[1], d_ba=d0[2]), best=dict(gamma=gbest, gamma_over_period=gbest / period, d_max=vb[0], d_ab=vb[1], d_ba=vb[2], shells=shells),
               scan=[dict(gamma=s[0], d_max=s[1], d_ab=s[2], d_ba=s[3]) for s in scan], threshold=0.10, agreement_mod_rotation=bool(vb[0] <= 0.10),
               script_sha256=sha(os.path.abspath(__file__)), torch=torch.__version__, seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print(f"{a.tag}: d at gamma 0 = {d0[0]:.4f} (ab {d0[1]:.4f}, ba {d0[2]:.4f}); min over gamma = {vb[0]:.4f} (ab {vb[1]:.4f}, ba {vb[2]:.4f}) at gamma = {gbest:.5f} "
          f"({gbest / period:.4f} of the period 2pi/{g}); pivots a {ia['pivot']}, b {ib['pivot']}; eval {t_eval:.1f} s; total {rec['seconds']:.0f} s")
    print("DONE", out_path, sha(out_path)[:16])


if __name__ == "__main__":
    main()
