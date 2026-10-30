# Audit of the localized low-energy estimate

## Setting and verdicts

Let U have Fourier symbol m(xi)=(xi_1 xi_2/|xi|^2,-xi_1^2/|xi|^2), and let R_j have symbol i xi_j/|xi|. Work on real L2(R2), restricted to S1 whenever the background is S1. Let V=cX+U[rho] be globally Lipschitz with div V=2c, and let A=V.grad-1+Q, Qh=U[h].grad rho. Assume grad rho bounded and uniformly continuous. Write Sym Q=P0+K, where K is compact with norm at most kappa, and

    <P0h,h>=integral (Rh)^T M(Rh),
    M=[[-rho_y,rho_x/2],[rho_x/2,0]],
    theta=lambda_max(M)=(|grad rho|-rho_y)/2.

The frozen source is T2_localized_BL2.md in source/. Its L1, Lemma C and L2 are confirmed below under the hypotheses stated here. The optional first-commutator Hilbert-Schmidt suggestion in Section8 is false. The orbit construction needs the qualifications in Section5 below. No candidate or nonlinear closure is certified here.

## 1. The unweighted numerical range

For every test h, transport contributes -(c+1)||h||_2^2 and P0 contributes at most sup theta ||h||_2^2. Therefore the numerical abscissa nu satisfies

    nu<=-(c+1)+sup theta+kappa.

For the converse fix a point off the axes and a unit top eigenvector xi of M there. Take a compactly supported smooth amplitude phi in a small ball and phi cos(n xi.X). Reflect the four disjoint copies with the S1 signs. On each packet R_j acts, up to an L2 error tending to zero, as -xi_j phi sin(n xi.X). This follows by dominated convergence of the shifted Fourier multiplier. Boundedness of M controls the quadratic-form errors; disjoint support controls the cross terms. The packets are weakly null, so compact K contributes zero in the limit. Reflection covariance of M makes all four limits equal. Shrinking the ball gives

    nu>=-(c+1)+sup theta.

Points on the axes follow by continuity. Thus L1 is correct. This is a numerical-range statement, not an assertion of the spectral bound.

## 2. Exact double-commutator identity

Let b be real, bounded, with distributional grad b in L2. Put

    T_b=sum_j R_j^* b R_j-b.

It is self-adjoint. For b in L2 with grad b in L2 its Fourier kernel, using the nonunitary Fourier transform, is

    (2pi)^-2 [cos(angle(xi,eta))-1] bhat(xi-eta).

Consequently

    ||T_b||_HS^2=(2pi)^-2 I ||grad b||_2^2,
    I=integral_R2 [1-cos(angle(eta+e,eta))]^2 deta,

where e is any unit vector. The scaling factor is |xi-eta|^2, exactly as required by the gradient norm.

Here is an independent evaluation of I. Translate the two foci to plus and minus1/2. In bipolar coordinates (tau,sigma), the area element is (1/4)(cosh tau-cos sigma)^-2 d tau d sigma and the angle cosine is cos sigma. For0<sigma<pi,

    integral_R (cosh tau-cos sigma)^-1 d tau
        =2(pi-sigma)/sin sigma,

obtained by v=tanh(tau/2). Differentiate with respect to cos sigma and use the equal contribution from pi<sigma<2pi. Substituting t=pi-sigma gives

    I=integral_0^pi (1+cos t)^2(sin t-t cos t)/sin^3 t dt.

With t=2u this integrand becomes

    2cot^2 u-2u cos u/sin^3 u+4u cot u.

An antiderivative is

    -cot u+u/sin^2 u-2u+4u log sin u
        -4 integral_0^u log sin v dv.

Its limit at0 is0. If J=integral_0^(pi/2) log sin u du, reflection gives the same integral for log cos u, and the double-angle formula gives2J=J-(pi/2)log2. Thus J=-(pi/2)log2. Evaluating the antiderivative yields I=pi(2log2-1/2). Hence

    ||T_b||_HS=C_T ||grad b||_2,
    C_T=sqrt((4log2-1)/(8pi)).

For completeness the extension to bounded b not in L2 does not use a square of a Fourier delta. Let H_t be the heat semigroup and approximate b by H_epsilon b-H_R b. These differences belong to H1: their Fourier multipliers cancel at zero, or equivalently integrate Delta H_t b over the finite time interval. Their gradients converge in L2 to grad b as epsilon tends to0 and R tends to infinity. They are uniformly bounded by2||b||_infinity. Moreover grad H_R b tends uniformly to0, since its L-infinity norm is bounded by C R^-1/2||grad b||_2. A subsequence of H_R b therefore converges locally uniformly to a constant. On that subsequence the multiplication operators converge strongly to multiplication by b minus that constant. The displayed Hilbert-Schmidt identity makes T of the approximants Cauchy in Hilbert-Schmidt norm. Its strong limit is T_b because constants cancel. This proves the full bounded-gradient scope claimed in Lemma C.

## 3. The main weighted estimate

Let psi be bounded, even in both coordinates and locally Lipschitz, with g=V.grad psi bounded. Put w=exp psi, Psi=osc psi. Assume theta<=theta_c+theta_1 with theta_c>=0, theta_1>=0 bounded and grad theta_1 in L2. For k=wh, the transport contribution is exactly

    -integral (1+c+g)|k|^2.

The difference wQw^-1-Q is w grad rho.[U,w^-1]. Since ||U||<=1, subtracting the midpoint of the range of w^-1 gives

    ||[U,w^-1]||<=sup w^-1-inf w^-1.

The conjugation cost is at most omega=||w grad rho||_infinity(sup w^-1-inf w^-1), which is at most ||grad rho||_infinity(exp Psi-1). Applying Section2 to theta_1 gives

    <Qk,k><=integral(theta_c+theta_1)|k|^2
                 +(kappa+C_T||grad theta_1||_2)||k||_2^2.

Therefore the weighted energy rate is at least

    ess inf(1+c+g-theta_1)-theta_c-kappa
        -C_T||grad theta_1||_2-omega.

This confirms L2. The identity applies first to compact tests and then by its stated domain/core hypothesis to a generator. A positive rate beta gives weighted semigroup decay exp(-beta t), unweighted decay at most exp(Psi-beta t), and inverse norm at most exp(Psi)/beta. Perturbed transport adds the separately stated cost ||U[k].grad psi||_infinity. These conclusions retain the generator and core assumptions.

## 4. The optional first-commutator HS bound is false

For every nonzero real f in C_c^infinity(R2), [U,f] is not Hilbert-Schmidt as a map from scalar L2 to vector L2. Its Fourier kernel is

    (2pi)^-2[m(eta+z)-m(eta)] fhat(z), z=xi-eta.

Write eta=r e(theta). The angular symbol is m(theta)=(cos theta sin theta,-cos^2 theta), so m'(theta)=(cos2theta,sin2theta) and |m'(theta)|=1. For fixed z!=0, Taylor expansion uniformly in theta gives

    m(r e(theta)+z)-m(r e(theta))
       =r^-1 m'(theta)(z.e_perp(theta))+O_z(r^-2).

The angular integral of the squared norm is therefore

    pi |z|^2/r^2+O_z(r^-3).

Its integral against r dr diverges logarithmically. A nonzero compactly supported smooth f has fhat nonzero on a positive-measure set away from z=0. Tonelli's theorem then proves that the full squared kernel integral is infinite. In particular choose psi=-log(1+epsilon f) for a real smooth even bump f with1+epsilon f>0. Then w^-1=1+epsilon f and [U,w^-1] is not Hilbert-Schmidt, although grad psi is in L2. Thus there is no finite universal C_U' in the Section8 suggestion. The operator-norm oscillation bound in Section3 remains valid; the double commutator of Section2 has stronger cancellation and is not affected.

## 5. Orbit-budget qualifications

The same packets as Section1, with amplitude w phi, confirm L3 at Lebesgue points of g:

    nu_w>=-(c+1)+ess sup(theta-g).

The commutator contributes zero on each fixed-amplitude high-frequency packet by the homogeneous symbol limit, without an HS claim. Use smooth local amplitudes approaching the ball indicator when shrinking to a Lebesgue point, rather than calling the indicator a smooth test.

For a locally Lipschitz psi, the chain-rule equality with g holds for almost every orbit, not for every chosen representative of the merely measurable g. The required orbit inequality does extend to every orbit: first integrate g>=theta-lambda on almost every orbit, then pass to all starting points using continuity of psi, the flow, and the integral of the continuous function theta-lambda. Thus osc psi>=sup_(X,T>=0) integral_0^T(theta-lambda)(Phi_t X)dt is valid under complete continuous flow. It is unnecessary to extend the equality containing g itself.

The assertions about a compactly supported Lindley weight require a uniform negative drift beyond a compact annulus, for example theta_1 tends to0 at the origin and infinity and lambda>0. The two inequalities V.X>=m_V r^2 and theta_1<lambda outside an annulus alone do not ensure compact support. For a counterexample take V=cX and, for log r>=2, theta_1(r)=lambda-(log r)^-2. Choose a smooth radial bump in a finite inner annulus with accumulated positive excess larger than the remaining integral of this negative tail, and make theta_1=0 near0. It is smooth, bounded, nonnegative, has grad theta_1 in L2 and is below lambda outside an annulus. The future negative integral is finite, so the positive Lindley workload never drains and remains positive for arbitrarily large r. Its orbit budget is finite but its support is not compact.

Under the stronger uniform negative-drift assumption, the past maximizing interval and the time needed to drain the workload have uniform finite bounds on its compact support. The flow is Lipschitz on these finite intervals, so taking the supremum preserves Lipschitz continuity. The workload derivative formula holds almost everywhere along each orbit. At a time when a positive workload reaches zero with strictly negative drift, it has different left and right derivatives. Thus the word everywhere in L4 must be replaced by almost everywhere or by the appropriate one-sided statement. No such qualification changes the energy argument, which uses g almost everywhere.

Dependencies: the elementary Fourier packet calculation, the stated compact remainder and complete-flow hypotheses, direct bipolar integration, heat approximation, and the chain rule for locally Lipschitz functions. The numerical cost model and candidate table are outside the proved assertions of this audit.
