# Independent weighted weak-distance audit

## Statement and hypotheses

Let 0<a<2 and w(X)=(1+|X|²)^(-a/2). Let H_a consist of real functions h even in x and odd in y with m=||w h||_2 finite. Assume the canonical divergence-free IPM velocity has a bounded extension to this space with a specified constant C_U:

    ||w U[h]||_2 <= C_U ||w h||_2.

Let c>1 and let rho and u=U[rho] be smooth real S1 fields satisfying

    |rho|+|u|=O((1+r)^gamma),
    |D rho|=O((1+r)^(gamma-1)),  0<gamma<1.

Put V=cX+u and F=V.D rho-rho. Suppose h in H_a satisfies

    F+div(Vh)-(2c+1)h+U[h].D rho+div(h U[h])=0

in distributions. All products are locally integrable by the stated hypotheses and the local L² membership of h and U[h]. For an integer k>=0 put t=r²/(1+r²), v=1-t and phi=y t^k v². Define

    ell=3c+1+2ck v-4ct,   g=1+2k v+4t,
    A=||phi ell/w||_2,
    B=||t^k v² g u/w||_2,
    C=||r t^k v² D rho/w||_2,
    I=|integral F phi|,
    D=A+B+C_U C.

For j>=0 and b>0 let S(0,b)=1 and

    S(j,b)=(j/(j+b))^j (b/(j+b))^b   if j>0.

One may take H=1 when k=0 and a<=3/2, and otherwise

    H=S(k,2-a)+2k S(k,3-a)+4S(k+1,2-a).

Then every such correction obeys

    I <= D m+C_U H m²,
    m >= 2I/[D+sqrt(D²+4C_U H I)].

The second formula is interpreted as zero if I=0. This is a necessary condition at fixed c, not an inverse theorem or existence assertion.

## Proof of the weak estimate

For compactly supported smooth phi, integration by parts gives

    integral F phi
      =integral h[(2c+1)phi+V.D phi]
       -integral U[h].(phi D rho)
       +integral h U[h].D phi.

The equality div(V)=2c accounts for the displayed linear coefficient in the distributional equation. Weighted Cauchy-Schwarz bounds the three integrals by

    m||(2c+1)phi+cX.D phi||_(L²(w^-2))
    +m||u.D phi||_(L²(w^-2))
    +C_U m||phi D rho||_(L²(w^-2))
    +C_U m²||D phi/w²||_infinity.

Direct differentiation yields (2c+1)phi+cX.D phi=phi ell and

    |D phi| <= t^k v²(1+2k v+4t).

The latter follows from

    D phi=t^k v² e_y+2yX t^(k-1) v³(kv-2t),

with the k=0 expression understood after cancellation. The inequality |yX|<=r² gives the stated bound. Also |phi|<=r t^k v². These estimates give A, B and C above.

To justify the noncompact test, multiply phi by a smooth cutoff supported in r<=2R and equal to one in r<=R. At infinity phi=O(r^-3), D phi=O(r^-4), and F=O(r^gamma). Thus F phi is absolutely integrable because gamma<1. The linear dual coefficients have orders r^(a-3) and r^(a+gamma-4), which lie in L² since a<2 and gamma<1. The nonlinear multiplier D phi/w² is O(r^(2a-4)), bounded and tending to zero. Each added cutoff derivative has the same order on its annulus and vanishes in the corresponding norm or by the weighted L² tails of h and U[h]. Passing R to infinity is therefore valid.

The maximum of t^j(1-t)^b is S(j,b), as follows by differentiation and the endpoint values. This proves the general H bound. For k=0, the Jacobian of X v² has radial and tangential eigenvalues v²(1-4t) and v². Hence

    sup_angle |D phi|/w²=v^(2-a) max(1,|1-4t|).

For a<=3/2 this is bounded by v^(1/2) max(1,|1-4t|)<=1. The second branch has its interior maximum one at t=3/4, and the first is at most one. Equality at the origin gives H=1. Solving the resulting quadratic inequality proves the distance bound.

## Independent numerical realization

The N4 radial-Fourier representation is constructed by Cartesian differentiation of the exact canonical potential. It supplies all components u1,u2,rho_x,rho_y, including all angular modes. The previously audited grouping routine expresses B² and C² as sums of integrals

    (pi/2) integral_0^1 v^b (1-v)^(2k+1) P(v) dv.

Its unweighted exponent b is shifted to b-a because multiplication by w^-2 contributes v^-a. The polynomial for B is additionally multiplied by [5+(2k-4)v]². This is a bound on |D phi|², not an assertion that the angular gradient bound is an equality. Likewise C uses y²<=r² before angular integration.

The scalar A² is obtained independently from

    (pi/2) integral_0^1 v^(1-a) (1-v)^(2k+1)
            [1-c+2c(k+2)v]² dv.

The signed pairing uses the complete first sine coefficient of the residual, already independently checked against a polar construction. If its radial polynomial at branch index l is P_l(v), then

    integral F phi=(pi/2) sum_l
        integral_0^1 v^(l delta/2-1) (1-v)^(k+1) P_l(v) dv.

All displayed integrals use outward Arb gamma values for the initial beta moment and its exact rational recurrence for successive moments. Endpoint exponents are checked before evaluation. This is independent of T4's gamma-free polar-square calculation. Precision, source hashes and each constituent interval are recorded.

The current comparisons use a=1 and C_U=2, with the latter supplied by the separately audited T4-054 weighted velocity estimate. More generally this proof is conditional on the displayed weighted velocity bound. No weighted residual norm, high-order inverse, or nonlinear closure is certified here.
