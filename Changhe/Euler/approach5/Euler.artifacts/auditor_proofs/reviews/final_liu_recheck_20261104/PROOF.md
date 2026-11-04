# Final primary-manuscript recheck of the ordinary Liouville theorem

This is a repeated audit of the ordinary stationary theorem already confirmed in A010, A197, A2045-A2047, A2776 and A3059-A3061. Its exact statement and complete argument are reconstructed below. The rotating extension in Section 7 remains open. No new theorem is introduced after the mathematical freeze.

## 1. Exact statement, conventions and dependencies

Let d be 2 or 3, let 0<c<1/2, and let U:R^d->R^d and P:R^d->R be C^1. Suppose on all of R^d that

    (1-c)U+(cy+U).grad U+grad P=0, div U=0,
    lim_(R->infinity) sup_(|y|>=R) |U(y)|/|y|=0.

Then U=b is constant and P(y)=-(1-c)b.y+C. In particular U(y)->0 implies U=0 and constant pressure. No pressure normalization, integrability, derivative bound, outgoing assumption or convergence premise is imposed.

Set V=cy+U, A=DV with A_ij=partial_j V_i, a=1-2c>0, W=A^T-A and Q=P-c(1-c)|y|^2/2. Here W_ij=partial_i U_j-partial_j U_i represents the two-form d(U.dy). Write H=|V|^2/2+Q and Phi_s for the flow of V. Matrix norms below are Euclidean operator or Frobenius norms as indicated. The standard inputs are local C^1 ODE existence and differentiable dependence, the C^1 inverse function theorem, elementary linear algebra, distributional differentiation and Weyl's lemma with the harmonic interior gradient estimate. The argument below proves the null-basin fact directly, so no unspecified center-stable theorem is used.

The retained actual sixteen-page manuscript was reread through its complete 846-line extraction in bounded displays during this shift. The complete earlier auditor proof and the present argument were also reread. Source identity and precise scope are recorded in the team records. No numerical computation is required.

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

## 8. Five mandatory manuscript-audit answers

The source is the actual PDF from Zenodo record 23461703, retained at in the team records. Its MD5 is ec7a624e0971e0176e3d409239289ff4 and its SHA256 is 026536095d523419aea765f1c8d054879b71a4cdf6b1c070f8f3c6bb233319c8. The current check is a fresh reading of this retained manuscript, not a fresh download. The record metadata is retained separately. Its conflicting publication-date field is not used for a priority claim.

1. The advertised ordinary theorem is proved under the hypotheses in Section 1. Sections 2-7 give a complete independent argument. It yields a constant velocity, with the affine pressure specified there; decay or the stated normalization makes that constant zero.
2. No extra pressure behavior is needed. Only compact backward trajectory sets enter the Bernoulli argument. Uniform sublinearity supplies complete flow and bounded backward trajectories before they are used. Invariance, connectedness and equilibrium containment of the limit set are proved, not assumed. No generic convergence hypothesis is introduced.
3. The rank and null-basin arguments are valid at C1. The inverse-function cylinder uses connectedness without local connectedness, the path-length estimate proves convergence at a critical interval, and the countable cover consists of open neighborhoods rather than a countable equilibrium set. The terminal unstable integral is justified by bounded trapped trajectories. The vorticity transport uses a distributional exterior derivative after integrating a C1 one-form identity.
4. Theorem 7.3 is conditional for rotationally discretely self-similar solutions. It requires almost every backward orbit of the actual untwisted period map to have a periodic-point limit. Uniform sublinearity and relative periodicity are not asserted to imply this condition. For a continuously rotating stationary profile put Q_s=exp(omega s J) and u_s(y)=Q_s U(Q_s^-1 y). Its time derivative is omega J u_s-omega(Jy).grad u_s, so it satisfies the time-dependent rescaled Euler equation. The particle map is Q_s composed with Phi_s^B, and the actual untwisted map over L is exactly Phi_L^B. Thus the additional condition survives the rotating-frame change.
5. The transport and contracting-form parts do extend to every fixed finite omega under the stated dynamical condition. The monotone ordinary Bernoulli argument does not extend unconditionally, because of the unsigned extra term in Section 7. No inference from frozen-vorticity recurrence or zero entropy to the missing particle-flow classification is valid. Arbitrary-rotation nonexistence from decay alone remains open.

## 9. Later sections and scope of this new check

The manuscript was read through Section 10, the declaration and references. Theorem 7.5 is a small-period compactness result with a fixed growth modulus, fixed local spatial and pressure-gradient bounds, and a fixed positive vorticity normalization. It does not yield a uniform period bound over uncontrolled profiles. Sections 8 and 9 concern respectively the frozen-vorticity flow and conditional critical-exponent Bernoulli criteria. Their stated qualifications remain separate from the ordinary theorem proved here. In particular the complete flow used by the expanding-flow tail lemma is a premise, the aligned-curl proof supplies its vanishing local weak-L1 tail, and the critical profile application obtains backward confinement from sublinearity. No claim about the full critical profile problem follows.

Earlier dedicated audits of those results remain the relevant verdicts. Reading their full manuscript text again does not collectively recertify every statement, proof or reference in Sections 7-10. This new check confirms the ordinary C1 theorem and its exact rotating-scope limitation. It adds no source theorem to the frozen report.

## 10. Comparison and evidence discipline

The existing Theory Agent C  eight-item analytical comparison, recorded in Section 10 of in the team records, was read again. Its countable-cover, terminal-integral, pullback, Frobenius and first-exit checks agree with the argument above. That C comparison did not itself read the manuscript; the present full primary-text reading supplies the distinct source check. The literature agent independently reports a complete retained-manuscript reading at 12:04:35Z, and its five answers agree. These are existing-agent exchanges, not a new remote model call. The coordinator, A and C agents are configured as model; provider execution remains independently unattested.

Only actual file reads and retained source hashes are evidence. The excluded unreturned-browser metadata incident identified in the shift worklog is unrelated to the Liu manuscript and is not a premise of any result here. Writes are confined to this agent.
