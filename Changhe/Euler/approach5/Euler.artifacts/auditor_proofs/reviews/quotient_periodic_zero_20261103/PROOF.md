# Quotient periods, velocity zeros and a local pressure obstruction

Status: CONFIRMED at the exact scopes of A691-A699. A700 keeps the general exclusion OPEN. The source hashes and independent postread are in the team records. No global nonexistence theorem is asserted here.

## 1. Setting and reading dependencies

Let 2/5<c<1/2, omega be any real number, p=(1-c)/c, lambda=p-1, mu=2-p, a=c lambda, t=omega/c, q=2p/lambda, and A=cI-omega J, where J(x1,x2,x3)=(-x2,x1,0). Thus lambda>0, mu>0 and q>6. On D=R3 minus the origin, let V be C1,alpha locally for every 0<alpha<1, divergence free, helicity free, and twisted homogeneous:

    V(exp(sA)x)=exp(-(1-c)s) exp(-omega s J)V(x).

Let P2 be C1, twisted homogeneous of degree -2(1-c) in this parametrization, and satisfy

    -Delta P2=partial_i partial_j(V_i V_j)

in distributions. Write W=curl V, S=P2-|V|^2/2 and k=(Ax).V. When used below, assume

    (N) k=0 implies W=0,
    (R) grad k cross grad S=0 wherever W!=0.

The sources also require W.grad S=0, but Section 10 shows this follows from (R) and (N). Distinguish the kinematic conclusions, which do not use the pressure equation or (R), from the pressure and scalar conclusions.

Use rho=log r, z=cos(theta), w=1-z^2, chi=phi+t rho. On the quotient sphere write

    V.flat=r^(-lambda)(K d rho+gamma),
    gamma=-(H/w)dz+F dchi,
    R=K+tF,
    k=c r^(-lambda)K,
    S=r^(-2p)h.

The round metric is dz^2/w+w dchi^2. Let Z=partial_chi be its smooth rotation vector field, and M=round inverse metric+t^2 Z tensor Z. Define the global C1 field

    B=M gamma+tKZ.

All pole assertions concern Cartesian regularity, not smoothness of the singular coordinate coefficients separately. The direct calculations below re-establish the needed identities. The invariant-measure argument is also proved in the team records (A645). The zero-free-S period theorem used only in Section 9 is in the team records (A667).

The surface recurrence input is the precise primary-source lemma of Tomoo Yokoyama, *A Poincare-Bendixson theorem for flows with arbitrarily many singular points*, arXiv:2109.12478v2, Lemmas 3.1 and 3.7, pages 9 and 15-16. Their full statements and proofs, the recurrence definitions and the paper's distinction between recurrence and singular limit sets were read from the actual archived manuscript. That theorem is a named dependency, not an assumption about finitely many equilibria.

## 2. Lift, nodal direction and weighted area

Substituting dphi=dchi-t d rho into the Euclidean metric gives

    g=r^2[(1+t^2w)d rho^2+dz^2/w-2tw d rho dchi+w dchi^2].

Inverting its rho,chi block and raising V.flat gives

    V=r^(-lambda-2)(R partial_rho+B),
    B=-H partial_z+(F/w+tR)partial_chi.

Thus a physical V-trajectory, with time tau, projects to a B-trajectory after the positive change ds/dtau=r^(-lambda-2). Along its lift d rho/ds=R. A trajectory may have finite maximal physical time in D; this local projection and the quotient's completeness do not assert physical completeness. The C1 field B on compact S2 has a complete flow Phi_s for every real s.

The divergence equation is H_z=mu R+tR_chi+F_chi/w. Hence

    div B=-mu R,                 integral_S2 R=0.             (1)

Differentiating the one-form gives

    dV.flat=r^(-lambda)[(dK+lambda gamma) wedge d rho+d gamma].

Therefore W=0 exactly when dK+lambda gamma=0 and d gamma=0. Under (N), on K=0,

    gamma=-dK/lambda,
    B=-M dK/lambda,
    B(K)=-|dK|_M^2/lambda.                                    (2)

A regular nodal point is crossed forward from K>0 to K<0. A critical nodal point has gamma=0 and V=B=0. Uniqueness prevents a nonconstant trajectory reaching such an equilibrium in finite quotient time. It follows that O={K>0} is backward invariant. This can also be checked by a first exit: a regular boundary exit in backward time contradicts the strict sign in (2), and a critical boundary exit contradicts uniqueness. Each connected component is separately backward invariant. Analogously, each component of {K<0} is forward invariant.

For b>=0 let O_b=Phi_(-b)O. For every nonnegative C1 function psi on S2,

    integral_O_b (mu psi R-B psi)<=0.                         (3)

Indeed Phi_(-h)O_b is contained in O_b for h>=0, so its psi-weighted area is nonincreasing. Differentiate at h=0 after changing variables by the ambient C1 diffeomorphism. The derivative of psi(Phi_(-h)x) Jac(Phi_(-h))(x) is mu psi R-B psi. Compactness bounds the difference quotients and justifies differentiation under the integral over the possibly irregular measurable set O_b. No boundary regularity is used. The same proof holds for any open backward-invariant subset.

## 3. Closed periods and the invariant-measure alternative

Twisted homogeneity and the vector identity for a gradient give

    grad k=-aV+(Ax) cross W.

Crossing with V, and using V.W=0, gives grad k cross V=kW. Thus curl(V/k)=0 wherever k!=0. Equivalently, for beta=gamma/K,

    V.flat/k=(d rho+beta)/c,             d beta=0.              (4)

If beta=df on an open positive-K region, then psi=exp(-mu f) obeys

    mu psi R-B psi=mu psi(R+Bf)=mu psi |v|^2/K>0,              (5)

where v=V at r=1. This is a local identity. Its use in (3) requires a single-valued f and an admissible global weight or justified limiting cutoffs. If K never vanishes on S2, beta is globally exact, since S2 is simply connected, and integrating (5) on the whole sphere contradicts (1). The negative-K case has the opposite strict sign and gives the same contradiction. Hence a nonzero field under (N) has a zero of K.

Suppose O is nonempty. C=closure(O) is compact and backward invariant. The nested nonempty compact sets Phi_(-b)C have a nonempty intersection Lambda. Shifting the parameter b proves Phi_s Lambda=Lambda for all real s. Any open neighborhood of Lambda contains Phi_(-b)C for all sufficiently large b, by compactness and nesting.

There is an invariant probability nu on Lambda with integral R dnu<=0. Here are the necessary measure and weight details. Time-average probabilities on a compact invariant set have invariant weak limits. The set of invariant probabilities is compact. If all their R averages were positive, their minimum would be delta>0. A sequence of arbitrarily long time averages below delta/2 would have an invariant limit contradicting that minimum. Thus for some T>0,

    A_T(x)=T^(-1) integral_0^T R(Phi_s x) ds>delta/2 on Lambda.

Set u(x)=-T^(-1) integral_0^T(T-s)R(Phi_s x) ds. This is a global C1 function with R-Bu=A_T, positive on a neighborhood of Lambda. Substituting psi=exp(mu u) in (3) on a late nonempty O_b gives a positive integral bounded above by zero, a contradiction. This establishes the claimed nu.

A regular K=0 point cannot lie in Lambda because it exits C forward. By (2), every K=0 point in Lambda is therefore a zero of V.

The surface recurrence lemma says that a nonclosed recurrent orbit on a compact surface admits a closed transversal intersecting it infinitely often, and any such transversal through a nonclosed recurrent point is essential. On S2 every simple closed curve separates; a transversal has a consistent crossing direction and an orbit cannot cross it again after its first crossing. Thus no nonclosed recurrent orbit exists. The primary lemma's short proof constructs the transversal by a return arc and a transverse segment, followed by the flow-box waterfall construction. It does not require isolated or finitely many zeros.

An ergodic invariant probability has almost every point recurrent, by Poincare recurrence for Phi_1, and generic for time averages of a countable dense set of continuous functions. Its generic recurrent orbit is consequently an equilibrium or periodic, and its probability is the point mass or normalized time measure on that orbit. By ergodic decomposition, a probability with nonpositive R mean has an ergodic component with nonpositive R mean. This last assertion also follows by minimizing the continuous functional integral R over the compact convex invariant-probability set and taking an extreme point of its minimizing face.

At B=0, intrinsic algebra yields

    gamma=-tK M^(-1)Z,
    R=K/(1+t^2 w).                                           (6)

The same formula gives R=K at a pole, where Z=0. Every equilibrium in K>0 has positive R. Consequently at least one of the following holds:

    (Z) Lambda contains a zero of V;
    (P) a periodic B-orbit Gamma contained in K>0 has
        I=integral_0^T R(Gamma(s)) ds<=0.                     (7)

Its transverse multiplier is exp(-mu I). The logarithm of the multiplier is -mu I, whereas the exponent per unit quotient time is -mu I/T. This is a classification of ergodic measures used in (7), not a classification of all limit sets. Singular circuits and continua of equilibria have not been removed.

The argument applies separately to every positive-K component. The negative version uses its forward core and produces either a velocity zero or a periodic orbit in K<0 with I>=0.

## 4. The periodic cone and transverse vorticity

Assume (P). A nonstationary periodic orbit of a C1 autonomous field is a C2 embedded circle. It bounds two disks in S2. Both open disks are invariant by uniqueness. The divergence theorem and tangency of B give

    integral_D_i R=0.                                        (8)

Each disk has a B equilibrium. To see this without assuming isolated zeros, if B were nonzero on the closed disk, its normalized direction would extend from the boundary to the disk. In a disk trivialization, its tangent direction on the oriented boundary has winding number one, impossible for a map extending to the disk.

After one quotient period, a lifted V-trajectory advances rho by I. Close it using the twisted scaling segment at the initial quotient point. Formula (4) gives the period

    P_Gamma=(1/c) integral_Gamma beta
           =(1/c) integral_0^T (|v|^2/K-R) ds>0.              (9)

The equality uses beta(B)=|v|^2/K-R. In physical V-time the same expression is integral_lift |V|^2/k d tau-I/c. If quotient time is used in this latter integral, the integrand is r^(lambda+2)|V|^2/k. These two time variables must not be interchanged. The lift over a finite quotient period and the closing scaling segment both remain in D and k!=0, so the closed curve and its integral are well-defined.

If either disk had no K zero, continuity and K>0 on its boundary would make beta a closed C1 form on the entire closed disk. Stokes would contradict its positive boundary period. Each open disk therefore contains a K zero.

A stronger statement is kinematic. On K>0 put zeta=d log K+lambda beta. Then

    dV.flat=r^(-lambda)K zeta wedge(d rho+beta),
    W=0 if and only if zeta=0.                               (10)

The cone over Gamma is parametrized by independent variables rho and s. Pullback of (10) is -r^(-lambda)K zeta(B) d rho wedge ds. Since dV.flat is contraction of Euclidean volume by W, its pullback vanishes precisely when W is tangent to the cone. But

    integral_0^T zeta(B) ds=lambda integral_Gamma beta>0.

Thus W is transverse to this cone somewhere. In particular the whole cone cannot be irrotational. This deduction uses helicity and the positive period, not the pressure equation or rank condition.

## 5. Linearization at a velocity zero

Let |x0|=1 and V(x0)=0. Then k(x0)=0, and (N) gives W(x0)=0. With L=DV(x0),

    L=L transpose,           trace L=0,           L Ax0=0.    (11)

The last identity follows by differentiating the zero along its twisted scaling orbit. Ax0 is nonzero because x0.Ax0=c>0. Hence the eigenvalues of L are 0,sigma,-sigma. If L is nonzero, sigma is nonzero.

At the zero, multiplying V by r^(lambda+2) leaves its differential unchanged at r=1. In twisted coordinates this field is R partial_rho+B and its differential has a zero rho-column, because R and B depend only on the quotient point. Its block matrix is

    [ 0  dR ]
    [ 0  DB ].

Coordinate change is a similarity. Thus if L!=0, DB has eigenvalues sigma,-sigma and the quotient zero is a hyperbolic saddle. If L=0, DB=dR=0. Conversely DB=0 forces all eigenvalues of L to vanish, so symmetry gives L=0. In particular, a nonisolated quotient equilibrium which is also a velocity zero has DV=DB=0. This assertion is about velocity zeros; it does not classify other quotient equilibria, where (6) permits V!=0.

At a zero with DV=0, Holder continuity yields V(x)=O(|x-x0|^(1+alpha)) for every alpha<1, and B,R=O(d_S2(x,x0)^(1+alpha)). No higher Taylor jet is assumed.

## 6. Singular weights and an exact local countertest

Let Z0 be the velocity-zero set and psi>=0 be C1 off it. Define

    I_psi=mu psi R-B psi=-div(psi B).

Choose 0<=xi_j<=1 smooth, vanishing near Z0, tending to one off Z0, with xi_j psi extended as a global C1 function. Applying (3) gives exactly

    integral_O_b xi_j I_psi<=integral_O_b psi B xi_j.          (12)

If I_psi is integrable, dominated convergence handles the left side. To recover its unweighted upper bound zero, the right side must have nonpositive upper limit. This is the condition to prove; zero first jets alone do not supply it.

For finitely many isolated zeros with ordinary flux limits, the defect is the sum of

    lim_epsilon->0 integral_(partial B_epsilon(x0) cap O_b)
                        psi B.n_out d length,               (13)

where n_out points out of the deleted disk. An infinite sum requires an additional uniform cutoff or absolute-convergence justification; isolated-point limits by themselves do not authorize interchanging a sum and limit. For nonisolated sets use (12). At a flat zero, a sufficient estimate for its individual flux to vanish is epsilon^(2+alpha) sup_(partial B_epsilon)psi ->0. At a general C1 zero use epsilon^2 instead. The required integrability in (12) remains separate.

For a local exact countertest, assume t!=0, put u=1-z, and fix an integer m>=2. Near the north pole define

    K=u^m,        R=-u^m,        F=-2u^m/t,
    H=mu u^(m+1)/(m+1).                                      (14)

Then R=K+tF and H_z=mu R, so incompressibility holds. Moreover

    beta=mu du/[(m+1)(2-u)]-(2/t)dchi

is closed, proving helicity freeness. In Cartesian angular coordinates, F/s e_phi has order 2m-1 and a smooth even radial coefficient multiplying Jx, while H/s e_theta has order 2m+1. Together with R this gives a smooth Cartesian velocity with V=DV=W=0 on the pole ray. K>0 away from that ray, so (N) holds locally. The quotient equation is du/ds=H>0: there is no local periodic orbit and backward trajectories approach the pole.

For psi=u^(-b), direct calculation gives

    I_psi=mu[b/(m+1)-1]u^(m-b),
    outward flux=2 pi mu u^(m+1-b)/(m+1).                    (15)

Area measure is du dchi. Positivity requires b>m+1, exactly where the interior integral diverges and the outward flux tends to infinity. At b=m+1 the interior expression is zero but the flux is a positive constant. With angular weights, their angular average gives -partial_u(H average(psi)), so it does not repair this elementary flux balance. This proves only a countertest to removing flux from first jets and the kinematic equations. Section 8 shows that (14) cannot satisfy the pressure equation and rank simultaneously. It is not a tail of an actual profile.

## 7. Local pressure lemma with exact regularity

The following statement is local in a full Euclidean ball and does not require homogeneity. Let V be C1,alpha for every alpha<1, div V=0, P be C1 with -Delta P=partial_i partial_j(V_i V_j), and S=P-|V|^2/2. Suppose V(x0)=curl V(x0)=0. If for some 0<=epsilon<1/4,

    S(x)-S(x0)>=-epsilon |V(x)|^2                            (16)

throughout a full neighborhood of x0, then V vanishes on a neighborhood of x0.

For a fixed Holder exponent, it suffices instead to assume some 0<alpha<1 with

    (1/2-epsilon)^(-1)<2+2alpha.

Here is a full proof. Distributional differentiation using div V=0 gives Delta P=-trace((DV)^2). This identity follows by local mollification if no second derivative of V is assumed. The source is C0,alpha; interior elliptic regularity upgrades P to C2,alpha. Translate x0 to zero. Let L=DV(0), which is symmetric and trace free, and let a bar denote normalized spherical average on radius r. Put E(r)=average |V|^2 and A0(r)=average(V.n)^2. First-order expansion of V and second-order expansion of P yield

    E(r)=|L|^2 r^2/3+o(r^2),
    average(S-S(0))=-|L|^2 r^2/3+o(r^2).

The latter uses Delta P(0)=-|L|^2 and the vanishing spherical average of the linear pressure term. Averaging (16) forces (1-epsilon)|L|^2<=0, hence L=0. Therefore E,A0=O(r^(2+2alpha)).

The exact spherical pressure identity is

    average(P)'=-A0'-(3A0-E)/r.                             (17)

For completeness, put Q=div(V tensor V)=(V.grad)V. Integrating -Delta P=div Q on a ball gives average(P)'=-average(Q.n). Decompose V=V_r n+V_tan. Using div V=partial_r V_r+2V_r/r+div_S V_tan/r=0 and integrating tangential derivatives on the sphere gives

    average(Q.n)=partial_r average(V_r^2)
                     +[3 average(V_r^2)-average|V|^2]/r.

This proves (17). The divergence theorem for Q follows first after mollification and then by uniform convergence of V,DV on compact sets; alternatively the flux identity follows for almost every r and then for all r by continuity. No second derivative of V or regularity at the origin of a coordinate vector is being assumed.

Set Y(r)=average(P-P(0))+A0(r). Equation (17) and (16) give

    Y'=(E-3A0)/r,
    Y>=(1/2-epsilon)E+A0>=0.                                (18)

Y(0)=0, and integrating its derivative gives Y=O(r^(2+2alpha)). With kappa=(1/2-epsilon)^(-1), (18) implies Y'<=kappa Y/r. Therefore r^(-kappa)Y is nonincreasing, nonnegative, and tends to zero at r=0 because 2+2alpha>kappa. For every positive r it is bounded above by its zero limit, so it vanishes. Equation (18) implies E=0 on every sufficiently small sphere. Continuity proves V=0 in a ball. This completes the argument.

Thus any velocity zero accumulated by nonzero velocity must violate (16) in every full neighborhood. The theorem does not hold here as an assertion from a one-sided region or from an averaged rank relation on a subset.

The strict exponent threshold is sharp for this local lemma. For 0<alpha<=1, let rho_c=sqrt(x1^2+x2^2) and set

    V=rho_c^alpha(-x2,x1,0),
    P=rho_c^(2+2alpha)/(2+2alpha).

This is a C1,alpha velocity (C1,1 when alpha=1), with divergence zero, curl V=(0,0,(2+alpha)rho_c^alpha), and V=curl V=0 on the rotation axis. Its derivative is homogeneous of degree alpha in the two transverse variables and extends with the asserted Holder modulus. For alpha=1, the second derivatives away from the axis are bounded; integration on line segments proves that the extended first derivative is Lipschitz. Direct differentiation gives

    (V.grad)V=-rho_c^(2alpha)(x1,x2,0)=-grad P,
    Delta P=(2+2alpha)rho_c^(2alpha),
    S=-[alpha/(2+2alpha)]|V|^2.

Thus it satisfies the local pressure equation and (16) at epsilon=alpha/[2(1+alpha)], but does not vanish in any neighborhood of an axis point. For alpha=1 it has all the regularity assumed in the main lemma and gives the exact endpoint epsilon=1/4 countertest. It is a local steady Euler test, not a negative-degree global twisted tail or a campaign-profile counterexample.

## 8. Bounded scalar constants near a zero

In the homogeneous setting of Section 1, assume (N) and (R). On W!=0, k!=0 and (Ax).grad k=-ak!=0. Thus grad k!=0. Rank and homogeneity give

    grad S=q(S/k) grad k,
    S=D_j |k|^q on each connected vortical component.         (19)

Suppose a velocity zero x0 has a punctured full neighborhood where (19) holds with uniformly bounded constants D_j. It is enough for this bound to hold on a dense subset, since the resulting inequality extends by continuity. Then S(x0)=0 and

    |S(x)|<=C |k(x)|^q<=C' |V(x)|^q=o(|V(x)|^2).

Because q>2 and V tends to zero, (16) holds for any fixed positive epsilon<1/4 in a small enough ball. Section 7 forces V to vanish there. In particular a nonzero velocity cannot accumulate at such a zero. This applies to a punctured connected vortical neighborhood or finitely many pieces only when those pieces supply the power bound densely throughout the full neighborhood. Arbitrary open irrotational gaps are not covered.

For (14), zeta=d log K+lambda beta has nonzero angular coefficient -2lambda/t on the punctured polar neighborhood. Thus it is entirely vortical there. Rank would give one constant D in (19), so Section 7 would force local V=0, contradicting (14). Therefore that local kinematic countertest fails pressure plus rank. This is an analytic exclusion, independent of a small residual or numerical approximation.

## 9. Consequence when S is nowhere zero

Assume additionally S!=0 on all D. A667 proves that every period of V.flat/k on each k-sign component vanishes. Its hypotheses are precisely the homogeneous C1 helicity-free field, (N), rank on W!=0 and zero-free S; the global regularization uses simple connectivity of D and does not assume that the k-sign component is simply connected. Section 4's positive period therefore excludes case (P).

Applying Section 3 separately to every connected component of K>0 shows that its compact backward core contains a velocity zero. Similarly every connected component of K<0 has a velocity zero in its compact forward core: a periodic alternative there would have K<0 and I>=0, giving a strictly negative period in (9), again impossible by A667. The zeros for different components need not be distinct. This refines their location; it does not exclude flat velocity-zero sets.

Under the full tail assumptions, the one-signed argument A677 forces both signs of K when S is nowhere zero and V is nonzero. Thus both versions of this core-zero conclusion apply to a hypothetical such tail. None of these implications proves that such a tail exists or that all its zeros are ruled out by Section 7.

## 10. Exact remaining periodic system and source qualifications

On a positive-K region let beta=gamma/K, f=h/K^q, e=|v|^2/2 and zeta=d log K+lambda beta. Reconstruct V from V.flat=r^(-lambda)K(d rho+beta). The system is

    d beta=0,
    B=K(M beta+tZ),             R=K(1+t beta(Z)),
    div B=-mu K(1+t beta(Z)),
    d f=0 wherever zeta!=0,
    e=K^2[(1+t beta(Z))^2+|beta|^2]/2,
    L_t(e+K^q f)=-trace((DV)^2) at r=1,                      (20)

where

    L_t u=(w u_z)_z+(1/w+t^2)u_chichi
                   +t(1-4p)u_chi+2p(2p-1)u.

The condition d f=0 is imposed on the vortical set. The original rank places no restriction on d f in the interior of zeta=0. If the vortical set is dense in an annulus, continuity does extend d f=0 there.

Helicity and grad k=-aV+(Ax) cross W give W.grad k=0. Therefore (19) implies W.grad S=0 on W!=0, and it is automatic on W=0. This transport is along W, not along V. If (19) holds all around the periodic cone, one lifted turn multiplies k by exp(-lambda I) and S by exp(-2p I); these are compatible and give no recurrence contradiction when I<0. If I=0, the positive period is permitted by the topology unless an additional theorem such as A667 is available.

The unresolved periodic problem is to exclude a solution of (20) extending to a globally Cartesian-regular nodal tail and admitting a periodic orbit with I<=0, positive beta-period, the two disk identities (8), and a K zero in each disk. Vorticity must cross its cone somewhere. In the S-zero-free subclass this periodic alternative has already been excluded by Section 9; the remaining difficulty there is the velocity-zero configuration. The general no-periodic-orbit premise does not by itself give a single-valued, integrable weight through arbitrary zeros, so the full zero-case exclusion is also OPEN.

The source's additional inputs must keep their scope. The rank-holding irrotational estimate is A651 and requires rank on that open irrotational component. It cannot be supplied from (R). In the pure swirl countertest K=-tw^2 is nonpositive only for t>=0; (N) and the nonzero period formula require t!=0. The canonical pressure calculation at p=5/4 is already A649, and its failed rank/transport means it is not a full-tail counterexample. Its positive-K sign has periodic latitudes with I=0, so it does not test a no-(P) hypothesis. The next pressure scalar is additional actual-profile input (A647-A648 and, including c=3/7, A653-A655); the variables defining it are not supplied by (20) alone.

## 11. Verification and limits

All arguments here are analytic. No numerical experiment, symbolic calculation or formal build was needed. The primary surface-flow lemma was read in the downloaded PDF extraction with its proof and definitions, not inferred from an abstract. Source snapshots and hashes are in the team records. The local pressure argument, boundary signs, Holder threshold, time change, pole algebra and every parameter restriction were independently reconstructed above.

The inner source reports a failed credential lookup for its requested model consultation and no actual response; it must not be counted as model collaboration. Existing configured model coordinator and theory agents supply the permitted continuing cross-agent comparison. Their model configuration is recorded, but provider execution is not independently attested. Focused feedback on the local pressure lemma and the two scope qualifications is recorded separately when received. No substitute model client is launched.
