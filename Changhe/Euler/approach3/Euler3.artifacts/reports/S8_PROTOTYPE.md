# S8 artificial-viscosity continuation device: implementation and prototype (numerics; written 2026-10-25T05:36Z)

Scope. Lead registration 2026-10-25T05:14:51Z (reports/stage2_plan_draft.md S8, readings R7-R9; derivations d63, d63a; the verifier's
theory/artificial_viscosity). AV: R^nu = R_u - nu Delta U with constant nu. Every state produced under nu > 0 is a "viscous continuation
state (nu = ...)"; it is never ranked with Euler states and never a candidate (an Euler candidate needs an inviscid refinement started from
it, with R_u at nu = 0 under the SPEC tiers and the independent route).

## Implementation (code paths)
- Delta U: Model.laplacian_grid / laplacian_points (src/equations/fields.py). For U = curl(T y) + curl curl(S y), Delta(f y) = (Delta f) y +
  2 grad f and curl grad = 0 give Delta U = curl((Delta T) y) + curl curl((Delta S) y); for a potential sum_q f_q(rho) P_q(y) (rho = r^2, P_q a
  degree-l solid harmonic) Delta[f P_q] = [(6 + 4 l) f' + 4 rho f''] P_q, so the Laplacian radial functions are built from the K = 6
  radial derivative arrays (twist included, since the twisted radial functions multiply the untwisted P_q) and fed to the same assembly.
- Residual: Problem(nu=...) adds mt['visc'] = -nu Delta U to the momentum residual (src/optimization/problem.py evaluate); the
  all5/all5far shell denominators include it as a sixth term. Pressure unchanged (div Delta U = 0).
- Parameters: c_l fixed by a pin row pin_weight (c_l - pin_c_l) on the free-parameter path (free_params=True, so omega moves and the
  pressure kernels are rebuilt per accepted step); nu fixed per run (this prototype; the lead's S8 has nu = nu_0 exp(s) free as well).
- Tail constraints (src/optimization/tail_constraints.py, TailConstraints(model, nu)): the rate alpha+1 moment stays zero; the rate alpha+2
  moment becomes C_2 = -(nu/(2 c_l R0^2)) B t with t = sum a + i sum b the leading amplitude of a cos/sin pair and
  B = (-P - i m kappa)(1 + 2 l - P - i m kappa), P = alpha + l (T) or alpha + l - 1 (S), kappa = omega/c_l (in the code's normalization
  (k4 - p).a + q 1.b is the coefficient of (R0/r)^(P+2) when sum a is the coefficient of (R0/r)^P).
- Diagnostics (src/validation/viscous.py): on the SPEC holdout family, rho^nu (six-term), sigma^nu = RMS(R^nu)/RMS((1 - c_l) U), the
  viscous share of the terms, the inviscid rho_u and sigma_u of the same state, D = int |DU|^2 over the holdout range; worker VISC line;
  ledger fields nu, label, rho_nu_max_holdout, sigma_nu_max_holdout, rho_u_inviscid_of_viscous_state, omega_final, c_l_final.
- Enqueue: scripts/enqueue_continuation.py --nu NU --free --pin_c_l 0.45 (job id carries _AVnu...).

## Implementation tests (tests/test_S8_viscous.py, all PASS 2026-10-25T05:36Z, GPU 4)
- I1 Delta U from the potentials against the exact AD Laplacian (forward-mode derivative of DU with respect to the point, summed): 4.2e-16 at
  33 points including axis and origin points; grid against point evaluation 5.6e-16 (requirement 1e-8).
- I2 (algebra, sympy, exact): Delta[r^-P e^(-i m kappa log r) P_q] = B r^(-P-2) e^(-i m kappa log r) P_q for l = 1, 2 and m = 0, 1, 2.
  I2 (end to end): on a random L4 state expanded through the two constraint versions, r^(alpha+2) RMS(L U - nu Delta U) on far spheres
  r = R0 2^14..2^20: homogeneous constraints 1.17, 0.73, 0.64, 0.62 (tends to the viscous constant nu |Delta U_0|); inhomogeneous
  0.70, 0.18, 0.044, 0.012 (rate alpha+3 decay, ratio 1.9e-2 at 2^20). Beyond 2^20 R0 the K = 6 Chebyshev derivatives are roundoff-limited
  (T1 alone is 1e11 there), and inside 2^14 R0 the rate alpha+3 term of a random state dominates; the nonlinear terms (rate 2 alpha + 1,
  only r^-(alpha-1) faster than alpha + 2) are excluded from this linear check.
- I3 ball identity int_B U.R^nu = beta_0 E + (c_l R/2) E' + R^2 int_S (P + |U|^2/2) U.n + nu int_B |DU|^2 - nu R^2 int_S U.(n.grad)U on a
  random L4 state with channels, R = 1.3, 64 radial Gauss nodes: relative difference 4.4e-16.
- I4 nu = 0 reproduces the Stage I residual vector exactly (0.0); nu = 1e-3 changes it by 5.4e-6.

## Prototype runs (lead budget at most 2 GPU-h before the gate; status 2026-10-25T07:26Z)
Free-omega formulation (c_l pinned at 0.45 by a row, omega free, nu fixed; 300 iterations each):
| run | start state | nu | result (viscous diagnostics on the holdout family) | reading |
|---|---|---|---|---|
| s8 L4 nu 3.8e-3 (0.1 c_l a_eff^2) | nest4 (0.45, 1) L4 | 3.8e-3 | rho^nu 0.87, sigma^nu 23.9, viscous share 0.91, omega 1.0 -> 0.207, max abs U 1.14 -> 0.034, origin-ball U_rms 2e-4, inviscid rho_u 0.86, E_ren -5.55, Q_sw 156, tau_F 1.00; 1992 s | failed viscous solve (R7 (a) fails by 2e3): the LM lowers the core amplitude until the field is its own tail; optimizer tendency, not a dynamical statement (verifier 07:00Z) |
| s8 L4 nu 3.8e-2 | nest4 (0.45, 1) L4 | 3.8e-2 | rho^nu 0.99, sigma^nu 580, viscous share 0.99, omega -> 0.533, max abs Omega 0.03; 3245 s | the same failure at 10x nu |
| s8 L6 nu 6.5e-4 (0.1 c_l a_eff^2) | d6t_L6 (channels at degree L) | 6.5e-4 | running (free omega; 1 h limit) | read for the lead's question whether the D6 lineage collapses the same way |
| s8 L6 nu 6.5e-3 | d6t_L6 | 6.5e-3 | CANCELLED (queue/cancelled) | superseded by the 06:56Z steering |
Steering applied (lead 06:56Z item 4): omega fixed as well as c_l; a core nontriviality row (core_pin: core RMS of U on the training nodes r < R0
pinned at its start value, weight 100); nu ladder from small values upward by factors of about 3. Pinned runs s8p on d6t_L6 at nu 6.5e-5 and
2e-4 (300 iterations, omega and c_l fixed, core RMS pinned at 1.685; finished 2026-10-25T07:38Z):
| s8p L6 nu 6.5e-5 | d6t_L6 | 6.5e-5 | rho^nu 0.0551, sigma^nu 2.00, viscous share 0.001; inviscid rho_u of the state 0.0547 / 0.0747, sigma_u 1.99; 1154 s | the viscous term is a 0.1 per cent perturbation: the LM stays at the D6 floor (no collapse with the pin, nothing to continue) |
| s8p L6 nu 2e-4 | d6t_L6 | 2e-4 | rho^nu 0.0565, sigma^nu 2.03, viscous share 0.004; inviscid rho_u 0.0550; omega 0.3000 | same |
Reading: with omega fixed and the core pinned, nu up to 2e-4 (0.03 c_l a_eff^2) changes nothing (viscous share below 0.5 per cent) and the D6
floor persists; the unpinned runs collapsed at 0.1 c_l a_eff^2 and above, where the viscous share would reach 10 to 90 per cent. The pinned
formulation has not yet been tried in that range (the next rungs 6.5e-4 and 2e-3 would cost 0.3 GPU-h); the Stage I cap of 2 GPU-h is used up
(about 2.0 GPU-h in total), so this is left to the Stage II decision (R7-R9). No S8 state is an Euler candidate; the AV continuation has so far
either done nothing (small nu) or destroyed the core (large nu, unpinned).
Cumulative S8 GPU time (Stage I): about 1.7 GPU-h for the four free-omega runs (incl. the running one) plus about 0.3 GPU-h for the two pinned runs.
