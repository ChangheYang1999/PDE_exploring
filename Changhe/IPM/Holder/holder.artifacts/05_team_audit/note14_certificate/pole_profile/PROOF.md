# An explicit positive contribution from the omitted pole disks

## Statement and conventions

Let 0<a<1. Use the real homogeneous Holder seminorm

    [f]_a = sup_{z != w} |f(z)-f(w)| / |z-w|^a,

and the increment-defined operators of ../../../01_setup/PROOF.md. In particular,

    K(u)=(u_1^2-u_2^2)/(2 pi |u|^4),    R_1^2=T_xx-I/2.

Let f be exactly the polygon-plus-projection witness of ../PROOF.md, with
poles 0 and e=(1,0). Write k=2^(a-1). In the half-plane z_1>1/2,

    g(z)=k sigma(z) dist(z,Z0(b))^a,
    P(u)=(|u|^a+sign(u_1^2-u_2^2)
                    (|u_1^2-u_2^2|/|u|)^a)/2,
    Q(z)=-1/2+lambda P(z-e),
    h(z)=(2z_1-1)^a/2,
    f(z)=max(-h(z),min(h(z),g(z)+c,Q(z))).

Here b>0, the closed polygon Z0(b) contains e, P(0)=0, and f is extended
oddly across z_1=1/2. Assume lambda>=0 and lambda[P]_a<=1. The parent
witness theorem then gives [f]_a<=1, provided the pole value is -1/2;
the conditions below in particular imply that value.

Fix 0<epsilon<1/2 such that

    (lambda+k) epsilon^a <= c+1/2,
    lambda epsilon^a <= 1/2.                              (1)

Set

    A(a)=Gamma(1+a/2)/(2sqrt(pi) Gamma(3/2+a/2)),
    M=lambda A(a) epsilon^a/a+epsilon^2/4,
    E=a epsilon/[pi(1-2epsilon)^(1-a)]
                   +epsilon^(a+2)/[(a+2)(1-epsilon)^2].   (2)

The absolutely convergent local integral

    J_e=integral_(|u|<epsilon)
             [K(u)(f(e+u)+1/2)-K(e+u)f(e+u)] du

satisfies

    |J_e-M| <= E.                                        (3)

The two omitted pole disks contribute exactly 2J_e to the principal-value
increment integral I0 of the parent proof. Thus their contribution lies
in [2M-2E,2M+2E]. This replaces a symmetric error bound centered at zero;
it leaves the separate diagonal identity contribution unchanged.

The result concerns only homogeneous seminorms and the stated circular
principal values. It asserts no production number before the separate
parameter and outward-arithmetic checks.

## The active profile and the lower clamp

Since e belongs to Z0(b), dist(e+u,Z0(b))<=|u|. Consequently

    g(e+u)+c >= c-k|u|^a,
    -1/2 <= Q(e+u) <= -1/2+lambda |u|^a.

The first condition in (1) therefore implies Q<=g+c throughout the
closed epsilon disk. The second gives Q<=0, whereas h>0 on this disk.
The only possible active clamp is the lower one:

    f(e+u)=Q(e+u)+d(u),
    d(u)=(-h(e+u)-Q(e+u))_+ >=0.                         (4)

At u=0 this equals -1/2. Since Q>=-1/2, the correction satisfies

    d(u) <= (1/2-h(e+u))_+.

It vanishes when u_1>=0. For -epsilon<=u_1<0, the derivative of
(1+2u_1)^a/2 is a(1+2u_1)^(a-1). The mean value theorem gives

    0<=d(u)<=a(-u_1)/(1-2epsilon)^(1-a).                 (5)

All these statements are pointwise, including the zero sets of P and g.
No differentiability of the signed power or polygon distance is used.

## The own-pole contribution

The radial part of P has zero integral against K on each circle. The
remaining angular integral is

    (1/(4pi)) integral_0^(2pi) |cos(2theta)|^(a+1) dtheta
       = Gamma(1+a/2)/(2sqrt(pi) Gamma(3/2+a/2))=A(a).

For example, reducing to a quadrant and substituting t=sin(theta)^2
in the cosine-power integral gives the beta integral and the displayed
Gamma expression. Radial integration therefore gives exactly

    integral_(|u|<epsilon) K(u) lambda P(u) du
       =lambda A(a) epsilon^a/a.                        (6)

The integral converges absolutely because a>0. To bound the correction,
use (5), |K(u)|<=1/(2pi|u|^2), and the polar-coordinate identity

    integral_(cos(theta)<0) (-cos(theta)) dtheta=2.

It follows that

    |integral_(|u|<epsilon) K(u)d(u) du|
        <=a epsilon/[pi(1-2epsilon)^(1-a)].             (7)

This also proves absolute convergence of that correction. The estimate
does not assume a favorable sign for K on the clamped region.

## The smooth other-pole contribution

The function z->K(z) is harmonic away from zero, since it is the real
part of 1/(2pi z^2). Its mean on the disk B(e,epsilon) is K(e)=1/(2pi).
Hence the constant pole value contributes exactly

    -integral_(|u|<epsilon) K(e+u)(-1/2) du
        =epsilon^2/4.                                   (8)

The admissibility bound [f]_a<=1 and f(e)=-1/2 give
|f(e+u)+1/2|<=|u|^a. Since |e+u|>=1-epsilon, the remaining part obeys

    |integral_(|u|<epsilon) K(e+u)(f(e+u)+1/2) du|
        <=epsilon^(a+2)/[(a+2)(1-epsilon)^2].            (9)

Equations (4), (6)-(9) prove (3).

## Reflection and the principal value

Reflection z->(1-z_1,z_2) interchanges the poles, reverses the sign of
K(z-e)-K(z), and reverses the sign of f. Thus the two disk contributions
agree. Within each disk the constant at its own pole has been removed;
its integral on every centered annulus is zero. This is exactly the
circular principal-value prescription and the near-disk decomposition
used by the numerical certificate. There is no remaining singular term
or change to the identity contribution of R_1^2.

## Dependencies and verification

The parent witness and setup proofs supply global admissibility, the
polygon containing its pole, reflection symmetry and the operator
normalization. Every additional estimate is proved above. Numerical use
must verify both inequalities (1), the profile certificate for lambda,
and the exact epsilon in the completed integral records. The analytic
argument is awaiting the lead's independent cross-read.
