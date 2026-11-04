# A strict smooth-class gap below the quarter pressure threshold

Status: CONFIRMED A2699-A2700; scope OPEN A2701. Complete source and independent reconstruction read; existing coordinator comparison completed.

## 1. Statement and definition of the constant

For a homogeneous quadratic vector polynomial Q on R3 and homogeneous quartic scalar polynomial R, write brackets for normalized unit-sphere averages. Define the feasible set of triples (gamma,Q,R) by

    0<=gamma<=1/4, div Q=0, <|Q|^2>=1,
    -Delta R=tr((DQ)^2), R(x)>=gamma|Q(x)|^2 for all x.

Let Gamma2 be the maximum feasible gamma. Its existence is proved below, together with 1/60<=Gamma2<1/4. Put gamma_s=max(1/6,Gamma2).

On any ball B_b centered at zero, suppose V is C3, P is C4, div V=0, -Delta P=tr((DV)^2) in distributions, and V(0)=DV(0)=P(0)=0. If for a real constant gamma>gamma_s,

    P(x)>=gamma|V(x)|^2 throughout B_b,                (1)

then V=P=0 on the entire ball. For every gamma<=gamma_s there is a nonzero polynomial pair satisfying these assumptions and (1). Thus gamma_s is the exact threshold for the stated C3/C4 class and its C-infinity subclass, with a strict inequality required for the vanishing conclusion. This is a kinematic Poisson statement, not an unconditional Euler profile theorem.

## 2. Sphere flux and normalization

Set E=|V|^2, T=V tensor V+P I, e(r)=<E(rn)>, v(r)=<(V(rn).n)^2>, pbar(r)=<P(rn)>, and A(r)=v(r)+pbar(r). The Poisson and divergence equations imply div div T=0. There is no center source because T is smooth enough on the whole ball. In the radial decomposition, the sphere integral of a tangential divergence is zero, giving

    0=A'(r)+[3A(r)-<tr T(rn)>]/r,
    r A'(r)=e(r)-3v(r).                              (2)

Since V=O(r^2) and P(0)=0, A(0)=0 and

    A(r)=integral_0^r [e(s)-3v(s)]ds/s.              (3)

For a homogeneous pair (Q,R), all these terms have degree four. With <|Q|^2>=1, equation (2) implies

    <R>=(1-7v_Q)/4, v_Q=<(Q(n).n)^2>.               (4)

The coefficient is seven: the radial velocity contribution occurs both inside A and on the right of (2).

## 3. Nonempty compact feasible set

Let rho^2=x^2+y^2 and define

    Q0=z(-y,x,0), E0=rho^2 z^2,
    R0=rho^4/240-rho^2 z^2/30+8z^4/45.

Direct differentiation gives div Q0=0, tr((DQ0)^2)=-2z^2 and Delta R0=2z^2. Also

    R0-E0/60=(rho^2-6z^2)^2/240+z^4/36>=0.

Since <E0>=2/15, the pair Q=sqrt(15/2)Q0, R=(15/2)R0 is feasible at gamma=1/60.

The sphere L2 normalization bounds every coefficient of Q because the space is finite dimensional and restriction to the sphere is injective. Every feasible R is nonnegative and, by (4), <R><=1/4. Choose a sphere-orthonormal basis phi_j of the restrictions of quartic homogeneous polynomials. Each expansion coefficient obeys

    |<R phi_j>|<=||phi_j||_infinity<R><=||phi_j||_infinity/4.

Thus all coefficients of R are bounded. Coefficient limits preserve homogeneity, divergence, the normalization and Poisson equations, and the pointwise inequality, the last by uniform convergence on the sphere followed by homogeneity. The feasible set is closed and bounded in a finite-dimensional space, hence compact. It is nonempty by the explicit pair. Therefore gamma attains a maximum Gamma2.

## 4. Exclusion of the quarter endpoint

At gamma=1/4, feasibility and (4) imply <R>>=1/4 and <R><=1/4. Hence v_Q=0 and R=|Q|^2/4 on the sphere and, by homogeneity, everywhere. Likewise x.Q(x)=0 everywhere.

Differentiating tangency and using homogeneity gives (DQ)^T x=-Q and DQ x=2Q. Thus x cross curl Q=-3Q. Since curl Q is linear, Q=x cross Mx for some real matrix M. Its divergence is -x.curl(Mx), so div Q=0 makes the constant curl(Mx) zero; equivalently M is symmetric. An oriented orthonormal eigenbasis then gives

    Q=(a yz,b xz,d xy), a+b+d=0.

The Poisson equation with R=|Q|^2/4 has the three coefficients

    b^2+d^2+4bd=0, a^2+d^2+4ad=0, a^2+b^2+4ab=0.

Equivalently a^2=-2bd, b^2=-2ad and d^2=-2ab. Multiplication gives (abd)^2=-8(abd)^2. Thus one coefficient is zero and the three equations force all of them to be zero, contradicting the normalization. The endpoint is infeasible. Compact attainment now gives Gamma2<1/4. Excluding an endpoint without attainment would not by itself prove this strict gap.

## 5. Reduction of a C3/C4 pair to its quadratic jet

Assume gamma>gamma_s and (1). In particular P>=0 and P(0)=0. Its linear Taylor term vanishes at this local minimum. Its quadratic term R2 is nonnegative by division of P(rx) by r^2. Since DV(0)=0, the Poisson equation gives Delta R2=0. A nonnegative quadratic has positive semidefinite Hessian, whose trace is zero here, so R2=0. Its remaining cubic term is nonnegative by division by r^3 and is odd, hence zero. Consequently

    V(x)=Q(x)+O(|x|^3), P(x)=R4(x)+o(|x|^4),

where Q and R4 are homogeneous of degrees two and four. C4 Taylor expansion of the second pressure derivatives and C3 expansion of the velocity derivatives show

    div Q=0, -Delta R4=tr((DQ)^2), R4>=gamma|Q|^2.    (5)

If Q were nonzero, divide Q by sqrt(K) and R4 by K, where K=<|Q|^2>>0. Equation (4) for this pair and (5) first give gamma<=1/4. The normalized pair is then feasible by definition, so gamma<=Gamma2, a contradiction. Thus Q=0 and V=O(r^3).

## 6. Whole-ball vanishing of the higher-order remainder

Now e,v=O(r^6), so (3) gives A=O(r^6) near the center. Everywhere on the ball (1) implies A=v+pbar>=gamma e>=0. From (2),

    A'(r)<=(1/gamma)A(r)/r.

The nonnegative function r^(-1/gamma)A(r) is nonincreasing. Since gamma>1/6 and A=O(r^6), its center limit is zero. At any positive radius its value is bounded above by that zero limit, hence it is zero. Then e=0 on every sphere, so V=0 on the entire ball. Finally P>=0 and pbar=A=0 imply P=0 everywhere by continuity. No local-to-global continuation principle is used.

## 7. Sharpness at the attained threshold

If Gamma2>=1/6, take an attained maximizing pair (Q,R). It is polynomial, nonzero, and satisfies (1) for every gamma<=Gamma2=gamma_s on every centered ball. This existence follows from the compact feasible set, without an optimizer computation.

If Gamma2<1/6, take the cubic polynomial swirl

    V=rho^2(-y,x,0), E=rho^6, P=rho^6/6.

It has div V=0, V=DV=P=0 at zero, tr((DV)^2)=-6rho^4 and Delta P=6rho^4. Thus it satisfies all assumptions for every gamma<=1/6=gamma_s. It also solves stationary Euler because (V.grad)V=-rho^4(x,y,0) and grad P=rho^4(x,y,0). This pair works at Gamma2=1/6 as well. All examples are polynomial and so belong to both claimed regularity classes.

The abstract maximizing pair is required to solve only the stated Poisson and divergence equations, not stationary or similarity Euler. The explicit cubic swirl does not decay. No counterexample to the campaign conjecture is obtained.

## 8. Dependencies and remaining questions

This argument uses the full-ball center flux, finite-dimensional norm equivalence and compactness, exact polynomial algebra, and ordinary Taylor expansions with the stated differentiability. All dependencies are reproduced above. The value of Gamma2 and whether it exceeds 1/6 are unresolved here. No numerical estimate, formal build or new model client was needed. The existing configured model comparison is completed in the final section; actual provider runtime is independently unattested.

## 9. Completed existing coordinator comparison

All nine coordinator items and wording point S1 were read, along with the complete shared check log. The source hash matches the pinned snapshot. The comparison agrees on the center sphere identity, compactness from R>=0 and its bounded sphere integral, the full real quadratic contradiction, the C3/C4 jet reduction, the whole-ball ODE step and the sharp threshold with equality examples. In item 6 the notation A>=pbar is valid because v>=0; the proof uses the stronger explicit A>=gamma e. No quantitative value of Gamma2 is inferred from compactness or random trials.

The lower bounds in subsequent LIT319 and LIT321, and the upper bound in LIT320, require their separate proofs and designated verdicts; they are not prerequisites for this exact implicit threshold theorem. The supplied numerical and random checks are supplemental only. No gap was found. Existing configured model file comparison is completed; actual provider runtime remains independently unattested.
