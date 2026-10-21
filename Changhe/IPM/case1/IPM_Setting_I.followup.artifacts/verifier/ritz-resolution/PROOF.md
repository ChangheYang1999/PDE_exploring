# Two-grid restricted action matrices and physical transport derivatives

Date: 2026-10-20. Status: finite-data audit and independently evaluated physical derivatives. No continuum spectral theorem is claimed.

## Measured matrix statement

At each saved parameter vector z, let Q have24 orthonormal columns in the unscaled Euclidean norm of density nodes, c_l and auxiliary C. Let the supplied columns D_j be the centered residual differences at step h=1e-4 along Q_j. Compute D=USV^T using independent linear algebra. The ascending singular values of D and parameter directions QV are intrinsic to this measured linear map. Column norms, the stored right directions, and their coordinate localization can be checked directly. Their signs are immaterial; align the signs before comparing coordinates. Node localization uses the actual compactification radius

    r(q)=L sqrt((1-q)^(-2/(1-1/c_l))-1),

with q=1 interpreted as infinity. The far fraction is the squared density-node norm at r>100 divided by the total squared parameter norm; it is not a spatial L2 fraction. C does not enter the reconstructed physical density.

If Q0 is a ten-dimensional source basis and Q0=QT exactly, the restriction of this measured24-column map is DT. This follows by multiplication. If Q0 is only approximately in the span, record the projection error; it does not certify a bound on the true derivative applied to the omitted component without an operator bound. Even when containment holds, recomputing a centered difference at finite h after rotating its direction need not give exactly DT. The scalar source summaries in the cross-grid files are a separate measurement. This audit does not invent a missing D0 array.

For a controlled error eta=||D-DF(z)Q||, minimax gives the standard restricted-singular-value perturbation bound eta. Without it, the small values are measured numbers. A step dependence resembling roundoff divided by h does not by itself certify either a roundoff floor or an upper bound for the exact derivative. Two grids and direction overlap do not establish a kernel or family; the exact instability counterexample is proved in ../crossgrid-actions/PROOF.md. The supplied PT files do not contain F(z), so their projection-of-F summaries remain metadata in this audit.

## Independent physical derivative

Write the reconstructed trial density as

    rho=x² y exp((k-3)ell/2) b(q,s),
    ell=log(1+r²/L²), k=1/c_l, q=1-exp(-(1-k)ell/2).

Here s is the inverse fixed angular map. Differentiate at a fixed physical point along a parameter vector (delta b,delta c_l,delta C). Ordinary chain and product rules give

    delta rho=x²y exp((k-3)ell/2)
      [delta b - delta c_l ell/(2c_l²) (b-(1-q)b_q)].

The auxiliary C has no direct physical-density contribution. The canonical inverse is linear, so delta U is its action on this full delta rho, including the c_l term. For

    R=(c_l X+U) dot grad rho-rho,

its derivative is

    delta R=delta c_l X dot grad rho
             +(c_l X+U) dot grad(delta rho)+delta U dot grad rho-delta rho.

This is an exact algebraic identity for a differentiable family for which the canonical inverse and parameter derivative commute. The finite polynomial trial family satisfies this condition on a small parameter interval: all its density variations grow as O(r^(k+epsilon) log r), with k+epsilon<1, and odd paired kernels give an integrable uniform tail. Local smoothness away from the center and source gives the usual local cancellation. No candidate-specific elliptic solver or residual code is needed for this calculation.

The implementation reconstructs delta b by an independent tensor DCT, evaluates spatial gradients by eighth-order Cartesian differences, and evaluates delta U with this lane's separate full-plane real-space inverse. The inverse is split into an origin-centered integral and a local principal-value integral, with odd pairing in the exterior and the required -rho e2/2 contact term. Several angular/radial resolutions and finite parameter perturbations check numerical differentiation and quadrature separately. The analytic identities are exact; floating-point quadrature values are not interval certificates.

Every physical action is reported both unnormalized and divided by the fixed base denominator |rho|+sum_i |(c_l X+U)_i rho_i|, which is the report's N_f. This is the derivative of the numerator in fixed base units, not the derivative of the absolute normalized ratio. Unit node norm is specified separately for each grid and should not be confused with a common function-space norm.

## Explicit tail bound for the derivative

For each finite direction let H be the ceiling of sqrt(2N(2M-1)), B and Bd the ceilings of the maximum base and direction nodal magnitudes, and epsilon=1/5-1/c_l>0. The independent DCT coefficient bound gives |b|<=HB and |delta b|<=HBd. The Markov polynomial inequality on q in[0,1] gives |b_q|<=2N²HB. For r>=1 and L=8, ell<=1+2log r and r^(-epsilon)ell<=1+2/epsilon. Hence the exact sufficient envelope is

    |delta rho| <= C_delta r^(1/5),
    C_delta=512 H [Bd+|delta c_l| B(1+2N²)(1+2/epsilon)/(2c_l²)].

Apply the odd exterior bound proved in exterior-tail/PROOF.md: beyond radius T, for |X|<=R0<T, each velocity error is bounded by (5C_delta/2)R0 T^(-4/5)/(1-(R0/T)²)². The base has C_base=512HB. The resulting linearized residual tail is bounded by delta-U error times |grad rho|_1 plus base-U error times |grad delta rho|_1. All envelope constants are computed as exact rational numbers from the saved binary inputs. This controls the omitted exterior, not the interior quadrature or its lower radial cutoff.

## Scope

Nonzero sampled physical derivatives show that particular directions of the measured orbit-map system are not exact physical transport null directions for the saved field. The base field itself has nonzero residual. Neither a small nor a large action on a few points establishes injectivity, a Fredholm index, the conditioning of the full continuum problem, or a nonlinear branch. Exact strong-center compatibility and the endpoint tests remain separate and fail for these saved finite representations as shown in grid-states/PROOF.md.
