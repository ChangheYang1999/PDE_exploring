# NUMERICS_REPORT (numerics team) - current summary

Updated 2026-10-28T17:55Z (final state of a session; run ends 18:20Z; no computation running since 16:53Z). CPU limit: 4 cores / 4 busy workers since 04:20Z (2 before). Background of every rigorous statement:
the exact modal trial rho~ (modal_v2.json + the exact scalar repair z, V005). Labels: CERTIFIED (ball arithmetic, inputs identified),
FLOATING (evidence only), PENDING, OPEN. Details and inputs: S2_NUMERICAL_CERTIFICATES.md (C1..C7 with addenda certified, N1..N4 numerical), S2_BASIS_CERTIFICATION.md.

1. Research copies: research_copy/case1, research_copy/analysis1 (verifier V001).
2. Section 6.1: earlier finite sections recovered exactly (notes team message 1) and REPRODUCED in floating point (C^1/H1q: 0.41312, 0.52004,
   0.54650; C^0/L2: 0.16978, 0.20276, 0.21306; archived 0.4131, ...; logs/repro_M16.log).
3. CERTIFIED (C1): exact trial strain c[rho~] - (3/k - 1) in [-1.62e-43, 1.62e-43] (three formulas, 320 bits).
4. Exact operator images, conforming basis, section assembly: identity test PASSED (C2, 1.7e-46). Code refereed by second-model referee (opcheck) and
   audited by the verifier (V020, V027, V033, V037, V043, V054, V056).
5. CERTIFIED (C3, C3b; finite statements only): section S0 (169 conforming columns + TAU, 12 x 69 rows, exact integration, 256 bits).
   Whitened domain Gram PD (||E|| = 1.75e-27, = verifier V056). sigma_min >= 4.3337e-07 with TAU (weakest direction = TAU: the
   compensated tail column is almost invisible to test splines ending at t = 16.1); without TAU sigma_min >= 2.0685e-02 (float 0.02111;
   weakest: far power columns out5/out8/out9). By Prop IV.O (V039) S0 cannot give a continuum bound: pipeline test, not a theorem input.
6. ENCLOSURE REPAIR (04:10Z to 04:35Z): the box enclosures of margin.py/hypA.py (f(h/2) +/- sup|f'| h/2 with coefficient sums) were useless
   on the spline cells (large cancelling coefficients: radii 1e2..1e5 too large) and on the inner sub-cells (V054 near-resonance, inner
   mode 27, lambda = 1.07e-12, lambda^-7 cancelling coefficients: radii 1e78). New encl.py: exact merging of near-resonant exponent
   clusters (truncated e^{lambda sigma}, J = 40, rigorous remainder, >= 512 bits) + Taylor enclosure of order 8 about the midpoint with the
   rigorous remainder + sub-intervals of width <= 6/|e|_max. Containment test at 512 bits (logs/dbg_encl2.log): cell 4 (inner, h = 1/2) sum of
   radii 4.3e-6 (old 3.4e78), cell 1 (h = 2) 1.2e-7 (old 9.2e33), cell 1563 (outer, h = 1/2) 1.9e-2 (old 1.3e5), 0 violations of 9 x 260
   sampled values per cell. The margin run of 02:06Z-04:03Z used the old enclosures and was stopped before producing a certificate.
7. CERTIFIED (C4, C5; 05:10Z; the two remaining coefficient hypotheses of the theory author's Theorem C', V055): on all 1569 radial cells x 64 angular
   boxes (zero negative boxes): Theorem R margin inf m >= 2.482724 for the weight e^{mu~} (theory author message 5; 1.029821 before the adaptive angular
   refinement, depth 6); anisotropic margin inf m_a >= 2.871539 for w_a (a = 17/4, theory author message 7; 0.965918 before the refinement and the sharper
   tail bound; IMPROVED 12:45Z to inf m_a >= 2.9270 by a finer radial cover of the first outer sub-cell, C4 addendum, and 15:54Z to
   inf m_a >= 3.000000 (exact 3.0000003) by the finer cover of the whole outer region [t_+, t_+ + 8] (OUTER_F8 + OUTER_F403, C4 addendum 2;
   team-certified, not independently verified); now limited by the bulk cell t_a = 5.1695, box 3); kappa_* >= 3.037693; axis data d(t) = V_2(0,e^t)/e^t in [5.575203, 21.301451]
   (d > 0), |d'| <= 5.6012, endpoint constants sup_{t<=0} |d - D| e^{-2t} <= 0.100883, sup_{t<=0} |d'| e^{-2t} <= 0.202073,
   sup_{t>=0} |d - c_l| e^{(1-k)t} <= 89.335, sup_{t>=0} |d'| e^{(1-k)t} <= 73.312; (CB) constants M_Q <= 337.66, M_P <= 1075.516; sup b_+ <= 11.229,
   sup |grad rho~| <= 30.42, sup |DU| <= 125.744; (Z) data: |V|/r >= 0.10006 outside a neighbourhood of P (255 boxes, t in [2.131, 2.212],
   theta <= 15.5 deg), DV on the P box: xx [9.9588, 10.3327], xy [-1.7668, 1.8053], yx [-0.5901, 0.5699], yy [0.8180, 1.1919].
   Conditional on the exact normalization (V005) for one dropped constant (ball -4.3e-37 +/- 2.0e-35). Verifier: V086 confirmed the margins, V197 the 2.9270 addendum; addendum 2 (3.000000, 15:54Z) is not yet independently verified.
8. Guard test test_minf.py on the exact trial: OK (04:35Z).
9. CERTIFIED (C6, finite statement): L_fix section in L^2(e^{mu~}) (169 columns, 12 x 69 rows): sigma_min >= 0.510914 (float 0.52134; weakest
   direction the inner power columns in5/in6/in7 at r < 0.0077), after two-sided exact whitening (raw cond 3.5e68). S0 Phase 2 (pipeline test)
   and the identity rerun were dropped from the chain at 05:40Z to free the cores (C2 stands on logs/test_identity3.log).
10. FLOATING items (theory author team message 19-25).
    (a) eta = ||F(rho~)||_Y: WITHDRAWN from this team. My eta.py (exact residual modes truncated at N <= 40, least-squares cos^4 division) and
    eta2.py (pointwise/FFT) are not controlled approximations of the Y norm (verifier V111/V113: the truncated raw-sine map is not a
    contraction; the residual's strong energy is a thin near-axis layer with a flat angular spectrum up to mode 160, theory author message 25). Reference
    values: the theory author's all-mode point densities give ||F||_Y about 7.24e3 (axis part 123; 70% of the energy from log r in [8.135, 12]; far
    decay rate 4k - 5/4) and the verifier's proved lower bound ||F||_Y > 933.47 (V110, from the window 9.9 <= log r <= 10.1 alone).
    (b) FLOATING (09:50Z): core section of S_1 = T_R + C_R on R = L^2(w_a) (theory author message 19 item 3; fsec.py FSEC_MODE=S1; work/runs/S1/fsec_result.json):
    Mh = 2, stride 60 -> 42 remainder columns x^2 y b_i(t)(cos 2 theta + 1) (angular remainder mode m = 1 ONLY), chi_0 = the exact J cutoff,
    R norm on both sides, COMPLETE angular mode set (531 modes: jet split exact to 1.2e-15, cos^4 quotient exact to 9e-8 relative), Gauss nodes
    3/8/16 per cell type, 4817 s on 4 workers. Generalized singular values (50-digit solve of the stored double pair): 4.1552, 6.0843, 23.314,
    51.576, 53.109, 53.158, ...; largest 1038; on c[h_0] = 0: 4.44, 6.09, 23.3. The columns are nearly dependent in R (normalized Gram
    eigenvalues 8.9e-13 for the outer power columns out5/out8/out9, 2.1e-11 for sp0+in/sp1+in; seven below 1e-6): the Rayleigh
    quotient of the computed weakest direction (0.75 out9 - 0.55 out5 - 0.23 sp32+out - 0.22 out8, concentrated just beyond t_+ = 8.135) is in
    [4.137, 4.174] under an accumulation-rounding model (x^T G_Z x = 8.8e-6, x^T B_Y x = 1.5e-4 against estimates 1.5e-10, 1.3e-6), so the
    section's smallest value is <= 4.18 up to unmodelled errors; the next two computed values (6.08, 23.3) lie in near-null directions whose
    image quotients are below the rounding estimate and are undetermined; the ordered smallest value is not bounded below by this check. (CAVEAT 13:00Z, verifier V187/V189: the rounding model covers the accumulation only; the cos^4 divisions (input quotients through a padding-dependent pseudoinverse, about 1e-7 relative in G_Z; image quotients with a worst-case amplification 5.4e10) are not covered, so 'resolved' means resolved with respect to the accumulation rounding only.) Without the seven near-dependent directions: 10.13, 13.63, 50.96; pure spline columns (33): 50.32, 51.58, 53.16.
    On c[h_0] = 0: 4.4563, 6.0844, 23.314 (re-assembled 12:35Z with the repaired assembler fsec_assemble.py v2, theory author message 38: the v1 assembler
    double-counted checkpointed cells; the values of s1_robust.py were never affected). Upper bound of the infimum over the subspace only; no
    injectivity statement. Certification of this section is not feasible in the window (S2_BASIS_CERTIFICATION.md section 7).
    (e) FLOATING (12:35Z): S1M3 = the same section with Mh = 3 (84 columns: m = 1 and m = 2 of the 42 radial functions; 8709 s on 4 workers;
    work/runs/S1M3/fsec_result.json; logs/s1m3_*.log). 50-digit generalized singular values 2.3443, 2.9209, 3.5011, 3.8285, 3.9096, 4.6996,
    5.6894, 6.3370, ..., largest 2389.5; on c[h_0] = 0: 2.3457, 2.9281, 3.5083. Flags: 2.3443, 2.9209, 3.8285, 3.9096, 4.6996 UNDETERMINED
    (near-null combinations of the outer power columns, image quotients below the rounding estimate), 3.5011 weakly resolved ([2.55, 4.25]).
    Sub-blocks: m = 1 alone = S1 to the printed digits (4.1552, 6.0836, 23.314; Grams differ by 9.3e-8 relative, pseudoinverse input quotients, V187); m = 2 alone 3.6676 ([3.655, 3.680], far junction), 4.34, 12.44; without the
    seven most dependent directions 3.024, 3.345, 4.048. RESOLVED AND WELL CONDITIONED: the 52 pure spline columns (sp4..sp29, m = 1 and 2)
    give 3.4557, 4.2477, 5.4604, whereas the m = 1 splines alone give 50.32 and the m = 2 splines alone 25.47: the weakest vector mixes the two
    angular modes with comparable weights on sp19..sp25 (t = 2.9..5.9, r = 18..360). The weakest vector has a nearly constant mode ratio a_b/c_b = 1.45..1.8 (m = 1 over m = 2 coefficient) across the splines sp18..sp27, i.e. a FIXED angular profile h ~ r^3 cos^4 theta sin theta (a - 4 c sin^2 theta) (zero near theta = 39 deg) times a broad radial profile over t = 2..7 (artifacts/data/S1/S1M3_pure_spline_block.json, work/s1_vectors.py). The smallest value of S_1 on the spline subspace falls from
    50 (m <= 1) to 3.46 (m <= 2) through the coupling of the angular modes in the bulk; with m = 3 it falls further to 2.77 (S1M4P, item 10(f)): not
    converged in the angular cutoff. Numerical evidence only.
    (f) FLOATING (15:43Z): S1M4P = the S_1 section on the 78 PURE SPLINE columns (sp4..sp29) with m = 1, 2, 3 (10758 s on 4 workers; 1569/1569
    cells; work/runs/S1M4P/fsec_result.json; logs/s1m4p_chain.log). 50-digit values 2.7655, 3.2685, 4.3913, 5.3953, 5.6169, 6.8798; on c[h_0] = 0:
    2.7662, 3.2695, 4.3933; weakest Rayleigh quotient in [2.7655, 2.7656] (accumulation model). Sub-blocks: m <= 2 gives 3.4557, 4.2477, 5.4604
    (= S1M3 pure block); m = 1 alone 50.3201, m = 2 alone 25.4729, m = 3 alone 12.1142; the 60 high-graph columns sp7..sp26 (V210) in the low
    norms: 2.8648 (m <= 3), 3.7223 (m <= 2), 53.6343 (m <= 1). Weakest vector in the bulk splines sp21..sp27 (r about 48 to 1000), one fixed
    angular profile (mode coefficients about 1 : 1 : 0.47) times a broad radial profile. Value against the angular cutoff: 50.32 (m <= 1),
    3.456 (m <= 2), 2.766 (m <= 3): the fall continues but slows; not converged; m <= 4 did not fit in the window. Input Gram against the
    verifier's exact V202 Gram: largest entrywise relative discrepancy 7.41e-7, congruent quadratic-form relative error 2.69e-6 (gram_compare.py).
    The producer file (12:41Z fsec.py, pinv input quotients) was not frozen: work/runs/S1M4P/PRODUCER_PROVENANCE.md. Numerical evidence only.
    (g) FLOATING (16:52Z): S1J1 = the theory author's junction test (team message 32): Mh = 2, sp+out columns dropped, outer power columns out5..out9 attached at
    t_+ + 1 (BASIS_OUT_SHIFT=1; 38 columns; 4165 s on 4 workers; work/runs/S1J1/fsec_result.json; logs/s1j1_chain.log). 50-digit values 4.7481,
    15.14, 34.29, 44.21, 51.58; c = 0: 4.7482. Weakest direction -0.79 out9 + 0.56 out5 + 0.25 out8 (normalized Gram eigenvalue 9e-12), Rayleigh
    quotient weakly resolved in [3.7414, 5.5835] (S1 at t_+: 4.1552 in [4.137, 4.174]); 15.14 and 34.29 undetermined; four values below 50, all concentrated in the
    outer-column coordinates. Without the outer power columns 50.32, 51.58, 53.16; pure splines 50.3201 (= S1). Reading (corrected after the verifier's
    V279): the values below 50 are concentrated in the outer-column coordinates and move little under the junction shift; their coordinate
    near-dependence makes them weakly resolved but does not show them spurious (a genuine operator minimum shows the same phenomena); OPEN.
    The pure-spline mode-coupling values (e), (f) are the small values in the bulk.
    (c) Truncation study (logs/dbg_div.log): the quotient by cos^4 in a truncated angular basis is ill-conditioned by ~N^3 and the far weight
    e^{6.75 t} amplifies the error (at t = 6: 20 modes give 5% of the exact weighted density, 80 modes 92%); hence complete modes.
    (d) The L_red jet-realization section (with the KP column, ~1 min/cell with complete modes) is a cross-check only and is not run.
11. C7 (10:09Z; directed lower bounds from the certified box data, theory author team message 26-28): near-axis refinement (theta boxes 56-63, depth 6) of the
    decoupled-family margin m_fam = m_a + (a_ang - 17/4) tan(theta) V.grad(theta) - Delta q 1_{r>=1} on the 469 cells t_a >= 4.5:
    (4, 0.3): inf over the plane >= 1.1296 (0.7268 before), at the first outer sub-cell next to the y-axis; with the finer cover of that
    sub-cell (C4 addendum) >= 1.2501; with the finer cover of the whole outer region (OUTER_F8, C7 addendum, 15:54Z) still >= 1.250190 (float 1.2501909638), now
    limited by the bulk cell t_a = 6.3452 (r about 570), box 61 (the outer region is no longer limiting);
    (3.6, 0.3): >= 0.9596 (0.2154 before; 774 refined cells with t_a >= 2.5), attained inside the refined range at t_a = 5.70 (r = 299), box 61.
    Zero negative boxes. Says nothing about the mapping properties of these weights.
12. a session (15:33Z-18:20Z): S1M4P assembled (10(f), N3, basis report 7.7); OUTER_F8 merged (C4 addendum 2: inf m_a >= 3.000000; C7 addendum:
    m_fam(4, 0.3) >= 1.250190); S1J1 done (10(g), N4, basis report 7.8). second-model referee of outer_merge2.py and gram_compare.py (16:05Z): both
    hardened, values unchanged, two rounded-up six-digit figures corrected (1.250191 -> 1.250190; 3.058367 -> 3.058366); C7 family values re-derived
    with directed rounding (identical floats). Verifier V279 refuted my 'artifact' reading of the S1J1 far value: withdrawn (team message 31), wording
    corrected in 10(g), N4, basis report 7.8. Input Grams checked against the verifier's exact exports: S1M4P 7.4e-7 (V252), S1J1 6.0e-7 (V277).
    No computation is running or planned; the remaining time goes to documentation and artifacts (artifacts/README.md).
