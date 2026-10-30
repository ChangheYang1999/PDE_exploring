# Exact origin Taylor audit of the saved candidate007

## Statement and conventions

Let chi be the potential defined by the2982 exact rational generators in C1-N1-007-d2w-j7-e2bal, raw SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21. Fix c=4076476460239181/2251799813685248 and define

 rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy),
 F=(cX+u).grad rho-rho, R_f=F/y.

The local function chi is real analytic and even in each coordinate; rho and F are even in x and odd in y. Thus R_f has a real analytic extension across y=0. All coefficients below are ordinary Taylor coefficients, without factorial factors. The constant coefficient of R_f is zero. Each of its five degree-two and degree-four coefficients has absolute value greater than2e-13. In particular

 2.0899e-11<[y^4]R_f<2.0900e-11.

This refutes the universal statement that every saved candidate satisfies these five Taylor equations to2e-13. It confirms N4-419's axis statement and the N1 referee's already disclosed counterexample. It concerns this exact saved rational potential, not an earlier floating projection or a different normalization. It changes neither the confirmed exact center relation nor the far-field cancellations or any sufficient-framework exclusion.

## Exact finite derivation

Set z=x^2+y^2, t=z/(1+z), gamma=1/c, delta=1-gamma and p_j=(3+gamma-j delta)/2. Write H_m=Re(x+iy)^(2m). A Legendre generator has the exact expansion

 a H_m sum_(h=0)^n (-1)^(n-h) binom(n,h)binom(n+h,h)
              z^(w+h)(1+z)^(p_j-m-w-h).

For a monomial generator the sum is its one saved radial power. Expanding the last factor by its rational binomial coefficients and retaining m+w+h+ell<=4 gives the exact potential Taylor polynomial through degree eight. Only60generators can contribute; every other generator has least degree at least ten.

To construct Cartesian coefficients, expand H_m by its even powers of y and expand each z^s by the ordinary binomial theorem. For an additional independent differential check, H_m is harmonic of degree2m, and

 Delta(H_m z^s)=4s(2m+s)H_m z^(s-1).

This follows either from polar differentiation or from the product rule, Euler's homogeneous identity and Delta z^s=4s^2 z^(s-1). Applying this identity to every truncated harmonic-radial term gives the same Laplacian coefficients as direct Cartesian differentiation. The checker uses this harmonic identity to construct rho and exact Cartesian derivatives to construct u.

No discarded term can affect the claim. A discarded even potential term has degree at least ten, so its third derivatives have degree at least seven. The nonzero terms of rho and u begin at degree one. Consequently a discarded contribution to u.grad rho has degree at least seven: either the velocity contribution has degree at least seven and the density gradient degree at least zero, or the density-gradient contribution has degree at least six and the velocity degree at least one. The drift and density terms preserve that cutoff. Hence F through degree five, and R_f through degree four, are determined by this finite potential polynomial.

For a polynomial sum a_ij x^i y^j, partial_x^p partial_y^q has coefficient a_ij times the two falling factorials at monomial x^(i-p)y^(j-q). The product coefficient is the finite convolution of the coefficient arrays. These exact rules produce rho, u and F through the required degrees. The checker verifies parity, the zero constant, all five strict tolerance failures and rational directed intervals. It also compares the axis potential, its x^2 coefficient, density, vertical velocity and residual with all saved exact N4-419 axis coefficients. No floating comparison establishes an inequality.

## Source binding, evidence and scope

The exact raw file is the immutable own-lane copy already used in the coefficient-rounding audit. N4-419's complete proof, program and result and the frozen numerical-report claim are copied as inert evidence. Their programs are read, not run. This audit implements finite rational polynomial arithmetic independently; it does not import any candidate evaluator. All derived polynomial coefficients and rational bounds are stored in JSON, with input hashes in the manifest. The original proof precedes the checker. Verification outputs record real execution times and every check. No field integral, optimization, PDE solver, Lean build, server or remote worker is used.
