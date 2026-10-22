# Projected source parameter and a finite-cutoff characteristic map

## Statement and scope

Let beta>2, rho=beta-2, and let G_z denote the divided vorticity field with coefficient vector z in a fixed finite linear representation. Put Omega_z=xG_z. Let V be the linear canonical relative whole-plane inverse, and let c(z)=Psi_xy(0) be its center strain. For the total transport W this is the anisotropic strain (partial_y W_y-partial_x W_x)/2 at the center; beta X contributes zero to this difference. Let f be a separately specified fixed vorticity source with relative velocity V_f and strain c_f. Fix a0 and c_star=1+beta/2. Choose a coefficient vector q with c(q)!=0. The source-parameter-dependent strain projection of a fixed unprojected vector z0 is

 z_lambda=z0+q[c_star-c(z0)-lambda c_f]/c(q).

Then the total transport field W_lambda=beta X+V[Omega_(z_lambda)]+lambda V_f has center strain c_star, and its derivative at fixed z0,beta is

 D_lambda W=V_f-(c_f/c(q))V[Omega_q].

In particular this derivative has zero center strain. It is different from V_f alone unless c_f=0 or the correction vanishes. This is the derivative of the projected map described in the numerical report, not the derivative holding the already projected physical field fixed. A basis coefficient derivative must retain this distinction.

Suppose the fields are C2 on an annulus containing a compact family of trajectories. Fix delta>0 and prescribe boundary temperature a0 x^2 and vorticity4a0 x/beta on the circle |X|=delta. Suppose each point Y under consideration has a unique backward hit at time T>0, all intervening trajectories stay in the annulus, and W.n>0 at the hit, where n is the outward unit normal. Then on the forward flow tube the characteristic construction below gives a C1 solution of both scalar transport equations with those boundary values. It is a finite-cutoff scalar problem with a prescribed velocity. It does not require or establish that the reconstructed vorticity has that velocity as its inverse.

## Projection derivative

Linearity gives c(z_lambda)+lambda c_f=c_star. Differentiating the coefficient formula gives z_lambda'=-q c_f/c(q). Apply the linear inverse to obtain the displayed velocity derivative; applying c to that derivative gives c_f-c_f=0. For projection along the Euclidean coefficient gradient q=grad c, c(q)=||q||^2. In the divided r2 spline representation with beta_basis=b, geometric scale L and normalized B-spline functions B_j(t),

 c(z)=-(b L/4) sum_j integral_0^1 B_j(t)dt [z_(1,j)-z_(3,j)],

with masked inactive entries removed. Here X=(r sin phi,-r cos phi), t=1-(1+(r/L)^2)^(-1/(2b)), and the odd cosine modes carry the factor rho_odd=r/sqrt(r^2+L^2). Differentiating the canonical relative kernel at the center gives c=(1/pi) integral Omega sin(phi)(-cos(phi)) dr dphi/r. The identity integral_0^(2pi) sin^2(phi)cos(phi)cos(k phi)dphi=(pi/4)(1_(k=1)-1_(k=3)), together with (1-t)^(b+1)rho_odd dr/dt=bL, proves the formula. This derivative is integrable at the center for the smooth odd sources here and at infinity for their decaying tails. Thus the gradient is computed independently from scalar spline integrals and contains only angular cosine modes1 and3. The projection corrects the strain without changing the mode-zero center value of G. The source c_f must be computed in its own recorded geometric scale, knots and beta_seed, not by reinterpreting its coefficients at the unknown field's beta_basis.

## Boundary gradient and transport reconstruction

Let X_0 be the backward hit of Y and let Phi_t be the forward flow. The temperature is

 Theta_delta(Y)=exp(rho T) a0 (X_0)_x^2.

The implicit function theorem applies to the hit equation |Phi_(-T)(Y)|=delta because its derivative in T is -W.n!=0. Hence T and X_0 are C1 functions of Y locally. The usual flow coordinates (one boundary coordinate and time) are nonsingular for the same reason. They define the displayed smooth transported temperature. Its tangential boundary derivative is that of a0 x^2; its normal derivative is uniquely fixed by W.grad Theta=rho Theta. Consequently the full gradient seed is

 g_0=(2a0 x,0)+n [rho a0 x^2-W.(2a0 x,0)]/(W.n).

Along a forward characteristic its gradient obeys g'=(rho I-DW^T)g, obtained by differentiating the thermal equation. Starting from g_0 therefore gives exactly grad Theta_delta, by uniqueness of this linear ODE and the preceding flow-coordinate construction. Starting instead from (2a0 x,0) without the normal correction need not give the gradient of the finite-cutoff temperature.

The reconstructed vorticity obeys omega'=g_x-omega with boundary omega_0=4a0 x/beta. Variation of constants gives

 Omega_delta(Y)=exp(-T) omega_0+integral_0^T exp(-(T-t)) g_x(Phi_t X_0)dt.

This proves (W.grad+1)Omega_delta=(Theta_delta)_x on the flow tube. The boundary value is imposed data, not a deduction from the finite-radius PDE. The C2 field assumption and transverse hitting also give ordinary parameter dependence on lambda for this finite-cutoff construction on a sufficiently small compact neighborhood of each tested parameter. No uniform infinite-time or delta-to-zero theorem is asserted here.

## Independent manufactured transport control

Take beta=4 and a real parameter k>0. On a bounded region define u=1+k x^2 and

 W_k=(x u, (7-3k x^2)y),
 Theta_k=x^2/u,
 Omega_k=(2/(5k)) sqrt(u)/x [1-u^(-5/2)],

with the removable value Omega_k(0)=0. These fields are smooth, W has divergence8 and center derivative diag(1,7), and Theta has center coefficient1. The vorticity expression is odd in x and has leading coefficient1=4/beta. The factor in brackets vanishes to order x^2, which proves removability and smoothness at the axis by its convergent power series.

Direct differentiation gives grad Theta=(2x/u^2,0), so W.grad Theta=2Theta. To check the vorticity equation, write it as the one-variable ODE x u Omega_x+Omega=2x/u^2. Its integrating factor after division by x u is mu=x/sqrt(u). The displayed formula has mu Omega=(2/(5k))[1-u^(-5/2)], whose derivative is2x/u^(7/2). This is precisely mu times the divided forcing2/u^3. Thus both scalar transport equations hold. Supplying their exact boundary data to the reconstruction must reproduce these same fields at every transverse test trajectory by uniqueness, independently of delta. Their exact parameter derivatives provide an additional test of the numerical parameter differences. These exact boundary data differ from a0 x^2 and4a0 x/beta at positive delta. The implementation must use the exact gradient2x/u^2 in this control. Tests are restricted to transverse hits, for example the positive-flux small circles and bounded trajectories specified in each output.

This is a transport-only manufactured control. Indeed -curl W=6kxy is not the displayed Omega, so it is not a Boussinesq solution or a whole-plane inverse test. The independent inverse checks use the actual saved sources and separate Cartesian quadrature controls.

## Verification meaning

The planned computation uses this lane's own SciPy spline reader, adaptive physical-radius modal inverse, quintic stream interpolation in log r, and DOP853 characteristics. It compares distinct inverse-node grids, ODE tolerances, finite-cutoff radii and parameter-difference steps. A separately implemented Cartesian Duffy full-plane inverse checks selected velocities. The interpolated stream is C2 and its velocity C1, with higher regularity inside each interpolation cell. It is a numerical approximation to the smooth source inverse, not itself an invocation of the C2 velocity theorem. All source integrals extend to infinity; restricting the interpolation annulus is a flow-evaluation restriction, not a finite-box Poisson inverse.

The projected lambda derivative is an exact algebraic statement. Numerical response values from a finite annulus, finite cutoff and interpolated velocity are only sampled diagnostics. Comparing them with a saved coefficient-fit derivative must account for the different discretization and for the fit itself. A matrix derivative at one stored forced state does not prove a fixed point, a continuum fold or a B2 profile. The broad endpoint remains OPEN.
