# Candidate026: unchanged2414-dimensional space and81 recorded objective rows

## Exact statement and hypotheses

Let c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
S=1+x^2+y^2, r=sqrt(x^2+y^2), v=1/S, t=1-v,
p_j=(3+gamma-j delta)/2 and H_m=Re(x+iy)^(2m).
The declared candidate C1-N1-026-heldin1e16-legqs25-m16to23 is a
continuation of C1-N1-022-legqs25-m16to23. The latter has exact raw hash
85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f.
This proof is prepared before026 publication. Its026-specific application
requires the immutable manifest, exact raw coefficients and ordered shapes
to be bound by the checker. It certifies no unpublished coefficient file.

Suppose that the026 shape list equals the accepted ordered022 list:
the1922 quotient potentials of013, followed by492 potentials

 H_m S^(p_j-m) [625/(625+r^2)]^4 P_N(2r^2/(625+r^2)-1),

where P_N(1)=1, N=0,...,11 and either j=1, m=9,...,19 or j=2,3,
m=9,...,23. There are no new shapes in026. Its potential space has real
dimension2414, and the density map chi -> -partial_y Delta chi is
injective on this space. The density-space dimension is also2414.
These are dimensions before the421 recorded constraints; no tangent
rank or conditioning claim follows. The accepted exact independence of
the1922 quotient functions is the dependency
../optimizer_quotient_audit/PROOF.md, bound through the independently
accepted022 result in ../candidate022_shape_peer/PROOF.md.

For positive odd n and integer K>=(n-1)/2, write

 phi_(n,K)=r S^(-2) t^K sin(n theta).

The026 objective contains81 analytic rows: the67 rows of022 and14
additional pairs. The first27 have n=1 and
K=0,...,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,
1536,2048,3072,4096. The next40 have n=3,5,...,17 and
K=(n-1)/2+s for s=0,8,32,128,512. The final14 have n=19,21,...,31
and K=(n-1)/2+s, first s=128 and then s=512. The first67 weights are
10^12 and the last14 weights are10^16.

The25 public pairs n in{19,23,25,29,31}, K in{600,900,1200,1800,2400}
and21 diagnostic pairs n=19,21,...,31, K=(n-1)/2+s for s=0,8,32 lie
outside the real span of these81 analytic rows. The14 added objective
rows are design rows, not held-out evidence. The assertion is analytic
span separation, not statistical independence or blindness.

## Potential independence and density injectivity

Angular orthogonality separates the potential frequencies2m. In a fixed
mode, a finite relation takes the form sum_j v^(-p_j)Q_j(v)=0, where
Q_j is rational and analytic near0. The eight p_j and28 pairwise
differences p_j-p_k are nonintegers, checked exactly in the accepted
022 rank graph. Each nonzero Q_j has an integer order e_j at0.
The exponents e_j-p_j are distinct. Dividing by the least exponent and
letting v tend to0 through positive values leaves a unique nonzero
coefficient. This contradicts the relation and separates every branch.
The same argument separates the branches from the integer exponent class.

Within each branch and mode, put L(v)=1+624v. The scaled radial factor is
625^4 v^4(1-v)^m P_N(2(1-v)/L(v)-1)/L(v)^4. At v0=-1/624 its pole
order is exactly4+N. The leading Laurent coefficient is

 625^4 v0^4 binom(2N,N)(1-v0)^(m+N)/624^(4+N),

which is nonzero. This follows from the leading coefficient
2^(-N)binom(2N,N) of P_N. Choose the largest N with a nonzero coefficient
in a proposed relation. Its pole cannot cancel with smaller N or the old
quotient terms, which are polynomial in t. Descending induction removes
all scaled terms. The accepted quotient independence removes the rest.
Counting gives1922+12*(11+15+15)=2414. The pole argument concerns a
rational identity after branch separation; it does not evaluate physical
fractional powers at negative S.

Each potential is smooth and separately even in x and y, and its kth
Cartesian derivatives are O(r^(3+gamma-k)) for0<=k<=4. The scaled
factors decay eight powers faster. Since gamma<1, every fourth derivative
tends to0 at infinity. If partial_y Delta chi=0, then Delta chi=f(x).
For fixed x, let |y| tend to infinity in
f''(x)=partial_xx Delta chi(x,y). Thus f''=0 and evenness makes f constant.
Subtract f r^2/4 from chi to get an entire harmonic function h of growth
O(1+r^(3+gamma)). The harmonic interior derivative estimate in a disk of
radius L about any point gives |D^4h|<=C L^-4 sup|h|. Its right side
tends to0 as L tends to infinity, so h is a polynomial of degree at most3.
Separate evenness and harmonicity leave A+B(x^2-y^2), and chi is a
quadratic polynomial. Its radial angular coefficients have integer powers
of v. The fractional-branch separation above, including the integer
class, forces this polynomial and every original coefficient to vanish.
The density map is therefore injective.

## Separation of the46 probes

Take the sine-n angular coefficient of a putative relation and divide by
the positive radial factor r S^-2 for r>0. For each n>=19 the only
objective exponents are a=(n-1)/2+128 and b=(n-1)/2+512. A proposed
held-out pair would therefore satisfy t^K=alpha t^a+beta t^b on0<t<1.
The checker verifies K is distinct from a and b for each of the46 pairs.
Distinct nonnegative monomials are linearly independent: divide a
nontrivial polynomial relation by its least power and let t tend to0 to
leave its unique nonzero coefficient. This contradiction proves the span
separation. The earlier022,016 and quotient stages contain subsets of
the current analytic row family, so separation persists through those
recorded stages. No earlier undocumented optimization is covered.

Every phi is smooth at the origin because
r^(2K+1)sin(n theta)=Im(x+iy)^n (r^2)^(K-(n-1)/2). Continuous functions
equal almost everywhere agree everywhere. A continuous nonzero function
pairs nontrivially with a smooth test supported in a neighborhood where
its sign is constant. The same separation holds pointwise, almost
everywhere and as distributions.

## Source, chronology and verification scope

Bind the independent022 shape acceptance and its exact inputs. Compare
every actual026 ordered shape and exact c with022. Bind all snapshot
SHA256SUMS, the frozen current launch source, completed iteration log,
row parser and row-weight implementation. Reconstruct all81 row pairs,
weights,60 attempted iteration indices and each ACC/rej flag. Check the
recorded rule angular180, MID16, balanced weights26214400 and3000000.
The current source is inspected as text only and is never executed.
Current source-byte equality with historical optimizer execution is not
asserted. The exact candidate is the final rational output, separate
from the logged floating vectors and mesh diagnostics.

The log reports rounded mesh dRho2 and dCoef values. Their sums are not
certified whole-plane correction norms. The source computes each accepted
step after its per-step Taylor projection. The chain omits the initial
Taylor projection and final rational conversion from those step sums.
The recorded launch is only minute-resolved11:31Z, while the held-out
document claims11:31:32Z and BEFORE launch. These data alone do not order
the two events within that minute. Preserve this timing limitation;
current file timestamps do not replace independent observation. The public
25-probe register has a separately retained earlier time.

Point and complete-prefix checks have their own dependencies in
../generator_sector_audit/PROOF.md and ../candidate026_prefix/PROOF.md.
An actual full-plane weak calculation additionally requires every
background mode, complete moments and agreement of direct and by-parts
pairings under ../joint_scaled_factored_weak/PROOF.md. This shape and
history result alone proves no pointwise residual bound, stationary
solution exclusion, optimizer minimum, inverse or existence theorem.
