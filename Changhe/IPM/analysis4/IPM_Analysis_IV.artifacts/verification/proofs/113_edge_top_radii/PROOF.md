# Exact radii of the highest-mode edge hierarchy

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement and notation

Let delta belong to (0,1), c=(1-delta)^(-1), and d=c-1. Let the leading density be a nonzero finite real sine polynomial supported at positive odd frequencies, with largest frequency L and coefficient alpha at that frequency. Set B=L+1 and eta=B-delta. In the canonical polynomial-log IPM recurrence, retain exactly the ordered pairs (i,j) with i+j=n and min(i,j)<=K, where K>=1 is fixed. At resonances the whole output stream constant is zero.

Let A_(n,K) be the coefficient of sin((Bn-1)theta). It is independent of log r, and has the form

    A_(n,K)=(-1)^(n-1) alpha^n h_(n,K),  h_(1,K)=1,

with strictly positive h_(n,K). Let h_n denote the corresponding full highest-mode coefficient. For i<=K, h_(i,K)=h_i. Define the positive polynomial

    V_K(z)=sum_(i=1)^K h_i z^i/(eta i+2),

and let R_K be its unique positive solution of

    V_K(R_K)=2d/B.                                         (1)

Then the ordinary limit exists and satisfies

    lim_(n->infinity) h_(n,K)^(1/n)=1/R_K.                 (2)

Thus sum h_(n,K)z^n has exact radius R_K. The unnormalized highest-mode series has radius R_K/|alpha|. At any fixed real logarithmic variable t, the power series whose coefficients are the full modified density polynomials evaluated at t has radius in the angular Wiener norm of strip sigma at most exp(-B sigma) R_K/|alpha|. The same bound holds for any norm on the log coefficients that dominates evaluation of the constant top coefficient.

Let

    a=2/eta, b=2(B-1)/eta,
    R_H=4d [a Beta(a,b)]^(1/a),
    Beta(a,b)=integral_0^1 t^(a-1)(1-t)^(b-1) dt.

The full highest-mode series has radius R_H. The edge radii satisfy

    R_K>R_(K+1)>R_H,
    R_K decreases to R_H,
    0<R_K-R_H <= 4d(eta+2)/[eta(K+1)+2].                 (3)

For K=1, the formula is explicit:

    R_1=2d(eta+2)/B.

At delta=2/3 and B=2 this gives R_1=20/3 and limiting normalized top-coefficient root3/20. This is not the finite-order root of the entire edge density norm.

## Exact finite-memory recurrence

The top-mode trigonometric calculation in topics38 and112 gives

    h_(n,K)=1/[4d(n-1)]
      sum_(i+j=n, min(i,j)<=K)
         [2Bj/(eta i+2)-1] h_(i,K) h_(j,K).             (4)

Pairing the two orientations gives the positive kernel

    B[j/(eta i+2)+i/(eta j+2)]-1>0.

Indeed the bracketed sum is at least2(i+j)/[eta(i+j)+4], by putting the difference over its positive common denominator. The resulting numerator of the kernel lower bound is(B+delta)(i+j)-4>0. Thus all h_(n,K) are positive. Every index n<=2K+1 retains all pairs, so induction gives h_(n,K)=h_n on that prefix, including all i<=K.

For n>2K, every retained pair has exactly one index i<=K; the other j=n-i is larger than K. Each orientation occurs exactly once. Hence

    h_(n,K)=sum_(i=1)^K q_(n,i) h_(n-i,K),

    q_(n,i)=h_i/[2d(n-1)] * {
                  B[(n-i)/(eta i+2)+i/(eta(n-i)+2)]-1 }.
                                                               (5)

The coefficients are positive and have limits

    c_i=lim_n q_(n,i)=B h_i/[2d(eta i+2)]>0.             (6)

A useful exact bound follows by division:

    q_(n,i)/c_i
       =1+{1-i-(eta i+2)/B
                  +i(eta i+2)/(eta(n-i)+2)}/(n-1).

Since n-i>i and eta i+2>B,

    0<q_(n,i)<c_i,
    q_(n,i)/c_i >=1-D_i/(n-1),
    D_i=i-1+(eta i+2)/B.                               (7)

These inequalities are sufficient to determine the radius. They involve only positive finite-memory recurrences, so no complex singularity theorem is needed.

## Determining the coefficient root

Put lambda=1/R_K. Equation(1) is exactly

    sum_(i=1)^K c_i lambda^(-i)=1.                     (8)

Its positive solution exists and is unique because the left side is continuous, strictly decreasing from infinity to zero as lambda increases from zero to infinity. Let

    C=max_(1<=n<=2K) h_(n,K)/lambda^n.

The initial bounds h_(n,K)<=C lambda^n hold by definition. Equations(5), (7) and(8) propagate them for n>2K. Thus limsup h_(n,K)^(1/n)<=lambda.

For a lower bound fix epsilon in(0,1). Choose an integer n_e>2K such that n_e-1>=max_i D_i/epsilon. Then q_(n,i)>=(1-epsilon)c_i for n>=n_e. Let lambda_e be the unique positive solution of

    (1-epsilon) sum_(i=1)^K c_i lambda_e^(-i)=1.

It satisfies lambda_e<lambda and tends to lambda as epsilon decreases to zero, by continuity and strict monotonicity of the same scalar polynomial equation. Positivity gives

    C_e=min_(1<=n<n_e) h_(n,K)/lambda_e^n>0.

Using(5) from n_e onward proves h_(n,K)>=C_e lambda_e^n by induction. Therefore liminf h_(n,K)^(1/n)>=lambda_e for every epsilon. Let epsilon tend to zero. This proves(2), and the Cauchy-Hadamard root test gives the exact radius.

For the angular consequence, the sine coefficient functional is bounded on C^0, and the Wiener norm dominates |A_(n,K)| exp(sigma(Bn-1)). Taking nth roots gives the stated upper bound for the full modified sequence. It gives no lower bound for that full sequence.

## Limit of the radii and an explicit error bound

Topic38 proves that

    H(z)=sum_(n>=1)h_n z^n,
    J(z)=sum_(n>=1)h_n z^n/(eta n+2)

have the positive real boundary values

    H(R_H)=4d,  J(R_H)=2d/B.                            (9)

For completeness, the beta-integral parametrization is H=4dx,

    z=4d[a Beta_x(a,b)]^(1/a),
    1-BJ/(2d)=x^a(1-x)^b/[a Beta_x(a,b)],

for0<x<1. Since b>1, as x increases to1 the right-hand side of the second identity tends to zero. Nonnegative coefficients justify the boundary sums in(9) by monotone convergence. This is the only boundary information used here.

Every omitted coefficient in J is positive, so V_K(R_H)<2d/B and R_K>R_H. Adding its positive(K+1)st term makes V_(K+1)(R_K)>2d/B, hence R_(K+1)<R_K.

Let

    tau_K=J(R_H)-V_K(R_H)
         =sum_(i>K) h_i R_H^i/(eta i+2)>0.

Because V_K'(z)>=1/(eta+2) for every positive z, integration between R_H and R_K gives

    R_K-R_H <=(eta+2) tau_K
       <= (eta+2)/[eta(K+1)+2] sum_(i>K)h_i R_H^i
       <=4d(eta+2)/[eta(K+1)+2].                       (10)

The bound tends to zero, proving the limit and(3). No inference about the radius of the full angular series follows from this particular coefficient limit.

## Dependencies and verification

The recurrence, canonical normalization and top-frequency support are established independently in topics01,10 and38. Topic38 supplies the beta-integral formula and the boundary values. Topic112 provides an independently written comparison proof and a scalar example showing that finite-edge convergence does not by itself control unrestricted recurrences. The present argument uses the actual IPM top-frequency coefficients and their positive limiting finite-memory recurrence.

Planned verification checks(5)-(7) against exact rational coefficients for several rational delta, B and K, compares the independently computed Cartesian K1/K3 top coefficients, and brackets the roots of(1) with exact rational endpoints. Finite checks supplement the proof. Their completion and an independent theory-part review are recorded in the chronological verification ledger (not included).
