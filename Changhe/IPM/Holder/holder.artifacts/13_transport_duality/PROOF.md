# Finite transport approximation of the principal-value norm

## Statement and conventions

Let 0<alpha<1. All functions are real valued, with

    [f]_alpha = sup_{z != w} |f(z)-f(w)|/|z-w|^alpha.

Work modulo additive constants. Put x=(1/2,0), y=-x and, in complex notation,

    K_phi(z) = Re(e^(i phi)/(2 pi z^2)),
    nu_phi(z) = K_phi(z-x)-K_phi(z-y)
              = Re(e^(i phi) z/[pi (z^2-1/4)^2]).

The functional Lambda_phi(f) is the centered principal value of integral
nu_phi f, with disks of equal radius removed at x,y and a centered outer
cutoff. It is the increment of T_phi=cos(phi)T_xx+sin(phi)T_xy. Its diagonal
counterpart is Lambda_phi^D(f)=Lambda_phi(f)-(f(x)-f(y))/2. The setup proof
in ../01_setup/PROOF.md establishes these increment definitions and their
extension to the homogeneous Holder space.

For 0<epsilon<1/2 and R>1, define

    Omega = B(0,R) \ (B(x,epsilon) union B(y,epsilon)),
    mu_phi = 1_Omega nu_phi dA,
    mu_phi^D = mu_phi - delta_x/2 + delta_y/2.

Both are finite signed measures with total mass zero. For any finite
zero-mass signed measure mu of compact support, let mu^+,mu^- be its
Jordan parts and define

    W_alpha(mu) = inf integral |z-w|^alpha d pi(z,w),

where the infimum is over nonnegative couplings with marginals mu^+,mu^-.
The zero measure has W_alpha(0)=0.

Write

    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)),
    E_loc=2 a2(alpha) epsilon^alpha/alpha
          +(1+2epsilon)^alpha epsilon^2/[2(1-epsilon)^2],
    E_far=2^alpha R^(alpha-1)
          /[(1-alpha)(1-1/(4R^2))^2],
    E=E_loc+E_far.

Then

    | ||Lambda_phi|| - W_alpha(mu_phi) | <= E,
    | ||Lambda_phi^D|| - W_alpha(mu_phi^D) | <= E,

uniformly in the phase phi. The functional norms take the supremum over
[f]_alpha<=1. In particular the operator norms defined in the task satisfy

    | C_alpha - sup_phi W_alpha(mu_phi) | <= E,
    | D_alpha - sup_phi W_alpha(mu_phi^D) | <= E.

As epsilon tends to zero and R tends to infinity, E tends to zero. Thus the
operator norms are limits of finite-measure transport problems. A sampled
transport objective alone is still not a bound unless all truncation,
spatial approximation and mass-computation errors are controlled.

## The principal-value truncation error

The function nu_phi is odd under z -> -z, and Omega is invariant under
that map. Its integral on Omega is therefore zero. The atoms of mu_phi^D
also have total mass zero. Absolute integrability on Omega follows from
its positive distance from both poles and its bounded radius.

Consider first the omitted two disks. The own-pole kernel on each circle
has mean zero. The angular Holder lemma in ../02_upper_bounds/PROOF.md
bounds its circle functional by a2(alpha) r^alpha [f]_alpha. Integrating
dr/r over (0,epsilon) and adding both disks gives the first term of E_loc.
No value f(x) or f(y) is estimated separately: its own-kernel integral is
exactly zero.

The remaining, smooth other-pole terms on the two disks combine by
reflection into

    - integral_{B(x,epsilon)} K_phi(z-y) [f(z)-f(-z)] dA(z).

Here |z-y|>=1-epsilon and |2z|<=1+2epsilon. Since
|K_phi(z-y)|<=1/[2pi(1-epsilon)^2], its absolute value is at most the
second term of E_loc times [f]_alpha. This argument proves convergence
of the omitted principal values as well as the error estimate.

On |z|>R, central reflection gives

    integral nu_phi(z) f(z) dA(z)
      = (1/2) integral nu_phi(z) [f(z)-f(-z)] dA(z).

The integrals converge absolutely after fixing, for example, f(0)=0.
The explicit rational kernel obeys

    |nu_phi(z)| <= r/[pi(r^2-1/4)^2],     r=|z|.

Therefore the tail is at most

    2^alpha [f]_alpha integral_R^infinity r^(alpha+2)/(r^2-1/4)^2 dr
    <= E_far [f]_alpha.

This uses (1-1/(4r^2))^-2 <= (1-1/(4R^2))^-2 and
integral_R^infinity r^(alpha-2) dr=R^(alpha-1)/(1-alpha).
The two atomic identity terms are present in both diagonal functionals,
so they cause no additional truncation error. The norm estimates follow
from the triangle inequality for bounded linear functionals, once the
finite-measure duality below is established.

## Finite-measure duality, including its compact approximation proof

For a finite zero-mass signed measure mu with compact support,

    W_alpha(mu) = sup_{[f]_alpha<=1} integral f dmu.                 (1)

The absolute value may be inserted on the right because f and -f are
both admissible. The snowflake distance d(z,w)=|z-w|^alpha is a metric:
(a+b)^alpha<=a^alpha+b^alpha. Any feasible coupling gives
integral f dmu=integral(f(z)-f(w))d pi <= integral d d pi. This proves
one inequality in (1).

For an atomic measure, finite-dimensional transport linear programming
duality gives the reverse inequality. Here is the conversion from the
two-potential dual to the single Holder potential, so no special
convention of transport duality is implicit. If positive masses are at
p_i, negative masses at q_j, a feasible dual pair obeys
A_i-B_j<=d(p_i,q_j). Set

    f(z)=min_j [B_j+d(z,q_j)].

It is 1-Lipschitz for d, f(p_i)>=A_i and f(q_j)<=B_j. Its signed integral
is therefore at least the dual objective. Strong duality applies to this
finite feasible bounded-cost linear program. If all masses vanish the
claim is immediate.

For the general compactly supported measure, choose a finite measurable
partition of its support, with Euclidean cell diameter at most h, and a
representative in each nonempty cell. Let P send each point to its
representative. Push mu^+ and mu^- forward separately, giving finite
nonnegative measures alpha_h,beta_h of equal mass M. Their difference
is mu_h=P_#mu. By the atomic result the optimal cost between alpha_h and
beta_h equals the single-potential norm of mu_h, even if the two atomic
measures have common mass. Indeed the same two-potential argument applies
with possibly coincident positive and negative locations; the single
potential objective depends only on their difference. Equivalently,
common mass may be cancelled at zero cost using the metric triangle
inequality.

For every [f]_alpha<=1,

    |integral f dmu - integral f dmu_h| <= h^alpha |mu|(R^2).       (2)

An optimal finite coupling between alpha_h and beta_h can be lifted to
a coupling between mu^+,mu^-: for each pair of representative cells use
the product of their normalized restrictions with the prescribed mass.
Zero-mass cells are ignored. On such a cell pair,

    d(z,w) <= d(Pz,Pw)+2h^alpha.

Consequently

    W_alpha(mu) <= W_alpha(mu_h)+2M h^alpha
                = ||mu_h||+|mu|(R^2) h^alpha
                <= ||mu||+2|mu|(R^2) h^alpha.

Let h tend to zero. Together with the first inequality this proves (1).
This proof requires only finite-dimensional linear-programming duality,
not an unproved infinite-measure transport assertion. Additive constants
are harmless because all signed measures have mass zero.

## From fixed increments to the operator norm

Translation and positive dilation reduce an arbitrary pair of evaluation
points to x,y. Rotation transfers its direction into phi, with every phi
represented. The Holder quotient is unchanged. The rotation identities
in ../01_setup/PROOF.md therefore give

    C_alpha=sup_phi ||Lambda_phi||,
    D_alpha=sup_phi ||Lambda_phi^D||.

Taking suprema preserves the preceding uniform error E and proves the
asserted operator estimates. The compact smooth test definition gives
the same constants by the approximation theorem in that setup proof.
No density claim in the full Holder seminorm is needed.

## Explicit spatial and phase errors for a finite computation

For either truncated signed measure mu, (1) and (2) imply the stronger
useful estimate

    |W_alpha(mu)-W_alpha(P_#mu)| <= h^alpha |mu|(R^2).

The total variation may be bounded without cancellation. On Omega,
|z-x| and |z-y| are between epsilon and R+1/2. Integrating each absolute
kernel over this larger annulus gives

    |mu_phi|(R^2) <= (4/pi) log((R+1/2)/epsilon),
    |mu_phi^D|(R^2) <= (4/pi) log((R+1/2)/epsilon)+1.

Indeed integral_0^{2pi}|cos(2theta-phi)|dtheta=4. Adding the two atoms
increases variation by at most one. For a grid with covering radius h0
in phase, a known upper bound C_alpha<=F(alpha) gives

    ||Lambda_phi-Lambda_psi||
      <= 2 sin(|phi-psi|/2) F(alpha).

The same difference formula holds for Lambda^D, because the atoms cancel.
Thus phase sampling adds at most 2F(alpha)sin(h0/2) to the uniform error,
provided 0<=h0<=pi. Spatial errors use the displayed variation bounds
and exact cell masses. Thus, if W_h is the maximum of the spatially
discretized transport values over the sampled phases, then

    |C_alpha-W_h| <= E+h^alpha V+2F(alpha)sin(h0/2),

with V=(4/pi)log((R+1/2)/epsilon). For D use the atomic transport values
and replace V by V+1. These formulas compare the operator norm with the
maximum sampled value, not a single phase.

There is also a simple mass-error allowance. Suppose the exact and
approximate atomic signed masses have total mass zero, their difference
has total variation at most e, and their union of supports has diameter
D0. Any admissible f has oscillation at most D0^alpha on this support.
Subtract the midpoint of its extrema; the absolute pairing with the
error is then at most e*D0^alpha/2. By duality the corresponding transport
values differ by at most that number. Add this error to the displayed
formula when certified mass enclosures provide e. Unbalanced signed
masses require explicit correction before this argument applies. No
floating quadrature is authorized as exact.

## Dependencies and scope

Dependencies are the established kernel/rotation/approximation theorem,
the angular Holder lemma, and finite-dimensional linear-programming
strong duality. All singular and infinite-region limits were proved
above. This theorem justifies convergence of finite transport
approximations. It does not turn the numerical team's existing LP values
into lower or upper bounds: those values have additional unbounded or
unrecorded errors and use heuristic omitted-region terms.
