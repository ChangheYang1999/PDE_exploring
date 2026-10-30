# Complete Hessian norms for the radius-scaled backgrounds

## Statement and notation

Let c>1, gamma=1/c, delta=1-gamma and p_j=2-(j+1)delta/2. Consider an
exact finite real S1 potential made from the campaign monomial, Legendre,
and scaled Legendre generators with radii in {1,10,25,50,100},
nonnegative branch indices j, and rho=-chi_xxy-chi_yyy.
Assume its retained generator identities establish smoothness at the
origin and D^k rho=O(r^(gamma-k)) for k<=2 at infinity. These conditions
are checked for the actual raw candidate through its structure audit.

This result encloses, on the whole plane,

    E_xx=int rho_xx^2, E_xy=int rho_xy^2, E_yy=int rho_yy^2,
    X^2=||D rho_x||2^2=E_xx+E_xy,
    Y^2=||D rho_y||2^2=E_xy+E_yy,
    ||D^2 rho||2^2=E_xx+2E_xy+E_yy.

The ordered Hessian counts the mixed derivative twice. It also evaluates

    kappa_HS^2=[(log 2-1/2) X^2+(3 log 2-2) Y^2]/(16pi).

Under the independently audited gradient-commutator theorem, this is the
exact Hilbert-Schmidt norm squared of

    K=(1/2)[R1,[R1,rho_y]]-(1/2)[R1,[R2,rho_x]],

where Rj has Fourier symbol i xi_j/|xi|. In particular ||K||<=kappa_HS.
The theorem's complete proof and cutoff extension to sublinear profiles
are in ../gradient_commutator/PROOF.md. The current calculation does not
prove a lower bound for ||K|| or an inverse estimate.

The calculation makes no assertion that theta is below a given bound.
Here theta=sup_X (sqrt(rho_x^2+rho_y^2)-rho_y)/2. A finite mesh maximum
is only a diagnostic. Even if the computed kappa is small, a signed
low-space rate requires its separate global theta certificate and the
operator's domain hypotheses. High inverse and nonlinear closure are
separate requirements.

## Direct Cartesian field construction

The exact raw potential is differentiated through order five. A derivative
with a derivatives in x and b in y, a+b=5, has the representation

    partial_x^a partial_y^b chi
      =sum_(j,n) v^(-p_j) r^-5 A_(j,n)(t) trig_n(theta),
    t=r^2/(1+r^2), v=1-t.

Each A is rational in t with denominator a product of 1+a_R v for
positive a_R=R^2-1 in the allowed scale set. All such factors are positive
on 0<=v<=1. The algebraic derivative recurrence is obtained by applying
partial_x=cos(theta) partial_r-sin(theta) partial_theta/r and
partial_y=sin(theta) partial_r+cos(theta) partial_theta/r. Its exact
implementation is shared with the own Cartesian rational-field backend.
Mixed partials are compared by both differentiation orders.

The second density derivatives are

    rho_xx=-chi_xxxxy-chi_xxyyy,
    rho_xy=-chi_xxxyy-chi_xyyyy,
    rho_yy=-chi_xxyyy-chi_yyyyy.

All fifth derivative coefficients contributing here are divisible by t^3;
the division is performed exactly and rejected if a remainder exists.
Since v^(-p_j)r^-5 t^3=r v^(3-p_j), their forms become

    f=r sum_(j,n) v^(1+(j+1)delta/2) B_(j,n)(t) trig_n(theta),

with f one of rho_xx, rho_xy, rho_yy. Here B=A/t^3 includes the indicated
signed sums. These fields have positive odd angular frequencies. The
xx and yy fields are sine series, and xy is a cosine series.

The exact t-divisibility verifies removal of the artificial polar
singularity. Physical derivatives at three nonzero rational Cartesian
points are compared against a separate order-five Taylor-jet evaluator
of the raw generators. This comparison does not replace the algebraic
derivation or endpoint checks.

## Complete-plane integration

Square each real component separately. Orthogonality gives angular square
integral pi at every positive frequency, zero between distinct modes,
and factor two for two different radial branches at the same frequency.
Let W_ell(t) be the exact rational sum of these products, grouped by
ell=j+j'+2. Then, since r dr=-dv/(2v^2) and r^2=(1-v)/v,

    int_R2 f^2 dX=(pi/2) sum_ell int_0^1
       v^(ell delta/2-1) (1-v) W_ell(1-v) dv.

Every group is integrated. For the nonnegative branch indices in these
candidates ell>=2 and ell delta/2-1>=delta-1>-1. The remaining factor
1-v is integrable at the origin; denominator factors stay positive.
Thus every displayed integral converges independently. This is also
consistent with f=O(r^(gamma-2)) at infinity and smoothness at zero.

The scalar factored-moment interface performs exact polynomial division
and partial fractions. It keeps the factor 1-v rather than replacing
the integrand by a finite spatial sample. Its beta and positive-pole
integrals are evaluated with outward Arb arithmetic, and each exact
decomposition is replayed. Group accuracy above 150 bits and a strictly
positive total energy are required. Components are then added with the
explicit tensor multiplicities. Square roots and logarithms are outward.

## Calibration, source binding and independent scope

Before new scaled candidates, all three component energies are assembled
for the accepted 007 source. The resulting X, Y, ordered Hessian norm and
kappa are compared with its independently accepted polynomial calculation.
All fifth-order mixed derivative identities and point jets are checked.
The candidate's exact coefficient file, manifest, structural audit,
previous calibration, proof and every executed helper are hashed.

For 016 and 017 the same complete procedure is used on their immutable
raw snapshots. Their saved FLOAT diag2 values are compared with the whole
plane X, Y and kappa. These differences include the finite radial range,
coefficient rounding and quadrature. The comparison alone does not
separate their individual contributions, and no mesh theta is promoted
to a whole-plane bound. The meshes' stored candidate hashes must match.

New candidate quantities remain OPEN until an independent lane checks
the scaled-background construction and integrals. Neither reproduction
of 007 nor agreement with FLOAT numbers certifies the new candidates by
itself. The new norm results have no effect on their already confirmed
necessary-distance exclusions.

## Dependencies and evidence

- ../joint_scaled_factored_weak/PROOF.md and code: exact rational fields.
- ../factored_pole_moments/PROOF.md and code: complete scalar integrals.
- ../background_sobolev/PROOF.md and accepted 007 record: calibration.
- ../gradient_commutator/PROOF.md: the operator interpretation.
- ../multiscale_generators/PROOF.md and Cartesian Taylor-jet code.

All outputs and execution evidence are in verification/, with code in
code/. The informal proof is written and checked before implementation.
No formal Lean build, external compute, quadrature-based certificate or
new axiom is used.
