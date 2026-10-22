# A vorticity obstruction for polynomial transport constants

## Exact statement and restricted scope

Let a be a strictly positive C3 function on R and H a C1 real function. Let Theta(x,y)=H(x/a(y)). Suppose W is a C2 vector field on R2 satisfying

    div W=4, W(X)=2X+o(|X|),
    W.grad Theta=0,
    Omega=-curl W, W.grad Omega+Omega=Theta_x,

where curl W=partial_x W2-partial_y W1. Let I be a nonempty open interval on which H' is nowhere zero. Put k=x/a(y), A(y)=integral_0^y a(t)dt and V(k,y)=W2(k a(y),y). Temperature transport and divergence imply that

    C(k)=a(y)V(k,y)-4A(y)

is independent of y for k in I. Assume, in addition, that C agrees on I with a nonconstant real polynomial of finite degree n>=1. Then no such fields exist.

In particular a smooth beta2 B2 profile with a global temperature representation of this form cannot have a nonconstant polynomial transport constant on even one regular k interval. This is a restricted representation theorem. General smooth C, a locally constant C, temperatures without this global representation and all beta other than2 are outside the conclusion. There is no inference that a numerical spline or an approximate polynomial satisfies this exact hypothesis. No full B2 endpoint is claimed.

A change of the base point defining A only adds a constant to C and preserves the nonconstant polynomial condition. The proof needs the vorticity equation and sublinear velocity. It uses neither parity nor the inverse operator, and never assumes U(0)=0. For a B2 field, curl W=curl U and W=2X+U-U(0)=2X+o(|X|), so the hypotheses have the stated sign and moving-center interpretation.

## Transport coordinates and vorticity identity

Set Q(k,y)=W1(k a(y),y)-k a'(y)V(k,y). The map (k,y) to (k a(y),y) is a diffeomorphism. Direct chain differentiation gives

    W.grad Theta=H'(k)Q/a,
    Q_k+(aV)_y=a div W=4a.

Since H' is nonzero on I, Q=Q_k=0 on I times R. Integrating (aV)_y=4a at fixed k proves the asserted independence of C. With D(k,y)=4A(y)+C(k), the field on that strip is

    W2=D/a, W1=k a'D/a.

Physical derivatives become partial_x=a^-1 partial_k and partial_y at fixed x equals partial_y at fixed k minus (k a'/a)partial_k. Hence

    partial_x W2=C'/a^2,
    partial_y W1=4k a'+kD(a''/a-2a'^2/a^2)-k^2 a'^2 C'/a^2.

Write B=a''/a-2a'^2/a^2 and E=a'^2/a^2. The sign convention Omega=-curl W then gives

    Omega=4k a'+k D B-(a^-2+k^2 E)C'.                 (1)

All y derivatives in what follows fix k. Along W, k'=0 and y'=D/a. Since Theta_x=H'/a, the vorticity equation is

    D Omega_y+a Omega=H'(k).                         (2)

Differentiate (1), using D_y=4a, and put P=2a'/a^3 and F=4a''+5aB. Equation (2) becomes the exact polynomial identity on I

    H'(k)=k[B' D^2+F D+4a a']
          +C'[P D-a^-1-k^2(E'D+aE)].                (3)

The highest coefficient of this identity, not a truncation in k, is decisive.

## Highest polynomial coefficient

Write C(k)=c_n k^n+lower powers, c_n nonzero. For each fixed y, the right side of (3) is a polynomial in k of degree at most2n+1. Its coefficient at k^(2n+1) is

    c_n^2 [B'(y)-n E'(y)].                           (4)

Indeed the two terms producing that degree are kB'C^2 and -k^2 E'C'C. All other terms have degree at most max(n+1,2n-1), strictly less than2n+1 for n>=1. No assumption that H is polynomial is needed initially: at one reference height (3) makes H' equal that finite polynomial on I. Comparing with any other height, equality of polynomials on a nonempty open interval forces equality of all their coefficients. Thus (4) is a constant independent of y. Dividing by c_n^2 and integrating in y gives real constants alpha,d such that

    a''/a-(n+2)(a'/a)^2=B-nE=alpha y+d.              (5)

This step does not extrapolate the polynomial C beyond I. It compares polynomials which agree on I and holds for every y because the regular strip extends over the entire real line.

## Positive scalar ODE

Define z(y)=a(y)^(-(n+1)), which is positive and C2 on R. Direct differentiation of (5) gives

    z''+(n+1)(alpha y+d)z=0.                         (6)

We give an elementary classification sufficient here. A positive C2 function cannot satisfy z''+q(y)z=0 on a positive ray on which q(y)>=q0>0. In that case z''<0, so z' is strictly decreasing. If z' becomes negative it stays at most a fixed negative number, forcing z to cross zero in finite distance. If z' stays nonnegative, then z>=z(Y)>0 and z''<=-q0 z(Y), forcing z' to become negative. Both cases contradict positivity. Reflection y to -y proves the same fact on a negative ray.

If alpha is nonzero, the coefficient in (6) is bounded below by a positive constant on one of the two rays, impossible. Thus alpha=0. If d>0 the same argument applies. If d=0, z is affine; positivity on the whole real line makes z a positive constant. If d<0, put kappa=sqrt(-(n+1)d)>0. Then z=p exp(kappa y)+q exp(-kappa y). This formula follows by solving the two first-order equations obtained from z''=kappa^2 z. Positivity on the whole line forces p,q>=0 and not both zero, by inspecting the two exponential limits. Therefore z tends to positive infinity on at least one end. In either remaining case, a=z^(-1/(n+1)) is bounded above on at least one vertical end. For d=0 it is constant; for d<0 it tends to0 on such an end.

## Sublinear transport forbids a bounded scale end

For completeness this uses only one regular value k_* in I. Let V(y)=W2(k_* a(y),y) and S(y)=a(y)V(y)=4A(y)+C(k_*). Then S'=4a. Suppose first a(y)<=M for y sufficiently large. Since x=k_*a(y) is bounded on this curve, sublinearity gives V(y)=2y+o(y). For all sufficiently large y>0,

    y<=V(y)<=3y, 0<S(y)<=3My,
    S'(y)/S(y)=4/V(y)>=4/(3y).

Integrating from a fixed sufficiently large Y yields S(y)>=S(Y)(y/Y)^(4/3), contradicting the upper bound3My. If a is bounded above on the negative end, use t=-y, a_tilde(t)=a(-t), and W_tilde(x,t)=(W1(x,-t),-W2(x,-t)). Divergence4, transport and the asymptotic field2(x,t)+o(sqrt(x^2+t^2)) are preserved. The same positive-end argument applies. This contradicts the consequence of (6), proving the theorem.

## Dependencies, verification and limits

The argument is complete before symbolic code. Its transport-coordinate identity is independently rederived here; the bounded-end lemma also appeared in the lead's A143 audit and is reproved rather than assumed. The new step is the highest coefficient of the full vorticity identity, followed by positivity of the scalar ODE. The proof uses calculus, elementary polynomial uniqueness and the explicit constant-coefficient ODE solutions; the variable-coefficient exclusion has been supplied without citing an oscillation theorem.

Planned checks independently differentiate the physical field to confirm the sign and formula (1), derive (3), extract the highest coefficients for several finite degrees, and verify the exact general derivative transformation and scalar comparison. Those finite-degree examples support but do not prove the general degree argument, which is supplied above. An actual Opus5.5 adversarial review and follow-up will be recorded, with any corrections preserved. No Lean/Lake build, external solver, server, JavaScript, GPU or RLScience cluster is used.

The assumption that C is nonconstant and exactly polynomial on a regular interval is substantial. This does not prove that all globally separable B2 temperatures are impossible, and does not settle the full smooth beta2 problem. A manufactured smooth transport field from P220 has C=-k^2 near the center and obeys the other transport/inverse/jet conditions, but fails the vorticity equation exactly. Its behavior is consistent with this obstruction, not evidence for it.
