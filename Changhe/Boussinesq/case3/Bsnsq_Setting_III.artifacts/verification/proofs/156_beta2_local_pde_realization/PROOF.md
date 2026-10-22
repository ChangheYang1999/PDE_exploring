# A beta-two configuration satisfying both equations near its equilibrium arc

Status: CONFIRMED by the complete independent proof and manufactured controls. This is an explicit smooth nonprofile. The vorticity equation fails in an exterior cone. ActualOpus5.5 requests243 and244 supplied no written audit; no external endorsement is claimed.

## 1. Statement and notation

Fix a0>0 and R0>0. There are smooth full-plane fields Psi, U=J gradPsi, Omega=-DeltaPsi and Theta, with J(a,b)=(-b,a), such that:

1. Psi and Omega are odd under x-reflection; Theta is even, nonnegative, and zero exactly on x=0. The ordinary full-plane Biot-Savart inverse is U, U(0)=0, and U=O(1/r) at infinity.
2. With W=2X+U, the thermal equation W.gradTheta=0 holds everywhere.
3. On the prescribed disk |X|<=R0, the fields are exactly

       Psi=2xy-a0 x^3/3, Omega=2a0 x, Theta=a0 x^2,
       W=(0,4y-a0 x^2).                              (1)

   Both defining B2 equations hold there. In particular c=Psi_xy(0)=2 and q=Omega_x(0)=2a0 are the required beta=2 center values.
4. The full equilibrium set is one compact embedded arc

       Z={(x,F(x)/4): -A<=x<=A},                     (2)

   with A>R0. On an open neighborhood of its interior, both B2 equations hold. Every derivative of the vorticity residual f=(W.grad+1)Omega-Theta_x vanishes at every point of Z. At either endpoint, every derivative of Omega and of Theta-M vanishes, where M=F(A)>0.
5. The field is not a profile. In a fixed exterior cone the residual has an explicit nonzero r^-1 leading term. Vorticity changes sign on x>0, and the constructed vorticity has the uniform bound O(r^-1). No exact exterior vorticity equation, compact residual, or full B2 endpoint is claimed.

The construction sharpens20 by correcting its vorticity equation throughout a prescribed core and near the interior of the equilibrium arc. It uses a compact area-preserving conjugacy, not a free harmonic velocity.

## 2. The smooth transport configuration, with independent core sizes

Choose A>R0+1. Let rho be smooth and even, equal to1 on |t|<=R0+1, positive on |t|<A and zero for |t|>=A, with all endpoint derivatives zero. Define

       F(x)=int_0^|x| 2a0 t rho(t)dt, M=F(A).

Then F is even, equals a0 x^2 on |x|<=R0+1, is strictly increasing on 0<x<A, and equals M outside that interval. F-M is flat at +/-A.

Choose B>R0+1+M/4. Let b be a nonnegative smooth probability density supported in (B,2B), positive inside and flat at its endpoints. Write

       m1=int t b(t)dt, m2=int t^2 b(t)dt,
       h(y)=int max(|y|,t)b(t)dt, H(y)=int_0^y h(v)dv,
       g0(y)=m1/h(y), p0(y)=4H(y)/h(y)-2y.

These functions are smooth: h=m1, g0=1 and p0=2y for |y|<=B; and for |y|>=2B,

       h=|y|, H=sign(y)(y^2+m2)/2,
       g0=m1/|y|, p0=2m2/y.                           (3)

Monotonicity of h gives |p0(y)|<=2|y|, and differentiation gives

       p0'=2-(h'/h)(2y+p0), g0'/g0=-h'/h.             (4)

To define the horizontal cutoff, choose a smooth probability density d supported in (1,2), positive inside and flat at its endpoints. Let e(t)=int_1^t d(s)ds, extended by0 for t<=1 and by1 for t>=2. Put

       q(t)=0 for t<=1, q(t)=int_1^t e(s)/s ds for t>1,
       chi(I)=exp[-2q(|I|/A)].

Then chi=1 on |I|<=A, 0<chi<1 outside, and chi=C/I^2 for |I|>=2A, for one C>0. Moreover

       a_chi(I)=chi(I)+I chi'(I)
               =chi(I)[1-2e(|I|/A)] lies in (-1,1].    (5)

The value1 occurs only in the plateau; the lower endpoint -1 is not attained. Define the base fields

       I=x g0(y), Psi0=x p0(y)chi(I), Theta0=F(I),
       U0=J gradPsi0, W0=2X+U0, Omega0=-DeltaPsi0.

On |I|<=A, chi=1 and (4) gives W0.grad I=0. Outside that region F'=0. Hence W0.gradTheta0=0 everywhere. The sign of (W0)_2=2y+p0(y)a_chi(I) is the sign of y when y is nonzero: if |a_chi|<1 the bound on p0 makes this strict, and in the case a_chi=1 it equals 4H/h. Thus all equilibria lie on y=0. There (W0)_1=2x(1-chi(x)), so the full zero set is exactly [-A,A] times{0}.

The full-plane decay and inverse proof is the same direct two-region calculation as20; its details are recorded here. If |y|>=2B and |I| is bounded, (3) makes Psi0 a smooth degree-zero angular function on a cone separated from y=0, so U0=O(r^-1), Omega0=O(r^-2). If |I|>=2A, then Psi0=D(y)/x, where D=C p0 h^2/m1^2. D and its derivatives are bounded for |y|<=2B, giving U0=O(|x|^-1), Omega0=O(|x|^-1) there. For |y|>=2B, D is a constant multiple of y, giving the better conic bounds. These regions cover infinity. Derivatives of any fixed order have analogous smooth strip/cone bounds, with no claim of isotropic full symbol decay.

The ordinary Biot-Savart integral is absolutely convergent at every point: the horizontal strip contributes O(|x|^-2) at infinity, and the conic source is O(r^-2) against an O(r^-1) kernel. The relative inverse uniqueness theorem03 applies to these smooth O(r^-1) vorticity bounds and the sublinear velocity U0. It identifies their relative velocities. The ordinary inverse at0 vanishes: Omega0 is odd in x and in y, so both components of its kernel integral at0 vanish by parity. U0(0)=0 as well. This step uses the fixed full-plane inverse, with no wall or added strain.

## 3. A compact Hamiltonian shear

Set

       g(x)=F(x)/4, G(x)=int_0^x g(t)dt.

F is even, so G is odd. Choose smooth even compact cutoffs kappa_x and kappa_y such that kappa_x=1 on |x|<=A+1 and kappa_y=1 on |y|<=B+M/4+2. Define the compact odd Hamiltonian

       eta(x,y)=G(x)kappa_x(x)kappa_y(y).

Let Phi_t be the complete flow of J grad eta, for 0<=t<=1. The flow is area preserving, commutes with x-reflection and is the identity outside a fixed compact set. It fixes the material center because grad eta(0)=0.

For |x|<=A+1 and |Y|<=B, the entire explicit path

       Phi_t(x,Y)=(x,Y+t g(x))                        (6)

stays in the region where the cutoffs equal1, since 0<=g<=M/4. There J grad eta=(0,g(x)), so (6) follows from uniqueness. Write Phi=Phi_1 and define

       W=Phi_*W0, Theta=Theta0 o Phi^-1, U=W-2X.

Exact thermal transport follows by the chain rule. The vector field W has divergence4, so U is divergence free. The compact stream formula is

       Psi-Psi0=int_0^1 [W_t.grad eta-4eta]dt.         (7)

To verify (7), differentiate the pushforward: dW_t/dt=D(J grad eta)W_t-DW_t(J grad eta). For div W_t=4 this equals J grad(W_t.grad eta-4eta). The correction in (7) is compact and odd. Consequently U is the canonical full-plane inverse of -DeltaPsi, with the same decaying exterior as U0. Its ordinary inverse correction is exactly J grad(Psi-Psi0), by compact Poisson uniqueness. No new velocity constant appears.

## 4. Both equations on the core and along the arc

In the region |x|<A, |y-g(x)|<B, the inverse point (x,y-g(x)) is in the base plateau where Psi0=2xy and Theta0=F(x). There W0=(0,4y), and (6) gives

       W=(0,4[y-g(x)]), Theta=F(x),
       Psi=2xy-4G(x), Omega=4g'(x)=F'(x).             (8)

The stream equality follows by integrating its gradient from the displayed W. The region is connected and invariant under x-reflection; oddness of Psi and G forces the integration constant to0. In the smaller common plateau where all intermediate inverse points and the fixed point lie in the base band, (7) also gives the correction -4G directly. That simpler correction formula is not asserted throughout the entire shifted band, whose upper edge can lie above y=B. Thus W.gradTheta=0 and (W.grad+1)Omega-Theta_x=0 throughout this open region.

The prescribed disk lies inside it because A>R0 and |y-g(x)|<=R0+M/4<B. Also F=a0x^2 and G=a0x^3/12 there. This proves all exact formulas (1), including Psi(0)=0 and U(0)=0.

Zeros of a vector field are carried exactly to zeros under a diffeomorphism. Equation (6) therefore gives the full zero set (2), with no hidden additional equilibria. Its interior lies in the exact-PDE region (8). Near an endpoint the shear formula still holds, the base chi-1 is flat in x-A or x+A, and F-M is flat. Equivalently, all jets of Psi at the endpoint agree with those of 2xy-Mx plus a constant, and all jets of Theta agree with the constant M. It follows that Omega and Theta-M are flat there. All derivatives of f vanish in the interior neighborhood and extend continuously to the endpoints, so every jet of f vanishes at all of Z.

The flow commutes with reflection, and Theta remains a nonnegative pullback with zero set precisely the fixed symmetry axis. The zero arc is compact, with flat endpoint data, even though both defining equations already hold on every neighborhood contained in its interior.

## 5. Explicit exterior failure

The shear is compact, so the fields agree with the base for sufficiently large r. Choose a fixed c>0 so small that m1 c<R0+1 and m1 c<A. In a narrow upper cone about x=cy with y>2B, I=m1 x/y stays in the quadratic-temperature plateau and chi=1. There

       Psi=2m2 x/y, Omega=-4m2 x/y^3,
       Theta=a0 m1^2 x^2/y^2,
       W=(2x+2m2 x/y^2, 2y+2m2/y).

A direct differentiation gives

       f=x[12m2/y^3+16m2^2/y^5-2a0m1^2/y^2].        (9)

Along x=cy this is -2a0 m1^2 c/y+O(y^-2), which is nonzero for every sufficiently large y. The vorticity is negative there for x>0, whereas it is positive in the right core. The residual is noncompact. This is an explicit rejection of the constructed field as a profile, independent of invoking a tail-exclusion theorem.

## 6. Dependencies and scope

Only the smooth base construction20, elementary compact Hamiltonian flow identities, and canonical inverse uniqueness03 are used. The base decay and transport calculations have been reproduced above, so the modification does not rely on an unverified numerical field. No assertion from the broad beta>2 gluing construction is needed.

This example excludes a local-to-global argument based solely on the normalized center, exact PDEs on a prescribed disk, the compact equilibrium arc, and all residual jets on that arc. It does not exclude a global argument using the missing vorticity equation in the exterior. In particular it does not supply the slow profile tail, the outgoing harmonic region forced by the full beta=2 equations, a compact vorticity residual, or a decisive YES/NO result.

Initial proof written UTC 2026-10-21T10:41:06.793316+00:00. Published 2026-10-21T10:49:37.789836+00:00. Independent controls complete; the external-review availability limitation is recorded below.


## 7. Independent controls and limitations

Seventeen exact algebra checks passed: the core fields and both equations, all three center values, the shear pushforward and divergence, the exterior vorticity and both residual formulas, its leading nonzero term, and both components of the compact Hamiltonian stream identity. The two quadrature orders64 and128 each used11 flow points, including the cutoff transition, the prescribed shear band, the center, reflected points and the exterior. Forward/backward DOP853 flows, the determinant, reflection and the exact shear and Jacobian on their stated region all passed. The largest inverse-flow error was below7.66e-13 and determinant error below7.74e-13. The run took2.702920116s, from2026-10-21T10:43:31.117948Z to10:43:33.820848Z.

These finite floating-point checks are manufactured controls, not a global profile computation or interval certificate. The flow controls use a polynomial base for the algebra checks. Canonical inversion of the constructed full-plane field is established by the proof above, not numerically certified by these controls. The inputs include an unused finite-difference-step field; no finite-difference test is claimed here.

An initial stream argument that incorrectly treated the entire shifted band as a common plateau for all intermediate times was corrected before the tests and the review requests. Its snapshot is retained. The control-run proof is also retained with the exact recorded hash. After the controls the unnecessary choice A>R0+2 was relaxed to A>R0+1, as used in the proof and in the control parameters R0=1,A=3. No tested formula changed. The text now states the direct O(r^-1) vorticity bound instead of appealing to a separate slow-tail exclusion result.

ActualOpus5.5 requests243 and244 returned model claude-opus-5-5, but their responses contained no written audit text (stop reason refusal, no written explanation). Their status records are retained. The focused244 request addressed the compact shear after the general243 request. Neither supplies a mathematical endorsement or an identified mathematical objection. The result is provided for further team review with that limitation explicit.
