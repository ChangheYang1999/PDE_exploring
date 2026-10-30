# Whole-plane signed gradient bound for rational scaled backgrounds

## Statement and exact inputs

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Let chi be a finite real linear combination of the campaign generators
at radii in {1,10,25,50,100}, with the exact coefficients and shapes in
an immutable candidate JSON. Put rho=-partial_y Delta chi. Each
potential is separately even, smooth on the plane, and has the canonical
velocity convention of ../multiscale_generators/PROOF.md. The derivative
construction and all inputs must be hash-bound to the stated candidate.
Let tau be the positive rational threshold recorded in the certificate.

A completed certificate proves on all of R^2 that

    theta(X)=(sqrt(rho_x(X)^2+rho_y(X)^2)-rho_y(X))/2 <= tau.

Its sufficient and necessary matrix form is

    A(X) = [[tau+rho_y(X), -rho_x(X)/2],
            [-rho_x(X)/2, tau]] >= 0.

The smaller eigenvalue of A is tau-theta. The sign of the off-diagonal
entry does not affect this equivalence. A finite mesh maximum does not
prove this statement. An incomplete partition, a failed cell bound, or
an unreviewed new certificate has the explicitly stated OPEN status.
No conclusion about an inverse or existence is part of this theorem.

## Exact compactified reconstruction

Set t=r^2/(1+r^2), v=1-t, w=v^(delta/2), and z=cos(2 theta_angle).
The raw Cartesian derivative recurrence, proved in
../joint_scaled_factored_weak/PROOF.md, gives each fourth derivative as
sum_(j,n) v^(-p_j) r^(-4) A_(j,n)(t) trig_n(theta_angle), where
p_j=2-(j+1)delta/2. The rational function A has denominator a product
of L_R(t)=1+(R^2-1)(1-t), and its numerator is divisible by t^2.
This divisibility is checked exactly for every retained coefficient.
It removes the artificial polar singularity, since

    v^(-p_j) r^(-4) t^2 = w^(j+1).

All angular frequencies of rho_y and rho_x are even. The first field
is a cosine series and the second a sine series with no constant mode.
Use cos(2k theta_angle)=T_k(z) and
sin(2k theta_angle)=sin(2 theta_angle) U_(k-1)(z). Let e_R be the
largest denominator exponent in any of these coefficients, and let
D(t)=product_R L_R(t)^e_R. Then D(t)>=1 for 0<=t<=1 and exact rational
clearing gives polynomial maps P_j(t,z), Q_j(t,z) such that

    D rho_y = sum_(j=1)^J w^j P_j(t,z),
    D rho_x = sin(2 theta_angle) sum_(j=1)^J w^j Q_j(t,z).

Set B=D A. Its diagonal entries are tau D plus the displayed first
sum, and tau D; its off-diagonal entry is minus one half the displayed
second sum. Because D>0, proving B>=0 proves A>=0. Every factor,
coefficient, branch, and angular term is retained. At t=0 all w powers
are one; the exact combined origin polynomial must be rho_x=0 and a
constant rho_y. At t=1 all positive w powers are zero, so the matrix is
tau times the identity. These endpoint identities and direct raw Taylor
jet overlaps at three nonzero rational points check the reconstruction.
The exact recurrence is the proof of its validity between those points.

## Polynomial bounds on one rectangle

Consider rational a<=t<=b in [0,1] and c0<=z<=d0 in [-1,1]. Affine
substitution to the unit square followed by the exact power-to-Bernstein
basis formula gives each polynomial a tensor Bernstein representation.
The basis functions are nonnegative and sum to one, so the minimum and
maximum of its Bernstein coefficients bound the polynomial everywhere.
Every arithmetic operation and coefficient enclosure uses outward Arb
balls. Rational operations before enclosure are exact.

There are two valid ways to enclose the sums in w. First treat t and w
as independent variables and use

    (1-b)^(delta/2) <= w <= (1-a)^(delta/2).

Convert each w polynomial to the Bernstein basis on this interval and
combine it with the two polynomial variables. Taking extrema of all
coefficients encloses every entry, including the actual correlated
curve w=(1-t)^(delta/2). This bound also applies when b=1.

When b<1, a second enclosure keeps the correlation. Expand
f_j(t)=(1-t)^(j delta/2) at mu=(a+b)/2 through degree six. Its kth
coefficient is (-1)^k (q)_k (1-mu)^(q-k)/k!, q=j delta/2. Its absolute
Taylor remainder is at most

    |(q)_7| H^7/7! * max((1-a)^(q-7), (1-b)^(q-7)),
    H=(b-a)/2.

This follows from the seventh derivative and the interval form of
Taylor's theorem; the maximum occurs at an endpoint because the
remaining positive power function is monotone. For j=0 the remainder
is zero. Express the Taylor polynomial and each P_j or Q_j in the
Bernstein basis and multiply them using

    B_(i,n) B_(k,m) = binom(n,i) binom(m,k)/binom(n+m,i+k)
                       * B_(i+k,n+m).

Bound the remainder of each product by its Taylor remainder times the
largest absolute Bernstein coefficient of the other factor. Add those
nonnegative errors to the final lower and upper bounds. This yields a
second valid enclosure for each matrix entry. It uses no quadrature.

## Matrix lower bound and complete partition

Suppose the diagonal entries are bounded below by A0,B0, and the
polynomial coefficient of sin(2 theta_angle) in the off-diagonal entry
has absolute bound Q0. On the angular interval,

    |sin(2 theta_angle)| <= sqrt(1-zmin^2),

where zmin=0 if the interval crosses zero and otherwise is the smaller
absolute endpoint. Put C0=Q0 sqrt(1-zmin^2). The smaller eigenvalue of B
is at least each of

    (A0+B0-sqrt((A0-B0)^2+4 C0^2))/2,
    min(A0,B0)-C0.

Indeed replacing the diagonals by lower bounds subtracts a positive
semidefinite diagonal matrix, and the explicit smaller eigenvalue is
monotone decreasing in the off-diagonal magnitude. The second bound
also follows from the diagonal part and the norm of the off-diagonal
part. Thus the larger of these two lower bounds is valid. The larger
of the independently valid correlated and independent-w lower bounds
is also valid. A cell is accepted only when a directed lower enclosure
is nonnegative.

The initial rectangle is [0,1] x [-1,1]. Every binary split bisects one
coordinate interval at its rational midpoint. The stored leaf paths
must be a complete, prefix-free binary partition; a recursive verifier
checks both children at every interior node and forbids overlapping
leaves. Splitting an inconclusive cell preserves coverage. The union
of accepted and pending leaves is checked after each step. Only an
empty pending set with all stored accepted lower bounds nonnegative
establishes the whole rectangle and hence every point of R^2. The map
(t,z) covers every radial and angular value, and continuity supplies
the origin. The endpoint at infinity is a compactification check, not
a finite radial cutoff.

## Calibration, interpretation, and independent review

Before accepting a new construction, compare all rational cleared-field
identities with the raw generator recurrence and the separate Cartesian
Taylor evaluator. For the unscaled 007 reference, compare the cleared
polynomial coefficients with its previously accepted construction when
D=1. This tests the new denominator bookkeeping without replacing the
analytic proof. The shared Bernstein helpers were independently accepted
for the unscaled reference; their exact source hashes are dependencies.

If a candidate also has an independently certified complete Hessian
commutator upper bound kappa, the signed low-space rate under the domain
hypotheses of ../gradient_commutator/PROOF.md is at least c+1-tau-kappa.
This implication is conditional on both certificates and that theorem.
It does not create a high-space inverse, a nonlinear closure, or a new
candidate/ball verdict. In particular, an existing necessary-distance
exclusion remains valid. Own new scaled calculations remain OPEN until
an independent lane reviews the complete construction and cover.

## Evidence

Exact coefficients remain in JSON, and large cleared polynomial tables
are compressed JSON under data/. Code and verification are separate.
The preparation record binds this proof before implementation. Every
candidate, helper, prior calibration and output is hash-bound. No foreign
code is executed, and no Lean build, server, JavaScript, remote compute,
spatial quadrature, or uncertified mesh maximum enters the proof.
