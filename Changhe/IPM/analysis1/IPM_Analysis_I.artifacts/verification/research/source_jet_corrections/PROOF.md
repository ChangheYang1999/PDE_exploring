# Source jets, normalized face coupling, and a non-Dini forcing

Status at proof writing: analytical arguments below; finite scalar consequences
await the recorded independent checks. This addresses lead requests V22(a-c).
No assertion in this note is a decisive endpoint for IPM Analysis I.

## 1. Exact stationary source jet and a small trial-centred exclusion

Write sigma[h] = psi[h]_{xy}(0) for the RAW canonical strain, so the scaling
functional denoted c[h] in PROMPT.md is sigma[h]/3. Define

    W[h] = U[h] + (sigma[h]/3) X,
    F(rho) = (((1+sigma[rho])/3) X + U[rho]).grad rho - rho.

The canonical maps U and sigma are linear on the stated admissible domain.
Assume the background rho0 has the exact centre normalization, the IPM parity
(even in x, odd in y), rho0 is C^2 near P=(x*,0), and its velocity V0 is C^1
there, with V0(P)=0. Let

    mu = partial_y V0_2(P), g = partial_y rho0(P),
    gp = partial_x partial_y rho0(P).

For a correction h in the same parity class, assume h is C^2 near P and W[h]
is C^1 there and exists canonically. Preserve the centre coefficient so that
the displayed normalized F is the relevant equation. Put

    z=h_y(P), v=h_xy(P), u=W[h]_1(P), w=partial_y W[h]_2(P).

Then the exact identities are

    partial_y F(rho0)(P) = (mu-1)g,
    partial_y F(rho0+h)(P)
      = (mu-1)g + (mu-1)z + g w + gp u + w z + u v.             (1)

Proof. Linearity gives V(rho0+h)=V0+W[h]. Oddness in y gives
rho0_x(x,0)=h_x(x,0)=0 and V0_2(x,0)=W[h]_2(x,0)=0. Differentiate the
product V.grad rho once in y. At P the first velocity component is u,
the second component is zero, its y derivative is mu+w, the density's y
derivative is g+z, and its xy derivative is gp+v. Thus the derivative is
u(gp+v)+(mu+w)(g+z)-(g+z), which expands to (1). The same computation with
h=0 gives the first identity. It uses no stationarity of the trial.

If |z|,|v|,|u|,|w| <= delta, then

    |partial_y F(rho0+h)(P) - (mu-1)g|
       <= C delta + 2 delta^2,
    C=|mu-1|+|g|+|gp|.                                      (2)

This follows term by term from (1). Therefore, if

    |(mu-1)g| > C delta + 2 delta^2,                         (3)

no exact solution F(rho0+h)=0 has all four jets bounded by delta. Indeed,
F is C^1 near P under the displayed hypotheses, so an exact local solution
has partial_y F(P)=0, contradicting (2)-(3).

The numerical input is the verifier's independently integrated all-mode
canonical trial certificate `../modal_source/evidence/source_result.json`,
with its prior exact output and import-binding audits. Its exact rational
endpoints, not the printed decimal approximations, are used below. The
proposed safe consequences are

    |(mu-1)g| > 6.70e-7, C < 30.0230,
    delta = 2.2e-8 satisfies (3).                            (4)

The requested intermediate coefficient 30.0229 must be checked: it is
smaller than the approximate sum 29.7494906633335 + 0.27341144397725 +
0.00000002252805. If the exact endpoint test confirms C > 30.0229, that
number is rejected as an upper bound from (2); the safe number in (4)
replaces it. This is a rounding correction, not a claim that a particular
stationary solution or admissible jet tuple exists.

For positive D and C, the positive root of 2 delta^2+C delta-D=0 is

    d(C,D)=2D/(C+sqrt(C^2+8D)).                              (5)

It decreases with C and increases with D, either by differentiating the
implicit equation 2d^2+C d=D or by comparing its increasing left side.
For interval inputs C in [Clo,Chi], D in [Dlo,Dhi], (3) holds for every
delta < d(Chi,Dlo). Fresh Arb and mpmath.iv evaluate this optional scale;
only the explicit rational radius in (4) is used for the exclusion.

Scope. This neighbourhood is centred on the exactly specified modal trial
at its fixed source P. The source of a perturbed solution need not remain
at P; equation (1) does not assume it does. The four jets include two
nonlocal velocity quantities. We have no certified bound placing X3 in
this four-jet ball, and this ball is much too small to constitute a
meaningful uncertainty neighbourhood of the numerical branch. Neither
(3) nor (4) is a NO endpoint. No varying unnormalized exponent is covered.

## 2. Normalized strain in the face-dilation obstruction

Let rho be C^2 near a compact segment of the x-axis and odd in y, and put
G1(x)=rho_y(x,0). For a correction whose leading local velocity is the
linear strain (-sigma x,sigma y), normalization adds (sigma/3)X. The
resulting leading normalized field is

    (-2 sigma x/3, 4 sigma y/3).

Differentiating its coupling with rho at y=0 gives

    (2/3) sigma (2G1-xG1').                                 (6)

Directly, -2 sigma x rho_x/3 contributes -2 sigma x G1'/3;
4 sigma y rho_y/3 contributes 4 sigma G1/3. The unnormalized coefficient
sigma(G1-xG1') is therefore not the normalized one. In the lead's V22(b),
the symbol c[F_R] in (6) denotes the RAW strain sigma[F_R], not the
one-third scaling functional c[h] in PROMPT.md. This distinction prevents
an extra or missing factor of three.

Here is a standalone construction of the dilation argument. Choose a
nonnegative smooth even-in-both-coordinates bump chi, supported on four
small reflected patches away from both axes and in 3x^2>y^2. Let
F=x^2 y chi. For the canonical velocity kernel in PROMPT.md,
K2(Z)=(z1^2-z2^2)/(2 pi |Z|^4), the local density term vanishes near zero.
Differentiating K2(-Z) in its evaluation variable y gives

    sigma[F]=(1/pi) integral y(3x^2-y^2) F(X)/|X|^6 dX > 0.    (7)

Indeed partial_y K2(Z)=-y(3x^2-y^2)/(pi |Z|^6), and evaluation at -Z
reverses this sign. The integrand in (7) is nonnegative and positive where
chi>0 away from the axes. The compact support is separated from zero,
so differentiating under the integral is justified by bounded smooth
kernel derivatives. Near zero psi[F] is harmonic and odd in x and y;
its Taylor expansion is sigma[F]xy+terms of degree at least four. Hence
U[F]=(-sigma[F]x,sigma[F]y)+O(|X|^3), with differentiated bounds.

For b>2 and R>=1, put F_R(X)=R^(b-1) F(X/R). Its H_b norm, where
H_b=L^2(R^2,|y|^(-2b)dX), is independent of R: squared amplitude,
Jacobian and weight contribute R^(2b-2) R^2 R^(-2b)=1.
Homogeneity of the order-zero canonical multiplier, or directly of its
homogeneous kernel plus local term, yields

    U[F_R](X)=R^(b-1) U[F](X/R),
    sigma[F_R]=R^(b-2) sigma[F].

Consequently, on each fixed compact set,

    R^(-(b-2)) W[F_R] -> sigma[F](-2x/3,4y/3)

in C^1 (indeed in every fixed derivative norm), with O(R^(-2)) error.
The normalized coupling therefore converges after the same scaling to
sigma[F](-2x rho_x+4y rho_y)/3. If 2G1-xG1' is nonzero at one axis point,
its transverse derivative there is nonzero, so by continuity the limit
is nonzero on some compact interior patch separated from y=0. The weighted
L^2 norm on that patch grows at least a positive constant times R^(b-2),
while the input H_b norm stays constant. There is no bounded map from
H_b to this fixed local coupling norm, hence no claimed global H_b bound.
This argument uses an interior patch so it does not assume the outputs
are integrable against the singular weight across the axis.

For G1=x^2, coefficient (6) is zero. Thus the raw canonical obstruction
cannot simply be transferred to the normalized one without checking the
background. For the actual trial at P, the certified endpoints for
H=2g-x*gp are used to prove the proposed safe bound H>57.1. Continuity
then gives an axis neighbourhood where H is nonzero, without claiming
a quantitative width. This proves the local normalized obstruction for
that background and b>2. It does not establish a global inverse result.

## 3. C^1 source forcing with no Dini modulus and a C^1 solution

This is a local PURE TRANSPORT statement, not a claim about the nonlocal
frozen IPM operator. For any real A consider T=As partial_s+y partial_y-1.
For 0<|y|<exp(-1), let t=log(1/|y|) and define

    I(t)=integral_t^infinity sin(u)/u du,
    h(s,y)=y I(t), f(s,y)=y sin(t)/t,
    h(s,0)=f(s,0)=0.                                      (8)

Integration by parts gives

    I(t)=cos(t)/t - integral_t^infinity cos(u)/u^2 du,
    |I(t)| <= 2/t.

The remainder is absolutely convergent, which both proves existence of
the original improper integral and its bound. Since I'(t)=-sin(t)/t,

    h_y=I(t)+sin(t)/t,
    f_y=(sin(t)-cos(t))/t+sin(t)/t^2.                       (9)

Both derivatives tend to zero as y tends to zero. Also h/y=I(t)->0 and
f/y=sin(t)/t->0. Thus h and f extend as C^1 functions with zero derivative
at y=0, and h is independent of s. Substituting (9) gives T h=f exactly.
Both functions are odd in y and even in s.

Let omega(r)=sup_{|y|<=r}|f_y(y)-f_y(0)|, for small positive r. For any
T>=2 pi choose a positive integer j such that T<=2 pi j<T+2 pi. At
y_j=exp(-2 pi j), formula (9) gives |f_y(y_j)|=1/(2 pi j), whence

    omega(exp(-T)) >= 1/(T+2 pi).

Therefore integral_0^epsilon omega(r) dr/r diverges, by r=exp(-T) and
the divergent integral of 1/(T+2 pi) on a half-line. In particular there
is no Dini modulus for f_y at zero, despite a C^1 solution with f_y(0)=0.
This disproves necessity of a Dini condition in this local transport
example. It does not disprove its sufficiency or imply convergence for
arbitrary C^1 data, nor does it supply a bounded source inverse.

## Evidence and dependencies

The scalar certificate is an explicit dependency previously proved by this
lane using all canonical modes, rational sign bisection and pinned import
and output audits. This note recomputes every new interval expression by
exact rational endpoint arithmetic and two independent interval engines;
it does not pretend to repeat the integration from infinity. Symbolic
checks independently expand (1), (6), (7), (9), the norm scaling and (5).
A fresh saved-output audit and actual Opus 5.5 review are required before
publishing CONFIRMED numerical statements. No numerical sample proves
non-Dini behaviour; that conclusion is the argument above for every T.
