# What the finite-edge hierarchy does and does not control

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

The K-edge experiments agree with the full recurrence for a growing finite prefix. Their highest Fourier coefficients also admit an all-order comparison. This comparison gives a useful test of the implementation, but it does not compare the full density or stream norms.

## Highest-mode comparison

Fix delta in (0,1), c=(1-delta)^(-1), and a nonzero finite real sine leading profile with positive odd frequencies. Let L be its largest frequency and alpha its nonzero coefficient there. Put B=L+1, d=c-1, eta=B-delta. Generate the canonical polynomial-log stationary recurrence, using the zero constant of the whole resonant stream mode. Let K be a positive integer, and let the K-edge recurrence retain precisely the ordered pairs with min(i,j)<=K. Write A_(n,K)(t) for the coefficient of sin((Bn-1)theta) in its density polynomial. A_(n,infinity) denotes the full recurrence.

Then every A_(n,K) is constant in t, and

    A_(n,K)=(-1)^(n-1) alpha^n h_(n,K),  h_(1,K)=1.

For all n and K,

    0<h_(n,K)<=h_(n,K+1)<=h_(n,infinity).                    (1)

The K-edge sequence agrees with the complete density and stream sequence through n=2K+1. Its first difference is exactly n=2K+2. With m=K+1, the top-coefficient difference there is

    h_(2m,infinity)-h_(2m,K)
      = [2Bm/(eta m+2)-1] h_(m,infinity)^2 / [4d(2m-1)] > 0. (2)

In fact h_(n,K)<h_(n,K+1) for every n>=2K+2.

Let H_K(z)=sum_(n>=1)h_(n,K)z^n and H(z)=H_infinity(z). Topic38 proves that H has the finite positive radius

    R_H=4d [a Beta(a,b)]^(1/a),
    a=2/eta, b=2(B-1)/eta,
    Beta(a,b)=integral_0^1 u^(a-1)(1-u)^(b-1)du.

For 0<r<r'<R_H,

    sup_(|z|<=r)|H(z)-H_K(z)|
       <=(r/r')^(2K+2) H(r').                               (3)

Thus every H_K converges at least on |z|<R_H, and the highest-mode generating functions converge uniformly to H on compact subsets of that disk. Their radii are nonincreasing in K and bounded below by R_H. No equality or convergence of those radii is asserted.

## Proof of the comparison

The support bound at order n is Bn-1 for density and Bn for stream. A product reaches the top output frequency only by multiplying the top input frequencies. The top stream coefficient is

    T_(i,K)=-A_(i,K)/[2(eta i+2)].

Its denominator is positive. All added resonant stream modes have frequency i delta-2<Bi and cannot affect it. Starting from the log-independent leading term, induction shows that both top coefficients remain log-independent. Direct multiplication of the top sine modes gives

    h_(n,K)=1/[4d(n-1)]
       sum_(i+j=n, min(i,j)<=K)
          [2Bj/(eta i+2)-1] h_(i,K)h_(j,K).                 (4)

The retained pair set is symmetric in i,j, so the bracket in (4) may be replaced by

    C_(i,j)=B[j/(eta i+2)+i/(eta j+2)]-1.

Every such C is strictly positive. Indeed,

    j/(eta i+2)+i/(eta j+2)-2(i+j)/(eta(i+j)+4)
      = eta[eta(i+j)+2](i-j)^2 /
        [(eta i+2)(eta j+2)(eta(i+j)+4)] >= 0,

and therefore C_(i,j)>=[(B+delta)(i+j)-4]/[eta(i+j)+4]>0.
Here i+j>=2, B>=2, and delta>0 give the last strict inequality.

The symmetric positive form of (4) proves positivity. Induction on n proves (1), since increasing K only adds nonnegative summands and increases preceding factors. No pair is omitted when n<=2K+1. At n=2K+2 the only omitted pair is (K+1,K+1), and all its inputs agree with the full sequence. This proves (2). It also proves the first strict comparison with K+1. The retained pair (1,n-1) has a positive symmetric coefficient, so induction propagates strictness to every larger n.

The beta-integral radius for H is the already confirmed topic38 theorem, whose hypotheses are exactly the present B>=2 and delta in (0,1). By positivity, the differences in (1) are dominated coefficientwise by h_(n,infinity). They vanish through 2K+1. Thus for |z|<=r,

    |H(z)-H_K(z)|
      <=sum_(n>=2K+2) h_(n,infinity) r^n
      <=(r/r')^(2K+2) sum_(n>=2K+2)h_(n,infinity)(r')^n,

which proves (3). Coefficientwise monotonicity and the power-series root test give the asserted ordering of radii. These arguments concern one coefficient at each order, and provide no monotonicity of all Fourier coefficients or their norms.

## A scalar counterexample to passing from every fixed edge to the full recurrence

Define positive real numbers by

    x_1=1,
    x_n=sum_(i+j=n) min(i,j)! x_i x_j, n>=2.                (5)

For each fixed K define x_(1,K)=1 and use the same sum restricted to min(i,j)<=K. Then every power series sum x_(n,K)z^n has positive radius, whereas the full series sum x_n z^n has radius zero. Moreover x_(n,K)=x_n for n<=2K+1 and x_(n,K)<=x_(n,K+1)<=x_n for every n.

The prefix agreement and comparison follow by the same positive induction. For n>2K, every retained pair has exactly one low index, and

    x_(n,K)=sum_(i=1)^K c_i x_(n-i,K),
    c_i=2 i! x_(i,K).

Set A=max(1,2 sum_i c_i) and C=max_(1<=n<=2K)x_(n,K)/A^n. The initial inequalities hold by definition, and the finite-memory recurrence gives

    x_(n,K)/(C A^n)<=sum_i c_i A^(-i)<=1/2.

This proves a geometric bound for every fixed K. For the full recurrence x_n>=1 by induction. Its central summand gives x_(2m)>=m! x_m^2>=m!. Since m!>=(m/2)^(floor(m/2)), the subsequence x_(2m)^(1/(2m)) is unbounded and the full radius is zero.

This example disproves the general implication that convergence for every fixed edge cutoff, together with exact growing-prefix agreement and positive coefficientwise monotonicity, forces convergence of the unrestricted quadratic recurrence. A uniform bound in K would be additional information. The example does not show divergence of the IPM sequence, whose highest-mode series actually has the positive radius above.

## Dependencies, checks and scope

The canonical recurrence and signs are independently derived in topics01 and10. Topic38 proves the full highest-mode recurrence and its exact radius; the present proof repeats the algebra needed for the comparison. Topic102 gives the exact Cartesian K1/K3 reference through order18. The planned finite check uses exact rational arithmetic to compare those top coefficients, both forms of the kernel, the first omitted pair, and the scalar counterexample. It is verification evidence for finite identities, not a replacement for either proof.
