# An axis residual can be small while the third obstruction stays fixed

Date: 2026-10-20. Status: complete informal argument, independent review pending. This is an axis-hierarchy result, not a coupled profile construction.

## Statement

Let A>2, beta=2/A, L>0, and let w,g be smooth on[0,L], analytic near both endpoints, odd and even respectively near0. Assume

    w g'=(w'-A)g,  w<0 on(0,L),  g>0 on(0,L],
    w=-Ax+O(x³),  g=x²+O(x⁴) at0,
    w(L)=0,  w'(L)=A,  g(L)=g_*>0.

Put p=6+beta, m=-w/g, H=A^beta g³ m^(-beta), Q=(g'-w'')/(2g³), and F=g⁴ Q'/3. Thus H/x^p tends to1 at0 and H has a pole of order beta at L. Define

    B_3=-FP integral_0^L F/(wH) dx.                      (1)

The finite part is the constant after subtracting divergent center powers in the x coordinate. No logarithm occurs under the stated assumptions. For a smooth trace G on[0,L] that is even analytic near0, define its third hierarchy residual

    r_G=wG'-(3w'-3A-2)G-F.                             (2)

Then

    B_3=FP integral_0^L r_G/(wH) dx.                    (3)

There are fixed admissible axis data w,g with B_3 nonzero and traces G_epsilon analytic near both endpoints, smooth on[0,L] and even near0, for which r_(G_epsilon) is supported in[epsilon,2epsilon] and

    ||r_(G_epsilon)||_(C^j[0,L])=O(epsilon^(6+beta-j)),
                    j=0,1,...,6.                      (4)

Thus the unweighted residual norms through order six tend to zero while the axis obstruction stays fixed. The smooth traces in this statement need not come from a solution of the two-dimensional canonical equations.

## Integrating factor and residual accounting

The first equation gives m'/m=A/w. Logarithmic differentiation therefore gives

    H'/H=3g'/g-beta m'/m=(3w'-3A-2)/w.

For Z=G/H, equation(2) is exactly Z'=(F+r_G)/(wH). Near0, H=x^p h(x²), where h is analytic and h(0)=1, while G is even analytic. Hence Z has a convergent expansion in powers x^(2n-p). Since p lies strictly between6 and7, no exponent is zero. The finite part of Z at0 is consequently zero. At L, H is a positive multiple of(L-x)^(-beta)(1+O(L-x)); bounded G implies Z tends to zero.

Integrate Z' on[delta,L-eta] and take eta to zero and the finite part as delta tends to zero. The endpoint difference has finite part zero, proving(3). Both separate integrals have finite parts: at0, F is even analytic, wH is x^(7+beta) times a nonzero even analytic factor, and r_G is also even analytic. The primitives have exponents2n-6-beta, none zero. At L, F and r_G are bounded and 1/(wH)=O((L-x)^(beta-1)), which is integrable. This also proves that no unspecified endpoint flux was discarded.

If r_G vanishes near0, (3) is an ordinary absolutely convergent integral and implies the sufficient estimate

    |B_3| <= integral_0^L |r_G|/|wH| dx.                (5)

The weight behaves like A^(-1)x^(-7-beta) at0. Its singularity is essential to this estimate.

## A fixed nonzero obstruction

Use the explicit compatible R12 data

    w=-Ax(1-x²/L²)/(1+x²/L²),  g=x²/(1+x²/L²).

The first axis equation and all endpoint assumptions follow by differentiation. For this family, direct integration of F/(wH), justified by subtracting its first three even center terms before the substitution t=x²/L², gives

    B_3=C_A L^(-4-2/A)(1-S_A/L²),
    S_A=6A(4A-3)/(8A-1),
    C_A=-(8A-1)Beta(-2-1/A,2/A)/(3A(2A-1))>0.         (6)

The two beta terms and their reduction are proved in ../r12-seventh-resonance/PROOF.md, “Corollary for the entire prescribed R12 family”, equations(4) and the following derivation. Its gamma-sign argument applies to all A>1. Only this exact axis identity is used here, not that topic's higher-order or source-regularity exclusions. In particular A=4,L=1 gives S_A=312/31 and B_3=-(281/31)C_4<0.

## Removing the center singularity and locating its residual

Let G_* be the unique solution of wG_*'-(3w'-3A-2)G_*=F bounded at L. It is

    G_*(x)=-H(x) integral_x^L F(s)/(w(s)H(s)) ds.

Near L the integral is O((L-x)^beta), so it is bounded. It is analytic there: in delta=L-x, the equation has the form A delta G_delta+2G plus analytic terms vanishing at delta=0, and each Taylor denominator A n+2 is nonzero. Equivalently the integrand is delta^(beta-1) times an analytic function, and its primitive times H is analytic. Every other solution differs by a multiple of H and is unbounded at L, proving uniqueness.

Near0, a primitive of F/(wH) has the form x^(-p) times an even analytic function, because the forcing starts at orderx² and no denominator2n-p vanishes. The integral representation and definition(1) therefore give

    G_*=G_an+B_3 H,

where G_an is even analytic near0. The sign follows by writing the primitive with zero finite part at0; its value at L is -B_3.

Choose a fixed smooth function chi on[0,infinity), equal to1 for t<=1 and0 for t>=2. For2epsilon smaller than the center analytic neighborhood, put

    G_epsilon=G_*-B_3 H chi(x/epsilon).                (7)

It equals G_an near0 and G_* near L, so it has the asserted endpoint regularity. Since H solves the homogeneous equation, direct differentiation gives

    r_(G_epsilon)=-B_3 wH chi'(x/epsilon)/epsilon.      (8)

This is supported in[epsilon,2epsilon]. On that annulus, wH is x^(7+beta) times a smooth function whose derivatives have the corresponding power bounds. Differentiating(8) j times proves(4). In particular the largest j=6 bound is O(epsilon^beta), still tending to zero.

The weighted integral is exact:

    integral_0^L r_(G_epsilon)/(wH) dx
      =-B_3 integral_1^2 chi'(t)dt=B_3.

Consequently(4) supplies no contradiction to(3) or(5). It disproves a bound of |B_3| by any of these unweighted residual norms with a constant depending only on this fixed w,g. It does not disprove an error bound in a stronger weighted topology or a theorem using additional global coupling.

## Verification and scope

Independent symbolic code checks the first axis equation, H'/H, the sign in(8), the residual-accounting identity and the rational factor in(6). A numerical manufactured test may sample the cutoffs and rates; it is supplementary to the exact argument. All code is this verifier's implementation. No claim is made about the full density residual R, the canonical velocity generated by an extension of G_epsilon, positivity of such an extension, a global family, or either task endpoint.
