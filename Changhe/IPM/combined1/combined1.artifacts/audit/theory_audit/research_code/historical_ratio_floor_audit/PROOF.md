# Exact audit of historical distance-ratio floors

## Statement, dependencies and scope

The frozen T2 ratio report claims that all 15 entries in section 5 of
The T2 final summary are floors at their displayed unit, while 13 of 18
entries in handoff O3 and 8 of 12 in REVIEW_T4ALT C4 exceed the corresponding
exact-ceiling quotient. It also claims that replacing those entries by
their correct floors preserves every ratio-above-one conclusion.
This audit proves these finite arithmetic statements from the exact
reported distance floors and the independently proved family suprema of
T4-454. It does not repeat the distance certificates or the analytic
family-ceiling proofs.

For PDE applications retain their hypotheses: a real S1 L2 correction
at fixed c, the canonical velocity including its local/contact term,
the weak stationary equation and the integrability and cutoff conditions
of the accepted distance certificate. Scalar norms must dominate
sqrt(w2)||h||2 and obey their positive-rate constraint. The original
graded norm uses its separately proved L2 embedding. The claims here
have no implication for a decaying-weight dyadic norm without such an
embedding, for a changed tail chart, or for an unrestricted solution.

All distances and parameters are exact rationals in data/parameters.json
or parsed from the frozen tables. The T4-454 result gives exact positive
rational squares q=b^2 for the six relevant family suprema. The graded
square is q=625/2992882662. The hash-bound standalone proof
source/brackets_PROOF.md proves these values. All source references
and copies are registered in data/input_sources.json and the manifest.
The historical peer report's summary and handoff hashes differ from the
current frozen reports because those files have later additions. This
audit checks the actual frozen rows and reports those changed hashes
rather than asserting an unobserved historical identity.

## Exact floor argument

Suppose d>0 is a proved strict distance floor and b>0 an exact supremum.
Let u>0 be the place value of the displayed final decimal digit. The
correct directed display is k*u where k=floor(d/(b*u)). Put

 t = d^2/(q*u^2),  q=b^2.

As all factors are nonnegative,

 k^2 <= t < (k+1)^2

is equivalent to k*u <= d/b < (k+1)*u. In exact integer arithmetic,
k=isqrt(floor(t)) has this property. The checker verifies both rational
square comparisons explicitly. No floating-point approximation, midpoint
estimate, iteration tolerance or guessed number of digits is used.
A positive printed p is a lower bound on this quotient exactly when
p^2*q <= d^2. A valid quotient floor k*u>1 therefore proves d>b, and
any correction of actual distance D>d lies outside every ball with
admissible L2 radius at most b.

For the summary table the denominator is instead a displayed rational
upper budget B>=b. Direct rational division gives floor(d/(B*u))*u.
Since d/B<=d/b, its floor is conservative for the exact supremum as
well. The three comparisons B^2>q are checked exactly. A quotient floor
is not an ordering of actual correction distances: different unknown
D's may exceed their floors by different amounts.

## Application to the three tables

Parse the five summary rows 007,005,008,d2,Mpen2 and their three budget
columns. All 15 displayed values equal their rational floors. In
particular d2/sharpw has floor 1.03e5 at unit 1000, whereas the historical
1.04e5 exceeds 0.29552675/(2.8496e-6). This corrects that numerical lower
factor without affecting exclusion.

Parse the six O3 rows and three distances, then the six C4 rows and two
distances. Match them to the six exact family squares in their stated
order. The square comparison proves that 13 O3 entries and 8 C4 entries
are not lower bounds. Each offending value exceeds its correct floor
by exactly one displayed unit. All 30 correct floors exceed one.
The complete exact-square witnesses, corrected floors and offending
entries are written to verification/result.json. These are independent
checks of T2's arithmetic report, using integer square roots rather than
its Arb midpoint-based starting estimate.

The statement being corrected is the interpretation of those printed
numbers as conservative lower factors. Their use as rounded approximations
would need an explicit approximation label. No historical certified
ball exclusion is withdrawn: the corrected lower factors still exceed
one, subject to the same accepted PDE and embedding hypotheses.

## Verdict

CONFIRMED are T2's counts, the corrected 1.03e5 summary entry, the exact
replacement floors and preservation of ratio-above-one conclusions.
REFUTED is the interpretation of the 21 identified historical entries
as conservative quotient lower bounds. No existence, inverse, actual
norm ordering or new spatial-integral result follows. This informal
argument was written and checked before implementing its finite checker.
