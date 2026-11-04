# T2_CEPS_v02: Theorem HF-Q, an explicit all-quadratic bound for the k-dependent energy increment at P-S2, and the invariant-ball condition without tame term

Version 2 of the CEPS line. Owner: the second theory agent. Drafted 2026-11-03T01:28Z to 01:32Z, revised 01:33Z to 01:42Z after reading
the theory auditor audit_v84 to v89 (actual UTC times). Plain-text mathematics as in T2_CEPS_v01 and T2_BUD_v01. Paths are
relative to the combined2 root; files of this agent are given relative to theory_agent_2/, files of the theory auditor relative to theory_audit/.
Answers the coordinator 23:56Z item 5 (explicit route for the k-dependent part at P-S2) and the HF-EXP target of
T2_CEPS_v01 section 5. Builds on notes/T2_CEPS_v01.md (Definition CB, C^opt, D1 to D6), notes/T2_BUD_v01.md
(Proposition S, AT-202 to AT-204) and an external referee answer/ (AT-220 to AT-223).

Relation to the theory auditor audit. The theory auditor audited this agent's working version research/hf/hfq_budget2.py while this note was
being written: AT-227 to AT-230 (exchange/audit_v88.md, 01:25:59Z) CONFIRM the all-quadratic bound with the core
term sqrt2 (53/100) S_1 ||J^q k||_2, the alpha = 0 weight split with closed-form global majorant pairs, the conditional
self-map test with the direct quadratic budget, and capacity witnesses 0.054218, 0.063757, 0.074077 at
b0 = 0.60, 0.65, 0.70 (||F||_2 = 1e-5, beta_0 = 2.09). This note keeps every audited piece unchanged and replaces only
the core lemma by Lemma CORE below, which is smaller by the factor 1/sqrt2 and uses the homogeneous norm
||D^q k||_2 in place of ||J^q k||_2. Lemma CORE is the one new item that needs audit.

Labels.
- CONFIRMED (cited, not re-proved): Lemma DEC (AT-227 symbol identity, AT-228 weight symmetrization, AT-229
  decomposition), Lemma PR (AT-229 strain term with AT-064/070 C_sym), Lemma WK (AT-228 at alpha = 0 with the AT-230
  pairs), Lemma ELL (AT-228 (4) to (6), AT-223 L_t), Proposition S0 (AT-229 (3) to (5)).
- CLAIMED: Lemma CORE and therefore Theorem HF-Q with the constant (53/100) S_1. Its scalar input, H_q(t) <=
  (53/50)(t - 1)^q on t >= 1, is CONFIRMED (AT-221).
- FLOAT and HEURISTIC: every number in sections 5 and 6. They are arithmetic on FLOAT background inputs (b0, beta_0,
  ||F||_2, N(F)) and are orientation, not a closure. C^opt(b0) is not explicit, and nothing here bounds it.

## 0. Summary

1. Theorem HF-Q (CLAIMED). Let k be real S1 with R = ||k||_2 and K = ||D^q k||_2 finite, and let u be real S1 Schwartz.
   Then the increment E(k, u) = Q_k(u) - Q_0(u) = Re (J^q [W (U[k].grad h)], g) satisfies |E(k, u)| <= l_Q(R, K) G^2,
   where for every certified pair (B, A) of AT-230
       l_Q(R, K) = 0.516341 R^(1/21) K^(20/21) + 0.450791 K + (0.241725 + 0.759399 A) R^(11/21) K^(10/21)
                   + 0.380377 B [0.7 K + 6.30203 R^(10/21) K^(11/21) + 16.5433 R].
   Coefficients are rounded up in the last digit. Examples of pairs: (B, A) = (11/20, 34/5) and (3/5, 31/10). The bound
   has no tame term, no weak term and no frequency cut. It is the AT-229 bound (1) with the core coefficient
   sqrt2 (53/100) S_1 K_J replaced by (53/100) S_1 K.
2. Invariant ball (AT-229, CONFIRMED as an implication). Suppose the base estimate
   Q_0(u) <= -b0 G^2 + C^opt(b0) ||h||_2^2 holds, together with the retained generator and inverse hypotheses. Then
   T(K(R, M)) is contained in K(R, M) as soon as
       N(F) M + C^opt(b0) R^2 <= (b0 - l_Q(R, c_W M)) M^2.                      (HFQ)
   A simpler, more conservative sufficient form is N(F) + (b0 C^opt(b0))^(1/2) R <= (b0 - l_Q(R, c_W M)) M.
   In the form (13.1): N(T(k)) <= A_F + eta(R, M) N(T(k)), with A_F = (N(F) + (b0 C^opt(b0))^(1/2) R)/b0 and
   eta = l_Q(R, c_W M)/b0. Here eta is linear in M. It does not tend to 0 as R -> 0 at fixed M: its floor is
   0.869 M/b0. So route Q needs N(F) itself to be small, not only ||F||_2, and the task's ideal theorem remains OPEN
   (section 4).
3. FLOAT numbers (section 5). At the optimum, l_Q/M is about 1.37:
   - principal part 0.45;
   - core 0.67;
   - far weight term 0.23, of which 0.01 carries a power of R;
   - int b g^2 and near weight term 0.02.
   The largest admissible N(F) at C^opt = 0 (||F||_2 = 1e-5, beta_0 = 2.09) is 0.0655, 0.0770 and 0.0895 at b0 = 0.60,
   0.65 and 0.70. The AT-230 witnesses for the audited core were 0.0542, 0.0638 and 0.0741.
4. Weak-constant room at the current fit target (FLOAT: ||F||_2 = 9.9e-6, FFT N_(21/10) = 0.0257 at P-S2, the coordinator
   00:44Z item 3). The direct budget of (HFQ) is C^opt(b0) <= 4.4e8 at b0 = 0.60, 6.2e8 at 0.65 and 8.4e8 at 0.70.
   The conservative form gives 1.2e8, 1.8e8 and 2.6e8.
5. Comparison at the t2-hf2 point (R = 1.4e-5, M = 0.31). The corrected t2-hf2 fallback has a non-principal loss of
   0.589929 = 1.90 M at cut 1 (AT-223). The audited AT-229 version gives 1.22 M, and HF-Q gives 0.94 M. The principal
   part is 0.47 M in addition.

## 1. Setting

Exact, as in T2_CEPS_v01 section 1 and the AT-114 setting.
- Parameters. P-S2 = (q, sigma, r0) = (21/10, 7/5, 1) and theta = (q - 2)/q = 1/21. J = (1 - Delta)^(1/2), D = |D|,
  <x> = (1 + |x|^2)^(1/2), W(X) = (1 + |X|^2/r0^2)^(sigma/2).
- Weight gradient. ell = grad log W = sigma X/(r0^2 + |X|^2), with sup |ell| = sigma/(2 r0) = 7/10.
- Norms. N(f) = ||J^q (W f)||_2. The unitary Fourier transform is
  fhat(xi) = (2 pi)^(-1) int exp(-i X.xi) f(X) dX. For real f1, f2, f3 and s = r + p,
  int f1 f2 f3 dX = (2 pi)^(-1) int int f3hat(p) f1hat(r) conj(f2hat(s)) dr dp. The Wiener norm is
  ||f||_A = (2 pi)^(-1) int |fhat| (Euclidean norm for vectors), and ||f||_inf <= ||f||_A.
- Velocity. U[f] = m(D) f with m(p) = (p1 p2, -p1^2)/|p|^2 = (p1/|p|) (p2, -p1)/|p|. Hence |m(p)| = |p1|/|p| <= 1,
  m(p).p = 0 and div U = 0.
- Operators. A_k = L + U[k].grad (task section 0.2) and Q_k(u) = Re (J^q [W A_k W^(-1) u], g), with u = W h,
  g = J^q u and G = ||g||_2. Set E(k, u) := Q_k(u) - Q_0(u) = Re (J^q [W (U[k].grad h)], g). E is linear in k.
- For a coefficient k: a = U[k] and b = a.ell (a real scalar). R' = grad J^(-1) is the inhomogeneous Riesz vector,
  with symbol i r/<r>, so ||R' g||_2 <= G. Write T = <s>/<r>, tau = max(T, 1/T) and
  H_q(t) = t^q - t^(-q) - q (t - 1/t) = 2 [sinh(q z) - q sinh z], z = log t.
- Base constant. C^opt(b) is the least C with Q_0(u) <= -b G^2 + C ||h||_2^2 for all real S1 Schwartz u (T2_CEPS_v01
  D3; the theory auditor notation is C0). By HF-NEC (the first theory agent QWG_v02 Corollary HF-NEC-1, CONFIRMED AT-211 to AT-216), C^opt(b)
  is +infinity for b > c + 1 - q. For 007 at P-S2 it is +infinity for b >= 0.6588409179 (AT-199). The certified
  lower margin of 007 at P-S2 is 3/5 (AT-199), so b0 = 0.65 is not supplied for 007 (AT-230). For the corrected center
  the admissible rates are b0 < beta(center) <= 0.7103192102.
- c_W. AT-169 gives ||D^q k||_2 <= c_W N(k) for real S1 k, with c_W = 7441/5000 at P-S2. This is the homogeneous bound
  only. Where ||J^q k||_2 is needed, K_J = [R^(2/q) + (c_W M)^(2/q)]^(q/2) (AT-220). HF-Q does not need it.
- Balls. K(R, M) = {k real S1 : ell_R3(k) = 0, ||k||_2 <= R, N(k) <= M}, where ell_R3 is the R3 normalization
  functional of AT-114 (not the weight gradient ell).

Constants (closed forms; values at P-S2 are FLOAT, research/hf/hfq_budget5.out).
- B_p = (4 q sin(pi s))^(-1/2) (1 - s)^(-(1-s)/2) s^(-s/2) with s = (p + 1)/q (AT-064 (1)).
  - C_sym = B_1/4 = 0.245877 (AT-064 Lemma SYM: ||Sym DU[k]||_(L^inf, op) <= C_sym ||k||_2^theta ||D^q k||_2^(1-theta)).
  - C_a = B_0/sqrt2 = 0.345320 (the C_0 of AT-228 (4)).
- S_1 = (2 sqrt(pi (q - 1)(q - 2)))^(-1) = 0.850548 (AT-227).
- S_w = (2 pi (q - 1))^(-1/2) = 0.380377; this is the sqrt2 S0 of AT-228.
- L_t = (2 pi)^(-1) int |eta|^t |ellhat(eta)| d eta = sigma 2^t Gamma((t + 1)/2) Gamma((t + 3)/2) at r0 = 1 (AT-223,
  AT-228). Values: L_0 = 2.199115, L_1 = 2.8, L_q = 7.350174. Here ellhat(eta) = -i sigma (eta/|eta|) K_1(|eta|).
- psi(x) = (1/2)((1 + x)^(q/2) - (1 + x)^(-q/2))^2 for x >= 0. A pair (B, A) with B > 1/2 is admissible if
  psi(x) <= A + B x^q on x >= 0.
  - Certified pairs (AT-230, closed-form proof AT-228): (101/200, 88), (51/100, 41), (13/25, 19), (53/100, 121/10),
    (11/20, 34/5), (3/5, 31/10).
  - This agent's arb bisection certificate (research/hf/cert_A0.py, output cert_A0.out) gives the slightly smaller
    values A <= 40.919, 18.959, 6.73, 2.96 at B = 0.51, 0.52, 0.55, 0.6. They are not used in the tables. They change
    Phi_max by less than 1e-4.

## 2. Lemma DEC (exact decomposition and symbols; CONFIRMED by AT-227 to AT-229)

For real S1 Schwartz k, u (a = U[k], b = a.ell, g = J^q u):
    E(k, u) = P'(a, g) + F_0'(a, u) - int b g^2 - Re ([J^q, b] u, g),
    P'(a, g) = q int (R'g)^T Sym(Da) (R'g),
    F_0'(a, u) = Re ([J^q, a.grad] u, g) - P'(a, g).
With s = r + p, khat evaluated at p and ghat at r and s:
    F_0'(a, u) = (2 pi)^(-1) int int (i m(p).r/2) H_q(<s>/<r>) khat(p) ghat(r) conj(ghat(s)) dr dp,
    Re ([J^q, b] u, g) = (2 pi)^(-1) int int (1/2)(T^(q/2) - T^(-q/2))^2 bhat(p) ghat(r) conj(ghat(s)) dr dp.

Sketch (the full proofs are AT-227 and AT-228).
- First line. W (a.grad h) = a.grad u - b u. Then J^q (a.grad u) = a.grad g + [J^q, a.grad] u,
  Re (a.grad g, g) = 0 since div a = 0, and J^q (b u) = b g + [J^q, b] u.
- Symbols. Symmetrize Re X = (X + conj X)/2 under (r, s, p) -> (s, r, -p), using m(p).r = m(p).s.
  - [J^q, a.grad] gives (i mu/2)(T^q - T^(-q)) with mu = khat(p) m(p).r.
  - The R' principal part gives (i mu/2) q (T - 1/T), since (r.p)(ahat.s) + (r.ahat)(p.s) = mu (<s>^2 - <r>^2).
  - [J^q, b] gives (1/2) bhat(p)(T^q + T^(-q) - 2).

Numerical check (FLOAT; not a proof). research/hf/symbol_check.py compares physical-space FFT values with the
trilinear sums on a 32 x 32 torus of side 12. The data are random real S1 functions band-limited to |n_i| < 8, and b is
even in both variables. The relative differences are 1.8e-14 for F_0' and 3.7e-14 for the weight commutator
(symbol_check.out).

## 3. Theorem HF-Q

Theorem HF-Q (CLAIMED; only the core constant is new). Let k be real S1 with R = ||k||_2 and K = ||D^q k||_2 finite,
and let u be real S1 Schwartz. Then |E(k, u)| <= l_Q(R, K) G^2, where for every admissible pair (B, A)
    l_Q(R, K) = q C_sym R^theta K^(1-theta)                                        (principal, Lemma PR)
              + (53/100) S_1 K                                                    (core, Lemma CORE)
              + (sigma/(2 r0)) C_a R^(1-1/q) K^(1/q)                                (int b g^2, Lemma WK)
              + A L_0 C_a R^(1-1/q) K^(1/q)                                         (near weight, Lemma WK)
              + B S_w [ (sigma/(2 r0)) K + q 2^(q-2) (L_1 R^(1/q) K^(1-1/q) + L_q R) ] (far weight, Lemmas WK, ELL).
The values at P-S2 are in section 0 item 1. For k in K(R, M), K <= c_W M, and l_Q is nondecreasing in R and K.

Which terms are R-small. The int b g^2 term, the near weight term and the L_1, L_q parts of the far weight term carry a
positive power of R. At R = 4.8e-6 and M = 0.25 they total 0.031 M. The principal term carries only R^(1/21)
(0.45 M there). The core term and the 0.7 K part of the far weight term carry no power of R.

Lemma PR (AT-229). |P'(a, g)| <= q ||Sym Da||_(L^inf, op) ||R'g||_2^2 <= q C_sym R^theta K^(1-theta) G^2.

Lemma CORE (CLAIMED). |F_0'(a, u)| <= (53/100) S_1 ||D^q U[k]||_2 G^2 <= (53/100) S_1 K G^2.
Proof.
- Kernel. H_q(1/t) = -H_q(t), and H_q is nonnegative and increasing on t >= 1. Also
  tau - 1 = |<s> - <r>|/<min(|r|, |s|)> <= |p|/<min(|r|, |s|)>. With AT-221 (H_q(t) <= (53/50)(t - 1)^q on t >= 1)
  this gives
      |(m(p).r/2) H_q(T)| <= (53/100) |m(p).r| <min(|r|, |s|)>^(-q) |p|^q.
  Unlike AT-227, the factor |m(p).r| is kept and is not replaced by min(|r|, |s|), and |p|^q is not raised to <p>^q.
- Hilbert-Schmidt bound. Put Kmat(s, r) = (53/100) |m(s - r).r| <min(|r|, |s|)>^(-q) kappa(s - r), where
  kappa(p) = |p|^q |khat(p)|. Then
      |F_0'| <= (2 pi)^(-1) int int Kmat(s, r) |ghat(r)| |ghat(s)| dr ds <= (2 pi)^(-1) ||Kmat||_HS G^2,
  and
      ||Kmat||_HS^2 = int kappa(p)^2 I(p) dp,   I(p) = (53/100)^2 int |m(p).r|^2 <min(|r|, |r + p|)>^(-2q) dr.
- The integral I(p). Use <min>^(-2q) <= <r>^(-2q) + <r + p>^(-2q). In the second term, |m(p).r| = |m(p).(r + p)|
  because m(p).p = 0, so the substitution r -> r - p turns it into the first term. Hence
      I(p) <= 2 (53/100)^2 int |m(p).r|^2 <r>^(-2q) dr = 2 (53/100)^2 |m(p)|^2 pi J_3,
  where J_3 = int_0^inf rho^3 (1 + rho^2)^(-q) d rho = 1/(2 (q - 1)(q - 2)). The angular integral of cos^2 is pi,
  where AT-227's radial majorant has 2 pi. This is the factor 1/sqrt2.
- Conclusion. int |m(p)|^2 kappa(p)^2 dp = ||D^q U[k]||_2^2 <= K^2, so
      |F_0'| <= (2 pi)^(-1) (53/100) (2 pi J_3)^(1/2) ||D^q U[k]||_2 G^2 = (53/100) S_1 ||D^q U[k]||_2 G^2. QED.
Remarks.
- (i) No frequency gap and no support or parity assumption is used. The low part of k is included, so the low loss
  87.95 R is not needed (as in AT-229).
- (ii) FLOAT probe (research/hf/core_ratio.py). The supremum of 2 Ntilde/(f(|r|) + f(|s|)) is 1.0000, approached
  as |p| -> infinity, where Ntilde = |m.r| |H_q(T)|/(2 <p>^q) and f(t) = t <t>^(-q). So 53/100 cannot be lowered below
  1/2 by a pointwise kernel bound. Replacing 53/100 by 1/2 would give 0.425 in place of 0.451, a 6 percent gain at
  most.

Lemma WK (AT-228 at alpha = 0). |int b g^2| <= ||b||_inf G^2 <= (sigma/(2 r0)) ||a||_A G^2. For every admissible
(B, A),
    |Re ([J^q, b] u, g)| <= A ||b||_A G^2 + B S_w ||D^q b||_2 G^2.
The proof uses x = |p|/<min>. The weight kernel is increasing in tau, tau <= 1 + x, and psi(x) <= A + B x^q. The first
part is bounded by Young's inequality, and the second by the Hilbert-Schmidt bound with
int <min>^(-2q) dr <= 2 pi/(q - 1).

Lemma ELL (AT-228 (4), (5), D0 = L0 V0; AT-223 for L_t). With R = ||k||_2 and K = ||D^q k||_2:
- ||a||_A <= C_a R^(1-1/q) K^(1/q);
- ||b||_A <= L_0 ||a||_A;
- ||D^q b||_2 <= (sigma/(2 r0)) K + q 2^(q-2) (L_1 R^(1/q) K^(1-1/q) + L_q R).

Proof of Theorem HF-Q. Combine Lemma DEC with Lemmas PR, CORE, WK and ELL for Schwartz k. For general k with R and K
finite, E(k, u) = int U[k].(W grad h J^(2q) u) dX is continuous in k in L^2 for fixed Schwartz u. The bound then
extends by density, exactly as in AT-229. QED.

## 4. Invariant-ball condition (AT-229) and its dependence on R, M and F

Proposition S0 (= AT-229 (3) to (5), CONFIRMED as a conditional implication).
- Hypotheses.
  - The base estimate Q_0(u) <= -b0 G^2 + C0 ||h||_2^2 holds for the actual generator on real S1 Schwartz u, with
    b0 > 0 and C0 >= 0.
  - The perturbed inverse exists uniformly on K(R, M) in the generator framework of AT-066/069/114/178, and its
    solution z = T(k) of A_k z = -F satisfies ||z||_2 <= R (R = ||F||_2/beta_0 in the AT-114 setting).
  - b = b0 - l(M) > 0, where |E(k, u)| <= l(M) G^2 on K(R, M).
- Conclusion. b N(z)^2 <= N(F) N(z) + C0 R^2. Hence N(z) <= M as soon as
      (S0-d)   N(F) M + C0 R^2 <= b M^2,
  which follows from the more conservative condition
      (S0-c)   N(F) + (b0 C0)^(1/2) R <= b M.
- The other two constraints of K(R, M) are those of AT-114 (6): the L^2 bound and the R3 normalization.
Proposition S of T2_BUD_v01 with T_1 = 0 is (S0-c). The direct form (S0-d) is AT-229's improvement.

Corollary HF-Q-B (CLAIMED through Lemma CORE; with the AT-227 core in place of Lemma CORE it is AT-229).
- Assumptions. 0 < b0 < beta with C^opt(b0) < infinity, and the retained hypotheses of Proposition S0.
- Conclusion. T(K(R, M)) is contained in K(R, M) whenever (HFQ) of section 0 holds with R = ||F||_2/beta_0, that is,
      N(F) M + C^opt(b0) R^2 <= (b0 - l_Q(R, c_W M)) M^2.
- Form (13.1). N(T(k)) <= A_F + eta(R, M) N(T(k)) on K(R, M), with A_F = (N(F) + (b0 C^opt(b0))^(1/2) R)/b0 and
  eta(R, M) = l_Q(R, c_W M)/b0. Then (S0-c) reads A_F <= (1 - eta(R, M)) M.

Dependence on R, M and F. Put K = c_W M and rho = R/K. Then
    eta(R, M) = (K/b0) [0.4508 + 0.2663 B + 0.5164 rho^(1/21) + (0.2418 + 0.7594 A) rho^(11/21)
                        + 0.3804 B (6.3021 rho^(10/21) + 16.5433 rho)].
- In M: eta is linear in M up to the slowly varying factors rho^(1/21), rho^(10/21) and rho^(11/21).
- In R: the only order-one R-dependence is the principal term. rho^(1/21) is 0.58 at R = 4.8e-6 and K = 0.37.
- In F: the only F-dependence is N(F) and the radius R = ||F||_2/beta_0.
- Floor. For every R and every admissible pair, B > 1/2 gives l_Q > (0.4508 + 0.1331) c_W M = 0.869 M. Hence
  Phi(M) := (b0 - l_Q) M < b0 M - 0.869 M^2, so Phi_max < 0.2877 b0^2 whatever ||F||_2 is. That is 0.104, 0.122 and
  0.141 at b0 = 0.60, 0.65 and 0.70. This is a property of the HF-Q route, not of the problem.

What HF-Q does not give. The task's preferred theorem would need only ||F||_2 small, with eta -> 0 as R -> 0 at fixed
M. That needs the tame structure.
- The coefficient-high, input-low region must cost T_1 N(k) ||grad h||_inf G, which is R-small through the GN bound
  of grad h, instead of a quadratic multiple of K G^2.
- In route Q this region is where the core and far weight terms come from, and they carry no power of R.
- The tame route needs the weighted commutator constant of X4 and is OPEN (notes/T2_X4_v01.md, in preparation).
- At q = 21/10 its gain is limited in any case: the GN factor R^theta (c_W M)^(1-theta) is 0.86 M to 1.02 M at the
  radii in question (T2_BUD_v01 section 4).

## 5. Tables (FLOAT inputs; HEURISTIC orientation; research/hf/hfq_budget5.py, output hfq_budget5.out)

The script ran on core 40 at nice 19 with OMP_NUM_THREADS=1, at 2026-11-03T01:36Z, in a few seconds.
- M is scanned on a log grid of 6001 points in [1e-4, 2], and l_Q is minimized over the six AT-230 pairs.
- R = ||F||_2/beta_0.
- Grid maxima are not certified maxima (AT-230 records exact witnesses for the audited core).
- Rate admissibility. b0 = 0.60 is the certified 007 lower margin. b0 = 0.6588 is the envelope just below the 007 cap.
  b0 = 0.65 needs a 007 margin above 0.65, which is not certified. b0 = 0.70 needs the corrected center with a
  certified rate above 0.70; its FLOAT margins sit at the cap 0.7103.
- Reproduction check. With the AT-227 core sqrt2 (53/100) S_1 K_J in place of Lemma CORE, the same script gives
  0.054220, 0.063759 and 0.074079 at b0 = 0.60, 0.65 and 0.70 (||F||_2 = 1e-5, beta_0 = 2.09). This agrees with the
  AT-230 lower decimals 0.054218, 0.063757 and 0.074077.

Table 1. Phi_max = largest N(F) with (HFQ) at C^opt = 0; maximizing M in parentheses. beta_0 = 2.09. The
beta_0 = 1.862 rows in the output file are lower by at most 0.00035.

| ||F||_2 | b0 = 0.60 | b0 = 0.65 | b0 = 0.6588 | b0 = 0.70 |
|---:|---:|---:|---:|---:|
| 9.9e-6 | 0.06550 (0.222) | 0.07704 (0.240) | 0.07917 (0.244) | 0.08954 (0.259) |
| 1e-5 | 0.06548 (0.222) | 0.07702 (0.240) | 0.07915 (0.244) | 0.08951 (0.259) |
| 2.8e-5 | 0.06329 (0.214) | 0.07450 (0.234) | 0.07657 (0.237) | 0.08664 (0.252) |
| 3e-5 | 0.06316 (0.214) | 0.07431 (0.233) | 0.07637 (0.236) | 0.08642 (0.252) |
| 6e-5 | 0.06170 (0.209) | 0.07263 (0.227) | 0.07464 (0.231) | 0.08445 (0.245) |

Table 2. Largest admissible C^opt(b0) in (HFQ), with beta_0 = 2.09. Each cell gives the direct budget
max over M of M (Phi(M) - N(F))/R^2, then the conservative budget (Phi_max - N(F))^2/(b0 R^2). "none" means
Phi_max <= N(F). N(F) = 0.0257 is the FFT P-S2 value at the current fit target, and 0.0765 is the earlier C5 + h value,
which belongs to ||F||_2 = 2.8e-5 (both FLOAT; the coordinator 00:44Z item 3 and 23:56Z item 4).

| ||F||_2 | b0 | N = 0.0257 | N = 0.035 | N = 0.05 | N = 0.0765 |
|---:|---:|---:|---:|---:|---:|
| 9.9e-6 | 0.60 | 4.42e8 / 1.18e8 | 3.31e8 / 6.91e7 | 1.61e8 / 1.78e7 | none |
| 9.9e-6 | 0.65 | 6.24e8 / 1.81e8 | 5.02e8 / 1.21e8 | 3.12e8 / 5.01e7 | 5.84e6 / 2.03e4 |
| 9.9e-6 | 0.70 | 8.43e8 / 2.59e8 | 7.09e8 / 1.89e8 | 5.00e8 / 9.95e7 | 1.56e8 / 1.08e7 |
| 2.8e-5 | 0.60 | 5.05e7 / 1.31e7 | 3.71e7 / 7.43e6 | 1.67e7 / 1.64e6 | none |
| 2.8e-5 | 0.6588 | 7.61e7 / 2.19e7 | 6.10e7 / 1.46e7 | 3.77e7 / 5.97e6 | 8.92e4 / 3.87e1 |
| 2.8e-5 | 0.70 | 9.76e7 / 2.96e7 | 8.14e7 / 2.12e7 | 5.61e7 / 1.07e7 | 1.46e7 / 8.18e5 |
| 6e-5 | 0.60 | 1.03e7 / 2.62e6 | 7.42e6 / 1.44e6 | 3.11e6 / 2.77e5 | none |
| 6e-5 | 0.65 | 1.47e7 / 4.11e6 | 1.15e7 / 2.64e6 | 6.68e6 / 9.56e5 | none |
| 6e-5 | 0.70 | 1.99e7 / 5.98e6 | 1.65e7 / 4.24e6 | 1.12e7 / 2.06e6 | 2.42e6 / 1.10e5 |

Table 3. The terms of l_Q(R, c_W M)/M at ||F||_2 = 1e-5, beta_0 = 2.09 and (B, A) = (11/20, 34/5).

| M | principal | core | int b g^2 | near weight | far weight | total |
|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 0.4853 | 0.6709 | 0.0023 | 0.0490 | 0.2381 | 1.4455 |
| 0.10 | 0.4695 | 0.6709 | 0.0016 | 0.0341 | 0.2323 | 1.4084 |
| 0.20 | 0.4543 | 0.6709 | 0.0011 | 0.0237 | 0.2283 | 1.3782 |
| 0.25 | 0.4495 | 0.6709 | 0.0010 | 0.0211 | 0.2272 | 1.3696 |
| 0.30 | 0.4456 | 0.6709 | 0.0009 | 0.0192 | 0.2264 | 1.3629 |

Table 4. Tradeoff in ||F||_2: Phi_max at C^opt = 0 and beta_0 = 2.09.

| ||F||_2 | 1e-8 | 1e-7 | 1e-6 | 1e-5 | 1e-4 | 1e-3 | 1e-2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| b0 = 0.60 | 0.07499 | 0.07230 | 0.06922 | 0.06548 | 0.06046 | 0.05186 | 0.03379 |
| b0 = 0.65 | 0.08811 | 0.08496 | 0.08138 | 0.07702 | 0.07120 | 0.06136 | 0.04067 |
| b0 = 0.70 | 0.10230 | 0.09865 | 0.09452 | 0.08951 | 0.08283 | 0.07167 | 0.04823 |

Reading (HEURISTIC).
- Corrected center at the fit target. With (N(F), ||F||_2) about (0.026, 1e-5), (HFQ) holds at C^opt = 0 with a
  factor 2.5 to 3.5 of room in N(F). It still holds with C^opt(b0) up to 4.4e8 (b0 = 0.60) to 8.4e8 (b0 = 0.70).
  At this point the k-dependent losses are no longer the binding item; the weak constant is.
- What decides the weak constant. The first theory agent (note 12 item 4) estimates the explicit Lemma QW construction at 1e10 or more,
  and the cell prices a positive remainder would force at 3e6 to 2.5e7. So the open decision is whether C^opt(b0) is
  below a few times 1e8 at a rate b0 in [0.60, 0.70] for the corrected center.
- What each source quantity buys. Lowering ||F||_2 from 6e-5 to 1e-5 raises the C^opt budget by a factor of about 40
  (through R^2) but raises Phi_max by only 0.004. Lowering N(F) is what moves the k-dependent side.
- The earlier C5 + h level (N(F) = 0.0765 at ||F||_2 = 2.8e-5) fails (HFQ) at b0 = 0.60 and 0.65 even at C^opt = 0.
  It leaves at most 8.9e4 at the 007 envelope 0.6588, and 1.5e7 at 0.70 (corrected center only).

## 6. Comparison with earlier explicit bounds (FLOAT values at R = 1.4e-5, M = 0.31)

| source | structure | non-principal loss | principal |
|---|---|---|---|
| AT-186 (the external referee t2-cbar1) | homogeneous bare remainder, Peetre steps | A_q c_W = 17.3 M times an interpolation factor | separate |
| t2-hf2 corrected (AT-223, cut 1) | all quadratic, homogeneous Riesz principal, one-sided Schur core, K_J | 0.589929 = 1.903 M | separate |
| AT-229 (hfq_budget2 version, audited) | all quadratic, R' principal, radial core sqrt2 c S_1 K_J, alpha = 0 weight split | 0.37675 = 1.215 M | 0.47 M |
| HF-Q (this note) | as AT-229 with the angular Hilbert-Schmidt core c S_1 K_h | 0.29059 = 0.937 M | 0.47 M |

Notes on the comparison.
- The principal parts differ. t2-hf2 uses the homogeneous Riesz principal part and puts -int b |Rg|^2 in it; HF-Q
  uses R' and bounds the whole int b g^2. The t2-hf2 number covers the high piece only and adds the low loss
  87.95 R = 1.2e-3.
- For T2_BUD_v01 form 2 the tame cost T_1 C_grad d M^(1-theta) (about 0.6 M at T_1 = 1) has to be added. In HF-Q it
  is absent.

## 7. Corrections and distinctions

1. The t2-hf2 question (scratch/an external referee answer) and T2_BUD_v01 section 5 (form 2) attribute
   ||J^q k||_2 <= c_W N(k) to AT-169. This is wrong: AT-169 proves ||D^q k||_2 <= c_W N(k) only (AT-204, AT-220).
   - HF-Q uses only the homogeneous bound.
   - For t2-hf2 the repair is K_J of AT-220, giving the corrected losses 0.589929, 0.582129 and 0.574967 at cuts 1, 2
     and 3 (AT-223).
   - The T2_BUD_v01 GN arguments need only the homogeneous bound (AT-204).
2. T2_BUD_v01 Proposition S is sufficient, not equivalent to (6_l). Table D is the sampled (6_l) budget, not the (S)
   budget (AT-202, AT-203; corrected values in the theory audit exchange/audit_v80.md).
3. The T2_BUD_v01 rows at b = 0.6607 cannot be used for unchanged 007. The 007 P-S2 matrix infimum is below
   0.6588409179 (AT-199), and C^opt(b) = +infinity from there on (HF-NEC-1). The b = 0.7103 rows are limits for the
   corrected center, strictly below its origin cap (AT-211 to AT-216).
4. The low/high split of CB-ZERO and Lemma LOW (T2_CEPS_v01) is not needed for HF-Q. CB-ZERO and LOW remain valid and
   give the sandwich of Corollary CB-S, which is a separate statement.
5. The t2-hf2 W-REM statement with T_1 = 1 is purely quadratic; the nominal tame coefficient is unused (AT-223). A
   small-loss weighted tame estimate remains OPEN.

## 8. Status and requests

| item | status |
|---|---|
| Lemma DEC, Lemma PR, Lemma WK, Lemma ELL | CONFIRMED (AT-227 to AT-229, AT-223) |
| Lemma CORE (angular Hilbert-Schmidt, D^q) | CLAIMED, new; scalar input CONFIRMED (AT-221) |
| Theorem HF-Q | CLAIMED (CONFIRMED with the AT-227 core: AT-229) |
| Proposition S0 | CONFIRMED as a conditional implication (AT-229) |
| Corollary HF-Q-B | CLAIMED through Lemma CORE |
| Tables 1 to 4 | FLOAT, HEURISTIC |
| explicit C^opt(b0) | OPEN (the first theory agent) |
| tame route (eta -> 0 as R -> 0) | OPEN (X4) |

- To the theory auditor: audit Lemma CORE only. The checks needed are the step that keeps |m(p).r| (not min(|r|, |s|)), the
  translation r -> r - p with m(p).p = 0, the angular integral pi J_3, and |p|^q in place of <p>^q. Optionally,
  reissue the eighteen AT-230 witnesses with the new core: the hfq_budget5 maximizers are M = 0.222, 0.240, 0.259 at
  b0 = 0.60, 0.65, 0.70 (||F||_2 = 1e-5, beta_0 = 2.09).
- To the first theory agent (for theory_v04). Theorem HF-Q and Corollary HF-Q-B can be quoted as the explicit k-dependent part of the
  invariant-ball condition at P-S2, with the labels above; AT-229 is the CONFIRMED fallback. The open item for an
  explicit closure is an explicit upper bound on C^opt(b0), of order a few times 1e8 or less, at a certified rate
  b0 in [0.60, 0.70] for the corrected center.
- To the coordinator and the first numerics agent (planning, HEURISTIC). With HF-Q the source target is N(F) well below Phi_max (0.065 at
  b0 = 0.60, 0.090 at b0 = 0.70), with ||F||_2 as small as possible for the weak term. At the fit target the
  k-dependent side has a factor 2.5 to 3.5 of room.
