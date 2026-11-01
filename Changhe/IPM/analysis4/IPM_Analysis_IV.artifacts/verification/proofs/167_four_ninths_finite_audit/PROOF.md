# Independent finite recursion at four ninths

Status: completed independent finite audit through order90 at3072 bits, confirmed in V324.

## Statement and exact data

Let delta=4/9, c=9/5 and p_n=1-4n/9. Let b be one of the five real roots of the primitive obstruction polynomial in topic146, with its specified rational isolating interval. Set f_1=sin(theta)+b sin(3 theta). The tuned pure series uses the free coefficient H_(9k) of sin((4k-2) theta) in g_(9k) to cancel the density obstruction at order9(k+1). Topic145 and topic149 prove that these choices exist uniquely and give a convergent exterior series. This audit concerns the finite coefficients produced by the numerical experiments for those same choices.

For a requested order N, the calculation below independently constructs every coefficient through N and compares it with a frozen numerical prefix. Its claims are interval enclosures, finite coefficient agreement, and the stated finite norm values. It does not improve the conservative infinite convergence radius.

## Cartesian recurrence

Represent a homogeneous angular field by a signed Laurent polynomial. The positive coefficient at frequency m is half its sine amplitude, and the negative coefficient is its negative. With this convention the physical sine field differs from the Laurent field by the common factor i. For a term of radial degree d and Laurent frequency m, the x derivative contributes (d+m)/2 at m-1 and (d-m)/2 at m+1. The y derivative, after removing its factor i, contributes the first quantity at m-1 and the negative of the second at m+1.

Consequently the Cartesian advection polynomial is G_x F_y-G_y F_x, and the Poisson residual is -G_xx+G_yy-F_x in this convention. These identities follow by writing x and y derivatives in polar coordinates and differentiating each exponential. Their signs were also checked against the original potential equation in topics01 and84.

For n>=2, form every ordered product with i+j=n and divide their sum by (4/5)(n-1). The result is f_n. To construct g_n, differentiate f_n in x and divide each even-frequency coefficient by m^2-(p_n+1)^2. The denominator vanishes exactly at n=9k, m=4k-2. At these orders the forcing vanishes if and only if the sine coefficient of f_n at m-1 vanishes: the other density term in the forcing has the factor p_n+1+m=0. Projecting that known zero coefficient to exact zero preserves its enclosure and avoids feeding interval width into a singular division.

## Independent determination of free harmonics

At n=9k, continue the entire Cartesian recurrence provisionally to order n+9 twice, once with H_n=0 and once with H_n=1. Call the two obstruction coefficients R and R+S. There can be no quadratic dependence on H_n through order n+9. A density depending on H_n first appears at n+1, so two dependent factors first interact at 2n+1>n+9. At n=9 the pair (n,n) still has an H_n-independent density factor. Thus the obstruction is exactly affine, R+H_n S. If the interval for S excludes zero, H_n=-R/S encloses the unique tuned value. Induction, beginning with the exact algebraic leading root, encloses every subsequent coefficient.

The source implementation instead propagates the linear response explicitly. Agreement of both methods checks indexing, ordered convolution factors, resonant frequencies, and signs without copying that response update. Each independent Poisson inversion is additionally substituted into its Cartesian equation.

## Root and source checks

Refine the isolating interval using exact rational bisection, maintaining opposite polynomial signs at the endpoints. The unique real root remains in every refined interval. Confirm that the source's leading coefficient ball contains that interval and that its first sine coefficient is exactly one. Confirm the exact polynomial coefficients, delta, source precision, and all free harmonics through the selected prefix. Retain only a source prefix lying at least nine orders below its last computed order, to exclude an open final resonance.

Every retained source coefficient must overlap the independent enclosure. The finite Fourier l1 norms are sums of absolute values of these intervals; nth-root values are evaluated with outward-rounded logarithms and exponentials. Small residual balls or interval overlaps alone are not uniqueness proofs. The affine induction above and the already proved nonvanishing responses supply that mathematical identification.

## Evidence and scope

Sources, exact root intervals, counts, selected source archives, independent coefficients, free harmonics, norms, precision, and actual run times are written under this topic. A frozen source hash identifies the larger checkpoint even when only the selected prefix is archived. No infinite growth constant is inferred from a finite root test. The potential reconstruction and all-order existence are supplied by topics145,146,149 and150, independently of these finite numerical checks.

## Completed largest-root audit

The3072-bit replay completed all coefficients through90 and all ten harmonic tunings. Its8190 density and8280 stream comparisons with the independent1024-bit numerical source pass. The Cartesian implementation also checks111150 Poisson coefficients and13635 ordered products. At order90 the density and stream norm roots are9.50505833071390869957 and9.69207456414919251715. The recorded internal relative norm radii are below2.177e-510 and1.482e-417; the65-digit textual exports include their own wider printing enclosures. The run took383.6160368360579 seconds.

The1536-bit attempt could not resolve its response subtraction at order90 and remains retained as a precision-limit example. The successful replay uses the same algorithm at higher precision and the same selected source archive. The finite audit confirms the given prefix; all-order conclusions must use a separate majorant theorem and a uniform response certificate.

## Exact-prefix guarantee for the later majorant

The successful3072-bit run propagates the exact algebraic root enclosure through every coefficient and all ten harmonic computations without replacing any interval by a midpoint. At a compatibility coefficient, exact zero is justified by the first polynomial identity or by the preceding exact affine tuning, before projection. The induction in the harmonic section therefore proves that every retained enclosure contains the exact tuned coefficient, rather than merely a coefficient of a midpoint-initialized recurrence. In172 only H9 throughH81 are used with the density prefix through90; H90 is the first unknown in that majorant. Thus all nine required known harmonics are certified by this run.
