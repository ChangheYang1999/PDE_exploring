# Independent interval prefixes at delta = 3/5

Status: PROVED finite enclosure procedure after independent theory-part review, V439. All four roots have independently enclosed coefficients and common potentials through40.

## Statement and hypotheses

Set delta=3/5, c=5/2 and p_n=1-3n/5. Let b be one of the four real roots, in increasing order, of the exact degree-ten compatibility polynomial certified in topic200. Start with f_1(theta)=sin(theta)+b sin(3theta). Stream resonances occur at n=10k and frequency6k-2; their density compatibility coordinate has frequency6k-3.

The finite target is to enclose the uniquely tuned coefficients f_n and g_n for1<=n<=40, including the harmonic H40 fixed by compatibility at50. Each computed tuning response must exclude zero. The intended independent comparison is with the numerical experiments' separately implemented polar recurrence. Any extracted source norms at larger orders remain explicitly source-bound until a separate enclosure audit is supplied.

## Exact finite construction and proof

Refine each rational isolating interval from200 by exact sign-preserving bisection. Simplicity and uniqueness of its root follow from the Sturm certificate. Enclose the resulting rational interval with directed ball arithmetic, without replacing it by its midpoint.

Represent each angular sine polynomial as a signed Laurent polynomial, with its homogeneous radial degree stored separately. The Cartesian derivative identities proved in topic01 act on every term. Ordinary Laurent multiplication then forms the velocity-density advection. Division by (n-1)(c-1)=3(n-1)/2 gives the next density coefficient. The stream equation is inverted on its nonresonant Fourier coordinates. Direct Cartesian second differentiation checks every resulting Poisson equation.

At n=10, the polynomial identity proves that the obstructed density coordinate is exactly zero. Its computed ball must contain zero before this coordinate is projected to the exact value zero. At each later resonance, the previous tuning step proves the same fact. Other projected zeros follow from the proved odd/even sine symmetries and the frequency bound4n-1 for density,4n for stream; their balls are checked before projection.

At a resonant n, continue provisionally through n+10 with H_n=0 and H_n=1. A product with two affected factors first appears at order2n+1, which exceeds n+10 for n>=10. The target obstruction is therefore affine in H_n. The difference between the two provisional obstructions encloses its exact response sigma_n. If that ball excludes zero, H_n=-R_n/sigma_n encloses the unique harmonic that cancels the next obstruction. This argument is finite and does not require the all-index result in200. Induction proves all retained interval enclosures through40, and includes the look-ahead needed for H40.

For comparison, require every source coefficient through40 to overlap its independent Cartesian enclosure, every source harmonic and response to overlap the independently computed values, and the exact parameter and root to agree. Coefficient overlap is an agreement test; the enclosure guarantee comes from the preceding directed construction, not from overlap alone.

## Norms, evidence and limitations

The sum of directed absolute values encloses the angular sine-coefficient l1 norm. Positive norms may be logged, divided by their order and exponentiated to enclose order roots. These finite quantities do not estimate a limiting growth constant without a separate argument. A final source stream harmonic is omitted when the producer has not yet tuned it.

Source hashes identify the exact checkpoint and harmonic table read. Selected source coefficients, independent prefix norms, all harmonic enclosures, operation counts, code snapshots and actual computation times are retained beside this proof. The finite result concerns the exterior density and stream series. The common-potential reconstruction and all weighted derivatives are consequences of the separately proved rational theorem when its full hypotheses are established.

## Independent common-potential reconstruction

For each enclosed pair, put q=p_n+1 and t=p_n+3. Write Delta chi_n=r^q sum_k D_k cos(2k theta). If a_k is the density coefficient of sin((2k+1)theta), direct differentiation gives

    a_k = (2k-q)D_k/2 + (q+2k+2)D_(k+1)/2,  k>=1,
    a_0 = -q D_0 + (q+2)D_1/2.

At delta3/5, q is never zero and never a positive even integer. Descending substitution therefore determines every D_k uniquely. The potential coefficient C_k is D_k/[t^2-(2k)^2] except when that denominator vanishes.

This exception occurs precisely at n=10l, t=-m with m=6l-4>=2. The resonant stream frequency is m+2. The coefficient of that frequency in partial_x rho=-partial_xy(r^q sum D_k cos(2k theta)) is -(m+1)(m+2)D_(m/2); the other possible neighboring contributions vanish at q=-m-2. Stream compatibility therefore gives D_(m/2)=0. Omit that known zero before division, retaining the potential harmonic as free.

The difference between the resulting stream and the prescribed stream is harmonic. In the even sine class it vanishes at nonresonant orders and has only frequency m+2 at n=10l. Direct differentiation gives

    partial_xy[r^(-m) cos(m theta)]
      = m(m+1) r^(-m-2) sin((m+2)theta).

Thus a unique multiple of this harmonic potential matches the remaining stream coordinate. No logarithm is required because m>=2. This construction is independent at each order and preserves the same density.

The implementation forms these cosine Laurent polynomials in interval arithmetic and checks all coefficients in rho=-partial_y Delta chi and psi=partial_xy chi by Cartesian differentiation. In the signed Laurent representation used here, a sine field is -i times its stored field, whereas a cosine field is its stored field. Consequently the stored identities are F=Y(X^2-Y^2)C and G=-XYC. These identities provide a finite direct check against the original potential formulation.

## Root4 outcome, 2026-10-31T15:14:42+00:00, V418

At2048 bits, all1640 density and1680 stream source-coefficient comparisons pass, together with the four harmonic and response comparisons. The computation checks26040 Poisson coefficients and the common-potential identities on6680 density and6600 stream coefficients. Four resonant potential coordinates satisfy their required zero conditions. Runtime18.294 seconds. The independent prefix ends at40, including the harmonic fixed by compatibility at50. Source norms through300 remain separately labeled.

## 2026-10-31T15:21:33+00:00 completion

All four real roots pass the independently enclosed prefix and common-potential checks through40. Root2 completed in18.550 seconds, with1640 density and1680 stream comparisons,26040 Poisson coefficients,6680 potential-density coefficients,6600 potential-stream coefficients, and four resonant potential compatibility coordinates. Source samples above40 retain their separate source-bound scope.
