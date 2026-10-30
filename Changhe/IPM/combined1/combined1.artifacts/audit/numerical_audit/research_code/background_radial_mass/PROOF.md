# Exact radial localization of the background commutator bound

## Statement and data

Let rho be a smooth real S1 density obtained from a finite exact rational campaign potential at fixed c>1. Let delta=1-1/c. Assume the second Cartesian derivatives have the exact finite representation

    partial^alpha rho = r sum_(ell,n) v^(1+ell delta/2)
                              P_(alpha,ell,n)(t) T_n(theta),
    v=(1+r²)^(-1), t=1-v, |alpha|=2,

where T_n is sine or cosine and P is a rational polynomial. Derive these polynomials by the exact Cartesian rules in ../whole_plane_norms/PROOF.md, with rho as the input instead of F. Assume the endpoint tests there establish integrability of the second derivatives. Define

    X(A)=integral_A (rho_xx²+rho_xy²) dX,
    Y(A)=integral_A (rho_xy²+rho_yy²) dX,
    K(A)=[(log2-1/2)X(A)+(3log2-2)Y(A)]/(16pi).

Both coefficients are positive, so K is a nonnegative additive measure on radial regions. The squared structured Hilbert-Schmidt bound in ../gradient_commutator/PROOF.md is K(R²). This topic only localizes that established formula; it does not assert a new operator identity.

For rational 0<r0<R, the exact full-plane K equals the sum of its contributions from r<r0, r0<=r<=R and r>R. Outward intervals for these three quantities distinguish truncation of the spatial domain from error in numerical quadrature on that domain. The comparison refers to the exact rational candidate, not the function obtained by independently rounding each coefficient to binary64.

## Finite antiderivatives

For each derivative and angular mode, set Q(v)=P(1-v), extract its exact vanishing order q at v=0 and write Q=v^q W. Angular orthogonality makes every unequal mode product zero. For equal modes, diagonal branch products occur once and distinct branch products twice. The cosine-zero mode has angular norm squared2pi; all nonzero sine or cosine modes have norm squaredpi.

The polar Jacobian gives r³ v² dr=-(1-v)dv/(2v). Consequently the contribution of a branch pair ell,ell' to the squared derivative integral is

    (pi/2) integral v^e (1-v) W(v)W'(v) dv,
    e=-1+(ell+ell')delta/2+q+q'.

Include the angular and branch multiplicities before summing. Each diagonal exponent is greater than-1 by hypothesis, and a cross exponent is the average of its two diagonal exponents. Thus every separated term is integrable. Grouping equal e gives a finite polynomial H_e(v)=sum_k h_(e,k)v^k for X or Y.

For U=(1+R²)^(-1), the exterior mass is exactly

    X(r>R)=(pi/2) sum_(e,k) h_(e,k) U^(e+k+1)/(e+k+1),

and likewise for Y. At R=0, U=1 and the sum is an exact rational times pi/2. Subtracting exterior masses gives the other two regions. Keep all signed polynomial coefficients in the calculation; dropping negative terms would destroy the identity. Every final squared mass must have a positive lower enclosure and their sum must overlap the full value.

## Numerical checks and interpretation

The implementation reconstructs all second derivatives, checks mixed derivative commutation and compares the full rational X and Y energies with the existing full-plane background record. It evaluates the complete finite antiderivatives with1536-bit ball arithmetic at r0=1/50 and the exact binary64 value of the launch argument8356.474846731926, whose original shell text is frozen under source/. This reproduces the mathematical cutoff specified by that argument. The actual floating mesh may stop before the cutoff and does not integrate the endpoints exactly.

The reported floating kappa is a diagnostic, not an enclosure. Differences between it and the exact finite-domain value can include grid truncation at selected nodes, quadrature error and floating evaluation error. A close numerical agreement by itself does not isolate those effects or certify the floating diagnostic. No full-plane margin should use a truncated kappa unless the omitted nonnegative contributions are included.
