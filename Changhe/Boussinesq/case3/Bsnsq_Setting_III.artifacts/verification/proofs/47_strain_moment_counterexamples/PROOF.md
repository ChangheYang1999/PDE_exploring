# A strain moment does not replace the transport equations

Date:2026-10-20. Status: CONFIRMED by independent derivation, own numerical checks,
and checked actual Opus5.5 followup. These are not B2 solutions. The target equations are
W.grad Theta=(beta-2)Theta and W.grad Omega+Omega=Theta_x, with
Omega=-curl U=-Delta Psi. This is the convention expressly imposed
by PROMPT.md, irrespective of other conventions in the literature.

## Statement and notation

Fix beta>=2, nu=1/beta, c=1+beta/2 and B=1/(2beta)>0. Let q=x^2+y^2,
H3=x(x^2-3y^2), and choose real A and nonzero delta. Define

    Theta=x^2(1+q)^(-(1+2nu)/2),
    Psi=B x(e^{-q}-1)+C xy e^{-q}+A H3 e^{-q}
          +delta xy[(1+q)^{-nu/2}-e^{-q}],    C=c,
    U=(-Psi_y,Psi_x), Omega=-Delta Psi, W=beta X+U-U(0).

All fields are smooth on the plane; Theta and U2 are even in x, while
Psi, Omega and U1 are odd. They have U(0)=0, Psi_xy(0)=c,
Theta=x^2+O(r^4), and Omega_x(0)=8B=4/beta. The velocity is sublinear,
and the nonzero leading source tail is

    Omega=r^{-nu}[delta nu(4-nu) sin(2theta)/2+o(1)],

where theta is the ordinary polar angle from the positive x-axis.
The velocity is the canonical full-plane relative inverse of Omega.
The temperature has the angular asymptotic r^{1-2nu} cos^2(theta).

Let K=xy/r^4 and

    Lambda=(1/pi) int K Theta_x dX,
    NL=(1/pi) int Omega U.grad K dX.

These integrals are absolutely convergent. For this family,

    Lambda=0,  NL=-3B^2/2-9AB/2.                    (1)

Thus NL is unbounded above and below at fixed beta, the listed center data, and
fixed nonzero leading vorticity tail. In particular take

    A=-B/3-2c/(9B).                                (2)

Then Lambda+NL=c exactly. Nevertheless the temperature equation fails:
for Theta=x^2 F, its divided residual has the expansion on the axis

    R_F(0,y)=-8c y/(3B)+O(y^2).                    (3)

Consequently kinematics, normalizations, the target leading tails and
the scalar strain identity do not imply even the first transport PDE.
This does not refute an estimate restricted to actual B2 solutions.

## 1. Smoothness, center and canonical inverse

The radial functions are smooth functions of q>=0. All displayed
polynomials have the asserted x parity. The subtracted Bx removes the
only nonzero stream gradient at0. Hence U(0)=0 in this representative
and W=beta X+U; this does not impose a physical B1 condition on B2. The added delta term begins at
order4, so it changes neither Psi_xy(0) nor Omega_x(0). Since H3 is a
homogeneous harmonic polynomial of degree3, its vorticity starts at
order3; direct differentiation of Bx e^{-q} gives
4Bx(2-q)e^{-q}. The Cxy term gives 4Cxy(3-q)e^{-q}. These prove all
center statements.

The leading stream at infinity is delta xy r^{-nu}, homogeneous of
degree2-nu, plus the harmonic linear term -Bx. For
P=r^{2-nu} sin(2theta),

    -Delta P=[4-(2-nu)^2] r^{-nu} sin(2theta).

The factor xy=r^2 sin(2theta)/2 gives the claimed tail. Its velocity is
O(r^{1-nu}), and all Gaussian contributions are bounded. Thus U=o(r).
The once-subtracted Biot-Savart integral converges for this decaying
source, which satisfies |Omega(Y)|<=C(1+|Y|)^(-nu) globally:
its far integrand is bounded by C_X r^{-2-nu}, with plane
measure. To check sublinearity of that integral, split at source radii
r/2 and2r for target radius r. The inner kernel term at the target is
bounded by r^{-1} times an O(r^{2-nu}) mass, while the center kernel
term integrates O(r^{1-nu}); in the middle annulus use local
integrability of 1/|X-Y| and |Omega(Y)|<=C r^{-nu}. In the exterior
the kernel difference is bounded by C r/|Y|^2, giving
C r int_{2r}^infty rho^{-1-nu}d rho=O(r^{1-nu}). Thus the inverse
is O(r^{1-nu}) and smooth, with the same div-curl
and center value. The difference from U is an entire sublinear harmonic
vector field, hence constant by the harmonic gradient estimate on
arbitrarily large balls; its center value is zero. This proves the
canonical inverse assertion without adding any free affine strain.

Near0, Omega=O(r), U=O(r), Theta_x=O(r). Since K=O(r^{-2}) and
|grad K|=O(r^{-3}), all moment integrands are O(r^{-1}) and locally
integrable with plane measure. At infinity, Lambda and NL have radial
absolute majorants O(r^{-1-2nu})dr, plus more rapidly decaying Gaussian
terms. This also justifies the angular integrations below.

## 2. Exact evaluation of the nonlinear moment

Use ordinary polar coordinates. Then

    K=sin(2theta)/(2r^2),
    U.grad K=Psi_theta sin(2theta)/r^4
               +Psi_r cos(2theta)/r^3.             (4)

The mode1 and mode3 radial stream coefficients are

    R1=B r(e^{-r^2}-1), R3=A r^3 e^{-r^2}.

The corresponding vorticity coefficients are

    O1=4B r(2-r^2)e^{-r^2},
    O3=4A r^3(4-r^2)e^{-r^2}.

For R1 cos(theta), expression(4) has cos(theta) coefficient
-B e^{-r^2}/r and cos(3theta) coefficient
B[(1-r^2)e^{-r^2}-1]/r^3. For R3 cos(3theta), its cos(theta)
coefficient is -A r e^{-r^2}; the other coefficient is cos(5theta),
which cannot pair with any source mode. These statements follow by
sin(mtheta)sin(2theta) and cos(mtheta)cos(2theta) product formulas.

Crucially, an arbitrary radial stream T(r) sin(2theta) contributes to
(4) only a sin(4theta) mode. Its vorticity is a sin(2theta) mode. Their
product has zero angular average, and every cross product with the
cosine modes1,3,5 also has zero average. Therefore **all** terms
involving C and delta integrate to zero. This observation extends the
Gaussian example in the numerics lane to a fixed nonzero algebraic tail.

Using integral_0^{2pi} cos^2(ktheta)dtheta=pi, the remaining terms are

    -4B^2 int_0^infty r(2-r^2)e^{-2r^2}dr = -3B^2/2,
    -4AB int_0^infty r^3(2-r^2)e^{-2r^2}dr = -AB/2,
    4AB int_0^infty r(4-r^2)e^{-r^2}
              [(1-r^2)e^{-r^2}-1]dr = -4AB.

Substitute t=r^2 and use integral_0^infty t^j e^{-a t}dt=j!/a^{j+1}
for j=0,1,2. Their sum gives(1). Since Theta is even in y and
K Theta_x is odd in y, its absolutely convergent integral is zero.
This proves Lambda=0 and all unboundedness claims.

## 3. Exact moment balance with a nonzero transport defect

Substitution of(2) into(1) gives NL=c. On the axis put H=Psi/x,
F=Theta/x^2. The local stream expansion is

    H=C y+(A-B)x^2+(-3A-B)y^2+O(r^3).

Thus h02=-3A-B=2c/(3B). Also F(0,y)=1+O(y^2), so F_y(0)=0.
The divided temperature residual on x=0 is exactly

    R_F=2[beta-H_y(0,y)]F(0,y)
          +W2(0,y)F_y(0,y)-(beta-2)F(0,y).

Its constant coefficient vanishes because C=c=1+beta/2. The linear
coefficient is -4h02, proving(3), which is nonzero. Since the smooth
coefficient R_F is nonzero at small y!=0, the original temperature
residual x^2 R_F is nonzero also at nearby points with x!=0. Merely
observing that the original residual is zero on the invariant axis
would miss this defect.

## 4. Noncoercivity of the temperature moment separately

For beta>=2 the same base Theta is nonnegative and equals xi^2 with
xi=x(1+q)^{-(1+2nu)/4}. Add M x^2 Bump(X), where Bump is a smooth
nonnegative x-even bump away from0 and the axis. Choose its support and
its x reflection in a region where sin(3theta)>0. Integration by parts,
with the convergent boundary terms justified in packet34, gives

    Lambda(Theta)=(1/pi) int Theta sin(3theta)/r^3 dX.

Hence the new Lambda tends to positive infinity with M. A bump in a
negative-kernel sector instead tends to negative infinity. The center
normalization, algebraic tail, nonnegativity and smooth square root
persist, since the base divided F is strictly positive everywhere.
These square roots are not asserted to be Koopman eigenfunctions of a
velocity. The coupled transport equation is precisely the missing
condition.

Dependencies: polar differentiation, angular orthogonality, elementary
exponential integrals, canonical inverse uniqueness, and packet34's
moment derivation. The numerics-lane proof was read, but no code from
that lane is imported or executed. This is a standalone informal proof;
no formal assistant verification is claimed.

## 5. Verification record

Own code code_independent/strain_moment_counterexamples.py uses direct
Cartesian derivatives and radial/angular quadrature for the moments,
with a separately implemented Cartesian full-plane inverse. The saved
checks and numerical limitations are in verification/SUMMARY.md. They
are checks on the exact derivation, not interval certificates.

Actual Opus35 (claude-opus-5-5,130.373100seconds) confirmed the algebra
but initially substituted the opposite curl convention. The verifier
rejected that sign objection and sent the exact prompt equations.
Actual Opus36 (same model,67.102282seconds) independently rederived the
moment identity in the stipulated convention and withdrew the objection
and its proposed change to A. The verifier checked this followup.
Both original responses are retained in opus_reviews/35_nonlinear_strain_moment
and opus_reviews/36_moment_sign_followup. No model was silently substituted.
