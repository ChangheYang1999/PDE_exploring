# Vortex smearing on regular supports and escape of typical vortex lines

Date: 2026-11-03T01:37:05Z. CONFIRMED A375 after focused configured-model review, literature-agent review and independent source and proof checking.

## Exact hypotheses and conclusions

Let U in C2(R3;R3), P in C1 solve the entire divergence-free rotating Euler profile equation with U tending uniformly to zero, 2/5<=c<1/2 and arbitrary finite omega. Put B=(cI-omega J)y+U, Omega=curl U, a=1-2c, kappa=1+c, d=3c and beta=5-2/c. Let Phi, Psi_t=Phi_-t and Gamma be the complete carrier, backward-carrier and vortex flows. Let H0=P_can+|U|2/2+((cI-omega J)y).U, with the canonical pressure fixed by A031/A277.

Let nu be a compactly supported full-carrier-flow-invariant probability with nu-almost-everywhere backward spectrum (a,0,-kappa), with directions E^u,span(B),span(Omega), and absolutely continuous conditional probabilities on full unstable plaques. These are given-measure hypotheses at C2; no measure-existence theorem at C2 is asserted. Define m_T=(2T)^-1 integral_(-T)^T (Gamma_s)_*nu ds. By A374, each m_T has an L1 density and nu-almost every starting point is two-sided recurrent for Gamma.

Sections1-2 prove exact covariance and that nu-almost every vortex semiorbit is also unbounded. Section3 gives an explicit sufficient uniform-plaque condition for bounded smear densities. Section4 proves that condition if the actual support K=supp nu avoids both {B=0} and {Omega=0}. Under this additional compact regular-support hypothesis, Section5 proves a polynomial Bernoulli-square average and matching averaged occupation exponents on suitable sets. The regular-support hypothesis is not known for the general measures in A308.

## 1. Exact covariance of the smeared measures

For every T>0 and every real t, carrier-vortex commutation and carrier invariance of nu give

    (Phi_t)_*m_T = m_(T exp(kappa t)).                  (1)

This is an identity of measures, first checked against bounded Borel functions. It uses no Bernoulli or density hypothesis. If m_1 has density rho_1, put S=exp(kappa t). Since det D Phi_t=exp(dt), change of variables in(1) gives

    rho_S(Phi_t y)=exp(-dt) rho_1(y) a.e.,
    ||rho_S||_q=S^(-(d/kappa)(1-1/q)) ||rho_1||_q,      (2)

whenever the indicated norm is finite, including q=1 and q=infinity.

Absolute continuity alone already implies, for every finite-volume measurable Q,

    m_S(Q)=m_1(Phi_-t Q) ->0 as S->infinity.            (3)

Indeed |Phi_-t Q|=exp(-dt)|Q| tends to0. Absolute continuity of the integral of the single L1 density rho_1 makes its integral on ANY sets with these shrinking volumes tend to0. The sets need not be bounded or nested. Thus the average over nu of the fraction of vortex time in Q tends to0.

## 2. Recurrence and unboundedness for nu-almost every starting point

The main proof transfers two-sided topological recurrence from ambient volume to nu. Combine it with(3). For a fixed integer R>0 let E_R^+ consist of starting points z whose entire positive vortex semiorbit stays in the closed ball of radius R. This is a closed set: it is the intersection, over nonnegative rational s, of the closed sets Gamma_s^-1(closed B_R). Continuity makes rational-time testing sufficient. For every S>0,

    m_S(closed B_R) >= nu(E_R^+)/2.

The positive half of the averaging interval supplies this inequality. By(3), nu(E_R^+)=0. The union over R contains all bounded positive semiorbits. The same argument with negative time treats bounded negative semiorbits. Consequently, for nu-almost every z, both vortex semiorbits are unbounded, and each returns arbitrarily close to z along unbounded sequences of times.

Continuity on finite time intervals shows that unboundedness of a semiorbit is equivalent here to limsup of its radius being infinity along that time direction. No individual occupation rate or vortex ergodicity is inferred. This conclusion concerns nu-typical starting points, not every point of the carrier support.

## 3. An explicit uniform-plaque criterion for bounded smear density

The following geometric criterion suffices for m_T to have a bounded density for each fixed T. Suppose supp nu is covered by finitely many measurable unstable boxes with these properties:

(i) Almost every conditional plaque in a box has a C1 parametrization gamma on a common bounded interval. Speeds, moduli of continuity of tangent vectors and the full-plaque lengths have uniform upper and positive lower bounds.
(ii) The plaques and fixed short carrier/vortex images stay in a compact regular set on which the three vectors gamma',B,Omega have determinant bounded away from0, uniformly over plaques and parameters.
(iii) Conditional densities on each full plaque are proportional to |alpha(gamma')|, where alpha=(B cross Omega).dy.

Choose short common carrier and vortex windows. For each plaque consider

    F_gamma(s,r,tau)=Gamma_tau Psi_r gamma(s).

The exact determinant is

    |det D F_gamma(s,r,tau)|
        =exp(ar)|alpha_gamma(s)(gamma'(s))|.            (4)

To check(4), pull back first by D Gamma_tau, which has determinant1, and then by D Psi_r, which has determinant exp(-dr). The three columns become gamma', -B and exp(kappa r)Omega. Their determinant has magnitude exp(kappa r)|alpha(gamma')|. This also checks the signs and shows that tau has no influence on the determinant.

Normalize the plaque conditional by Z_gamma=integral |alpha(gamma')| ds. On each injective parameter piece, its pushed density relative to volume is exactly exp(-ar)/Z_gamma, apart from the fixed averaging constants. Conditions(i)-(ii) give a positive lower bound for Z_gamma. Their determinant lower bound also gives the uniform least singular value needed for the next step. The uniform tangent modulus, determinant lower bound and compact flow derivatives allow subdivision of the fixed parameter box into a uniformly bounded number of pieces on each of which F_gamma is one-to-one with a uniform inverse bound. One direct construction subdivides until D F_gamma varies by less than half its uniform smallest singular value; on a convex subbox the integral along each line segment then gives injectivity and a lower Lipschitz bound. The change-of-variables formula makes the pushforward of each conditional times dr d tau have density bounded by one common constant. Integrating the transverse probability and summing the finite boxes proves the bound.

Overlaps cause no partition-length problem: cover nu by restrictions to the full boxes and dominate the original measure by their finite sum. Each restriction is disintegrated on its own full plaques; no arbitrary disjoint partition is used to shorten them. Full carrier invariance permits insertion of the carrier-time average exactly as in A374, equation(5).

This proves bounded density for a short vortex smear m_delta. A fixed longer interval [-T,T] is covered by finitely many translates of [-delta,delta]. The corresponding unnormalized smeared measures are vortex translates of 2delta m_delta and dominate 2T m_T. Vortex translations preserve volume and preserve the L-infinity norm of a density. Hence m_T has bounded density for every fixed T.

## 4. Compact regular supports meet the criterion

Assume now the actual support K=supp nu is compact and avoids both {B=0} and {Omega=0}. A056 proves that B cross Omega is nonzero throughout K and gives uniform hyperbolicity, with backward stable line span(Omega), center span(B), and a continuous unstable line transverse to them. Thus the determinant of the three unit directions has a positive lower bound on K. The local unstable manifold theorem on a compact uniformly hyperbolic set supplies uniform C1 plaque size and tangent control. The directly checked source is Dyatlov, Notes on hyperbolic dynamics, Theorem5 and equation(4.67); the required continuous C1 plaque dependence is the compactness and uniqueness reconstruction CONFIRMED A131. For the flow orientation, A056's forward stable line is the Psi-unstable line, and its exp(-at) bound gives expansion at least C^-1 exp(at) for Psi on that line. A207 identifies the conditionals with normalized alpha-length.

For precision about full plaques, positivity in A207 first puts a possibly short conditional interval through almost every point inside supp nu: a relatively open missing subarc would otherwise have positive conditional measure outside the closed support. To obtain a uniform interval, partition the typical points into measurable sets on which the contained interval has radius at least1/m. Backward recurrence for the invariant probability and the map Psi_1 gives, for almost every point in each such set, arbitrarily remote backward visits to the same set. Pushing its radius1/m intervals forward by these long Psi times expands unstable arclength at least C^-1 exp(an). The images remain in K by full invariance and contain the fixed local unstable interval about the original point once n is large. This proves that one common shortened local unstable radius lies in K at almost every base point. It uses recurrence, not an a priori lower bound on the original measurable partition atoms, and does not require ergodicity. The typical set is dense in K; continuous dependence of the uniform local unstable plaques and closedness of K extend the inclusion to every point of K.

The change from the original subordinate partition to full box plaques preserves this conditional formula. Ledrappier-Young PartI, Section6.1, Corollary6.1.4 and the nonergodic Corollary6.2 give the unstable Jacobian ratio formula; Section6.2 explicitly treats a measurable partition subordinate to the unstable foliation. Comparison uses a joint refinement and the invariance/change-of-variables relation. For two points in a box plaque, their backward iterates approach one another. Backward recurrence of a typical base point to atoms containing a fixed-size neighborhood places both iterates in a common atom along a subsequence. The ratio formula transfers back to the original pair. Here the cocycle telescopes to A(y)/A(z), where A=|alpha(e^u)|; on the compact regular support A is positive and continuous, so the remaining ratio of backward A-values tends to one. The resulting density is the same normalized alpha-length on the full connected box plaque. Mere local absolute continuity, without this invariant density formula, would not justify uniform normalized densities on larger plaques.

Thus K is locally saturated by its unstable plaques. Small ambient transverse disks and the uniform graph property of the plaques give local lamination boxes with fixed longitudinal intervals; after shrinking the transverse disks their central boxes cover K, and compactness reduces this to finitely many boxes. Their fixed lengths and compact transversality give conditions(i)-(iii) above. Short carrier and vortex images need only stay near K, where the determinant bound persists; they need not stay in K.

This step uses the usual uniform local unstable manifold theorem and its continuous plaque dependence, not a smooth weak-unstable foliation. The focused coordinator and literature reviews both checked the recurrence passage and the uniform-box construction. The source and reconstruction above supply the needed plaque continuity and partition change. This result is not claimed for supports meeting either zero set.

## 5. Consequences under the bounded-density condition

Apply the main proof with q=infinity. In the decaying Euler range 2/5<=c<1/2,

    (1/(2S)) integral nu(dz) integral_(-S)^S
                   |H0(Gamma_s z)|^2 ds <= C S^(-2a/kappa), S>=1. (5)

No Dini hypothesis is needed, because A277's local L2 estimate pairs directly with the compactly supported bounded density. Equivalently, if rho_1 is supported in B_R1 and M=||U||_infinity, then rho_S is supported in B_(exp(ct)(R1+M/c)), because d|Phi_t y|/dt<=c|Phi_t y|+M. Together with ||rho_S||_infinity=S^(-d/kappa)||rho_1||_infinity and integral_(B_R) H0^2<=C R^(beta+2), this gives the exponent

    (c/kappa)(beta+2)-d/kappa
      =(c/kappa)(beta-1)=-2a/kappa.
 Under the same condition, (2) yields for every finite-volume measurable Q

    integral nu(dz) integral_(-S)^S 1_Q(Gamma_s z) ds
        <= 2 ||rho_1||_infinity |Q| S^(1-d/kappa)
         = 2 ||rho_1||_infinity |Q| S^(a/kappa).        (6)

This is an averaged upper bound for compact occupation, not a pointwise lower rate. If a bounded positive-volume Q lies where rho_1>=delta>0, the ambient Cauchy-Schwarz lower bound in the main proof also gives the same exponent as an averaged lower bound, with a harmless change from S to S+1: writing R_S(mu)=integral mu(dy) integral_(-S)^S 1_Q(Gamma_s y)ds, one has R_(S+1)(nu)>=R_S(m_1)>=delta integral_Q integral_(-S)^S 1_Q(Gamma_s y)ds dy>=C_Q S^(a/kappa). This requires a bounded positive-volume Q with rho_1>=delta there, not an arbitrary Q. These bounds are consistent with recurrence and unbounded excursions, and do not force H0 to vanish on the carrier support.

The polynomial H0 mean and occupation upper bounds are restricted to the bounded-density class. The general A308 support can meet zeros, so the main proof establishes only L1 and the qualitative conclusions there. No new nonexistence or C2 coverage theorem is asserted.

## Verification and exact sources

Input snapshots and hashes, including both focused reviews, are in verification. The actual Ledrappier-Young PartI manuscript was reread at printed pages533-535, Section6.1 through Corollary6.2. The actual Dyatlov manuscript was reread at Section4.6, Theorem5, and equation(4.67); the complete A131 reconstruction of continuous plaques was also reread. No claim is made that Theorem5 alone states the extra continuity clause. The full A056 graph-complement proof and A207 density proof were reread. The existing coordinator agent is configured for the primary model; this is configuration evidence, not independent provider attestation. No new model client or numerical computation was used.
