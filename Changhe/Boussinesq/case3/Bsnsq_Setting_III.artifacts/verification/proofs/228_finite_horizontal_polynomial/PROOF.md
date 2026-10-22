# Finite polynomial dependence on the horizontal coordinate is impossible

## Statement and exact scope

Fix beta>0. Let W be C1 on the full plane, with

    div W=2beta,  W(X)=beta X+o(|X|)

uniformly as |X| tends to infinity. Let Theta be C1, solve

    W.grad Theta=(beta-2)Theta,

and have a finite polynomial representation in x on the whole plane:

    Theta(x,y)=sum_{j=0}^N f_j(y)x^j,

where N is one fixed nonnegative integer and every f_j is C1 on R. Then every coefficient f_j with j>=1 is identically zero. In particular, if Theta(0,y)=0 for every y, then Theta is identically zero. Thus no smooth B2 profile with a nonzero quadratic center jet can have finite polynomial dependence on x of globally bounded degree.

No vorticity equation, inverse, parity, sign of Theta, derivative bound at infinity, or normalization W(0)=0 is used. The conclusion is a restricted-class theorem. Polynomial growth at infinity is much weaker than being an exact polynomial in x; the prompt's general polynomially controlled tails are not excluded by this result. A degree that grows without a fixed bound as y varies is also outside the stated hypothesis. No assertion about the x-independent coefficient without the B2 axis condition is needed.

## 1. Choose a nonzero highest coefficient

Suppose some coefficient of positive degree is not identically zero, and take N>=1 to be the highest such degree, deleting identically zero higher coefficients. Write f=f_N and let J be a connected component of the nonempty open set {y:f(y)!=0}. It is an open interval, and f has fixed sign on J. Set

    lambda=beta-2,  K=N beta-lambda=(N-1)beta+2>0.

At a fixed y, as x tends to positive infinity, the global small-o assumption implies

    W1(x,y)/x -> beta,  W2(x,y)/x -> 0.           (1.1)

These are fixed-height limits; no derivatives of asymptotic statements will be taken.

## 2. The highest coefficient cannot have a critical point in J

Suppose f'(y)=0 at a point of J. At that height,

    Theta/x^N -> f,
    Theta_x/x^(N-1) -> N f,
    Theta_y/x^(N-1) is bounded as x -> infinity.

For N=1 the last expression is simply f_0'(y), since the leading derivative vanishes. Divide the temperature equation by x^N. By (1.1), the W1 term tends to N beta f, and the W2 term tends to zero. The right side tends to lambda f. This gives K f=0, contradicting K>0 and f!=0. Consequently f' is nowhere zero on J.

## 3. A finite horizontal limit for the vertical field

At each y in J, Theta_y/x^N tends to f'(y)!=0. For sufficiently large x, the temperature equation can therefore be solved as

    W2(x,y)=[lambda Theta(x,y)-W1(x,y)Theta_x(x,y)]/Theta_y(x,y).

Divide numerator and denominator by x^N and use (1.1). It follows that

    W2(x,y) -> g(y):=-K f(y)/f'(y).               (3.1)

The function g is continuous and nowhere zero on J. The convergence is uniform on every compact subinterval of J: f' stays bounded away from zero there, the finitely many coefficient functions and their derivatives are bounded, and W1(x,y)/x->beta uniformly for y in that compact interval by the full-plane small-o condition. The argument below needs only the endpoint limits in (3.1), but this uniform observation checks that no regularity at infinity is being smuggled in.

## 4. Integrate divergence on long rectangles

Fix a<b in J and integrate div W=2beta over [R,2R] times [a,b]. The ordinary divergence theorem, valid for C1 W, gives exactly

    2beta R(b-a)
      =integral_a^b [W1(2R,y)-W1(R,y)]dy
        +integral_R^(2R) [W2(x,b)-W2(x,a)]dx.     (4.1)

Divide by R and let R tend to infinity. The first integral divided by R tends to beta(b-a): its two W1 terms are 2beta R+o(R) and beta R+o(R), uniformly on the bounded y interval. The second integral divided by R tends to g(b)-g(a). Indeed each W2(x,a) or W2(x,b) converges to its finite limit as x->infinity, so its average over [R,2R] has that same limit. Therefore

    g(b)-g(a)=beta(b-a).

Since a,b were arbitrary in J, there is a constant d such that

    g(y)=beta y+d  on J.                         (4.2)

This derivation uses integrated divergence rather than differentiating a velocity limit or assuming convergence of DU.

## 5. The coefficient cannot end smoothly at either boundary

Equations (3.1) and (4.2) give, throughout J,

    f'/f=-K/(beta y+d).

The denominator is nonzero on J because g is nowhere zero. Integrating this elementary first-order identity gives a nonzero constant c such that

    f(y)=c |beta y+d|^(-K/beta)  on J.            (5.1)

The constant c has the sign of f. The exponent K/beta is strictly positive. At any finite boundary point e of J, continuity of f and maximality of the nonzero component imply f(e)=0. But (5.1) cannot tend to zero as y approaches e from J. If beta e+d!=0, the limit is finite and nonzero. If beta e+d=0, its absolute value diverges. Both contradict continuity with f(e)=0.

Thus J has no finite endpoint, so J=R. But the affine function beta y+d, with beta>0, vanishes at y=-d/beta, contrary to its being nonzero on J. This contradiction excludes any nonzero coefficient of positive degree.

Only f_0 remains. If the B2 axis condition Theta(0,y)=0 holds, then f_0=0 too, proving the asserted exclusion. There is no inference about arbitrary nonpolynomial temperatures or the unrestricted B2 endpoint.

## Dependencies and planned controls

This is a standalone informal proof written before its symbolic controls or model review. It uses finite polynomial asymptotics, the classical divergence theorem on bounded rectangles, the elementary fact that averages on [R,2R] preserve a finite limit, and integration of a scalar ODE. The regularity of the coefficients is stated explicitly and follows automatically for a smooth temperature with a fixed finite polynomial representation, by evaluating at finitely many distinct x values and inverting a fixed Vandermonde matrix.

Exact controls will check the highest coefficient argument, quotient limit, rectangle factors, scalar ODE exponent and boundary alternatives. Manufactured counterexamples outside the hypotheses should be retained: a nonzero polynomial temperature can solve the transport and divergence equations with a linearly growing anisotropic W, but such W fails the required isotropic asymptotic W=betaX+o(|X|). A singular power coefficient of the form (5.1) can hold on a proper half-line, which shows why smoothness and the full y axis matter. Finite controls are not a substitute for the global proof. Formal sources are not compiled because Lean/Lake builds are prohibited.
