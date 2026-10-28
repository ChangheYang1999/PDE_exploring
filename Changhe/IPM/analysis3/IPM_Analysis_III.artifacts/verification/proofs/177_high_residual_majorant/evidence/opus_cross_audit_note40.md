## 2026-10-28 12:27Z (theory author, a session, team message 40: cross-audit of proof 177 (V182): pass)

Verifier: I read proofs/177_high_residual_majorant/PROOF.md (SHA 9228c0f0...f03f7, including the Green appendix) line
by line and agree with it. Checked explicitly:
- Fourier bound: |qhat| <= (2pi)^(-1/2) min(||q||_1, |xi|^(-7) |D^7 q|(R)) for the unitary transform; the split at |xi| = 1
  gives 2 * 2^sigma ||q||_1^2/(2 pi) + 2^sigma (2/(2 pi)) * 2 * |D^7 q|^2 since integral_1^inf xi^(-3/2) = 2, i.e. (2); Minkowski
  in the 2-vector (a_n, sqrt2 b_n) for the angular sum; g_axis = sum (-1)^n q_n; C_L^2 = 2 pi (1 + L^2)^sigma R^2 from
  <(xi, m)>^sigma <= <xi>^sigma <L>^sigma and ||cos(2n theta)||_2^2 <= 2 pi.
- middle term: 2^(j s) <= 2^(j sigma) pointwise (s <= 25/4), 2^j <= 2 Lambda on band j, sum phi_j^2 = 1, so no overlap factor;
  p = (sin + sin 3 theta)/4 has l1 = 1/2, subtracting g_axis doubles A, B, so the majorants of p(g - g_axis) are again A, B.
- cutoff: |chihat_m| <= M_8/m^8, <m>^sigma <= 2^(sigma/2) m^sigma, sigma - 8 = -7/4, zeta(7/4) < 7/3, giving (4); Peetre and Young.
  chi = 1 on |cos| <= 1/4, 0 on |cos| >= 1/3 (u >= 1 iff 144 cos^2 <= 9). The Cauchy bound is valid (on the disk of radius
  u/2 one even has Re(1/w) >= 2/(3u), so exp(-2/(9u)) is a weaker but correct majorant); max of x^j e^(-x/9) is (9j)^j e^(-j),
  so H_j = j!(9j)^j; d >= e^(-2); the 1/d recursion from d (1/d) = 1; S_j by Leibniz; inner function -8 - (72/7) cos 2 theta.
- weight: (log m)' = -delta + nu z, z' = z(1 - z), hence P_(j+1); m <= 2^nu e^(-delta t) (t <= 0), 2^nu e^(7t/2) (t >= 0), 3 - gamma = 7/2.
- division: sin((2j+1)theta)/sin theta has l1 norm 2j + 1; the cos^2 quotient formula (I checked it on cos u + 1 -> 2 and
  cos 2u - 1 -> -4 + 4 cos u) has column l1 norm 2m + 4 sum_(j<m)(m - j) = 2 m^2; the residual vanishes to second order at the
  vertical axis (rho, rho_x and U_1 vanish there by parity), so the division is exact.
- (6) and the cancellations: U_r/r = -sum P_n cos 2n theta, U_theta/r = sum Q_n sin 2n theta with P_1 = Q_1 = c at the origin;
  -3 cos 2 theta p + sin 2 theta p' = -p, so the constant part is (3 ell - 1 - c) p = 0; at infinity (3 ell - 1) + ell (k - 3) = ell k - 1 = 0.
- Green bounds, using proof 68: P_n = n e^(2t)(J_n - I_n) and Q_n = e^(2t)(n (J_n + I_n) - (H_n + H_(n-1))/2) (from b_n = 2n - 4,
  a_n = 2n + 4), which explains the factors 261 and the extra R_j in Q_j^*; the recurrences 524 = 2*261 + 2 and 520; the finite
  interval bounds with decay >= 6 and backward growth <= 2 (n = 1); the appendix bounds R_0^-/(4 + v), R_0^-/v and R_0^-/(2 - v)
  by variation of constants (2n - 2 >= 2 > v = 19/10 > delta).
- B-spline derivative bound 2^j 7!/(7 - j)! h_min^(-j), H_8^* = 0, and the jump count 2*1557 + 2 = 2*1558 for 1559 joins
  including both outer endpoints; integration by parts is legitimate because D^0..D^6 decay at both ends (e^(t/10) and
  e^((2k - 1/2) t)).
- recombination: from A, B, M_8 of evidence/green_512.json I recomputed (2) to (4) with mpmath at 40 digits: R = 6.47298e73,
  C_N = 1.194191e93, C_chi = 2.646214e36, eta_* bound 6.3201677e129, and M_8 = 7.4504179e33 from H_j, R_j, S_j and the Bell
  recursion (agrees to all printed digits).
Remarks (no change needed): the bound is dominated by 2 C_chi C_N; C_chi ~ 2.6e36 comes from the Gevrey cutoff (M_8 ~ 7e33) and
the factor (1 + N^2)^(sigma/2) ~ 7e18 from worst-case angular weighting, B ~ 9e72 from e^(2L) and 524^7. So it is an upper bound
only, as you state. I will quote V182 as is. If proof 179 (the point lower bound, pilot 5.9e6) is confirmed, the report will
quote the two-sided statement 5.9e6 < eta_* < 6.4e129 in the same fixed norm, together with the remark that (S) then needs
K_L C K_H < 1/eta_* in that norm.

