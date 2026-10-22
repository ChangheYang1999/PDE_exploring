# Exclusion of a global separated temperature foliation at beta2

## Statement and exact scope

Let a:R->(0,infinity) be C3 and H:R->R be C1 and nonconstant. There is no C2 vector field W on R2 satisfying, classically,

    Theta(x,y)=H(x/a(y)),  div W=4,  W(X)=2X+o(|X|),
    W.grad Theta=0,
    Omega=-curl W=partial_y W1-partial_x W2,
    W.grad Omega+Omega=Theta_x.

The small-o statement is global as |X| tends to infinity. No inverse assumption or parity is needed for this exclusion. In particular it excludes smooth beta2 B2 profiles with this global temperature representation. A nonzero B2 temperature center jet implies H is nonconstant. This is a restricted-class theorem: a general smooth even temperature x²F(x²,y) need not have this representation. No conclusion for beta different from2 or for representations holding on only part of the y axis is asserted.

The proof first bounds the regular set of H using horizontal infinity. It then propagates the exact equations to a critical curve at a boundary of that set. Along this curve the vorticity source vanishes, forcing a scalar monotonicity that conflicts with vertical infinity. These are identities at finite points followed by separately justified limits. Numerical sampling is not part of the proof.

## 1. Coordinates and regular strips

Set k=x/a(y), A(y)=integral_0^y a(t)dt, and, in coordinates (k,y),

    V(k,y)=W2(k a(y),y),
    Q(k,y)=W1(k a(y),y)-k a'(y)V(k,y).

The coordinate map is a global diffeomorphism. Direct differentiation gives

    W.grad Theta=H'(k)Q/a,
    Q_k+(aV)_y=a div W=4a.                         (1)

The y derivative on the left fixes k. Let E={k:H'(k)!=0}, an open nonempty set. Nonemptiness follows from the mean value theorem and nonconstancy of H. On each open component I of E, temperature transport gives Q=0 on I times R, and therefore Q_k=0 there. Define the global C2 function

    C(k)=a(0)W2(k a(0),0).

Integration of (1) over finite y intervals yields, on every such strip,

    D(k,y)=4A(y)+C(k),
    V=D/a,  W1(k a(y),y)=k a'D/a.                  (2)

The same definition of C works on all components. We do not use temperature transport to assert Q=0 in the interior of the critical set.

## 2. The regular set is bounded in both directions

Suppose there is a sequence k_j in E tending to positive infinity or to negative infinity. At every fixed y, x_j=k_j a(y) tends to the corresponding horizontal infinity. The global small-o assumption implies W1(x_j,y)/x_j tends to2 in either case. From (2),

    W1(x_j,y)/x_j = a'(y)[4A(y)+C(k_j)]/a(y)^2.   (3)

If a' vanished at one height, this would contradict that limit at that height. Thus a' is nowhere zero. Fix one reference height y1. Equation (3) implies C(k_j) tends to the finite constant

    C_infinity=2a(y1)^2/a'(y1)-4A(y1).

The identical sequence C(k_j) occurs in (3) at every other fixed height. Consequently

    4A(y)+C_infinity=2a(y)^2/a'(y)

for every y. Differentiate the C1 identity to obtain

    4a=4a-2a² a''/(a')².

It follows that a''=0. An affine function positive on the whole real line is constant, contrary to a' being nowhere zero. This contradiction applies to either sign of horizontal infinity, so E is bounded above and below.

## 3. Extension to a critical boundary curve

Choose a nonempty component I=(l,r) of E. Both endpoints are finite. At least one endpoint k0 is nonzero, since l<r. Choose such an endpoint. Continuity of H' gives H'(k0)=0: otherwise k0 would be an interior point of E and not an endpoint of its component.

The identities (2) extend to k=k0 for every finite y. More explicitly, the compositions of W and the right sides of (2) are C2 functions in (k,y). They agree on I times R. Their difference and each of its first derivatives are zero there, and continuity makes these differences zero on {k0} times R. Also Q and Q_k vanish on this boundary. This reasoning relies on closure from the regular strip, not on division by H'(k0). It validates both the field and its first derivative identities at the critical curve. Omega is C1 because W is C2.

For completeness, the physical differentiation operators are

    partial_x=a^-1 partial_k,
    partial_y at fixed x=partial_y at fixed k-(k a'/a)partial_k.

Applying these to (2), and then extending to k0, gives, with B=a''/a-2(a'/a)^2,

    Omega(k a(y),y)=4k a'+k D B-(1+k² a'²)C'(k)/a²    (4)

at k=k0 and on the regular strip. Indeed partial_x W2=C'/a² and partial_y W1=4k a'+kDB-k² a'² C'/a². This checks the required negative-curl convention.

From now on k=k0 is fixed. Put

    D(y)=4A(y)+C(k0),  v(y)=D(y)/a(y),
    p(y)=a'(y)v(y)/a(y),  g=C'(k0)/k0,
    r(y)=Omega(k0 a(y),y)/k0.

All constants and functions are well defined because a>0 and k0!=0. Direct differentiation and (4) yield

    D'=4a,  v'=4-p,
    a p'=4a'+DB,
    r=a p'-g(1+k0² a'²)/a².                       (5)

The extended Q=0 identity means that the curve x=k0 a(y) is invariant under W, and its height solves y'=v(y). Applying the classical vorticity equation on this curve, with Theta_x=H'(k0)/a=0, gives

    v r'+r=0.                                    (6)

No derivative of H' is required. The derivative r' exists by the C1 regularity of Omega and the smooth curve. The equality in (4) along the entire curve can also be differentiated in y, using a in C3.

## 4. A unique equilibrium and backward compactness

Since D'=4a>0, D is strictly increasing and has at most one zero. Suppose it has none. If D is positive everywhere, then for Y<0,

    integral_Y^0 a(t)dt=(D(0)-D(Y))/4<D(0)/4.

Hence a is integrable on the negative half-line, and there exists y_j tending to negative infinity with a(y_j)<=1. Otherwise a would eventually be greater than1, contradicting integrability. At X_j=(k0 a(y_j),y_j), the first coordinate is bounded. Sublinearity gives

    v(y_j)=W2(X_j)=2y_j+o(|y_j|)<0

for sufficiently large j, contrary to v=D/a>0. If D is negative everywhere, integrate D'=4a on the positive half-line to get a sequence y_j tending to positive infinity with a(y_j)<=1; sublinearity then gives v(y_j)>0, again a contradiction. Because a continuous nowhere-zero D has one sign, these exhaust the no-zero case.

There is therefore exactly one zero y_* of D. The function v has the same zero and has the sign of y-y_*. At y_*, p=0 and v'=4. For every initial height y0, the trajectory y'=v(y), y(0)=y0 is defined for all negative times and converges to y_*. If y0!=y_*, its backward path is monotone and stays in the compact interval with endpoints y_* and y0. The locally Lipschitz v prevents crossing y_*, and compactness prevents a finite backward escape. Its backward limit must be a zero of v, because otherwise its speed near the limit would be bounded away from zero. At y0=y_* the trajectory is constant.

Along this compact backward path, (6) gives

    d/ds [exp(s)r(y(s))]=0.

The continuous r is bounded on that compact interval. Taking s to negative infinity forces the constant to be zero. Thus r(y0)=0 for every y0, and r is identically zero. This step needs neither a global bound on vorticity nor a sign of vorticity.

## 5. The scale must be monotone or constant

Substituting r=0 in (5) gives

    p'=g(1+k0² a'²)/a³.                           (7)

If g>0, p is strictly increasing through p(y_*)=0. Away from y_*, both p and v have the sign of y-y_*, so a'/a=p/v>0. At the zero itself (5) gives p'=4a'/a, and hence a'>0 there too. Thus a is strictly increasing and is bounded above on every negative half-line.

If g<0, p is strictly decreasing through zero. The same identities give a'<0 everywhere, so a is bounded above on every positive half-line. If g=0, then p'=0 and p(y_*)=0 imply p=0 everywhere. Since v is nonzero except at y_*, a'=0 away from that point, and continuity gives a'=0 at it as well. Then a is constant. In every case a is bounded above on at least one end of the real line.

## 6. No bounded scale end is possible

This final contradiction uses the already extended identities D=a v and D'=4a on the critical curve, together with the full sublinear asymptotic field. It does not use nonzero H' at that curve.

First suppose a(y)<=M for all sufficiently large positive y. Along x=k0 a(y) the horizontal coordinate is bounded, so v(y)=2y+o(y). For sufficiently large y,

    y<=v(y)<=3y,  0<D(y)<=3My,
    D'(y)/D(y)=4/v(y)>=4/(3y).

Fix a sufficiently large Y. Integrating the last inequality gives

    D(y)>=D(Y)(y/Y)^(4/3),

contradicting the preceding linear upper bound as y tends to infinity.

If instead a is bounded above on a negative end, set t=-y,

    a_tilde(t)=a(-t),  D_tilde(t)=-D(-t),
    v_tilde(t)=-v(-t).

Then D_tilde=a_tilde v_tilde, D_tilde'=4a_tilde, and v_tilde(t)=2t+o(t) as t tends to positive infinity along the bounded-width curve. The identical positive-end argument applies. These are scalar changes of variable in the transport identities; no convention for reflecting vorticity is being assumed.

Both possibilities from Section5 are impossible. The assumed vector field W therefore does not exist.

## Dependencies, verification and limitations

This is a standalone informal proof. The coordinate and fixed-height argument were first developed in P218; the compact trajectory and sign argument were developed in P224. Every step needed here has been restated and proved. P223's polynomial assumption is absent. Neither a sampled profile nor a numerical inverse is used in the exclusion, and the full-plane inverse can only impose additional conditions on an already excluded field.

The new step is continuity from a regular strip to a nonzero critical boundary curve. A transport-only plateau example can satisfy the other geometric assumptions, as P220 and P222 demonstrate, but it fails the vorticity equation used in Section4. H constant is excluded from the statement; W=2X, Omega=0 and constant Theta show that this exclusion is necessary. A positive scale defined only on part of R also lies outside the statement. Temperatures not expressible through the specified one-variable foliation remain open in this work, as do the prompt's other remaining parameter and tail classes. This result is not a decisive endpoint.

The argument is written before its symbolic controls and before a requested adversarial actual Opus5.5 review. Verification should test the physical derivative signs, closure hypotheses, both horizontal tails, the zero and compact-trajectory arguments, the g=0 case and the scalar end reflection. Finite controls cannot replace those global arguments. Formalization is not attempted because Lean and Lake builds are prohibited.
