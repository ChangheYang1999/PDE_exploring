# The Bernoulli coefficient in scattering coordinates

## Exact statement

Let 2/5<c<1/2, omega be any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, a=1-2c, k=(1-c)/c, and eta=k-1=a/c. Thus 1<k<3/2 and 0<eta<1/2. Suppose U is a real C2 vector field and P is C1 on R3, with

    div U=0,
    (1-c)U+(Ay+U).grad U+omega JU+grad P=0.

Assume U is bounded, U(R .)->0 in distributions as R->infinity, and

    integral_1^infinity m(r) dr/r < infinity,
    m(r)=sup_(|y|>=r)||DU(y)||.

Choose the unique L2 representative P0 of the canonical pressure. It exists under these hypotheses, as proved below. Put B=Ay+U, q=|U|^2/2 and H=P0+q+Ay.U. Let Phi be the complete B flow, S its scattering map, and C=S^(-1)({0}) its compact null forward-trapped set. The use of C here avoids confusing the trapped set with the scalar coefficient K. Let V and W be the velocity and vorticity tails from A210, so W=curl V in distributions and

    V(exp(tA)z)=exp(-(1-c)t)exp(-omega tJ)V(z),
    W(exp(tA)z)=exp(-t)exp(-omega tJ)W(z).

Define b(z)=(Az).V(z) for z!=0, and b1=b restricted to S2. Then:

1. H(y)=O(|y|^(-eta)) uniformly at infinity, in particular H(y)->0.
2. For every x outside C the following integral converges absolutely:

       H(x)=a integral_0^infinity (U.B)(Phi_t x)dt.

   At every such point, locally uniformly in x outside C,

       exp(at)(U.B)(Phi_t x)->b(Sx),
       exp(at)H(Phi_t x)->b(Sx).

3. The coefficient of A288 has the representative K=b composed with S on R3 minus C. It is C1 there, obeys K(Phi_t x)=exp(-at)K(x) for all real t, and

       Omega.K=-a (V.W) composed with S,
       Omega=curl U.

   No boundedness, continuity, or value of K on C is asserted.
4. Put pcrit=3/eta=3c/a. For every finite 1<=p<pcrit and R>0,

       integral_(S^(-1)(B_R)) |K|^p
          = R^(3-p eta)/(3-p eta) integral_S2 |b1|^p.

   The value assigned to K on C is immaterial. In particular K belongs to every local Lp below pcrit. If b1 is nonzero, K fails local Lp at every p>=pcrit on any open neighborhood of the entire C. More precisely, for every lambda>0,

       |{x: |K(x)|>lambda}|
          = (1/3) lambda^(-pcrit) integral_S2 |b1|^pcrit.

   Thus K belongs globally to weak Lpcrit; its distribution formula is exact. If b1=0, then K=0 almost everywhere instead. This is a conditional sharpening of A292, using the Dini hypothesis.

The pointwise part of this theorem audits Theory Agent A C28, which was still explicitly an unsubmitted sketch when read. Parts 2 through 4 also identify and analyze the previously audited coefficient. This is not an exclusion theorem.

## Dependencies and canonical pressure

A209 gives completeness, S_*Leb=Leb, the C1 volume-preserving diffeomorphism S:R3 minus C -> R3 minus {0}, DS B=A S, and DS Omega=W composed with S. A210 gives continuous V,W away from zero and the uniform bounds

    U=V+o(r^-k), Omega=W+o(r^(-k-1)),
    |U|<=Cr^-k, |Omega|<=Cr^(-k-1), r>=1.

In particular U decays uniformly and belongs to L4(R3), since 4k>3 and U is bounded on compact sets. Each U_i U_j belongs to L2. The L2 double-Riesz pressure P0=sum R_i R_j(U_i U_j) exists, is unique as an L2 function, and has the same gradient as P by A031. Since P is C1, P0 has its corresponding C1 representative after changing by the determined constant. No unproved pointwise Riesz bound is used.

The exact Lamb identity is

    a U+grad H=B cross Omega.

Consequently grad H=O(r^-k). Along each radial ray this bound is integrable, and the distance from H(Rw) to its radial limit is at most C R^(1-k), uniformly in w. Any two points on the radius-R sphere can be joined by a spherical arc of length at most pi R, so its H oscillation is at most C R^(1-k). Thus all radial limits agree in one constant Hinf and H-Hinf=O(r^(1-k)) uniformly. Since q+Ay.U tends to zero, P0 tends uniformly to Hinf. Its L2 integrability forces Hinf=0. This proves part 1, including the claimed rate.

## Orbit integral and pointwise coefficient

Write M=sup|U|. A209 gives

    |Phi_t x-exp(tA)Sx|<=M/c, t>=0.

For x outside C, let z=Sx!=0. Therefore |Phi_t x| is comparable to exp(ct)|z| for all sufficiently large t and tends to infinity. The comparison is uniform for x in any compact subset of R3 minus C. Since |U.B|(y)<=C|y|^(1-k) outside a ball, its absolute future integral converges. Dot the Lamb identity with B and integrate BH=-a U.B up to time T. The terminal H(Phi_T x) tends to zero by part 1. This proves the integral formula without omitting an endpoint.

Set y_t=Phi_t x. Exact tail homogeneity gives

    (A exp(tA)z).V(exp(tA)z)=exp(-at)b(z).

To replace exp(tA)z by y_t, apply exp(-tA) to both arguments. Their difference is at most (M/c)exp(-ct), and the rescaled arguments lie in a fixed compact annulus. Uniform continuity of V there implies

    V(y_t)-V(exp(tA)z)=o(exp(-(1-c)t)).

The remaining linear-factor error is O(exp(-(1-c)t)), while the product of A y_t and the displayed velocity error is o(exp(-at)). The uniform tail remainder U-V gives the same little-o bound after multiplication by A y_t. Finally |U(y_t)|^2=O(exp(-2(1-c)t))=o(exp(-at)). Hence exp(at)(U.B)(Phi_t x)->b(z), locally uniformly on the escaping region.

Let g(t)=(U.B)(Phi_t x). The proven integral formula also holds starting at Phi_t x:

    exp(at)H(Phi_t x)
       =a integral_0^infinity exp(-ar) [exp(a(t+r))g(t+r)] dr.

The bracketed factor tends to b(z) and is uniformly bounded for large t. Dominated convergence gives the same limit b(z), including local uniformity. The independent measurable coefficient of A288 agrees almost everywhere with this pointwise limit because both are defined by that same limit. Its full-measure absolute-integral domain is not needed to assign the present representative outside C.

## C1 regularity and directional derivative

The distributional linear Lamb identity for the tail is

    a V=Az cross W-grad b.

It follows either by the ordinary vector identity applied distributionally to the linear profile equation for V, or by the Cartan calculation verified in A211. Both V and W are continuous away from zero, so the displayed distributional gradient is continuous. A continuous function with continuous distributional first derivatives is C1; local mollification proves this assertion. Thus b is C1 and K=b composed with S is C1 outside C. Its exact homogeneity is b(exp(tA)z)=exp(-at)b(z), proving covariance. Finally,

    Omega.K=(DS Omega).grad b(Sx)
            =W(Sx).[(ASx) cross W(Sx)-a V(Sx)]
            =-a(V.W)(Sx).

This is a derivative only on R3 minus C. It supplies no distributional or integrable derivative across C.

## Exact integrability and distribution function

For r>0 write t=log(r)/c. Since exp(tA) is radius dilation by r followed by a rotation, homogeneity and rotational invariance of surface measure give

    integral_S2 |b(rw)|^p dA(w)
       =r^(-p eta) integral_S2 |b1(w)|^p dA(w).

Change variables through the volume-preserving S and integrate in radius. For p<pcrit this is exactly the finite integral in part 4. Every bounded set is contained in S^(-1)(B_R) for some R, so local Lp follows. If b1 is nonzero it is nonzero on an open spherical patch, and the radial integral diverges at zero for p>=pcrit.

If N is any open neighborhood of C, then S^(-1)(B_epsilon) is contained in N for some epsilon>0. Otherwise points x_n outside N with Sx_n->0 have a convergent subsequence by properness of S; its limit would lie in C and outside N, a contradiction. Thus the preceding divergence occurs inside every such N.

For the global distribution function, use twisted polar coordinates, or rotate each radius sphere before integrating. For each w the inequality r^-eta |b1(w)|>lambda holds for 0<r<( |b1(w)|/lambda )^(1/eta). Tonelli and the radial volume element r^2 dr give the exact expression in part 4. The null set C contributes no volume. This proves the weak endpoint and its coefficient without a qualitative comparison argument.

## Scope

Constants may depend on the profile, c and omega; no bound uniform in omega is asserted or needed. Every finite omega is covered. The Dini hypothesis is additional to the original prompt. The improved scalar endpoint information can coexist with nonzero formal linear tails, as the adjacent zero_bernoulli_tail result shows. That construction is not an Euler profile and does not refute a future theorem that K=0 forces actual U=0. No computation, formalization, build or extra model client was used. A focused continuing configured-model review is requested through the existing working files; no unreceived response is treated as evidence.


## CO23 cross-check and angular qualification

Audit A300-A301, 2026-11-03T00:17:02Z. Coordinator Proposition24.1 and Corollary24.2 agree with the preceding theorem. Their endpoint c=2/5 is also valid: the same estimates have k=3/2, eta=1/2 and all necessary strict inequalities k>1, 4k>3. In addition A210 already excludes a nonzero profile at that endpoint. The local Lp equivalence is valid for every finite p>=1, with local integrability failing at and above pcrit unless b vanishes. The source step(i) needs radial comparability only for sufficiently large t, not every t>=0; an escaping point may itself be the origin. This change does not affect any limit.

The equivalent zero condition is

    b=0 iff aV=Az cross W iff c w.F(w)=omega(Jw).F(w) on S2.

The first equivalence follows from grad b=Az cross W-aV and homogeneity: a spatially constant homogeneous scalar of nonzero degree must vanish. The last equivalence follows by restricting to the unit sphere and using twisted homogeneity. The nonzero construction A297 satisfies these conditions for every omega; no nonlinear profile follows.

There is an essential twist in any POINTWISE angular formula. For z=rw and R_theta=exp(theta J),

    b(rw)=r^(-eta) b1(R_((omega/c)log r) w).

Indeed exp(A log(r)/c)=r R_(-(omega/c)log r), so this is the rearranged homogeneity identity. Consequently a sufficient criterion for unboundedness at a particular p in C is the existence of x_n->p outside C with

    |b1(R_((omega/c)log|Sx_n|) Sx_n/|Sx_n|)|>=delta>0.

The untwisted value b1(Sx_n/|Sx_n|) cannot be substituted without another argument. This is not an issue for integrated spherical formulas, because rotations preserve surface area. As a scalar illustration, take b1(w)=w1, w=e1 and omega!=0; radii tending to zero can make the twisted angle pi/2 modulo2pi. Then the untwisted value is1 but b(rw)=0. This illustrates the missing implication along that sequence; it is not an Euler counterexample or a disproof of every possible pointwise-core theorem. CO23 Remark4's stated per-core-point criterion is therefore OPEN as written. The preceding theorem deliberately asserts strong-Lp divergence on any neighborhood of the ENTIRE core, which needs no such angular hypothesis.

CO23 Remark2 also needs a scope qualification. Exact tail homogeneity prohibits integrability at or above pcrit for nonzero b. It does not prove that A292's smaller guaranteed range is optimal for actual Euler coefficients. Under Dini the present theorem itself improves that range to every p<pcrit. Without Dini the coefficient's precise tail representation has not been established here.

The source snapshot had headings00:40Z and00:45Z while the actual read and audit time was 2026-11-03T00:17:02Z. Those source labels must be corrected by their owner to real times; they are not evidence of future work. The mathematical verdict does not certify those labels.


## The local tail-Laplacian criterion

Audit A303, 2026-11-03T00:21:22Z. Let 1/3<c<1/2 and omega be finite, with A,a,k,eta as above; now 0<eta<1. Let V and W be continuous away from0, div V=0 and curl V=W in distributions, and suppose the linear tail equation and twisted homogeneity in the exact statement hold. Define b=(Az).V and

    sigma=2 omega W3+(Az).curl W

as a distribution on R3 minus0. Then

    Delta b=-sigma,
    sigma=0 iff b=0 iff aV=Az cross W.

The linear Lamb identity gives grad b=Az cross W-aV. Taking divergence yields Delta b=-2 omega W3-(Az).curl W. Thus b=0 implies sigma=0, and the equivalence with aV=Az cross W was already proved. To prove the converse from sigma=0, homogeneity first gives |b(z)|<=C|z|^-eta both near zero and at infinity.

Weyl's lemma makes b harmonic away from zero. The singularity is removable as a DISTRIBUTION because eta<1. For a compactly supported smooth phi and a cutoff chi_epsilon equal to0 on B_epsilon and1 outside B_(2epsilon), harmonicity gives integral b Delta(chi_epsilon phi)=0. The two cutoff derivative terms are bounded by C epsilon^(2-eta) and C epsilon^(1-eta). The missing term integral b(1-chi_epsilon)Delta phi is O(epsilon^(3-eta)). All vanish. Hence Delta b=0 globally. Weyl's lemma and the decay at infinity now imply b=0 by the harmonic Liouville theorem. This proves the criterion without a spherical-harmonic expansion or angular-mode truncation.

In the scattering theorem, the Lp equivalence of A300 extends to p=infinity. If b is nonzero on one compact annulus, its essential supremum on its backward-scaled annuli grows by exp(an). Volume preservation of S and its bounded displacement transfer this failure of local essential boundedness to K. If b=0, K=0 almost everywhere. This does not identify which individual core points have unbounded neighborhoods.

The sigma condition is additional. For every omega, the explicit rotation-covariant angular field

    F(w)=((2-k)/2)e3+(k/2)w3 w,
    V(rw)=r^-k F(w)

is divergence-free and solves the linear tail equation. Its spherical components are Fr=cos(theta), Ftheta=-(2-k)sin(theta)/2 and Fphi=0. The spherical divergence cancels (2-k)Fr. It has b=c r^-eta cos(theta), which is nonzero and not harmonic for 0<eta<1. Thus the linear equation does not imply sigma=0. Conversely A297 gives nonzero formal tails with sigma=0 for every omega. Neither construction is a smooth nonlinear profile.

Source revisions removed the original untwisted per-core-point assertion and no longer assert that A292 is an optimal Euler estimate. These repairs are accepted at their current mathematical scope. Step(i) must still use sufficiently large time T_y, because replacing t>=0 by t>=1 does not rule out an orbit passing through the origin at time2. The proof never needs a universal starting time. Recorded revision times should be real shell times; this audit date is 2026-11-03T00:21:22Z.
