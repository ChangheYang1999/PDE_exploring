# Arbitrary values of the strain functional with fixed positive fields and center jets

Date:2026-10-20. Status: independently proved below. This is a family of smooth nonprofiles, including beta2.

## Statement, hypotheses and notation

For every beta>=2 there exist a fixed smooth odd-in-x vorticity Omega, its canonical relative velocity V, and a number a0>0 with the following properties. Put nu=1/beta and c=1+beta/2. Then

    V(0)=0, div V=0, -curl V=Omega, DV(0)=diag(-c,c),
    Omega_x(0)=4a0/beta, Omega(x,y)>0 for x>0.

The inverse is the absolutely convergent centered full-plane integral with K(z)=(z2,-z1)/(2pi|z|^2), and V=o(r). For every real number M there is a smooth even-in-x temperature Theta_M, zero on the entire axis x=0 and strictly positive on x>0, such that

    Theta_M=a0 x^2+O(r^4) near0,
    J(Omega,Theta_M)=M,

where

    f(x,y)=xy/r^4, g=partial_x f,
    J(Omega,Theta)=integral Omega V.grad f
                   -(1/2)integral Theta V.grad g.

All integrals here converge absolutely. For every integer j>=0 the fields obey at infinity

    D^j Omega=O(r^-nu-j), D^j V=O(r^(1-nu-j)),
    D^j Theta_M=O(r^(1-2nu-j)).

Also Omega/x and Theta_M/x^2 are respectively O((1+r)^(-1-nu)) and O((1+r)^(-1-2nu)); their axis limits are smooth and strictly positive. These are size bounds for the constructed fields, not assertions that they solve the transport equations.

In particular M=pi c gives the single integrated strain identity of a B2 profile, together with the displayed signs, inverse, center jets and decay. This works at beta=2 as well as beta>2. Every constructed field fails temperature transport far out. The conclusion establishes neither a profile nor simultaneous validity of the other homogeneous identities.

## 1. A fixed admissible vorticity and its velocity

Choose a nonnegative, radially symmetric, smooth unit-mass bump eta supported in a disk of radius less than1/4 about0. Let A=(1,1), A*=(-1,1), and

    Omega_b(X)=Gamma[eta(X-A)-eta(X-A*)], Gamma=2pi c.

The supports are disjoint and avoid the center and the entire axis. Thus Omega_b is odd in x, nonnegative in x>0 and identically zero near0. Its canonical relative inverse V_b is smooth. It decays to a vertical constant at infinity, with the nonconstant part O(r^-2), because the two masses have total mass0. The constant is the prescribed center subtraction, not an added strain.

The function f=xy/r^4 is harmonic away from0. Radial averaging of a harmonic function over each blob therefore gives its exact value at that blob center. The center strain is exactly

    c_b=(1/pi)integral f Omega_b
       =(Gamma/pi)[f(A)-f(A*)]=Gamma/(2pi)=c.

The other entries of DV_b(0) vanish by the x parity of its stream. Hence DV_b(0)=diag(-c,c).

Put q=(1-nu)/2, so q>0 for beta>=2. Define

    Psi_t=-x(1+r^2)^q,
    Omega_t=-Delta Psi_t
            =4q x(1+r^2)^(q-2)[2+(q+1)r^2].

This is smooth, odd in x, even in y and positive on x>0. Its gradient at0 is (8q,0). The velocity J_+ grad Psi_t, after subtracting its value at0, has derivative0 at0 and growth O(r^(1-nu)). It equals the centered canonical inverse of Omega_t: both fields have identical divergence and curl, are sublinear, and vanish at0. Their difference is an entire harmonic sublinear field, hence constant by the interior harmonic derivative estimate and then zero.

Fix any mu>0 and set

    Omega=Omega_b+mu Omega_t,
    V=V_b+mu V_t, a0=2beta q mu.

All asserted vorticity signs, jets, inverse conditions and tail bounds follow. In particular the tail does not change the center strain and Omega_x(0)=8q mu=4a0/beta. Define the base temperature

    Theta_0=a0 x^2(1+r^2)^(-(1+2nu)/2).

It has all the asserted temperature properties. Neither mu smallness nor a sign of the vorticity quadratic functional is needed in this proof.

## 2. Two temperature bumps vary the functional in opposite directions

The function g=partial_x f=y(y^2-3x^2)/r^6 is even in x and homogeneous of degree-3. Let C(X)=V(X).grad g(X). Since V(X)=c(-x,y)+O(r^2),

    C(X)=c(-x partial_x+y partial_y)g(X)+O(r^-2).

At x=0 the leading term equals -3c/y^3. It is negative on the upper axis and positive on the lower axis. By homogeneity and continuity of the leading angular factor, there are narrow fixed cones about those axes where its sign remains the same. For sufficiently small radii the O(r^-2) remainder is dominated by the leading term of order r^-3. In each cone choose a nonzero nonnegative smooth even-in-x bump H_+ or H_-, whose support is compact, avoids the axis and the origin, and lies in that small annulus. Here H_+ is the upper bump and H_- the lower one. Consequently

    B_+=integral H_+ C<0, B_-=integral H_- C>0.

The bumps can be paired across x=0 inside their respective cones to enforce evenness. They vanish in a neighborhood of every point of the axis and outside a compact set, so all center jets, all axis values of the quotients, and all tails of Theta_0 remain unchanged.

Write J0=J(Omega,Theta_0). If M>=J0, set

    Theta_M=Theta_0+[2(M-J0)/(-B_+)] H_+.

If M<J0, set

    Theta_M=Theta_0+[2(J0-M)/B_-] H_-.

The added coefficients are nonnegative. Direct substitution gives J(Omega,Theta_M)=M. Strict positivity in x>0 follows from Theta_0>0 there.

Near0, Omega=O(r), V=O(r), Theta=O(r^2), grad f=O(r^-3) and grad g=O(r^-4). Thus the two absolute integrands, including polar area, are bounded by a constant times dr. At infinity they are bounded respectively by C r^(-1-2nu)dr and C r^(-1-3nu)dr. This proves the stated absolute convergence and makes the linear changes in the functional legitimate. Compact bumps do not change any tail derivative bound.

## 3. Explicit nonprofile defect and the beta2 case

For sufficiently large x>0 on y=0 all temperature bumps vanish. The horizontal component of V_t and the y derivative of Theta_0 vanish there. Since V_b,1(x,0)=O(x^-2), direct differentiation yields

    [W.grad Theta_M-(beta-2)Theta_M]/Theta_M
      =(beta+2)/(1+x^2)
        +V_b,1(x,0)[2/x-(1+2nu)x/(1+x^2)]
      =(beta+2)x^-2+O(x^-3)>0,

where W=beta X+V. Thus no member of the family solves temperature transport, regardless of M.

At beta2 the same construction has q=1/4,a0=mu and bounded Theta_0. The vorticity also fails its transport equation. On the same positive x ray,

    Omega=mu[(5/4)x^-1/2-(3/16)x^-5/2+O(x^-9/2)],
    Theta_x=2mu x^-3+O(x^-5).

Therefore

    W.grad Omega+Omega-Theta_x
       =(3mu/4)x^-5/2+o(x^-5/2),

because the horizontal blob advection is O(x^-7/2) and the tail's horizontal velocity is zero on that ray. For beta>2 the corresponding leading defect is -a0(1-2/beta)x^(-2/beta)+o(x^(-2/beta)), as in packet69. Both equations fail explicitly.

## Dependencies, audit status and scope

The proof uses the harmonic mean-value property, elementary tail differentiation, centered full-plane inverse uniqueness and local sign continuity. It was written before numerical checking. Packet69 supplies a related one-sided bump construction with beta>2 and a radial-blob limit; the present two-sided adjustment removes its beta2 limitation and does not rely on that limit or its margin. No formal proof assistant or server is used.

This does not show that the full family of homogeneous identities can hold for a nonprofile. Under their stated bounds that family is equivalent to the PDE. It does not impose or verify global-source dynamics. It shows exactly that this single scalar functional has every real value among smooth fields with the specified positive signs, center jets and tails. Thus its lack of a fixed sign applies to the whole functional, not only its vorticity part.
