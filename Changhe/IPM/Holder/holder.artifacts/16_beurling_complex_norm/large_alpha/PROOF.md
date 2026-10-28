# The complex Beurling norm at the Lipschitz endpoint

## Statement

For 0<alpha<1, let [f]_alpha=sup_(z!=w)|f(z)-f(w)|/|z-w|^alpha,
using the complex Euclidean modulus. Let S=T_xx+iT_xy have kernel
1/(2pi conjugate(z)^2), with circular principal values and convergent
increments modulo complex constants. Write M_alpha for its norm on
complex homogeneous Holder functions modulo constants. The same norm
is the supremum over complex compact smooth inputs, by the approximation
proof in ../PROOF.md. The conventional Beurling transform has kernel
-1/(pi z^2), and its complex-input norm is 2M_alpha.

Define the following positive explicit quantities:

    e_alpha=(1-alpha) alpha^(alpha/(1-alpha)),
    H_alpha=2^(1-alpha)+2^alpha e_alpha,
    t_alpha=sqrt(1-alpha)/3,
    q_alpha=(2 sin(t_alpha))^alpha/[2 sin(3t_alpha)],
    J_alpha=2^(-3alpha/2)/alpha+(3/2)^alpha/18+2log6.

Then

    (alpha+3)/[2(1-alpha)3^alpha H_alpha]
       <= M_alpha
       <= J_alpha+2q_alpha/(1-alpha)+16/[9(3-alpha)].       (1)

Consequently

    lim_(alpha->1-) (1-alpha) M_alpha=2/3,
    lim_(alpha->1-) (1-alpha) ||B||_complex=4/3.            (2)

Combined with the previously proved real-input coefficient,

    lim_(alpha->1-) ||B||_complex/||B||_real
       =8pi/(9sqrt3).                                    (3)

The inequalities in (1) are explicit bounds, not exact finite-alpha
norm formulas. The real-input coefficient used in (3) is
lim (1-alpha) C_alpha=3sqrt3/(4pi), and ||B||_real=2C_alpha.

## A Fourier-coefficient bound on each circle

For a complex function with [f]_alpha<=1 and a radius r>0, set

    c_3(r)=(1/(2pi)) integral_0^(2pi) exp(3i theta)
                                         f(r exp(i theta)) dtheta.

Shifting theta by 2t multiplies this Fourier coefficient by a complex
number whose distance from one is 2|sin(3t)|. The Holder condition
therefore gives, whenever sin(3t)!=0,

    2|sin(3t)| |c_3(r)| <=(2r|sin t|)^alpha.

Taking t=t_alpha is legitimate because 0<3t_alpha<1<pi. Thus
|c_3(r)|<=q_alpha r^alpha. No assumption about real-valued inputs is
made in this argument.

## The upper bound

Reduce the output increment by translation, rotation and dilation to
x=1/2 and y=-1/2. Normalize f(0)=0 and [f]_alpha<=1. The complete local
calculation in ../PROOF.md bounds the two radius-1/4 pole disks and
their complement inside the unit disk by J_alpha. Its circle
cancellation, cross-kernel reflection and middle-annulus arguments
use only the complex modulus, so they apply here unchanged.

On |z|=r>1 the increment kernel is

    nu_S(z)=conjugate(z/[pi(z^2-1/4)^2])
           =exp(3i theta)/(pi r^3) + E(z).

For a complex number w with |w|=u<=1/4,

    |(1-w)^(-2)-1|
      <=sum_(n>=1) (n+1)u^n
      =(2u-u^2)/(1-u)^2 <=32u/9.

Substitute w=1/(4z^2), or its conjugate. It follows that
|E(z)|<=8/(9pi r^5). The remainder paired with f is absolutely
integrable, and |f(z)|<=r^alpha gives

    integral_(r>1) |E(z)f(z)| dA(z)
      <=16/[9(3-alpha)].

The leading term is bounded using the circle estimate:

    |integral_(r>1) exp(3i theta)f(z)/(pi r^3) dA(z)|
       <=2q_alpha integral_1^infinity r^(alpha-2) dr
       =2q_alpha/(1-alpha).

Both integrals converge for alpha<1. Adding the local contribution
proves the upper inequality in (1).

As alpha tends to one, t_alpha tends to zero,
(2sin t_alpha)^(alpha-1) tends to one because
(alpha-1)log(2sin t_alpha) tends to zero, and
sin(t_alpha)/sin(3t_alpha) tends to 1/3. Hence q_alpha tends to 1/3.
The quantity J_alpha and the remainder bound stay bounded. Therefore
limsup (1-alpha)M_alpha<=2/3.

## A radial-power seminorm estimate

Let R_alpha(v)=|v|^(alpha-1)v for v in C, with R_alpha(0)=0. We prove

    [R_alpha]_alpha<=H_alpha,     H_alpha->1 as alpha->1-. (4)

Take z,w with R=max(|z|,|w|)>0 and d=|z-w|. If d<=R/2, the segment
between the points has radius at least R-d. The differential norm of
R_alpha at radius s is s^(alpha-1): its radial eigenvalue is
alpha s^(alpha-1), its tangential eigenvalue is s^(alpha-1). Integrating
along the segment gives

    |R_alpha(z)-R_alpha(w)|/d^alpha
       <=(d/(R-d))^(1-alpha)<=1.

If d>=R/2, use homogeneity to set R=1. At the point of radius one the
radial-power map is the identity. At the other point it differs from
the identity by at most

    max_(0<=s<=1)(s^alpha-s)
      =(1-alpha)alpha^(alpha/(1-alpha))=e_alpha.

The maximum follows by differentiation; the endpoints both give zero.
Now 1/2<=d<=2, so

    |R_alpha(z)-R_alpha(w)|/d^alpha
       <=d^(1-alpha)+e_alpha d^(-alpha)
       <=2^(1-alpha)+2^alpha e_alpha=H_alpha.

This includes points at zero and proves (4). Since e_alpha tends to
zero, H_alpha tends to one. The estimate is intentionally elementary;
its exact optimal value is not needed.

## The cubic homogeneous input

Define g(z)=|z| exp(-3i arg z) for z!=0 and g(0)=0. Its differential
in the orthonormal polar frame has singular values 1 and 3, so its
norm is 3 away from zero. Integrating along a segment proves that g is
3-Lipschitz; if the segment passes through zero, apply the same argument
to the two subsegments and use continuity at zero.

Set

    f_alpha(z)=|z|^alpha exp(-3i arg z)=R_alpha(g(z)),
    f_alpha(0)=0.

Composition with (4) yields [f_alpha]_alpha<=3^alpha H_alpha.
To compute its transform, put beta=alpha+2 and

    U(z)=-|z|^beta exp(-3i arg z)/(beta^2-9), U(0)=0.

The polar Laplacian gives -Delta U=f_alpha away from zero. Since
beta>2, the first two derivatives extend continuously through zero.
Integration by parts on an excised disk has boundary terms tending
to zero, so the same equation holds distributionally on the plane.
The elementary polar differentiation identity

    (partial_x+i partial_y)(r^b exp(i n theta))
       =(b-n)r^(b-1)exp(i(n+1)theta)

then gives

    (1/2)(partial_x+i partial_y)^2 U
       =(alpha+3)/[2(1-alpha)] |z|^alpha exp(-i arg z).     (5)

The coefficient is positive: the factor alpha+5 cancels from
(beta^2-9)=(alpha-1)(alpha+5).

The right side in (5) agrees with S f_alpha modulo a constant. Indeed
both are globally alpha-Holder and solve

    -Delta V=(1/2)(partial_x+i partial_y)^2 f_alpha

distributionally. For the singular integral this follows by compact
smooth approximation from its verified Fourier multiplier, as in the
homogeneous degree-three proof. Their difference is an entire harmonic
complex function with growth at most a constant times 1+|z|^alpha.
Apply the Poisson gradient estimate to its real and imaginary parts
on disks of radius R and let R tend to infinity. Both gradients vanish,
so the difference is constant.

The output increment of (5) between 1 and 0 has magnitude
(alpha+3)/[2(1-alpha)]. Dividing by the upper bound 3^alpha H_alpha for
the input seminorm proves the lower inequality in (1). Compact smooth
approximation preserves this fixed increment in the limit, so the
original test-function supremum has the same lower bound.

Finally, 3^alpha H_alpha tends to 3. Hence the lower inequality proves
liminf (1-alpha)M_alpha>=2/3, which completes (2). The real-input
asymptotic and the factor-two identities then give (3).

## Dependencies and scope

The dependencies are the established kernel, multiplier, increment
extension and compact-approximation results; the local complex bound
in ../PROOF.md; and the real scalar large-alpha coefficient for (3).
All new inequalities and the complex cubic calculation are proved
above. This does not assert boundedness at alpha=1 or any full
sup-plus-Holder norm estimate. It does not use numerical optimization
or attribute the endpoint constant to an unchecked source.
