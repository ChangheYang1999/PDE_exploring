# Independent finite-regularity weak-L2 continuation audit

Status: CONFIRMED A2898 at the exact scope stated below. The complete existing model comparison has been read; the stronger LIT345 result is separately confirmed. This is a local conditional scalar theorem and its local carrier consequence. It is not a proof of the Euler conjecture.

## 1. Exact statement and scope

Let D be a bounded open disc in the complex plane. Let n>=2 be an integer, f in C^n(D;C), and b:D->[0,infinity) be measurable and finite almost everywhere. Write dbar=(partial_x+i partial_y)/2 and assume

    |dbar f|<=b|f| almost everywhere,
    M=sup_(t>0) t sqrt(area{b>t})<infinity,
    sigma=2M/sqrt(pi)<=n-1.

Then either f is identically zero or all its zeros are isolated. Every zero a in the second alternative has finite integral order: there are C>0, N<infinity and r0>0 with

    integral_(B(a,r)) |f|^2 >= C r^N,    0<r<r0.

Thus vanishing of that integral faster than every power at one point implies f=0. The result localizes to a connected domain covered by relatively compact discs with these hypotheses; the integer may vary with the disc if the indicated regularity holds. For C2 the sufficient bound is M<=sqrt(pi)/2. No claim of optimality of this bound is made.

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

## 6. Uniform Taylor remainders on the entire set F

Work in two nested compact convex discs K0 inside the interior of K1 inside D. For z in K0 sufficiently close to F, a nearest a in F lies in K1. Set delta=dist(z,F). Uniform continuity of D^n f on K1, its vanishing at a, and Taylor's integral formula give a positive nondecreasing modulus eta(t)->0 such that

    |f(w)|<=eta(|w-a|)|w-a|^n

whenever the segment from a to w stays in K1. Lower Taylor coefficients vanish at a as well. For w in B(z,delta/2), therefore,

    |f(w)|<=eta(3delta/2)(3delta/2)^n.

The whole ball avoids F. Apply the submean inequality for log|H| there, the logarithmic identity in Section 5, boundedness of Z on K1, and the disc-mean lower bound for Re s. This gives

    |H(z)|<=C eta(3delta/2)delta^(n-sigma).

Since n-sigma>=1, this is o(delta), locally uniformly near F. Define H=0 on F. The extension is continuous. On the circle of radius delta/2 about z, the distances to F are between delta/2 and 3delta/2. The same estimate and Cauchy's derivative inequality give

    |H'(z)|<=C eta(3delta)delta^(n-sigma-1)->0.

For a in F, delta(z)<=|z-a| implies H(z)=o(|z-a|), so the real derivative at a is zero. These derivatives are continuous across F by the displayed estimate. The extension is C1 with dbar H=0 everywhere, hence holomorphic on D. No theorem about removal of an arbitrary closed or perfect set has been assumed.

This explicitly proves the closed endpoint n-sigma=1. Replacing the Taylor remainder by only O(delta^n) would lose the needed little-o statement at that endpoint.

## 7. Isolation of every zero and finite integral order

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

## 8. Connected domains and the smooth theorem

The local construction also proves weak continuation on each admissible disc. If f vanishes on an open subdisc, H vanishes there, so the holomorphic identity theorem and Section 7 imply f=0 throughout that disc. The set of points having a zero neighborhood is therefore both open and closed in a connected domain covered by admissible discs: at a closure point, an admissible disc intersects one of those zero neighborhoods and weak continuation applies. Infinite integral order first gives a zero disc by the local theorem, and propagation gives zero on the domain.

For smooth f and locally finite weak-L2 norm, choose n on each compact disc after M is known, with n>=2 and n>=1+2M/sqrt(pi). This recovers continuation for arbitrary finite weak norm without borrowing the earlier smooth theorem as a premise. It also recovers the smooth finite-Taylor-order alternative: a smooth infinite-order Taylor zero would have infinite integral order and hence force zero. At finite n only the integral-order conclusion is proved.

## 9. The conditional C^n carrier consequence

Fix 0<c<1/2 and finite real omega. Let Jx=e3 cross x, A=cI-omega J, L=(1-c)I+omega J, X=Ax. On an open region avoiding zero assume V is C^n and

    div V=0, X.V=0, (DV)X=-LV.

For a smooth transverse section sigma, let g be the positive transverse metric formed by projecting its coordinate tangent vectors onto X-perp. The exact quotient equations A2463-A2464, independently reread through Sections 1-3 of in the team records, involve only first derivatives of V. All their metric coefficients depend smoothly on X and the section, not on extra derivatives of V. Smooth local isothermal coordinates therefore produce a C^n scalar f by an invertible smooth real-linear transformation of the two independent components of V.

If |(curl V).X|<=B|V| on the section, the equations imply

    |dbar f|<=b|f|,
    b(z)=C1+C2 B(y(z)),

with finite nonnegative constants C1,C2 on a smaller coordinate disc Delta. The additional hypothesis is exactly

    sup_(t>0)t sqrt(area{z in Delta:b(z)>t}) <=(n-1)sqrt(pi)/2.

It is a norm of this reduced coefficient in this actual chart. It must not be silently replaced by the same numerical bound on the raw Euclidean quotient B. Smooth changes of measure preserve weak-L2 membership but can change this numerical constant.

Assume V restricted to the section vanishes faster than every pointwise power at the center. The invertible transformation and local coordinate comparability give infinite integral order for f, so V=0 on a smaller section. The transport ODE yields

    V(exp(tA)x)=exp(-tL)V(x)

for the finite local times remaining in the region. The inverse function theorem for the transverse flowbox gives V=0 on an ambient neighborhood. Completeness of any nonlinear characteristic flow, boundary terms at infinity and a pressure normalization play no role.

All fixed finite omega are allowed; the constants, chart and raw-coordinate sufficient norm can depend on c and omega. This does not establish a uniform raw-quotient threshold, any Euler estimate of b, exclusion of the full common-flat system, or the unrestricted conjecture.

## 10. Source verification and unresolved extensions

All nine submitted sections and all 32 manual self-checks were read. The exact submitted proof is retained with SHA256 3a23f74b7ade8edc819e0a6bcdad8d6257d7ce4584fcf2b7e1633d43a44662f6. No mathematical computation is needed or was run for this reconstruction. The independent checks include the sign of the disc kernel, the finite-regularity o(1/r) logarithmic derivative, the count of zero-index zeros, the direct closed-endpoint C1 extension, and the finite integral order at points of F.

The standard scalar inputs are the distributional Cauchy fundamental solution, the harmonic or dbar Weyl lemma, Taylor's formula, the argument principle, holomorphic mean and Cauchy estimates, and Jensen's inequality. No endpoint uniqueness theorem is imported. The only carrier-specific dependency is the confirmed pre-continuation quotient calculation.

The finite-n theorem with an arbitrary weak norm, the optimal norm threshold, a Sobolev version, the needed Euler quotient bound and the global Euler nonexistence conjecture remain open here. The distinction between this finite-n statement and the unrestricted smooth statement is essential.

## 11. Combined comparison and relation to LIT345

The full thirteen-item coordinator comparison of LIT344 and LIT345 was read, including its separate item10 on the direct C1 extension. It agrees with this proof: n-sigma>=1 gives H=o(delta), Cauchy estimates give H'=o(1), and extension by zero is C1 with dbar H=0. Thus this theorem is valid without an external zero-set removability theorem. The stronger LIT345 proof covers n>=1 and sigma<=n by continuous extension and the classical Rado lemma. LIT344 is a true special case, while its direct extension mechanism is independently verified here.

The comparison scripts, complete outputs, limited diagnostic scope and chronology defect are documented in the team records Section13, with captured evidence there. Neither proof needs the floating tests. Existing configured model collaboration is through files, with provider execution independently unattested. No additional mathematical computation was run.

## 12. Further Theory Agent C  comparison

The entire nine-item Theory Agent C  comparison headed04:12:40Z, its script and its full14-condition log were read. Its hand arguments agree with Sections1-10: the exact disc mean, the angular-ray contradiction from1/t level area, the index budget, the punctured logarithm, the uniform Taylor remainder and the direct C1 zero extension all retain their stated hypotheses. Its proposed finite-regularity extension of the first-derivative C67 reduction is now explicit in A2901.

The following limits apply to its diagnostic, which was not rerun here. It ends with a printed summary rather than a nonzero failure exit; a failing assertion would therefore not necessarily fail the process. Several conditions use quadrature or finite grids, as the note and file otherwise disclose. The index inequality is tested only for1<=m<30. Its universal proof is elementary: withk=-m+2N and0<=N<=m, one hasm-k=2(m-N); ifk<=0 thenm-N>=ceil(m/2)>=1, and ifk<0 thenm>=-k impliesm-k>=2|k|. The weak-norm identity line tests the high-level area formula, while the low-level bound requires the minimum with the disc area, already supplied by this audit. None of these diagnostic limitations creates a gap in the hand proof.

The optional corrections are appropriate: the corollary choosing an integern>=1+sigma should also retainn>=2 for this particular theorem; the holomorphic difference denotedh_a can be named explicitly; and estimates on slightly larger compact subsets are used for the Cauchy derivative bound. A2900 separately coversn=1 at its stronger threshold. No new unqualified finite-regularity or Euler theorem follows from this comparison.

## 13. Qualification of the comparison: equality in the mean bound

The further literature-agent check identifies a literal exception to the comparison approved in A2907. Item2 says that source(7) is an equality forq=alpha/conjugate(z), R=1. The complete source(7) is a chain of two inequalities. Its first inequality is strict for this example: the exact absolute centered mean is2alpha log(1/rho)+alpha, whereas its final upper bound is2alpha log(1/rho)+2alpha. The positive difference isalpha. Only the second inequality, usingW(r)=2pi alpha r, is an equality. The coefficient oflog(1/rho) is sharp, as both the source theorem and the independent proof correctly state.

Thus the all-of-(7) equality wording is refuted. Section12 and A2907 confirm the mathematical comparison subject to this explicit correction; they must not be cited to certify that literal equality. A2898 and the finite-regularity theorem are unchanged. This correction was identified through the existing cross-agent comparison, not by a new calculation.

## 14. Source confirmation revision

The complete difference from the submitted source to the revision with SHA256 bfb6f7df98f130eea3856bf0e8c98079b72f048257122924565deff7c0ca7d48 was read. It changes the status to A2898, keeps the open scope A2902, requires n>=max(2,1+sigma) in the smooth recovery, identifies h_a=s-s_a, and uses a slightly larger compact disc in the Cauchy estimate. Its added Section10 reports the comparison scope and the correct mean-chain counterexample. These are valid clarifications, and none changes the proven threshold or conclusion. The original submission, full exact difference and current revision are all retained.

## 15. Repaired Theory Agent C  diagnostic scope

The complete v2 script difference and full14-condition log were read. Only the condition classes and failure-exit behavior change. The count is5 symbolic identities,4 algebraic checks of a stated formula,2 quadratures,1 finite random sample,1 finite integer grid and1 exact example. The weak-norm formula check concerns its stated high-level regime, and the integer grid remains1<=m<30; the universal arguments are the written ones in this proof. Failures now exit with status1. This repairs the diagnostic limitation in A2907, while the literal mean-chain wording corrected by A2908 remained in the old comparison when last inspected. No theorem or constant changes and no diagnostic was rerun here.


## 16. Corrected Theory Agent C  mean comparison

The new Theory Agent C 04:27:42 note and the corrected original item2 were fully read. They expressly distinguish the exact mean 2alpha log(1/rho)+alpha from the upper bound 2alpha log(1/rho)+2alpha. The triangle step with the exact kernel is equality in this radial example; replacement of the interior kernel r/rho^2 by 1/rho is strict. The final distribution-function bound is equality. These statements agree with Section13 and repair the literal comparison defect A2908. The original erroneous text remains acknowledged in the correction. No theorem, constant or computation changes.
