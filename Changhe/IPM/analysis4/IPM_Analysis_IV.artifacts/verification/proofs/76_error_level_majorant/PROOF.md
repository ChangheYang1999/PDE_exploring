# A smaller convergence constant from exact continued-fraction errors

Status: CONFIRMED after the theory part's stepwise review at2026-10-31T06:08Z and the verifier's recheck. The theorem and its radius corollaries may be labeled PROVED.

The earlier convergence theorem charges a full logarithm of a continued-fraction denominator at each small-divisor level. Nested levels allow a telescoping charge instead. Using the actual approximation errors also enlarges the separated sets. Both changes concern the majorant constant; the resulting arithmetic condition is equivalent to the Brjuno condition already used.

## Statement and notation

Let 0<delta<1 be irrational, alpha=delta/2, c=1/(1-delta), and d_n=dist(n delta,2Z). Let p_k/q_k be the continued-fraction convergents of alpha, with p_0=0, q_0=1, and let

\[
 e_k=|q_k\alpha-p_k|,\qquad
 E(\alpha)=\sum_{k=1}^{\infty}
       \frac{\log(e_{k-1}/e_k)}{q_k}.
 \tag{1}
\]

Assume E(alpha)<infinity. For a finite nonzero S1 sine polynomial f_1, let L be its largest frequency, F the sum of its absolute sine amplitudes, and put

\[
 \lambda_\delta=\frac32+\frac\delta2+\frac1\delta,
 \qquad K=\frac{2\lambda_\delta(L+2)}{c-1},
 \qquad A_E=\frac{4KF}{\alpha\delta}\exp(2E(\alpha)).
 \tag{2}
\]

The unique pure stationary recursion satisfies

\[
 \frac{n\|f_n\|_{\mathcal A_0}}{d_n}
 \le \frac{\alpha}{4K}A_E^n.
 \tag{3}
\]

Consequently its density, stream and original potential series converge absolutely and uniformly, with every fixed Cartesian derivative in the corresponding radial weight, on r>=R for every R>A_E^(1/delta). They define a nonzero real analytic exterior solution of the stationary potential equation. This is an exterior assertion, with no global stationary extension asserted.

Condition E(alpha)<infinity is equivalent to the usual Brjuno condition

\[
 \mathcal B(\alpha)=\sum_{k=0}^{\infty}
        \frac{\log q_{k+1}}{q_k}<\infty.
 \tag{4}
\]

Thus (2) supplies an alternative explicit constant for the established theorem. It need not be smaller for every alpha; the two valid constants can be compared and their minimum used.

## 1. Separation at an error threshold

For k>=1 the best-approximation inequality is

\[
 0<m<q_k\quad\Longrightarrow\quad
       \|m\alpha\|_{\mathbb R/\mathbb Z}\ge e_{k-1}.
 \tag{5}
\]

Here is the short integer-lattice proof. Consecutive convergent vectors (p_(k-1),q_(k-1)) and (p_k,q_k) have determinant plus or minus one. Write (l,m) as their integer linear combination with coefficients a,b. The constraint 0<m<q_k excludes a=0 and excludes a,b both positive or both negative. In the remaining cases b=0 or the coefficients have opposite signs. Consecutive convergent errors also have opposite signs, so their nonzero contributions to m alpha-l have the same sign. Its absolute value is therefore at least e_(k-1). Taking the minimum over l proves (5).

Define the nested sets

\[
 S_k=\{m\ge1:\|m\alpha\|<e_{k-1}/2\},\qquad k\ge1.
 \tag{6}
\]

Every element of S_k is at least q_k. If distinct m,m' lie in S_k, the triangle inequality gives ||(m-m')alpha||<e_(k-1), so their distance is at least q_k by (5). The errors strictly decrease to zero; hence the sets are nested and any fixed positive integer belongs to only finitely many of them.

For an integer m which belongs to exactly S_1,...,S_h, with h=0 allowed, the first failed membership gives d_m=2||m alpha||>=e_h. Since e_0=alpha, telescoping yields the pointwise bound

\[
 \log(d_m^{-1})\le\log(\alpha^{-1})+
       \sum_{k:m\in S_k}\log(e_{k-1}/e_k).
 \tag{7}
\]

This remains true when d_m>1 would make the left side negative; in the present normalization d_m<=1 anyway. No pointwise polynomial bound on d_m is used.

## 2. Charge the nested levels on a binary tree

Consider an ordered full binary tree with n leaves. For an internal vertex v let s(v) be the number of leaves below it. Mark the vertices with s(v) in S_k and compress their ancestry into a forest.

A terminal marked vertex contains at least q_k leaves. A marked vertex with exactly one marked child has at least q_k leaves outside that child's subtree, since their distinct sizes lie in S_k. Assign those leaves to the terminal or unary vertex. These assigned sets are disjoint. If the compressed forest has l terminal and u unary vertices, then q_k(l+u)<=n. Its number b of vertices with at least two children satisfies b<=l, by its edge count. Therefore

\[
 N_k:=\#\{v:s(v)\in S_k\}\le2n/q_k.
 \tag{8}
\]

There are exactly n-1 internal vertices. Summing (7), using the nonnegativity of log(e_(k-1)/e_k), and then (8), gives

\[
 \prod_{v\ \mathrm{internal}}d_{s(v)}^{-1}
 \le\alpha^{-(n-1)}\exp(2nE(\alpha)).
 \tag{9}
\]

The argument also covers the one-leaf tree, whose empty product is one.

## 3. The scalar majorant and reconstruction

The independently derived recurrence and Fourier multiplier bounds in topic13 give, with Y_n=n||f_n||/d_n,

\[
 Y_1=F/\delta,\qquad
 Y_n\le\frac{K}{d_n}\sum_{i+j=n}Y_iY_j.
 \tag{10}
\]

Its equality majorant expands over ordered full binary trees. A tree contributes K^(n-1)(F/delta)^n times the product in (9). There are at most 4^(n-1) such trees. Hence

\[
 Y_n\le(4K/\alpha)^{n-1}(F/\delta)^n e^{2nE}
       =\frac{\alpha}{4K}A_E^n,
\]

including n=1, when the right side is e^(2E)Y_1>=Y_1.

For completeness, the reconstruction uses no further arithmetic loss. The stream bound is ||g_n||<=C_delta ||f_n||/d_n, and the finite-potential triangular inversion gives ||C_n||<=C_chi ||f_n||/d_n, with C_chi finite at fixed irrational delta. These bounds were derived directly in topic13. The density, stream and potential angular bandwidths are linear in n, and the radial degrees are linear in n. A fixed Cartesian derivative therefore costs only a fixed power of n after its natural radial weight is removed. This is summable against A_E R^(-delta)<1. A sufficiently small angular complex strip adds another geometric factor which the same strict margin absorbs. Absolute convergence permits products and regrouping of the stationary recurrence, while termwise differentiation preserves rho=-partial_y Delta chi and psi=chi_xy. The nonzero leading profile proves nontriviality.

## 4. Arithmetic equivalence and a computable tail

The convergent error recurrence and alternating signs give

\[
 e_{k-1}=a_{k+1}e_k+e_{k+1},
 \qquad a_{k+1}<e_{k-1}/e_k<a_{k+1}+1.
 \tag{11}
\]

Also q_(k+1)/q_k=a_(k+1)+q_(k-1)/q_k lies in the same interval. Thus the logarithms of these two ratios differ in absolute value by at most log 2. Since q_(k+2)>=2q_k, the sum of 1/q_k converges. Consequently E is finite if and only if the sum of log(q_(k+1)/q_k)/q_k over k>=1 is finite. Adding the convergent sum of log(q_k)/q_k and the single k=0 term gives equivalence with (4). To justify that added convergence explicitly, q_k grows at least geometrically every two steps, and log x/x decreases for x>=e, so a geometric lower bound on q_k dominates its summands by a summable sequence.

If a_(k+1)<=M for every k>=N, then (11) and q_(N+j)>=2^floor(j/2) q_N imply

\[
 0<\sum_{k=N}^{\infty}\frac{\log(e_{k-1}/e_k)}{q_k}
 \le\frac{4\log(M+1)}{q_N}.
 \tag{12}
\]

This bounds the tail using exact denominator recurrences and outward-rounded elementary functions. For alpha=1/(2 sqrt(5)), the exact continued fraction is [0;4,2,8,2,8,...], so M=8 is valid from N=1. The calculation below will use this exact pattern, rather than extract it from rounded decimal digits.

## Dependencies and scope

The required mathematical inputs are the independently checked stationary recurrence and reconstruction from topic13, the elementary convergent determinant and error identities proved above, and the finite full-binary-tree count. No new numerical convergence assumption enters the proof. The alternative constant does not establish optimality, a larger arithmetic existence class, rational logarithmic convergence, or a global stationary solution.

## 5. A uniform exterior radius for an explicit large-c family

A concrete consequence keeps the leading amplitude fixed and varies the exponent. Let N>=16 be an integer and define

\[
 c_N=2N+\sqrt5,\qquad \delta_N=1-c_N^{-1},
 \qquad f_1(\theta)=\sin\theta.
 \tag{13}
\]

Then the proposed theorem proves convergence of the full nonterminating exterior series and all its weighted derivatives on r>=128, for every such N.

To prove the numerical radius without decimal approximations, put phi=(1+sqrt(5))/2 and T=N+1/phi. Thus c_N=2T+1, alpha=T/(2T+1), and

\[
 \alpha=[0;2,N,1,1,1,\ldots].
\]

The first errors are e_0=alpha and e_1=1/(2T+1), so e_0/e_1=T. Every subsequent error ratio is phi. Therefore

\[
 E(\alpha)=\tfrac12\log T+
           (\log\phi)\sum_{k=2}^{\infty}\frac1{q_k},
 \qquad q_2=2N+1.
\]

The denominator doubling estimate bounds the last sum by 4/(2N+1). Substituting K=lambda_delta(L+2)/T into (2) gives, for arbitrary finite leading norm F and largest frequency L at this parameter,

\[
 A_E\le\frac{8\lambda_\delta(L+2)F}{\delta^2}
                 \phi^{8/(2N+1)}.
 \tag{14}
\]

For N>=16, delta>32/33 and lambda_delta<2+33/32=97/32. Also phi<2 and 2^(8/33)<6/5; the latter is the integer inequality 2^8 5^33<6^33. Consequently

\[
 A_E<8\frac{97}{32}\left(\frac{33}{32}\right)^2
                   \frac65 (L+2)F
       <32(L+2)F.
 \tag{15}
\]

The final comparison is rational arithmetic. For sin(theta), F=L=1, this gives A_E<96. Finally 96^33<128^32 implies 96<128^(32/33)<128^delta. Thus the strict convergence margin at R=128 holds for every N>=16. This changes the exact exponent at fixed leading amplitude; it does not rely on shrinking the amplitude or rescaling an existing exterior solution.

The radius 128 is a sufficient common radius, not an optimal one. The family is far from Candidate007's exponent. Its purpose is to give a transparent explicit parameter family with a smaller certified domain bound; the near-reference constants remain separate.

## Independent finite checks, 2026-10-31T05:56:21Z

The 1024-bit Arb computation encloses the defining partial sums and the explicit tails separately. At delta=1/sqrt(5), it gives E<.449555117500 and A_E<2886.635 for sin(theta), and A_E<436180.855 for the exact unnormalized Candidate007 leading polynomial. The strict inequalities A_E<2^(26 delta) and A_E<2^(42 delta) hold respectively. The same dyadic radii work at the explicitly defined quadratic irrational within 2e-32 of the stored reference delta from topic13. These are conditional corollaries of the proposed theorem pending its independent review.

The calculation also checks 270,000 finite threshold classifications, 29,638 exact dynamic-programming comparisons for the largest possible number of marked vertices over all binary trees through 512 leaves, and 4,599 inequalities for the positive scalar equality majorant through order 512. Nine exact quadratic-irrational parameter families are used. The three integer/rational inequalities in (15) and the final radius comparison pass exactly. The final audit took 1.2690979060716927 seconds. Input hashes, full enclosures and exact source snapshots are in verification/checks.json and sources/. These finite checks do not replace the all-order proof.

## Independent review closure, 2026-10-31T06:11:13Z

The retained theory-part review checks separation, nesting, the forest count, the scalar prefactor, arithmetic equivalence, tail estimate, and the explicit large-c family. The verifier rechecked every step and the previously certified constants. The theorem and radius corollaries are CONFIRMED. A sufficient radius and a prescribed geometric tail ratio are distinct: at delta1/sqrt5, the sin1 ratio is below .913 at R2^26, and below1/2 at R2^28.
