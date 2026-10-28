# Independent audit: far-field obstruction on the common Hoelder target Y

Audited file: theory-working-files/Far_Y_obstruction.md
sha256: 70d799f122d16ebdba43565fae886f844a7055bb866c5b0a77fe40e7813355de
Inputs consulted (read only): verifier/proofs/117, 213 (V222), 214 (V224), 216 (V227), 217 (V228).
Checks: every step re-derived by hand. Exponent algebra of Steps 5 and 6 and the delta_1 constant were
checked numerically with a small python script.

VERDICT: PASS WITH REMARKS

The core argument is correct. No gap affects the proposition or its application to L_ren and A_0. One
constant is wrong as written (finding 1). The prose around the proof (Mechanism paragraph, Remarks 1 and 3)
claims more than is proved.

## Findings

1. (typo) Step 1, delta_1. From x_tau >= R_1 e^(ell0 tau/2) we get
   int_0^inf C x_tau^(k-1) dtau <= 2 C R_1^(k-1)/((1-k) ell0) = 2 C R_1^(k-1)/(ell0 - 1).
   So int (|a|+|b|) <= 4 C R_1^(k-1)/(ell0 - 1), which is larger than the stated delta_1 = 4 C R_1^(k-1)/ell0
   by the factor 1/(1-k) = 1.2186. Repair: define delta_1 := 4 C R_1^(k-1)/(ell0 - 1) and keep the condition
   delta_1 <= log(3/2)/8 by taking R_1 larger. Nothing downstream changes. Minor points: d/dtau log(y/x) = b - a,
   so y/x changes by at most the factor e^(delta_1); e^(2 delta_1) is a safe overestimate. The C in
   |a| <= C x^(k-1) absorbs the factor 2^(k/2) from r <= sqrt(2) x on S.

2. (remark) Step 1, far velocity input. These bounds are available. Proof 117 gives the velocity as a finite
   angular sum, U_r/r = -sum P_n cos(2n theta) and U_theta/r = sum Q_n sin(2n theta), with
   P_n, Q_n = (p_n, q_n) e^((k-1) tau) + O(e^((2k-2) tau)), termwise differentiable. So the bounds are uniform in
   theta, including near theta = 0. Proof 217 (V228) records U[rho0] = O(r^k) with fixed cylinder derivatives.
   Converting to Cartesian derivatives gives |DU| <= C r^(k-1). U_2 is odd in y: by kernel parity (K2 even,
   rho0 odd in y), and U_2 = U_r sin(theta) + U_theta cos(theta) vanishes at theta = 0. The formula for b is
   correct, and every point (x, t y) has r >= x >= R_1. Caveat: proof 117 is stated for t >= t_+, that is
   r >= R_+ = e^(t_+) = 3413, not for "r >= 1". On 1 <= r <= R_+ the bounds follow from C^1 regularity on
   compact annuli (C^5 joins, proof 217), but this is never needed. Write "r >= R_+" and take R_1 >= R_+.
   The bootstrap is fine: y = 0 is invariant, so y_tau > 0; x_tau increases; |V| <= C r, so the orbit
   exists for all tau >= 0.

3. (remark) Step 2 is correct, uniformly in X0, for all four parts.
   - f is smooth on R^2 and vanishes for |x| < X0. It is even in x, odd in y, has f(0, y) = 0, and |f| <= 1.
   - |d_x f| <= C/X0 holds globally. The sigma' term is bounded by (2/alpha)||sigma'|| |x|^(2/alpha) |y|/|x|
     <= C/X0 on supp sigma'. This covers pairs with one point outside the support and pairs that cross x = 0,
     giving [f]_x <= C.
   - [f]_(y,2): the product rule with min(1, C X0 d) <= C X0^alpha d^alpha <= C x^2 d^alpha (since x >= X0 >= 1)
     and min(2, C |x|^(2/alpha) d) <= C x^2 d^alpha.
   - L^2: ||f||^2 <= C X0^(-gamma). This needs only gamma >= 0.
   Typo: the theta difference is at most min(1, .), not min(2, .). Harmless.

4. (remark) Step 3 is correct. Entry time: e^(-tau_0) >= (2 e^(delta_1))^(-k) (R_1/X0)^k, with exponent
   k = 1/ell0. The length of I is >= (log(3/2) - 2 delta_1)/ell0. On I: x^(2/alpha) y >= 1 by the choice of y*,
   so sigma = 1; phi = 1; and X0 y_tau <= (3/2) e^(4 delta_1) 2^(-2/alpha) X0^(1 - 2/alpha) < 1, so theta = 1.
   Also y* <= R_1/4. Since y_tau > 0, f(Phi_tau X*) >= 0 for all tau. Then (2) holds with
   c_1 = (2 e^(delta_1))^(-k) (1 - e^(-log(3/2)/(2 ell0))). Only alpha < 2 is used here.

5. (remark) Step 4: closedness is automatic. V224 proves that the maximal transport T on D_Y is closed, and
   adding any bounded B keeps it closed on the same domain. So "or by assumption" in Step 4 and
   "(when A is closed on D_Y)" in the Statement can be dropped. A closed bijection has a bounded inverse by
   the closed graph theorem, as used.
   Representation (3) is correct: V is C^1 (V224), |V| >= ell0 x/2 > 0 on S, the forward orbit is global
   (Step 1), and e^(-tau) u(Phi_tau X*) -> 0 because u is bounded. Suggest adding one line on the flow box.
   In coordinates Psi(s, z) = Phi_s(z), the Jacobian J satisfies d_s J = (div V o Psi) J. So
   <V.grad u, phi> = -int u div(V phi) becomes d_s(u o Psi) = (V.grad u) o Psi in distributions, and u o Psi
   is C^1 in s. This is where V in C^1 and the distributional definition of D_Y enter.

6. (remark) Stronger conclusion available. The argument never uses injectivity. If A is only surjective,
   the open mapping theorem on (D_Y, graph norm) gives K such that every f has a preimage with
   ||u||_Y <= K ||f||_Y. Steps 4 to 6 then run unchanged. So the proof shows T + B is not surjective onto Y.
   This also holds on any smaller domain D contained in D_Y. Suggest stating "not surjective" as the result.

7. (remark) Step 5 is correct, with one line missing.
   - The bound |h(Z)| <= [h]_(y,2) z_1^2 |z_2|^alpha (constant 1, from h(z_1, 0) = 0) is correct.
   - For tau >= tau_2R, beta_R = 1 at Phi_tau X*, because r_tau increases.
   - The first integral is correct, using e^(ell0 tau_2R) <= 2 R e^(delta_1)/R_1. The exponents
     (R_1/X0)^k (R/X0)^(2+alpha-k) are confirmed: the ratio to the hand bound depends only on alpha.
   - Missing line, second integral: the text bounds only tau >= tau_1. Let F be the upper envelope
     e^(3 delta_1) R_1^2 y*^alpha e^((2+alpha) ell0 tau) and tau_1' the time where F = 1. Then the part before
     tau_1 is at most int_0^(tau_1') e^(-tau) F = e^(-tau_1')/((2+alpha) ell0 - 1), and
     e^(-tau_1) <= e^(-tau_1') = c (R_1/X0)^k.
   - tau_2R needs 2R > |X*|, i.e. X0 larger than about R_1^2/4. State "X0 large" here.
   - The second term is of the same order as (2). Its smallness comes only from eps(X0^(1/2)) -> 0, as the
     bracket correctly shows.

8. (remark) Step 6 is correct. Using |u(X*)| >= (c_1/2)(R_1/X0)^k and
   y*^alpha = e^(2 alpha delta_1) R_1^alpha (2 X0)^(-(2+alpha)), one gets
   [u]_(y,2) >= c (X0/R_1)^(2+alpha-k) -> infinity, since 2 + alpha - k > 0. Oddness is not even needed:
   |u(X*)| <= [u]_(y,2) R_1^2 y*^alpha gives the same bound.

9. (remark) Scope "every 0 < alpha < 1 and 4k < gamma < 2" is justified. The proposition needs
   (2+alpha) ell0 > 1 (always true), alpha < 2 and gamma >= 0. The range 4k < gamma < 2 is where V224/V228 give
   boundedness of C_ren and C_0 = C_ren + c[.] m_0 and the tail rates. Those rates are R^(k-1)(1 + log R),
   with beta_R H0 = 0 for large R, and R^(2k - gamma/2)(1 + log R). Both tend to 0. Labels V222/V224/V227/V228
   match the verifier folders 213/214/216/217.

10. (remark) The Mechanism paragraph is heuristic and should say so. The necessity "compatible only if
    beta < k" and the window 2k - 1 <= beta < k are cited to "3.2 of the report" and not proved here. The
    proof covers only the x^2-weighted vertical seminorm. At beta = k the same computation gives
    amplification X0^0, so this construction does not exclude beta = k.

11. (remark) Remark 1 is a sketch but says "shows". The two-orbit version (orbits from (R_1, y*) and
    (R_1 + d, y*), forcing of amplitude L^alpha at wavelength L ~ d X0/R_1) gives a quotient of order
    (X0/R_1)^(alpha - k). It also needs control of the vertical drift between the orbits and of the coupling
    differences. I see no obstruction, but it is not proved. Relabel it as a sketch or expectation.

12. (remark) Remark 2: "properties of the target Y, not of the operator" is imprecise. The far obstruction
    uses the far dilation rate ell0 (through (2+alpha) ell0 > 1 and the exponent k), and V227 uses
    V.grad chi != 0. Suggest "properties of the transport V.grad - 1 on Y, independent of the coupling B".
    "Realization theorems unaffected" is correct. V227 itself says that neither invertibility nor its failure
    follows from it.

13. (remark) Remark 3 overstates. "A global Hoelder inverse needs a target ... with beta < k" is not
    established. Only the failure of this Y is proved, plus finding 11 heuristically. Targets with anisotropic
    or different weights for x and y differences, or non-Hoelder targets, are not excluded. Suggest
    "suggests" or "within isotropically scaled Hoelder seminorms, heuristically".

No gaps found. Suggested edits, in priority order: fix delta_1 (1); add the missing line in Step 5 (7);
replace "r >= 1" by "r >= R_+" (2); drop "by assumption" and state non-surjectivity (5, 6); relabel the
Mechanism paragraph and Remarks 1 and 3 (10, 11, 13).
