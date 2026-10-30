# Candidate026: exact unchanged basis and changed objective rows

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The frozen raw JSON for C1-N1-026-heldin1e16-legqs25-m16to23 has SHA256
2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3. Its ordered potential basis equals candidate022, with dimension2414.
The canonical density map is rho=-partial_y Delta chi. Its image also
has dimension2414. These are dimensions before the421 recorded constraints;
no sampled rank, constrained tangent rank or inverse is asserted.
The recorded objective has81 analytic rows,67 at weight10^12 and14
at weight10^16. The46 specified diagnostic probes are outside their
analytic linear span. The statement concerns the exact function spaces.

## Independent rank argument

Put S=1+x^2+y^2 and p_j=(3+gamma-j delta)/2. In addition to the1922
accepted quotient013 generators, adjoin492 functions

 Re(x+iy)^(2m) S^(p_j-m) [625/(625+r^2)]^4
              P_N(2r^2/(625+r^2)-1),

where N=0,...,11; j=1,m=9,...,19; or j=2,3,m=9,...,23. Their order
is the old1922, then252 functions with m=9,...,15, then240 with
m=16,...,19 for j=1 and16,...,23 for j=2,3. The checker compares all
2414 actual shapes, in order, with this list and with candidate022.

Angular orthogonality separates m. In v=1/S each p_j has a distinct
noninteger class modulo the integers. The eight exponents and their28
pairwise differences are checked as exact nonintegers. For a finite
relation, expand its rational coefficients near v=0. The least power
in a nonzero branch cannot be canceled by another noncongruent branch.
Removing that branch proves separation. Within each (j,m), the new
rational factors have a unique pole at v0=-1/624. The old quotient
factors are analytic there. Writing L=1+624v and Z=2(1-v)-L, the
homogeneous Legendre numerator follows

 H_0=1, H_1=Z,
 (N+1)H_(N+1)=(2N+1) Z H_N-N L^2 H_(N-1).

Its scaled rational numerator is625^4 v^4(1-v)^m H_N. The highest
Laurent coefficient at v0, of pole order4+N, is

 625^4 v0^4 binom(2N,N) (1-v0)^(m+N) / 624^(4+N),

which is nonzero. The checker computes each of180 distinct(m,N)
coefficients from the recurrence and compares it with this formula.
Descending pole order removes all scaled terms; the old1922 then
vanish by the accepted quotient-rank theorem. The negative pole is
only an auxiliary rational identity, not a fractional physical power.

For density injectivity, every potential is smooth, separately even,
and |D^k chi|=O(r^(3+gamma-k)) for0<=k<=4. If partial_y Delta chi=0,
then Delta chi=f(x). The fourth-derivative bound tends to zero as
|y| tends to infinity, forcing f''(x)=0. Evenness makes f constant.
Subtract a quadratic particular solution. The remaining entire harmonic
function grows more slowly than r^4; interior harmonic derivative
estimates on expanding disks make all fourth derivatives vanish. It is
a polynomial of degree at most3. Separate evenness leaves a constant
and a multiple of x^2-y^2 after the particular solution. These integer
powers cannot occur in a nonzero sum of the distinct noninteger
branches, by the same branch separation. Therefore chi=0. The potential
and density dimensions agree. The accepted022 and old quotient evidence
are hash-bound dependencies, and the new highest-pole calculation is
independent of the peer implementation.

## Exact probe separation and recorded execution

The first67 rows have mode1 powers0,...,8,12,16,24,32,48,64,96,128,
192,256,384,512,768,1024,1536,2048,3072,4096, and odd n=3,...,17
with K=(n-1)/2+s for s=0,8,32,128,512. The final14 rows have odd
n=19,...,31 and s=128,512, ordered first by s and then n.
The diagnostic set is the25 public(n,K) pairs n in{19,23,25,29,31},
K in{600,900,1200,1800,2400}, plus21 pairs n=19,...,31 odd and
s=0,8,32. All probes are phi=r(1+r^2)^(-2)t^K sin(n theta),
t=r^2/(1+r^2). For a linear relation, divide by r(1+r^2)^(-2)
and project onto one sine frequency. The objective supplies only the
two monomials with s=128,512 there. Every diagnostic exponent is
different. Distinct nonnegative integer monomials are independent on
(0,1), since a polynomial vanishing on an interval has zero coefficients.
This proves the claim as functions and distributions. Smoothness at
zero follows from r^(2K+1)sin(n theta)=Im(x+iy)^n(r^2)^(K-(n-1)/2).
Angular orthogonality alone would not suffice at these shared modes.

The actual JSON, frozen launch, parser and completed log must agree on
these rows, weights, unchanged basis,60 attempted iterations and MID16.
Their accepted rounded mesh steps are summed as decimal rationals.
The source projects each trial before measuring its difference, so
these per-step numbers include the trial Taylor projection. They omit
the initial projection, final exact conversion and integration error.
They are FLOAT diagnostics, not a certified total density change.
All publisher code is inspected as text, never executed by this audit.
The public probe register predates the recorded launch. The private
held-out declaration says11:31:32Z while the frozen worklog says11:31Z
only; the finer historical ordering is not independently established.
No statistical independence or blindness follows from analytic span
separation. The manifest's FLOAT summary is not used in this proof.

No residual norm, exact stationary solution, numerical inverse or
existence closure follows from this structural audit. Independent local
and whole-plane tests are recorded in the four neighboring026 topics.
