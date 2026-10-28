## 2026-10-28 13:01Z (theory author, a session, team message 42: V185 and V186 accepted; where the high norm sits; a heuristic violation of the V185 test)

Verifier, numerics.
1. V185 (scalar-radius test) and V186 (eta_* > 36400585492) accepted. Theory author cross-audit of proof 182: the constant
   re-derived by hand (inner integral 4 sqrt2 h^(3/2), outer 4 sqrt2 h^(3/2)/3, total over 2 pi gives
   8 sqrt2/(3 pi)); floating central fifth differences give g_axis^(5)(1001/125) = -618839860.3 (steps 2^-18 and
   2^-20; the point is 1.5e-5 from a knot, the stencil stays inside the span), so the difference with g_axis^(5)(8)
   is 1.0668240e9, as in V186 (code: artifacts/code/farres/axis_d5b.py). V187 to V189 noted; the S_1 section values stay
   NUMERICAL and I will add the input division error to their description.
2. Where the high norm sits (NUMERICAL, theory author, floating; artifacts/code/farres/axis_profile.py and axis_profile.json):
   g_axis, g_axis^(5) and the axis transport coefficient d_axis = ell_0 - sum_n (-1)^n P_n at every 4th span midpoint.
   The knot-scale structure is concentrated in two zones: (a) t in [1.92, 2.62] (r about 7 to 14), where the knot gaps
   go down to 0.0019, with |g_axis^(5)| up to 6.06e9 at the sampled midpoints and sign changes between neighbours;
   (b) t in [7.9, 8.135], next to the outer junction (uniform gap 0.00796), up to 1.93e9. Elsewhere |g_axis^(5)| <= 2.1e6
   (and <= 3.4e4 for t < 1.85); beyond t_+ it drops to 9e5 at 8.25 and about 30 at 8.5. So eta_* is very likely of order
   1e13 or more: the point functional of V183 at t = 2.2335 gives about 2.6e10, and the pair (2.2259, 2.2335)
   (difference 9.4e9 over 0.0076) gives about 3.3e11 with the V186 constant. Certifying these is cheap but cosmetic;
   do it only if you have nothing more useful. d_axis is 21.30 near the origin (ell_0 + c[rho_0] = 5.575 + 15.73),
   18.1 to 14.2 in zone (a), 5.71 to 5.69 in zone (b).
3. A heuristic violation of the V185 test (DERIVED heuristic, not a bound; please look for a flaw). Leading order in
   the knot scale: f_0 = (ell_0 X + U[rho_0]).grad rho_0 - rho_0 has knot-scale part (ell_0 + u) dt(rho_0,knot), u the
   radial transport coefficient of U[rho_0] (the angular transport and U[rho_0,knot] are lower order). The chart
   direction M_0 = [X.grad rho_0 - k^2 L_fix(KP)]/n' has knot-scale part (1 - k^2 u[KP]) dt(rho_0,knot)/n'. For a smooth
   inner test d = x^2 y beta(t) with beta supported in t in [0, 1], A_0 d = L_fix d + c[d] M_0, and the knot-scale part of
   L_fix d is u[d] dt(rho_0,knot), with u[d] a decaying multipole above the support. Hence in both zones
   A_0 d is about W f_0 at the knot scale, W = c[d] (1 - k^2 u[KP] + n' u[d]/c[d]) / (n' (ell_0 + u)), plus terms that
   are smooth or of lower order in the knot scale. If the high norm is dominated by the knot scale (item 2), then
   eta_H |c[d]| / ||A_0 d||_(Y_H) is about n' (ell_0 + u) >= 3 ell_0 > 16.7 in zone (b) and about 3 x 16 = 48 in zone (a),
   against N4 < 9.06. So the test of V185, and with it (S), would fail for the archived trial in this chart and this norm.
   Mechanism: the linearization explains the knot-scale residual as a dilation-rate error, so the Newton step wants
   Delta ell = c[h_1]/n' of the order of -ell_0, outside I. A rigorous version needs an upper bound of
   ||A_0 d - W f_0||_(Y_H) and a multiplier bound for W in the same norm; with the present tools (the cutoff constant
   C_chi and the factor 2^sigma of the unspecified partition) that is not sharp enough, so I record it as a heuristic
   and as a requirement on the next trial (report 6.5 item 9: the high norm of the residual must not be dominated by
   knot-scale structure; joins of higher continuity or an analytic representation). If you see a cheap rigorous route,
   tell me; otherwise do not spend time on it.
4. Verifier, remaining priorities as I see them: (i) a flaw check of item 3 (short); (ii) numerics message 25 (C4 addendum
   inf m_a >= 2.9270, family bounds 1.2501 and 0.9596) if you intend to confirm them; (iii) the S1M4P audit when it is
   done (about 14:45Z); (iv) from about 17:00Z, a label audit of the final report: every THEOREM must cite a CONFIRMED
   V-number and every certified number an independent recomputation.
5. Numerics: before S1J1, please adopt V188 (record the expected cell-ID set at run creation; assert equality, not
   cardinality) and V189 (exact cos4 quotient templates Q_j = 2 (-1)^(m-1-j) (2m - 2j - 1) for the inputs VM[m]). In the
   S1M4P flags, state the input division error of V187 (relative Gram change about 1e-7); with normalized Gram condition
   4.4e4 its first-order effect on the pure-spline value 3.4557 is at most a few 1e-3 relative (floating estimate).

