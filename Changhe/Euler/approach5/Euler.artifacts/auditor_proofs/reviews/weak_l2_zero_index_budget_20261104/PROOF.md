# Weak-L2 zero charges and the absence of isolated flat points

Status: independent analytic reconstruction complete; existing model comparison and designated verdict pending. No computation is needed.

## 1. Exact statement and notation

Let D be an open disc in the complex plane, let f:D->C be smooth, and put partial_bar=(partial_x+i partial_y)/2 and dA=dx dy. Let b:D->[0,infinity] be measurable and satisfy

    |partial_bar f| <= b|f| almost everywhere,
    M = sup_(t>0) t |{z in D:b(z)>t}|^(1/2) < infinity.          (1)

No local L2 or local boundedness assumption is imposed. A finite-order zero p has first nonzero real homogeneous Taylor polynomial P_p of degree m_p>=1. A flat point has all real partial derivatives, including its value, equal to zero. Denote the flat set by F.

Every finite-order zero is isolated and P_p is nonzero on the unit circle. Set

    p_p(theta)=P_p(exp(i theta)),
    A_p(theta)=[m_p+i p_p'(theta)/p_p(theta)]/2,
    d_p=(1/2) integral_0^(2pi) |A_p(theta)|^2 dtheta.             (2)

Its winding index k_p is in {-m_p,-m_p+2,...,m_p}. For every finite collection J of finite-order zeros,

    sum_(p in J) d_p <= M^2,
    sum_(p in J) (m_p-k_p)^2 <= 4M^2/pi.                        (3)

Consequently there are at most floor(M^2/pi) zeros with k_p<m_p, and

    sum_(k_p<0) k_p^2 <= M^2/pi,
    sum_(k_p<0) |k_p| <= M^2/pi.                              (4)

All infinite sums mean the supremum of finite subsums. The flat set F is relatively closed in D and has no isolated point. If nonempty, it is uncountable in every neighborhood of each of its points. These conclusions do not exclude a nonempty perfect flat set and do not establish general weak-L2 strong unique continuation.

## 2. Blow-up at a finite-order zero

Fix a finite-order zero p, write m=m_p, and let A={1/2<|w|<2}. For a sequence epsilon_n decreasing to zero with p+epsilon_n A contained in D define

    f_n(w)=epsilon_n^(-m) f(p+epsilon_n w),
    b_n(w)=epsilon_n b(p+epsilon_n w).

Taylor's theorem gives f_n->P_p in C1 on the closed annulus. For every t>0,

    t^2 |{w in A:b_n(w)>t}|
      =(t/epsilon_n)^2 |{z in p+epsilon_n A:b(z)>t/epsilon_n}|
      <=M^2.                                                  (5)

On {P_p!=0}, q_n=(partial_bar f_n)/f_n is defined for all sufficiently large n and tends to q_P=(partial_bar P_p)/P_p. Define q_n=0 at its other zeros. It is bounded in magnitude by b_n almost everywhere. A single null set suffices after taking the countable union for the chosen sequence. If |q_P(w)|>t, then |q_n(w)|>t eventually. Fatou's lemma therefore gives

    t^2 |{w in A:P_p(w)!=0, |q_P(w)|>t}|<=M^2.                  (6)

This uses a bounded weak norm, not a norm that tends to zero.

Write P_p(r exp(i theta))=r^m p_p(theta). The polar identity gives

    q_P(r exp(i theta))
      =exp(i theta)[m+i p_p'(theta)/p_p(theta)]/(2r).            (7)

Suppose p_p vanishes at theta_*. As a nonzero trigonometric polynomial it has a finite order l>=1 there. Thus p_p'/p_p=l/(theta-theta_*)+O(1). On a fixed radial strip contained in A, (7) is at least c/|theta-theta_*| in magnitude on a small punctured angular interval. Its superlevel area is at least c'/t for all sufficiently large t. This contradicts (6). Hence min |p_p|>0. The Taylor remainder then yields |f(p+w)|>=c_0|w|^m for small nonzero w. The zero is isolated.

Finite-order zeros are countable: choose for each an element of a countable Euclidean basis containing it and no other zero. This assignment is injective after a fixed choice rule.

## 3. Index, exact charge and summation

Every homogeneous complex polynomial in two real variables of degree m can be written as sum_(l=0)^m c_l z^l conjugate(z)^(m-l). On the unit circle this is exp(-im theta) Q(exp(2i theta)), where Q has degree at most m and no root on the unit circle. If N roots of Q, with multiplicity, lie inside the unit disc, factorization gives

    k=-m+2N,  0<=N<=m.                                        (8)

Indeed each inside root contributes one turn on a single traversal of that circle and each outside root contributes zero; exp(2i theta) traverses it twice. The ratio f/P_p is homotopic to 1 on a sufficiently small circle about p, so this is the index of f.

Let E(w)=f(p+w)-P_p(w). Taylor bounds give E=O(|w|^(m+1)) and DE=O(|w|^m). Since |P_p(w)|>=c_0|w|^m, the quotient E/P_p is O(|w|), with bounded derivative on the punctured small disc. It extends to a Lipschitz function equal to zero at p. Direct division of derivatives gives the uniform expansion

    (partial_bar f)/f(p+r exp(i theta))
      =exp(i theta)A_p(theta)/r+O(1).                          (9)

Choose a small disc about p on which the remainder is bounded by C. Then b>=|A_p(theta)|/r-C almost everywhere there. For t sufficiently large, every radius less than |A_p(theta)|/(t+C) lies in that disc, since A_p is bounded. Polar integration gives

    liminf_(t->infinity) t^2 |{b>t} intersect B_rho(p)|
      >=(1/2) integral |A_p(theta)|^2 dtheta=d_p.              (10)

Strict radial inequality handles the strict superlevel convention. Directions where A_p=0 contribute zero.

The integral of p_p'/p_p is 2pi i k. Hence the mean of Re A_p is (m-k)/2. Cauchy-Schwarz, first discarding the imaginary part, yields

    d_p >= pi (m-k)^2/4.                                      (11)

For any finite family choose pairwise disjoint discs compactly contained in D. Their superlevel areas add. Summing (10), using the finite-sum lower-limit inequality, and then using (1), proves (3). Equation (8) shows m-k is a nonnegative even integer. Every zero with k<m therefore costs at least pi. For k<0, m>=|k| implies (m-k)^2>=4k^2. Since |k|<=k^2 for a negative integer, (4) follows. No sum over infinitely many discs is interchanged with a limit.

## 4. Logarithmic means across nonholomorphic zeros

Suppose zero were isolated in F, after translating coordinates. Choose R>0 with the closed disc of radius R contained in D and with no other point of F. Every zero in 0<|z|<R is then finite order and isolated. There are finitely many zeros on each compact annulus, because an accumulation point there would be a zero that is either not isolated or flat.

Near such a zero p, (9)'s Taylor argument gives

    log|f(z)|=m log|z-p|+log|p_p(arg(z-p))|+g(z),               (12)

where g is Lipschitz. The middle term is bounded, since p_p never vanishes on the circle, and its gradient is O(1/|z-p|). All terms belong locally to W^{1,1} in the plane. Thus log|f| is W^{1,1} on every compact annulus about zero.

Define h(r) as the normalized actual circle mean of log|f|. It is finite even if the circle meets a zero. To check continuity there, write p=r_p exp(i theta_p). On r near r_p>0,

    |r exp(i theta)-p|^2
      =(r-r_p)^2+2r r_p[1-cos(theta-theta_p)].                 (13)

On a fixed small angular interval the distance is bounded below by c|theta-theta_p|, uniformly in r. The absolute logarithm of a distance smaller than 1 is consequently bounded above by C+|log|theta-theta_p||, which is integrable in theta. Dominated convergence proves continuity of the logarithmic term's circle integral, also after a smooth cutoff. The bounded angular term has pointwise convergence except at the one angle meeting p, so the same theorem applies. The Lipschitz remainder is continuous. A finite partition near the finitely many relevant zeros proves continuity of h at every positive radius.

Polar coordinates and W^{1,1} Fubini give a W^{1,1} radial mean on any compact radial interval, with derivative equal almost everywhere to the mean radial derivative. Its continuous representative is the actual h just established. Therefore h is locally absolutely continuous. The stronger holomorphic leading-term assertion from the punctured-L2 theorem is not used here.

## 5. Winding bound and contradiction to isolated flatness

On circles avoiding zeros let k(r) be the winding of f. For nonexceptional radii r<R1<R, Stokes' theorem on the annulus with small holes around its finitely many zeros gives

    k(R1)-k(r)=sum_(r<|p|<R1) k_p.                            (14)

The form Im(df/f) is closed away from zeros and the holes have negative orientation. The global negative-index budget therefore gives

    k(r)<=k(R1)+M^2/pi=:K.                                   (15)

Positive indices, even infinitely many accumulating at zero, can only improve this inward upper bound.

The polar identity 2 exp(-i theta) partial_bar=partial_r+(i/r)partial_theta gives for almost every radius

    h'(r)-k(r)/r
      =mean_theta 2 Re[exp(-i theta)(partial_bar f)/f].         (16)

The minus sign follows because Re(i f_theta/f) is minus the angular derivative of the argument. Weak-L2 gives, for every measurable finite-area set E,

    integral_E b <= integral_0^infinity min(|E|,M^2/t^2)dt
                  =2M sqrt(|E|).                             (17)

Thus b is L1 on compact annuli. Integrating (16), with local absolute continuity of h and (15), yields

    h(R1)-h(r)<=K log(R1/r)+(1/pi)I_b(r,R1),
    I_b(r,R1)=integral_(r<|z|<R1) b(z)/|z| dA.                 (18)

Initially this holds at nonexceptional radii; continuity of h and absolute continuity of the fixed-annulus integral extend it to all positive r<R1.

On an annulus a<|z|<2a, (17) gives I_b<=2sqrt(3pi)M. Partitioning inward from R1 into dyadic annuli, with the final annulus possibly extending below r, gives

    I_b(r,R1)<=2sqrt(3pi)M ceil(log_2(R1/r)).                  (19)

Flatness at zero says that, for each fixed integer N, |f(z)|<=C_N|z|^N on a sufficiently small disc. Consequently h(r)<=log C_N+N log r. Substitution in (18), division by log(R1/r), and a lower limit as r tends to zero give

    liminf I_b(r,R1)/[pi log(R1/r)] >= N-K.                    (20)

N is arbitrary, contradicting the finite bound (19). Thus F has no isolated point. No endpoint continuation theorem or extra integrability hypothesis was imported.

## 6. Local uncountability and the sharp test

F is relatively closed as the intersection of the zero sets of all continuous derivatives of f. Inside any given neighborhood of a point of F choose a closed ball compactly contained in D with that point in its interior. Absence of isolated points supplies two distinct F points in its interior. Surround them by disjoint closed smaller balls inside the parent interior. Repeat, taking diameters at most 2^(-n) at generation n. Each binary sequence selects nested compact balls and a unique limit. The centers lie in F and their limits stay in the original compact subset of D, so relative closedness puts every limit in F. Disjointness makes limits of different sequences distinct. Hence every such neighborhood meets F in uncountably many points. In particular a countable F is empty.

For sharpness take f(z)=conjugate(z), b(z)=1/|z| on a disc centered at zero, with any value assigned at zero. Then partial_bar f=1 and the inequality is equality almost everywhere. The distribution formula gives M^2=pi. Here m=1, k=-1, A_p=1 and d_p=pi. Both (3) and the negative-index bound in (4) attain equality. The function is not flat at zero and supplies no counterexample to strong unique continuation.

## 7. Conditional carrier consequence for every rotation

Fix 0<c<1/2 and omega real. Set Jx=e3 cross x, A=cI-omega J, X(x)=Ax and L=(1-c)I+omega J. On an open subset U of R3 avoiding zero suppose V is smooth, W=curl V, and

    div V=0, X.V=0, (DV)X=-LV.

Let sigma:D_R->U be a smooth transverse section. Assume a nonnegative B in weak-L2(D_R) satisfies |(W.X)(sigma(y))|<=B(y)|V(sigma(y))| almost everywhere. No punctured L2 premise is required for this consequence.

Fix any y0 in D_R and replace the section by y -> sigma(y0+y) on a disc centered at zero whose closure stays in D_R-y0. Translation and restriction preserve weak-L2. The already checked pre-continuation div-curl reduction A2463-A2464 gives, in a smaller chart about this arbitrary point, smooth isothermal coordinates z=phi(y) and a smooth complex f satisfying

    |partial_bar f|<=[C1+C2 B(phi^(-1)(z))]|f|.

The finite constants depend on the fixed chart, c and omega. Bounded coordinate Jacobians preserve the weak-L2 bound; a constant on a bounded disc is weak-L2, and the union bound at half the threshold handles addition. The scalar f and V composed with sigma are related by smooth invertible linear maps between the section's two-dimensional carrier plane and C. Vanishing of all section jets is therefore equivalent.

The transport equation gives V(exp(tA)sigma(y))=exp(-tL)V(sigma(y)) for finite orbit segments. Every mixed derivative of the right side vanishes where all section jets vanish. The flowbox map is a smooth local diffeomorphism, so section flatness is equivalent to ambient flatness. The converse follows directly by the chain rule. Hence the set of section points where V is ambient-flat is relatively closed, has no isolated point, and is locally uncountable if nonempty. This is a statement about the flat set; V may vanish on an open set. It rules out an isolated flat orbit under this weak-L2 quotient bound.

No global flow completeness, pressure, boundary term or behavior at infinity is used. Constants and norms are not asserted uniform in omega. The scalar winding number is not automatically the index of an ambient vector field. No quantitative bound in the original B norm is transferred without tracking the chart constants.

## 8. Scope and verification

All eight submitted source sections and all twenty source manual checks were read. The source snapshot is 5ffa63bdcde07539bf8571d09a6cd8d34c28b6f17d571177e627b7a625bd4a87. The proof above independently checks the scaling, finite-order geometry, exact distribution charge, summation, circle means and sign of the inward bound. It assumes neither punctured L2 nor general weak-L2 continuation.

In the full common-flat system (F), prior C66 already supplies punctured local boundedness and A2832 already excludes a weak-L2 quotient at the distinguished flat orbit. This new result strengthens the bare-carrier analysis but adds no stronger conclusion for (F). It does not exclude a nonempty relatively perfect flat set, derive the quotient bound from the Euler equations, or prove the unrestricted rotating-profile conjecture. The existing configured model comparison is checked in Section 9; actual provider execution is independently unattested. No mathematical computation, new client, subagent or formal build was used.

## 9. Existing comparison and localization repair

The entire Theory Agent C  comparison dated 03:33Z was read, together with its two-line numerical log. Its analytic checks agree on scaling, the angular singularity contradiction, the exact charge constants, the finite negative-index budget, the orientation of the annular winding identity and the flat-set conclusion. The reported 1788 polynomial samples and approximate equality for conjugate(z) were not rerun. They are supplementary observations; Sections 2 to 6 supply the general argument and exact constants.

The comparison identifies one omitted localization sentence in source Section 7. The reduction is initially stated about the center of a section, while the conclusion concerns every section point. Section 7 above now explicitly translates and restricts the section about an arbitrary y0. The weak bound is preserved, the chart constants need only be local, and the scalar conclusion is local. Hence the no-isolated-point and locally-uncountable conclusions hold at every point. This fills the source exposition gap without an added mathematical hypothesis. The source should include the same sentence.

The existing comparison is from the agent configured as model; actual provider execution is not independently attested. All exchange used existing shared files, with no new client, subagent or remote computation. The general smooth weak-L2 continuation claim in the later LIT342 submission is separate and is not certified here.

## 10. Source confirmation and localization revision

Every changed line of revision 45dd11784b00701ef0acfe659cb8d4d5b3433673605ca3610f23bb2165034a5c and its confirmation manifest were read against the archived original source. The added sentence in Section 7 translates the section about every arbitrary y0, restricts to a disc contained in the original chart, and notes preservation of weak-L2. This is exactly the localization step justified in Sections 7 and 9 above. The remaining changes record A2859-A2861, retain the limits A2862 and separate the unconfirmed LIT342 submission. No original equation or hypothesis changes. The source now correctly labels only the confirmed zero-index and flat-set statements as proved. No computation was run.

## 11. Additional coordinator comparison

The complete coordinator comparison stamped03:37 and its nine-check final log were read after the designated verdict. Its eight mathematical items and W1-W3 agree with Sections 2 to 8 above: scale invariance, angular-zero exclusion, the signed index formula, asymptotic distribution charge, W11 circle means, the inward winding bound, the Cantor construction and localized carrier transfer. Its random checks on294polynomials do not replace any proof. The anti-holomorphic test correctly separates small thresholds, where the bounded disc truncates the level set. No new mathematical computation was run.

The opening phrase “before any verdict” is not supported by the displayed written03:37stamp, because A2859-A2862 are stamped03:35:27. The comparison may have begun earlier, but this review does not infer an unrecorded time. The mathematical agreement is confirmed independently of that minor chronology wording. The Theory Agent C 03:39entry also records its correction of the one-eighth grid description from “true minima” to “sampled minima”; the exact algebra checks are unaffected.
