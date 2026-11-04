# Vanishing high tails and finite-regularity continuation

This is the independent audit of LIT346. Its small-disc continuation input is the confirmed A2900, proved in the preceding audit. The present deductions are elementary, but their strict threshold, germ hypothesis and coordinate dependence matter. At initial writing the independent reconstruction is complete; the existing configured model comparison is pending. No new computation or formalization is needed.

## 1. Definitions and the exact input

Let D be a bounded open disc in the complex plane, and let b be nonnegative, measurable and finite almost everywhere. Write

    mu_D(t) = area({z in D : b(z) > t}),
    M_D = sup_(t>0) t sqrt(mu_D(t)),
    T_D = lim_(T->infinity) sup_(t>=T) t^2 mu_D(t).

The last limit exists in the extended nonnegative reals, since the supremum decreases with T. In this audit b is locally weak-L2, meaning M_D is finite on every relatively compact disc under consideration. Thus T_D is finite. The condition T_D=0 is called vanishing high tails.

Fix an integer n>=1. The input A2900 states that, if f belongs to C^n(D;C), satisfies

    |dbar f| <= b |f| almost everywhere,  dbar = (partial_x+i partial_y)/2,
    M_D <= n sqrt(pi)/2,

then f is identically zero on D or every zero is isolated and has finite integral order. The last phrase means that for each zero a there are C>0, r0>0 and a finite real N with

    integral_(B(a,r)) |f|^2 dA >= C r^N,  0<r<r0.

Integral infinite order means that the integral divided by r^L tends to zero for every L>0. A nonzero Taylor jet is not asserted by finite integral order at fixed C^n regularity. The proof below imports the entire closed-threshold input, not a conclusion for arbitrary M_D.

## 2. Distribution split

For a measurable E contained in D, define mu_E and M_E by restriction. For every T>0,

    M_E^2 <= max(T^2 area(E), sup_(t>T) t^2 mu_D(t)).

Indeed, the terms with t<=T are bounded by T^2 area(E), and the terms with t>T are bounded by the second supremum. These two ranges exhaust t>0.

If E_j are measurable subsets of D with area(E_j)->0, taking limsup first with T fixed gives

    limsup_j M_(E_j)^2 <= sup_(t>T) t^2 mu_D(t).

Letting T tend to infinity proves limsup M_(E_j)^2<=T_D. The version with t>T has the same decreasing limit as the version with t>=T: they bound each other after shifting T by any fixed positive amount. In particular, for discs centered at an interior point a,

    limsup_(r->0) M_(B(a,r))^2 <= T_D.

This argument does not assume absolute continuity of the weak-L2 norm. That property is false for general weak-L2 functions.

## 3. Local and connected-domain continuation

Let O be connected and open, let f belong to C^n(O;C), and assume the differential inequality and local weak-L2 membership. Suppose each a in O has a relatively compact disc D about a with

    T_D < pi n^2/4.

Choose lambda strictly between these two numbers. A sufficiently large T makes the high-level supremum in Section 2 smaller than lambda. A sufficiently small disc B(a,r) inside D also satisfies T^2 pi r^2<lambda. Consequently M_(B(a,r))<n sqrt(pi)/2, and A2900 applies.

Let Z_open consist of points with an identically zero neighborhood. It is open. If a lies in its relative closure in O, choose the small disc from the preceding paragraph. That disc contains a nonempty open subset of Z_open. The alternative that its zeros are all isolated is therefore impossible. The function is identically zero on the disc and a belongs to Z_open. Thus Z_open is also closed. Connectedness gives Z_open empty or O.

If it is O, f=0. Otherwise every local application of A2900 is nontrivial, and every zero is isolated with the stated finite integral order. This proves LIT346's scalar theorem. A vanishing-tail coefficient satisfies the strict inequality for every integer n>=1, including n=1, regardless of the original disc norm.

## 4. Necessary concentration at a nontrivial zero germ

Now fix a disc D with finite M_D, and assume a is a zero of f. Assume also that f is not identically zero on any neighborhood of a. If a is nonisolated in the zero set, or if f has infinite integral order at a, then every sufficiently small disc B(a,r) contained in D must satisfy

    M_(B(a,r)) > n sqrt(pi)/2.

A contrary disc would contradict A2900: its trivial alternative is excluded by the germ hypothesis, and its nontrivial alternative supplies both isolation and finite integral order.

The quantities M_(B(a,r)) decrease as r decreases, so their limit exists. The strict inequality for each r yields the possibly nonstrict limit bound

    lim_(r->0) M_(B(a,r))^2 >= pi n^2/4.

For every disc D' containing a with closure inside D, Section 2 bounds this limit from above by T_(D'). Hence T_(D')>=pi n^2/4. The germ qualification cannot be dropped: the identically zero function satisfies the differential inequality with b=0.

## 5. L2 and finite Lorentz exponents

If b belongs to L2(D), then

    t^2 mu_D(t) <= integral_({b>t} intersect D) b^2 dA -> 0

by absolute continuity of its integrable square. Thus T_D=0.

More generally, assume for some 0<q<infinity that

    I_q = integral_0^infinity (t sqrt(mu_D(t)))^q dt/t < infinity.

For each t0>0, monotonicity of mu_D gives

    I_q >= (t0 sqrt(mu_D(t0))/2)^q log 2.

This bounds M_D by 2(I_q/log 2)^(1/q). If T_D were positive, one could find epsilon>0 and arbitrarily large t_j with t_j sqrt(mu_D(t_j))>=epsilon. Passing to a subsequence with t_(j+1)>2t_j makes the intervals [t_j/2,t_j] disjoint. Each contributes at least (epsilon/2)^q log 2 to I_q, a contradiction. Thus T_D=0.

This proves the assertion for every finite-q L^(2,q) class under the displayed distribution-function convention. It also covers 0<q<1: no triangle inequality or Banach-space assertion is used. Local membership means the argument is applied on relatively compact discs.

## 6. The strict non-L2 example and the inverse-radius contrast

On 0<|z|<exp(-1), set

    b(z) = 1/(|z| sqrt(log(1/|z|))),

and give b any finite value at the origin. With r=|z| and s=log(1/r)>=1, the derivative of log b with respect to r is (-1+1/(2s))/r<0. Therefore its superlevel sets are centered discs. Above the boundary value, their radius r_t satisfies

    t r_t sqrt(log(1/r_t)) = 1,
    t^2 mu(t) = pi/log(1/r_t) -> 0.

On the whole disc, the supremum equals pi: below the boundary value it is bounded by that value, and above it the last expression is at most pi with equality in the limiting boundary case. Thus M=sqrt(pi). On a disc of radius R<=exp(-1), the same argument gives M^2=pi/log(1/R).

Nevertheless,

    integral b^2 dA = 2pi integral_1^infinity ds/s = infinity.

The coefficient is not L2 near zero, but has vanishing high tails. Its whole-disc norm exceeds the n=1 threshold; sufficiently small discs meet that threshold. Away from zero it is locally bounded.

For C>0, the coefficient C/|z| instead has

    mu_(D_R)(t) = pi min(R^2,C^2/t^2),  T_(D_R)=pi C^2.

Its local weak norm does not shrink. The strict tail criterion covers C<n/2 only. This does not claim failure at equality, since A2900 itself covers C<=n/2 on centered discs. Nor does it dispute the stronger special inverse-radius theorem in Pan-Zhang for scalar H1 functions. That theorem concerns additional structure of the majorant, rather than all weak-L2 coefficients of the same norm.

## 7. Coordinate changes and bounded terms

Let chi be a C1 diffeomorphism on the relevant compact coordinate neighborhood, with absolute Jacobian determinant at most J. For b_tilde=b composed with chi inverse,

    mu_(chi(D),b_tilde)(t) <= J mu_(D,b)(t).

Thus T_(chi(D),b_tilde)<=J T_(D,b). If instead

    0 <= b_tilde <= K0+K1 b composed with chi inverse,

with finite nonnegative K0,K1, then for K1>0 and t>K0 the corresponding superlevel set is contained in the pullback of {b>(t-K0)/K1}. On writing u=(t-K0)/K1 and taking the high-tail limit, this yields

    T_(chi(D),b_tilde) <= J K1^2 T_(D,b).

For K1=0 the transformed coefficient is bounded and its tail is zero. The same inequalities give local weak-L2 membership; low t are controlled by the finite coordinate area. In particular, zero tail is preserved. A nonzero numerical threshold is not claimed to be invariant under arbitrary coordinate changes.

## 8. Exact conditional carrier consequence

Fix 0<c<1/2 and any finite real omega. Let J be the fixed rotation generator, A=cI-omega J, L=(1-c)I+omega J, and X(x)=Ax. On an ambient neighborhood of a point x0!=0, assume a C1 vector field V satisfies

    div V=0,  X dot V=0,  (X dot grad)V=-LV.

Choose a smooth transverse section through x0. Assume a nonnegative finite almost everywhere majorant B on that section satisfies

    |(curl V) dot X| <= B |V|

almost everywhere, with local weak-L2 membership and vanishing high tails. Assume V restricted to the section vanishes to every pointwise order at x0.

The confirmed C67 pre-continuation reduction, whose first-derivative nature was separately checked in A2901, gives smooth fixed local coordinates and an invertible smooth dependent-variable transformation taking V to a complex C1 scalar f. Its inequality has the actual coefficient

    |dbar f| <= b |f|,  b(z)=C1+C2 B(chi inverse(z)).

Here C1 and C2 are finite nonnegative local constants. The coordinate maps are smooth with bounded derivatives and inverse derivatives on smaller compact charts. They preserve pointwise infinite order and, by area comparison, imply integral infinite order for f. Section 7 gives vanishing tails for b. Section 3 with n=1 then implies f=0 on a smaller section.

The transport equation along the linear X-flow gives, for times and points remaining in the ambient neighborhood,

    V(exp(tA)x)=exp(-tL)V(x).

Since A is invertible and x0!=0, X(x0)!=0. The transverse flow map has invertible derivative at (0,x0), and its image contains an ambient neighborhood. Vanishing on the section therefore gives ambient vanishing. Only finite local times are used; no global completeness or boundary behavior is assumed.

The conclusion holds for every fixed finite omega, with constants and neighborhoods allowed to depend on it. The input B bound is not derived from the Euler hypotheses.

## 9. Verification and limits

All five source sections and all twenty supplied manual checks have been read. The source and checks are retained with their hashes in `verification`. This audit uses no numerical approximation, optimization, formalization or new model client. Existing configured model comparison is requested through the permitted working files; provider execution is not independently attested.

The equality T_D=pi n^2/4, the optimal continuation threshold, general arbitrary-norm weak-L2 continuation at fixed C1 or C2 regularity, general Sobolev versions, the required Euler quotient estimate and unrestricted rotating-profile nonexistence remain open here. This result does not add a conclusion to the already settled smooth full common-flat case.

## 10. Existing model comparison and independent response

The complete Theory Agent C note of 2026-11-04T04:34:34Z was read and retained. This is the existing configured model comparison, with actual provider execution independently unattested. Its first three items cover the full submitted proof. The distribution split, strict choice of an intermediate tail constant, connected propagation, finite-q Lorentz argument and coordinate transformation agree with Sections2-8 above. The note's radial example has exact truncated integral 2pi log(log(1/epsilon)) on epsilon<r<1/e and squared norm pi/log(1/R) on the disc of radius R<=1/e. Thus the closed C1 input applies on that disc for R<=exp(-4). The original whole-disc norm need not be small.

The suggested clarification is adopted in this independent statement: vanishing tails for the carrier coefficient means T_D(B)=0 on each relatively compact coordinate disc in the section. It is invariant under the bounded local changes in Section7; no chart-independent positive threshold is claimed. The source citation to Pan-Zhang is not needed for this deduction. The comparison's script counts and sampled tests are reported evidence only: they were not read or rerun for this verdict. The mathematical agreement rests on the explicit proofs here.

## 11. Confirmed-source revision check

The exact source revision945d86debdb66b9e82b97dcda81c06cd13054143a3368b805854632a430c5827 was compared with the submitted source in full. The only changes update the designated status and LIT345 dependency, retain the original submission record, and add the confirmation note with the explicit local-disc definition of vanishing tails. These agree with A2918-A2919 and Section10. No equation or hypothesis is weakened, and no diagnostic count is promoted to proof.


## 12. Correction of the previous section's exact-hash attribution

The preceding section and A2928 quoted the earlier announced hash 945d86debdb66b9e82b97dcda81c06cd13054143a3368b805854632a430c5827. The actual source retained at04:45:35Z and compared with the submission already had hash 723eda3d4af4899282baed8e1eced06a84bd0718e26234b2716d039ea38eac73, as its unchanged capture JSON proves. Thus the attribution of that exact earlier hash to that earlier file inspection was inaccurate. It does not affect the mathematics.

The earlier version has now been retrieved from the literature agent's archived04:45:25Z handoff, copied into verification, and hashed independently. The complete difference between it and the retained version is one heading: 10 C becomes 6. There is no other change. Both versions therefore preserve the same statements and proofs, and the earlier announced version is now directly checked as well. The earlier reading must not be backdated. The current live file is byte-identical to the version actually retained at04:45:35Z. The full original-to-retained difference and this one-heading difference have both been read.
