# A plain-norm criterion involving only the realized stream ratio

Status: PROVED as a conditional theorem, after the independent theory-part review at2026-10-31T06:46Z and closure V151. Its single all-order hypothesis is not proved for the generated sequence.

## Statement

Let delta=a/b be reduced with0<a<b and c=(1-delta)^(-1). Let f_1 be a nonzero finite real S1 sine polynomial, with highest frequency L and sine coefficient norm F. Use the canonical polynomial-log stationary recursion with every resonant stream constant zero. Write

\[
 q_0=2b/\gcd(a,2),\quad h=a/\gcd(a,2),\quad
 \epsilon=\begin{cases}1&h=1,\\0&h\ge2,\end{cases}
\]

\[
 d_n=\max(0,\lfloor(n-1)/q_0\rfloor-\epsilon),\qquad
 e_n=\max(0,\lfloor n/q_0\rfloor-\epsilon).
\]

For H=sum_(q,m) h_(q,m)t^q sin(m theta), set
||H||_*=sum_(q,m)|h_(q,m)|. Define M_n=||F_n||_* and N_n=||G_n||_*. Suppose there is a finite H_0>0 such that

\[
 N_n\le H_0 M_n\qquad(n\ge1).                         \tag{1}
\]

Put

\[
 C_0=3-\delta+2/q_0\le3,\qquad
 K=\frac{2H_0(L+1)C_0}{c-1},\qquad A=4KF.
\]

Then

\[
 M_n\le\frac F n A^{n-1},\qquad
 N_n\le\frac{H_0F}n A^{n-1}.                          \tag{2}
\]

For any R>e satisfying

\[
 A R^{-\delta}(\log R)^{2/q_0}<1,                     \tag{3}
\]

the density, stream and compatible potential series converge absolutely and uniformly on r>=R in every natural weighted Cartesian derivative norm. Their sums are real analytic and satisfy the original stationary potential equation in the exterior.

For delta2/3,c3,f_1=sin(theta), the hypothesis N_n<=M_n/4 for all n would imply convergence on r>=64. No such all-order inequality is asserted here.

## The stationary inverse in the plain norm

The canonical degree bounds are deg F_n<=d_n and deg G_n<=e_n. We first show

\[
 d_n\le\frac\delta2(n-2)\qquad(n\ge2).                \tag{4}
\]

If h=1, then delta=2/q_0. When d_n>0,
d_n<= (n-1)/q_0-1 <=(n-2)/q_0 because q_0>=1. When d_n=0, (4) follows from n>=2. If h>=2, then1/q_0=delta/(2h)<=delta/4. For n>=3,
d_n<=delta(n-1)/4<=delta(n-2)/2. At n2, d_2=0 because q_0>1. This proves(4).

On polynomials of degree at most d_n, ||D||_*<=d_n, where D=partial_t. With lambda_n=(n-1)(c-1)=c delta(n-1), (4) gives

\[
 \lambda_n-cd_n\ge\frac{c\delta n}{2}>0.
\]

The finite Neumann inverse therefore satisfies

\[
 n\|F_n\|_*\le\frac{2}{c-1}\|S_n\|_*,                \tag{5}
\]

where (lambda_n-cD)F_n=S_n is the exact stationary density equation. This estimate uses the degree of the polynomials, not a uniform derivative bound on an infinite polynomial space.

## The product estimate

The plain polynomial Wiener norm is a Banach algebra: convolution in log degree and in angular Fourier frequency gives ||UV||_*<=||U||_*||V||_*. Starting with frequency at most L, products add frequencies and the Poisson map shifts them by one; induction gives frequencies at most(L+1)n-1 for F_n and(L+1)n for G_n. The angular supports give
||partial_theta F_j||_*<=(L+1)j M_j and
||partial_theta G_i||_*<=(L+1)i N_i.
Also e_i<=i/q_0 and d_j<=j/q_0. For every i,j>=1,

\[
 |2-i\delta|\le(2-\delta)i,\qquad |1-j\delta|\le j.
\]

For the first inequality, divide by i and note 2/i-delta lies between -delta and2-delta, with delta<2-delta. The second follows from |1/j-delta|<=1. Thus

\[
 \begin{split}
 \|S_n\|_*
 &\le(L+1)\sum_{i+j=n}
 \{j(|P_i|+e_i)+i(|p_j|+d_j)\}N_iM_j\\
 &\le(L+1)(3-\delta+2/q_0)
       \sum_{i+j=n}ijN_iM_j.
 \end{split}                                                   \tag{6}
\]

Here P_i=2-i delta and p_j=1-j delta. There is no binomial coefficient loss in this norm. Since delta q_0=2h>=2, one has2/q_0<=delta and C_0<=3.

Set Y_n=nM_n. Equations(1),(5),(6) give

\[
 Y_1=F,\qquad Y_n\le K\sum_{i+j=n}Y_iY_j.
\]

The Catalan majorant is Y_n<=Cat_(n-1)K^(n-1)F^n<=F(4KF)^(n-1). This proves(2).

## Potential and exterior convergence

For X=n delta>=20, the independently proved joint plain-norm reconstruction gives

\[
 \|C_n\|_*\le\frac{432}{X^2}
 \{M_n+n(L+1+3\delta/2)N_n\}.
\]

The potential has degree at most n/q_0 at these orders. The finitely many earlier potential coefficients exist by the formal potential construction, possibly with additional logarithms. Consequently all three plain coefficient norms have geometric bounds with base A after enlarging a constant.

For t=log r>=1 and n>=2, t^(n/q_0)<=t^(2(n-1)/q_0). Each naturally weighted term is bounded by a constant times a fixed polynomial in n times
[A r^(-delta)(log r)^(2/q_0)]^(n-1). Since delta q_0>=2, the bracket decreases for r>=e. Condition(3) therefore gives uniform absolute convergence, including every fixed derivative. The finite early coefficients do not affect this argument. A local complex logarithm and a sufficiently small complex angular neighborhood preserve the strict margin, proving real analyticity. Absolute convergence justifies differentiation, multiplication and regrouping in the original potential identities and stationary equation.

For the stated special case, q_0=3,C_0=3,F=1,L+1=2,c-1=2. If H_0=1/4, then K=3/2 and A=6. Condition(3) at R64 is equivalent to 6^(3/2)log64<64. Since 6^(3/2)<15 and log64=6log2<21/5, their product is less than63<64. The elementary bound log2<7/10 follows, for example, because the first four terms of exp(7/10) already sum to more than2. Thus radius64 is a rigorous conditional radius.

## Dependencies and limits

The degree bounds are proved in topic17; the recurrence is derived in topic01 and its logarithmic form in topic10; the joint potential reconstruction is topic41. The present statement trades a factorial-norm product-loss hypothesis for a uniform realized plain stream/density ratio. General-input counterexamples to a bounded Poisson operator do not decide(1) on the generated sequence. Conversely, checking(1) through finitely many orders is not a proof of its all-order form. Neither necessity of(1) nor unconditional rational convergence is claimed.
