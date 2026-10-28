## 2026-10-28T14:12:16Z  Note 60: V228 (phase_uniform_density) cross-read: CORRECT

I re-derived every step of 08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/PROOF.md:
- q_r(v) = cos(2d)/|P|^2 times 2pi at P = c e + u (N = D + 2r^2 v^2 - 2r^2, D = c^2 + 2crv + r^2);
- q_r' = (N'D - 2ND')/D^3 = 2r(-c^3 + 3cr^2 + 2r^3 v)/D^3, bracket <= c^3(-1 + 3/4 + 1/4) = 0 for r <= c/2 (strict for r < c/2,
  and here a < c/2 since c > 2/3, so q_r is strictly decreasing);
- q_r'' = 4r^2(r^2 D - 3cM)/D^4 = 4r^2(3c^4 - 8c^2r^2 - 4cr^3 v + r^4)/D^4; with t = r/c <= 1/2 the bracket/c^4 is at least
  3 - 8t^2 - 4t^3 + t^4, decreasing in t, so >= 9/16 > 1/2;
- the F-invariant minorant min(q(u), q(Fu)) = q(|cos g cos th| + sin g sin th) (q decreasing); the disk is F-invariant (F reflects in
  the line through the disk centre perpendicular to the increment), so the reflection plus translation of the rest keeps both
  marginals; the pair th, -th and midpoint convexity give the gamma = 0 bound, then A <= |cos th| and monotonicity;
- d/dy [y/((c+x)^2 + y^2)] = ((c+x)^2 - y^2)/((c+x)^2 + y^2)^2, so the y-integral is sqrt(a^2-x^2)/(c^2 + 2cx + a^2); the factor
  4 quadrants x 2 disks / (2pi) times 2^(2n) gives H_n = 2^(2n+2)/pi (-binom(alpha,2n)) s^(2n) I_n;
- cutoff: the retained density is pointwise >= q - kappa, so min(q(u), q(Fu)) - kappa is an F-invariant minorant of the retained
  measure, positive since q >= 1/(c+r)^2 >= 1 > kappa; the constant gives exactly (2);
- Jensen (4): total weight pi a^4/16, first moment 2a^5/15, mean 32a/(15pi); (5) = 8 alpha(1-alpha) s^2 I_1/pi bound; cutoff term
  alpha(1-alpha) s^2 kappa a^4/2. All correct.
Float diagnostic (scratch/crossread_v228/check.py, .out; scipy quadrature, not a certificate), alpha = 1/2, s = 1/2, c = V226 centre:
the density formula and the y-integral agree to 1e-12; the 2D-quadrature saving at gamma = 0, pi/8, pi/4, 3pi/8, pi/2 is
1.5651e-4, 1.5903e-4, 1.6758e-4, 1.8530e-4, 2.1728e-4 for n = 1 (minimum at gamma = 0, equal to H_1 to 1e-12), likewise for n = 2, 3.
H_1 = 1.56514e-4 against the radial-minimum term A_1 B_3 s^2 = 1.52379e-4 (gain 4.1e-6); Jensen (5) gains 2.91e-6 (your 2.9e-6).
Eight terms: 1.58092e-4 against 1.53932e-4, gain 4.16e-6 at alpha = 1/2. So a certified eight-term I_n evaluation would lower D_{1/2}
to about 2.645084 (Table 1 now 2.645088). Suggestion: the substitution x = a sin(phi) gives
I_n = a^(2n+2) int_0^(pi/2) sin^(2n) phi cos^2 phi /(c^2 + a^2 + 2ca sin phi) dphi, analytic on the closed interval, convenient for
rigorous quadrature. If you certify the eight-term values for the table rows (and the cutoff rows and the uniform K_D), I will put
them into the report as part (c) of Theorem 3.10, replacing the radial minimum; the savings are again never added.

## 2026-10-28T14:13:28Z  Note 61: lead evaluation of V228 (eight phase-uniform terms on the V226 disks), for comparison with your certification

scratch/v228_eval/eval_v228.py, .json (384 and 768 bits, identical ten-place results). I_n by two methods with overlapping balls:
the exact expansion in the moments M_m = a^(m+2) W_m/(m+2) (Wallis W_m) with remainder M_(2n) r^K/(A(1-r)), r = 2ca/(c^2+a^2), K = 400,
and acb quadrature after x = a sin p. Bases: the V226 base_upper rationals; same rows and radii as V226; eight terms subtracted once.
   alpha (rho)              V226            with V228       improvement
   1/20  (1/2)              13.6146578709   13.6146570782   7.93e-7
   1/10  (1/2)               7.2859044187    7.2859029173   1.50e-6
   1/5   (1/2)               4.1825632814    4.1825606142   2.67e-6
   3/10  (1/2)               3.2166553546    3.2166518563   3.50e-6
   1/2   (1/2)               2.6450878204    2.6450836612   4.16e-6
   3/4   (1/2)               3.0973767898    3.0973736749   3.11e-6
   9/10  (1/2)               5.4688740775    5.4688725835   1.49e-6
   99/100 (1/2)             42.6816713682   42.6816712039   1.64e-7
   1/1000 (31977/100000)   637.4271353454  637.4271353386   6.8e-9
   1/200  (31963/100000)   128.1421838895  128.1421838557   3.4e-8
   1/100  (15973/50000)     64.4938359260   64.4938358589   6.7e-8
   uniform K_D (31987/100000) 2.7249482772   2.7249415501   6.7e-6
Table 1 would change at 0.1, 0.2, 0.3, 0.5, 0.75, 0.9 (7.285903, 4.182561, 3.216652, 2.645084, 3.097374, 5.468873); the boxed
coefficient 2.7250 is unchanged. If you certify these (or your own radii), I will add Theorem 3.10(c) and update Table 1 in v35.
