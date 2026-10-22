# Conditional X bounds on the coherent derivative annulus

Written 2026-10-21T19:50:40.547551+00:00 before the new computation. This composes the accepted finite scalar audit152 with the accepted coherent geometry theorem160. It does not validate the imported physical derivative majorants.

## Statement and notation

Let k=1615536043799051/9007199254740992 and L=8614738245908811/1125899906842624. Let t=log r, u=r/L, m(r)=u^3(1+u^2)^((k-3)/2), and w(r)=m(r)^(-2)(1+u^2)^(-3/2). Put

 alpha=-1389482001461413/140737488355328,
 beta=7074968463789829/281474976710656,
 E=[exp(alpha),exp(beta)],
 delta=1677/629659522901737472.

For g define ||g||_(X(E))^2 as the integral over r in E and theta in[0,2pi] of [g^2+r^2|grad g|^2]w(r)r dr dtheta, with weak derivatives.

Use the19389 exact contiguous true log cells of topic160, with starts a_i and lengths d_i. In the corresponding saved row let ahat_i,h_i,W00_i,W10_i,W20_i,W01_i,W11_i be the exact binary64 numbers audited in topic152. The data obligations are that these are precisely the same rows and parameters in both accepted results. Topic160 gives d_i<=h_i and |a_i-ahat_i|<=delta.

Suppose f(t,theta)=sum_N f_N(t) sin((2N+1)theta), with finitely many nonzero modes. Assume each f_N is C2 on an open neighborhood of[alpha,beta]. On every true cell assume

 sum_N(2N+1)^q |partial_t^p f_N(t)| <= Wpq_i

for(p,q)=(0,0),(1,0),(2,0),(0,1),(1,1). The same conclusion holds for a countable expansion if both f and f-f_t, together with their weak first derivatives, are limits of their partial sums in the indicated weighted L2 spaces and the displayed majorants hold. Under these hypotheses,

 ||f||_(X(E)) < 0.385656,
 ||f-f_t||_(X(E)) < 585.874.

The numbers are exact terminating rationals. The W inequalities are hypotheses, including physical source-to-cell identification and regularity; they are not consequences of reading an interval table.

## Proof

Define A_i=W00_i^2+W10_i^2+W01_i^2 and B_i=(W00_i+W10_i)^2+(W10_i+W20_i)^2+(W01_i+W11_i)^2. Set v(t)=exp(2t)w(exp(t))=L^2 u^(-4)(1+u^2)^(3/2-k). Its logarithmic derivative is -4+(3-2k)u^2/(1+u^2), strictly between-4and0. For t in cell i, v(t)<=v(a_i)<=exp(4delta)v(ahat_i).

Polar derivatives and full-circle orthogonality give the three sums f_N^2,(f_N')^2,(2N+1)^2f_N^2 in the X integrand, with factor pi v(t). The inequality sum b_N^2<=(sum|b_N|)^2 gives A_i. The triangle inequalities for f_N-f_N', f_N'-f_N'', and(2N+1)(f_N-f_N') give B_i. Therefore

 ||f||_(X(E))^2 <= exp(4delta) S_A^2,
 ||f-f_t||_(X(E))^2 <= exp(4delta) S_B^2,
 S_A^2=pi sum_i h_i v(ahat_i) A_i,
 S_B^2=pi sum_i h_i v(ahat_i) B_i.

The accepted topic152 scalar computation proves S_A<0.385655 and S_B<585.873. Those sums are functions of the saved numbers and have no dependence on which true cells later receive the numbers. The new complete row and parameter binding will establish their equality with the sums in these displays.

For0<=x<1, the positive series gives exp(x)=sum_j x^j/j! <=sum_j x^j=1/(1-x). Here x=4delta is strictly between0and1. Thus exp(4delta)<1/(1-4delta). It is enough to check exactly

 (0.385655)^2/(1-4delta) < (0.385656)^2,
 (585.873)^2/(1-4delta) < (585.874)^2.

The new checker uses Fraction for these integer-rational inequalities and an independent fmpq computation of the equivalent cross-multiplied differences. Separate Arb and mpmath.iv evaluations enclose the two corrected ceilings exp(2delta) times the old ceilings. All comparisons are outward.

For finite sums the C2 assumption prevents distributional contributions at cell boundaries in f-f_t. For countable sums the explicit weak-derivative convergence justifies passage from finite Parseval identities to the asserted norms. Merely ignoring cell-boundary derivative jumps because the boundaries have measure zero is insufficient for the weak X norm, so this proof includes the regularity premise explicitly.

## Dependencies and scope

Topic152's PROOF.md, ADDENDUM.md, both complete scalar outputs and final verdict supply only the finite numerical sums. Topic160's PROOF.md, mandatory supplements, exact geometry and final verdict supply the coherent partition and coordinate displacement. The new proof uses both conclusions with their original scope. It does not rerun their complete enclosures. All accepted file pins are checked.

This is a conditional bound on E only. It becomes a bound for the IPM residual only if its W and regularity hypotheses are proved for that residual. It supplies no bound for r<exp(alpha) or r>exp(beta), no rigorous numerical norm of the scaling vector, no global inverse-constant lower bound, and no existence or exclusion endpoint.
