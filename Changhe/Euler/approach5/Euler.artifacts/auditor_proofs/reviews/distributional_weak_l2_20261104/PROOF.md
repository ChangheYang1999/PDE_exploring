# Distributional continuation with a small weak-L2 coefficient

Status: independent analytic reconstruction of submitted LIT347. Existing configured model comparison is pending. The numerical constant is sufficient, not asserted optimal. This is a planar theorem, not a new Euler nonexistence theorem.

## 1. Exact statement and dependencies

Let O be a connected open subset of the complex plane and N a positive finite integer. The operator dbar=(partial_x+i partial_y)/2 acts componentwise on complex N-vectors. All vector magnitudes below are Euclidean, and dA is planar area. For 1<p<infinity set

    K_p(h;D)=sup_(t>0) t area{x in D:|h(x)|>t}^(1/p).

Assume u belongs to local weak-L4 on O, dbar u=g in distributions with g locally integrable, and |g|<=b|u| almost everywhere. Assume b>=0 is finite almost everywhere and locally weak-L2. At every a in O require a relatively compact disc D about a with

    K_2(b;D)<sqrt(pi)/32.

Then either of the following hypotheses implies u=0 almost everywhere on O: u vanishes almost everywhere on a nonempty open set; or, at some a0,

    integral_(B(a0,r)) |u|^2 = o(r^L) for every L>0.

The same conclusions hold if each a has a relatively compact disc D on which

    lim_(T->infinity) sup_(t>=T) t^2 area_D{b>t}<pi/1024.

In particular local finite-q Lorentz L^(2,q), 0<q<infinity, coefficients meet the latter requirement. Local H1, bounded or continuous unknowns qualify if they satisfy the distributional equation: H1 embeds locally into L4 in dimension two, and the other two classes are locally bounded. This embedding is an explicit standard additional input to the Sobolev specialization.

The direct proof below uses layer cake, Tonelli, elementary rearrangements, smooth cutoffs and the distributional Cauchy fundamental solution. It is independent of LIT344-LIT346 and of the Seo lemma discussed in Section9. It uses neither pressure nor any global characteristic flow. No zero-isolation conclusion or pointwise representative of u is asserted.

## 2. A genuine norm and the product estimate

Extend restricted functions by zero when using whole-plane norms. For 1<q<infinity define

    A_q(h)=sup_(0<|E|<infinity) |E|^(-1+1/q) integral_E |h|.

It has the triangle inequality by the triangle inequality under each integral. Taking finite pieces of a superlevel set gives K_q<=A_q; layer cake, or h*(s)<=K_q s^(-1/q), gives A_q<=q K_q/(q-1). The argument applies without dimension-dependent constants to vectors. If A_q is finite, an infinite-measure positive superlevel set is impossible, by taking arbitrarily large finite pieces. The definiteness of this norm and its triangle inequality are all that absorption needs; no assertion of completeness is needed.

Let B=K_2(b), F=K_4(v). If either is zero the product is zero almost everywhere. Otherwise for t,a>0,

    area{|bv|>t}<=B^2/a^2+F^4 a^4/t^4.

The choice a^6=B^2 t^4/F^4 makes the two terms equal. Each equals (BF/t)^(4/3), so

    K_(4/3)(bv)<=2^(3/4)BF<=2^(3/4)B A_4(v).

This is a weak-space product inequality. Strong Holder into L^(4/3) is not being assumed. On any finite-area set, local weak-L4 also gives L2: integrating min(|E|,F^4/t^4) against 2t dt is finite. Thus u has the local integral quantities used in Section1.

## 3. Direct Cauchy-potential bound

Put k(z)=1/(pi|z|). For a measurable E of finite positive area m let K_E(y)=integral_E k(x-y)dA(x). Radial rearrangement, or layer cake and the intersection bound min(m,pi r^2), gives

    K_E(y)<=2 sqrt(m/pi).

Split k at radius R. Its near part has L1 norm2R, hence the near part of K_E has L1 norm2Rm. The far part of K_E is at most m/(pi R). Taking R=2m/(pi lambda), Markov gives

    area{K_E>lambda}<=8m^2/(pi lambda^2).

Its decreasing rearrangement therefore satisfies

    K_E*(s)<=min(2sqrt(m)/sqrt(pi),sqrt(8/pi)m s^(-1/2)).

The two bounds meet at s=2m. If G=K_(4/3)(h), then h*(s)<=G s^(-3/4). Double layer cake bounds the integral of two nonnegative functions by the integral of their decreasing rearrangements: at each pair of levels use the smaller superlevel measure as an upper bound for their intersection. Tonelli now gives

    integral_E(k*|h|)<=G integral_0^infinity s^(-3/4)K_E*(s)ds.

The integral on (0,2m) equals at most 8*2^(1/4)G m^(3/4)/sqrt(pi); the integral on (2m,infinity) has the same bound. Hence, with C0=16*2^(1/4)/sqrt(pi),

    A_4(k*|h|)<=C0 K_(4/3)(h).

In particular the nonnegative convolution is integrable on every bounded set and finite almost everywhere. The complex integral

    Th(z)=integral h(zeta)/[pi(z-zeta)]dA(zeta)

is absolutely convergent almost everywhere, componentwise and in Euclidean magnitude. The bound |Th|<=k*|h| proves A_4(Th)<=C0 K_(4/3)(h). Every estimate is independent of N. This proves existence of the needed integral, instead of inserting pointwise convergence as an extra premise.

## 4. Compact distributional inversion

The locally integrable distribution E(z)=1/(pi z) satisfies dbar E=delta_0. If v is a compactly supported distribution, the convolution with E is defined and derivatives commute with convolution. Therefore

    E*(dbar v)=(dbar E)*v=delta_0*v=v.

There is no unspecified entire correction in this identity. Compact support of v is the hypothesis that permits this convolution identity globally. When dbar v is a compactly supported weak-L^(4/3) function, Section3 gives the locally integrable absolutely convergent representative of E*(dbar v). This is the representative to which the norm estimate applies.

## 5. Integer weights and absorption

Translate the point of infinite integral order to0 and choose a relatively compact disc B_R on which B=K_2(b;B_R)<sqrt(pi)/32. Let 0<=chi<=1 be smooth, compactly supported in B_R, and equal1 on B_(R/2). Let eta_epsilon be a radial smooth cutoff, zero on B_epsilon and one outside B_(2epsilon), between0 and1, with |dbar eta_epsilon|<=C/epsilon; take epsilon<R/8.

For a positive integer m put v_epsilon=z^(-m)chi eta_epsilon u, extended by zero to the plane. It is compactly supported and weak-L4. The multiplying function is smooth across0 because the inner cutoff vanishes nearby. On its nonzero region z^(-m) is single-valued and holomorphic. The distributional product rule gives

    dbar v_epsilon=h0+h1+h2,
    h0=z^(-m)chi eta_epsilon g,
    h1=z^(-m)eta_epsilon u dbar chi,
    h2=z^(-m)chi u dbar eta_epsilon.

The first term satisfies |h0|<=b|v_epsilon| and is weak-L^(4/3) by Section2. The other two have compact support and are in L^(4/3), since for fixed m and epsilon their coefficients are bounded and u is locally L2. Thus all three terms are compactly supported, locally integrable weak-L^(4/3) functions.

Apply Section4, the triangle inequality for A4, then Section3 to each term separately. Section2 gives

    A_4(v_epsilon)<=32B/sqrt(pi) A_4(v_epsilon)
                     +C0[K_(4/3)(h1)+K_(4/3)(h2)].

The constant is exactly C0*2^(3/4)=32/sqrt(pi). The finite left side is absorbable because a=1-32B/sqrt(pi)>0. Consequently

    A_4(v_epsilon)<=C0/a [K_(4/3)(h1)+K_(4/3)(h2)].

No false constant-one triangle inequality for the weak quasi-norm K_p occurs.

## 6. The two limits

Set A=K_(4/3)(u dbar chi), finite independently of m and epsilon. Since dbar chi vanishes for |z|<R/2,

    K_(4/3)(h1)<=(R/2)^(-m)A.

On the inner annulus, of area at most4pi epsilon^2, finite-area Holder yields

    K_(4/3)(h2)<=||h2||_(4/3)
       <=C epsilon^(-m-1)||u||_(L^(4/3)(B_(2epsilon)))
       <=C epsilon^(-m-1/2)||u||_(L2(B_(2epsilon))).

For each fixed m, the flatness assumption with L=2m+1 makes the last quantity o(1). Any larger power also works. First let epsilon tend to0 at fixed m. Fatou on every E in the A4 definition, followed by taking the supremum, gives

    A_4(z^(-m)chi u)<=C0/a A(R/2)^(-m).

This simultaneously proves the necessary weighted integrability. Next fix0<rho<R/2. Since chi=1 there and multiplication by a function of modulus at most rho^m multiplies A4 by at most rho^m,

    A_4(u 1_(B_rho))<=C0/a A(2rho/R)^m.

Now let the positive integers m tend to infinity. The right side tends to0, all other constants being independent of m. Thus u=0 almost everywhere on B_rho. A countable increasing sequence of rho proves vanishing on B_(R/2). The order of limits is indispensable; no uniform inner-cutoff error in m was assumed.

## 7. Propagation and high tails

The set Z of points with an open almost-everywhere zero neighborhood is open. Section6 makes it nonempty under integral flatness, and it is nonempty by definition under the alternative open-set assumption. At a point b0 in its closure choose a small-norm disc B(b0,R). Pick a in Z with |a-b0|<R/16. The disc B(a,R/2) is contained in B(b0,R), so has the same strict coefficient bound; u is integral-flat at a. The local theorem gives zero on B(a,R/4), which contains a neighborhood of b0. Hence Z is also closed in O, and connectedness gives Z=O.

For a measurable F contained in D and T>0,

    K_2(b;F)^2<=max(T^2|F|,sup_(t>T)t^2 area_D{b>t}).

For a high-tail limit strictly below pi/1024 first choose T so the second term is below that number, then shrink the disc F so the first term is also below it. This yields exactly the strict small-norm hypothesis. Local L2 has zero tails by absolute continuity of the integral of b^2 on {b>t}.

For the finite-q Lorentz assertion write a(t)=t sqrt(area_D{b>t}). Finiteness of integral_0^infinity a(t)^q dt/t implies a(t) is bounded, since on [t/2,t] its value is at least a(t)/2 by monotonicity of the distribution. If its high tail did not tend to0, choose unbounded t_j with a(t_j)>=epsilon and a subsequence with disjoint intervals [t_j/2,t_j]. Each contributes at least (epsilon/2)^q log2, a contradiction. Thus the asserted high tails vanish for every finite q>0.

## 8. Exact scope and missing Euler input

The unknown is an almost-everywhere vector class with a distributional equation. No representative value at a point, classical derivative there, isolated-zero result or lower bound by one fixed power at every nonzero germ is inferred. Negating infinite-order little-o vanishing alone does not give a uniform power lower bound at all small radii. The constants are independent of the number of components. The threshold and high-tail inequalities are strict, with no equality claim or optimality assertion.

The H1 specialization only invokes the standard local planar H1-to-L4 embedding. A rough three-dimensional field has not been shown to possess the required sectional trace, a distributional quotient equation, or the needed regularity in isothermal coordinates. Each of those inputs, the actual coefficient estimate and integral flatness must be established separately before applying this planar result to an Euler carrier. No additional arbitrary-omega Euler conclusion follows here. The global decaying-profile conjecture remains unresolved.

## 9. Actual Seo source and the all-real counterexample

The retained primary source is Ihyeok Seo, A remark on unique continuation for the Cauchy-Riemann operator, arXiv1409.1747v5,4May2015. Its actual five-page PDF has SHA25673e0a1b2c4bf56a44f5aaf6dd73e9bc0132e53a5795254b2922cd9a933ace1c4. All five extracted pages were read, and the rendered printed page2 was visually inspected. The reading covers its statements, full proofs and references; it does not include a journal-version comparison.

Theorem1.1 assumes global u in Lp intersect Lq, 1<p<2<q<infinity, 1/p-1/q=1/2, and a global L2 coefficient, and concludes vanishing from a nonempty open zero set. Its Lemma2.1 asserts the weighted estimate

    || |z|^(-t)f ||_q <= C || |z|^(-t)dbar f ||_p

for every real t>0, uniformly in t, and all smooth f compactly supported away from0. The printed proof starts with z^(-t)f on the punctured plane. For noninteger t this multiplier has no single-valued global holomorphic branch.

There is also an explicit failure of the asserted inequality at one fixed t. Choose p=4/3,q=4,t=1/2. Let chi be smooth radial, supported in r<1 and equal1 on r<=1/2; let eta be smooth radial, zero on r<=1 and equal1 on r>=2. For0<epsilon<1/8 put f_epsilon(z)=chi(|z|)eta(|z|/epsilon). This is smooth and compactly supported away from0. It equals1 for2epsilon<=r<=1/2, so

    ||r^(-1/2)f_epsilon||_4^4>=2pi log(1/(4epsilon))->infinity.

The fixed outer derivative annulus contributes a bounded weighted L^(4/3) integral. On the inner annulus |dbar f_epsilon|<=C/epsilon and

    integral_(epsilon<r<2epsilon) |r^(-1/2)dbar f_epsilon|^(4/3)dA
       <=C epsilon^(-4/3) integral_epsilon^(2epsilon) r^(1/3)dr<=C.

Thus the right side stays bounded. Even a constant depending on the fixed t=1/2 cannot make the displayed inequality valid. This refutes the literal all-real Lemma2.1. It does not refute Theorem1.1: a positive integer sequence suffices for its limiting mechanism, and Sections3-6 supply a direct integer-weight route for the present theorem. The Fourier-multiplier proof was read but is not imported as an unexamined premise or collectively certified here. No novelty of the earlier Carleman strategy is claimed.

## 10. Verification record

All eight submitted LIT347 sections and35 manual self-checks were read. The submitted proof SHA256 is03ba40bd82862b31d10e72e0d4a9eac76e9f576ec5071f5c29a20b4de775a690. Copies of the source, checks, actual Seo PDF, text, rendered page, reading note and retrieval record are in the team records, with exact capture hashes. The provenance record is the literature agent's reported retrieval; this audit independently accessed and inspected its retained primary source. No successful browser response is used as evidence.

No mathematical computation, formalization, new model call, subagent or prohibited execution was needed for this reconstruction. The independent argument agrees with the submitted statement; the existing configured model comparison remains pending before designated promotion. Actual provider execution of that existing agent is not independently attested.

## 11. Existing model comparison and independent response

Items4-6 of the complete Theory Agent C note of 2026-11-04T04:34:34Z were independently checked against Sections1-9 and retained. This is an existing configured model comparison; actual provider execution is independently unattested. Both weak-product terms at the optimizing split equal (BF)^(4/3)t^(-4/3), yielding 2^(3/4). The kernel bounds intersect at s=2m. Each rearrangement integral is 8*2^(1/4)G m^(3/4)/sqrt(pi); after the product bound, the absorption factor is exactly32B/sqrt(pi). The strict inequality and two ordered limits are essential. The open-zero propagation uses a new center in the known zero set and therefore introduces no pointwise representative assumption.

The actual Seo PDF hash independently retained here agrees with the comparison's reported retrieval. Its all-real-weight lemma fails at t=1/2 by Section9. At the integer t=1, the same cutoffs give both norms of order epsilon^(-1/2), so they do not refute the integer estimate. No unrestricted rough scalar or Euler theorem is inferred. The comparison's numerical script and its count are not independently certified or needed for the hand proof.

## 12. Confirmed-source revision check

The exact source revisionb2eeb792b79f4dce438aa1fb20a05ad871943a4affcf505b9e8c837f5c4b3533 was compared with the submission in full. It changes the opening status and adds a confirmation note. The actual weak-L4, distributional-equation and strict coefficient hypotheses remain unchanged. The new note restricts A2921 to the literal retained Seo v5 lemma and does not refute the main theorem or an unseen journal version. The old pending sentence is retained within the dated original submission record and is superseded by the new note.


## 13. Correction of the previous section's exact-hash attribution

The preceding section and A2928 quoted the earlier announced hash b2eeb792b79f4dce438aa1fb20a05ad871943a4affcf505b9e8c837f5c4b3533. The actual source retained at04:45:35Z and compared with the submission already had hash 509568fd5906815197a820542fa7b9b15802cb8155152af933e7ffeeb11aa9ea, as its unchanged capture JSON proves. Thus the attribution of that exact earlier hash to that earlier file inspection was inaccurate. It does not affect the mathematics.

The earlier version has now been retrieved from the literature agent's archived04:45:25Z handoff, copied into verification, and hashed independently. The complete difference between it and the retained version is one heading: 9 C becomes 9. There is no other change. Both versions therefore preserve the same statements and proofs, and the earlier announced version is now directly checked as well. The earlier reading must not be backdated. The current live file is byte-identical to the version actually retained at04:45:35Z. The full original-to-retained difference and this one-heading difference have both been read.
