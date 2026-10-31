#!/usr/bin/env python
"""Lead diagnostic: the best rotation angle about the z axis on each dyadic shell separately (information).

For states a and b (F-gauge, saved files) and each shell j = jmin..jmax of the SPEC 6.5 norm, computes
  d_j(gamma) = max(RMS_j(U_a(gamma) - U_b) / RMS_j(U_b), RMS_j(U_a(gamma) - U_b) / RMS_j(U_a(gamma)))
with U_a(gamma) the field of state a rotated by gamma (exact coefficient rotation of Problem.phase_align, as in
tools/branch_field_rot.py), and reports gamma_j* = argmin d_j and min d_j per shell. If the two states differ by a
rotation that depends on radius, gamma_j* varies with j and min d_j is small on every shell; if they differ in
structure, min d_j stays large. Scan of n_scan points on one period 2 pi / g, then golden-section refinement per shell.
Uses the producer's grid and RMS (not independent). Numerics, not a proof.
Usage: python tools/branch_field_twist.py <state a .pt> <state b .pt> --tag <tag> [--n-scan 120]
Output: artifacts/branch_field/<tag>_twist.json (never overwritten)."""
import sys, os, json, time, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branch_field_rot import ROOT, OUT, rotate, pivot_info, HoldoutGrid, load_state, sha, torch


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--tag", required=True)
    ap.add_argument("--n-per-shell", type=int, default=6); ap.add_argument("--n-scan", type=int, default=120)
    ap.add_argument("--jmin", type=int, default=-4); ap.add_argument("--jmax", type=int, default=8)
    a = ap.parse_args()
    out_path = os.path.join(OUT, f"{a.tag}_twist.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time(); dev = torch.device("cpu")
    ma, za, ia = load_state(a.a, dev); mb, zb, ib = load_state(a.b, dev)
    assert (ma.L, ma.Nk, float(ma.R0)) == (mb.L, mb.Nk, float(mb.R0))
    assert [tuple(q) for q in ma.modes] == [tuple(q) for q in mb.modes], "different mode sets"
    ia["pivot"] = pivot_info(ma, za); ib["pivot"] = pivot_info(mb, zb)
    R0 = float(ma.R0)
    js = list(range(a.jmin, a.jmax + 1))
    edges = [(R0 * 2.0 ** j, R0 * 2.0 ** (j + 1)) for j in js]
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
        rb = Ha.rms(Ub)
        def shell_d(gamma):
            Ua = Ha.model.fields_grid(rotate(ma, za, gamma), need_vort=False)["U"]
            rd = Ha.rms(Ua - Ub); ra = Ha.rms(Ua)
            return [max(x / y, x / z) for x, y, z in zip(rd, rb, ra)]
        grid = [period * k / a.n_scan for k in range(a.n_scan)]
        scan = [shell_d(gm) for gm in grid]
        res = []
        phi = (math.sqrt(5) - 1) / 2
        for i, j in enumerate(js):
            kb = min(range(a.n_scan), key=lambda k: scan[k][i])
            lo, hi = grid[kb] - period / a.n_scan, grid[kb] + period / a.n_scan
            f = lambda x: shell_d(x)[i]
            x1, x2 = hi - phi * (hi - lo), lo + phi * (hi - lo); f1, f2 = f(x1), f(x2)
            for _ in range(25):
                if f1 < f2:
                    hi, x2, f2 = x2, x1, f1; x1 = hi - phi * (hi - lo); f1 = f(x1)
                else:
                    lo, x1, f1 = x1, x2, f2; x2 = lo + phi * (hi - lo); f2 = f(x2)
            gb = 0.5 * (lo + hi)
            gw = (gb + 0.5 * period) % period - 0.5 * period   # representative in [-period/2, period/2)
            res.append(dict(j=j, r_in=edges[i][0], r_out=edges[i][1], d_at_gamma0=scan[0][i], gamma_best=gb, gamma_best_wrapped=gw,
                            d_min=f(gb), d_scan_max=max(s[i] for s in scan)))
    rec = dict(kind="lead diagnostic: best rotation angle about the z axis per dyadic shell (information; registered rule unchanged)",
               tag=a.tag, a=ia, b=ib, m_values=ms, gcd_m=g, period=period, n_scan=a.n_scan, shells=res,
               scan=[dict(gamma=gm, d=s) for gm, s in zip(grid, scan)], script_sha256=sha(os.path.abspath(__file__)),
               torch=torch.__version__, seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_path, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    for r in res:
        print(f"j={r['j']:2d} r=[{r['r_in']:.4g},{r['r_out']:.4g}] d(0)={r['d_at_gamma0']:.4f} min d={r['d_min']:.4f} at gamma={r['gamma_best_wrapped']:+.4f}")
    print("DONE", out_path, sha(out_path)[:16], f"{rec['seconds']:.0f} s")


if __name__ == "__main__":
    main()
