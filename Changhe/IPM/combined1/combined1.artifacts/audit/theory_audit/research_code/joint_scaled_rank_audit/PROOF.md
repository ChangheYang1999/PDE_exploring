# Independent audit of the simultaneous-scale dimension

## Exact statement

Fix c = 4076476460239181/2251799813685248, gamma = 1/c,
delta = 1-gamma and p_j = (3+gamma-j delta)/2. Let r^2=x^2+y^2,
S=1+r^2, t=r^2/S, v=1/S and H_m=Re((x+i y)^(2m)). Let V_old be
the 1922-dimensional potential space with the selected original basis
in data/old_basis.json, already proved independent in T4-195 and
T4-230. Its elements are sums H_m S^(p_j-m) P_jm(t), where each P_jm
is polynomial and j is in {0,...,7}.

For each R in {25,50}, j in {1,2,3}, m in {9,...,15}, and
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
1-a_(R')/a_R is nonzero for a_R=624 and a_(R')=2499, or conversely.
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

## Verification and limits

This is an independent audit of N4-274. The checker reconstructs the
abstract list, verifies all branch conditions and both cross-pole
values, and recomputes every Laurent coefficient from the closed
formula. It compares all 168 coefficients with the independently
accepted single-scale records and the new N4 record. All quantities
are rational; no floating rank or numerical conditioning is used.
The old rank and canonical generator definitions are retained as
explicit dependencies. The theorem gives no lower singular value,
optimizer floor, PDE inverse, or existence statement.
