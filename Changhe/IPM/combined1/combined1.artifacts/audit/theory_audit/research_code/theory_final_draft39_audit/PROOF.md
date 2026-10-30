# Independent audit of THEORY_FINAL draft 39

## Object and hypotheses retained

This audit concerns the frozen 1897-line draft39 saved at13:47Z on
29 October2026, SHA256
28f5f6ce4bd47463335e8b76b07bdfb53a1c6445bd9e1f0552a81dbb1ae5b97b.
The accepted preceding draft38 has SHA256
ccaa8623477ffdffbb977e866e669cffc9546a657eade246d053941ea0162a02.
All88 changed-word blocks in the352-line comparison were read.
Whitespace-only changes are ignored. Unseen later edits are outside scope.

The unchanged analytic results retain the exact domains and hypotheses
in the standalone source/draft38_PROOF.md and its named predecessors.
In the scalar chart J=(1-Delta)^(1/2), c is fixed, c[h]=0,
omega=(1+4r^2)^(2/5), and

 X_(s,w)(h)^2=||omega D^2 J^s h||_2^2
                +w1||D J^s h||_2^2+w2||J^s h||_2^2.

All norms use Lebesgue measure on R2 and the ordered Cartesian Hessian.
The canonical velocity includes the local/contact contribution. The
leading far-field angular profile and exponent are fixed. A scaling
direction with a nonintegrable leading tail is not a direction of this
L2 chart. The numerical rate does not provide the missing reference
coercivity hypotheses, a closed operator realization, a high inverse
or the nonlinear estimates required by the conditional existence theorem.
The decaying-weight dyadic result retains the origin slope, strain,
partition and absorption hypotheses of T4-442 section2. No L2 distance
lower bound transfers to it without a separate norm comparison.

## 1. Unchanged conditional arithmetic and new distance entries

For sharpw use mu=97/250, C=397, s=1/5184, cU=8/5, w2=1048576,
r=1351/10^6, eta=4207/20000000 and betaL=2. The high rate equals

 mu-C*s-cU*r/sqrt(s)=63092119/405000000>1557/10000.

Thus r-eta/(1557/10000)=7/1557000000>0, the inverse rate is below
6.4226 and r/(2*betaL*sqrt(pi*s*(1+s)))<0.0137200. These exact
conditional inequalities are recomputed without asserting their missing
analytic premises. The necessary scalar family ceiling is

 b_w=(2mu/3)*sqrt(mu/(3C))/(cU*sqrt(w2))<2.8496e-6.

The table uses the conservative exact ceilings3.7930e-6,2.8496e-6
and25/54684 for TB-sharp, sharpw and the original graded family.
If every admissible correction has distance D>d and a family permits
radius at most b, then d/b>q implies D/b>q. This proves the factor
comparison used in all22 numeric table rows. It compares certified
lower bounds, not actual distances of different candidates.

For025 the accepted full weak probe(n,K)=(19,1800) gives
D>0.002065801265578052. For026 it gives
D>0.001355907204057457. The separate proofs frozen here require a real
S1 L2 correction, a weak stationary equation at fixed c, the canonical
divergence-free velocity with ||U[h]||_2<=||h||_2, and locally integrable
weak products. The smooth background growth and decaying probe justify
the full-plane cutoff limit. In their notation subtraction gives

 |I|<=(M+C)||h||_2+Hbar||h||_2^2.

Solving the nonnegative quadratic yields the displayed strict floors
from the already accepted containing moment enclosures. This audit binds
those results; it does not repeat the spatial integrations. Both floors
exceed every registered scalar and original graded ceiling. Candidate026
has been independently reproduced in T4-446 to450 since the draft's
stated T4-445 cutoff. Its dyadic status remains separate.

The factors above28895 for007,013,014 at the two small Db targets follow
from their already accepted floors0.004769166867,0.00199234339 and
0.00198301351067 divided by1/33554432 or6.8626e-8. All six divisions
are checked exactly. This independent distance argument persists even
where the endpoint certificate with an improved valid coefficient is OPEN.

## 2. Endpoint quantifiers, constants and finite reach

The corrected endpoint statement follows from T4-443 and T4-452,
whose proofs and results are frozen here. Let A be the set of velocity
coefficients valid uniformly on the specified real S1 C1 weighted space,
and Emin=(-q-1)/(2*(-q)*(-q-3)). The test requires E<=K(beta),
whereas E in A implies E>=Emin. Thus K(beta)<Emin excludes every
valid coefficient; the reverse comparison alone constructs none.
The draft now correctly leaves2^-25 and6.8626e-8 OPEN for an improved
valid coefficient. The tested printed radii from3.5125e-7 up are excluded
for this certificate, and2^-23 is excluded when V>=|U_lead(0)| is retained.
These are limitations of this sufficient CI certificate, not nonexistence.

The floor min(1.747261,lambda*(5/r)^delta) applies to the current list
of estimates. For c=4076476460239181/2251799813685248, q=1/c-4,
delta=1-1/c, lambda=1/2+5*2^(1-q), the T4-443 split-integral formula
bounds the full current-list CI value by2.66323e-8<2^-25. The constant
coefficient bounds are1.66122e-8 and1.89061e-9. The older9.28e-11
bound used the historical upper-estimate formula with coefficient
133.004... . Replacing that derivation with a weaker bound does not
refute the possibility that the full current value is smaller.

The normalized R1-038 condition is

 E*sqrt(2*pi)*Hmax/B<Emax(beta),
 Emax(beta)=D*(B/(beta*sqrt(alpha)))^(delta/(-q-1))/g0,
 D=5c-1, alpha=-2q-2.

At25/54684, Emax<7.9417; at the exact graded ceiling
50/(651*sqrt(28248)), Emax>7.942167. With Hmax>=999745,
the unnormalized cutoff for E is below0.2694533 even at the exact
graded ceiling, as independently checked in T4-452. Both versions of
the obstruction remain valid. Section0's shortened phrase about
"E below7.9417" should display the normalized expression above to
match section3.4. The shorter statement is a weaker necessary condition
under the known budget, not a refuted nonexistence assertion.

The repaired lambda value109.602422548... is strictly above109.6024.
The remainder lower bound is lambda*H*(5/r)^delta forr>=max(L0,5)
and lambda*H forL0<=r<5. Consequently it exceeds2.74*H throughout
the stated interval ending at18860. The corrected two-mode projection
lower bound is13.75867597, below the enclosing projected norm and below
the previously upward-rounded13.758676. The FLOAT exponent near1.05
is restricted to its replacement-tail model, not every stationary estimate.

## 3. The new016 sufficient forcing assertion

T4-451 independently proves for F in H1, s>=0 and positive weights

 X_(s,w)(F)>sqrt(w1*ell1^2+w2*ell0^2)

from strict lower endpoints ell0<||F||_2 and ell1<||DF||_2.
Unitary Plancherel gives each unweighted Bessel comparison; dropping
the nonnegative Hessian and optional negative-norm entries finishes
the proof, allowing infinite norms. The accepted N3/N4 H1 enclosures
of the exact016 residual imply failure of all ten registered sufficient
scalar forcing tests. No P2, actual homogeneous negative norm or
fractional upper bound is used. The draft labels this a failed sufficient
condition correctly. Cite T4-451 alongside N4-374 in the next version.
This does not order the016 and007 actual norms or distances.

## Publication updates and verdict

1. Replace all current026 "OPEN/reproduction OPEN/none certified" entries
by the independent446-450 result, with the fixed-c scalar/original graded
scope. Add its downward-rounded table ratios357.4,475.8,2.965 and point
gaps. Extend the scalar/original graded summary through026 except011.
The present026 row also conflicts with the following unqualified
"every listed candidate" sentence. Keep011 and the dyadic list explicit.
2. Mark the016 forcing test independently audited through451. In the
outstanding-components list, distinguish accepted G0,rF,G1 from the
remaining P2 and actual homogeneous negative norm. Do not call the
whole set unaccepted or interpret a failed sufficient test as an exclusion.
3. In section0 display the normalized R1-038 condition above. Where the
T4-425 no-radius-dependent-use statement is summarized without targets,
name its four original targets or cite443 for the larger registered-target
scope. It does not rule out every improved coefficient at the two small Db
targets. State the basis for a current status separately from historical
matrix versions, which remain historical evidence.

CONFIRMED: all changed conditional mathematics within these hypotheses,
all22 numeric table rows, the six small-Db distance ratios, the repaired
endpoint quantifiers and the016 sufficient-forcing assertion. REFUTED
as current status: the026 reproduction is OPEN or no026 bound is
certified. OPEN: every unprovided inverse, candidate hypothesis and
stationary-only improvement. No exact profile or existence closure has
been proved. These checks execute no peer program and repeat no large
moment integral.
