# Three diagonal lower bounds with an explicit pole profile

Use real functions on R^2 modulo constants with the Euclidean seminorm
[f]_a=sup_(z!=w)|f(z)-f(w)|/|z-w|^a. Let T_xx have circular principal-value
kernel (z_1^2-z_2^2)/(2 pi |z|^4), using kernel differences at infinity,
and let D_a be the seminorm operator norm of R_1^2=T_xx-I/2. Then

    D_(1/2)>=2.4440555830,
    D_(3/4)>=2.8867542113,
    D_(9/10)>=5.2405443821.

These are lower bounds, not exact norms. They also hold for the supremum
over compact smooth test functions by the established compact approximation.

Use exactly the three witnesses, parameters, profile admissibility bounds,
finite prefix tasks and homogeneous exterior integrals of
../../homogeneous_tail/numerical_values/PROOF.md. That proof specifies
all global conventions and gives [f]_a=1 and D_a>=|I0|+1/2. The finite
integrals and every exact task endpoint remain unchanged here.

At the omitted pole disks, replace the symmetric zero-centered error E0
in that proof by the interval [M-E,M+E] of ../PROOF.md. The replacement
is valid under the two explicit inequalities there. Both inequalities
are checked with 320-bit outward arithmetic in each independent_audit.json.
The two disks have the same integral by reflection. Thus add 2M to the
finite and exterior integral and charge 2E as the total pole error.
Retain the entire midpoint sliver and homogeneous exterior error.

The auditor independently verifies all old source and prefix hashes,
parameters, complete radial coverage and exact rational sums before
this replacement. Its exact lower endpoint for I0 is positive in all
three cases. Adding 1/2 and rounding downward to ten decimal places gives
the displayed values. The unchanged cells and exact radii, and the new
Gamma, power and rational enclosures, are in ../verification/a50_prefix376,
a75_prefix398 and a90_prefix406.

The parent local proof was independently rederived in lead Note29, saved
as ../verification/lead_note29.txt. V138 accepts the analytic theorem and
all three numerical consequences; ../verification/accepted.json binds
that source, the original prefix audits and the new exact recombinations.
No numerical optimization or unproved approximation enters the inequality.
