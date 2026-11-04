# Finite regularity at a zero-vorticity polar interface

Status: CONFIRMED as a local regularity and parameter-reduction result. General interface exclusion remains OPEN.

## 1. Exact statement

Let 0<d<1/2, p=1+d, sigma=1-d, c=1/(d+2), q=2p/d and omega in R. Put A=cI-omega J, Jx=(-x2,x1,0), r=|x|, z=x3/r and w=1-z^2. Fix -1<h<1. On a full azimuthal one-sided band r>0,h<z<h+delta<1, let V be locally C1 and P2 locally C2 up to z=h, away from the origin. Assume V is axisymmetric, has no azimuthal component, is divergence-free, and satisfies

    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    -Delta P2=tr((DV)^2),
    dk wedge dS=0, k=(Ax).V, S=P2-|V|^2/2.

At r=1,z=h suppose curl V=0 and V.e_r=lambda!=0. Divide V,P2 by lambda,lambda^2; this preserves every equation even when lambda is negative. Then, for some real b and D!=1/q, on a smaller band,

    V=r^-p[R e_r+f e_theta/sqrt(w)], R=f'/sigma,
    f(h)=b, R(h)=1, R'(h)=db/(1-h^2),
    P2=r^-2p Q,
    Q=-D R^q+(R^2+f^2/w)/2.

The function f is the unique analytic germ solving the leading pressure equation with these initial data. Analyticity and parity were not assumed. The statement neither identifies the field on the other side of an actual interface nor excludes the surviving germs.

## 2. Reduction and the full gradient trace

Axisymmetry and scaling give the displayed form. Spherical divergence gives f'=sigma R, hence f is C2. Curl is

    curl V=r^(-p-1)(wR'-df)e_phi/sqrt(w).

This gives the stated first jet. Shrink until R>0. Since k=c r^-d R, its radial derivative is nonzero. Homogeneity and the rank identity give d(S/k^q)=0, so connectedness supplies the constant D and also axisymmetry of P2.

In the orthonormal spherical frame the gradient matrix, multiplied by r^(p+1), is

    [[-pR,-(wR'+f)/sqrt(w),0],
     [-pf/sqrt(w),R-f'-zf/w,0],
     [0,0,R+zf/w]].

Its squared trace gives the exact scalar equation

    (wQ')'+ell Q+T=0, ell=2p(2p-1),
    T=2(d^2+d+1)R^2+2zff'/w+2z^2f^2/w^2
      +2pfR'+2pf^2/w.

All terms are continuous at the interface under the assumed regularity.

## 3. The exceptional coefficient is impossible

Suppose D=1/q. Let w0=1-h^2, u=z-h and F(R)=-DR^q+R^2/2. Then F'(1)=0 and F''(1)=-2/d. Only the known expansions are needed:

    R=1+(db/w0)u+o(u),
    f=b+sigma u+(sigma db/(2w0))u^2+o(u^2).

The quadratic expansion of F(R) and f^2/(2w), compared with Q in C2, gives

    Q(h)=1/(2p)+b^2/(2w0),
    Q'(h)=sigma b/w0+h b^2/w0^2,
    Q''(h)=sigma^2/w0+4h sigma b/w0^2
       +(1-d-d^2)b^2/w0^2+4h^2b^2/w0^3.

No second derivative of R was used. Substitute in the pressure equation and set y=b/w0. Its residual is

    3d^2+2d+4+4h sigma y
      +[(3d^2+6d+4)w0+4h^2]y^2
    =4(hy+sigma/2)^2+(3d^2+6d+4)w0 y^2
      +2d^2+4d+3>0.

This is impossible. It covers every b, both signs of the original amplitude and every nonpolar latitude.

## 4. Analytic uniqueness

For D!=1/q, Q_R=R-DqR^(q-1) is nonzero at the initial point. The analytic implicit function theorem expresses R in terms of z,f,Q; hence R is C2 and f is C3. In the scalar pressure equation the coefficient of f''' is

    w[R-DqR^(q-1)]/sigma,

nonzero on a smaller neighborhood. The equation is an analytic first-order system for f,f',f''. Its unique analytic solution through

    f(h)=b, f'(h)=sigma, f''(h)=sigma db/w0

equals the given one-sided C3 solution by ordinary local uniqueness. Noninteger powers are analytic because R stays positive. This proves the claim without formal-series existence or a symmetry assumption.

## 5. The optional next scalar and scope

If a C1 scalar p1 additionally has twisted degree -(3-2c) and satisfies

    dk wedge d(p1-2V.grad P2)=0,

write m=3p+1 and gamma=m/d. The same integration gives, for a real constant C1,

    p1=r^-m[C1 R^gamma-4pRQ-2fQ'].

Here V.grad P2=r^-m(-2pRQ-fQ'). Thus p1 is analytic on this band as well. This reduction alone imposes no next-pressure compatibility or exclusion for b!=0. Zero radial amplitude, swirl, nonaxisymmetric local geometry and the poles are outside the theorem.

The full five-section LIT172 source was read. The gradient trace, finite-regularity quadratic expansion and sum of squares were independently derived by hand. No numerical check was needed. For actual profiles all the separate global zero-helicity, natural-rate and adjacent-band premises supplying the rank equations remain necessary.
