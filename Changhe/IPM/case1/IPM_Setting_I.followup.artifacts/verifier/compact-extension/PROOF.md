# A canonical compact extension of the analytic local solution

Date: 2026-10-20. Status: proved manufactured-field construction, not a stationary full-plane profile. Lead Claude Opus 5.5 reviewed the proof and independently checked its identities at15:37Z; AV33 confirms the proposed report text. It strengthens the local example in the lead's section6.3.1(c) by imposing the canonical inverse globally.

## Statement

Fix A>1, put c_l=(A+1)/2 and k=sqrt(2/A), and fix any X0,Y0>0. There are smooth compactly supported functions rho,psi on the plane such that rho is even in x and odd in y, rho=x^2 y a with a smooth and a(0)=1, and

    -Delta psi=rho_x,   U=(-psi_y,psi_x)=U_canonical[rho],
    psi_xy(0)=3c_l-1.

On the rectangle |x|<X0, |y|<Y0 they coincide with

    g(x)=A(1-cos(kx)),  w(x)=-(A/k)sin(kx),
    rho_local=g(x)y,   psi_local=(c_l x-w(x))y,

and solve the transport equation there exactly. They satisfy the admissible sublinear density and gradient growth bounds globally. Taking X0>pi/k includes both the normalized center and the first positive axial source P=(pi/k,0), together with the whole connecting axis interval. All local higher transverse coefficients G_j with j>=3 vanish, and their actual coupled axis hierarchy on that interval is that of the analytic local example.

The extended fields are not global transport solutions. At a nonzero attained extremum of rho their transport residual has normalized magnitude one for either normalizer used in the report. There is no positivity assertion away from the center and no approximation theorem for a global profile.

## The local identities

Write h(x)=c_l x+(A/k)sin(kx). Then h'=c_l+A cos(kx), h''=-Ak sin(kx), g'=Ak sin(kx), and h'(0)=c_l+A. Thus -Delta(hy)=g'y=rho_x. The local velocity and dilated field are

    U=(w-c_l x,(c_l-w')y),
    W=(w,(2c_l-w')y).

Since 2c_l=A+1 and w'=-A cos(kx),

    W.grad(gy)-gy = y [w g'+(2c_l-w'-1)g]
                 = y [-A^2 sin(kx)^2+A^2(1+cos(kx))(1-cos(kx))]=0.

Moreover g=x^2+O(x^4), psi_xy(0)=c_l+A=3c_l-1, w'(pi/k)=A and W_2/y=1 at P. This checks every sign without relying on the lead's summary.

## Compact extension preserving the axis factor

Choose an odd smooth compactly supported h_bar(x) agreeing with h on |x|<X0. Set

    H0=h_bar'(0)=c_l+A,   I=integral_0^infinity h_bar(x) dx.

Choose an odd smooth compactly supported q(x), vanishing on a neighborhood of [-X0,X0], with integral_0^infinity q=1. Such a q is the odd extension of a positive bump on an interval to the right of X0, divided by its integral. Choose an odd smooth compactly supported J(y), agreeing with y^3/6 on |y|<Y0, and put

    f(y)=J''(y),   j(y)=H0 J(y)-I f(y),
    psi(x,y)=h_bar(x) f(y)+q(x) j(y).

This is smooth and compact, odd in each variable, and equals h(x)y on the specified rectangle. The sole obstruction to making its integrated source vanish in both x tails is removed by the q term. Indeed,

    integral_0^infinity psi(x,y) dx = I f(y)+j(y)=H0 J(y),
    psi_x(0,y)=H0 f(y),
    integral_0^infinity Delta psi(x,y) dx
       =-psi_x(0,y)+(integral_0^infinity psi dx)''=0.

Now define on the entire plane

    rho(x,y)=-integral_0^x Delta psi(s,y) ds.

This is smooth, even in x, odd in y, and vanishes at x=0. The integral identity makes it zero beyond the x support of psi; it is also zero beyond its y support. Thus it is compactly supported. Its derivative is rho_x=-Delta psi. Smooth evenness and rho(0,y)=0 give a smooth x^2 factor by the integral Taylor formula. Oddness in y gives a smooth additional y factor. On the local rectangle the definition gives

    rho=[H0-h'(x)]y=A(1-cos(kx))y,

so the factor's value at zero is one. Smoothness, parity, normalization and growth are therefore verified globally, except that transport is deliberately required only on the interior rectangle.

An explicit separable density formula is useful for independent quadrature. Define the even functions H(x)=integral_0^x h_bar(s)ds and Q(x)=integral_0^x q(s)ds. Direct integration gives

    rho=[H0(1-Q)-h_bar'+I q'] J''
        +[I Q-H] J''''-H0 q' J.

It is exactly zero beyond the supports because Q=1 and H=I there. This formula also supplies an implementation independent of differentiating a two-dimensional interpolant.

## Why the inverse is canonical

Let Gamma=-(1/(2pi))log|X|, so -Delta Gamma is the unit point mass. Since psi is smooth and compactly supported,

    Gamma*rho_x=Gamma*(-Delta psi)=(-Delta Gamma)*psi=psi

as distributions, by integration by parts with a compactly supported test factor. The convolution is a well-defined smooth potential after the usual locally integrable logarithmic kernel is paired with rho_x. Its gradient is the canonical full-plane velocity. No harmonic field is chosen independently, and no boundary condition at a finite wall is imposed. Equivalently the two velocities solve the same div/curl system and decay at infinity, and their harmonic difference is zero.

In particular, both rho and U can be compactly supported for this sign-changing manufactured density. That is consistent with the IPM Fourier multiplier: the source was constructed to lie in this special range. It does not make transport hold outside the local rectangle.

## The necessary exterior failure

The density is nonzero near the center and has compact support, so it attains a strictly positive maximum or strictly negative minimum with nonzero value. At such a point grad rho=0. Therefore

    R=(c_l X+U).grad rho-rho=-rho,
    N_f=|rho|+sum_i |W_i rho_i|=|rho|,
    N_v=|rho|+|X.grad rho|+|U.grad rho|=|rho|.

Both normalized residuals equal one. The failure lies outside the rectangle, since R vanishes identically inside it. Thus an exact solution of every local equation on an arbitrarily large prescribed finite interior set, even with the correct global canonical inverse and normalization, does not establish the full-plane equation. This is a manufactured warning about finite-region evidence, not a counterexample to any claimed global theorem.

Dependencies: the explicit local trigonometric pair, smooth one-dimensional cutoffs, the integral Taylor formula, the distributional fundamental solution and an extremum argument. No proof-assistant build is used. A finite-smoothness polynomial-cutoff instance is sufficient for the numerical checks; the theorem itself uses smooth cutoffs.
