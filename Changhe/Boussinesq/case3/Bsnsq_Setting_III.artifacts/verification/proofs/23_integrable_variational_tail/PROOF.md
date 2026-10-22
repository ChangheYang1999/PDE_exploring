# Scattering from an integrable variational tail

Status: independent verification of the weakened derivative hypothesis H1' in the lead's Theorem E. CONFIRMED under the exact assumptions below. In particular, a power bound on V is not needed in addition to this uniform orbit-integral assumption. This hypothesis has not been derived from the broad prompt or from pointwise vorticity decay alone.

## Statement and scope

Let W(X)=beta X+V(X) on R^2, beta>0, with V smooth, V=o(r), V(0)=0 and div V=0. Let phi_t be its complete flow, E its forward escaping set, and suppose

    epsilon(R):=sup_(|Y|>=R) int_0^infinity |DV(phi_t Y)| dt ->0  as R->infinity.   (D)

Take R large enough that W points strictly outward outside that radius. Then

    Phi_t(X)=e^(-beta t)phi_t X -> Phi(X)

in C1 on compact subsets of E. The limit Phi is a C1 area-preserving diffeomorphism from E onto R^2 minus{0}, with

    Phi(phi_s X)=e^(beta s)Phi(X),
    Phi(X)=X+o(|X|), DPhi(X)=I+o(1) at infinity.                 (1)

If smooth Omega,Theta solve the B2 transport equations with beta>=2, then on E

    Theta(phi_t X)=e^((beta-2)t)Theta(X),
    Omega(phi_t X)=e^(-t)A(X)-e^(-2t)[g(X)+o(1)],               (2)
    g(X)=[DPhi(X)^(-T) gradTheta(X)]_1,
    A(X)=Omega(X)+int_0^infinity e^t Theta_x(phi_t X) dt.

The convergence and remainder in(2) are locally uniform on E. In scattering coordinates, Theta is homogeneous of degree1-2/beta and A of degree-1/beta. Uniformly in ordinary polar angle,

    Omega(r e(theta))=r^(-1/beta)[a(theta)+o(1)]                (3)

for a continuous function a. Under the B2 center/parity hypotheses a is not identically zero. A fixed-polar second coefficient is not asserted, since the o(r) discrepancy in(1) has no specified rate.

## 1. Complete flow and the matrix limit

V=o(r) gives |W|<=C(1+r), so the flow exists in both time directions. Outside a fixed circle its radius increases at least exponentially in positive time. Every compact subset of E reaches each sufficiently large circle by a uniformly bounded time; this follows from openness of the escape set, continuity of the flow and a finite cover. After the circle has been reached, radius is monotone increasing.

Set M_t(X)=e^(-beta t)Dphi_t(X). Its variational equation is

    dM_t/dt=DV(phi_t X)M_t, M_0=I.

For fixed X in E the coefficient is integrable: it is smooth on the initial finite-time segment and satisfies(D) afterward. Gronwall bounds M_t. For s>t,

    |M_s-M_t| <= sup_(u>=0)|M_u| int_t^s |DV(phi_u X)|du.

On a compact subset of E the bounds are uniform and the tails tend uniformly to0 by(D), because its minimum outgoing radius tends to infinity. Thus M_t converges uniformly there to M_infinity. Since div W=2beta, det M_t=1 at every time, hence det M_infinity=1.

## 2. Position limit without a separately assumed power velocity bound

The autonomous-flow identity Dphi_t(X)W(X)=W(phi_t X) gives

    e^(-beta t)W(phi_t X)=M_t(X)W(X).

Integrating dphi_t/dt=W(phi_t X),

    Phi_t(X)=e^(-beta t)X
       +int_0^t e^(-beta(t-s)) M_s(X)W(X) ds.

The matrix limit and the elementary exponential averaging identity yield

    Phi(X)=M_infinity(X)W(X)/beta.                             (4)

The convergence is locally uniform on E. Together with locally uniform convergence of the derivatives DPhi_t=M_t, it proves C1 convergence and DPhi=M_infinity. If X is escaping then W(X)!=0, so(4) and invertibility of M_infinity show Phi(X)!=0.

For |X| large, the integral in(D) is at most epsilon(|X|). The matrix integral equation gives |M_infinity-I|<=exp(epsilon)-1. Equation(4), W(X)=beta X+o(r), and this bound prove the two asymptotics in(1). Thus(D) supplies the precise radius asymptotic on escaping compact sets even when the original assumption was only V=o(r).

## 3. Global diffeomorphism

A local C1 diffeomorphism follows from det DPhi=1. At sufficiently large radius the estimates |Phi(X)-X|=o(r) and |DPhi-I|=o(1) imply that for every large z the map

    X -> z-[Phi(X)-X]

is a contraction of the closed ball B(z,|z|/2) into itself. It has a unique fixed point there. Any preimage of a sufficiently large z is in this ball, by Phi(X)=X+o(r); points in a bounded subset of E have bounded Phi, as follows from(4) outside a large circle and equivariance before reaching it. Hence Phi has exactly one preimage for each sufficiently large z.

Equivariance follows directly by shifting time in the defining limit. For arbitrary z!=0 choose s>0 with e^(beta s)z in the exterior image and flow its preimage backward for time s. This proves surjectivity. If two points have the same image, flow them forward until the common image is large and apply uniqueness there, then flow backward. This proves global injectivity. Its inverse is C1 by the local inverse theorem, and det DPhi=1 proves area preservation.

For clarity, the boundedness of Phi on bounded subsets used above does not require regularity at the nonescaping set. Choose a large transverse exit circle. Its Phi image is compact. Any escaping point inside that circle has Phi equal to e^(-beta T) times the Phi of its first exit point, where T>=0. This gives the needed uniform bound.

## 4. Transport and vorticity asymptotics

Temperature transport and the chain rule give the exact covector identity

    gradTheta(phi_t X)=e^(-2t) M_t(X)^(-T) gradTheta(X).

The inverse matrices converge locally uniformly, so Theta_x(phi_t X)=e^(-2t)[g(X)+o(1)]. The integral defining A therefore converges locally uniformly. Solving the scalar vorticity ODE and subtracting its tail yields

    Omega(phi_t X)=e^(-t)A(X)
       -e^(-t)int_t^infinity e^(-s)[g(X)+o(1)]ds,

which is(2). In particular A(phi_s X)=e^(-s)A(X). With F=Theta o Phi^(-1) and Ahat=A o Phi^(-1), equivariance gives

    F(rz)=r^(1-2/beta)F(z), Ahat(rz)=r^(-1/beta)Ahat(z).

F is C1 away from0, and Ahat is continuous. Thus their restrictions to the unit circle have bounded values and F has bounded first derivatives there. Formula(1) implies gradTheta=O(r^(-2/beta)) uniformly at infinity. Also (4) and the uniform smallness in(D) give |phi_t X| comparable to e^(beta t)|X| for all large X and t>=0, with constants independent of X,t. Consequently

    |A(X)-Omega(X)|<=C |X|^(-2/beta).

Write Ahat(r,theta)=r^(-1/beta)a(theta). Combining its homogeneity, continuity on the circle and Phi(X)=X+o(r) proves(3). The same argument gives the uniform angular temperature limit, with the corresponding exponent.

## 5. Nonzero leading vorticity coefficient for B2

The continuity-only circulation argument of research/17 constructs rectangles with sign(a0)A_D>0. The domain can be chosen with compact closure in E, using only sublinearity, as in sections1-2 of research/18. For beta>2 nonzero temperature forces escape. For beta=2 select a global regular value of Theta by Sard; on that level every nonstationary point escapes, since all zeros of the one-dimensional level flow are simple repellers with derivative divW=4 and there are no periodic orbits. A compact regular-level segment and openness of E then give a sufficiently thin rectangle inside E. This part of research/18 does not require a power velocity bound.

On this domain D, equation(2) is uniform. Changing variables by the flow Jacobian gives

    A_D=lim_(t->infinity)e^(-(2beta-1)t)int_(phi_t D)Omega
       =lim_(t->infinity)int_D e^t Omega(phi_t X)dX
       =int_D A(X)dX.

Thus A is nonzero somewhere, so a is not identically zero. This proves a pointwise angular classification only under(D), not for the complete prompt class. It also avoids differentiating the circulation resolvent H at the center or integrating a limit over the nonescaping set.

Dependencies: elementary ODE and variational flow, Gronwall, the inverse/contraction theorems, the transport equations, research/17's circulation coefficient, and the independently audited regular-level escape lemma in research/18. No numerical evidence is used as proof.

Audit 2026-10-20T15:04:32.861202+00:00: actual returned claude-opus-5-5 in opus_reviews/13_variational_flow/answer.md independently confirms sections1-4 and section5 conditional on research/17-18. It checks the exterior contraction ball, bounded images near the nonescaping set, covector identity, uniform polar limit, and the lack of an unconditional derivative-decay theorem. Sections1-4 in fact hold for all beta>0; beta>=2 is retained in the profile statement because the nontrivial B2 center problem has already excluded beta<2.
