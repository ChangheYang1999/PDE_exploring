# A velocity estimate for a quadratically growing Hessian weight

Status: proposed operator theorem, OPEN independent Opus review. This
estimate supplies one derivative row for a possible graded space. It
does not supply a transport inverse or an a posteriori existence theorem.

## Statement

Let h be a real, smooth, compactly supported, centrally odd function on
R2. In particular h may have S1 parity, even in x and odd in y. Let
U[h]=(-R1R2h,R1^2h), where Rj has Fourier symbol -i xi_j/|xi|. For R>0
put w2(X)=1+|X|^2/R^2. Let D2 be the full ordered Cartesian Hessian,
with squared scalar norm |h_xx|^2+2|h_xy|^2+|h_yy|^2 and the additional
sum over both velocity components. Then

    ||w2 D2 U[h]||2 <= (1+sqrt(6))/2 ||w2 D2 h||2.       (1)

The bound is independent of R. It extends to the completion of the
stated compact test class in the input Hessian norm, with the canonical
velocity acting on the limiting derivative tensor.

The main new input is the homogeneous moment estimate

    ||r^2 D2 B h||2^2 <= 6 ||r^2 D2 h||2^2,             (2)

where B has multiplier (xi1-i xi2)^2/|xi|^2. The constant6 in (2) is sharp
on real S1 tests; no sharpness of the velocity constant in (1) is claimed.

## 1. The angular mode and Mellin calculation

Write d=(partial_x-i partial_y)/2 and dbar=(partial_x+i partial_y)/2.
The multiplier identity dbar B=d gives, for

    h_m=f(r)e^(im theta), B h_m=g(r)e^(i(m-2)theta),

    (D-m+2)g=(D+m)f,  D=partial_t, t=log r.            (3)

Only odd integers m occur. The canonical solution is selected by
regularity at zero and decay at infinity. For m=1 it is g=f. For m>=3
it vanishes beyond the support of f and near zero is O(r^(m-2)). For
m=-M<=-1 it is regular, O(r^(M+2)) near zero, and outside the support
it is a multiple of r^(-M-2). These statements also follow directly by
integrating the first-order equation (3). They agree with the canonical
multiplier: any difference solves the homogeneous equation, and either
its singular origin or its growing exterior excludes it. For m=1 the
extra homogeneous solution is r^-1 and is excluded at zero.

The complex derivative change of basis is unitary up to the factor2.
Consequently, for any complex v,

    |D2 v|^2=4(|d^2 v|^2+2|d dbar v|^2+|dbar^2 v|^2).

For v=f(r)e^(im theta), the three derivative factors, apart from their
unit angular phases, are

    d^2:    r^-2 (D+m-2)(D+m) f /4,
    d dbar: r^-2 (D-m)(D+m) f /4,
    dbar^2: r^-2 (D-m-2)(D-m) f /4.

Put F(t)=e^t f(e^t), G(t)=e^t g(e^t), and Fourier transform in t with
frequency tau. The r^4 moment cancels the r^-4 derivative factor, and
r dr=e^(2t)dt. Thus D on f becomes kappa=-1+i tau on F. If u=tau^2,
the energy for mode m, divided by its common factor pi/2, is

    integral Q_m(u) |Fhat(tau)|^2 dtau,
    Q_m(u)=4[m^4+10m^2+5+(2m^2+6)u+u^2].              (4)

For clarity this polynomial is the sum

    [(m+1)^2+u][(m+3)^2+u]
      +2[(m-1)^2+u][(m+1)^2+u]
      +[(m-1)^2+u][(m-3)^2+u].

Equation(3) in these coordinates gives

    Ghat=(m-1+i tau)/(1-m+i tau) Fhat.                 (5)

For m !=1 this multiplier has absolute value1. For m=1, G=F directly,
so the removable value at tau=0 causes no problem. The output moment
energy is therefore the same integral with Q_(m-2) replacing Q_m.
The origin and exterior behavior stated above implies F,G and their
first two derivatives are square integrable in t. All Mellin and
Fourier operations are legitimate, including modes whose input reaches
the origin.

## 2. The exact uniform mode bounds

Write q(M,u)=Q_M(u)/4. It is even in M and increasing in M>=0 for u>=0.
For positive odd m, |m-2|<=m, hence Q_(m-2)<=Q_m. For m=-M, M>=1,

    11q(M,u)-q(M+2,u)
      =(M-1)(10M^3+2M^2+78M+6)
          +(20M^2-8M+52)u+10u^2 >=0.                (6)

The coefficient20M^2-8M+52 is positive on M>=1. Thus the positive mode
has squared bound1 and its negative partner has squared bound11.
For a real input f_(-m)=conjugate(f_m). Since Q_m is even in both m
and tau, the two input energies are equal. Summing their output bounds
therefore gives (1+11)/2=6. Orthogonality across distinct input modes
and across their distinct output modes proves (2).

The factor6 is sharp already for the real S1 pair m=1,-1. Take
h(r,theta)=r^-1 a((log r-T)/L) sin(theta), where a is a fixed nonzero
smooth real bump of compact support. Each such function is smooth and
compactly supported on an annulus. In Mellin coordinates F=a((t-T)/L)
and the normalized spectral energy concentrates at tau=0 as L tends
to infinity. At that frequency Q_1=64 and Q_3=704, giving the paired
ratio (64+704)/(2*64)=6. Polynomial growth of Q and rapid Fourier decay
of a justify passage to the limit by scaling and dominated convergence.
There is no boundary term at either edge of the annulus.

## 3. Velocity and the inhomogeneous weight

The exact signed IPM symbol gives

    U2[h]+i U1[h]=-(h+B h)/2.

Because h is real, summing the squares of the real velocity components
agrees with the squared complex norm on the right. The triangle
inequality and (2) imply

    ||r^2 D2 U[h]||2 <= (1+sqrt(6))/2 ||r^2 D2 h||2.    (7)

The unweighted multiplier gives ||D2 U[h]||2<=||D2 h||2. The audited
T4-206 first-moment identity gives

    ||r D2 U[h]||2 <= sqrt(5/3) ||r D2 h||2.

Finally w2^2=1+2r^2/R^2+r^4/R^4. Add the three squared estimates,
using 1 and 5/3 no larger than ((1+sqrt(6))/2)^2. This proves (1).

For a general compact smooth odd h, finite angular Fourier truncations
converge in the input moment norms: the full Hessian norm splits into
the nonnegative modal energies just displayed. The inequalities make
the output truncations Cauchy in the weighted norm; unweighted L2
continuity of B acting on D2 identifies the limit with D2 B h. This
also proves (2) without a finite angular support assumption.

For the stated completion, D2 h_n converges in unweighted L2 as well
as in the weighted tensor norm. The canonical U acting componentwise
on that unweighted limiting tensor is unique and agrees with the
weighted output limit. The assertion concerns the derivative tensor;
it imposes no unjustified pointwise normalization on a representative
of a homogeneous Sobolev completion.

## Scope and dependencies

The new p=2 Hessian row goes beyond applying the existing weighted
scalar bound separately to each even derivative component. It uses
their common scalar origin and the odd angular modes of h. It can be
combined with the audited p=0 scalar row and p=1 gradient row in
||h||2+||w1 grad h||2+||w2 D2 h||2, where w1=sqrt(w2). Controlling
transport, its coefficient derivatives, the strain functional and the
nonlinearity in that space remains separate work.

Dependencies: the displayed canonical multipliers, Plancherel and
angular orthogonality, the elementary mode solution also audited in
T4-194, and T4-206's first-moment bound. No numerical candidate data
or external weighted singular-integral theorem is used. Symbolic
checks in verification/ supplement the complete proof above.
