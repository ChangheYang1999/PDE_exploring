# Oscillatory negative spherical source with small gradient excess

## 1. Exact statement and scope

Fix0<beta<1 and L>0. Put t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta, D=k^2+2, K0=D/2, H=t^2(k^2+4)/D and C_s=mt^2/D. For every sufficiently small delta>0 there is a smooth divergence-free field U on R3, uniformly decaying with all its derivatives, such that at every fixed center a

    E_a(R)=L R^beta+O_a(R^-1),
    G_a(R)=beta L(H+delta)log R+O_a(1),
    K_a^-(R)=beta L kappa log R+O_a(1),
    J_a(R)=beta L(C_s+kappa)log R+O_a(1),
    kappa>=delta/(4m)>0.

Here E_a is ball energy, q=tr((DU)^2), Q_a(r)=integral_S2 q(a+rn)dn,

    G_a(R)=integral_(1<|y-a|<R)|y-a|^(2-beta)|DU|_F^2dy,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr.

The constants in the remainders may depend on delta,beta,L and a. The field has a homogeneous degree-one leading velocity with relative error O(r^-k), but its derivative has a nonconstant oscillating leading term. A smooth Newton pressure solves the Poisson equation. Nevertheless the full rotating Euler momentum equation fails for every real c,omega and any C1 pressure. Thus this is a kinematic obstruction to an o(delta) negative-spherical-source or upward J stability estimate, even under the strong energy remainder. It is not an Euler example or a sharp-constant theorem.

This proof independently reconstructs all eight sections and56manual obligations of source72facc3a, retained in `verification`. No unconfirmed LIT389 assertion is used.

## 2. Periodic pulse and exact coefficients

Choose a fixed smooth b supported in(-1/2,1/2), with0<=b<=1 and b=1 on[-1/4,1/4]. Let B1=integral b, B2=integral b^2. Then0<B2<=1 and B1^2<=B2. Set

    f0=sqrt(beta L/K0), S0=beta L C_s,
    c0=-t f0>0, A=4S0/c0,
    d_beta=4m^2t^2/D,
    theta0=min(1/4,beta/(2d_beta)).

For0<theta<theta0, define on the period cell(-1/2,1/2)

    g(s)=A[theta B1-b(s/theta)]

and extend periodically. The scaled bump is supported strictly inside the cell, so the periodic extension is smooth. Its mean is zero, and mean(g^2)=A^2(theta B2-theta^2 B1^2). Integrating a zero-mean periodic function gives a periodic primitive; subtract that primitive's mean before integrating again. This constructs smooth periodic w with w''=g. All derivatives of w are bounded at each fixed theta; no uniformity as theta decreases is asserted.

Let Qstar=S0+c0g=S0[1+4theta B1-4b(s/theta)]. It is positive outside the pulse. On |s|<=theta/4 it is at most-2S0, because theta B1<1/4. This plateau has length theta/2. Consequently

    kappa_theta=mean([-Qstar]_+)/(beta L)
       =C_s theta integral_(-1/2)^(1/2)[4b(u)-1-4theta B1]_+du
       >=C_s theta.

Define delta_theta=d_beta(theta B2-theta^2 B1^2). Direct algebra gives A^2/(2beta L)=d_beta and C_s/d_beta=1/(4m). Also

    (3/4)d_beta B2 theta<=delta_theta<=d_beta theta<beta/2,
    delta_theta'=d_beta(B2-2theta B1^2)>0.

Thus kappa_theta>=delta_theta/(4m). Continuity and strict monotonicity give every delta in an interval(0,delta0). Dominated convergence gives

    lim_(theta->0) kappa_theta/delta_theta
       =integral[4b(u)-1]_+du/(4m B2)>0.

The plateau proves strict positivity of the numerator.

## 3. Solenoidal field and full derivative energy

Write z=log r, s=r^k. With the real harmonic Y(n)=sqrt(3/(4pi))n_3, integral Y^2=1 and -Delta_S Y=2Y, define on a far exterior

    f(z)=f0+k^-2 r^-2k w(r^k),
    U(rn)=r^t[fY n+(f'+kf)grad_S Y/2].

Primes on f mean z derivatives and primes on w mean s derivatives. The divergence is r^(t-1)[(f'+kf)Y+(f'+kf)Delta_S Y/2]=0. Differentiation gives exactly

    f'=-(2/k)r^-2k w+(1/k)r^-k w',
    f''=4r^-2k w-3r^-k w'+g(r^k).

Therefore f-f0=O(r^-2k), f'=O(r^-k), f''=g(r^k)+O(r^-k). The velocity error relative to its homogeneous leading field is O(r^-k). For integer j>=1,

    |D^j U|=O_(j,theta)(r^(t-j+(j-1)k)).

Indeed the largest oscillating velocity term has amplitude r^(t-k). Each phase derivative costs r^(k-1), and each angular or nonphase derivative costs r^-1, a smaller power. The homogeneous part has rate r^(t-j), bounded by the displayed rate. Induction on j proves the estimate; its exponent is t-1+(j-1)(k-1)<0. Every fixed derivative therefore decays.

The exact spherical velocity energy and Cartesian gradient energy, after removing the homogeneous radial factors, are

    K=f^2+(f'+kf)^2/2,
    Dpol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/2.

For verification, the integrated radial derivative contributes (f'+tf)^2 and half the last square. The integrated angular derivative contributes

    4f^2-4f(f'+kf)+(f'+kf)^2=(f'+tf)^2,

using k-2=t. These are Cartesian derivatives of vector components; no scalar substitution is made. Substitution of the exact f derivatives gives

    K=beta L+O(r^-k),
    Dpol=beta L H+tk f0 g(r^k)+g(r^k)^2/2+O(r^-k).

The constant identity is H K0=t^2(2+k^2/2). All error terms are integrable in z at infinity.

## 4. Spherical source and logarithmic means

For a smooth divergence-free field write N(r)=integral_(partial B_r)|U.n|^2 and T(r)=integral_(partial B_r)|U|^2. The divergence theorem applied to q=div((U.grad)U), followed by angular integration by parts and div U=0, gives

    integral_(B_r)q=N'(r)-(T(r)-N(r))/r.

For example, the angular term integral U_T.grad_S U_r equals integral U_r(r partial_r U_r+2U_r), which produces this formula. After differentiating, the right side depends only on the local exterior data, independently of the choice of smooth core. Since N=r^(beta-1)f^2 and T=r^(beta-1)K,

    Qflat(z)=r^(5-beta)Q_0(r)
       =(f^2)''+(2beta-2)(f^2)'+beta(beta-2)f^2-K'-(beta-2)K.

Here K'=2ff'+(f'+kf)(f''+kf'), so no f''' occurs. The coefficient of g in (f^2)''-K' is(2-k)f0=-t f0=c0. The constant term is m(K0-beta)f0^2=S0, because K0-beta=t^2/2. All remaining terms are O(r^-k). Thus

    Qflat(z)=Qstar(r^k)+O(r^-k).

For every continuous period-one F, the zero-mean part F-mean F has a bounded primitive. Substitution s=e^(kz) and integration by parts against that primitive show

    integral_(z0)^Z F(e^(kz))dz=mean(F)(Z-z0)+O(1).

The zero-mean remainder integral actually converges, since its integrated remainder is bounded by a constant times integral s^-2 ds. Apply this to g,g^2 and the continuous functions [Qstar]_+ and [-Qstar]_+. Positive parts are1-Lipschitz, so the integrable error in Qflat stays integrable after either truncation. The critical radial weights convert the G,J and K^- integrals exactly to their logarithmic forms. Their origin-centered coefficients are precisely those of Section1, since mean Qstar=S0 and mean[Qstar]_+=S0+mean[-Qstar]_+. On arbitrarily distant phase plateaus, the error tends to zero while Qstar<=-2S0, so the spherical source is negative on infinitely many exterior radial intervals.

## 5. Strong energy remainder and exact core correction

Let d=f-f0. An exact expansion is

    K-beta L=k f0 f'+2K0 f0 d+K0d^2+k d f'+f'^2/2.

All terms except k f0 f' are O(r^-2k); the exceptional term equals f0r^-k w'(r^k)-2f0r^-2k w(r^k). Because k>beta, the energy difference r^(beta-1)(K-beta L) is absolutely integrable at infinity. Define

    Tcorr(R)=integral_R^infinity r^(beta-1)(K-beta L)dr.

For its leading term use r^(beta-1-k)w'(r^k)=k^-1 r^(beta-2k)d[w(r^k)]/dr. Integration by parts, boundedness of w and beta-2k=-1 give Tcorr(R)=O(R^-1). The other terms satisfy the same bound by absolute integration.

Choose a large R0 and arrange the core energy to be exactly L R0^beta-Tcorr(R0). Then direct addition of the exterior integral, without differentiating any remainder, gives

    E_0(R)=L R^beta-Tcorr(R)=L R^beta+O(R^-1).

The subtracted tail constant is essential. An arbitrary compact completion would generally leave an O(1) constant.

## 6. Smooth exact-energy core and failure of momentum

Put F(r)=r^t f(log r). The exterior field is FY n+(rF'+2F)grad_S Y/2. Continue F by the constant F(R0) on r<=R0-h and smoothly interpolate on the intervening width h to the exterior F. A cutoff multiplies a difference O(h), so F and F' stay bounded as h decreases at fixed R0,theta. The transition energy tends to zero. The inner velocity is sqrt(3/(4pi))F(R0)e3, and its limiting ball energy is

    R0^3F(R0)^2=f0^2 R0^beta+O(R0^(beta-2k)).

Since f0^2=beta L/K0<L, a sufficiently large R0 followed by a sufficiently small h leaves a positive deficit relative to the corrected target in Section5. Take a smooth nonnegative radial psi supported in r<1/2 and equal to1 near0. With Jv=e3 cross v, the solenoidal W=psi Jy is pointwise perpendicular to the zonal poloidal completion. Adding a0W, with a0=sqrt(deficit/integral|W|^2)>0, fills the deficit exactly, with no energy cross term.

Near0, U=d e3+a0 Jy. Its vorticity is the constant2a0e3 on a whole neighborhood and DU=a0J. With B=(cI-omega J)y+U, the curl of the pressure-free rotating momentum residual is

    Omega+B.grad Omega-(Omega.grad)U+omega J Omega=2a0e3.

Every term after Omega vanishes there. This holds for all real c,omega. A C1 pressure gradient has zero distributional curl and cannot repair the equation.

The completed q is smooth and O(r^(beta-5)), by the first-derivative bound. The Newton integral P(y)=integral q(x)/(4pi|y-x|)dx converges absolutely: the local kernel is integrable and the far radial bound is r^(beta-4). It solves -Delta P=q distributionally and is smooth by local elliptic regularity. Only the Poisson relation is proved.

## 7. Every fixed center

The poloidal velocity is even and the compact swirl is odd, with pointwise zero product. Hence |U|^2 is even. The first derivative of E_a(R) with respect to the center at a=0 is integral_(partial B_R)|U|^2 n and vanishes. The second center derivative is bounded by a sphere integral of |grad(|U|^2)|=O(R^(2t-1)), hence is O_a(R^(2t+1))=O_a(R^(beta-2)), uniformly on a bounded set of centers. Taylor's theorem and beta-2<-1 preserve the O(R^-1) energy remainder.

The first two derivative bounds give

    |grad(|DU|^2)|+|grad q|=O(r^(2t-3+k)).

A fixed translation changes these densities by that order. After the critical radial weight and Jacobian, the bound is a constant times r^(k-2), integrable because k<1. Thus G_a-G_0=O_a(1). Comparing q(a+rn) directly with q(rn), integrating on the sphere, and then using the1-Lipschitz positive-part map gives the same conclusion for J_a-J_0 and K_a^--K_0^-. All inner annuli contribute finite constants. No translation of the Euler equation is used.

## 8. Conclusions and comparison status

The whole-space fields have the exact coefficients of Section1 for every sufficiently small delta. Their nonzero negative-spherical coefficient is bounded below by a positive constant times delta, and its ratio to delta has a positive finite limit. Therefore neither that coefficient nor the upward J deviation has a uniform o(delta) bound in this class. The construction itself proves no universal upper estimate; any matching upper estimate requires a separate theorem.

The leading derivative oscillation is genuine: g is nonconstant, and the f'' term enters the Cartesian gradient nontrivially wherever grad_S Y is nonzero. Phase sequences with different g values therefore give different normalized derivative limits, although the normalized velocity converges. All derivatives still decay by Section3. This prevents substituting derivative asymptotics for velocity asymptotics without proof.

The existing configured model A comparison is reconciled in Section9. Actual provider execution is independently unattested. No mathematical computation, diagnostic execution, formal build or fresh source retrieval was used in this reconstruction. The universal optimal constant, any automatic Euler radial-phase rigidity, and the unrestricted arbitrary-rotation conjecture remain OPEN.

## 9. Independent comparison and a family-specific upper bound

The complete A comparison retained as in the team records, SHA2566ebc74e2d0fe990d6db6a09267f40a15c9c6e614440c2cf802e2e04dfbbd2e98, was read, including items1-11 and remarks R1-R4. Its analytical conclusions agree with Sections1-8. In particular no third derivative of f is needed to compute either the gradient energy or the pressure source. The exact correction to the core energy has the minus sign in Section5. The center estimates use only the stated derivative rates and the even energy density; no centered symmetry is assumed for the Euler equation.

R1 yields a useful additional inequality confined to this explicit family. For0<=b<=1,

    [4b-1]_+<=4b^2,

because4b^2-(4b-1)=(2b-1)^2 and4b^2>=0. Therefore

    kappa_theta<=4 C_s theta B2,
    delta_theta>=(3/4)d_beta B2 theta,
    1/(4m)<=kappa_theta/delta_theta<=4/(3m).

The limiting ratio in Section2 is at most1/m. This establishes two-sided linear order within the family without any use of pending LIT391. It does not prove a universal upper bound over all solenoidal fields.

R2 follows exactly from t-2+k=2t: the second derivative bound here is O(r^(2t)), slower than the homogeneous rate O(r^(t-2)). The genuinely oscillating coefficient in the second logarithmic derivative of f prevents a homogeneous leading gradient. R3 identifies the leading velocity as the pure poloidal endpoint of the previously confirmed degree-one family. Its source already changes sign pointwise; the new oscillation makes the spherical integral itself negative. R4 correctly keeps all remainder constants dependent on theta. The order conclusion compares exact logarithmic coefficients of separate fields and needs no uniform remainder as theta tends to zero.

The comparison's symbolic and sampled diagnostics are not certified or used as proofs here. No numerical computation was performed for this review. The existing A agent is configured as model; actual provider execution remains independently unattested. The constructions provide no counterexample to the Euler profile conjecture because the full momentum residual has nonzero curl in the core for every c,omega.
