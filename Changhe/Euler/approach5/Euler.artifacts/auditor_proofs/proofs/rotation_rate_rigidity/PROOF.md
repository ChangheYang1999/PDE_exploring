# Uniqueness of rotation rate and the decaying linear kernel

## Rotation-rate theorem (C08)

Let 0<c<1/2, U in C^2(R^3), div U=0 and U(y)->0 uniformly at infinity.
Suppose that for two distinct real rates omega_1, omega_2 there are C^1
pressures P_1,P_2 solving the respective complete profile equations with the
same U and c. Then U=0.

Subtract the equations and put
q=(P_1-P_2)/(omega_1-omega_2). With L U=(Jy.grad)U-JU,

    grad q=LU, div LU=(Jy.grad)div U=0.

Thus q is harmonic and grad q is harmonic. Smoothness follows either from
the displayed gradient or from distributional elliptic regularity. At any
fixed y0, the mean-value formula gives

    grad q(y0)=1/|B_R| int_(B_R(y0)) LU.

Integration of the angular derivative, using div Jy=0 and
Jy.n=Jy0.n on the boundary sphere, bounds this by

    (3|y0|/R) sup_(partial B_R(y0))|U| + avg_(B_R(y0)) |U|.

The first term tends to zero because U is bounded; the second tends to zero
by its uniform decay, splitting off any fixed compact ball. Hence LU=0.
Differentiating R_alpha U(R_-alpha y) in alpha and using LU=0 shows rotation
equivariance of U. The original equation then reduces to the ordinary,
nonrotating profile equation. The independently audited C^1 sublinear
nonrotating theorem in the team records gives U constant. Its
decay gives U=0. This is the sole non-elementary dependency of this theorem.
It uses no global bound on DU and no assumed pressure normalization.

## Trivial linear kernel (C09)

Let c>0, omega real, V in C^2(R^3), div V=0, V->0, and p in C^1 solve

    (1-c)V+(cy-omega Jy).grad V+omega JV+grad p=0.

For W=curl V and B0=cy-omega Jy, taking curl gives

    W+(B0.grad)W+omega JW=0.

Along y(s)=exp(cs)R_-omega_s y0,

    W(y(s))=exp(-s)R_-omega_s W(y0).

As s tends to minus infinity the trajectory approaches zero, where W is
bounded. Therefore W(y0)=0. All components of V are now entire harmonic
functions, bounded and tending to zero, hence vanish. This proof does not
need a global vorticity bound.

The conclusion is a trivial kernel on this exact class. It does not supply
a normed inverse, Fredholm property, spectral gap, or nonlinear neighborhood
of uniqueness. An unrestricted assertion of 'no bifurcation' does not follow
from the kernel computation alone.

Audit recorded: 2026-11-02T18:42:51Z
