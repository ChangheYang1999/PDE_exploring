# The represented and required first nonlinear far-field coefficients

Written 2026-10-29. Status: the finite-representation identities below are proved informally. The conclusion about a full pressure is conditional on its stated remainder. Numerical evaluations and their errors are separate.

## Statement, notation and hypotheses

Fix real numbers 2/5 < c < 1/2, omega != 0 and R0 > 0. Put alpha = (1-c)/c, kappa = omega/c and beta = 2 alpha + 1. Then 1 < alpha < 3/2 and 3 < beta < 4. Let J(x,y,z) = (-y,x,0), and let Q_t = exp(tJ). All curls and derivatives use fixed Cartesian coordinates. The sphere has surface-area measure dS, of total mass 4 pi.

Use the finite real orthonormal scalar harmonics Y_lm on S^2, with separate cosine and sine labels when m > 0, and solid harmonics H_lm(y) = |y|^l Y_lm(y/|y|). The common index set is finite, contains whole cosine/sine pairs, and has l >= 1. Missing channels are zero. A, B, C and D are finite real Chebyshev coefficient matrices. A coefficient at the Chebyshev endpoint 1 is its column sum; denote these sums by Ainf, Binf, Cinf and Dinf. Let r = |y| and theta = kappa log(r/R0).

For y != 0 define

    T0(y) = sum Ainf_lm (r/R0)^(-alpha-l) H_lm(Q_theta y),
    S0(y) = sum Cinf_lm (r/R0)^(1-alpha-l) H_lm(Q_theta y),
    T1(y) = sum Binf_lm (r/R0)^(-beta-l) H_lm(Q_theta y),
    S1(y) = sum Dinf_lm (r/R0)^(1-beta-l) H_lm(Q_theta y),
    Uj = curl(Tj y) + curl curl(Sj y),   j = 0,1.

These fields are smooth away from zero and divergence free. Write F(n) = U0(n), G(n) = U1(n), H(n) = curl U0(n), and define

    L V = (1-c)V + c(DV)y + omega(JV - (DV)Jy).

The following identities hold exactly.

1. L U0 = 0 and L U1 = -U1.
2. For any lambda > 0 and j = 0,1,

       Uj(lambda Q_[-kappa log lambda] y)
         = lambda^(-gamma_j) Q_[-kappa log lambda] Uj(y),
       gamma_0 = alpha, gamma_1 = beta.

3. Put s(n) = tr((DU0(n))^2). In orthonormal complex spherical harmonics Y_lm proportional to exp(i m phi), expand s = sum s_lm Y_lm. For q_m = -2 alpha + i m kappa define

       p_lm = s_lm / [l(l+1) - q_m(q_m+1)].

   Every denominator is nonzero. The real pressure

       P0(rn) = r^(-2alpha) sum p_lm Y_lm(Q_[kappa log r] n)

   solves -Delta P0 = tr((DU0)^2) on R^3 minus {0}. Its unit-sphere gradient is

       grad P0(n) = sum p_lm [q_m n Y_lm(n) + grad_S Y_lm(n)].

   Let Greq = (DU0)U0 + grad P0 on S^2. The coefficient with velocity decay r^(-beta) in the formal primitive residual is Greq - G, provided the full represented field has the channel expansion described below and its pressure satisfies grad P - grad P0 = O(r^-4). This conditional statement does not say that other coefficients vanish.

4. Define tau_lm = R0^(beta+l) Binf_lm and sigma_lm = R0^(beta-1+l) Dinf_lm. Then

       integral |G|^2 dS
         = sum l(l+1) tau_lm^2
           + sum {l^2(l+1)^2
                  + l(l+1)[(2-beta)^2 + (m kappa)^2]} sigma_lm^2.

5. The squared shell-energy coefficient due to U1 is 2 integral F dot G dS. Its corresponding helicity coefficient is

       integral [F dot curl U1 + G dot H] dS
         = integral [2H - (1-3alpha) n cross F] dot G dS.

   Here curl U1 is evaluated at radius one. This is a coefficient identity, not an identity for a complete finite-ball integral.

## Proof

For a constant rotation Q, solid harmonics compose with Q, and the maps T -> curl(Ty) and S -> curl curl(Sy) commute with its action on scalar potentials and Cartesian vector fields. Homogeneity of H_lm therefore gives identity 2 directly from each displayed potential. Differentiating it in lambda at one gives

    (DUj)y + kappa(JUj - (DUj)Jy) = -gamma_j Uj.

Multiplying by c and adding (1-c)Uj gives eigenvalue 1-c-c gamma_j. It is zero for gamma_0 = alpha and equals -1 for gamma_1 = 2alpha+1. This proves identity 1. Smoothness away from zero follows from the finite sums and positive r, and divergence of a curl vanishes there.

The source transforms as a scalar of degree -2alpha-2 in the rotating coordinates, because DU0 transforms by conjugation with constant rotations as well as scalar dilation. For a complex spherical harmonic,

    -Delta [r^q Y_lm(n)]
      = [l(l+1)-q(q+1)] r^(q-2) Y_lm(n).

The term Y_lm(Q_[kappa log r] n) contributes r^(i m kappa). This proves the pressure formula. If m != 0, the imaginary part of q(q+1) is m kappa(1-4alpha), which is nonzero. If m = 0, a zero denominator would require l(l+1) = 2alpha(2alpha-1), strictly between 2 and 6. No nonnegative integer l has that value. Reality follows from the conjugate symmetry of the real source. The gradient formula follows by radial and tangential differentiation. This proves identity 3 for the homogeneous pressure.

For the regular representation, replace r by sqrt(r^2+R0^2) in radial envelopes and the twist, use the compactified Chebyshev argument tending to one with a differentiated O(r^-1) error, and allow a finite nonnegative power of r^2/(r^2+R1^2), where R1 > 0, on B,D,E. Every such damping factor is 1+O(r^-2) with differentiated bounds. Thus the regular B,D velocity is U1+O(r^(-beta-1)), with the corresponding derivative bound. The regular A,C terms have powers r^(-alpha-j), j a nonnegative integer, because their envelopes, logarithms and finite Chebyshev polynomials admit convergent expansions in 1/r near zero. No positive integer j equals alpha+1 in (2,5/2), so no regular A,C correction has velocity rate beta. The E channels have velocity rates l+2+j, l>=2 and j>=0, so all are at least four. Contributions to advection involving a subleading field have rates strictly larger than beta. Under the stated pressure-gradient remainder, pressure contributes only grad P0 at rate beta. Since the linear contribution at that rate is -U1, the coefficient of the residual is Greq-G. Proving the full-space pressure remainder is a separate analytical task; it is not inferred from a quadrature computation here.

For identity 4, on the unit sphere write the constant-phase-rotated toroidal and poloidal amplitudes as tau and sigma. Their vector components are

    toroidal: -n cross grad_S tau,
    poloidal radial: -n Delta_S sigma,
    poloidal tangential: grad_S[(2-beta)sigma + kappa partial_phi sigma].

The poloidal formulas follow by differentiating curl curl(Sy) = 2 grad S + (D^2 S)y - y Delta S. Radial and tangential vectors are orthogonal pointwise. Every tangential gradient is orthogonal in surface L2 to every surface-rotated gradient: integrate their product by parts and use that the surface divergence of n cross grad_S tau is zero. Thus the toroidal and poloidal contributions have no integrated cross term. Harmonic orthogonality gives the l(l+1) factors. On a real m pair, partial_phi is skew-adjoint and its square is -m^2 times the identity, so its cross term with sigma integrates to zero. The constant phase -kappa log R0 rotates each real pair orthogonally, preserving the sum of their squares. These facts prove the displayed norm formula, including its factor 2-beta.

The energy formula is the cross term in |U0+U1|^2. For helicity, use

    div(U0 cross U1) = U1 dot curl U0 - U0 dot curl U1.

The vector U0 cross U1 has rotating homogeneity degree -(alpha+beta) = -(3alpha+1). On a sphere, the integral of its tangential divergence is zero, as is the azimuthal derivative introduced by the rotating coordinates. Consequently the sphere integral of its divergence at r=1 is (2-alpha-beta) integral n dot(F cross G) dS, which equals (1-3alpha) times that flux. Rearranging the vector identity gives statement 5. This argument is a surface calculation away from the origin; no divergence theorem through the singular homogeneous origin is used.

## Evaluation without large-radius subtraction

An auxiliary exterior A,C evaluator can produce U1 exactly at the level of the formulas: replace c by c/2, omega by omega/2, A by B and C by D. Then alpha_aux = (1-c/2)/(c/2) = beta and kappa_aux = kappa. This is an algebraic reuse of homogeneous potentials. The auxiliary parameter c/2 is outside the campaign's physical interval and is not a candidate profile or an optimizer input. It must never pass through a physical-input validator as a saved candidate. A direct Cartesian-jet implementation of T1 and S1 and the independent norm formula supply separate checks of this substitution.

The coefficient Greq depends on the homogeneous pressure P0, not on a pressure obtained by fitting the full field at an arbitrary finite radius. A small relative defect, if observed, tests only this asymptotic coefficient. Zero denominators in reported relative norms are undefined and must be recorded as null. Quadrature agreement is not a certified continuum error bound.

## Dependencies, provenance and scope

Read the field reconstruction and angular normalization proofs first, followed by the stable linear operator proof and this result. Relevant local files are research/field_reconstruction/PROOF.md, research/normalized_angular_recurrence/PROOF.md and research/stable_linear_operator/PROOF.md. The frozen campaign's derivation at RUN_ROOT/frozen_euler3/verifier/theory/primary_first_correction/PROOF.md and its far-helicity coefficient derivation were read and checked against the present conventions. The pressure-remainder implication is deliberately conditional in this version. There are no Lean sources or formal proof claims. Numerical evidence and source bindings belong in verification/ and the associated artifacts. The proof neither constructs an Euler solution nor proves a degree-six obstruction for all coefficients.
