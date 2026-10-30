# Independent audit of the candidate024 dimension and recorded probe history

## Exact statement

Fix c = 4076476460239181/2251799813685248, gamma = 1/c,
delta = 1-gamma and p_j = (3+gamma-j delta)/2. Let r^2=x^2+y^2,
S=1+r^2, t=r^2/S, v=1/S and H_m=Re((x+i y)^(2m)). Let V_old be
the 1922-dimensional potential space with the selected original basis
in data/old_basis.json, already proved independent in T4-195 and
T4-230. Its elements are sums H_m S^(p_j-m) P_jm(t), where each P_jm
is polynomial and j is in {0,...,7}.

For each R in {25,100}, j in {1,2,3}, m in {9,...,15}, and
N in {0,...,11}, adjoin

    G_RjmN = H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                       P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial normalized by P_N(1)=1.
The 2426 resulting potentials are linearly independent over the reals.
The map chi -> -partial_y Delta chi is injective on their span V.
Consequently both V and its density image have dimension 2426.
This is a theorem about the stated abstract function list, not a claim
about an unregistered candidate's shape list or coefficient rank.

## Potential independence

Separate each cos(2m theta) by angular orthogonality. The radial
relation then has the form sum_j v^(-p_j) Q_j(v)=0, where Q_j is
rational and analytic at zero. All p_j and all nonzero differences
p_j-p_k are nonintegers, as the exact check verifies. A nonzero Q_j
has some finite integer vanishing order n_j at zero. The exponents
n_j-p_j are distinct. Dividing by the smallest power and taking
v down to zero leaves one nonzero coefficient, a contradiction.
Thus each Q_j vanishes separately. The same argument separates these
branches from one additional integer Laurent-polynomial class.

For fixed (j,m) the new rational factor is

    A_RmN(v) = R^8 v^4 (1-v)^m
               P_N(2(1-v)/(1+a_R v)-1)/(1+a_R v)^4,
    a_R = R^2-1.

At v_R=-1/a_R, the factor has pole order 4+N. Its leading Laurent
coefficient is

    C_RmN = R^8 v_R^4 binom(2N,N)
                       (1-v_R)^(m+N)/a_R^(4+N) != 0.

Indeed only the leading term 2^(-N) binom(2N,N) x^N of P_N can
contribute to this order. Every old radial polynomial is analytic
there. The other scale is also analytic, since
1-a_(R')/a_R is nonzero for a_R=624 and a_(R')=9999, or conversely.
Therefore the largest N with a nonzero coefficient at either scale
would have an uncancellable pole. Descending in N removes every new
coefficient at both scales. The old independent basis removes the
remaining coefficients. There are 504 new generators, proving 2426.
The pole argument is applied only after branch separation to rational
functions; it does not analytically continue a noninteger power
through a negative pole.

## Density injectivity

Every element chi of V is smooth and separately even in x and y.
Differentiation of its explicit finite generators gives
|D^k chi|=O(r^(3+gamma-k)) for 0<=k<=4 as r tends to infinity.
The scaled rational factors improve these bounds. In particular every
fourth derivative tends to zero, since gamma<1.

Suppose partial_y Delta chi=0. Then Delta chi=f(x). For fixed x,
f''(x)=partial_xx Delta chi(x,y) tends to zero as |y| tends to infinity.
It is independent of y, so it is zero. Evenness forces f=K constant.
The function chi-Kr^2/4 is entire harmonic and grows at most like
r^(3+gamma), with 3+gamma<4. Its fourth derivatives vanish by the
interior harmonic derivative bound on disks of radius L, followed by
L tending to infinity. It is a polynomial of degree at most three.
Separate evenness leaves only a constant and even quadratics, and
harmonicity leaves the form A+B(x^2-y^2). Thus

    chi=A+B(x^2-y^2)+Kr^2/4.

Its angular coefficients are integer Laurent polynomials in v.
The branch separation already proved, including the integer class,
forces these coefficients and every branch to vanish. Hence chi=0,
and potential independence forces the entire coefficient vector to
vanish. This proves density injectivity.

## Candidate024 restriction and recorded objective

The abstract two-scale theorem above contains the candidate024 space as
the subset with all radius100 coefficients zero. Restriction preserves
linear independence and density injectivity. Therefore candidate024 has
both dimensions2174 once its ordered1922 old and252 radius25 shapes
are checked. Its raw coefficient SHA256 is
3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.
The checker rebinds the accepted full two-scale evidence and compares
the actual shapes with parent016, whose abstract old ordering may differ.

The recorded024 optimizer starts from the exact013 quotient and appends
zero coefficients at radius25 before a Taylor projection. It uses67
analytic rows:27 first-mode exponents0,...,8,12,16,24,32,48,64,96,128,
192,256,384,512,768,1024,1536,2048,3072,4096, and40 rows at odd n=3,...,17,
K=(n-1)/2+s with s=0,8,32,128,512. Every25 public and35 diagnostic probe
with n>=19 is outside this analytic span: divide by r(1+r^2)^(-2),
then project onto its sine frequency. The objective contributes zero,
the probe contributes the nonzero power t^K. Smoothness follows from
r^(2K+1)sin(n theta)=Im(x+iy)^n(r^2)^(K-(n-1)/2).

The actual metadata, launch and log must agree on middle order32,
angular order180, all objective weights and12 attempted iterations.
Accepted and rejected iterations are counted separately. Parent016
uses middle order16 and CPU, while024 records CUDA. Thus the comparison
changes more than one execution parameter. No causal conclusion about
optimizer stopping or mathematical minimum follows. Source files are
inspected as text only; their current bytes are not launch-time archives.

The current held-out file hashes to e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab.
Replacing its single 'Objective rows (67):' by 'Objective rows (81? no: 67):'
reconstructs the quoted58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5
preimage. All60 probe pairs and other bytes are unchanged. This confirms
the proposed byte explanation, not the claimed09:13 save times. The
snapshot index still has two incorrect MID16 labels; neither held-out
hash occurs in its immutable manifest. The checker records these limits.

No norm or existence conclusion follows from this structural audit.
The fresh point, origin, sector and whole-plane weak reproductions are
separate results with complete proofs and exact inputs.
