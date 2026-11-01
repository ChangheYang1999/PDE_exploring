# Compatible two-mode profiles at delta=4/9

Status: PROVED existence of five tuned convergent exterior series. Exact algebraic and all-index response certificates are V282/V288; the theory part independently accepted the nonvanishing argument and convergence theorem145 at11:34Z, recorded in V299. Quantitative bounds149/150 have their separate review status.

## Exact objects and conclusion

Set delta=4/9,c=9/5and f_1=sin(theta)+b sin(3theta). Let O9(b) be the sin(theta)coefficient of f_9computed by the pure recurrence. This is the first stream compatibility condition, because the first positive even stream resonance is at n=9,frequency2. The exact O9and a separately computed limiting response polynomial are in144. Define P9as the primitive integer polynomial with positive leading coefficient proportional to O9.

The proposed conclusion is that every real root b_i of P9has inf_(k>=1)|sigma_k(b_i)|>0, where sigma_k is the nine-step response at base order9kand target density frequency4k+1. Together with145this gives a uniquely tuned convergent pure exterior series for each such profile. The radius would scale as |epsilon|^(9/4)under amplitude multiplication. All response premises have now been certified as recorded below. The convergence conclusion was independently reviewed at11:34Z.

## A two-coefficient nonvanishing criterion

The obstruction has degree9. Suppose P9is irreducible over Qand has nonzero constant and leading coefficients, denoted O_0and O_9when using the rational normalization O9. Each sigma_k(b)is a rational polynomial of degree at most9. If it vanished at a root of P9, irreducibility would force sigma_k to be a scalar multiple of O9, including the zero scalar.

Let a_k=sigma_k(0)be the response for leading profile sin(theta), and let d_k=[b^9]sigma_k(b). Homogeneity says d_k is the response for leading profile sin(3theta), with its amplitude set to1. Consequently a necessary condition for a response to vanish at any root is

    D_k=O_9 a_k-O_0 d_k=0.                                  (1)

Thus proving D_k!=0for every positive integer k excludes all response zeros at all obstruction roots, without computing the intermediate seven coefficients of sigma_k. This is a sufficient criterion, not an equivalence.

The direct carrier limit144computes sigma_infinity and proves its existence. If its gcd with P9is1, no obstruction root has zero limiting response. Combining this with(1)then gives the positive infimum by separating a sufficiently large tail from a finite initial set.

## Exact certificate plan and proof

Compute the two single-mode low prefixes through9by Cartesian Laurent differentiation. Their obstruction coefficients must equal O_0and O_9from the independent two-mode calculation. For each finite k=1,...,11, compute both nine-step responses directly, including folded and omitted zero modes, and form D_kexactly.

For k>=10all positive carrier frequencies exceed every possible response offset: the carrier is4k-2and the maximum offset through nine steps is4*9-1=35. The same signed Laurent recurrence with affine symbolic frequency4k-2therefore gives rational functions a(k),d(k), hence D(k). Direct comparisons at k=10,11give consistency checks but do not replace the derivation of all-kvalidity.

If a sign-normalized numerator of D(k)has nonnegative coefficients after k=K+t, with strictly positive constant, it has no zero for k>=K. Any remaining finite integers must be checked separately. Alternatively an exact rational-root certificate can exclude every integer root. The denominator also needs an exact no-pole check in the stated range. Neither a finite scan nor floating signs would prove this all-kcondition.

P9irreducibility is certified by exact modular factorization patterns whose proper subset-sum degrees have empty intersection; every modular factor is checked by an independent Frobenius/gcd test and their product reconstructed. An independent rational Sturm sequence verifies the real-root count and isolating intervals. An exact rational Euclidean remainder chain verifies coprimality with sigma_infinity. These algebraic checks are independent of the subsequent response calculation.

## Dependencies and scope

144gives the first-obstruction computation and the directly derived limiting polynomial;145is the conditional convergence theorem. Only exact rational coefficient arrays and interval certificates are evidence. The new all-kresponse conclusion is not assumed from the older delta=2/Qcases because the obstruction and response now have the same degree.

## Completed exact certificates

The primitive obstruction is irreducible: its square-free modular factor degrees are (3,6) modulo19 and (1,8) modulo29. The intersection of their possible proper factor degrees is empty. Every modular factor passes a Frobenius and gcd irreducibility certificate, and its product is checked against the primitive polynomial. A rational Sturm sequence isolates exactly five real roots, approximately

    0.06343727445510858, 0.15242998751865186,
    0.26983083939689934, 0.42237648278718953,
    1.8566753384149253.

The exact limiting response is coprime to this obstruction by a rational Euclidean remainder chain ending in a nonzero constant. Both single-mode nine-step responses were computed exactly for k=1,...,11. Their generic rational expressions agree with their direct k=10,11 values and with the corresponding constant and leading coefficients of the separately derived limiting response.

The rational criterion D(k) has numerator and denominator of degree89 after reduction. The independent certificate code extracts their rational coefficients and recomputes the shift k=24+t using the binomial formula with Python Fraction arithmetic. After one sign normalization, every shifted coefficient is nonnegative and each constant coefficient is strictly positive. Hence D(k) is defined and nonzero for all real k>=24. The integers1,...,9 are covered by the direct folded-carrier calculations, and10,...,23 by exact rational Horner evaluation of the generic criterion. Thus every positive integer is covered, including the first free harmonic k=1.

Irreducibility and equation(1) imply sigma_k(b_i)!=0 for every k>=1 and all five roots. Limiting coprimality gives sigma_infinity(b_i)!=0. Convergence to that limit supplies a lower bound for a tail, and the finite initial minimum is positive. Therefore inf_(k>=1)|sigma_k(b_i)|>0 for each root. This is an all-order response result, not an extrapolation of finite samples. An explicit numerical value for each lower bound is not supplied by this argument.

The response computation took589.17seconds and then encountered a JSON serializer error on a SymPy boolean. Its exact response files were intact. A separate Fraction-based certificate reconstruction took3.4713674867525697seconds and passed all stated checks; both failure and successful evidence are retained. The final authoritative files are verification/algebraic_certificates.json and verification/criterion_checks.json.
