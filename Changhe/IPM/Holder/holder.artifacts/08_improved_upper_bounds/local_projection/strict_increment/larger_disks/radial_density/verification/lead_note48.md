## Note 48 (2026-10-28T12:43Z): cross-reads of V180, general radius, V183, V185, V186, V188, V191 (fourth moment), V184 and the near-zero separation note: all pass

To the verification work. Independent analytic cross-reads, with my own symbolic/numeric checks in scratch/crossread_v186_v188/
(check.py, check2.py, check_v184.py and their .out files). Hashes read: V183 23243e67..., V185 7dad779f...,
V186 aba25f01..., V188 afa7bbef..., fourth moment 3164de2a..., V184 39c0c377..., near-zero 5a3abb36....

1. V180 (larger disks, sha 872f552d...): CORRECT. I expanded p(s) = 1/2 - 3s + 4s^2 + 3s^3 - 4s^4 exactly (Fractions) and
   confirmed the minimum 11/1944 on [0, 1/sqrt 2] through t = s - 1/3; the containment of the radius-R/4 disks centred at
   3R/4 in the region where Q dominates the stated uniform density holds; the saving 7/18432 alpha(1-alpha)(5/4)^(alpha-2)
   follows from the reflection coupling verbatim (gain over V176 at least 1.4235).
2. General radius (sha 9199f443...): CORRECT. Scaling gives eta(s) = (7 s^2/4608) a, a = alpha(1-alpha)(1+s/2)^(alpha-2),
   for 0 < s < 2, and s_D <= 2^(alpha-1)(3 - alpha) < 2 from a_3 <= a_1 = 2^alpha A and b <= a_1.
3. V183 (radial density): CORRECT. The radial density (1 - 32t^2/9)/(2 pi R^2 (3/4+t)^2) is below Q on each disk; the
   saving is 2 s^2 a I with I = int_0^{1/4} t^3(1 - 32t^2/9)/(3/4+t)^2 dt; quadrature at 40 digits gives
   2I - J = 9e-41 with J = 653/288 - (63/8) log(4/3) = 0.00186479055..., and J/(7/4608) = 1.22756.
4. V185 (cutoff plan): CORRECT, including the retained-marginal step. The point to check is the sign structure: the
   Q-edge targets lie in the negative lobes, where the marginal is |m| = q, and the sources sit near the other pole,
   so the cross-kernel deficiency at either marginal is at most H = 1/(2 pi (1-rho)^2) and the retained translation
   density is at least q - H. Positivity: H / min w = H / (7/(18 pi rho^2)) = 9 rho^2/(7 (1-rho)^2) <= 9/28 at
   rho <= 1/3. The constant-density moment is 4 pi H int_0^{rho/4} r^3 dr = rho^4/(512 (1-rho)^2) (sympy). The
   reflection replacement acts on retained flows only, so the residual and every other edge are unchanged.
5. V186 (all radii): CORRECT. Multiplying w - H by 2 pi rho^2 (3/4+t)^2 gives exactly p(t) = 1 - (32/9)t^2 - q^2(3/4+t)^2,
   q = rho/(1-rho) (sympy identity). p = -[(32/9+q^2)t^2 + (3/2)q^2 t - (1 - 9q^2/16)], and
   (9/16)q^4 + (32/9+q^2)(1-9q^2/16) = 32/9 - q^2 identically, so the positive root is the stated t_* (checked also by
   substitution at q = 1/10, 1/2, 9/10). p(0) = 1 - 9q^2/16 > 0, p is decreasing on t >= 0, and p(1/4) = 7/9 - q^2, so
   tau = 1/4 for rho <= 1/3 and the formula reduces to V185 there. The subtracted term is
   4 pi H int_0^{tau rho} r^3 dr = rho^2 q^2 tau^4/2, as in E(alpha, rho). (w - H)_+ is radial and below the retained density.
6. V188 (symmetric concavity): CORRECT. Reflection in the line through c perpendicular to e preserves the radial
   submeasure; the displacement is (h - 2u.e)e with |2u.e/h| <= s/2 < 1. Averaging u and -u (same w) gives the even
   function q(v) = ((1-v)^alpha + (1+v)^alpha)/2, and q'' = -alpha(1-alpha)[(1-v)^(alpha-2)+(1+v)^(alpha-2)]/2 <= -alpha(1-alpha)
   by Jensen (mean of the arguments is 1). int (u.e)^2 w du = pi I_w (int cos^2 = pi); two disks save
   4 pi alpha(1-alpha) I_w/h^2 = J s^2 alpha(1-alpha). Sampled check: max over nine alphas and 399 v of
   q(v) - (1 - alpha(1-alpha)v^2/2) is -3e-15 (equality only at v = 0). The cutoff form (3) and the removal of
   (1+rho/2)^(alpha-2) from E in V186 follow.
7. V191 (fourth moment): CORRECT. The fourth derivative is -q[(1-v)^(alpha-4)+(1+v)^(alpha-4)]/2 with
   q = alpha(1-alpha)(2-alpha)(3-alpha) (checked at six points, residual 0), <= -q by Jensen; A(0) = 1, A'(0) = A'''(0) = 0,
   A''(0) = -alpha(1-alpha), so A <= 1 - p v^2/2 - q v^4/24 (sampled max residual -8e-21). int cos^4 = 3 pi/4; the
   coefficients 4 pi p and pi q; pi I_5 = K R^4; the B_n formula agrees with quadrature to 2e-41 for n = 3, 5, 7;
   K = 1.835705523698e-5; the quartic cutoff correction rho^6/(49152 (1-rho)^2) (sympy). Positivity of the corrected fifth
   moment follows from w - H > 0. Remark: at the cutoff radii selected for J_D (and at the local radii of Section 3)
   these savings are below 1e-6, so I will state them as a strictness remark after Theorem 5.7, not as new table values,
   unless you or the numerical team prefer otherwise.
8. V184 (direct periodic Hilbert): CORRECT. Checked: (1/2)[cot((a-y)/2) - cot((-a-y)/2)] = sin a/(cos y - cos a);
   F_a(u)du = 2 ds/(1-s^2) and F_a(rho(u)) rho'(u) = F_a(u) (numerically at nine (a, s) points, residual 4e-37 together
   with the next items); the arctangent subtraction branch (b^2 > -1, difference in (0, pi/2)); arctan b >= b/(1+b^2);
   Q_ch formula and the identity (s^2+b^2)(1+b^2s^2) - s^2(1+b^2)^2 = b^2(1-s^2)^2; Q_ang, Q_ch <= (1-s^2)/(2s) at all
   sample points; 2^(1-alpha) B((1-alpha)/2, alpha)/pi = Gamma(alpha/2)Gamma((1-alpha)/2)/pi^(3/2) (duplication). The
   principal-value cutoff adjustment is O(eps) since rho(a - eps) = a + eps + O(eps^2) and F_a ~ -1/(y - a); the paired
   integrand is O((a-u)^(alpha-1)). In the rescaling, the d <= sqrt(eps) / d > sqrt(eps) split and the bound
   (delta/(2 sin(delta/2)))^alpha -> 1 for the chordal metric are right, and eps cot(eps t/2)/(2 pi) = 1/(pi t) + O(eps^2 t)
   gives the local limit. The pairing integral at fixed a stays below N_alpha (e.g. 2.2573 < 2.8443 at alpha = 0.3,
   a = pi/2), consistent with the supremum being approached as a -> 0. Dependency: the real-line theorem
   (hilbert_exact, V014).
9. strict_separation_near_zero (sha 5a3abb36...): CORRECT (a direct corollary of Theorems 5.4 and 5.6 / 5.7(iv),(v)).
   I will adopt your replacement sentence for Section 8(4) in v30.

Nothing here changes a number in the report. Plan for v30: the Section 8(4) sentence; a short remark after Theorem 5.7
on the strict savings (V188 and V191 with V185/V186) once you mark them CONFIRMED; the cross4096 recombination of
Theorem 3.6 if it improves D (my run finishes about 13:41Z; I will post hashes and the recombination as Note 49).

