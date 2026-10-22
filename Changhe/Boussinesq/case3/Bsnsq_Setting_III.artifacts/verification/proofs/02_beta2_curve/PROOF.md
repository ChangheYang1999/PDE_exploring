# The local equilibrium curve at beta=2

Status: proved necessary condition, not a global exclusion. Independently checked on 2026-10-20.

## Statement, hypotheses and notation

Let Theta and W be C^3 near the origin, with W(0)=0, div W=4, curl W=-Omega, and

    W.grad Theta=0,    W.grad Omega+Omega=Theta_x.

Assume Theta is even in x, Theta(0,y)=0, Theta(x,y)=a x^2+O(|(x,y)|^3), a!=0. Assume W1 is odd and W2 even in x, and DW(0)=diag(0,4), as forced by the B2 center identities at beta=2.

There is a unique local graph y=h(x) of W2=0 through the origin. It is even, h(0)=h'(0)=0, and W vanishes everywhere on this graph. The eigenvalues of DW on the graph are 0 and 4. Write b=Theta_xxy(0)/2, so the temperature cubic term is b x^2 y. Then

    h(x) = (a^2+b)/(4a) x^2 + o(x^2).

## Proof of the equilibrium curve

Since W2_y(0)=4, the implicit function theorem gives a C^3 graph W2(x,h(x))=0. Its derivative at zero is -W2_x(0)/W2_y(0)=0. Evenness of W2 and local uniqueness give h(-x)=h(x).

The temperature jet implies Theta_x(x,h(x))=2a x+O(x^2). This is nonzero for small nonzero x. On the graph, W.grad Theta=0 reduces to W1 Theta_x=0. Thus W1 vanishes there for x!=0; it also vanishes at zero by hypothesis. Consequently W(x,h(x))=0.

Differentiating this vector identity shows that DW annihilates the nonzero tangent (1,h'). Therefore zero is one eigenvalue. Its trace is div W=4, giving the other eigenvalue.

## Proof of the curvature identity

At P=(x,h(x)), abbreviate s=h'(x), p=Theta_x(P), q=Theta_y(P), A=W1_y(P), and B=W2_y(P). Differentiating W(P)=0 along the curve gives

    DW(P) = [[-sA, A],[-sB,B]].

The trace condition is B-sA=4. The vorticity equation at an equilibrium gives Omega(P)=p. Since curl W=-Omega, it follows that A+sB=p. Solving these two linear equations yields

    A=(p-4s)/(1+s^2),    B=(4+sp)/(1+s^2).

Differentiate W.grad Theta=0 in y at P. Since W(P)=0, the result is A p+B q=0. Hence

    p^2-4sp+(4+sp)q=0,
    s=(p^2+4q)/(p(4-q))

for sufficiently small nonzero x, when its denominator is nonzero. Taylor expansion and h(x)=O(x^2) give p=2a x+o(x^2) and q=b x^2+o(x^2). Therefore s=(a^2+b)x/(2a)+o(x). Integrating from zero proves the asserted expansion for h.

## A local consistency test

For arbitrary constants a!=0 and V, the polynomial fields

    Theta=a x^2,
    Psi=2xy-(a/3)x^3+Vx,
    Omega=2a x,
    U=(-2x,2y-a x^2+V),
    W=(0,4y-a x^2)

satisfy every displayed profile equation and parity condition at beta=2. Direct differentiation gives -Delta Psi=Omega, W.grad Omega=0, Omega=Theta_x, and W.grad Theta=0. The equilibrium curve y=a x^2/4 agrees with the curvature formula when b=0.

These fields violate U=o(|X|), including through both their linear strain and their quadratic vertical velocity. They are not admissible full-plane B2 candidates. Their purpose is to disprove any proposed local contradiction or any claim that zero PDE residual alone certifies the full-plane inverse class.

## Dependencies and scope

This proof uses the implicit function theorem, the profile equations, Taylor expansion, and the trace/curl identities. It uses no center-manifold theorem or whole-plane inverse. The graph is local. Nothing here establishes a compact global equilibrium curve or rules one out. The full beta=2 class remains open.
