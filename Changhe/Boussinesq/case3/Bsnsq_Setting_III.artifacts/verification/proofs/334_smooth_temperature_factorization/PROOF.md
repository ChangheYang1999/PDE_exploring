# Smooth temperature factorization at a simple hyperbolic endpoint

Prepared 2026-10-22T09:46:05.503104+00:00, before finite controls. This is a conditional theorem about an actual smooth solution on an open neighbourhood, not a convergence theorem for the formal hierarchy.

## Exact statement
Let W=(x a(x,s),P(x,s)) be a real C-infinity vector field on an open neighbourhood of (0,0) in R^2, invariant under x reflection: a and P are even in x. Assume

    a(0,0)=5,  P(0,0)=0,  P_s(0,0)=-1,
    k=P_xx(0,0)/2.

Let Theta be a real smooth function, even in x, satisfying W Theta=0 and Theta(0,0)=0. For s near0 suppose

    Theta_xx(0,s)/2 = (C/2)s^10 + O(s^11),   C!=0.

Here O(s^11) means a smooth function divisible by s^11, or equivalently the stated Taylor jet for a smooth function. No analyticity is assumed. Then, as germs at the origin and after restriction to a sufficiently small reflection-symmetric neighbourhood:

1. There is a smooth even graph s=H(x), the local unstable manifold of W, with H(0)=H'(0)=0 and H(x)=(k/11)x^2+O(x^4).
2. There is a unique smooth Z with Z_s(0,0)=1 and Theta=(C/2)x^2 Z^10. Its zero set is s=H(x), and Z=(s-H(x))L with L smooth, even in x and strictly positive, L(0,0)=1.
3. WZ=-(a/5)Z. The smooth odd function I=x Z^5 satisfies WI=0 and Theta=(C/2)I^2.
4. Theta is zero exactly on {x=0} union {s=H(x)} and has strict sign C everywhere else in that neighbourhood. Each point of the unstable graph with x!=0 has transverse vanishing order exactly10. Thus Theta has no sign change across either local zero curve.

These are properties of any actual smooth field and temperature satisfying the hypotheses. They neither produce such a solution nor exclude B2 globally.

## Axis vanishing and division by x squared
Evenness gives P_x(0,0)=0, so DW(0,0)=diag(5,-1). Since P(0,s)=-s+O(s^2), it is nonzero for small s!=0. On the invariant axis x=0, WTheta=0 gives P(0,s)Theta_s(0,s)=0. Hence Theta(0,s) is constant on each of the two punctured half-intervals; continuity and Theta(0,0)=0 make both constants zero. Evenness also gives Theta_x(0,s)=0. Taylor's formula with integral remainder in x gives

    Theta(x,s)=x^2 F(x,s),
    F(x,s)=integral_0^1 (1-t) Theta_xx(tx,s) dt.

Thus F is smooth and even, with F(0,s)=Theta_xx(0,s)/2. The divided transport equation is

    x a F_x + P F_s + 2 a F=0.

It first holds for x!=0 by algebra and then everywhere by continuity. This is not cancellation in an integral domain of smooth germs.

## Smooth invariant graph
First restrict to a reflection-symmetric open box around the origin. Apply the smooth local stable-manifold theorem to -W, whose eigenvalues are -5 and1, with stable direction the x axis. This yields a smooth graph H tangent to the x axis. Use precisely the source's local gamma-stable set for -W: forward trajectories stay in a fixed small ball and decay faster than exp(-2t). The theorem states that this set is the graph. Reflection commutes with the flow, preserves the ball and this decay condition, so H is even. Invariance gives

    P(x,H(x)) = x a(x,H(x)) H'(x).

Writing H=h2 x^2+O(x^4), the degree2 coefficient of this equation is k-h2=10h2, so h2=k/11. The graph theorem used here is the sole external dependency: Dutilleul, Theorem1.1 (and its local proof in Section3.3), as pinned in sources/SOURCE.md. The field is defined locally; multiplication by a smooth cutoff equal to1 near0, after reversing time, gives the global-domain hypothesis without changing the local graph germ. The pinned Theorem1.1 assumes a smooth family on R^n with a fixed singularity and a partially hyperbolic splitting. Take the constant parameter family, F the x axis, G the s axis and gamma=-2: -5 < -2 < min(0,1). Its conclusion is one smooth graph on a fixed neighbourhood, not merely a sequence of C^j graphs on shrinking domains; the addendum gives all derivative orders on one neighbourhood. No global derivative bounds are required in Theorem1.1, and the compactly supported cutoff supplies them if needed.

For completeness, any sufficiently small invariant C1 graph tangent to the x axis is this graph germ. Along that graph x'=x a, with 4<a<6 after shrinking. For the reversed field, |x(t)|<=|x(0)|exp(-4t), and a C1 graph tangent to the x axis has |(x,H(x))|<=K|x|. Hence its forward -W orbit stays in a small ball and decays faster than exp(-2t). It belongs to the source's gamma-stable graph; two graph germs with the same x domain are therefore identical.

## Vanishing of ten transverse derivatives
Set q=s-H(x). This is a smooth coordinate change preserving x, with inverse s=q+H(x). Restrict its domain to the inverse image of a symmetric box |x|<epsilon, |q|<epsilon. This gives every segment used by the q-integral and the x-axis scalar ODE. All uniqueness assertions refer to the resulting graph and function germs. In (x,q) coordinates write

    W=x alpha(x,q) partial_x + q d(x,q) partial_q,
    alpha(x,q)=a(x,q+H(x)),
    q d(x,q)=P(x,q+H(x))-x alpha(x,q)H'(x).

The last expression vanishes at q=0, so d is smooth by its integral first-derivative formula. We have alpha(0,0)=5 and d(0,0)=-1. Put f(x,q)=F(x,q+H(x)). Its equation is

    x alpha f_x + q d f_q + 2 alpha f=0.

For j>=0 define f_j(x)=(partial_q^j f)(x,0)/j!. Suppose f_0,...,f_(j-1) vanish identically. Differentiating the displayed equation j times in q and evaluating at q=0 leaves

    x alpha(x,0) f_j'(x)+[2 alpha(x,0)+j d(x,0)]f_j(x)=0.

All other product terms multiply lower f_l or their x derivatives, which are zero. For0<=j<10, after shrinking the x interval, alpha>0 and

    b_j(x)=[2 alpha(x,0)+j d(x,0)]/alpha(x,0) >= delta_j>0.

Any nonzero solution of x f_j'+b_j(x)f_j=0 on0<x<=x0 obeys

    |f_j(x)|=|f_j(x0)| exp(integral_x^x0 b_j(t)/t dt)
             >= |f_j(x0)|(x0/x)^delta_j.

It would be unbounded as x decreases to0, contradicting smoothness. If it is zero at one positive point, uniqueness for the scalar linear ODE makes it zero throughout that half-interval. Thus f_j=0 for x>0. Replacing x by -x proves the same for x<0, and continuity gives f_j(0)=0. Starting with j=0 and inducting proves f_0=...=f_9=0 as actual functions, not only as Taylor coefficients. This argument excludes possible nonzero flat solutions as well.

Taylor's integral remainder now gives

    f(x,q)=q^10 K(x,q),
    K(x,q)=(1/9!) integral_0^1 (1-t)^9 (partial_q^10 f)(x,tq) dt.

K is smooth and even in x. Since H(0)=0 and F(0,s) has the specified leading jet, K(0,0)=C/2. Shrink the neighbourhood so that U=2K/C is strictly positive, and define L=U^(1/10) by the positive real root. Then L is smooth, even, and L(0,0)=1. Substituting q=s-H(x) in Z=q L proves the factorization, zero set and sign assertions. At x!=0 on the graph, its q^10 coefficient in Theta is x^2 K(x,0)!=0, proving exact transverse order10.

## Transport and uniqueness
Differentiate Theta=(C/2)x^2 Z^10. The product rule yields

    0=C x^2 Z^9 [a Z+5 WZ].

On the open set x Z!=0, cancel its nonzero real factors to obtain WZ=-aZ/5. The complement is the union of two smooth curves and has empty interior; continuity extends the identity everywhere. Then W(x Z^5)=xZ^5(a-5a/5)=0. Parity gives I odd.

If Ztilde is another smooth factor with Ztilde_s(0,0)=1, the identity at x!=0 gives |Ztilde|=|Z|; continuity extends this across x=0. Both vanish exactly on the graph. On a small neighbourhood both s derivatives are positive, so they have the same sign as s-H(x), and Ztilde=Z. This proves the asserted germ uniqueness without division in the ring of smooth functions.

## B2 application and boundaries
At beta=2, the prompt thermal equation is W.grad Theta=0. Use s=y_*-y at an actual smooth simple endpoint with b(y_*)=0 and b'(y_*)=-1. The prompt has Psi odd in x, so U1=-Psi_y is odd and U2=Psi_x is even. Since U1(0)=0 and the relative drift subtracts only a constant vertical component, W1 is odd and W2 even. Smooth division gives W1=x a with a even. The divergence identity gives a(0,0)=4-b'(y_*)=5, while the transformed second component P=-W2 has P_s(0,0)=b'(y_*)=-1. If T=Theta_xx(0,y) has leading jet C s^10, as in the relevant simple-end relations, then the theorem applies. The prompt explicitly imposes Theta(0,y)=0 and evenness in x, so Theta(0,y_*)=0 holds at this endpoint. The definition b(y)=W2(0,y) is the actual axis drift, not a separately fitted scalar. The identity div W=4 follows pointwise from W=2X+U-U(0) and div U=0. In the tuned family P321, v1(0)=-k gives P_xx(0,0)/2=k, so the graph curvature agrees with P328 and P331. P321 alone is formal and does not supply the actual smooth solution required here. This theorem does not upgrade P321 to a convergent or smooth solution satisfying the PDE on a neighbourhood.

This is not uniqueness of Theta from the jet. For a fixed odd first integral I, smooth changes such as Theta=(C/2)(I^2+I^4) retain the same leading jet and are allowed; the corresponding factor Z changes. The theorem fixes Z only after W and Theta are fixed.

## Flat perturbation warning for formal data
The actual PDE hypothesis is essential even if every x Taylor coefficient along the axis is specified. Define phi(x)=exp(-1/x^2) for x!=0 and phi(0)=0. Repeated derivatives are polynomials in1/x times phi, so they tend to0 at x=0; phi is smooth, even and flat. For W=(5x,-s), set

    Theta_test=x^2(s^10-phi(x)).

This has Theta_test_xx(0,s)/2=s^10, C=2, the same full x Taylor series along every axis point as the exact first integral x^2s^10, and all formal thermal residual coefficients vanish. However Theta_test(x,0)<0 at x!=0. Direct differentiation gives

    W Theta_test=-(10x^2+10)phi(x),

which is nonzero at x!=0 but flat on the axis. Thus a formal thermal identity alone does not imply the actual sign conclusion. This is a counterexample to that inference, not to the theorem: it fails the actual PDE. It is not a full B2 construction and makes no claim about the vorticity equation or canonical inverse.

The argument uses only the thermal equation, reflection and local hyperbolic data. It does not use the full-plane inverse, far field, vorticity equation or center matching to prove existence. It is a necessary local condition, not a decisive endpoint. General B2 remains OPEN.

No JavaScript/TypeScript, servers/listeners, RLScience cluster, Lean/Lake builds or external posts. Write only in verification.
