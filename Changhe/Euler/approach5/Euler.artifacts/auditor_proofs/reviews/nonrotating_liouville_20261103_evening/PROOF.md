# Repeated audit of the ordinary stationary Liouville theorem

Status: CONFIRMED A2045-A2047 after a full seven-section final read. The extensions identified in Section 7 remain OPEN A2048. This is the unconditional nonrotating result of Liu Theorem 1.1, previously confirmed in A010 and A197. It is not a rotating Liouville theorem.

## 1. Exact statement, conventions and dependencies

Let d be 2 or 3, let 0<c<1/2, and let U:R^d->R^d and P:R^d->R be C^1. Suppose on all of R^d that

    (1-c)U+(cy+U).grad U+grad P=0, div U=0,
    lim_(R->infinity) sup_(|y|>=R) |U(y)|/|y|=0.

Then U=b is constant and P(y)=-(1-c)b.y+C. In particular U(y)->0 implies U=0 and constant pressure. No pressure normalization, integrability, derivative bound, outgoing assumption or convergence premise is imposed.

Set V=cy+U, A=DV with A_ij=partial_j V_i, a=1-2c>0, W=A^T-A and Q=P-c(1-c)|y|^2/2. Here W_ij=partial_i U_j-partial_j U_i represents the two-form d(U.dy). Write H=|V|^2/2+Q and Phi_s for the flow of V. Matrix norms below are Euclidean operator or Frobenius norms as indicated. The standard inputs are local C^1 ODE existence and differentiable dependence, the C^1 inverse function theorem, elementary linear algebra, distributional differentiation and Weyl's lemma with the harmonic interior gradient estimate. The argument below proves the null-basin fact directly, so no unspecified center-stable theorem is used.

The actual manuscript Sections 1-7.1, the complete earlier auditor reconstruction and the complete literature reconstruction were reread. Their snapshots and SHA256 values are in the team records. No computation is required.

## 2. Complete flow, Bernoulli monotonicity and the limit set

Expanding V in the equation gives (V.grad)V+aV+grad Q=0. Since (V.grad)V=A V and grad(|V|^2/2)=A^T V,

    grad H=-(aI-W)V,  V.grad H=-a|V|^2,
    |grad H|^2=a^2|V|^2+|WV|^2.                         (1)

Consequently a|V|<=|grad H|<=(a+||W||)|V|. All identities use first derivatives only.

Uniform sublinearity gives |V(y)|<=C(1+|y|), which by the scalar Gronwall inequality prevents finite-time escape in either time direction. Thus the C^1 flow is complete and each finite-time map is a C^1 diffeomorphism. For a sufficiently large fixed R, V(y).y>=c|y|^2/2 on |y|>=R. Reversed trajectories z(t)=Phi_-t(y), t>=0, remain in the ball of radius max(R,|y|). Z={V=0} is contained in the fixed ball.

The closures of the tails z([T,infinity)) are nested, nonempty, compact and connected. Their intersection K is nonempty, compact and connected. Completeness and continuity give Phi_s(K)=K for every real s: limits of z(t_n) are carried to limits of z(t_n-s), and the inverse map gives equality. By (1), H(z(t)) increases to a finite number h, since the trajectory closure is compact. H=h throughout K. Invariance and differentiation of H(Phi_s p), p in K, imply V(p)=0. Thus K subset Z; this also proves Z nonempty. Only pressure values on compact sets have been used.

## 3. Vorticity transport at exactly C^1 regularity

Let alpha=U.dy. In coordinates the Lie derivative is (L_V alpha)_i=V_j partial_j U_i+U_j partial_i V_j. Since partial_i V_j=c delta_ij+partial_i U_j, momentum gives

    L_V alpha+a alpha=d(|U|^2/2-P).

For every finite s, differentiating a pulled-back one-form along the flow and integrating gives

    exp(as) Phi_s^*alpha
       =alpha+d integral_0^s exp(at)(|U|^2/2-P)(Phi_t y) dt.  (2)

The scalar integral is C^1 in y by differentiating on a compact finite-time flow tube. Although the pulled-back one-form need not be C^1 in y, it is continuous and its exterior derivative exists as a distribution. Approximate Phi_s locally in C^1 by smooth maps. For each approximating map the pullback identity for the C^1 one-form alpha follows either by the coordinate calculation or by also approximating alpha in C^1. The one-forms converge uniformly and their pulled-back exterior derivatives converge uniformly. Passing to distributions therefore proves d(Phi_s^*alpha)=Phi_s^*(d alpha). Taking d in (2), and using that both resulting two-forms are continuous, gives the pointwise identity

    Y_s^T W(Phi_s y)Y_s=exp(-as)W(y),  Y_s=D Phi_s(y).       (3)

Since Y_s'=A(Phi_s y)Y_s with continuous coefficients, the formula W(Phi_s y)=exp(-as)Y_s^-T W(y)Y_s^-1 is C^1 in s. Differentiating it gives

    dW(Phi_s y)/ds=-A^T W-WA-aW.                           (4)

No spatial derivative of W was assumed.

## 4. Good equilibria force vanishing on their backward basins

Call an equilibrium p good if all eigenvalues of A(p) have nonnegative real part. At such a point (3) reads

    W(p)=exp(-at)exp(-t A(p)^T)W(p)exp(-t A(p)), t>=0.

The two matrix exponentials grow at most polynomially, by the Jordan form and the spectral assumption. Since a>0, W(p)=0. Therefore A(p)=A(p)^T is positive semidefinite.

Suppose K consists only of good equilibria. Compactness and continuity give sym A>=-aI/4 on a neighborhood O of K. The whole sufficiently negative trajectory lies in O. Otherwise a sequence outside O on the compact trajectory closure would have a limit in K. Taking Frobenius inner products in (4), and applying the least eigenvalue bound separately to rows and columns, yields

    (1/2)d|W|_F^2/ds
      =-a|W|_F^2-<W,A^T W+WA>_F
      <=-(a+2 lambda_min(sym A))|W|_F^2
      <=-(a/2)|W|_F^2.                                    (5)

For s<s0 on this tail, |W(Phi_s0 y)|_F^2<=exp(-a(s0-s))|W(Phi_s y)|_F^2. W is bounded on the compact trajectory closure. Letting s tend to negative infinity forces W(Phi_s0 y)=0, and invertibility in (3) gives W(y)=0. This applies both to a single good point and to a compact continuum of good equilibria.

## 5. Bad equilibria have a null set of converging backward initial points

At an equilibrium p with some eigenvalue of A(p) of negative real part, the reversed linearization L=-A(p) has a nonzero unstable generalized eigenspace E_u. Let E_cs be the complementary real generalized eigenspace. Choose numbers 0<epsilon<eta<beta and M<infinity such that for t>=0,

    ||exp(t L_cs)||<=M exp(epsilon t),
    ||exp(-t L_u)||<=M exp(-beta t).

This is possible by the strict positivity of the unstable real parts and the nonpositivity of the remaining real parts. Translate p to zero. On a sufficiently small convex open neighborhood the reversed field is Lx+r(x), with Lipschitz constant delta of r arbitrarily small because Dr(0)=0.

Let x(t),x'(t) be any two reversed trajectories that stay in this neighborhood for every t>=0, and put w=x-x' and D=sup_(t>=0) exp(-eta t)|w(t)|. D is finite because both trajectories are bounded. Variation of constants on E_cs gives the contribution M|w_cs(0)|+M delta D/(eta-epsilon). On E_u, boundedness justifies the terminal formula

    w_u(t)=-integral_t^infinity exp(L_u(t-s))
                       (r(x(s))-r(x'(s)))_u ds,

which contributes at most M delta D/(beta-eta) after multiplication by exp(-eta t). In a direct-sum norm, increasing M to absorb projections if needed,

    D<=M|w_cs(0)|+M delta[(eta-epsilon)^-1+(beta-eta)^-1]D.

Choose delta so the last coefficient is at most 1/2. Projection onto E_cs is injective on the trapped initial set and its inverse is Lipschitz, since |w(0)|<=2M|w_cs(0)|. Thus the trapped set is contained in a Lipschitz graph of dimension at most d-1. A coordinatewise Lipschitz extension gives a graph over all E_cs if its original domain is not closed. Such a graph is Lebesgue null by Fubini in these linear coordinates.

For every bad equilibrium choose one such open neighborhood. Their open union has a countable subcover O_j. A trajectory converging backward to any bad equilibrium eventually stays in one O_j, since that equilibrium belongs to O_j. At some integer backward time N its point is in the local trapped null set. Its original point therefore belongs to a countable union of images Phi_N of null graphs. Each Phi_N preserves null sets locally by its C^1 Lipschitz bound on compact sets, and globally by a countable compact covering. Hence this union is null. Neither the equilibrium set nor its spectra need be discrete, isolated or uniformly hyperbolic.

## 6. Connected nonpoint limit sets have rank at most d-2

Assume K is not a singleton. If rank DV(p)=d at p in K, the inverse function theorem isolates p in Z. Then {p} is a proper nonempty clopen subset of K, impossible.

If rank DV(p)=d-1, select d-1 components G of V with independent differentials and a complementary linear coordinate tau. A C^1 inverse-function chart y=chi(tau,xi) satisfies G(chi(tau,xi))=xi. Every zero in the chart lies on xi=0. Shrink its product domain so that some point of K lies outside its closure. If the axis had a point absent from K on each side of p, choose these two points as the caps of a thin closed cylinder compactly inside the chart. Its lateral boundary has xi!=0 and contains no zero. Its caps can meet K only at the excluded axis points. Its boundary therefore misses K, but K meets its interior and its exterior. The intersection of K with the cylinder is a nonempty proper clopen subset of K, again impossible. Thus an entire one-sided axis interval belongs to K.

Choose an interior point q of this interval and a smaller product box whose whole axis belongs to K. There H=h and V=0 on the axis. The selected components and bounded C^1 derivatives give

    |xi|<=|V(chi(tau,xi))|<=C0|xi|.

Integrate grad H along the transverse segment chi(tau,t xi), using (1) and the bounded derivative of chi, to obtain |H-h|<=C1|xi|^2. The lower bound |grad H|>=a|xi| now gives, in this box,

    |H-h|^(1/2)<=C|grad H|,  |grad H|<=M|V|.                (6)

These estimates use no Hessian or analyticity.

Let e(t)=h-H(z(t))>=0. If it vanishes at finite time, monotonicity and the limiting value make the future trajectory stationary. Otherwise, while z remains in the box,

    -d sqrt(e(t))/dt=a|V(z(t))|^2/(2 sqrt(e(t)))
                       >=a|V(z(t))|/(2CM).                (7)

Take a closed ball of radius rho centered at q inside the box. Since q is in the limit set, choose a sufficiently late visit with distance to q less than rho/4 and (2CM/a)sqrt(e) less than rho/4. Equation (7) bounds the path length before any first exit by rho/4, whereas exit would require at least 3rho/4. No exit is possible. The remaining path has finite length and converges. This contradicts the assumption that K has more than one point. Hence rank DV<=d-2 everywhere on every nonpoint K.

## 7. Low-dimensional conclusion and exact limits

For d=2 the rank restriction gives DV=0 on a nonpoint K, contradicting trace DV=2c>0. For d=3 it gives rank A=1 since trace A=3c>0. Writing A=u v^T shows A^2=(trace A)A, so its spectrum is {3c,0,0}. All points of K are good, and Section 4 gives W(y)=0. Every trajectory with a point limit at a good equilibrium has the same conclusion. Section 5 confines all remaining points to a null set. Thus W=0 almost everywhere and, by continuity, everywhere.

Since curl U=0 and div U=0 in distributions, each component U_i is distributionally harmonic. Weyl's lemma and the interior gradient estimate give for fixed x

    |grad U_i(x)|<=(C_d/R) sup_(B_R(x)) |U_i| -> 0

as R tends to infinity. The supremum is o(R): split the ball into a fixed compact region and its complement, where |U_i(y)|<=epsilon |y|, then let epsilon decrease. Thus U is constant. Substitution yields the stated affine pressure, and decay gives zero.

The proof does not assume the conclusion in the pressure or harmonic step. It does not extend to d>=4 by this rank argument: rank<=d-2 then permits negative eigenvalues despite positive trace. For the rotating equation with transport cy+U, put T=omega[J U-(J y).grad U]. The same H satisfies grad H=-(aI-W)V-T, hence V.grad H=-a|V|^2-V.T. The extra term has no sign supplied by the hypotheses. Using instead the rotating transport also changes the Bernoulli identity. Neither this theorem nor its null-basin lemma removes the missing rotating monotonicity. Arbitrary-omega bare-decay nonexistence remains open.

## 8. Repeated primary-source audit (2026-11-04T02:22:39.062212+00:00)

The actual sixteen-page manuscript, retained as in the team records at the agent root with SHA256 026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8, was read through the end of its extracted text in this shift. The independent Sections1-7 above, the earlier complete proof and the literature agent's complete reconstruction were reread. The coordinator's Theorem2 and its proof-dependency paragraphs were compared with these exact hypotheses. The theorem remains at omega=0, dimensions2 and3, global C1 velocity and pressure, uniform sublinearity and 0<c<1/2. No new pressure or integrability premise is needed.

The adversarial checks were repeated at the four potentially delicate steps. First, the C1 pullback argument differentiates the integrated one-form identity in distributions, then uses continuity to get an everywhere identity; it does not take spatial derivatives of continuous vorticity. Second, bounded reversed trajectories justify the terminal unstable formula in the null-graph proof. The countable cover is a cover by open neighborhoods, so convergence to any covered equilibrium ensures eventual trapping in one selected neighborhood, without making the set of equilibria countable. Third, the rank argument only needs a one-sided critical interval in a connected limit set. The quadratic transverse bound follows by integrating the gradient bound along C1 coordinate segments. The first-exit path estimate then supplies convergence instead of assuming it. Fourth, distributional harmonicity and the interior gradient estimate use uniform sublinearity to force constancy, with no pressure normalization at infinity. All four checks agree with the complete proofs above.

The manuscript's later time-dependent and relative-periodic sections remain separate. In the rotating problem the ordinary Bernoulli derivative has the additional unsigned term described in Section7. Passing to a time-dependent rotated frame does not eliminate the missing almost-everywhere backward-limit classification. The frozen-vorticity statements in Section8 concern another flow. Section9's critical-exponent statements are not premises of Theorem1.1. Reading those sections in this shift is not a new collective certification of their claims.

A2776 confirms this repeated audit of the full ordinary C1 proof. A2777 leaves an unconditional arbitrary-rotation extension from this argument open. This is continued file collaboration with the existing configured model coordinator and literature agent, not a fresh model call; actual provider execution is independently unattested.


## 9. Morning recheck of the stationary argument

A further reading of the actual manuscript's extracted lines 1-485, the full earlier auditor proof, the present Sections 1-8, and all nine current literature-reconstruction sections again finds no gap in the ordinary stationary theorem. This reading includes the complete C1 transport completion and the separate relative-periodic criterion. It is not a new reading of all sixteen manuscript pages. The new snapshots and exact reading scope are in the team records.

The distinction in Section 5 between a countable cover of open neighborhoods and a countable equilibrium set is essential and remains correct. Any convergent trajectory eventually stays in the chosen open neighborhood containing its limiting point, even if that neighborhood was originally centered at another bad equilibrium. The local trapped-set estimate is valid throughout that neighborhood, not merely for trajectories converging to its center. The terminal unstable integral uses boundedness of the full trajectory difference, and the exponentially decaying backward unstable semigroup removes the terminal term. A Lipschitz graph extension, rather than an assertion that every graph-domain subset is measurable, supplies a measurable null set containing the trapped set.

The rank argument likewise requires no local connectedness. A closed thin coordinate cylinder whose entire boundary misses K would separate the connected K into nonempty relatively open and closed parts. The absence of two missing axis endpoints therefore gives a one-sided interval of K. Its interior contains a full smaller axis interval on which H is constant. Integration along the transverse coordinate segment uses only C1 bounds and supplies the quadratic energy defect. The first-exit estimate is what turns that local information into convergence of the particular orbit. No general theorem that all gradient-like trajectories converge is invoked.

At C1 regularity, the one-form identity is integrated before taking an exterior derivative. Uniform convergence of the forms and their continuous pulled-back exterior derivatives under local C1 smoothing of the flow map justifies passage to distributions. Continuity then gives equality everywhere, and only the time derivative along a trajectory is subsequently taken. The argument therefore never assumes spatial differentiability of W.

The current report's Theorem 2 and its proof-dependency paragraph reproduce the correct omega=0, uniform-sublinearity and C1 hypotheses. Its rotation-axisymmetric velocity corollary correctly cancels the rotation terms before applying this theorem. The new pressure-axisymmetry theorem has a distinct C2 proof and should not be silently absorbed into that C1 corollary. The unsigned rotational Bernoulli term in Section 7 remains the obstruction to applying the stationary proof to arbitrary omega. Existing coordinator comparison of this recheck is requested; no new verdict is recorded merely from this draft.


## 10. Existing-agent comparison and precise current scope

The complete C07:18:52 comparison was read, including all eight analytical items and its diagnostic description. It independently checks the countable open-neighborhood cover, bounded terminal unstable integral, C1 distributional pullback, Frobenius estimate and coordinate-cylinder first-exit proof. These agree with Sections1-9. Its explicit affine control for the rotating defect is also correct: for U=(s x1,-s x2,0), the extra term is -V.T=-4c omega s x1 x2. It changes sign when c omega s is nonzero. No absent spatial derivative of vorticity or unproved convergence of arbitrary gradient-like flows has been introduced.

The comparison did not reread the actual manuscript or our verification files, so it is an analytical comparison of this reconstruction with the named report theorem, not a second primary-source reading. Its eleven described diagnostic checks, twenty-thousand random matrix samples and first failed diagnostic run are not read or certified by this audit. The finite sample is unnecessary for the exact Frobenius calculation in Section4. The report's D4-D6 byte-identity assertion is not independently recertified by this comparison.

The separate pressure-axisymmetry theorem has since been confirmed at C1 in A3047 by a different proof. This updates the contemporaneous C2 description at the end of Section9; it does not turn that pressure theorem into the velocity-axisymmetry corollary of the stationary theorem. The ordinary stationary theorem retains exactly the hypotheses of Section1, in dimensions2 and3, and its rotating velocity-axisymmetry corollary cancels the rotational term before applying it. The unrestricted rotating extension remains open. Existing configured model file collaboration was used; actual provider execution is independently unattested.
