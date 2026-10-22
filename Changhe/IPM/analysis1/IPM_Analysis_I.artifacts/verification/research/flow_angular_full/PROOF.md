# Complete finite angular audit for the frozen flow certificate

Status: proof and verification design before new code. The full numerical
claim is OPEN until complete execution, independent output audit and review.
This result concerns the frozen angular source, not the radial fields or a
full-flow or stationary-profile theorem.

## 1. Statement, inputs and exact meanings

Let n=1,...,261. For theta in[0,pi/2] define the trigonometric polynomials

 c_n(theta)=cos(2n theta),
 C_n(theta)=1+cos(2n theta)+2 sum_(j=1)^(n-1)cos(2j theta),
 S_n(theta)=(-1)^(n-1)[1+(-1)^n cos(2n theta)
                            +2 sum_(j=1)^(n-1)(-1)^j cos(2j theta)]. (1)

The exact angular cells are

 [l*pi/51200,r*pi/51200], r-l=128/2^d, d=0,...,7,
 l a nonnegative multiple of r-l, 0<=l<r<=25600.                  (2)

There are 200 sum_(d=0)^7 2^d=51000 cells. Each has exact center
(l+r)pi/102400 and half-width (r-l)pi/102400. The finite geometry,
source cache keys and half-width remainder expressions were checked in
flow_angular (topic73), but its center coefficient checks covered only221
cells. The present full audit must check all51000 cells, including those
221, with no sampling claim replacing the remaining centers.

The frozen source is flow_certificate/evidence/source/cert_flow.py,
SHA256 bb47a2d7a46807b02c0e943d7b50d31fb31b6a42c4be55fdbbf1c3a2b90031f6,
with its pinned cert_resid.py and midrad.py dependencies. The actual
floating midpoint/radius boxes returned by AngCache.factors are the
untrusted candidate enclosures being checked. For each cell, all
3 families times3 Taylor coefficients times261 modes, a total2349boxes,
must independently contain the exact coefficients

 f(theta0), f'(theta0), f''(theta0)/2.                            (3)

No assertion about the source's arithmetic alone is used in place of
these checks. Every binary64 midpoint/radius is treated as an exact dyadic.
The exact finite trigonometric values are enclosed by independently
implemented Arb512 even-frequency sums and mpmath.iv180 angular recurrences.
A fresh Arb1536 complex recurrence must then recheck every full-run row.

The claim also covers the source's four endpoint trigonometric intervals,
cos/sin at each endpoint, its a_lo and b_hi outward angle bounds, and its
outward half-width d. Those seven geometric outputs per cell are checked
against both independent interval engines. The old cache keys and integer
node identities are rechecked in the actual source128 construction.

If all these checks and the documented third-derivative remainder checks
pass, every such angular Taylor box and geometric interval is valid for
the stated exact cell. This is a finite, conditional-on-execution claim.
It does not assert any radial coefficient membership, floating matrix
multiplication model, complete cell classification or global dynamics.

## 2. Independent derivation of the angular identities

For 0<theta<pi/2, telescoping the sine addition identity gives
sin(2n theta)/sin theta=2 sum_(j=0)^(n-1)cos((2j+1)theta).
Multiplication by cos theta gives C_n in(1). The alternating telescoping
identity gives tan theta sin(2n theta)=S_n in(1). Both identities extend
to the closed interval because the right sides are finite trigonometric
polynomials. No quotient by zero is evaluated on an axis.

If the canonical stream is psi=sum_n psi_n(r)sin(2n theta), put
P_n=2n psi_n/r^2 and R_n=psi_n'/r. The convention
U=(-psi_y,psi_x) gives U_r=-psi_theta/r and U_theta=psi_r.
Rotating into Cartesian coordinates and dividing by the explicit x or y
factor gives the continuous extensions

 X.(c_l X+U)/r^2=c_l-sum_n P_n c_n,
 (c_l y+U_2)/y=c_l-sum_n P_n c_n+sum_n R_n C_n,
 (c_l x+U_1)/x=c_l-sum_n P_n c_n-sum_n R_n S_n.                   (4)

This shows exactly which angular coefficients enter the source. It does
not enclose P_n or R_n.

Differentiating(1), write for each n the three coefficients

 v_n=(cos(2n theta0), -2n sin(2n theta0), -2n^2 cos(2n theta0)).

The C vector is (1,0,0)+v_n+2 sum_(j<n)v_j. The S vector is
(-1)^(n-1)[(1,0,0)+(-1)^n v_n+2 sum_(j<n)(-1)^j v_j].           (5)

For the second implementation, start c_0=1,s_0=0 and use
c_(n+1)=c_n cos(2theta0)-s_n sin(2theta0),
s_(n+1)=s_n cos(2theta0)+c_n sin(2theta0).
Addition formulas prove the exact recurrence by induction. Evaluating it
with outward intervals encloses every sine and cosine, including all
rounding and dependency growth. Substitution into(5) gives independently
enclosed vectors. The third auditor obtains these sines/cosines by powers
of exp(2i theta0) in complex Arb balls at1536bits. None of the independent
methods uses the source's odd-frequency product formulas.

## 3. Remainders on whole angular cells

For c_n, sup|c_n'''|<=(2n)^3. The product representations of C_n and S_n
in the telescoping derivation and Leibniz's rule give

 sup|C_n'''|, sup|S_n'''|
 <=2 sum_(j=0)^(n-1)[1+3(2j+1)+3(2j+1)^2+(2j+1)^3]
 =16 sum_(j=1)^n j^3=4n^2(n+1)^2.                              (6)

The source uses the larger integer 4n^4+8n^3+6n^2+2n.
Taylor's theorem on the closed interval therefore bounds the remainder
by this integer times d^3/6, where d is any outward half-width.
Every distinct actual binary64 d in the finite tree is checked against
its exact half-width, and the actual source remainder array is checked
by exact Fraction arithmetic against M_source(n)d^3/6. The C and S
remainder arrays must agree bitwise. Every repeated remainder array is
compared with its checked exact-dyadic representative, so no unverified
floating power formula or generic libm error estimate is assumed.

The old tree has eight distinct exported widths. The new run verifies
that precise finite set, rather than treating the number eight as a
general floating-arithmetic theorem. There are eight times two families
times261=4176 distinct exact remainder inequalities. The same tables are
compared for all51000 source outputs.

## 4. Exact source geometry, cache and bounded storage

The source128 base endpoints are obtained as (pi/2)*i/200 and
(pi/2)*(i+1)/200. Bisection replaces(a,b) by(a,(a+b)/2) and
((a+b)/2,b) at source precision128. In the primary run a depth-first
construction reproduces the original source arithmetic. Its integer
(l,r,d) records and four-number cache keys must match every row of the
frozen73geometry archive. The freshly reconstructed exact mathematical
endpoints must belong to the emitted source interval bounds.

The third auditor reconstructs the same candidate endpoints by starting
at the cell's base interval and following its finite left/right ancestry
from the bits of l inside that base. This is a different enumeration of
the same finite arithmetic path, which is checked against the saved
node/key identities. All cache keys in the full finite tree are unique,
as already independently checked in73 and rechecked here. Clearing the
source cache after each emitted cell affects storage only: factors is a
pure function of the endpoint balls when its key is absent, and no later
cell can require a different mathematical value for the same key.

Storing all midpoint/radius arrays would require about1.92GB. Instead the
checker processes one cell at a time. Each cell's exact binary64 arrays,
remainder arrays and endpoint fields are serialized in an explicit
little-endian order and hashed. The row record stores that hash, exact
node identity and completed check counts. A deterministic small set of
coefficient boxes is retained as hex witnesses. A chained hash covers
the ordered row records; code, dependency and geometry hashes are pinned
in the header. This is reproducible computation evidence, not a claim
that a hash proves an inequality.

The third auditor regenerates the actual source arrays, requires their
hashes and witnesses to equal each saved row, and independently checks
all2349 coefficient boxes and geometric outputs at1536bits. Thus loss of
the large transient arrays does not prevent complete independent replay.
Every inequality is rerunnable from the frozen source and exact cell.

## 5. Completion and restart requirements

A full completion has exactly51000 distinct rows in the declared order,
119799000 coefficient containments per engine,357000 geometric output
checks per engine,4176 unique exact remainder inequalities, and51000
bitwise remainder-table comparisons. A partial prefix is diagnostic only.
The output auditor reconstructs the exact tree independently, verifies
every row count, source hash, header, chain and footer, and rejects a
truncated, duplicated, reordered or mismatched record. No acceptance
is inferred from a process exit code or progress message alone.

Restart may retain only an authenticated complete prefix. It must reject
a changed source/input/header or mismatched completed row, remove only
an incomplete final JSON line, resume at the next exact cell, and record
that repair. A prior missing or stale summary cannot make a partial
file into a certificate. A finalized full result requires independent
whole-bundle model review and explicit verifier adjudication after all
outputs are current. These are evidentiary requirements in addition to
the analytical proof.

## 6. Scope and dependencies

This result extends only the finite angular membership and endpoint
geometry portions of flow_angular. It reuses that topic's audited
partition and remainder proof while rechecking all numerical coefficients
at every center. It relies on trusted exact Python arithmetic and the
outward arithmetic semantics of Arb/python-flint and mpmath.iv. It makes
no claim that either library is formally verified or that the frozen
source is byte-identical to a historical numerics-lane executable.

Full middle radial Taylor membership, outer and inner radial membership,
mode-product bounds, classification thresholds and full aggregates must
be verified separately. Even complete flow bounds would not establish
the full IPM inverse or any a posteriori endpoint. No new heavy run is
authorized to overlap the existing primary lane computation; full work
must be serialized after the earlier queued tasks.
