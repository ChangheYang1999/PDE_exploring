# Forward growth in a derivative-bin curve cover

Auditor verdicts: A393 CONFIRMS Sections1-5 and A394 CONFIRMS Sections6-8 at the exact written hypotheses. A395 keeps the coverage upgrade OPEN. Audited 2026-11-03T01:52:53Z.

## 1. Exact hypotheses and conclusions

Fix an integer r>=2, a dimension m>=1, eta=1/100 and D=50/49. Let g be a C^r map on an open neighborhood of a regular C^r curve gamma:[-1,1]->R^m. Norms of vector derivatives are Euclidean operator norms. Let M>=1 bound ||Dg|| on that neighborhood. Choose 0<epsilon<=1 such that

    epsilon^(j-1) sup ||D^j g|| <= M,     2<=j<=r.          (1)

Assume, with s=sup|gamma'|>0, that

    s<=epsilon,     sup|gamma^(j)|<=eta s,  2<=j<=r.       (2)

We call a curve satisfying the derivative comparison in (2) bounded, and call it small if its maximum speed is at most epsilon. For each integer l define the tangent-expansion bin

    E_l={t: e^l <= |(g gamma)'(t)|/|gamma'(t)| < e^(l+1)}.

For every nonempty E_l there is a finite family of increasing affine maps theta_i from [-1,1] into [-1,1] with these properties. A constant C_r depends only on r, with the displayed eta,D fixed; it does not depend on m, g, l, M, epsilon or higher derivatives after (1).

1. The intervals theta_i([-1,1]) have disjoint interiors, cover E_l, and each meets E_l. They need not cover the entire input interval.
2. Every affine slope is at most 1/100. The output curves g gamma theta_i are small and bounded. The restricted input curves gamma theta_i are also small and bounded.
3. Tag an output large if its maximum speed is at least epsilon/3. Every large output has length between epsilon/2 and 2epsilon. The number of outputs not tagged large is at most

       C_r (M e^(-l))^(1/(r-1)).                         (3)

   The total number of outputs is at most

       C_r max(e^l,(M e^(-l))^(1/(r-1))).                (4)

4. The arclength Jacobian of g on each input interval has distortion at most D^2<2.

The construction requires no inverse derivative bound. It even applies to a noninvertible g, because it only covers a bin with positive tangent expansion. For the dynamical statements below we separately assume a diffeomorphism with bounded inverse derivative.

## 2. Vector Taylor approximation on the scale of the chosen bin

Boundedness gives s/D<=|gamma'|<=s. Indeed integrate gamma'' between any point and a maximum-speed point, a distance at most two. Affine restrictions of slope b<=1/D preserve boundedness: their derivative-to-speed ratio in order j>=2 is at most eta D b^(j-1)<=eta.

Put F=g gamma. The chain rule and (1)-(2) give

    sup|F^(r)| <= A_r M s,                              (5)

where A_r depends only on r. Each chain-rule term with j derivatives on g contains products of curve derivatives bounded by a constant times s^j. For j>=2 use s^(j-1)<=epsilon^(j-1) and (1); the j=1 term uses (2). The finite scalar combinatorial coefficients do not depend on m.

Fix delta=1/100. Nonemptiness of E_l implies e^l<=M, so R_l=M e^(-l)>=1. Set

    N=ceil((A_r D R_l/delta)^(1/(r-1))),
    v=e^l s/D,     w=v/N.

Increasing A_r if necessary makes N>=1 and N<=C_r R_l^(1/(r-1)). Divide [-1,1] into N equal intervals and normalize each by an affine map of slope 1/N. Denote the resulting curve by F_I. Then

    sup|F_I^(r)| <= delta w.                            (6)

Let P be the vector Taylor polynomial of F_I' at zero of degree r-2. Taylor's formula with integral remainder gives

    sup|F_I'-P| <= delta w/(r-1)! <= delta w.            (7)

For r=2 this is just the constant polynomial F_I'(0), and (7) follows by integration of F_I''. This degree choice uses only the asserted C^r regularity.

At a point of the normalized interval corresponding to E_l,

    w <= |F_I'| < D e w.

Hence at such a point

    (1-delta)w <= |P| < (D e+delta)w.                    (8)

## 3. Two polynomial cuts and bounded derivatives

Consider the closed set in the normalized interval where

    (1-2delta)w <= |P| <= (D e+2delta)w.                 (9)

The two boundary polynomials are |P|^2-((1-2delta)w)^2 and |P|^2-((D e+2delta)w)^2. Each has degree at most 2(r-2). A nonzero polynomial has at most its degree many real roots; an identically zero polynomial adds no cuts. Thus (9) is a union of at most C_r closed intervals and isolated points. Discard every component that does not meet E_l. By the strict margins in (8), an isolated point cannot meet E_l. The retained nondegenerate intervals cover the portion of E_l in this normalized interval, including possible endpoints.

Throughout every retained interval, (7) and (9) imply

    (1-3delta)w <= |F_I'| <= (D e+3delta)w.              (10)

Normalize a retained interval by an affine map of slope b<=1, obtaining G. Its minimum speed m_G satisfies

    m_G >= b(1-3delta)w,
    sup|G'| <= b(D e+3delta)w,
    sup|G^(r)| <= b^r delta w <= b delta w.              (11)

We use the following elementary interpolation estimate:

    max_(2<=j<=r) sup|G^(j)|
       <= B_r(sup|G'|+sup|G^(r)|).                     (12)

For completeness, apply Taylor's formula to H=G', using degree r-2 at zero and the bound on H^(r-1). For r>=3, evaluate at r-1 equally spaced fixed points in [-1,1]. Inverting their fixed Vandermonde matrix bounds every Taylor coefficient in vector norm by a constant times sup|H|+sup|H^(r-1)|. Taylor's formula applied to each derivative of H then bounds its supremum by the same quantity. All matrix coefficients are scalar; the vector estimate follows by the triangle inequality. The final derivative is already on the right. For r=2, (12) is immediate.

Equations (11)-(12) yield

    max_(2<=j<=r) sup|G^(j)| <= B'_r m_G.                (13)

Choose an integer K_r>=100 with B'_r/K_r<=eta. Divide each G interval into K_r equal pieces. After normalization their derivative-to-maximum-speed ratios in orders j>=2 are at most B'_r K_r^(-(j-1))<=eta. These curves are bounded. Their original affine slopes are at most 1/(N K_r)<=1/100. The number of these intermediate pieces is at most C_r N.

## 4. Speed normalization and the two counts

Let H be one intermediate bounded curve and t_H=sup|H'|. If t_H<=epsilon, retain it. If t_H>epsilon, subdivide its parameter interval into L=ceil(t_H/epsilon)>=2 equal pieces. The new maximum speeds are at most epsilon and at least

    t_H/(D L) > epsilon/(2D) > epsilon/3.

Thus every new piece is large. It remains bounded by the affine restriction estimate. Consequently each intermediate curve contributes at most one output that is not large. This proves (3).

By (10), before final speed normalization every intermediate curve has maximum speed at most C e^l epsilon/N, where C is a fixed constant; the further component and K_r slopes only reduce this bound. It therefore produces at most 1+C e^l/N outputs. There are at most C_r N intermediate curves. Their total number is at most

    C_r(N+e^l) <= C'_r max(R_l^(1/(r-1)),e^l),

which proves (4) after enlarging C_r. Discard final intervals missing E_l. All remaining intervals still have disjoint interiors and cover E_l. Only interval restrictions and subdivisions have been used, so no interior overlap has been introduced within the chosen bin.

A bounded large curve has minimum speed at least epsilon/(3D), hence length at least 2epsilon/(3D)>epsilon/2. Its maximum speed is at most epsilon, giving length at most 2epsilon. The input and output parameterizations of every final interval are bounded, so the ratio of their speeds has distortion at most D^2. This proves the remaining conclusions of Section 1.

## 5. Different bins: a bounded overlap fact, not a partition claim

Each selected interval for bin l lies in the enlarged tangent-speed band

    [(1-3delta)e^l/D, (D e+3delta)e^l].                 (14)

This follows from (10) after undoing its affine normalization, and from s/D<=|gamma'|<=s. The logarithmic width of (14) is less than two for the stated constants. Thus a given point lies in intervals of at most three integer bin labels, and in at most two intervals for any fixed label. The combined family over all bins has multiplicity at most six.

This bounded overlap is useful, but it does not turn the combined family into an interval partition. In particular, intersections of a geometric interval with the set of points having one prescribed derivative itinerary need not be intervals. We retain that distinction below.

## 6. Iteration and actual derivative itineraries

Assume now that g is a C^r diffeomorphism of R^m, with bounded derivatives through r and bounded first derivative of its inverse. Use M=max(1,||Dg||). Start with one straight curve of speed epsilon, tagged large. Iterate the preceding construction, giving children the integer label l of their bin on the current image curve and retaining only nodes meeting their full actual derivative itinerary.

At every parent, the children of one prescribed next label have disjoint interiors. Therefore, for each fixed finite derivative word, the resulting original intervals have disjoint interiors, are nested along its prefixes, and cover all points realizing that word. Apart from the countable collection of geometric interval boundaries, each point follows a unique path whose labels are its actual derivative bins. Different words can still have overlapping geometric intervals; the unique actual path is selected by the bins of the point itself.

Every depth-n interval has small bounded parameterizations at all times 0<=k<=n, since subsequent restrictions have slopes at most 1/100. Its time-k image has diameter at most 2epsilon 100^(-(n-k)). Any restricted iterate has distortion at most D^2 by comparing its bounded endpoint parameterizations. In particular, on any such interval, one-step logarithmic Jacobians oscillate by less than one. These assertions concern entire geometric intervals, not only their assigned itinerary subsets.

Let q be a finite bound for the number of possible derivative bins; the inverse derivative bound supplies one. The upper bound for each bin is L=log M. Define a hyperbolic time j for a point x by

    sum_(i=s)^(j-1) l_i(x) >= h(j-s)  for every 0<=s<j,

where 0<h<alpha<=L. Let G_n(x) count those hyperbolic times j<=n whose actual depth-j curve is large. Put

    theta=(alpha-h)/(L-h),
    gamma_*=(r h-log M)/(r-1)-log C_r.                  (15)

If gamma_*>0 and 0<beta<theta, then normalized original arclength lambda satisfies

    lambda{sum_(i<n)l_i>=alpha n, G_n<beta n}
      <=2 exp(n[log(32q)-gamma_*(theta-beta)]).          (16)

At any counted large hyperbolic time j, every point of its geometric interval has tangent expansion from time s to j at least exp((h-1)(j-s)).

## 7. Proof of the finite-time estimate

Fix a derivative word l_0,...,l_(n-1) with sum at least alpha n and a large/small color word, the initial color being large. Let E consist of the points realizing both actual words. Record maxima of the partial sums of l_i-h give at least theta n hyperbolic times: the total increase is at least (alpha-h)n and each increase is at most L-h.

From every maximal consecutive run of small times containing a hyperbolic time, retain (s,t], where s is its preceding large time and t its last hyperbolic time. These intervals of depths are disjoint. Their total length T is at least the number of hyperbolic small times. For a bad word in (16), T>=(theta-beta)n.

For each depth j let R_j be the supremum, over geometric intervals P with the chosen prefix and meeting E, of

    length(g^j(E intersect P))/length(g^j P).

For fixed s<t the relevant descendants within each depth-s parent have disjoint interiors, since the full word is fixed. They cover E intersect P, although they need not cover the rest of P. The distortion bound on every restricted iterate therefore gives R_s<=2R_t: the relevant input-length weights sum to at most one. Equality or a partition of the unused portion is unnecessary for this estimate.

Across a retained interval (s,t], every intermediate color is small. The number of descendants of one parent is at most

    product_(i=s)^(t-1) [C_r exp((log M-l_i)/(r-1))]
      = exp((t-s)log C_r
               +((t-s)log M-sum_(i=s)^(t-1)l_i)/(r-1)).

Hyperbolicity at t makes the sum in this formula at least h(t-s). At a witness in each relevant descendant the restricted-iterate Jacobian is at least exp(h(t-s)). Distortion makes the Jacobian at least half that throughout the descendant. Its final length is at most 2epsilon; the starting large parent has length at least epsilon/2. Summing the relative occupied lengths thus yields

    R_s <= 8 exp(-gamma_*(t-s)) R_t.                    (17)

Combine (17) over retained intervals with R_s<=2R_t across gaps. There are at most n retained intervals and at most n+1 gaps, while R_n<=1 and R_0=lambda(E). Hence

    lambda(E)<=2*16^n exp(-gamma_* T).

There are at most q^n derivative words and 2^n color words. Summing gives (16). The estimate never uses a count of large children.

Finally, logarithmic distortion below one on every restricted one-step interval gives l_i(y)>=l_i(x)-1 throughout a depth-j geometric interval. Summing this at a hyperbolic witness gives the stated whole-interval expansion. This remains true at points assigned to another derivative word.

## 8. Consequence using only forward exponential growth in the threshold

Suppose a C^r diffeomorphism f has bounds

    ||Df^n||<=exp(n Lplus),   ||Df^(-n)||<=exp(n Lminus), n>=1,

with Lplus>0, Lminus>=0, and the finite derivative bounds needed for each fixed iterate. Let a straight original arc contain a measurable positive-length set F on which

    limsup_N N^(-1)log J_(f^N)(x)>=lambda_0>0.

If

    r lambda_0 > Lplus,                               (18)

then there exist one iterate g=f^p, one scale epsilon and beta>0 such that infinitely many n have subsets E_n of that original F, of normalized original length at least 1/(2n^2), with at least beta n large hyperbolic times at a fixed threshold h>1 in the labelled cover just constructed.

Choose Lplus/r<chi<chi'<lambda_0. Necessarily lambda_0<=Lplus. Set h=p chi+2, alpha=p chi'-1, L=p Lplus, and use

    q=ceil(p(Lplus+Lminus))+4.

The actual ||Dg|| can be smaller; enlarging M to exp(p Lplus) is permitted throughout the proof. For sufficiently large p, alpha>h>1 and theta is bounded below by a fixed positive theta_0. Also

    gamma_* >= p(r chi-Lplus)/(r-1)+2r/(r-1)-log C_r,

which grows linearly in p, whereas log(32q) grows only logarithmically. Choose beta=theta_0/2 and then p so that the right side of (16) is at most 2exp(-n). Choose epsilon for the C^r derivatives of this fixed g only afterward, and restrict the original straight arc to one speed-epsilon interval retaining positive F measure.

The bounded derivatives of the finitely many remainders f^j, j<p, and their inverses preserve the upper exponent along multiples of p. Each point of F consequently belongs to infinitely many sets F_n on which J_(g^n)>=exp(np chi'). If their lengths were below 1/n^2 eventually, the first Borel-Cantelli lemma would contradict positive length of their limsup. Thus infinitely many F_n have length at least 1/n^2. Removing the exponentially small bad set gives E_n as asserted. All parameters can be fixed before a further positive-length restriction of F; the same selection applies afterward.

The inverse growth affects the number of labels and therefore the choice of p. It does not enter the strict threshold (18). At r=2 this is a finite-time geometric assertion under 2lambda_0>Lplus. It is not a C2 coverage assertion.

## 9. The remaining issue before any Euler coverage upgrade

For a cutoff backward Euler flow, its exact transverse covector gives lambda_0=a=1-2c on suitable original targets. Thus (18) would read r a>Lplus. The present proof supplies the finite-time geometry under that condition. It does not license replacing the independently confirmed coverage condition (r-1)a>Lplus+Lminus by r a>Lplus.

Specifically, A307 applies the A257 relative-entropy lemma to nested interval partitions, selects whole parents, and compares normalized reference arclength on a parent with normalized image arclength. Our geometric intervals for different words overlap. Assigning a point to its actual word gives a measurable partition, but its atoms can be proper noninterval subsets of the geometric intervals. Their normalized arclength need not be uniformly comparable to that on the entire interval. The multiplicity bound in Section 5 alone does not justify A257 on these atoms. Nor does cutting all overlapping intervals automatically preserve the small-child count or lower lengths of large pieces.

A correct incoming-measure construction for this labelled cover, or a compatible global interval partition with the same small-child estimate, is still needed. No claim is made that A307 or A308 is unchanged. The C2 coverage question and the main rotating-profile nonexistence conjecture remain UNRESOLVED.

## 10. Source comparison and verification scope

David Burguet, arXiv:2111.06651v2, actual retained manuscript in the team records, gives the surface threshold chi>R(f)/r in the Main Theorem, printed page 3. Its reparametrization lemma, Section 4.2, printed pages 15-18, has a per-label small-child factor C_r exp((k-k')/(r-1)), with local operator and tangent bins k,k'. Section 4 begins on arbitrary-dimensional compact manifolds; the later SRB theorem is for surfaces.

Sections 1-8 above are an independent Euclidean reconstruction with a global forward bound replacing the operator bin, genuine vector Taylor approximation, an explicit interpolation proof and disjoint interiors within each tangent bin. They do not cite Burguet's surface SRB theorem as a three-dimensional theorem. The source uses a covering tree and central portions of large pieces; its later measure argument cannot be replaced by an unproved reference to A307's different partition construction.

No computation is needed: every count and constant dependence is established above. No formalization is attempted. This submission requires independent mathematical review, including the itinerary selection and the fixed-word disjointness used in Section 7.


## Independent audit of the construction and itinerary estimate

The complete argument was independently reconstructed. Its Taylor polynomial has degree r-2 for F prime and needs only C^r regularity, including r=2. Applying scalar interpolation coefficients to vector values gives constants independent of ambient dimension. Each polynomial speed cut has only O_r(1) components because the squared vector norm is a scalar polynomial of degree at most2(r-2). The strict Taylor margins exclude isolated components at points in the actual bin.

An output that is small and bounded is embedded: its tangent projection on its maximum-speed direction stays positive, since its derivative changes by at most2 eta times that speed. This makes the arclength ratios in Section7 unambiguous. More generally the diffeomorphism preserves the original straight arc's embedding. For a fixed word, distinct parent interiors and then same-bin child interiors are disjoint. Thus the selected descendants' arclength weights sum to at most one even though they need not cover all of a parent. The relative-entropy argument is not used in this finite estimate.

In a retained small run of length k, each final child has relative input length at most8 exp(-h k), while its count is at most exp(k log C_r+(k log M-sum l_i)/(r-1)). This gives exactly gamma_*=(r h-log M)/(r-1)-log C_r. The endpoint distortion of each restricted iterate is at most D^2<2; one-step logarithmic oscillation is less than one. Record increments are at most L-h, so their number is at least theta n. The retained runs cover all small hyperbolic record times. Word and color counts give the written32q factor. The finite-iterate remainder and first Borel-Cantelli steps justify selection on the original positive-length set, without limiting measures.

The current construction uses a cover across bin labels. Its actual-itinerary cells can be noninterval measurable sets, so the A257 whole-parent reference comparison has not been proved for those cells. A393-A394 therefore authorize only the finite curve geometry and selection theorem, including the conditional r=2 case. They do not replace the established A373 Euler coverage criterion. A separate proposed partition repair, if completed and reviewed, would require a new verdict. The actual Burguet Main Theorem on printed page3 was compared only for the surface threshold; the complete source proof was not newly audited here.
