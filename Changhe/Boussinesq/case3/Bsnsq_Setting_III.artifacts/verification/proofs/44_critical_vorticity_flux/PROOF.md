# Critical vorticity flux at infinity

Date:2026-10-20. Verdict: CONFIRMED by independent derivation.
This verifies and extends lead notes/beta2_arc.md R6; it is a necessary
identity, not a nonexistence obstruction.

## Exact statement

Let beta>=2, W=beta X+V, div V=0, and let smooth real Omega,Theta solve
W.grad Omega+Omega=Theta_x on R2. Assume V=o(r),
|grad Theta|<=C(1+r)^(-2/beta), and

    Omega(r e_theta)=r^(-1/beta)[a(theta)+o(1)]         (1)

uniformly in theta, with continuous a not identically0. Also assume the
corresponding uniform bound |Omega|<=C(1+r)^(-1/beta), which follows
from(1) outside a disk and smoothness inside. Then the integral below
converges absolutely and

    int_R2 |Omega|^(2beta-2) Omega Theta_x dX
               = (1/2) int_0^(2pi) |a(theta)|^(2beta)dtheta >0.   (2)

Every class A B2 profile has these bounds by confirmed packet33, and
packet40 puts every polynomial-tail target profile into that class.
At beta2, packet39 requires no vorticity growth assumption. This
application imports those proved results, not additional integrability
of Omega: Omega is in fact excluded from L^(2beta).

## Proof

For p=2beta>=4, the scalar |s|^p is continuously differentiable even
when p is not an integer. The chain rule yields

    div(W |Omega|^p)
      =2beta |Omega|^p+p |Omega|^(p-2)Omega W.grad Omega
      =(2beta-p)|Omega|^p+p |Omega|^(p-2)Omega Theta_x.

At p=2beta the first term cancels identically. No division by Omega
is used at its zero set. The last integrand is bounded near finite
points and, at infinity, by C r^(-(p-1)/beta-2/beta)
=C r^(-2-1/beta), which is integrable in the plane.
Apply the divergence theorem on B_R, with normal e_theta and surface
measure R dtheta. The boundary integral is

    int [beta R+V(R e_theta).e_theta]
                  R^(-2)[|a(theta)|^p+o(1)] R dtheta
      -> beta int |a(theta)|^p dtheta.

Uniformity of(1), V=o(R), and boundedness of a justify this limit.
Absolute convergence permits the limit of the volume integral.
Dividing by p=2beta proves(2). Its right side is strictly positive
because a is continuous and nonzero somewhere. No statement that the
integrand is pointwise nonnegative is implied.

For any p>1 the same finite-radius calculation, without cancelling,
remains an exact disk identity. Passing to infinite integrals for a
noncritical p requires separate integrability conditions and is not
asserted here. At beta2,(2) reads int Omega^3 Theta_x=(1/2)int a^4.
It is compatible with the known circulation lower bound and supplies
a useful independent numerical consistency check.

Dependencies: chain rule, divergence theorem, and the explicitly stated
uniform decay and angular limit. The complete identity proof is above.
