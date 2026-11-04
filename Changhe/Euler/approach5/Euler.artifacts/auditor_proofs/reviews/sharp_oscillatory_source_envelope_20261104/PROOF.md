# Exact negative-source envelope for the radial oscillation family

## 1. Statement and notation

Fix 0<beta<1 and L>0. Put

    t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta,
    D0=k^2+2, K0=D0/2, H=t^2(k^2+4)/D0,
    C_s=mt^2/D0, f0=sqrt(beta L/K0),
    S0=beta L C_s, c0=-t f0.

In particular beta<k<1, t<0, beta-2k=-1, K0-beta=t^2/2>0 and c0>0. For each nonzero real smooth periodic function g of period one and mean zero, take its mean-zero periodic second primitive w. With r=|y|, n=y/r, z=log r, define for sufficiently large r

    Y(n)=sqrt(3/(4pi))n_3,
    f(z)=f0+k^(-2)r^(-2k)w(r^k),
    U_ext(rn)=r^t[fY n+(f'+kf)grad_S Y/2].

Primes on f mean z derivatives, and primes on w mean derivatives of its argument. The family considered here consists of the smooth divergence-free completions built in Section 4, with the exact prescribed interior energy. This is a specified kinematic family, not all divergence-free fields.

Set delta=mean(g^2)/(2beta L)>0 and kappa=mean([-S0-c0g]_+)/(beta L). Every such field has all spatial derivatives tending uniformly to zero. At each fixed center a, let E_a be its energy in B(a,R), q=tr((DU)^2), Q_a(r)=integral_S2 q(a+rn)dn, and

    G_a(R)=integral_(1<|y-a|<R)|y-a|^(2-beta)|DU|_F^2dy,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr.

Then

    E_a(R)=LR^beta+O_(a,g)(R^-1),
    G_a(R)=beta L(H+delta)log R+O_(a,g)(1),
    K_a^-(R)=beta L kappa log R+O_(a,g)(1),
    J_a(R)=beta L(C_s+kappa)log R+O_(a,g)(1).

For each prescribed delta>0 the supremum of kappa in this family is

    F_beta(delta)=[sqrt(C_s^2+4C_s delta/m)-C_s]/2.

No smooth member attains the supremum. It is strictly less than delta/m, but F_beta(delta)/delta tends to 1/m as delta decreases to zero. Every field has a smooth Newton pressure solving its Poisson equation; none solves the complete rotating Euler equation for any real c,omega.

## 2. The scalar optimization, with exact variance

Let V=S0+c0g. Its mean is S0 and

    mean(V^2)=S0^2+c0^2 mean(g^2)
             =(beta L)^2[C_s^2+4C_s delta/m],

because c0^2=2beta L C_s/m. The identity [-V]_+=(|V|-V)/2 and Cauchy-Schwarz on a period of measure one give the stated upper bound for kappa. Equality requires |V| to be constant. A continuous real V on the circle with constant positive absolute value has constant sign and is constant, forcing delta=0. Thus equality is impossible at positive delta.

Conversely set A=sqrt(S0^2+2beta L c0^2 delta)>S0 and p=(1-S0/A)/2. A periodic function V_* equal to -A on an interval of length p and to A elsewhere has mean S0 and second moment A^2. Hence g_*=(V_*-S0)/c0 has mean zero and variance v=2beta L delta. Mollifying g_* on the circle preserves mean zero and gives smooth g_n tending to g_* in L2. Their variances v_n tend to v>0. For sufficiently large n, h_n=sqrt(v/v_n)g_n is smooth, has exactly variance v, and tends to g_* in L2 and L1. The map g to mean([-S0-c0g]_+) is c0-Lipschitz in L1, so the corresponding kappa values tend to (A-S0)/(2beta L)=F_beta(delta). Section 4 supplies an admissible completion for every h_n. No uniform bound on its core radius or derivative constants is needed.

Rationalization gives

    F_beta(delta)/delta
       =2/[m(sqrt(1+4delta/(mC_s))+1)]<1/m.

Also sqrt(1+x)<=1+x/2 for x>=0 implies this ratio is at least [1-delta/(mC_s)]/m. For any 0<epsilon<1 and each 0<delta<epsilon mC_s/2, choose n so its kappa differs from F_beta(delta) by less than epsilon delta/(2m). Then kappa>(1-epsilon)delta/m. This establishes the lower approximation at every sufficiently small delta, not merely along a selected sequence. The discontinuous optimizer is never counted as a smooth velocity.

## 3. Exterior identities and logarithmic coefficients

The mean-zero primitive exists by integrating g, subtracting the first primitive's mean, then integrating again and subtracting the second primitive's mean. The harmonic Y satisfies integral Y^2=1, integral |grad_S Y|^2=2 and Delta_S Y=-2Y. The polar divergence of the displayed field is r^(t-1)[(t+2)f+f'-(f'+kf)]Y=0. Direct differentiation yields

    f'=-(2/k)r^(-2k)w+(1/k)r^-k w',
    f''=4r^(-2k)w-3r^-k w'+g(r^k).

The degree-one spherical identities, equivalently direct substitution of grad_S Y=sqrt(3/(4pi))(e3-n_3 n), give

    integral_S2 |r^-t U_ext|^2=K=f^2+(f'+kf)^2/2,
    integral_S2 |r^(1-t)DU_ext|_F^2
      =Dpol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/2.

These use the full Cartesian derivative norm. The angular contribution is 4f^2-4f(f'+kf)+(f'+kf)^2=(f'+tf)^2. Substituting the exact derivatives gives

    K=beta L+O_g(r^-k),
    Dpol=beta L H+tkf0 g(r^k)+g(r^k)^2/2+O_g(r^-k).

To check the source coefficient, use q=div div(U tensor U), valid for this smooth solenoidal field. Its radial distribution identity is

    integral_(B_r)q=N'(r)-(T(r)-N(r))/r,
    N(r)=r^(beta-1)f^2, T(r)=r^(beta-1)K.

Testing in the exterior or differentiating gives

    Qflat(z)=r^(5-beta)Q_0(r)
      =(f^2)''+(2beta-2)(f^2)'+beta(beta-2)f^2-K'-(beta-2)K
      =S0+c0g(r^k)+O_g(r^-k).

The constant is m(K0-beta)f0^2=S0. The g coefficient is (2-k)f0=-tf0=c0. Only f,f',f'' occur: no third derivative or differentiated asymptotic error is used.

For a continuous periodic function F, F-mean(F) has a bounded primitive. Substitution s=e^(kz) and integration by parts give

    integral_(z0)^Z F(e^(kz))dz=mean(F)(Z-z0)+O_F,z0(1).

Indeed the zero-mean remainder is k^-1 integral F_0(s)/s ds; its primitive is bounded, and the derivative of 1/s is integrable at infinity. Since all O(r^-k) remainders are integrable in z and the positive-part map is 1-Lipschitz, apply this formula to g, g^2 and [-S0-c0g]_+. The three logarithmic coefficients at center zero follow, including the J coefficient from mean([V]_+)=S0+mean([-V]_+).

## 4. Exact energy correction and smooth whole-space completion

Write d=f-f0. Expanding K gives the exact equality

    K-beta L=kf0 f'+2K0 f0d+K0d^2+kdf'+f'^2/2.

Apart from kf0 f', every term is O_g(r^-2k); the only possible larger term is f0 r^-k w'(r^k). The tail correction

    Tcorr(R)=integral_R^infinity r^(beta-1)(K-beta L)dr

is absolutely convergent, since beta<k. For its leading term use

    r^(beta-1-k)w'(r^k)=k^-1 r^(beta-2k) d[w(r^k)]/dr.

Integration by parts, boundedness of w and beta-2k=-1 yield Tcorr(R)=O_g(R^-1). All other terms have the same bound directly.

Let F(r)=r^t f(log r). The exterior field is FY n+(rF'+2F)grad_S Y/2. At a sufficiently large R0, join F smoothly over a thin annulus to the constant F(R0) on the inside. The difference between the exterior F and F(R0) is O(h) across an annulus of thickness h, so a cutoff with derivative O(1/h) keeps F and F' bounded as h decreases at fixed R0. Thus its annular energy tends to zero. Inside the annulus the field is the constant sqrt(3/(4pi))F(R0)e3, whose limiting ball energy is R0^3 F(R0)^2=f0^2 R0^beta+O_g(R0^-1).

Since f0^2=beta L/K0<L, choosing R0 large and then h small leaves a strictly positive deficit between this completed poloidal field V's interior energy and LR0^beta-Tcorr(R0). Let W=psi(r)Jy, where psi is smooth, nonnegative, supported in r<1/2 and equal to one near zero, and J y=e3 cross y. Then W is solenoidal, and it is pointwise perpendicular to the poloidal V. Taking a0>0 with a0^2 integral|W|^2 equal to the deficit gives U=V+a0W and

    E_0(R)=LR^beta-Tcorr(R)

for every R>=R0. The sign of the correction is essential. A generic completion would leave a nonzero constant energy error.

Near zero U=C e3+a0Jy, with C constant. Direct substitution into the pressure-free momentum expression gives

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU
       =a0Jy+a0^2J^2y+(1-c)C e3.

Its curl is 2a0e3 for every real c,omega. Adding any gradient pressure cannot remove this curl. Hence none of these completions is a full Euler profile.

## 5. Derivatives, pressure and translated centers

For every integer j>=1, differentiating the explicit exterior field gives

    |U|=O_g(r^t),
    |D^jU|=O_(j,g)(r^(t-j+(j-1)k)).

The largest oscillating velocity term has amplitude O(r^(t-k)), and each spatial derivative of its phase costs at most r^(k-1). The stated exponent includes the homogeneous part, which decays faster when j>1. As k<1 and t<0, every fixed-order derivative tends uniformly to zero. A nonconstant g nevertheless remains in the leading rescaled derivative, so derivative decay does not supply a homogeneous derivative expansion.

The smooth source q is O_g(r^(beta-5)). Thus P(y)=integral q(x)/(4pi|y-x|)dx converges absolutely for every y, solves -Delta P=q distributionally and is smooth by local elliptic regularity. This is only a Poisson pressure, consistent with the nonzero full momentum curl above.

The poloidal V is even, and W is odd and perpendicular to V, so |U|^2 is even. The first center derivative of E_a at a=0 vanishes. Its second center derivatives can be written as boundary integrals of first spatial derivatives of |U|^2. Because |U||DU|=O(r^(2t-1)), these are O_a(R^(2t+1))=O_a(R^(beta-2)), uniformly over a fixed bounded set of centers. Taylor's theorem gives E_a-E_0=O_a(R^(beta-2))=O_a(R^-1).

Likewise |grad |DU|^2|+|grad q|=O_g(r^(2t-3+k)). A fixed center translation changes the corresponding densities by this order on large spheres. The critical weight and surface measure turn the error into O_(a,g)(r^(k-2))dr, integrable because k<1. The finite inner region contributes a finite constant. Applying the same estimate before the 1-Lipschitz positive part gives O_(a,g)(1) differences for G, K^- and J. This proves every assertion at every fixed center.

## 6. Consequences for universal bounds and their limits

If a bound K_a^-/(beta L log R) in limsup is at most C_beta(M-H) for all smooth solenoidal fields in a class containing these completions, with M the finite gradient coefficient, then Section 2 forces C_beta>=1/(2-beta). The same holds for a linear upper bound on the J coefficient's deviation above C_s. Taking beta to one forces any beta-independent coefficient to be at least one. These remain true with the additional all-center O(R^-1) energy remainder, smooth Poisson pressure and decay of every derivative.

The exact nonlinear envelope F_beta is established only for the specified radial oscillation family. Its lower obstruction for a broader class does not make it an upper bound in that class. The result does not determine the optimal universal logarithmic coefficient, and gives no example or upper obstruction for the class of actual rotating Euler profiles.

## 7. Dependencies and review status

The construction uses the already confirmed LIT390 mechanism, A3181-A3182, and reproduces all needed identities, exact energy fitting and translation estimates here. Its new optimization is the scalar moment argument in Section 2. Neither the LIT393 modal constant nor any numerical computation is a premise. The original source c2ead677, all seven sections, all 46 manual obligations and its formal-status note were read. The complete existing C comparison of 11:23:02Z, SHA256 80648ccf4ad386780fcb6503b43b703502ecd6a047c3bd17f9a6d777e1247b0f, has been read and reconciled. Its analytical items1-5 agree, including the finite transition-annulus gradient cost; its numerical diagnostics and reduced-model item6 are not proof inputs. The weaker earlier fixed-family lower bound is superseded by the exact slope1/m. Existing configured model collaboration is through files; actual provider execution is independently unattested. The main arbitrary-omega conjecture remains open.
