# Audit of the N40 M36 finite smooth approximation

Verifier result148. Prelaunch protocol: ../smooth_N36_refinement_audit/N40_PROTOCOL.md. This standalone audit concerns one frozen finite formula and a controlled finite comparison with N36 M32. It is not an existence proof.

Fix ell=5/2, length L=1, and alpha equal to the exact binary value computed from the saved exponent by alpha=(1-p_saved)/2. With w=(1+r^2)^(-alpha), sigma=r^2/(1+r^2), t=1-2w, the density is

    rho=y w sum_(k=0)^35 sigma^k B_k(t) cos(2k theta),
    B_k(t)=sum_(j=0)^40 z_kj T_j(t).

The stored binary coefficients z are interpreted as exact rationals. The factor sigma^k cos(2k theta) is Re((x+iy)^(2k))/(1+r^2)^k, so this is smooth everywhere, even in x and odd in y, with no singular angular definition at the origin. Its growth is sublinear. The canonical full-plane inverse solves -Delta psi=rho_x with U=(-psi_y,psi_x)=o(r), odd stream parity and no added harmonic strain. The inverse formula and gauge uniqueness are in ../inverse/PROOF.md, and the finite modal source integrals are in ../smooth_full_inverse_primitives/PROOF.md. All evaluations reconstruct the frozen density, not the optimizer's interpolated velocity.

The exact center slope a=B_0(-1), canonical strain c and all Taylor coefficients to degree11 are computed by the independent rational density-moment formula of ../smooth_canonical_high_jets/PROOF.md. The identity R_y(0)=a(ell+c-1) follows by differentiating R=(ell X+U).grad rho-rho at zero, using rho(0)=0, grad rho(0)=(0,a), U(0)=0, U2_y(0)=c. Thus a nonzero exact value disproves exactness of this finite formula, without giving a lower bound on distance to any exact profile. Its actual y-axis amplitude K=sum_k(-1)^k B_k(1) is evaluated separately from the stored coefficients; the solve projects c=1-ell and K=a in floating arithmetic, so exact equality is not presumed.

The residual denominators are N_f=|(ell x+U1)rho_x|+|(ell y+U2)rho_y|+|rho| and N_v=|rho|+|x rho_x+y rho_y|+|U.grad rho|. Undefined ratios at a zero denominator remain undefined. Wide polar grids, refined local grids and complementary angular charts identify finitely many points for high precision checks; these are observed maxima, not uniform bounds. Independent Cartesian kernel quadrature with centered eighth-order differences uses the same physical points and three step sizes. If dU=Uhat-U, dg=ghat-grad rho and dr=rhohat-rho, direct expansion gives

    Rhat-R=dU.grad rho+(ell X+Uhat).dg-dr.

This exact identity separates velocity error from derivative error. In particular, step convergence does not cure cancellation in U2 near the horizontal axis. A disagreement there must be reported even if both normalized values are small. Any targeted parity correction would require a separate recorded evaluation; none is assumed in this protocol.

At large radius the exact saved p=1-2alpha is retained, including ell p-1. Its leading residual is (ell p-1)r^p Theta_0, followed by the nonlinear correction of degree2p-1. A large absolute residual at an enormous radius due to this exponent defect does not exclude a separately defined field with p=1/ell exactly. Such fields, if studied, are distinct data in result164.

The N36 and N40 solves use the same frozen N24 seed, coefficient transfer, ell, length, density-moment inverse order108, jet weight/scale and1000 function evaluations. They differ in radial/angular dimensions and the prescribed training grid. Comparing their outputs is controlled at this finite protocol level, but a fixed evaluation budget does not ensure comparable stationarity or convergence of either solve. Older sizes used a different inverse implementation and are not resolution-only comparisons. Changes of a and center derivatives, canonical residuals and the location of their peaks must be reported. A finite-angular nonzero exact solution is independently excluded by ../finite_angular/PROOF.md, but increasing-M approximation remains possible.

Verdicts distinguish verified finite evaluations from unresolved stationarity, three-resolution/domain stability and a primary endpoint. No fixed absolute1e-6 cutoff or rigorous uniform certificate is imposed as an extra prompt condition. Absolute residuals and their interpretation are still reported. These finite experiments alone do not justify ending the run.
