# Origin vorticity sensitivity at fixed reduced coefficients

Status: proved informal identity for the exact even-mode representation. Numerical certificates and the lead's independent review are recorded separately. No optimized state or Euler solution is asserted.

## Statement and hypotheses

Use the smooth finite toroidal-poloidal representation and harmonic normalization of `../canonical_origin_vorticity/PROOF.md`. In particular, every azimuthal order is even, the smooth twist is zero at the origin, the main envelopes are one there, and every correction channel vanishes there with the damping specified in that proof. Let the main radial count be an integer N >= 2. For each main A or C mode, hold its first N-2 Chebyshev coefficients fixed as real numbers. Reconstruct its final two coefficients by the exact inviscid constraints in `../tail_coordinates/PROOF.md`. This defines the *exact reduced-coordinate family*. It need not equal the originally stored full coefficient array after rounded reconstruction.

Let c lie in [2/5,1/2] and let w be any positive real number. These closed c endpoints are used only to enclose a family whose physical parameter domain is the open interval. The algebraic tail constraints and smooth core representation remain defined at both endpoints. Set

    n = N-2, m = N-1, d = m^2-n^2, Q = (8/3)n^2 m^2,
    K_j = (8/3)j^2(j^2-1).

For an axial mode (ell,0,0), put sigma=0 for A and sigma=1 for C. For its fixed free coefficients z_j, 0 <= j < n, define

    S0 = sum z_j, S2 = sum j^2 z_j, S4 = sum K_j z_j,
    F = sum (-1)^j z_j,
    C0 = (m^2+n^2)S4 - (K_m+K_n)S2,
    C1 = 2S2 - (m^2+n^2)S0,
    A = F + (-1)^n C1/d,
    B = (-1)^n (C0-Q C1)/d,
    H = Q + (ell-sigma-1)/2.

An empty sum is zero. The reconstructed alternating sum of this mode is exactly

    L(c) = A + 2Bc/(1+2Hc),
    L'(c) = 2B/(1+2Hc)^2.                                      (1)

Its denominator is positive throughout [2/5,1/2]. Consequently its range on any closed subinterval is the interval between its endpoint values. These axial quantities are independent of w.

Write a1=L_A,ell=1, a2=L_A,ell=2, g1=L_C,ell=1 and g2=L_C,ell=2. A missing axial mode contributes zero. With C10=sqrt(3/(4 pi)) and C20=sqrt(5/(16 pi)), the exact axial vorticity residual is

    R3(c,w) = 2 C10 [a1(c) + 12 C20(g1(c)a2(c)-a1(c)g2(c))].     (2)

The full residual vector at the origin is R3 e3. At fixed reduced coefficients,

    partial_w R3 = 0,
    partial_c R3 = 2 C10 [a1' + 12 C20
                         (g1'a2+g1a2'-a1'g2-a1g2')].           (3)

If interval evaluation of (2), using the exact endpoint ranges from (1) and rigorous positive enclosures of C10 and C20, excludes zero, then no member of this fixed-reduced-coefficient family solves the rotating Euler momentum equation with a C2 pressure, for any c in the enclosed interval and any w>0. The conclusion does not apply when the reduced coefficients change.

## Proof

For an axial mode, the complex parameter of the tail-constraint proof is real:

    P = (alpha+ell-sigma)/2 = 1/(2c)+(ell-sigma-1)/2.

It has no w dependence. The final two coefficients u and v solve

    n^2 u + m^2 v = -S2,
    (K_n-P)u + (K_m-P)v = -S4 + P S0.

The determinant is d(Q+P). It is positive: d>0, Q>=0, and alpha=1/c-1>=1 gives P>0 for ell>=1 and sigma in {0,1}. Cramer's rule yields

    u = [m^2 S4-K_m S2+P(S2-m^2 S0)]/[d(Q+P)],
    v = [K_n S2-n^2 S4+P(n^2 S0-S2)]/[d(Q+P)].

Since m=n+1, the alternating sum of all N coefficients is

    F+(-1)^n(u-v)
      = F+(-1)^n(C0+C1 P)/[d(Q+P)]
      = A+B/(Q+P).

Multiplying the last denominator by 2c gives (1). Also H>=-1/2, so 1+2Hc>=1-c>=1/2 if H<0; when H>=0 the denominator is at least one. Differentiation proves the formula for L'. Its sign is constant, or zero when B=0, proving the endpoint-range assertion. For N=2 every free sum is zero and the same formulas give the identically zero mode.

The origin-vorticity proof shows that only these four axial alternating sums enter the axial residual. It also proves that the full vector is axial and that the explicit c and w terms vanish there. In particular, non-axisymmetric even modes and all allowed correction channels cannot contribute to (2), including through radial derivatives of the twist. Substituting (1) into that established identity proves (2). The reconstructed m=0 tail constraints have no w dependence, so differentiating (2) proves both parts of (3).

For the interval conclusion, the elementary interval sum and product rules include every value obtained from the enclosed real inputs, even when some inputs are dependent. Applying them to (2) therefore encloses every R3 in the stated family. If this enclosure omits zero, each member has nonzero curl of its momentum residual at the origin. The identity curl R_u=R_Omega from the origin-vorticity proof holds for any C2 pressure. Such a member cannot have R_u identically zero.

## Interpretation and scope

The zero w derivative is a local diagnostic of the origin residual in the even-mode class. It is not a statement that the full field, pressure, objective or other spatial residuals are w-independent. It is not a null direction of the complete objective Jacobian.

The interval argument can certify only the explicitly defined fixed reduced coordinates. Joint optimization changes those coordinates, so even a whole-interval exclusion says nothing about nonexistence in the basis or in the Euler problem. A full-array checkpoint, its floating tail projection and the exact reduced family must be distinguished in the numerical record. No finite precision evaluation or small residual is used as a proof premise.

Dependencies: the two complete informal proofs cited above, Cramer's rule, elementary differentiation, and inclusion-preserving interval arithmetic. No formal verification has been performed.
