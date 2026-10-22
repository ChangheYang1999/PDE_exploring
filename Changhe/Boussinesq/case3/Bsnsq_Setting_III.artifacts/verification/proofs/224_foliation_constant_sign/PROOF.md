# Opposite derivative signs on regular temperature curves

## Statement, notation and scope

Let a be strictly positive and C3 on R, let H be C1 on R, and let W be a C2 vector field on R2. Assume

    Theta(x,y)=H(x/a(y)), div W=4, W(X)=2X+o(|X|),
    W.grad Theta=0, Omega=-curl W,
    W.grad Omega+Omega=Theta_x.

Here curl W=partial_x W2-partial_y W1, and the final two equations hold classically. Let I be a nonempty open interval on which H' is nowhere zero. Put k=x/a(y), A(y)=integral_0^y a(t)dt and V(k,y)=W2(k a(y),y). Transport and divergence imply that

    C(k)=a(y)V(k,y)-4A(y)

is independent of y on I. Then for every k in I with k nonzero,

    H'(k) C'(k)<0.                                  (1)

In particular C cannot be constant on a regular interval. Together with P223, this excludes any exact finite polynomial C on such an interval, including degree0. The sign theorem itself does not require C to be polynomial. It is a necessary condition for this global temperature representation, not an exclusion of all smooth representations or the full B2 class. All beta other than2 and temperatures without the representation remain outside its scope.

For a beta2 B2 field W=2X+U-U(0), all vector-field hypotheses have the specified moving-center and negative-curl signs. No zero-center gauge, y parity, vorticity sign or inverse choice is added. The proof uses the transport equations and sublinear relative velocity. The base point of A changes C only by a constant and therefore does not change (1).

## Exact coordinate equations

Define Q=W1(k a(y),y)-k a'(y)V(k,y). The change of variables is a global diffeomorphism. Direct differentiation gives

    W.grad Theta=H'(k)Q/a,
    Q_k+(aV)_y=a div W=4a,

where y derivatives hold k fixed. Since H' is nonzero on I, Q=Q_k=0 on I times R. Integration over finite height intervals proves the claimed independence of C. For D(k,y)=4A(y)+C(k), the field in that strip is

    W2=D/a, W1=k a'D/a.

Physical derivatives are partial_x=a^-1 partial_k and partial_y at fixed x equals partial_y at fixed k minus (k a'/a)partial_k. Consequently, with B=a''/a-2a'^2/a^2,

    Omega=4k a'+k D B-(1+k^2 a'^2)C'/a^2.           (2)

The formula follows by subtracting partial_x W2=C'/a^2 from partial_y W1=4k a'+kDB-k^2 a'^2 C'/a^2. It uses the prescribed negative curl, not the opposite convention.

Fix k0 in I with k0 nonzero. In the remainder D(y)=4A(y)+C(k0), v(y)=D(y)/a(y), and

    p(y)=a'(y)v(y)/a(y), h=H'(k0)/k0, g=C'(k0)/k0.

The constants h and g are finite, and h is nonzero. Since D'=4a, differentiation gives

    v'=4-p, a p'=4a'+DB.                           (3)

Define r(y)=Omega(k0 a(y),y)/k0. Formula(2) becomes

    r=a p'-g(1+k0^2 a'^2)/a^2.                     (4)

Along W, k remains k0 and y evolves by y'=v(y). Thus the vorticity equation reduces exactly to

    v r'+r=h/a.                                   (5)

All quantities used here have the classical regularity needed for these derivatives. No approximation or expansion in k is made.

## The regular curve contains a unique equilibrium

Because D'=4a>0, D is strictly increasing and has at most one zero. Suppose it has no zero and is positive everywhere. For every Y<0,

    integral_Y^0 a(t)dt=(D(0)-D(Y))/4<D(0)/4.

Therefore a is integrable on the negative half-line. In particular there exists a sequence y_j tending to negative infinity with a(y_j)<=1: otherwise a would eventually exceed1 and its integral would diverge. At X_j=(k0 a(y_j),y_j), the first coordinate is bounded and |X_j|/|y_j| tends to1. The global growth assumption implies

    v(y_j)=W2(X_j)=2y_j+o(|y_j|)<0

for all sufficiently large j, contradicting D/a>0. If D is negative everywhere, integrate D'=4a over the positive half-line to obtain a sequence y_j tending to positive infinity with a(y_j)<=1; sublinearity then gives v(y_j)>0, the opposite contradiction. Thus D has one and only one zero y_*. Since a>0, v has the same zero and the sign of y-y_*. At that point p=0 and v'=4.

For every initial height y0, the scalar trajectory y'=v(y), y(0)=y0 exists for all negative times and converges to y_*. Indeed, unless y0=y_*, the backward trajectory moves monotonically within the compact interval with endpoints y_* and y0. Local existence and uniqueness for the C1 field v prevent a finite negative-time escape or crossing of y_*. Its backward limit must be a zero of v, since otherwise its speed is bounded away from zero near that limit. The unique possible limit is y_*. The trajectory at y_* is constant.

## Sign supplied by vorticity transport

On the backward trajectory, equation(5) reads

    d/ds [exp(s)r(y(s))]=exp(s) h/a(y(s)).

The path remains in a compact height interval. The positive continuous a has a positive minimum there, and r is bounded there. Integrating from s=-T to0 and sending T to infinity is justified by these bounds. It yields

    r(y0)=h integral_(-infinity)^0 exp(s)/a(y(s)) ds. (6)

The integral is finite and strictly positive. Therefore r(y) has the strict sign of h for every y, including y_*. This argument does not assume any sign of the original vorticity over the plane.

## A same-sign derivative would force a bounded scale end

Suppose for contradiction that h g>=0. From(4),

    p'=r/a+g(1+k0^2 a'^2)/a^3.

Since a is positive and r has the strict sign of h, p' also has that strict sign everywhere. If h>0, p is strictly increasing through p(y_*)=0. Thus p has the sign of y-y_*, as does v. At y different from y_*, the identity a'/a=p/v shows a'>0. At y_*, equation(3) gives p'=4a'/a, so a'>0 there as well. Hence a is strictly increasing and is bounded above on every negative half-line. If h<0, p is strictly decreasing, so the same calculation gives a'<0 everywhere and a is bounded above on every positive half-line.

Such a bounded end is impossible already under temperature transport. To see this without an external lemma, first suppose a(y)<=M for y sufficiently large. Along the same curve x=k0 a(y), the first coordinate is bounded, so v(y)=2y+o(y). Put S(y)=a(y)v(y)=D(y), with S'=4a. For sufficiently large positive y,

    y<=v<=3y, 0<S<=3My, S'/S=4/v>=4/(3y).

For any fixed sufficiently large Y, integration gives S(y)>=S(Y)(y/Y)^(4/3), contradicting S(y)<=3My. If a is bounded above on a negative end, reflect y to -y and W to (W1(x,-y),-W2(x,-y)). Temperature transport, divergence4 and the asymptotic field2X are preserved, so the same positive-end argument applies. No vorticity reflection convention is needed in this last transport-only step.

This contradiction rules out h g>=0. Hence h g<0, which is equivalent to H'(k0)C'(k0)<0 since k0^2>0. The arbitrary choice of k0 proves(1).

## Corollary and limitations

A constant C has C'=0 at every regular nonzero k, contradicting(1). Any nonempty regular open interval contains a nonzero point. Therefore constant C is excluded even if that interval includes0. P223 independently excludes every nonconstant finite polynomial C by its highest coefficient and a positive scalar ODE. Combining the two complete arguments excludes all exact finite polynomials on a regular interval. P223 alone did not settle degree0; this is a subsequent strengthening, not a reinterpretation of its earlier scope.

The condition(1) leaves many smooth nonpolynomial functions available. In the x-even B2 situation H and C are even where defined symmetrically, so their derivatives vanish at0; this theorem makes no assertion at a point with H'=0. Approximate polynomial fits and finite spline pieces do not imply an exact polynomial transport constant. No B2 candidate, full nonexistence endpoint or numerical existence result follows.

## Verification plan and dependencies

This standalone argument is complete before symbolic code. The checker will differentiate the physical field with general C, verify(2)-(5), the compact trajectory integrating factor, the identity at the unique equilibrium, the sign implication and the bounded-end comparison. The zero existence and backward compactness arguments are supplied above and cannot be certified by finite samples. An actual Opus5.5 review will be sought, with its model metadata, visible advice and independent adjudication preserved. The polynomial corollary additionally depends on P223; the sign theorem does not.
