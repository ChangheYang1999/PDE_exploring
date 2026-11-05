# Independent review of the cubic Riesz-residual coordinate

Status: analytic method and complete saved assembly reviewed successfully. This is one coordinate of the original-N residual, not an existence theorem or a Q-norm residual certificate.

Reviewed producers: `coercivity_residual/certify_source_projection.py`, `source_projections013.py`, and the frozen exact-source evaluator. The separate `ROOT_CUBIC_SOURCE_REASSEMBLY.json` verifies the hashes, the complete disjoint index set 0 through584, exact rational endpoint coverage, the sum of all saved Arb integrals and errors, and containment in the published coordinate interval.

For width a=3/200, the test psi=(2-r²/a²)y exp(-r²/(2a²))/(sqrt(pi)a²) has norm one: its squared norm is one half of the integral of s(2-s)²exp(-s), namely1. The oscillator identity gives J²psi=(1+(8-s)/a²)psi. The vector Riesz transform is an L2 isometry and q-1/10=2, so the exact coordinate is <R Jq(WF),R J^-0.1 psi>=<WF,J²psi>. Thus no pointwise replacement of a Riesz transform occurs.

Angular orthogonality reduces the last integral to the exact sine-one coefficient of F=(cX+u)·grad(rho)-rho. The product-to-sum code retains the signs of positive and negative sine modes and uses exact coefficients0 and±1/2. The separate absolute-coefficient majorant is valid on each complex radial disk. The frozen evaluator encloses every Cartesian derivative of the potential used here.

On the disk |z-r|<=r/8, Re(z²)>=(7r/8)²>3r²/4. Therefore the producer's Gaussian bound exp(-3r²/(8a²)) is valid. The W factor has its analytic branch in the right half-plane and modulus at most sqrt(1+4(r+r/8)²). All remaining polynomial factors use the triangle inequality on the same disk. Integrating the even Taylor coefficients exactly and charging 2h M(h/R)^(d+1)/(1-h/R) consequently bounds the entire core integral, including its analytic Taylor tail.

On either omitted radial region, Cauchy-Schwarz charges the inherited whole-plane ||F||2 upper against ||W J²psi||2 on that region. With s=r²/a², the squared test norm has exact density s(1+4a²s)(2-s)²(1+(8-s)/a²)²exp(-s)/2. The incomplete-Gamma polynomial computation is exactly this integral; cancellation is enclosed by Arb, and both tail squares are positive. No weighted residual norm is substituted for the unweighted one.

The resulting coordinate is contained in [-0.000402408±1.79e-10]. The core Taylor error is below5.273e-12 and the combined endpoint error below1.268e-10. These are useful actual data for a Bessel/finite-matrix dual estimate. The matrix inverse Gram and all linear-energy closure obligations remain separate.
