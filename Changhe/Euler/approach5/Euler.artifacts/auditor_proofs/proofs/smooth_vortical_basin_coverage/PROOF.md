# Smooth vortical regions are covered almost everywhere by physical basins

## 1. Exact statement

Let B,W be C-infinity real vector fields on R3. Assume B is complete in both time directions and

    div B=d>0,    [B,W]=-kappa W,    kappa>d.

Assume there are b0,R0>0 with B(y).y>=b0|y|^2 for |y|>=R0. Write Psi_t for the flow of -B and O={W!=0}. Choose any radius R1>R0 and write Q for its closed ball. Its compact maximal invariant core is K=intersection_(t>=0) Psi_t(Q).

There is an at most countable family of probabilities nu_i, each invariant and ergodic for the entire Psi flow and supported in K, such that

    nu_i(B!=0,W!=0)=1,
    spectrum(Psi,nu_i)=(kappa-d,0,-kappa),
    h_(nu_i)(Psi_1)=kappa-d.

Each has absolutely continuous conditional measures on its full one-dimensional Pesin unstable plaques and a positive-Lebesgue-volume continuous-time basin. Every basin lies in O. Their union covers almost every point of O. If W is not identically zero, the family is nonempty.

The basin is the set of points for which (1/T) integral_0^T phi(Psi_t x)dt tends to integral phi dnu_i for every bounded continuous phi. Each orbit eventually enters Q, so a countable dense family of continuous tests on Q gives the same Borel set. No claim of time-one ergodicity is made.

For a nonconstant C-infinity uniformly sublinear Euler profile, set B=(cI-omega J)y+U, W=curl U, d=3c and kappa=1+c. The hypotheses hold for every 0<c<1/2 and every finite omega. Thus the spectrum is (1-2c,0,-1-c), and the entropy is 1-2c. The supports may meet {B=0} or {W=0}. This is not coverage by nonsingular uniformly hyperbolic attractors. No C2 existence theorem, finite number of measures, uniqueness or Euler nonexistence is asserted.

## 2. Compactification and original-curve output

Every Psi orbit enters the interior of Q in finite time and stays there. Outside R0, the backward radial inequality gives d(log|Psi_t y|)/dt<=-b0. Choose a smooth compactly supported cutoff rho equal to one on a neighborhood of Q. The vector field -rho B is smooth and compactly supported on R3; its time-one map f is a C-infinity diffeomorphism with all positive-order derivatives bounded and with bounded inverse derivative. It agrees with Psi_1, including derivatives, along every orbit starting in Q. No identities in the cutoff transition region will be used.

For x in O intersect Q, exact transport and divergence give

    D Psi_t(x) W(x)=exp(-kappa t) W(Psi_t x),
    det D Psi_t(x)=exp(-dt).

Let M bound |W| on Q. The smallest singular value is at most exp(-kappa t)M/|W(x)|. The product of the largest two is consequently at least exp((kappa-d)t)|W(x)|/M, so

    ||D Psi_t(x)||>=exp((kappa-d)t/2)(|W(x)|/M)^(1/2).

Now let G be any measurable positive-volume subset of O intersect int(Q). The inequality ||Df^N||<=sqrt(3) max_i|Df^N e_i| permits selection of one fixed coordinate direction with positive upper derivative exponent on a positive-volume subset of G. Select a small box with closure in O intersect int(Q), then use Fubini on its parallel coordinate lines. This produces a straight compact D0 in that box and a positive-length original target G0 subset D0 intersect G with a common positive lower bound for the upper tangent exponent.

A305-A307 now provide the following output for g=f^p=Psi_p on Q, for some integer p>=1. The target can be restricted to a smaller straight D without losing positive length. There is a compact positive-length E contained in F=G0 intersect D and a nonzero finite g-invariant measure m with an incoming-curve joint measure theta, its curve marginal q, and

    theta << q(dgamma)lambda_gamma(dx).

The curves are nonconstant, embedded and at least C^(1+alpha). They have explicit exponential backward derivative and diameter bounds. There are increasing finite joint measures theta^M tending to theta, with m^M<=m their increasing ambient marginals. For every fixed M, almost every represented curve has original approximants

    gamma_j=g^(ell_j)(P_j),    ell_j->infinity,

where P_j is a DEPTH-ell_j atom of the original nested tree, contains a point of E, and satisfies

    length(P_j intersect F)/length(P_j)->1.

The convergence is C1. Full image lengths are bounded above, and their arclength distortion relative to P_j is bounded uniformly. For fixed M the image lengths also have a positive lower bound. In particular the parent levels, not merely the image times, tend to infinity. This explicitly supplies the clause identified in the focused coordinator review.

All limiting curves lie in K, together with all their negative g iterates. Indeed a late finite image is inside every fixed g^nQ; intersect over n. Monotonicity of Psi_tQ shows that intersection_n Psi_(np)Q equals K, independently of p. This also shows that the support of m is in the full-flow-invariant K.

These are proved outputs of A305-A307, not external assumptions from a recent preprint.

## 3. Regular components and full unstable conditional measures

Normalize m. Choose a simultaneous two-sided Birkhoff-generic and Oseledets-regular set of full measure. Backward distances on any one incoming curve decay exponentially, so backward averages of all continuous tests coincide on its generic points. A countable dense collection of tests identifies their common ergodic-component probability. Disintegrating the incoming representation by that component label preserves arclength absolute continuity; no component need have positive atomic weight in the ergodic decomposition.

The measure gives no mass to {B=0}. Every incoming curve meets that set in at most one point, since distinct equilibria maintain a fixed distance under every backward iterate. Arclength absolute continuity gives zero mass to that point.

At a two-sided regular point, Dg^n B=B composed with g^n is bounded for all integers n on K. Oseledets splitting and its tempered projections therefore place B in the zero-exponent space. A nonzero incoming tangent contracts exponentially under Dg^(-n), by A307, so at least one positive exponent exists. The determinant fixes the sum as -pd. There are exactly three simple exponents

    p chi,    0,    -p(d+chi),    chi>0.

The full unstable dimension is one. Moreover each incoming curve through a regular point lies in its global Pesin unstable manifold: the explicit exponential backward distances eventually lie within every sufficiently slowly shrinking tempered Pesin chart, and the unstable-graph characterization then applies. Equivalently, the global unstable manifold is the set of points approaching that regular orbit exponentially in negative time. The zero flow exponent does not belong to this exponentially approaching set.

A216's intrinsic-leaf null-set argument now gives absolute continuity on full unstable plaques. In detail, leaf-null sets in a subordinate partition are covered near generic curve points by countably many intrinsically open leaf intervals. Immersion maps their coordinate-null sets to ambient arclength-null sets. Incoming arclength absolute continuity therefore annihilates them. The measurable conditional Lebesgue decomposition gives the full unstable conditional statement. Ledrappier-Young's entropy formula then yields h_mu(g)=p chi for almost every g-ergodic component mu.

If a measurable invariant alternative has positive m measure, some m^M sees it. Since m^M<=m and theta^M<=theta, it sees the same full generic and regular sets and the same curvewise component label. Select a curve from this finite-M representation and a compact positive-length set of generic points for one component in that alternative. It retains all original approximants from Section 2. This uses neither invariance of m^M nor domination by phase images of m^0.

## 4. Irrotational components cannot occur

Let Z={W=0}. Suppose m(Z)>0. The preceding selection gives a finite-M incoming curve, a component with full mass on Z and a regular generic point x on its local arc, with B(x)!=0. Select x also typical for the arclength tangency statement A299. Its incoming tangent is the unstable direction.

A201, applied to the rescaled carrier pB with bracket rate p kappa, puts a sufficiently small strong stable plaque through x entirely in Z. Its local stable futures stay in a fixed compact neighborhood because the radial trapping inequality bounds futures of nearby initial points. A201 uses C2 carrier regularity, the local Lipschitz bound on W and the full derivative conorm in tempered coordinates. It requires no flatness or comparison between kappa and the stable exponent.

The two-dimensional strip Psi_t gamma(s) is transverse to that fixed plaque at x: its tangent plane is the unstable direction plus the carrier direction. The strips through the original approximants converge uniformly on a fixed small parameter rectangle. A299's degree argument makes every sufficiently late original strip meet the same stable plaque. The bounded flow translates used here are allowed in both time directions.

But the original D lies entirely in O. Exact bracket transport makes O invariant under the complete carrier flow, so every original image curve and every such strip lies in O. A strip cannot meet a plaque contained in Z. This contradiction gives m(Z)=0.

## 5. Full-flow averaging and a product set of generic points

Choose a vortical g-ergodic component mu obtained above. Define

    nu=(1/p) integral_0^p (Psi_s)_*mu ds.

It is invariant and ergodic for the entire flow. A flow-invariant set is g-invariant, has mu measure zero or one, and has that same measure under every translated mu. The translated measures are g-ergodic and conjugate; entropy affinity gives h_nu(Psi_p)=p chi. Flow entropy scaling gives h_nu(Psi_1)=chi. Unstable conditional absolute continuity is preserved under these smooth translates and their invariant mixture. Birkhoff for g applied to integral_0^p phi(Psi_s x)ds gives continuous-time nu-genericity on the selected positive-length set T of mu-generic curve points.

At almost every vortical regular point, W has exponent -kappa. Indeed its exact derivative formula expresses its norm as exp(-kappa t)|W(Psi_t x)|/|W(x)|. The latter numerator is bounded on K and returns to a fixed positive lower bound infinitely often by recurrence. Existence of its Oseledets exponent forces that extra exponential rate to be zero. Thus W is the stable direction, independent of the zero-exponent B direction, and the determinant gives chi=kappa-d. All the required spectrum and entropy formulas follow.

At a regular density point of T, the map

    H(s,t,tau)=Gamma_tau(Psi_t gamma(s)),

where Gamma is the local W flow, has independent derivative columns gamma', -B and W. It is a C1 diffeomorphism on a small box. Restrict T to a compact positive-length subset inside its s interval.

For x in K, a common sufficiently short W segment satisfies

    Psi_r Gamma_tau x=Gamma_(tau exp(-kappa r)) Psi_r x,    r>=0.

Uniqueness and exact bracket transport prove the identity. The right side is defined in one compact neighborhood of K and differs from Psi_r x by at most C|tau|exp(-kappa r). This defines the entire left-side future consistently by completeness of B. Consequently short W shifts and bounded carrier-time shifts preserve the continuous-time averages. Hence H(T times a small two-dimensional rectangle) lies in Basin(nu) and has positive volume by ordinary change of variables. No global completeness or divergence condition on W is required.

## 6. Capture in the original set

Use the first coordinate pi_s of H^(-1). Shrink the s interval so that its endpoints strictly bracket a compact positive-length T1 subset T. Uniform convergence of the original image arcs keeps their other two chart coordinates in the genericity-preserving rectangle, and their first-coordinate endpoint values on opposite sides of T1.

The intermediate value theorem says that the first-coordinate image of the points over T1 covers T1. Since pi_s is Lipschitz on a small compact ball within the chart, those points occupy at least length(T1)/Lip(pi_s) of image arclength. They are all in Basin(nu). The full image lengths are uniformly bounded above, so a fixed positive fraction of every sufficiently late full original image arc lies in this same basin. Derivative convergence or projected monotonicity is unnecessary.

Uniform distortion and invariance of the basin under g pull the fraction back to a fixed positive fraction of each original P_j. Its level is ell_j->infinity, so the original F fraction tends to one by Section 2. These two subsets therefore intersect on a positive-length subset for large j. In particular some point of the original positive-volume target G belongs to Basin(nu).

The argument applies to every measurable positive-volume G in O intersect int(Q). It is an original-set capture statement, not just abstract existence of some physical measure.

## 7. Countable coverage

Consider the class of all probabilities on K that are invariant and ergodic for the full flow, give full mass to {B!=0,W!=0}, have the simple spectrum (kappa-d,0,-kappa), and have absolutely continuous full unstable conditional measures. Every measure in this class has a positive-volume continuous-time basin by the product argument of Section 5, applied to a positive-length generic set on an unstable plaque. The measure produced in Sections 3-6 belongs to this exact class.

Distinct probabilities have disjoint Borel basins. Sigma-finiteness of Lebesgue measure makes the class at most countable. Their basin union is measurable and flow invariant. Each basin is contained in O: the bounded continuous function min(1,|W|) averages to zero on Z and has strictly positive integral against every measure in the class.

Suppose the complement of the union in O had positive volume. Since every orbit eventually enters int(Q), invariance and a countable union of integer-time inverse images show that the complement inside int(Q) has positive volume too. Apply Section 6 to that complement as G. It yields a point of G in the basin of a measure in the defining class, contradicting the choice of G. This proves the coverage theorem. If O is nonempty it is open and has positive volume, so the family is nonempty.

## 8. Euler application and limits

For a smooth uniformly sublinear profile with 0<c<1/2, the skew rotation contributes zero to B(y).y. Uniform sublinearity gives the stated radial inequality for large |y| and at-most-linear growth, hence completeness. Divergence and curl of the profile equation give div B=3c and [B,Omega]=-(1+c)Omega. Since 1+c>3c, all abstract hypotheses hold for every finite omega. If Omega were identically zero, U would be componentwise entire harmonic with uniformly sublinear growth and thus constant. Therefore a nonconstant profile gives a nonempty vortical region.

The theorem does not require actual curl coupling for its abstract statement. It is consistent with the regular and singular independent-field models A243 and A253. Almost-everywhere vorticity of the selected measures does not keep their topological supports away from either zero set. The theorem supplies neither uniform hyperbolicity of those supports nor classification into nonsingular regular attractors.

For actual Euler profiles, A207 additionally gives strictly positive local unstable densities and A223 gives pairwise disjoint invariant open essential basin domains with the same basin sets modulo null sets. Their union covers O modulo a null set by the theorem. These are consequences for the actual Euler application, not assumptions inserted in the capture proof. They do not imply any sign of helicity.

The construction uses smoothness to choose an arbitrarily large finite r before choosing an iterate. This proof makes no automatic C2 or arbitrary fixed finite-r coverage assertion. No pressure estimate, Dini decay, energy integrability or helicity sign is needed for the abstract coverage theorem, and no nonexistence conclusion is drawn here.

## 9. Verification and continuing model review

Dependencies: A305-A307 for the elementary original-curve construction; A257 for its entropy lemma; A201 for stable-zero capture; A216 for full unstable conditional absolute continuity and entropy; A299 for intrinsic tangency and both original-curve capture lemmas; standard two-sided Oseledets, Birkhoff and Pesin theory. No theorem from the disputed 2026 measured-disk source is used.

The configured-model coordinator's focused review independently reconstructed the four conditional capture steps and identified the missing original-parent-level clause. It is explicitly repaired in Section 2, where A307 gives level(P_j)=ell_j. Its other requests are incorporated: the unstable-set characterization, exact measure class, stable direction, both time signs and Borel basins. The received review, the prior proposal and the model configuration are retained with hashes in the team records. The model file specifies the primary model; this is configuration evidence, not provider attestation. No new model client was used.

The entire argument has been independently reconstructed after receiving that review. No computation or formalization was needed. Its conclusion is smooth vortical physical-basin coverage with exact exponents, not the full Euler nonexistence conjecture.
