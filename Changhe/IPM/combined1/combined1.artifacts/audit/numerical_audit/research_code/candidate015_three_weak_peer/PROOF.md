# Candidate015: independent comparison of three complete weak tests

## Exact statement and hypotheses

Let c=4076476460239181/2251799813685248 and let rho_bar and its canonical
IPM velocity u_bar be defined by immutable candidate015, raw SHA256
d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae.
Set F=(cX+u_bar).grad rho_bar-rho_bar. The exact generator convention,
full fields and whole-plane integral algorithm are given in
../scaled_factored_weak/PROOF.md. This note compares the three probes
(n,K)=(19,600),(23,600),(23,2400), with r=|X|,t=r^2/(1+r^2),
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

## Source linkage, exact checks and retained limitations

The frozen source manifest binds the complete015 N3 probe output and the
three code files whose hashes that output records. Current e2norms,
legqs_integrals and general_probe imports are frozen separately as
explanatory text. Historical import versions and the deleted015 F cache
are not observed. No foreign program is executed. The own source-bound
whole-plane computations in N4-237 and N4-239 independently supply every
I, M and C. Bind each own result and all seventeen declared inputs before
finite arithmetic and require all hashes unchanged afterward.

For each of the three rows check the exact candidate raw identity, c,
monomial coefficient1, angular mode, endpoint conditions, all-background
flag, direct/parts agreement and previously checked critical-point cap.
Require each wider printed peer I,M,C ball to strictly contain the own
100-digit ball. Independently compute rational(3). The peer H_upper is
a printed upper endpoint, so verify it lies above(3) by a positive amount
less than10^-300, rather than requiring overlap. Recompute both roots in(2)
using the own containing moments and the coarse or sharper cap. Check
peer-root overlap, positivity and exact directed terminating-decimal
floors. The own root has a lower containing endpoint, which justifies
any strictly smaller rational floor. The exact scalar monotonicity shows
the sharper cap gives a larger root; report the actual relative change
rather than the peer source's unverified generic1e-5 approximation.

The peer code's generic Bernstein label is not the method of these three
monomial rows; their individual source fields identify the closed cap.
Its note saying distance from F is inaccurate: equation(1) bounds the
L2 correction from the reference density rho_bar. Neither wording error
changes the source-bound integral comparison. Quantify rather than assume
the effect of replacing the sharp H by the coarse H.

The(19,600) and(23,600) sharper roots were independently accepted in
N4-241 and N4-245. The(23,2400) own integral was OPEN for candidate-level
reproduction in N4-239. Comparing its complete own moments with the
independent N3 construction supplies that second numerical construction
if every test passes; no additional integration is claimed by this
finite comparison. The monomial gradient proof is candidate-independent.
The four other015 N3 probes and the own first-mode6144 result remain
outside this acceptance. No maximum over probes, full residual norm,
Hdot^-1 value, inverse, dyadic implication or existence follows. The
conditional distance uses real S1 L2 corrections, fixed c, canonical
velocity and the complete cutoff hypotheses already stated above.

The proof was written before the new checker. Its computation and
historical-source limitations are recorded in immutable JSON. A success
accepts containing intervals at the displayed precision, not every
internal peer1024-bit endpoint.
