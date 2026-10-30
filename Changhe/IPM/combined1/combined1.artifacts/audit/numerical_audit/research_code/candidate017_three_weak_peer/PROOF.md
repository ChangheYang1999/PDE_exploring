# Candidate017: independent comparison of three complete weak tests

## Exact statement and hypotheses

Let c=4076476460239181/2251799813685248 and let rho_bar and its canonical
IPM velocity u_bar be defined by immutable candidate017, raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Set F=(cX+u_bar).grad rho_bar-rho_bar. The exact generator convention,
full fields and whole-plane integral algorithm are given in
../scaled50_factored_weak/PROOF.md. This note compares the three probes
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

## Independent sharp global gradient verification

Write a=2K+1 and b=2K+4. The radial gradient amplitude is
f(t)=t^K(1-t)^2(a-bt). Its derivative factors exactly as

 f'(t)=t^(K-1)(1-t)[Ka-((K+2)a+(K+1)b)t+(K+3)bt^2].

For each stated positive integer K, compute the two roots of this
quadratic with containing Arb balls. Verify the discriminant is positive
and both root balls lie strictly in(0,1). These are all interior critical
points; f vanishes at both endpoints. The angular amplitude
n t^K(1-t)^2 has its only positive interior critical point K/(K+2)
and also vanishes at both endpoints. At fixed radius the full Euclidean
gradient norm is at most the larger absolute amplitude. Therefore an
exact positive rational cap larger than both radial critical values and
the angular critical value bounds the gradient on the whole plane.

The new checker independently performs this elementary quadratic-root
calculation with no imported gradient helper, and requires the result
to lie strictly below the exact sharp cap in each saved own computation.
This justifies both the coarse and sharp roots, without treating the
saved critical-point flags alone as fresh proof of a global bound.

## Source binding and scope

Freeze the completed six-probe N3 record and all three code files whose
hashes it records. Bind the current omitted imports separately as
explanatory source; their historical loaded versions are not observed.
No N3 code or F cache is used by this comparison. The own completed
scaled50_factored_weak computations N4-256,257,259 supply independent
whole-plane moments, and every declared own source hash is checked.
For each of the three rows, compare the signed I,M,C intervals, requiring
the wider peer display to contain the own100-digit interval. Recompute
the exact coarse rational cap, check the printed H endpoint direction,
then recompute both quadratic roots and exact strict floors. Rehash the
inputs at the end. No field integration is repeated in this finite step.

This supplies a second complete moment construction for the previously
unreviewed(21,522) diagnostic if all tests pass. It does not make that
probe part of the pre-registered25-probe family. The two registered
higher-K tests were already independently accepted. Three remaining N3
probes are outside this acceptance. Their values, any maximum over
probes, actual homogeneous negative norm, full residual norm, dyadic
statement, inverse or existence are not conclusions here. The source's
generic Bernstein label does not describe these monomial rows; its
phrase distance from F should instead refer to the reference density.
The relative effect of the coarser H is computed, not assumed below1e-5.
All conditional stationary-distance hypotheses above remain essential.
