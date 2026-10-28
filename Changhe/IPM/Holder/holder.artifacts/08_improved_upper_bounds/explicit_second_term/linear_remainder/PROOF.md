# Explicit upper bounds with a remainder linear in the Holder exponent

## Statement

Use the spaces, kernels, quotient extension, constants a2(a), A(a), E(rho)
and tau of ../PROOF.md. For 0<a<1 and 0<rho<1/2 define

    N0(rho) = 1/2-(2/pi)log(rho),
    L(rho) = max{-log(1-2rho), (1+2rho)log(1+2rho)},
    B_C(rho) = rho^2/(1-rho)^2 [-log(rho)+3/2-log(2)/2],
    B_D(rho) = 3rho^2/[4(1-rho)^2] [-log(rho)+log(2)+2/3],
    T(a) = (2^(a+1)/pi) a [1/(1-a)+1/2-log(3/2)],
    J_C(a,rho) = 2a2(a)rho^a/a + 2^a N0(rho)
                 +(2^a-1)E(rho)+T(a)+a[B_C(rho)+E(rho)L(rho)],
    J_D(a,rho) = 2A(a)rho^a/a+1/2 + 2^a N0(rho)
                 +(2^a-1)E(rho)+T(a)+a[B_D(rho)+3E(rho)L(rho)].

Then the homogeneous seminorm constants satisfy

    C_a <= J_C(a,rho),       D_a <= J_D(a,rho).               (1)

All constants are explicit. For each fixed 0<rho<1/2,

    J_C(a,rho) = 2/(pi a)+C0+O_rho(a),
    J_D(a,rho) = 2/(pi a)+2C0+O_rho(a),
    C0 = 1/2+(log(2)-1)/pi.                                 (2)

Thus these upper bounds have the sharp first two terms and only a linear
upper error. Statement (2) alone does not supply a matching linear lower
error for the true sharp norms. The old estimate in ../PROOF.md remains
independently valid.

## Notation and the finite part

Put x=1/2, y=-1/2 and nu_b(w)=K_b(x-w)-K_b(y-w). Write D_rho for the
complement of the two radius-rho pole disks. The definitions and exact
finite-part identity from the parent proof are

    V_b(rho) = (1/2) integral_(D_rho) |nu_b|,
    Delta_b(rho) = (1/2) integral_(two disks)
                         (|nu_b|-|own kernel|),
    V_b(rho)+Delta_b(rho) = N(b)-(2/pi)log(rho),
    N(b)<=1/2,   |Delta_b(rho)|<=E(rho),   V_b(rho)<=N0(rho)+E(rho).

The cross kernel has absolute integral at most E(rho) on each disk,
and pointwise absolute value at most

    H(rho) = 1/[2pi(1-rho)^2].

The exterior antipodal plan from the parent proof has cost at most

    V_b(rho)+(2^a-1)[N0(rho)+E(rho)]+T(a).                  (3)

Indeed, subtract the base cost 1, bound the remaining cost below radius1
by 2^a-1, and bound the excess above that base for radius>1 by the same
positive Fourier series used there. Negative excess below radius1/2 may
be discarded. It remains to build local plans with cost at most the
usual own-kernel cost plus Delta_b(rho) and the stated linear error.

For any point w in a pole disk or at a pole, 2|w| lies between 1-2rho
and 1+2rho. The mean value theorem applied to s -> t^s proves

    |(2|w|)^a-1| <= a L(rho).                               (4)

## Local circle plan for C

At each radius r, split the positive lobes of the own kernel into four
half-lobes. Let t in (0,pi/4) be distance in angle from the adjacent zero
ray. Reflection across that ray pairs points p and q whose distance is

    d = 2r sin(t).

Relative to r dr dt, the own signed densities at this pair are u and -u,
where u=sin(2t)/(2pi r^2). The true densities of nu_b at these two points
are A=u+e and B=-u+f, with |e|,|f|<=H(rho). Extract an opposite-sign pair
of mass

    m = (|A|+|B|-|A+B|)/2.

This is nonnegative. It pairs min(|A|,|B|) when the signs differ, and zero
when they agree. The direction is chosen according to the actual signs.
The residual has total variation |A+B|. The triangle inequality gives

    |m-u| <= |e|+|f|,      |A+B| <= |e|+|f|.                 (5)

Make the reflected construction at the other pole. The complete
residual is odd under w -> -w, and is paired antipodally. Its flow mass
is the total variation on one pole disk, at most the integral of the
absolute cross kernel there, hence at most E(rho).

Subtract the original own-kernel circle cost and also the change
Delta_b(rho) in one-half total variation. The exact resulting expression
is the integral of 2(m-u)(d^a-1) over the four right-disk pair families,
plus the residual antipodal cost minus its flow mass. Since d<1,

    |d^a-1| <= a[-log(d)].

Equations (4) and (5), four pair families and two poles bound the first
error by

    16a H(rho) integral_0^rho r dr integral_0^(pi/4)
                                  [-log(2r sin(t))] dt.

Concavity gives sin(t)>=(2sqrt(2)/pi)t on this angular interval. Thus

    integral_0^(pi/4) [-log(2r sin(t))]dt
       <= (pi/4)[-log(r)+1-log(2)/2].

Integrating r dr yields exactly a B_C(rho). The residual error is at most
a E(rho)L(rho). The two own-kernel circle plans have cost
2a2(a)rho^a/a. We have proved the local bound

    2a2(a)rho^a/a+Delta_b(rho)+a[B_C(rho)+E(rho)L(rho)].      (6)

The residual variation and the cost differences are finite down to r=0.
The original circle plan has finite d^a cost. Thus the construction acts
on every Holder input and agrees with the circular principal value by
first truncating the circle integrals, then using the integrable cross
kernel to pass to the limit.

## Finite perturbation of the projection plan for D

We spell out a general transport modification used here. Suppose a
centrally odd signed measure m has a transport plan pi, invariant under
central reflection with source and target exchanged. Its positive and
negative marginals may have infinite mass near the poles, but its
Holder cost is finite. Let delta be a finite centrally odd perturbation,
and put m'=m+delta. At each positive source retain at most the available
positive m' density, and at each negative target retain at most the
available negative m' density. More precisely, if q_s and q_t are the
fractions of the old marginal that must be removed at the two ends,
retain the fraction min(1-q_s,1-q_t) of pi on each edge. Retained
marginals have the right sign and do not exceed those of m'.

Let R be the mass of the removed flow. Since the removed fraction is at
most q_s+q_t, R is at most the sum of the two marginal deficiencies,
which is at most the total variation of delta. The residual signed
measure is centrally odd and is paired antipodally. Its flow mass is

    R+(1/2) integral (|m'|-|m|).                             (7)

The integral is finite, bounded in absolute value by ||delta||/2.
Equation (7) follows by subtracting the two marginals of the removed
finite flow; it does not subtract two divergent total masses. In
particular the residual flow mass is at most 3||delta||/2.

Relative to the original plan and to the half-variation change, the
new cost is bounded above by the removed-flow integral of 1-d^a plus
the residual integral of d_antipodal^a-1. These integrals are finite in
the application below. The difference of the represented functionals
is exactly the integral against delta. This follows because both the
removed and residual flows have finite mass and their signed marginal
difference is delta. Thus the argument also applies to a sigma-finite
plan representing a prescribed principal-value normalization.

Apply this construction to the two local projection plans in
../../local_projection/PROOF.md, together with their remaining positive
convolution measure and identity contribution. Their cost is

    2A(a)rho^a/a+1/2.

For a single pole the projection edge connects r v_+(t) to
lambda(t)r v_-(t), where lambda=cos(2t), 0<t<pi/4. Its length is

    d=r sin(2t).

The other edges, from Q_rho and the remaining atom, have length1. Their
coefficient is nonnegative since 1/pi<1/2. The full plan is invariant
under central reflection, including the reflected copy of each
Q_rho translation edge. It represents the own local increment minus
one half the pole jump, as proved by the identity
N_rho=P_rho+(1/pi)I-Q_rho. This normalization is essential: the finite
atom remaining in the transport representation has coefficient
1/2-1/pi, while the full represented operator has the required identity
coefficient 1/2.

Perturb the own-kernel density by the smooth cross kernels on both pole
disks; leave all atoms unchanged. The total variation of the perturbation
is at most 2E(rho), and its half-variation change is Delta_b(rho).
Consequently the residual flow mass is at most 3E(rho), by (7), and its
cost error is at most 3a E(rho)L(rho).

The length1 edges have zero removed-flow error. For each projection edge
family, its source deficiency is bounded by H(rho)r dr dt. In target
coordinates r'=lambda r, the target deficiency pulled back to the same
parameters is bounded by H(rho)lambda^2 r dr dt. These statements follow
from the exact projection-plan marginals and the pointwise cross-kernel
bound; no regularity of the retained fraction is needed. There are four
families at each of two poles. Hence the removed-flow error is at most

    8a H(rho) integral_0^rho r dr integral_0^(pi/4)
        (1+cos(2t)^2)[-log(r sin(2t))]dt.

The elementary angular integrals are

    integral_0^(pi/4) (1+cos(2t)^2)dt = 3pi/8,
    integral_0^(pi/4) (1+cos(2t)^2)[-log(sin(2t))]dt
         = (3pi/8)log(2)+pi/16.

They follow by t -> u/2 and differentiation at p=0 of
integral_0^(pi/2) sin(u)^p cos(u)^2 du
=Gamma((p+1)/2)Gamma(3/2)/(2Gamma((p+4)/2)); the ordinary log-sine
integral is the analogous formula without cos(u)^2. Radial integration
now gives exactly a B_D(rho). Therefore the local diagonal cost is at
most

    2A(a)rho^a/a+1/2+Delta_b(rho)
        +a[B_D(rho)+3E(rho)L(rho)].                         (8)

All deficit integrals, including the logarithmic weights, are finite.
In particular lambda -> 0 at one angular endpoint introduces no
uncontrolled target singularity; its Jacobian is lambda^2, and the
length is still r sin(2t). Sigma-finite marginals and the distributional
identity above justify the calculation without a false absolute
convergence claim for the unpaired own kernel.

## Completion

Add (3) to (6), or to (8). The exact identity
V_b(rho)+Delta_b(rho)=N(b)-(2/pi)log(rho), together with N(b)<=1/2,
gives (1), uniformly in the phase. Translation, rotation and scaling
restore every increment. The homogeneous extension and compact smooth
approximation are those of the setup. Phase projection proves the same
scalar-operator estimates on complex-valued inputs.

For fixed rho, every term in the two upper formulas, after subtracting
2/(pi a), is analytic at a=0. Using a2'(0) and A'(0) from the parent
proof, their values at a=0 are respectively C0 and 2C0. This proves (2).
The formulas remain valid at any admissible rational rho, whether or not
that cutoff is numerically optimal.
