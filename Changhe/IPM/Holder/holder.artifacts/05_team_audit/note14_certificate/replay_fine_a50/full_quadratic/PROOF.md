# Certified half-exponent diagonal lower bound

## Statement

Let [f]_(1/2)=sup_(x!=y)|f(x)-f(y)|/|x-y|^(1/2) for real functions on R^2. Define T_xx by the circular principal-value kernel (z_1^2-z_2^2)/(2 pi |z|^4), extended modulo constants by its absolutely convergent increment formula, and put R_1^2=T_xx-I/2. The operator seminorm D_(1/2), equivalently its supremum over real smooth compactly supported test functions, satisfies

    D_(1/2) >= 2.4531232777.

This is a rational decimal lower bound, not a claim of equality. Its numerical acceptance is bound to accepted.json in this folder.

## Witness and proof

Use the polygon-plus-projection witness of ../../pole_profile/PROOF.md and its cited global admissibility theorem with the exact parameters alpha=1/2, b=3/4, c=-3/20 and lambda=1000/1021. These dependencies define the polygon distance profile and the lattice clamp explicitly and prove its global Holder seminorm is at most one. The two evaluation points have unit separation, opposite witness values, and their diagonal identity contribution adds one half to the selected trace-free increment. The accepted smooth compact approximation theorem transfers this witness to the defining test class.

All 1847 tasks of ../manifest.json were independently evaluated by the frozen interval cell evaluator. The exact finite partition and every task hash are in independent_audit.json. The replay used 13777550 cells. The outer midpoint radius is R=100000000. It leaves only pole disks, the recorded midpoint sliver, and the exterior region. Task coverage, shared endpoints, evaluator source identity and interval finiteness are checked before recombination.

Remove the first 934 near-pole tasks and set epsilon=11700857978944199/1000000000000000000, their exact outer endpoint. The quadratic pole theorem gives each omitted disk the lower bound M-E_c-E_s and upper bound M+E_s. Here, with a=1/2,

    C_e=(1-2epsilon)^(a-1),
    A=Gamma(1+a/2)/(2 sqrt(pi) Gamma(3/2+a/2)),
    M=lambda A epsilon^a/a+epsilon^2/4,
    E_c=a C_e^3 epsilon^(3-2a)/(6 pi lambda^2(3-2a)),
    E_s=epsilon^(a+2)/((a+2)(1-epsilon)^2).

The exact outward record verifies (lambda+2^(a-1))epsilon^a<=c+1/2, lambda epsilon^a<=1/2 and a C_e epsilon^(1-a)<=lambda/2. The first two conditions justify the local active profile; the third justifies its nonpositive clamp correction and the sharper upper endpoint.

The homogeneous exterior theorem and its angular error refinement supply the tail main term and its explicit error at R. The required limiting-profile condition has an outward lower bound exceeding 1.67, hence exceeds one. The retained midpoint-sliver error and both smooth pole errors are subtracted, never omitted. Exact rational endpoint addition gives a complete trace-free increment I0 in the interval recorded in independent_audit.json; its lower endpoint is greater than 1.9531232777. Consequently

    D_(1/2) >= 1/2 + max(0, lower(I0), -upper(I0)) >= 2.4531232777.

The displayed decimal is rounded down from the exact rational result. Selecting epsilon among finitely many already valid endpoints does not require an unproved optimization claim.

## Dependencies and reproducibility

The analytic dependencies are the global polygon witness and its Holder profile certificate, the two quadratic pole lemmas, the homogeneous tail lemma, the angular tail error lemma, and the homogeneous-space approximation theorem. Their hashes and the lead's accepted independent cross-read are retained by accepted.json. The full finite replay is recorded separately from these analytic arguments. Run code/audit_note14_annular_profile.py with this replay folder, --task-count 1847 --optimize-inner --one-sided --angular-tail, writing to a new folder; then run code/accept_annular_replay.py on that audit. The acceptance script checks all hashes, task identities, pole conditions, exact recombination and downward rounding before admitting the number to data/accepted_external_D.json.
