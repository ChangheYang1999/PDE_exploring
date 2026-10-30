# Density injectivity of the two scaled potential spaces

## Exact statement and dependencies

Let c = 4076476460239181/2251799813685248, gamma = 1/c,
delta = 1 - gamma, p_j = 2 - (j + 1) delta/2 for 0 <= j <= 7,
S = 1 + x^2 + y^2, r^2 = x^2 + y^2, t = r^2/S, v = 1/S,
and H_m(x,y) = Re(x + iy)^(2m). Let V_old be the real span of the
1922 selected potential generators in
../optimizer_quotient_audit/source/N1_013_quot_exact.json. They are
H_m S^(p_j-m) P(t), where P is a polynomial. Their independence is
a dependency, proved and checked in ../optimizer_quotient_audit/PROOF.md.

For R = 25 or 50, let V_R be V_old augmented by the 252 functions

 G_jmN = H_m S^(p_j-m) (R^2/(R^2+r^2))^4
                         P_N(2r^2/(R^2+r^2)-1),
 j in {1,2,3}, m in {9,...,15}, N in {0,...,11},

where P_N is the Legendre polynomial with P_N(1) = 1. The exact potential
rank 2174 for both values of R is the independently confirmed result
N4-263, ../scaled_rank_peer/PROOF.md. Here we prove that the linear map

 V_R -> C^infinity(R^2),   chi -> -partial_y Delta chi

is injective. Consequently the corresponding density space also has
real dimension 2174. The actual shapes of immutable candidates 016 and
017 are these bases. The theorem concerns the generator functions,
regardless of the fitted coefficient values.

## Complete argument

Every generator is smooth on the plane and even in each coordinate.
At infinity the old generators have convergent expansions of the form
r^(2p_j) times a power series in r^(-2) times cos(2m theta). The new
ones have an additional r^(-8) factor. Differentiating these convergent
expansions shows, for 0 <= k <= 4, growth O(r^(2p_j-k)) for the old
functions and O(r^(2p_j-8-k)) for the new ones. In particular, with
d = 2p_0 = 3 + gamma < 4, every chi in V_R satisfies

 chi = O(1+r^d),   D^4 chi = O(r^(d-4)) as r -> infinity.

Suppose -partial_y Delta chi = 0. Then Delta chi = f(x). Holding x fixed
and sending |y| to infinity gives f''(x) = partial_x^2 Delta chi(x,y) = 0.
Thus f is affine. Evenness in x forces f = K, a constant. The function
h = chi - K r^2/4 is entire harmonic, even in both coordinates, and has
growth O(1+r^d). Interior derivative estimates on a disk of radius L
centered at any fixed point give |D^4 h| <= C L^(-4) sup|h| = O(L^(d-4)).
Sending L to infinity shows D^4 h = 0, so h is a polynomial of degree at
most three. Evenness in x and y and harmonicity leave precisely
h = A + B(x^2-y^2). Therefore

 chi = A + B(x^2-y^2) + K r^2/4.                         (1)

Separate each angular mode cos(2m theta) in (1), and divide by r^(2m)
for r > 0. Each resulting left side is a finite sum

 sum_j v^(m-p_j) Q_jm(v),

with Q_jm rational and analytic near v = 0. The right side is an integer
Laurent polynomial: A + K(1-v)/(4v) for m = 0, B for m = 1, and zero
for every other m. All eight p_j are nonintegers and their 28 pairwise
differences are nonintegers, as checked exactly in the evidence.

For a nonzero analytic Q_jm, let e_j be its least Taylor exponent. The
nonzero left terms have leading exponents m-p_j+e_j in distinct,
noninteger classes modulo the integers. A nonzero right Laurent
polynomial has an integer leading exponent. These finitely many leading
exponents are all distinct. Dividing the equality by its unique least
power of v and taking v down to zero contradicts its nonzero leading
coefficient. Thus every Q_jm and each right Laurent polynomial vanish.
It follows that A = B = K = 0 and chi is the zero function. Potential
independence, the named N4-263 dependency, then forces the entire
coefficient vector to vanish. This proves injectivity and density rank.

## Independent review and exact finite checks

Opus lane the T1/T3 theory worker reviewed the full analytic argument in R1-036, frozen as
source/review set 33. T4 accepted that review in T4-332. We reread the
argument, bind both review records, compare their extracted shapes with
our exact candidate files, verify all 36 nonintegrality conditions and
the growth exponent, and recheck the full N4-263 rank dependencies.
The peer's code and output are retained as evidence; only our own
checker is executed. No sampled matrix calculation proves injectivity.

## Scope

No condition number, quantitative coercivity, PDE inverse, optimizer
minimum, or candidate existence statement follows. Exact rank and a
numerically singular sampled Gram matrix are compatible. The previously
confirmed scalar and graded exclusions of 016 and 017 do not change.
The same injectivity argument extends to finite analytic radial factors
satisfying the stated smoothness, parity, growth and branch hypotheses;
a dimension count for a different family requires its own independence
proof.
