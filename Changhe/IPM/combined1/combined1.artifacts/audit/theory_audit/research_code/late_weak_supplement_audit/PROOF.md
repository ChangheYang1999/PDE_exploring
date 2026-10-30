# Audit of six supplemental weak tests for candidates 015 and 017

Written at 2026-10-29T14:46:41.074419+00:00, before the finite checker.

## Exact statement and source scope

Let c=4076476460239181/2251799813685248 and gamma=1/c. Let rho be
one of the immutable references C1-N1-015-pairQ-quot013 or
C1-N1-017-legqs50-quot013, with raw SHA256 respectively
 d7759bbaa98fb5d686c8f88af4ec6b9ddd96e457acc2d9166924c5c729ee8eae
and
 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Their canonical potential fields are rho=-partial_y Delta chi and
u=(-chi_xyy,chi_xxy). These are smooth, div u=0, and their differentiated
finite-generator asymptotics give |rho|+|u|=O(r^gamma) and
|grad rho|=O(r^(gamma-1)). These reference properties are imported from
the previously accepted exact snapshot and generator audits. This audit
does not repeat their field construction or full-plane integrations.

Lebesgue L2 is on R2 and uses the Euclidean vector norm. Define U[h]
by its Fourier symbol (xi1 xi2/|xi|^2,-xi1^2/|xi|^2), with any value at
xi=0. This gives a real divergence-free L2 vector with norm at most
||h||2. Suppose h is real, S1 symmetric, and in L2, and satisfies the
fixed-c distributional stationary correction equation

 F + div((cX+u)h) -(2c+1)h + U[h].grad rho + div(h U[h])=0,
 F=(cX+u).grad rho-rho.                                      (1)

No derivative or point trace of h is required. The theorem applies in
particular to a more regular normalized subset, but does not evaluate
c[h] at L2 regularity. At regularity where it exists that functional has
its canonical local/contact term. No normalization or scaling mode is
silently removed. A changed c requires a separate exponent-pinning
argument and is outside this application.

For each of the six probe rows in data/rows.json, equations (2)-(5)
below and the accepted whole-plane moment intervals imply the stated
strict lower bound for ||h||2. In particular, candidate 015 at (23,2400)
has

 ||h||2 > 758369800173081/250000000000000000
         = 0.003033479200692324.                              (2)

The other five exact floors are recorded in the JSON. This is a
necessary distance from the reference density rho. It is neither a
distance from F nor an upper distance to an existing solution.

## Complete weak identity

For positive odd n and integer K >= (n-1)/2, put

 t=r^2/(1+r^2), v=1-t, phi=r v^2 t^K sin(n theta),
 Mfield=(2c+1)phi+(cX+u).grad phi,
 I=int F phi, M=||Mfield||2, C=||phi grad rho||2.

The numerator of phi is the homogeneous harmonic polynomial
Im(x+iy)^n times (r^2)^((2K+1-n)/2), so phi is smooth at the origin.
It and its gradient decay as r^-3 and r^-4 at infinity. The growth
hypotheses ensure every displayed reference integral is finite.

Test (1) against a compact radial cutoff of phi. Integration by parts
in the first and last divergence terms and Cauchy-Schwarz give

 |I| <= (M+C)m + Hbar m^2, m=||h||2, Hbar>=||grad phi||infinity. (3)

The linear cutoff errors vanish by the L2 tails and the decay of
phi and grad phi. The quadratic error vanishes since h U[h] is L1 and
the cutoff derivative times phi tends uniformly to zero on its
escaping annulus. This justifies the same identity for the full probe.
It also proves I=-int rho Mfield, checked independently by the
production integrations. There is no derivative loss in (3).

For positive I0<=|I| and Dbar>=M+C, (3) implies

 m >= 2 I0/(Dbar+sqrt(Dbar^2+4 Hbar I0)).                     (4)

This root is increasing in I0 and decreasing in Dbar and Hbar. A
strict rational number below its containing interval is a strict
necessary floor. The finite checker uses containing intervals for
|I|, M and C and compares every requested floor by directed arithmetic.
It also verifies I_lower-D_upper*f-Hbar*f^2>0 directly for each floor f,
which avoids relying on a rounded square-root display.

## Global gradient, including all critical points

Set A=2K+1 and B=2K+4. The radial and angular gradient amplitudes are

 f(t)=t^K(1-t)^2(A-Bt), g(t)=n t^K(1-t)^2.

At fixed t, the supremum over theta of the gradient norm is
max(|f(t)|,g(t)): its squared norm is f^2 sin^2(n theta)+g^2 cos^2(n theta).
All six rows have K>0, so both amplitudes vanish at both endpoints.
The angular amplitude reaches its maximum at t=K/(K+2). Division of
f' by t^(K-1)(1-t) gives the exact quadratic

 B(K+3)t^2-[(K+2)A+(K+1)B]t+KA.                            (5)

The checker verifies the coefficient identity independently, encloses
both roots, confirms both lie strictly in (0,1), and bounds |f| at both
roots and g at its sole critical point by the stored exact Hsharp.
Zeros of f cannot be positive maxima of |f|. This supplies the global
cap without a grid, truncation, or candidate-dependent transfer.

For the coarse cap, |A-Bt|<=A when K>=1, and n<=A. The maximum of
t^K(1-t)^2 is 4 K^K/(K+2)^(K+2). Therefore

 Hcoarse=4(2K+1) K^K/(K+2)^(K+2)

is valid for every listed row. It is a closed monomial bound, not a
Bernstein certificate. The accepted N3 displayed upper values are checked to lie strictly
above this exact number as outward upper approximations. The checker
recomputes both roots using the same accepted I,M,C. If R denotes
(4) with the true I and D, implicit differentiation of
D R+H R^2=I gives dR/dH=-R^2/(D+2HR)<0. All six containing relative
changes (Rsharp-Rcoarse)/Rsharp are strictly above 10^-5. Thus the
generic smaller-than-10^-5 source sentence is false for these rows.
These wording corrections do not invalidate either necessary floor.

## Provenance, dependencies and limitations

The frozen N4-383 and N4-384 comparison results bind three separate
production calculations apiece. This audit checks their original
source hashes, candidate identities, complete-field flags, I/M/C
containment in the independent N3 displays, both identities for I,
global caps, root monotonicity and strict rational floors. Direct
input paths were rehashed at the preparation time recorded in
external_bindings.json. Those large shared dependencies are not
copied again; the original accepted production remains responsible
for the integrations. This finite audit is not a third independent
field integration. It runs no foreign code.

The N3 historical F cache is missing and some historical imported
module versions cannot be observed. The independent N4 physical
construction supplies the source-to-moment link; present-day source
hashes are not asserted to recover missing historical execution.

The (21,522) result for 017 remains a diagnostic outside the public
25-probe family. Four other N3 probes for 015, three other N3 probes
for 017, and the separate first-mode 6144 calculation remain outside
this acceptance. A maximum over unaccepted probes is not certified.
No dyadic implication or ranking of full residual norms follows.
The stronger 015 floor reinforces its existing scalar and original
graded ball exclusions. Their precise family scopes remain those of
T4-459, which is frozen as a dependency. No new existence or inverse
claim is made.
