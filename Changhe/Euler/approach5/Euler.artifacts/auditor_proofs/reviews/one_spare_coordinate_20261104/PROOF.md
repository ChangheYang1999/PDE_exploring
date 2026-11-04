# One spare coordinate in the ambient inverse-radius construction

## 1. Claim, norm and dependencies

Fix an integer k>=1 and C>1/4. The claim is that some R>0 admits a map u in C-infinity(B_R in C^k; C^(k+1)) which is nonzero at every nonzero point, has every real derivative zero at zero, and satisfies

    |partial_bar u(z)| <= C |u(z)|/|z|,  0<|z|<R.

Here partial_bar_a=(partial_xa+i partial_ya)/2. The left side is the Euclidean norm of all (k+1)k entries. The target is fixed before the radius and is independent of C. Zero padding permits every fixed target N>=k+1.

The construction uses a smooth step, finite-sum Holder and Jensen inequalities, and elementary differentiation. It does not use the preceding LIT356 or LIT357 constructions. The positive endpoint theorem is a separate dependency of the sharpness corollary in Section 6. No Euler equation, divergence condition or carrier-pressure coupling is imposed on u.

## 2. Ordered transfers and a noncancellation invariant

Choose a smooth nondecreasing chi which is zero on (-infinity,1/4] and one on [3/4,infinity). Write M=max chi'>0. Define on [0,1]

    nu(tau)=chi(4tau)/2+chi(4tau-3)/2,
    theta_j(tau)=(pi/2)chi(3k tau-k-j+1),  1<=j<=k.

The jth angle varies only in

    I_j=((k+j-3/4)/(3k),(k+j-1/4)/(3k)).

The first left endpoint is 1/3+1/(12k), the last right endpoint is 2/3-1/(12k), each interval has length 1/(6k), and adjacent intervals have a gap of 1/(6k). Thus at most one angle is changing. Before I_j its value is zero and after I_j it is pi/2. Each derivative is at most D_k=3k pi M/2. The function nu is exactly 1/2 on [1/4,3/4], which contains all transfers. It goes smoothly from zero to 1/2 before the transfers and from 1/2 to one afterwards.

Label the k+1 target basis vectors e_0,...,e_k. At stage n, let h_n be the vacant slot and let s_(n,j) carry the jth coordinate. Initially h_1=0 and s_(1,j)=j. Set

    s_(n+1,1)=h_n,
    s_(n+1,j)=s_(n,j-1),  2<=j<=k,
    h_(n+1)=s_(n,k).

This is a permutation of all k+1 labels. In the transfer for coordinate j, the destination is vacant: for j=1 it is h_n; for j>1 it is the old slot of j-1, whose transfer has ended. For k=1 this reduces to exchanging the two slots.

There is only one possible type of collision in the written sum: old coordinate j and new coordinate j+1 share s_(n,j). Their coefficients cannot both be nonzero, because theta_(j+1)>0 forces theta_j=pi/2. The positive gaps also separate their derivative supports. Consequently every nonzero summand, including the old and new terms of the active transfer, occupies its own orthogonal target direction. This conclusion is valid at interval endpoints as well as in their interiors.

## 3. Radial envelope and exact differential

For r=|z|, put t=-log r and Q_(n,j)=r^(-n)z_j^n. For a unit direction zeta, set x_j=|zeta_j|^2 and S_n=sum_j x_j^n. Since sum_j x_j=1,

    k^(1-n)<=S_n<=1,
    S_(n+1)<=S_n<=k S_(n+1).

Indeed Holder gives S_(n+1)>=k^(-1/n)S_n^(1+1/n); dividing by S_n and using Jensen's lower bound gives S_(n+1)/S_n>=1/k. There is no division by an individual x_j, so coordinate-axis directions are covered.

Choose a fixed L>0 with 1/4+sqrt(k)D_k/(2L)<C and R=exp(-L). For t in [nL,(n+1)L], put tau=(t-nL)/L. Define F(L)=0 and F'=n+nu(tau). Near an endpoint the adjacent slopes both equal n+1 on neighborhoods. The continuous primitive F is therefore smooth and

    F(t)>=(t^2-L^2)/(2L)-(t-L).

All derivatives of F of order at least two are uniformly bounded in n, and F'=O(1+t).

Let

    Z=sum_j [cos(theta_j(tau)) Q_(n,j)e_(s_(n,j))
              +sin(theta_j(tau)) Q_(n+1,j)e_(s_(n+1,j))],
    u(z)=exp(-F(t))Z.

The noncancellation invariant gives the exact squared norm

    |Z|^2=sum_j [cos^2(theta_j)x_j^n+sin^2(theta_j)x_j^(n+1)].

Thus S_(n+1)<=|Z|^2<=S_n and u is nonzero off zero.

Holomorphicity of z_j^n leaves only derivatives through t. The target residual is A=A0+A1, where

    A0=sum_j [-nu cos(theta_j)Q_(n,j)e_(s_(n,j))
                  +(1-nu)sin(theta_j)Q_(n+1,j)e_(s_(n+1,j))],
    A1=sum_j dot(theta_j)W_j,
    W_j=-sin(theta_j)Q_(n,j)e_(s_(n,j))
                  +cos(theta_j)Q_(n+1,j)e_(s_(n+1,j)).

Dots denote t derivatives, bounded by D_k/L. The array partial_bar u is the outer product exp(-F)A tensor partial_bar t. Since partial_bar_a t=-z_a/(2r^2),

    |partial_bar t|=1/(2r),
    |partial_bar u|=exp(-F)|A|/(2r).

These equalities use the whole derivative array, not an individual complex coordinate or an operator-norm substitution.

## 4. The estimate covers every stage time

During the central interval nu=1/2. Orthogonality gives |A0|=|Z|/2 exactly. At most one dot(theta_j) is nonzero. The two basis vectors in that W_j are distinct, and

    |W_j|^2=sin^2(theta_j)x_j^n+cos^2(theta_j)x_j^(n+1)
             <=x_j^n<=S_n<=k S_(n+1)<=k|Z|^2.

It follows by the triangle inequality that |A|<=(1/2+sqrt(k)D_k/L)|Z|. Cross terms between A0 and A1 need not vanish and are not discarded; the triangle inequality handles them.

Before tau=1/4 all angles are zero, all angle derivatives vanish, and 0<=nu<=1/2. Hence A=-nu Z. After tau=3/4 all angles are pi/2, their derivatives vanish, and 1/2<=nu<=1. Hence A=(1-nu)Z. These cases and the central interval cover all times and all inter-transfer plateaus. Therefore

    |partial_bar u|/|u| <= [1/4+sqrt(k)D_k/(2L)]/r < C/r.

## 5. Stage joins and the origin

Near t=(n+1)L the old stage has all angles pi/2, the new stage has all angles zero, and both use the same slots s_(n+1,j). There F=(n+1)t+d_n for one constant d_n. Both formulas coincide on a full annular neighborhood with

    exp(-d_n)sum_j z_j^(n+1)e_(s_(n+1,j)).

Thus every derivative matches across every stage join, and the inequality also holds there. Within a stage the formula is a finite sum of smooth functions, including every transfer endpoint.

For each fixed real multi-index alpha with |alpha|=m, differentiation and the product rule give

    |D^alpha Q_(n,j)|<=K_(m,k)(n+1)^m r^(-m).

A derivative of order a of r^(-n) contributes at most K_(a,k)(n+1)^a r^(-n-a); a derivative of order b of z_j^n contributes at most a constant times (n+1)^b r^(n-b), or vanishes when b>n. This proves the bound uniformly in n and direction. Derivatives of t of order a>=1 are O(r^(-a)), the cutoff derivatives are uniformly bounded, and the slot vectors have norm one regardless of n. The chain and product rules therefore yield

    |D^alpha u|<=A_m(1+t)^B_m exp(-F(t)+mt).

For every p>0, the ratio of this bound to r^p tends to zero: F has a positive quadratic leading term in t, whereas (m+p)t and B_m log(1+t) are lower order. This is uniform over all annuli and directions.

Extend u and all punctured derivatives by zero at the origin. Each extension is continuous and is o(r), hence Frechet differentiable at zero with zero derivative. Induction identifies the extensions as the actual derivatives. This proves a smooth flat map, not merely a flat function value. The same uniform estimates give infinite-order local L^q flatness for every finite q>0.

## 6. Coefficient norm, sharpness and limitations

For d=2k, let v_d be the real unit-ball volume, and set b(z)=C/|z| off zero and b(0)=0. On B_R,

    measure{b>lambda}=v_d min(R,C/lambda)^d.

Its weak-L^d quasinorm sup_lambda lambda measure{b>lambda}^(1/d) is C v_d^(1/d), and its high-tail limit is v_d C^d. The inequality also holds at the origin because u and its first derivatives vanish. Arbitrary finite weak-L^d coefficients therefore do not imply vector continuation for these target dimensions. This is not an arbitrarily small coefficient example.

The independently confirmed endpoint theorem LIT354, A2977, gives continuation at C=1/4 under its distributional L1 equation, complete-array norm and infinite-order L1 integral flatness hypotheses, for all finite source and target dimensions. The present maps meet those regularity and flatness hypotheses. Combining the two results gives sharp inverse-radius threshold 1/4 for each k and each prescribed N>=k+1. The construction itself does not depend on that endpoint theorem.

No conclusion for N<=k, higher-dimensional logarithmic sharpness, scalar continuation, an Euler carrier quotient or the rotating Euler conjecture follows. In particular, a smooth complex vector map satisfying this inequality has not been made into a real divergence-free Euler profile.

## 7. Audit status and evidence

The submitted proof 340aeee3ff4fb0a1e2c5ebba75682ce5dfaa26ffbddf6c1dbe2b1c2416e7430d was read completely, together with its plan and all 42 author checks. Sections 1-6 above independently reconstruct the argument. The existing configured model comparisons are now checked in Sections 8-9. Actual provider execution is independently unattested. No numerical or symbolic computation is used in this proof.


## 8. Existing C comparison and exact scope of its diagnostics

The complete Theory Agent C  comparison of 2026-11-04T06:18:28Z was read, including all eight analytical items and its diagnostic qualifications. Its interval arithmetic, cyclic slot update, noncancellation, Holder ratio, full-array identity, half-slope decomposition, seam and origin arguments agree with Sections 1-6. The source leaves the change from a tau derivative to a t derivative implicit; our Section 3 explicitly gives dot(theta)=theta'(tau)/L. This is a notation clarification, not a missing estimate. The final C script and its complete retained log were read without execution.

The log records 28 passing checks: eight symbolic checks, seven exact checks, five negative controls and eight numerical samples. Six of the seven exact checks use only finitely many integer or rational samples. The slot computations cover all stages for each tested k between 1 and 10 by the verified period k+1, but do not computationally cover every k. The symbolic radial calculation is made in C^3; the symbolic flatness limit uses one logarithmic polynomial exponent. The corresponding general statements follow analytically above. Four negative controls are exact and one is numerical. The example 45/41 shows that the stated all-times bound for W cannot discard its dimension factor; it does not prove optimality of a bound restricted to an actively changing angle.

The numerical samples use 60-decimal-digit arithmetic at 14 and 18 points for the two tested configurations. They include coordinate-axis directions, zero coordinates, transfer interiors, gaps and two seam radii. The cutoff derivative supremum is estimated by a grid and enlarged by 1.02, without certification. No finite-difference identity, sampled ratio, sampled seam or this grid supremum is a proof premise. The general construction uses the true finite maximum of the cutoff derivative. The retained C log is reported as its first run; no earlier C run is asserted as independent evidence.

## 9. Coordinator comparison and repaired diagnostic history

The full coordinator comparison, first saved at 2026-11-04T06:15:06Z and amended at 06:15:44Z, was read. Its nine analytical items and five remarks agree with Sections 1-6, including the explicit division by L and the precise fixed-target sharpness statement. The suggested report replacement by N>=k+1, with N<=k excluded, has the correct scope when it cites this construction and A2977 separately.

The final coordinator script, all three retained logs and both complete source diffs were read without execution. The final log records nine passes. One is a finite exact integer check of slot permutations; the remaining checks use numerical directions, grids, quadrature or finite differences. Calling all nine numerical samples in the note is conservative about their proof status, but the first has this more specific classification. The finite-difference test uses L=1, for which the identity and preliminary bound are valid but the final chosen-C premise need not hold. A separate cylinder test uses large L and C=0.26 without constructing underflowing radii. The derivative maximum is again sampled, not a certified supremum. The final log retains two quadrature roundoff warnings.

The first script could create the zero direction, divided diagnostic errors by a derivative norm which vanishes on a plateau, and indexed the slot pair incorrectly in the seam check. It also contained a vacuous norm comparison and an algebraically zero summand. The second revision corrects the derivative normalization and slot index, removes the vacuous comparison and zero summand, and adds the cylinder test; it still allows simultaneous coordinate zeroings to remove the whole direction. The final revision replaces that zero direction by a unit coordinate. The two complete diffs substantiate this history; no unavailable earlier source is assumed. The first log has three explicit failures followed by the index error; the second has one failure; the final has none. Warning paths were normalized to relative agent paths in the retained copies, and both hashes are recorded. These diagnostics neither prove nor invalidate the independent analytic construction.

The actual model configuration for these existing collaborators is model; provider execution remains independently unattested. No new model client, agent, numerical job or formal build was used here. The construction and its endpoint comparison do not establish any Euler profile theorem.


## 10. Confirmation revision of the source

The source revision a68237f563578915ecf59f0366abb545ffc127102856f329bdfd19ee79508db3 was compared in full with the submitted source, and every changed passage was read. Its construction is unchanged. The new derivative sentence explicitly writes dot(theta_(n,j))=theta_j'(tau)/L, the factor already used in Sections 3 and 8 of this audit. It is a clarification of the chain rule, not a new estimate.

The status and separately dependent endpoint corollary accurately record A3011-A3013 and A2977. The new final section distinguishes the literature agent's reading of the two comparisons from any reading or execution of their scripts. Its fixed-target, logarithmic, scalar and Euler limitations remain correct. No new theorem or diagnostic is introduced.
