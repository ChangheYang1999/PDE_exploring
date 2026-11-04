# T2_WGK_v01: a k-uniform Garding inequality on the ball, the sharp strain constant, the exact order of the gap loss, and a closure function

Version 1. Owner: the second theory agent. Started 2026-11-02T20:25Z. Plain-text mathematics as in T2_O2S_v02.

Builds on (frozen files are not edited):
- theory_agent_2/notes/T2_O2S_v02.md (SHA256 da418c66...), sections 1 to 10, notation unchanged;
- theory_agent_2/research/kpw/PROOF.md (Lemma KP-W, SHA256 c06f660d...), CONFIRMED by AT-049 to AT-051 (the coordinator 20:10Z item 2);
- THEORY_NEW_RESULTS.md, Lemma WG and its proof (AT-029), IMPORTED;
- an external referee answer (launched 2026-11-02T19:45Z, collected about 20:05Z). Its statements are claims;
  section 1.3 lists what the second theory agent checked.

## Change list against T2_O2S_v02

1. v02 section 10 ("WG-k", OPEN) is replaced by Lemma WG-K (CLAIMED, section 1).
2. In the closure, the absorption kappa_bar(R, M) of v02 section 5, which carries the non-explicit KP-W constants c_1,
   c_2, c_3, is replaced by the explicit tau_bar(R, M) of section 3. The HEURISTIC value c_1 = q of v02 section 8(c) is no
   longer needed: q enters through the exact frozen matrix.
3. New: Lemma SYM. The strain enters only through Sym DU[k], and its pointwise constant is C*_sym = 0.1324 at q = 5/2,
   against C_GN^U = 0.4051 in v02 (section 3).
4. New: the gap loss on K^S_{R,M} has exact order R^theta M^(1-theta) at fixed M, with the constant q C*_sym up to the
   factor c_W^(1-theta) (section 4). Origin cancellation (v02 section 10) gives no gain in order.
5. The necessary test of v02 section 8(d) is revised for this route (section 5).
6. New: the binding term of the closure is the tame term, not the absorption (section 6).
7. New: a closure function for the numerics, with every unknown constant named (section 7; the coordinator 20:10Z item 4(c)).
8. Route and target times for the explicit constants (section 8; the coordinator 20:10Z item 3(a)).
9. Answer to the question left in PROOF.md section 10 (section 1.4).

## Status table

| ID (proposed) | statement | status | section |
|---|---|---|---|
| T2-WGK | Lemma WG-K: Garding inequality uniform over the ball, with the exact frozen matrix | CLAIMED | 1 |
| T2-NC | the full rough remainder is not weakly continuous on the ball | CLAIMED | 1.4 |
| T2-UTK | stationary estimate UT-K | CLAIMED | 2 |
| T2-SinvK | invariance (S-inv-K) and Corollary THR-K | CLAIMED (implication as in AT-036) | 2 |
| T2-SYM | Lemma SYM, sharp pointwise strain constant | CLAIMED | 3 |
| T2-TAU | explicit gap bound beta_Kbar >= beta - tau_bar | CLAIMED | 3 |
| T2-OBS | lower bound for the gap loss | CLAIMED | 4 |
| T2-INF | condition at infinity for an origin-binding gap | CLAIMED | 4 |
| T2-NT2 | revised necessary test | implication CLAIMED; values FLOAT | 5 |
| T2-CF | closure function | HEURISTIC (unknown constants) | 7 |

## 1. Lemma WG-K

### 1.1 Setting

Notation of v02 section 1: N(f) = ||<D>^q (W f)||, W = (1 + |X|^2/r0^2)^(sigma/2), 2 < q < 3, theta = (q - 2)/q,
theta_0 = (q - 1)/q, A(z) = ||grad z||_inf + ||z||_inf. For real k put a = U[k], ell_W = grad log W = sigma X/(r0^2 + |X|^2),
p_k = a.ell_W, and (v02 section 8(a))
    N_q^(k)(X) = N_q(X) + q Sym DU[k](X) - p_k(X) I,     N_q = q Sym DV + Kmat - (c + 1 + a_W) I,   a_W = V.ell_W.
Reference ball, without the constraint ell = 0:
    Kbar = Kbar_(Rbar, Mbar) := {k real, S1, ||k||_2 <= Rbar, N(k) <= Mbar},
    beta_Kbar := inf over k in Kbar of inf over X of ( -lambda_max N_q^(k)(X) ).
K^S_{R,M} is contained in Kbar_(Rbar, Mbar) when R <= Rbar and M <= Mbar. Since 0 is in Kbar, beta_Kbar <= beta, the
BG-q gap of rho_bar.

### 1.2 Statement and proof

Lemma WG-K [T2-WGK]. Assume (BG-reg; gamma_*), the R1 Hilbert-Schmidt identity, 2 < q < 3, 0 <= sigma < 1 + gamma_*,
r0 > 0, and beta_Kbar > 0. Then sigma > q - 1 - 1/c > 0, and for every 0 < eps < beta_Kbar there is C_eps_bar < infinity
such that for every k in Kbar and every real S1 Schwartz u, with g = <D>^q u and h = W^(-1) u:
    Re < <D>^q W A_k W^(-1) u, g > <= -(beta_Kbar - eps) ||g||^2 + C_eps_bar ||h||^2 + c_4' N(k) A(h) ||g||.      (WG-K)
Here c_4' = c_4 (1 + C_chi), c_4 is the KP-W tame constant, and C_chi bounds N(chi(D/Lambda) f) <= C_chi N(f) uniformly in
Lambda >= 1 (chi a fixed radial cutoff). C_eps_bar depends on Kbar, eps and the background, not on k. For k not Schwartz
the k-part of the left side is defined by KP-W (ii).

Proof (route of the external referee t2-wgk1 part (a)).
- Step 1 (sigma > 0). As |X| -> infinity, a, Da, Sym D u_bar, Kmat and a_W - sigma c tend to 0, so N_q^(k)(X) tends to
  (q c - c - 1 - sigma c) I. With k = 0, beta_Kbar > 0 gives q c - c - 1 - sigma c < 0, that is
  sigma > q - 1 - 1/c, and q - 1 - 1/c > q - 2 > 0 since c > 1.
- Step 2 (compactness of the ball in L^2). The operator W^(-1) <D>^(-q) is compact on L^2: f(X) m(D) is compact when f and m
  are continuous and tend to 0 at infinity (truncate both; the truncations are Hilbert-Schmidt and converge in norm),
  and W^(-1) tends to 0 because sigma > 0. Hence Kbar is compact in L^2. With the uniform bound ||k||_(H^q) <= C N(k),
  weakly convergent sequences in Kbar converge in H^s for every s < q, so U[k] and DU[k] converge uniformly.
- Step 3 (uniform compact remainders). If a family of compact operators on L^2 is norm compact, then for every eta > 0
  there is C_eta with |<C g, g>| <= eta ||g||^2 + C_eta ||W^(-1) <D>^(-q) g||^2 for every member C. (Take a finite
  operator-norm net, approximate its members by finite-rank operators with Schwartz vectors psi, and use
  <g, psi> = <W^(-1) <D>^(-q) g, W <D>^q psi>.) Note W^(-1) <D>^(-q) g = h.
- Step 4 (frequency truncation of the coefficient). Put k_Lambda = chi(D/Lambda) k and e_Lambda = k - k_Lambda. By Fourier
  Cauchy-Schwarz, uniformly on Kbar: ||U[e_Lambda]||_inf <= C Mbar Lambda^(1-q), ||DU[e_Lambda]||_inf <= C Mbar Lambda^(2-q),
  ||e_Lambda||_2 <= C Mbar Lambda^(-q). Also N(e_Lambda) <= (1 + C_chi) N(k) (Peetre: W(X)/W(X - Z/Lambda) <= C <Z>^sigma,
  with the same bound for the X-derivatives through order three).
- Step 5 (band-limited coefficient). For a = U[k_Lambda] (divergence free, in L^2, Fourier support in |xi| <= 2 Lambda),
  the principal-plus-compact calculation of Lemma WG (IMPORTED) extends to
      Re < <D>^q W A_(k_Lambda) W^(-1) u, g > = int (R g)^T N_q^(k_Lambda) (R g) dX - q c ||<D>^(-1) g||^2 + <(C_0 + C_a) g, g>,
  with C_0 the compact operator of Lemma WG and C_a compact. The k-terms: W (a.grad)(W^(-1) u) = a.grad u - p u; the form
  of a.grad g vanishes (div a = 0); the Taylor expansion of <xi>^q gives the principal commutator
  q sum_(j,l) (d_j a_l) Rt_j^* Rt_l; the Taylor remainder has Fourier kernel bounded by C_L |a_hat(eta)| <xi>^(-1), so it is
  Hilbert-Schmidt after an input frequency cut and small in norm after it, and it is norm continuous in a in L^2
  (||a_hat||_1 <= C_L ||a||_2 for fixed band); [<D>^q, p] <D>^(-q) is treated the same way, with ||p||_(H^(q+2))
  <= C_L ||a||_2; moving the C_0 coefficients d_j a_l and p between Riesz factors and replacing Rt by R are compact
  ([R_j, f] compact for f in C_0, uniformly continuous). By Step 2, k -> U[k_Lambda] is continuous from Kbar (weak) to
  L^2, so the family {C_0 + C_a} is norm compact.
- Step 6. Choose Lambda, independent of k, such that q ||DU[e_Lambda]||_inf + ||p_(e_Lambda)||_inf <= eps/3 and the
  non-tame KP-W coefficient c_1 eps(e_Lambda) + c_2 ||e_Lambda||_2 + c_3 ||U[e_Lambda]||_inf <= eps/3. Weyl's inequality
  gives lambda_max N_q^(k_Lambda) <= -beta_Kbar + eps/3, and sum_j ||R_j g||^2 = ||g||^2. With Step 3 (eta = eps/3) and
  dropping -q c ||<D>^(-1) g||^2 <= 0, the k_Lambda energy is at most -(beta_Kbar - 2 eps/3) ||g||^2 + C_eps_bar ||h||^2.
  The k-part of the energy is linear in k, so KP-W applied to e_Lambda gives a difference of at most
  (eps/3) ||g||^2 + c_4 N(e_Lambda) A(h) ||g||. With Step 4 this is (WG-K). QED.

### 1.3 What the second theory agent checked

- Step 1: the limit of N_q^(k) and the chain sigma > q - 1 - 1/c > q - 2.
- Step 2: compactness of W^(-1) <D>^(-q) and the H^s convergence.
- Step 4: the three Cauchy-Schwarz bounds (exponents 1 - q, 2 - q, -q).
- Step 5: consistency with the first theory agent's form Q(g): q c ||Rt g||^2 = q c ||g||^2 - q c ||<D>^(-1) g||^2; the sign of p from
  W a.grad(W^(-1) u) = a.grad u - (a.grad log W) u, which matches v02 section 8(a); the two Fourier kernel bounds.
- Step 6: linearity of the k-part of the energy, so KP-W (form (i), and (ii) for rough e_Lambda) applies to e_Lambda.
Not checked independently: the value of C_chi (only finiteness is used), and the extension of Lemma WG's principal
calculation in Step 5, which follows the first theory agent's proof structure (AT-029) and should be audited together with it.

### 1.4 Remark: the rough remainder is not weakly continuous [T2-NC]

For each k the remainder after the principal form is compact, but it is not weakly continuous on the ball. Example
(the external referee t2-wgk1, checked): chi_0 in C_c^infinity, S1, supported away from 0; psi_n = n^(-q-2) chi_0(X) cos(n x);
k_n = -Delta psi_n. Then U[k_n] = (-d_x d_y psi_n, d_x d_x psi_n) exactly, ell(k_n) = 0, N(k_n) is bounded, k_n -> 0 weakly,
and U[k_n], DU[k_n] -> 0 uniformly. For a fixed S1 h in C_c^infinity with chi_0 d_y h not 0 and u = W h, the term
<D>^q (W U[k_n].grad h) has L^2 norm tending to ||W chi_0 d_y h||/sqrt(2) > 0. So the tame part has to be split off before
any compactness argument, as Step 4 does.
This answers the question left in research/kpw/PROOF.md section 10 (frozen, not edited): a compactness argument relative
to the weight works after the frequency truncation of Step 4, and the C^delta remainder of the refinement is not needed.

## 2. UT-K and the invariance (S-inv-K)

UT-K [T2-UTK]. Assume Lemma WG-K and the IMPORTED R1 and R2 hypotheses. Let k be in Kbar with ||k||_2 < Rbar and
N(k) < Mbar, and let G be real and S1 with N(G) < infinity. Then the L^2 solution z of A_k z = -G has N(z) < infinity and
    b N(z) <= N(G) + c_4' N(k) A(z) + (b C_eps_bar)^(1/2) ||z||,      b := beta_Kbar - eps.
Proof. AT-038 (reviewed in v02 section 4.2), with the gap condition kappa(k) < beta - eps replaced by (WG-K). The Schwartz
approximants k_n of k lie in Kbar for large n because the inequalities are strict; they need not satisfy ell = 0, and
Kbar has no ell constraint. The last step is b x^2 <= d x + C y^2 => b x <= d + (b C)^(1/2) y. QED.

(S-inv-K) [T2-SinvK]. Assume (H-S) of v02 section 5, Lemma WG-K for Kbar = Kbar_(Rbar, Mbar), R = ||F||_2/beta_0 < Rbar,
0 < M < Mbar and 0 < eps < beta_Kbar. Put b = beta_Kbar - eps and
    A_F^K := N(F)/b + (C_eps_bar/b)^(1/2) R,
    eta^K(R, M) := (c_4'/b) [ C_GN c_W^(1-theta) R^theta M^(1-theta) + C_inf c_W^(1-theta_0) R^theta_0 M^(1-theta_0) ].
If A_F^K + eta^K(R, M) M <= M, then T(K^S_{R,M}) is contained in K^S_{R,M}, and N(T(k)) <= A_F^K + eta^K M for every k in
K^S_{R,M}.
Proof. Theorem D-S (v01 section 6, AT-036) with UT-K in place of UT-S. Nothing else changes. QED.

Corollary THR-K (only ||F||_2 small). Assume (H-S) and N(F) > 0. Let eps = beta/4, M = 8 N(F)/beta, Mbar = 9 N(F)/beta,
choose R0 > 0 with tau_bar(R0, Mbar) <= beta/4 (section 3; explicit), and let C_bar be the constant of Lemma WG-K for
Kbar_(R0, Mbar) and eps. If R < R0, (2 C_bar/beta)^(1/2) R <= 2 N(F)/beta and eta^K(R, M) <= 1/2 (computed with
b = beta/2), then T(K^S_{R,M}) is contained in K^S_{R,M}.
Proof. Section 3 gives beta_Kbar >= beta - tau_bar >= 3 beta/4, so b >= beta/2. Then A_F^K <= 2 N(F)/beta + 2 N(F)/beta
= M/2, and A_F^K + eta^K M <= M/2 + M/2. QED.
This is a theorem of the preferred type (only ||F||_2 small, N(F) finite), like THR-S of v02. The difference: the
absorption threshold R0 is explicit. The other two conditions still contain C_bar and c_4'.

## 3. Lemma SYM and the explicit gap bound

Lemma SYM [T2-SYM]. Let 2 < q < 3 and let f be real in L^2 cap Hdot^q. For every X,
    ||Sym DU[f](X)||_op <= C*_sym(q) ||f||^theta ||f||_(Hdot^q)^(1-theta),
    C*_sym(q) = (2 pi)^(-1) (pi/8)^(1/2) (J_0 + J_2) / (J_0^(theta/2) J_2^((1-theta)/2)),
    J_0 = B(2/q, 2 - 2/q)/(2q),   J_2 = B(1 + 2/q, 1 - 2/q)/(2q)   (B the Beta function).
C*_sym is the sharp constant of the Fourier-L^1 bound used, and C*_sym <= C(q, 1, pi/8) = C_ell = C_GN^U/sqrt(8)
(v01 section 2).
Proof. div U = 0, so Sym DU[f](X) is trace free and its operator norm is sup over unit e of e^T DU[f](X) e. With
m(xi) = (xi_1 xi_2, -xi_1^2)/|xi|^2 = cos(phi) (sin phi, -cos phi) and e = (cos alpha, sin alpha),
    e^T DU[f](X) e = (2 pi)^(-2) int i (e.xi)(e.m(xi)) fhat(xi) e^(i X.xi) d xi,   (e.xi)(e.m(xi)) = |xi| cos(phi) sin(2 phi - 2 alpha)/2.
The angular weight w_alpha = |cos(phi) sin(2 phi - 2 alpha)|/2 has int_0^(2 pi) w_alpha^2 d phi = pi/8 for every alpha
(the cross term cos(2 phi) cos(4 phi - 4 alpha) integrates to 0). Lemma GN with p = 1 and I_w = pi/8 gives the constant
C_ell. For the sharp constant, maximize int |xi| w |fhat| under fixed ||f|| and ||f||_(Hdot^q). The problem is convex. The
KKT maximizers are |fhat| = |xi| w/(lambda + mu |xi|^(2q)); all of them are dilations and multiples of the case
lambda = mu = 1, and the ratio is invariant under both. That case gives the formula, with J_1 = J_0 + J_2. QED.
FLOAT values (scratch/wgk/sharp_sym.out):

| q | C_GN^U (v02) | C_ell | C*_sym |
|---|---|---|---|
| 2.40 | 0.432792 | 0.153015 | 0.142941 |
| 2.50 | 0.405052 | 0.143208 | 0.132432 |
| 2.60 | 0.384663 | 0.135999 | 0.124718 |

Cross-check (scratch/wgk/check_kkt.out, FLOAT): direct quadrature of J_0, J_1, J_2 agrees to six digits; 300 random
radial profiles per q stay below C*_sym (best ratios 0.114, 0.110, 0.111). Against v02 the strain constant drops by the
factor 0.327 at q = 5/2 (1/sqrt(8) = 0.354 from the angular weight, 0.925 from the sharp radial profile).

Proposition TAU [T2-TAU]. For all Rbar, Mbar > 0,
    beta_Kbar >= beta - tau_bar(Rbar, Mbar),
    tau_bar := q C*_sym Rbar^theta (c_W Mbar)^(1-theta)
               + min{ sigma C_GN^U Rbar^theta (c_W Mbar)^(1-theta),  (sigma/(2 r0)) C_inf^U Rbar^theta_0 (c_W Mbar)^(1-theta_0) }.
Proof. Weyl: lambda_max(N_q + q S - p I) <= lambda_max N_q + q ||S||_op + |p|. Lemma SYM with ||k||_(Hdot^q) <= c_W N(k)
bounds ||S||_op. For p: |ell_W(X)| = sigma r/(r0^2 + r^2) <= sigma/(2 r0) with ||U[k]||_inf <= C_inf^U R^theta_0 (c_W M)^(1-theta_0)
(v01 section 2); or U[k](0) = 0 (R3.2) gives |U[k](X)| <= eps(k) r, so |p_k| <= sigma eps(k) r^2/(r0^2 + r^2) <= sigma eps(k). QED.
All constants in tau_bar are explicit except c_W (>= 1; the second theory agent section 8).
Pointwise refinement (the external referee (13), (14), (16); CLAIMED, Weyl). With mu(X) := -lambda_max N_q(X) - beta >= 0,
beta_Kbar >= beta - sup over X of [ q d(|X|) + (sigma |X|/(r0^2 + |X|^2)) min(E, B(|X|)) - mu(X) ]_+, where
d(r) = min(D, H r^(q-2)) bounds ||Sym DU[k](X)||_op (D from Lemma SYM; H bounds the C^(q-2) seminorm, H <= C c_W Mbar by
the external referee (20), whose integral int |xi|^(2-2q) min(1, r^2 |xi|^2) d xi converges at both ends exactly when 2 < q < 3),
E = C_inf^U Rbar^theta_0 (c_W Mbar)^(1-theta_0), and B(r) = int_0^r of a bound for ||DU[k]||_op on the radius s. A FLOAT
evaluation needs the field mu(X) of the BG-q screen. Section 4 shows that at fixed M this cannot change the order.

## 4. The order of the gap loss is exact

Proposition OBS [T2-OBS]. Assume that the BG-q gap of rho_bar is attained at the origin: beta = c + 1 - q, that is
mu(0) = 0. (FLOAT: true at q = 5/2 for sigma >= 1.2 and r0 <= 1/2 in the first theory agent's screen; see v02 section 10.) Fix M > 0.
Then, as R -> 0,
    beta - beta_(K^S_{R,M}) >= q C*_sym R^theta M^(1-theta) (1 - o(1)).
With Proposition TAU (R0 = R, Mbar = M):
    q C*_sym R^theta M^(1-theta) (1 - o(1)) <= beta - beta_(K^S_{R,M}) <= q C*_sym R^theta (c_W M)^(1-theta) + O(R^theta_0 M^(1-theta_0)).
So the order R^theta M^(1-theta) is exact, and so is the constant up to the factor c_W^(1-theta). The vanishing of the
k-perturbation at the origin (v02 section 10) gives no gain in order at fixed M.
Proof.
- (i) Parity. S1 means h(-x, y) = h(x, y) and h(x, -y) = -h(x, y); rho_bar is S1. Then U_1[h] is odd in x and even in y,
  U_2[h] is even in x and odd in y, so the diagonal entries of DV and Kmat are even in both variables, the off-diagonal
  entries are odd in both, and a_W is even in both. Hence N_q(0) is diagonal and N_q(X) - N_q(0) = O(|X|^2). Let e_0 be a
  top eigenvector of N_q(0) (a coordinate vector).
- (ii) Profile. For delta > 0 take real f_delta with fhat_delta in C_c^infinity(R^2 minus 0) and
  e_0^T Sym DU[f_delta](0) e_0 >= (1 - delta) C*_sym ||f_delta||^theta ||f_delta||_(Hdot^q)^(1-theta) (smooth approximation
  of the KKT maximizer with phase -i sgn(w)). Translate it to Y_A = (A, A), make it S1 by adding the three reflected
  images (mutual distances >= 2A), and restore ell = 0 by subtracting a small multiple of a fixed S1 Schwartz function
  with ell not 0. By Schwartz decay the ratio at Y_A is >= (1 - 2 delta) C*_sym for A large. Call the result f.
- (iii) Scaling. Put k_lambda(X) = s f(X/lambda), with s and lambda fixed by the two conditions
  ||k_lambda||_(Hdot^q) = (1 - delta) M and ||k_lambda||_2 = R. In two dimensions ||f(./lambda)||_(Hdot^r) = lambda^(1-r) ||f||_(Hdot^r), so lambda is proportional to
  (R/M)^(1/q) and tends to 0. k_lambda is concentrated in |X| <~ A lambda, where W = 1 + O(A^2 lambda^2), so
  N(k_lambda) = ||k_lambda||_(Hdot^q) (1 + o(1)) <= M for R small. Thus k_lambda is in K^S_{R,M}. U is homogeneous of degree 0,
  so e_0^T Sym DU[k_lambda](lambda Y_A) e_0 = s lambda^(-1) e_0^T Sym DU[f](Y_A) e_0
  >= (1 - 2 delta) C*_sym R^theta ((1 - delta) M)^(1-theta).
- (iv) At X_lambda = lambda Y_A: e_0^T N_q^(k_lambda)(X_lambda) e_0 >= -beta - C A^2 lambda^2 + q (that strain) - |p(X_lambda)|,
  with |p(X_lambda)| <= (sigma |X_lambda|/r0^2) C_inf^U R^theta_0 M^(1-theta_0). Both error terms are o(R^theta M^(1-theta)):
  lambda^2 is of order R^(2/q) and 2/q > (q-2)/q since q < 4. Let delta -> 0. QED.
the external referee t2-wgk1 gives the case of the polynomial profile (1/2)(x - 2)^2 (y - 2), with a non-sharp constant. The second theory agent checked its
identity U[-Delta psi] = (-d_x d_y psi, d_x d_x psi), the values (22) (U = 0 and Sym DU = diag(-1, 1) at (2, 2)) and the
exponents A_lambda = t M lambda^(q-1), ||k_lambda||_2 = t M lambda^q ||f||_2, strain t M lambda^(q-2).

Remark (shrinking M). A gain in order is possible only if M shrinks with R: with a quadratic lower margin
mu(X) >= kappa |X|^2 near 0 and the exterior condition, the external referee (21) gives a loss <~ min(R^theta M^(1-theta), M^(2/(4-q))).
For a fixed F this regime is not available, since every admissible M is at least N(h_0) (section 5). HEURISTIC remark only.

Proposition INF [T2-INF]. At infinity N_q(X) tends to (q c - c - 1 - sigma c) I, so the BG-q gap is at most
min(c + 1 - q, c + 1 + sigma c - q c). An origin-binding gap beta = c + 1 - q therefore requires sigma >= q (1 - 1/c):
1.074 at q = 12/5, 1.119 at q = 5/2, 1.164 at q = 13/5 (c = 1.8103192102). This agrees with the first theory agent's screen (origin binds
at sigma >= 1.2, far field at sigma <= 1.1, q = 5/2).

## 5. Revised necessary test (replaces v02 section 8(d) for this route)

UT-K at k = 0 (which lies in Kbar) gives N(h_0) <= A_F^K <= M. With c_W >= 1, the condition tau_bar < beta of the
sufficient criterion therefore requires
    N(h_0) R^((q-2)/2) < [beta/(q C*_sym)]^(q/2).
FLOAT values at R = 0.18814 (the AN-010 upper value for 007; scratch/wgk/sharp_sym.out). Bound on N(h_0):

| tuple | beta | v02 8(d) (q C_GN^U, c_1 = q HEURISTIC) | this note, C_ell | this note, C*_sym |
|---|---|---|---|---|
| q = 5/2 | 0.31 | 0.346 | 1.268 | 1.399 |
| P-Q1 = (13/5, 7/5, 1/4) | 0.2103 (origin value, an upper value) | 0.217 | 0.840 | 0.940 |
| P-Q2 = (12/5, 1, 1/4) | 0.2442 | 0.246 | 0.856 | 0.929 |
| P-BG1 = (13/5, 7/5, 1/4, 1/10) | 0.1 (certified, AN-022) | 0.083 | 0.320 | 0.358 |
| P-BG2 = (5/2, 7/5, 1/2, 1/4) | 0.25 | 0.264 | 0.969 | 1.069 |

By Proposition OBS, for small R/M no route that uses a k-uniform pointwise Garding inequality on K^S_{R,M} can relax this
absorption condition by more than the factor c_W^(1-theta). The FLOAT proxy N(F)/beta for N(h_0) at 007 (N(F) about 7375
at P-Q1 and 1735 at P-Q2, the coordinator 19:56Z item 3) exceeds these bounds by a factor of order 1e3 to 1e4. The gain of about
4 over v02 does not change that. A failed sufficient inequality refutes nothing (v02 section 8(d)).

## 6. The binding term is the tame term

In the closure condition A_F^K + eta^K M <= M, the tame coefficient eta^K requires, roughly,
c_4' [C_GN R^theta (c_W M)^(1-theta) + C_inf R^theta_0 (c_W M)^(1-theta_0)] < b: the unweighted Lipschitz size A(z) of the
ball elements must be below b/c_4'. This has the same order R^theta M^(1-theta) as the absorption, but with
C_GN = 0.573 against q C*_sym = 0.331 at q = 5/2, before the factor c_4'. In the closure function of section 7 with
c_4' = 1, C_eps_bar = 0 and c_W = 1 (HEURISTIC), the tame condition binds at every tuple in the table. So the sharp value
of c_4' is the explicit constant that matters most on the T2 side (section 8).

## 7. Closure function (the coordinator 20:10Z item 4(c)) [T2-CF, HEURISTIC]

Script: theory_agent_2/scratch/wgk/closure_fn.py (Python; copy it before running). Function
closure(G0, Nq, q, sigma, r0, beta, beta0, eps, Ceps, c4p, cW). It returns the interval of M that closes, or None.
- Inputs: G0 = ||F||_2; Nq = N(F) at (q, sigma, r0). From the coordinator's triple, Nq <= N_2^(3-q) N_3^(q-2) exactly
  (Hoelder in Fourier variables, same weight W); Nq_from(N2, N3, q) implements it. beta is the BG-q gap of rho_bar at the
  tuple, beta0 the L^2 gap; R = G0/beta0.
- Conditions, for some M > 0:
      (D2-K)  b(M) := beta - eps - tau_bar(R, M) > 0;
      (D1-K)  N(F)/b + (C_eps_bar/b)^(1/2) R + (c_4'/b) [ C_GN c_W^(1-theta) R^theta M^(2-theta) + C_inf c_W^(1-theta_0) R^theta_0 M^(2-theta_0) ] <= M.
  (The strict margins Rbar > R, Mbar > M of section 2 are ignored; they cost an arbitrarily small factor.)
- Unknown constants, named: C_eps_bar (Lemma WG-K, not explicit), c_4' (KP-W tame constant times (1 + C_chi), not
  explicit), c_W (not explicit, >= 1), eps (> 0 in the lemma; C_eps_bar may grow as eps -> 0). Any evaluation with
  chosen values is HEURISTIC. The constants C*_sym, C_GN, C_inf, C_GN^U, C_inf^U are explicit and computed in the script.

Largest N(F) that closes (FLOAT; scratch/wgk/closure_fn.out; beta0 = 2.00215, the 007 value):

C_eps_bar = 0, c_4' = 1, c_W = 1, eps = 0:

| tuple | G0 = 0.377 | 0.0521 | 0.0376 | 0.01 | 1e-3 | 1e-4 | 1e-6 |
|---|---|---|---|---|---|---|---|
| P-Q2 (12/5, 1, 1/4), beta 0.2442 | 0.0051 | 0.0113 | 0.0132 | 0.0225 | 0.0435 | 0.0735 | 0.190 |
| P-BG2 (5/2, 7/5, 1/2), beta 1/4 | 0.0049 | 0.0152 | 0.0179 | 0.0313 | 0.0660 | 0.124 | 0.401 |
| P-Q1 (13/5, 7/5, 1/4), beta 0.2103 | 0.0031 | 0.0085 | 0.0103 | 0.0222 | 0.0590 | 0.129 | 0.533 |
| P-BG1 (13/5, 7/5, 1/4), beta 1/10 | 0.0004 | 0.0014 | 0.0016 | 0.0034 | 0.0100 | 0.0229 | 0.0963 |

C_eps_bar = 1, c_4' = 10: no closure for G0 >= 0.01; at G0 = 1e-3 the largest N(F) is 0.004 to 0.005 (P-BG1 0.0006).

Reading.
- N(F) >= ||F||_2 = G0 always. So an entry below G0 means no F with that G0 closes. Without re-centering, nothing closes
  for G0 >= about 0.05, whatever N(F), even with the optimistic constants.
- Where it closes, the admissible ratio N(F)/G0 is at most of order 10 to 100. FLOAT ratios for 007-class candidates
  are of order 1e4 (7375/0.377 at P-Q1).
- The function applies unchanged to the re-centered problem of v02 section 9: replace (G0, N(F), beta, beta0) by
  (||F_*||_2, N(F_*), beta_*, beta0_*), where F_* = F + L h_* + U[h_*].grad h_* is the nonlinear residual at a smooth
  computed h_*, beta_* is the BG-q gap of rho_bar + h_* (AT-039 matrix), and beta0_* >= beta0 - ||grad h_*||_inf
  (T2-RC-L2). The KP-W and GN constants do not depend on the background (v02 section 1); C_eps_bar does. N(h_*) itself
  may be large. This is the one route on the T2 side in which the numerics can lower the required strong norm by
  orders of magnitude: it asks for N(F_*) of order 1e-2 or less with ||F_*||_2 <= 1e-3 (c_4' = 1).
- q decreasing to 2: C*_sym, C_GN and C_GN^U grow like (q - 2)^(-1/2) (the integral int_rho^infinity r^(3-2q) dr), and
  theta -> 0, so R^theta -> 1 and the condition loses all help from a small G0. It becomes an absolute smallness of the
  strong norm. So q close to 2 does not weaken the requirement. At larger q the G0 exponent grows but the origin cap
  c + 1 - q falls (q < c + 1 = 2.81). In the table P-BG2 (q = 5/2) is best for G0 between 0.01 and 1e-3, and P-Q1
  (q = 13/5) for G0 <= 1e-4; the two tuples also differ in r0.
- r0: no T2 constant restricts r0. The p-term (sigma/(2 r0)) and the KP-W quantities M_ell <= C sigma sum r0^(-r) and
  L = sigma/(2 r0) decrease as r0 grows, and N(F) decreases with r0 (near-field weight). Larger r0 helps everywhere
  except through beta (BG-q, the first theory agent's screen sets the window). Lemma E needs sigma < 1 + gamma_* (1.4476 for 007).
- A weaker strong norm, other than through re-centering: a two-tier ball (a small Lipschitz-level tier and a large
  qualitative N tier) would remove the GN conversion, because both the absorption and the tame term need only
  Lipschitz-level smallness of the ball elements. Its missing piece is the invariance of the Lipschitz tier, which needs a
  linear estimate for A_k with a gap in a Lipschitz-level space (for example weighted C^(1,alpha)) and an L^2 remainder.
  OPEN; not started. The source requirement would then be smallness of F in that space (1 + alpha derivatives in L^inf
  instead of q derivatives in L^2). A frequency split of F that keeps the high near-field modes in L^2 only does not work
  as stated: the transport A_k needs a Lipschitz velocity, so every part of h must have Lipschitz-level control.

## 8. Explicit constants: route and target times (the coordinator 20:10Z item 3(a))

- In the WG-K route, c_1, c_2, c_3 of KP-W enter only through the choice of Lambda in Step 6 (any explicit upper bound
  suffices), and then through C_eps_bar. c_4' and c_W enter the closure directly, and c_4' binds (section 6).
- c_4 and c_W: explicit, non-sharp values from the constants of PROOF.md (Peetre constant G, the Littlewood-Paley and
  paraproduct constants C_q and C_W, L = sigma/(2 r0), M_ell) and a Leibniz bound for multiplication by W^(-1). Target:
  2026-11-03T06:00Z.
- C_eps_bar: replace the finite net of Step 3 by explicit cuts: an input frequency cut, using the Fourier kernel bounds
  of Step 5, and a spatial cut, using the weight (N(k) <= M forces ||W k||_2 <= M, so the part of k far out is small
  in L^2 with an explicit factor; the far field of U[k] is controlled by the kernel tail). Input: the first theory agent's explicit C_eps
  for k = 0 (Lemma Q-WG). Target for the k-dependent part: 2026-11-03T12:00Z.
- Then a sharper tame constant (the leading paraproduct term of KP-W) as a second item.

## 9. Requests

- The theory auditor: audit Lemma WG-K (section 1; inputs AT-029 and AT-049 to AT-051), UT-K and (S-inv-K) (section 2), Lemma SYM
  and Proposition TAU (section 3), Proposition OBS and Proposition INF (section 4). Proposed IDs in the status table.
- The first theory agent: register the IDs; for theory_v01 (X1), the WG-K route is the absorption of FW-C2-Hq, with the explicit
  tau_bar; the KP-W constants c_1 to c_3 no longer appear in the absorption.
- The coordinator, for the numerics: closure_fn.py for (G0, N(F)) and for the re-centered pair (||F_*||_2, N(F_*)). When a
  correction h (h_N, h_0) is reported, give ||Sym DU[h]||_(inf,op) (not only ||DU[h]||_(inf,op)), the unweighted
  A(h) = ||grad h||_inf + ||h||_inf (the tame quantity), and for h_N also ||F_*||_2 and N(F_*).
