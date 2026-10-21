# Critical ordinary Holder regularity does not determine the axis obstruction

Date: 2026-10-20. Status: complete informal proof; independent review pending. All conclusions below concern compatible scalar axis data.

## Statement

Fix A>2, beta=2/A in (0,1), L>0, and a smooth compatible pair (w_0,g_0) on [0,L]. Assume w_0 is odd analytic near zero and

    w_0(0)=w_0(L)=0,  w_0'(0)=-A,  w_0'(L)=A,
    w_0<0 on (0,L),  g_0>0 on (0,L],
    w_0 g_0'=(w_0'-A)g_0,  g_0(x)/x^2 -> 1.

Rebuild g_w by the same normalized first equation. Define

    Q_w=(g_w'-w'')/(2g_w^3),  m_w=-w/g_w,
    B[w]=(beta-1)A^(1-beta)/3
        * FP integral_0^L (Q_w-Q_w(L)) m_w^(beta-2)/g_w dx.

The finite part subtracts divergent powers in the physical coordinate x at zero, with no added constant. For an integer k>=0, use the ordinary norm

    ||f||_(C^(k,beta)) = sum_(j=0)^k ||f^(j)||_infinity
        + sup_(x!=y) |f^(k)(x)-f^(k)(y)|/|x-y|^beta

on [0,L]. For every delta in (0,L), epsilon>0 and b in R, there is a smooth compatible pair (w,g_w) such that

    B[w]=b,
    ||w-w_0||_(C^(7,beta)) + ||g_w-g_0||_(C^(8,beta)) < epsilon,

and the pair agrees with the base on [delta,L] and on a neighborhood of zero. Thus B has all real values in every such positive-radius neighborhood, even when all jets at finitely many prescribed axis points and both endpoint germs are fixed. No coupled two-dimensional realization is asserted.

## A weighted derivative lemma

Suppose a continuously differentiable function F on (0,L] extends continuously with F(0)=0 and satisfies

    |F(x)|<=e x^beta,  |F'(x)|<=e x^(beta-1).

Then [F]_(C^beta[0,L])<=C_beta e. To prove this, take 0<x<y, h=y-x. If h>=x/2, then x<=2h and y<=3h, so the amplitude bounds give |F(y)-F(x)|<=e(2^beta+3^beta)h^beta. If h<x/2, integrate F' on [x,y]. Since beta-1<0, the result is at most e h x^(beta-1)<=e h^beta. The case x=0 follows from the amplitude bound. Multiplying the constants in the hypotheses by fixed factors only changes C_beta.

Consequently, if a smooth function u vanishing near zero satisfies

    |u^(j)(x)|<=e x^(k+beta-j),  j=0,...,k+1,

then ||u||_(C^(k,beta))<=C_(k,beta,L)e. The first k derivatives are uniformly bounded by the displayed estimates, and the lemma applies to F=u^(k). This estimate is uniform as the neighborhood on which u vanishes shrinks.

## The exact constraint construction

Choose 0<r_0<min(1,delta)/8. Let chi be smooth, equal to zero on (-infinity,0], equal to one on [1,infinity), with values in [0,1]. Fix a nonnegative nonzero smooth function f supported in (b_0,c_0), where 2r_0<b_0<c_0<delta. For |a|<=M, with M fixed, put

    p_(N,a)(x)=(a/N)x^(7+beta)
        chi(log(r_0/x))chi(N+2-log(r_0/x)),  0<x<r_0,

extended by zero. For all sufficiently large N, define

    I_N(a)=integral_0^L [1/(w_0+p_(N,a))-1/w_0]dx,
    J(t)=integral_0^L [1/(w_0+t f)-1/w_0]dx,
    t_N(a)=J^(-1)(-I_N(a)),
    w_(N,a)=w_0+p_(N,a)+t_N(a)f.

Here J'(0)=-integral f/w_0^2<0, and I_N(a)=O_M(1/N) uniformly, so the same local inverse of J applies to every |a|<=M once N is large. In particular t_N(a)=O_M(1/N). Negativity is preserved. Disjoint supports give exactly

    integral_0^L [1/w_(N,a)-1/w_0]dx=0.

The normalized equation has the exact solution formula

    eta(x)=log(g_(N,a)(x)/g_0(x))
        =log(w_(N,a)(x)/w_0(x))
            -A integral_0^x [1/w_(N,a)-1/w_0]dt.

It implies exact agreement with the base after c_0 and before r_0 exp(-(N+2)). Thus all endpoint hypotheses and both endpoint germs hold.

The obstruction calculation proved in ../origin-fixed-source/PROOF.md, with the uniform amplitude version proved in ../finite-observation-fibers/PROOF.md, gives

    B[w_(N,a)] = B[w_0]+a kappa_A+O_M(1/N),
    kappa_A=(1-beta)(6+beta)(7+beta)/(6A)>0.                 (1)

The error is uniform on [-M,M]. Its leading term follows by two integrations by parts from

    (1-beta)/(6A) integral p_(N,a)'' x^(-6-beta)dx
       =kappa_A integral p_(N,a)x^(-8-beta)dx
       =a kappa_A [1+(2/N)integral_0^1 chi(t)dt].

The subtracted finite-part integrand has an ordinary integrable error bounded by C_M N^(-1)(x+x^(-beta)) near zero. On the fixed interior correction interval it is O_M(1/N); near L the endpoint subtraction gives the integrable bound C_M N^(-1)(L-x)^(beta-1). These bounds justify (1) without assuming continuity of B in any of the norms under discussion. All needed constants depend on the fixed base, cutoffs and M, not on N.

## Uniform ordinary Holder bounds for w

Differentiating in the logarithmic coordinate shows, for each fixed integer j and in particular for j<=9,

    |p_(N,a)^(j)(x)|<=C_(j,M) N^(-1)x^(7+beta-j).

All derivatives of the two cutoff factors to that fixed order are bounded independently of their separation N. The function is flat at both support endpoints, so the inequality holds on the entire interval after extension by zero. The weighted derivative lemma with k=7 therefore gives

    sup_(|a|<=M)||p_(N,a)||_(C^(7,beta))<=C_M/N.

The fixed smooth function f has a fixed C^(7,beta) norm, and |t_N(a)|<=C_M/N. Hence

    sup_(|a|<=M)||w_(N,a)-w_0||_(C^(7,beta))<=C_M/N.        (2)

## Uniform ordinary Holder bounds for the rebuilt density

First, the normalized equation gives

    d_x log(g_0/x^2)=(w_0'-A)/w_0-2/x.

Odd analyticity of w_0=-Ax+O(x^3) makes the right side analytic of order O(x) near zero. Normalization therefore gives g_0=x^2 times a positive analytic function there.

On (0,r_0], the interior correction has not yet occurred. Write sigma=p_(N,a)/w_0. Since w_0=x times a fixed smooth nonzero function there, differentiating a reciprocal and using the preceding bounds gives

    |sigma^(j)(x)|<=C_(j,M) N^(-1)x^(6+beta-j),  j<=9.

For large N, |sigma| is uniformly small. The finite derivative formula for log(1+sigma) consists of a finite sum of products of derivatives of sigma, divided by a bounded power of 1+sigma. A product with q>=1 factors and total derivative order j is bounded by

    C N^(-q) x^(q(6+beta)-j)
        <= C N^(-1)x^(6+beta-j),

because x<=r_0<1. Similarly, the reciprocal difference equals -p_(N,a)/[w_0^2(1+sigma)] and satisfies

    |d_x^j [1/(w_0+p_(N,a))-1/w_0]|
        <=C_(j,M) N^(-1)x^(5+beta-j),  j<=8.

Integrating for eta at order zero and differentiating its exact formula at orders 1 through 9 gives

    |eta^(j)(x)|<=C_(j,M) N^(-1)x^(6+beta-j),  j<=9.       (3)

The same product estimate applies to exp(eta)-1. Multiplication by g_0=x^2 times a fixed analytic function now yields

    |(g_(N,a)-g_0)^(j)(x)|
        <=C_(j,M) N^(-1)x^(8+beta-j),  j<=9,              (4)

on (0,r_0]. To check the product powers, derivatives of g_0 of order 0,1,2 cost at most the corresponding powers of x, while higher derivatives are bounded; their powers in (3) are then at least as favorable as (4).

On [r_0,L], the uncorrected normalized density is lambda_(N,a)g_0 with lambda_(N,a)=1+O_M(1/N). The interior correction is a fixed smooth f with coefficient O_M(1/N), supported where w_0 is bounded away from zero. Differentiating the exact normalized formula on this fixed interval gives C^9 differences O_M(1/N). After c_0 the differences vanish exactly. Since r_0>0 is fixed, increasing a constant extends (4) to all x in (0,L]. The weighted derivative lemma with k=8 gives

    sup_(|a|<=M)||g_(N,a)-g_0||_(C^(8,beta))<=C_M/N.        (5)

No bound on the tenth derivative is needed.

## Exact prescribed value and scope

Let D=b-B[w_0], choose a_-=(D-1)/kappa_A and a_+=(D+1)/kappa_A, and then choose M larger than their absolute values. By (1), for sufficiently large N the value at a_- is below b and the value at a_+ is above b. At each such fixed N, B[w_(N,a)] is continuous in a: the endpoint germs and Q(L) are fixed, so differences of its finite parts are ordinary integrals over a common compact subinterval of (0,L), with smooth parameter dependence and no vanishing denominator. The intermediate value theorem gives an a_N between a_- and a_+ with B[w_(N,a_N)]=b. Choose N still larger so that the sum of (2) and (5) is below epsilon.

For any finite set of prescribed positive axis points, choose delta below their minimum. The pair and all its local derivatives agree at those points because they agree on [delta,L]; at zero they agree as germs. This proves the stated fixed-observation consequence.

The norm statement strengthens the critical weighted-C2 construction for this particular family. It does not infer high derivative bounds from a general weighted-C2 bound. Each constructed pair is smooth, with shrinking inner support; no uniform analyticity neighborhood or stronger Holder exponent is supplied. The argument neither determines a canonical IPM trace nor shows that a profile family exists. It proves no strong-setting endpoint.
