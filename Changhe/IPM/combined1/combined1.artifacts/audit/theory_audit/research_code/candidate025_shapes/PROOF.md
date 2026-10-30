# Independent audit of the candidate025 dimension and recorded probe history

## Exact statement

Fix c = 4076476460239181/2251799813685248, gamma = 1/c,
delta = 1-gamma and p_j = (3+gamma-j delta)/2. Let r^2=x^2+y^2,
S=1+r^2, t=r^2/S, v=1/S and H_m=Re((x+i y)^(2m)). Let V_old be
the 1922-dimensional potential space with the selected original basis
in data/old_basis.json, already proved independent in T4-195 and
T4-230. Its elements are sums H_m S^(p_j-m) P_jm(t), where each P_jm
is polynomial and j is in {0,...,7}.

For each R in {25,50,100}, j in {1,2,3}, m in {9,...,15}, and
N in {0,...,11}, adjoin the following generators. Also adjoin R=25,
j=1,m=16,...,19 and j in {2,3},m=16,...,23, with N=0,...,11:

    G_RjmN = H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                       P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial normalized by P_N(1)=1.
The 2918 resulting potentials are linearly independent over the reals.
The map chi -> -partial_y Delta chi is injective on their span V.
Consequently both V and its density image have dimension 2918.
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
there. Every other scale is analytic there, since
1-a_(R')/a_R is nonzero for distinct a_R,a_(R') in{624,2499,9999}.
Therefore the largest N with a nonzero coefficient at any scale
would have an uncancellable pole. Descending in N removes every new
coefficient at all three scales. The old independent basis removes the
remaining coefficients. There are 996 new generators, proving 2918.
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

## Actual candidate025 and recorded analytic span

The exact candidate ID is C1-N1-025-combined-heldin1e16. Its raw JSON
SHA256 is 3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17. The actual ordered list consists of the1922 old quotient013
shapes,252low-order R25 shapes already in parent016,252low-order R50,
252low-order R100, and240high-order R25 shapes as specified above.
All coefficients are exact rationals. The dimensions2918 concern the
full potential/density spaces before the421 recorded constraints;
no tangent-space rank claim follows from the number421.

The independent checker expands each homogenized Legendre numerator by
its three-term recurrence and evaluates it exactly at its negative pole.
It compares that value with the displayed binomial leading-coefficient
formula. There are348distinct(scale,m,N)witnesses and six ordered
cross-pole evaluations. It separately checks the36noninteger conditions,
growth below degree4, the full shape order, and the old1922rank evidence.

The first67 analytic objective rows are27 mode-one exponents0,...,8,12,
16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096 and
40rows at odd n=3,...,17, K=(n-1)/2+s for s=0,8,32,128,512. Their weight
is10^12. Fourteen further rows have odd n=19,...,31 and s=128,512,
ordered first by s and then n, with weight10^16. The actual JSON, launch,
row parser and recorded iteration log must agree on all81rows and these
split weights. The launch records60attempts from016, angular order180,
middle order16, zero extension followed by Taylor projection and a
CUDA backend. These files are inspected as text, never executed.

The46held-out probes consist of25public(n,K) pairs and21higher-frequency
pairs with s=0,8,32. Divide any proposed linear relation by
r(1+r^2)^(-2), then project onto a sine frequency. At that frequency the
objective has only t^((n-1)/2+128) and t^((n-1)/2+512). The probe has a
distinct nonnegative integer exponent. Distinct monomials are linearly
independent on(0,1), since a polynomial vanishing on an interval has all
coefficients zero. This proves exclusion from the analytic span. Angular
orthogonality alone is insufficient because these frequencies occur in
the objective. The identity
r^(2K+1)sin(n theta)=Im(x+iy)^n(r^2)^(K-(n-1)/2)
proves smoothness at the origin. No independence of sampled rows or
statistical independence is asserted. Public registration predates the
recorded launch; document self-reported save times are not independent
historical observations.

The log's accepted rounded mesh-step norms are summed exactly as decimal
rationals. This is a diagnostic only: it omits the initial projection,
final exact conversion and integration error, and is not a rigorous
whole-plane correction bound. The immutable manifest's basis description
and loss definition end at the words 'at weight ' and omit the numerical
weight. The exact metadata and launch resolve it as10^16; the truncated
manifest text must be qualified in reports, not silently rewritten.

No residual norm, inverse, exact stationary profile or existence closure
follows from this structural audit. Separate point, origin, complete
prefix and whole-plane weak proofs provide the quantitative conclusions.
