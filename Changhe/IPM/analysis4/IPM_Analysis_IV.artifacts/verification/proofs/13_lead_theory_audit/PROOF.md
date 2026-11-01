# Independent audit of the finite-polynomial Brjuno convergence theorem

## Exact claim and scope

Let 0<delta<1 be irrational, c=1/(1-delta), alpha=delta/2 and

\[
d_n=\operatorname{dist}(n\delta,2\mathbb Z).
\]

Write p_n=1-n delta, P_n=p_n+1, q_n=p_n+3. Let f_1 be a nonzero finite linear combination of sin((2k+1)theta), with largest frequency L, and put B=L+1 and F=||f_1||_0, the sum of the absolute sine amplitudes. Let q_k^CF be the continued-fraction denominators of alpha, with q_0^CF=1, and assume

\[
\mathcal B(\alpha)=\sum_{k=0}^{\infty}
 \frac{\log q_{k+1}^{\rm CF}}{q_k^{\rm CF}}<\infty.
\]

Define

\[
\lambda_\delta=\frac32+\frac\delta2+\frac1\delta,
\quad K=\frac{2\lambda_\delta(B+1)}{c-1},
\quad A=8K e^{2\mathcal B(\alpha)}F/\delta.
\]

The pure stationary recursion is defined at every order and gives

\[
Y_n:=\frac{n\|f_n\|_0}{d_n}\le\frac{A^n}{8K}.
\tag{1}
\]

Consequently the density, stream and original potential series, with all fixed Cartesian derivatives in their natural radial weights, converge absolutely and uniformly for r>=R whenever R>A^(1/delta). Their sums are real analytic on r>A^(1/delta), obey S1 symmetry, and solve the original stationary potential equation exactly. This is an exterior theorem. It gives no global canonical-velocity extension.

The independent audit confirms this claim. The proof below supplies the elementary continued-fraction fact used in the theory part's proof, verifies the tree argument, and checks the reconstruction. The source under audit is the retained file in `sources/lead_theory_a36363b93f0b9596038ca88b9921014647efa86fbf0cc50eea4b99db51d6f314.md`, sections 1 to 7.1. The analytic-data extension is audited separately in the next topic.

## Recurrence and scalar normalization

The independent Cartesian derivation in `../01_recurrence/PROOF.md` proves

\[
b_{n,j}=-\frac{a_{n,j-1}}{2(2j+P_n)}
 +\frac{a_{n,j}}{2(2j-P_n)},
\]

\[
(n-1)(c-1)f_n=\sum_{i+j=n}
 [P_i g_i f_j'-p_jg_i'f_j].
\tag{2}
\]

The sum is over ordered pairs. The Fourier supports satisfy deg f_n<=nB-1 and deg g_n<=nB. Since delta is irrational all denominators are nonzero. Each fixed coefficient is determined before any convergence claim is made.

For the stream multipliers, |2j+P_n|>=d_n and 2j-P_n>=n delta. The frequency shift in either channel is one. At angular strip width sigma>=0 this yields

\[
\|g_n\|_\sigma\le\frac{e^\sigma}{2}
 (d_n^{-1}+(n\delta)^{-1})\|f_n\|_\sigma.
\]

For the radial multiplier, use |P_n|<=2+n delta. For the derivative multiplier, split the first channel into 2(j+1)>=2n delta and its complement; its ratio 2j/|2(j+1)-n delta| is at most 2n/d_n. The second channel has ratio at most max(1,2/(n delta)). These estimates give

\[
\max(\|g_n'\|_\sigma,|P_n|\|g_n\|_\sigma)
\le e^\sigma\lambda_\delta\frac n{d_n}\|f_n\|_\sigma.
\tag{3}
\]

The two channels can have different output frequencies for the same input mode; the bounds apply to each separately. No equality of those frequencies is assumed.

At sigma=0, the Wiener product inequality, (2), (3), and

\[
(\deg f_j)+|p_j|\le(jB-1)+|1-j\delta|\le j(B+1)
\]

imply

\[
(n-1)(c-1)\|f_n\|_0\le
 \lambda_\delta(B+1)\sum_{i+j=n}\frac{ij}{d_i}
 \|f_i\|_0\|f_j\|_0.
\]

Multiplying by n/d_n, using n/(n-1)<=2 and d_j<=1, gives

\[
Y_n\le\frac K{d_n}\sum_{i+j=n}Y_iY_j,
\qquad Y_1=F/\delta.
\tag{4}
\]

In particular, the divisor of the root order n must remain in (4). Replacing it by a pointwise polynomial bound before expanding the trees discards the useful arithmetic separation.

## Continued-fraction separation proved directly

In this subsection abbreviate q_k^CF to q_k, and write p_k/q_k for the corresponding convergents. Their elementary recurrences imply

\[
p_kq_{k-1}-p_{k-1}q_k=(-1)^{k-1}.
\]

Thus the vectors (p_{k-1},q_{k-1}) and (p_k,q_k) are an integer basis of the integer lattice. Their errors epsilon_l=q_l alpha-p_l have opposite signs. The continued-fraction tail formula gives

\[
|\epsilon_{k-1}|=
 \frac1{q_{k-1}\alpha_k+q_{k-2}}
 >\frac1{q_k+q_{k-1}},
\tag{5}
\]

where alpha_k=a_k+1/alpha_{k+1} lies strictly between a_k and a_k+1.

For any integers p,q with 0<q<q_k, write

\[
(p,q)=a(p_{k-1},q_{k-1})+b(p_k,q_k).
\]

If a,b are both positive then q>=q_{k-1}+q_k, impossible; if both negative then q<0. If a=0 then q is a nonzero multiple of q_k, also impossible. In every remaining case, either b=0 or a,b have opposite signs. Because the convergent errors have opposite signs, the two terms in a epsilon_{k-1}+b epsilon_k then have the same sign, or one is zero. Therefore

\[
|q\alpha-p|\ge|\epsilon_{k-1}|>
 \frac1{q_k+q_{k-1}}\ge\frac1{2q_k}.
\tag{6}
\]

Taking the minimum over p proves the needed best-approximation inequality without an external small-divisor theorem.

Let S_k={m>=1: ||m alpha||<1/(4q_k)}. For k=0, q_0=1 and the assertions below are immediate. For k>=1, (6) shows that every m in S_k is at least q_k. If distinct m,m' belong to S_k, the distance inequality gives

\[
\|(m-m')\alpha\|<1/(2q_k),
\]

so |m-m'|>=q_k. The sets S_k are nested, and every fixed m belongs to only finitely many of them.

## The tree count and product estimate

Expand the equality majorant of (4) into ordered full binary trees with n leaves. Each internal vertex v carries the factor 1/d_(s(v)), where s(v) is its number of descendant leaves. Apart from these factors, every tree contributes K^(n-1)Y_1^n. There are at most 4^(n-1) trees.

Fix k and mark vertices whose subtree size belongs to S_k. Compress the marked ancestry relation to a forest. A terminal marked vertex has at least q_k leaves beneath it. A marked vertex with exactly one marked child has at least q_k leaves outside that child's subtree, by the separation just proved. Charge those leaves to the terminal and unary vertices. The charged sets are disjoint: a descendant charge lies inside the child subtree excluded by every unary ancestor, while incomparable subtrees are disjoint.

If l,u,b are the numbers of terminal, unary and branching marked vertices, then q_k(l+u)<=n. The forest edge count gives b<=l. Thus the total number N_k of marked vertices satisfies

\[
N_k\le2(l+u)\le2n/q_k.
\tag{7}
\]

If m is not in S_0 then 1/d_m<=2. If m belongs to S_k but not S_(k+1), then 1/d_m<=2q_(k+1). Since the sets are nested and each membership list is finite, these statements imply the deliberately loose bound

\[
\log(1/d_m)\le\log2+
 \sum_{k:m\in S_k}\log q_{k+1}.
\]

Summing over vertices and applying (7) gives

\[
\prod_{v\text{ internal}}d_{s(v)}^{-1}
\le2^{n-1}e^{2n\mathcal B(\alpha)}.
\tag{8}
\]

Combining (4), the tree count and (8) proves (1), with precisely the constants in the statement. The proof remains valid for n=1: its upper bound includes the harmless factor e^(2 B(alpha)). This checks the normalization at the base order as well as at nonlinear orders.

## Potential reconstruction and all derivatives

Write Delta chi_n=r^(p_n+1)D_n and D_n=sum d_m cos(2m theta), using d_m here only for these temporary Fourier amplitudes. With x=(n delta-2)/2 the density equations are

\[
a_0=2x d_0+(1-x)d_1,
\qquad a_m=(m+x)d_m+(m+1-x)d_{m+1}\quad(m\ge1).
\tag{9}
\]

For n delta>=3, x>=1/2 and |m+1-x|<=m+x. Solving downward gives the more explicit estimate

\[
|d_m|\le\sum_{k\ge m}\frac{|a_k|}{k+x}
 \le\frac{\|f_n\|_0}{m+x}\quad(m\ge1),
\]

and |d_0|<=3||f_n||_0. This intermediate sum justifies the downward induction in the theory part's shorter argument.

The Laplacian inverse divides d_m by q_n^2-4m^2. For m>=1, both factors |q_n-2m| and |q_n+2m| are distances of n delta from even integers, and their larger is at least 2m. Hence the product is at least 2m d_n. For m=0, q_n^2>=d_n |4-n delta|. Therefore

\[
\|C_n\|_0\le\frac{\|f_n\|_0}{d_n}
 \left(\frac3{|4-n\delta|}+
 \sum_{m\ge1}\frac1{2m(m+1/2)}\right)
\le\left(\frac3{|4-n\delta|}+1\right)
 \frac{\|f_n\|_0}{d_n}.
\tag{10}
\]

The finitely many earlier orders have invertible finite triangular potential matrices because n delta is not an even integer. The expression |4-n delta| can be below one at only finitely many orders, and none is zero. This gives a finite uniform constant C_chi with ||C_n||_0<=C_chi ||f_n||_0/d_n. The support of C_n is at most nB-2.

Equations (1), (3), (10) give geometric bounds for all three series. Every Cartesian derivative lowers the radial degree by one and raises the angular degree by at most one. After h derivatives, the norm grows by at most

\[
\prod_{t=0}^{h-1}(|s|+J+2t)
 \le(|s|+J+h)^h
\]

on a term r^s h(theta) of degree J. The last inequality follows from the arithmetic-geometric mean inequality, since the average of 2t is h-1. Both |s| and J grow at most linearly with n. Fixed derivative orders therefore cost only a polynomial in n, which is summable against the strict geometric margin A R^(-delta)<1.

In a sufficiently small complex angular strip, the same argument adds e^(sigma nB), which is still absorbed by that margin. The weighted sums are analytic in z=r^(-delta) and theta near every real point with r>A^(1/delta). Their compositions with polar coordinates are real analytic away from the origin. The identities rho=-partial_y Delta chi and psi=chi_xy pass to the limit. The stationary nonlinear double series converges absolutely; regrouping it by i+j and using (2) gives zero at every order. The leading weighted density tends to the nonzero f_1, so the solution is nontrivial.

## Certified constants and a correction to the reported tail

For alpha=1/(2 sqrt(5)), the continued fraction is [0;4,2,8,2,8,...]. Indeed the repeating tail x=2+1/(8+1/x) has positive root 1+sqrt(5)/2, and 1/(4+1/x)=1/(2 sqrt(5)). Thus all denominator recurrences are exact integer computations.

If every partial quotient after q_N is at most M, then

\[
q_{N+j}\ge2^{\lfloor j/2\rfloor}q_N,
\qquad q_{N+j+1}\le(M+1)^{j+1}q_N.
\]

Summing these bounds gives the explicit tail estimate

\[
\sum_{k=N}^\infty\frac{\log q_{k+1}}{q_k}
\le\frac{4\log q_N+14\log(M+1)}{q_N}.
\tag{11}
\]

Here sum 2^(-floor(j/2))=4 and sum (j+1)2^(-floor(j/2))=14. The artifact `verification/brjuno_constants.json`, produced by `../../code/brjuno_constants_verify.py`, uses exact denominators and 512-bit Arb enclosures for logarithms and exponentials. Its lower ball encloses a finite partial sum; its upper ball encloses that sum plus (11). Thus the true number is between the lower endpoint of the first ball and the upper endpoint of the second.

The resulting values, displayed approximately here, are

\[
\mathcal B(1/(2\sqrt5))=2.5385730957725673412\ldots,
\]

and its tail after 25 terms is 1.24475947706... times 10^(-14), confirming the claimed bound 4 times 10^(-14).

For the quadratic irrational with Candidate 007's exact rational continued-fraction prefix followed by all ones, the exact prefix and the distance formula in the theory part's report are correct. The difference in delta is below 2 times 10^(-32). Its Brjuno sum is 2.5575257197547515713..., but the tail after the 31-term finite prefix is 1.28097313566... times 10^(-14). Thus the report's claim that this tail is below 10^(-14) is false. It can be replaced by 1.281 times 10^(-14), or by the fully enclosed value in the artifact.

The displayed table in the theory part report consists of rounded approximations, not outward bounds. For example its value A=8.42 times 10^4 is 84200, whereas the actual defined A is 84217.9540587955.... Suitable outward bounds include A<84218 for sin(theta) and A<12725638 for the raw extracted Candidate 007 density polynomial, both at delta=1/sqrt(5). The true log10 radius values are respectively 11.01353969619955... and 15.88654644922865.... Calling rounded table entries rigorous upper bounds requires this correction; the symbolic formulas and the convergence theorem are unaffected.

## Audit conclusion

The finite-polynomial theorem, including its potential and all-derivative conclusion, is confirmed. The elementary leaf-count proof in `../07_diophantine_convergence/PROOF.md` is a consistent independent Diophantine version of the same mechanism, and its explicit sin(theta) and extracted-profile corollaries are confirmed as well. The conclusions do not depend on the minor decimal corrections above. The general analytic-data extension, parameter continuity, rational logarithms, and whole-plane canonical velocity require their separate statements and audits.
