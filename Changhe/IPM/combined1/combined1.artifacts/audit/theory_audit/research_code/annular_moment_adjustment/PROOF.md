# A prescribed dipole moment with arbitrarily small correction norm

## Statement, notation and scope

All fields are real on the plane. S1 means even in x and odd in y. The
canonical velocity is

    U[h]=(partial_xy v,-partial_xx v), Delta v=h,

with the logarithmic Newton potential for a compactly supported density.
This agrees with Fourier symbol(xi1 xi2,-xi1^2)/|xi|^2. Constants and affine
terms in v do not change U. Let eta be any nonnegative nonzero smooth
function supported in(1,2), scaled so that

    pi integral_1^2 r^2 eta(r) dr=1,
    f(r,theta)=eta(r) sin(theta), u_f=U[f].

For a prescribed real number m and R>=1 define

    h_R(X)=m R^(-3) f(X/R).

Then h_R is smooth, compactly supported in R<|X|<2R and S1, with

    integral y h_R=m, integral x h_R=0,
    U[h_R](X)=0 for |X|<R,
    U[h_R](r,theta)=m/(pi r^3)(cos3theta,sin3theta) for r>2R.       (1)

Thus every interior density and velocity jet, including the origin
normalization, is preserved by adding h_R to a reference. Its L2 norm is
exactly |m| R^(-2)||f||2.

Use the already audited high norm

    X(h)^2=||omega D2 J^s h||2^2+w1||D J^s h||2^2+w2||J^s h||2^2,
    omega=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2),
    s=1/5184, w1=2^15, w2=2^20.

Derivative tensors contain all ordered Cartesian components. Define
A_(k,b)=||r^b D^k f||2 and the finite constants

    H=[5^(4/5) A_(2,4/5)^2+w1 A_(1,0)^2+w2 A_(0,0)^2]^(1/2),
    Q=5^(2/5) A_(3,4/5), Cw=32770.28,
    CX=H^(1-s)(2Q^2+Cw H^2)^(s/2)+(48/25)s H.

Then

    X(h_R)<=CX |m| R^(-2).                                      (2)

For each fixed q<-3 and nonzero m the weighted C1 quantity

    Hq(h)=max(sup(1+r)^(-q)|h|,sup(1+r)^(1-q)|grad h|)

instead grows like |m| R^(-q-3). In particular the moment functional is
not continuous for either the L2 norm or X, even on compact smooth S1
functions whose velocity vanishes on an arbitrarily large interior disk.
There is no finite constant C with Hq(h)<=C X(h) on this class.

Let a reference rho have canonical velocity u, and suppose for r>=1

    |u(X)|<=V r^gamma, |grad rho(X)|<=G r^(gamma-1), gamma<1,

where V,G are finite nonnegative constants. For fixed real c, write
F(rho;c)=(cX+u).grad rho-rho. Define the finite constants

    Ac=||cX.grad f-f||2,
    Av=||r^gamma grad f||2,
    Ag=||r^(gamma-1) u_f||2,
    An=||u_f.grad f||2.

No singularity occurs in Ag at zero because u_f vanishes on r<1. Then

    ||F(rho+h_R;c)-F(rho;c)||2
      <=|m| Ac R^(-2)+|m|(V Av+G Ag)R^(gamma-3)+m^2 An R^(-6).   (3)

If in addition, uniformly in angle,

    grad rho=r^(gamma-1)[gamma Theta(theta)e_r+Theta'(theta)e_theta]
                 +O(r^(gamma-1-epsilon)), epsilon>0,

then outside2R the residual change has expansion

    F(rho+h_R;c)-F(rho;c)
      =(m/pi) r^(gamma-4) P(theta)+O(r^(gamma-4-epsilon)),
    P=gamma cos(2theta)Theta+sin(2theta)Theta'.                   (4)

Here Theta is continuously differentiable and the differentiated
remainder bound is an explicit hypothesis. Thus an endpoint residual
coefficient A can be shifted by any multiple(m/pi)P at arbitrarily small
X cost, without changing any interior density or velocity value. Its
orthogonal projection onto the complement of span P is unchanged. If
P is nonzero, the least circle-L2 norm in this family is attained at
m=-pi<A,P>/||P||2^2. This is a reference-design statement. It does not
construct a stationary solution, an inverse, or a successful closure.

## Proof of the exact potential and screening

The angular mode of v=Delta^-1 f is1. A direct solution of the radial
Poisson equation gives

    v(r,theta)=-1/2 [r^(-1) integral_0^r s^2 eta(s) ds
                         +r integral_r^infinity eta(s) ds] sin(theta). (5)

Differentiate to check v_rr+r^(-1)v_r-r^(-2)v=eta(r)sin(theta).
The solution is regular at zero and decays at infinity; it is therefore
the canonical Newton potential. Equivalently, its asymptotic logarithmic
term vanishes because the angular integral of f is zero, and separation
of the logarithmic kernel gives(5).

For r<1 formula(5) is a constant times r sin(theta)=y. All its second
derivatives vanish, proving u_f=0 there. For r>2 it is

    v=-y/(2pi r^2).

Direct differentiation gives

    partial_xy(y/r^2)=-2 cos(3theta)/r^3,
    partial_xx(y/r^2)= 2 sin(3theta)/r^3,

hence the last formula in(1) at unit scale. The velocity operator has
homogeneity zero on densities: U[m R^-3 f(./R)]=m R^-3 u_f(./R).
This proves all of(1), including the absence of an R factor in the
exterior coefficient. Changing variables in the two first moments
proves their exact values. The same change of variables proves
||h_R||2=|m|R^-2||f||2.

As a separate normalization check, the audited contact formula is

    c[h]=-h_y(0)/4+(1/pi) PV integral sin(3theta)h/r^3 dX.

Here both terms vanish: h_R is zero near zero and its only density
angular mode is1. This agrees with the stronger velocity-screening
statement and does not omit the local term.

## High norm and the weighted tail budget

For every k>=0 and real b, compact support away from zero gives the
exact homogeneous-weight scaling

    ||r^b D^k h_R||2=|m|R^(-2-k+b) A_(k,b).                    (6)

On the support r>=R>=1, omega<=5^(2/5)r^(4/5). Since R>=1, (6) yields
E_w(h_R)<=H|m|R^-2 and ||omega D3 h_R||2<=Q|m|R^-2, where E_w is X
with J^s omitted. The sharper power in the latter inequality is R^-21/5.
The raw-to-fractional norm comparison proved in
../sharp_l2_audit/PROOF.md, section4, is

    X(h)<=E_w(h)^(1-s)(2||omega D3 h||2^2+Cw E_w(h)^2)^(s/2)
                                      +(48/25)s E_w(h).

It applies to every compact smooth S1 h. Its right side increases with
both nonnegative inputs. Substitution proves(2). In particular no
unsupported assertion that fractional derivatives preserve support is
being used.

For z on the support of f and R>=1, R|z|<=1+R|z|<=R(1+|z|).
Because -q and1-q are positive, substitution in Hq gives lower and
upper bounds by |m|R^(-q-3) times fixed finite suprema of f and grad f.
The lower constant is positive because f is nonzero. Since -q-3>0,
the claimed growth follows. Taking fixed m=1 and R tending to infinity
proves discontinuity of the moment functional and rules out an X-to-Hq
bound. Each h_R individually has finite Hq; the obstruction is uniformity.

## Residual perturbation and endpoint coefficient

Linearity of U and the product rule give exactly

    F(rho+h_R;c)-F(rho;c)
      =(cX.grad-1)h_R+u.grad h_R+U[h_R].grad rho
                                      +U[h_R].grad h_R.       (7)

The first, second and fourth terms are supported in R<r<2R. The third
vanishes for r<R by(1). Scaling gives the first and fourth norms in(3)
exactly. The two background growth hypotheses give the middle two
bounds in(3) after changing variables X=Rz. Ag is finite at infinity
because u_f=O(r^-3), so its squared integrand with polar measure is
O(r^(2gamma-7)), integrable for gamma<3. Our stronger gamma<1 also
makes every power in(3) negative. Thus the full residual change tends
to zero in L2. Its value is identically zero on r<R.

For r>2R only the third term in(7) survives. The exterior velocity has
polar components m/(pi r^3)(cos2theta,sin2theta). Taking its scalar
product with the differentiated leading density gives(4), including
the controlled smaller error. The final minimization is the elementary
orthogonal projection in the real Hilbert space L2 of the circle.

## Dependencies and verification status

The only imported analytic inequality is the audited raw-to-fractional
comparison in sharp_l2_audit. The screening, moment, scaling, residual
and projection arguments are proved above. A short independent symbolic
check verifies the Cartesian derivatives and the radial Green formula;
it cannot replace the proof. No candidate is modified here, and no
numerical constant depending on a particular bump is asserted.

This new construction is OPEN independent Opus review. Its exact algebra
will be recorded separately. All data and verification evidence remain
in this topic; there is no formalization or Lean build.
