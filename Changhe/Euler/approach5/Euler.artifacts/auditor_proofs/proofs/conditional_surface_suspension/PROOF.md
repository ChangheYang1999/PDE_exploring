# Conditional exact suspension of a smooth surface embedding

Written: 2026-11-02T21:49:22Z. A204: CONFIRMED as a conditional implication. Update 2026-11-02T22:30:39Z: A233 now supplies the required surface triple, and A234 identifies the unmarked exterior. The original conditional argument is retained below; its historical statements that the triple remains unconstructed are superseded by in the team records and in the team records.

## Statement and missing input

Let S be a compact smooth once-holed torus. Let lambda>mu>0, delta=lambda-mu, r=lambda/mu, K>1, rho=K^(-r) and T=log(K)/mu. Assume a smooth embedding f:S->int S, a smooth nowhere-zero field Y and a smooth nowhere-zero closed one-form eta satisfy everywhere

    eta(Y)=0,    f*eta=K eta,    Df Y=rho Y composed with f.

Then these data produce a smooth compact three-dimensional trapping region N with one torus boundary, vector fields X=-B and W, and a smooth positive volume m satisfying

    div_m B=delta,    div_m W=0,    [B,W]=-lambda W,

with X strictly inward at its boundary and no zeros, and W nowhere zero. Its maximal invariant set is the suspension of Lambda=intersection_(n>=0) f^n(S), which is hyperbolic with rates (-lambda,0,mu). If the surface attractor is transitive with the requested nontrivial expanding local structure, the suspended set has those properties. They are additional hypotheses for that conclusion.

The manifold is a once-holed-torus mapping torus. An embedding into R3, a specified knot-exterior monodromy and a required meridian condition must be supplied or checked separately. In particular this statement does not construct the desired regular plug in R3.

## Area and cohomological restriction

There is a unique nonvanishing two-form omega with i_Y omega=eta: at each point both sides belong to the one-dimensional annihilator of Y. Choose its positive orientation. Closedness of eta gives L_Y omega=0. Contracting f*omega with Y gives rho f*eta=rho K eta, hence

    f*omega=K rho omega=exp(-delta T)omega.

Thus f preserves orientation. The complement of int f(S) in S is an annulus. Indeed its sole new boundary separates off the embedded genus-one subsurface; the remaining connected surface has two boundary components, genus zero and Euler characteristic zero. Consequently inclusion of f(S) is a homotopy equivalence.

The form eta is not exact. Otherwise eta=du would give u composed with f=Ku+C. Iteration and boundedness of u on S force u to be constant, contrary to eta nowhere zero. Thus [eta] is a nonzero K-eigenvector of the integral automorphism f* on H1-cohomology of S. This automorphism preserves the oriented intersection form, so has determinant one. Its other eigenvalue is K^(-1), giving

    K+K^(-1) is an integer at least 3.

This is a necessary restriction, not an existence theorem for the triple.

## Hyperbolicity of the surface core

Choose a smooth transverse field Z with eta(Z)=1. In the frame (Y,Z),

    Df_x=[[rho,h(x)],[0,K]].

On Lambda, f is invertible. The uniformly convergent series

    p(x)=sum_(j>=1) K^(-1)(rho/K)^(j-1) h(f^(-j)x)

satisfies K p(fx)=rho p(x)+h(x). Therefore the continuous line spanned by Z+pY expands by K, while the line spanned by Y contracts by rho. The frame and its inverse are bounded on compact Lambda. This proves uniform hyperbolicity, independently of transitivity or local Cantor structure.

## Ambient suspension and exact seam

First extend the surface to an open ambient surface U on which f becomes a diffeomorphism F. Take the direct limit of the open embeddings int S -> int S -> ... given by f. Denote its points by [x,n], identifying [x,n]=[f(x),n+1]. Each stage is open and the stages are nested. Any two points lie in one stage and can be separated there by open subsets, proving Hausdorffness; a countable union of countable chart bases proves second countability. The shift

    F[x,n]=[f(x),n],    F^(-1)[x,n]=[x,n+1]

is a smooth diffeomorphism. The map x->[f(x),1] embeds the original compact S and extends its initial interior chart.

Extend the tensors to U using, whenever F^n x lies in int S,

    Y_x=rho^n (DF^n_x)^(-1)Y_(F^n x),
    eta_x=K^(-n) (F^n)*eta_x.

The original covariance identities ensure compatibility on overlaps. On the suspension of F with period T define

    X=partial_t,    B=-partial_t,    W=exp(lambda t)Y,
    m=exp(-delta t) dt wedge omega.

The identification (z,t)->(Fz,t-T) preserves these tensors exactly: Df Y=rho Y, rho=exp(-lambda T), and f*omega=exp(-delta T)omega cancel the exponential factors. The identities hold on full collars, so every derivative matches. Direct differentiation gives the asserted divergence and bracket identities.

## Smooth strictly transverse boundary

In the annulus S minus int f(S), construct a smooth vector field V pointing from the inner to the outer boundary. Choose it on a two-sided outer collar and transport it by F to the inner collar. In annulus product coordinates these prescribed fields have positive radial component, so a partition-of-unity interpolation with a positive radial field supplies V throughout. Thus F_*V=V on the paired collars and every trajectory crosses the annulus.

Multiply V by a common positive constant so all crossing times L(theta) are less than T. In its trajectory coordinates (theta,s), choose a nonnegative smooth beta supported away from the collars with integral_0^L(theta) beta(theta,s) ds=1. Replace V by

    V/[1+(T-L(theta)) beta(theta,s)].

The new crossing time is exactly T. The replacement equals V on the collars, so their compatibility is unchanged.

Let C_t be the image of the inner circle under V at time t and D_t its inner domain. Then D_0=f(S), D_T=S and the domains increase. In the ambient suspension put

    N={(z,t):0<=t<=T, z in D_t}/((z,T)~(f(z),0)).

The collar covariance of V makes its swept boundary smooth across the seam. On the swept annulus let s(z) be its crossing-time coordinate. Locally N is the side t-s(z)>=0, and X(t-s(z))=1. Thus X points strictly inward. The top and bottom faces are identified, leaving one torus boundary.

An isotopy identifying the varying once-holed-torus fibers D_t identifies N with a mapping torus. Its maximal invariant set has phase-zero section Lambda, and therefore is its suspension. Dividing the surface logarithmic rates by T gives (-lambda,0,mu). Transitivity passes from the surface attractor to the constant-roof suspension.

## Scope and dependencies

This proof verifies the seam, boundary and hyperbolicity steps from the smooth triple. It does not supply that triple, smooth switch compatibility, the monodromy, a meridian slope, or the actual-curl Euler relation. The topology and smooth calculus used above are elementary surface and suspension constructions; no classification of arbitrary expanding attractors is invoked. No computational existence assertion is made.
