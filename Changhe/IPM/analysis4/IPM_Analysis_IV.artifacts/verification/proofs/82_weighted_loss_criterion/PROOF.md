# A single realized-loss criterion in a weighted factorial norm

Status: PROVED as a conditional theorem, including the smaller constant8b. Independent theory-part review at06:30Z confirmed the stationary refinement. No all-order nonlinear hypothesis has been established for the generated sequence.

## Exact statement

Let delta=a/b be in lowest terms with0<a<b, c=(1-delta)^(-1), and let f_1 be a nonzero finite real S1 sine polynomial of largest frequency L and sine coefficient norm F. Use the canonical polynomial-log recursion, with all resonant stream constants zero. Set s=4b and

\[
 \|H\|_{!,s}=\sum_{q\ge0}q!s^q\|[t^q]H\|_{\ell^1},
 \quad p_j=1-j\delta,\quad P_i=2-i\delta,
 \quad w_{i,j}=(L+1)\{j(|P_i|+1)+i(|p_j|+1)\}.
\]

The exact signed forcing S_n satisfies (lambda_n-c partial_t)F_n=S_n with lambda_n=(n-1)(c-1). Suppose a finite T>0 satisfies, for every n>=2,

\[
 \|S_n\|_{!,s}\le T\sum_{i+j=n}w_{i,j}\|G_i\|_{!,s}\|F_j\|_{!,s}.
 \tag{1}
\]

Define

\[
 K_s=\frac{16b(L+1)(5-2\delta)T}{c-1},\qquad A=4K_sF.
 \tag{2}
\]

Then

\[
 \|F_n\|_{!,s}\le\frac F n A^{n-1},\qquad
 \|G_n\|_{!,s}\le\frac{4bF}n A^{n-1}.
 \tag{3}
\]

For every R>A^(1/delta), the density, stream and compatible potential series converge absolutely and uniformly on r>=R in every fixed natural weighted Cartesian derivative norm. Their sums give a nonzero real analytic exterior solution of the stationary potential equation. This is conditional on (1); no whole-plane stationary extension is asserted.

## Proof

The coefficient norm has

\[
 \|\partial_tH\|_{!,s}\le s^{-1}\|H\|_{!,s},\qquad
 \left\|\int_0^tH\right\|_{!,s}=s\|H\|_{!,s}.
\]

Every nonzero scalar Poisson shift is at least1/b in modulus. Its inverse has norm at most(1/b-1/s)^(-1)=4b/3. The resonant inverse is integration with zero integration constant; the nonresonant channel is adjusted by its constant value to impose the stated stream normalization. The two channels and this adjustment give the already proved estimate of topic17,

\[
 \|G_n\|_{!,s}\le4b\|F_n\|_{!,s}.
 \tag{4}
\]

Thus the stream bound is a theorem, rather than an additional hypothesis on the actual sequence.

For n>=2,

\[
 \frac{c}{s\lambda_n}=\frac1{4a(n-1)}\le\frac14.
\]

The finite Neumann inverse of lambda_n-c partial_t has norm at most2/lambda_n. Consequently n||F_n||_{!,s}<=4||S_n||_{!,s}/(c-1). The exact inequalities

\[
 |2-i\delta|+1\le(3-\delta)i,\qquad
 |1-j\delta|+1\le(2-\delta)j
\]

give w_(i,j)<=(L+1)(5-2delta)ij. Setting Y_n=n||F_n||_{!,s} and using(1),(4) now gives

\[
 Y_1=F,\qquad Y_n\le K_s\sum_{i+j=n}Y_iY_j.
\]

The Catalan comparison proves(3).

The reconstruction of topic79 uses only ||partial_t||<=1, so its potential bound applies in this norm as well. Explicitly, for X=n delta>=20,

\[
 \|C_n\|_{!,s}\le\frac{432}{X^2}
 \{\|F_n\|_{!,s}+n(L+1+3\delta/2)\|G_n\|_{!,s}\}.
\]

There are finitely many early potential coefficients, which are absorbed into a constant. Finally

\[
 \|H(t)\|_{\ell^1}\le e^{|t|/s}\|H\|_{!,s}.
\]

After factoring out the leading radial growth, a fixed derivative of an order n term is bounded by a constant times n^h A^(n-1)e^(|log r|/s)r^(-delta(n-1)). For r>=max(R,1), this decreases radially once delta(n-1)>1/s. On any remaining compact radial interval the logarithmic factor is bounded. The margin A R^(-delta)<1 therefore proves uniform absolute convergence of each weighted derivative series. The finite early terms are bounded because their lower radial powers dominate their log polynomials. A small angular complex strip and a local complex logarithm cost an additional geometric factor absorbed by the same strict margin. This gives real analyticity. Absolute convergence justifies products and regrouping; termwise differentiation gives the original potential identities and stationary equation.

## A smaller constant

The factor16b in(2) can be replaced by8b. This uses the sharper stationary step already proved in topic79. Before the first genuine resonance N0, where N0 delta>=4, the density coefficients are constant in t, and n/lambda_n<=2/(c-1). At every later order, ||partial_t||_{!,s}<=1 and

\[
 \frac{n}{\lambda_n-c}\le\frac2{c-1}
\]

as in topic79. The same bound therefore holds at all orders, halving K_s. An alternative direct check handles n>=3 using

\[
 \frac{n}{\lambda_n-c/s}
 =\frac1{c-1}\frac{n}{n-1-1/(4a)}\le\frac2{c-1};
\]

n=2 is constant in t. This refinement uses no further assumption on the nonlinear forcing. The theory part independently confirmed this refinement at06:30Z; the review is retained in sources/lead_review_0630.md.

## Numerical scope

The accompanying code computes(1)'s realized ratio in the frozen delta2/3, c3, sin(theta) prefix with s=12. It also repeats s=1 and compares every result with topic78. It reconstructs the forcing from (lambda-c partial_t)F, so it independently audits the norm arithmetic but does not regenerate all high-order nonlinear coefficients. A bounded ratio through any finite order does not establish(1). Even a geometric order-dependent bound is not enough by itself, as the scalar counterexample in topic78 proves.

## Dependencies

The canonical log recurrence and Poisson bounds are in topics10 and17. Topic79 gives the independently confirmed stationary estimate, potential reconstruction, radial summability and Catalan closure. The conditional theorem uses no numerical evidence as a hypothesis substitute.


## Finite curvature statistic

For the logarithm L_n=log10||F_n||_{!,s} (or its stream analogue), define, whenever n>2h,

\[
 \widehat\sigma_{n,h}=
 \frac{L_n-2L_{n-h}+L_{n-2h}}
 {\log_{10}(n!)-2\log_{10}((n-h)!)+\log_{10}((n-2h)!)}.
\]

The denominator is positive because it is the logarithm of
product_(j=0)^(h-1)(n-j)/(n-h-j), whose factors exceed1. If the norm has the exact finite model C A^n(n!)^sigma at these three orders, the numerator cancels log10 C and n log10 A and the statistic equals sigma exactly. Without that model it is only a finite second difference. Polynomial corrections, migrating dominant columns and residue effects can change it. The accompanying interval computation uses h9,18,30, all multiples of3, to avoid mixing the three basic residue classes. A stable-looking finite statistic does not prove Gevrey asymptotics, and topic83 explains why even genuine factorial-norm Gevrey growth would not by itself prove divergence of the physical exterior series.
