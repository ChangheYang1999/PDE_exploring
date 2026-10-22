# Supercritical exclusion for a global separated temperature with a quadratic center jet

## Statement and scope

Fix beta>2. Let a:R->(0,infinity) be C2 and H:R->R be C2, with

    H(0)=H'(0)=0, H''(0)!=0.

There is no C1 vector field W on R2 satisfying all of

    Theta(x,y)=H(x/a(y)),
    div W=2 beta, W(0,0)=0, W(X)=beta X+o(|X|),
    W.grad Theta=(beta-2)Theta.

The small-o condition is global at infinity: sup over |X|>=R of |W(X)-beta X|/|X| tends to0 as R tends to infinity. The theorem requires neither the vorticity equation nor the full-plane inverse. Every smooth beta>2 B2 field with the stated global representation and nonzero quadratic temperature center jet satisfies these hypotheses. Indeed B2 defines W=beta X+U(X)-U(0), so W(0)=0; div U=0 gives div W=2 beta; and U=o(|X|) makes U(X)-U(0)=o(|X|) as |X| tends to infinity. The physical quadratic coefficient is H''(0)/(2a(0)^2). No reflection in y is introduced; evenness in x is not needed beyond the specified center jet. The conclusion excludes this representation, not arbitrary smooth B2 temperatures.

The endpoint beta=2 is outside this proof: one crucial scale exponent reaches1 there. P225 proposes a separate argument using the vorticity equation for beta2. No subcritical assertion is needed here. This is a partial result in the full problem.

## 1. Transport coordinates on a regular interval

Write lambda=beta-2>0, k=x/a(y), A(y)=integral_0^y a(t)dt and

    V(k,y)=W2(k a(y),y),
    Q(k,y)=W1(k a(y),y)-k a'(y)V(k,y).

The coordinate identities are

    W.grad Theta=H'(k)Q/a,
    Q_k+(aV)_y=2 beta a.                           (1)

For a regular k with H'(k)!=0, put

    q(k)=lambda H(k)/H'(k), d(k)=2 beta-q'(k).

Since H is C2, q is C1 on each regular interval. Equations(1) give Q=a q and, after integration in y,

    a(y)V(k,y)=d(k)A(y)+C(k),
    W1(k a(y),y)=a(y)q(k)+k a'(y)V(k,y),           (2)

where C(k)=a(0)W2(k a(0),0). The integration constant is well defined even at nonregular k as a C1 function of k. No second derivative of q is used.

Let h2=H''(0), nonzero. Taylor's formula with the available regularity gives

    H(k)=h2 k²/2+o(k²), H'(k)=h2 k+o(k),
    H''(k)=h2+o(1).

Thus H' is nonzero on a sufficiently small punctured neighborhood of0. There,

    q(k)->0,
    q'(k)=lambda[1-H(k)H''(k)/H'(k)²]->lambda/2.

Define q(0)=0 and q'(0)=lambda/2. The first equality also gives q(k)/k->lambda/2, so q extends C1 across0. Set

    alpha=lambda/2=(beta-2)/2,
    d0=2 beta-alpha=1+3 beta/2.

Taking k to0 in the first identity of(2), using continuity and W2(0,0)=0, gives the exact axis identity

    v0(y):=W2(0,y)=d0 A(y)/a(y).                  (3)

This follows from limits of regular strips, so it does not divide by H'(0). The second identity likewise gives W1(0,y)=0, consistently with B2 symmetry.

## 2. The scale grows at both ends but more slowly than |y|

On the positive axis, sublinearity gives v0(y)/y->beta. Since A(y)>0 for y>0, (3) gives

    y a(y)/A(y)=d0 y/v0(y)->delta=d0/beta.

Write gamma=delta-1=1/2+1/beta. Because beta>2,

    0<gamma<1.

Fix epsilon with0<epsilon<min(gamma,1-gamma). For y sufficiently large and positive,

    (delta-epsilon)/y <= A'(y)/A(y) <= (delta+epsilon)/y.

Integrate from a fixed large Y to y. There are positive constants c,C such that

    c y^(delta-epsilon) <= A(y) <= C y^(delta+epsilon).

Also beta y/2<=v0(y)<=2 beta y eventually. Combining with a=d0 A/v0 yields new positive constants c1,C1 such that

    c1 y^(gamma-epsilon) <= a(y) <= C1 y^(gamma+epsilon). (4)

Since gamma-epsilon>0 and gamma+epsilon<1, this proves

    a(y)->infinity, a(y)/y->0, a(y)y->infinity

as y tends to positive infinity. These are inequalities derived from the axis equation, not a differentiated asymptotic ansatz or an assumed power law.

For the negative end put t=-y, a_tilde(t)=a(-t), A_tilde(t)=-A(-t), and v_tilde(t)=-v0(-t). Then A_tilde'=a_tilde, A_tilde>0 for t>0, and v_tilde=d0 A_tilde/a_tilde with v_tilde/t->beta. The same proof yields(4) with t=|y|. Consequently a tends to infinity at both ends, while a(y)=o(|y|).

## 3. Vertical infinity forces the regular transport coefficient

Let I=(0,L), with L possibly infinite, be the component of the positive regular set {k>0:H'(k)!=0} adjacent to0. Such a component exists by the quadratic center jet. Fix any k in I. As y tends to positive infinity, x=k a(y)=o(y), so |(x,y)|/y->1. The global sublinear assumption gives

    V(k,y)/y->beta.

On the other hand, (2) and (3) give

    V(k,y)/y=d(k) A(y)/(a(y)y)+C(k)/(a(y)y)
               ->d(k) beta/d0.

The constant term tends to zero because a(y)y tends to infinity by Section2. Hence d(k)=d0 and

    q'(k)=alpha

for every k in I. Integrating this C1 identity and using q(k)->0 at0 yields q(k)=alpha k. As lambda>0, its defining equation then becomes

    H'(k)=2H(k)/k.

Equivalently (H(k)/k²)'=0 on I. The center limit fixes the constant, giving

    H(k)=h2 k²/2, H'(k)=h2 k   on I.              (5)

If L were finite, continuity would give H'(L)=h2 L!=0. Then L would lie inside the positive regular set, contradicting that it is the finite endpoint of its component. Therefore L=infinity. Formula(5) holds for every positive k. No assumption about H at infinity was used to reach it.

## 4. A scale minimum contradicts horizontal infinity

The continuous positive function a tends to infinity at both ends by Section2. It therefore attains a global minimum at some finite height y_m. Since a is differentiable, a'(y_m)=0.

For every k>0, the second identity of(2) and q(k)=alpha k give

    W1(k a(y_m),y_m)=a(y_m)alpha k.

Thus W1(x,y_m)/x=alpha for all x>0. But at that fixed height the global sublinear assumption implies this ratio tends to beta as x tends to positive infinity. This is impossible because

    beta-alpha=1+beta/2>0.

The contradiction proves the theorem.

## Dependencies and verification plan

Every step is given above. The argument uses the same coordinate divergence identity as P218 but neither its beta2 proof nor P225 is a logical dependency. In particular the scale minimum is forced here by the exact axis relation and beta>2, not by an unproved monotonicity of the flow. W(0)=0 is the moving-center identity and does not impose U(0)=0 on the canonical velocity. The local coefficient h2 belongs to H, while a is the positive scale; the physical quadratic coefficient is h2/(2a(0)^2), nonzero as required.

The informal proof is complete before symbolic checks and model review. Planned independent controls include the divergence and temperature identities in physical coordinates, the C2 center quotient limit, the axis exponent bounds, scalar reflection, the fixed-k vertical limit and quadratic solution, and the final ratio contradiction. The global comparison and endpoint continuation are mathematical arguments, not finite numerical tests. No formalization is claimed; Lean/Lake execution is prohibited. This theorem cannot decide the entire prompt because the representation is restrictive.
