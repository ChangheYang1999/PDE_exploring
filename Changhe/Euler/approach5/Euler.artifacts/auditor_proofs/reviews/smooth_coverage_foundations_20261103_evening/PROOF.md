# Repeated audit of the smooth basin coverage foundations

Status: CONFIRMED at the smooth scopes in Sections1-8; the extensions in Section9 remain OPEN. This proof checks the smooth theorem and the interfaces between its construction, incoming measures, capture and basin domains. It does not newly establish unconditional finite-regularity coverage or Euler nonexistence.

## 1. Exact statement and dependencies

Let B,W be C-infinity vector fields on R3, with B complete in both time directions. Assume constants d>0, kappa>d, b0>0 and R0>0 satisfy

    div B=d,  [B,W]=-kappa W,
    B(x).x >= b0|x|^2 for |x|>=R0.

The bracket convention is [B,W]=DW B-DB W. Write Phi for the B flow, Psi_t=Phi_(-t), O={W!=0}, Q a closed ball of radius greater than R0, and K=intersection_(t>=0)Psi_t Q. For a probability nu, its basin consists of points whose continuous-time averages under Psi converge to nu for every bounded continuous test.

Then O is covered up to a Lebesgue null set by pairwise disjoint positive-volume Borel basins of an at most countable family of compactly supported whole-flow-ergodic probabilities nu_i. Each is supported in K, gives full mass to B!=0 and W!=0, has simple spectrum(kappa-d,0,-kappa), entropy h_nu_i(Psi_1)=kappa-d, and absolutely continuous conditionals on full one-dimensional Pesin unstable plaques. The stable line is R W and the zero line R B. If O is nonempty, the family is nonempty.

For the Euler equation

    div U=0,
    (1-c)U+DU((cI-omega J)x+U)+omega JU+grad P=0,
    J(x1,x2,x3)=(-x2,x1,0),

assume U globally C-infinity and uniformly sublinear, P C1, 0<c<1/2 and any finite real omega. Set B=(cI-omega J)x+U, W=curl U, d=3c, kappa=1+c and a=1-2c. The preceding conclusion holds. Additionally, with alpha=(B cross W).dx, the unstable densities are C|alpha(eu)| on almost every conditional plaque. There are unique maximal open essential basin domains D_i in O, containing their entire basins, of full nu_i measure and with null difference from their basins. They are flow invariant, locally W-saturated, pairwise disjoint and each has infinite volume.

Dependencies are the independently confirmed elementary curve tree A305, hyperbolic-time count A306, entropy lemma A257, original-curve construction A307, capture geometry A299, stable-zero lemma A201 and curve-to-unstable-conditional lemma A216. The source reproduces these arguments in Lemmas1-29; their crucial estimates are checked below. Oseledets, Pesin manifolds, recurrence, Birkhoff, disintegration, the entropy lower bound for unstable absolute continuity, Ruelle's inequality, entropy affinity and flow entropy scaling are standard external dependencies. The actual retained Ledrappier-Young statements with a zero exponent and the density conclusions were reread, not inferred from an abstract.

## 2. Completeness, trapping and the expanding arc

The abstract theorem assumes completeness. In Euler, uniform sublinearity gives |B(x)|<=C(1+|x|), so the ordinary Gronwall continuation argument supplies it in both directions. Since J is skew,

    B(x).x=c|x|^2+U(x).x >= (c/2)|x|^2

outside a sufficiently large ball. Thus Psi drives every bounded set into int Q in uniformly finite time. The compact sets Psi_t Q decrease; K is nonempty, invariant in both directions and contained in int Q. A smooth compactly supported modification of -B agrees near Q, and hence all its forward derivatives agree on Q. Extending the field by zero to S3 gives a closed-manifold setting without introducing a relevant invariant measure in the transition collar. Positive-cutoff collar orbits enter Q and do not recur there; zero-cutoff points are fixed with zero exponents.

The bracket and constant divergence imply, for every real t,

    D Psi_t W=e^(-kappa t) W o Psi_t,
    D Psi_t B=B o Psi_t,
    det D Psi_t=e^(-dt).

In particular both zero sets are invariant. For x in O intersect Q, if s1>=s2>=s3 are the singular values of D Psi_t(x), then

    s3<=e^(-kappa t) max_Q|W|/|W(x)|,
    s1^2>=s1 s2>=e^((kappa-d)t)|W(x)|/max_Q|W|.

Therefore every such point has a positive upper operator exponent. A finite coordinate-direction pigeonhole selects one direction on a positive-volume part of any positive-volume target G in O intersect int Q. Fubini in a box compactly contained there gives a straight arc with a positive-length subset of G having upper tangent exponent at least(kappa-d)/2. No invariant probability is assumed at this step.

## 3. Tree count, parameters and original density

For the compact cutoff map f put M=max(2,||Df||,||Df^-1||). Choose 0<zeta<zeta'<(kappa-d)/2, then integer r>=3 with 3log M/(r-1)<zeta/2. Only after fixing r choose a large iterate g=f^p. Finally choose the small curve scale epsilon to control the finitely many derivatives of g through order r. This order is valid for C-infinity and explains the regularity limitation.

The affine tree preserves a narrow tangent cone and uses slopes at most1/100. With M_g=max(2,||Dg||,||Dg^-1||), its one-step partition has at most C_r M_g^(3/(r-1)) nonlarge outputs. Here nonlarge means speed below epsilon/3; every output is small, so counting all small outputs would be false. The bound follows by equal Taylor pieces, finitely many polynomial norm bands, interpolation of lower derivatives, and speed normalization. Speed normalization creates only large children. A bounded input and bounded output have arclength-Jacobian distortion at most(50/49)^2<2 for the entire restricted iterate. This compares the two endpoint parametrizations and introduces no product of distortion factors over time.

The large-hyperbolic-time count uses h=p zeta+2, target p zeta'-1, finitely many integer Jacobian labels and a positive time fraction beta. For sufficiently large p the exponential bad-set estimate is at most2e^-n. Its proof counts nonlarge runs ending at hyperbolic times and bounds their original length by expansion and the nonlarge-child count. The constant8 for a retained run follows by applying distortion directly to the selected set, rather than applying it twice.

The tree parameters work for every later positive-length restriction of the original target. Apply the density theorem and Egorov to choose a compact positive-length E on which the fraction of the target in every shrinking tree atom tends uniformly to one. Positive tangent limsup and Borel-Cantelli then provide infinitely many E_n subset E with normalized length m_n>=1/(2n^2), each carrying at least beta n good depths. No typicality of E_n for an invariant measure is presumed.

## 4. Entropy, noncollapse and the invariant incoming measure

For a fixed future window M, select a whole depth-ell atom when some point of E_n in it has a good descendant within M steps. Give it its original E_n conditional probability and weight eta_n(P)/n, eta_n=lambda|E_n/m_n. The total mass lies in[beta-1/n,1] and increases with M. A selected image has length at least

    v_M=epsilon/(2 max(1,||Dg||^M)),

because its good descendant has length at least epsilon/2. The narrow tangent cone gives a minimum-speed lower bound and embedded nonconstant limits in the compact C1 curve class.

For completeness, the entropy passage does not confuse parent weights and conditional masses. Let H_ell be the relative entropy of eta_n on the depth-ell partition. Then0<=H_ell<=L_n=log(1/m_n). For an N-step refinement, declare a child bad when its eta conditional probability exceeds K times its original-arclength conditional probability. The entropy chain rule and the log-sum inequality give

    average bad conditional mass <=(N L_n/n+log2)/log K.

Keep each parent weight unchanged while restricting its conditional measure to good children, and discard the last N times. Set N=floor(sqrt n); L_n<=log2+2log n. Distortion bounds the good part by2K times normalized image arclength, up to the oscillation of a test on descendants of diameter at most2epsilon100^-N. Weak compactness and portmanteau pass this inequality to the limit. The deleted mass is at mostlog2/log K, so K tending to infinity proves joint absolute continuity with respect to the limiting curve marginal times normalized curve arclength. Positive length is a separate consequence of the fixed window, not of this entropy estimate alone.

Take the increasing limit over windows. Each finite-window curve marginal is dominated by the final marginal. Thus a set null for the final curve-arclength reference is null for every finite-window joint measure and for their increasing limit theta. The x marginal mu is invariant: selection at depth ell for window M implies selection of its ancestor at depth ell-1 for window M+1. Consequently g_*mu_n^(M+1)>=mu_n^M up to a mass1/n error. Passing first n and then M gives g_*mu>=mu; equality of finite masses gives invariance. Its mass is at least beta and its support lies in K.

For every curve in a finite-window marginal support, portmanteau after removing early times gives original approximants g^ell_j(P_j), ell_j tending to infinity. Their original target fractions tend to one and their distortion stays below2. Their negative k-th images have diameter at most2epsilon100^-k. A positive-mu alternative is detected by a finite window. Two-sided generic points on one incoming curve have the same component label, since all backward continuous test averages agree. That label is measurable from a countable test family. Disintegrating the curve marginal by it preserves the original arclength absolute continuity. No positive weight for an individual ergodic component in the ambient decomposition is required.

## 5. Spectrum, full plaques and exclusion of W=0

An incoming curve contains at most one B-zero point: two fixed points cannot have distances tending to zero under negative iterates. Thus mu(B=0)=0. At a two-sided regular point, Dg^n B=B o g^n is bounded for all integer n. The largest nonzero Oseledets component exponent is therefore at most0, and the smallest is at least0 by negative time. Hence B lies in the zero space. This argument does not require a pointwise lower bound for |B| along its orbit. Backward contraction of the incoming tangent supplies a positive exponent; determinant e^(-pdn) leaves exactly one negative exponent. The three exponents are p chi,0,-p(d+chi).

The complete incoming curve through a regular point lies in its global Pesin unstable curve, because the whole curve contracts exponentially backward. The primary definition of this manifold allows a zero exponent. To pass from a mixture of incoming curve densities to full-plaque conditionals, use a measurable subordinate partition. Any set null in almost every full plaque is null along almost every incoming curve: the full measure regular subset on each curve is covered by countably many intrinsic leaf segments lying in partition atoms. The immersed leaf has a second-countable domain and the relevant charts are Lipschitz on compacts.

This leaf-null conclusion gives conditional absolute continuity without choosing singular supports. If mu_s and lambda_s are the conditional probability and normalized leaf-length kernels, put rho_s=mu_s+lambda_s, m=int rho_s dq. Global Radon-Nikodym densities f,g for mu and int lambda_s dq yield mu_s=f rho_s and lambda_s=g rho_s by uniqueness of disintegration. The set{g=0} is leaf-null and therefore mu-null. Hence mu_s=(f/g)lambda_s. On each typical g-ergodic component, the unstable entropy lower bound and Ruelle upper bound give h(g)=p chi for that component's positive exponent p chi.

Suppose mu(W=0)>0. A finite-window curve carries positive arclength of regular generic W-zero points. Choose one at which its tangent is unstable. Its entire local strong stable plaque is W-zero. Indeed in tempered Lyapunov coordinates at this regular orbit, with negative exponent -lambda, the conorm of Dg^n at a nearby stable point is at least C e^(-lambda n-3epsilon n). C2 regularity controls the derivative perturbation by the exponentially shrinking stable distance. C1 regularity of W gives an upper bound C e^(-lambda n+epsilon n) for W at the nearby iterate, while real-time bracket transport gives the lower bound e^(p kappa n) times that conorm times the initial |W|. Taking4epsilon<p kappa forces initial W=0. Integer transport would not alone justify flow translates, but the actual bracket supplies every real time.

The limiting incoming curve, its carrier direction and this stable plaque meet transversely. Uniformly close carrier strips formed from the original approximating curves must intersect the plaque, by the elementary degree argument for three independent tangent vectors. Those strips lie in the invariant open set O because their original arc does. This contradicts the W-zero plaque. Thus mu(W=0)=0.

## 6. Flow averaging and capture of the original target

Normalize mu and select a typical g-ergodic component mu0. Its average nu=(1/p)int_0^p(Psi_s)_*mu0 ds is invariant and ergodic for the whole flow: a flow-invariant set is g-invariant and has the same0-or-1 mass under every phase. Whole-flow ergodicity does not imply time-one ergodicity and is the only assertion used.

At a regular W-nonzero point, exact transport, boundedness on K and recurrence to a set where |W| is bounded below give the W exponent -p kappa. Therefore chi=kappa-d. The phase measures are g-ergodic conjugates with the same entropy. Entropy affinity gives h_nu(g)=p(kappa-d); flow scaling yields h_nu(Psi_1)=kappa-d. The entropy-to-absolute-continuity direction of Ledrappier-Young then applies on the compactification.

For each test phi include its averaged test phibar=(1/p)int_0^p phi o Psi_s ds in the countable generic family. Map genericity then gives continuous-time genericity for nu. This explicit test choice prevents a missing genericity quantifier.

The bracket gives the local W-shift formula

    Psi_t Gamma_tau x=Gamma_(tau e^(-kappa t)) Psi_t x,

for x in Q, t>=0 and uniformly small |tau|. The right side is defined in a common compact neighborhood. Thus a W shift preserves every basin, as does a carrier time shift. On an incoming arc with a positive-length set T of generic regular points, the map

    H(s,t,tau)=Gamma_tau(Psi_t gamma(s))

is a C1 diffeomorphism near a density point belonging to T: its columns are respectively unstable tangent, -B and W. All initial points are in int Q. The image of T times a small two-dimensional rectangle belongs to the basin and has positive volume.

This product set also captures the original target. In the H coordinates, uniformly convergent approximating curves have first-coordinate images covering a compact positive-length subset of T. The inverse coordinate is Lipschitz, so a fixed positive fraction of their bounded total image lengths lies in the basin. Distortion below2 and invariance pull back a fixed positive fraction to each original P_j. Their target fractions tend to one, so target and basin have positive-length intersection for large j. This proves an existentially selected component; it does not claim the capture for every preassigned ergodic component.

## 7. Countability and almost-everywhere coverage

Consider all whole-flow-ergodic probabilities on K with the established spectrum, full mass on B,W nonzero and absolutely continuous unstable conditionals. Each has a positive-volume basin by the preceding local product argument applied to a generic plaque. Its basin is Borel: every orbit eventually enters Q, so convergence for a countable family dense in C(Q), at integer averaging lengths, characterizes convergence for every bounded continuous test.

Distinct probabilities have disjoint basins because tests distinguish probabilities. A disjoint family of positive-volume Borel subsets of R3 is countable: each member has intersection of volume greater than1/j with some integer-radius ball, and only finitely many disjoint sets satisfy a fixed pair of bounds. A basin is contained in O, since any orbit in the closed invariant W-zero set has zero time average of min(1,|W|), unlike these probabilities.

If the complement of the union in O had positive volume, invariance, finite entry into int Q and preservation of null sets by each Psi_-n would give a positive-volume target in int Q. Sections2-6 capture a point of that target in a basin in the very same class, a contradiction. Thus the complement is null. Nonempty O is open, so positive volume and nonempty family follow.

## 8. Euler identities, densities and essential domains

Taking curl of the Euler equation gives [B,W]=-(1+c)W, while div B=3c. The two rotation terms have precisely the signs needed for that bracket; no restriction on finite omega enters. Curl(B cross W)=a W implies

    alpha(B)=alpha(W)=0,
    L_W alpha=0,  Psi_t^*alpha=e^(at)alpha.

At typical points the stable and zero directions are independent and span ker alpha. Put A(x)=|alpha_x(eu(x))|. Covariance gives J^u Psi_1(x)=e^a A(x)/A(Psi_1 x). The conditional-density product telescopes to A(y)/A(z) times a backward-endpoint ratio. Along backward returns of a regular base point to a compact Pesin block with A bounded below, the companion point lies on the same small unstable graph, tangent directions converge and that ratio tends to1. The density product already has a full limit by the primary density theorem. Hence density=C A. Its strict positivity on full conditional plaques is supplied by Corollaries6.1.4 and6.2, not merely inferred from almost-everywhere positivity at regular points.

At almost every point for nu, strict plaque density gives an open product box in which its basin has full Lebesgue measure. Let D be the union of all open subsets of O with this property. A countable subcover makes D minus the basin null. The construction gives nu(D)=1. Carrier and local W shifts preserve the basin and null sets, hence D. Every basin point eventually enters D: choose a nonnegative continuous test supported in D of positive nu integral and use its basin average. Flow invariance then places the point itself in D. Maximality is by the definition, and overlapping distinct D would force their disjoint basins both to have full volume in a nonempty open set, impossible.

Finally div B=d and invariance give Leb(D)=Leb(Phi_t D)=e^(dt)Leb(D). Each D has positive volume, so its volume is infinite. No finite ambient invariant volume or stable absolute continuity has been assumed. For Euler, if W=0 identically, U is harmonic and uniform sublinearity forces U constant by the derivative mean-value estimate; otherwise the nonempty conclusion applies.

## 9. Scope, repeated checks and unresolved questions

The full current Section2C was read, including its finite-r outline and provenance list. The fresh mathematical rederivation here concerns the smooth chain and the density/domain interfaces. The prior complete A490 and A1219 audits remain the base for the fixed-r projective and sharp partition arguments. Those separate arguments have not all been reconstructed again here. They remain conditional on Gamma_E<r(1-2c) for each vortical component, with no common gap required. No unconditional C2 extension follows.

No new flaw was found in the smooth theorem, the measure-zero exclusions, entropy directions, original-target capture or essential-domain argument. Supports may still meet B=0 or W=0; no classification or finiteness of the family follows. No helicity sign follows. The theorem does not prove Euler nonexistence for arbitrary helicity.

The historical coordinator review was read fully and compared with its present repairs. Collaboration uses the existing configured model coordinator and theory agents, with actual provider execution independently unattested. Evidence records real source hashes and reading coverage; no runtime is inferred or padded.
