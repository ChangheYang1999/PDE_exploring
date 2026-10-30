# Candidate028: exact space and the67 recorded analytic objective rows

## Statement and notation

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
S=1+x^2+y^2, r=sqrt(x^2+y^2), v=1/S, t=1-v,
p_j=(3+gamma-j delta)/2 and H_m=Re(x+iy)^(2m).
This statement is prepared before candidate028 publication. An actual
candidate application requires its immutable manifest, raw exact JSON,
ordered shapes and all file hashes to be bound. It certifies no
unpublished coefficient file. All source files are inspected as text.

The parent is candidate022, exact raw SHA256
85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f.
Its accepted space comprises the1922 independent quotient potentials of013
followed by492 scale25 terms

 H_m S^(p_j-m) [625/(625+r^2)]^4 P_N(2r^2/(625+r^2)-1),

where P_N(1)=1, N=0,...,11 and j=1,m=9,...,19 or j=2,3,m=9,...,23.
Candidate028 appends precisely252 terms of the same displayed form with
j=1,2,3, m=9,...,15 and N=12,...,23, in that order. Its potential
dimension and the dimension of its density image chi -> -partial_y Delta
chi are2666. The appended252 are new radial degrees at the existing pole.
These dimensions precede421 recorded constraints. They do not identify
a constrained tangent dimension or establish conditioning. The old quotient
rank and the parent022 shape result must be rebound through
../optimizer_quotient_audit/PROOF.md and
../candidate022_shape_peer/verification/result.json, whose accepted hash is
81f34093ebb36d8e4386696e2f53d2768d96a391f1530903988e3cc197d5f6bd.

## Independence and injectivity

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
For the parent the count is1922+12*(11+15+15)=2414. The new terms add
3*7*12=252. In each affected branch and angular mode, their pole
orders16,...,27 are distinct and exceed every parent scaled pole order.
Descending from the largest order removes every new term first. The
accepted parent independence then gives the full dimension2666. The pole argument concerns a
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

## Analytic rows and60 outside-span probes

For odd positive n and integer K>=(n-1)/2, define
phi_(n,K)=r S^-2 t^K sin(n theta). The objective is required to contain
exactly67 rows: n=1 with
K=0,...,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,
1536,2048,3072,4096, followed by n=3,5,...,17 with
K=(n-1)/2+s for s=0,8,32,128,512. Every row has weight10^12.
There are no additional held-in rows. The25 public pairs
n in{19,23,25,29,31}, K in{600,900,1200,1800,2400}, and35 pairs
n=19,21,...,31, K=(n-1)/2+s for s=0,8,32,128,512, are outside
this analytic row span.

Indeed all objective frequencies are at most17. Project a putative
relation onto any named frequency n>=19 by full-circle sine
orthogonality. The objective projection is zero, while its proposed
probe projection is pi r S^-2 t^K, strictly positive for r>0. This
is impossible. Smoothness at0 follows from
r^(2K+1)sin(n theta)=Im(x+iy)^n (r^2)^(K-(n-1)/2). Continuous
functions equal almost everywhere agree everywhere. A nonzero continuous
function pairs nontrivially with a smooth function supported in a
neighborhood of fixed sign. The separation also holds almost everywhere
and as distributions. It is analytic span separation, not statistical
independence, blindness or independence of sampled objective arrays.
The earlier022,016 and quotient stages have subsets of these rows.
Undocumented earlier stages are outside this history claim.

## Recorded optimizer and chronology scope

The candidate-specific checker must reconstruct every ordered shape,
exact coefficient, c, all snapshot SHA256SUMS, all67 analytic row pairs
and weights from the final metadata and the current saved launch source.
It must inspect all60 attempted iteration indices and ACC/rej flags in
the completed log, angular rule180, MID16, and the two recorded weights
26214400 and3000000. The publisher's Python and shell are text only;
none is executed. Accepted floating mesh step norms include per-step
Taylor projection, but not initial projection or final exact conversion.
A rounded sum is not a certified endpoint density distance.

The public25-probe registration is independently timestamped earlier
than these launches. New held-out document times and minute-level
work log launch times are reported as recorded claims. A file mtime is
not an independent observation of its historical creation. Candidate028's
held-out document claims12:51:53Z, while the work log launch description
is only12:51Z, so ordering within that minute is unresolved without a
separate finer record. Candidate027's prepared snap027.sh description
and work log both record a12:34Z launch. The later note says optimization
steps began at12:50Z; this can follow an earlier construction phase and
is not a contradictory launch record. Neither historical event was
independently observed here. The028 within-minute ambiguity does not
alter analytic span separation or a separately proved weak bound.

## Exact verification and limits

Recheck all36 noninteger exponent conditions and growth gamma<1.
For028, independently expand each distinct new pair(m,N) and evaluate
its numerator at v0=-1/624 to verify its nonzero leading Laurent
coefficient. There are7*12=84 distinct new pole witnesses, shared across
j=1,2,3 after branch separation. For027 exact identity with the accepted
parent space suffices. Store large exact coefficients and witness values
in JSON. Hash proofs, code, source copies, parent acceptance and snapshot
files before and after execution. A later reviewer must reproduce actual
candidate results before the independent audit is complete. No finite
radius tail bound, residual upper norm, stationary solution, inverse,
closure margin or existence follows from this structural result.
