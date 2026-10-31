# Lead review of four verifier proofs (2026-10-29)

Reviewed: research/pressure_cartesian_difference, azimuthal_projection, finite_tail_integrability, newton_tail_decay
(verifier side, read only). Each was checked line by line; arithmetic of every constant recomputed.

1. pressure_cartesian_difference: CORRECT.
   - Five-point first-derivative stencil: moments t^0..t^4 give 0,1,0,0,0 (recomputed); remainder weights
     (1,8,8,1) at |t| = 2h,h,h,2h give 80 h^5/(12h*120) = h^4/18.
   - Second-derivative stencil: moments t^0..t^5 give 0,0,2,0,0,0 times the Taylor coefficients (so g''(0));
     remainder 160 h^6/(12 h^2 * 720) = h^4/54; the centre point has zero remainder.
   - Evaluation error: sum |coeffs| 18/(12h) = 3/(2h); Laplacian over three axes with the shared centre counted
     three times: (3*34 + 90)/(12 h^2) = 16/h^2, the same as stated.
   - (2) follows by the triangle inequality. Hypothesis C^6 on the three segments is what the Lagrange remainders need.
2. azimuthal_projection: CORRECT.
   - V' = Q_{-phi}[DU(y) J y - J U(y)] recomputed from dn/dphi = J n and the commutation of J with Q_phi.
   - Exactness needs N > 2M for |V|^2, |V - A|^2 and |V'|^2; stated.
   - Parseval bounds E_non <= G <= M^2 E_non, and 4 E_non <= G for even nonzero frequencies; ratio bounds follow.
   - The application paragraph correctly says that M must be the largest active azimuthal index over all channels,
     including the correction channels (V136: |m| <= 12, even), not the main degree.
   - Spherical components equal B0^T Q_{-phi} U with a phi-independent B0; stated.
3. finite_tail_integrability: CORRECT.
   - psi - psi0 = (kappa/2) log(1 + R0^2/r^2) recomputed from psi = (omega/(2c)) log(1 + r^2/R0^2).
   - xi = 2x - 1 with x = (s - R0)/(s + R0), s = sqrt(r^2 + R0^2), gives 1 - 4R0/(s + R0) = 1 + O(1/R).
   - Orders: T - T0 = O(R^(-alpha-1)), S - S0 = O(R^(-alpha)); toroidal operator keeps the order, poloidal loses one;
     B, D and E channels are of lower order for alpha in (1, 3/2) and l >= 2.
   - Scaling law checked: T0(lambda y) = lambda^(-alpha) T0(Q_{kappa log lambda} y) uses commutation of rotations
     about the third axis; the toroidal and poloidal operators have scaling orders 0 and -1 (checked by the change of
     variable y' = lambda y).
   - Energy: sphere integral of |U0|^2 is A r^(2-2alpha) by rotation invariance of the measure; the remainder
     r^(1-2alpha) is integrable at infinity because alpha > 1, i.e. c < 1/2. Helicity absolutely convergent likewise.
4. newton_tail_decay: CORRECT.
   - Hessian of 1/|x - y| in y has operator norm 2/|x - y|^3; remainder 8|y|^2/r^3 on |y| < r/2.
   - The four regional bounds recomputed: 2^(q-2)/(5-q), 2^(q-3) (using the volume pi r^2/2 of the near ball
     integral of 1/|z|), 3*2^(q-3)/(q-3), 2^(q-4)/(q-4).
   - Condition r >= 2 is not needed by the argument; harmless.
   - Application: q = 2 alpha + 2 is in (4, 5) for c in (2/5, 1/2). Wording to add where it is applied: the bound
     |tr((DU)^2)| <= |DU|_F^2 (Cauchy-Schwarz on sum_ij A_ij A_ji), so C = C_1^2 holds if C_1 bounds the Frobenius
     norm of DU; with the operator norm use C = 3 C_1^2.
   - The vanishing first moment needs alpha > 1 for the boundary terms (R^(2 - 2 alpha)); this lies in
     pressure_moments (reviewed earlier) and holds on the whole target interval.

Scope as the verifier states it: exact statements about the represented field; no numerical constants for any
checkpoint; no quadrature-error bound; no existence statement. Any report use must keep those conditions.
