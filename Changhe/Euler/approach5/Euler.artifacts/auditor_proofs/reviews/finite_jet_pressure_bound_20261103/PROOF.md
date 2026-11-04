# Pressure at a finite-order incompressible zero

## 1. Statement

Let m>=1 be an integer, v in C^m on a ball in R3 about zero, and P continuous. Assume div v=0 and div div(v tensor v+P I)=0 distributionally. Suppose v has first nonzero Taylor term V_m, a homogeneous polynomial of degree m. Define sphere averages

    E=|v|^2, F=P(0)-P,
    K=<|V_m(theta)|^2>, K>0, N=<(V_m(theta).theta)^2>.

Then

    lim_(r->0) <F(r theta)>/<E(r theta)>
      =[(2m+3)N-K]/(2mK),
    -1/(2m) <= [(2m+3)N-K]/(2mK) <= 1/2.             (1)

Consequently F>=beta E on a neighborhood is impossible for beta>1/2. If F>=E/2, the leading polynomial V_m is the gradient of a nonzero homogeneous harmonic polynomial of degree m+1. The upper constant is attained by stationary Euler fields for every m. No pressure derivative, global growth condition or rotation parameter enters this local theorem.

## 2. The pressure mean without pressure derivatives

Set a=(v.grad)v and M(r)=<F(r theta)>, A(r)=<a(r theta).theta>. Since div v=0, Delta F=div a. A radial distributional test gives

    integral [r^2 M psi''+2r M psi'+r^2 A psi']dr=0.

Equivalently -r^2 M'+r^2 A is constant in distributions away from zero. A is continuous and bounded there, and a nonzero constant would produce a nonzero 1/r term in M, impossible since P is continuous at zero. Thus M'=A and M(r)=integral_0^r A(t)dt. This proves the identity at the stated regularity, with no pressure normalization other than subtraction of P(0).

The C^m Taylor expansion and its differentiated C^(m-1) version give uniformly on the sphere

    v(r theta)=r^m V_m(theta)+o(r^m),
    Dv(r theta)=r^(m-1)DV_m(theta)+o(r^(m-1)).

For m=1 the second assertion is continuity of Dv. Divergence freedom gives div V_m=0. If A_m=<((V_m.grad)V_m).theta>, then A(r)=r^(2m-1)A_m+o(r^(2m-1)), so M(r)=r^(2m)A_m/(2m)+o(r^(2m)). The denominator in (1) is r^(2m)K+o(r^(2m)).

## 3. The exact angular coefficient

Write f=V_m.theta and w=V_m-f theta on the unit sphere. Homogeneity and incompressibility give div_S w=-(m+2)f. The radial acceleration is

    ((V_m.grad)V_m).theta=m f^2+w.grad_S f-|w|^2.

Integrating by parts gives <w.grad_S f>=(m+2)N. Since <|w|^2>=K-N, it follows that A_m=(2m+3)N-K. This proves the exact formula and the lower bound in (1).

## 4. Polynomial degree and the sharp upper bound

The scalar f is the sphere trace of x.V_m(x), a homogeneous polynomial of degree m+1. It decomposes into orthogonal spherical harmonics f_l with l<=m+1. For completeness the polynomial decomposition follows inductively from

    Delta(|x|^(2j)H_l)=2j(2l+2j+1)|x|^(2j-2)H_l

for a harmonic homogeneous polynomial H_l. Decompose the Laplacian by degree induction, invert each nonzero coefficient j>=1 and subtract; the remainder is harmonic. Restrictions have eigenvalue l(l+1), and integration by parts gives their orthogonality. No infinite-dimensional spectral assertion is needed here. The constant component of f is zero by the divergence theorem in the ball.

Let g=(m+2) sum_(l>=1) f_l/[l(l+1)]. Then Delta_S g=-(m+2)f. The tangential field h=w-grad_S g is divergence free and L2 orthogonal to grad_S g. Therefore

    <|w|^2> >= <|grad_S g|^2>
       =(m+2)^2 sum_(l>=1) <|f_l|^2>/[l(l+1)]
       >= (m+2)N/(m+1).

Adding N gives K>=(2m+3)N/(m+1), hence (2m+3)N-K<=mK. This proves the upper bound 1/2.

Equality with K>0 requires h=0 and f pure degree m+1. Conversely those conditions give equality. Then g=f/(m+1), and

    V_m(theta)=f theta+grad_S f/(m+1)
              =grad[|x|^(m+1)f(x/|x|)]/(m+1) at |x|=1.

The polynomial in brackets is harmonic, and homogeneity extends this identity to V_m everywhere. The pointwise condition F>=E/2 forces equality in the mean limit, giving the stated necessary leading-jet form. It does not assert that the entire germ is irrotational.

## 5. Exact equality models and the tail ratio

Choose any nonzero harmonic homogeneous Q of degree m+1 and set v=grad Q, P=-|grad Q|^2/2. Then div v=0, curl v=0 and (v.grad)v=grad(|v|^2/2), so stationary momentum holds exactly. Both pressure-stress equations follow. Since v(0)=0, F=E/2 and equality is attained. For example Q=Re(x1+i x2)^(m+1)/(m+1). These polynomial fields grow at infinity and are not decaying profiles.

For the ratio consequence assume P(0)=0, H=E/2-P>=0 and v=0 where H=0. On {H>0} put R=E/H. If limsup_(x->0,H>0) R<1, choose Rstar<1 above that upper limit on a smaller neighborhood. Then -P>=(1/Rstar-1/2)E with coefficient greater than 1/2. On {H=0}, E=P=0, so the inequality holds there too. Section 1 contradicts a finite-order velocity zero. Hence limsup R>=1 at every such zero. The harmonic-gradient models attain R=1 off their velocity zero sets.

## 6. Verdict and scope

All six submitted sections and all six independent sections were read. The exact mean formula, sharp upper bound, equality characterization and conditional ratio statement are CONFIRMED. For smooth nonzero germs the condition F>=beta E, beta>1/2, forces any zero to be infinitely flat. It does not exclude such an infinitely flat zero. In particular this is not a replacement of the previously audited 2/3 common-flat ratio obstruction by 1. The all-omega unrestricted Euler question remains OPEN. No computation or formal build was used.
