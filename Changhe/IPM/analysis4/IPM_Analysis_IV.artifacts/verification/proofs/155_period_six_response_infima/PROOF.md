# Response infima and sufficient radii at delta = 1/3

Status: PROVED. Every exact finite/tail certificate and all seven rational majorant boxes pass in V303.

## Statement

Use the six real roots b_1 < ... < b_6 of P12 from154, the normalization f_1 = sin(theta) + b_i sin(3 theta), and the responses sigma_k defined there for k >= 2. The claimed infimum of |sigma_k| occurs uniquely at k = 6,5,6,6 for roots1,2,3,6, respectively. At roots4 and5 the infimum equals |sigma_infinity| and is attained at no finite integer k.

The proposed rational lower bounds, in root order, are

    s = (434/25, 87/500000, 309/1000000, 29/20000, 189/10000, 483/1000).

The corresponding upper bounds for 1+|b_i| are

    a = (161/100, 109/100, 23/20, 6/5, 32/25, 38/25).

For the majorant of131, these imply strict sufficient radii

    R > (2^180, 2^219, 2^219, 2^213, 2^204, 2^195)

for the respective unit-amplitude profiles. The common bound is R > 2^231. Under amplitude epsilon != 0, multiply each radius by |epsilon|^3. These bounds are sufficient and are not claims about the exact convergence radius.

## Infimum proof

Let sigma_k(b) = N(k,b)/D(k) be the independently computed rational tail from154. Normalize the sign so that D has positive leading coefficient. Expand at k = 13+t. Verify every coefficient of D(13+t) is positive. For a fixed root interval I_i, let A_i(b) be the absolute value of the claimed minimizing response, represented as the appropriate signed polynomial in b. At roots4 and5 use the signed limiting polynomial instead. Prove its positivity on I_i and its strict lower bound s_i by rational interval Horner evaluation.

Let e_i be the sign of the limiting response at b_i. Check every coefficient in t of

    e_i N(13+t,b) - D(13+t) A_i(b)

is nonnegative on I_i and that the constant coefficient is strictly positive. The polynomial is then strictly positive for every real t >= 0. Consequently the signed tail response exceeds A_i, so its absolute value exceeds A_i as well. When A_i is the limiting polynomial, the highest coefficient cancels exactly; test this algebraic zero before interval evaluation. It does not affect strict positivity for finite t.

For k = 2,...,12, evaluate each response by its independently computed finite polynomial. Its absolute value must exceed the upper endpoint of the A_i interval, except at the asserted unique finite minimizer. This proves the stated infimum and uniqueness or nonattainment. If shift13 does not certify coefficient positivity, a later exact shift is allowed only after checking every newly omitted integer separately.

## Majorant proof

Set Q = 6, B = 4, L = Q/2 = 3 and kappa = B(Q-2)(3-2/Q) = 128/3. The positive polynomial map Phi is the one proved in131 and implemented independently in code/general_component_radius.py. With its affine part Phi(0,Y) = c+JY, let T = (I-J)^(-1), Y0 = Tc and

    G(z,Y) = Y0 + T[Phi(z,Y)-Phi(0,Y)].

Strict lower triangularity of J makes T a finite nonnegative matrix sum. Evaluate G at the componentwise box Y = 2Y0 and z = 2^(-q), with q = 60,73,73,71,68,65. If G(z,Y) < Y in every coordinate, positive iteration gives a finite majorant at z and hence the stated coefficient bound. Since the physical variable is r^(-1/3), any R > z^(-3) = 2^(3q) lies strictly inside the resulting exterior convergence domain. Every derivative is justified by a strict radius margin and the finite Fourier support, as in131/132.

The same construction with a = 161/100, s = 87/500000 and q = 77 gives the common radius. Checking failure at the immediately preceding dyadic point describes this particular box test only; it cannot prove that a smaller physical radius is impossible.

## Evidence and dependencies

Exact inputs are154's independently generated rational responses and root intervals. Save all finite gaps, shifted coefficient intervals, rational matrices, box values and positive margins. The infimum proof depends on the exact tail identity in154. The analytic conclusion uses131 and132. No empirical root test is used.

## Completed verification

Every tail passes at the first shift13. The infima, in root order, are approximately17.36197658049,0.000174760998923,0.000309283615590,0.00145328950071,0.0189856985937,0.483508941290. Roots4 and5 approach their infimum only as k tends to infinity. The other four attain it at the single listed integer. The maximum majorant component ratios are below0.915,0.829,0.770,0.810,0.799,0.812, respectively. The common box also passes, and every preceding dyadic box fails. See verification/checks.json for exact rational inequalities and all input hashes.
