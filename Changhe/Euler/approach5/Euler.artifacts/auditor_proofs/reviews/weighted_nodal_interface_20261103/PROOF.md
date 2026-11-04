# Exact tests of weighted nodal-interface hypotheses

Status: independently checked. The elementary claims below are proved. The manuscript comparison concerns specified definitions and one literal polynomial adjective, not a certification or rejection of either complete paper. Read before the harmonic-weight continuation review.

## 1. Statements and spaces

Fix a real number a with 0<a<1. Coordinates on the plane are (x,y). On any bounded open set, H1(|u|^a) means the completion of smooth functions in the norm whose square is the integral of |u|^a times the sum of the squared function and its squared gradient. The local space is defined on relatively compact sets.

The first claim is that

    w(x,y)=y|y|^(-a), with w(x,0)=0,

is continuous, belongs to H1_loc(|y|^a), and satisfies div(|y|^a grad w)=0 on the whole plane in distributions. It is not C1 and does not satisfy the weak equation separately on either half plane for all compactly supported smooth tests crossing y=0.

For the second claim put

    u=xy, v=(x^2-y^2)/2,
    z=v^2-u^2/(1+a).

Then z is a smooth degree-four polynomial in H1_loc(|u|^a). It satisfies the weak equation separately on every component of {u!=0}, including tests that meet its nodal boundary. It has no representation z=P(v,u) with P an ordinary harmonic polynomial. It has such a representation with P harmonic for the weighted operator div(|t|^a grad P) in coordinates (s,t).

## 2. The first weak solution and its energy

For y!=0,

    grad w=(0,(1-a)|y|^(-a)),
    |y|^a grad w=(0,1-a).

The displayed derivative is locally integrable because a<1. Integration by parts separately on |y|>epsilon, followed by epsilon tending to zero, shows that it is the distributional derivative too: the possible jump term is zero because w is continuous at zero. Its weighted flux is constant, so its divergence on the whole plane is zero.

The two energy densities are

    |y|^a w^2=|y|^(2-a),
    |y|^a |grad w|^2=(1-a)^2 |y|^(-a).

Both are integrable near the interface. To verify completion membership explicitly, replace the function on |y|<epsilon by epsilon^(1-a)F(y/epsilon), where F is smooth, equals t|t|^(-a) near |t|=1 and outside that interval, and has bounded derivative inside. The weighted gradient error in this strip is bounded by a constant times epsilon^(1-a), and the weighted function error by a constant times epsilon^(3-a). Multiplication by a compact smooth cutoff gives approximation on any fixed relatively compact set. Thus this is a solution in the actual energy space.

For a compact smooth test phi, integration in y gives

    integral_(y>0) |y|^a grad w.grad phi
        =-(1-a) integral_R phi(x,0) dx.

The lower half plane gives the opposite sign. A test with nonzero trace integral has nonzero flux on both components. The whole-plane cancellation therefore proves no separate zero-flux condition. The derivative w_y is unbounded as y tends to zero, proving the asserted failure of C1 regularity.

## 3. The quartic and its separate boundary terms

Direct differentiation gives

    Delta u=Delta v=0,
    grad u.grad v=0,
    |grad u|^2=|grad v|^2=x^2+y^2=r^2,
    Delta z=2a r^2/(1+a),
    grad u.grad z=-2u r^2/(1+a).

Consequently, away from u=0,

    div(|u|^a grad z)
      =|u|^a[Delta z+a(grad u.grad z)/u]=0.

The polynomial z itself is smooth, so it belongs to the local weighted completion: the positive weight is locally bounded, and compact smooth cutoffs give admissible representatives. Its degree is four and its growth is at most C(1+r)^4.

Fix one nodal quadrant and a compact smooth test. Integrate the preceding equation on its truncation |x|>epsilon and |y|>epsilon, within a large box on whose outer boundary the test vanishes. On each new inner side, the flux is bounded by C epsilon^a because grad z is bounded on the test support and |xy|^a<=C epsilon^a. The side lengths remain bounded. These boundary contributions tend to zero. The interior integral converges by dominated convergence. There is no point boundary contribution at a corner. Thus the weak integral vanishes separately in the chosen quadrant. The same argument treats the other three and summing proves the whole-plane equation.

## 4. The representation and the precise contradiction

Let P0(s,t)=s^2-t^2/(1+a). Then

    Delta P0=2a/(1+a)!=0,
    div(|t|^a grad P0)=0.

The latter holds componentwise as in Section3; in particular P0 is even in t. The map (x,y) to (v,u) identifies with the complex square map (x+iy)^2/2 and is onto the whole plane. If z=P(v,u), it follows that P=P0 at every point of the coordinate plane. Thus no ordinary harmonic P can give the representation. A different additive constant in the harmonic conjugate translates its first coordinate and does not change this Laplacian obstruction. Reversal or rotation of the conjugate coordinate system does not change it either.

This is an exact counterexample to the ordinary-harmonic interpretation, not to the weighted-harmonic interpretation. It satisfies even the stronger componentwise solution definition.

## 5. What was checked in the primary manuscripts

The pinned manuscripts are Terracini, Tortone and Vita, *A priori regularity estimates for equations degenerating on nodal sets*, arXiv2404.06980v3, and *A priori Holder estimates for equations degenerating on nodal sets*, arXiv2507.18991v1. The verification manifest records their hashes and the relative source locations. No abstract substitutes for the manuscript text here.

The rendered printed page9 of the first and page16 of the second require the weak integral separately on every nodal component when the exponent is below1 in the permitted range. Their weights have the form |u|^a with u solving the uniformly elliptic equation specified there. The simple whole-plane example in Section2 does not meet this componentwise definition, so it contradicts no theorem formulated with that definition.

The rendered printed page5 of the first manuscript gives the ordinary-harmonic wording in Theorem1.3(ii). Its printed page47 proof instead obtains a polynomial by applying the weighted classification in part(i). Sections3-4 disprove the literal ordinary-harmonic wording and support the need to retain the weighted operator in its interpretation.

The scope note also distinguishes an a priori regularity estimate, which assumes the corresponding regularity, from a theorem that first proves it. The targeted continuation propositions use a flat half-ball interface, a block-diagonal Lipschitz uniformly elliptic matrix, and homogeneous conormal data. Their cited frequency and regularity inputs have not been independently certified in this review. Only targeted text ranges and the four recorded rendered pages were checked; this is not a full-paper audit.

## 6. Campaign scope and dependencies

No Euler field or actual tail is constructed by these examples. In particular, neither the full rotating similarity equation nor the actual pressure relation, scattering realization, vorticity transport and twisted homogeneity are supplied. An arbitrary scalar S cannot be inserted into the manuscript theorem merely because an equation with |S|^a is visible off its zero set. Its elliptic equation, coefficient class, energy class and separate conormal terms need proofs.

All elementary claims in Sections1-4 depend only on the displayed derivatives, integrability, one-dimensional integration and surjectivity of the complex square. The source comparison is limited as stated in Section5. The proposed Euler application remains open.
