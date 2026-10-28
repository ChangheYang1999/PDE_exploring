## 2026-10-28 13:28Z (theory author, a session, team message 45: V198 and V199 accepted; V198 cross-audit PASS)

Verifier, numerics.
1. V198 cross-audit PASS. The membership argument is correct: the trial is a degree-7 spline in t with C^6 joins, so
   rho_0 is locally in H^s for s < 15/2 (enough for the correction space, H^(29/4)), but X.grad rho_0 = d_t rho_0 has
   a sixth-derivative jump wherever the seventh derivative of the relevant cofactor jumps, hence lies only in H^s for
   s < 13/2. A smooth cutoff equal to 1 near the knot does not change the jump. Independent interval check (my own
   short script from the original spline polynomials, sine-coefficient form of the axis cofactor
   A = -sum_j (-1)^j (2j+1)^2 h_j / 2, spans 699 and 700): at knot 700, t = 2.2021335932..., the jumps of A^(j) for
   j = 0..6 contain 0 (widths up to 3e3 for j = 6) and the jump of A^(7) is -9.3e8 +- 5.7e6 (left 3.63e8, right
   -5.71e8). So beta_K = -2A - A' has a nonzero sixth-derivative jump of about 9.3e8. This also confirms the size of
   the knot-scale structure in zone (a). Recorded in the report (1.6, 6.3, 6.6), CLOSURE item 9, L2 verdict list and
   RESTART item 7 ("do not use the scaling tangent as d"). Note that f_0 and M_0 are in the targets, which need only
   H^(25/4) < 13/2, so the chart and Theorem E are unaffected, as you say.
2. V199 accepted: the documents now state the relative threshold 0.0507 (from N4 <= B = 9.0450253607...), and keep
   0.050584... as the value from 9.06 alone. The heuristic comparison now reads 0.036 to 0.041 (zone a, n'_0 = 3)
   against 0.0507.
3. Priorities unchanged. Verifier: S1M4P audit when numerics posts it; the label and consistency audit of the report
   from about 17:00Z (please flag any THEOREM label not backed by a CONFIRMED record, and any number quoted without its
   record). Numerics: S1M4P (about 15:00Z), then S1J1 or the outer cover refinement, then end documents by 17:30Z.

