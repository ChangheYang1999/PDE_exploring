# A marked regular bracket construction

## Statement

Fix 0<c<1/2 and a finite real omega. Put a=1-2c, kappa=1+c, d=3c and A=cI-omega J. There exist smooth real vector fields B,W,U on R3 such that

    B=Ay+U,  div B=d,  div U=div W=0,  [B,W]=-kappa W.

The field U has compact support, and W is nowhere zero. Both flows are complete. The backward B flow has a nontrivial transitive regular hyperbolic attractor K with exponents -kappa,0,a. Its basin is R3 minus a smooth proper line ell, which is one complete W orbit. The only zero of B is on ell and has eigenvalues kappa,-a/2,-a/2. For every integer j>=0,

    |D^j W(y)|=O(|y|^(-1/c-j)) as |y| tends to infinity.

Constants may depend on c, omega and j. In particular W is not curl U: curl U vanishes on an exterior open set, while W does not.

This is an exact independent-eigenfield construction, not an Euler profile. Its proof uses the published classification theorem specified below. It does not claim an elementary proof of that classification or a numerical verification of topology.

## 1. The surface and the exact suspension

Use the completely analytic construction in the team records with

    K0=(3+sqrt(5))/2,  r=kappa/a,  rho=K0^(-r).

It gives a smooth torus M, a diffeomorphism F, a repelling disc D, a source p, a transitive one-dimensional hyperbolic attractor L, and exact tensors on S=M\int(D):

    F*eta=K0 eta,  DF(Y)=rho Y composed with F,
    d eta=0,  eta(Y)=0,  Y and eta nowhere zero.

The complement M\L is the backward basin of p. The induced homology action is [[2,1],[1,1]]. Take roof T=log(K0)/a. The proof in the team records constructs a smooth trapping exterior N in the closed suspension, with positive volume m and fields

    B=-partial_t,  W=exp(kappa t)Y,  m=exp(-dt)dt wedge nu,
    i_Y nu=eta.

The tensors have been extended to M\{p} by their exact covariance before suspension. Thus they descend with all derivatives. The field -B is strictly inward on the smooth boundary, and B,W are independent and nonzero on N. The required divergence and bracket identities hold there. The maximal invariant set is the transitive suspension K of L.

The remaining issue is a meridian on the actual boundary transverse to span(B,W). An unmarked exterior identification alone would not give it.

## 2. The precise classification input and its hypotheses

Use Jiagang Yang and Bin Yu, arXiv:2004.08921v1, Proposition 4.13, printed pages 22-26. It states that an Axiom A diffeomorphism of T2 whose nonwandering set is one transitive expanding attractor and one isolated fixed repeller, and which is isotopic to the Thom automorphism [[2,1],[1,1]], is topologically conjugate to the standard DA diffeomorphism. The proof in Section 4.3 constructs the conjugacy preserving stable leaves, including the two free stable separatrices of the boundary periodic points. Its external surface-classification input is Theorem 2.3; that external classification is used as a theorem, not reproved here.

Here are the hypotheses for our F. The nested source discs give a fundamental annulus for its punctured source basin. Their iterates cover that basin, and an orbit moves strictly through their levels. Each point other than p is wandering: locally only finitely many adjacent annuli need be considered, and absence of periodicity lets one shrink the neighborhood to avoid the remaining finitely many iterates. Thus NW(F)=L union {p}. Each point of L is nonwandering, since a dense recurrent orbit in L meets every relative neighborhood arbitrarily late.

For periodic density, each nonempty relative open subset of L contains all L-preimages of a sufficiently small old torus rectangle under the construction's collapse P. Choose a nonzero periodic point of the old automorphism in that rectangle. Such points are dense, and none is on the unstable leaf of zero: a point on that leaf tends to zero backward, whereas a nonzero periodic orbit cannot. Its P-preimage in L is unique and is periodic because PF=AP. Hence periodic points are dense in L. The hyperbolic splitting on L and the hyperbolic source p prove the full Axiom A condition. The attractor is transitive, and its local product is a Cantor set times an unstable interval, so it is expanding and one-dimensional.

The orientation-preserving torus mapping class is determined by its integral homology action. This gives the required isotopy class. Every premise of Proposition 4.13 is therefore satisfied.

## 3. The actual plane foliation is preserved

Let h conjugate F to the standard DA diffeomorphism. Using equal roofs, H([x,t])=[h(x),t] is a time-preserving conjugacy of the compact closed suspensions. It carries the source orbit and K to their standard counterparts.

The plane span(B,W) is the weak stable foliation on N. Indeed the exact transport under X=-B is

    D flow_X^t W = exp(-kappa t) W composed with flow_X^t.

The forward orbit of each sufficiently short W segment in N stays in the compact trapping region. Its length therefore decays exponentially, since W is bounded there. Near K the uniformly hyperbolic stable-manifold characterization identifies these curves with the strong stable curves. Every point of N eventually enters a neighborhood of K, so backward transport proves the identification throughout N. Flow saturation gives the weak stable planes. In the surface construction this is also the vertical stable foliation ker eta.

Uniform continuity of H and its inverse on the compact closed suspensions preserves strong asymptotic equivalence. Equivalently one can use the explicit stable-leaf preservation in the proof of Proposition 4.13. After flow saturation, H preserves the weak stable foliation on the basin.

Let N0 be a smooth standard DA trapping exterior. The two boundaries H(partial N) and partial N0 are topologically transverse to the same flow. Every orbit through either boundary runs from the source toward the attractor and crosses each boundary exactly once. Following that orbit gives a boundary homeomorphism. Crossing time tau is continuous, by transverse flow boxes, and bounded by compactness.

This map extends to the exteriors without an assumption at K. In H(N)\K use the unique boundary-time coordinates (q,s), s>=0. Choose a smooth function f with f(0)=1, f(s)=0 for s>=R, and sup|f'| sup|tau|<1. Map the point at time s to the point on the same orbit at time

    s+tau(q)f(s).

This is strictly increasing in s and maps [0,infinity) onto [tau(q),infinity). It is the identity for s>=R. The finite orbit collar with s<=R is compact and disjoint from K. Thus the map and its inverse extend continuously as the identity on K. This proves the exterior homeomorphism and preservation of the boundary weak stable leaves. No derivative of h or H is asserted.

## 4. Marking the leaf, then computing its smooth holonomy

In the standard DA model the induced boundary foliation has two compact leaves. Yang-Yu Proposition 2.6 gives its two Reeb annuli. Their introduction, printed page 4, calls a compact leaf c_v; the proof of Proposition 3.8, printed page 16, explicitly identifies c_v as a meridian of the figure-eight knot exterior. Independently, Christy 1993, Section 6, printed pages 776-777, identifies the two boundary periodic orbits of the suspended Thom DA model as meridians. These are statements about the marked standard model, not just its unmarked homeomorphism type.

Pull one standard compact boundary leaf back by the exterior homeomorphism. It is a genuine compact leaf C of the smooth nonsingular line foliation

    T(partial N) intersect span(B,W).

Consequently C is a smooth embedded circle. The exterior homeomorphism takes its slope to the standard meridian. Composing with the standard embedding makes C meridional for an identification of N with the figure-eight exterior. Equivalently meridional filling along C gives S3. Standard smoothing uniqueness in dimension three lets the exterior identification be chosen smooth in the same boundary isotopy class, preserving this slope.

The topological conjugacy is not used to compute a derivative. For that use the actual smooth form

    theta=i_B i_W m,  L_B theta=-a theta,  L_W theta=0.

The leaf C lies in the free weak stable cylinder of a periodic B orbit. It is essential in that cylinder, as follows from its image in the standard free stable cylinder. Thus its loop is homotopic there to a nonzero integer number of circuits of the periodic orbit. If the orbit period is S0>0, the transverse holonomy derivative along that orbit is exp(-a S0), directly from the displayed pullback identity. Holonomy along homotopic loops is conjugate by smooth transverse holonomy. The derivative along C is therefore exp(plus or minus k a S0) for an integer k>=1. The global orientation of W excludes a twisted stable bundle. In particular the derivative is positive and different from one.

The local argument in the team records now applies. To recall it, write the boundary foliation near C as partial_u+v(u,z)partial_z with v(u,0)=0, and put mu equal to the mean of partial_z v(u,0). Nonunit holonomy says mu!=0. Choose a positive periodic h with h'=(partial_z v(u,0)-mu)h. Then the nearby graph z=epsilon h(u) has transverse difference epsilon mu h+O(epsilon^2), with one strict sign for small nonzero epsilon. This is a smooth embedded transverse circle E isotopic to C. It is a meridian. Since B is transverse to the boundary, E is also transverse to span(B,W).

## 5. Euclidean completion and limits of the result

All hypotheses of in the team records now hold. Its explicit meridian collar has

    W=partial_z, B=partial_r+kappa z partial_z,
    m=h0 exp(-ar) dr du dz.

The polar substitution R^2=(2h0/a)exp(-ar), x=R cos u, y=-R sin u extends this collar over a two-handle with Euclidean volume and

    B=-(a/2)(x partial_x+y partial_y)+kappa z partial_z,
    W=partial_z.

Meridional attachment gives a ball, and the handle has just the claimed zero. Its off-axis points enter N backward; its axis tends backward to that zero. Matching the outgoing flux to a Euclidean sphere and applying an interior relative volume correction gives B=Ay near and outside that sphere for any specified omega. Exterior transport is

    W(exp(As)y0)=exp(-s)exp(-omega J s)W(y0).

This proves the derivative bounds, nonvanishing, completeness and compact support of U. The two axial outgoing orbits and the central zero make the one proper exceptional line. Every other point enters N backward, so its limit approaches K. The construction is a spatial conjugacy on N with no time change, preserving all stated rates and transitivity.

This closes the missing marked-boundary step for this independent bracket model. It does not close W=curl U. That equality is actually false here, and no momentum equation has been obtained.

## Dependencies and evidence

The independent proof uses A233-A234, the specified Yang-Yu Proposition 4.13 and standard-model marking, A183's local transverse perturbation, and A181's explicit completion. The entire Yang-Yu Section 4.3 and the marking passages were read in the actual retained manuscript; Christy's actual Section 6 was also read. Source paths and hashes are in the team records. No numerical computation is a premise. The construction is confirmed as a deduction from these stated classification and topology inputs; no full new proof of the external classification is claimed.
