# Angular improvement of the homogeneous-tail error

## Statement

Retain every convention and hypothesis of ../PROOF.md: 0<a<1, b>0,
the exact admissible projection witness f, its midpoint m, the kernel
K(z)=(z_1^2-z_2^2)/(2 pi |z|^4), the homogeneous limiting function g_inf,
and the constants B and a3(a). For R>1/2 put q_R=1/(4R^2). Then

    | integral_(|z-m|>R) [K(z-e1)-K(z)] f(z) dz
        - 2 a3(a) R^(a-1)/(1-a) |
    <= 4B/(pi R) + B/(3 R^3(1-q_R)^2)
         + R^(a-3)/(2(3-a)(1-q_R)^2).                  (1)

One may take the minimum of this error and the parent error. Both are
explicit global bounds, and neither changes the local identity term or
principal-value convention. The result concerns homogeneous seminorms.

## Proof

In midpoint polar coordinates w=z-m=r exp(i theta), let

    nu(w)=K(w-e1/2)-K(w+e1/2),
    d(w)=cos(3theta)/(pi r^3).

The parent proof establishes |f(m+w)-g_inf(w)|<=B, |g_inf(w)|<=r^a/2,
and the absolutely convergent estimate

    |nu(w)-d(w)|<=1/(2 pi r^5(1-q_R)^2) for r>R.

Decompose the difference of the tail integrands exactly as

    nu f-d g_inf = d(f-g_inf)+(nu-d)(f-g_inf)+(nu-d)g_inf.

The first term is bounded using the angular cancellation in size:

    integral_(r>R) |d| B
      = B/pi integral_R^infinity r^(-2)dr
                       integral_0^(2pi)|cos(3theta)|dtheta
      =4B/(pi R).

The second term is at most

    B/(1-q_R)^2 integral_R^infinity r^(-4)dr
      =B/(3R^3(1-q_R)^2).

The third term is at most

    1/(2(1-q_R)^2) integral_R^infinity r^(a-4)dr
      =R^(a-3)/(2(3-a)(1-q_R)^2).

All three integrals are finite for the stated range. The parent proof
computes integral d g_inf exactly as the main term in (1). Summing the
three bounds proves the theorem. Taking a minimum of two independently
valid absolute bounds is valid.

## Dependencies and scope

Only the explicit signed-distance witness comparison and dipole identity
of the parent proof are used. Finite-region coverage and interval arithmetic
must still be audited before a numerical operator bound is accepted.
The present analytic improvement is awaiting independent cross-read.
