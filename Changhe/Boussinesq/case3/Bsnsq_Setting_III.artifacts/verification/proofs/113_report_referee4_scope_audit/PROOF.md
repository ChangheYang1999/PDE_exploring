# Audit of the exterior C=0 construction and report scope

Written 2026-10-21T02:46:07.566370+00:00. Status: independent analytic verification. This is an example satisfying the vorticity equation only, not the B2 target.

## Statement

Let beta>2, s=1/beta, lambda=(1-s)(3-s), and let chi be smooth, radial, zero for r<=1 and one for r>=2. Define Psi=chi(r)x r^(1-s), Omega=-Delta Psi, V=(-Psi_y,Psi_x), W=beta X+V and F=W.grad Omega+Omega. Set

    Theta_inf(x,y)=-(lambda/s)y r^(-2s),
    Theta(x,y)=Theta_inf(-3,y)+integral_(-3)^x F(t,y)dt.

Then Psi and Omega are smooth and odd in x; Theta is smooth and even in x. The canonical relative velocity is V, V(0)=0 and V=O(r^(1-s)). The vorticity equation W.grad Omega+Omega=Theta_x holds on the whole plane. For r>=2,

    Omega=-lambda x r^(-1-s), Psi=x r^(1-s),
    Theta=Theta_inf, V=u0,

where u0 is the homogeneous velocity from this Psi. Hence the relative inverse constant C is zero. These are the expansions of lead4.26(d), with a1=-lambda cos(theta), f0=-(lambda/s)sin(theta), all later coefficients zero. The conclusion about this example holds for all beta>2, although4.26(d) itself concerns noninteger beta.

## Direct exterior computation

For r>2, the radial homogeneous Laplacian gives -Delta[x r^(1-s)]=-[(2-s)^2-1]x r^(-1-s)=-lambda x r^(-1-s). Since Omega has degree -s, beta X.grad Omega+Omega=0. Direct derivatives give

    V1=-(1-s)xy r^(-1-s),
    V2=r^(1-s)+(1-s)x² r^(-1-s),
    Omega_x=-lambda[r^(-1-s)-(1+s)x² r^(-3-s)],
    Omega_y=lambda(1+s)xy r^(-3-s).

Their product is V.grad Omega=2lambda xy r^(-2-2s)=Theta_inf,x. The cancellation of the two x³y terms verifies both the sign and coefficient.

## Primitive, parity and exterior matching

Global smoothness follows from the cutoff at0 and smooth parameter-dependent integration over finite intervals. V1 is odd in x, V2 is even, Omega_x is even and Omega_y odd, so F is odd. Therefore the primitive differs from its value atx=0 by an even function of x; Theta is even. For an exterior point x<=0, the interval joining -3 to x remains in r>=2: when x>=-3 its smallest absolute horizontal coordinate is |x|; when x<-3 every point has |t|>=3. Thus the exterior identity F=Theta_inf,x gives Theta=Theta_inf on the negative exterior. Evenness extends this equality to the positive exterior. Points on the circle follow by continuity.

## Canonical inverse and limitations

The kernel is K(Z)=(Z2,-Z1)/(2pi|Z|²), so curl V=-Omega with the prompt convention. Omega=O(r^-s), s>0, so the canonical subtracted kernel integral converges absolutely at infinity. A three-region split gives its relative velocity O(1+r^(1-s)). It and the displayed V have the same distributional curl and divergence; their difference is an entire harmonic sublinear vector field. Interior derivative estimates on arbitrarily large balls force that field to be constant. Both vanish at0, so the difference is zero. The exterior equality V=u0 therefore gives C=0 without an appended harmonic field.

This example fails the temperature equation explicitly. At y=0,x>2 its residual is

    W.grad Theta-(beta-2)Theta
       =-lambda(2-s)r^(1-3s)/s !=0.

It also fails the target's global axis condition: Theta(0,y)=-(lambda/s)y|y|^(-2s)!=0 for |y|>2. Thus it establishes compatibility of the vorticity equation, parity, sublinear canonical velocity and the displayed exterior expansions with C=0. It does not show that the full center/axis-normalized expansion subclass contains a profile or a solution of either full transport system.

## Required length rescaling in the axis compatibility summary

Packet106 constructs a unit-length example with sufficiently large superposition amplitude A. Its axis coefficient is a0=A, its axis speed is b(y)=mu y(1+y²)/(1+ell y²), and positivity is proved only for A above a finite threshold. To cover any prescribed a0>0, take L=A/a0 and

    Psi_L=L²Psi(X/L), Omega_L=Omega(X/L), V_L=L V(X/L),
    b_L(y)=L b(y/L), e_L(y)=L e(y/L), H_L(y)=H(y/L)/L.

Direct differentiation preserves the center strain, b_L e_L'=mu e_L and Omega_L,x(0,y)=H_L/e_L'. Moreover b_L H_L'+(beta/2)H_L=(2A/L)/e_L'=2a0/e_L'. Positivity is preserved and the new a0 is exactly A/L. One may not enlarge A while saying that a0 and the unit-length b both remain fixed. Packet107's unbounded Q_L family at fixed a0 uses A=a0 L and takes L sufficiently large.

The conditional positive-weight result in106 requires a hypothetical G+ profile, a proper area-preserving global linearizing chart with kappa=0, and Theta_x>0. Under these hypotheses its interval2beta-1<nu<2beta+(beta/2-1) and identity(nu+1-2beta)int Omega w=int Theta_x w>0 remain correctly quoted. Those hypotheses are not claimed for the compatibility construction.

## Dependencies and evidence

Elementary differentiation, parity, finite-interval integration, the canonical inverse estimate and harmonic uniqueness, plus packet106 for positivity of the rescaled axis construction. No Lean/Lake or formal machine proof is claimed. The source snapshots and report-change audit are in verification. No JavaScript/TypeScript, servers, RLScience cluster or GPU execution.
