# The logarithmic axis constant at c=2

Result234. This proof is written before implementation or evaluation. It is a theorem about finite polynomial hydrostatic trial fields. It assumes the compactification exponent P=2 exactly. It is not a theorem about a full IPM profile, and the finite core moment formula for1<P<2 must not be continued through its pole.

Let C>0, let k(w)=sum_(j=1)^J k_j w^j and H(w)=sum_(j=1)^D h_j w^j be real polynomials, and define w in(0,1) by

    y=C sqrt(1-w) w^(-2),  y>0.

The map is strictly decreasing from infinity to zero, so w(y) exists uniquely. Set G(y)=y H(w(y)), V(y)=integral_0^y k(w(s))ds. For the saved smooth basis, k is the independently derived full-tail curvature integral, so V is the vertical hydrostatic velocity on the positive axis. The assumptions k(0)=H(0)=0 are exact finite-polynomial identities. No origin normalization is needed for this calculation.

Define

    K=h_1 sqrt(C), Q=k_1 sqrt(C)/2,
    c2=C(h_2-h_1/4),
    c3=C^(3/2)(h_3-h_2/2-h_1/32),
    B=C(k_2-k_1/4).

Missing polynomial coefficients are zero. Then, as y tends to infinity,

    G(y)=K sqrt(y)+c2+c3 y^(-1/2)+O(y^(-1)),
    V(y)=4Q sqrt(y)+B log(y)+M+O(y^(-1/2)),          (1)

with the exact finite constant

    M=C[k_1(-1/2-log2)+k_2(4log2-3)
          +sum_(j>=3) j k_j BETA(j-2,3/2)]-B log(C). (2)

Formula(2) uses only positive beta parameters. It is valid for arbitrary finite coefficients, including either sign of K or Q. If K>0 and c=2, define the signed axis residual and its exact pointwise denominator by

    R=(2y+V)G'-G, Nf=|(2y+V)G'|+|G|,
    r2=-c2+2KQ.

Then

    y R/Nf = [r2/(2K)] sqrt(y)+(B/4)log(y)
              +M/4-c3/K-r2(2c2+r2)/(4K^2)+o(1).    (3)

Thus a small r2 does not by itself produce a constant limit. If r2=0 but B!=0, the logarithm still diverges. All coefficients in(1)-(3) concern this finite trial field, not a solved transport equation.

## Derivation of the constant

Integration by parts, with y(w)=C sqrt(1-w)w^(-2), gives the exact identity

    V(y)=y k(w)+C integral_w^1 sqrt(1-v)v^(-2) k'(v)dv.  (4)

The boundary at v=1 vanishes. Put A=2k_2-k_1/2 and

    L(v)=[sqrt(1-v)k'(v)-k_1-A v]/v^2.

This is continuous at v=0 and integrable at1. Separating the first two powers in(4) yields

    V=y k(w)+C[k_1(1/w-1)-A log(w)+I0-integral_0^w L(v)dv],
    I0=integral_0^1 L(v)dv.                            (5)

Two elementary integrals are

    integral_0^1 [sqrt(1-v)-1+v/2]/v^2 dv=1/2-log2,
    integral_0^1 [sqrt(1-v)-1]/v dv=2log2-2.

For the first, integration by parts leaves1/2 plus half of the integral of(1-1/sqrt(1-v))/v; substitution u=sqrt(1-v) gives -2log2. The second follows by the same substitution, integrating -2u/(1+u) on[0,1]. Therefore

    I0=k_1(1/2-log2)+2k_2(2log2-2)
         +sum_(j>=3)j k_j BETA(j-2,3/2).             (6)

As w tends to zero, y k(w)=C[k_1/w+k_2-k_1/2+O(w)] and 4Q sqrt(y)=2C k_1/w-C k_1/2+O(w). Also log(y)=log(C)+(1/2)log(1-w)-2log(w). Substituting these into(5) gives B=CA/2 and M=C(k_2-k_1+I0)-B log(C), which is exactly(2). Its remainder is O(w)=O(y^(-1/2)). No divergent integral has been used without its two explicit subtractions.

## Density expansion and normalized residual

Let u=sqrt(C/y). The radial equation is w=u(1-w)^(1/4). Taylor inversion, or direct substitution into this relation, gives

    w=u-u^2/4-u^3/32+O(u^4).

Insert this in yH(w), proving the first expansion in(1). These are convergent expansions for sufficiently small u, so termwise differentiation is justified. Inserting the two expansions in the residual gives

    R=r2+y^(-1/2)[(KB/2)log(y)+KM/2-2c3]
          +O(y^(-1)log(y)).                          (7)

For K>0, both G and(2y+V)G' are positive for sufficiently large y. Hence Nf=2G+R exactly there. Expanding its reciprocal through the next term yields(3), including the constant correction from a nonzero r2. Dropping that correction would be incorrect even though it vanishes when r2=0.

## Complete finite-radius evaluation and an analytic series remainder

Write sqrt(1-v)=sum_(n>=0)b_n v^n, where b_0=1 and b_n=b_(n-1)(n-3/2)/n. In(5),

    integral_0^w L(v)dv
       =sum_(j>=1)j k_j sum_(n>=max(0,3-j))
                       b_n w^(j+n-2)/(j+n-2).         (8)

For0<w<1 the series converges absolutely. Truncating the n sum at N>=2 leaves an error in V bounded by

    C/(1-w) sum_(j>=1)|j k_j| w^(j+N-1)/(j+N-1).    (9)

Indeed |b_n|<=1, each denominator is increasing, and the remaining powers form a geometric series. This is a bound on the exact analytic truncation error. Floating-point error in coefficient conversion, beta evaluation and cancellation is separate and must be tested at higher precision; it is not included in(9).

The derivative G' is evaluated independently from

    G'=H(w)-w(1-w)H'(w)/(2-3w/2),

obtained by differentiating the defining map. The map is inverted in log(w), so large physical y does not create an underflow before arbitrary precision is applied. Formula(5) and the convergent series evaluate the complete axis velocity, including the core, without a finite-box closure or a numerical fit of M.

## Verification and scope

Manufactures will compare(5),(8) with direct quadrature of(4) for individual monomials and signed polynomials, vary C, check the exact map and derivative identities, verify(2) by an independent convergent integral for I0, and test the residual expansion at increasing radii with two precisions and truncations. All dependencies are independently written: ../hydrostatic_axis_primitive/PROOF.md supplies k,H for saved fields; ../hydrostatic_axis_core_moment/PROOF.md supplies the prior B formula. The argument above derives the new finite constant and residual correction independently. Its verification will precede use on candidate data. No producer code is imported. No PDE solution, endpoint or uniform numerical error bound follows.
