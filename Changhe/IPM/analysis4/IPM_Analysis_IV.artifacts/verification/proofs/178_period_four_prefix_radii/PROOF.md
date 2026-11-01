# Sufficient radii from the period-four prefixes

Status: PROVED sufficient radii, V340. All 30 exact supersolutions pass.

## Statement

Let delta=1/2 and c=2. In increasing order, let b_1,...,b_6 be the six real roots of the degree-eight compatibility polynomial isolated in142. Set f_1=sin(theta)+b_i sin(3theta). Use the unique tuned pure density and stream series of131, with all-index response lower bound s_i from143. The first free stream harmonic occurs at order8. The independent enclosure177 contains the exact density coefficients through40 and the harmonics H_8,H_12,...,H_40.

Choose N in {8,16,24,32,40}. Let d_j>j||f_j||_1 be rational upper bounds obtained from those enclosures, and let e_1=0 and e_a>aQ|H_(aQ)| for2<=a<N/Q, where Q=4. Form the finite-prefix residue system175 with

    B=4, L=12/11, kappa_N=8(N+1)/N.

If its transformed nonnegative polynomial map satisfies b>=Y0 and G(2^(-q),b)<=b for a rational vector b, then the density, stream and their common potential converge absolutely and uniformly, with every appropriately weighted spatial derivative, on every closed exterior

    r>=R>2^(q/2).

For leading amplitude epsilon, multiply this sufficient radius by |epsilon|^2. The conclusion is an exterior stationary solution. It does not claim the smallest possible radius or a global stationary extension.

## Proof and numerical boundary

The enclosure proof177 propagates the exact algebraic root interval through each signed Cartesian product, derivative, Poisson inverse and tuning step without resetting midpoints. Its coefficients and harmonics therefore enclose the same unique tuned series used in131. Taking interval absolute values, summing, multiplying by the order, and rounding the resulting exact dyadic upper endpoint strictly upward produces valid d_j and e_a. At order4 there is no positive-frequency free harmonic, so e_1 is exactly zero. The final H_N is not needed by the prefix map and is omitted from its input.

The hypotheses of175 now hold: N is a multiple of4 at least8, B=4 bounds the angular carrier, and the response lower bound has been proved for every resonance in143. Substitution of delta=1/2 into the nonlinear bound in175 gives kappa_N=8(N+1)/N. The Poisson column bound169 gives L=3*4^2/[4(3*4-1)]=12/11. No asymptotic fit or high-order numerical estimate enters these constants.

The scalar sums indexed by total order and the projected polynomial system are compared using exact rational coefficients. Approximate iterations may suggest the rational vector b, but admission requires every component of the complete exact inequality. Once that inequality holds, the monotone formal iteration proof175 gives absolute summability at w=2^(-q). The density base is w^(-1/4), and delta=1/2 converts this to the radius w^(-1/2)=2^(q/2). The strict radius absorbs every fixed polynomial factor coming from derivatives. The potential has only the finite logarithmic corrections at orders4 and8, as proved in132, and the same strict exterior suffices. Homogeneity gives the amplitude factor |epsilon|^2.

A failed search is not a proof that no supersolution exists. Each output records the complete rational box and image, source hashes, exact norm bounds, check counts, and actual runtime.

## Completed certificates at 2026-10-31T13:19:15+00:00

All30prefix boxes pass720direct scalar coefficient identities and240componentwise retained-inequality checks. The best adaptive q values for roots1 through6 are41,46,48,48,46,47, first attained at N24,32,24,16,16,16. Their sufficient exterior radii are respectively2^(41/2),2^23,2^24,2^24,2^23,2^(47/2), with amplitude factor |epsilon|^2. The successful computation took11.31357939215377seconds. The first attempt's decoder mismatch occurred before arithmetic and is retained in verification/first_attempt. No numerical estimate of an optimal radius is made.
