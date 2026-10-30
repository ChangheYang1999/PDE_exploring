"""Independent numerical review of T4-185 (c1-t1 R1-022): the angular mode-7 weak probe for candidate 007.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B check_T4185.py > check_T4185.out

Weak test (c1-t4 research/angular_weak_probes/PROOF.md, the T4-172 / T2-W4 inequality with a higher angular mode):
a = 0, w = 1, C_U = 1, phi_n = r W^2 P(t) sin(n theta), n odd, t^((n-1)/2) | P. Every S1 correction h with
F(rho + h; c) = 0 has ||h||_2 >= 2|I|/(D + sqrt(D^2 + 4 H |I|)), I = int F(rho) phi_n, D = ||M||_2 + ||phi_n D rho||_2,
M = (2c+1) phi_n + (cX + U[rho]).D phi_n, H = sup |D phi_n| = sup_t W^2 max(|Q|, n|P|), Q = (1-4t)P + 2tW P'.

Independence from T4: fields from the c1-n1 generator snapshot with the c1-t2 builder (as in check_T4182.py, whose
head is executed here: load, build, integ, to_arb). The angular expansions below are derived and coded here:
  rho = r sum W^(K delta/2) R sin(l theta), D_r rho = sum W^(K delta/2) Top(R, K delta/2, 1) sin(l theta),
  psi = r^2 sum W^(K delta/2) S sin(m theta), u = (-psi_y, psi_x): u_r = -r W^.. m S cos(m theta),
  u_theta = r W^.. Top(S, K delta/2, 2) sin(m theta)   (K = j + 1),
and every product is reduced with product-to-sum identities to a sine or cosine series and squared by Parseval. The
pairing is computed twice: directly from the sin(n theta) component of F, and as -int rho M. The series are checked
pointwise against Cartesian central differences of rho, psi and phi at four points. At n = 1 the code reproduces the
T4-182 values of check_T4182.json (c1-t2 Gram route) and the N4-091 pairing. H is certified by an own bisection.
Input: data/T4185_n7_a0.json = c1-t4 research/optimized_probe_007/verification/n7_a0.json (sha256 checked).
"""
import json
import sys
import time
from pathlib import Path

exec(compile(Path("check_T4182.py").read_text().split("# ---------------- pairing forms (copied from c1-t2 PREP")[0],
             "check_T4182_head", "exec"))
T85 = Path("data/T4185_n7_a0.json")
T85_SHA = "2a268c62e9e45096d2b745679a49adeee0cb9a3da532a06e4b89faaffdb3ef1f"
assert sha(T85) == T85_SHA
T5 = json.loads(T85.read_text())
print(f"T4-185 n7_a0.json sha256 {T85_SHA}")
cA = A(c)
dA = A(delta)
Z0 = arb_poly([])


def acc(d, key, P):
    d[key] = d.get(key, Z0) + P


def add_sin(d, k, K, P):          # coefficient of sin(k theta); sin(-k theta) = -sin(k theta)
    if k == 0:
        return
    if k < 0:
        k, P = -k, -P
    acc(d, (k, K), P)


def add_cos(d, k, K, P):
    acc(d, (abs(k), K), P)


rhoR, rhoT, psiS, psiT = {}, {}, {}, {}
for (j, l), P in R.items():
    acc(rhoR, (j + 1, l), to_arb(P))
    acc(rhoT, (j + 1, l), to_arb(Top(P, (j + 1) * delta / 2, 1)))
for (j, m), P in S.items():
    acc(psiS, (j + 1, m), to_arb(P))
    acc(psiT, (j + 1, m), to_arb(Top(P, (j + 1) * delta / 2, 2)))
tA = arb_poly([0, 1])


def wexp(K, off):                  # exponent off + K delta/2 of W, exact
    return fmpq(off) + K * delta / 2


def probe(coef, n):
    k0 = (n - 1) // 2
    assert all(k >= k0 for k in coef), "t^((n-1)/2) must divide P"
    Pq = fmpq_poly([0])
    for k, q in coef.items():
        Pq += q * tp**k
    Qq = fmpq_poly([1, -4]) * Pq + 2 * tp * Wq * Pq.derivative()
    return Pq, Qq


def series(Pq, Qq, n):
    Pa, Qa = to_arb(Pq), to_arb(Qq)
    # M / (r W^2) = sum_(k,K) W^(K delta/2) B sin(k theta)
    Ms = {}
    add_sin(Ms, n, 0, Pa * (2 * cA + 1) + Qa * cA)
    for (K, m), Sp in psiS.items():
        TS = psiT[(K, m)]
        # u.D phi / (r W^(K delta/2 + 2)) = -m S Q cos(m th) sin(n th) + n T_S P sin(m th) cos(n th)
        add_sin(Ms, n + m, K, (TS * Pa * n - Sp * Qa * m) * arb(0.5))
        add_sin(Ms, n - m, K, (-TS * Pa * n - Sp * Qa * m) * arb(0.5))
    # F / r, only the sin(n theta) component
    Fs = {}
    for (K, l), Rp in rhoR.items():
        if l == n:
            add_sin(Fs, n, K, rhoT[(K, l)] * cA - Rp)
    for (Ki, l), Rp in rhoR.items():
        Ti = rhoT[(Ki, l)]
        for (Kj, m), Sp in psiS.items():
            if l + m != n and abs(l - m) != n:
                continue
            TS = psiT[(Kj, m)]
            # u.D rho / (r W^(..)) = -m S T cos(m th) sin(l th) + l T_S R sin(m th) cos(l th)
            if l + m == n:
                add_sin(Fs, l + m, Ki + Kj, (-Sp * Ti * m + TS * Rp * l) * arb(0.5))
            if abs(l - m) == n:
                add_sin(Fs, l - m, Ki + Kj, (-Sp * Ti * m - TS * Rp * l) * arb(0.5))
    Fs = {key: P for key, P in Fs.items() if key[0] == n}
    # phi D rho / (r W^2 P): e_r cosine series, e_theta sine series
    Cr, Ct = {}, {}
    for (K, l), Rp in rhoR.items():
        T = rhoT[(K, l)]
        add_cos(Cr, n - l, K, T * arb(0.5))
        add_cos(Cr, n + l, K, -T * arb(0.5))
        add_sin(Ct, n + l, K, Rp * (arb(l) / 2))
        add_sin(Ct, n - l, K, Rp * (arb(l) / 2))
    return Pa, Qa, Ms, Fs, Cr, Ct


def bymode(d):
    out = {}
    for (k, K), P in d.items():
        out.setdefault(k, []).append((K, P))
    return out


def quad_sum(d, weight, off, extra=None):
    """sum_k weight(k) sum_(K,K') int_0^1 t W^(off + (K+K') delta/2) B_(k,K) B_(k,K') extra dt."""
    E = {}
    for k, lst in bymode(d).items():
        wk = weight(k)
        for i, (K1, P1) in enumerate(lst):
            for K2, P2 in lst[i:]:
                f = 1 if K1 == K2 else 2
                acc(E, K1 + K2, P1 * P2 * (wk * f))
    tot = arb(0)
    for KK, P in E.items():
        b = wexp(KK, off)
        assert b > -1
        tot += integ(P * extra if extra is not None else P, 1, b)
    return tot


def values(coef, n):
    Pq, Qq = probe(coef, n)
    Pa, Qa, Ms, Fs, Cr, Ct = series(Pq, Qq, n)
    I_dir = pi / 2 * sum((integ(G * Pa, 1, wexp(K, -1)) for (k, K), G in Fs.items()), arb(0))
    I_rm = arb(0)
    for (K, l), Rp in rhoR.items():
        for (k, K2), B in Ms.items():
            if k == l:
                I_rm += integ(Rp * B, 1, wexp(K + K2, -1))
    I_rm = -pi / 2 * I_rm
    M2 = pi / 2 * quad_sum(Ms, lambda k: 1, 1)
    C2 = arb(0.5) * (quad_sum(Cr, lambda k: 2 * pi if k == 0 else pi, 1, Pa * Pa)
                     + quad_sum(Ct, lambda k: pi, 1, Pa * Pa))
    return dict(Pq=Pq, Qq=Qq, Pa=Pa, Qa=Qa, Ms=Ms, Fs=Fs, Cr=Cr, Ct=Ct, I_dir=I_dir, I_rm=I_rm, M=M2.sqrt(),
                C=C2.sqrt())


# ---------------- (A) n = 1 reproductions ----------------
v = values({0: fmpq(1)}, 1)
n4_091_k0 = arb("0.00015509843384403807441")
print(f"(A1) n = 1, P = 1: I direct {v['I_dir'].str(25)}, I = -int rho M {v['I_rm'].str(25)};"
      f" N4-091 0.00015509843384403807441")
assert abs(v["I_dir"] - n4_091_k0) < arb("1e-22") and abs(v["I_rm"] - n4_091_k0) < arb("1e-22")
c82 = json.loads(Path("check_T4182.json").read_text())
coef82 = {int(k): fmpq(*map(int, (vv.split("/") + ["1"])[:2])) for k, vv in T4["probe_coefficients"].items()}
v = values(coef82, 1)
ok = {}
for lab, mine in (("pairing", v["I_dir"]), ("pairing_rm", v["I_rm"]), ("M", v["M"]), ("C", v["C"])):
    s = c82[lab.split("_")[0]].strip("[]").split("+/-")
    ref = arb(s[0].strip(), s[1].strip())
    ok[lab] = mine.overlaps(ref)
    print(f"(A2) n = 1, T4-182 vector, {lab:10s} {mine.str(25)}  check_T4182.json {ref.str(25)}  overlap {ok[lab]}")
assert all(ok.values())
print(f"    [{time.monotonic() - T0:.1f} s]", flush=True)

# ---------------- (B) T4-185 n = 7 ----------------
n = int(T5["angular_mode"])
assert n == 7 and T5["a"] == "0" and T5["C_U_exact"] == "1"
coef = {int(k): fmpq(*map(int, (vv.split("/") + ["1"])[:2])) for k, vv in T5["probe_coefficients"].items()}
print(f"(B) n = {n}, {len(coef)} powers {sorted(coef)}")
v7 = values(coef, n)
print(f"    I direct        {v7['I_dir'].str(30)}\n    I = -int rho M  {v7['I_rm'].str(30)}")
assert v7["I_dir"].overlaps(v7["I_rm"])
cmp = {}
for lab, mine in (("pairing", v7["I_dir"]), ("M", v7["M"]), ("C", v7["C"])):
    s = T5[lab].strip("[]").split("+/-")
    theirs = arb(s[0].strip(), s[1].strip())
    cmp[lab] = mine.overlaps(theirs)
    print(f"    {lab:8s} c1-t1 {mine.str(30)}\n             T4    {theirs.str(30)}  overlap {cmp[lab]};"
          f" |difference| {abs(mine - theirs).str(3)}")
assert all(cmp.values())
print(f"    [{time.monotonic() - T0:.1f} s]", flush=True)

# ---------------- (C) pointwise check of the series against Cartesian central differences ----------------
ctx.prec = 512
hh = arb(2) ** -150


def field_point(x, y, which):
    r2 = x * x + y * y
    r = r2.sqrt()
    th = arb.atan2(y, x)
    t = r2 / (1 + r2)
    W = 1 / (1 + r2)
    tot = arb(0)
    if which == "rho":
        for (K, l), P in rhoR.items():
            tot += r * W ** A(wexp(K, 0)) * P(t) * (l * th).sin()
    elif which == "psi":
        for (K, m), P in psiS.items():
            tot += r2 * W ** A(wexp(K, 0)) * P(t) * (m * th).sin()
    else:
        tot = r * W * W * v7["Pa"](t) * (n * th).sin()
    return tot


def grad(x, y, which):
    return ((field_point(x + hh, y, which) - field_point(x - hh, y, which)) / (2 * hh),
            (field_point(x, y + hh, which) - field_point(x, y - hh, which)) / (2 * hh))


def eval_series(d, r, th, trig, off, mult):
    t = r * r / (1 + r * r)
    W = 1 / (1 + r * r)
    return sum((W ** A(wexp(K, off)) * P(t) * mult * trig(k * th) for (k, K), P in d.items()), arb(0))


pmax = 0
for (x, y) in ((arb("0.3"), arb("0.7")), (arb("1.9"), arb("0.45")), (arb("-4.2"), arb("2.6")), (arb("17"), arb("-11"))):
    r = (x * x + y * y).sqrt()
    th = arb.atan2(y, x)
    t = r * r / (1 + r * r)
    W = 1 / (1 + r * r)
    rho, (rx, ry) = field_point(x, y, "rho"), grad(x, y, "rho")
    px, py = grad(x, y, "psi")
    u1, u2 = -py, px
    phi, (fx, fy) = field_point(x, y, "phi"), grad(x, y, "phi")
    F = (cA * x + u1) * rx + (cA * y + u2) * ry - rho
    M = (2 * cA + 1) * phi + (cA * x + u1) * fx + (cA * y + u2) * fy
    Mser = r * W * W * eval_series(v7["Ms"], r, th, arb.sin, 0, 1)
    gr2 = (phi * rx) ** 2 + (phi * ry) ** 2
    Cser = (r * W * W * v7["Pa"](t)) ** 2 * (eval_series(v7["Cr"], r, th, arb.cos, 0, 1) ** 2
                                             + eval_series(v7["Ct"], r, th, arb.sin, 0, 1) ** 2)
    dM, dC = abs(M - Mser) / (abs(M) + 1e-300), abs(gr2 - Cser) / (abs(gr2) + 1e-300)
    pmax = max(pmax, float(dM.upper()), float(dC.upper()))
    print(f"(C) point ({x.str(3)}, {y.str(3)}): M direct {M.str(15)} series {Mser.str(15)}; |phi D rho|^2 direct"
          f" {gr2.str(15)} series {Cser.str(15)}")
assert pmax < 1e-30
# sin(n theta) component of F: average of F(r, theta) sin(n theta) over an equispaced theta grid (exact for trigonometric
# polynomials of degree < number of points - n), compared with the series G at one radius.
r0 = arb("2.3")
NP = 2 * (max(k for k, _ in R) + max(m for _, m in S)) + 8
acc_n = arb(0)
for i in range(NP):
    th = 2 * pi * i / NP
    x, y = r0 * th.cos(), r0 * th.sin()
    rho, (rx, ry) = field_point(x, y, "rho"), grad(x, y, "rho")
    px, py = grad(x, y, "psi")
    acc_n += ((cA * x - py) * rx + (cA * y + px) * ry - rho) * (n * th).sin()
Fn_grid = 2 * acc_n / NP
t0, W0 = r0 * r0 / (1 + r0 * r0), 1 / (1 + r0 * r0)
Fn_ser = r0 * sum((W0 ** A(wexp(K, 0)) * G(t0) for (k, K), G in v7["Fs"].items()), arb(0))
print(f"(C) sin({n} theta) component of F at r = 2.3: grid ({NP} angles) {Fn_grid.str(15)}, series {Fn_ser.str(15)}")
assert abs(Fn_grid - Fn_ser) < arb("1e-30") * abs(Fn_ser)
print(f"    pointwise relative differences below {pmax:.1e} [{time.monotonic() - T0:.1f} s]", flush=True)

# ---------------- (D) own certificate for H = sup_t W^2 max(|Q|, n|P|) ----------------
ctx.prec = 256
polys = [(to_arb(Z), to_arb(Z.derivative()), to_arb(Z.derivative().derivative())) for Z in (n * v7["Pq"], v7["Qq"])]
H_target = fmpq(*map(int, T5["H_upper_exact"].split("/")))


def cell_bound(lo, hi):
    """Upper bound of W^2 max(|Q|, n|P|) on [lo, hi]: W^2 <= (1 - lo)^2, |Z(t)| <= |Z(m)| + r|Z'(m)| + r^2/2 sup|Z''|."""
    m, r = (lo + hi) / 2, (hi - lo) / 2
    mA, rA = A(m), A(r)
    ball = arb(mA, rA * (1 + arb(2) ** -100))
    bnd = [abs(Z(mA)) + rA * abs(dZ(mA)) + rA * rA / 2 * abs(d2Z(ball)) for Z, dZ, d2Z in polys]
    return A((1 - lo) ** 2) * max(b.upper() for b in bnd)


stack, accepted, maxub = [(fmpq(0), fmpq(1))], 0, arb(0)
while stack:
    lo, hi = stack.pop()
    ub = cell_bound(lo, hi)
    if ub < A(H_target):
        accepted += 1
        maxub = max(maxub, ub)
    else:
        assert hi - lo > fmpq(1, 2**44), (lo, hi)
        mid = (lo + hi) / 2
        stack += [(lo, mid), (mid, hi)]
    assert accepted < 200000
print(f"(D) sup_t W^2 max(|Q|, {n}|P|) < T4's H_upper_exact = {H_target} = {A(H_target).str(10)}: CERTIFIED on"
      f" {accepted} cells (largest cell bound {maxub.str(10)}) [{time.monotonic() - T0:.1f} s]", flush=True)
NS = 20000
best = (arb(0), 0)
for i in range(NS + 1):
    val = max(abs(Z(A(fmpq(i, NS)))) for Z, _, _ in polys) * A((1 - fmpq(i, NS)) ** 2)
    if val > best[0]:
        best = (val, i)
print(f"    sampled lower value on t = i/{NS}: {best[0].str(10)} at t = {best[1]}/{NS}"
      f" (T4 sample {T5['H_certificate']['lower_sample']})")
ctx.prec = 1024

# ---------------- (E) radius ----------------
H = A(H_target)
D = v7["M"] + v7["C"]
Iabs = abs(v7["I_dir"])
rad = 2 * Iabs / (D + (D * D + 4 * H * Iabs).sqrt())
floor_T4 = fmpq(*map(int, T5["strict_lower_exact"].split("/")))
print(f"(E) D = {D.str(20)}, H <= {H.str(10)}, radius {rad.str(30)}")
print(f"    radius > T4 strict floor {floor_T4} = {A(floor_T4).str(12)}: {rad > A(floor_T4)}")
assert rad > A(floor_T4)
for lab, b in (("N4-091 (k = 0)", "4.3987003470e-5"), ("T4-182 (n = 1 span, AUDITED)", "3.1474108e-4"),
               ("FW-T-TB-sharp-v1 budget", "3.7930e-6"), ("FW-T-T4L2-sharpw-v1 budget", "2.8496e-6"),
               ("graded boxes (NC-T-GRADED-L2) budget", "4.5717e-4")):
    print(f"    distance / {lab}: {(rad / arb(b)).str(6)}")
out = dict(review="R1-022 (T4-185)", snapshot_sha256=SNAP_SHA, t4_json_sha256=T85_SHA, n=n, pairing=v7["I_dir"].str(40),
           pairing_minus_int_rho_M=v7["I_rm"].str(40), M=v7["M"].str(40), C=v7["C"].str(40),
           H_certified_below=str(H_target), H_cells=accepted, radius=rad.str(40),
           exceeds_T4_floor=bool(rad > A(floor_T4)), overlaps=cmp, n1_reproduction=ok, seconds=time.monotonic() - T0)
Path("check_T4185.json").write_text(json.dumps(out, indent=1))
print(f"done [{time.monotonic() - T0:.1f} s]")
