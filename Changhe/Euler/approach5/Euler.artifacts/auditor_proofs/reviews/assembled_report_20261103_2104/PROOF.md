# Notes120-121: bracket repair and summary scope

## 1. Statement and evidence

This audit concerns the report pinned at SHA256 58227395cd21816e1d4bdda88b7a183babcd58396e8294e29ff554a0bf56aa6f,6734 lines, and its four companion files in the team records. The baseline is Note119 at bf26780396864cdf045378dac0a1b906f9c4402cdf3af7e37406f11574f01854, audited in the team records. All21860 report-delta characters and26138 assumptions-delta characters were read. The other three companions are unchanged. The complete sections2A-2D are byte identical, with their hashes in the team records. AppendixA begins at4703 and AppendixB at5167.

The predecessor package accidentally overwrote its pinned companion README with a verification guide after its mathematical comparison. Its original README has now been restored from the identical current companion and verified against its original manifest hash4294118a74e0803b0c2e53e0eb545d7835b4a8722a508706ef69a6496939e8ab. The guide is named in the team records. The evidence maintenance changes no mathematical content or comparison conclusion.

## 2. The missing bracket hypothesis is restored

Let0<c<1/2 and let X,W,W0 be smooth vector fields, with div X=-3c, div W=div W0=0 and [X,W]=(1+c)W, [X,W0]=(1+c)W0. Suppose W=fW0 along a neighborhood of a positive X-orbit, W(a)=f(a)W0(a) is nonzero, the orbit is precompact, and W0 is nowhere zero on its compact limit set. Then W has no zero on that limit set.

Indeed, subtract the two bracket equations in [X,fW0]=(Xf)W0+f[X,W0]. At every point of the orbit W is nonzero by the invertible characteristic formula for [X,W]=(1+c)W. Hence W0 is nonzero there and Xf=0. Thus f is the same nonzero value f(a) along the orbit. For any limit point q, continuity gives W(q)=f(a)W0(q), which is nonzero. A local scalar f near a point where W0 is nonzero is automatically smooth from f=(W.W0)/|W0|^2; no additional scalar regularity issue arises on these orbit and limit neighborhoods.

The revised AppendixA and ASSUMPTIONS sentence now explicitly requires W0 smooth, divergence free and satisfying the same bracket equation. This proves the stated implication, repairs A2314 exactly as specified in A2315, and retains the precompactness and nonzero conditions restored in A2299. The divergence of W0 is harmless additional structure; the bracket calculation itself is what was previously missing. It does not establish any general profile exclusion because the relation W=curl U and the pressure equation are not part of this kinematic lemma.

## 3. Linear-weight normalization and the summary quantifier

The C66 clause now quantifies a>0 and b,gamma real in the linear weight (a,b,gamma t). This is precisely TheoremSF.3 and A2316: dividing the density by a normalizes a=1, whereas allowing a=0 would admit the identically zero density and invalidate a claim excluding every nonnegative density. No new value of the threshold is asserted here, and C67 is not yet inserted.

For row10 retain the hypotheses of Theorem7:2/5<c<1/2, arbitrary omega, U in C2, P in C1, the full divergence-free profile equation, uniform decay, global zero helicity, and its derivative bound. The actual leading tails define T0 as in Theorem7. If the tail is smooth near every point of T0, Theorem7(f)/A1292 says that a nonzero profile has at least one common infinitely flat point of V and S in T0. It does not exclude every individual finite-order point in T0. Thus the shortened words "only points at which V and S both vanish to infinite order remain" are valid only as a description of the remaining obstruction. The same sentence explicitly retains the parenthesis that an individual finite-order point is not excluded, A1272. With that explicit qualification it retains the prior quantifier. For unambiguous prose, restore "a nonzero profile must have a point of T0 at which V and S both vanish to infinite order".

The irrotational-sector conclusion still assumes the global two-sided comparison on the whole unit sphere. The lower-bound-only-near-common-zeros case remains explicitly unresolved by A2066. The removed list of special sector classes remains unchanged in the referenced sections7(R3) and10(1); referring to it does not strengthen the general claim. The new derivative-bound and Theorem6-witness sentence retains the same class implications already checked in the team records, Section3: excluding all three precise witnesses gives vanishing for helicity-free decaying C2 profiles without a tail or derivative premise. No such exclusion has been proved. The C-infinity essential-basin problem with helicity of both signs is separately retained as open.

## 4. Verdict and limits

The Note120 repairs and the Note121 summary, read with its explicit finite-order parenthesis, are confirmed at the scopes above. The front, main text and AppendixA, lines1-5166, inherit the earlier assembly audit with A2314 now repaired. Previously audited individual historical statements retain their own verdicts. This is not a new blanket approval of all AppendixB-D. In particular, neither the exact linear threshold newly submitted in C67 nor the unrestricted decay-only conjecture is established by this assembly comparison. No numerical calculation or PDE computation was needed.
