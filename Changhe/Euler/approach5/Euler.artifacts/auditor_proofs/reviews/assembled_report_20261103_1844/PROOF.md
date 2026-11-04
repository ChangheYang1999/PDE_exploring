# Audit of the Note105 report revision

Status: independent audit of the pinned Note105 assembly, with repairs listed below. This is a delta audit, not approval of every unchanged statement in the report. The manifest records the exact four-file pin and independently generated differences against Note103.

## 1. Object, scope and labels

The pinned report has 6462 lines and SHA256 499f03d00c9ce26f03bf57627fb0202d64d93cd16f61b40543c0908d7173d928. Euler.report was byte-identical at capture. All 601 lines of the independent report difference and all 50 lines of the README difference were read, including the long table rows separately. THEOREM_ATTEMPTS and PROOF_OBSTRUCTIONS are unchanged from the previously checked Note103 versions. The complete current README, Theorem7(g), the new part of Theorem8(a), the label rationale and Note105 were read. The rest of Section2D is being checked separately.

The convention now distinguishes a CONFIRMED proof from its profile assumptions. Theorems5, L and L-infinity and Corollary5.3 retain the helicity-sign premise and are CONDITIONAL. Theorem6 and Remarks6.1 and7.1 retain zero helicity. The integral corollaries of Theorem1 retain their integral assumptions, and Corollary2.1 retains axisymmetry. Theorem3(i) states its annular vorticity assumption. Theorems1-4 and Corollaries5.1-5.2 retain the label of their stated base class. In particular row7 is UNRESOLVED and states an equivalence, not exclusion of a sign-changing basin. These label changes are correct.

The normalization in Theorem1 is correct. With A=cI-omega J, M=(1-c)I+omega J, z0=-A^(-1)b and U_b(y)=U(y+z0)-b, one has Ay+U_b=A(y+z0)+U(y+z0), while the new pressure gradient is grad P(y+z0)+Mb. Thus the constant terms cancel in momentum. The energy assertions concern U_b. At omega=0 the corrected H_0 equals H-c(1-2c)|y|^2/2 and satisfies (cy+U).grad H_0=-(1-2c)|cy+U|^2. Neither identity discards an omega term.

## 2. The strengthened removal theorem and the remaining comparison ambiguity

Here is the precise confirmed input, A2020-A2026. On D=R3 minus{0}, fix 2/5<c<1/2, any finite omega, A=cI-omega J, X=Ax, a=1-2c and b=2(1-c). Suppose V is locally C^(1,alpha), 2/c-4<alpha<1, P is continuous, S=P-|V|^2/2, W=curl V, k=X.V, and

    div V=0, DV X=-((1-c)I+omega J)V,
    Delta P=-tr((DV)^2), X.grad S=-bS, W.grad S=0.

Assume |V|^2<=r_+|S| on the whole unit sphere, together with either k=0 everywhere or grad k cross grad S=0 on {S!=0}. If r_-|S|<=|V|^2 on a neighborhood of the entire common zero set, for some r_->0, then V=S=P=0. The neighborhood can be specified on the sphere and saturated by X. The two ratio inequalities have the same scaling.

The local Poisson estimate gives P in C^(2,alpha), and |P|<=(1+r_+/2)|S|. The negative exponent rho-1, rho=c/(2(1-c)), makes the pressure term in the regularized derivative bounded by a constant times |P|^(rho-1)|DP|. Together with the component root estimates, this gives beta=|S|^(-eta)V, eta=a/b, in W_loc^(1,t) for 1<=t<1/(1-rho), continuous and zero on {S=0}. Curl is removed across those zeros only after classical curl beta=0 off them has been established from the displayed structural hypotheses.

The global potential has zero additive drift: a nonzero drift would force V,S nowhere zero and produce a compact regular level of one strict flux sign, contradicting div V=0 and the zero spherical flux from homogeneity. For zero drift the potential is invariant under X. Its weighted m-Laplace equation, m=1/c>2, has coefficient R^(-tau), R=|V|^2/|S| and tau=(m-2)/2. Harnack with a positive lower bound on this coefficient and local integrability excludes any nonconstant extremum. Therefore every boundary point of either extremal set has an infinite local integral of R^(-tau). The assumed lower comparison near the whole common zero set contradicts this. Poisson and harmonic homogeneity then remove P. The actual-profile transfer uses the full natural U and DU bounds and the faithful-tail argument A1877. This proves that both cases(i) and(ii) of Theorem7(g) may use the localized lower comparison. In case(i), scalar transport must still be separately stated when helicity is dropped.

The report's new strengthening paragraph and the lower-bound qualification of cases(i)-(ii) preserve these premises and are correct. The bounded-weight outline just above it applies to the original two-sided case. It should be identified as that outline so its global upper bound on the coefficient is not accidentally read as applying before the localized argument.

A remaining ambiguity occurs immediately afterwards: the paragraph beginning "Without the rank relation the comparison class" assumes "the tail comparison of (g)". The confirmed LIT271 sector argument A1904-A1908 used the original global two-sided comparison, whereas(g) now also includes a weaker lower comparison. Replace this reference by explicit two-sided bounds on the whole sphere. Do the same in summary row10 before the sector alternative. Sections7 and10 now correctly name the global two-sided comparison, and the final README recap now correctly includes W.grad S=0 in its k=0 branch. The earlier README paragraph states the original two-sided bounds explicitly before invoking the sector theorem and is unambiguous.

## 3. The strain criteria and their family

The full profile class is U in C2, P in C1 on R3, div U=0, (Ay+U).grad U+MU+grad P=0 with A,M from Section1, and Hb (bounded U and U(R.) tending to0 in distributions on R3), 0<c<2/3, all omega. Write G=DU, S=(G+G^T)/2, W=curl U, t=|W|^2 and kappa0=1-3c/2. The density of A2004-A2009 is

    D[a,b,g]=a|S|^2+b tr(S^3)+(3b/4-2g'(t))W.SW
              +2g'(t)t-3c g(t)-a t/2.

For g=t, b=8/3 and a=2kappa0+2l/3, the trace-free cubic inequality gives D>=(2/3)(3kappa0-l)|G|^2 when -lambda_min(S)<=l<3kappa0. Trace zero bounds S. The compact kinematic identity then gives Y(R)=int_(B_R)|G|^2<=CR^3 even if W is unbounded. The compact master identity gives kappa Y(R)<=CR^(beta-2)+C Y(2R)/R, beta=max(5-2/c,0)<2. Successive substitutions yield bounds by R^2, R,1 and finally a quantity tending to0, so G=0 and Hb gives U=0. Thus Theorem8(a) correctly removes W boundedness from both strain forms. The displayed cutoff outline has the correct order of dependence and assumes no derivative decay.

For the algebraic family with constant a,b and scalar g in C1, g>=0, g(0)=0, tested for every W and every matrix in the chosen trace-free strain set, the strict-bound suprema are

    max(3kappa0,1/2),
    max((3sqrt(6)/2)kappa0,sqrt(3/2)),
    max((3/2)kappa0,1)

for -lambda_min, the Frobenius norm and lambda_max respectively. The second alternatives can also be obtained on the core ball by the separate characteristic theorem. This is an algebraic limitation of the stated global family, not a proof of optimality of all methods or a theorem about weights varying in space. The report's conclusion should spell out g>=0, g(0)=0 and the domain of the universal test; these restrictions are essential to the classified family.

The precise mixed theorem SF.3 additionally assumes S(y) lies in one compact set K, |W|<=M, a>0, b real, g in C1([0,M^2]), g>=0 and g(0)=0. Its strict positivity is required on all K times {|W|<=M}, apart from(0,0), and g'(0)>a/(4kappa0). Near0 the density is a|S|^2+(2kappa0 g'(0)-a/2)t+o(|S|^2+t); compactness elsewhere then gives uniform coercivity. This is exactly what allows the same finite cutoff iteration.

The short SF.3 sentence in Theorem8(a) and the C62 ledger row omit the compact strain set, a>0 and the weight normalization and regularity. These should be restored, with the density definition or an exact source reference. Do not read pointwise strict positivity only on attained field values as a replacement for positivity on the compact product set. The numerical-instance caveat in this pin is historically correct; C63 is a new pending submission, not part of this pin.

## 4. A misplaced C58 conclusion

Let Y={W!=0} intersect int{k=0} in the local smooth tail system of C58, and assume the actual-profile sign law at supported common zeros V=W=0. A2013 proves that Y intersect {S<0} is both open and closed in {S<0}. Each connected component C of {S<0} is therefore either contained in Y or disjoint from Y.

If C is contained in Y, k=0 and V,W are nonzero. If C is disjoint from Y, k!=0 on C intersect int(supp W), and on each connected component C' of that intersection, k|S|^(-1/q) is a nonzero constant K. Consequently S=-|K|^(-q)|k|^q on C'. The power formula belongs to the second case, not the first.

The new C58 row instead says "Y intersect {S<0} is open and closed in {S<0} and S=D abs(k)^q there with D<0". Its placement of the power formula is a false attribution to A2013: on the stated set k=0 while S<0. Restore the two alternatives and put the formula on the components C' just specified. This correction does not refute C58 or the confirmed profile sign law, and does not prove the negative part of Y empty.

## 5. Exact premises in the two new ledger rows

The upper-only-removal row should put the full common structural setting of Section2 before its conclusions. As written it calls beta curl-free after just the Poisson and upper-comparison hypotheses; the later clause names homogeneity and transport but never explicitly states div V=0 or X.grad S=-bS. Local removal preserves existing zero curl; it does not create it.

An elementary countertest separates these assertions. Take V=(1,sin x1,0) and P=2 on R3. Then div V=0, tr((DV)^2)=0, Delta P=0 and S=2-(1+sin^2 x1)/2 lies in[1,3/2]. The global upper comparison |V|^2<=2S holds. Nevertheless at x1=0,

    curl(|S|^(-eta)V)=(3/2)^(-eta)e3 !=0.

This example satisfies the preliminary local removal hypotheses for every allowed c and alpha; it deliberately has no twisted homogeneity or scalar transport and is not an Euler profile. Thus a claim of automatic zero curl from those preliminary hypotheses is false, whereas A2021's removal theorem and A2022's structural application stand. State 1<=t<1/(1-rho), not just t<1/(1-rho), for the Sobolev range.

The LIT282 main paragraph and row should explicitly impose X.grad f=-af and X.grad Q=-bQ on their analytic harmonic germs, with X=(cI-omega J)x and the axial point e3. Their finite-jet obstruction repeatedly uses those two homogeneities to fix the normal derivatives and scalar matching recurrence. The words "analytic harmonic f,Q" and "axial anisotropic class" alone do not state them. This audit neither proves nor disproves an unweighted harmonic variant. LIT283 has subsequently been confirmed A2055-A2060 and may be incorporated separately; its extra isotropic conclusion does not resolve general matching.

## 6. W2 endpoint, verification and remaining report work

Remark6.1 correctly retains the helicity-free profile, natural bounds, C1_loc tail convergence and escaping lower-window W2 hypotheses. Its C^(2,1) tail premise suffices, by A2038, at every rate. The reduced-symbol indefiniteness is confined to the displayed reduction, as A2036 requires. It does not assert that no other elliptic or regularity argument exists. The scalar Poisson estimate supplies the needed pressure regularity without an endpoint C^(3,1) claim. No new inference of an infinitely flat T0 point is made. This transfer is confirmed.

The remaining tasks for assembly approval are the precise repairs in Sections2-5, a check of the resulting stable delta, and completion of a coverage ledger for the unchanged current report sections. This audit has not reread all 6462 lines or every external input; it cannot certify the entire report merely because this delta is largely correct. The mathematical proofs already CONFIRMED retain their existing verdicts. No computation, model client, server, formal build or external write was used. Collaboration is through the existing configured model coordinator's revision and rationale and the theory owners' files; provider runtime is independently unattested.
