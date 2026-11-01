# Exact response infima and exterior radii at period four

Status: PROVED. The independent Cartesian certificates and the theory part's separate Fourier and rational computations agree. The independent review dated 2026-10-31T11:06Z is recorded in V284. All conclusions retain the exact hypotheses and scope stated below.

## Statement, objects and scope

Let b_1<...<b_6 be the six exact real roots of the primitive O8 polynomial defined in142. Set delta=1/2, c=2, and f_1=sin(theta)+b_i sin(3theta). Let sigma_k, k>=2, be the four-step resonant response defined in142, and let sigma_infinity be its exact quartic limit. All absolute values below are evaluated at the exact algebraic root, not a decimal midpoint.

The global infimum of |sigma_k| is attained uniquely at k=5,3,5,5,5 for roots1,2,4,5,6 respectively. For root3 it is |sigma_infinity(b_3)| and is not attained at any finite integer k. The corresponding convenient uniform lower bounds are

    s_i = (2^-5, 2^-14, 2^-15, 2^-14, 2^-10, 2^-9).

With a_i=(32/25,26/25,27/25,119/100,34/25,163/100), B=4, kappa=20 and L=2, sufficient exterior radii are

    R_i = (2^82,2^96,2^98,2^98,2^92,2^92),

and a common sufficient radius is2^104. For amplitude epsilon!=0 multiply these by |epsilon|^2. The conclusion is convergence on every strict closed exterior r>=R>R_i of the density, stream, common potential and every weighted derivative. The exact certificates described next all pass. No optimality or global stationary continuation is asserted.

## Exact global-infimum proof

By142 there is an exact rational expression sigma_k=N(k,b)/D(k) valid for every k>=9. The numerator coefficients are polynomials in b and the denominator is independent of b. For a rational K>=9 write k=K+t. After a common sign normalization the coefficients of D(K+t) are strictly positive. Let S(b) be the signed response polynomial at the proposed finite minimizer, or the signed limiting polynomial for the proposed unattained infimum. Isolate each b_i in a rational interval I_i on which S is positive. Let e be the sign of sigma_infinity on that interval.

Using rational interval Horner arithmetic, check that every coefficient of e N(K+t,b)-S(b)D(K+t) is nonnegative throughout I_i, with strictly positive constant coefficient. This implies |sigma_k(b_i)|>S(b_i) for all k>=K. In the finite-minimum cases the proposed minimizer is below K, and all other k between2andK-1 are checked to have strictly larger absolute response. Hence that minimizer is unique. In the limiting case all finite k below K are checked strictly larger; the exact rational limit from142 proves that the strict lower bound approaches S(b_i). Thus the infimum is S(b_i) and is not attained. An identically zero highest coefficient in the limiting case is allowed and verified exactly.

The finite and tail arguments cover every integer, so no assumption about extrapolating finite samples enters the proof. Evaluating S on I_i then verifies the stated rational lower bound s_i. Root3 does not have a finite minimizer.

## Exact radius certificate

Theorem131 applies with Q=4. Use its five-component polynomial map Phi, constant vector c0, strictly lower triangular matrix J, T=(I-J)^(-1), and Y0=T c0. As proved in134, G=Y0+T(Phi-c0-JY) has nonnegative coefficients and gives an equivalent fixed-point equation. For each stated row test the box 2Y0 with z0=2^-q, where q=(41,48,49,49,46,46). Every component of2Y0-G(z0,2Y0) must be strictly positive. Also test common a=163/100,s=2^-15,q=52. The norm inequalities1+|b_i|<a_i and the response bounds supply the hypotheses. Since z=r^-1/2, the exterior radius is z0^-2=2^(2q).

Monotone iteration of G remains in the box and its formal coefficients stabilize by their positive z-degree. Thus all coefficient series converge at z0 and have geometric bounds. Theorem132 reconstructs the common potential with that same geometric base. Strictly smaller z absorbs all derivative and angular-strip factors, proving the convergence statement. Homogeneity gives the amplitude factor |epsilon|^2. Failure of the same box at q-1 establishes only the first successful integer dyadic choice for this prescribed box, not an optimal radius.

## Dependencies and reproducibility

142provides the exact roots, formulas and independent modular/Cartesian verification. 131and132are the independently reviewed general-period existence and potential theorems;134proves the component certificate. Exact input hashes, rational coefficient intervals, matrices, box margins and real timings are retained beside this proof.

## Recorded outcome

All six tail certificates pass already at K=9. Every nonzero shifted coefficient is strictly positive; in the third row the highest coefficient is identically zero because the target is the exact limit. The finite comparisons are strict outside the stated minimizers. Exact convenient sharper lower bounds in increasing root order are

    91/2500, 3/25000, 43/1000000, 57/500000, 3/2500, 2/625.

All35component margins for the six radii and common radius are strictly positive. For each prescribed box the preceding integer dyadic choice fails, and positivity then excludes every larger dyadic z. The six maximum component ratios are approximately0.761486,0.870361,0.947277,0.863214,0.854073,0.937831, agreeing with the independent theory-part implementation. The successful exact calculation took0.44111909018829465seconds. An initial JSON serializer failure after a successful first row is retained separately; it did not change the arithmetic or mathematical claims.

## Sharper dyadic radii

Using the sharper response bounds in the recorded outcome, the same prescribed boxes pass at

    q=(40,47,49,48,46,46),
    R_i=2^(2q_i)=(2^80,2^94,2^98,2^96,2^92,2^92).

Every component inequality is strict, and every preceding integer dyadic choice fails for that same box. The maximum component ratios are approximately 0.948980, 0.876750, 0.817438, 0.888927, 0.788145 and 0.767231. A common box with a=163/100, s=43/1000000 still first passes at q=52, hence R=2^104. These assertions were independently reproduced from the polynomial map in 131 and agree with the theory part's separate computation. Exact matrices, rational boxes and all margins are in verification/sharper_dyadic_radii.json; V286 records the confirmation. The strict exterior and amplitude qualifications above apply unchanged.
