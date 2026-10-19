You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

# Request: referee a far-field diagnosis and a proposed test (IPM Setting I team, numerics lane)

Problem (orientation): a stationary self-similar profile of 2D IPM on the full plane, (c_l X + U).grad rho = rho, U = grad^perp (-Delta)^{-1} d_x rho,
rho even in x and odd in y, rho = x^2 y a(x,y) near 0, a(0) = 1, c_l = (1 + psi_xy(0))/3. The team (lead lane) fits a trial family by
Gauss-Newton / LSQR and reports normalized residual maxima N_f = |R| / (|W_1 rho_x| + |W_2 rho_y| + |rho|) and N_v = |R| / (|rho| + |X.grad rho| +
|U.grad rho|) measured by an independent verifier between fit nodes, on a log-radial grid out to r = 7.65e6 (physical units; the fit's
inverse domain is 1e3 shape units = 7651 physical, with a two-term homogeneous closure beyond). Expected far field (SPEC): rho ~ r^k Theta(theta)
(1 + r^{k-1} Theta_1 + ...), k = 1/c_l = 0.1794.

Trial formula (lead's section 4.2, file final_sec4_v5_full.md, lines 101-130): with u = r/L,
q = 1 - (1+u^2)^{-(1-k)/2}, rho = x^2 y exp(H), H = ((k-3)/2) log(1+u^2) + sum_{m<=200} chi^{max(m-1,0)} b_m(q) cos(2 m theta) + (fractional term),
b_m clamped splines of degree 7 in q on [0,1] with 375 coefficients each. Fit rows: polar grid points with 1e-4 <= r < 900 shape units (0.9 x
R_shape), every second angle; LSQR damping 1e-8.

Facts measured by me (numerics lane) on the candidate's shape file c6g_shape.npz
(keys spline_knots (384 values incl. 8-fold end knots), k, L, R_shape; the lead's reader is centre_fit.py
load_shape / configure): the 370 distinct knots in q have their last interior knot at q = 0.99330, which is u = 446 shape units (previous ones
0.98662 = u 192, 0.97994 = u 117). The fit rows end at u = 900, q = 0.99624. So on the last knot interval [0.99330, 1] each b_m is one degree-7
polynomial, and the rows cover only its first 44 percent in q; the far-field model's Theta_0, Theta_1 (b_m(1), b_m'(1)) are the extrapolated
end values of that polynomial.

Verifier's far-field finding (VERIFY_REPORT VERIFY_REPORT.md, entries G73 and G76 (a)): on every fit
of the family, N_v for r > 1000 (physical) has its maximum 1.06e-6 to 1.15e-6 at r 3.4e4 to 3.7e4 physical (u 4400 to 4800 shape units, q ~ 0.9990),
next to the y-axis (first columns off the axis; the axis column itself is 9e-9; R and N_v grow like (pi/2 - theta)^2 off the axis), while inside
the fit domain (1000 <= r <= 7651) N_v is at most 2.2e-7; N_f for r > 1000 is 1.3e-7 at r 3.3e4, theta 0.84. The band beyond the fit radius is
"hardly moved by any fit" (fits differing by factors 2 elsewhere agree there to 1-2 percent).

My reading: the far N_v band lies in the unfitted extrapolation of the last polynomial piece; its value is set by the damping-regularised
extrapolation, not tested by any row; it is neither evidence for nor against the far-field model.

My proposed test (to run tonight on the GPU, ~1.5 h): the same fit (c6g end, c_l fixed, same basis) continued for 20750 LSQR iterations with
fit radius 9000 shape units (R_shape 1e4, two-term closure there; rows then reach q = 0.99943, 91 percent of the last interval), on a
log-radial grid 24576 x 960 (same density per decade as the 20480-point grid on 7 decades). Reading: (a) interior agreement with c6g by the
lead's domain rule (2-10 and 10-100 N_f within 1.5x, |h(P) - 1| < 1e-7); (b) N_v over 1000 <= r <= 7651, over 7651 < r <= 76514 (now fitted), and
over r > 76514 against c6g's 2.15e-7 / 1.1e-6 / (same band).

Questions:
1. Is the diagnosis right, i.e. can the far N_v maximum at u ~ 4700 be an unfitted-extrapolation value of the last spline piece? Is there a
   better explanation of its location next to the y-axis (where rho ~ x^2 y is small and N_v is dominated by |X.grad rho| ~ r^k |Theta|)?
   For instance, could it be the known finite regularity along the y-axis (a term ~ y^3 |x|^{p_3}, p_3 = 6 + 2/(2 c_l - 1) ~ 6.2, SPEC Lemma 5)
   that a cos(2 m theta) basis with m <= 200 resolves only algebraically, or a defect of the two-term closure at R_shape, or of the first
   correction term r^{k-1} Theta_1 (the lead's formula gives Theta_1 = -L^{1-k} (sum b_m'(1) cos 2 m theta + ...))? Give the test that
   would distinguish these.
2. Is the proposed fit-radius-9000 run a sound test? Pitfalls to expect: (i) does the degree-7 polynomial on [0.9933, 1] have enough freedom to
   satisfy the equation to 1e-7 out to q 0.9994 while keeping the interior (compare: the fitted part now spans 0.0029 in q and the new rows
   0.0061)? (ii) the log-radial quadrature density (24576 points over 8 decades) for the modal inverse and the rows; (iii) the exterior
   two-term closure now at 1e4 shape units: is its error negligible (the team measured the closure impact at R_shape 1000 as 2.6e-9 next to
   P and 1.3e-8 at r 20-300 in normalized-residual terms, scaling like R^{-(3-3k)} = R^{-2.46} between 1000, 333 and 111)? (iv) anything that
   would make the comparison with c6g unfair (different row count changes the objective's weights: weights are sqrt(14000/N_rows) x
   max(1, (0.04/r)^2); the fixed c_l; the same basis).
3. What is the right statement for the report if (b) falls by a factor >= 5 while (a) holds? And if it does not fall although fitted?
   Formulate both in one or two sentences each, with the caveats an adversarial reader would demand.
4. Independent of the test: for a profile with rho ~ r^k Theta_0(theta) and U ~ r^k V(theta) at infinity, write down the leading-order
   far-field equation for Theta_0 (angular ODE with the nonlocal V from Theta_0) and the first-correction equation for Theta_1; is Theta_1
   determined by Theta_0 or free? This decides whether a fit can lower the far band by adjusting b_m'(1) alone.
Answer concretely; small CPU checks (a few minutes) are fine; write only in your own folder.
