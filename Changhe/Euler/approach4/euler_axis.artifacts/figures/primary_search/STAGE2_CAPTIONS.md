# Captions for the numerics figures (Stage II set; F1 and F5 have their own caption files F1_caption.txt and F5_caption.txt)

All residual values are the holdout rho_max of section 6.1 of the pre-registered specification, computed by the primary numerical search; they are not registered values of the independent verifier unless stated.
No state meets any pre-registered threshold; every displayed residual is of order one or larger.

- stage2_rho_vs_level.png: holdout rho_max, inner relative R_q and inner relative R_eta against the ball polynomial degree D for every pinned-q0
  T1 group (q0, c_l, parity, matching radius) with at least two levels (D24/n12/K16, D36/n24/K24, D48/n32/K32, D64/n43/K43; the run with the
  most iterations per level). No series shows a sustained decrease with resolution (and no state is an accepted profile); the eta equation is met to 0.4 to 1 percent while rho_max
  stays above one because of the momentum and circulation equations in the core.
- stage2_rho_vs_cl.png: c_l continuation at D36 for the chains (ladder q0 3.5 by small steps from 0.749; fmA, fmB, fmC, fmD; reflection class)
  and the direct seeds (stars), with the core swirl fraction s_core in the right panel; dashed lines mark the bounds 0.749 and 0.501, the
  dotted line c_l = 2/3.
- stage2_farfield_convergence.png: R^alpha times the mu-rms of the poloidal and swirl velocities against R for six states; the leading tail
  is imposed by the analytically factored exterior from the matching radius 10 (dashed) on and is constant to 0.1 percent beyond R = 100;
  the kink at R = 10 shows that the asymptotics do not emerge from the interior.
- stage2_axis_origin.png: axis and origin-collar rms residuals of the q and eta equations for the q0 = 3.5 branch against c_l (offset by
  level) and against level at c_l 0.749; no growth with level or along the chain (no axis or origin singularity indicator).
- <job>_cost.png, _residual_vs_radius.png, _spectral_decay.png, _fields.png, _axis.png (per-run set for six key states: L1, L2, D64, q0 5.0,
  reflection D36, chain 0.74): weighted cost history; shell-wise rms residuals against radius; spectral coefficient decay per element and
  field; swirl and poloidal field maps; axis profiles. The spectral decay improves with level (ratio 2e-2 at D36, 1e-3 at D64) while the
  residuals do not.
