# Certified diagonal lower bound at exponent 3/4

## Statement

For real-valued compact smooth functions on R^2, with Euclidean Holder
seminorm [f]_(3/4), the operator R_1^2=partial_xx(-Delta)^(-1) satisfies

    D_(3/4) >= 2.8821844092.

The same sharp seminorm is obtained on homogeneous Holder functions
modulo constants with the increment definition in ../../../01_setup/PROOF.md.
This statement is a rigorous lower bound, not an exact sharp norm.

## Witness and dependencies

Use the polygon Z0(b), signed distance g, projection profile P, half-plane
clamp and odd extension stated in ../PROOF.md, at b=3/4, c=-3/10 and
lambda=50/53. The full-range profile certificates in
../../../07_diagonal_identity_term/full_range_profile/verification/
(a75_k106_same.json and a75_k106_opposite.json) give [P]_(3/4)<=53/50.
The lattice lemma then gives [f]_(3/4)<=1 and pole values -1/2,+1/2.

With K(z)=(z1^2-z2^2)/(2 pi |z|^4), let I0 be the circular principal
value integral of (K(z-e1)-K(z))f(z). The norm identity for the two
choices of the local identity term gives D_(3/4)>=|I0|+1/2.
Compact approximation with asymptotically unchanged seminorm justifies
the initial compact smooth class; see the setup and lattice proofs.

## Verified integral

The analytic cell rules and remainders are proved in ../PROOF.md and
../repairs/PROOF.md. The immutable repaired sources are recorded in
manifest.json. The verifier independently enumerated and computed all
456 tasks, totaling 9078024 cells, with exact rational
endpoints saved in task_*.json. The radial partitions cover
[10^(-6),1/2] about the right pole and [1/100,10^16] about the midpoint.
The left near disk contributes the same amount by reflection. The
inner disks, midpoint sliver and exterior are covered by the three
explicit analytic remainder bounds. No tail or boundary region is
omitted.

The independent auditor checks exact once-only radial coverage,
source and profile dependencies, and independently recomputes all
remainders at 256 bits. It then sums rational endpoints exactly.
Its outward interval for I0 is

    [2.3821844092033339, 2.4089788200920158].

The exact rational lower endpoint plus 1/2, preserved in
independent_audit.json, exceeds 2.8821844092. This proves the claim.

The earlier submitted decimal 2.8823170689 is slightly larger than
this replay supports. It remains unconfirmed here. Distinct partition
choices and the repaired implementation can produce different valid
enclosures of the same integral; this difference alone does not refute
the earlier number.

Verification date: 2026-10-28T08:37:21.557000+00:00.
