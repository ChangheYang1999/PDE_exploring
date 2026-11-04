# T2_EXP_v01: explicit constants at P-S1 and the AT-064 tuples (c_W, c_4', C_eps_bar), closure v3, and the
# corrections to T2_TT_v01 from AT-103 to AT-114

Version 1. Owner: the second theory agent (theory agent). Written 2026-11-02T23:25Z.
Requested by theory_v01 T2.4 (explicit constants, owned by the second theory agent), the coordinator 20:28Z item 3(a) (second priority: the c_4'
and c_W route) and the coordinator 22:06Z item 3(e) (carry AT-103 to AT-109 into T2_TT and the theory_v02 inputs; explicit
constants at P-S1 = (21/10, 1, 1/2): c_W(2), c_W(3), c_4', C_eps_bar).
Plain-text mathematics as in T2_TT_v01. Paths are relative to the combined2 root.

Inputs used (read-only): theory_audit/exchange/audit_v48.md (AT-103 to AT-109), audit_v49.md (AT-110 to AT-114), audit_v55.md
(AT-128), audit_v56.md to audit_v58.md (AT-131 to AT-135, an audit of a draft of this note) with the standalone proofs
they index; theory_agent_2/notes/T2_TT_v01.md (SHA256 36891bdc...), T2_WGK_v01.md, T2_REV_v01.md;
an external referee answer (SHA256 fc0fab831a4f51e58f68972ba8cb361817f4e3f76e737c3e3880a7211a142a53);
the coordinator team notes 22:06Z.
Scripts (theory_agent_2/research/explicit/, Python): cw_ub.py, cw_hom_ub.py, cw_power.py, cw_power_big.py, cw_hom.py, cw_ps1.py,
cw_end.py, cw_box.py, cw_box2.py, cw_box3.py, closure_fn_v3.py, closure_fn_v4.py, closure_cert_v2.py,
closure_scaling.py, each with its .out file (closure_fn_v4.py has no .out; its self-test is printed by running it);
theory_agent_2/scratch/exp/q115_check.py (+ .out). SHA256 values are in theory_agent_2/scratch/exp/freeze.log.
Changes after the theory auditor audit of the draft (audit_v56 to audit_v58): the cw_hom_ub.py values are FLOAT, not a
certificate (AT-133); the P-S1 inputs are the exact rational bounds of AT-135; the closing set in M is a union of at
most two intervals, not one (AT-134), and the tables of section 4 are recomputed in the branch form (closure_fn_v4.py)
with component lists; closure_cert.py and closure_minterval.py were not run and are superseded.

## Summary

| ID | statement | label | section |
|---|---|---|---|
| T2-CW-Q | c_W(q) <= c_W(2)^(3-q) c_W(3)^(q-2), S1 and homogeneous consequences | PROVED (AT-109) | 2.2 |
| T2-EXP-HI | the same interpolation for the homogeneous constant c^hom(q) = \|\| \|D\|^q W^(-1) J^(-q) \|\|, on S1 | PROVED (AT-131) | 2.2 |
| T2-EXP-CWF | full-space endpoint bounds by Leibniz and Sobolev (the "lin" route); at P-S1 c_W(2) <= 3.0887, c_W(3) <= 6.7253, c_W(21/10) <= 3.3386 | UB (FLOAT inputs) | 2.3 |
| T2-EXP-CWH | S1 homogeneous endpoint bounds with an S1 Hardy inequality and the dual bound; at P-S1 c_2 <= 1773/1000, c_3 <= 508/125, c^hom_(S1)(21/10) <= 1927/1000 | method PROVED (AT-131, AT-132); P-S1 values EXACT UB (AT-135); cw_hom_ub.py values FLOAT (AT-133) | 2.4 |
| T2-EXP-CWV | power-iteration values of the four c_W variants | FLOAT | 2.5 |
| TAME-LB | c_4 >= 1 in the unslacked KP-W energy estimate, also for normalized outputs | PROVED (AT-110) | 3 |
| CU | weighted high-pass conjugation, O(1/Lambda) on H^r, 0 <= r <= 3 | PROVED, qualitative (AT-111) | 3 |
| TAME-UB | high-frequency tame coefficient 1 + C/Lambda, error C N(k) Lambda^(-(q-2)/4) G^2 | PROVED (AT-112) | 3 |
| TAME-T | uniform compact low-frequency remainder transfers TAME-UB to a full energy estimate | CONDITIONAL (implication CONFIRMED, AT-113) | 3 |
| WG-K-1 | full WG-K inverse with tame coefficient 1 + delta_0 and remainder sqrt(b C_bar) on a fixed reference ball | CONDITIONAL (implication CONFIRMED, AT-114) | 3 |
| T2-CF3 | closure criterion (AT-114 form): CONFIRMED conditional rearrangement (AT-134); its tables | tables HEURISTIC (C_bar unknown) | 4 |
| T2-CF3-SHAPE | for fixed trial constants the closing set in M is a union of at most two intervals, one per gap branch; the earlier single-interval claim is REFUTED | PROVED (AT-134) | 4 |
| T2-CF3-SC | exact scalings of (CF3): the admissible (N(F), R C_bar^(1/2)) set scales like 1/c (S-c); with C_bar = 0, branch 1 depends on N(F) R^((q-2)/2) only (S-R) | CLAIMED (elementary; FLOAT check) | 4 |
| C_bar | the remainder constant C_eps_bar of WG-K-1 | OPEN (finite, not quantified) | 5 |

Main reading.
- The explicit constants asked for at P-S1 are in section 1. Two are explicit (c_W, c_4' = 1 + delta_0), one is not
  (C_bar). For c_W the exact S1 homogeneous bound 1927/1000 (AT-135, section 2.4) replaces the full-space bound 3.34 of
  the earlier tables.
- The tame constant problem is closed in the following sense: c_4' = 1 + delta_0 with the gradient-only tame quantity is
  CONDITIONAL with a CONFIRMED implication (AT-114), and 1 is the right leading value for the unslacked estimate (AT-110).
  The whole price is moved into C_bar, which is finite but not quantified.
- Because R = ||F||_2/beta_0 is small for a re-centered center, the closure inequality tolerates a large C_bar. Section 4
  gives the C_bar budget at P-S1 for trial values of N(F); this is a requirement table, not a closure.
- It does not tolerate a large N(F). With c = 1927/1000 and the FLOAT re-centered inputs, (CF3) needs
  N(F_*) <= 0.0785 in every row of section 4 table (b), even with C_bar = 0 and delta_0 = 0 (HEURISTIC). By (S-R) a
  smaller ||F_*||_2 barely changes this at q = 21/10; by (S-c) a smaller c raises it in proportion.
- T2_TT_v01 is corrected as listed in section 0. None of the corrections changes a table of T2_TT_v01; two change
  statements about C_eps_bar growth that are withdrawn.

## 0. Corrections to T2_TT_v01 and status after audit

T2_TT_v01 is frozen; this list is the record of the corrections. Each item gives the place in T2_TT_v01, the audit item
and the corrected statement.

- C1 (section 8, c_W bullet; AT-109 scope paragraph). The values "c_W <= 7.41, 4.95, 12.88" came from the "opt" column
  of research/explicit/cw_ub.out, a Nelder-Mead maximum of the Leibniz majorant, which can miss the supremum. They are
  not upper bounds. Replace them by the "lin" column, which is an upper bound for exact inputs (section 2.3):
  c_W <= 8.2328, 5.6465, 13.8436 at P-Q2, P-BG2, P-Q1, and 3.3386 at P-S1 (these "lin" values have FLOAT inputs as
  well; section 2.3). The quantity used by the closure is the S1 homogeneous constant; its bounds are in section 2.4
  (EXACT at P-S1 by AT-135, FLOAT elsewhere by AT-133). T2-CW-Q is PROVED (AT-109).
- C2 (section 5, (N3); AT-107). "(N3) is qualitative ... if and only if C_eps_bar(class)^(1/2) = o(M)" is wrong in the
  "only if" direction. Write (N3) as N(F) + (b C(M))^(1/2) R <= a M with a = b - c_4' c_A eps > 0. It holds for all
  large M if limsup_M C(M)^(1/2)/M < a/(b^(1/2) R), and it fails for all large M if liminf_M C(M)^(1/2)/M >
  a/(b^(1/2) R). Little-o growth is sufficient, not necessary. AT-107's example: b = 1, R = 1, a = 1/2, N = 1,
  C(M) = M^2/16, which closes for every M >= 4. (Checked: 1 + M/4 <= M/2 iff M >= 4.)
- C3 (summary bullet on T6.4 item 6; section 5, second bullet; section 8, C_eps_bar bullets; AT-107, AT-109 scope).
  Withdrawn: "C_eps_bar is expected to degenerate faster than any power", "the dependence is at least polynomial in
  M^(4/(q-2)) unless C_eps_bar is independent of Lambda", "Unless C_eps_bar is independent of Lambda, it grows faster than
  any power of (q - 2)^(-1); a growth like exp(C/(q-2)) is plausible". The cut Lambda_1 = max(C/delta_0,
  (C M/delta_0)^(4/(q-2))) of TAME-UB is a sufficient cut of one construction. It gives no lower bound for the actual
  weak constant; AT-107 gives a scalar example where a cut-dependent constant grows only like log(e + Lambda). The growth
  of C_eps_bar in M and in q - 2 is OPEN.
- C4 (section 8, "Consequence for T4.1"; AT-107, AT-114). Replace the advice "do not combine c_4' = 1 + delta_0 with an
  M-independent C_eps_bar" by the fixed reference ball rule. C_bar is the constant of one fixed reference ball
  Kbar = K_(Rbar, Mbar). It may be used for every trial ball K_(R, M) with R <= Rbar and M <= Mbar (with the margin b of
  Kbar), but it cannot be frozen while M is optimized without bound. Closure functions therefore report the smallest
  closing M, which is the reference radius that has to be certified (section 4).
- C5 (section 2, second remark; AT-106). "(H-L) is equivalent to H(z) <= beta_L^(-1) S_F(G) + C'_L ||G||_2" is
  one-way: (H-L) implies that inequality (since ||z||_2 <= ||G||_2/beta_0 and N_Y = ||G||_2 + S_F), but not conversely
  with the named constants. AT-106's example: beta_L = beta_0 = C_L = 1, ||z||_2 = 1, ||G||_2 = 100, S_F = 1, H = 150.
  The rewritten inequality allows 1 + 2 x 100 = 201, while (H-L) allows 101 + 1 = 102. (Checked.)
- C6 (section 4, closure_H; AT-106). The search of closure_H stops at 0.999 beta_0/c_grad, so "None" does not exclude
  (CF-H). The exact admissible set is eps in [a, eps_L] intersected with [0, beta_0/c_grad), a = beta_L^(-1) N_Y(F) +
  C_L R. AT-106's example: beta_0 = beta_L = c_grad = 1, C_L = 0, eps_L = 2, G0 = 1/2, N_Y = 1999/2000; then a = 0.9995
  and [0.9995, 1) is admissible, but closure_H returns None. (Checked.) The table of T2_TT_v01 section 4 is unaffected:
  eps_L < 0.999 beta_0/c_grad in every row, so the upper end eps_L binds.
- C7 (section 0 notation, section 3; AT-104). [grad k]_alpha := max_j [d_j k]_alpha is the component seminorm. The
  registered seminorm is the Euclidean one, [grad k]^E_alpha = sup |grad k(X) - grad k(Y)|/|X - Y|^alpha. They satisfy
  component <= Euclidean <= sqrt(2) component. T2-TT-CZ is proved with the component seminorm on the right side, so it
  holds verbatim with the Euclidean seminorm; any conversion in the other direction costs sqrt(2). Keep the two
  definitions distinct in H(k) and S_F.
- C8 (section 6; AT-108). T2-TT-NT is a necessary test for the named WG-K criterion T2-CF only (CONFIRMED,
  criterion-specific), not an obstruction to existence. In the FLOAT proxy paragraph: the bound ||h_N - h_0||_2 <=
  0.1255 is not a certified continuum bound, and the sampled gaps above the global origin cap c + 1 - q are not
  whole-plane margins (0.2184 at q = 13/5 against the cap 0.2103; 0.3117 and 0.3185 at q = 5/2 against 0.3103). In the
  v3 criterion (section 4) the test reads (1 + delta_0) ||grad h_0||_inf + q ||Sym DU[h_0]||_(inf,op) < beta - eps
  (the same proof, with the gradient-only tame quantity of WG-K-1).
- C9 (section 1; AT-103). T2-TT-LIP is strengthened: AT-103 proves that compact normalized real S1 C^1 coefficients with
  arbitrarily small A(k) need not have Lipschitz velocity. A positive Hoelder exponent is one sufficient modulus; Dini or
  Besov moduli are alternatives (T2_TT_v01 section 9 (e)).
- C10 (section 8, kappa_q bullet). The upper end is exact: C_norm(q) = kappa_q C_sym with 1/sqrt2 < kappa_q < 1
  (T2-NC-EX, CONFIRMED, AT-128), with FLOAT kappa_(21/10) = 0.71395 and kappa_(5/2) = 0.70773 (T2_REV_v02 section 3;
  no decimal kappa bound is certified). The conclusion of the bullet is unchanged. The sharpened origin loss is a
  two-sided bound q kappa_E C_sym <= liminf <= limsup <= q kappa_q C_sym, with equality only if kappa_E = kappa_q for
  the binding top eigenspace E of the origin matrix (AT-128; T2_REV_v03 section 0, R2-3).
- C11 (section 6 remarks, section 8 c_4' bullet; AT-110 to AT-114). TAME-LB, CU and TAME-UB are PROVED. The uniform
  low-frequency hypothesis ((32), (34) of the external referee t2-tame1) is supplied in the WG-K setting by AT-065/AT-069 on a fixed
  reference ball, so WG-K-1 is CONDITIONAL with a CONFIRMED implication (AT-114). The remark of section 6 that c_4' < 1
  in UT-K is not excluded stays correct: AT-110 is a lower bound for the unslacked estimate only, and an absorbed WG-K
  variant can place the whole tame cost in the weak remainder (audit_v49 header).

Status of the T2_TT_v01 IDs after audit_v48:

| ID | label after audit |
|---|---|
| T2-TT-LIP | PROVED in the stronger normalized C^1 form (AT-103) |
| T2-TT-CZ | PROVED, constants EXACT (AT-104) |
| T2-TT-OR | PROVED (AT-105); re-centered form a0_* ell(z) = -G_y(0), with a0_* > 0 required |
| T2-TT-H1 | PROVED: H1 on a small ball implies H-L (AT-106); the converse is not claimed |
| T2-TT-CL | CONDITIONAL on H-L (implication CONFIRMED, AT-106) |
| T2-TT-NQ | HEURISTIC / OPEN, with C2 and C3 above |
| T2-TT-NT | PROVED as a necessary test for T2-CF only (AT-108) |
| T2-CW-Q | PROVED (AT-109) |

## 1. Explicit constants at P-S1 = (q, sigma, r0) = (21/10, 1, 1/2)

| constant | value | label | source |
|---|---|---|---|
| q C*_sym = q B_1/4 (strain) | 0.516341 | EXACT formula, FLOAT value | T2_REV_v01, AT-064 |
| C_grad = B_1/sqrt2, C_value = B_0 | 0.695444, 0.488357 | EXACT formula, FLOAT value | AT-064 |
| c_W(2), c_W(3) (full space, inhomogeneous) | <= 3.0887, <= 6.7253 | UB (FLOAT inputs) | 2.3 |
| c_W(21/10) (full space) | <= 3.3386 | UB (FLOAT inputs), via T2-CW-Q | 2.3 |
| c_2, c_3 (S1 homogeneous endpoints) | <= 1773/1000, <= 508/125 | EXACT UB (AT-135; method AT-131, AT-132) | 2.4 |
| same, from cw_hom_ub.py | <= 1.770513, <= 4.058254 | FLOAT (not a certificate, AT-133) | 2.4 |
| c^hom_(S1)(21/10), the constant used in closure v3 | <= 1927/1000 | EXACT UB (AT-135, via T2-EXP-HI = AT-131) | 2.4 |
| same, from cw_hom_ub.py | <= 1.923637 | FLOAT (AT-133) | 2.4 |
| same, power iteration | 1.0473 (full space 1.3966) | FLOAT | 2.5 |
| c_2, c_3, power iteration (S1 homogeneous) | 1.03262, 1.44308 | FLOAT (box-checked) | 2.5 |
| c_4' | 1 + delta_0 for every delta_0 > 0, gradient-only tame quantity | CONDITIONAL (implication CONFIRMED, AT-114) | 3 |
| C_bar(delta_0, Kbar) | finite | OPEN | 5 |

## 2. The weight constant c_W

### 2.1 Definitions

W(X) = (1 + |X|^2/r0^2)^(sigma/2), a := W^(-1) = b(X/r0) with b(Y) = (1 + |Y|^2)^(-sigma/2), J = (1 - Delta)^(1/2),
N(k) = ||J^q(W k)||_2. Four constants:
- c_W(q) = ||a||_(H^q -> H^q) (multiplication, full space); c_W^(S1)(q) the same on the S1 subspace;
- c^hom(q) = sup ||k||_(Hdot^q)/N(k) = || |D|^q a J^(-q) ||_(L^2 -> L^2); c^hom_(S1)(q) the same on S1.
Then c^hom_(S1) <= c^hom <= c_W and c^hom_(S1) <= c_W^(S1) <= c_W, since |xi|^q <= (1 + |xi|^2)^(q/2). Closure v3 uses
c^hom_(S1)(q): it enters through ||k||_(Hdot^q) <= c^hom_(S1) N(k) in the GN bounds of Sym DU[k] and grad z.

### 2.2 Interpolation [T2-CW-Q, PROVED (AT-109); T2-EXP-HI, PROVED (AT-131)]

T2-CW-Q (AT-109): c_W(q) <= c_W(2)^(3-q) c_W(3)^(q-2) for 2 <= q <= 3, on the full space and on S1, and
||k||_(Hdot^q) <= c_W(q) N(k). The weight must not depend on q.

T2-EXP-HI. For 2 <= q <= 3, c^hom_(S1)(q) <= c^hom_(S1)(2)^(3-q) c^hom_(S1)(3)^(q-2), and the same without S1.
Proof. Same three-lines argument as AT-109, applied to B(z) = |D|^(2+z) a J^(-2-z), 0 <= Re z <= 1. Take f, h S1 with
Fourier support in a compact annulus {e <= |xi| <= 1/e}. Then <B(z) f, h> = <a J^(-2-z) f, |D|^(2+conj z) h> is analytic
and bounded on the strip. On Re z = 0, B(it) = |D|^(it) B(0) J^(-it), and |D|^(it), J^(-it) are unitary on L^2 (moduli one
for xi != 0) and preserve S1 and the annulus class; so |<B(it) f, h>| <= c^hom_(S1)(2) ||f|| ||h||. On Re z = 1 the bound
is c^hom_(S1)(3). The three-lines theorem bounds <B(theta) f, h> by c^hom_(S1)(2)^(1-theta) c^hom_(S1)(3)^theta ||f|| ||h||.
Annulus-supported S1 functions are dense in S1 L^2 ({0} is a null set). For k with N(k) finite, u = J^q(W k) is the L^2
limit of such u_n; a J^(-q) u_n -> k in L^2, and |D|^q a J^(-q) u_n is Cauchy in L^2, so its limit is |D|^q k (the
operator |D|^q is closed). Taking theta = q - 2 gives ||k||_(Hdot^q) <= c^hom_(S1)(2)^(3-q) c^hom_(S1)(3)^(q-2) N(k). QED.

### 2.3 Full-space endpoint bounds (research/explicit/cw_ub.py, "lin" column) [T2-EXP-CWF, UB with FLOAT inputs]

Norm identity (exact): ||g||_(H^m)^2 = sum_(j=0..m) binom(m, j) x_j^2, x_j = ||grad^j g||_2 with full tensors and the
Frobenius norm, because (1 + |xi|^2)^m = sum binom(m, j) |xi|^(2j) and the sum over ordered index tuples of xi^(2 alpha)
is |xi|^(2j).

Bound. With v_j = ||grad^j(a g)||_2, the Leibniz rule and |sym(A x B)| <= |A||B| give
v_j <= x_j + sum_(l=1..j) binom(j, l) T_(j,l), where T_(j,l) = || |grad^l a| |grad^(j-l) g| ||_2 is bounded either by
A_l x_(j-l) (A_l = sup |grad^l a|) or, if j - l <= m - 2, by ||grad^l a||_2 K(j-l, m) ||g||_(H^m). Here
||grad^i g||_inf <= K(i, m) ||g||_(H^m) with K(i, m) = (2 pi)^(-1) [I_i B(i+1, m-i-1)/2]^(1/2), I_0 = 2 pi, I_1 = pi
(Cauchy-Schwarz in Fourier; for i = 1 the directional form with int cos^2 = pi). With a fixed route per term, v <= x + L x +
c ||g||_(H^m) componentwise, L strictly lower triangular, so
  ||a g||_(H^m) <= (1 + ||S L S^(-1)||_2 + ||S c||_2) ||g||_(H^m),  S = diag(binom(m, j)^(1/2)).
Scaling: sup |grad^l a| = r0^(-l) sup |grad^l b|, ||grad^l a||_2 = r0^(1-l) ||grad^l b||_2.
Inputs: sup |grad^l b| on a radial grid (step 2.5e-5 on [0, 5]) and ||grad^l b||_2 by quad. These are FLOAT; section 2.4
computes the same quantities exactly. The "opt" column of cw_ub.out is not a bound (C1).

| tuple (q, sigma, r0) | M_2 (lin) | M_3 (lin) | c_W(q) <= M_2^(3-q) M_3^(q-2) |
|---|---|---|---|
| P-S1 (21/10, 1, 1/2) | 3.0887 | 6.7253 | 3.3386 |
| P-Q2 (12/5, 1, 1/4) | 4.9801 | 17.4989 | 8.2328 |
| P-BG2 (5/2, 7/5, 1/2) | 3.6604 | 8.7101 | 5.6465 |
| P-Q1, P-BG1 (13/5, 7/5, 1/4) | 6.1386 | 23.8067 | 13.8436 |

These bound the full-space inhomogeneous constant, which is larger than the constant the closure needs. The cost is the
second-derivative peak of a at the origin (|grad^2 b|(0) = sqrt2 sigma, so |grad^2 a|(0) = 5.66 at P-S1).

### 2.4 S1 homogeneous endpoint bounds (research/explicit/cw_hom_ub.py) [T2-EXP-CWH: method PROVED (AT-131, AT-132); values EXACT UB at P-S1 (AT-135), FLOAT elsewhere (AT-133)]

Three ingredients are added to section 2.3.

Lemma HARDY-S1. For real S1 g in H^1(R^2), || g/|X| ||_2 <= ||grad g||_2.
Proof. In polar coordinates S1 means even under phi -> pi - phi and odd under phi -> -phi, so the angular Fourier series
of g has only the terms f_n(r) sin(n phi) with n odd (sin(n(pi - phi)) = -(-1)^n sin(n phi)). Then
int |grad g|^2 = pi sum_n int (f_n'^2 + n^2 f_n^2/r^2) r dr >= pi sum_n int f_n^2 r^(-1) dr = int g^2/|X|^2, since n >= 1.
For g in H^1 use density of S1 functions in C_c^infinity(R^2 minus {0}) (a point has zero H^1 capacity in R^2) and Fatou.
QED.

Leibniz with exact tensor factors. 0 < a <= 1, and for the homogeneous norms only the top order j = m enters:
- m = 2: |grad^2(a g)| <= a |grad^2 g| + 2 |grad a| |grad g| + |grad^2 a| |g|, since |u (x) v + v (x) u| <= 2|u||v|.
- m = 3: |grad^3(a g)| <= a |grad^3 g| + 3 |grad a| |grad^2 g| + t_2 |grad g| + |grad^3 a| |g|, where for the term
  T_ijk = A_ij v_k + A_ik v_j + A_jk v_i (A = grad^2 a symmetric) one has |T|^2 = 3|A|_F^2 |v|^2 + 6|A v|^2, so
  t_2 = (3 |A|_F^2 + 6 |A|_op^2)^(1/2) <= 3|A|_F. For radial a the Hessian has eigenvalues f'' and f'/r.
Each lower term is bounded by one of three routes: sup (coefficient on x_i), L^2 times sup with K(i, m) (constant term),
or, for the term with |g| and on S1 only, Hardy: || |grad^l a| g ||_2 <= sup(|X| |grad^l a|) x_1.

Lemma DUAL. For c_i >= 0 and any t_i > 0,
  sum_i c_i x_i <= [ sup_(p >= 0) Q_t(p)/(1 + p)^m + sum_i c_i t_i/2 ] ||g||_(H^m),  Q_t(p) = sum_i c_i p^i/(2 t_i).
Proof. Normalize ||g||_(H^m) = 1 and let mu be the image of (2 pi)^(-2) |ghat|^2 d xi under p = |xi|^2. Then
x_i^2 = int p^i d mu and int (1 + p)^m d mu = 1. Use x_i <= (x_i^2/t_i + t_i)/2 and int Q_t d mu <= sup Q_t/(1 + p)^m.
QED. With optimal t this is the exact maximum of the concave program over the moment set; for m = 2 and the form
x_2 + c x_1 it equals (1 + (1 + c^2)^(1/2))/2, which is the single-frequency value.

Inputs. For rational sigma, |grad^l b|_F^2 = P_l(s)(1 + s)^(-sigma-2l) with s = |Y|^2 and P_l a polynomial with
rational coefficients (rotation invariance; evaluated on the x axis); the Hessian eigenvalue switch is at s = 2/sigma.
These formulas are exact (AT-133). Suprema come from the real roots of the critical-point equation, L^2 norms from exact
integration, and the dual parameters t_i are rational.
Status of the numbers (AT-133). The evaluation in cw_hom_ub.py is not a containing certificate: the roots are exact but
their function values are compared and padded (relative 1e-12) as 30-digit approximations without an error bound, and
the final values pass through binary floats and six-decimal nearest rounding, which can lower an upper end. The values
below are therefore FLOAT upper estimates. At P-S1 they are replaced by the exact rational bounds of AT-135
(the theory auditor research/ps1_exact_endpoint; reviewed in T2_REV_v04 section 1): A_1 < 77/100, Hardy coefficients H_2 < 4/5 and
H_3 < 97/20 from exact Sturm tests, the Hessian contraction integral 199 pi/36, the rational dual witness t_i = 7/20 with
S = 73/50, and (1773/1000)^9 (508/125) < (1927/1000)^10. Same routes as cw_hom_ub.py; the FLOAT values lie below the
rational ones, as they must. A containing implementation along AT-133 (rational witnesses, Sturm or other exact
polynomial sign tests, directed evaluation of rational powers, outward rounding) for the other tuples is not done here.
cw_hom_ub.py also had a sympy defect at integer sigma (an uncancelled rational in the radial polynomial); it was fixed
with sp.cancel before the run, and the sigma = 1 polynomials agree with AT-135 (2).

Values (research/explicit/cw_hom_ub.out; c_2 = c^hom(2), c_3 = c^hom(3), c^hom(q) <= c_2^(3-q) c_3^(q-2)):

| tuple (q, sigma, r0) | S1: c_2 | S1: c_3 | c^hom_(S1)(q) | full: c_2 | full: c_3 | c^hom(q) | label |
|---|---|---|---|---|---|---|---|
| P-S1 (21/10, 1, 1/2), AT-135 | 1773/1000 | 508/125 | 1927/1000 | not done | not done | not done | EXACT UB (AT-135) |
| P-S1 (21/10, 1, 1/2) | 1.770513 | 4.058254 | 1.923637 | 2.283954 | 5.460660 | 2.491972 | FLOAT |
| P-Q2 (12/5, 1, 1/4) | 2.888893 | 11.383664 | 4.999789 | 3.850807 | 15.687815 | 6.753921 | FLOAT |
| P-BG2 (5/2, 7/5, 1/2) | 2.107602 | 5.414702 | 3.378171 | 2.741264 | 7.230899 | 4.452169 | FLOAT |
| P-Q1, P-BG1 (13/5, 7/5, 1/4) | 3.596376 | 15.772762 | 8.731537 | 4.807978 | 21.616526 | 11.848313 | FLOAT |
| (11/5, 1, 1/2) | 1.770513 | 4.058254 | 2.090004 | 2.283954 | 5.460660 | 2.718935 | FLOAT |

Routes chosen by the script (all tuples alike): on S1, m = 2 bounds the term |grad^2 a| |g| by Hardy (coefficient on
x_1) and has no constant term; m = 3 bounds |grad^3 a| |g| by Hardy and the other lower terms by the sup route. On the
full space Hardy is not available and the |g| terms go through the L^2-times-K(i, m) route (constant terms 0.8660 and
3.9142 at P-S1). Since c_2 and c_3 do not depend on q, the AT-135 endpoint bounds hold at every q in [2, 3] for the same
weight; with T2-EXP-HI this gives for instance c^hom_(S1)(11/5) <= (1773/1000)^(4/5) (508/125)^(1/5) < 2093/1000
(CLAIMED; exact rational check (2093/1000)^5 > (1773/1000)^4 (508/125) in scratch/exp/q115_check.py). The P-BG3 tuple
(21/10, 1, 1/2) of section 4 has the P-S1 weight, so 1927/1000 applies there too.

### 2.5 FLOAT values (power iteration on a periodic box; not certificates)

cw_power.out, cw_hom.out, cw_ps1.out (q-norms, L = 20, N = 1024; L = 40, N = 2048 checks agree to 1e-5) and cw_end.out
(integer endpoints):

| tuple | c_W full | c_W^(S1) | c^hom full | c^hom_(S1) |
|---|---|---|---|---|
| P-S1 (21/10, 1, 1/2) | not run | not run | 1.39657 | 1.04730 |
| P-Q2 (12/5, 1, 1/4) | 3.75052 | 1.32978 | 3.64315 | 1.30303 |
| P-BG2 (5/2, 7/5, 1/2) | 2.52233 | 1.28479 | 2.34610 | 1.23362 |
| P-Q1 (13/5, 7/5, 1/4) | 7.11215 | 1.73976 | 6.97634 | 1.71003 |

Integer endpoints (cw_end.out at L = 20, N = 1024, with the (1, 1/2), m = 3 entries replaced by the box checks
cw_box.out, cw_box2.out, cw_box3.out at L = 40, N = 2048 and L = 80, N = 4096; same grid step):

| (sigma, r0) | m | c_W full | c_W^(S1) | c^hom full | c^hom_(S1) | bound on c^hom_(S1), section 2.4 |
|---|---|---|---|---|---|---|
| (1, 1/2) | 2 | 1.43837 | 1.05592 | 1.32086 | 1.03262 | 1773/1000 EXACT; 1.770513 FLOAT |
| (1, 1/2) | 3 | 3.46166 | not rerun (L = 20 value 3.55378 is an artifact) | 3.19577 | 1.44308 | 508/125 EXACT; 4.058254 FLOAT |
| (1, 1/4) | 2 | 2.13760 | 1.10063 | 2.06452 | 1.08800 | 2.888893 FLOAT |
| (1, 1/4) | 3 | 11.52407 | 2.34406 | 11.30049 | 2.28778 | 11.383664 FLOAT |
| (7/5, 1/2) | 2 | 1.61976 | 1.07667 | 1.50863 | 1.05431 | 2.107602 FLOAT |
| (7/5, 1/2) | 3 | 4.64925 | 1.76323 | 4.36567 | 1.67244 | 5.414702 FLOAT |
| (7/5, 1/4) | 2 | 2.58530 | 1.13537 | 2.52122 | 1.12464 | 3.596376 FLOAT |
| (7/5, 1/4) | 3 | 16.28676 | 2.87308 | 16.03288 | 2.82295 | 15.772762 FLOAT |

Box artifact. On the periodic box the weight a is continuous but its normal derivative jumps at the box faces, by
2 sigma (L/2) r0^(-2) (1 + L^2/(4 r0^2))^(-sigma/2-1): 0.00996 at (1, 1/2) and L = 20, against 0.0050, 0.0042, 0.0016
for the other pairs, and four or more times less at L = 40. A third-order constant sees this jump on the grid scale. At
(1, 1/2), m = 3, the S1 homogeneous value at L = 20 is 1.44308 at N = 512, 3.55304 at N = 1024 and 10.04805 at
N = 2048, while L = 40, N = 2048 and L = 80, N = 4096 both give 1.44308; the full-space values at L = 40 and L = 80 agree
(3.46166, 3.19577), against 4.52295, 4.52214 at L = 20. So the L = 20 entries at (1, 1/2), m = 3 of cw_end.out are
artifacts, and the table above uses the L = 40 values. Where checked, the other entries agree at L = 40 to five digits:
m = 2 at (1, 1/2) (full and S1), m = 3 at (1, 1/4) and (7/5, 1/4) (full and S1), and at (7/5, 1/2) (full and S1). The
q-norm values in the first table of this section agree at L = 40, N = 2048 (cw_ps1.out at P-S1, cw_power.out at P-Q1).
With the corrected m = 3 value, the FLOAT interpolation at P-S1 is 1.03262^(9/10) 1.44308^(1/10) = 1.0678, above the
direct q-norm value 1.04730, as it must be. The m = 3 bound 508/125 is 2.8 times the FLOAT value 1.44308, and the
m = 2 bound 1773/1000 is 1.72 times 1.03262.

### 2.6 Reading

- The S1 restriction is worth a factor of 1.3 to 4 in the FLOAT values. It removes the bad direction: on S1, g vanishes on
  the x axis, so the multiplier peak of grad^2 a at the origin acts on |g| <= |X| |grad g|-type sizes. The certified
  bounds of section 2.4 use exactly this through Lemma HARDY-S1.
- The certified P-S1 value 1927/1000 is 1.84 times the FLOAT value 1.0473 (section 2.5). Most of the slack is in the
  m = 2 endpoint: 1773/1000 against the FLOAT 1.0326 (factor 1.72, exponent 9/10), against 508/125 and 1.44308 at m = 3
  (factor 2.8, exponent 1/10); 1.72^(9/10) 2.8^(1/10) = 1.81 matches the ratio 1.927/1.0678 = 1.80 between the certified value
  and the interpolated FLOAT value, up to rounding. The slack comes from the Leibniz majorant (triangle inequality across the three terms, each term at its own
  supremum) and from Hardy, not from the dual step, which is exact for the majorant (AT-132).
- At r0 = 1/4 the FLOAT upper estimates of section 2.4 are 3.8 to 5.1 times the power-iteration values (4.999789 against
  1.30303 at P-Q2, 8.731537 against 1.71003 at P-Q1); the m = 3 endpoint is the main loss there.
- In the closure every factor in c is a factor in the admissible N(F) (section 4, scaling (S-c)). Two improvements are
  possible and neither is done here: an m = 2 bound closer to the FLOAT value, and a small-R form of the weight
  transfer. For the second, AT-071 (7) proves sup over K_(R,M) of ||k||_(Hdotq) <= M + o(1) as R -> 0 (compactness, no
  rate). A commutator bound ||W^(-1) [|D|^q, W] k||_2 <= C_(q,W) ||k||_(H^(q-1)) with explicit C_(q,W) would give
  ||k||_(Hdotq) <= N(k) + C_(q,W) R^(1/q) (c_W M)^((q-1)/q), an effective c of 1 + O((R/M)^(1/q)), where
  (R/M)^(1/q) is about 0.013 at the re-centered P-S1 row (OPEN; T2_REV_v04 section 6, remark).
- c_W does not degenerate as q -> 2 (T2-CW-Q); the interpolation exponents put weight 0.9 on the m = 2 endpoint at
  q = 21/10, so the m = 2 bound is what matters at P-S1.

## 3. The tame constant c_4' [TAME-LB, CU, TAME-UB PROVED; TAME-T, WG-K-1 CONDITIONAL (implications CONFIRMED)]

Statements as audited (audit_v49):
- TAME-LB (AT-110). If the unslacked KP-W energy estimate
  |E(k, u)| <= (c_1 ||Da||_inf + c_2 ||k||_2 + c_3 ||a||_inf) ||g||^2 + c_4 N(k) A(h) ||g||
  holds for all real S1 Schwartz k, u with ell(k) = 0 (A(h) = ||grad h||_inf + ||h||_inf or ||grad h||_inf), then
  c_4 >= 1; also when the outputs are restricted to ell(h) = 0. It is not a lower bound for a full inverse with a weak
  remainder.
- CU (AT-111). ||W T_Lambda W^(-1) - T_Lambda||_(H^r -> H^r) <= C_r/Lambda for the high-pass multipliers, 0 <= r <= 3;
  numerical constants OPEN.
- TAME-UB (AT-112). For the high-frequency coefficient Q_Lambda k, the energy obeys the tame bound with leading
  coefficient 1 + C/Lambda times N(k) ||grad h||_inf ||g|| and a quadratic error C N(k) Lambda^(-(q-2)/4) ||g||^2, on a
  fixed coefficient ball.
- TAME-T (AT-113). A uniform compact low-frequency remainder transfers this into a full energy estimate; bounded
  injectivity of the weak norm map suffices.
- WG-K-1 (AT-114). On one fixed reference ball Kbar with actual full matrix margin beta_K > 0, for every eps in
  (0, beta_K) and delta_0 > 0 there is a finite C_bar = C_bar(delta_0, eps, Kbar) such that the full L^2 inverse
  satisfies, uniformly on Kbar including its boundary,
    b N(z) <= N(G) + (1 + delta_0) N(k) ||grad z||_inf + (b C_bar)^(1/2) ||z||_2,  b = beta_K - eps.
  The velocity value term is not in the tame term; it stays in the matrix loss.

My own step check of the external referee t2-tame1 (before the audit; all AGREE): in (A), the oscillatory limit (dominated
convergence), the exact derivatives of k_n and a_n, N(k_n) -> C0/sqrt2, the energy limit tau D0^2/2 > 0, the bound
c_4 >= D0/(C0 A(h0)), the saturation h0 = e sin(y/e) theta with packets of radius e^2 at (x*, 2 pi e) where
cos(y/e) >= cos e, and the order of limits n, then tau, then e. In CU, the annular kernels, the first-moment bound
C/(Lambda 2^j) using P(v/Lambda) <= P(v), the fixed-z representation with normalized derivatives of W and W^(-1)
(Peetre), and interpolation over H^r. In (B), the mean-value commutator bound followed by Young and Cauchy-Schwarz,
||a||_inf <= C K Lambda^(-1-eta), ||Da||_inf <= C K Lambda^(-eta) with eta = (q-2)/2, the split at mu = Lambda^(1/2)
giving the rate Lambda^(-(q-2)/4), and the cut Lambda_1 = max(C/delta_0, (C M/delta_0)^(4/(q-2))). AT-110 adds the
normalized-output extension (an origin mode-3 correction e0 disjoint from the packets, with ell(h0) = O(e^L)); I read
it and agree; a formal review follows in the next T2_REV note.

Consequences for the closure.
- c_4' = 1 + delta_0 for every delta_0 > 0, at every q in (2, 3), with tame quantity ||grad z||_inf only. In the
  scalar closure the tame factor is
    zeta_grad = ((1 + delta_0)/b) C_grad c^(1-theta) R^theta M^(1-theta),  theta = (q-2)/q, c = c^hom_(S1)(q).
- Nothing about c_4' is left to compute. What is not explicit is C_bar (section 5) and the constants of CU and TAME-UB
  that enter it.
- AT-110's scope matters for necessary tests: a statement "c_4' >= 1 in every UT-K" is not available, so NT-L in the v3
  form is necessary for the named criterion with the coefficient actually used.

## 4. Closure v3 [T2-CF3: rearrangement CONFIRMED (AT-134), tables HEURISTIC; T2-CF3-SHAPE PROVED (AT-134)]

Inequality (AT-114 form; research/explicit/closure_fn_v3.py with tame = "grad" for the grid rows, closure_fn_v4.py
for the branch rows). With R = ||F||_2/beta_0,
theta = (q-2)/q, theta_0 = (q-1)/q and the v2 constants (AT-064),
  tau(M) = q (B_1/4) R^theta (c M)^(1-theta) + min(sigma (sqrt5 B_1/4) R^theta (c M)^(1-theta),
                                                   (sigma/(2 r0)) sqrt(3/8) B_0 R^theta_0 (c M)^(1-theta_0)),
  b(M) = beta - eps - tau(M) > 0,
  N(F)/b + (C_bar/b)^(1/2) R + ((1 + delta_0)/b) (B_1/sqrt2) c^(1-theta) R^theta M^(1-theta) M <= M.       (CF3)
If (CF3) holds at M with C_bar the constant of the reference ball K_(R,M) itself (margin b(M)), the ball is invariant
under T (AT-114; the fixed-point step is as in T2_WGK_v01). AT-134 confirms this as a conditional rearrangement, with
hypotheses that an actual theorem must keep: eps > 0 and delta_0 > 0; a C_bar for the same reference ball and margin
(a value obtained for one ball and margin cannot be reused for larger radii or margins); and delta > alpha/(2 c_l - 2)
in the fixed-point step. Every table below uses trial values of C_bar and eps = 0, so it is HEURISTIC; the rows with
delta_0 = 0 are optimistic limits, not admissible choices. Entry G0max: the largest G0 = ||F||_2 for which some
N(F) >= G0 closes.
The first six rows are grid thresholds of closure_fn_v3.py (radius grid; frozen as an audit target). A grid point that
closes is a closing radius, so a grid threshold is at most the branch value (up to FLOAT error); it is not a closing
interval. The last three rows use closure_fn_v4.py (branch form below) with the c values of section 2.4.

| run | P-Q2 | P-BG2 | P-Q1 | P-BG1 | P-BG3 |
|---|---|---|---|---|---|
| v2 tame A, c = 1 (T2_REV_v01) | 0.02281 | 0.02846 | 0.0213 | 0.006254 | 0.06471 |
| v3, c = 1 | 0.02617 | 0.03327 | 0.02441 | 0.006988 | 0.07405 |
| v3, c = S1 FLOAT (1.303, 1.234, 1.71, 1.71, 1.047) | 0.0214 | 0.02846 | 0.01695 | 0.004807 | 0.07101 |
| v3, c = full-space UB (8.23, 5.65, 13.84, 13.84, 3.339) | 0.005056 | 0.008981 | 0.003854 | 0.001064 | 0.02444 |
| v3, 1 + delta_0 = 1.1, C_bar = 1, c = S1 FLOAT | 0.01771 | 0.02358 | 0.01446 | 0.004226 | 0.05166 |
| v3, 1 + delta_0 = 1.1, C_bar = 100, c = S1 FLOAT | 0.008499 | 0.01152 | 0.007735 | 0.002533 | 0.01718 |
| v4, c = S1 UB (4.99979, 3.37817, 8.73154, 8.73154 FLOAT; 1927/1000 EXACT), C_bar = 0, delta_0 = 0 | 0.007514 | 0.01331 | 0.005378 | 0.001491 | 0.04063 |
| v4, same c, 1 + delta_0 = 1.1, C_bar = 1 | 0.006158 | 0.01097 | 0.004532 | 0.0013 | 0.02943 |
| v4, same c, 1 + delta_0 = 1.1, C_bar = 100 | 0.002887 | 0.00528 | 0.002352 | 0.000763 | 0.009697 |

(research/explicit/closure_cert_v2.out (a); beta_0 = 2.00215453 and the AT-064 values of beta as in T2_REV_v01.)

Closing set in M [T2-CF3-SHAPE, PROVED (AT-134)]. The draft of this note said that for a fixed trial C_bar the closing
set in M is an interval. That is REFUTED: AT-134 gives an exact witness with two components and a failing radius between
them. The correct statement is as follows. Write eta = 2/q = 1 - theta, B = beta - eps, w = R C_bar^(1/2), and
  s_1 = q C_sym R^theta c^eta, s_2 = sigma C_DU R^theta c^eta, s_3 = (sigma/(2 r0)) C_U R^theta_0 c^(eta/2),
  t = (1 + delta_0) C_grad R^theta c^eta,
with C_sym = B_1/4, C_DU = sqrt5 B_1/4, C_U = sqrt(3/8) B_0, C_grad = B_1/sqrt2. Then b(M) = max(g_1, g_2) with
g_1 = B - (s_1 + s_2) M^eta and g_2 = B - s_1 M^eta - s_3 M^(eta/2), and (CF3) holds at M if and only if for some j,
g_j(M) > 0 and
  Phi_j(z) = N(F) e^(-z)/g_j + w e^(-z)/g_j^(1/2) + t e^(eta z)/g_j <= 1,  z = log M.
Each log Phi_j is convex where g_j > 0, so branch j closes on one interval, and the closing set is the union of at most
two intervals. research/explicit/closure_fn_v4.py computes each branch interval (minimizer of log Phi_j by golden
section, then two bisections) and reports the components, never their hull. Its self-test reproduces the AT-134 witness
(eta = 4/5, s_1 = s_2 = s_3 = t = 1/2, B = 13/5, w = 0, N = 1101/1000): components [0.91933, 0.98859] and
[1.01105, 1.10631], M = 1 fails, and (99/100)^5 and (101/100)^5 close.
By C4 the reference radius to certify is the lower end of the component that is used, with C_bar the constant of that
ball and margin. In every re-centered P-S1 case below there is one component (at N(F) = max/2 in table (b), at the
budget point in table (c), and at seven fractions of the maximum in research/explicit/closure_cert_v2.out (d)). This is
a FLOAT observation for these parameters only.

Two exact scalings of (CF3) (elementary; FLOAT check in research/explicit/closure_scaling.out).
- (S-c) Under M = u/c the gap terms s_i M^eta, s_3 M^(eta/2) and the tame term t M^eta do not depend on c, while the
  N(F) and w terms are multiplied by c. So the admissible set of pairs (N(F), w) scales exactly like 1/c, and with
  C_bar = 0 the largest closing N(F) is proportional to 1/c. Check: at the re-centered P-S1 row with G0 = 1e-4 and
  C_bar = 0, c = 1.0473 gives 0.139218 and c = 1.927 gives 0.0756634, ratio 1.839969 = 1.927/1.0473.
- (S-R) Under M = R^(-theta/eta) u, with C_bar = 0, branch 1 depends on N(F) R^(theta/eta) only, theta/eta = (q-2)/2.
  So on branch 1 the largest closing N(F) grows only like ||F||_2^(-(q-2)/2) = ||F||_2^(-1/20) at q = 21/10. Branch 2
  improves a little faster (s_3 carries R^theta_0, theta_0 - theta/2 = 1/2 > 0), and it is the better branch at the
  re-centered P-S1 row (0.0757 against 0.0513 at G0 = 1e-4).
So at q = 21/10 a smaller ||F||_2 does not materially raise the N(F) that (CF3) accepts, while c enters linearly.

Re-centered P-S1 row (the coordinator 22:06Z inputs, FLOAT: BG-q margin 0.6797 of rho_bar + h_0, beta_0* >= 1.862 from
||grad h_0||_inf about 0.140). HEURISTIC: the inputs are FLOAT and C_bar is a trial value. No ratio against a measured
N_q(F_*) is formed here; the deciding inputs are N_q(F_*) of a converged center and C_bar.

Table (b) (closure_cert_v2.out (b); c = 1927/1000, q = 21/10, sigma = 1, r0 = 1/2, beta = 0.6797, beta_0 = 1.862,
eps = 0): the largest N(F) that closes, the closing components at half of it, and the grid threshold of closure_fn_v3.py
for comparison.

| ||F_*||_2 | C_bar, 1 + delta_0 | max N(F) | components at max/2 | v3 grid threshold |
|---|---|---|---|---|
| 5e-5 | 0, 1 | 0.078413 | [0.06847, 0.4069] | 0.078399 |
| 5e-5 | 1, 1.1 | 0.073936 | [0.06461, 0.3837] | 0.073908 |
| 5e-5 | 1e2, 1.1 | 0.073758 | [0.06483, 0.3836] | 0.07373 |
| 5e-5 | 1e4, 1.1 | 0.071985 | [0.06705, 0.382] | 0.071951 |
| 5e-5 | 1e6, 1.1 | 0.054265 | [0.0908, 0.3646] | 0.054258 |
| 1e-4 | 0, 1 | 0.075663 | [0.06609, 0.3927] | 0.075663 |
| 1e-4 | 1, 1.1 | 0.071325 | [0.06238, 0.3703] | 0.071308 |
| 1e-4 | 1e2, 1.1 | 0.07097 | [0.06282, 0.37] | 0.070954 |
| 1e-4 | 1e4, 1.1 | 0.067424 | [0.0673, 0.3668] | 0.067414 |
| 1e-4 | 1e6, 1.1 | 0.032036 | [0.1199, 0.3269] | 0.032009 |
| 1e-3 | 0, 1 | 0.066921 | [0.05853, 0.3481] | 0.066908 |
| 1e-3 | 1, 1.1 | 0.062738 | [0.0557, 0.328] | 0.062738 |
| 1e-3 | 1e2, 1.1 | 0.059198 | [0.0602, 0.3248] | 0.059195 |
| 1e-3 | 1e4, 1.1 | 0.023878 | [0.1146, 0.2832] | 0.023877 |
| 1e-3 | 1e6, 1.1 | 0 | none | 0 |

Reading: with these FLOAT inputs and the certified c, (CF3) requires N(F_*) <= 0.0785 in every row, even with C_bar = 0
and delta_0 = 0, and by (S-R) a smaller ||F_*||_2 changes this little. This is a requirement on N(F_*), not a closure
statement.

C_bar budget at the re-centered P-S1 row: the largest trial C_bar for which (CF3) still closes at a given
(||F_*||_2, N(F_*)), with 1 + delta_0 = 1.1 and the certified c. This is the size that a quantified C_bar must meet.

Table (c) (closure_cert_v2.out (c); same inputs as table (b); at the budget the closing set shrinks to one radius, listed):

| ||F_*||_2 | N(F_*) = 0.01 | N(F_*) = 0.03 | N(F_*) = 0.1 or 0.3 |
|---|---|---|---|
| 5e-5 | C_bar <= 1.06e7, at M = 0.2356 | C_bar <= 4.9961e6, at M = 0.2317 | no closure even with C_bar = 0 |
| 1e-4 | C_bar <= 2.4406e6, at M = 0.2273 | C_bar <= 1.1065e6, at M = 0.2234 | no closure even with C_bar = 0 |
| 1e-3 | C_bar <= 18354, at M = 0.2013 | C_bar <= 7118.5, at M = 0.1974 | no closure even with C_bar = 0 |

The radius M at the budget is the reference radius whose C_bar would have to be certified (C4); C_bar must be the
constant of that ball and margin (AT-134).

## 5. C_bar OPEN

- What is known: C_bar(delta_0, eps, Kbar) is finite on a fixed reference ball (AT-113, AT-114, via AT-065/AT-069
  compactness). Its value is not quantified, and AT-107 shows that no growth law follows from the sufficient cut Lambda_1.
- Route to an explicit value (plan for the k-dependent C_eps_bar note, due 2026-11-03T12:00Z). Replace the compactness
  step of TAME-T by an explicit low-frequency bound: on frequencies below Lambda_1 the energy error is bounded through
  Bernstein (||J^q P_(<= Lambda) f||_2 <= <Lambda>^q ||f||_2) and the explicit CU and TAME-UB constants, so C_bar is
  bounded by an explicit function of Lambda_1, delta_0 and the ball. This gives an upper bound only. At q = 21/10 the
  exponent 4/(q-2) = 40 in Lambda_1 makes such a bound large; section 4 shows how large C_bar may be.
- The alternative, keeping the KP-W constant c_4 instead of 1 + delta_0 (T2_TT_v01 section 5), avoids the cut; its
  literal constants (research/kpw/PROOF.md) are numerically poor (M_ell about 476 at r0 = 1/4).

## 6. Requests

- The theory auditor: T2-EXP-HI, Lemma HARDY-S1, the tensor factor, Lemma DUAL and the P-S1 values are audited (AT-131 to AT-135;
  my review is T2_REV_v04). Open for audit: closure_fn_v4.py against AT-134 (branch intervals, component list, the
  bisections in max_N and max_w), the scalings (S-c) and (S-R) of section 4, the q = 11/5 consequence of section 2.4
  (CLAIMED), and C1 to C11 as the accepted corrections to T2_TT_v01. A containing certificate for the S1 constants at
  P-Q2, P-BG2, P-Q1 (AT-133 interface) is not done; until it is, those c values are FLOAT.
- The first theory agent (theory_v02): use c^hom_(S1)(21/10) <= 1927/1000 (EXACT UB, AT-135) for c_W at P-S1 and P-BG3, and label the
  other tuples' c values FLOAT; c_4' = 1 + delta_0 with the gradient-only tame quantity; the (CF3) form of section 4 with
  the closing set as a union of at most two intervals (AT-134) and its retained hypotheses (eps > 0, delta_0 > 0, C_bar
  of the same ball and margin, delta > alpha/(2 c_l - 2)); the fixed reference ball rule C4; and C2, C3, C5 to C10
  wherever T2_TT_v01 is quoted. The cw_end.out m = 3 values at (sigma, r0) = (1, 1/2) are box artifacts (section 2.5)
  and must not be quoted.
- The coordinator: the P-S1 constants are in section 1. c_W and c_4' are now explicit; C_bar is the remaining non-explicit
  constant, and section 4 gives the budget it must meet at the re-centered P-S1 row. With the certified c, (CF3) needs
  N(F_*) <= 0.0785 at the FLOAT re-centered inputs in every row of table (b); by (S-c) a sharper c raises this bound in
  proportion, and by (S-R) a smaller ||F_*||_2 barely does.
- The second numerics agent: for the converged center, ||F_*||_2 and N_q(F_*) at q = 21/10 decide where the center sits in the budget
  table; ||grad h_*||_inf and the BG-q margin fix beta_0* and beta.

## 7. Files

- research/explicit/cw_ub.py (+ .out): full-space Leibniz bounds (section 2.3).
- research/explicit/cw_hom_ub.py (+ .out): S1 homogeneous bounds, FLOAT (AT-133) (section 2.4); frozen as an audit
  target by the theory auditor and not modified after the audit.
- scratch/exp/q115_check.py (+ .out): exact rational check at q = 11/5 (section 2.4).
- research/explicit/cw_power.py, cw_power_big.py, cw_hom.py, cw_ps1.py, cw_end.py, cw_box.py, cw_box2.py, cw_box3.py
  (+ .out): FLOAT values and box checks (section 2.5).
- research/explicit/closure_fn_v3.py: closure v3 on a radius grid (grid rows of section 4); frozen as an audit target.
- research/explicit/closure_fn_v4.py: closure in the AT-134 branch form; closure_cert_v2.py (+ .out): tables (a) to (d)
  of section 4; closure_scaling.py (+ .out): the checks of (S-c) and (S-R).
- research/explicit/closure_minterval.py and closure_cert.py: superseded by closure_fn_v4.py and closure_cert_v2.py;
  neither was run.
- an external referee answer, PROOF.md, VERIFICATION.md: referee route for TAME-LB, CU, TAME-UB (audited as AT-110 to AT-112).
