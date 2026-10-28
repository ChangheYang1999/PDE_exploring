"""Third computation for verification topic 76 (quadratic transport U[h].Dh is not continuous at zero from the
logarithmic space into itself, even on compact densities with b = c = 0).

Written from the statement of topic 76 only; no verifier code is imported. Routes:

1. Exact (sympy): the Fourier symbols of -R1R2 and R1^2 composed with -Delta are those of -d_xy and d_xx, so
   U[-Delta phi] = (-phi_xy, phi_xx) (5); psi = phi_x solves -Delta psi = h_x and U = (-psi_y, psi_x); on the plateau
   phi_0 = +-x^2/2 gives h_0 = -+1, U[h_0] = (0, +-1), Dh_0 = 0 (6); parities of phi_0, h_n, b_tilde = s b and g_n;
   the cross term g_n = s d_y h_n = -A d_y Delta(b_tilde cos ny) for constant s (9); for a generic envelope b(x, y),
   the n-degree of every entry of D^2 g_n (yy: 5, with leading coefficient -A s b d_y^5 cos(ny)/1, xy: 4, xx: 3) and
   of T(h_n) (at most 3), with frequencies 0 and 2n only; the scaling algebra A_n n^4 L^beta = 1, A_n n^5 L^beta = n,
   A_n^2 n^5 L^beta = n^-3 L^-beta, and n^(-1/2) n = n^(1/2).
2. FLOAT (numpy FFT on [-5/2, 5/2]^2, 1024^2 points, compact bump envelopes): U computed by the Fourier symbols equals
   (-phi_xy, phi_xx) for a compact potential; for beta = 1 and beta = 0, ||D^2 Q_beta g_n||_2/n approaches
   ||b||_2/sqrt(2) as n grows (n = 32 to 256) while the unweighted top component of T(h_n) decays at least like n^-2.

Usage: python3 check_p76.py [OUTPUT_JSON]
"""
import json, sys, time, hashlib
from pathlib import Path
import sympy as sp
import numpy as np
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
chk, out = {}, {}
x, y = sp.symbols('x y', real=True)
x1, x2 = sp.symbols('xi1 xi2', real=True)
n, A, L, bt = sp.symbols('n A L beta', positive=True)
s = sp.symbols('s', real=True)
xi2 = x1 ** 2 + x2 ** 2
R1, R2 = sp.I * x1 / sp.sqrt(xi2), sp.I * x2 / sp.sqrt(xi2)
lap_sym = -xi2
# symbol of h = -Delta phi is |xi|^2 phi_hat
chk['(5) symbol: -R1 R2 (|xi|^2) = symbol of -d_xy = -(i xi1)(i xi2)'] = sp.simplify(-R1 * R2 * xi2 - (-(sp.I * x1) * (sp.I * x2))) == 0
chk['(5) symbol: R1^2 (|xi|^2) = symbol of d_xx = (i xi1)^2'] = sp.simplify(R1 ** 2 * xi2 - (sp.I * x1) ** 2) == 0
phi = sp.Function('phi')(x, y)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
h = -lap(phi); psi = sp.diff(phi, x)
chk['psi = phi_x solves -Delta psi = h_x and (-psi_y, psi_x) = (-phi_xy, phi_xx)'] = \
    sp.simplify(-lap(psi) - sp.diff(h, x)) == 0 and sp.simplify(-sp.diff(psi, y) + sp.diff(phi, x, y)) == 0
for sgn, name in ((1, 'upper'), (-1, 'lower')):
    p0 = sgn * x ** 2 / 2
    chk[f'(6) {name} plateau: h_0 = -s, U[h_0] = (0, s), Dh_0 = 0 with s = {sgn}'] = \
        sp.simplify(-lap(p0) + sgn) == 0 and sp.diff(p0, x, y) == 0 and sp.diff(p0, x, 2) == sgn and \
        sp.diff(-lap(p0), x) == 0 and sp.diff(-lap(p0), y) == 0
# parities with explicit envelopes: chi even in x, theta(y) - theta(-y) odd in y
cx = sp.exp(-x ** 2); th = sp.Function('theta')
phi0 = x ** 2 / 2 * cx * (th(y) - th(-y))
chk['phi_0 even in x, odd in y; h_0 too'] = sp.simplify(phi0.subs(x, -x) - phi0) == 0 and sp.simplify(phi0.subs(y, -y) + phi0) == 0 and \
    sp.simplify((-lap(phi0)).subs(y, -y) - lap(phi0)) == 0
bx = sp.exp(-x ** 2); by = sp.exp(-(y - 3) ** 2) - sp.exp(-(y + 3) ** 2)
bb = bx * by
sgn_y = sp.sign(y)
hn = -A * lap(bb * sp.cos(n * y))
chk['b even in x, odd in y; h_n = -A Delta(b cos ny) S1; b_tilde = sign(y) b even in y'] = \
    sp.simplify(bb.subs(x, -x) - bb) == 0 and sp.simplify(bb.subs(y, -y) + bb) == 0 and \
    sp.simplify(hn.subs(x, -x) - hn) == 0 and sp.simplify(hn.subs(y, -y) + hn) == 0 and \
    sp.simplify((sgn_y * bb).subs(y, -y) - sgn_y * bb) == 0
# generic envelope
b = sp.Function('b')(x, y)
w = b * sp.cos(n * y)
hn = -A * lap(w)
gn = s * sp.diff(hn, y)
chk['(9) for constant s: s d_y h_n = -A d_y Delta(s b cos ny)'] = sp.simplify(gn - (-A * sp.diff(lap(s * w), y))) == 0
C, S = sp.symbols('C S')


def ndeg(expr):
    e = sp.expand(expr.subs({sp.cos(n * y): C, sp.sin(n * y): S}))
    return sp.Poly(e, n).degree()


H = {'xx': sp.diff(gn, x, 2), 'xy': sp.diff(gn, x, y), 'yy': sp.diff(gn, y, 2)}
deg = {k: ndeg(vv) for k, vv in H.items()}
chk['n-degrees of D^2 g_n entries: xx 3, xy 4, yy 5'] = deg == {'xx': 3, 'xy': 4, 'yy': 5}
lead = sp.expand(H['yy'].subs({sp.cos(n * y): C, sp.sin(n * y): S})).coeff(n, 5)
chk['leading yy coefficient: -A s b times d_y^5 cos(ny)/n^5 = -A s b (-sin ny)'] = sp.simplify(lead - (-A * s * b * (-S))) == 0
U1 = -A * sp.diff(w, x, y); U2 = A * sp.diff(w, x, 2)
Tn = sp.expand(U1 * sp.diff(hn, x) + U2 * sp.diff(hn, y))
chk['n-degrees: U1[h_n] 1, U2[h_n] 0, d_x h_n 2, d_y h_n 3'] = \
    (ndeg(U1), ndeg(U2), ndeg(sp.diff(hn, x)), ndeg(sp.diff(hn, y))) == (1, 0, 2, 3)
chk['T(h_n) has n-degree at most 3 and is quadratic in (cos ny, sin ny), i.e. frequencies 0 and 2n'] = \
    ndeg(Tn) <= 3 and all(sum(m[:2]) == 2 for m in sp.Poly(sp.expand(Tn.subs({sp.cos(n * y): C, sp.sin(n * y): S})), C, S).monoms())
An = 1 / (n ** 4 * L ** bt)
chk['scaling: A n^4 L^beta = 1, A n^5 L^beta = n, A^2 n^5 L^beta = n^-3 L^-beta, n^(-1/2) n = sqrt(n)'] = \
    sp.simplify(An * n ** 4 * L ** bt - 1) == 0 and sp.simplify(An * n ** 5 * L ** bt - n) == 0 and \
    sp.simplify(An ** 2 * n ** 5 * L ** bt - n ** -3 * L ** -bt) == 0 and sp.simplify(n ** sp.Rational(-1, 2) * n - sp.sqrt(n)) == 0
e1, e2 = sp.symbols('e1 e2', real=True)
diff_ = sp.expand(2 * (1 + n ** 2) * (1 + e1 ** 2 + e2 ** 2) - (1 + e1 ** 2 + (e2 + n) ** 2))
chk['(2): 2(1 + n^2)(1 + |eta|^2) - (1 + |eta + n e_y|^2) = 1 + e1^2 + (n - e2)^2 + 2 n^2 |eta|^2 >= 0'] = \
    sp.expand(diff_ - (1 + e1 ** 2 + (n - e2) ** 2 + 2 * n ** 2 * (e1 ** 2 + e2 ** 2))) == 0
out['sos_display'] = str(sp.factor(diff_))

# 2. FLOAT
Nn, Lb = 1024, 2.5
g1 = (np.arange(Nn) - Nn // 2) * (2 * Lb / Nn)
X, Y = np.meshgrid(g1, g1, indexing='ij'); dA = (2 * Lb / Nn) ** 2
k1 = 2 * np.pi * np.fft.fftfreq(Nn, d=2 * Lb / Nn)
KX, KY = np.meshgrid(k1, k1, indexing='ij'); K2 = KX ** 2 + KY ** 2


def bump(t):
    o = np.zeros_like(t); m = np.abs(t) < 1; o[m] = np.exp(-1 / (1 - t[m] ** 2)); return o


fh = np.fft.fft2; ifh = lambda f: np.real(np.fft.ifft2(f))
# compact S1 potential and velocity by symbols
ph = bump(X / 1.5) * (bump((Y - 1.5) / 1.2) - bump((Y + 1.5) / 1.2)) * (1 + X ** 2)
P = fh(ph)
hh = ifh(K2 * P)
Hh = fh(hh); K2s = np.where(K2 == 0, 1, K2)
U1 = ifh((KX * KY / K2s) * Hh)         # -R1R2 h: symbol -(i kx/|k|)(i ky/|k|) = kx ky/|k|^2
U2 = ifh(-(KX ** 2 / K2s) * Hh)        # R1^2 h: symbol (i kx/|k|)^2 = -kx^2/|k|^2
pxy = ifh(-KX * KY * P); pxx = ifh(-KX ** 2 * P)
err5 = max(np.abs(U1 + pxy).max(), np.abs(U2 - pxx).max())
chk['(5) FLOAT: symbol velocity of h = -Delta phi equals (-phi_xy, phi_xx) for a compact S1 potential'] = err5 < 1e-9
out['err5_FLOAT'] = float(err5)
benv = bump(X / 0.45) * (bump((Y - 1.5) / 0.24) - bump((Y + 1.5) / 0.24))
sgn = np.sign(Y); btil = sgn * benv
nb = np.sqrt(np.sum(benv ** 2) * dA)
res = {}
NS = (32, 64, 128, 256)
for beta in (1.0, 0.0):
    Qs = (1 + np.log1p(K2)) ** beta
    rows = []
    for nn in NS:
        Ln = 1 + np.log1p(nn ** 2); An_ = 1 / (nn ** 4 * Ln ** beta)
        wv = fh(btil * np.cos(nn * Y))
        Gn = -An_ * (1j * KY) * (-K2) * wv        # g_n = -A d_y Delta(b_tilde cos ny)
        QG = Qs * Gn
        hxx, hxy, hyy = ifh(-KX ** 2 * QG), ifh(-KX * KY * QG), ifh(-KY ** 2 * QG)
        top = np.sqrt(np.sum(hxx ** 2 + 2 * hxy ** 2 + hyy ** 2) * dA)
        # self interaction T(h_n) with h_n = -A Delta(b cos ny)
        Wn = fh(benv * np.cos(nn * Y))
        hn = ifh(An_ * K2 * Wn)
        u1 = ifh(An_ * KX * KY * Wn); u2 = ifh(-An_ * KX ** 2 * Wn)
        Tn = u1 * ifh(1j * KX * fh(hn)) + u2 * ifh(1j * KY * fh(hn))
        QT = Qs * fh(Tn)
        txx, txy, tyy = ifh(-KX ** 2 * QT), ifh(-KX * KY * QT), ifh(-KY ** 2 * QT)
        ttop = np.sqrt(np.sum(txx ** 2 + 2 * txy ** 2 + tyy ** 2) * dA)
        rows.append({'n': nn, 'top_g_over_n': float(top / nn), 'top_T': float(ttop)})
    res[f'beta={beta}'] = rows
    rat = [r_['top_g_over_n'] / (nb / np.sqrt(2)) for r_ in rows]
    for r_, q_ in zip(rows, rat):
        r_['ratio_to_limit'] = float(q_)
    chk[f'(10) FLOAT beta = {beta}: ||D^2 Q g_n||/n / (||b||/sqrt 2) approaches 1 monotonically (n = 32 .. 256)'] = \
        all(abs(rat[i + 1] - 1) < abs(rat[i] - 1) for i in range(len(rat) - 1)) and abs(rat[-1] - 1) < 0.1
    chk[f'(11) FLOAT beta = {beta}: top component of T(h_n) decays at least like n^-2 (n = 32 .. 256)'] = \
        rows[-1]['top_T'] <= rows[0]['top_T'] * (NS[0] / NS[-1]) ** 2
out['FLOAT'] = {'norm_b': float(nb), 'rows': res}
out['checks'] = {k: bool(v) for k, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k for k, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
