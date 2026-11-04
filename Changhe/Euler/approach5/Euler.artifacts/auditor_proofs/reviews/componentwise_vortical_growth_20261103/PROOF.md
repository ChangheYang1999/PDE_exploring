# Derivative growth restricted to vortical components

Independent reconstruction completed 2026-11-03T02:43:42Z. Confirmed as A430-A432 after the focused configured-model coordinator review and independent verification of its four precision remarks. This proof retains the additional growth and helicity-sign hypotheses. It does not establish them from decay.

## 1. Statement

Let r>=2 be an integer, 0<c<1/2 and omega in R. Let U be C^r on R3, P be C1, and assume the complete rotating profile equation

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    B=Ay+U, A=cI-omega J, J(x,y,z)=(-y,x,0).

Assume U(y)=o(|y|) uniformly at infinity. Put W=curl U, a=1-2c, kappa=1+c, d=3c, and let Psi be the complete flow of -B. Write O={W!=0}. For each nonempty connected component E of O and any closed ball Q of radius R satisfying

    B(y).y>=b|y|^2 for |y|>=R, b>0,

define

    K=intersection_(t>=0) Psi_t(Q),
    Q_E=Q intersect closure(E), K_E=K intersect closure(E),
    Z_E=K_E intersect ({B=0} union {W=0}),
    M_n(E)=max(1,max_(Q_E)||D Psi_n||).

Then Q_E is nonempty compact and forward invariant, and K_E is nonempty compact and invariant for the whole flow. The finite limit

    Lambda_E=lim_(n->infinity) log M_n(E)/n
            =inf_(n>=1) log M_n(E)/n

is independent of the admissible radius and of a fixed equivalent norm, equals the rate on K_E, and is at least a. Let Gamma_E be the attained maximum of the largest backward Lyapunov exponent over whole-flow-ergodic invariant probabilities supported on Z_E. Use Gamma_E=-infinity when Z_E is empty. Then

    Lambda_E=max(a,Gamma_E).                         (1)

If, for every component E,

    Lambda_E<r a,                                   (2)

then the full A417 vortical coverage conclusion holds: almost every vortical point lies in a continuous-time physical basin of one of at most countably many compactly supported whole-flow-ergodic vortical SRB probabilities. Each such probability has spectrum (a,0,-kappa), entropy a for Psi_1, and the positive one-dimensional unstable conditional densities of A207. Their invariant open essential basin domains are those of A223. Their supports may meet either zero set.

Condition (2) is equivalent to Gamma_E<r a for each E, and to the existence, for each E separately, of an integer N_E>=1 with log M_(N_E)(E)<r a N_E. No common gap below r a is assumed across different components. Since each nonempty Z_E has an attained maximum, failure for one E is witnessed by an ergodic probability there with largest exponent at least r a. A supremum over different E can equal r a without being attained while every individual condition holds; this is a logical possibility, not a constructed Euler profile.

If also U tends to zero, 2/5<=c<1/2, and U.W has one sign on each essential basin domain, the sign being allowed to differ between domains, then U=0. This corollary retains every A422 hypothesis except that its sufficient coverage condition is replaced by (2).

## 2. Complete flows, invariant components and strict trapping

Uniform sublinearity implies at most linear growth of B. A locally Lipschitz field with that bound has complete solutions in both time directions, by the integral growth bound and local continuation. The stated radial inequality holds on sufficiently large balls because the skew matrix J has y.Jy=0.

The exact transport identity is

    D Psi_t(x) W(x)=exp(-kappa t) W(Psi_t x).          (3)

Invertibility makes O invariant. For x in E the continuous orbit path stays in O, hence in the same connected component. Inverse time gives Psi_t(E)=E for all real t. Homeomorphisms also preserve closure(E).

Components of an open subset of R3 are open and countable: each contains a rational-coordinate point and different components are disjoint. The inward radial inequality for -B makes Q forward invariant with a strictly inward boundary. Every bounded set enters int Q in a common finite time. To see the last assertion, the radial differential inequality first bounds the entry time into Q; strict inwardness and compactness then give entry into its interior uniformly. Equivalently, apply continuity and a finite subcover after individual finite entry times.

A point of E therefore enters E intersect int Q. Thus Q_E is nonempty. It is compact and forward invariant. Its images are nested compact sets, with

    Psi_t(Q_E)=Psi_t(Q) intersect closure(E).

Their nonempty intersection is exactly K_E. Shifting the time index in the intersection proves invariance under any fixed real time. Also K lies in int Q: for any t>0, strict inwardness gives the compact inclusion Psi_t(Q) subset int Q.

Every relative neighborhood of K_E in Q_E contains Psi_T(Q_E) for sufficiently large T. Otherwise a sequence in the nested compact images and outside that neighborhood has a subsequential limit in K_E outside the neighborhood. This is impossible.

Every nonempty E is unbounded. If E were bounded, it would have finite positive Lebesgue measure. Invariance under the forward B flow and div B=d>0 would imply |E|=exp(dt)|E| for t>0. This ancillary observation is not used in (1) or (2).

## 3. Rate and core reduction

Forward invariance and the chain rule give M_(m+n)(E)<=M_m(E)M_n(E). Division n=qN+s proves existence of the rate and its infimum formula. Bounds for the derivative and its inverse over compact unit-time segments prove finiteness and equality of integer-time and real-time rates. Equivalent norms change log M_n by a bounded additive constant.

If R1<R2 are admissible radii, one integer T sends Q_R2 into int Q_R1. It also sends the intersections with closure(E) into each other. With C_T a bound for D Psi_T on the larger ball,

    M_n(E,R1)<=M_n(E,R2),
    M_(n+T)(E,R2)<=max(1,C_T) M_n(E,R1).

Their rates agree. There is no point-dependent entry time in this comparison.

Fix N>=1 and epsilon>0. By continuity, in a relative neighborhood V of K_E in Q_E,

    max(1,||D Psi_N||)<=M_N(K_E)+epsilon.

For some fixed T every later image of Q_E lies in V. Divide time after T into blocks of length N and a remainder s<N. The chain rule yields

    M_(T+qN+s)(E)<=C_(T,N)(M_N(K_E)+epsilon)^q.

First let q tend to infinity, then epsilon to zero, and then take the infimum over N. The rate on Q_E is at most that on K_E. Inclusion gives the opposite inequality. This uses no convexity or boundary regularity.

For the positive lower bound use the exact covector alpha=(B cross W).dy. At C2,

    d alpha=a i_W vol, Psi_t^*alpha=exp(at)alpha.      (4)

It cannot vanish identically on E since its exterior derivative is nonzero there. Choose alpha(x)!=0 in E and flow that point into int Q. Put A_E=max_(Q_E)|alpha|>0. Equation (4) gives

    exp(an)|alpha(x)|<=A_E ||D Psi_n(x)||,

so Lambda_E>=a. The zero set of alpha in E is null: at each of its points (4) makes one first derivative of one coefficient nonzero, so the coefficient's zero set is locally a C1 hypersurface; use a countable cover.

## 4. Attainment and the degenerate measure formula

Here is the compact variational argument, including the case of a negative rate. On any nonempty compact whole-flow invariant F consider its projective derivative flow on F times RP2. With X=-B and unit v, the instantaneous rate q(x,[v])=v.sym DX(x)v is continuous, and

    log|D Psi_t(x)v|=integral_0^t q(Psi_s x,[D Psi_s v])ds.

Maximize ||D Psi_n|| on F and average the maximizing orbit and direction for time n. A subsequential weak limit is invariant under the full projective flow and has q integral equal to the untruncated growth rate. Conversely, every invariant projective probability has q integral at most n^(-1)log max_F||D Psi_n|| for each n, and hence at most that rate.

Ergodic decomposition therefore supplies a maximizing whole-flow-ergodic lift. Its projection is whole-flow ergodic. Birkhoff and the displayed equality give a directional exponent equal to the maximum. Oseledets applies since the cocycle and its inverse are bounded over compact unit-time segments. The largest base exponent is at least that direction's exponent and at most the uniform growth rate, so equality holds. This proves attainment over ergodic base probabilities. No continuity of the largest exponent as a function of probability, or compactness of the set of ergodic probabilities, is assumed.

Apply this argument to K_E and, if nonempty, Z_E. Both zero sets are invariant. An ergodic probability on K_E either is carried by Z_E or gives it zero mass. In the second case the exact identities

    D Psi_t B=B composed with Psi_t,
    D Psi_t W=exp(-kappa t) W composed with Psi_t,
    det D Psi_t=exp(-dt)

give directional exponents 0 and -kappa. For precision, intersect Oseledets regularity with recurrence to each set {|B|>=1/j,|W|>=1/j}. Boundedness supplies upper rates; a subsequence of recurrent returns supplies the opposite inequalities. Directional limits exist, so the rates are exact. This requires neither log|B| and log|W| integrability nor ergodicity for Psi_1. Distinct exponents imply independent directions. The determinant gives the remaining exponent kappa-d=a.

Thus each largest exponent on K_E is either a or at most Gamma_E. The variational formula and Lambda_E>=a show (1), including the empty-set convention. If every ergodic probability on K_E is carried by Z_E, the variational formula reads Lambda_E=Gamma_E and the lower bound forces Gamma_E>=a. Attainment on each fixed Z_E turns a strict bound for every ergodic probability there into a strict bound for its maximum. It supplies no uniform gap across infinitely many E.

## 5. Localization of the finite curve construction

Fix one E satisfying (2). Choose

    Lambda_E<L0<L<r a, L/r<chi<chi'<a.

For every sufficiently large integer p,

    max_(Q_E)||D Psi_p||<=exp(pL0)<M=exp(pL).

Set g=Psi_p. The strict margin and compactness supply an open neighborhood V_p of Q_E with ||Dg||<M there. The finitely many higher derivatives of this fixed C^r map are bounded on a smaller neighborhood. Only now choose epsilon>0 sufficiently small that epsilon^(j-1)||D^j g||<=M for 2<=j<=r. Thus even the literal neighborhood hypotheses of A393 and A416 are met without increasing the exponent L. The neighborhood may depend on E and p and need not be invariant or convex. This one neighborhood serves all the actual curves in Q_E simultaneously, as required by the literal A393 hypothesis.

Alternatively, the Taylor proof uses F=g composed with gamma as a function of its one-dimensional parameter. Every chain-rule derivative of g is evaluated at gamma(t), and the integral Taylor remainder uses only parameter values on that curve. It never uses a spatial chord joining points of Q_E. Derivative bounds on the actual curve therefore suffice. The neighborhood argument above avoids any need to weaken the finite lemma's printed hypothesis.

For a point starting in Q_E its whole forward segment lies in Q. The inverse of its time-p derivative has norm at most exp(pLminus), with

    Lminus=max(0,max_Q lambda_max(cI+sym DU)).

Indeed the inverse variational equation uses -D(-B)=DB along that same forward segment; its symmetric part is cI+sym DU. The skew rotation contributes zero to this norm derivative. No backward trapping assertion is made. This gives O(p) possible integer tangent bins.

Take any positive-volume residual target S in E intersect int Q. Remove the null alpha-zero set. Equation (4) gives upper operator exponent at least a. Since ||T||<=sqrt(3) max_i|T e_i|, one fixed coordinate direction has upper exponent at least a on a positive-volume subset. Choose a box with closure in E intersect int Q and use Fubini to obtain a straight arc, lying wholly in that box, with a positive-length original target of that upper tangent exponent. Countable boxes and three directions suffice, with no assumption of a lower tangent exponent.

Every forward image of the whole arc is in E intersect Q. Every partition child is an affine restriction of such an image, so it remains there as well. The A416 partition and its A418 nonlarge-output count apply to every parent. Choose h=p chi+2 and the conservative target p chi'-3. Then

    gamma_*=(r h-pL)/(r-1)-log C_r

has positive linear growth in p, which dominates the logarithm of the O(p) label count. All derivative and count constants are fixed before selecting the positive-density geometric times. Multiples of p retain the original upper tangent exponent because the finitely many remainder derivatives and inverses are bounded on Q. The A394 selection consequently applies to every further positive-length restriction of the original target.

This reproduces the entire finite-time construction of A417 on Q_E. Nonlarge outputs, not every output of speed at most epsilon, are the objects counted. Actual whole interval partitions are used, rather than measurable fragments with one assigned itinerary.

## 6. Incoming measures, boundary limits and residual capture

The construction just obtained has exactly the inputs of A307's whole-parent measure argument. Its finite-window length lower bound can use the bound ||Dg||<=M along the actual curves; a coarse ambient bound on a compactification would also suffice here, because this constant does not enter the threshold (2). Uniform second derivatives give a compact C1 class even for r=2. The limits are regular embedded C1,1 arcs in every fixed noncollapse window.

A257 applies to the genuine nested interval partitions, with image distortion at most D^2 and shrinking descendant diameter. Its entropy cost for selected original sets is O(log n), and the choice of sublinear window N_n gives incoming absolute continuity. The existential whole-parent witness rule gives the invariant nonzero measure exactly as in A307. Every limit curve and each of its fixed inverse iterates lie in Q_E, since the corresponding finite-time predecessor curves do. Such curves can meet its boundary; they are not declared vortical on that basis.

For clarity, the remaining reviewed capture interfaces are these. Incoming arclength absolute continuity and backward contraction give the unstable leaf representation. A216 identifies one positive exponent, one neutral flow exponent and one negative exponent and gives full unstable conditional absolute continuity and physicality. Equilibrium components are excluded by the nonconstant-curve representation. If an irrotational component remained, A201 would make its strong stable plaques irrotational. At a regular incoming point, A299's transverse persistence forces uniformly close original carrier strips to meet such a fixed plaque, contrary to their lying in E. This removes that component. A299's product-set and original-parent density argument then captures a positive part of the original S in a vortical basin. These are the same proved A417 interfaces, not an inference from existence of one physical probability to coverage.

All relevant measure supports lie in K_E subset int Q. Sufficiently small stable plaques and their forward iterates can be kept in Q. Ambient C2 derivative comparisons near those plaques use finite bounds on Q and introduce no new exponential-growth hypothesis. Extending the original field outside a neighborhood of Q to a closed ambient manifold leaves all original orbits, derivatives and capture arguments unchanged. Neither the stable plaques nor the product boxes are required to stay inside Q_E. Only the original curve iterates need its sharper bound. Thus an irregular boundary of E introduces no missing geometric assumption.

Apply this capture construction to every positive-volume residual S in this fixed component. Distinct physical basins of probabilities are disjoint measurable sets, so at most countably many have positive volume. If their union failed to cover E intersect Q up to a null set, its measurable complement would be a residual target and would yield an additional positive portion in a basin, a contradiction. Invariance and countably many finite-time pullbacks of int Q give coverage in all of E. Repeat independently over countably many E. The exceptional null sets have null union; no sum of derivative estimates or common gap is used. A207 and A223 then give the asserted positive conditionals and essential domains.

## 7. Corollary and limits

After coverage, the entire A422 given-measure proof uses only C2 U and C1 P. Its recurrent complete vortex-flow argument turns the fixed helicity sign on each essential domain into zero helicity there. Its normalized-pressure mean identity gives zero reduced Bernoulli value there. Its arbitrary-boundary locally Lipschitz zero extension across the irrotational interior and convex radial stress test then give U=0 for decaying U and 2/5<=c<1/2. The growth constant is used only to produce the coverage package. Substituting the identical package proved in Section6 therefore proves the corollary, with every sign, pressure and decay premise retained.

The original condition Lambda_core<r a implies the condition on Q intersect closure(O), which implies (2). The latter does not need a uniform positive gap over components. No actual target profile separating these sufficient conditions is constructed here. An invariant probability supported in the interior of {W=0} lies outside closure(O), so it does not enter any Gamma_E. Also closure(O) can strictly contain the union of the individual component closures, since components can accumulate. A probability supported outside that union enters no Gamma_E, even if it is carried by closure(O). Irrotational component-boundary probabilities and vortical carrier equilibria remain in the test. These possible distinctions between sufficient tests are not asserted to occur in an actual decaying profile.

At C2 the condition Gamma_E<2(1-2c) is still unproved from decay for every E. At C-infinity the one-sign theorem still does not exclude sign-changing essential domains. No unrestricted target nonexistence or counterexample is obtained.

## Dependencies and evidence

The complete elementary rate and projective arguments are included above. The finite curve lemmas and capture theorems are dependencies with proved exact statements: A393-A394, A416-A418, A257, A307, A201, A216 and A299; A207 and A223 identify the precise basin package; A422 proves its Liouville consequence. Their entire relevant proof passages were reread, with particular attention to C2 compactness, actual-curve derivative evaluation, stable plaques outside Q_E, and whole-parent target localization. No new computation or formalization was required. The source submission and hashes are in verification. The full focused coordinator review in the team records was checked against every interface above. Its four optional precision points are incorporated. The existing coordinator agent is configured as the primary model; configuration is not provider attestation. No new model client was used.
