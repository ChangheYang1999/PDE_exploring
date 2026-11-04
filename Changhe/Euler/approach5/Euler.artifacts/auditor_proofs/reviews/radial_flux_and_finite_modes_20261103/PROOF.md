# Radial flux and finite angular spectra

Status: CONFIRMED in A635-A637 after complete independent reconstruction and postread. These are two distinct conditional rigidity arguments. Section6 is a kinematic countertest to identifying their hypotheses.

## 1. An ordinary homogeneous radial-zero theorem

Let D=R3 minus {0}. Let 1<p<2 and let V in C1(D;R3) be divergence free and ordinarily homogeneous: V(rx)=r^(-p)V(x) for all r>0. Set W=curl V. Assume

    x.V(x)=0 implies W(x)=0, for every x in D.                 (1)

Then V=0. No pressure, helicity, scalar weight or momentum equation is assumed.

Write V(rn)=r^-p(R(n)n+T(n)) on the unit sphere, where R and the tangent field T are C1. Put d=p-1>0 and s=2-p>0. The spherical divergence identity and its integral give

    div_S T=-sR,                 integral_S R=0.               (2)

Expanding Cartesian derivatives and using DV x=-pV gives

    x cross W=grad(x.V)+(p-1)V.

Its tangential restriction to the sphere is n cross W=grad_S R+dT. Thus (1) implies

    T=-grad_S R/d on {R=0}.                                   (3)

Let F=-T. Its C1 flow Phi_t is complete on the compact sphere, and every finite-time map is a C1 diffeomorphism. The set O={R>0} is forward invariant. Indeed, at a first finite contact with R=0 and grad_S R!=0, the derivative of R along the orbit is |grad_S R|^2/d>0, whereas a differentiable function positive before its first zero has nonpositive derivative there. If instead grad_S R=0, (3) makes F=0 at contact; uniqueness backwards makes the original orbit this equilibrium. Both alternatives contradict a start in O.

Since div_S F=sR, the area Jacobian for n in O and any t>0 is

    J_t(n)=exp(s integral_0^t R(Phi_tau(n))d tau)>1.

If O were nonempty, it would have positive finite area, and change of variables would give

    area(Phi_t(O))=integral_O J_t dA>area(O).

This contradicts Phi_t(O) subset O. Hence R<=0. Its zero integral and continuity give R=0, and (3) then gives T=0. This proves the theorem without regularity of the zero-set boundary or a Sard argument. More generally, (2)-(3) alone force R=T=0 for any positive d,s.

At p=2, V=Qx/|x|^3, Q!=0, is divergence free on D and has no radial zero, so (1) is vacuous. It refutes extension to that endpoint. No statement at p=1 is made.

## 2. A conditional scalar consequence at omega=0

Let 1/3<c<1/2, p=(1-c)/c, a=1-2c, and let V satisfy the assumptions before (1), with the stronger local regularity C1,alpha for EVERY alpha<1. Let sigma in C1(D) have ordinary degree -nu/c, where nu>a. Assume

    W.grad sigma=0 on D,
    grad(c x.V) cross grad sigma=0 on {W!=0},
    w=|sigma|^(a/nu) is locally A2.                           (4)

Here local A2 means w and 1/w are locally integrable and their product of ball averages is bounded on each relatively compact neighborhood. The independently proved localization A609 applies exactly to (4). It says W!=0 implies c x.V!=0. Its contrapositive is (1), so Section1 gives V=0.

The EVERY-alpha and A2 assumptions are used only in the imported localization, not in Section1. For an actual natural helicity-free nonrotating tail, sigma=S=P2-|V|^2/2 and nu=2(1-c) give this consequence when its A2 premise holds. The full nonrotating profile exclusion A053 is stronger and already available; this is not a new unconditional profile theorem.

## 3. A nodal finite-spectrum theorem for actual tails

Let 2/5<c<1/2, let omega be any finite real number, and put

    Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c,
    d=p-1, a=1-2c=cd, eta=d/(2p).

Let U in C2(R3;R3), P in C1(R3) solve

    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    div U=0, U.curl U=0.                                     (5)

Assume uniform U->0 and DU=O(r^(1/2)), or assume the explicit natural bounds U=O(r^-p), DU=O(r^(-p-1)). Use the ACTUAL velocity and canonical pressure tails V,P2 from the confirmed tail theorems. Set W=curl V, k=(Ax).V and S=P2-|V|^2/2. Suppose |S|^eta is locally A2 on D.

In spherical coordinates z=cos theta, s=sqrt(1-z^2), chi=phi+(omega/c)log r, suppose

    V=r^-p[R(z,chi)e_r+H(z,chi)e_theta/s+F(z,chi)e_phi/s],    (6)

where R,H,F are real trigonometric polynomials in chi of degree at most an integer N>=1, with the actual Cartesian regularity of V at both poles. Assume

    eta not in {j/m: 1<=j<=N, 1<=m<=2N}.                     (7)

Then U=0. The hypotheses impose the spectral bound and A2; neither follows from bare decay.

## 4. Polynomial rank and continuation through irrotational bands

The actual regularity is V in C1,alpha_loc and P2 in C2,alpha_loc for every alpha<1. Write t=omega/c and

    k=c r^-d K, K=R-tF,             S=r^-2p h.

The entries of DV in the spherical orthonormal frame are linear combinations of R,H,F and their first derivatives with coefficients depending only on z. Therefore tr((DV)^2) and |V|^2 have degree at most2N. This assertion uses the trace in that frame; Cartesian frame factors must not be counted as extra scalar frequencies.

The global canonical pressure has no higher frequencies. In fact a homogeneous harmonic pressure component with scalar degree -2p in r has spherical operator

    M=Delta_S+t^2 Z^2+t(1-4p)Z+2p(2p-1), Z=partial_chi.

On a spherical harmonic of degree l and angular frequency m its eigenvalue is

    -l(l+1)-t^2m^2+i t(1-4p)m+2p(2p-1).

If tm!=0 it has nonzero imaginary part. If tm=0, it could vanish only for l=2p-1, strictly between1 and2. Thus it never vanishes. Fourier projection commutes with the Laplacian and twisted scaling, and the global regularity permits the complete spherical harmonic expansion. Projecting the Poisson equation above degree2N therefore gives zero. Consequently K has degree at mostN and h degree at most2N. This is a global pressure argument; local harmonic pressure additions are not permitted.

Let Z_v be the open set of z in (-1,1) at which W is not identically zero around the latitude. The spherical components of W are trigonometric polynomials. For z in Z_v one component is a nonzero polynomial, whose zeros on the circle are finite; hence W!=0 is dense on that circle.

The actual rank relation dk wedge dS=0 on {W!=0}, contracted with Ax and an angular vector, gives

    h K_chi=eta K h_chi.                                     (8)

Continuity extends (8) to every point of a latitude in Z_v. Localization A597 gives K!=0 and h!=0 at any vortical point, so neither polynomial is identically zero on that latitude. Real polynomials of positive degrees j,m have nonzero positive-frequency leading coefficients. The coefficient of frequency j+m in (8) gives

    (j-eta m)K_j h_m=0.

This contradicts (7). If just one polynomial is a nonzero constant, (8) forces the other to be constant also. Thus K and h are both independent of chi on each latitude in Z_v.

We first extend axisymmetry of k. Let f=(Jx).grad k. It vanishes on the closure of {W!=0}. On O=int_D{W=0}, the homogeneous identity

    grad k=-aV+(Ax) cross W                                  (9)

gives V=-grad k/a and Delta k=0. The rotation derivative f is harmonic on O, continuous on D, zero on its complement, and |f|<=C r^-d with 0<d<1. On O intersect {epsilon<r<R}, the harmonic function

    C epsilon^(1-d)/r+C R^-d

dominates |f| on both spheres and every remaining boundary point. The maximum principle on this bounded open set needs no boundary smoothness. Sending epsilon to0 and R to infinity proves f=0. Hence k is axisymmetric globally.

Next let I be a component of (-1,1) minus closure(Z_v). On its entire band W=0, so (9) makes V, its kinetic energy and its Poisson source axisymmetric. For every m!=0, the coefficient h_m equals the pressure coefficient there and solves

    ((1-z^2)h_m')'+[2p(2p-1)-m^2/(1-z^2)-t^2m^2
                                  +i t(1-4p)m]h_m=0.         (10)

If Z_v is nonempty, every such component I has at least one endpoint z0 in (-1,1). There is a sequence in Z_v tending to z0, along which h_m=0. Continuity and the existence of h_m'(z0) imply h_m(z0)=h_m'(z0)=0. Equation(10) is a regular linear ODE near this endpoint. Uniqueness for its first-order system gives h_m=0 on I. No singular initial condition is placed at a pole. On closure(Z_v) the same vanishing holds by continuity, so S is axisymmetric.

If Z_v is empty, continuity gives W=0 on D, including the poles. Then k is globally harmonic and bounded by C r^-d. The same barrier applied to k gives k=0 and (9) gives V=0, so actual-tail recovery gives U=0 directly.

## 5. Symmetry transfer and limitations

In the remaining case, Section4 proves axisymmetry of the ACTUAL S. Its degree is -2(1-c) in twisted time, its reciprocal weight is locally integrable by A2, and the actual identities supply W.grad S=0 globally and rank on {W!=0}. The independently proved symmetry transfer A622 therefore makes the actual V axisymmetric. A569-A570, the canonical axisymmetric-tail exclusion, then gives V=0 and U=0. This completes the proof of Section3.

Since 0<eta<1/6, (7) holds throughout the target interval for N<=3. It also holds at any finite N if eta is irrational. At N=4 the only possible exceptional values in this interval are eta=1/8 and1/7, equivalently p=4/3 and7/5, or c=3/7 and5/12. These are failures of this sufficient condition, not examples. N=0 is already A570.

No original or tail vorticity density is assumed. Scalar nodes and open irrotational regions are allowed. The zero-free CO35 integral has not been used across nodes. Vanishing low pressure multipoles, now known in the whole stated natural-profile class by A623, does not imply a finite velocity angular spectrum. Arbitrary spectra and a general proof of the A2 property remain open.

## 6. Why the radial-zero theorem does not use k when omega is nonzero

For 1<p<2 and omega!=0 set rho^2=x1^2+x2^2 and

    V=rho^2 r^(-p-3) Jx.

This is nonzero, smooth on D, ordinarily homogeneous of degree -p and axisymmetric, hence also twisted homogeneous when p=(1-c)/c. Its scalar multiplier is axisymmetric and div(Jx)=0, so div V=0. Writing the multiplier as q, curl V=grad q cross Jx+2q e3 is poloidal, so V.curl V=0. On the punctured axis q=0 and grad q=0, hence W=0. However

    k=(cx-omega Jx).V=-omega rho^4 r^(-p-3),

whose zero set is exactly that axis. Thus k=0 implies W=0, although V is not zero. This refutes the proposed substitution of k for x.V in Section1 even under divergence freedom, helicity freedom, smoothness on D and twisted homogeneity.

Off the axis, V/k=-Jx/(omega rho^2). It is closed but its integral along a positive azimuthal circle is -2pi/omega. Its nonzero period prevents a single-valued potential on that complement. The implication W=0 at zeros of k does not repair this topology. This field is singular at0 and has no supplied actual pressure compatibility or global profile extension. It is only a kinematic countertest.

## 7. Dependencies and verification

Section1 is self-contained. Section2 imports only A609 localization. Sections3-5 use the actual-tail regularity and identities, A597 localization, the global canonical pressure theorem A591, symmetry transfer A622 and axisymmetric exclusion A569-A570. The elementary harmonic barrier and Fourier and ODE arguments are supplied in full. Both complete submitted sources were read, and no computation is needed. Existing configured-model CO35 comparison is relevant and has been read; a focused comparison of this nodal extension is requested through the existing working files, without claiming that a reply has arrived.
