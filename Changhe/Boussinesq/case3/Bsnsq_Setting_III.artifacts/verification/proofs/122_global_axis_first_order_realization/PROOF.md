# The complete first axis system with a flat center residual

Written 2026-10-21T04:18:01.905486+00:00, before packet122 code. Independent audit of the lead's draft4.29 dated 2026-10-21 04:10Z. Status: complete informal construction and executable controls CONFIRMED. The construction satisfies the temperature equation and the first vorticity equation on the axis. No full-plane Boussinesq profile is asserted.

## Statement, notation and dependencies

For every beta>2 and a0>0 there exist smooth Psi odd in x, Omega=-Delta Psi odd in x, and Theta even in x, with relative velocity V=U-U(0), U=(-Psi_y,Psi_x), W=beta X+V, such that:

- V is the canonical full-plane relative inverse, U is sublinear, Omega has a nonzero r^(-1/beta) tail, and DU=O(r^(-1/beta)).
- Theta>0 off the axis, Theta(0,y)=0, Theta=a0x^2+O(r^3), and W.grad Theta=(beta-2)Theta globally. It has the polynomial bound C(1+r)^[2(beta-2)/beta].
- Omega>0 for x>0, Psi_xy(0)=1+beta/2 and Omega_x(0)=4a0/beta. Every backward trajectory tends to zero.
- For R_Omega=W.grad Omega+Omega-Theta_x, d_x R_Omega(0,y)=0 on the whole axis, and every derivative of R_Omega at (0,0) is zero.

Relative to the explicit base field of packet121, Omega-Omega_e is supported in a strip |x|<=x0 and bounded by C|x|(1+|y|)^(-1-1/beta), while U-U_e is bounded by C(1+|y|)^(-1-1/beta). No claim is made for the x^3 coefficient of R_Omega at nonzero y or for R_Omega off the axis.

For reference define l=(beta-2)/2, mu=1+3beta/2, Lambda=2mu, M=2beta+1, c=1+beta/2, s=1/beta, p=(1-s)/2,

    L=3c sqrt(beta)/(4a0), h=sqrt(beta)L,
    S=L^2+x^2+(y-h)^2, S0=L^2+h^2,
    B=c/(2ph S0^(p-1)), Psi_e=-BxS^p,
    q_e(y)=4Bp[L^2+(y-h)^2]^(p-2)[2L^2+(p+1)(y-h)^2],
    b(y)=beta y-B[L^2+(y-h)^2]^p+B S0^p.

Packet121 gives b'>=l, b(0)=0, b'(0)=mu, and q_e>0 with tail Q_e|y|^(-1-s), Q_e=4Bp(p+1). Packet119 supplies the formal homogeneous center recursion and the smooth xi construction for any small perturbation preserving the source bounds. The regular singular ODE lemma is proved in packet121. We restate the application and the new cutoff argument here in full.

## The axis equations and the positive solution Q

Write g1(y)=Psi_x(0,y), g3(y)=Psi_xxx(0,y)/6, a(y)=Theta_xx(0,y)/2 and q(y)=Omega_x(0,y). Directly differentiating the original Cartesian equations, using parity and div W=2beta, gives

    b=beta y+g1(y)-g1(0), q=-g1''-6g3,
    b a'=(2b'-Lambda)a,
    d_x R_Omega=bq'+(M-b')q-2a.                 (1)

Fix b to be the base b, and set

    a(y)=a0 exp(int_0^y (2b'-Lambda)/b),          (2)
    b Q'+(M-b')Q=2a.                            (3)

The quotient in (2) is smooth across zero. To solve (3), write b=y btilde, btilde(0)=mu, kappa=(M-b')/btilde and g=2a/btilde. Then kappa0=beta/Lambda>0. The unique bounded solution near zero is

    Q(y)=int_0^1 u^(kappa0-1)
       exp[-int_u^1 (kappa(vy)-kappa0)/v dv] g(uy) du.             (4)

Indeed, this follows from the integrating factor of yQ'+kappa(y)Q=g(y); differentiating the expression verifies the equation. The inner integrand extends smoothly to v=0, and all y derivatives of its exponential and of g(uy) are bounded on a small fixed neighborhood. The integrable factor u^(kappa0-1) therefore permits differentiation to every order. Homogeneous alternatives grow as |y|^(-kappa0), so (4) is the unique bounded solution. It extends globally since b has no other zero. Positivity of a and of the outward flow solution implies Q>0 everywhere, and Q(0)=g(0)/kappa0=4a0/beta.

At either infinity,

    b=beta y+O(|y|^(1-s)), b'=beta+O(|y|^-s),
    b''=O(|y|^(-1-s)),
    (2b'-Lambda)/b=-(1+2s)/y+O(|y|^(-1-s)),
    (M-b')/b=(1+s)/y+O(|y|^(-1-s)).

The errors are integrable, so a=C_+-|y|^(-1-2s)(1+o(1)) with positive constants. An integrating factor E of (3) is c_+-|y|^(1+s)(1+o(1)), c_+-, C_+->0. On the positive half-axis, (EQ)'=2aE/b>0 is integrable at infinity, of order y^(-1-s). Its integral limit is strictly positive because EQ is already positive at any fixed starting point and increases. On the negative half-axis the derivative is negative, so EQ again increases when followed outward toward negative infinity and has a finite positive limit. Hence

    Q=C_Q,+- |y|^(-1-s)(1+o(1)), C_Q,+->0.

The ratio Q/q_e is positive continuous with positive finite limits. There is therefore K>=1 such that K^-1<=Q/q_e<=K on the entire line. From (3), Q'=O(|y|^(-2-s)); differentiation of (3), using a'=O(|y|^(-2-2s)), gives Q''=O(|y|^(-3-s)). The same estimates hold for q_e. Thus f=Q-q_e is smooth and |f|+|f'|+|f''|<=Cq_e globally. No numerical estimate of K is used in the proof.

## A compact cutoff with a controlled Laplacian

For any delta>0 there is a smooth even gamma, equal to one near [-1,1], zero outside [-T,T], with |gamma|<=1 and

    -delta<=m(t):=(t^3 gamma(t))''/(6t)<=1.       (5)

Here the quotient at zero is its smooth continuation. A useful construction avoids an unspecified asymptotic coefficient. Choose a smooth even rho1, one on [-1,1], supported in (-2,2), with 0<=rho1<=1. Choose a nonzero smooth rho on (1,2), 0<=rho<=1. On t>=0 put rho2(t)=rho(t/A) and rho3(t)=rho(t/(4A)), with A>2; extend them evenly. Their supports are disjoint from each other and rho1. Let

    mu_i=int_0^infinity t rho_i(t)dt,
    t_i=(int_0^infinity t^2 rho_i(t)dt)/mu_i,
    d2=mu1(t3-t1)/[mu2(t3-t2)],
    d3=mu1(t2-t1)/[mu3(t3-t2)].

For large A, t1<t2<t3 and both coefficients are positive. Scaling gives mu2=A^2 mu_rho, mu3=16A^2 mu_rho, t2=A t_rho, t3=4A t_rho. Thus d2,d3=O(A^-2); choose A so d2<=delta and d3<=1. The smooth even function m=rho1-d2rho2+d3rho3 obeys (5), equals one near zero and has the two exact vanishing moments int_0^infinity t m=int_0^infinity t^2 m=0.

For t>=0 define F(t)=int_0^t (t-u)6u m(u)du, and extend it oddly. Near zero F=t^3, so the odd extension is smooth. Beyond the support, F=6t int u m-6int u^2 m=0 by the two moment conditions. Also |F(t)|<=int_0^t (t-u)6u du=t^3, since |m|<=1. Set gamma=F/t^3 and extend it by one at zero. It is smooth, even, compactly supported, bounded by one, and satisfies the required identity. This proves existence of a C-infinity cutoff. Any finite-order polynomial control used in verification below checks the moment algebra but does not replace this smooth existence argument.

## The strip perturbation, positivity and full-plane inverse

Take gamma above with delta<=1/2 and delta(K-1)<=1/2, and choose eps>0 small. Put

    D(x,y)=-f(y)x^3 gamma(x/eps)/6,
    Psi1=Psi_e+D, Omega1=-Delta Psi1.

Then g1 is unchanged and g3 decreases by f/6. In particular b is unchanged, q1=q_e+f=Q, and U1(0)=U_e(0). Direct differentiation gives

    Omega1/x=Omega_e/x+f(y)m(x/eps)+(f''(y)/6)x^2 gamma(x/eps).    (6)

Uniformly for |x| small and all y, the explicit base formula gives Omega_e/x>=q_e(y)(1-Cx^2). For example differentiate it twice in x; on a bounded x strip the second derivative is bounded by C[L^2+(y-h)^2]^(p-2)<=C' q_e(y), because L>0. If f>=0, then q_e+fm>=q_e-delta f>=q_e/2. If f<0, m<=1 gives q_e+fm>=q_e+f=Q>=q_e/K. In both cases this is at least q_e/(2K). Since |f''|<=Cq_e and |gamma|<=1, (6) implies

    Omega1/x>=q_e[1/(2K)-C'(eps T)^2]>0

for sufficiently small eps. Outside the strip |x|<=eps T, the field is the base field.

The induced velocity grad-perp D is smooth, bounded, vanishes at zero and decays at infinity. Its divergence is zero and minus its curl is Omega1-Omega_e. The canonical relative inverse is well-defined for the perturbed tail class: the difference vorticity is integrable in y in a strip and locally smooth, and in particular admits the same subtracted full-plane kernel. More precisely, apply the canonical relative inverse to the difference vorticity -Delta D. This inverse and grad-perp D differ by a whole-plane harmonic vector field with sublinear growth, hence by a constant. Both relative fields vanish at zero, and grad-perp D(0)=0, so they agree. Add the already verified canonical base relative field. Thus the perturbation introduces no harmonic or fitted affine field.

The estimates |f|+|f'|+|f''|<=C(1+|y|)^(-1-s), along with compact x support and fixed eps, give |Omega1-Omega_e|<=C|x|(1+|y|)^(-1-s), |grad-perp D|<=C(1+|y|)^(-1-s), and the same y decay for its first derivatives. Therefore its vorticity is uniformly o(r^-s) and the base leading angular tail is unchanged, including near the axis. The velocity and derivative bounds stated in the theorem follow.

Further, W1,1/x changes by f'(y)x^2 gamma(x/eps)/6, whose magnitude is at most (eps T)^2 sup|f'|/6. Choose eps small enough that W1,1/x>=l/2; b'>=l is unchanged. Second stream derivatives remain bounded. The global backward-basin and smooth xi argument in packet119 therefore applies. Its temperature has the axis value a from (2), because the first equation of (1), with normalization a(0)=a0, has a unique smooth solution. Equation (3) now makes d_x R_Omega vanish everywhere on the axis.

## Making the center residual flat without changing axis data

Starting with Psi1, perform the formal homogeneous recursion from packet119. At degree n, the residual defect determines

    delta Omega_n=-(A X.grad+1)^(-1)(R_Omega)_n,
    A=diag(l,mu), -Delta D_(n+2)=delta Omega_n.

Choose the harmonic coordinate of D_(n+2) so that its xy^(n+1) coefficient is zero. This is possible and unique because the odd harmonic polynomial of that degree has a nonzero xy^(n+1) coefficient. Inductively all previous corrections are divisible by x^5 and preserve g1 and g3, hence preserve b,a,q and the entire first axis identity. Thus the coefficient of xy^(n-1) in the current residual is zero. The diagonal operator A X.grad+1 preserves this zero coefficient, so it is also absent in delta Omega_n. If D=d1 xy^(n+1)+d3 x^3y^(n-1)+..., comparison in -Delta D gives

    -n(n+1)d1-6d3=0.

Since d1=0 by the chosen complement, d3=0. Every D is divisible by x^5, closing the induction. Degrees with no possible x^5 monomial simply require D=0.

Use smooth radial cutoffs with sufficiently small supports and the Borel bounds of packet119 to realize all these D in a compactly supported C^3-small smooth sum delta. Every summand is divisible by x^5, and C-infinity convergence permits taking axis derivatives termwise. Hence delta_x(0,y)=delta_xxx(0,y)=0 for all y. The functions g1,g3,b,q, and consequently a and the first axis identity, remain unchanged exactly. Compactness and C^3-smallness preserve Omega>0 on the support (Omega1/x has a positive minimum there) and the source bounds. The normalization is preserved exactly: in packet119, I(0)=int_0^infinity B1(phi_(-t)0)dt=0, since B1(0)=0 and zero is a fixed point. Therefore xi_x(0)=exp(-I(0))=1 and Theta_xx(0)=2a0 for every such perturbation. The x^5 corrections preserve DW(0), so the same l and B1(0)=0 are used. The new global temperature from xi has the formal center series selected by the recursion. Thus all center residual derivatives vanish, while the whole-axis first-order identity continues to hold.

The added compact perturbation is contained in a strip after enlarging x0 if necessary and satisfies the stated tail bounds by adjusting constants. It has no effect on the leading angular tail. This completes the construction.

## Scope and exterior obstruction

The full vorticity PDE is not established off the axis, nor in its higher x Taylor coefficients at nonzero y. The construction prevents an exclusion based only on the listed properties, but says nothing about an argument using the complete PDE.

If the vorticity were instead changed only on a compact set, packet121 proves H=bq'+(M-b')q<0 far down the lower axis. That contradicts H=2a>0. This remains true if passing to the relative velocity changes b by a constant. The stronger no-open-exterior-interval argument using the particular F_e of packet119 requires the center drift to remain unchanged; do not silently identify b with b_e from exterior equality of U alone. The strip perturbation above does preserve the center drift but changes q outside every compact set, as required to evade that obstruction.
