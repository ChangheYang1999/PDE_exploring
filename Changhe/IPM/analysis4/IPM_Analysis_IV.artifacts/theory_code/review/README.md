# Review checks (independent reproductions of results reviewed in the theory)

- edge_top_check.py N: direct exact polynomial-log 1-edge recurrence at delta = 2/3, f_1 = sin(theta), canonical
  constants, through order N (run with N = 24, a few seconds). Checks the degree bounds, that the top stream column at
  order 3k is a single mode sin((2k-2) theta), the values b_2 and b_3, b_(k+1)/b_k = R(k) for k = 3..7, the profile a_1,
  the positivity of P(x+3), lim k R(k) = 1/3240, and |[t^82 sin 165 theta] F_250| < 2^-1075 from the product formula
  (Proposition 14.21c).
- edge_top_symbolic.py: the same top-degree cycle carried symbolically in k with signed frequencies; checks
  [sin((2k-1) theta)] a_3 = -2k R(k) identically and the nonzero limits of the offset coefficients.
- zero_delta_check.py: pure recursion for f_1 = sin(3 theta) at delta = 1e-10 and 1e-12 (mpmath, 80 digits); compares
  delta^(2n-2) [sin theta] f_n and delta^(2n-2) [sin 3 theta] f_n with the Taylor coefficients of the explicit generating
  functions for n <= 9 (Section 10.5, Remark on the endpoint).
- top_mode_bracket.py: the top-mode radius R_H (Proposition 8.2) at delta = 2/3, 2/5, 1/2, 1/3, 4/9 with B = 4, by the
  beta-integral formula and by the scalar top recursion (to order 1500, corrected by the n^(-1-nu) law); the necessary
  radii (|b_i|/R_H)^(1/delta) at the explicit roots; h_2..h_5 against the direct Fourier recurrence at delta = 4/9 (theory
  Section 12.6, Remark 3). About 2 minutes.
