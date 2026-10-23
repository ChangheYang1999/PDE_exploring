# Exact polynomial primitive of the hydrostatic inverse on the axis

Written on 2026-10-21 before the implementation. This result concerns finite trial densities and the hydrostatic inverse. It is not an existence theorem for the hydrostatic problem or Setting III.

## Statement and notation

Let P > 1 and L > 0. Set sigma=(1+t)/2, w=(1-t)/2 and Q=w+2P sigma. The compact radial coordinate t belongs to [-1,1), with

    r(t) = L sqrt(sigma)/(2w)^P.

Let beta_k(t) be real polynomials for 0 <= k < M and put

    g(x,y) = y H(t,theta),
    H(t,theta) = w sum_k sigma^k beta_k(t) cos(2k theta).

Here r=sqrt(x^2+y^2) and theta is its polar angle. This extends smoothly through the origin because sigma is an analytic function of r^2 near zero and sigma^k cos(2k theta) is analytic there. For fixed finite polynomials it has sublinear growth exponent p=1-1/P in (0,1), with the required derivatives. Write H_A(t)=H(t,pi/2), a=beta_0(-1), and define the polynomial J by

    J(-1)=0,
    J'(t)=sum_{k>=1} k^2 (-1)^k Q(t) sigma(t)^(k-1) beta_k(t).

Define the polynomial K(t)=-H_A(t)-J(1)+J(t). Then the canonical hydrostatic inverse satisfies, for y>=0,

    d_y V_2(0,y) = K(t(y)),
    V_2(0,y) = integral_0^y K(t(s)) ds,
    c_H = d_y V_2(0,0) = -a-J(1).

The second identity is a finite integral. No artificial exterior boundary condition or finite cutoff is used: J(1) is the exact full-tail primitive. The first identity is algebraic after exact rational reconstruction when the coefficients, P and nodes are rational, as they are for the saved binary numbers.

For any real transport coefficient c define G(y)=g(0,y), v(y)=cy+V_2(0,y), R_A=vG'-G. Its pointwise denominators are

    N_f=|vG'|+|G|,
    N_v=|G|+|yG'|+|V_2 G'|.

These coincide with the prompt's denominators on the axis for the hydrostatic transport equation. Ratios at zero denominators are undefined and are not replaced by zero. They are not residuals of the original full-plane elliptic inverse.

## Proof

For y>0, write z=log r. Direct polar differentiation at theta=pi/2 gives

    g_xx(0,y) = (H_z + H_{theta theta})(t(y),pi/2)/y.

For completeness, differentiate g=yH at fixed y. At x=0 one has r_x=0, r_xx=1/y, theta_x=-1/y and theta_xx=0, hence g_xx=H_r+H_{theta theta}/y. Since H_r=H_z/y this is the stated formula. Also dH_A/dy=H_z/y.

Logarithmic differentiation of r=L sqrt(sigma)/(2w)^P gives

    dt/dz=4 sigma w/Q.

At the axis H_{theta theta}=-4w sum_{k>=1} k^2 (-1)^k sigma^k beta_k. Thus

    H_{theta theta} dz
      = -sum_{k>=1} k^2 (-1)^k Q sigma^(k-1) beta_k dt
      = -J'(t) dt.

Consequently

    integral_0^y g_xx(0,s) ds = H_A(t(y))-a-J(t(y)).

The endpoint at zero is legitimate: H_A tends to a, and the integrand is O(y). At infinity H_A tends to zero because of its factor w, while J tends to its polynomial endpoint J(1). Since g_xx=O(y^{p-2}) with p<1, the integral converges absolutely. Therefore its total is c_H=-a-J(1), and subtracting the finite partial integral gives

    integral_y^infinity g_xx(0,s) ds = -H_A(t(y))-J(1)+J(t(y))=K(t(y)).

The canonical hydrostatic inverse is V_2(0,y)=integral_0^y s g_xx(0,s) ds + y integral_y^infinity g_xx(0,s) ds. Differentiating the two terms cancels the boundary contributions, giving d_y V_2=K. Odd parity gives V_2(0,0)=0, so integration proves the finite formula. In particular K(1)=0, a useful exact endpoint check. All sign conventions agree with V=(-Phi_y,Phi_x), -Phi_yy=g_x.

## Exact representation and independent verification

Compute H_A, J' and the Chebyshev antiderivative J using rational arithmetic. The antiderivative formulas are integral T_0=T_1, integral T_1=T_2/4, and for n>=2,

    integral T_n = T_{n+1}/(2(n+1)) - T_{n-1}/(2(n-1)).

Choose the constant so J(-1)=0. Exact differentiation then returns J'; K(1)=0 and K(-1)=c_H hold exactly. These are algebraic checks, separate from numerical quadrature.

Evaluate the finite integral of K(t(s)) by composite Gauss-Legendre quadrature in physical s using two orders and multiprecision arithmetic. Recover t(s) by monotone bisection on sigma in (0,1), or a safeguarded root solve of r(sigma)=s. This radial inversion differs from the double precision reader. Compare its density derivatives against scalar multiprecision differentiation and compare V_2, R_A and both normalized residuals against result187's independent infinite-tail Jacobi quadrature. Manufactured low-degree polynomials admit direct checks of K'=-g_xx and full-line inverse agreement. Quadrature differences and precision refinement are empirical error checks, not interval enclosures.

## Dependencies and scope

The only mathematical dependencies are polar differentiation, convergent one-dimensional integration and polynomial identities proved above. The full-line hydrostatic inverse and the original anisotropic limit are derived separately in results174,175 and185. This computation uses the saved finite density, not the producer's inverse, differentiation matrices or optimizer. The reconstruction metadata must identify the same density before a result is attributed to a producer state. An observed nonzero residual disproves exact satisfaction by that trial density only; it gives no nonexistence result for either PDE.
