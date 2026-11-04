# Bounded smooth curves need not be compact in the endpoint Lipschitz norm

Written: 2026-11-02T21:47:31Z. Audit A202: CONFIRMED. This checks LIT42 and a precise source-reading limitation.

## Statement

For every integer r>=2 and epsilon>0 there are smooth embedded curves gamma_j:[0,1]->R2 with uniformly bounded C^r norms and speeds bounded below by 1, but no subsequence converging in the usual C^(r-1,1) norm. They do converge in C^(r-1).

Conversely, a uniformly bounded family in C^(r-1,1) on [0,1], with bounded values, is relatively compact in C^(r-1), and each limit retains the same highest-derivative Lipschitz bound. Thus C1 convergence and uniform Lipschitz first derivatives are available for r>=2. The source application only needs the safer r>=3 choice.

## Proof

Let n_j=2^j and

    phi_j(t)=epsilon (2 pi n_j)^(-r) cos(2 pi n_j t-r pi/2),
    gamma_j(t)=(t,phi_j(t)).

The first coordinate proves injectivity and speed at least 1. For 0<=k<=r,

    sup |D^k phi_j| <= epsilon (2 pi n_j)^(k-r).

All C^r norms are bounded, and derivatives through order r-1 converge uniformly to zero. In particular gamma_j converges in C^(r-1) to the horizontal segment.

But D^r phi_j(t)=epsilon cos(2 pi n_j t). If j<k, at t=1/(2n_j) the j derivative equals -epsilon and the k derivative equals epsilon, since n_k/n_j is even. For a C1 scalar function g on an interval, Lip(g)=sup|g'|, by the mean-value theorem and the definition of derivative. Therefore

    Lip(D^(r-1)(phi_j-phi_k)) >= 2 epsilon.

No subsequence is Cauchy in the C^(r-1,1) norm.

For the converse, the derivatives of order r-1 are uniformly bounded and equicontinuous, and lower derivatives are equicontinuous by the bounds on their next derivatives. Repeated Arzela-Ascoli yields uniform limits for the map and all these derivatives. The fundamental theorem of calculus identifies the limits as successive derivatives of the limiting map. Passing to the limit in the uniform Lipschitz inequality preserves that inequality. This proves C^(r-1) compactness and endpoint regularity of the limits, without convergence in the endpoint Lipschitz seminorm.

## Exact source check

The retained actual manuscript is in the team records, arXiv:2506.18238v2, revised February 2026. Section 3.1, printed page 21, defines C^(r-1,1) regularity with a highest-derivative Lipschitz seminorm. Definition 6.1, page 43, explicitly equips the measured-disk space with the C^(r-1,1) topology and the weak-star measure topology. Definition 6.4, page 44, declares the bounded-geometry subspace compactly contained. Proposition 6.11, pages 46-47, uses that precompactness to extract limiting measured disks.

Uniform finite-regularity bounds alone do not justify that assertion if the named topology means its usual norm topology. The explicit curves prove this general inference false. They are not a demonstration that the particular dynamically produced family lacks an additional compactness property. The inspected definitions do not state such an additional property or explicitly specify a weaker topology on bounded sets.

A possible repair is the weaker C^(r-1) topology on families with uniform C^(r-1,1) bounds. Composition with a fixed smooth map is continuous there, and the limits retain the regularity needed for the local C1 geometric arguments in this agent. Checking every later entropy, measurable-disintegration and compactness step under that repair would be additional work. It has not been completed here.

## Scope and dependencies

The elementary compactness result is proved without external analytic inputs beyond Arzela-Ascoli and elementary calculus. The source theorem itself is neither proved nor refuted by this check. A198 and any later consequence of that theorem remain explicitly conditional on their exact external premises. In particular this issue must not be silently converted into an unconditional Euler theorem or described as a disproof of the generalized Gibbs theorem.
