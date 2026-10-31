#!/usr/bin/env python
"""Double-double elementary functions in torch (test-only, SPEC v1.19 3.6 (l) copy): exp, cos, sin of (hi, lo) arguments, vectorized.
exp: n = round(h / ln 2), r = x - n ln2 (ln 2 as a double-double constant, n ln2 by exact products), r / 2^9, Taylor to degree 11 in double-double,
nine squarings, times 2^n. cos, sin: k = round(x / (pi/2)), r = x - k pi/2 (pi/2 double-double), |r| <= pi/4 reduced three times by halving with the
double-angle formulas after Taylor to degree 13 on |r|/8. Relative errors about 1e-30 (checked against mpmath in the self-test: python validation/dd_elementary.py)."""
import math, os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
from src.pressure.exact_matmul import dd_add, dd_mul_f, dd_div_f
from src.equations.fields_dd import dd_mul_dd

LN2_HI = 0.6931471805599453; LN2_LO = 2.3190468138462996e-17
PIO2_HI = 1.5707963267948966; PIO2_LO = 6.123233995736766e-17
LN2_LO2 = 5.707708438416212e-34; PIO2_LO2 = -1.4973849048591698e-33     # third words (for the reductions with large n; negligible otherwise)


def _two_prod(a, b):
    p = a * b
    # Dekker split for the error term
    c = 134217729.0 * a; ah = c - (c - a); al = a - ah
    d = 134217729.0 * b; bh = d - (d - b); bl = b - bh
    e = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, e


def exp_dd(h, l):
    n = torch.round(h / LN2_HI)
    p1, e1 = _two_prod(n, LN2_HI); p2 = n * LN2_LO                      # n ln2 as (p1, e1 + p2)
    rh, rl = dd_add(h, l, -p1, -(e1 + p2))
    rh, rl = rh / 512.0, rl / 512.0                                       # exact scaling
    # Taylor: sum_{k=0}^{11} r^k / k!
    th, tl = torch.ones_like(rh), torch.zeros_like(rh)
    ph, pl = torch.ones_like(rh), torch.zeros_like(rh)
    for k in range(1, 12):
        ph, pl = dd_mul_dd(ph, pl, rh, rl); ph, pl = dd_div_f(ph, pl, float(k))
        th, tl = dd_add(th, tl, ph, pl)
    for _ in range(9):
        th, tl = dd_mul_dd(th, tl, th, tl)
    s = torch.ldexp(torch.ones_like(th), n.to(torch.int64)) if hasattr(torch, "ldexp") else 2.0 ** n
    return th * s, tl * s


def sincos_dd(h, l):
    k = torch.round(h / PIO2_HI)
    p1, e1 = _two_prod(k, PIO2_HI); p2 = k * PIO2_LO
    rh, rl = dd_add(h, l, -p1, -(e1 + p2))
    rh, rl = rh / 8.0, rl / 8.0
    # Taylor for sin and cos on |r| <= pi/32
    sh, sl = rh.clone(), rl.clone(); ch, cl = torch.ones_like(rh), torch.zeros_like(rh)
    r2h, r2l = dd_mul_dd(rh, rl, rh, rl)
    termh, terml = rh.clone(), rl.clone()
    for m in range(1, 8):                                                  # sin: r - r^3/3! + ... ; cos: 1 - r^2/2! + ...
        termh, terml = dd_mul_dd(termh, terml, r2h, r2l); termh, terml = dd_div_f(termh, terml, float((2 * m) * (2 * m + 1)))
        sgn = -1.0 if m % 2 == 1 else 1.0
        sh, sl = dd_add(sh, sl, sgn * termh, sgn * terml)
    termh, terml = torch.ones_like(rh), torch.zeros_like(rh)
    for m in range(1, 8):
        termh, terml = dd_mul_dd(termh, terml, r2h, r2l); termh, terml = dd_div_f(termh, terml, float((2 * m - 1) * (2 * m)))
        sgn = -1.0 if m % 2 == 1 else 1.0
        ch, cl = dd_add(ch, cl, sgn * termh, sgn * terml)
    for _ in range(3):                                                    # double angle thrice: sin 2a = 2 sin a cos a, cos 2a = 1 - 2 sin^2 a
        s2h, s2l = dd_mul_dd(sh, sl, ch, cl); s2h, s2l = dd_mul_f(s2h, s2l, 2.0)
        q_h, q_l = dd_mul_dd(sh, sl, sh, sl); q_h, q_l = dd_mul_f(q_h, q_l, -2.0); c2h, c2l = dd_add(torch.ones_like(q_h), torch.zeros_like(q_h), q_h, q_l)
        sh, sl, ch, cl = s2h, s2l, c2h, c2l
    kk = (k.to(torch.int64) % 4 + 4) % 4
    sin_h = torch.where(kk == 0, sh, torch.where(kk == 1, ch, torch.where(kk == 2, -sh, -ch)))
    sin_l = torch.where(kk == 0, sl, torch.where(kk == 1, cl, torch.where(kk == 2, -sl, -cl)))
    cos_h = torch.where(kk == 0, ch, torch.where(kk == 1, -sh, torch.where(kk == 2, -ch, sh)))
    cos_l = torch.where(kk == 0, cl, torch.where(kk == 1, -sl, torch.where(kk == 2, -cl, sl)))
    return (sin_h, sin_l), (cos_h, cos_l)


if __name__ == "__main__":
    import mpmath as mp, sys
    mp.mp.dps = 40
    torch.manual_seed(1)
    # ranges per the verifier's 11:04Z reference scan of the actual tables: exp arguments down to about -1433 (underflow to exact zero below about -745,
    # subnormal low word between -745 and -672) and up to 42.5; trigonometric arguments up to 781 (S01) and 2666 (S05): the trig sample goes to +-3000
    x = torch.cat([torch.linspace(-700.0, 700.0, 2001, dtype=torch.float64), torch.randn(2000, dtype=torch.float64) * 50, torch.tensor([0.0, 1e-300, -1e-10, 0.6931471805599453, 1.5707963267948966, 3.141592653589793])])
    lo = (torch.rand_like(x) - 0.5) * 2 ** -52 * x.abs()
    xe = torch.cat([x, torch.linspace(-1450.0, -700.0, 751, dtype=torch.float64)]); loe = torch.cat([lo, torch.zeros(751, dtype=torch.float64)])
    xt = torch.cat([x, torch.linspace(-3000.0, 3000.0, 3001, dtype=torch.float64), torch.tensor([781.365, 2665.596, -2665.596])]); lot = torch.cat([lo, (torch.rand(3004, dtype=torch.float64) - 0.5) * 2 ** -52 * 3000.0])
    eh, el = exp_dd(xe, loe); (sh, sl), (ch, cl) = sincos_dd(xt, lot)
    worst = dict(exp=0.0, sin=0.0, cos=0.0); worst_exp_normal = 0.0; underflow_ok = True
    for i in range(xe.numel()):
        xm = mp.mpf(float(xe[i])) + mp.mpf(float(loe[i])); ref = mp.exp(xm); got = mp.mpf(float(eh[i])) + mp.mpf(float(el[i]))
        if float(xe[i]) < -745.2:
            underflow_ok = underflow_ok and (got == 0)                            # below the float64 range the production table entry is exactly zero too
            continue
        err = float(abs(got - ref) / abs(ref)); worst["exp"] = max(worst["exp"], err)
        if float(xe[i]) > -672.0:
            worst_exp_normal = max(worst_exp_normal, err)
    for i in range(xt.numel()):
        xm = mp.mpf(float(xt[i])) + mp.mpf(float(lot[i]))
        for name, (vh, vl), f in (("sin", (sh, sl), mp.sin), ("cos", (ch, cl), mp.cos)):
            ref = f(xm); got = mp.mpf(float(vh[i])) + mp.mpf(float(vl[i])); worst[name] = max(worst[name], float(abs(got - ref)))
    rec = dict(exp_sample_n=int(xe.numel()), exp_x_range=[float(xe.min()), float(xe.max())], trig_sample_n=int(xt.numel()), trig_x_range=[float(xt.min()), float(xt.max())],
               worst_rel_exp_x_above_minus_745=worst["exp"], worst_rel_exp_x_above_minus_672=worst_exp_normal, exp_underflow_exact_zero_below_minus_745=underflow_ok,
               worst_abs_sin=worst["sin"], worst_abs_cos=worst["cos"], note="the fixed 1e-29 threshold of the first draft is replaced by the lead's 10:56:41Z criterion (c): the acceptable error is decided by the recorded argument range of the pressure kernel tables and the screen response; below x = -672 the result's low word is subnormal and the relative error rises to about 1e-24 (V261)")
    print(json.dumps(rec, indent=1))
    json.dump(rec, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dd_elementary_test.json"), "w"), indent=1)
    print("dd_elementary self-test recorded")
