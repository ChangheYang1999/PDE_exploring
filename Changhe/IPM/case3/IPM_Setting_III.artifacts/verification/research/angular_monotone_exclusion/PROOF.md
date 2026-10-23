# Exclusion under a one-sided quotient and angular monotonicity

Status: CONFIRMED by independent mathematical reconstruction on2026-10-20. This audits the lead's QTHETA request at21:39Z. It is a nonexistence theorem for an explicitly smaller class, not the principal SettingIII NO endpoint.

## Exact statement

There is no smooth primary exact full-plane IPM profile satisfying both EXTRA conditions

    q(X)=rho(X)/(a y)<=1 everywhere,
    partial_theta q(r,theta)>=0 for r>0,0<theta<pi/2,       (S)

where a=rho_y(0)!=0 and q is smoothly extended across y=0.

The primary assumptions are ell>1; rho even in x and odd in y; psi odd in both coordinates; U=(-psi_y,psi_x); -Delta psi=rho_x; (ell X+U).grad rho=rho; the canonical law U=o(r); and strictly sublinear density and weighted-gradient growth. There is no added positivity of q, coordinate monotonicity, analyticity, strain bound, or nonflatness assumption.

Put D=ell-1>0 and A=2ell-1=2D+1. The theorem is invariant under the genuine spatial scaling, which leaves a,ell and(S) unchanged.

## The canonical angular strain identity and its sign

The first-order profile equation gives c=psi_xy(0)=-D. For the sine coefficient

    rho3(r)=(4/pi)int_0^(pi/2) rho(r,theta)sin(3theta)dtheta,

the cancellation-renormalized canonical inverse gives

    c=-a/4+int_0^infinity rho3(r)r^(-2)dr.                (1)

This formula is used only after its angular projection. It does not assert absolute convergence of the unprojected area kernel at the origin. Smooth parity gives rho3=O(r^3) at zero, and the strictly sublinear growth bounds it by O(r^gamma), gamma<1, at infinity. Thus the radial integral in(1) is absolutely convergent.

Since rho=a r sin(theta)q and

    d_theta(cos(theta)sin(theta)^3)
                   =sin(theta)sin(3theta),

integration by parts on each fixed circle gives

    rho3(r)/a=-(4r/pi)int_0^(pi/2)
                          cos(theta)sin(theta)^3 q_theta dtheta.

The boundary term vanishes because q is smooth on the circle and the explicit weight vanishes at both endpoints. Inserting this into(1) yields

    D/a=1/4+(4/pi)int_0^infinity int_0^(pi/2)
                           cos(theta)sin(theta)^3 q_theta dtheta dr/r. (2)

The integrand in(2) is nonnegative under(S). Its circular integral is -pi rho3/(4ar), so absolute convergence of(1) makes the nonnegative double integral finite. Tonelli's theorem permits either order. In particular the right side of(2) is at least1/4. Since D>0 and a!=0, this proves

    0<a<=4D.                                            (3)

The sign of a is a conclusion of(2); it was not assumed when defining q or deriving(1).

## Why a finite first Taylor degree exists

Set H=y-rho/a=y(1-q). The condition q<=1 gives Hy>=0. The independently proved local sign theorem, result76 claim1 (and its global-sign special case result70), excludes flat H for an exact profile. Its assumptions are exactly the primary assumptions stated here: smoothness, canonical growth, the source identity, and exact transport and Poisson. It does not require positivity of q or a strain bound.

For clarity, the mechanism of that theorem is as follows. If H were flat, V=U2+Dy would also be flat and would solve W.grad H-H=V, Delta V=a H_xx. For m>2, cutoff integration by parts with y r^(2-2m) and y r^(-2m) gives

    J_m=a/[2(m-2)]int Hy r^(-2m)(2m x^2/r^2-1),
    J_m=2m int Hy r^(-2m)B-(2ell+1)I_m-int HW2 r^(-2m),
    I_m=int Hy r^(-2m), J_m=int Vy r^(-2m), B=X.W/r^2.

The positive weighted mass concentrates at the innermost nonzero support of H, where B is positive. An exactly affine open core is included because H=0 implies V=0 and then W=(Ax,y) throughout that core. Exterior signed tails are bounded by C R^(4-2m)/(2m-4), whereas fixed inner positive mass is at least c0 r0^(-2m) with r0<R. The first identity bounds |J_m|/I_m uniformly for large m; the second makes it tend to positive infinity. The complete cutoff and concentration proof is in ../local_flat_sign_and_trajectories/PROOF.md. Thus H cannot be flat here.

Division by y in smooth odd functions preserves the flat/nonflat distinction: q-1=-int_0^1 H_y(x,ty)dt. Its first nonzero Taylor term is therefore an even homogeneous polynomial

    Q_(2k)=sum_(j=0)^k t_j x^(2j)y^(2k-2j), k>=1.        (4)

The first-order jet of q is zero by its two even parities, and q(0)=1. A nonzero H of degree2k+1 has precisely the nonzero term(4).

## Two coefficient signs

Apply q<=1 on the positive vertical axis and send its radius to zero. From(4), t0<=0. Angular differentiation preserves homogeneous degree. Therefore q_theta>=0, divided by r^(2k) and followed by r tending to zero along each fixed ray, gives

    (x partial_y-y partial_x)Q_(2k)>=0 in the first quadrant.

At fixed y>0 and x tending to zero,

    (x partial_y-y partial_x)Q_(2k)
                      =2(k t0-t1)x y^(2k-1)+O(x^3).

It follows that

    t1<=k t0<=0.                                       (5)

No claim about either coordinate derivative of the full q has been used.

## Independent leading-jet compatibility and contradiction

Write H_(2k+1)=-y Q_(2k). Since all lower nonlinear density terms vanish, the lower nonlinear stream terms vanish by transport and oddness in x. The leading equations for V_(2k+1) and H_(2k+1) are

    V_(2k+1)=(A x partial_x+y partial_y-1)H_(2k+1),
    Delta V_(2k+1)=a partial_xx H_(2k+1).

Define d_j=2jA+2(k-j)>0. Comparing x^(2j-2)y^(2k+1-2j),1<=j<=k, gives

    2j(a-d_j)t_j
      =[(2k-2j+3)(2k-2j+2)/(2j-1)]d_(j-1)t_(j-1).       (6)

For example k=1 gives (a-2A)t1=6t0, the independently derived primary cubic identity. Formula(6) also follows directly by differentiating each monomial of the displayed leading equations, so no old x^2 y normalization is involved.

By(3),

    a<=4D<4D+2k=2A+2k-2=d1,

and d_j increases strictly with j because A>1. In(6) at j=1, the coefficient a-d1 is strictly negative. By(5), its left side is nonnegative and its right side nonpositive. Equality forces t0=t1=0. For every j>=2, a-d_j remains strictly negative, so(6) inductively forces t_j=0. This contradicts the nonzero Taylor term(4), proving the theorem.

## Dependencies and limits

Dependencies are the canonical center strain formula, the independently proved flat-defect sign theorem, elementary integration by parts on a circle, and monomial comparison in the exact PDE. Their scopes and all new inequalities are stated above. A positive angular covariance argument alone would only give(3), not nonexistence. The exact transport recurrence is indispensable.

As a consistency example without exact transport, q=(1+beta y^2)exp(-r^2),0<beta<=1, satisfies both(S), q>0 and smooth decay. Its canonical strain is c/a=-1/4-beta/8. Taking a=8D/(2+beta) gives c=-D but does not give a profile: its cubic coefficients b=-a,e=a(beta-1) have transport defect

    (a-2A)b-6e=a(4D+8-6beta-a)>0.

Thus the theorem is not excluding all canonical smooth densities obeying the scalar sign restrictions; it uses both exact equations. Arbitrary profiles with q>1 somewhere or angular sign changes remain outside this exclusion. Neither extra condition in(S) has been proved automatic for the full primary class.
