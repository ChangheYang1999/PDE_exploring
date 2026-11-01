# Six candidate compatible profiles at delta = 1/3

Status: PROVED after the independent exact recurrence, algebraic certificates and theory-part comparison in V302. The general convergence and potential arguments131/132 were already independently reviewed.

## Statement and normalization

Set delta = 1/3, c = 3/2, p_n = 1 - n/3 and P_n = 2 - n/3. Normalize the leading density to f_1 = sin(theta) + b sin(3 theta). At a stream resonance n = 6k, k >= 2, delete the entire resonant output from the particular inverse and denote its free coefficient by H_(6k). Its stream frequency is 2k - 2. The next density compatibility is the coefficient of sin((2k - 1) theta) in f_(6k+6).

Let O12(b) be the coefficient of sin(theta) in f_12. Define P12 to be the primitive integer polynomial with positive leading coefficient proportional to O12. Let sigma_k(b) be the response of the next compatibility coefficient to a unit change of H_(6k). The proposed result is that P12 has exactly six real roots, and every root b_i satisfies

    inf_(k >= 2) |sigma_k(b_i)| > 0.

By the already proved convergence and potential theorems in131 and132, this implies a uniquely tuned convergent exterior density and stream series at each root. The potential has the finite exceptional logarithms allowed by132. The normalized leading profiles can be multiplied by any nonzero real epsilon, with the sufficient radius multiplied by |epsilon|^3. This conclusion concerns the local exterior stationary equation, not a smooth whole-plane extension.

## Independent recurrence

Use the signed Laurent polynomial S_m = (z^m - z^(-m))/2 for a sine mode. A field of radial degree a has encoded Cartesian derivatives

    X_a z^m = ((a+m) z^(m-1) + (a-m) z^(m+1))/2,
    Y_a z^m = ((a+m) z^(m-1) - (a-m) z^(m+1))/2.

The common imaginary factor is suppressed. The physical y derivative is iY. Thus the encoded Poisson equation is -XXg + YYg = Xf, and the transport coefficient is Xg Yf - Yg Xf. For n >= 2 the density is twice the sum of all ordered transport products divided by n-1. The stream coefficient of signed frequency m is the corresponding Xf coefficient divided by m^2 - P_n^2.

Compute f_1 through f_12 and g_1 through g_11 in Q[b]. The apparent order6 zero mode is absent by sine symmetry. Every other stream order below12 is nonresonant. Hence the calculation of O12 uses no arbitrary harmonic.

For a unit stream harmonic e_k at n = 6k, define its density response phi_r at n+r by

    phi_r = 2/(n+r-1) [T(e_k,f_r)
             + sum_(s=1)^(r-1) {T(g_(r-s),phi_s) + T(Pi phi_s,f_(r-s))}],

for r = 1,...,6, where T is the encoded Cartesian transport and Pi is the nonresonant inverse. Then sigma_k is the sin((2k-1) theta) coefficient of phi_6. The formula uses only f_1,...,f_6 and g_1,...,g_5.

For the symbolic tail use the two frequency carriers m = +/-2k + v. Their supports remain disjoint when k >= 13, since q = 2k-2 >= 24 = 6B with B = 4. In that range the fixed signed-carrier calculation equals the full Laurent calculation. Explicit direct comparisons on their overlap check the implementation. This yields a rational function of k whose coefficients are polynomials in b of degree at most6.

## Algebraic and all-index certificate argument

The proof of irreducibility will use exact modular factors and independent finite-field powers and gcds. The proposed degree patterns modulo13 and19 are [3,9] and [1,11]. Their proper subset-degree sets have empty intersection. After checking that both reductions preserve degree and are squarefree, Gauss's lemma excludes every proper rational factor. An exact Sturm chain and disjoint rational intervals must show that precisely six roots are real.

For each finite initial k, check that sigma_k is a nonzero polynomial of degree at most6. For the rational tail, check that the common factor of its b-coefficients has no integer zero k >= 13, and that the denominator has no zero there. Check that its limit is a nonzero polynomial of degree at most6. Irreducibility of the degree12 polynomial then excludes every finite response zero and every limiting response zero at all its roots. Continuity of the rational function at infinity supplies a positive lower bound in the tail; a finite initial minimum completes the claimed positive infimum.

Each inference needs its exact recorded calculation. Finite root tests alone are insufficient. Quantitative infima and radii will have their own certificate folder and proof.

## Evidence and dependencies

The independent implementation uses code/tuned_cartesian_exact.py and a new period-six driver. The theory part's output is read only for the final exact comparison. Retain the actual source hashes, intermediate fields, polynomial coefficients, modular certificates, Sturm evidence and elapsed time alongside this proof. Dependencies:131 for the positive majorant and132 for the common potential and derivative convergence. No Lean build is required or run.

## Completed certificates

The exact obstruction and limiting response agree with the theory part's independent Fourier computation. The Cartesian driver checks all66 ordered products and11 Poisson inversions below the first resonance, all17 direct responses k2 through18, and the symbolic overlap k13 through18. The tail has common numerator-coefficient factor(k-1)(2k-1)^2, with no tail zero. Every denominator root lies below13. Its limiting response is nonzero of degree6.

Independent modular certificates give factor-degree patterns[3,9] modulo13 and[1,11] modulo19, with empty intersection of possible proper rational factor degrees. The rational Sturm chain has variations9 and3 at the infinities and isolates the six roots near-0.608726913793,0.0885568921012,0.140724179095,0.196515363511,0.278497889439,0.512156473620. The irreducibility and lower response degree prove the asserted positive infima. Explicit values and sufficient radii are proved in155. All evidence and source hashes are in verification/root_response_certificates.json.
