# Independently replayed three-quarter-exponent lower bound

## Statement

For real functions on R^2 let [f]_(3/4)=sup_(x!=y)|f(x)-f(y)|/|x-y|^(3/4). Let T_xx have circular principal-value kernel (z_1^2-z_2^2)/(2pi|z|^4), extended modulo constants by the convergent increment formula. Put R_1^2=T_xx-I/2 and let D_(3/4) be its operator seminorm. The explicit bound D_(3/4)>=2.8938332593 holds, also when the defining supremum uses real smooth compactly supported test functions. No sharpness assertion is made.

## Admissible witness

Use the polygon-plus-projection witness of ../../pole_profile/PROOF.md and its global admissibility theorem with exact parameters alpha=3/4, b=3/4, c=-3/10, lambda=50/53. Those dependencies define the closed polygonal zero set, its signed distance profile, and the lattice clamp. They prove [f]_(3/4)<=1. The two evaluation points have distance one, and the identity contribution adds exactly 1/2 to the selected trace-free increment. The accepted compact approximation theorem transfers this homogeneous witness to the defining test class.

## Finite annuli and omitted regions

All 1220 tasks of ../manifest.json were independently evaluated by the frozen interval cell evaluator. The mesh uses delta=.005; it is a different computation from the producer's delta=.0035 result. Task identity, source identity, finite interval endpoints, exact radial coverage, and every retained task hash are checked in independent_audit.json. The midpoint exterior radius is exactly R=10^16. Remaining omitted regions are the two pole disks, the midpoint sliver, and the exterior.

The pole radius epsilon is selected among exact endpoints of the completed near-pole tasks. Removing a prefix of those tasks replaces it by the following analytic enclosure, never by zero. Write a=3/4 and

    C_e=(1-2epsilon)^(a-1),
    A=Gamma(1+a/2)/(2sqrt(pi)Gamma(3/2+a/2)),
    M=lambda A epsilon^a/a+epsilon^2/4,
    E_c=a C_e^3 epsilon^(3-2a)/(6pi lambda^2(3-2a)),
    E_s=epsilon^(a+2)/((a+2)(1-epsilon)^2).

The quadratic pole theorem supplies the lower endpoint M-E_c-E_s per pole. The active profile is valid when

    (lambda+2^(a-1))epsilon^a<=c+1/2,
    lambda epsilon^a<=1/2.

These inequalities are checked outward. If also a C_e epsilon^(1-a)<=lambda/2, the upper endpoint is M+E_s; otherwise the valid additional upper error a C_e epsilon/pi is retained. The selected record identifies which case holds.

The homogeneous exterior theorem gives main term 2a_3(a)R^(a-1)/(1-a), where a_3 is the angular integral defined in ../../homogeneous_tail/PROOF.md. Its required limiting-profile condition lambda(1+2^(-a))>=1 is checked outward. The angular tail theorem gives the explicit exterior error. The midpoint sliver is bounded by

    2^(a+3) eta^(a+3)/(pi(a+3)sqrt(1-eta^2)), eta=1/100.

Every smooth pole, clamp, sliver, and exterior error is included with the adverse sign. Exact rational addition of the remaining task endpoints and these outward analytic endpoints yields I0 in the recorded interval. Consequently

    D_(3/4)>=1/2+max(0,lower(I0),-upper(I0)).

The resulting trace-free lower endpoint exceeds 2.3938332593, and the final bound D_(3/4)>=2.8938332593 is rounded downward from that exact rational expression. Choosing the strongest of finitely many valid pole cutoffs does not require any claim about a continuous optimum.

## Reproduction and dependencies

Run code/audit_note14_annular_profile.py with this replay directory, --task-count 1220 --optimize-inner --one-sided --angular-tail, writing to a new directory. Then run code/accept_annular_replay.py on the result with this proof. The acceptance binds the complete task replay, the accepted global witness theorem, quadratic pole and angular exterior theorems, and their independent lead cross-read. These separate the finite interval computation from its analytic soundness argument. The exact selected radius, cells, error values, and admitted decimal are in accepted.json and independent_audit.json.
