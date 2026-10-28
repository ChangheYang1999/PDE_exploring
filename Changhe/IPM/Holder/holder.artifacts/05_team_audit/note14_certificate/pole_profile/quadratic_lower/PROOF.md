# A one-sided quadratic pole bound without a sign restriction

## Exact statement

Use the real homogeneous Holder seminorm [f]_a, circular principal-value
kernel K(u)=(u_1^2-u_2^2)/(2 pi |u|^4), and exact polygon-plus-projection
witness f of ../PROOF.md. Assume 0<a<1, b>0, lambda>0 and
lambda[P]_a<=1. Let 0<epsilon<1/2 satisfy only

    (lambda+2^(a-1)) epsilon^a <= c+1/2,
    lambda epsilon^a <= 1/2.                              (1)

Define

    C_e=(1-2epsilon)^(a-1),
    A=Gamma(1+a/2)/(2 sqrt(pi) Gamma(3/2+a/2)),
    M=lambda A epsilon^a/a+epsilon^2/4,
    E_c=a C_e^3 epsilon^(3-2a)/(6 pi lambda^2(3-2a)),
    E_s=epsilon^(a+2)/((a+2)(1-epsilon)^2),
    E_b=a C_e epsilon/pi.                                (2)

For the complete right-pole contribution

    J_e=integral_(|u|<epsilon)
          [K(u)(f(e+u)+1/2)-K(e+u)f(e+u)] du,

one has

    M-E_c-E_s <= J_e <= M+E_b+E_s.                       (3)

The left-pole contribution is equal to J_e. Thus twice this interval
may replace the omitted pole disks in a complete increment certificate.
No condition that E_c comes from a globally nonpositive clamp correction
is required. The assertion concerns homogeneous seminorms only, and
contains no numerical operator bound before the remaining region is
certified and the conditions are checked.

## Proof

The parent proof gives the exact pointwise identity on the disk

    f(e+u)+1/2=lambda P(u)+d(u),
    d(u)=(1/2-(1+2u_1)^a/2-lambda P(u))_+ >=0.

It also gives d=0 when u_1>=0 and

    d(u)<=a C_e(-u_1) when u_1<0.                       (4)

Decompose the clamp integral as a sum over K>=0 and K<0. The first
piece is nonnegative, without any further assumption. On K<0 and
u_1<0 write r=|u| and t=-u_1/r. Then 0<t<1/sqrt(2) and

    P(u)=r^a[1-(1-2t^2)^a]/2 >= a r^a t^2,

by the concavity tangent inequality s^a<=1+a(s-1). Hence

    d(u)<=a(C_e r t-lambda r^a t^2)_+.

There are two angular arcs with this value of t. Their combined measure
is 2dt/sqrt(1-t^2). Since

    0 <= (1-2t^2)/sqrt(1-t^2) <= 1,

polar integration gives

    -integral_(K<0, |u|<epsilon) K(u)d(u) du
    <= (a/pi) integral_0^epsilon dr/r
         integral_0^(1/sqrt(2)) (C_e r t-lambda r^a t^2)_+ dt
    <= (a/pi) integral_0^epsilon dr/r
         integral_0^(C_e r^(1-a)/lambda)
                       (C_e r t-lambda r^a t^2) dt
    = a C_e^3 epsilon^(3-2a)/(6 pi lambda^2(3-2a)).

The extension is valid even when its endpoint exceeds 1/sqrt(2): the
quadratic is nonnegative up to its positive zero, and the original
integrand is its positive part. Combining with the nonnegative piece
proves integral Kd >= -E_c. The independent absolute estimate (4)
gives |integral Kd|<=E_b exactly as in the parent proof. Both integrals
converge absolutely, since 3-2a>1 and the crude bound is integrable.

The pure projection term integrates to lambda A epsilon^a/a. The smooth
other-pole constant contributes epsilon^2/4 by harmonicity of K on
B(e,epsilon). The remaining smooth term has absolute value at most E_s,
using [f]_a<=1 and |e+u|>=1-epsilon. These facts prove (3).

The reflection u about the pole midline maps the two full contributions
to each other. The only discarded constants have zero integral on each
centered annulus, so the formula agrees with circular principal values.
The diagonal identity term of R_1^2=T_xx-I/2 is unchanged.

## Dependencies and verification scope

The parent proof supplies admissibility and the active projection
identity from (1). Every additional inequality is proved above. All
conditions, radii and exact finite-region coverage must be checked in
a numerical application. The bound is awaiting independent cross-read.
