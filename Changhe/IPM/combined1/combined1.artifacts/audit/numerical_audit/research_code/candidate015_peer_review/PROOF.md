# Independent acceptance of the candidate015 reproductions

## Statement and scope

Fix c=4076476460239181/2251799813685248 and the exact candidate
C1-N1-015-pairQ-quot013, raw SHA256
 d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae.
The point and weak inequalities below are necessary conditions for a
stationary correction under the fixed-c canonical-velocity hypotheses
of ../generator_sector_audit/PROOF_CANDIDATES.md and
../scaled_factored_weak/PROOF.md. They make no existence or inverse claim.
This review accepts the independent polar reproductions of the own
Cartesian point calculation and the complete weak test n=19,K=600.

## Point test

Let V=cX+u and g=grad rho. If h belongs to H^(2+s)(R2), s>0, and
||h||_(H^(2+s))<=r, the correction equation and the audited Fourier
point embeddings give

 |F(X)| <= r[C1(s)|V|+C0(s)(1+|g|)]+C0(s)C1(s)r^2,
 C0(s)=(4pi(1+s))^(-1/2), C1(s)=(8pi s(1+s))^(-1/2).

At X=(1/10,73/100), a positive gap excludes precisely the stated ball.
The universal original-graded bound uses

 b0=50/(651 sqrt(28248) sqrt(4pi)), b1=25/(217 sqrt(8pi)),
 upper=b1|V|+b0(1+|g|)+b0b1.

These constants and hypotheses are proved in the existing graded-point
and generator proofs. T4 differentiates the finite potential using
exact radial Taylor jets through order four, then polar density and
velocity formulas. Our prior calculation uses Cartesian jets. The
frozen T4 proof and code have been inspected; the angular addition
recurrence retains the previous cosine in the sine update, and all
radial prefactor derivatives are included. We compare all eight field
enclosures, all six exact s/radius specifications, all scalar right
sides and positive gaps, the positive quadratic roots, and the universal
graded right side and gap. The signed theta diagnostic is compared
without treating it as a global supremum.

## Whole-plane weak test

Let phi=r(1-t)^2 t^600 sin(19 theta), t=r^2/(1+r^2). For a real S1
correction h in L2 with canonical divergence-free U[h] and
||U[h]||2<=||h||2, the cutoff weak identity implies

 |integral F phi| <= (M+C)||h||2+H||h||2^2,
 M=||(2c+1)phi+(cX+u).grad phi||2,
 C=||phi grad rho||2, H>=||grad phi||infinity.

Every norm and pairing is over the whole plane. The proof of the cutoff
and products is the existing weak proof. T4 independently expands the
polar angular products and integrates factored beta moments. We compare
both signed direct and integrated-by-parts pairings, M^2,C^2,M,C,D=M+C.
The radial derivative critical points are the two roots of the exact
quadratic stated in the frozen proof; the angular derivative maximum
comes from t=K/(K+2). All three outward amplitude bounds must be below
our finer rational H. Recompute the positive root using this same H and
verify that our strict rational floor is smaller. The coarser original
T4 H is a valid alternative, not an equality of the two H values.

## Identity, independence and records

The raw input and each canonical serialization are bound separately.
Their coefficient maps must agree exactly; different serialization
hashes are not interpreted as different profiles. All peer input hashes
are verified before copying, and copies or byte-identical retained own
files are recorded. Large new JSON inputs may be stored losslessly with
gzip, with both hashes recorded. No peer code is executed. The own code
compares two independently obtained results and re-evaluates their
scalar consequences with outward Arb arithmetic. Acceptance of this
R=1 candidate does not certify the new R=25 integration backend on a
scaled candidate. The declared-objective separation is the independently
proved result235, with its historical and selection limitations.
