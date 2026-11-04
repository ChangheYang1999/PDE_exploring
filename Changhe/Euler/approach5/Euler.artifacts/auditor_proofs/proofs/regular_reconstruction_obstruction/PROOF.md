# No decaying first integral for the regular bracket model

## Exact abstract theorem

Let B,W be smooth real fields on R3 with complete flows Phi_s and Gamma_t. Suppose:

1. div B=d>0, div W=0 and [B,W]=-kappa W for a constant kappa>0. For every compact Q, the union of Phi_s(Q), s<=0, is bounded.
2. W is nowhere zero, and almost every point is recurrent for Gamma_1 in both time directions.
3. A smooth proper embedded line ell is one complete W orbit. Its complement is the basin of a compact attractor K for X=-B. There is q in K with omega_X(q)=K.
4. The attractor has a compact smooth trapping neighborhood N in this basin, with X strictly inward on its boundary and K its maximal full invariant set. On the basin B,W are independent. On the torus boundary of N, the line foliation T(partial N) intersect span(B,W) has a compact leaf.

Then every smooth real F with W(F)=0 and F(y)->0 as |y|->infinity is identically zero.

For the model in the team records, these hypotheses hold for every 0<c<1/2 and finite omega. For 2/5<c<1/2, its Biot-Savart inverse V cannot be an Euler profile at any nonzero scalar amplitude: [lambda V-U0,W] is nonzero for all real lambda!=0, where B0=(cI-omega J)y+U0 is its constructed carrier.

This is a theorem about the specified bracket model and, more generally, the exact abstract hypotheses above. It does not exclude regular attractors of an arbitrary Euler profile.

## 1. Periodic orbits and the rank of first integrals

The bracket integrates to

    Phi_s Gamma_t = Gamma_(exp(kappa s)t) Phi_s.

If a nonconstant W orbit had period T, its images under Phi_-s would have periods exp(-kappa s)T. All those image loops lie in one compact ball. Let L bound the Lipschitz constant of W there. For any periodic solution z of period tau, subtract its temporal mean zbar and use periodic Wirtinger:

    integral |z'|^2
      = integral (W(z)-W(zbar)) dot z'
      <= L ||z-zbar||_2 ||z'||_2
      <= L tau/(2pi) integral |z'|^2.

A nonconstant orbit has tau>=2pi/L. If L=0 there is no such orbit. The shrinking periods contradict this bound, so W has no nonconstant periodic orbit.

Now let F,G be two smooth W first integrals. If (F,G) had rank two on a nonempty open set O, Sard's theorem and the submersion theorem imply that almost every point of O maps to a globally regular value. To justify the word globally, the critical-value set has planar measure zero, and its preimage in each submersion chart is null by Fubini. Use countably many charts. Recurrence supplies a recurrent point x in O with globally regular value.

Its fiber is a closed embedded one-dimensional manifold. W is nonzero and tangent. A connected component is a circle or a line. A circle gives a periodic orbit. On a line the nonvanishing flow is monotone and cannot return to an intrinsic neighborhood of x. The embedded-submanifold chart identifies this neighborhood topology with the ambient topology near x, so ambient recurrence is also impossible. Completeness removes a finite-time endpoint possibility. Hence

    dF wedge dG=0 everywhere.                                  (1)

## 2. A nonzero first integral would give a trapping torus

Suppose F is nonzero. Decay implies that each nonzero level is compact. Choose a nonzero regular value in the image, and a connected component T of that level. It is a compact oriented embedded surface with nonvanishing tangent field W. Its Euler characteristic is zero, so T is a torus.

Set G=B(F). Then W(G)=[W,B](F)+B(W(F))=0. By (1), G is constant on T. If that constant were zero, B would be tangent to T, contradicting the divergence theorem on its bounded enclosed domain D:

    integral_T B dot n = d |D| > 0.

If the constant is nonzero, B has one strict normal sign on connected T, and the same identity makes that sign outward. Thus X=-B is strictly inward and D is positively invariant. No assumption that D is an unknotted solid torus is needed.

The value of F on ell is constant, since ell is one W orbit. Properness and decay make this value zero. The line is disjoint from T. It cannot enter D: otherwise connectedness and separation would put the entire proper unbounded line inside compact D. Therefore D is contained in the basin of K.

## 3. The compact leaf yields a forbidden periodic W orbit

First K is contained in int(D). A forward X orbit starting in D has a nonempty limit in K intersect D. Its limit cannot meet T, because at T the negative X orbit leaves D. Thus K intersects int(D). The point q whose omega-limit is K eventually enters int(D), since K intersect int(D) is a nonempty relative open subset. It then stays in D. Consequently its omega-limit K lies in D, and invariance together with strict boundary transversality puts K in int(D).

Compact subsets of the basin of an attractor approach K uniformly. Indeed choose a smaller stable trapping neighborhood inside any given neighborhood of K. Every point of a compact basin subset eventually enters its interior. Continuity and a finite subcover give a common upper bound on entry times; forward invariance then gives uniform attraction. It follows that K is the maximal full invariant set in D as well as in N.

Every orbit through T crosses partial N exactly once. In forward time it approaches K and enters either trapping neighborhood. In backward time it must leave either neighborhood unless it lies in K. Strict inward transversality forbids multiple crossings. The same argument starting at partial N proves surjectivity. The implicit function theorem at the transverse crossings gives a smooth orbit map

    h:T -> partial N

with smooth inverse. Its time may have either sign.

The B flow preserves E=span(B,W). The differential of a variable-time orbit map is the fixed-time differential plus a scalar multiple of B. It therefore preserves the boundary line intersections with E. On T, W is tangent and B is transverse, so E intersect TT is exactly RW. Pulling the assumed compact leaf on partial N back by h gives a compact W leaf on T. Since W is nonzero, this is a periodic orbit, contradicting Section 1. Hence F=0.

## 4. Verification for the constructed model

Use A242-A243's fields B0,W. Backward boundedness follows from B0=Ay+U0 with bounded compactly supported U0 and y dot Ay=c|y|^2. The proper exceptional line, its single W orbit, the full basin complement and the compact boundary leaf were proved in the marked completion. Independence transports from N along B0. A forward dense orbit of the surface attractor has omega-limit the entire attractor: its local Cantor-times-interval structure has no isolated points, so each relative open set is visited infinitely often. Its suspension supplies q.

The only remaining hypothesis is recurrence. Set gamma=1/c>2. Exterior transport gives |W(y)|<=C(1+|y|)^(-gamma). Along any W trajectory,

    |d_t(1+|y|)^(gamma+1)| <= C1

in the almost-everywhere sense, including passages through zero. Thus integer iterates up to time n of a bounded set lie in a ball of volume O((1+n)^(3/(gamma+1))). This power is strictly less than one. If E in a bounded set Q never returns to Q at positive integer times, its iterates are disjoint and volume preservation gives

    (n+1)|E| <= C2(1+n)^(3/(gamma+1)).

Therefore E is null. Points with finitely many returns reduce to this case by their last return. Apply the argument to a countable basis of bounded balls and to the inverse flow. Almost every point is recurrent in both directions. This proves the abstract theorem's application without adding an ergodicity assumption.

## 5. Biot-Savart inversion and its leading field

Now assume 2/5<c<1/2, so 2<gamma<5/2. Beyond some sphere of radius R0,

    W(exp(As)y0)=exp(-s)exp(-omega Js)W(y0), |y0|=R0.

Extend this formula to all positive radii, obtaining Wh. It is smooth off zero, locally integrable at zero, and distributionally divergence free. To check the last assertion, its ordinary flux is independent of radius and scales by radius^(2-gamma), hence is zero. Subtracting a test function's value at zero leaves a boundary error O(radius^(3-gamma)), which tends to zero.

D=W-Wh is compactly supported, integrable and divergence free. Testing its divergence against a cutoff equal to y_i on its support gives integral D_i=0. Its first absolute moment is finite.

The Newton potentials of W and Wh converge at infinity since gamma>2; their curls V,Vh satisfy

    div V=0, curl V=W,  div Vh=0, curl Vh=Wh,
    Vh(lambda Q_lambda y)=lambda^(1-gamma)Q_lambda Vh(y),
    Q_lambda=exp(-(omega/c)J log lambda).

The fields are smooth on R3 and R3\{0}, respectively. Since Wh is nonzero, so is Vh. Subtract the constant Biot-Savart kernel term using integral D=0. The first-moment estimate gives

    D^j(V-Vh)=O(|y|^(-3-j))

for each fixed j. In particular V decays and its rotating blow-down converges to Vh. These are the direct potential estimates in the team records; they use no feature of that file's earlier singular model.

## 6. Every nonzero amplitude fails the Euler equation

If lambda V were an Euler profile for lambda!=0, its vorticity lambda W and the curl equation would imply

    [Ay+lambda V,W]+kappa W=0.

Subtracting the exact original bracket gives [lambda V-U0,W]=0. The two fields in this last bracket are divergence free. Hence (lambda V-U0) cross W is curl free, and simple connectivity gives a smooth potential F with

    grad F=(lambda V-U0) cross W.

This is a W first integral. In the exterior grad F=O(|y|^(1-2gamma)). Integration along rays gives finite limits; comparison along large spheres shows that the limits agree. Normalize their common value to zero. Then F=O(|y|^(2-2gamma)). The abstract theorem forces F=0.

Outside the support of U0 this gives V cross W=0. Scaling to infinity using the preceding blow-down, whose velocity error is O(lambda^(gamma-4)), gives

    Vh cross curl Vh=0.                                       (2)

Here the lambda in the error is a positive dilation parameter, independent of the fixed profile amplitude.

For completeness, (2) is impossible for a nonzero real rotating homogeneous divergence-free field H of degree -beta with 1<beta<2. Its stress S=H tensor H-|H|^2 I/2 has zero divergence. Apply div(S y)=tr S=-|H|^2/2 on an annulus. If P and Q are the spherical integrals of |H_rad|^2 and |H_tan|^2 at radius one, the spherical boundary expression is r^(3-2beta)(P-Q)/2. Differentiate the annular identity with respect to its outer radius to get

    (3-2beta)(P-Q)=-(P+Q),
    (2-beta)P+(beta-1)Q=0.

Rotation preserves these spherical integrals. Both coefficients are positive, so H=0. In our case beta=gamma-1 lies in (1,3/2), contradicting Vh!=0. No regularity at the singular origin was used in this annular argument.

Thus [lambda V-U0,W] cannot vanish for any nonzero amplitude. Conversely, a zero vorticity residual would make the smooth momentum residual curl free on R3 and would supply a pressure. The failed condition is exactly the missing Euler equation in this reconstruction, not an unrelated diagnostic.

## Scope and dependencies

The abstract proof uses the stated recurrence, proper-line basin geometry, and compact boundary leaf. The application uses the specifically constructed marked model. A different W or a joint change of carrier and vorticity need not satisfy the same argument. In particular this does not prohibit every decaying Euler profile with a regular attractor.

Sources checked: LIT49's full proof; A242-A243; A181; the potential estimates in A179; the recurrent-rank mechanism of A194; and the real annular stress argument of A191. No numerical computation or formal build enters the deduction. Inspected versions are recorded in the team records.
