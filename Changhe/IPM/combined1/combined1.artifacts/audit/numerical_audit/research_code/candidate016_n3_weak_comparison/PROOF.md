# Candidate016: independent comparison of three complete weak tests

## Exact statement and hypotheses

Let c=4076476460239181/2251799813685248 and let rho_bar and its canonical
IPM velocity u_bar be defined by immutable candidate016, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Set F=(cX+u_bar).grad rho_bar-rho_bar. The exact generator convention,
full fields and whole-plane integral algorithm are given in
../scaled_factored_weak/PROOF.md. This note compares the three probes
(n,K)=(21,522),(23,2400),(19,1800), with r=|X|,t=r^2/(1+r^2),
v=1/(1+r^2), and phi=r v^2 t^K sin(n theta).

Suppose rho_bar+h is an exact stationary density at this same c,
h belongs to L2(R2), its velocity increment w is the canonical IPM
operator applied to h, and ||w||_2<=||h||_2. Require the regularity,
distributional pairing and cutoff-limit hypotheses stated in the
accepted weak inequality: all pairings below are defined and integration
by parts has no boundary contribution. No change of c, arbitrary
velocity gauge or different realization is included.

Define the complete whole-plane quantities
 I=integral F phi,
 M=|| (2c+1)phi+(cX+u_bar).grad phi ||_2,
 C=||phi grad rho_bar||_(L2(R2;R2)), H=||grad phi||_infinity.
The claim under audit is equality of N3's displayed I,M,C intervals to
our independent exact construction and validity of its resulting
coarser quadratic distance floors. An actual containing-interval
claim is accepted only after the comparison checker passes.

## Weak inequality and root

Subtract the equation for rho_bar from that of rho_bar+h:
 F+(cX+u_bar).grad h-h+w.grad rho_bar+w.grad h=0.
Pair with phi and integrate by parts in the transport terms, using
div u_bar=div w=0. The linear
transport pairing is minus h paired with
(2c+1)phi+(cX+u_bar).grad phi. Hence, with r_h=||h||_2,

 |I| <= (M+C)r_h + H r_h^2.                              (1)

The C term follows from Cauchy-Schwarz and ||w||_2<=r_h; the quadratic
term follows from ||grad phi||_infinity||h||_2||w||_2. If Hcap>=H
and |I|>0, the right side is increasing for r_h>=0. Thus

 r_h >= 2|I|/(M+C+sqrt((M+C)^2+4 Hcap |I|)).              (2)

This is a distance from the reference density to a putative exact
density, not a distance from F to that density.

## Independent closed gradient cap used by N3

For our three integer K values, K>=1 and 1<=n<=2K+1. The radial and
angular gradient amplitudes are
 v^2 t^K [(2K+1)-(2K+4)t],  n v^2 t^K.
At each radius, maximizing over theta gives the larger absolute
amplitude, since the squared norm is A^2 sin^2(n theta)+B^2 cos^2(n theta).
For0<=t<=1, the absolute affine factor is at most2K+1, since its
endpoint values are2K+1 and-3 and K>=1. Therefore

 H <= Hcoarse=(2K+1) max_[0,1](1-t)^2 t^K
            =(2K+1) 4 K^K/(K+2)^(K+2).                (3)

The maximum is at t=K/(K+2): the derivative has sign
K-(K+2)t after positive factors are removed, and both endpoint values
are zero. Formula(3) is an exact rational number, independently
evaluated by the checker. The source's global method label mentioning
Bernstein is not the method of these monomial rows; their individual
H_source fields correctly name the closed formula.

Our previous records use sharper, separately verified gradient caps.
For each of the three probes require Hsharp<Hcoarse, recompute(2) with
both choices from our independently computed I,M,C balls, and verify
the sharper root is larger. This completely explains the small
reported distance differences without changing the underlying
pairing or norms. It does not explain unrelated differences between
other inequalities or trial estimates.

## Complete comparison and source linkage

Freeze N3_probe.json with SHA256
e71575779cd09d4c06bb438fdae06b9c1e6b43d63bb99e7263f1db8040a44f82
and the three source files whose hashes it records. Read but never
execute that code. Bind each own earlier complete calculation and all
its declared inputs, including the immutable candidate, endpoint
conditions, exact positive-pole decompositions and gradient certificate.
The(19,1800) and(23,2400) records were independently accepted through
T4-310/311 and N4-253. The additional(21,522) own record is N4-265;
this comparison supplies a separate N3 construction of its I,M,C.

For each probe require the same exact c, raw coefficient hash, angular
mode and monomial coefficient1. Compare the signed pairing, M and C
balls, requiring the wider printed N3 interval to contain the own
100-digit interval. Check the exact rational(3) against the N3 H_upper
ball. Then compare the complete coarser root(2) with its saved N3 radius
ball, and the sharper root with the own saved radius. Preserve every
input hash before and after calculation, and publish the comparisons,
strict terminating-decimal floors and their precise conditional scope.
Finite group construction is not rerun here: it is the already retained
whole-plane own computation, with all source hashes rechecked.

## Scope

This accepts only the three specified complete probes and the conditional
weak inequality. It does not reproduce N3's frozen n1/n7 vectors, first
mode2048, individual1024-bit internal endpoints, modewise Hardy table,
full norms or seven dyadic cells. None of these three probes is an
estimate of a maximum over all probes. The two registered high-K probes
already exclude the registered graded box at016, so no new campaign
verdict is needed. Historical provenance and analytic objective-span
independence remain exactly as in the retained earlier audits.

## Endpoint serialization correction, 2026-10-29T12:34Z

The first comparison failed because its proposed overlap assertion read
H_upper as a ball enclosing the exact rational formula. Inspection of
the frozen source shows that H_upper is the printed upper endpoint of
that ball. It is therefore above the exact formula, rather than required
to overlap it. The repaired assertion proves Hcoarse < lower(H_upper)
and upper(H_upper)-Hcoarse < 10^-300. Both are directed interval tests.
This proves that the printed value is an admissible upper bound and
agrees to the stated absolute tolerance. The root computation uses the
exact rational Hcoarse, as the source's internal ball formula does.
The 30-digit root comparison, rather than reproduction of its internal
1024-bit endpoint, remains the claim. The failed checker and original
proof are retained, and no successful result existed before this repair.
