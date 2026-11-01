# Independent finite audit of the tuned series

Status: finite coefficient and continuum-residual checks CONFIRMED in V265 and V266. Infinite convergence is supplied by the already proved topics119,121and126, with their stated conservative radii. Finite checks at smaller radii do not improve that theorem.

## Objects and exact hypotheses

Let c=3, delta=2/3, p_n=1-2n/3 and let b be the first real sextic root isolated in119. Write f_1=sin(theta)+b sin(3theta). Let f_n,g_n be the uniquely compatible pure series of TheoremT, including the tuned free coefficient of sin((2k-2)theta) in g_(3k). The numerical source is a finite 1024-bit interval evaluation of that construction. Its coefficients are stored as exact dyadic midpoints with dyadic error bounds.

A checkpoint at order3k may still have its final free coefficient H_(3k) set provisionally to zero. The affine lookahead determines it from orders3k+1through3k+3. Hence the last saved density order and the last fully tuned stream order are different notions. All residual truncations in this audit use a completed stream prefix. The low-order independent Cartesian intervals in119 provide a separate coefficient comparison.

## Cartesian consistency checks

Represent a sine field r^q sum a_m sin(m theta) by the real signed Laurent polynomial F=sum a_m(z^m-z^(-m))/2. Its physical value on z=exp(i theta) is -i r^q F. Define X and Y on a monomial of degree m by

    X(r^q z^m)=r^(q-1)[(q+m)z^(m-1)+(q-m)z^(m+1)]/2,
    Y(r^q z^m)=r^(q-1)[(q+m)z^(m-1)-(q-m)z^(m+1)]/2.

Thus physical x differentiation uses X and physical y differentiation uses iY. The signed Laurent representative of advection is

    T(g,f)=Xg Yf-Yg Xf.

The Poisson and stationary identities become

    -XXg_n+YYg_n=Xf_n,
    2(n-1)f_n=sum_(i+j=n) T(g_i,f_j).

The audit constructs these Cartesian derivatives independently. Laurent products are ordinary interval-polynomial products, not the source's sine-product formulas. Every residual coefficient must contain zero. This is a consistency check on all tested finite orders. Containment of zero alone does not prove a new exact identity or validate an arbitrary interval algorithm. Exact identities and compatibility are proved in119; source enclosure validity additionally requires the audited interval construction and root isolation.

## Validity of the source interval construction

The source uses its Arb ring for every coefficient operation. Its sine products are sums and differences of interval polynomial products; the two reflected convolution branches and factors1/2 agree with the exact sine identities. The recurrence divides by the interval enclosing the exact nonzero lambda_n. Only trailing exact zeros are trimmed. Floating-point statistics and grid values are never fed back into coefficient construction.

The retained leading b interval is checked to contain an independently isolated exact root of the sextic. This directly validates the starting data, independently of the source root-enclosure routine. At a pure resonance the exact compatibility theorem implies that the forbidden coefficient is zero. The source deletes that stream mode in the provisional inverse. Its Q=3 response formulas agree term by term with the proved affine block equations. The provisional obstruction R and response sigma enclose the exact quantities; the source rejects any response interval containing zero. Consequently -R/sigma encloses the unique exact harmonic. Adding its three affine response corrections encloses the exact tuned density coefficients. Recomputing their Poisson inverses encloses the corresponding streams. Induction proves coefficient containment for the completed prefix.

The additional tests that each obstruction interval contains zero are useful consistency checks; they are not the reason exact compatibility holds. That reason is the exact algebraic root and tuning theorem. The last potentially open harmonic is excluded by the selection rule. Midpoints and radii are exported as exact dyadic data and independently reconstructed before the Cartesian checks.

## Weighted finite residual and full-circle bounds

For a truncation N with completed g_1,...,g_N, set z=R^(-2/3). Let A_N,B_N,C_N,D_N be sums of z^(n-1)Xg_n, z^(n-1)Yg_n, z^(n-1)Xf_n, z^(n-1)Yf_n. Then the signed Laurent representative of R^(-1/3) times the stationary residual on r=R is

    z(A_N D_N-B_N C_N)-2 sum_(n=1)^N (n-1)z^(n-1)f_n.

This identity follows directly from the radial exponents, since p_i+p_j-1=p_(i+j). It computes the entire residual, including any finite arithmetic enclosure uncertainty. Exact cancellation of orders at most N reduces it to the tail formula used by the numerical experiments.

For any real trigonometric polynomial h and a uniform angular mesh of spacing d, linear interpolation on one mesh interval gives

    |h(theta)-L(theta)| <= d^2 sup|h''|/8.

Indeed the interpolation remainder is h''(xi)(theta-a)(theta-b)/2, whose absolute value is at most d^2 sup|h''|/8. Also |L| is at most the larger endpoint absolute value. Consequently

    max_grid |h| <= sup |h| <= max_grid |h| + d^2 sum_m m^2 |h_m|/8.

Interval evaluation bounds each grid value and the coefficient sum. Odd sine harmonics and all their angular derivatives have absolute value of period pi, so a mesh on[0,pi] covers the full circle. The same argument applies to the residual, its first two angular derivatives and the next density increment. The reported lower and upper endpoints therefore bound the continuum supremum. The source evaluator itself supplies only floating-point grid maxima; it does not include this interpolation error.

Partial sums at theta=3/10,9/10,13/10 are evaluated as interval trigonometric polynomials. Comparisons across N=20,40,80 measure finite stability only. No tail beyond the computed truncations is bounded by these tests at small R.

## Evidence and scope

The verification folder records the selected exact dyadic checkpoint prefix, its source hash and selection rule, root containment, all finite Cartesian consistency comparisons, the independent order30 comparison, and full-circle residual bounds. Source code snapshots and hashes accompany the output. Any failed check remains visible in the ledger before correction. No formal Lean verification is performed.

The completed computation selected orders1through150 from the checkpoint at273. All91350 Poisson and91039 nonlinear coefficient checks passed, including all11175 ordered products. The residual comparisons certify75 strict decreases across the stated four truncation orders and five radii. Exact dyadic inputs, source snapshots, output intervals and actual timings are retained.
