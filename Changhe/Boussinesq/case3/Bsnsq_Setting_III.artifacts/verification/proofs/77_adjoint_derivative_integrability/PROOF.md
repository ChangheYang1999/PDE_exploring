# Absolute integration by parts can fail for the adjoint strain kernel

Date:2026-10-20. Status: complete proof below, independent actual Opus review unavailable (requests78/79; no endorsement). This is a smooth kinematic counterexample, locally an exact B2 field, not a global B2 profile.

## Statement and scope

Fix beta>2. There exist smooth full-plane fields W=beta X+V, Omega=-curl V, Theta, with the following properties:

- V is its centered canonical inverse, is compactly supported, and div W=2beta.
- W has only the zero0; every nonzero backward orbit tends to0 and every forward orbit escapes. Reflection parity is exactly the B2 parity.
- Theta is smooth, even in x, zero on the entire vertical axis, positive for x>0, and satisfies temperature transport everywhere.
- The exact center relations hold with a0>0 and c=1+beta/2. BOTH B2 transport equations hold in a whole neighborhood of0.
- The fields obey the class A size bounds. Omega is compactly supported, so the global vorticity transport equation fails.

For the adjoint strain kernel

    K(X)=xy/|X|^4, alpha=2beta-1,
    M(Y)=integral_0^infinity exp(alpha t) K(phi_t Y) dt,

M is smooth off0 and integral |Theta_x M| is finite. Nevertheless, for every sufficiently small ball,

    integral_B |Theta partial_x M| = infinity.

Consequently these flow, temperature, center, inverse and local-PDE conditions alone do not justify an ABSOLUTELY CONVERGENT integration by parts from integral Theta_x M to -integral Theta M_x. A conditional or distributional integration by parts is not refuted. The theorem does not assert this failure for any actual global B2 profile. Such a profile might have extra constraints from its global vorticity equation.

## 1. Compact stream construction and exact local equations

Write lambda=(beta-2)/2>0, mu=(3beta+2)/2, c=1+beta/2. Choose a smooth radial cutoff chi with0<=chi<=1, chi=1 for r<=1 and chi=0 for r>=2. Let d<0 be sufficiently small, to be chosen more precisely below, and put

    Psi=(cxy+d x^3)chi(r), V=(-Psi_y,Psi_x), W=beta X+V,
    a0=-3beta d/2>0.

The field is smooth, has the required parity, V(0)=0 and div V=0. The terms arising from differentiating chi are tangent to circles and hence do not contribute to W.X. Therefore

    W.X=beta r^2+c chi(y^2-x^2)+3d chi x^2 y
        >=(lambda-6|d|)r^2.

Choose |d|<lambda/12. The radius is strictly increasing on every nonzero orbit, uniformly at a positive exponential rate. W is linear outside a compact set, so its flow is complete. Its only zero is0, all nonzero backward orbits tend to0 and all forward orbits escape.

The vorticity Omega=-Delta Psi is compactly supported. The centered canonical full-plane inverse of Omega equals V: their difference is an entire harmonic sublinear vector field and hence constant, and both vanish at0. Near0 the equations are exactly

    W=(lambda x,mu y+3d x^2), Omega=-6d x.

In particular DV(0)=diag(-c,c) and Omega_x(0)=-6d=4a0/beta.

For each physical point Y, take T large enough that phi_-T Y lies in the unit ball and define

    xi(Y)=exp(lambda T) [phi_-T Y]_1.

The definition is independent of T once the orbit is in that ball, since there x'=lambda x and backward orbits remain there. On each compact set a fixed sufficiently large T works, giving a smooth function; near0 it is exactly x. It is odd in x and positive in x>0, by reflection and uniqueness of trajectories at the invariant vertical axis. It satisfies W.grad xi=lambda xi. Thus Theta=a0 xi^2 has all the stated temperature properties and solves W.gradTheta=(beta-2)Theta globally.

Near0, Theta=a0x^2. The local vorticity equation is also exact:

    W.gradOmega+Omega=(-6d)(lambda+1)x=-3beta d x=Theta_x.

Outside radius2, W=beta X. Hence Theta=r^(1-2/beta)h(theta) there, with smooth angular h inherited from the radius2 data; all differentiated class A bounds follow. V and Omega have compact support. The global vorticity equation cannot hold: it would imply Theta_x=0 outside that support, whereas on every horizontal line with |y|>2, Theta vanishes at x0 and is positive at every x>0.

## 2. Adjoint regularity away from0

For Y outside radius2, phi_tY=exp(beta t)Y and homogeneity gives M(Y)=K(Y), since alpha-2beta=-1. For any Y!=0, the first forward hitting time T(Y) of radius2 is finite and smooth wherever Y is inside that circle, because W.X>0. Thus

    M(Y)=integral_0^T exp(alpha t)K(phi_tY)dt
          +exp(alpha T)K(phi_TY).

This proves smoothness off0 and smooth dependence on d on compact sets avoiding0. It also proves ordinary convergence of the defining integral.

The absolute integrability of Theta_x M follows by the same Fubini majorant as packet64; it does not use the global vorticity equation. Explicitly, let f=Theta_x and J_f(Y)=integral_0^infinity exp(-t)|f(phi_-tY)|dt. Near0 the backward flow contracts and f=O(r), so J_f=O(r). At infinity the flow is exactly radial until radius2, with hitting time tau=beta^(-1)log(r/2); f=O(r^(-2/beta)) there and is bounded on the remaining backward orbit. Splitting at tau gives J_f=O(r^(-1/beta)). Thus integral |K|J_f is finite. Changing variables by the flow, whose Jacobian is exp(2beta t), proves integral |f|M_abs finite, where M_abs uses |K| in place of K. In particular integral |Theta_x M| is finite.

## 3. A singular funnel near the curved slow orbit

Set

    k=3d/(mu-2lambda), kappa=mu/lambda>3,
    q=alpha/lambda=4+6/(beta-2)>4.

In the unit ball the coordinates (xi,eta)=(x,y+kx^2) give xi'=lambda xi, eta'=mu eta. For bounded z and sufficiently small u>0 write

    Y_d(u,z)=(u,u^kappa z-ku^2).

Then phi_tY_d(u,z)=Y_d(u exp(lambda t),z) as long as the orbit stays in that ball. Fix a small u0>0 and a bounded z interval such that this holds for0<u<=u0. Splitting M at the time when u reaches u0 gives

    M(Y_d(u,z))=u^(-q) A_d(z)+R_d(u,z),
    A_d(z)=u0^q M(Y_d(u0,z))
        +(1/lambda) integral_0^u0 v^(q-1) K(Y_d(v,z))dv,
    R_d(u,z)=-(u^(-q)/lambda) integral_0^u v^(q-1)K(Y_d(v,z))dv.

The formulas are exact. Uniformly for bounded z and small d,

    K(Y_d(v,z))=O(v^-1),
    partial_z K(Y_d(v,z))=O(v^(kappa-3)).

They follow by direct differentiation of K and |Y_d(v,z)| comparable to v. Since q>4, the defining integral for A and its z derivative converge. Consequently A_d is C1 in z and depends continuously in C1 on d. Further direct differentiation of R gives

    R=O(u^-1), R_u=O(u^-2), R_z=O(u^(kappa-3)).

For the physical derivative at fixed y,

    partial_x=partial_u+[2k u^(1-kappa)-kappa z/u]partial_z.

It follows that partial_x R=O(u^-2), uniformly in the same region.

## 4. Nonconstant outgoing coefficient persists under small curvature

At d0, the stream cxy chi makes both coordinate axes invariant: W1 has a factor x and W2 a factor y. Every trajectory starting in the first quadrant remains there for all finite times. Thus for z>0, K is strictly positive on the whole orbit from Y_0(u0,z). The integral formula for A gives A_0(z)>0. For z0 that orbit lies on the horizontal axis, so A_0(0)=0. Choose, for example, z1=1 after making u0 smaller if necessary. By the mean value theorem A_0' is positive at some point in(0,1), and by continuity it is bounded below by a positive constant on a compact interval I inside(0,1).

The C1 dependence established above implies A_d'>=m>0 on a possibly smaller I for all sufficiently small |d|. Choose a nonzero negative such d that also satisfies |d|<lambda/12. Then k!=0 and all previous construction properties hold.

## 5. Divergence of the absolute derivative integral

Differentiate the exact singular term at fixed physical y:

    partial_x [u^-q A_d(z)]
       =2k u^(-q+1-kappa) A_d'(z)
         +u^(-q-1)[-q A_d(z)-kappa z A_d'(z)].

Since kappa>3, the first term dominates the second as u tends to0. It also dominates partial_x R=O(u^-2). Therefore for z in I and0<u sufficiently small,

    |M_x(Y_d(u,z))| >= C u^(-q+1-kappa), C>0.

Locally Theta=a0u^2. The exact physical area element in (u,z) is u^kappa du dz. This funnel lies in every neighborhood of0 when u is small. Hence

    integral |Theta M_x| >= C a0 integral_0^epsilon u^(3-q)du = infinity,

because q>4. This proves the theorem.

The leading absolute divergence arises from differentiating across the very narrow funnel around the curved slow orbit. It does not conflict with the finite integral of |Theta_x M| or with smoothness of M away from0. A principal value or distributional derivative can involve cancellations that absolute integration does not permit. No such cancellation or finite-part identity is needed or claimed here.

## Dependencies and verification status

Only smooth ODE theory, elementary stream-function identities, compact radial cutoffs, the mean value theorem, and the explicit local characteristic formulas are used. Packet64 supplies the same Fubini argument, reproduced above. This proof is complete before any numerical illustration. The construction is deliberately not a global B2 profile; it identifies an additional estimate that an adjoint-based exclusion would have to justify from the full PDE. Eleven independent symbolic identities passed; own physical-flow quadrature and step/tolerance checks are summarized in verification/README.md. Actual claude-opus-5-5 request78 returned provider refusal without audit text; focused request79 also returned provider refusal without text after8.168405s. No external endorsement is claimed.
