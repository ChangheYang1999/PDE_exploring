# Two attracting saddle networks and the pointwise expansion quantifier

Status: CONFIRMED at the exact construction and source-reading scopes of A450-A452, after focused configured-model review and independent verification of its precision points. The constructions are compact smooth flows, not Euler profiles. The source comparison below separates literal pointwise hypotheses from positive-volume hypotheses, pointwise neighborhood hypotheses, and an added neighborhood bundle-containment assumption.

## 1. Statement and conventions

Equip the torus T2=(R/(2pi Z))^2 and M=T2 times S1 with their flat product metrics. Fix 0<epsilon<1, 0<delta<1 and 0<zeta<pi/2. Define

    H(x,y)=cos x cos y, J2(u,v)=(-v,u),
    Wnet={H=0}, S={cos x=cos y=0},
    Xminus=(cos x(sin y+epsilon sin x),
            cos y(-sin x+epsilon sin y)),
    Xzero=J2 grad H-epsilon H grad H,
    Gminus=(Xminus,-10 sin z), Gzero=(Xzero,-10 sin z),
    U={|H|<delta} times {|z|<zeta}, Lambda=Wnet times {0}.

For either field the flow Phi is complete and C-infinity, U is strictly trapping in the sense closure(Phi_t U) is contained in U for every t>0, and its maximal invariant set is Lambda. This set admits the invariant splitting

    Es=R partial_z, Ecu=T(T2) times {0}

with dim Es=1, dim Ecu=2, stable contraction at rate10 and domination at rate at least4. It consists of four hyperbolic saddles and eight connecting open arcs. Every point of Lambda converges forward to a saddle. Thus the set of its points not converging to an equilibrium is empty.

Every invariant probability supported on Lambda is a mixture of its four equilibrium atoms. Neither field admits an SRB probability supported there, where SRB means the positive-exponent entropy formula or absolute continuity of unstable conditional measures. These conclusions hold also for time-one invariant probabilities.

For Gminus no probability supported on Lambda is physical, even if physical probabilities are allowed to be nonergodic. For Gzero the unique ordinary physical probability supported on Lambda is

    mu0=(1/4) sum_(sigma in S) delta_(sigma,0).

Its basin has full volume in U, it is nonergodic, and no ergodic probability supported on Lambda is physical. Here an ordinary physical probability is an invariant probability whose basin of convergence of continuous-time empirical probabilities has positive ambient volume. The same conclusions hold for time-one empirical probabilities.

For every p in U the central logarithmic determinant growth rate is -2epsilon for Gminus and zero for Gzero. Consequently neither example satisfies positive sectional expansion on a positive-volume subset of U. No continuous extension of the prescribed Ecu to a neighborhood of Lambda can contain G everywhere in that neighborhood.

## 2. Trapping and the invariant set

Direct differentiation gives

    Xminus H=-epsilon H(sin^2 x+sin^2 y),
    Xzero H=-epsilon H|grad H|^2.                         (1)

The sign of H is invariant. Since

    sin^2 x+sin^2 y >= 1-H^2,

nonzero |H| for Xminus decreases at least exponentially at rate epsilon(1-delta^2) in the closed delta band. It increases at that rate in backward time and reaches the boundary in finite time. The closed band therefore maps strictly inside itself at each positive time, and its maximal invariant set is Wnet.

The critical points of H are exactly S at level0 and the four points sin x=sin y=0 at levels1 or -1. For Xzero, the boundary of the delta band is regular and the derivative of |H| is strictly negative there. The closed band is positively invariant by the inward-pointing boundary condition and uniqueness. Every boundary point enters its interior immediately and every interior point stays interior. Its image at any positive time is compact, hence is a compact subset of the interior. On each compact band a<=|H|<=delta with a>0, |grad H| has a positive minimum. Equation(1) makes an orbit with initial |H|=a exit the delta band in finite backward time. It also rules out a positive forward limit of |H|. Thus the maximal invariant set is Wnet and every forward orbit in the band approaches it in distance.

The z equation is strictly trapping on [-zeta,zeta], with maximal invariant set {0}, because sin|z| >= (sin zeta/zeta)|z| there. This proves the asserted product trapping, maximal invariance and attraction. Compactness of M gives completeness in both time directions.

## 3. The saddle network and domination

For Xminus, simultaneous zeros with both cosines nonzero would satisfy sin y=-epsilon sin x and sin x=epsilon sin y. They therefore lie at |H|=1, outside the band. If one cosine vanishes, epsilon<1 forces the other to vanish at a zero. For Xzero, J2-epsilon H I is invertible, so its zeros are exactly the critical points of H. Thus both fields have exactly S as zeros in the band.

At a point of S write sigma=sin x sin y in {1,-1}. The two horizontal Jacobians are

    DXminus=diag(-sigma-epsilon,sigma-epsilon),
    DXzero=diag(-sigma,sigma).                           (2)

The second identity uses H=grad H=0 at S. The eigenvalues are respectively 1-epsilon,-1-epsilon and 1,-1. On the edge cos x=0, Xminus has remaining component

    y'=cos y(-sin x+epsilon sin y).

The factor in parentheses is nonzero of fixed sign because |sin x|=1>epsilon. The other edges have the same property. Xzero restricts to J2 grad H on Wnet and has the same directed connections. There are four corners and eight open connecting arcs. Every point on an arc converges forward to its outgoing corner, and no arc point is recurrent.

The product splitting is invariant. Its stable derivative equals exp(-10t). Globally ||DXminus|| is at most its Frobenius norm, bounded by sqrt(2(1+epsilon)^2+2)<sqrt(10). Also

    ||D(J2 grad H)||<=2,
    ||D(H grad H)||<=|grad H|^2+|H| ||Hess H||<=4.

Thus ||DXzero||<6. The variational equation gives ||D Phi_-t|Ecu||<=exp(6t). Consequently on Lambda, for t>=0,

    ||D Phi_t|Es||=exp(-10t),
    ||D Phi_t|Es|| ||D Phi_-t|Ecu||<=exp(-4t).          (3)

All four product equilibria are hyperbolic saddles with one positive and two negative eigenvalues. The flow direction at regular points of Lambda is horizontal, so it belongs to Ecu there.

## 4. Invariant measures and central growth

Poincare recurrence for an invariant probability of the time-one map gives zero measure to every open connecting arc. There are only eight such arcs, so every invariant probability on Lambda is a mixture of its four atoms. A full-flow invariant probability is in particular time-one invariant. These mixtures have entropy zero and the positive-exponent sum equal to 1-epsilon or1. Hence none satisfies the positive-exponent entropy formula. Their unstable conditional measures are also atomic, not absolutely continuous with respect to unstable length.

For Gzero, entropy nevertheless equals the integral of the logarithmic central determinant: both are zero. This equality is weaker than the positive-exponent entropy formula, whose right side is1. It supplies neither a positive entropy assertion nor an SRB conclusion.

The horizontal bundle extends invariantly over all of M, whether or not it contains G. Put

    q(p)=log det(D Phi_1|Ecu_p).

It is a continuous real function. At every equilibrium q=-2epsilon for Gminus and q=0 for Gzero. Every time-one empirical weak limit of a point p in U is invariant and supported on Lambda by attraction. Its q integral is therefore that same constant. Compactness of the space of probabilities implies that every subsequential q average has this value, so the q averages converge. The determinant cocycle then yields

    lim_(n->infinity) n^(-1) log det(D Phi_n|Ecu_p)
         =-2epsilon or0.                                (4)

Uniform derivative bounds over a residual time interval of length at most1 give the identical limit for arbitrary real times. The central dimension is2, so inverse exterior-square expansion is exactly the negative of this logarithmic determinant. Strictly positive asymptotic central area expansion occurs at no point of U.

## 5. Corner passage estimates, with their uniform errors

The signs of cos x and cos y are preserved by either field. For Xzero this follows from the factorized coordinates

    Xzero_x=cos x(sin y+epsilon sin x cos^2 y),
    Xzero_y=cos y(-sin x+epsilon sin y cos^2 x).

The four components of T2 minus Wnet are invariant rectangular cells. An off-network point of the delta band approaches the boundary of its cell. It cannot converge to one corner: the local stable manifold there is its invariant coordinate edge, by the local saddle equations and uniqueness. Small corner boxes and flow strips along the regular edges cover a sufficiently small one-sided neighborhood of the cell boundary. The edge directions fix the order of passage through the four corners. Thus each such orbit eventually visits the four distinct corners cyclically forever.

Let a,b be the positive unstable rate and the absolute stable rate. They are a=1-epsilon,b=1+epsilon for Xminus, and a=b=1 for Xzero. Signed local coordinates u,v, chosen into the cell along unstable and stable axes, satisfy

    u'=u(a+R1), v'=v(-b+R2),
    |R1|+|R2|<=C(|u|+|v|).                              (5)

This follows from the smooth invariant coordinate axes and(2). Choose a common sufficiently small box size h for all four corners. On a visit entering at |v|=h,|u|=s and exiting at |u|=h,|v|=t, both coordinates are monotone in magnitude and

    integral |u| dt<=2h/a, integral |v| dt<=2h/b.

Integrating(5) over its residence time tau gives

    log(h/s)=a tau+O(1), log(t/h)=-b tau+O(1).             (6)

The constants are independent of the small incoming distance s and of the corner. Smooth transition maps along each compact regular edge have nonzero transverse derivative and bounded positive travel time. The next incoming distance is c_j t+O(t^2), with c_j>0. Therefore consecutive residence times satisfy

    tau_(n+1)=(b/a) tau_n+O(1), tau_n->infinity.           (7)

The last limit follows from attraction to the network and (6). There are only four boxes and strips, so the error bound in(7) is uniform for all sufficiently late visits. Total transition time over N visits is O(N).

For each continuous observable f and visited corner A_n,

    integral_(visit n) f(Phi_t p) dt=f(A_n,0) tau_n+o(tau_n). (8)

Indeed, outside a fixed smaller corner box the logarithmic monotonicity bounds give a uniformly bounded time per visit. Inside it uniform continuity makes f close to its corner value. The vertical coordinate tends to0, and its effect also disappears by uniform continuity. First let n grow and then shrink the smaller box. The same argument bounds the summed errors relative to the summed residence times.

## 6. Historic behavior when the central trace is negative

For Xminus put r=b/a>1. From(7), tau_n/r^n converges to a finite limit L. This limit is positive: once tau_N exceeds K/(r-1), where K bounds the recurrence error, the lower recurrence gives a strictly positive geometric lower bound. The tail of the absolutely convergent error series then yields

    tau_n=L r^n+O(1), L>0.                               (9)

At the end of the nth visit, along a subsequence ending at corner A_j, (8)-(9) give the limiting empirical probability

    nu_j=(r^3 delta_(A_j,0)+r^2 delta_(A_(j-1),0)
          +r delta_(A_(j-2),0)+delta_(A_(j-3),0))
          /(1+r+r^2+r^3).                               (10)

Here corner indices are cyclic. The weights follow by summing each residue class of the geometric residence series. The transition time O(n) and any initial time are negligible. All four nu_j are distinct, so every off-network point in U has nonconvergent empirical probabilities. The same limits hold with time-one sampling: rounding each visit endpoint changes the number of samples by a bounded amount, and the number of visits is negligible relative to total time.

The exceptional set Wnet times (-zeta,zeta) has ambient volume zero. If an initial point anywhere in M has an empirical limit supported on Lambda, it must enter U: integrate a continuous function supported in U and equal to1 near Lambda. Its limiting average is1. After entry the orbit remains in U. If its empirical probabilities converge, its image at an integer time after entry must therefore lie in the exceptional null set. A countable union of smooth inverse images of that set has zero volume. No probability supported on Lambda has a positive-volume basin anywhere in M.

## 7. The ordinary physical measure at zero central trace

For Xzero, (7) gives tau_n->infinity and |tau_(n+1)-tau_n|<=C0 for a fixed C0>0 after finitely many visits. Within each block of four visits the residence times differ by at most3C0. Up to N complete visits, the sums belonging to any two corner classes therefore differ by O(N), apart from at most four unmatched final visits. Meanwhile

    (tau_1+...+tau_N)/N -> infinity.                      (11)

The last unmatched visit is negligible. For large n put m=floor(tau_n/(2C0)). Since tau_n<=tau_N+C0(n-N), eventually m fits among the preceding visits after the fixed initial segment. For 1<=j<=m,

    tau_(n-j)>=tau_n-C0j>=tau_n/2.

It follows that

    tau_n/(tau_1+...+tau_(n-1))<=2/m ->0.                (12)

Equations(11)-(12) make both unmatched visits and O(N) transition times negligible. Each corner has asymptotic time proportion1/4, including at arbitrary times within visits. Formula(8) then proves empirical convergence to mu0 at every point in U off the network product. Integer-time sampling has the same limit by the visit-count bound used above.

Thus mu0 has full-volume basin in U and is an ordinary physical probability. It is nonergodic. Any basin elsewhere in M of a probability supported on Lambda must eventually enter U, by the preceding cutoff argument. Almost every point in U has limit mu0. Smooth finite-time transport and a countable union over entry times show that every different supported probability has basin of volume zero globally. This proves uniqueness among ordinary physical probabilities supported on Lambda. It does not classify measures elsewhere in M.

## 8. The neighborhood bundle obstruction

Fix a corner sigma. For every sufficiently small z!=0,

    G(sigma,z)=(0,0,-10 sin z)

is a nonzero vertical vector. Any two-plane containing G(sigma,z) contains the vertical line. If such planes extended continuously to (sigma,0), their limit would also contain that line. The prescribed Ecu_(sigma,0) is horizontal and does not contain it. Therefore the central bundle cannot have the asserted neighborhood extension with flow containment. The invariant horizontal extension used in(4) exists; the additional flow-containment requirement fails.

## 9. Comparison with the actual source statements

The pinned ASS manuscript is arXiv2205.04207v6. The audited pages are4-7,11,13-14,45,51-53. Its page14 Corollary G imposes expansion pointwise at every point of the attracting set not converging to an equilibrium, with dim Ecu=2 and saddle equilibria, and concludes existence of a physical/SRB probability. On the literal pointwise reading, Gminus satisfies the printed attracting-set hypotheses: the quantified set is empty, and hence satisfies any universal expansion requirement. Sections2-6 prove that its existence conclusion fails even for ordinary nonergodic physical probabilities. The proof on page45 chooses a point outside the union of equilibrium stable manifolds, but that set is empty here. The proposed countertest therefore identifies this particular quantifier issue, not a failure of a positive-volume expansion theorem.

ASS Theorem E on page13 explicitly requires expansion on a positive-volume subset of the trapping neighborhood. Both examples fail that requirement by(4). Neither is a counterexample to that theorem or to Corollary G strengthened by that premise. Its page6 automatic extension assertion is separately contradicted by Section8. If neighborhood flow containment is imposed as an additional hypothesis, both examples fail that strengthened hypothesis too. This interpretation must remain explicit.

A third possible reading imposes the pointwise expansion requirement at every point of U that does not converge to an equilibrium, rather than only at points of Lambda. Both examples fail this reading: every off-network point of U fails to converge to an equilibrium, and its central growth is -2epsilon or0 by(4). ASS's sentence following Corollary G and AS's Remark1.11 on page9 motivate checking this distinction. The remark describes expansion along all ambient trajectories not converging to singularities. The literal attracting-set quantifier must not be silently replaced by that stronger neighborhood quantifier.

The pinned AS manuscript is arXiv2511.18986v1; pages4-9 were read. Page7 Theorem1.5 has a pointwise formulation but references a display with a positive-volume premise. Page8 Theorem A again quantifies over points not converging to equilibria and adds alternatives including central time-one determinant at least1 at each equilibrium. Gzero meets this equilibrium alternative with equality. Under a purely pointwise expansion reading on Lambda, its absence of any SRB or nonatomic invariant probability contradicts the physical/SRB conclusion as interpreted in the paragraph immediately after that theorem, which explicitly excludes equilibrium atoms. It does not contradict existence of an ordinary, possibly nonergodic physical probability: Section7 supplies exactly one such probability. If the named expansion condition imports the positive-volume clause from page6, Gzero fails the hypothesis instead. Its failure of neighborhood flow containment is also unchanged.

The source formulations therefore require separate verdicts by interpretation. Neither construction licenses a blanket refutation of either manuscript. The negative-trace example does not meet AS's equilibrium determinant alternative. The zero-trace example does not lack ordinary physical measures.

## 10. Dependencies, verification and scope

The proof uses elementary smooth-flow existence and uniqueness, the finite-dimensional hyperbolic stable-manifold theorem to identify the local stable branch, smooth transverse flow maps, Poincare recurrence and weak compactness of probabilities on a compact space. All passage estimates, physical-basin claims and determinant limits are proved above. No Euler assertion is used. Actual source PDFs and extracted text are pinned in verification; the decisive statement and proof pages were also rendered and visually inspected. The submitted proof and focused coordinator review are pinned separately. Neither agent's symbolic script has been reproduced by this auditor, and neither is evidence for the dynamical conclusions here. The exact differentiation has been independently checked by hand.

The focused coordinator review confirms the construction, residence asymptotics, physical basins and literal source readings. Its requested distinction concerning the pointwise condition in U, the vertical-coordinate limit and the zero-trace entropy equality are incorporated. Its broader claim about every singular partially hyperbolic attracting set is not used: Section8 proves the needed obstruction directly for these two models. The mechanism is the attracting saddle-network mechanism also discussed in ASS's examples on pages51-53; no priority claim for that mechanism is made.

These compact torus flows are countertests for source hypotheses. They are not rotating self-similar Euler profiles and make no progress toward constructing a target counterexample or removing the unresolved global C2 growth condition. The review was exchanged through existing working files configured for model; this identifies the configured model and is not independent provider attestation.
