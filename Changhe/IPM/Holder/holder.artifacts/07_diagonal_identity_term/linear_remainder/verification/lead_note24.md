## Note 24 (2026-10-28T08:47Z): cross-read of the D linear remainder: ACCEPTED; closed_form37 D remark corrected

(a) Independent cross-read of 07_diagonal_identity_term/linear_remainder/PROOF.md (11503 bytes, 08:28Z). I accept
 the proof of D_a = 2/(pi a) + 2C0 + O(a). What I re-derived, step by step:
 - (3): F(x) = -1/2 since b(0) = 1/2, V(x) = 0; F <= c needs -h <= c, true since [h]_a <= 2^(a-1) and h(x) = 1/2;
   F in [-1/2, 1/2] because the inner min(h, c, max(-1/2, .)) is >= -1/2 and -h <= 0.
 - (4): rows of DV are the unit normal (n1, n2) and (0, 1) with n2 = O(R^3); |DV w|^2 <= 1 + n2^2 + 2|n2| gives
   Lip V <= 1 + |n2|. [G]_a <= L_a as min of g (Theorem 5.6 Step 1) and the frozen profile (seminorm 1: same signs by
   Lip S = 2, opposite signs via a zero of S on the segment and concavity).
 - (5): both frozen: opposite signs cross Gamma u {Y=0} (Pi <= 2 dist), equal signs Lip(S o V) <= 2 sqrt2 and
   (2 sqrt2)^a/2 <= 1. Mixed: for p unfrozen (|p-x| < 2 rho), q with R = |q-x| >= 20 rho, BOTH orderings are bounded by
   (rho^a + Pi_q^a)/2 (G(p) in [0, rho^a), G(q) in [(rho^a - Pi^a)/2, (rho^a + Pi^a)/2]), and Pi_q <= 2R <= (20/9)|p-q|,
   rho <= |p-q|/18; [18^-a + (20/9)^a]/2 <= 1 on [0, 1/2] by convexity. The case split (outside/outside, outside/frozen
   inside, outside/unfrozen) is complete. Remark only: "the one remaining direction" could say that both directions
   satisfy the same bound.
 - (6)-(9): E(x) = -1/2; q with |p-q| >= r cannot lower E by (3) and L_a >= 1; q with |p-q| < r lies in B(x, 2r), so
   (4) with R = 2r gives (7); outside B(x, 20 rho), (5) gives E = F. f = max(E, -h): f >= E, f <= F, |f| <= h, cross
   half-plane bound by concavity. Repair integral O(a) since |nu| <= C(r^-2 + 1).
 - (10)-(13): A(a) = (1/4pi) int |sin 2t|^(1+a) = Gamma(1+a/2)/(2 sqrt(pi) Gamma(3/2+a/2)), A(0) = 1/pi,
   A'(0)/A(0) = (psi(1) - psi(3/2))/2 = log2 - 1, so 2A d^a/a = 2/(pi a) + (2/pi)(log d + log2 - 1) + O(a). On B(x, d) the
   limit W_0 = sign(S(V))/2 = sign(nu)/2 = F_0, so the clamp part is compared with 0 and (11) suffices (range clamps
   inactive as g(V) in [0, |V|^a]; upper h clamp inactive for 2d < 1 - 2d; lower h clamp <= (1 - (2X)^a)/2 <= C a r;
   cone <= C a r^(a+3)). Same-sign set: |(v^a - w^a)/a| <= |log(v/w)| with v = r|t_r|, w = r|q| < 1, and (13) by the
   u = cos(theta) rescaling (I checked the |u| >= C1 r^3 and |u| < C1 r^3 pieces). Opposite-sign set: measure O(r^3),
   |q| <= C r^3, weight a[2|log r| + |log|t|| + |log|q||] gives C a r^6 (1 + |log r|). Against |K| = |q|/(2 pi r^2) all
   integrable with an O(a) total.
 - (14): |(v^a - 1)/a| <= (1 + v^(1/4))|log v| for 0 < a <= 1/4; min/max are 1-Lipschitz in sup norm, so |F_a - F_0| is
   bounded by the largest entry change; log|V| is singular only at the poles (Gamma n {Y=0} n H = {x}); at infinity
   (1 + v^(1/4)) <= C r^(1/4), |nu| = O(r^-3), Pi in [sqrt2, 2] x min(|s|, |Y|), and the scaled graph tends to the cone
   X = |Y|/sqrt3 (simple crossings at theta = +-pi/3), giving the r^(-7/4)(1 + log r) majorant.
 - (15)-(16): the constant corrections plus int mu_d F_0 recombine to V(d) + Delta(d) exactly (disk part int(|nu| - |K|)
   absolutely convergent). Independent consistency check of (16): d/dd [V + Delta] = -(1/2) x 2 x oint_{|u|=d} |K| =
   -2/(pi d), the derivative of -(2/pi) log d; the constant 1/2 is the finite part of Theorem 5.2 of the report.
 - (17): identity term -(1/2)(f(x) - f(y)) = +1/2; total 2/(pi a) + 1 + 2(log2 - 1)/pi = 2/(pi a) + 2C0; dividing by
   L_a = 1 + 2a^2 costs O(a). With V118's J_D bound this gives D_a = 2/(pi a) + 2C0 + O(a).
 No defect found. Once you record it as CONFIRMED (V-number), the report states it as part of Theorem 5.7 (C and D both
 with O(a) remainders; the lower O(a) constant for D is not explicit, as your scope section says).
(b) closed_form37 audit points (your 08:39Z note): (i) agreed, g is increasing for all a >= 0 (minus a positive distance
 moment plus an increasing term); the 7/8 split in the check is redundant but valid. (ii) Agreed and fixed: PROOF.md line
 16 now proves F** + 1/2 > G* through Q(a) = 2^(1-a)(a2 - A)/a = (4/pi) int_0^(pi/4) sin2t sin^a t (1 - cos^a t)/a dt,
 decreasing, Q(1) = 4/(3 sqrt2 pi) - 1/4 = 0.050105 > 0.0348 (mpmath check: Q(.001) 0.09761, Q(.5) 0.06964,
 Q(.999) 0.05014). Only PROOF.md changed (new sha256 24d545de...b962, SHA256SUMS.txt updated); code and data unchanged.
(c) table37 (single-exponent Theorem 3.7 certificates at 1/1000, 1/100, 1/20, 1/10, 1/5, 99/100, plans at the exponent
 itself, pass-3 grids) is running on core 62: exterior and local done, middle chunks next. Audit request follows when done.

