# Correction of a scope inference in the first model review

Date 2026-10-22T02:19:53.368173+00:00. This note preserves the original proof unchanged and challenges one sentence in the complete actual Claude Opus5.5 review, request7febcb4a-6050-41ad-9002-3d8f21d384bd.

The review correctly verifies the quasimode construction. Its section7 also says: "As a consequence, L_ρ does not map general Σ ≠ 0 domain elements into X_m when m ≥ 3." This does not follow from the preceding fact that D rho is outside X_m. The rank term and nonlocal term can cancel at the center. Nonzero strain by itself is not an obstruction to membership of the full image. The statement should not be used to exclude every nonzero-strain perturbation, or to infer generic failure already for m=3,4 among compact perturbations vanishing near the center.

Here is an exact counterexample to such an exclusion for the distinguished canonical modal background. Let chi0 be smooth, nonnegative, nonzero, supported in1<r<2, and set b0=x^2 y chi0(r). This is smooth compact, has J(b0)=0 and the required even-even global factor. Its only nonzero density sine modes are

    F_1(r)=F_3(r)=r^3 chi0(r)/4.

Formula(5) of PROOF.md therefore gives

    Gamma_2(b0)=(1/8) integral_1^2 r chi0(r)dr>0,
    Gamma_n(b0)=0 for every even n>=4.

Put sigma=2 Gamma_2(b0)>0. Inside r<1 the canonical stream is exactly sigma x y, because it is harmonic, odd in both coordinates, and has no other allowed homogeneous coefficients. Consequently U[b0]=(-sigma x,sigma y) there. The local density transport terms are zero there. Thus

    L_rho b0=sigma(-x partial_x+y partial_y)rho+(sigma/3)D rho.

For rho3=x^2 y the coefficient is sigma(-2+1+3/3)=0. This cancellation was also verified by independent symbolic differentiation in code/independent.py, recorded as additional_cubic_affine_plus_rank_identity=0 in evidence/independent.json. The source and input hashes are bound in that audit.

For this actual modal background, research/modal_graph_scaling/PROOF.md equation(3), with ADDENDUM.md and REVIEW_RESOLUTIONS.md, proves the differentiated remainder estimates

    R=rho-rho3=O(r^5), grad R=O(r^4), Hess R=O(r^3).

It follows that L_rho b0=O(r^5) and grad(L_rho b0)=O(r^4) near0. The squared X_m norm density is therefore bounded by a constant times r^(9-2m) dr, integrable for m=3 and m=4. On the fixed middle annulus all functions are regular. At infinity, b0 and its derivatives are zero; U[b0]=O(r^-2), DU[b0]=O(r^-3), while D rho=O(r^k), grad D rho=O(r^(k-1)). The full image has order O(r^k) and derivative O(r^(k-1)), so its squared norm density is O(r^-2) dr for every fixed m. Hence b0 and L_rho b0 belong to X_m for m=3,4 although Sigma(b0)>0.

The same leading cancellation applies to any smooth compact density vanishing near0: all velocity terms beyond its affine strain start at cubic order by harmonicity and parity, producing order r^5 after multiplication by grad rho. This observation does not claim that all such perturbations have images in X_m for m>=5, nor does it assert that every permitted general domain element has a center hole. The explicit b0 example alone suffices to refute automatic exclusion from nonzero strain for m=3,4.

None of this changes the quasimode proof. That proof cancels Sigma(v) exactly, imposes the required higher velocity moments, and estimates the corrected full expression directly. Its cautious statement that the separate images "need not belong" is a reason to avoid splitting possibly singular terms, not an asserted classification of all such images. The original proof's graph-domain qualification remains essential, since the operator composition must be defined. The claims about every fixed m>=2 remain subject to actual input review and later independent adjudication. This is not a PDE endpoint.
