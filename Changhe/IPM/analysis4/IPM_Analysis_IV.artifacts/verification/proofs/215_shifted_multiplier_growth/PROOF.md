# Conditional growth laws from an isometric shifted projection

Status: PROVED conditional statements after independent theory-part review, V443. Their all-order hypotheses have not been established for the canonical IPM sequence.

## Statement and notation

Let x_n be nonzero vectors in a real Hilbert space H, for n >= 1. Let S be a linear isometry of H. Fix an integer Q >= 1 and, for n > Q, define

    a_n = <S x_(n-Q), x_n> / ||x_(n-Q)||^2,
    r_n = x_n - a_n S x_(n-Q),
    e_n = ||r_n|| / ||x_n||.

Whenever a_n is nonzero,

    ||x_n|| / ||x_(n-Q)|| = |a_n| / sqrt(1-e_n^2).                 (1)

Thus the projection multiplier alone is not exactly the norm ratio unless the residual vanishes.

Suppose every sufficiently large n satisfies the stated assumptions, uniformly across the Q residue classes.

(a) If |a_n| tends to a finite A > 0 and e_n tends to E < 1, then

    lim_(n->infinity) ||x_n||^(1/n) = [A/sqrt(1-E^2)]^(1/Q).

In particular, the limit is A^(1/Q) if e_n tends to zero.

(b) If there are constants C_-, C_+ > 0 and E < 1 such that

    C_- n^beta <= |a_n| <= C_+ n^beta,   0 <= e_n <= E,

for some real beta, then positive constants B_-, B_+ and K_-, K_+ exist with

    K_- B_-^n (n!)^(beta/Q) <= ||x_n|| <= K_+ B_+^n (n!)^(beta/Q).

For beta > 0 the H-valued power series sum x_n z^n has radius zero. The phrase Gevrey exponent beta/Q here describes this coefficient growth scale; it is not a convergence theorem for the logarithmic IPM series.

(c) The weaker lower bound |a_n| >= C n^beta with C > 0 and beta > 0 already implies radius zero. It suffices that this lower bound hold eventually on one fixed residue class modulo Q. No separate residual upper bound is needed for this implication.

## Proof

By the defining projection, r_n is orthogonal to S x_(n-Q). The isometry and Pythagoras give

    ||x_n||^2 = a_n^2 ||x_(n-Q)||^2 + ||r_n||^2.

Dividing by ||x_n||^2 proves (1). It also proves ||x_n|| >= |a_n| ||x_(n-Q)||, even without a uniform bound on e_n.

For (a), take logarithms in (1) and telescope on each residue class. Each summand tends to log A - (1/2)log(1-E^2). The Cesaro mean has the same limit, and the number of summands divided by n tends to 1/Q. Finitely many starting norms have no effect after division by n. This proves (a).

For (b), (1) bounds each step ratio between C_- n^beta and C_+ n^beta/sqrt(1-E^2). On a fixed residue class n = s+kQ, telescope from a sufficiently large starting index. The logarithm of the product of the powers n^beta is

    beta sum_j log(s+jQ) = (beta/Q) log(n!) + O(n).

To justify the last estimate without an asymptotic formula, write log(s+jQ) = log Q + log j + O(1/j) for fixed s and j >= 1. Hence its sum is k log Q + log(k!) + O(log(k+1)). The integral inequalities for the increasing function log t give log(k!) = k log k - k + O(log(k+1)); the same estimate for n! gives the claimed relation, with even O(log(n+1)) error when aligned carefully. The constant step factors contribute O(n). Exponentiating and enlarging finitely many starting constants proves (b). Stirling's estimate is not needed to conclude radius zero: (n!)^(1/n) tends to infinity by the elementary lower bound n! >= floor(n/2)^(floor(n/2)). For (c), use only the lower step bound and the same product estimate.

## Applicability to the saved IPM diagnostic

For a logarithmic coefficient F_n, use H = l2 of the coefficient array indexed by logarithmic degree q and positive Fourier-mode index j. Embed each finite array in the infinite array by zero padding. The mode shift is

    (Sx)_(q,j+1) = x_(q,j),   (Sx)_(q,0) = 0.

It is an isometry. The producer's adjacent-period diagnostic pads by an extra mode before shifting, so it has the same isometry and does not discard the highest coefficient. The fixed-reference diagnostic is a separate quantity and is not used in (1).

At delta = 2/3 the period is Q = 3. If an all-order law |a_n| comparable to n^0.555 were proved, (c) would force zero radius for the coefficient-array generating series, and under the upper hypotheses of (b) its coefficient growth scale would have exponent 0.185. If instead |a_n| tended to 0.04091 and e_n tended to zero, (a) would give an array-norm radius 0.04091^(-1/3). Neither law follows from the available finite fit. Physical evaluation with powers of log(r) is a further issue and is not identified with this array-norm radius.

At these orders the coefficient arrays have at most a polynomial number of positions, from the linear angular bandwidth and linear logarithmic degree. Therefore l1 and l2 coefficient norms differ by at most a polynomial factor: ||x||_2 <= ||x||_1 <= sqrt(d_n)||x||_2. Such a factor does not change an exponential root limit or the coefficient of n log n. This observation permits comparison with the reported l1 coefficient norms when the hypotheses of (a) or (b) hold.

## Finite evidence and limitations

The numerical audit in topic 207 supplies conditional enclosures for some finite a_n and e_n. The continuation depends on the reset input at order 329 and excludes the discarded prior uncertainty. A finite least-squares fit supplies no all-order lower bound, no residual limit, and no choice between the two models. The conditional implications above therefore leave convergence of the canonical logarithmic series open.

## Finite fit audit specification

For orders 348 through 370, form the shifted dot products directly from the packed coefficient intervals. If A = ||Sx_(n-3)||^2, B = ||x_n||^2 and C = <Sx_(n-3),x_n>, then a_n = C/A and e_n^2 = 1-C^2/(AB). All three sums use directed arithmetic. Compare selected rows with the separately audited intervals in topic 207.

For data (t_n,y_n), the least-squares slope is sum((t_n-tbar)(y_n-ybar))/sum((t_n-tbar)^2), and the intercept is ybar minus slope times tbar. Substitution in the two normal equations verifies these formulas; the denominator is strictly positive for nonconstant t_n. Apply them to y_n = log10|a_n| with t_n = log10 n and t_n = 1/n. The root mean squared residual is the square root of the mean squared difference from the fitted line. Directed evaluation gives finite enclosures conditional on the input checkpoint. Also fit the published rounded multipliers as exact decimal data, so a change caused by input rounding can be distinguished from an implementation discrepancy. A close fit over these 23 orders is not evidence sufficient to choose an all-order model.

## Consequence for the physical canonical IPM series

Assume in addition that the arrays x_n are the density coefficients F_n of the canonical stationary polynomial-log recursion at a rational delta in (0,1), with a nonzero finite real odd-sine leading profile. If the hypotheses of (a) hold, the density, stream and common-potential series converge with all fixed weighted derivatives on some exterior. If the hypotheses of (c) hold, their individual terms are unbounded almost everywhere in the punctured physical plane, and on a common dense residual set; this includes the radial-velocity series.

For the first implication, (a) gives a finite root limit for the l2 norms. The number of coefficient positions is bounded by C n^2, so the l1 density norm satisfies M_n <= sqrt(C)n ||x_n||_2. It therefore has an exponential bound. The density-to-stream theorem in topic98 gives an exponential stream bound, and the exterior reconstruction theorem in topic99 gives the asserted common solution. Its radius need not equal the coefficient-array radius: both the logarithmic powers and the density-to-stream estimate enter its quantitative value.

For the second implication, the fixed-residue-class product in (c) gives limsup ||x_n||_2^(1/n)=infinity. Since M_n >= ||x_n||_2, no exponential bound for M_n exists. Topic99, whose hypotheses are exactly the finite leading support and the canonical recursion stated here, then gives unbounded density terms outside a null and meagre set. The equivalence of exponential density and stream bounds in topic98 gives the same failure for N_n; topic94 supplies the corresponding stream, radial-velocity and potential conclusions. Intersecting the finitely many full-measure residual sets preserves both properties. None of these arguments proves that either multiplier hypothesis holds for the computed sequence.
