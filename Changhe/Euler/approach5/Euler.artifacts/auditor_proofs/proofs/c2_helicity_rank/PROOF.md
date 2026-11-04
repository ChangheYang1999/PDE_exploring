# The global helicity-free rank argument at C2

## Statement, hypotheses and dependencies

Let 0<c<1/2 and omega be any real number. Write Jy=(-y2,y1,0), A=cI-omega J, a=1-2c, kappa=1+c, B=Ay+U and W=curl U. Suppose U is C2 on R3, P is C1, div U=0, and

    (1-c)U+(B.grad)U+omega JU+grad P=0.

Assume U(y)=o(|y|) uniformly at infinity and U.W=0 everywhere. Set O={W!=0}, H=P+|U|^2/2+(Ay).U and G=BH. Then H and G are C2, and dG wedge dH=0 on O.

If O is dense, there is K in C2(R3), unique up to a constant, with dK=G dH and BK=G^2. On the support of every compactly supported invariant probability for the complete B flow, G=0. On the support of every such full-flow-ergodic probability, H is constant. For every y, G(Phi_s y) tends to zero as s tends to negative infinity.

Retain dense O for the following conclusions. Suppose a compactly supported, full-flow-ergodic vortical SRB probability nu for Psi_t=Phi_-t is GIVEN with the exact geometric properties of A207/A223: its spectrum is (a,0,-kappa), its flow and strong stable directions are R B and R W, its unstable conditional measures on local one-dimensional unstable arcs are equivalent to arclength with positive densities, and its basin agrees modulo spatial null sets with an open full-flow-invariant domain D_nu. Then H is constant on D_nu. If these domains cover almost every point of O, U=0. Because U=0 makes O empty, the last assertion excludes the simultaneous dense-O and coverage hypotheses. It does not construct those probabilities.

The proof uses the usual C2 Sard theorem for maps R3 to R2, elementary ODE and integration results, and the explicitly assumed given-basin geometry. It refines the C3 scope of A269. No bootstrap of U beyond C2 is claimed.

## 1. The extra derivative is supplied by the equation

The equation makes grad P C1 and hence P C2. Therefore H is C2. Direct expansion of the momentum equation gives

    a U+grad H=B cross W,       [B,W]=-kappa W.

The first equation dotted with B gives

    G=-a U.B.

Both factors on the right are C2, so G is C2. This is stronger than the generic regularity of a directional derivative of a C2 function. Dotting with W gives WH=0, and then

    WG=W(BH)=[W,B]H+B(WH)=kappa WH=0.

Only H C2 and W C1 are used in this commutator calculation.

## 2. Complete recurrent vortex flow without periodic orbits

Uniform sublinearity implies linear growth of B. Its locally unique flow Phi is complete. Since B(y).y=c|y|^2+U(y).y is positive outside a ball, backward trajectories from any compact set remain in a common compact ball. For epsilon>0 the radial differential inequality gives

    |Phi_s z|<=C_epsilon exp((c+epsilon)s)(1+|z|), s>=0.

The bracket identity gives

    D Phi_s W=exp(kappa s) W o Phi_s,
    Phi_s Gamma_t=Gamma_(exp(kappa s)t) Phi_s.

Here Gamma initially denotes a short local W flow. On a fixed compact backward trap it exists for a uniform short time, with images in a slightly larger compact set. For any prescribed t, pull the initial point back by s, run this short flow for exp(-kappa s)t, and push forward. Taking s comparable to log(1+|t|)/kappa proves completeness and, for every compact initial set Q,

    sup_(x in Q)|Gamma_t x|<=C_(Q,epsilon)(1+|t|)^((c+epsilon)/kappa).

Since div W=0, Gamma preserves volume. Choose epsilon with 3(c+epsilon)<kappa, possible exactly because c<1/2. If a bounded positive-volume set were wandering under Gamma_1, the first N iterates would have total volume proportional to N, but all lie in a ball of volume O(N^(3(c+epsilon)/kappa)), a contradiction. An unbounded wandering set would have a bounded positive-volume subset, so no positive-volume wandering set exists. The last-visit decomposition in a countable family of bounded open balls now proves almost-everywhere topological recurrence for Gamma_1.

A nonconstant periodic orbit of period T would, after backward carrier time s, give an orbit of period exp(-kappa s)T in a fixed convex compact ball. Let L bound ||DW|| on that ball. For a periodic solution z of period T', subtract its average zbar and use Wirtinger:

    integral |z'|^2=integral (W(z)-W(zbar)).z'
       <=L ||z-zbar||_2 ||z'||_2
       <=L T'/(2pi) ||z'||_2^2.

If L=0 this already excludes a nonconstant orbit; otherwise T'>=2pi/L. The shrinking periods are impossible.

## 3. Two first integrals cannot have rank two on O

Suppose F=(H,G) has rank two somewhere in O. Its rank-two vortical locus contains an open set of positive volume. By Sard, the global critical values of F have planar measure zero. In submersion charts, the inverse image of that null set also has spatial measure zero within the rank-two locus. Choose there a recurrent point whose F value is globally regular.

Its fiber is a closed embedded one-dimensional manifold. The nonzero W orbit stays in a connected component. A connected component is a line or a circle. On a line, or on an interval obtained by removing zeros from a circle, a nonzero complete orbit is strictly ordered and cannot recur. The regular-level chart near the starting point rules out an accumulation through other fiber sheets. A circle without a zero gives a forbidden periodic orbit. Every possibility contradicts recurrence. Thus dG wedge dH=0 on O.

## 4. Global primitive and compact invariant dynamics

If O is dense, continuity extends the rank identity to R3. The C1 form G dH is closed. Its explicit radial primitive is

    K(y)=integral_0^1 G(t y) grad H(t y).y dt.

Differentiating and using closedness gives dK=G dH, so K is C2 and BK=G^2. If mu is an invariant probability with compact support, differentiation of invariance on that compact invariant support gives

    integral G^2 dmu=integral BK dmu=0.

Continuity gives G=0 throughout the support. Thus H is constant along its B orbits. Full-flow ergodicity makes it a single constant almost everywhere, and continuity extends that value to the support.

Along a backward orbit, K is bounded on the compact orbit closure and nondecreasing in forward time. Hence

    integral_(-infinity)^0 G(Phi_s y)^2 ds<infinity.

The derivative BG is bounded on the same compact set. Thus G along the orbit is uniformly Lipschitz. Infinitely many values bounded away from zero at times tending to negative infinity would create disjoint intervals of uniformly positive square integral. This proves the asserted limit zero.

## 5. From the given SRB measure to its essential basin

Write H=h_nu on supp nu. The assumed positive unstable conditional densities provide local unstable arcs gamma with full-arclength subsets T of support points generic for nu. At a regular point, gamma', -B and W are independent. Therefore

    C(s,t,tau)=Gamma_tau(Psi_t gamma(s))

is a C1 diffeomorphism on a sufficiently small parameter box. If s belongs to T, the inner point remains on the invariant support and W preserves H. H=h_nu on a full-volume subset of the image V, hence everywhere on V by continuity.

For every real r the exact conjugacy is

    Psi_r C(s,t,tau)=Gamma_(tau exp(-kappa r)) Psi_(r+t) gamma(s).

For s in T the rightmost point stays on the support; completeness of Gamma permits the indicated shift. The same full-volume and continuity argument gives H=h_nu on Psi_r V. Union these boxes and their carrier translates over a family covering nu-almost every typical point. The resulting open invariant set E has full nu measure and H=h_nu everywhere. Second countability supplies countable subcovers when null sets are used.

Choose a nonnegative continuous compactly supported observable inside E with positive nu integral. Every basin point must enter E because its limiting time average of that observable is positive. Invariance gives Bas(nu) subset E. Since D_nu differs from the basin only by a spatial null set, continuity gives H=h_nu throughout D_nu.

## 6. The final constant-H implication at the stated growth

If the given domains cover almost every point of O, continuity gives grad H=0 on O. Dense O makes H constant globally. The Lamb equation then implies U.B=0, so

    H=P-|U|^2/2+U.B,       P=|U|^2/2+H.

Subtract the constant H from P and put q=|U|^2/2. Divergence of momentum gives

    partial_i partial_j(U_i U_j)+Delta q=0.

The skew rotation terms cancel exactly. For E(R)=integral_(|y|<R)|U|^2 and M_R=sup_(|y|=R)|U|, the energy equation and divergence theorem give

    c R E'(R)-(5c-2)E(R)=-2 integral_(|y|=R)|U|^2 U.n,
    (cR-2M_R)E'(R)<=(5c-2)E(R).

For large R the coefficient is positive. If c<2/5, U=0 follows immediately. At c=2/5, E is bounded. Above 2/5 choose epsilon>0 with epsilon<min(c/2,1-2c), and eventually M_R<=epsilon R. Then E(R)<=C R^p with p=(5c-2)/(c-2epsilon)<1. In both remaining cases E(2R)/R tends to zero.

Test the tensor equation with chi_R sqrt(1+|y|^2), where chi_R is one on the radius-R ball and zero outside radius 2R, with its first two derivatives O(R^-1), O(R^-2). Its Hessian main term is

    integral chi_R [U^T D2 sqrt(1+|y|^2) U
                         +q Delta sqrt(1+|y|^2)].

It is nonnegative and strictly positive wherever U is nonzero. The cutoff error is bounded by C E(2R)/R and tends to zero. On every fixed ball the main integral must vanish; hence U=0. This repeats A256 with all boundary terms explicit.

## Scope and verification

The basic rank identity requires neither dense O nor any invariant measure. Global primitive and support statements require dense O. Basin and final exclusion statements additionally require the specified measures and coverage. No conclusion about all C2 profiles follows without those hypotheses. In an open irrotational region WH=WG=0 is vacuous, so the proof cannot simply discard density. Source snapshot and its hash are retained alongside this independent reconstruction. No computation was needed.
