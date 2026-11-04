# Independent continuous zero-set extension and weak-L2 audit

Status: CONFIRMED A2899-A2901 at the exact scopes stated below; broader extensions remain OPEN A2902. The complete existing model comparison has been read. This is a local conditional scalar theorem and its local carrier consequence. It is not a proof of the Euler conjecture.

## 1. Exact statement and scope

Let D be a bounded open disc in the complex plane. Let n>=1 be an integer, f in C^n(D;C), and b:D->[0,infinity) be measurable and finite almost everywhere. Write dbar=(partial_x+i partial_y)/2 and assume

    |dbar f|<=b|f| almost everywhere,
    M=sup_(t>0) t sqrt(area{b>t})<infinity,
    sigma=2M/sqrt(pi)<=n.

Then either f is identically zero or all its zeros are isolated. Every zero a in the second alternative has finite integral order: there are C>0, N<infinity and r0>0 with

    integral_(B(a,r)) |f|^2 >= C r^N,    0<r<r0.

Thus vanishing of that integral faster than every power at one point implies f=0. The result localizes to a connected domain covered by relatively compact discs with these hypotheses; the integer may vary with the disc if the indicated regularity holds. For C1 the sufficient bound is M<=sqrt(pi)/2; for C2 it is M<=sqrt(pi). No claim of optimality of this bound is made.

The proof separates n-jet vanishing from infinite integral order. The set F below consists of points where every derivative through degree n vanishes. A nonzero holomorphic z^(n+1) has a point in F and does not have infinite integral order there. The theorem cannot conclude that every nonzero solution has a nonzero Taylor term of degree at most n.

## 2. The exact disc-mean potential estimate

Define q=dbar f/f off the zero set and q=0 on that set, then extend q by zero outside D. The assumed inequality gives dbar f=qf almost everywhere, including almost every zero, and |q|<=b. Layer cake gives, for a measurable set E of finite area,

    integral_E |q| <= integral_0^infinity min(area(E),M^2/t^2)dt
                   =2M sqrt(area(E)).

Consequently q is L1 and has bounded support. The Cauchy potential

    s(z)=pi^(-1) integral q(zeta)/(z-zeta) dA(zeta)

is L1 on every compact set by Fubini and local integrability of the reciprocal-distance kernel, and dbar s=q in distributions. Its pointwise absolute convergence everywhere is neither asserted nor needed.

For B(a,rho), set w=zeta-a. Angular integration followed by radial integration with density 2r/rho^2 gives

    mean_(z in B(a,rho)) 1/(z-zeta)
      =-conjugate(w)/rho^2       if |w|<rho,
      =-1/w                     if |w|>=rho.

Indeed the circle mean is -1/w when r<|w| and zero when r>|w|; the single exceptional radius does not affect the locally integrable two-dimensional integral. In particular the modulus of the disc mean is at most 1/max(rho,|w|).

Choose R>rho so that the support of q lies in B(a,R). With W_a(t)=integral_(B(a,t))|q|, Tonelli applied to

    1/max(rho,r)=1/R+integral_(max(rho,r))^R t^(-2)dt

gives

    |mean_B s| <= pi^(-1)[W_a(R)/R+integral_rho^R W_a(t)/t^2 dt]
               <=sigma[1+log(R/rho)].

Here W_a(t)<=2sqrt(pi)Mt. One common finite R works for all centers in a fixed compact subset. Thus, uniformly in such centers,

    mean_(B(a,rho)) Re s >= sigma log rho-C.

Only a mean is controlled. No pointwise bound or exponent-one integrability of exp(-s) is inferred.

The logarithmic coefficient is sharp as a potential estimate. For q(z)=alpha/conjugate(z) on the unit disc, alpha>0, the weak norm is alpha sqrt(pi). Its potential is 2alpha log|z| inside and zero outside. The two pieces agree on the circle, the weak derivative is q without a boundary measure, and their difference from the Cauchy transform is entire holomorphic and tends to zero at infinity. Its centered mean is 2alpha log rho-alpha. This example does not show optimality of the continuation condition.

## 3. Zeros having a nonzero n-jet

Suppose a is a zero whose first nonzero Taylor degree is m<=n. There is a nonzero homogeneous complex polynomial P of degree m such that, uniformly in direction,

    f(a+w)=P(w)+o(|w|^m),
    Df(a+w)=DP(w)+o(|w|^(m-1)).

The rescaled functions epsilon^(-m)f(a+epsilon w) converge in C1 to P on 1<|w|<2, including when m=n. The coefficient epsilon b(a+epsilon w) has weak-L2 norm at most M on that annulus. On P!=0 the logarithmic derivatives converge. A countable sequence of scales and Fatou on strict superlevel sets give

    area{1<|w|<2: |dbar P/P|>t}<=M^2/t^2.

Write P(re^(i theta))=r^m p(theta). Then

    dbar P/P=e^(i theta) A(theta)/r,
    A=(m+i p'/p)/2.

If p had an angular zero of multiplicity d>=1, p'/p would be d/(theta-theta0)+O(1). On any fixed radial subannulus this yields a superlevel area at least c/t for all sufficiently large t, contradicting M^2/t^2. It is the superlevel estimate, not mere failure of angular L2, that proves the contradiction. Thus p is nowhere zero. In particular |f(a+w)|>=c|w|^m near a, and a is isolated.

Because P is homogeneous in the real coordinates,

    p(theta)=e^(-im theta)Q(e^(2i theta)),
    k=wind(p)=-m+2N0,

where Q has degree at most m and N0 counts its roots in the unit disc with multiplicity. Therefore |k|<=m and k has the parity of m. The winding of f on sufficiently small circles is k.

## 4. A finite budget for every nonpositive index

The Taylor remainder yields

    q(a+r e^(i theta))=e^(i theta)A(theta)/r+o(1/r)

uniformly. For every epsilon>0 and all sufficiently small r, |q|>=(|A|-epsilon)_+/r. Integrate the polar region r<(|A|-epsilon)_+/t in a fixed small disc, multiply its area by t^2, then let t increase and epsilon decrease. Since b>=|q| almost everywhere,

    liminf_(t->infinity) t^2 area{b>t near a}
      >=d_a=(1/2)integral_0^(2pi)|A|^2 dtheta
      >=pi(m-k)^2/4.

The last inequality follows from mean A=(m-k)/2 and Cauchy-Schwarz. Any finite collection of such zeros has disjoint small discs. The weak bound then gives

    sum_a d_a<=M^2,
    sum_a(m_a-k_a)^2<=4M^2/pi.

These sums mean suprema over finite subsets; no infinite limit is interchanged. If k<0, m-k>=2|k|, so sum_(k<0)k^2<=M^2/pi. If k<=0, parity and m>=1 imply m-k>=2. Consequently there are at most M^2/pi nonpositive-index zeros with nonzero n-jet. The statement is a real upper bound for an integer count, so its floor may be taken. Zeros in F are not counted by this argument.

## 5. Meromorphic reduction without an exponential chain rule

Let F be the relatively closed set where all derivatives of f through degree n vanish. Every zero in D minus F is isolated by Section 3. On a small disc where f is nonzero, a C1 logarithm exists, and dbar(s-log f)=0. Weyl's lemma therefore makes s-log f holomorphic. Hence h=f exp(-s), defined through this local representative, is holomorphic and nonzero there.

Near an isolated zero a outside F, take a smooth periodic logarithm psi of p(theta)e^(-ik theta). Let g=log(f/P) on a small punctured disc, using f/P->1. Taylor's estimates imply g=o(1) and Dg=o(1/r). These bounds imply g in W1,1 across a; its boundary contribution is o(r). Put

    s_a=(m-k)log r+psi(theta)+g.

This also lies in W1,1 locally. Its boundary contribution on radius r is O(r(1+|log r|))+o(r), which tends to zero. Away from a, exp(s_a)=f/(z-a)^k and dbar s_a=q, so the same derivative equation holds distributionally across a. Weyl then gives s-s_a=h_a holomorphic and

    h(z)=(z-a)^k exp(-h_a(z)).

Thus the only poles have negative k. Section 4 gives finitely many of them throughout D. The polynomial

    Z(z)=product_(k_j<0)(z-a_j)^(-k_j)

cancels all of them. H=Zh is holomorphic on D minus F, and there

    log|H|=log|Z|+log|f|-Re s

almost everywhere. These logarithms are locally integrable on D minus F: at its isolated zeros the Taylor bounds and meromorphic form suffice. H cannot vanish identically on any nonempty component of D minus F, since such a component has points with f nonzero. Every zero of Z is a zero of f outside F.

## 6. Uniform Taylor remainders give a continuous zero extension

Work in two nested compact convex discs K0 inside the interior of K1 inside D. For z in K0 sufficiently close to F, a nearest a in F lies in K1. Set delta=dist(z,F). Uniform continuity of D^n f on K1, its vanishing at a, and Taylor's integral formula give a positive nondecreasing modulus eta(t)->0 such that

    |f(w)|<=eta(|w-a|)|w-a|^n

whenever the segment from a to w stays in K1. All lower Taylor coefficients vanish at a as well. For n=1 this follows directly by integrating Df along that segment, subtracting Df(a)=0, and using its uniform modulus of continuity. For w in B(z,delta/2), therefore,

    |f(w)|<=eta(3delta/2)(3delta/2)^n.

The ball avoids F. Apply the submean inequality to the subharmonic function log|H| there, using its locally integrable logarithmic identity from Section 5. Boundedness of Z and the lower bound for the disc mean of Re s give

    |H(z)|<=C eta(3delta/2)delta^(n-sigma).

At zeros of H the bound holds trivially. All constants are uniform on the chosen compact discs. Since n-sigma>=0, H tends to zero as z approaches F, including at the equality n=sigma. Define H=0 on F; it is continuous on D. A mere O(delta^n) Taylor bound would not give this conclusion at equality, so the little-o modulus is essential.

The extension is holomorphic wherever it is nonzero: every such point is outside F, where Section 5 already gives holomorphy. Its actual zero set may also contain isolated points outside F. The next lemma applies to that entire actual zero set. No C1 extension or differentiability at F is assumed.

## 7. A complete proof of the classical Rado lemma

Let O be an open planar set, let G:O->C be continuous, and assume G is holomorphic on O minus E, where E={G=0}. Then G is holomorphic on O. Here E can have arbitrary geometry and positive area.

Choose a smooth nondecreasing function theta on the real line, zero on (-infinity,1], equal to one on [2,infinity), and between zero and one. Integrating theta from zero gives a smooth convex nondecreasing function chi on [0,infinity), with chi=0 below 1, chi'=1 above 2, and 0<=chi(t)<=t. For epsilon>0 define

    chi_epsilon(t)=epsilon^2 chi(t/epsilon^2),
    u_epsilon=chi_epsilon(|G|^2).

Each u_epsilon is smooth throughout O. Off E this follows from holomorphy. At every point of E, continuity makes |G|<epsilon on a neighborhood, and u_epsilon is identically zero there. The ordinary smooth chain rule away from E gives

    Delta u_epsilon
      =4[chi_epsilon'(|G|^2)+|G|^2 chi_epsilon''(|G|^2)]|G'|^2 >=0.

The bracket is one when |G|>=sqrt(2)epsilon, and both sides are zero near E. For a compact K in O choose phi smooth, nonnegative, compactly supported in O and equal to one near K. Ordinary integration by parts gives

    4 integral_(K intersect {|G|>sqrt(2)epsilon}) |G'|^2
      <= integral phi Delta u_epsilon
       = integral u_epsilon Delta phi
      <= sup_(supp phi)|G|^2 integral |Delta phi|.

The right side is finite by continuity and independent of epsilon. Taking a decreasing sequence epsilon->0 and monotone convergence shows that G', defined to be zero on E, is in L2 locally on O. This energy estimate is proved before any assertion that G has weak derivatives across E.

Next choose a smooth psi:[0,infinity)->[0,1], zero below 1 and one above 2, and set

    v_epsilon=G psi(|G|^2/epsilon^2).

Again v_epsilon is smooth, including near E, and |v_epsilon-G|<=sqrt(2)epsilon. Off E, dbar G=0 and dbar |G|^2=G conjugate(G'), whence

    dbar v_epsilon=G^2 conjugate(G') psi'(|G|^2/epsilon^2)/epsilon^2,
    |dbar v_epsilon|<=2 norm_infinity(psi') |G'|
                         1_{epsilon<|G|<sqrt(2)epsilon}.

On E the derivative vanishes. The indicator tends pointwise to zero off E, while the extended G' is zero on E. The proved L2 bound and dominated convergence give dbar v_epsilon->0 in L2 locally. Uniform convergence v_epsilon->G and integration against compactly supported smooth test functions therefore yield dbar G=0 in distributions. Weyl's lemma provides a holomorphic representative; continuity identifies it with G everywhere. This proves the lemma without a prior Sobolev assertion, a distributional nonlinear chain rule, or a removability hypothesis on E.

Apply this lemma to the extension H in Section 6. It is holomorphic throughout D. The proof does not claim this classical lemma as new.

## 8. Isolation of every zero and finite integral order

If H is identically zero, f is identically zero: a point with f nonzero is outside F and outside the zeros of Z, and its local representative gives H nonzero. Assume instead H is not identically zero.

All points of F are zeros of the holomorphic H, hence form a discrete set. Positive-index zeros outside F also give zeros of H. Nonpositive-index zeros outside F are finitely many by Section 4; H is nonzero at each, by the exact local meromorphic expression and exact pole cancellation. Thus zeros of f cannot accumulate at any point of D. This proves the full isolation assertion without assuming F empty.

At a zero outside F, |f(a+w)|>=c|w|^m gives the required integral lower bound immediately. At a in F, choose a small disc containing no other zero of H and no zero of Z. Write

    H(z)=(z-a)^ell H0(z),

with finite ell>=1 and H0 holomorphic and nowhere zero. The logarithmic identity now extends almost everywhere across the discrete exceptional set and proves log|f| locally integrable. Its disc means are

    mean log|H|=ell(log r-1/2)+log|H0(a)|,
    mean log|Z|=log|Z(a)|.

Using mean Re s>=sigma log r-C yields

    mean_(B(a,r)) log|f| >=(ell+sigma)log r-C.

Jensen's inequality for exp(2x), including the area factor pi r^2, gives

    integral_(B(a,r)) |f|^2 >= C' r^(2(ell+sigma)+2),

with C'>0. This finite power contradicts infinite integral order. The exponent need not be an integer; a larger finite integer also gives a lower bound after shrinking to r<1.

## 9. Connected domains and the smooth theorem

The local construction also proves weak continuation on each admissible disc. If f vanishes on an open subdisc, H vanishes there, so the holomorphic identity theorem and Section 8 imply f=0 throughout that disc. The set of points having a zero neighborhood is therefore both open and closed in a connected domain covered by admissible discs: at a closure point, an admissible disc intersects one of those zero neighborhoods and weak continuation applies. Infinite integral order first gives a zero disc by the local theorem, and propagation gives zero on the domain.

For smooth f and locally finite weak-L2 norm, choose n on each compact disc after M is known, with n>=1 and n>=2M/sqrt(pi). This recovers continuation for arbitrary finite weak norm without borrowing the earlier smooth theorem as a premise. It also recovers the smooth finite-Taylor-order alternative: a smooth infinite-order Taylor zero would have infinite integral order and hence force zero. At finite n only the integral-order conclusion is proved.

## 10. The conditional C^n carrier consequence

Fix 0<c<1/2 and finite real omega. Let Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X=Ax. On an open region avoiding zero assume V is C^n and

    div V=0, X.V=0, (DV)X=-LV.

For a smooth transverse section sigma, let g be the positive transverse metric formed by projecting its coordinate tangent vectors onto X-perp. The exact quotient equations A2463-A2464, independently reread through Sections 1-3 of in the team records, involve only first derivatives of V. All their metric coefficients depend smoothly on X and the section, not on extra derivatives of V. Smooth local isothermal coordinates therefore produce a C^n scalar f by an invertible smooth real-linear transformation of the two independent components of V.

If |(curl V).X|<=B|V| on the section, the equations imply

    |dbar f|<=b|f|,
    b(z)=C1+C2 B(y(z)),

with finite nonnegative constants C1,C2 on a smaller coordinate disc Delta. The additional hypothesis is exactly

    sup_(t>0)t sqrt(area{z in Delta:b(z)>t}) <=n sqrt(pi)/2.

It is a norm of this reduced coefficient in this actual chart. It must not be silently replaced by the same numerical bound on the raw Euclidean quotient B. Smooth changes of measure preserve weak-L2 membership but can change this numerical constant.

Assume V restricted to the section vanishes faster than every pointwise power at the center. The invertible transformation and local coordinate comparability give infinite integral order for f, so V=0 on a smaller section. The transport ODE yields

    V(exp(tA)x)=exp(-tL)V(x)

for the finite local times remaining in the region. The inverse function theorem for the transverse flowbox gives V=0 on an ambient neighborhood. Completeness of any nonlinear characteristic flow, boundary terms at infinity and a pressure normalization play no role.

All fixed finite omega are allowed; the constants, chart and raw-coordinate sufficient norm can depend on c and omega. This does not establish a uniform raw-quotient threshold, any Euler estimate of b, exclusion of the full common-flat system, or the unrestricted conjecture.

## 11. Source verification, attribution and unresolved extensions

All ten submitted sections and all 46 manual self-checks were read. The exact submitted proof is retained with SHA256 5cf9ecb72399f0d2dfd43b608b2e53e49f10b1b765c505eb1af64859624f10f9. No mathematical computation is needed or was run for this reconstruction. Sections 2-5 and 8-10 have been reconstructed here independently of the pending LIT344 verdict. The new step is the continuous extension and the fully proved zero-set lemma in Sections 6-7, which allow n=1 and the improved closed condition sigma<=n.

The standard scalar inputs are the distributional Cauchy fundamental solution, the harmonic or dbar Weyl lemma, Taylor's formula, the argument principle, holomorphic mean estimates and Jensen's inequality. No endpoint uniqueness theorem is imported. The only carrier-specific dependency is the confirmed pre-continuation quotient calculation.

For historical attribution I read page 1 and the precise reference 19 of the actual local PDF of Slawomir Dinew and Zywomir Dinew, Rado-type theorem for subharmonic and plurisubharmonic functions, arXiv:2109.10842v1, September 22, 2021. Its page 1 Theorem 1.1 states exactly the continuous, holomorphic-off-own-zeros theorem. Its reference 19 is T. Rado, Uber eine nicht fortsetzbare Riemannsche Mannigfaltigkeit, Mathematische Zeitschrift 20 (1924), no. 1, 1-6. The PDF SHA256 is d18848d733eb72d354bf81fa535491ed38ce2cb93e3ff85ff266e678e2543fb4. Its broader theorems have not been read or used; the original 1924 paper was not obtained or read. The lit agent's reading note and retrieval manifest were read. Its two earlier mistaken candidates, an unrelated semigroup HTML response and an unrelated physics PDF, are explicitly rejected and supply no evidence. Our Section 7 is the complete proof of the only classical statement used, so its validity does not depend on these retrievals.

The finite-n theorem with an arbitrary weak norm, the optimal norm threshold, a Sobolev version, the needed Euler quotient bound and the global Euler nonexistence conjecture remain open here. The distinction between this finite-n statement and the unrestricted smooth statement is essential. For the already smooth full common-flat system, this does not improve the existing necessary weak-L2 obstruction.

## 12. Endpoint and counterexample checks

The first-order case uses only the C1 Taylor expansion with derivative remainder o(1), the resulting logarithmic remainder g=o(1), Dg=o(1/r), and the uniform first-derivative modulus in Section 6. The reciprocal-radius bound is locally integrable in two dimensions, and its boundary term is o(r); no second derivative is needed. The carrier reduction likewise uses only first derivatives of V and smooth geometry independent of V.

The holomorphic function z^(n+1) with b=0 has a nonempty n-jet-zero set and finite integral order. It does not satisfy infinite integral order, so the theorem does not force it to vanish. For f=conjugate(z) on the unit disc, b=1/|z| has M=sqrt(pi), sigma=2, and index -1 at its only zero. It meets the n=2 equality case, its negative-index charge is pi, and its finite integral order agrees with the conclusion. Its Cauchy potential is log|z|^2 inside the unit disc; exp(-Re s)=|z|^(-2) is not locally integrable. The present proof never assumes that integrability. No positive-index conclusion, optimal continuation constant, or Euler upper bound is inferred from these tests.

## 13. Complete comparison and evidence scope

All thirteen items and remarks W1-W3 of the coordinator's combined LIT344/LIT345 comparison were read. They agree with Sections1-12 here and with the direct C1-extension proof for LIT344. In particular, the comparison independently identifies the non-L2 angular-ray obstruction by superlevel area of order1/t, the finite charge of nonpositive indices, the n-jet set rather than the infinite-flat set, the uniform little-oh Taylor modulus at the closed endpoint, and the actual reduced-coefficient norm in the carrier consequence. No additional mathematical premise is needed.

Both versions of the comparison script and both full outputs were read, not run. The first polar quadrature hits an angular singularity, emits warnings, and reports a failure; its old item11 is a literal True. The revised quadrature uses a legitimate Stokes representation: F(z)=conj(z-zeta)/(z-zeta) has modulus one off zeta, its gradient is locally integrable, and the boundary contribution of a removed epsilon-circle tends to zero. Thus dbar F=1/(z-zeta) distributionally and the area mean is a boundary integral. The seven floating evaluations corroborate, but do not prove, the exact disc-mean calculation in Section2. The revised script reports19 passing conditions, several of which are finite grids or evaluations at selected points. Its Rado derivative formulas are evaluated at one point of one polynomial example, whereas Section7 proves the formulas for every holomorphic function. No exact or universal theorem is inferred merely from that pass count. Both scripts print their outcome without assigning a failing process exit code.

The comparison's header claims a finish time that was still in the future when its complete text and outputs were captured. The actual capture time, source hashes and a record of this chronology defect are in the team records. That header is not accepted as observed runtime; the mathematical comparison is evaluated on its contents. The first output's absolute local path prefixes were replaced by relative labels in the retained evidence, and both original and transformed hashes are recorded. No runtime was padded.

The comparison continues the existing configured model collaboration through files. Actual provider execution is independently unattested. The classical Rado lemma is not claimed as novel; its proof and the limited primary-source coverage remain as recorded in Section11. The finite-regularity theorem and its carrier consequence do not supply an Euler coefficient bound, an arbitrary-norm C1 or C2 theorem, or a Sobolev extension.

## 14. Corrected comparison chronology and a second future heading

The corrected combined-comparison header was captured and read as an exact diff. It now says that the first save was04:12:35Z and that the incorrect04:20Z finish was replaced at04:15Z using file records. All remaining comparison text is unchanged. The first save time is the coordinator's reported record; this audit independently observed the complete file before the designated verdicts at04:14:26Z. The correction removes the future finish and distinguishes the source of its chronology.

A separate Note209 was observed and captured at the real time in the team records, before its heading's04:21Z time. Its mathematical and planning content does not make that future time an observed publication time. That heading also needs correction from real records. The capture preserves the original heading; later passage of time would not validate it retroactively. Neither chronology issue changes A2898-A2901.

## 15. Source revision, W4 and the corrected Note209

The full difference from the submitted source to SHA25664a5c20ed9e217b85f650d0f58fe3d975efc3406e204cb2724ddc4d007707ee1 was read. It changes the status to A2899-A2901 with open scope A2902 and adds a confirmation section accurately describing the comparisons, diagnostic reading limits, and the mean-chain qualification. The mathematical proof does not change.

The exact difference from the previously captured header-corrected coordinator comparison to SHA25614813d7e68e433437f8f22db03bb83d3f8b04555428228783afe8df7c2569ddd was read in full. It adds W4, stating that the scripts print failures without setting a failing exit code, and that the selected-point and finite-grid evaluations are not general symbolic proofs. The header identifies this as its only further change. This accurately records the limitations already found in Section13; it does not add a mathematical premise.

The new Note209 explicitly records that its original04:21Z heading was in the future and that the heading was corrected at a reported04:19Z to04:13Z. This is accepted as an explicit repair of A2905's chronology claim. The originally reported posting and correction times remain the coordinator's records rather than independently observed event times. The prior capture is retained, and no waiting until a false future time became present was used to validate it.

## 16. Further Theory Agent C  comparison and diagnostic

The full Theory Agent C 04:21:23 comparison was read. Its Rado cutoff derivation, dominated-convergence bound, n=1 Taylor remainder, closed endpoint, finite-jet logarithmic remainder and exact norm substitutions agree with Sections1-12. Its requested explicit extension of the C67 calculation to C^n is already part of A2901 and this proof: the quotient equations involve only V and its first derivatives, with smooth geometric coefficients. The actual transformed coefficient and finite-time transport hypotheses are retained.

Both versions of the Theory Agent C 345 script and both full logs were read, not rerun. V2 has4 exact checks for two explicit polynomial examples,5 finite-grid checks and1 algebraic constant check. It removes the tautological first-version grid condition and exits with status1 on a failed condition. The generic Rado formulas follow from the hand calculation, not those finite examples. The comparison entry additionally mentions two negative controls, but no such controls occur in either inspected script or log; that particular reported execution is not independently verified or used as evidence. The hand proof and the ten recorded checks are unaffected.

## 17. Located negative controls

The complete Theory Agent C note of 2026-11-04T04:35:57Z, the complete script in the team records and its complete log were read. The new script adds one combined EX condition requiring both deliberately wrong identities to be false. On G=z^2-1/4 and phi(w)=w^3+2w^2-w, it tests the incorrect factor2 instead of4 in the Laplacian identity and the incorrect single G instead of G^2 in the dbar identity. These residuals are nonzero polynomials: the correct formulas were independently derived in the preceding sections, and their missing factors are nonzero on an open set. The log reports11 conditions passing, with five EX, five GRID and one FORMULA. It does not represent eleven universal symbolic identities. The script exits1 on a failure.

This supplies the previously unlocated controls as retained file evidence and repairs that part of A2913. The earlier interactive executions are not independently attested. No script was rerun, and no theorem or constant changes.
