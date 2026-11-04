# T2_FAR_C5_v01: rows C5a and C5b of the 013 far owner table (parity, smoothness, symbol class and Fourier hypotheses of Lemma HSB for the complete 013 far piece)

Agent the second theory agent, written 2026-11-03T14:26Z for the coordinator 14:05Z item 4(b) ("the second theory agent takes, in order, C5a, C5b and C1,
then the assembly F ... each item goes to the theory auditor when it is ready"). Rows C5a and C5b are those of
notes/T2_013_FAR_OWNERS_v01.md section 2.1. Theorems C5a and C5b below are CLAIMED here and submitted to the theory auditor. Their
proofs use only the exact representation of the two inputs; the evidence that the inputs have the stated structure
is an exact rational check (code/c5_check.py, Part A). Paths are relative to research/h4/far009/ of agent the second theory agent unless
another agent is named. No far constant is certified in this note: every statement about S_h, M2 or the envelopes of
the transform is a finiteness statement without an enclosed value.

## 0. Summary

1. C5a (Theorem C5a). The complete 013 far piece a_f is real, C-infinity on R^2, bounded, and even in x_1 and in
   x_2. It is exactly a finite sum a_f(r, theta) = sum over k = 0, ..., 80 of f_k(r) cos(2 k theta) (the largest
   angular frequency is 160). Its transform is real and even in xi_1 and in xi_2, and the Schur rows of Lemma HSB with
   a weight invariant under the two reflections take the same value at xi and at its reflections.
2. C5b (Theorem C5b). a_f lies in the symbol class S^(-lambda), lambda = 1 - 1/c = 1824676646553933/4076476460239181
   (about 0.4476): for every multi-index beta, A_beta = sup over x of <x>^(lambda + |beta|) |d^beta a_f(x)| is finite.
   With AT-1021 (the theory auditor, the Fourier lemma of research/theory_v11_scope_audit/PROOF.md, CONFIRMED conditionally on
   exactly these derivative bounds) this gives: a_f^ is a function; for every integer N >= 3 it obeys the envelopes
   |a_f^(xi)| <= C0(N) |xi|^(lambda - 2) for |xi| <= 1 and <= Cinf(N) |xi|^(-N) for |xi| >= 1 with finite constants;
   every moment (2 pi)^-2 int |zeta|^p |a_f^| with p >= 0 is finite (so M0, M2, int |a^| <zeta>^(q+1) and M2[w_new]
   are finite); and the Schur supremum S_h of NR-21 (cases O and B, so S_h^B of Lemma HSB) is finite for every
   measurable weight with h(eta)/h(xi) <= C_h <xi - eta>^(s_h), which includes h = 1, the Perron weights of
   code/hsb_far.py with positive node values and h = <xi>^-s for every real s.
3. Consequence. The hypotheses of Lemma HSB (T2_FAR_v02 section 2.3), of Corollary HSB-R, of NR-21 cases (O) and (B)
   and item C5 of T2_FAR_v02 section 3.1 hold for the unwindowed 013 far piece at every erflog or log cut, in
   particular at erflog 8, rho 1 and at log 16, rho 2. For route F-a (NR-26, AT-911) the windowed piece a_W is in
   C_c-infinity and the tail a_t lies in S^(-lambda), so the hypotheses of Lemma HSB hold for a_W and those of the OMF
   baseline (AT-665: real, bounded, finite osc, M2 and M2[w_new]) hold for a_t. This fills, for the 013 source, the
   premise that AT-1021 left OPEN ("No source013 constants A_beta, B0, BN are enclosed here") in its qualitative form.
4. Not done. The constants A_beta, and so C0, Cinf and the moment bounds of AT-1021, are not enclosed. C1 needs
   explicit A_beta for |beta| <= 2 on r >= R_ext (the exterior part of SC^+); C3 and FA5 need explicit C0, Cinf or
   an equivalent majorant. The finiteness of S_h is qualitative: the bound of section 4 contains the factor
   sup h/inf h, which is 3.0e3 for the saved Perron weight at Rw 50 (runs/hsb_erflog_lam8_b18s2_N2048_RW50.json,
   B_8pi_K0.25) and is not a usable number.

## 1. The objects

Constants. c = 4076476460239181/2251799813685248 (cl_exact of data/C1-N1-007_exact.json and c_exact of
inputs013/phi_007_b18s2_phi_exact.json, equal), q = 21/10, gamma = 1/c, lambda = 1 - 1/c, mu = 4/c - 3.

Candidate 007 (unchanged; data/C1-N1-007_exact.json, SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21,
the unchanged 007 raw hash of the theory auditor reports/SOURCE013_CHAIN_CONDITIONS_v01.md). Its format string reads "chi = sum
coef * H_m (1+r^2)^(p-m) T(t), T = t^h (mono) or t^w P_n(2t-1) (leg); p = (3+gamma-j lambda)/2 for branch j; coef exact
rational", with H_m = Re (x + i y)^(2m), R = 1 + r^2 and t = r^2/R (code/lib/ipm_exact.py, header). The fields are
psi = chi_xy and U_007 = (-psi_y, psi_x) (same header). There are 2982 generators.

C2-N1-013 correction (inputs013/phi_007_b18s2_phi_exact.json, SHA256
a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, the raw correction hash of
SOURCE013_CHAIN_CONDITIONS_v01). Its definition string reads "phi = sum coefficient_exact Im(x+iy)^n (x^2+y^2)^h
(1+x^2+y^2)^b_exact (scale_exact+x^2+y^2)^(-d); ... U[h_phi] = (-phi_xy, phi_xx)", and an atom with legendre_degree k
carries the extra factor P_k(2 ts - 1), ts = (x^2 + y^2)/(scale_exact + x^2 + y^2). There are 12273 atoms. The
center is u_star = U_007 + v with v = (-phi_xy, phi_xx) (SOURCE013_CHAIN_CONDITIONS_v01).

Far coefficient. atil_013(X) = (4 u_star(X).X - c)/(1 + 4 |X|^2) on R^2, the coefficient of T2_FAR_v02 and
T2_013_FAR_OWNERS_v01 section 1. Split into atil_007 = (4 U_007.X - c)/(1 + 4|X|^2) and datil_013 =
4 v.X/(1 + 4|X|^2).

Cuts and windows. For lam > 1 and rho > 0, the erflog cut is chi_E(r) = (1/2)(1 + erf((log r - y0)/sigma)) with
y0 = log(rho lam^(1/2)) and sigma = log(lam)/(2 pi^(1/2)), and the log cut is chi_L(r) = Sinf(log(r/rho)/log(lam))
(code/hsb_far.py, function cutf). Sinf(t) = e0/(e0 + e1) with e0 = exp(-1/t) for t > 0, e0 = 0 for t <= 0,
e1 = exp(-1/(1 - t)) for t < 1, e1 = 0 for t >= 1 (code/hsb_far.py, function Sinf). The far piece is
a_f(x) = chi(|x|) atil_013(x) with chi = chi_E or chi_L, unwindowed and with all angular modes. For Rw > 0, Ww > 0
put W(x) = Sinf((|x| - Rw)/Ww), a_W = a_f (1 - W) and a_t = a_f W (NR-26).

## 2. Symbol classes

Definition. For m real, S^m is the set of f in C-infinity(R^2) such that for every multi-index beta there is a finite
C_beta with |d^beta f(x)| <= C_beta <x>^(m - |beta|) for all x, where <x> = (1 + |x|^2)^(1/2).

Lemma S1 (closure; standard). Let m, m' be real.
(a) S^m is contained in S^m' when m <= m', and S^m + S^m' is contained in S^max(m, m').
(b) A polynomial of degree n lies in S^n. In particular x_1, x_2 lie in S^1.
(c) For s > 0 and e real, (s + |x|^2)^e lies in S^(2e).
(d) S^m S^m' is contained in S^(m + m').
(e) d_j maps S^m into S^(m - 1), and d_theta = x_1 d_2 - x_2 d_1 maps S^m into S^m.
(f) A polynomial in an element of S^0 lies in S^0.

Proof. (a) <x>^(m - |beta|) <= <x>^(m' - |beta|). (b) d^beta P is a polynomial of degree at most n - |beta| (zero if
|beta| > n), and a polynomial of degree k is bounded by C <x>^k. (c) By induction on |beta|, d^beta (s + |x|^2)^e is
a finite sum of terms c (s + |x|^2)^(e - i) Q(x) with i <= |beta| and Q a polynomial of degree at most 2 i - |beta|;
since min(1, s) <x>^2 <= s + |x|^2 <= max(1, s) <x>^2, each term is bounded by C <x>^(2e - 2i + 2i - |beta|).
(d) Leibniz rule. (e) The first statement is the definition; the second follows from (b), (d) and the first.
(f) From (d) and (a). QED.

Lemma S2 (cuts and windows). Let lam > 1, rho > 0, Rw > 0, Ww > 0.
(a) The function G_E(x) = chi_E(|x|) for x != 0, G_E(0) = 0, is C-infinity on R^2, all its derivatives vanish at
    x = 0, and G_E lies in S^0.
(b) G_L(x) = chi_L(|x|) (G_L = 0 on |x| <= rho) is C-infinity, lies in S^0, vanishes on |x| <= rho and equals 1 on
    |x| >= rho lam.
(c) W(x) = Sinf((|x| - Rw)/Ww) is C-infinity, lies in S^0, vanishes on |x| <= Rw and equals 1 on |x| >= Rw + Ww; so
    1 - W lies in C_c-infinity with support in |x| <= Rw + Ww.

Proof. Sinf is C-infinity on R with Sinf = 0 on t <= 0 and Sinf = 1 on t >= 1, since e0 and e1 are C-infinity,
nonnegative and e0 + e1 > 0 everywhere. Hence G_L and W are C-infinity: each is constant on a neighbourhood of the
origin and is a C-infinity function of |x| on x != 0. Their derivatives of order >= 1 vanish outside a bounded
annulus, so G_L and W lie in S^0; this proves (b) and (c).
(a) Put F(y) = (1/2)(1 + erf((y - y0)/sigma)) and g(r) = F(log r) for r > 0. For i >= 1, F^(i)(y) is a polynomial in y
times exp(-(y - y0)^2/sigma^2), so for every M >= 0 there is C with |F^(i)(y)| <= C exp(-M |y|) for all y, and also
F(y) <= C exp(-M |y|) for y <= 0. By induction, g^(j)(r) = r^(-j) sum over 1 <= i <= j of c_(j,i) F^(i)(log r) for
j >= 1, with integer constants c_(j,i), since d/dr [r^(-j) F^(i)(log r)] = r^(-j-1) (F^(i+1)(log r) - j F^(i)(log r)). Hence for every M and j there is C
with |g^(j)(r)| <= C r^M on 0 < r <= 1, and |g^(j)(r)| <= C r^(-j) on r >= 1. On x != 0, d^beta (g(|x|)) is a finite
sum of terms g^(i)(|x|) H_(beta,i)(x), 0 <= i <= |beta|, with H_(beta,i) C-infinity on x != 0 and homogeneous of degree
i - |beta| (chain rule; d^gamma |x| is homogeneous of degree 1 - |gamma|). So |d^beta G_E(x)| <= C |x|^M for every M
on 0 < |x| <= 1 and |d^beta G_E(x)| <= C |x|^(-|beta|) on |x| >= 1. Every derivative of G_E on x != 0 therefore
extends continuously by 0 to x = 0. A function that is continuous on R^2, C^1 on R^2 minus the origin, and whose
gradient extends continuously to the origin is C^1 on R^2 with that gradient (mean value theorem on segments that avoid
the origin, then continuity); applied inductively to the derivatives, G_E is C-infinity with all derivatives 0 at the
origin. The two bounds give G_E in S^0. QED.

## 3. Theorem C5a (parity and angular structure)

Theorem C5a. Let a_f = chi(|x|) atil_013(x) with chi = chi_E or chi_L as in section 1, built from the two inputs of
section 1 with the structure verified in section 5 (Part A). Then:
(i) a_f is real-valued and C-infinity on R^2, and bounded.
(ii) a_f(-x_1, x_2) = a_f(x_1, x_2) = a_f(x_1, -x_2) for all x.
(iii) In polar coordinates, a_f(r, theta) = sum over k = 0, ..., 80 of f_k(r) cos(2 k theta) for r > 0, with f_k
     C-infinity on r > 0. The 007 part has angular frequencies 2 m +- 2 with m <= 79, the 013 part n +- 1 with n odd,
     n <= 159; the largest frequency is 160 in both.
(iv) a_f^ is real and even in xi_1 and in xi_2. For a weight h that is invariant under the reflections
     (xi_1, xi_2) -> (-xi_1, xi_2) and (xi_1, xi_2) -> (xi_1, -xi_2) (in particular any radial h), the Schur row
     rho_h(xi) of NR-21 (both cases) and the HSB row rho_h^B(xi) take the same value at xi and at both reflections of
     xi, so their supremum may be taken over the closed first quadrant (item C4 (i) of T2_FAR_v02 section 3.1).
(v) The Hessian expression E(x) = (1/2)[(q^2 - 1) lambda_max D^2 a_f(x) + Delta a_f(x)] of SC is invariant under
     the two reflections of x, so SC(a_f) = sup over the closed first quadrant of max(0, E).

Proof. (i) Every coefficient in the two inputs is rational and every factor is real-valued, so a_f is real. Each
007 generator coef H_m (1 + r^2)^(p - m) T(t) is C-infinity on R^2: H_m is a polynomial, 1 + r^2 > 0, and T(t) is a
polynomial in the C-infinity function t = r^2/(1 + r^2), because h, w, n are nonnegative integers (Part A). Each 013
atom is C-infinity on R^2: Im(x + i y)^n and (x^2 + y^2)^h are polynomials (h a nonnegative integer, Part A), and
1 + r^2 and scale_exact + r^2 are positive (scale_exact > 0, Part A), as is the argument of P_k. Hence chi_007, psi,
U_007, phi, v and atil_013 = (4 (U_007 + v).X - c)/(1 + 4 |X|^2) are C-infinity on R^2, and a_f is C-infinity by
Lemma S2. Boundedness follows from Theorem C5b (a_f lies in S^(-lambda), contained in S^0).
(ii) H_m(x) = r^(2m) cos(2 m theta) is invariant under theta -> -theta and theta -> pi - theta, and the other factors
of a generator are radial, so chi_007 is even in x_1 and in x_2. Then psi = d_1 d_2 chi_007 is odd in x_1 and odd in
x_2, psi_y is odd in x_1 and even in x_2, psi_x is even in x_1 and odd in x_2, and U_007.X = -x_1 psi_y + x_2 psi_x is
even in both. For an atom, Im(x + i y)^n = r^n sin(n theta) is odd under theta -> -theta and, n being odd (Part A),
invariant under theta -> pi - theta (sin(n pi - n theta) = sin(n theta)); the other factors are radial. So phi is
even in x_1 and odd in x_2, phi_xy is odd in x_1 and even in x_2, phi_xx is even in x_1 and odd in x_2, and
v.X = -x_1 phi_xy + x_2 phi_xx is even in both. The factors 1/(1 + 4 |X|^2) and chi(|x|) are radial.
(iii) Write d = (1/2)(d_1 - i d_2) and dbar = (1/2)(d_1 + i d_2). For a radial f, d (f(r) e^(i n theta)) =
(1/2)(f' + (n/r) f) e^(i (n - 1) theta) and dbar (f(r) e^(i n theta)) = (1/2)(f' - (n/r) f) e^(i (n + 1) theta).
Since d_1 = d + dbar, d_2 = i (d - dbar) and d_1 d_2 = i (d^2 - dbar^2), the field psi of a generator with H_m has the
frequencies 2 m - 2 and 2 m + 2 (in absolute value), and phi_x of an atom has n - 1 and n + 1. The operator
d_theta keeps each frequency, and U_007.X = -d_theta psi, v.X = -d_theta (phi_x) (from U_007 = (-psi_y, psi_x),
v = (-phi_xy, phi_xx) and d_theta = x_1 d_2 - x_2 d_1). Multiplication by radial functions keeps frequencies. With
m_max = 79 and n_max = 159 (Part A) every frequency is at most 160, and by (ii) only cos(2 k theta) occurs.
(iv) a_f is real and even in each variable, so a_f^ (the distributional transform; a function by Theorem C5b) is real
and even in each variable. Let R be one of the two reflections. Ktil and P depend on xi and eta only through |xi|,
|eta|, w.w' and (zeta.w)(zeta.w'), which are invariant when R is applied to both; so are phi(|xi|), theta(|xi|) and
the corresponding factors at eta, hence r_L(R xi, R eta) = r_L(xi, eta). Substituting eta = R eta' in the row integral
and using |a_f^(R zeta)| = |a_f^(zeta)| and h(R eta')/h(R xi) = h(eta')/h(xi) gives rho_h(R xi) = rho_h(xi).
(v) a_f(R x) = a_f(x) gives D^2 a_f(R x) = R D^2 a_f(x) R^T, which has the same eigenvalues and trace. QED.

## 4. Theorem C5b (symbol class and the Fourier hypotheses)

Theorem C5b. Let a_f be as in Theorem C5a. Then:
(i) a_f lies in S^(-lambda), lambda = 1 - 1/c. More precisely atil_007 + c/(1 + 4|X|^2) lies in S^(2 p_max - 4) with
    2 p_max - 4 = -lambda, datil_013 lies in S^(tau_max - 3) with tau_max = mu, and -c/(1 + 4|X|^2) lies in S^(-2).
(ii) (with AT-1021) The distributional transform a_f^(xi) = int exp(-i x.xi) a_f(x) dx is a function. For every integer
    N >= 3 there are finite constants C0(N), Cinf(N) (those of AT-1021 with gamma = lambda, built from A_beta,
    |beta| <= N) with |a_f^(xi)| <= C0(N) |xi|^(lambda - 2) for 0 < |xi| <= 1 and |a_f^(xi)| <= Cinf(N) |xi|^(-N) for
    |xi| >= 1. There is no point mass at xi = 0.
(iii) For every real p >= 0, (2 pi)^-2 int |zeta|^p |a_f^(zeta)| d zeta is finite, at most
    (1/(2 pi)) [C0(N)/(p + lambda) + Cinf(N)/(N - p - 2)] for any integer N > p + 2. In particular M0 + M2 =
    (2 pi)^-2 int (1 + |zeta|^2) |a_f^| is finite, int |a_f^| <zeta>^(q + 1) is finite, and M2[w_new] =
    (2 pi)^-2 int |zeta|^2 w_new(|zeta|) |a_f^| with w_new(t) = H_q(asinh(t/2)) is finite (AT-1021:
    t^2 H_q(asinh(t/2)) <= 2^(q - 1)(t^2 + t^(q + 1))).
(iv) Let phi, theta : [0, infinity) -> [0, 1] be measurable, L = |w - w'|^2 (case O) or L = Ktil (case B), and r_L as
    in NR-21. Let h > 0 be measurable with h(eta)/h(xi) <= C_h <xi - eta>^(s_h) for all xi, eta, for some finite
    C_h >= 1 and s_h >= 0. Then the rows of NR-21 satisfy, for every xi,
      rho_h(xi) <= C_h (2 pi)^-2 int (1/2) |a_f^(zeta)| (kappa(|zeta|) + q^2 |zeta|^2 + 4) <zeta>^(s_h) d zeta,
    kappa(s) = (2 + s)^2 + q^2 s^2 (1 + s)^(q - 1), and the right side is finite. So S_h and, with
    r_B = (1 - theta theta') Ktil - phi phi' P, the HSB supremum S_h^B are finite. The class of weights contains
    (a) every measurable h with 0 < inf h <= sup h < infinity (C_h = sup h/inf h, s_h = 0), in particular h = 1 and
    every Perron weight of code/hsb_far.py with positive node values (values at 32 nodes u_j = log<r_j>, linear in u
    between them and constant outside), and (b) h = <xi>^-s for every real s (C_h = 2^(|s|/2),
    s_h = |s|, Peetre's inequality).
(v) The same conclusions (i) to (iv) hold for a_t = a_f W and for a_f with chi_L in place of chi_E. The windowed
    piece a_W = a_f (1 - W) lies in C_c-infinity with support in |x| <= Rw + Ww, so a_W^ is a Schwartz function and
    (ii) to (iv) hold for a_W with every moment finite.

Proof. (i) Generators: H_m is a polynomial of degree 2 m, in S^(2m) (Lemma S1 (b)); (1 + r^2)^(p - m) lies in
S^(2p - 2m) (S1 (c)); t = 1 - (1 + r^2)^-1 lies in S^0 (S1 (a), (c)), so T(t) lies in S^0 (S1 (f)). By S1 (d) each
generator lies in S^(2 p_j), and by S1 (a) chi_007 lies in S^(2 p_max). By S1 (e), psi = d_1 d_2 chi_007 lies in
S^(2 p_max - 2) and U_007.X = -d_theta psi lies in S^(2 p_max - 2). The factor 4/(1 + 4|X|^2) = (1/4 + |X|^2)^-1
lies in S^-2, so 4 U_007.X/(1 + 4|X|^2) lies in S^(2 p_max - 4). Part A gives p_max = p_0 = (3 + 1/c)/2 =
14481229194402791/8152952920478362 exactly (the branches are j = 0, ..., 7 and p_j decreases in j), so
2 p_max - 4 = 1/c - 1 = -lambda.
Atoms: Im(x + i y)^n lies in S^n, (x^2 + y^2)^h in S^(2h), (1 + r^2)^b in S^(2b), (s + r^2)^-d in S^(-2d) for s > 0
and every integer d, and P_k(2 ts - 1) in S^0 since ts = 1 - s (s + r^2)^-1 lies in S^0. So an atom lies in
S^(tau), tau = n + 2 h + 2 b - 2 d, and phi lies in S^(tau_max) with tau_max = mu exactly (Part A: tau <= mu for every
atom, with equality attained). Then phi_x lies in S^(mu - 1), v.X = -d_theta (phi_x) in S^(mu - 1) and datil_013 in
S^(mu - 3); mu - 3 = 4/c - 6 is about -3.79.
The constant part -c/(1 + 4|X|^2) lies in S^-2. Since mu - 3 < -2 < -lambda, atil_013 lies in S^(-lambda) by
S1 (a). Finally a_f = G atil_013 with G = G_E or G_L in S^0 (Lemma S2), so
a_f lies in S^(-lambda) by S1 (d).
(ii) and (iii). By (i), a_f is C^N for every N and satisfies |d^beta a_f(X)| <= A_beta <X>^(-lambda - |beta|) for all
|beta| <= N with finite A_beta. Since 0 < lambda < 2, the hypotheses of the AT-1021 lemma hold with gamma = lambda for
every integer N >= 3. Its conclusions are (ii) and the moment bound of (iii) for 0 <= p < N - 2; given p, take
N > p + 2. M2[w_new] is finite by the inequality quoted in (iii) and the moments p = 2 and p = q + 1.
(iv) Since 0 <= phi, theta <= 1, |w.w'| <= 1 and |zeta.w| <= |zeta|, one has |P| <= |zeta|^2 + (q^2 - 1) |zeta|^2 =
q^2 |zeta|^2. In case (O), |r_L| <= Ktil + |P| + |w - w'|^2 <= Ktil + q^2 |zeta|^2 + 4. In case (B),
r_L = (1 - theta theta') Ktil - phi phi' P with 0 <= 1 - theta theta' <= 1 and Ktil >= 0, so |r_L| <= Ktil +
q^2 |zeta|^2. NR-23 (PROVED, AT-845) gives Ktil(xi, eta) <= kappa(|xi - eta|). Insert these bounds and
h(eta)/h(xi) <= C_h <xi - eta>^(s_h) into the row and substitute zeta = xi - eta. The integrand of the right side is
at most C (1 + |zeta|^(q + 1 + s_h)) |a_f^(zeta)|, because (2 + s)^2 <= 8 + 2 s^2 and
s^2 (1 + s)^(q - 1) <= 2^(q - 2) (s^2 + s^(q + 1)) (q - 1 >= 1 and convexity), so the right side is finite by (iii).
For (a), h(eta)/h(xi) <= sup h/inf h. An interpolation that is linear between positive node values and constant
outside is bounded above and below by the largest and the smallest node value. (In the saved rows read for this note,
erflog 8 at rho 0.9, 1 and 1.25 with Rw 50, Ww 10 and at rho 1 with Rw 100, Ww 100, the node values are positive;
the smallest is 3.3e-4 of the largest for B_8pi_K0.25 at rho 1, Rw 50, and 9.1e-7 at Rw 100, Ww 100.) For (b), Peetre's inequality <xi>^t <= 2^(|t|/2) <xi - eta>^|t| <eta>^t (t real) with t = s gives
h(eta)/h(xi) = (<xi>/<eta>)^s <= 2^(|s|/2) <xi - eta>^|s|.
(v) a_t = a_f W with W in S^0 (Lemma S2 (c)) lies in S^(-lambda), and the proofs of (ii) to (iv) apply. With chi_L
the proof of (i) is unchanged (Lemma S2 (b)). a_W = a_f (1 - W) is C-infinity with compact support (Lemma S2 (c)),
so a_W^ is a Schwartz function, and the integrals of (iii) and (iv) are finite. QED.

Corollary C5 (hypotheses of the far lemmas for the 013 source). Under the structure verified in Part A, for every
erflog or log cut (lam > 1, rho > 0), in particular erflog 8, rho 1 and log 16, rho 2:
(a) the unwindowed far piece a_f satisfies the hypotheses of NR-21 (cases O and B), of Lemma HSB and of Corollary
    HSB-R (T2_FAR_v02 sections 2.3 and 2.4) and item C5 of T2_FAR_v02 section 3.1, with S_h^B finite for h = 1, for
    the Perron weights and for h = <xi>^-s (every real s), and with any 0 <= K < K';
(b) for route F-a (NR-26) at any Rw > 0, Ww > 0 (so also Ww = Rw, AT-1012), a_W satisfies the hypotheses of Lemma
    HSB and a_t those of the OMF baseline (AT-665: real, bounded, finite osc, M2 and M2[w_new]);
(c) the Fourier premise of V11-4 that AT-1021 left OPEN holds for the 013 source in the form "A_beta finite for
    every beta"; the enclosure of A_beta, B0, BN is not done.
Nothing in the corollary bounds a far constant. The certified inputs SC^+, A_low^+ or A_E^+, S^+ and OMF^+ remain
those of rows C1 to C4 and FA1 to FA5 of T2_013_FAR_OWNERS_v01.

Remarks.
1. On the necessary conditions of T2_FAR_v02 Remark 3 (AT-797). For a_f these hold for every s, so the restriction
   0.6 < s <= 1.4 discussed there (for a hypothetical |zeta|^(-9/2) envelope of spline profiles) does not arise for
   the 013 representation, and the Perron weight extended constantly is admissible. The obstacle of AT-800 (no decay
   envelope for the spline field of 009) concerned the 009 FLOAT representation; the theorem above is about the exact
   013 representation, not about the grid field used by the FLOAT codes.
2. Sharpness is not used: if the leading coefficients of order -lambda cancel, a_f lies in a smaller class and the
   conclusions hold a fortiori. The exponent agrees with the FLOAT decay of order r^(-0.448) reported by the second numerics agent.
3. Angular truncation. Theorem C5a (iii) makes the omitted modes of the FLOAT rows (8 kept, reading 6 of
   T2_013_FAR_OWNERS_v01) a finite list: k = 8, ..., 80. A certificate can keep all 81 modes.
4. The constants A_beta, C0 and Cinf depend on the cut parameters and on Rw and Ww. Only finiteness is claimed.

## 5. Evidence: code/c5_check.py

Run from research/h4/far009/ with the campaign interpreter (Python 3.12.13, python-flint 0.9.0):
python3 code/c5_check.py runs/c5_check_1413.json > runs/c5_check_1413.out (Part B took 8.4 s).

Part A (exact rational arithmetic, fractions.Fraction). Results (runs/c5_check_1413.out):

| check | result |
|---|---|
| SHA256 of the 013 input | a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a |
| SHA256 of the 007 input | ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21 |
| c equal in both files; mu_exact = 4/c - 3 | yes (assertions) |
| 013 atoms | 12273; n odd and positive (n_max 159); h >= 0 integer (h_min 0); d integer in [0, 80]; legendre_degree integer in [0, 24]; scale_exact > 0; tau_exact = n + 2h + 2b - 2d for every atom; tau <= mu for every atom; tau_max = mu = -3222230125976551/4076476460239181; 0 failures |
| 007 generators | 2982; m >= 0 integer (m_max 79); spec 'mono' with h >= 0 integer or 'leg' with w, n >= 0 integers; branch j integer in {0, ..., 7} with p_j = (3 + 1/c - j(1 - 1/c))/2 (equal to ipm_exact.p_branch); p_max = 14481229194402791/8152952920478362; 0 failures |
| symbol orders | atil_007: 2 p_max - 4 = -1824676646553933/4076476460239181 = -lambda; datil_013: tau_max - 3 = -15451659506694094/4076476460239181 (about -3.79); constant part -2; atil: -lambda |
| largest angular frequency | 160 (007: 2 m_max + 2; 013: n_max + 1) |

Part B (arb at 256 bits; spot checks of the formulas against the FLOAT fields, not part of any proof). At five grid
nodes of runs/main.json (r = 0.5, 0.757, 1.99, 7.96, 63.4):
- atil_007 from the closed form U_007.X = -d_theta (chi_xy), evaluated on the 1922 canonical terms of
  ipm_exact.generators_to_terms, agrees with the FLOAT library field runs/main_atil.npy to relative differences
  4e-14 to 2.4e-12;
- datil_013 = 4 v.X/(1 + 4|X|^2) from the 12273 atoms in Legendre form agrees with the binary64 field
  runs/main_b18s2_datil.npy (code/corr_datil.py) to relative differences 1.6e-6 to 3.1e-5 (absolute at most 4e-9;
  the binary64 code works with rounded coefficients);
- the parity: the upper ends of |f(r, theta) - f(r, -theta)| are at most 7.4e-56 for atil_007 and 2.4e-65 for
  datil_013, within twice the radii of the arb balls (at most 3.7e-56 and 1.2e-65). Those of
  |f(r, theta) - f(r, pi - theta)| are at most 2.6e-16 and 1.0e-18; the angle pi - theta is formed in binary64, and
  these differences are of the size of that rounding times the angular derivative.

## 6. What C1 and C3 need from here

1. C1 (SC^+ on R^2). Theorem C5a (iii) and (v) reduce the evaluation to 81 radial mode functions and the first
   quadrant. Beyond a radius R_ext, C1 needs an explicit bound of |D^2 a_f| there, that is explicit A_beta for
   |beta| <= 2 on |x| >= R_ext (or a direct bound of the second derivatives of the mode functions); the proof of (i)
   gives it term by term once each factor's derivative bounds are enclosed. How much the coefficient sums cancel at
   large r is not yet measured (the elementary form of the 013 atoms has large cancelling coefficients, per the
   legendre_convention string of the input); if they do, a bound by the sum of the absolute values of the terms is
   usable only far out, and the region up to R_ext must be covered by panels.
2. C3 and FA5 need explicit C0(N), Cinf(N) (AT-1021: from B0 and BN of the dyadic pieces) or an equivalent majorant
   of |a^|. This note does not supply them.
3. F (assembly) will cite Corollary C5 for the hypotheses and state the remaining certified inputs.
