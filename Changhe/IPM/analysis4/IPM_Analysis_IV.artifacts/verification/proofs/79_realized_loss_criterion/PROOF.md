# A sufficient criterion in terms of realized logarithmic losses

Status: CONFIRMED after the theory part's independent06:16Z review and the verifier's recheck. The conditional theorem is PROVED, including every rational delta in(0,1). Its all-order loss hypotheses have not been proved for the actual infinite IPM sequence.

## Statement

Let Q>=3 be an integer, delta=2/Q, c=Q/(Q-2), and let the nonzero leading datum be a finite real S1 sine polynomial. Write F for its sine coefficient norm and L for its largest frequency. Use the canonical polynomial-log recursion, with every resonant stream constant zero. Set t=log r,

\[
 p_j=1-j\delta,\quad P_i=2-i\delta,\quad
 \lambda_n=(n-1)(c-1),\qquad
 \|H\|_!=\sum_{q\ge0}q!\|[t^q]H\|_{\ell^1}.
\]

Let S_n be the exact signed quadratic forcing in the density equation

\[
 (\lambda_n-cD_t)F_n=S_n.
\]

Suppose there are finite constants B,T>0 such that, for every relevant order,

\[
 \|G_n\|_!\le B\|F_n\|_!,                                      \tag{1}
\]

\[
 \|S_n\|_!\le T\sum_{i+j=n}w_{i,j}\|G_i\|_!\|F_j\|_!,
\quad
 w_{i,j}=(L+1)\{j(|P_i|+1)+i(|p_j|+1)\}.                       \tag{2}
\]

These are inequalities for the actual generated sequence, not assertions about arbitrary inputs to the quadratic map. Define

\[
 K=(Q-2)(L+1)(5-4/Q)BT,\qquad A=4KF.
\]

Then

\[
 \|F_n\|_!\le\frac F n A^{n-1},
 \qquad \|G_n\|_!\le\frac{BF}n A^{n-1}.                        \tag{3}
\]

For every R>A^(1/delta), the density, stream and compatible original potential series converge absolutely and uniformly on r>=R in each natural weighted Cartesian derivative norm. Their sums are real analytic exterior solutions of the stationary potential equation. This theorem does not establish (1) or (2), nor a global stationary extension.

## Proof of the scalar majorant

The factorial norm gives ||D_t H||_!<=||H||_!. The first genuine stream resonance is at n=2Q: at n=Q the radial stream exponent is zero, while all stream angular frequencies are nonzero and even. Therefore every density F_n for n<=2Q is independent of t. For those orders,

\[
 n\|F_n\|_!\le\frac n{\lambda_n}\|S_n\|_!
 =\frac{(Q-2)n}{2(n-1)}\|S_n\|_!
 \le(Q-2)\|S_n\|_!.
\]

For n>=2Q+1 the finite Neumann inverse, the factorial derivative bound, and lambda_n>c imply

\[
 n\|F_n\|_!\le\frac n{\lambda_n-c}\|S_n\|_!
 =\frac{(Q-2)n}{2n-Q-2}\|S_n\|_!
 \le(Q-2)\|S_n\|_!,
\]

since n>=Q+2. Thus the same estimate holds at every n>=2.

For every positive integer i and 0<delta<1,

\[
 |2-i\delta|+1\le(3-\delta)i,\qquad
 |1-i\delta|+1\le(2-\delta)i.
\]

For a nonnegative expression inside the absolute value these follow by moving the constant term to the right and using i>=1. In the negative case the two left sides equal i delta-1 and i delta, respectively, and the inequalities follow from delta<1. Consequently

\[
 w_{i,j}\le(L+1)(5-2\delta)ij.
\]

Put Y_n=n||F_n||_!. Combining the preceding bounds with (1)-(2) gives

\[
 Y_1=F,\qquad Y_n\le K\sum_{i+j=n}Y_iY_j.
\]

The equality recursion has solution Y_n=Cat_(n-1)K^(n-1)F^n. Induction and Cat_(n-1)<=4^(n-1) prove (3).

## Potential and exterior convergence

The joint reconstruction in topic41 applies also in the factorial norm. Here are the needed changes explicitly. Its Euler identity has the factors (q-1+D_t)(q-2+D_t), q=4-n delta. For X=n delta>=20, their inverse norms are at most 4/X each, because ||D_t||<=1<=X/2. Its angular derivative bound remains (L+1)n, and its radial multiplier is bounded by 3X/2. Hence its estimate for V=r^(1-q)partial_y chi remains valid:

\[
 \|V_n\|_!\le \frac{16}{X^2}
 \{\|F_n\|_!+n(L+1+3\delta/2)\|G_n\|_!\}.
\]

The inverse y-derivative matrix T(q+z) in topic41 satisfies ||T_h||<=3s^(-h), where s=3(X-5)/4. Substitution z=D_t now costs at most sum_h 3s^(-h)<=27, since 1/s<=8/9 for X>=20. It therefore gives a compatible potential with

\[
 \|C_n\|_!\le \frac{432}{X^2}
 \{\|F_n\|_!+n(L+1+3\delta/2)\|G_n\|_!\}.                  \tag{4}
\]

All inverses preserve the stated finite angular and log degrees. The finite early potential coefficients exist by the canonical potential reconstruction and can be absorbed into a constant. Equations (3)-(4) consequently give geometric factorial-norm bounds for all three fields.

For any polynomial H,

\[
 \|H(t)\|_{\ell^1}\le e^{|t|}\|H\|_!,
\]

because |t|^q/q!<=e^(|t|). A fixed Cartesian derivative costs at most a fixed polynomial in n in the factorial coefficient norm: angular frequencies and radial exponents grow linearly, while D_t has norm at most one. After removing the prescribed leading radial weight, a large-order term is therefore bounded by a constant times

\[
 n^h A^{n-1}e^{|\log r|}r^{-\delta(n-1)}.
\]

On r>=max(R,1), once delta(n-1)>1, the radial factor is decreasing and its maximum is at the left endpoint. On a possible compact interval R<=r<=1, e^(|log r|)<=1/R. Both estimates yield a summable series because A R^(-delta)<1. The finite early terms with n>=2 have a negative power r^(-delta(n-1)) times a finite polynomial in log r, hence bounded weighted norms. The leading terms have no logarithms. This proves all weighted uniform derivative assertions.

In a small complex neighborhood of any exterior point, the logarithm is analytic, and the finite angular bandwidth costs at most an additional geometric factor in n. The strict margin A r^(-delta)<1 absorbs that factor, so the sums are real analytic. Absolute convergence permits the formal stationary products to be regrouped, and the three potential identities pass to the limit. This proves the conditional exterior statement.

## Uniform deficit rates also need boundary control

A second sufficient criterion clarifies what a uniform deficit rate would need to mean. Suppose nonnegative values a_(k,d), 0<=d<=k-1, obey

\[
 a_{d+1,d}\le C A_0^{d+1},\qquad
 a_{k+1,d}\le \Lambda a_{k,d}\quad(k>=d+1),
\]

with constants independent of d. Then

\[
 a_{k,d}\le C A_0^{d+1}\Lambda^{k-d-1}
 \le C\max(A_0,\Lambda)^k.
\]

The sum over d has at most k terms and is therefore exponentially bounded. For factorial-weighted fixed-deficit columns, the initial value is the degree-zero column at the first admissible block. The conclusion must be applied to each residue class and to both density and stream.

A uniform step ratio by itself is insufficient. The explicit polynomials

\[
 H_k(t)=\sum_{d=0}^{k-1}2^{d^2-k}
          \frac{t^{k-1-d}}{(k-1-d)!}
\]

have factorial-weighted fixed-deficit amplitudes a_(k,d)=2^(d^2-k), so every admissible fixed-d step ratio is exactly 1/2. Nevertheless

\[
 \|H_k\|_!\ge 2^{(k-1)^2-k},
\]

which grows faster than any geometric sequence. In fact their ordinary generating series has radius zero at every t>=0. This is an exact scalar counterexample to omitting uniform initial bounds or uniform control of the onset of the rate estimate. It is not an IPM counterexample.

## Extension to every rational exponent

The same conditional criterion holds for every rational delta in (0,1), with c=(1-delta)^(-1), if its constant is written as

\[
 K=\frac{2(L+1)(5-2\delta)BT}{c-1},\qquad A=4KF.
 \tag{5}
\]

Here is the only change in the proof. A genuine stream resonance requires 2-n delta to be a nonzero even integer. Since n>0 and 0<delta<1, the first such negative integer is at most -2. Thus every possible first genuine resonance order N0 satisfies N0 delta>=4. Before that order the canonical stream and density coefficients contain no logarithms, and F_(N0) also has no logarithms.

For constant density polynomials, n/lambda_n<=2/(c-1). For all potentially nonconstant orders n>=N0+1, one has n>=4/delta+1>2+2/delta, so

\[
 \frac{n}{\lambda_n-c}
 =\frac1{c-1}\frac{n}{n-1-1/\delta}
 \le\frac2{c-1}.
\]

This replaces Q-2 by 2/(c-1), with the same product estimate and Catalan argument. The first resonance may be compatible or absent from the actual support; that only postpones the appearance of logarithms and does not weaken the bound. The potential reconstruction and exterior convergence argument are unchanged. At delta=2/Q, (5) is exactly the earlier constant.

## Dependencies and scope

The proof uses the canonical log recurrence and first-resonance count, elementary factorial norms, the Catalan recursion, and the independently reviewed joint potential reconstruction of topic41. Numerical checks of B, T, or deficit rates over finite ranges only test the hypotheses over those ranges. No extrapolation to all orders is part of this result.
