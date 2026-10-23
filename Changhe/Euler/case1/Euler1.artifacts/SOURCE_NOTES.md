# SOURCE_NOTES.md (lead): sources consulted, versions, what was borrowed, what was changed

Version: v1.1, 2026-10-23 07:38Z (v1 06:55Z; v1.1 updates section 5 for Theorem L2).
A detailed line-referenced digest of R1, R2 and R4 is in
sources/DIGEST_R1R2R4.md (lead artifacts); the verifier keeps its own independent source notes. Line numbers "l.N"
below refer to the pdftotext extractions saved beside the PDFs.

## 1. Primary sources named in the task

| Tag | Source | Version read | Date of version | SHA256 prefix (PDF) |
|---|---|---|---|---|
| R1 | Ganeshram, Duruisseaux, Anandkumar, "Self-Similar Singularity of the Euler Equations on R^3", arXiv:2609.10867 | v2 (main text and supplement); v1 compared | v1 9 Sep 2026, v2 24 Sep 2026 | v2 0518681bb991d8f4, v1 96cfb9899d1a1121 |
| R2 | Wang, Liu, Li, Anandkumar, Hou, "High precision PINNs in unbounded domains: application to singularity formulation in PDEs", arXiv:2506.19243 | v1 | 24 Jun 2025 | e2b866a596f46b51 |
| R2 code | github.com/RoyWangyx/High-precision-PINNs-unbounded-domains- | commit 466370c4f826503f6b9147dcc60e39222398acea (2026-03-23) | | read only, never executed |
| R3 | Constantin, Ignatova, Vicol, "On putative self-similarity for incompressible 3D Euler", arXiv:2602.17570 | v3 | 20 Jul 2026 | 81e987a26db35ea8 |
| R4 | G. Wang, Toftrup, Loeschcke, Yixuan Wang, Anandkumar, "SS-eSOAP: Self-Scaled Adaptive Preconditioning for Physics-Informed Learning", arXiv:2608.29448 | v1 | 29 Aug 2026 | 9e800c26a841ef69 |

Inaccessible or absent:
- R1: no training code, network sizes, loss weights, point counts, learning rates, iteration counts or profile data
  are public. v2 says the spline profile "will be made available"; the linked repository is a formalization
  repository and was not treated as training code.
- R2 code has NO LICENSE file. Nothing was copied; the campaign code re-implements from the published formulas.
- R4 gives no code URL; several hyperparameters (tau_min, warm-up length, weight decay, selected learning rate,
  per-layer vs global tau) are not stated.
- The journal version of Chae (Comm. Math. Phys. 2007) could not be retrieved by the referee; the arXiv preprint
  math/0601060v2 was retrieved and its hypothesis checked (by the verifier). For Chae-Wolf, J. Nonlinear Sci. 33
  (2023) only the abstract was accessible.

## 2. What was borrowed (method only), and how it was changed

| Idea | Source | Use in this campaign | Change |
|---|---|---|---|
| Direct stationary residual minimization of the profile equations | R1, R2 | yes | full 3D velocity-pressure system (E) instead of R1's axisymmetric (u^theta/r, omega^theta/r, psi^theta/r) system; c_l fixed in (0.4, 0.5), not 1/2 |
| FP64 end to end | R1 SI 2.1.2; R2 code | yes | none |
| Hard symmetry by output symmetrization (f +- f o R)/2 | R2 3.2; R1 SI 2.1.4 | yes | replaced reflection parities by the rotation projection S F(y) = [F(y) + Q F(Qy)]/2, Q = diag(-1,-1,1), applied to a vector potential A (curl commutes with Q), so U = curl A is exactly divergence free and exactly Q-equivariant. No reflection or inversion parity is imposed |
| Hard constraint against the trivial solution | R2 3.2 (Taylor constraint) | partly | no Taylor constraint at the origin; nontriviality from a smooth, divergence-free, non-axisymmetric seed (task section 9) plus a soft scale gauge (smooth max of |U| on the core equal to 1). The R2 constants (U'(0) = -1 etc.) are problem specific and not used |
| Wide-range coordinates (sinh map on a [-30,30] box) | R1 (S38)-(S41); R2 3.1 | changed | the campaign networks take bounded direction features y/sqrt(l^2+R^2) and |xi|^2 with explicit algebraic envelopes rho^(d+1), rho^(2d) for A and rho^(2d), rho^(3d-1) for P (d = 1 - 1/c_l), so the leading and first subleading far-field degrees are built in. An earlier variant with an unbounded log-radius input was shown (by the verifier) to force an axisymmetric leading learned tail and is kept only as a negative result |
| "Exact asymptotics" U = U_tilde + chi g | R2 3.1 | changed | the leading angular profile g is unknown in 3D and is left free (learned over the envelope), not prescribed |
| Smoothness loss on the residual gradient | R1 (S42); R2 (1) | not yet | not in the first sweep |
| Residual-based adaptive sampling, origin-biased sampling | R1 SI 2.1.5 | partly | region-stratified sampling (core ball, origin ball, axis tube, logarithmic shells to R_max) in physical coordinates; RAD not yet implemented |
| Staged optimization Adam -> SS-eSOAP -> SS-Broyden | R1 SI 2.1.2; R4; R2 code | changed | Adam stages followed by standard PyTorch L-BFGS with strong Wolfe line search. SS-eSOAP and SS-Broyden are NOT implemented and are not claimed |
| Boosting with frozen earlier stages | R1 (S36) | not yet | |
| Free scaling exponent | R1 (side study, drifted to 1/2); R2 code (exact quadratic update, since the residual is affine in the exponent) | planned | fixed-c_l sweeps first; a bounded trainable-c_l branch later; drift toward the bound 1/2 is to be reported, not hidden |
| Free axial drift C | R1 traveling ansatz | available | C e_3 in the transport is equivalent to a center shift by C/c_l along e_3 (EQUATIONS.md 1.2); current runs use C = 0 |
| Region-by-region validation on many independent points | R1 Table S1 | yes | physical-volume measure (R1 reports computational-coordinate cRMSE); independent evaluator written by the verifier with finite differences, not the training autograd path; nonlinear-scale tail checks |

## 3. Assumptions in the sources NOT borrowed (incompatible with the task)

1. Axisymmetry (R1 throughout). R3 Theorem 4.5 (with its assumptions (3.5) and (3.8)) excludes axisymmetric C^2
   decaying profiles with c_l < 1/2, so an axisymmetric reduction cannot reach the target range.
2. lambda = 1/2 fixed (R1 (S27)) and the dynamic-rescaling normalization built on it.
3. The local outgoing property at stagnation points (R3 Definition 3.7). By R3 Theorems 3.8 and 3.9 it is
   incompatible with nontrivial profiles with c_l < 1/2 under (3.7), (3.8); it is never imposed.
4. Reflection parities and boundary conditions specific to Burgers, 2D Boussinesq and the axisymmetric problem.
5. Truncation of the profile to zero outside a box (R1 spline stage): valid there only because the exterior is
   handled analytically with lambda = 1/2.

## 4. R3: hypotheses checked (as required by the task)

- Finite-energy restriction (R3 Theorem 2.1): assumes a smooth physical Euler solution with finite initial kinetic
  energy that actually blows up, plus the stated uniform bound on the rescaled vorticity gradient; it gives
  c_l >= 2/5. It does not exclude profiles in 0.4 < c_l < 0.5. Elementary scaling: the energy in the ball
  |x - x_*| < tau^(c_l) is tau^(5c_l - 2) times a profile integral, and the blowup-time limit |x|^d is locally L^2
  iff c_l > 2/5 (EQUATIONS.md section 8).
- Local outgoing restriction (Definition 3.7, Theorems 3.8, 3.9): assumes N_V finite and the local outgoing
  inequality at every zero, plus (3.7), (3.8). It is conditional and not an exclusion of the task class.
- Axisymmetric restriction (Theorems 4.3, 4.5): Theorem 4.3 concerns a meridional fixed point with nonzero swirl
  (forcing gamma = 1/2); Theorem 4.5 assumes C^2, axisymmetry, (3.5) and (3.8). Neither is transplanted to m = 2.
- Exponent conventions: R3 gamma = R1 lambda = this campaign's c_l.

## 5. Further literature used for the stagnation-set result (THEORY_NOTES.md)

Exponent conversion: u = (T-t)^(-alpha/(1+alpha)) v(x/(T-t)^(1/(1+alpha))) gives c_l = 1/(1+alpha).
- D. Chae, Comm. Math. Phys. 273 (2007) 203-215 (arXiv:math/0601060v2): Omega in L^p for all 0 < p < p_1 implies
  Omega = 0 (the hypothesis is "for all small p", not one p).
- D. Chae, R. Shvydkoy, Arch. Ration. Mech. Anal. 209 (2013) 999-1017 (arXiv:1201.6009).
- L. Bronzi, R. Shvydkoy, Indiana Univ. Math. J. 64 (2015) 1291-1302 (arXiv:1310.8611).
- D. Chae, arXiv:1308.1051 (maximum principle approach).
- D. Chae, J. Wolf, Comm. Math. Phys. 376 (2020) (arXiv:1706.02020); J. Nonlinear Sci. 33, 115 (2023) (abstract only).
- M. Shub, Global Stability of Dynamical Systems (1987), Thm III.7; restated in Lee, Simchowitz, Jordan, Recht,
  COLT 2016, Thm 7 (stable-center manifold theorem, used for the measure-zero basin step).
- A. Vanderbauwhede, Dynamics Reported 2 (1989); C. Chicone, Ordinary Differential Equations with Applications.
None of these was found to imply the stagnation-set theorem L1, or its successor L2 (no hypothesis on the stagnation
set; THEORY_NOTES.md section 7), under their exact hypotheses; this is a bounded search, not a novelty claim. The
stable-center manifold references were used for L1. L2 proves the needed local null-graph property directly by a
weighted contraction estimate in an adapted norm and does not depend on them.

## 6. Code and data provenance

All campaign code (solver, runner, ledger, validation) was written for this campaign. No source code from R1, R2
or R4 was copied or executed. Model parameters from R1 or R2 were not used.
