# A C2 comparable scalar with nonintegrable normalized derivative

## 1. Exact countertest

Fix 2/5<c<1/2 and define

    eta=(1-2c)/(2-2c), gamma=1-2eta=c/(1-c),
    b=(1+gamma)/2, a=gamma/b.

Then 0<eta<1/6, 2/3<gamma<b<1, b>2/3 and 0<a<1. On a product box containing0 in R3, with coordinates(x,y,z), define for x>0

    f(x)=exp(-1/x^2), t(x)=exp(b/x^2),
    A(x)=2+sin t(x), S(x)=-f(x)^2 A(x), V=f(x)e_2.

Extend f and S by zero for x<=0. Then V is smooth and divergence free, S is C2 but not C3 at x=0, all its derivatives through order2 vanish there, and

    |S|/3<=|V|^2<=|S|, (curl V).grad S=0.

The normalized vector beta=|S|^(-eta)V, defined to be zero on S=0, is continuous and infinitely flat in value on the plane, but is not W1,1 on any open product box crossing that plane. This disproves a Sobolev-extension claim based only on the displayed regularity, comparability and transport premises. It does not disprove LIT264, whose C3 scalar version and full tail structure are different hypotheses.

## 2. Exact regularity and the transport identities

Every derivative of f on x>0 is a polynomial in1/x times f, so the zero extension is smooth with all jets zero at0. Since V has only a y component depending on x, div V=0 and curl V=f'(x)e_3. Since S depends only on x, its gradient is orthogonal to this curl. The bounds1<=A<=3 give the two-sided comparison, including the zero set.

For j=0,1,2, repeated differentiation of S gives finitely many terms bounded near0 by

    C_j x^(-M_j)exp(-(2-jb)/x^2).

Indeed each derivative of a trigonometric factor introduces at most one extra factor t and a power of1/x; all other factors have the same property. Because b<1, these bounds tend to zero faster than every power. Difference quotients successively across0 therefore give a C2 extension with all derivatives through order2 zero there.

At x_n defined by t(x_n)=2pi n, the term with three differentiated phase factors in S''' is f(x_n)^2(t'(x_n))^3, with magnitude

    8b^3 x_n^(-9)exp((3b-2)/x_n^2).

Here t'=-2b x^(-3)t. All other terms at these points have fewer factors t, and their ratios to this magnitude tend to zero: polynomial factors in1/x cannot overcome the lost exponential factor. Since3b-2>0, |S'''(x_n)| tends to infinity. Hence S cannot extend as a C3 function across0. This calculation concerns continuity of the third derivative, not merely existence of a third difference quotient at the plane.

## 3. Infinite variation of the normalized form

The nonzero component of beta on x>0 is

    B(x)=f(x)^gamma A(x)^(-eta).

Since A is between1 and3, B extends continuously by zero, with infinite value order. In the strictly monotone variable t=exp(b/x^2),

    B=t^(-a)(2+sin t)^(-eta), 0<a<1.

Its derivative satisfies the lower bound

    |dB/dt| >= eta 3^(-eta-1)t^(-a)|cos t|
                  -a t^(-a-1).

This follows by the reverse triangle inequality, using1<=2+sin t<=3. The second term has a finite integral on every positive half-line. The first has an infinite integral: each sufficiently late period contains an interval of fixed positive length where |cos t|>=1/2, and the contributions dominate a positive constant times the divergent series sum n^(-a). Therefore integral_T^infinity |dB/dt|dt=infinity for every finite T>0.

On each closed x interval bounded away from0, B is smooth and the monotone substitution preserves its derivative variation. Taking the endpoint to0 proves integral_0^epsilon |B'(x)|dx=infinity. In three dimensions, any W1,1 weak derivative would coincide on the positive half-box with this classical derivative. Its integral there is infinite by Fubini. Thus beta is not W1,1 on any box crossing the plane. No distribution supported on the plane can repair this failure of integrability on the open half-box.

## 4. Missing Euler structure and exact scope

Let J(x,y,z)=(-y,x,0) and X=(cI-omega J)(x,y,z). Its contraction is

    X.V=(cy-omega x)f(x),

which is not identically zero on an open box for any c>0 and real omega. The required twisted homogeneity fails as well: for omega!=0 its transverse component fails wherever f!=0; for omega=0 it would require cxf'=-(1-c)f, whereas cxf'/f=2c/x^2>0. The normalized form is not closed on the positive half-box, since its curl is B'(x)e_3 and B is nonconstant.

There is also no pressure which makes U=V a full rotating Euler profile. A necessary vorticity residual is

    [f'(x)+(cx+omega y)f''(x)]e_3.

For omega!=0 its y coefficient cannot vanish because f'' is nonzero for sufficiently small positive x. For omega=0 the residual equals

    f(x)[(2-6c)x^(-3)+4c x^(-5)]e_3,

which is nonzero for small positive x whenever c>0. This checks the full-equation obstruction independently of the contraction. The example also lacks three-dimensional spatial decay.

LIT266 is therefore CONFIRMED as a limitation of the comparability-only normalized-root extension. A possible C2 scalar theorem using the full tail equations remains OPEN; the example establishes no necessity of C3 for an Euler nonexistence theorem. The sufficient C3 version in LIT264 remains unaffected. No numerical calculation, new source theorem or formalization was needed.
