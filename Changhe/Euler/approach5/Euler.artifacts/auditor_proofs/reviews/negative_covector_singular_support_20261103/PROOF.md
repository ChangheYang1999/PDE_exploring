# A remaining exceptional measure must meet a singular stratum

Status: CONFIRMED as A463 after independent reconstruction, full postwrite inspection and focused configured-model review. The periodic-orbit obstruction used below is A449. The support conclusion does not exclude the measure itself, and the stronger A460 now implies it directly.

## 1. Exact statement

Let U in C2(R3;R3),P in C1 solve the full incompressible rotating Euler profile equation for 0<c<1/2 and arbitrary real omega. Assume uniform U=o(|y|) and U.curl U=0 everywhere. Write

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c,
    H=P+|U|^2/2+(Ay).U, g=U.B.

Let mu be invariant and ergodic for the complete backward carrier flow Psi, with compact support S, and suppose mu almost everywhere

    B!=0, W=0, DW!=0, D(B cross W)=0.

Then the conclusion is

    S intersects ({B=0} union {DW=0}).                     (1)

Both sets on the right have mu measure zero by hypothesis. Thus(1) concerns the compact topological support and allows arbitrarily close visits to a removed stratum. It gives no positive mass or atom there, and no exclusion of aperiodic measures approaching such points.

The already confirmed A444-A445 imply that only the negative covector branch remains: H has one constant value h0 on S, g=0 there, every zero of U on S is a carrier equilibrium at the origin, and

    grad g=-kappa U wherever U!=0 on S.                  (2)

We retain those exact inputs rather than treating the covector identity as an assumption obtained from decay alone outside this globally helicity-free class.

## 2. A regular surface containing the whole support under the contrary hypothesis

Assume for contradiction that B and DW are nonzero everywhere on S. Then U is nonzero there by A444, and grad H=-aU is nonzero there because W=0 on S by continuity. Define the regular level surface

    N={H=h0} intersect {B!=0,U!=0,DW!=0,grad H!=0}.

Every point of N has a neighborhood where one scalar component of W has nonzero derivative. Its regular zero surface contains {W=0}, so the vortical set is dense in that neighborhood. A413 gives dH wedge dg=0 on the vortical set and continuity extends it to the neighborhood. The C2 submersion theorem then gives g=f(H) in every sufficiently small connected-fiber box.

The scalar q defined locally by grad g=q grad H is C1. In each such box q=f'(H); hence both g and q are locally constant on N. They are constant on each connected component M of N. A component meeting S consequently has g=0 and q=kappa/a by(2), so throughout that component

    BH=0, B tangent to M, grad(BH)=-kappa grad H.          (3)

There are countably many components of N because N is a second-countable manifold and its components are open in N. Each S intersect M is invariant under the whole flow: an orbit stays in S, is regular by the contrary hypothesis, and its continuous path cannot change connected component of N. Ergodicity selects one component M with mu(M)=1. Components are closed relative to N. Since every point of S lies in N and S is the support of mu, this full-measure component contains every point of S. In detail, S is contained in the ambient closure of M, whose intersection with N is M. Thus S is genuinely a compact subset of this single regular surface.

M need not be compact or complete. We use the flow only near its compact invariant subset S, which is enough for all estimates below. This direct component argument supplies the needed portion of the regular-surface result without invoking a compact-surface theorem or assuming that an arbitrary full-measure subset contains its support.

## 3. Exact uniform contraction normal to the surface flow

Equation(3) gives along any flow segment staying in M

    D Phi_s(x)^T grad H(Phi_s x)=exp(-kappa s)grad H(x).

The ambient determinant is exp(ds). The codimension-one area formula therefore gives for the backward flow on M

    J_M Psi_t(x)=exp(-(d+kappa)t)
                  |grad H(Psi_t x)|/|grad H(x)|.          (4)

For clarity, the area factor of a linear map L on the oriented plane with unit normal n is det(L)|L^(-T)n|. Substitution of the covector identity into this formula proves(4) with the displayed direction of the gradient ratio.

Let N_x be the line in T_x M orthogonal to B(x). Write P_x^t for the derivative D Psi_t followed by orthogonal projection to N_(Psi_t x), restricted to N_x. Since D Psi_t B(x)=B(Psi_t x), the determinant in a unit flow/normal frame gives

    |P_x^t|=exp(-(d+kappa)t)
       |grad H(Psi_t x)|/|grad H(x)|
       |B(x)|/|B(Psi_t x)|.                              (5)

Every point of S remains in S. Compactness and nonvanishing of B and grad H give fixed positive lower and finite upper bounds for these norms. Consequently there is C>=1 with

    |P_x^t|<=C exp(-(d+kappa)t), x in S, t>=0.            (6)

This is a uniform estimate for every point and every time. No integrability of logarithmic speeds or inference from a merely negative almost-everywhere exponent is involved.

## 4. Uniform contraction on a compact regular surface set forces periodicity

We prove the precise elementary dynamical fact required. Let a C1 flow on an oriented C2 surface be defined near a compact full invariant set S, be nonvanishing on S, and have the one-dimensional linear Poincare estimate |P_x^t|<=C exp(-eta t), eta>0. Assume its local derivative maps have the usual joint continuity of a C1 flow. Then every recurrent point in S belongs to an attracting periodic orbit of the surface flow. In particular a whole-flow-ergodic probability supported on S is normalized time measure on one such orbit.

Work on a small neighborhood of S where the field has positive minimum speed. In the present application the surface is oriented; choose the unit normal-to-flow tangent field there. Its C1 local flow supplies transverse sections I_x(s) through every x in S, with coordinate s centered at x and unit transverse derivative at0. Finite flow boxes and compactness give uniform section and projection domains. The inverse maps in these boxes have uniformly bounded first derivatives. This construction needs no compact ambient surface.

Choose a block time L so large that C exp(-eta L)<1/4. The flow holonomy F_x from I_x to I_(Psi_L x), with transit time close to L, maps coordinate0 to0. Its derivative at0 is the linear Poincare map, so has absolute value below1/4. For this fixed finite time L, continuous dependence on initial points and derivatives is uniform on a compact neighborhood of S. There is one delta>0 for which every block holonomy is defined on [-delta,delta], has positive transit time, and satisfies

    |F_x'(s)|<=1/2, |F_x(s)|<=|s|/2.                    (7)

The transit-time corrections are uniformly small compared with L. These assertions follow by shrinking the common domains after choosing L, not by imposing an infinite-time flow box.

Successive block holonomies along the central orbit of x can therefore be composed for all integers n>=0 on the whole initial interval. Their images have radius at most2^(-n)delta and derivative norm at most2^(-n). Each composition is a genuine positive-time flow holonomy; its center is the point Psi_(nL)x. The entire intermediate image lies in the domain of the next block by(7).

Let x be recurrent. Choose t_j tending to infinity with Psi_(t_j)x tending to x, and write t_j=n_j L+r_j,0<=r_j<L. Append the bounded remaining time r_j and the small final projection to the fixed initial section I_x. The shrinking block images lie in the domain of this final projection for all sufficiently large j. The resulting return holonomy R_j on [-delta,delta] has central coordinate s_j tending to0 and derivative bounded by C0 2^(-n_j), where C0 is uniform for the bounded remaining time and the final local projection. Hence for large j it maps the closed interval strictly into itself and has derivative norm below1/2.

The contraction mapping theorem gives a fixed point p_j of R_j. Its positive return time makes it periodic. The derivative of this return, possibly an iterate of the first return, has modulus below1/2, so its periodic orbit is hyperbolically attracting within the surface. Iterating R_j shows that x approaches this periodic orbit. The fixed return map has a continuous positive transit-time function bounded above and below on its interval, so return-section convergence also gives convergence in continuous time. Since x is recurrent, it lies on the periodic orbit: distance to that closed orbit tends to zero, while a recurrent subsequence returns to x.

For almost every x under an invariant probability, Poincare recurrence holds. For a whole-flow-ergodic probability one may also choose x with its continuous-time empirical measures converging to that probability. The periodic orbit through such x has empirical measure equal to its normalized time measure, so the given probability is exactly that measure. No ergodicity of the time-L map is assumed.

## 5. Euler contradiction and remaining scope

Apply Section4 to the backward surface flow X=-B on M and the exact estimate(6). The probability mu is supported on one periodic carrier orbit Gamma. Every original almost-everywhere exceptional condition holds everywhere on that orbit by continuity and the full support of its normalized time measure; the nonvanishing assumptions already hold on all of S. The negative covector data follow from A444-A445. The rank-one image statement follows from A433, or directly from its differentiated Cauchy classification. Thus Gamma satisfies A449 and is excluded. This contradicts the assumption that B and DW are nonzero everywhere on S and proves the proposed support assertion(1).

The result provides no uniform distance of typical points from the exceptional strata, no estimate of recurrence near them, no hyperbolicity of carrier zeros and no control of the first-jet-flat stratum. It cannot be reapplied when the support merely has a full-measure regular part: the compact regular set, positive speed lower bound and bounded gradient ratios used in(6) would then be absent. It gives no bound on Gamma_E for the unrestricted profile class.

## 6. Dependencies and evidence

The Euler dependencies are confirmed A413, A433, A444, A445 and A449, together with the exact Lamb, Cauchy and volume identities. The required regular-component deduction has been reconstructed in Section2. The compact regular recurrence lemma is proved in Section4; no Araujo theorem on a compact ambient manifold or unverified completion of M is invoked.

The complete hand argument was written before computation; none is needed or planned. The source LIT99 proof and complete focused configured-model review are pinned in verification. The review and full postwrite audit are complete. The general decay-only nonexistence conjecture remains OPEN.
