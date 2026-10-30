# Candidate 017 signed background condition

## Exact statement and scope

Let c=4076476460239181/2251799813685248 and let chi be the exact finite
potential in C1-N1-017-legqs50-quot013, raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Its copied exact generator JSON is in
../candidate_audits/data/C1-N1-017-legqs50-quot013/
quot013_legqs50_m9to15_cpu_m16_exact.json.
Put rho=-partial_y Delta chi and

    theta=sup_X in R2 (sqrt(rho_x(X)^2+rho_y(X)^2)-rho_y(X))/2,
    K=(1/2)[R1,[R1,rho_y]]-(1/2)[R1,[R2,rho_x]],

where R_j is the L2 Riesz transform with Fourier symbol i xi_j/|xi|.
Let kappa=||K||_HS. The accepted complete Hessian calculation N4-268,
T4-366 and N4-303 gives the strict upper bound

    kappa < kstar=729080538628955349/1000000000000000000.

If the hash-bound rational Bernstein cover is complete and all its
leaf matrix bounds are nonnegative, it proves

    theta <= 2/25,
    c+1-theta-kappa > c+1-2/25-kstar > 2.00123867 > 2.

The finite cover and final strict rational comparison are checked in
the companion code. Before successful completion, and before independent
review of the new reconstruction and cover, this remains OPEN as a
team certificate. The scalar rate verifies the numerical (B-L2)
background inequality. Its use in an operator energy estimate remains
subject to that theorem's operator and domain hypotheses. This result
does not supply any other background hypothesis, high-space inverse,
nonlinear closure or existence theorem. The existing necessary-distance
exclusions for this exact candidate are unaffected.

## Proof of the implication

The full exact reconstruction in ../scaled_background_cover/PROOF.md
retains every generator and gives, for t=r^2/(1+r^2),
z=cos(2 theta_angle), and w=(1-t)^((1-1/c)/2),

    D(t)rho_y=sum_j w^j P_j(t,z),
    D(t)rho_x=sin(2 theta_angle) sum_j w^j Q_j(t,z),

with all coefficients rational and D(t)>=1 on [0,1]. Its exact
polynomial identities, origin cancellation, direct Cartesian values,
and calibration against every coefficient of the accepted007
reconstruction are retained and bound by hashes.

For tau=2/25 the symmetric matrix

    A_tau=[[tau+rho_y,-rho_x/2],[-rho_x/2,tau]]

has smaller eigenvalue tau-(sqrt(rho_x^2+rho_y^2)-rho_y)/2. The rational
Bernstein theorem of ../scaled_rational_background_cover/PROOF.md
bounds this eigenvalue on every rectangle by dividing each numerator
Bernstein coefficient by the corresponding strictly positive
denominator coefficient. Its independent-w enclosure is valid even at
t=1; its correlated degree-six Taylor enclosure includes an explicit
uniform remainder on t<1. Either lower bound can establish positivity.

The finite tree checker proves that the stored accepted rectangles
form a complete binary partition of [0,1] times [-1,1], with no missing
child and no ancestor/descendant or duplicate leaves. Nonnegative
stored outward eigenvalue lower bounds therefore prove A_tau>=0 on
the rectangle. The exact reconstruction and continuity at the origin
transfer this to all of R2. The t=1 boundary is included; it does not
represent an omitted finite radial tail. Thus theta<=tau.

The accepted Hilbert-Schmidt identity in
../gradient_commutator/PROOF.md applies to this smooth sublinear
profile. The complete-plane Hessian moments give kappa<kstar. Subtracting
the upper bounds for theta and kappa from c+1 gives the asserted strict
inequality. The final decimal lower bound is interpreted as the exact
rational200123867/100000000. Comparing it by integer arithmetic with
c+1-2/25-kstar proves its direction without decimal rounding.

## Evidence and limitations

The companion result binds the complete cover, every reconstruction
input, all accepted Hessian input hashes, the raw candidate, the proof,
and the checker. It independently reconstructs the leaf rectangles and
checks their exact areas as an additional diagnostic; the complete
binary-tree argument, not the area sum alone, establishes coverage.
Every positivity check uses the lower endpoint of its stored outward
ball. The leaf lower bounds were produced by the full interval range
calculation; the summary checker does not rerun each large matrix
product and cannot replace the requested independent cover replay.

A positive lower eigenvalue on a finite cover also gives a slightly
smaller upper bound for theta, but no such sharpening is needed here.
No sampled maximum, quadrature error estimate or new fitted candidate
enters this calculation. The complete original cover and run-stage
logs retain real runtime, including every incomplete stage.
