# Ambient curve geometry for original-set capture

## Purpose and exact statements

The three elementary lemmas below justify the geometric steps of the conditional basin-coverage proposal without assigning the ambient subspace topology to a globally immersed Pesin leaf. They also weaken the required convergence of original image curves from C1 to uniform convergence. They do not construct any invariant measure or supply the finite-time reparametrization premise.

### 1. Tangency at almost every point of an incoming curve

Let L be the image of an injectively immersed C1 one-manifold in R3. Assume its domain is second countable. Let gamma:I->R3 be C1 on a compact interval, with gamma(I) contained in L. Then gamma'(s) is tangent to L at gamma(s) for Lebesgue-almost every s in I. The same assertion holds almost everywhere on a measurable subset E of I when only gamma(E) is contained in L. Consequently it holds at almost every point for any incoming measure absolutely continuous with respect to the arclength of gamma. Critical parameters with gamma'=0 contribute no arclength.

### 2. A fixed transverse plaque is met by uniformly close strips

Let F:O->R3 be C1 on a neighborhood O of (0,0) in R2, and sigma:J->R3 a C1 regular arc through sigma(0)=F(0,0). Suppose the three columns partial_1 F(0,0), partial_2 F(0,0), sigma'(0) are linearly independent. If continuous F_n converge uniformly to F on a fixed neighborhood of (0,0), then for all sufficiently large n, the image of F_n meets a fixed arbitrarily small open subarc of sigma around sigma(0). No derivative convergence of F_n is required.

### 3. A fixed fraction of a uniformly close curve enters a product set

Let H be a C1 diffeomorphism from an open rectangular box in R3, with coordinates (s,t,tau), onto an open subset of R3. Put gamma(s)=H(s,0,0). Let T be a compact positive-length subset of the interior of a compact s interval I. Suppose a measurable set E contains H(T times J times L) for open intervals J,L around zero.

Let gamma_n:I->R3 be C1 curves converging uniformly to gamma. Then, after reducing I around a density point of T and replacing T by a compact positive-length subset there if necessary, a fixed positive amount of arclength of gamma_n lies in E, for every sufficiently large n. If these arcs are restrictions of full curves with lengths bounded above by L0<infinity, a fixed positive fraction of the full lengths lies in E.

If the full curves are images g^(ell_n)(P_n) of original embedded arcs under a C1 diffeomorphism g, and the ratio of maximum to minimum arclength Jacobian on each P_n is at most D<infinity, the same assertion pulls back to a fixed positive fraction of each original P_n whenever E is invariant under g. If additionally length(P_n intersect F0)/length(P_n)->1, then F0 intersects E on a positive-length subset of P_n for all sufficiently large n.

## Proof of tangency

Cover the domain of L by countably many compact coordinate arcs whose images L_j are embedded C1 arcs. Every point of L is covered, and each L_j is compact in R3. The sets E_j={s in E: gamma(s) in L_j} are measurable. Almost every point of their union is a Lebesgue density point of one such E_j: apply the density theorem to each E_j and remove the countable union of exceptional null sets.

Fix such a parameter s in the interior of I. There are distinct s_n in E_j tending to s. Because L_j is an embedded compact arc, any limit of normalized secants between gamma(s_n) and gamma(s) lies in its tangent line at gamma(s). Equivalently, projecting onto the normal plane gives a quantity of size o(|gamma(s_n)-gamma(s)|). The C1 expansion of gamma then puts gamma'(s) in that tangent line. If gamma'(s)=0 the assertion is immediate. The tangent of the immersed leaf is well defined because its immersion is injective. This proves the lemma.

A full Pesin unstable leaf is an example of such a countably charted injectively immersed manifold. Hence an incoming arclength-absolutely-continuous measure supplies a generic regular point where the incoming curve is tangent to the unstable line. No assertion about a whole incoming arc being contained in a single intrinsic leaf chart is used.

## Proof of transverse persistence

Translate the common intersection to zero and define

    G(s,t,v)=F(s,t)-sigma(v).

Its derivative A0 at zero is invertible. On a sufficiently small closed three-dimensional ball of radius r in the parameter domain,

    |A0^(-1)G(z)-z|<=r/4.

This follows from differentiability at zero and G(0)=0. Uniform convergence gives, for sufficiently large n,

    |A0^(-1)(G_n(z)-G(z))|<=r/4,
    G_n(s,t,v)=F_n(s,t)-sigma(v),

on that whole ball. The continuous map z -> z-A0^(-1)G_n(z) therefore sends the closed radius-r ball into the radius-r/2 ball. Brouwer's fixed-point theorem gives z_n with G_n(z_n)=0. Reducing r initially places the resulting sigma coordinate in any prescribed open subarc. This proves the claim with only uniform convergence.

For the coverage proposal take F(s,t)=Psi_t(gamma(s)) and F_n(s,t)=Psi_t(gamma_n(s)). Uniform convergence of gamma_n and continuous dependence of the flow on a compact set give the required uniform strip convergence. At a regular point, the strip columns are the unstable direction and the carrier direction, while the fixed plaque is a strong stable arc. They are independent by the Oseledets splitting and the first lemma. If A201 puts that fixed plaque in {W=0}, and every original curve and its bounded carrier-time translates lie in {W!=0}, transverse persistence is an immediate contradiction.

## Proof of the arclength lower bound

Choose a density point of T in I. Shrink to a sufficiently small subinterval whose endpoints lie strictly to either side of a compact positive-length subset T1 of T. Work in a small Euclidean ball contained in the image of H, containing the central arc and all sufficiently late gamma_n arcs. The first coordinate pi of H^(-1) is Lipschitz on this ball, with some finite constant L1, after choosing the ball with compact closure in the chart. The remaining two coordinates of the close curves lie in J and L.

The continuous functions pi composed with gamma_n converge uniformly to s. Their endpoint values therefore bracket T1 for all large n. The intermediate value theorem gives

    pi(gamma_n(A_n))=T1,
    A_n={s: pi(gamma_n(s)) in T1}.

The sets A_n are compact. By the product-set hypothesis gamma_n(A_n) is contained in E. The elementary Lipschitz inequality for one-dimensional Hausdorff measure gives

    length(T1)<=L1 H1(gamma_n(A_n))
              <=L1 integral_(A_n)|gamma_n'(s)|ds.

The second inequality permits parametrization multiplicity. Thus at least length(T1)/L1 of image arclength belongs to E, uniformly in n. If the full image length is at most L0, its E fraction is at least delta=length(T1)/(L1 L0)>0. Oscillation or loss of monotonicity of the projected curves does not harm this bound.

For the pullback let j_min>0 and j_max<=D j_min be the extreme arclength Jacobians on P_n. If Q_n is the part mapped into E, then

    length(Q_n)>=length(g^(ell_n)Q_n)/j_max
                >=delta length(g^(ell_n)P_n)/j_max
                >=(delta/D)length(P_n).

Here the displayed image lengths are parametrized lengths, equal to ordinary arclength when the original arcs and images are embedded. Invariance of E identifies Q_n with P_n intersect E. Finally the F0 complement has relative length tending to zero, so it cannot contain this fixed positive fraction. For large n the intersection P_n intersect F0 intersect E has positive length.

## Application and limits

In the vortical component of the proposal, the map H(s,t,tau)=Gamma_tau(Psi_t gamma(s)) is a local C1 coordinate map at an arclength-typical regular point, by lemma 1 and independence of the unstable, carrier and W directions. Continuous-time genericity is preserved in the two extra coordinates by the bracket contraction. A compact positive-length set of generic s values gives exactly the product set required by lemma 3. The original-parent density and bounded distortion then give capture in the original starting set.

These lemmas validate geometric implications of explicit premises. They do not certify the original measured-curve construction, its invariant measure, noncollapse, entropy bound, selected mass, or source derivative estimates. They therefore do not resolve the OPEN status of the entire original-set coverage proposal. No computation or formalization was used. The standard elementary inputs are the Lebesgue density theorem, arclength and Hausdorff measure, continuous dependence for ODEs, and Brouwer's theorem.
