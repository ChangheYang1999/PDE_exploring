# Forward-strain vortical coverage at finite regularity

This is the final proof after complete independent literature and configured-model reviews. It repairs A395 by constructing an actual interval partition before speed normalization. Sections 1-5 prove the finite geometric assertion; Sections 6-7 state the exact conditional Euler coverage theorem. The finite geometry and finite-time estimate A393-A394 are used at their recorded scopes.

For an integer r>=2, a C^r uniformly sublinear rotating Euler profile with 0<c<1/2 and arbitrary real omega has the full vortical basin coverage described below whenever r(1-2c)>Lambda_core. Here Lambda_core is the intrinsic forward derivative-growth rate of the backward carrier flow on a strict absorbing ball, defined in Section 7. This is a profile-dependent sufficient condition, not an automatic estimate or unconditional nonexistence theorem.

## 1. Exact partition statement

Fix an integer r>=2. Use eta=1/100, D=50/49 and the definitions of small and bounded curves in [A393](auditor_proofs/proofs/forward_bin_cover/PROOF.md). Let g be a C^r diffeomorphism on a neighborhood of a regular bounded C^r curve gamma:[-1,1]->R^m. Let M>=1 bound its first derivative. Choose epsilon<=1 with

    epsilon^(j-1) sup ||D^j g|| <= M, 2<=j<=r,
    s=sup|gamma'|<=epsilon,
    sup|gamma^(j)|<=eta s, 2<=j<=r.

Let rho(t)=|(g gamma)'(t)|/|gamma'(t)| and

    E_k={t: exp(k)<=rho(t)<exp(k+1)}.

There is a finite interval partition of [-1,1], modulo shared endpoints, with increasing affine parameter maps theta from [-1,1], such that:

1. All slopes are at most1/100; both gamma theta and g gamma theta are small and bounded.
2. An output is large when its maximum speed is at least epsilon/3. Its length then lies in [epsilon/2,2epsilon].
3. For every integer k, the number of outputs which are not large and whose input interval meets E_k is at most

       C_r (M exp(-k))^(1/(r-1)).                       (1)

4. The arclength Jacobian on every atom has distortion at most D^2<2.

Here C_r depends only on r and the fixed numerical constants. It does not depend on the dimension, the inverse derivative, the number of nonempty bins, the iterate or the normalized higher derivatives. The inverse derivative is used only to know that finitely many bins cover the whole curve. Its quantitative bound is not in (1).

The key order is to cut overlaps after the polynomial and bounded-derivative steps of A393, before its final speed subdivisions. At that stage each bin has only C_r(M exp(-k))^(1/(r-1)) intervals, including its potentially long images.

## 2. The precise already-proved input

Stop A393 at the end of its Section3. For each nonempty bin k it gives a finite family I_k of closed, nondegenerate parameter intervals. They have disjoint interiors within their own bin and cover E_k. Write

    R_k=M exp(-k)>=1,  N_k=R_k^(1/(r-1)).

The number m_k of intervals satisfies m_k<=C_r N_k. Each original affine slope is at most1/100. Its output curve is bounded, although its speed need not yet be at most epsilon. Every point of every retained interval satisfies

    a0 exp(k)<=rho(t)<=b0 exp(k),
    a0=(1-3/100)/D,  b0=D exp(1)+3/100.                 (2)

These assertions follow from A393's Taylor and polynomial cuts and its fixed K_r subdivision. Intervals missing E_k may be discarded at this stage. Nothing in that proof requires first doing the speed subdivision.

The constants satisfy log(b0/a0)<2, a0>exp(-1) and b0<exp(2). Therefore two intervals whose labels differ by more than2 cannot intersect. Also an interval labeled k can meet an actual tangent bin E_l only when |l-k|<=2. In fact both integer differences are at most1, but the conservative bound2 is sufficient here.

The positive continuous function rho has a positive minimum and finite maximum on the compact curve. Only finitely many bins occur. Thus the union of the intermediate families covers [-1,1].

## 3. Cut all intermediate endpoints, then count by their labels

Take the sorted finite set of all intermediate endpoints, together with -1 and1. Its consecutive nondegenerate closed intervals form a global interval partition. Every such atom A is contained in at least one intermediate interval: choose an interior point away from the finite endpoint set, and use the cover; neither endpoint of that covering interval lies inside A. Assign A one covering interval and its label k, with any deterministic tie rule.

Let n_k be the number of atoms assigned label k. Charge each such atom to its left endpoint. Apart from -1, this is an endpoint of some intermediate interval of label j. Because the atom is contained in an interval of label k, its left endpoint belongs to both closed intervals. Equation(2) implies |j-k|<=2. There are at most two endpoints per intermediate interval, so

    n_k<=1+2 sum_(|j-k|<=2) m_j
        <=C'_r N_k.                                  (3)

For the last inequality set m_j=0 for empty bins and use N_j=exp((k-j)/(r-1))N_k. Every assigned label k came from a nonempty E_k, so exp(k)<=sup||Dg||<=M and N_k>=1. The estimate does not multiply by the total number of bins. It counts even atoms assigned k which no longer meet E_k. Their uniform enlarged speed band is all that is needed later.

This endpoint argument would be ineffective after speed normalization: the count at that later stage can contain an exp(k) term. Before normalization, (3) has only the desired N_k term.

## 4. Restore bounded derivatives and normalize speed last

An atom A is an affine restriction of its assigned bounded intermediate curve H. If that restriction has slope b<=1, then, since min|H'|>=sup|H'|/D,

    sup|(H theta)^(j)|/sup|(H theta)'|
          <=eta D b^(j-1), 2<=j<=r.

Divide A into two equal pieces. The composite slope relative to H is at most1/2, so every resulting curve is bounded with the original eta, because D/2<1. The input curve remains bounded as well: its total original slope was already at most1/100. This costs only a factor2 in (3).

For each resulting bounded output of maximum speed t, keep it if t<=epsilon. If t>epsilon, divide its parameter interval into L=ceil(t/epsilon) equal pieces. Every new speed lies between t/(D L) and epsilon, and t/(D L)>epsilon/(2D)>epsilon/3. Thus every piece created by this last subdivision is large. It remains bounded because L>=2. Each pre-normalization piece consequently creates at most one nonlarge child.

A final child meeting E_l has an assigned intermediate label k with |k-l|<=2, by (2). Equations(3) and the preceding paragraph give

    # {nonlarge children meeting E_l}
       <=2 sum_(|k-l|<=2) n_k
       <=C''_r N_l.

This is (1). The construction retains a full interval partition at every step. Its final slopes are at most1/200, hence satisfy the stated1/100 bound. A bounded large curve has length at least2epsilon/(3D)>epsilon/2 and at most2epsilon. Comparing the minimum and maximum speeds of its bounded input and output proves the D^2 distortion bound.

All four assertions in Section1 follow. No point is assigned to a noninterval derivative-itinerary atom.

## 5. Iteration and the existing finite-time estimate

Iterate this construction on every parent. It now gives actual finite nested interval partitions P^ell of the original straight arc. Shape and length tags are attached to these geometric parents. Actual integer tangent bins may vary on a parent; they need not define its partition.

For the bad-set estimate fix the derivative word of a point, exactly as in A394. At one parent, the number of nonlarge children meeting the next actual bin is bounded by (1). These are disjoint children of a global partition. Thus the fixed-word count and density-ratio proof of A394 apply with C_r replaced by C''_r. They give

    gamma_*=(r h-log M)/(r-1)-log C''_r

and its same finite-time estimate. Apply A307's existential selection rule verbatim to these new geometric atoms. Select a whole depth-ell atom if it contains a point of the retained target whose descendant within the specified future window is large and has that point as its hyperbolic witness. The ancestor rule is unchanged. Actual derivative itineraries are used only for the upper count and the existence of a witness; the measure is always restricted to the whole interval parent. No passage to a possibly disconnected itinerary subset is used.

At all earlier times, descendant image diameters are at most2epsilon 100^(-N). Relative original arclength on a parent maps to normalized image arclength with density at most D^2. The new global partitions therefore meet precisely the two reference-measure and shrinking-descendant premises of [A257](auditor_proofs/proofs/entropy_curve_absolute_continuity/PROOF.md). The overlap obstruction recorded in A395 has been removed at the level where that lemma is used.

## 6. Finite-regularity Euler coverage under a one-sided strain bound

Retain the full profile, cutoff and one-sided strain notation of [A373](auditor_proofs/proofs/strain_sum_vortical_coverage/PROOF.md), except allow any integer r>=2. Thus U in C^r is uniformly sublinear, P in C1, 0<c<1/2, every finite omega,

    B=(cI-omega J)y+U, W=curl U, a=1-2c,
    X=omega Jy-zeta(y)(cy+U),
    Lplus=max(0,sup lambda_max(sym D[-zeta(cy+U)])),
    Lminus=max(0,sup -lambda_min(sym D[-zeta(cy+U)])).

The cutoff zeta is one near a ball trapping the backward carrier flow and vanishes outside a larger ball, with inward radial transport throughout the intervening annulus. For its complete flow Theta,

    ||DTheta_t||<=exp(t Lplus),
    ||DTheta_(-t)||<=exp(t Lminus), t>=0.

A sufficient condition is

    r(1-2c)>Lplus.                                    (4)

If W is identically zero, the vortical coverage assertion is vacuous. Otherwise the expanding covector law gives a<=Lplus, so Lplus>0. Choose Lplus/r<chi<chi'<a. Take g=Theta_p, h=p chi+2, alpha=p chi'-1, M=exp(p Lplus), and q=ceil(p(Lplus+Lminus))+4. Exactly as in A394, sufficiently large p makes gamma_* positive and dominates log(32q). Choose epsilon for the derivatives of this fixed iterate only afterward. Condition(4) is strict and all constants in the nonlarge-child count are independent of p.

For every positive-volume residual subset of the vortical set, the covector identity first gives operator growth. The coordinate-direction choice and Fubini argument of A312 Section 3 and A308 Section 2 then obtain a positive-arclength transversal subset with upper tangent exponent at least a in a fixed coordinate direction. No tangent liminf bound is asserted. The original-curve construction in [A307](auditor_proofs/proofs/original_curve_measure/PROOF.md) uses precisely these upper exponents and the finite geometric times. Its density-subset choice, diagonal compactness, expansion and invariant-curve construction are unchanged. The only missing interface in A395 was the global interval partition for A257; Sections3-5 supply it. The uniform second-derivative bound gives compactness in C1 even at r=2, and the limiting first derivative is Lipschitz. For each fixed future window the image length lower bound and bounded-speed distortion give a strictly positive minimum speed. The tangent lies in a fixed narrow cone, so the incoming limit is an embedded C1,1 arc. Such an arc is C^(1+theta) for every0<theta<1 on its compact parameter interval. Its short carrier flow strips remain C1,1 because B is C2. A201 needs exactly a C2 carrier and C1 transported W; A216's full-leaf absolute-continuity argument needs only a regular embedded C1 incoming arc already in the unstable manifold; A299 uses C1 local product coordinates and uniform convergence. The original A307 finite-window construction and A257 use C1 compactness, not a third derivative. Thus none of these remaining steps introduces r>=3. One can extend the cutoff field outside a neighborhood of the trapped core to a closed three-manifold when applying a compact-manifold Pesin theorem, without changing any core orbit, derivative or strain constant used in the Euclidean partition construction.

For completeness, the conclusion is exactly that of [A308](auditor_proofs/proofs/smooth_vortical_basin_coverage/PROOF.md): almost every vortical point lies in the continuous-time basin of a compactly supported full-flow-ergodic vortical SRB probability with exponents (a,0,-1-c). Arclength nonatomicity of the nonconstant incoming curves excludes equilibrium components as in A308 Section 3. The combination of [A201](auditor_proofs/proofs/pesin_zero_capture/PROOF.md) and A299 excludes W=0 components; [A216](auditor_proofs/proofs/generalized_curve_srb/PROOF.md) supplies full unstable absolute continuity and physicality; [A299](auditor_proofs/proofs/original_curve_capture_geometry/PROOF.md) captures a positive portion of the original residual target. Taking the union of all physical basins and applying the same residual-target contradiction proves almost-everywhere coverage. There are at most countably many positive-volume basins. [A207](auditor_proofs/proofs/unstable_alpha_density/PROOF.md) and [A223](auditor_proofs/proofs/vortical_essential_basins/PROOF.md) then give disjoint invariant open essential basin domains, with complements null in their respective basins. Supports are still allowed to meet zero sets.

Every cited interface was fully reread by the auditor and by the focused configured-model reviewer. Their complete earlier proofs are dependencies, rather than additional hypotheses assumed without a proof. In particular the original-curve target localization is retained, so one does not infer full coverage merely from constructing a single physical measure.

## 7. Intrinsic growth and the exact final hypothesis

Let Q be any sufficiently large strict absorbing ball for Psi, the complete flow of -B. Define

    M_n=max(1,max_(y in Q)||D Psi_n(y)||),
    Lambda_core=lim_(n->infinity) log(M_n)/n
               =inf_(n>=1) log(M_n)/n.

[A398](auditor_proofs/proofs/absorbing_core_growth/PROOF.md) proves existence, independence of the admissible radius and of the chosen norm, and Lambda_core>=a whenever W is nonzero. It also proves the localized parameter estimates needed here. All curves and all Taylor segments are in the same convex forward-invariant Q. Uniform entry into Q transports any bounded positive-volume residual target there by a fixed carrier time and preserves its positive volume. Inverse derivative estimates are needed only along those compact orbit segments, to bound the number of possible integer bins.

The exact sufficient condition is

    r a>Lambda_core,                    r>=2 integer.          (5)

Choose Lambda_core<L<r a and L/r<chi<chi'<a. By the definition of the limit, for all sufficiently large integer p the first-derivative bound for g=Psi_p on Q is at most exp(pL). Choose epsilon afterward to control the finitely many higher derivatives of this fixed map on Q. The inverse bound on Q gives a bin count q=O(p). With h=p chi+2 and alpha=p chi'-1, the nonlarge-run exponent is

    gamma_*=p(r chi-L)/(r-1)+2r/(r-1)-log C''_r.

It grows linearly, while log(32q) grows only logarithmically. Because a<=Lambda_core<L, alpha<=pL for large p. The time-selection, nested partition, whole-parent measure and C2 capture proofs above all apply. Compact-manifold extension is made only after this Euclidean geometry, away from a neighborhood of the trapped core, and does not change its orbits or derivatives. This proves the claimed coverage under (5).

Equivalently, a sufficient finite-iterate test is log(M_n)<r a n for some positive integer n. No such norm bound has been numerically certified for an unknown profile.

Let K=intersection_(t>=0) Psi_t(Q) and Z=K intersect ({B=0} union {W=0}). [A399](auditor_proofs/proofs/degenerate_core_growth/PROOF.md) proves

    Lambda_core=max(a,Gamma_Z)

when W is nonzero. Gamma_Z is the attained maximum of the top backward Lyapunov exponent among full-flow-ergodic invariant probabilities supported on Z; set it to negative infinity if Z is empty. Consequently (5) is equivalent to Gamma_Z<r a. In particular C2 coverage follows if Gamma_Z<2a. This is a strict bound on every such measure, including entropy-zero measures and point masses, not merely on physical or positive-entropy probabilities.

## 8. Scope and verification

The conclusion is almost-everywhere vortical coverage by at most countably many compactly supported full-flow-ergodic SRB probabilities, with exponents (a,0,-kappa), the positive unstable densities of A207 and the open essential basin domains of A223. Their supports may meet the zero sets. The proof does not establish (5) for arbitrary C2 profiles and does not exclude a sign-changing essential basin.

A373's older strain-sum criterion implies (4), and (4) implies (5), but (5) is the hypothesis of the strongest result recorded here. Arbitrary-omega decay-only nonexistence and unconditional C2 coverage remain open. Transfer of any separate Liouville corollary is outside this proof and requires its own given-measure regularity check.

The endpoint partition and all C2 interfaces were independently challenged through existing configured with the primary model working files. This is a configuration statement, not independent provider attestation. The literature review, its alternative greedy construction and the complete focused coordinator review are retained with hashes. No new model client, numerical computation or formal build was used for this theorem.

## 9. Independently checked greedy alternative and its terminology

LIT80 supplies a second construction. In the intermediate per-bin cover of Section 2, double the fixed derivative subdivision so that each output obeys sup|H^(j)|<=(eta/2)sup|H'|. Starting from the left endpoint, choose an interval containing the current point whose right endpoint is greatest, and take the segment up to that endpoint. At any point short of 1, finiteness and closedness of the cover guarantee an interval extending right: otherwise covered points decreasing to that point from the right would contradict the asserted failure. The right endpoints strictly increase. The construction terminates, uses each intermediate interval at most once, and makes a genuine partition.

Every selected segment is an affine restriction of its assigned interval. The stronger derivative bound gives min|H'|>=(1-eta)sup|H'|, so every restriction has derivative-to-speed ratios at most (eta/2)/(1-eta)<eta, even if its restriction slope is close to 1. Give a segment from original bin k the assigned label ell=k-1. The band in (2) gives ell<=log rho<=ell+3 throughout the entire segment. Speed normalization last produces at most one nonlarge output per assigned intermediate interval. Hence, for each ell, the number of nonlarge outputs is at most C_r(M exp(-ell))^(1/(r-1)). Every child has a constant assigned label and the whole tree partitions the original arc.

For a word of these assigned labels, the fixed-word run count of A394 is unchanged: the number times relative input length over a retained run of k steps is at most

    8 C_r^k exp((k log M-sum ell_i)/(r-1)-h k)
       <=8 exp(-gamma_* k).

The gap argument uses disjoint partition children. Summing words and retained runs gives the same exponential bad-set estimate with q the label count. Since log rho<=ell+3, a tangent-growth time now uses alpha=p chi'-3 rather than p chi'-1. This changes an additive constant only; the limiting positive-density parameter and strict threshold r a>Lplus are unchanged. The whole-parent, C2 and localized-core arguments of Sections 5-7 then apply identically. This confirms LIT80's intended construction as an alternative proof, with the following explicit wording repair.

In the submitted LIT80 finite lemma and its counting paragraphs, "small outputs" must mean NONLARGE outputs, those with maximum speed below epsilon/3. All outputs are already small in the separately defined sense of maximum speed at most epsilon. The literal bound on the number of all small outputs is false: take g(x)=Kx and gamma(t)=epsilon t e1. Their total output length is 2K epsilon, while each final small output has length at most 2epsilon, so at least K outputs are necessary. Yet there is one assigned label ell=floor(log K)-1 and (M exp(-ell))^(1/(r-1))<=exp(2/(r-1)), independent of K. Thus the literal reading cannot be authorized. The corrected nonlarge count is precisely what the subsequent retained-run argument uses.
