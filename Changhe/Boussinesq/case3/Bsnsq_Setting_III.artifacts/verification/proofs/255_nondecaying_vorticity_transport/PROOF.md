# Sublinear canonical velocity and exact thermal transport do not force vorticity decay

## Statement and scope

Fix a0>0, R0>0 and kappa>0. There are smooth fields on the full plane, with Psi and Omega odd in x and Theta even in x, such that U=(-Psi_y,Psi_x) is the ordinary absolutely convergent full-plane Biot-Savart inverse of Omega and:

1. U=O(1/r), U(0)=0, Omega=-Delta Psi and |Omega(X)|<=C(1+|X|)^kappa. Every fixed derivative of Omega is also polynomially controlled. Omega is in L2(R2), but it is unbounded along a sequence tending to infinity.
2. With W=2X+U, the equation W.grad Theta=0 holds everywhere. Theta is bounded, nonnegative and zero exactly on the symmetry axis. On the prescribed disk, Psi=2xy-a0 x^3/3, Omega=2a0 x, Theta=a0 x^2, so both B2 transport equations and all center conditions hold exactly.
3. The equilibrium set of W is the same compact arc as in the base construction below. Every derivative of the vorticity residual vanishes on that arc, and both equations hold near its interior.
4. For some R>0 and r_j=R 2^j, j>=1, the exact values are Omega(r_j,0)=r_j^kappa and R_Omega(r_j,0)=r_j^kappa. In particular these fields do NOT satisfy the full vorticity equation.

This is a counterexample to deriving uniform pointwise vorticity decay from the canonical inverse, sublinear velocity, polynomial control, bounded temperature, exact thermal transport and normalized local B2 data. It does not refute a decay theorem using the full missing vorticity equation. It does not construct a B2 profile or exclude any profile. Its purpose is to isolate the extra uniform-decay assumption in class A from the broader prompt's polynomially controlled tails. The observer representative U(0)=0 is exhibited explicitly; it is not imposed as an exclusion of moving-center profiles.

## 1. Base fields and the plateau used by the perturbation

Take the exact smooth beta2 transport configuration proved in the appendix (the verifier's P156 construction), with a0 and R0 as above. Denote it by Psi_b, Omega_b, U_b, Theta_b, W_b=2X+U_b. The appendix supplies the complete construction and proof, not an assumed B2 solution. It gives the exact stated core, compact equilibrium arc, flat residual jets there, ordinary canonical inverse, and U_b=O(1/r).

There are B,A,C,M>0 and a compact set Q such that, outside Q in the strip |y|<B and |x|>2A,

    Psi_b=2C y/x,  Omega_b=-4C y/x^3,  Theta_b=M,
    W_b=(2x-2C/x, 2y-2C y/x^2).                 (1)

This follows directly from h=m1, g0=1, p0=2y and chi(x)=C/x^2 in the base formulas; the compact Hamiltonian shear is the identity there. These are exact formulas on an open strip, not only asymptotics. In particular Omega_b(r,0)=0 there. All changes below lie in this constant-temperature strip and outside Q and the prescribed core.

The same two-region estimates in the appendix show Omega_b in L2. On the finite-width horizontal strip it is O(1/|x|). In the complementary conic region at infinity it is O(r^-2). The squares are integrable on their respective regions. These separate estimates, rather than the weaker isotropic O(r^-1) bound alone, justify this assertion.

## 2. Disjoint compact stream bumps

Let s=|Z|^2 and define the radial smooth compact function

    phi(Z)=(e/4) exp[-1/(1-s)] for s<1,
    phi(Z)=0 for s>=1.

It is smooth across the unit circle by the elementary flatness of exp(-1/t) at t=0+. Its derivatives at0 satisfy -Delta phi(0)=1, grad phi(0)=0 and grad(-Delta phi)(0)=0. For the first identity, if phi=F(s), then Delta phi=4(F'+sF''), and F'(0)=-1/4. The other two follow from radial evenness.

Choose R sufficiently large. Put r_j=R 2^j, epsilon_j=r_j^(-kappa-1), a_j=r_j^(-kappa-2), and P_j=(r_j,0). Increase R until the closed disks of radius epsilon_j about +/-P_j are pairwise disjoint, lie in the strip where (1) holds, avoid Q and the core, and have radii less than min(1,B/2). Define

    delta Psi_j(X)=a_j[phi((X-P_j)/epsilon_j)
                          -phi((X+P_j)/epsilon_j)],
    delta Psi=sum_{j>=1} delta Psi_j,
    delta U=J grad delta Psi, delta Omega=-Delta delta Psi.

The supports escape to infinity and are disjoint, so the sum is locally finite and smooth. Each summand is odd in x and even in y. Thus it supplies precisely the required x parity without adding a y-reflection condition to the B2 problem. The new fields are

    Psi=Psi_b+delta Psi, Omega=Omega_b+delta Omega,
    U=U_b+delta U, Theta=Theta_b, W=2X+U.

No free harmonic velocity or exterior multipole is introduced.

## 3. Pointwise bounds, square integrability and canonical inversion

On the j-th pair of disks, |X| is comparable to r_j. Fixed shape constants give

    |delta U|<=C a_j/epsilon_j=C/r_j,
    |D^l delta Omega|<=C_l a_j epsilon_j^(-l-2)
                           =C_l r_j^(kappa+(kappa+1)l).       (2)

Off all disks the perturbation is zero. Hence U=O(1/r), Omega has the claimed polynomial value bound, and every fixed derivative of delta Omega has a polynomial bound. The explicit strip/cone formulas and smooth transitions in the base yield polynomial derivative bounds there as well. At the positive center P_j, the other bumps vanish and (1) and radial symmetry give

    Omega(P_j)=a_j epsilon_j^-2=r_j^kappa.             (3)

Thus uniform pointwise decay, and even boundedness, fails.

For any finite p>=1, disjoint supports and change of variables give exactly

    ||delta Omega||_p^p
       =2 ||Delta phi||_p^p sum_j a_j^p epsilon_j^(2-2p)
       =2 ||Delta phi||_p^p sum_j r_j^(p kappa-2kappa-2). (4)

The fixed shape norm is finite and positive. The geometric series converges exactly when p<2+2/kappa. In particular delta Omega is in L1 and L2, and Omega is in L2 by the base estimate. Equation(4) concerns the perturbation; no L1 assertion about the base is used.

For each fixed X, all sufficiently far disks have distance comparable to r_j from X. Their contribution to the absolute Biot-Savart integral is bounded by

    C sum_j (1/r_j) ||delta Omega_j||_1
        <=C sum_j a_j/r_j < infinity.              (5)

The finitely many nearby disks cause no divergence: their smooth bounded sources meet only the locally integrable kernel |X-Y|^-1. The base's absolute convergence was proved in the appendix. Thus the ordinary inverse of the sum exists absolutely at every X, and absolute convergence allows the countable sum to pass through that integral.

For each compact smooth delta Psi_j, distributional integration by parts against the fundamental solution Gamma=-(1/(2pi))log|.| gives Gamma*(-Delta delta Psi_j)=delta Psi_j. Taking J grad shows K*delta Omega_j=delta U_j with K(Z)=(Z_2,-Z_1)/(2pi |Z|^2), in the prompt's sign convention. Therefore (5) proves K*Omega=U_b+sum delta U_j=U. At every fixed X at most one of the compact perturbation velocities is nonzero. At0 all perturbations vanish with all their derivatives. The ordinary canonical center velocity remains U(0)=0. No assumption of a uniform decaying vorticity envelope entered this proof.

## 4. Thermal equation, equilibria, and explicit vorticity failure

Each perturbation support lies where Theta_b=M, so grad Theta_b=0 there. Off the supports delta U=0. Consequently

    W.grad Theta=W_b.grad Theta_b+delta U.grad Theta_b=0

on the whole plane, including the support boundaries where the bumps are smooth and flat. Theta itself was not changed, so its sign, boundedness, zero set and exact center jet persist. Near the core and equilibrium arc every field is unchanged, retaining both local equations and all residual jets.

Outside a sufficiently large disk, W_b.X>=|X|^2 follows from W_b=2X+O(1/r). By (2), |delta U.X| is bounded uniformly on the perturbation disks. Increasing R once more makes W.X>0 on every such disk. Off them W=W_b. Thus no new equilibrium is introduced, and the old compact arc remains exactly the full zero set.

At P_j the perturbation velocity is zero and grad delta Omega=0. Formula(1) gives W2(P_j)=0, partial_x Omega_b(P_j)=0 and Theta_x(P_j)=0. Therefore

    W(P_j).grad Omega(P_j)=0,
    R_Omega(P_j)=W.grad Omega+Omega-Theta_x=r_j^kappa. (6)

This exact failure prevents interpreting the example as a profile. It also confirms that no inference using the full exterior vorticity equation has been challenged.

## 5. Dependencies and verification scope

The entire informal argument precedes the new symbolic and physical-space controls. The appendix proves the base construction. The new ingredients are elementary flat radial bumps, a locally finite sum, scale estimates, a geometric series, and compact Poisson integration by parts. Proposed numerical quadrature checks will test individual compact bumps, for which the full-plane velocity is exactly J grad delta Psi_j, using a separately implemented physical-space integral. They will not certify the infinite construction numerically; that construction and its bounds follow from the proof.

Formal Lean/Lake builds, servers, JavaScript/TypeScript, GPU use, RLScience access and external posting are prohibited and not used. Any external model review is recorded by its actual returned model and separately adjudicated. The global B2 problem remains OPEN.

## 5a. Direct canonical-inverse lemma for the base

For completeness the canonical identification in the appendix can be obtained without importing uniqueness theorem03. If a smooth stream psi is bounded, grad psi=O(1/r), and the ordinary velocity integral of -Delta psi converges absolutely, then that integral equals J grad psi. Indeed apply Green's second identity on a large disk, with a small disk removed about the fixed observation point X, to psi(Y) and each component of K(X-Y). The small-circle term tends to the corresponding component of J grad psi(X), by the distributional identity -Delta Gamma=delta. On the large circle K=O(1/R), its normal derivative is O(1/R^2), psi=O(1), and its normal derivative is O(1/R). Both boundary terms have absolute size O(1/R), since the circumference is O(R). They vanish as R tends to infinity. Absolute convergence passes the volume integral to the ordinary full-plane inverse.

The appendix's base stream is bounded: in its conic regions it is a smooth degree-zero angular function, and in the fixed-width strip it is D(y)/x with D bounded. Its gradient is O(1/r) and its velocity integral converges absolutely by the explicitly proved two-region estimates. The compact shear changes the stream by a compact smooth function, so these conditions persist. This proves the base canonical identity directly, including the absence of a free constant velocity. The axis core formula gives U_b(0)=0. The earlier appendix citation to theorem03 is therefore dispensable here.

## Appendix: complete base construction

The following base proof is reproduced from the verifier's P156, through its mathematical dependency and scope section. Its earlier status and chronology refer to that base result. Its numerical controls are not counted as new checks here.

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


