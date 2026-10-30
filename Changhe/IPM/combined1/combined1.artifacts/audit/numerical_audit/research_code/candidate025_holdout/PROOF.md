# Candidate025: three-scale dimension and recorded analytic probe span

## Exact statement and notation

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2 for j=0,...,7, S=1+x^2+y^2,
r=sqrt(x^2+y^2), v=1/S, t=1-v and H_m=Re(x+iy)^(2m).
Let V_old be the accepted1922-dimensional quotient potential space of013,
with its exact ordered basis in the dependency
../optimizer_quotient_audit/PROOF.md. Its radial coefficients, after
factoring v^(-p_j) cos(2m theta), are polynomials in t.
For R in {25,50,100}, define the additional smooth potential

 G_RjmN=H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                         P_N(2r^2/(R^2+r^2)-1),

where P_N is the degree-N Legendre polynomial normalized by P_N(1)=1.
Take N=0,...,11 and the following branch/angular blocks:

* at each R=25,50,100, take j=1,2,3 and m=9,...,15;
* also at R=25, take j=1,m=16,...,19 and j=2,3,m=16,...,23.

The resulting2918 potentials are linearly independent over the reals.
The density map D chi=-partial_y Delta chi is injective on their span.
These dimensions precede the421 recorded constraints and do not assert
a tangent dimension, sampled rank or conditioning bound.

This proof is prepared before the immutable025 snapshot. Its application
to C1-N1-025-combined-heldin1e16 is conditional on the checker binding the
actual raw SHA256 and all2918 ordered shapes. The declared immediate
input is016, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
The declared addition order is radius50 low blocks, radius100 low blocks,
then radius25 high blocks, appended to016's2174 shapes. The finite output
records actual raw and manifest hashes; no unpublished candidate is
certified by this proof alone.

Define phi_(n,K)=r S^(-2) t^K sin(n theta) for odd n>0 and integer
K>=(n-1)/2. The declared025 objective has81 analytic rows: the same67 rows
as016, followed by14 pairs n=19,21,...,31 at K=(n-1)/2+128 and then
K=(n-1)/2+512. The original67 rows are27 first-mode exponents

 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
 768,1024,1536,2048,3072,4096

and40 pairs n=3,5,...,17, K=(n-1)/2+s for s=0,8,32,128,512.
The25 public pairs n in {19,23,25,29,31}, K in
{600,900,1200,1800,2400}, together with21 diagnostic pairs n=19,21,...,31,
K=(n-1)/2+s for s=0,8,32, lie outside the real span of those81 rows.
The14 new rows are design rows and are not held out.

## Potential independence

Angular orthogonality separates cos(2m theta). Within a fixed angular
mode, write a finite relation as sum_j v^(-p_j) Q_j(v)=0, with rational
Q_j analytic near0. The exact eight p_j and their28 pairwise differences
are nonintegers; the finite checker re-establishes all36 conditions.
A nonzero Q_j has an integer vanishing order e_j at0. The leading
exponents e_j-p_j of nonzero summands are pairwise distinct. Divide by
the smallest power of v and send positive v to0. A unique nonzero leading
coefficient remains, a contradiction. Hence each branch vanishes
separately. The same argument separates these branches from an integer
Laurent polynomial, whose leading exponent is integral.

Put a_R=R^2-1 and L_R(v)=1+a_R v. The scaled branch factor is

 A_RmN(v)=R^8 v^4(1-v)^m P_N(2(1-v)/L_R(v)-1)/L_R(v)^4.

Rodrigues' formula gives the leading coefficient of P_N as
2^(-N) binom(2N,N). At the auxiliary pole v_R=-1/a_R, the pole order of
A_RmN is exactly4+N, with nonzero Laurent coefficient

 C_RmN=R^8 v_R^4 binom(2N,N)(1-v_R)^(m+N)/a_R^(4+N).

The three values a_R are624,2499,9999 and are distinct positive integers.
Every other scaled factor is analytic at v_R because
L_Rprime(v_R)=1-a_Rprime/a_R is nonzero. Old polynomial factors are
analytic there. In a fixed branch and angular mode, choose the largest
N with a nonzero coefficient at one radius. Its highest pole cannot
cancel with any other term. Descending induction removes all terms at
that radius. Repeat at the other radii, then use the accepted old
independence. There are1922+3*252+240=2918 independent potentials.
The argument concerns rational functions after separating the fractional
branches. It does not evaluate the physical S^p_j at negative S.

The checker expands the actual generator numerator and evaluates it at
each auxiliary pole. There are348 distinct(scale,m,N) Laurent witnesses:
252 in the three low-block scale families and96 in the radius25 high
angular range16,...,23. Branch duplicates share the same radial witness.
All six ordered cross-pole denominator values must be nonzero.

## Density injectivity

All generators are smooth and separately even in x and y. Finite
explicit differentiation gives |D^k chi|=O(r^(3+gamma-k)) for0<=k<=4.
The scaled envelope contributes eight further powers of decay. Since
3+gamma<4, all fourth derivatives tend to0 at infinity. If
partial_y Delta chi=0, then Delta chi=f(x). For fixed x, taking |y| to
infinity in f''(x)=partial_xx Delta chi(x,y) proves f''=0. Evenness makes
f constant, say K0. The function h=chi-K0*r^2/4 is entire harmonic,
separately even, and has growth O(1+r^(3+gamma)).

The harmonic interior derivative estimate on a radius-L disk around any
fixed point gives |D^4 h|<=C L^(-4) sup|h|=O(L^(gamma-1)). Letting L
tend to infinity shows D^4 h=0. Thus h is a polynomial of degree at most3;
separate evenness and harmonicity reduce it to A+B(x^2-y^2). Therefore
chi is a separately even quadratic polynomial. Its angular radial
coefficients are integer Laurent polynomials in v, while its original
expression is a sum of the distinct noninteger branches above. Branch
separation, including the integer exponent class, makes both sides zero.
Hence chi=0, proving injectivity. The harmonic estimate is an analytic
dependency and is not replaced by a finite-rank computation.

## Probe span and recorded history

For r>0 divide a proposed relation by the positive factor r S^(-2), and
take the sine-n coefficient around the full circle. If the probe has
n>=19, the resulting relation has the form

 t^K = alpha*t^((n-1)/2+128) + beta*t^((n-1)/2+512), 0<t<1.

The probe exponent K is different from the two exponents on the right.
Distinct nonnegative integer powers are independent: in a nonzero
polynomial relation, division by its least power and passage t down to0
leaves a unique nonzero coefficient. This contradiction proves the46
asserted span separations. Angular separation alone is insufficient here,
because the objective now contains these same angular modes. The14
additional pairs themselves are objective members. For the parent016
and earlier audited stages, objective rows form a subset, so all46
separations persist through the recorded chain.

Each phi is smooth: r^(2K+1)sin(n theta) equals Im(x+iy)^n times
(r^2)^(K-(n-1)/2). Continuous functions equal almost everywhere are equal
everywhere. A continuous function nonzero at a point pairs nontrivially
with a smooth test in a neighborhood where its sign is constant. Thus
the span proof also applies to almost-everywhere and distributional
equality. It makes no claim of statistical independence or blindness.

The checker binds the immutable snapshot, current frozen launch source,
completed log, all81 analytic row pairs and weights: first67 at10^12,
last14 at10^16. It records60 attempted iterations, each accepted or
rejected, and parses the reported dRho2 and dCoef values as FLOAT log
entries. A sum of rounded mesh step norms is not a certified full-plane
bound on the total correction. Zero initial coefficients of the744 new
shapes are a source-level statement before the Taylor projection, not a
claim about the projected initial vector. The declared rule is angular180,
MID16, with the unchanged balanced weights26214400 and3000000.

The public25-probe register has an independently retained earlier time.
The025 held-out document claims09:13:13Z creation and09:41:40Z addendum;
its current bytes and recorded10:05Z launch can be checked, but a current
copy alone does not independently observe those earlier filesystem events.
No exact historical source-byte identity is inferred from current source.

## Numerical dependencies and scope

The existing joint-scaled field representation already stores four poles
99,624,2499,9999. Its accepted rational and scalar fixtures include
simultaneous four-pole products. The moment theorem in
../factored_pole_moments/PROOF.md allows any finite collection of distinct
positive rational poles. Actual025 weak tests must still retain every
field component, complete group integral and direct/by-parts check, and
must be independently reproduced. The relevant correction hypotheses are
exactly those in ../joint_scaled_factored_weak/PROOF.md: fixed c, realS1
L2 correction, canonical divergence-free L2-contractive velocity and the
distributional stationary equation with its locally integrable products.

Point, origin and finite-prefix checks follow
../generator_sector_audit/PROOF.md and PROOF_CANDIDATES.md. This shape
and history result proves no residual upper bound, optimizer minimum,
background bound, inverse or existence theorem. Three-scale actual025
acceptance remains OPEN until its distinct raw input is independently
checked, regardless of earlier two-scale successes.
