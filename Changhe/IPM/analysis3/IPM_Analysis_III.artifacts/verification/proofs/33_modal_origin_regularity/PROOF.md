# The exact modal trial is C4, not C5, at the origin

## Exact statement

The normalized modal trial defined by the copied exact input
`trial_v2_h0.008.npz` and the scalar repair of proof 04 is C4 on a
neighborhood of the origin. In fact its fourth derivatives are locally
Lipschitz. It is not C5 there. On every punctured subregion inside a single
radial piece it is smooth. The local coupling estimate and smooth-cutoff
inverse of proof 25 need only C4 regularity, so they apply to this trial.
The fixed-flow nonlinear counterexamples of proof 27 are constructed inside
one such smooth punctured region and retain smooth compact inputs.

## Inner expansion and regularity

In the inner region t=log r<t_minus the exact definition is

    rho=x^2 y [1+sum_{m=0}^{259}sum_{j=1}^7
                   D_mj exp(2j(t-t_minus))cos(2m theta)
                +exp(bi(t-t_minus))
                    sum_{m=0}^{259}sum_{i=0}^6 E_mi(t-t_minus)^i
                                                   cos(2m theta)].

Here bi=3518437208883275/70368744177664>50, an exact dyadic close to50.
The repair changes the far coefficient A_00, not this inner density.
The functions r^d H(theta), with H smooth on the circle and d>4, have
Cartesian derivatives through order4 of the form r^(d-l)H_l(theta),
l<=4. They extend continuously to0 with those derivatives zero. This
follows inductively from partial_x=cos(theta)partial_r-
(sin(theta)/r)partial_theta and the corresponding partial_y formula,
and from difference quotients at0. For the lowest degree d=5, the fourth
derivatives are homogeneous of degree1 with smooth angular factors and
are Lipschitz: their first derivatives are bounded off0, and integrate
along line segments, splitting at0 when necessary. The higher degrees
and degree(3+bi) logarithmic terms have at least the same regularity. Finite
sums preserve it. Thus rho is C4,1 locally, with leading polynomial x^2 y.

## Failure of C5

The degree5 term is

    r^5 H5(theta),
    H5(theta)=exp(-2t_minus) cos^2(theta)sin(theta)
                          sum_{m=0}^{259}D_m1 cos(2m theta).

The exact identity cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4
shows that the sin(521theta) coefficient of H5 is
exp(-2t_minus)D_259,1/8. No lower m contributes to this frequency.
Independent extraction of the original dyadic coefficient gives

    D_259,1=6648046164061931/10384593717069655257060992658440192,

which is strictly positive. Higher inner powers are of degree at least7
and vanish after division by r^5 as r tends to0, uniformly in theta.

If rho were C5 at0, Taylor's theorem would give
rho=x^2 y+P5(X)+o(r^5), with P5 a homogeneous polynomial of degree5.
Indeed the lower Taylor terms are fixed by the already-established C4
expansion. Restricting to rays and dividing by r^5 gives
H5(theta)=P5(cos(theta),sin(theta)). A degree5 polynomial restricted to
the circle has angular frequencies at most5. Its sin(521theta)
coefficient is zero, contradicting the exact nonzero coefficient above.
Thus C5 regularity is impossible, however small that coefficient is.

## Why C4 suffices in the local coupling proof

Let rho be any C4 function near0, even in x and odd in y, with rho(0,y)=0,
and leading term x^2 y. Even x parity gives rho_x(0,y)=0. Twice applying
the fundamental theorem in x, and once differentiating in y, gives

    rho_x=x a1, a1(x,y)=integral_0^1 rho_xx(sx,y)ds,
    rho_y=x^2 a2, a2(x,y)=integral_0^1(1-s)rho_xxy(sx,y)ds.

These identities and their first derivatives use at most four derivatives
of rho. Since rho_xx(0,0)=0 by odd y parity, on B_delta they imply

    ||a1||_infinity<=C delta, ||Da1||_infinity<=C,
    ||a2||_infinity+||Da2||_infinity<=C.

These are exactly the coefficient bounds used in proof 25. All its product,
cutoff and Holder estimates follow unchanged. A C5 assumption was stronger
than necessary and was not satisfied by the actual modal input. The revised
proof states C4 and omits a generic sharper Taylor remainder that was not
used in any inequality. This correction does not upgrade the localized
frozen-transport inverse into an inverse for the actual variable transport.

Finally the modal formula is smooth wherever r>0 and no radial joining
circle is crossed. At a sufficiently small regular point in the first
quadrant, choose every flow box and cutoff strictly inside the inner radial
region. The local vector field is then smooth there, since its explicit
Green expansion is a finite sum of smooth powers and logarithms. The flow
coordinates in proof 27 are therefore smooth. The much weaker statement
that V is C2 on arbitrary compact sets would not alone justify smooth
inputs obtained from those coordinates; the box choice supplies the needed
hypothesis.

Dependencies: exact original input, its defining inner formula, and the
independent scalar repair of proof 04. No numerical smallness or interval
integration is used in the non-C5 argument.
