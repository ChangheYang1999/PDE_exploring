# Realized angular temperature moments with sign-changing vorticity

Status: CONFIRMED conditional construction by the independent verifier. Written 2026-10-21 during shift5, before computation. This independently derives and audits the wider reference construction in lead/astra/impulse434, conditional on one already verified reference from126. It supplies exact thermal configurations, not solutions of the full vorticity equation. The vorticity changes sign, as146 proves.

## 1. Exact statement and fixed conventions

Fix beta>2, s=1/beta, m=1-2s, a0>0 and one reference from126. Write its relative stream as Psi_*, its relative velocity as V_*=(-Psi_*,y,Psi_*,x), W_*=beta X+V_*, its vorticity as Omega_*=-Delta Psi_*, and its temperature as Theta_*=a0 xi_*^2. Here xi_* is smooth, odd in x, positive on x>0, and W_*.grad xi_*=(beta-2)xi_*/2. On a prescribed disk D it has the exact polynomial core from126. Every backward trajectory tends to0. Outside a disk its relative stream equals a fixed shifted anisotropic formula Psi_ext, with the fixed linear term that makes V_*(0)=0. In particular V_ext=O_symbol(r^(1-s)). Fix

    w(theta)=1-(m+2)cos(theta)^2.

**Theorem.** There is a smooth one-parameter family of reference configurations, indexed by t in[0,1], with all the following properties. The members have the same beta, a0, polynomial core on D, parity, whole-plane backward basin, canonical relative velocity and exact thermal equation as above. Their streams equal the same Psi_ext outside one common disk. Their temperatures have expansions

    Theta_t=r^m A_t(theta)+O_symbol(r^(m-s)),

where A_t is smooth, reflection symmetric, positive off the vertical axis and has quadratic zeros there. All fixed-order symbol bounds are uniform in t and continuous in t. The two endpoint moments integral w A_t have opposite strict signs. Consequently some member has exactly zero moment. Each member has negative vorticity somewhere in x>0. The theorem imposes no vorticity sign condition, and does not assert the vorticity equation.

## 2. A compact auxiliary stream with radial exterior

Choose M so large that D lies inside B_M and W_*.e_r>=beta r/2 for r>=M. Choose a smooth radial cutoff kappa that is1 near B_M and0 outside B_(2M), taking values in[0,1]. Set Psi_0=kappa Psi_* and W_0=beta X+gradperp Psi_0. The term Psi_* gradperp kappa is tangential. Therefore

    W_0.e_r=beta r+kappa V_*.e_r>=beta r/2  (r>=M).

Beyond2M the drift is exactly beta X. The whole flow is complete because the vector field grows at most linearly. A backward trajectory outside B_M reaches its boundary in finite time: while outside, its backward radial coordinate decreases at least exponentially. The ball is invariant under backward flow since the drift points strictly outwards on its boundary. Inside, W_0=W_*; hence every backward trajectory converges to0.

Keep xi_0=xi_* inside B_M and extend it along forward trajectories from the boundary by xi_0(X(t))=exp((beta-2)t/2)xi_*(X(0)). The boundary is transverse, every exterior point reaches it backwards exactly once, and the vector fields agree on a neighborhood of it. The extension is smooth and agrees to all orders across the boundary. It is odd in x and positive on the right because trajectories preserve the two half-planes. Thus Theta_0=a0 xi_0^2 solves exact thermal transport. For r>=2M radial transport gives

    Theta_0(r,theta)=r^m A_0(theta).

The function A_0 is smooth and positive on the right. Its zeros at the two vertical directions are quadratic with nonzero coefficients. One way to check the last assertion without a tail assumption is to use the scalar equation for xi_0 and its transverse derivative on an axis characteristic. Its positive transverse derivative near the source obeys a homogeneous linear ODE with finite coefficients up to the fixed circle r=2M, so it remains nonzero. In the radial exterior its appropriately scaled derivative is constant.

## 3. Area-preserving angular maps and a smooth extension

Use x=r cos(theta), y=r sin(theta). Thus x-reflection is P(theta)=pi-theta, interchanging the right and left semicircles; theta->-theta would instead be the unassumed y-reflection. Let f be an orientation-preserving smooth circle diffeomorphism commuting with P(theta)=pi-theta. Require f to be the identity on neighborhoods of the two vertical directions. Define, away from0,

    F_f(r,theta)=(r/sqrt(f'(theta)), f(theta)).

The area form transforms to R dR dphi=r dr dtheta; the term containing dtheta in dR drops from this wedge product. Thus F_f preserves area. It is homogeneous of degree1. Compatible lifts on the two half-circles give an isotopy f_u=(1-u)id+u f with positive derivative for0<=u<=1. Its angular Eulerian generator is

    v_u(phi)=partial_u f_u(f_u^(-1)(phi)),

and its radial generator is -r v_u'(phi)/2. These are the polar components of gradperp H_u for H_u=r^2 v_u(phi)/2. Choose a smooth radial cutoff zeta, zero on a disk containing D and one beyond a larger disk. The Hamiltonian zeta H_u is smooth everywhere, since it is identically zero near0. Its vector field is divergence free and at most linear, uniformly over u. Its time-one map Ftilde_f is therefore a globally defined smooth area-preserving diffeomorphism, equal to the identity on D. Reflection gives v_u(pi-phi)=-v_u(phi), so zeta H_u is odd in x and the flow commutes with reflection.

For sufficiently large starting radii the complete homogeneous isotopy stays where zeta=1. Indeed the homogeneous radius is the starting radius divided by sqrt(f_u'), whose factor has positive upper and lower bounds on the compact parameter-angle domain. Uniqueness of the ODE then gives Ftilde_f=F_f outside one disk. This proves the required extension; smoothness at the origin was not assumed for the original homogeneous map.

Push forward W_0 by Ftilde_f and pull back xi_0 by its inverse. Call the resulting fields W_f, xi_f and Theta_f=a0 xi_f^2. The chain rule proves exact transport, and conjugacy proves the whole-plane backward basin. All fields agree with the original reference on D. Area preservation implies div W_f=2beta. Outside one disk, W_0=beta X and DF_f(X)X=F_f(X), so W_f=beta X. Consequently V_f=W_f-beta X is compact, smooth, divergence free and reflection equivariant.

There is a compact odd stream for V_f. Explicitly set Psi_f(x,y)=integral_0^x V_f,2(u,y)du. The divergence equation and V_f,1(0,y)=0 give Psi_f,y=-V_f,1, while Psi_f,x=V_f,2. Parity makes Psi_f odd. Outside a disk containing supp V_f its gradient vanishes; that exterior is connected and meets the axis, where Psi_f=0. It is therefore zero on that entire exterior. By146 this compact stream necessarily has a negative-vorticity region in the right half-plane, since the positive core was retained.

The homogeneous angular map gives the exact tail formula

    A_f(f(theta))=f'(theta)^(m/2) A_0(theta),
    A_f(phi)=A_0(g(phi))/g'(phi)^(m/2), g=f^(-1).     (1)

This follows by substituting r=R sqrt(f') into Theta_0=r^m A_0. It is an actual transported temperature, not freely assigned angular data.

## 4. Both signs can be realized

Work on I=(-pi/2,pi/2) and reflect to the other half-circle. Choose theta0 in I with A_0(theta0)>0. For either sigma=+1 or-1, choose closed intervals J contained in the interior of J' contained in I on which sigma w>=c>0. Both choices exist: w(0)=-(m+1)<0 and w approaches1 at the endpoints of I.

Choose a smooth d0>=0 on the closed interval I, zero exactly on J, strictly positive outside J, equal to1 near the endpoints of I, such that its integral over I is pi and its integral from the left endpoint to the left endpoint of J is theta0+pi/2. To construct it, take small endpoint neighborhoods and positive smooth functions on each component of I minus J that vanish to all orders on J, with integrals initially smaller than the two positive targets theta0+pi/2 and pi/2-theta0. Add independent positive bumps on those two components to attain the targets. Compactness gives a positive lower bound for d0 outside J'. Put

    d_epsilon=epsilon+(1-epsilon)d0,
    g_epsilon(phi)=-pi/2+integral_(-pi/2)^phi d_epsilon.

For every fixed0<epsilon<1/2 this is a smooth increasing diffeomorphism, the identity near both endpoints. On the left semicircle define g=P g_right P. The two pieces are identical to the identity near their common endpoints, so this gives a smooth orientation-preserving circle map commuting with P. No oddness of g on I or symmetry under theta->-theta is required. The initial A_0 is already a smooth P-invariant full-circle function from section2, so no arbitrary nonsmooth reflected amplitude is being introduced. On J, g_epsilon'=epsilon and g_epsilon converges uniformly to theta0. Formula(1) then gives A_f>=c1 epsilon^(-m/2) on J for small epsilon. Outside J', the derivative g_epsilon' has a uniform positive lower bound, so A_f is uniformly bounded there. The remaining part J' minus J contributes with the chosen sign and is finite for every fixed positive epsilon, since g_epsilon'>=epsilon and A_0 is bounded. The weight satisfies w(P(theta))=w(theta), and g'(P(theta))=g'(theta). Formula(1) makes A_f P-invariant. Reflection therefore doubles the right-semicircle integral, whence

    sigma integral_circle w A_f >=c2 epsilon^(-m/2)-c3>0

for small enough fixed epsilon. This yields two finite smooth maps f_- and f_+ with strict opposite moment signs. No singular map at epsilon=0 is used.

## 5. Restore the common exterior and retain the signs

For either fixed map choose N beyond the support of Psi_f and beyond the original exterior matching radius. With a smooth radial cutoff chi_N equal0 near B_N and1 outside B_(2N), define

    Psi_f,N=Psi_f+chi_N Psi_ext.

The exterior formula is used only where it is defined. The stream agrees with Psi_f on B_N and with Psi_ext outside B_(2N). The restored drift equals beta X+E_N for r>=N, with |partial^j E_N|<=C_j r^(1-s-j); these constants are independent of N. Its radial component is >=beta r/2 for all sufficiently large N, since the derivative-of-cutoff contribution is tangential. The backward basin, center and smooth exact transport are preserved by the same boundary construction as in section2. The negative-vorticity point of the compact auxiliary stream remains unchanged inside B_N.

For the exterior transport write ell=log r, b=r^-m Theta and e=E_N/r. Along a trajectory parametrized by ell,

    dtheta/dell=e_theta/(beta+e_r),
    db/dell= -m e_r b/(beta+e_r).

The coefficients and every fixed number of cylindrical derivatives are O(r^-s), whose integral from N to infinity is O(N^-s). Differentiating the angular-flow ODE shows that its first angular derivative is exp of an integrable coefficient, hence bounded away from0. Higher derivatives follow inductively from linear equations with integrable coefficients and already bounded lower derivatives. The amplitude equation has the same property. Thus the limiting scattering map S_N is id+O_Cj(N^-s), and its amplitude multiplier M_N is1+O_Cj(N^-s). Since the trace at N is A_f,

    A_f,N(S_N(theta))=M_N(theta)A_f(theta),
    A_f,N=A_f+O_Cj(N^-s).                            (2)

The constants may depend on the fixed map f. Choosing N large preserves each strict endpoint sign. Integrating only from r to infinity yields the stated symbol remainder in the temperature. Reflection fixes each vertical direction, and the angular map has a nonzero derivative there; the nonzero multiplier consequently preserves the quadratic zeros and positivity elsewhere.

The resulting relative velocity is canonical. Its vorticity has the fixed O_symbol(r^-s) tail, so the subtracted whole-plane inverse exists and grows sublinearly, as in135. The constructed V also has this divergence, negative curl, sublinear growth and value0 at the center. The difference between these two velocities has entire harmonic components. The interior harmonic gradient estimate on larger disks forces every derivative of their sublinear difference to vanish; it is constant, and its value0 at the center makes it zero. This checks that the stream construction has not appended a free strain or an independent drift.

## 6. A common continuous family and zero angular moment

Use lifts on I and set g_t=(1-t)g_-+t g_+. They have a common neighborhood of the endpoints where they are the identity. Their derivatives have a uniform positive lower bound, so their inverses f_t and all fixed-order derivatives depend smoothly on t. The cutoff Hamiltonian construction can use one fixed cutoff. The homogeneous radial factors are uniformly bounded on the compact parameter domain, so all auxiliary streams have support in one common disk. They and their transported temperatures depend smoothly on t on compact sets.

Choose a single N outside that disk, large enough to retain both endpoint signs in(2). The restored exterior drift is now independent of t; only its incoming temperature trace varies. The scattering formulas show that every A_t and its derivatives depend continuously on t. The exterior symbol estimates, and the bounds on the compact interior, are uniform at every fixed order. The intermediate value theorem gives integral w A_t*=0 for some t* in(0,1). All constructions at this parameter are finite and smooth. This proves the theorem.

## 7. Scope and dependencies

Dependencies: the verified126 reference; smooth scalar ODEs and transport on an outgoing region; area preservation for Hamiltonian flows; compact-stream sign loss146; the canonical relative inverse estimates135. The resulting family has no fixed sign of vorticity. Its common exterior stream does not mean its exterior temperature is fixed. The latter varies precisely through A_t. A zero leading angular moment does not alone make a finite-radius glued impulse zero. That separate conclusion requires continuity of the gluing construction, addressed in148. Nothing here constructs a B2 profile or decides the prompt's full endpoint.

Initial complete draft saved 2026-10-21T08:34:02.599798+00:00. Final independent verification completed 2026-10-21T09:30:38.893111+00:00.

Audit evidence:18 independent manufactured controls passed at2026-10-21T08:39:50.489407Z in0.521417s; see verification/SUMMARY.md. The C7 manufactured maps test exact area and homogeneity formulas, both moment signs at three exponents, and exterior scattering decay. They are not the actual126 reference or smooth B2 profiles. ActualOpus227 supplied a written scalar-moment review, and229 explicitly withdrew its symmetry objection after recognizing that theta->-theta is y-reflection. Its remaining weight and endpoint-regularity hypotheses are satisfied by the explicit w and the already smooth full-circle A_0 above. The reviewer's incidental radius-preserving angular extension is not used: our area-preserving extension includes1/sqrt(f'), whose P-invariance follows from f'(Ptheta)=f'(theta). Requests for complete geometry/whole-construction reviews returned no written audit, as recorded in the evidence; no endorsement is inferred. The complete Hamiltonian, scattering and inverse arguments are independently proved above.
