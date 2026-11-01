# Gevrey bounds determined by the retained low logarithms

Status: PROVED after the independent review in V312. This concerns a modified finite-edge recursion, not the full stationary IPM equation.

## Statement

Let delta=a/b belong to (0,1), in lowest terms, and put c=(1-delta)^(-1). Let F_1 be a nonzero finite real sine polynomial supported at positive odd frequencies, with largest frequency L. Fix an integer K>=1. Generate polynomial-log density and stream coefficients F_n(t,theta), G_n(t,theta), with t=log r, by the canonical stationary recursion, retaining precisely the ordered pairs (i,j) with i+j=n and min(i,j)<=K. Every ordered pair is counted once. At every stream resonance, set the constant of the entire resonant output mode to zero.

For 1<=i<=K, let d_i=max(deg_t F_i,deg_t G_i,0), taking degree zero for a zero polynomial, and set

    sigma=max_(1<=i<=K) d_i/i.

Then constants C_0,A>0, explicitly given below in terms of finitely many coefficients, satisfy

    ||F_n||_s <= C_0 A^n (n!)^sigma,
    ||G_n||_s <= C_P C_0 A^n (n!)^sigma,     n>=1,       (1)

where

    d_*=gcd(a,2)/b, s=C_P=2/d_*, r_*=1/s,
    ||H||_s=sum_(q>=0) q! s^q ||[t^q]H||_0.

Here ||.||_0 is the sum of absolute sine coefficients, equivalently the Fourier Wiener norm on the indicated parity space. Products use the full Fourier Wiener norm, which is submultiplicative. The symbol r_* is a norm constant and is not the spatial radius.

If sigma=0, these bounds imply convergent exterior density and stream series with every fixed natural weighted derivative. If sigma>0, (1) is only a Gevrey upper bound. It proves neither convergence nor divergence.

For delta=2/q_0 with an integer q_0>=3, one may use the explicit upper bound

    sigma <= 0,                                  K<2q_0,
    sigma <= (m-1)/(q_0 m) < 1/q_0,               K>=2q_0,
    m=floor(K/q_0).                                         (2)

In particular, at delta=2/3, K=10 admits order2/9 and K=30 admits order3/10, both strictly smaller than the general order1/3 bound. These are sufficient Gevrey orders, not optimality claims.

## Recursion and linear estimates

Write p_n=1-n delta, P_n=2-n delta, D=partial_t and lambda_n=(n-1)(c-1). The density recurrence is

    (lambda_n-cD)F_n
      =sum_((i,j) retained) [(P_i+D)G_i F_j' - G_i'(p_j+D)F_j],   (3)

where a prime means partial_theta. The Poisson relation is

    -[(P_n+D)^2+partial_theta^2]G_n
      =cos(theta)(p_n+D)F_n-sin(theta)F_n'.                     (4)

For a density mode A(t)sin(m theta), each allowed stream incidence has coefficient -1/2 times the inverse of D+P_n+m+1 or D+P_n-m+1, respectively. Zero stream frequency is omitted. A zero shift is inverted by integration from zero, and the entire constant at a resonant output frequency is then deleted. Thus (3)-(4) determine finite polynomials inductively.

The norm of D is at most r_* because (q-1)!s^(q-1)q/(q!s^q)=1/s. Every nonzero Poisson shift has modulus at least d_*. Its finite inverse series has norm at most1/(d_*-r_*)=C_P. Integration from zero also has norm s=C_P. The two half-weighted angular incidences and the contractive resonant deletion give

    N_n:=||G_n||_s <= C_P M_n,  M_n:=||F_n||_s.                (5)

Since d_*<=delta and c delta=c-1,

    ||(lambda_n-cD)^(-1)||
       <= 1/[(c-1)(n-3/2)],                  n>=2.            (6)

These bounds apply to all finite polynomial degrees. They follow from finite Neumann sums, bounded above by the indicated convergent geometric series.

Set B=L+1. Direct support induction gives

    maxfreq(F_n)<=Bn-1,   maxfreq(G_n)<=Bn.

For completeness the degree bound needed below is deg F_n,deg G_n<=floor(n/q_0), where q_0=2b/gcd(a,2). It follows by adding the input degrees in (3), observing that the stationary inverse does not raise degree, and that a stream degree can rise only at n a/b=2(j+1), hence at a multiple of q_0. The sharper bounds are

    deg F_n<=max(0,floor((n-1)/q_0)-epsilon),
    deg G_n<=max(0,floor(n/q_0)-epsilon),                      (7)

with epsilon=1 if a/gcd(a,2)=1 and zero otherwise. To verify the induction, the degree in every forcing product is bounded by the sum of the stream bound at i and the density bound at j. The floor inequality bounds this by the density bound at i+j. For epsilon=1, use max(0,u-1)+max(0,v-1)<=max(0,u+v-1). At a genuine resonance the stream bound is one larger than the density bound, and otherwise they agree. Omitting products preserves each upper bound. In particular every product appearing at order n has total log degree at most n.

## Multiplication by a fixed low-degree factor

Suppose U has degree at most d and V is another polynomial such that deg U+deg V<=n, with n>=1. A product of a degree-l coefficient of U and a degree-q coefficient of V acquires the factor

    (q+l)!/(q!l!) = binomial(q+l,l) <= n^l <= n^d.

The angular Wiener product inequality and summation over l,q yield

    ||UV||_s <= n^d ||U||_s ||V||_s.                         (8)

Angular derivatives preserve log degree; D lowers it. Thus (8) applies to each differentiated factor in (3) with d=d_i when the low index is i. This polynomial loss is the only extra cost compared with a log-independent low factor.

## A finite-memory inequality

For each i<=K put H_i=||F_i||_s and Q_i=||G_i||_s, and define

    b_i=4B/[3(c-1)] * {
        [|P_i|+r_*+i(1+r_*)]Q_i
        +C_P[i(2-delta+r_*)+|p_i|+r_*]H_i } .               (9)

If n>2K, every retained pair has exactly one low index i<=K. Its other index j=n-i is larger than K, so j>=2, and the two orientations are distinct. Bounds (8), |p_j|<=j, |P_j|<=(2-delta)j, and the angular support estimate give

    ||(P_i+D)G_i F_j' - G_i'(p_j+D)F_j||_s
      <= B j n^(d_i) [|P_i|+r_*+i(1+r_*)]Q_i M_j,

    ||(P_j+D)G_j F_i' - G_j'(p_i+D)F_i||_s
      <= B j n^(d_i) [i(2-delta+r_*)+|p_i|+r_*]H_i N_j.

Here r_*<=j r_* is sufficient; no derivative on a low logarithm is discarded. Apply (5)-(6) and use j/(n-3/2)<=4/3, since n>=3 and j<=n-1. The result is

    M_n <= sum_(i=1)^K b_i n^(d_i) M_(n-i),    n>2K.       (10)

Every b_i is a finite, explicitly determined nonnegative number.

## Gevrey induction

Define b_i'=2^(sigma i)b_i and choose

    A=max(1,2 sum_(i=1)^K b_i'),
    C_0=max_(1<=n<=2K) M_n/[A^n(n!)^sigma].                (11)

The first2K inequalities in (1) hold by definition. For n>2K and i<=K, every factor of n!/(n-i)! is greater than n/2. Since d_i<=sigma i,

    n^(d_i) [(n-i)!/n!]^sigma
       <= 2^(sigma i) n^(d_i-sigma i)
       <= 2^(sigma i).                                   (12)

Assuming (1) at smaller orders and substituting into (10) gives

    M_n/[C_0 A^n(n!)^sigma]
      <=sum_(i=1)^K b_i' A^(-i)
      <=sum_(i=1)^K b_i'/A <=1/2.

This closes the induction; (5) supplies the stream estimate. Positivity of C_0 follows from F_1 nonzero.

When sigma=0, factorial weights imply ||H(t)||_0<=exp(|t|/s)||H||_s. For any spatial radius R>A^(1/delta), sufficiently late terms of the normalized series r^(-1)rho and r^(-2)psi are dominated uniformly for r>=R by a geometric series, because exp(log(r)/s)=r^(1/s) is a fixed power. The finitely many earlier terms are harmless. The leading-growth normalization r^(-1+delta)rho is handled in the same way. Angular derivatives cost at most (Bn)^j, radial derivatives polynomial factors in n together with bounded powers of D, so each fixed differentiated series also converges. A sufficiently small complex angular strip and a local complex logarithm preserve the strict geometric margin. This proves the asserted convergence statement. Nothing in this argument removes (n!)^sigma when sigma>0.

## The explicit improvement for delta=2/q_0

Here a/gcd(a,2)=1 after reduction, so epsilon=1 in (7). Therefore

    d_i<=max(0,floor(i/q_0)-1).

If K<2q_0 this vanishes. Otherwise, on the block q_0 l<=i<q_0(l+1), the quotient is at most(l-1)/(q_0 l), attained by this bound at the first index of the block. This value increases with l. The largest block present is l=m=floor(K/q_0), proving (2). At delta=2/3 and K10 this is(3-1)/9=2/9; at K30 it is(10-1)/30=3/10. Actual vanishing low columns can lower sigma further.

For general rational delta, (7) gives sigma<=1/q_0. A strict improvement is not asserted when a/gcd(a,2)>=2: the first resonant low coefficient can already have d_(q_0)=1.

## Dependencies and scope

The recurrence and common-potential consistency are independently derived in topics01 and10. The degree induction is the same elementary induction as topic17, repeated here. The factorial Poisson estimate is topic89, repeated in (5), and the log-independent special case is topic107. This proof uses no extrapolation from numerical columns and no externally invoked existence theorem.

The equation represented by an edge recurrence retains only min(i,j)<=K. A bound for it is not a bound for the unrestricted quadratic recursion. Even a strictly smaller positive Gevrey order does not imply that the corresponding series diverges, converges, is Borel summable, or has an optimal truncation error of a stated size.
