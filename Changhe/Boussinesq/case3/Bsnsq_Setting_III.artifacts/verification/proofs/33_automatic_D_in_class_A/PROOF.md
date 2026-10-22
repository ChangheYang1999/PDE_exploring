# An automatic derivative-decay bootstrap from transported temperature

Date:2026-10-20. Status: CONFIRMED by the independent verifier on 2026-10-20 after checking the proof below and the lead's distinct double div-curl proof. Recent requests to actual Claude Opus 5.5 produced no usable audit text; they are not endorsements.

## Theorem

Let beta>=2. Let Theta,Omega,V be smooth on R2 and satisfy

    W=beta X+V, div V=0, -curl V=Omega, V(0)=0, V=o(|X|),
    W.gradTheta=(beta-2)Theta,
    W.gradOmega+Omega=Theta_x,
    |Omega(X)|<=C(1+|X|)^(-delta), delta>0,

where V is the canonical whole-plane relative inverse of Omega. No derivative bound at infinity is assumed. Then, for every

    0<kappa<min(delta,1), gamma=min(kappa,2/beta),

there are finite constants such that

    |DV(X)|<=C |X|^(-gamma)                             (1)

outside a sufficiently large ball. Hence the orbit-integral condition(D) holds, with upper bound C R^(-gamma).

This argument removes the extra derivative hypothesis from the scattering theorem within the power-decay class A. It is not a nonexistence theorem for that class or for the broader prompt. The mechanism uses both transport equations: (T) supplies a fixed positive Hölder exponent for temperature on rescaled annuli, and (V) permits integration by parts against that Hölder temperature in a directional velocity estimate.

## 1. Annular velocity bounds with a small logarithmic modulus

Fix kappa as above. The relative inverse and the vorticity power bound give

    |V(X)|<=C(1+|X|)^(1-kappa).                          (2)

Here a weaker exponent than delta was chosen to cover logarithmic and bounded cases without endpoints. One can prove(2) directly by splitting the once-subtracted integral into |Y|<2|X| and its complement. In the first region the singular kernels are locally integrable against bounded Omega, and shell integration gives O(1+r^(1-kappa)); in the exterior use |K(X-Y)-K(-Y)|<=Cr/|Y|^2 and integrate the decaying source. When delta>=1, the resulting bounded or logarithmic bound is weaker than(2), as required.

We also need a difference bound that does not follow by differentiating(2). If P,Q lie in the annulus r/2<=|X|<=2r, h=|P-Q|<=r/8, then

    |V(P)-V(Q)|<=C r^(-kappa) h[1+log(r/h)].            (3)

To prove it, split the integral into the union of the two radius-2h balls about P,Q, the nearby region out to distance r/4 from P, and the remaining region. On the first two regions Omega is bounded by C r^(-delta). The kernels give respectively C r^(-delta)h and C r^(-delta)h log(r/h). In the remaining region the mean-value bound gives

    C h integral_{|P-Y|>=c r} |Omega(Y)|/|P-Y|^2 dY
       <=C h r^(-kappa).

For this last estimate split |Y|<=r/4, r/4<|Y|<4r, and |Y|>=4r. Their bounds are respectively

    C r^(-2) integral_0^(r/4) s(1+s)^(-delta)ds,
    C r^(-delta), C r^(-delta),

all bounded by C r^(-kappa). Minor changes of the radii handle the boundaries of the near regions. For h comparable to r, (2) extends(3) with a larger constant. The fixed relative subtraction has cancelled in the difference, so it adds no term to(3).

## 2. Polar characteristic equations

Take an exterior radius r0 large enough that W.radial>=beta r/2. Put s=log r, e(theta)=(cos theta,sin theta), and define

    v(s,theta)=V(e^s e(theta))/e^s,
    v_r=v.e, v_t=v.e_perp,
    a(s,theta)=v_t/(beta+v_r),
    m=(beta-2)/beta,
    b(s,theta)=(beta-2)/(beta+v_r)-m,
    H(s,theta)=e^(-ms)Theta(e^s e(theta)).

Since dr/dt=r(beta+v_r), the two exact equations are

    dtheta/ds=a(s,theta),
    H_s+a H_theta=b H.                                 (4)

Equations(2)-(3), including the smooth angular dependence of e, imply, for s>=s0=log r0,

    |a|+|b|<=C e^(-kappa s),
    |a(s,theta)-a(s,theta')|+|b(s,theta)-b(s,theta')|
       <=L(s) omega(d(theta,theta')),
    L(s)=C e^(-kappa s), omega(h)=h log(e/h), 0<h<=1.    (5)

For larger angular distances, increase constants and use boundedness. In particular L is integrable on[s0,infinity). These are zero-order logarithmic moduli, not bounds on a_theta or b_theta.

## 3. Uniform Hölder control of angular characteristic maps

Let theta_i(s), i=1,2, be two angular solutions on any interval inside[s0,infinity). Their geodesic separation h satisfies the upper and lower scalar differential bounds |h'|<=L(s)omega(h) whenever 0<h<=1, apart from the harmless geodesic cut where we instead use boundedness. Integration of the Osgood inequality gives a uniform exponent

    alpha=exp(-integral_s0^infinity L(s)ds)>0

and a constant C such that the angular flow from any s1 to s2 and its inverse satisfy

    d(theta_1(s2),theta_2(s2))<=C d(theta_1(s1),theta_2(s1))^alpha,
    d(theta_1(s1),theta_2(s1))<=C d(theta_1(s2),theta_2(s2))^alpha.   (6)

For clarity, on an interval where h<=1 one has

    d/ds log(e/h)>=-L(s)log(e/h)

in the forward comparison. Thus h(s2)<=e h(s1)^alpha. The identical comparison for the reversed equation gives the inverse bound. If the separation crosses1, the estimate follows by stopping at the first crossing; enlarging C covers all initial separations on the compact circle. Smoothness of the coefficients ensures classical diffeomorphisms for finite s intervals. No uniform bound on their derivatives was used.

## 4. Temperature is uniformly Hölder on rescaled annuli

Equation(4) along an angular characteristic gives

    H(s,theta(s))=H(s0,theta(s0)) exp(integral_s0^s b(v,theta(v))dv).

The initial circle is compact and smooth, while b is uniformly integrable. Hence |H|<=C everywhere outside r0. Compare two final angles of separation h at the same s. By(6), their entire backward angular trajectories have separation at most C h^alpha. The initial H values differ by at most C h^alpha. Equation(5) bounds the difference of the two exponential integrals by

    C h^alpha[1+|log h|] integral_s0^infinity L(v)dv.

Thus, for any fixed 0<sigma<alpha,

    |H(s,theta)-H(s,theta')|<=C_sigma d(theta,theta')^sigma        (7)

uniformly for all s>=s0. The formula compares signed initial values directly; it never takes log H and remains valid at temperature zeros.

For radial comparison, take s1,s2 with bounded difference and transport an angle theta1 from s1 to s2. The angle moves by at most C|s2-s1|, and H changes along that characteristic by at most C|s2-s1|. Combining this with(7) at s2 yields

    |H(s1,theta1)-H(s2,theta2)|
       <=C(|s1-s2|+d(theta1,theta2))^sigma              (8)

for points in a fixed-ratio annulus, with a constant independent of its large radius. The linear term is absorbed into the sigma power on bounded intervals. Translating polar distances back to Cartesian distances, and multiplying by r^m, proves

    sup_{B(X,r/4)}|Theta|<=C r^m,
    [Theta]_{C^sigma(B(X,r/4))}<=C r^(m-sigma), r=|X| large.      (9)

For the radial factor use |r1^m-r2^m|<=C r^(m-1)|r1-r2| on that annulus, and |r1-r2|<=Cr. No a priori temperature derivative bound was used.

## 5. Directional div-curl estimate using Hölder temperature

Fix X with r=|X| large. Put w=|W(X)|, e=W(X)/w and A=DV(X). In the oriented orthonormal basis(e,e_perp), divergence and curl give

    A=[[a,c+Omega(X)],[c,-a]],
    |A|<=C(|Ae|+|Omega(X)|).                            (10)

Thus only one directional derivative of V needs estimation. Let ell=r/16 and choose a smooth radial cutoff chi_ell(Z), equal to1 for |Z|<=ell and0 for |Z|>=2ell. Differentiating the relative inverse in distributions gives

    Ae=integral [partial_e K(X-Y)]Omega(Y)dY.

The part with1-chi_ell has no singularity and is O(r^(-kappa)), by the far integral estimate used in(3). In the local part write W(X)=W(Y)+(W(X)-W(Y)). The first contribution, integrated by parts in Y using div W=2beta and the vorticity equation, is

    (1/w) integral K(X-Y) {
       chi_ell(X-Y)[Theta_x(Y)+(2beta-1)Omega(Y)]
       +Omega(Y) W(Y).grad_Y chi_ell(X-Y)}dY.            (11)

This includes the distributional delta term in the derivative of K. The terms in(11) involving Omega are O(r^(-delta)): use w>=cr, |W(Y)|<=Cr, |Omega(Y)|<=Cr^(-delta), |K|<=C/|X-Y| and the cutoff support. The term containing Theta_x is the crucial one. Integrate by parts once more:

    integral K(X-Y)chi_ell(X-Y)Theta_x(Y)dY
       =-integral partial_{Y1}[K(X-Y)chi_ell(X-Y)]
                   [Theta(Y)-Theta(X)]dY.              (12)

Subtracting Theta(X) is legitimate because the distributional derivative of the compactly supported locally integrable kernel K chi_ell has integral zero. Its delta term annihilates the displayed difference. Equation(9) and polar integration give an ordinary absolute bound for the remaining kernel:

    abs((12))<=C [Theta]_{C^sigma(B(X,r/4))} ell^sigma
              <=C r^m.

After division by w>=cr, the temperature contribution is O(r^(m-1))=O(r^(-2/beta)). This estimate uses positive Hölder regularity, not a bound on Theta_x.

The remaining local commutator is

    (1/w) integral chi_ell(X-Y)
        [W(X)-W(Y)].grad K(X-Y) Omega(Y)dY.              (13)

Its delta term vanishes. For rho=|X-Y|<=2ell, equations(3) and W=beta X+V give

    |W(X)-W(Y)|<=beta rho+C r^(-kappa)rho[1+log(r/rho)].

The absolute integral in(13) is consequently bounded by

    C r^(-1-delta) integral_0^(2ell)
            [1+r^(-kappa)(1+log(r/rho))]d rho
       <=C r^(-delta),                                (14)

since ell=r/16. Combining(10)-(14) proves

    |DV(X)|<=C[r^(-kappa)+r^(-delta)+r^(-2/beta)],

which is(1).

## 6. Orbit integration and scope

Sublinearity gives |phi_t Y|>=|Y| exp(beta t/2) for every sufficiently large starting point Y and all t>=0. Inserting(1),

    integral_0^infinity |DV(phi_tY)|dt
       <=C |Y|^(-gamma) integral_0^infinity exp(-beta gamma t/2)dt
       <=C' |Y|^(-gamma).

This proves(D). Together with packet23 and the circulation theorem17, it gives a nonzero continuous leading angular vorticity coefficient of order r^(-1/beta) for every nontrivial smooth class A profile. The second correction remains a trajectory statement unless a separate fixed-angle expansion is justified. No full YES or NO follows.

## Dependencies and origin of the argument

The power bound and local difference kernel estimates are derived above. The angular Osgood estimate is proved by a scalar integration, and the temperature Hölder bound follows from its exact transport formula. The directional integration by parts follows the useful Lemma3.1 in lead astra/tailD/PROOF.md, but changes its estimate of the Theta_x term by a second integration by parts against the Hölder temperature. That extra argument closes the bootstrap gap. It was independently rechecked, including the Osgood estimate, the distributional subtraction and both cutoff boundary terms. The disjoint-strip counterexamples to(D) do not contradict it because they fail the vorticity equation. No formalization or numerical proof is claimed.


## 7. Independent check of the lead's second proof and sharper class A rate

The lead's `astra/tailD/PROOF.md`, frozen in
`verification/lead_tailD_20261020T1554/PROOF.md` at the lane root, gives a shorter proof
which does not use the temperature Hölder lemma. The following is the verifier's
rederivation. All cutoffs below are frozen when their convolution is differentiated.

The vorticity bound implies Omega in L-infinity intersect L-p for a finite
p>max(1,2/delta). Kernel splitting at distances h and1 gives a global logarithmic
modulus C h(1+log(1/h)) for 0<h<=1. In the exterior use Hölder's inequality
with |K'|1_{|Z|>1} in L-p', which is valid since p'>1. Subdivision into segments
of length between1/2 and1 gives a C h bound when h>=1. Consequently

    |W(P)-W(Q)| <= C r^(1/2)|P-Q|^(1/2),

for r>=1 and |P-Q|<=r. This estimate uses no bound on DV.

Fix large X, r=|X|, and f smooth supported in B(X,r/4). Suppose
|f|<=A and |W.grad f|<=C A on this ball. For Z=K*f, w=|W(X)|>=c r,
e=W(X)/w, integration by parts gives

    w DZ(X)e = integral K(X-Y) div(W f)(Y)dY
      + integral grad K(X-Y).[W(X)-W(Y)] f(Y)dY.

The singular delta part in the second term vanishes because its coefficient is
W(X)-W(X). The remaining commutator is absolutely integrable. Since
|div(W f)|<=C A, the first term is <=C A r. The Hölder modulus bounds the
second by C A r^(1/2) integral_0^(r/4) rho^(-1/2) d rho <=C A r.
The div-curl algebra of(10), now with -curl Z=f, implies |DZ(X)|<=C A.

Apply this result to f=chi_X Theta, where chi_X=1 on B(X,r/8), is supported
in B(X,r/4), and |grad chi_X|<=C/r. Temperature transport gives
|W.grad f|<=C A_X, with A_X=sup_{B(X,r/4)}|Theta|<=C r^m.
It follows that |D[K*(chi_X Theta)](X)|<=C r^m. In the local directional
vorticity formula(11), therefore,

    integral K(X-Y)chi_X(Y)Theta_x(Y)dY
      = partial_1[K*(chi_X Theta)](X)
        - integral K(X-Y)(partial_1 chi_X)(Y)Theta(Y)dY

has magnitude <=C r^m. The other terms are exactly those already estimated
in section5. This proves the same automatic(D) conclusion independently of
sections2-4's Hölder argument.

There are two useful precisions when using the lead's formulation. First,
D(K*((1-chi_X)Omega)) means the derivative of the regularized relative inverse;
the unsubtracted remote convolution itself need not exist. Its derivative is
an absolutely convergent ordinary integral. Second, without the nontrivial B2
center data and the circulation theorem, the estimate is

    |DV| <= C(r^(-eta)+r^(-2/beta)),  0<eta<min(delta,2),

not automatically O(r^-delta) for an arbitrary prescribed delta. When
0<delta<2, the remote kernel integral is O(r^-delta), so eta may be delta.
For a nontrivial class A B2 profile, packet17's circulation bound forces
any admissible decay exponent delta to satisfy delta<=1/beta<=1/2.
Thus |DV|<=C r^-delta and |V|<=C r^(1-delta) in that class.

Differentiating(T) gives the exact vector equation for q=grad Theta,

    W.grad q = -(2 I+DV^T)q.

Every exterior orbit starts on one fixed sphere; its radius satisfies
r(t)=R0 exp(beta t+O(1)) uniformly because V/r decays with a positive power.
The newly proved(D) bound and Gronwall therefore give
|grad Theta(X)|<=C r^(-2/beta).
Packet23, combined with17 and18, gives the uniform nonzero continuous angular
vorticity tail r^(-1/beta)a(theta). This improves the source bound to
O(r^(-1/beta)); repeating the same derivative estimate with this improved
source exponent gives |DV|<=C r^(-1/beta) and |V|<=C r^(1-1/beta).
None of these consequences is a nonexistence theorem. They remain restricted
to the power-decay class, which is smaller than the prompt's broad target.
