# Exact global derivative caps from finite potential coefficients

Every finite potential in the recovered algebraic family has explicit finite bounds for the three derivatives left adjustable in89. The bounds below are intentionally coarse. They require a short exact coefficient calculation instead of a spatial mesh, and distinguish finiteness of these three quantities from the remaining reference hypotheses.

## 1. Statement

Let 0<gamma<1, delta=1-gamma, and let a finite potential be

    chi(X)=sum_(j,m,k) a_(j,m,k) P_(m,k)(X)(1+r^2)^(p_j-k),
    P_(m,k)=(x^2+y^2)^(k-m) Re(x+iy)^(2m),
    p_j=(3+gamma-j delta)/2, j>=0, k>=m>=0,                    (1)

with real coefficients. Define rho=-partial_y Delta chi and u=(-chi_xyy,chi_xxy). These expressions represent the canonical IPM velocity for the references considered here, as verified in their source audit; the derivative bounds below are statements about these explicit expressions and require no Fourier argument.

For a real q, write (q)_l=q(q-1)...(q-l+1), with (q)_0=1. Define

    R_d(q)=sum_(z=0)^floor(d/2)
             [d! 2^(d-2z)/((d-2z)! z!)] |(q)_(d-z)|,
    S_d(j,m,k)=2^d 2^(k+m)
                sum_(l=0)^min(d,2k) binom(d,l)(2k)_l R_(d-l)(p_j-k),
    C_d=sum_(j,m,k) b_(j,m,k) S_d(j,m,k),                       (2)

where b_(j,m,k) is any nonnegative upper bound for |a_(j,m,k)|. For rational coefficients the ceiling of the absolute coefficient is an admissible integer choice. Terms with zero coefficient can be omitted.

**Theorem.** With ordered Cartesian tensor norms, the following global inequalities hold:

    |D^d chi(X)| <= C_d <r>^(3+gamma-d) for every integer d>=0,
    <r>|D^3u(X)| <= 2 C_6,
    <r>^2|D^3rho(X)| <= 2 C_6,
    <r>^2|D^4rho(X)| <= 2 C_7.                                (3)

The bounds apply at the origin as well as at infinity. If all data in(1) are rational, C_d is rational and can be checked using integer arithmetic. Thus finite upper caps U3=B3=2C_6 and B4=2C_7, or any larger rational or dyadic values, satisfy exactly the three adjustable derivative inequalities of89.

This does not certify the other five fixed derivative bounds, any matrix inequality, a small residual, or existence of a profile. In particular, increasing the three caps does not evade the exclusions of90.

## 2. Polynomial and radial estimates

The sum of the absolute coefficients of (x^2+y^2)^(k-m) is 2^(k-m). For m>=1 the corresponding sum for Re(x+iy)^(2m) is

    sum_(b=0)^m binom(2m,2b)=2^(2m-1)<=2^(2m),

and for m=0 it equals1. Submultiplicativity of the coefficient sum therefore gives

    coefficient_sum(P_(m,k))<=2^(k+m).                         (4)

Each monomial has homogeneous degree n=2k. An ordered l-fold partial derivative of a degree-n monomial has coefficient factor at most (n)_l, and its absolute value on |X|=r is at most that coefficient times r^(n-l). Consequently, for any particular ordered derivative of P,

    |partial_I P(X)| <= (2k)_l 2^(k+m) r^(2k-l), l<=2k.        (5)

It is zero for l>2k. At r=0 the usual convention for the constant term applies.

To differentiate (1+r^2)^q d times, partition the d ordered differentiations among first and second derivatives of 1+r^2. No block can have size greater than2. If there are z pairs and s=d-2z singletons, the number of partitions is d!/(s! z! 2^z). A singleton contributes a factor bounded by2r; a pair by2. The outer derivative is (q)_(d-z)(1+r^2)^(q-d+z). Since r^s<= <r>^s,

    |partial_I (1+r^2)^q| <= R_d(q) <r>^(2q-d).               (6)

The identity 2q-2d+2z+s=2q-d gives the exponent. Absolute values of falling factorials handle all signs of q; no positivity assumption on q is used.

## 3. Product, tensor and field bounds

For a specified ordered d-fold derivative of one generator, Leibniz' rule has binom(d,l) terms in which l derivatives hit P. Combining(5),(6) and r^(2k-l)<= <r>^(2k-l), each term has common radial exponent

    2k-l+2(p_j-k)-(d-l)=3+gamma-j delta-d.

There are 2^d ordered Cartesian tensor components. Their Euclidean norm is at most 2^(d/2) times the maximum component, bounded in turn by 2^d times that maximum. This proves

    |D^d[P_(m,k)(1+r^2)^(p_j-k)]|
        <= S_d(j,m,k)<r>^(3+gamma-j delta-d).                  (7)

Since j delta>=0 and <r>>=1, summing with |a|<=b proves the first inequality of(3).

For an ordered q-fold derivative of rho, the defining expression is a sum of two selected (q+3)-fold potential derivatives. Squaring and summing gives

    |D^q rho|<=sqrt(2)|D^(q+3)chi|<=2|D^(q+3)chi|.

The selected derivatives of the two velocity components form a subset of the full ordered tensor, so the same constant2 is also valid for u. With d=6, multiplication by <r> for D^3u yields exponent gamma-2<0, and multiplication by <r>^2 for D^3rho yields gamma-1<0. With d=7, multiplication by <r>^2 yields gamma-2<0. Dropping these nonpositive powers proves the other three inequalities of(3).

All functions in(1) are smooth because 1+r^2 never vanishes. Formula(7) for arbitrary fixed d also proves that every derivative has polynomial growth. This supplies the additional smoothness and growth condition used in the logarithmic generator construction, separately from its quantitative energy hypotheses.

## 4. Exact input recovery and reproducible certificate

The original is recovered directly from the read-only state131 checkpoint, using exact binary64 hex values, its center-strain constraint and the integer shifted-Legendre expansion. Its reconstructed canonical serialization must equal the original checkpoint's recorded hash and its own independent source audit. The two refits are recovered directly from their exact producer JSON and compared with the independently reconstructed canonical arrays and hashes in19 and52. The calculation does not import producer evaluation code.

For each finite canonical array, the verification chooses b=ceil(|a|), computes the rational quantities in(2) at d=6,7, and rounds 2C_6,2C_7 upward to powers of2. It then applies the exact parameter choices in89 to these caps, recording Astar, Kstar and an admissible positive dyadic tau. All scalar choices, coefficient inputs, source hashes and proof dependencies are stored in JSON. A separate computation verifies the radial combinatorial formula from a derivative recurrence and checks the polynomial coefficient estimate on a finite diagnostic set; the analytic proof above covers every generator.

No large numeral table is embedded in mathematical or formal source. No spatial integration or numerical fit is used. The resulting caps may be far larger than sharp derivative bounds. Their purpose is a rigorous finite certificate and a concrete parameter choice, not an improved residual or a claim that the remaining reference contract holds.
