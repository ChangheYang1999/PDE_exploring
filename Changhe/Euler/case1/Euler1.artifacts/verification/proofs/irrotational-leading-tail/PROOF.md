# A nonzero natural homogeneous tail cannot be irrotational

Date: 2026-10-23. Status: proved under the explicit homogeneous-tail hypotheses below. No formal verification is claimed.

## Statement and notation

Let -3/2 < d < -1 and let A be a smooth vector field on the entire unit sphere S². Define F(y)=|y|^d A(y/|y|) on R³ minus the origin. If div F=0 and curl F=0 there, then A=0.

Consequently, a nonzero leading velocity tail of the natural degree d=1-1/c for 2/5<c<1/2, with smooth global angular coefficients and differentiation-compatible asymptotics, cannot have zero leading curl. This result does not exclude a nonzero vortical leading tail, a different decay class, angular singular limits, or an approximation on a finite set of rays.

## Proof

The vector identity ΔF=grad(div F)-curl(curl F) gives ΔF=0 componentwise. For each Cartesian component, write F_i(Rn)=R^d a_i(n). The spherical Laplacian formula gives

    ΔF_i(Rn)=R^(d-2) [d(d+1)a_i(n)+Δ_S a_i(n)].

Thus -Δ_S a_i=λ a_i with λ=d(d+1). In the stated range, 0<λ<3/4.

There is no nonzero scalar eigenfunction of -Δ_S with eigenvalue strictly between 0 and 2. One short proof uses the integrated Bochner identity on the unit sphere:

    integral (Δ_S a)^2 = integral |Hess_S a|² + integral |grad_S a|².

To obtain this identity, differentiate |grad a|²/2, commute one covariant derivative, use Ric_S=g_S, and integrate the resulting Laplacian and divergence terms over the closed sphere. In two dimensions, Cauchy-Schwarz applied to the eigenvalues of Hess a gives |Hess a|² >= (Δa)²/2. Therefore

    integral (Δa)^2 >= 2 integral |grad a|².

For an eigenfunction of eigenvalue λ, integration by parts gives integral |grad a|²=λ integral a² and integral (Δa)²=λ² integral a². A nonzero eigenfunction with λ>0 must therefore satisfy λ>=2. Our value λ<3/4 is impossible. Hence each a_i vanishes, which proves A=0.

## Application to an actual asymptotic expansion

Suppose a divergence-free smooth field U satisfies R^(-d) U(Rn) -> A(n), with enough angular and radial derivative convergence to pass div and curl to the leading homogeneous field. Divergence implies div F=0. If the leading curl were zero, the theorem would force A=0, contradicting a nonzero leading term. Decay of U alone without derivative convergence does not justify passing those operators to the limit.

This is independent of Chae's small-p integrability theorem. Correcting Chae's hypothesis does not make a smooth, nonzero, irrotational homogeneous tail of this noninteger degree possible.

Dependencies: the Cartesian vector Laplacian identity; the spherical-coordinate Laplacian; integration by parts on the closed unit sphere and the differentiated Bochner identity explained above. No numerical experiment is used in this proof.
