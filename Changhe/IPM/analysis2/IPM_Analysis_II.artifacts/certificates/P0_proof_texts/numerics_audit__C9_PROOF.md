# Independent audit of the combined annular certificate C9

Status: analytical formula and independent numerical recomputation CONFIRMED (V102); independently reviewed CONFIRMED by the lead (V110).

## Statement and scope

Let F be the residual of the exact original state131, with the canonical velocity and exponent recovered in source_audit. For R in {2^31,2^32,2^35}, let w_R=(1+r^2/R^2)^(-11/10). Use the homogeneous negative norm L_R(F)=||w_RF||_(dot H^-1) and the same completed weighted fractional norm N_(s,R) as topics18 and20, with0<s<=2^-12. The proof below gives an explicit duality lower bound, not a norm upper bound. Topic20 establishes membership and N_(s,R)(F)>=2^(53/2)L_R(F)/6 for this growing forcing.

The test is phi_R=chi(r/R) sum_m a_m sin(m theta), where chi(t)=(t-1)^2(2-t)^2 on[1,2], zero elsewhere, e_m are the exact leading r^(2gamma-1) residual coefficients, d_m=1/35+m^2/630 and a_m=e_m/d_m. All sums are over the nonzero positive odd harmonics of that leading sector.

## Exact test energy

The compact C1 test belongs to homogeneous H1. Orthogonality gives

    ||D phi_R||_2^2=pi sum_m a_m^2(1/35+m^2 I),
    I=int_1^2 chi(t)^2/t dt.

The first integral is int_1^2 t chi'(t)^2 dt=1/35. The second is a rational number plus a rational multiple of log2, obtained by expanding the exact polynomial chi^2 and integrating each monomial divided by t. This evaluates the test energy without numerical differentiation or quadrature.

## Exact-sector pairing and uniform remainder

Independently expand the original potential through binomial orderQ=3. Retain in F_Q all generated sectors with second index q<=3. Use the pointwise remainder construction in C8_PROOF: the omitted potential terms and their Cartesian derivatives have a complete geometric majorant; additionally bound the finite nonlinear sectors with q>3. This supplies an explicit B(R) with

    |F-F_Q|<=B(R) r^(2gamma-1), r>=R.

Then

    P_Q=pi sum_(h,q) [sum_m a_m E_(h,q,m)]
            R^(p_(h,q)+2) int_1^2 (1+t^2)^(-11/10)
                                      chi(t)t^(p_(h,q)+1)dt.

A uniform pairing remainder is

    D=4B(R) sum_m |a_m| R^(2gamma+1)
            int_1^2 (1+t^2)^(-11/10)chi(t)t^(2gamma)dt.

Indeed int_0^(2pi)|sin(m theta)|dtheta=4. The producer uses the larger constant2pi, which is also valid. If P_Q>D>0, duality gives

    L_R(F)>=(P_Q-D)/||D phi_R||_2.

All radial integrals have analytic branches on the positive real interval. The independent implementation uses z=log t and analytic logarithms with domain checking, unlike the producer's direct-radial integration. Arb balls enclose the integrals, and all published lower endpoints are checked against the resulting lower bound. Integer conversion uses exact Arb endpoints rather than a floating-point cast.

## Provenance and limitations

Every original canonical coefficient is reconstructed from the read-only accepted checkpoint. No numerics producer code is imported. The audit compares the producer's finite-sector pairing and test-energy balls and independently checks every advertised decimal and integer lower bound. Its own complete remainder bound need not reproduce the producer's sharper remainder coefficient digit for digit. Numerical findings, source hashes and final verdicts are stored beside this proof and in the chronological root ledger.


The08:04 producer update encodes its additional binary endpoint by the exact pair[m,e]. The audit reads it as the rational m times2^e and compares it with the independently enclosed test range, separately from the downward published decimal and integer claims. It snapshots and hashes the input bytes once and checks that they are unchanged at completion. An unresolved finer endpoint comparison does not change any independently certified published bound.
