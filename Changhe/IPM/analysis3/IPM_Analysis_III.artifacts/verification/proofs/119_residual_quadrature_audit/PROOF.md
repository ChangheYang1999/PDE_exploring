# Independent audit of the residual quadrature

## Statement and scope

The theory author's files far_points_160.json and far_points_192.json contain directed pointwise energy densities. They do not contain interval bounds between the sampled radii. This audit verifies the arithmetic of the stated numerical quadrature and compares its point at t=33/4 with the independent original-data computation of proof 117. It does not certify the integral of the actual residual.

For positive endpoint densities f_0,f_1 on [t_0,t_1], the exponential interpolant is

 f(t)=f_0 exp(lambda(t-t_0)), lambda=log(f_1/f_0)/(t_1-t_0).

Its exact integral is (f_1-f_0)/lambda, with continuous value f_0(t_1-t_0) when lambda=0. A partial segment [a,b] has integral f_0 exp(lambda(a-t_0)) expm1(lambda(b-a))/lambda. These formulas follow by integrating the exponential. Summing them is a quadrature convention, not a theorem that the true density equals or is bounded by this interpolant.

The theory author's whole-segment quadrature is reproduced independently using exact interval midpoints converted to binary floats. The region split is also recomputed with the actual partial-segment formula. Assigning a proportion of a segment's total integral according to its length is generally inaccurate when the segment crosses a region boundary. It does not change the total quadrature, but it can change the quoted shares.

For the numerical tail convention, fit the rate from the t=30 and t=60 samples and integrate its extrapolation from t=20 to infinity. Proof 117 proves that the true limiting rate is 4k-5/4. It does not prove a finite-radius error bound for that extrapolation. Point samples at t=-10 and -40 do not provide an upper bound for the omitted interval t<0. Thus neither the interpolation, the omitted inner tail nor the extrapolated outer tail is a certified enclosure.

## Evidence

The code reads both theory author files without modifying them, checks their hashes and the overlap of the t=33/4 intervals with proof 117, recomputes the quadrature, and records full-resolution, every-other-point and trapezoidal variants. These variants measure sensitivity of the numerical convention only. A close agreement is not a rigorous quadrature error bound.
