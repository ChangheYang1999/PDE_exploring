# Captured numerical report section7.11

7.11 X norms of the scaling tangent K, of the residual and of eps~ - X.grad eps~ (lead 13:54Z, after ver topic 138; FLOATING; shift 5, 16:57Z)
Weight w = m^-2 (1+u^2)^-3/2 (the H1m weight of the C2 Gram, section 7.4b), ||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX = pi int e^{2t} w(t) sum_N
[f_N^2 + (d_t f_N)^2 + (2N+1)^2 f_N^2] dt for f = sum_N f_N(t) sin((2N+1) theta); modes of the trial from the closed-form inverse (src/trial_green.py:
rho_modes, residual_modes), d_t of the residual modes by central differences; src/xnorm_K.py, runs/xnorm/. The integral is taken over 1e-4 <= r <= 1e7
in five pieces of spacing dt = 0.002 in t = log r (the residual's derivative has knot-scale structure, knot spacing 0.008: at dt = 0.0169 and 0.0101
the derivative term is not resolved, see the last two columns), merged in runs/xnorm/xnorm_K_merged.json; the omitted tails are below 2e-2 (inner)
and 13 (outer) in norm^2 for K and rho~ (against 5.9e7), and negligible for the residual quantities. K = rho~ - X.grad rho~ is the scaling tangent
(J(K) = -2, c[K] = 0; L K = eps~ - X.grad eps~ for the exactly normalized trial, ver topic 138).
| quantity | r < 2 | 4 <= r <= 16 | rest (2 <= r < 4 or r > 16) | all (fine, dt = 0.002) | all at dt = 0.0101 | all at dt = 0.0169 |
|---|---:|---:|---:|---:|---:|---:|
| K = rho~ - X.grad rho~ | 2.9419e+03 | 5.1576e+03 | 4.8380e+03 | 7.6591e+03 | 7.6582e+03 | 7.6567e+03 |
| eps~ | 2.7172e-04 | 1.5093e-02 | 3.0948e-03 | 1.5409e-02 | 1.4436e-02 | 1.4199e-02 |
| eps~ - X.grad eps~ | 3.2184e-03 | 2.5790e+00 | 3.0018e-01 | 2.5964e+00 | 5.1542e-01 | 3.6694e-01 |
| rho~ | 1.5209e+03 | 5.0252e+03 | 4.0099e+03 | 6.6064e+03 | 6.6064e+03 | 6.6064e+03 |
CORRECTION (17:04Z): the two derivative-containing rows above (eps~, eps~ - X.grad eps~) are NOT converged and not reliable: their t-derivatives were
taken by finite differences of the residual modes, and the modes carry small-scale evaluation noise that the first and second differences amplify
as the spacing shrinks (on the lobe 2 <= r <= 20: ||eps~ - X.grad eps~||_X = 2.72 at dt = 0.002 and 18.7 at dt = 0.001, while the residual modes
themselves are clean: their Wiener sums stay within the certified per-cell bound W <= 1.2e-4 at every spacing). The K and rho~ rows are fine (smooth,
large; stable to 4 digits across the spacings). RIGOROUS replacement (src/xnorm_cert.py, runs/xnorm/xnorm_cert.json; this lane's certificate data,
audit pending): from the per-cell Wiener sums W_i_j of the derivative certificate (7.3b), with sum_N a_N^2 <= (sum_N |a_N|)^2 and the cell maximum
of e^{2t} w at the left cell end (e^{2t} w = L^2 u^-4 (1+u^2)^{3/2-k} is decreasing),
  ||eps~||_X^2 <= pi sum_cells h max(e^{2t} w) [W_0_0^2 + W_1_0^2 + W_0_1^2],   ||eps~ - d_t eps~||_X^2 <= pi sum_cells h max(e^{2t} w) [(W_0_0 + W_1_0)^2 + (W_1_0 + W_2_0)^2 + (W_0_1 + W_1_1)^2]:
  middle region 0.00765 <= r <= 3413 (7809 cells): ||eps~||_X <= 3.8565e-01, ||eps~ - X.grad eps~||_X <= 5.8587e+02; of which r < 2: 1.425e-03 / 3.392e-02 and the lobe
  annulus 4 <= r <= 16: 3.8519e-01 / 5.8586e+02; with the outer (r > 3413) and inner (r < 0.00765) region certificates added: totals 3.8565e-01 / 5.8587e+02 over 5.2e-5 <= r <= 8.2e10.
Reading: ||K||_X = 7.6591e+03 (floating, converged) and the rigorous upper bound ||L K||_X = ||eps~ - X.grad eps~||_X <= 5.8587e+02 give, for any estimate
||h||_X <= C ||L h||_X on the graph domain of topic 138 (which contains K and, by the zero-strain bumps of topic 137, elements with J = c = 0
arbitrarily close to K), the LOWER bound C >= ||K||_X / ||L K||_X >= 1.3073e+01 (floating numerator over a rigorous upper bound of the denominator; a
rigorous lower bound of ||K||_X would need the certified rho~ data and is not done). The lobe annulus carries 100 percent of the upper bound of
||L K||_X^2. B(K, K) = U[K].grad K was not computed (needs the canonical inverse of d_x K; not cheap with the present tools). The coarse floating
values 0.0142 / 0.367 of the 16:57Z note are superseded.

