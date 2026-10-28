# Certified diagonal lower bounds with explicit pole and tail integrals

## Exact statement

Let 0<a<1 and let [f]_a be the Euclidean homogeneous Holder seminorm for
real functions on R^2. Define T_xx by the circular principal-value kernel
(z_1^2-z_2^2)/(2 pi |z|^4), with its extension modulo constants by
convergent increments. Put R_1^2=T_xx-I/2, and let D_a be its sharp real
operator seminorm, equivalently the supremum over smooth compactly
supported functions. The following rational decimal lower bounds hold
when the adjacent acceptance manifest has verdict CONFIRMED:

    D_(1/2) >= 2.4516960171,
    D_(3/4) >= 2.8870680072,
    D_(9/10) >= 5.2413008171.

The first value uses a finer independently replayed finite partition;
the other two use the previously completed partitions. No equality or
sharpness at a fixed exponent is asserted.

## Witness, coverage and proof

Use the exact polygon-plus-projection witness of ../../PROOF.md. Its
parameters and global Holder admissibility are recorded in each
independent_audit.json. The seminorm is at most one, the pole values
are opposite and differ by one, and the diagonal identity contributes
one half to the chosen output increment. Approximation by smooth
compactly supported functions preserves the lower-bound conclusion by
the accepted homogeneous-space approximation argument.

The finite region consists of disjoint annular tasks around the two
poles and the midpoint. Every task in the acceptance manifest has been
replayed by the immutable interval cell evaluator. Its source hashes,
exact interval endpoints, positive angular counts and complete radial
coverage are rechecked by audit_note14_annular_profile.py. The left
pole task contribution equals the right one by the witness symmetry.
Initial near-pole tasks are removed only at an exact completed annular
endpoint epsilon.

The omitted pole disks are replaced by twice the lower bound

    lambda A(a) epsilon^a/a + epsilon^2/4 - E_c - E_s

proved in ../PROOF.md. Each of its two hypotheses is checked outward
at the selected epsilon. The midpoint sliver retains its previously
proved symmetric error. Beyond the last completed midpoint radius R,
use the explicit homogeneous main term 2a3(a)R^(a-1)/(1-a), subtracting
the smaller of the two valid tail-error bounds in the homogeneous-tail
proof and its angular_error refinement. The limiting-profile condition
is separately checked. This accounts for the entire plane, the circular
principal values and infinity.

Adding exact rational lower endpoints of the retained finite tasks and
subtracting every positive error upper endpoint gives a lower endpoint
for the complete T_xx increment I0. Therefore

    D_a >= 1/2 + max(0, lower(I0), -upper(I0)).

The displayed decimals are downward roundings of this expression.
Finite optimization over epsilon selects among already valid bounds;
it supplies no unproved inequality. The acceptance manifest binds the
complete input hashes and the lead's independent analytic cross-read.

## Dependencies and evidence

The analytic dependencies are the parent quadratic-pole theorem, its
parent witness proof, and the homogeneous-tail and angular-error proofs.
The numerical evidence is in ../verification/, including the immutable
annular audits and accepted.json. code/accept_quadratic_pole_records.py
checks record identity and binds those completed computations after the
analytic cross-read. It performs no new integration. The exact JSON
records, not rounded narrative values, are the certificate inputs.
