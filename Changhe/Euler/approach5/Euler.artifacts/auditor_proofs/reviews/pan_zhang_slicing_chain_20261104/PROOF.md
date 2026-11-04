# The Pan-Zhang slicing chain and the published sequel

Status: independently reconstructed; existing configured model comparison received and assessed in Section 10. This is a source audit, not an Euler nonexistence theorem. First saved 2026-11-04T05:17:52.830259+00:00; exact postreading time is recorded separately. The initial heading rounded this to 05:18Z before that minute began; it is corrected here to the actual first-save filesystem time.

## 1. Sources and statement being audited

The submitted literature-agent proof is retained as in the team records, SHA256 `9860ff4938afb88c43240b761b7ddd11e852d81181733871d78cdfaf163412fb`. Its eight sections and 49 manual checks have been read. Its source is the twelve-page author manuscript in the team records, SHA256 `6889cfa47af191d69ae4b4b9c343c37566936c809a0849cdc2ad1249e0ab0a6f`.

This audit also obtained the actual published sequel, Yifei Pan and Yuan Zhang, *A remark on unique continuation of partial_bar*, Nagoya Mathematical Journal 261 (2026), e55, 1-12, DOI `10.1017/nmj.2026.10126`. The retained in the team records has SHA256 `f9a18d2aade0a78104c044706908a0bb3fd4f3f997e9145cba82b2c585513f45`. Retrieval returned HTTP 200, application/pdf, 284812 bytes. The source URLs, real retrieval times and hashes are in the adjacent retrieval JSON files. The journal page gives online publication on 21 October 2026; its separate citation publication field says January 2026. These are distinct metadata fields. The PDF states received 17 January, revised 16 June and accepted 6 August 2026. The earlier 2025 Comm. Anal. Geom. article is a different source; its publisher PDF has not been audited here.

Both twelve-page texts, including the bibliographies, have been read in full. Published pages 3, 4, 6, 7, 9, 10 and 11 were additionally rendered and visually inspected. The publication adds an introductory comparison for source dimension one and changes references and typesetting. No byte identity, full textual identity or identity of every peripheral claim with the author manuscript is asserted. The statements and proof chain considered below persist in the publication.

Let O be a connected open subset of C^n, d=2n, and N a positive finite integer. Write dV for unnormalized d-dimensional Lebesgue measure, dA for planar Lebesgue measure and dS for ordinary surface measure. The norm of partial_bar u is the Euclidean norm over its nN complex components, with partial_bar_j=(partial_xj+i partial_yj)/2. Lq integral flatness at zero means

    lim_(r->0) r^(-m) integral_(B_r) |u|^q dV = 0

for every positive integer m. The author and published main statements are:

1. If u is W1,1_loc, |partial_bar u|<=V|u|, V is Ls_loc for some s>d, and u is L1 integral flat at an interior point, then u=0.
2. If N=1, u is W1,p_loc for some p>d, V is Ld_loc, and the same inequality and flatness hold, then u=0.
3. If n=2, N is finite, u is W1,p_loc for some p>4 and V is L4_loc, the same conclusion holds.
4. If zero belongs to O, u is W1,1_loc, |partial_bar u|<=C|u|/|z| and u is L1 integral flat at zero, then u=0 for every finite C>=0 when N=1, and for 0<=C<1/4 when N>=2.

The next sections prove the analytic reductions and their transfer to these statements. Section 6 names the external continuation premises. Their complete underlying proofs are not newly certified here.

## 2. Polar slicing and the critical loss

For every nonnegative measurable h, and then every integrable h,

    integral_(B_R) h dV
      = (1/(2pi)) integral_(S^(d-1)) integral_(D_R)
          |w|^(d-2) h(w zeta) dA(w) dS(zeta).             (1)

Indeed write w=r exp(i theta). Multiplication of zeta by exp(i theta) preserves surface measure. The theta integral therefore contributes 2pi, and the remaining radial power is r^(d-1), the ordinary polar formula. Tonelli justifies this proof for nonnegative h; decomposition into positive and negative real and imaginary parts gives the integrable case.

If h is Lp(B_R), p>n, then for almost every zeta its weighted Lp slice integral is finite. For 1<=q<p/n, Holder gives

    integral_(D_R)|h(w zeta)|^q dA
      <= (integral_(D_R)|w|^(d-2)|h(w zeta)|^p dA)^(q/p)
         (integral_(D_R)|w|^(-(d-2)q/(p-q)) dA)^((p-q)/p).

The second integral is finite because (d-2)q/(p-q)<2. For n=1 the same conclusion holds, although q=p is also possible and not claimed. A countable cofinal sequence of q, followed by finite-measure inclusions, puts all the asserted exponents on one full-measure set of directions. In particular p>d yields L2 slices.

This conclusion cannot be obtained by setting p=d. For n>=2 and 1/2<epsilon<(d-1)/d, put h(z)=|z|^(-1)(log(1/|z|))^(epsilon-1) near zero. Its ambient Ld integral is a constant times

    integral^infinity t^(d(epsilon-1)) dt < infinity.

The L2 integral of every radial complex slice is a constant times integral^infinity t^(2(epsilon-1)) dt, which diverges. Every ambient power p>d also diverges, because its transformed integrand includes exp((p-d)t). This independently verifies Example 3 and identifies the exact obstruction to unweighted L2 slicing.

## 3. The distributional chain rule

Suppose u is W1,p(B_R;C^N), p>d. Then for almost every unit zeta, v(w)=u(w zeta) belongs to W1,2(D_R;C^N) and

    partial_bar_w v(w)
       = sum_(j=1)^n conjugate(zeta_j) partial_bar_j u(w zeta). (2)

In real coordinates the complete formula is Dv=Du L_zeta, where the real linear isometry L_zeta maps w to w zeta. This removes the ambiguity of the source's abbreviated gradient dot product.

Take smooth u_k converging to u in W1,p on the ball. The Sobolev-Morrey embedding gives uniform convergence, so the corresponding slices converge uniformly for every zeta. Set

    g_k(zeta)=integral_(D_R)|w|^(d-2)|Du_k(w zeta)-Du(w zeta)|^p dA.

Equation (1) gives integral_S g_k=2pi ||Du_k-Du||_p^p ->0. Choose a subsequence whose displayed integrals are summable. Tonelli gives g_k->0 for almost every zeta along that subsequence. Holder with the integrable weight |w|^(-(d-2)/(p-1)) then gives unweighted L1 convergence of the restricted derivatives. Thus the smooth real chain rule passes to distributions. Writing the Wirtinger derivative of w zeta yields (2). Section 2 applied to both u and Du with q=2 proves the claimed W1,2 regularity.

Finite intersections handle all components. An ambient null exceptional set for the differential inequality has, by (1), a planar null intersection with almost every radial complex line: its polar weight is positive away from w=0. Consequently all derivative and inequality assertions hold on a common full-measure set of directions. Cauchy-Schwarz in the j index gives

    |partial_bar_w v(w)| <= |partial_bar u(w zeta)|.        (3)

There is no dimension-dependent loss in the coefficient. For local Sobolev assumptions choose a ball whose closure is contained in O before making these arguments.

## 4. Integral flatness and pointwise flatness

For u in W1,p(B_R;C^N), p>d, L1 integral flatness at zero is equivalent to: for every positive integer m there are C_m and r_m>0 such that |u(z)|<=C_m |z|^m for |z|<r_m. The representative is the continuous Sobolev representative. The constants do not depend on direction.

First take a complex scalar. Boundedness and L1 flatness imply u(0)=0 and flatness of every finite power >=1. Choose d<q<p and put f=u^2. The product rule gives Df=2u Du. For any prescribed integer m, choose the original flatness order large enough that

    integral_(B_t)|u|^(qp/(p-q)) = O(t^(2pqm/(p-q))).

Holder and the fixed Lp bound of Du give integral_(B_t)|Df|^q=O(t^(2qm)). The scale-correct Morrey oscillation inequality and f(0)=0 imply

    sup_(B_(t/2))|f| <= C t^(1-d/q) ||Df||_(Lq(B_t)).     (4)

Since 1-d/q>0, take t=2|z| sufficiently small and discard this extra positive power to obtain |u(z)|^2=O(|z|^(2m)). The identity |u^2|=|u|^2 is valid for a complex scalar. For finite vectors apply this argument separately to every component; no square of a vector is defined or needed.

Conversely the pointwise estimate of order m gives integral_(B_t)|u|^q<=C t^(mq+d) for every fixed finite q>=1. Since m is arbitrary, all those integral flatness conditions follow. Restricting to w zeta preserves |w zeta|=|w| and the same constants. Every continuous slice is therefore L2 integral flat, and almost every slice also has the regularity from Section 3. This step does not intersect uncountably many exceptional sets.

## 5. The inverse-radius bootstrap in every dimension

Assume u is W1,1_loc(O;C^N), L1 integral flat at zero, and satisfies |partial_bar u|<=C|u|/|z| with finite C>=0. Then u is W1,q_loc(O) for every finite q>1. No initial merely distributional L1 formulation in higher dimension is asserted here.

For each fixed M>0, L1 flatness implies |u|/|z|^M is locally integrable and L1 integral flat at zero. To see this, fix m>=1 and epsilon>0. For sufficiently small s, integral_(B_s)|u|<=epsilon s^(m+M). Splitting B_t into annuli with outer radii t/2^(j-1) gives

    integral_(B_t)|u|/|z|^M
      <= epsilon 2^M t^m sum_(j>=1)2^(-m(j-1))
      <= epsilon 2^(M+1)t^m.                              (5)

For u in Lp near zero, p>1, choose 1<q<p and eta=(p-q)/(p-1). Since q=eta+p(1-eta), Holder and (5) imply

    integral (|u|/|z|)^q
       <= (integral |u|/|z|^(q/eta))^eta
          (integral |u|^p)^(1-eta) < infinity.             (6)

Use the local elliptic estimate for partial_bar: u and its distributional partial_bar derivative in Lq, 1<q<infinity, imply u in W1,q on smaller balls. This is the constant-coefficient elliptic estimate; the identity Delta u=4 sum_j partial_j partial_bar_j u reduces it to the usual local singular-integral estimate. Sobolev and Morrey embeddings and this elliptic estimate are explicitly used analytic premises.

Here the bootstrap has finitely many steps. Initially Sobolev gives p=d/(d-1). While 1/p>=1/d, choose 1/q=1/p+1/(2d). Then 1<q<p and q<d. Equation (6), the inequality and elliptic regularity give W1,q on a smaller ball; Sobolev replaces 1/p by 1/p-1/(2d). After 2d-3 steps p=2d. Now choose d<q<2d and use (6), elliptic regularity and Morrey to obtain boundedness. Only finitely many ball shrinkages were required.

For bounded u, (5) gives, for every finite q>1,

    integral (|u|/|z|)^q
       <= ||u||_infinity^(q-1) integral |u|/|z|^q < infinity.

Thus elliptic regularity gives every claimed exponent near zero. Away from zero the coefficient is locally bounded and the ordinary finite bootstrap gives the same conclusion. Boundedness also transfers L1 flatness to L2 flatness. This proves the content of Lemma 4.4, including the iteration suppressed in the source.

## 6. External inputs and the transfer to the four statements

The source explicitly states the following continuation inputs on connected domains. Each unknown is finite-vector valued unless scalar is specified, belongs to H1_loc and has the indicated differential inequality almost everywhere.

- Theorem 2.1(1): an L2_loc coefficient gives weak continuation from a nonempty open zero set in any C^n.
- Theorem 2.1(2): in C, an L2_loc coefficient and L2 integral flatness give strong continuation.
- Theorem 2.2: a scalar in any C^n, L2 integral flat at zero, has strong continuation under C/|z| for every finite positive C.
- Theorem 2.3: in C, the same statement holds for finite vectors when C<1/4. The campaign separately proves this implication in LIT348, positive verdict A2923.
- Theorem 2.4: in C, a scalar has strong continuation under |z|^(-(beta-1)/beta)W, W in L^(2beta)_loc, beta>1, with L2 integral flatness.
- Theorem 2.5: in C, finite vectors have the preceding conclusion for beta=2 and W in L4_loc.

These exact formulations are checked against published pages 3-4. This audit does not replace them by stronger claims or certify every proof in the earlier sources.

For statement 1, write s>d for the coefficient exponent. If u is Lp, Holder places partial_bar u in Lq with 1/q=1/p+1/s. Initially p=d/(d-1), hence q>1. While q<d, elliptic regularity and Sobolev lower 1/p by the fixed positive amount 1/d-1/s. Eventually q>=d. At equality, critical Sobolev gives every finite Lp exponent, so the next q can exceed d. Thus u is locally bounded and then W1,s_loc. Sections 2-4 now provide H1, L2-flat slices with L2 coefficients. Theorem 2.1(2) makes almost every slice zero, and (1) gives zero on a ball. The improved H1 regularity and V in L2_loc allow Theorem 2.1(1) to propagate this zero through O.

For statements 2 and 3, the given p>d supplies Sections 3-4 directly. Set W_zeta(w)=|w|^((n-1)/n)V(w zeta). Its 2n-th power has exactly the polar weight |w|^(2n-2), so (1) gives W_zeta in L^(2n) for almost every direction. Equation (3) becomes

    |partial_bar v| <= |w|^(-(n-1)/n)W_zeta |v|.           (7)

When N=1 and n>=2, use Theorem 2.4 with beta=n. When n=1, beta=1 is not admissible there; instead use Theorem 2.1(2) directly, since W_zeta is L2. When n=2 and N is finite, use Theorem 2.5. In each case u vanishes on a ball by (1); ambient weak continuation applies because u is H1_loc and V is Ld_loc, hence L2_loc. This does not resolve the case n>=3 and N>=2 with only an Ld coefficient.

For statement 4, Section 5 supplies all finite Sobolev exponents and L2 flatness. The scalar case follows from Theorem 2.2. For vectors, Sections 3-4 and |w zeta|=|w| give an H1, L2-flat slice with exactly C/|w|. Theorem 2.3 applies for C<1/4, so u vanishes on a ball. Before final weak propagation, replace the coefficient by zero on a smaller known zero ball and leave it C/|z| outside. This is now locally bounded everywhere and the same inequality holds. Theorem 2.1(1) applies. No false assertion that 1/|z| is planar L2 at zero is used. The source's strict vector constant is retained.

## 7. Literal repairs and a new peripheral overstatement

Both inspected versions print j->0 twice in the approximation argument on page 6; the sequence limit is j->infinity. The chain rule is given precisely in Section 3. In the author page 7 estimate, replacing 2^q by 2^p is harmless since p>q; the published page uses 2^q. The omitted positive power of t at the end of the Morrey estimate is harmless for sufficiently small t. The final paragraph calls the sliced function f after using f=u^2 earlier; the intended sliced function is v, as Section 4 makes explicit.

The combined proof of statements 2-3 on published page 9 still invokes Theorem 2.4 for N=1 without separating n=1. Theorem 2.4 requires beta>1. Theorem 2.1(2), together with Section 4, repairs that endpoint. The publication's added introduction on page 2 already compares the n=1 case with Theorem 2.1, but the proof citation itself remains overbroad.

Published page 10 still orders the complex number u_k(z) in Example 5. Its correct lower bound is on |u_k(z)|, proved in Section 8. Neither this notation repair nor the n=1 citation repair refutes a main theorem.

Published page 4 additionally asserts that none of the hybrid potentials |z|^(-(beta-1)/beta)W with W in L^(2beta)_loc belong to L2_loc. Read as a universal statement this is false. For example W=1 on a bounded planar disc is in every finite Lp and the square of the hybrid coefficient has radial integral

    2pi integral_0^R r^(-1+2/beta) dr < infinity

for every finite beta>1. The correct assertion is that membership in the hybrid class does not force L2 membership. For an example of the failure, choose W=r^(-1/beta)t^(-a) near zero, where t=log(1/r) and 1/(2beta)<a<=1/2. Then W is L^(2beta), while the hybrid coefficient is r^(-1)t^(-a), not L2. This peripheral sentence has no role in the continuation proofs.

The submitted literature-agent Section 6 cites A2922 for the positive LIT348 implication. The correct positive verdict is A2923; A2922 concerns its negative construction. This is a verdict pointer correction, not a mathematical failure.

## 8. Example 5 with weak derivatives and finite order

Let n>=2, d=2n, 1/2<epsilon<(d-1)/d and k>=1. For 0<r=|z|<1/2 and t=log(1/r), set u_k(z)=exp(-t^epsilon)z_1^k and u_k(0)=0. Direct differentiation off zero gives

    |partial_bar u_k| = [epsilon t^(epsilon-1)/(2r)] |u_k|.

The coefficient is Ld but in no Lp with p>d, and every radial complex restriction fails L2, by Section 2. For t>=1, exp(-t^epsilon)>=exp(-t), so

    |u_k(z)| >= r |z_1|^k.

Integrate on the annulus rho/2<r<rho and the angular set |z_1|>=r/2, which has positive surface measure. For each finite q>=1 this gives integral_(B_rho)|u_k|^q>=c rho^(d+q(k+1)), with c>0 independent of sufficiently small rho. Thus u_k is not infinitely integral flat.

Off zero,

    |Du_k| <= C exp(-t^epsilon)r^(k-1)(k+epsilon t^(epsilon-1)),

which is bounded near zero. To identify this as the weak derivative across zero, use a cutoff supported in an annulus of radius rho. The additional term is bounded by C rho^(d+k-1)exp(-(log(1/rho))^epsilon), which tends to zero. Therefore u_k is locally W1,infinity, and its stated equation holds weakly and almost everywhere.

It is not C^(k+1) near zero. Along the positive real z_1 axis, u_k(x)=o(x^k), but u_k(x)/x^(k+1)=exp(t-t^epsilon)->infinity. If this restriction were C^(k+1), Taylor's formula and the first relation would annihilate all coefficients through degree k; the ratio in the second relation would then be finite. This contradiction supplies a valid nonsmoothness proof; one cannot merely infer it from nonsmoothness before multiplication by z_1^k.

## 9. Scope and original comparison request

Sections 2-5 are complete independent proofs of the slicing, chain-rule, flatness and bootstrap reductions. Section 6 proves the four source conclusions conditional on its explicitly named external continuation inputs. The strict planar inverse-radius input also has an independently confirmed campaign proof. Section 7 separates literal and citation repairs from the newly refuted peripheral nonmembership sentence. No main theorem of the sequel is refuted by this audit.

No finite-regularity scalar continuation theorem for arbitrary weak-L2 norm, no coefficient bound for an Euler reduction and no unrestricted Euler nonexistence statement follows. No original Pan-Wolff proof was retrieved or read. The derivative conversion in the sequel's Example 2 is consistent: for u=(partial Re v, partial Im v), |partial_bar u|=|Delta v|/4 and |u|=|grad v|/2, but existence of its starting scalar example is still an external premise here.

At the initial save, existing configured model file comparison had been requested. It is assessed below; actual provider execution is independently unattested. No new agent or model client was used. No mathematical numerical experiment or formal build was run. Source HTTP retrieval, offline extraction and rendering do not test an Euler theorem.

## 10. Completed comparison and latest source revision

The complete Theory Agent C  comparison dated 2026-11-04T05:39:24Z, its Python script and its retained log have now been read. The eight hand-checked items agree with Sections 2-9. In particular the C reader independently checked the published page 7 image: the radius in its Morrey estimate is t/2, despite an extraction rendering that looks like 2t. The n=1 invocation of the hybrid theorem needs the same repair already made here; replacing the inverse-radius coefficient on the known zero ball makes the final weak-continuation input valid.

The retained log has 37 passing checks: 22 SYM, nine EXACT, four EX and two SAMPLE. The EX controls in this script are exact arithmetic or symbolic counterchecks, unlike some other agent scripts. The EXACT label includes finite dimension or parameter samples, one exact polar integral and checks specialized to epsilon=3/4. The two SAMPLE entries use twenty floating-point points for n=2, k=2, epsilon=3/4 and are numerical only. Symbolic polynomial and specialized tests do not prove the universal analytic assertions by themselves. The general conclusions rest on the hand arguments above. The script has not been rerun.

The latest literature source, hash 722318d490915b86d05e3fd228a343a4ab980829e90fc29c49b13717e4fd3bd3, and its 61 manual checks have been read. It incorporates the publisher comparison and correctly changes the positive LIT348 reference to A2923. The publisher addendum is consistent with this audit, including the false universal hybrid nonmembership sentence and the exact Example 2 derivative conversion. The literature agent's total source-inventory count is not independently certified here.

Thus the slicing and regularity reductions are confirmed, and the four main statements are confirmed as deductions from the named continuation inputs. The peripheral universal nonmembership sentence is refuted by W=1, for which the exact square integral is pi beta R^(2/beta). No new critical scalar, higher-dimensional sharpness or Euler conclusion follows. The comparison comes through an existing configured model agent; actual provider execution is independently unattested.

The literal published combined-proof sentence has also been checked again in the retained text at line 655: it invokes Theorem 2.4 for N=1 and Theorem 2.5 for n=2. Thus the C comparison correctly transcribes the second condition as source dimension n=2. This is distinct from its separate target dimension N, and does not change the n=1 repair above.
