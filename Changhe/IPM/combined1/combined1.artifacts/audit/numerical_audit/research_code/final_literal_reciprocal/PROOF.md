# Reciprocal audit of the final origin and FLOAT presentation findings

## Statements and dependencies

Fix the exact potential of C1-N1-007-d2w-j7-e2bal, raw SHA256
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21,
and c=4076476460239181/2251799813685248. On the plane put
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho. Taylor coefficients have no factorial scaling.
The quotient R_f=F/y is real analytic near the origin by parity.

The exact constant of R_f is zero. Each of its five nonconstant
coefficients of degrees two and four has absolute value above 2e-13.
Their strict rational enclosures are the five explicitly registered
pairs in source/T4_490_parameters.json, bound by the source manifest.
This accepts T4-490, including the N4-419 axis counterexample, at the
saved exact coefficients. It says nothing about an earlier optimizer
projection, and changes no center, tail, distance or existence verdict.

A separate finite statement accepts T4-492's recomposition of N4-420:
all 600 rounded source-data displays, all 200 exact ratios and all
25 stage-comparison ratios agree. These quantities are interpretations
of serialized FLOAT data, without an error bound for any PDE pairing.
The six original scope findings retain N4-420's restrictions. Later
report repairs are governed by N4-422 and any successor audit, not by
an acceptance of the old frozen report's wording.

## Complete finite jet argument

Let z=x^2+y^2, t=z/(1+z), gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2 and H_m=Re(x+iy)^(2m). Every saved generator
is a rational multiple of H_m (1+z)^(p_j-m) times either t^w or
 t^w P_n(2t-1).
The shifted Legendre coefficient at t^h is
(-1)^(n-h) binom(n,h) binom(n+h,h). Thus the term with radial indices
h,ell contributes

 a (-1)^(n-h) binom(n,h) binom(n+h,h)
   binom(p_j-m-w-h,ell) H_m z^(w+h+ell).

For a monomial there is just h=0 and Legendre coefficient one. Retain
exactly m+w+h+ell<=4. Expand H_m and the integer power of z by their
finite binomial formulas. Ordinary Cartesian differentiation of this
rational polynomial gives rho and both components of u. Differentiate
each monomial by its falling factorial and multiply by exact coefficient
convolution to obtain F through degree five. Independently check the
harmonic identity Delta(H_m z^s)=4s(2m+s)H_m z^(s-1) on every term.

The omitted potential terms have degree at least ten. Their third
derivatives have degree at least seven. By parity the nonzero density
and velocity start at degree one, so a product involving any omitted
contribution to u.grad rho has degree at least seven. Drift and density
terms preserve this cutoff. The computed F jet through degree five is
therefore exact. Division by y gives precisely the requested quotient
jet through degree four. No numerical Taylor remainder is required.

Compare every rational Cartesian coefficient, all five directed
intervals and the zero center relation with T4-490's saved record.
Also compare every axis coefficient with the independently accepted
N4-419 record. Exact enumeration over all 2982 input generators proves
that the 60 relevant generators and their 140 radial terms are complete.
Strict rational comparison with 2e-13 proves each tolerance failure.

## Presentation arithmetic and source integrity

For a printed decimal d whose final place is u, nearest-place agreement
with an exact serialized number q means 2|q-d|<=u. Reapply this inequality
to every N4-420 operand and factor, and compare T4-492's full ordered
ratio lists and eight extrema/count records with the already accepted
exact N4-420 arrays. Recompute the first-mode and stage extrema by
exhaustive fraction comparison, not by ordering approximate displays.
This accepts a finite arithmetic replay and its stated scope. It does
not rerun quadrature, prove a tail remainder, infer a historical save
time or compare actual correction distances.

Freeze both T4 proofs, programs, results and all direct manifest inputs.
Reuse an existing own-lane copy only after comparing its exact digest;
otherwise copy the immutable peer bytes to this topic. Record the
mapping and each external provenance path separately. Peer programs
are read as text and never executed. Register the standalone proof
before creating the checker, verify all local bindings before and after
execution, and retain any failed version. This audit runs on CPU57 at
nice19 with the sole long worker paused, then resumes only that worker.
Opus collaboration continues through the existing theory lanes; the
configured model is Opus 5.5 and its returned provider identity is not
observable here.
