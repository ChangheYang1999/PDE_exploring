# Independent admissibility audit of the numerics N-B candidates

Status: exact admissibility CONFIRMED. The required global matrix inequality is REFUTED for the exact A2 and A3 candidates. Numerical fitting is not used as proof.

## Statement to be checked

The numerical work supplied the finite exact potential nb_stableA2_exact.json. Its exponent c is intended to equal the accepted state131 exponent. A generator in this file means

    chi_(j,m,T)=r^(2m) cos(2m theta)(1+r^2)^(p_j-m)T(t),
    p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma,
    t=r^2/(1+r^2).

The density and canonical velocity are

    rho=-partial_y Delta chi,
    U=(-partial_x partial_y^2 chi,partial_x^2 partial_y chi).

We check exact center normalization, a positive center slope, the full original leading angular density, and the vanishing of every residual sector whose radial degree is at least -2. These conditions establish admissibility for the previously defined unweighted residual spaces. They do not establish any coercivity or residual-size condition.

## Canonical reconstruction and origin

Expand T as an exact rational polynomial. A term b_h t^h becomes the canonical generator with k=m+h,

    b_h r^(2k)(1+r^2)^(p_j-k) cos(2m theta).

Combine all duplicate (j,m,k) indices. Since k>=m, each term is smooth at the origin: r^(2m)cos(2m theta) is a harmonic polynomial and r^(2k-2m) is an even radial polynomial. For the original legendre representation the polynomial coefficients are computed from binomial integers, not sampled values.

Only k<=2 contributes to the origin strain c[rho]=partial_x^2 partial_y^2 chi(0) or the slope a0=-partial_x^2 partial_y^2 chi(0)-partial_y^4 chi(0). They are therefore exact finite rational sums. We check c+c[rho]=1 and a0>0 directly on the reconstructed potential, independently of the projection algorithm.

## Exterior powers and the membership criterion

For each canonical term, expand (1+r^-2)^(p_j-k). The leading two binomial moments are the coefficients1 and p_j-k. Each order-q moment has density power

    alpha_(j,q)=gamma-j delta-2q.

To form its angular density and velocity independently, represent cosines in complex Laurent coordinates, apply the Cartesian derivative rules, and multiply Laurent polynomials for advection. A linear sector contributes (c alpha-1) times its density. Advection of branches (i,u),(j,v) contributes to index (i+j+1,u+v). Keeping exact phases in y derivatives is necessary for the signs.

For the given exponent, the only indices with alpha>=-2, after the automatically zero leading sector, are

    (1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1).

The program also checks (0,0). If all eight residual angular polynomials vanish identically and the leading potential agrees with the original, then the residual and all its derivatives have decay O(r^(-2-epsilon)) for epsilon=7delta-3>0. All omitted binomial orders have strictly lower powers. Finite sums of regularized powers have convergent differentiable exterior expansions, so this is a symbol estimate, not a sampled asymptotic. It implies membership in the unweighted residual spaces proved in topics09,11,12 and13, including the parity homogeneous negative norm. The same residual is then in the weaker weighted space.

## Necessary inequality tests

A positive point value cannot certify a global lower bound. A negative certified eigenvalue of the required matrix M, or a certified value below19/5, disproves that required global inequality for this exact candidate. Any such point will be evaluated by two independent derivative methods before it is reported as a counterexample. No finite grid of successful points will be reported as proof of coercivity.

## Evidence and scope

The exact input is read from the numerical work and copied here with its hash. The audit program does not import its projection or far-field code. It imports only previously verified independent Laurent differentiation routines from the independent verifier. Output records distinguish exact identities, individually certified numerical values, and open global conditions.

## Certified results for nb_stableA2_exact

The2342 supplied generators combine into1282 nonzero canonical terms. Exact rational reconstruction confirms c=4076476460239181/2251799813685248, c+c[rho]=1, the original full leading angular profile, all six stationary leading potential branches, the two vanishing first descendants and all eight required residual cancellations. The center slope lies in(7.19290788491380,7.19290788491382). The first nonzero residual power is gamma-6delta, about-2.13328; its full-circle angular L2 norm lies in(3081.2744,3081.2745). These are identities and rigorous intervals for this exact finite function.

At(0,1), two independent derivative constructions give

    2.22252637111320 < lambda_min(M) < 2.22252637111321.

This contradicts M>=19I/5, one of the required reference hypotheses in both current conditional theorems. It does not prove the absence of a smaller positive coercivity constant: global positivity is still open. Additional point violations below19/5 occur at(0,1/10),(1,1),(0,2).

At(0,2), the same methods give

    -26.52452060617171 < F < -26.52452060617170.

Consequently the sufficient weighted residual smallness also fails. In fact the norm embedding from topic18, valid independently of any reference coefficient hypothesis, gives |F(0,2)|<=16*2^(1/5)N(F)<20N(F). Since |F(0,2)|>26, we have N(F)>13/10 for every0<s<=2^-12 and either R=2^32 or R=2^35. The strict comparison2^(1/5)<5/4 follows by raising positive quantities to the fifth power:2<3125/1024. Thus the gap over eta=2^-35 is greater than2^35. This is a point-duality lower bound, not an upper estimate of the complete norm or a numerical nonexistence argument.

The point calculations use Cartesian Taylor jets through order7 and a separately differentiated polar polynomial representation. All seven field enclosures agree at each of eight points. The audit certificate records its actual Arb precision and the exact hashes of both methods. The finite point list establishes only the displayed individual inequalities.


## Subsequent exact candidates

The same statement, rational reconstruction and continuum membership argument apply to any subsequent N-B file with the displayed generator convention. Each new file is audited independently and identified by its exact source and canonical hashes. Its earlier candidate's center slope, point values, coercivity verdict and residual lower bounds do not transfer. For nb_stableA3_exact.json the exact identities and the same eight rational test points will now be checked before any numerical conclusion is recorded.


## Certified results for nb_stableA3_exact

The2342 supplied generators again combine into1282 nonzero canonical terms. Independent rational expansion confirms the original exponent, exact center normalization, original full leading profile, all six stationary branches, vanishing first descendants for branches0 and1, and all eight required residual cancellations. Its center slope is in(8.77823087391110,8.77823087391111). Its first nonzero residual sector is again(6,0), with the same angular polynomial as A2.

At(0,1), two independent768-bit methods give3.13523976212836<lambda_min(M)<3.13523976212837, below19/5. At(0,2), they give-13.75690624824585<F<-13.75690624824584. Since |F(0,2)|>40/3 and the reference-independent growth embedding is |F(0,2)|<20N(F), it follows thatN(F)>2/3. This holds for every0<s<=2^-12 and anyR>=1 in the defined weighted space, includingR2^31 by the uniform-radius audit. The sufficienteta2^-35 therefore fails by more than2^34. All eight points agree in all seven fields between the Cartesian-jet and polar-polynomial methods. This does not refute a smaller global positive matrix bound, later candidate iterates, or actual existence.
