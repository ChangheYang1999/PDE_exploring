# Axis normalization and a conditional primitive-tail obstruction

Status: independent informal proof answering the lead's 05:53 questions. Actual claude-opus-5-5 review 179 confirmed the conditional conclusions; its requests for explicit PDEs, a standalone primitive argument and support for the source-only limitation are incorporated below. Written follow-up 181 by the actual claude-opus-5-5 model confirmed the revisions and found no mathematical error. No full B2 existence or exclusion claim.

## Statement A: axis normalization under a zero-free axis drift

Let beta>0 and W be a smooth vector field on R² with W1(0,y)=0, b(y)=W2(0,y), b(0)=0 and b'(0)=lambda2=(3beta+2)/2. Let Theta be smooth, have the local jet Theta=a0 x²+O(|X|³), and satisfy W.gradTheta=(beta-2)Theta. If b has no zeros except 0, then Theta(0,y)=0 for all y.

This is sufficient, not a necessary hypothesis on b. In the prompt's target, Theta(0,y)=0 is explicitly imposed or an equivalent global structure must be proved. Without further information on other zeros of b, the axis ODE alone does not establish it globally.

### Proof and sharp limitation of the axis argument

Put t(y)=Theta(0,y), k=beta-2. Then b t'=k t. On each punctured neighbourhood of 0,

    k/b(y)=alpha/y+O(1), alpha=k/lambda2=2(beta-2)/(3beta+2).

A nonzero solution is a nonzero constant times |y|^alpha times a smooth positive factor with nonzero limit. For beta<2, alpha<0 and boundedness at 0 excludes it. For beta=2 the solution is constant and the center value is 0. For beta>2, 0<alpha<1, so a nonzero solution is not differentiable at 0 (also inconsistent with t=O(y³)). Thus t vanishes near 0. On each half-axis where b is nonzero, ordinary uniqueness propagates this zero, proving the statement.

Other degenerate zeros can support a smooth solution born flat at a zero. For example, choose a smooth b with b=lambda2 y near 0, b=(y-1)² near 1, b=beta y for sufficiently large |y|, and b>0 for y>0 except y=1. Such a b is constructed by positive smooth interpolation away from the specified neighbourhoods. For beta>2 set t=0 on y<=1. For y>1 solve b t'=k t with positive value at a fixed y>1. Near1 this solution equals C exp(-k/(y-1)), hence extends smoothly by 0, and at infinity it grows as a constant times y^(k/beta). This satisfies the axis transport and all center jets while being nonzero beyond 1. It is only a counterexample to an inference from the scalar axis equation, not a B2 profile. It shows why a zero-free or another proved propagation hypothesis must be stated when removing the prompt's axis normalization assumption.

## Statement B: a sufficient exterior transport hypothesis for moment necessity

Let beta>2, s=1/beta, m=1-2s. Let Psi be smooth and odd in x, Omega=-DeltaPsi, V=grad_perpPsi-grad_perpPsi(0), W=beta X+V and F=W.gradOmega+Omega. Let Theta be smooth and satisfy explicitly F=partial_x Theta, W.gradTheta=(beta-2)Theta, and Theta(0,y)=0. Assume for r>=r0 that

    |V(X)|<=C r^(1-s), |DV(X)|<=C r^-s,                    (1)
    F(X)=f(X)+O(r^(m-1-delta)), delta>0,                   (2)

uniformly in angle, where f is smooth away from 0, odd in x and homogeneous of degree m-1. Then the two finite-part constants C_+(f), C_-(f) of packet129 vanish. It is enough in (2) to have uniform o(r^(m-1)) with the corresponding global source bound; a power gap is a convenient stronger hypothesis.

Thus a remainder O_symbol(r^(m-1-s)) is sufficient together with (1) and the thermal PDE. The source remainder by itself is not sufficient. The actual thermal PDE supplies the angular differentiability that the source primitive alone does not supply.

### Proof: identify the pointwise primitive limit

The vorticity equation and the axis condition give the exact identity

    Theta(x,y)=integral_0^x F(u,y) du.

The source bound |F(X)|<=C<X>^(m-1) follows from (2) and compact smoothness. For x>=0 and lambda>=1,

    lambda^(1-m)|F(lambda u,lambda y)|<=C u^(m-1).

The right side is integrable on0<u<x because m>0. Dominated convergence and homogeneity yield

    lim_(lambda->infinity) lambda^-m Theta(lambda x,lambda y)
                      =int_0^x f(u,y)du=:T_infinity(x,y).   (3)

Evenness gives the same identity for x<0. This step alone supplies only a pointwise limit. Hypothesis (2) is used in this identification; the C1 convergence argument below instead uses (1) and the thermal PDE.

### Proof: the thermal equation supplies a C1 angular limit

Increase r0 so beta r+V_r>=beta r/2. Put tau=log r and u(tau,theta)=r^-m Theta(r cos(theta),r sin(theta)). In polar components the thermal equation becomes

    u_tau+a(tau,theta)u_theta=btilde(tau,theta)u,
    a=V_theta/(beta r+V_r),
    btilde=-m V_r/(beta r+V_r).                            (4)

Here V_theta denotes the tangential component, not a derivative. Because |partial_theta V|<=r|DV|+|V| in polar components, (1) implies

    ||a(tau,.)||_C1+||btilde(tau,.)||_C1<=C exp(-s tau).

These norms are integrable in tau. Let z(tau,eta) solve z_tau=a(tau,z) with z(tau0,eta)=eta. The flow is a circle diffeomorphism. Its derivative is exp(int a_theta), uniformly bounded above and away from 0. The integrable C1 bound makes z and z_eta uniformly Cauchy as tau->infinity; the limit is a C1 circle diffeomorphism and the inverses converge in C1. Along this flow,

    u(tau,z(tau,eta))=u(tau0,eta)
                          exp(int_tau0^tau btilde(v,z(v,eta))dv).

The exponent and its eta derivative converge uniformly by the same integrable bounds and the bound on z_eta. Therefore u(tau,.) converges in C1(S1). By (3) this limit is the restriction of T_infinity to the unit circle.

For completeness, the needed part of packet129 has a direct proof. Put a=f(1,0). For x>0 define

    H(x,y)=a x^m/m-integral_x^infinity[f(u,y)-a u^(m-1)]du.

For bounded y, the integrand is O(u^(m-2)) at infinity. Its j-th y derivative for j>=1 is O(u^(m-1-j)), so every such derivative is integrable there; x derivatives follow by differentiating the lower endpoint. Thus H is smooth near any positive horizontal-axis point. The finite parts

    C_sigma=lim_(R->infinity)[integral_0^R f(u,sigma)du-a R^m/m]

exist by the same tail estimate and smoothness near (0,sigma). Scaling on each side y of 0 and splitting the integral at x give exactly T_infinity=H+C_sign(y)|y|^m. Reflection handles negative x. Since 0<m<1, any nonzero C destroys differentiability. The C1 limit just proved therefore forces C_+=C_-=0.

Only C1 convergence is needed above. To check the warning about a source bound without the thermal PDE, take any 0<m<1 and the smooth odd source

    F=x(1+x²+y²)^((m-2)/2),
    Theta=((1+x²+y²)^(m/2)-(1+y²)^(m/2))/m.

It has partial_x Theta=F, Theta(0,y)=0 and a uniform differentiated source expansion with a two-power gap. Yet its homogeneous temperature limit is (r^m-|y|^m)/m, which is not C1 on the horizontal axis. This is a counterexample to the source-only angular regularity inference, not a B2 stream or a profile.

## A usable stream assumption and scope

One way to ensure the displayed hypotheses is a stream expansion, modulo a linear stream gauge,

    Psi=r^(2-s)A(theta)+r^(2-2s)A1(theta)
                            +O_symbol(r^(2-2s-delta0)),

through three spatial derivatives, where A,A1 are smooth and delta0>0. Here O_symbol means that each spatial derivative lowers the stated radial power by one. It gives (1); applying the Laplacian and the transport operator gives (2) with delta=min(s,delta0), since the constant relative velocity contributes a term of smaller degree -1-s and s<1/2. The leading source f is the one derived in packet130. Linear gauges cancel from V and Omega, so they must be removed before assigning a power gap to the stream remainder.

This is a conditional necessary-tail result for an exact profile. A numerically small thermal residual is not the thermal PDE and cannot be substituted in (4) without a separate error estimate. It is not an exclusion of every profile in the broad prompt, and it does not show that a moment-compatible stream solves the thermal equation.

Dependencies: elementary ODE uniqueness, smooth scalar transport on the circle with integrable C1 coefficients, dominated convergence, and the homogeneous primitive criterion of packet129, whose needed direction is reproved above. No numerical assumption enters this argument.

Written UTC: 2026-10-21T06:00:42.167248+00:00
