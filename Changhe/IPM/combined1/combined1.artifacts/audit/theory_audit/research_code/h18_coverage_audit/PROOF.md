# H18 coverage of registered scalar and original graded correction balls

Written at 2026-10-29T14:39:28.265107+00:00, before the finite coverage checker. This is a composition
of previously accepted weak certificates and analytic radius estimates. It
is not a new computation of the candidate integrals.

## Statement and exact scope

Let c0=4076476460239181/2251799813685248. For each immutable snapshot
C1-N1-NNN in data/registry.json, let rho_NNN be its exact stored density
and u_NNN its canonical smooth incompressible velocity. Write
U[h]=(-R1R2 h,R1^2 h), with Fourier symbols Rj=i xi_j/|xi|. L2 denotes
Lebesgue measure on the entire plane. A stationary correction at c0 means
a real h in L2 satisfying

 F+div((c0 X+u_NNN)h)-(2c0+1)h+U[h].grad rho_NNN
                   +div(h U[h])=0                           (1)

in distributions, where F=(c0 X+u_NNN).grad rho_NNN-rho_NNN.
All products are locally integrable and U is a vector L2 contraction.

Subject to the accepted input certificates listed in data/coverage.json,
for every NNN in {002,...,026} except011, every correction (1) has

                  ||h||2 > 1/1000.                          (2)

Consequently these24 references have no stationary correction at c0 in
any of the following balls, for any parameters satisfying the indicated
necessary positive margin:

1. The eight scalar tuples of data/families.json, comprising baseline
   FW-A2-Db, original T4L2, TB-rebal, the two registered bL instances
   beta_L=1 and7/5, sharpw, sharp and TB-sharp. Computed-defect versions
   use the same total correction radius and inherit the same exclusion.
2. Original graded and gradedL2 component boxes, with their original
   top margin m2 below.
3. T4L2-trans and T4L2-statL instances and their parameter choices that
   retain the same top margin and X_s norm. This includes every K_L
   in the registered statL list; no low inverse is asserted to exist.

Candidate001 is treated separately: its accepted non-L2 residual already
makes the L2-forcing schemes inapplicable. The stronger new T4-458 annular
application asserts no stationary L2 correction at any c and any radius,
but remains pending independent Opus review at the time of this writing.
It is not silently converted to a weak-distance certificate. Candidates
011 and027 remain OPEN here. The snapshot registry was frozen at the
actual time in data/registry.json; later snapshots require separate checks.

This statement concerns the exact eight tuples, original graded margins,
and stated transient/stationary extensions. It does not quantify over
arbitrary bL weights or beta_L, improved commutator constants, a new
high-space inverse, generic families with five or more branches, or the
decaying-weight dyadic schemes. It neither proves existence nor ranks the
true distances of different candidates.

## Weak necessary inequality with no derivative loss

For each reference, smooth sublinear asymptotics give rho,u=O(r^gamma)
and grad rho=O(r^(gamma-1)), gamma=1/c0<1. Each accepted probe phi is
smooth, phi=O(r^-3), grad phi=O(r^-4). Put

 I=|int F phi|,
 D>=|| (c0 X+u).grad phi+(2c0+1)phi ||2+||phi grad rho||2,
 H>=||grad phi||infinity.

Testing (1) first with a compactly supported radial cutoff of phi yields

 I <= D m+H m^2,  m=||h||2.                                 (3)

Indeed transport contributes the coefficient (2c0+1)phi after integrating
by parts because div(c0 X+u)=2c0. The other linear term is bounded by
||U[h]||2 ||phi grad rho||2, and the nonlinear divergence term by
||h||2 ||U[h]||2 ||grad phi||infinity. No derivative of h is used.
The cutoff errors vanish: the linear coefficient error on an escaping
annulus is O(r^-3) from c0 X and O(r^(gamma-4)) from u; their L2 norms
tend to zero. The nonlinear coefficient error tends uniformly to zero
and h U[h] is L1. The residual pairing is absolutely convergent, since
F=O(r^gamma) is enough with gamma<1 and phi=O(r^-3). Thus the argument
also applies when only these explicit growth hypotheses, rather than
F in L2, are known. The earlier localized certificates do satisfy their
stated stronger L2 residual hypothesis.

The stored results enclose the signed pairing and the upper coefficients.
If I_- is a lower bound on its absolute value and D_+,H_+ are upper bounds,
then the entirely rational strict test

       I_- - D_+/1000 - H_+/1000000 > 0                     (4)

excludes every m<=1/1000 by monotonicity. All decimal midpoints and errors
are interpreted as exact rational intervals, with no binary floating
conversion. For the old localized probes D is a valid triangle-inequality
upper bound; for newer angular probes D is the sharper M+C. Both satisfy
(3). This check deliberately uses one conservative floor and does not
reoptimize probes or call a tabulated lower bound an actual distance.

## Uniform scalar ceiling

Let a scalar norm X_s dominate sqrt(W2)||h||2, and suppose its radius r
obeys

 mu-C s-cU r/sqrt(s)>0,  s>0.                               (5)

Then ||h||2<=r/sqrt(W2)<sqrt(s)(mu-C s)/(cU sqrt(W2)). The right side
is positive only for s<mu/C. Writing z=sqrt(s), the derivative of
mu z-C z^3 is mu-3C z^2. Its unique positive maximum is at
s=mu/(3C), and the squared L2 supremum is exactly

                 b^2=4 mu^3/(27 C cU^2 W2).                (6)

The checker reads all eight tuples, verifies their positive parameters,
and proves b^2<(3793/1000000000)^2. Hence every admissible scalar ball
has ||h||2<3.7930e-6<1/1000. Restricting s further in a theorem only
shrinks this bound. The weights are fixed by the corresponding norm,
including W2=512^2 in original T4L2 and1024^2 in the two bL instances
and sharpw. For a computed predictor g, the closure radius r is the total
correction h=g+e and must still satisfy(5). A separate error radius for e
does not enlarge the allowable norm of h.

## Original graded and transient/stationary ceilings

For omega=(1+4r^2)^(2/5)>=1, put
P=||omega D^2 J^s h||2, a=||D J^s h||2, b=||J^s h||2,
J=(1-Delta)^(1/2), and ordered Cartesian Hessian norm. The Fourier
identity (1+|xi|^2)^2=1+2|xi|^2+sum_ij xi_i^2 xi_j^2 gives
||h||H^(2+s)^2<=P^2+2a^2+b^2. In a component box P<=r2,a<=r1,b<=r0,
write n^2=r2^2+2r1^2+r0^2. Thus ||h||2<=n.

The original graded top margin is

 m2=1/2-4708s-(217/50+(1049/5)s)n/sqrt(s)>0.                (7)

It implies s<1/9416 and n<(50/217)sqrt(s)(1/2-4708s).
The cubic derivative vanishes at s=1/28248 and its maximum is
1/(3 sqrt(28248)). Therefore

 n<50/(651 sqrt(28248))<25/54684<1/1000.                    (8)

The middle inequality follows from168^2<28248; the last is an exact
integer comparison. This relaxed upper bound need not be attainable,
since a positive term in(7) was discarded. Its squared irrational term
is625/2992882662.

For trans/statL, the same formula(7) uses the total X_s radius R in place
of n. Here X_s^2=P^2+128^2 a^2+512^2 b^2, so ||h||2<=R/512.
Thus every parameter choice with its required m2>0 satisfies
||h||2<25/(54684*512)<3.7930e-6. This is a necessary-condition extension
of the existing fixed-ball comparison, independent of K_L, alpha,
normalization or the low resolvent. Those other hypotheses are still
required to establish an existence theorem, and are not inferred here.

## Normalization, scaling and the separate001 issue

Every normalized correction is a member of the larger L2 class tested
above. For smooth h its constraint is c[h]=partial_y U2[h](0)=0,
with the contact term -h_y(0)/4 in the canonical integral formula.
Equation(3) never evaluates that trace and does not replace its contact
term by an exterior integral. It therefore excludes the normalized
subset without assuming an illegitimate L2 trace. The nonzero growing
scaling mode is outside these L2 correction spaces. The finite weak tests
are fixed at c0; they alone do not exclude changes to c. Such a conclusion
requires a separately accepted far-field pinning result and its exact
hypotheses, or the separate001 annular argument.

For001 the nonzero leading residual at q=2/c0-1>0 fails L2 membership,
so all registered schemes requiring L2 forcing fail at that reference.
A failed forcing hypothesis alone does not prove absence of a solution
in the associated ball. T4-458 supplies a separate annular distributional
argument to obtain that stronger conclusion once independently reviewed.
The H18 coverage table records these two claims with different statuses.

## Source bindings and verification

The frozen closure matrix is version135. The original source manifest
records its hash and its distinct capture time. data/registry.json binds
each immutable ID to an exact raw coefficient hash verified directly
against its registry manifest. Every weak result is copied unmodified;
raw-to-canonical bridges are included when a result uses canonical
coefficients instead of the raw format. For013-015 the local canonical
serialization differs from N4's, so the exact accepted local build is
used rather than comparing unlike canonical hashes. The candidate proof
hash is checked against the result whenever embedded. Accepted review
ledger excerpts are copied with the relevant result hashes retained.

The finite checker validates all27 registry entries, the24 witness
assignments, their strict comparisons(4), the exact eight tuples and
all frozen matrix rows mentioning those snapshots. It also records001,
011 and027 separately. Matrix labels are evidence of team status, not
substitutes for the necessary inequality. This audit reuses accepted
integration certificates, and does not claim a fresh reproduction of
the whole underlying numerical calculation or of every matrix theorem.
