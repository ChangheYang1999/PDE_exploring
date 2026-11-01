# The highest logarithmic degree at delta = 2/3

Status: CONFIRMED after the theory part's independent all-step review at 2026-10-31T04:08Z and verifier closure V059. The complete logarithmic series remains unresolved.

## Statement

Set delta=2/3 and c=3, take f_1(theta)=sin(theta), and use the polynomial-log recurrence of topic10 with every resonant stream coefficient normalized to have zero constant term. Write t=log(r), p_n=1-2n/3, P_n=2-2n/3 and denote the density and stream polynomials by F_n(t,theta),G_n(t,theta). The log-degree bounds of topic17 are

\[
 d_n=\max(0,\lfloor(n-1)/3\rfloor-1),\qquad
 e_n=\max(0,\lfloor n/3\rfloor-1).
\]

For every k>=2, the coefficient of t^(k-1) in G_(3k) is

\[
 b_k\sin((2k-2)\theta).
 \tag{1}
\]

The first two values and every subsequent ratio are

\[
 b_2=-\frac{177047}{1204224000000},\qquad
 b_3=\frac{416591591}{16616364441600000000},
 \tag{2}
\]

\[
 \frac{b_{k+1}}{b_k}=R(k):=
 \frac{(k-1)(2k-1)^2
 (8478k^4-13599k^3+507k^2+4184k-340)}
 {9600k^2(3k-4)(3k-2)(3k+1)(3k+2)(6k-5)(6k-1)},
 \quad k\ge3.
 \tag{3}
\]

In particular b_k>0 for k>=3 and, with lambda=157/129600,

\[
 \lim_{k\to\infty}
 \big((k-1)!|b_k|\big)^{1/k}=\lambda.
 \tag{4}
\]

For r=1,2,3 let H_(k,r)(theta)=[t^(k-1)]F_(3k+r). Then

\[
 \lim_{k\to\infty}
 \big((k-1)!\|H_{k,r}\|_0\big)^{1/(3k+r)}
 =\lambda^{1/3}.
 \tag{5}
\]

Here the norm is the sum of absolute sine coefficients. The same limit holds for the highest-degree stream coefficients at orders3k,3k+1,3k+2. With the extra weight S^(k-1), the limit is (S lambda)^(1/3).

Thus the maximal-degree coefficients grow geometrically in a factorial log norm. Their corresponding subseries, before factorial weighting and regarded as functions of the independent variables z and t, converge absolutely for every finite complex z,t. They cannot by themselves force divergence of the full canonical log series. Lower log degrees remain outside this result.

## 1. Why the top degree satisfies a linear three-step cycle

For i,j>=4 with i+j=n,

\[
 e_i+d_j
 =\lfloor i/3\rfloor+\lfloor(j-1)/3\rfloor-2
 \le d_n-1.
\]

Therefore a product contributing to the highest allowed degree must have i<=3 or j<=3. In each such product a radial derivative of t lowers the degree, so only the pure radial factors P_i,p_j enter. The density inverse divides the top degree by 2(n-1).

At order3k the stream has one more allowed degree than the density. Only the resonant angular mode2k-2 acquires that extra degree; every other inverse preserves degree. Hence (1). Given b_k, put m=2k-2 and divide all the next highest-degree coefficients by b_k. Define h_0=sin(m theta), h_1,h_2 for the normalized stream profiles at orders3k+1,3k+2, and a_1,a_2,a_3 for the normalized density profiles at orders3k+1,3k+2,3k+3. The lower-case subscripts here count positions in this cycle and are not the full order index.

Let f_j,g_j, j<=3, be the pure initial density and stream profiles. The complete top-degree cycle is

\[
 2(3k+r-1)a_r
 =\sum_{i=0}^{r-1}
 \left[P_{3k+i}h_i f_{r-i}'-p_{r-i}h_i'f_{r-i}\right]
 +\sum_{i=1}^{r-1}
 \left[P_i g_i a_{r-i}'-p_{3k+r-i}g_i'a_{r-i}\right],
 \quad r=1,2,3.
 \tag{6}
\]

For r=1,2, h_r is the nonresonant Poisson inverse of a_r at P_(3k+r). These formulas include all admissible ordered pairs. No quadratic interaction of two later profiles reaches this log degree.

For a sine term A sin(K theta), the Poisson inverse places

\[
 -\frac{A}{2(K+1+P)}\sin((K+1)\theta)
 +\frac{A}{2(K-1-P)}\sin((K-1)\theta).
 \tag{7}
\]

These identities hold with signed frequencies, using sin(-K theta)=-sin(K theta) and sin(0)=0. At the next resonance, the coefficient of sin((2k-1)theta) in a_3 gives

\[
 b_{k+1}=-\frac{b_k}{2k}
 [\sin((2k-1)\theta)]a_3.
 \tag{8}
\]

This follows from the resonant half-inverse -one-half times integration in t, applied to the density coefficient at degree k-1.

## 2. Exact low data and scalar simplification

The initial profiles required by (6) are

\[
 f_1=\sin\theta,\quad
 f_2=-\frac3{40}\sin\theta-\frac1{40}\sin3\theta,
\]

\[
 f_3=\frac1{6400}\sin\theta+
 \frac{39}{11200}\sin3\theta+
 \frac{11}{5600}\sin5\theta,
\]

\[
 g_1=-\frac3{20}\sin2\theta,\qquad
 g_2=\frac3{640}\sin2\theta+\frac3{1120}\sin4\theta.
\]

Only these two streams enter (6). They follow directly from the pure recurrence and (7). Computing F_6 gives the first value b_2 in (2) by (8) at the first resonance.

For a compact reproducible simplification of (6), write a_r=sum_s A_(r,s)(k) sin((m+s)theta). The supports are s=+/-1 for r=1, s=+/-1,+/-3 for r=2, and s=+/-1,+/-3,+/-5 for r=3. Equations (6),(7) give

\[
 A_{1,1}=-\frac{2(k-1)}{9k},\qquad
 A_{1,-1}=-\frac{k-1}{9k},
\]

\[
 A_{2,3}=\frac{k-1}{90k},\qquad
 A_{3,5}=-\frac{11(k-1)}{8400k},
\]

and

\[
 A_{3,1}=-\frac{(k-1)(2k-1)^2
 (8478k^4-13599k^3+507k^2+4184k-340)}
 {4800k(3k-4)(3k-2)(3k+1)(3k+2)(6k-5)(6k-1)}.
 \tag{9}
\]

The full small table of rational coefficients is in verification/symbolic_chain.json. It can be reproduced from (6),(7), with no high-order recursion. The listed code computes them as exact rational functions and factors each result.

For k>=3 no negative signed frequency from this table reflects onto the next resonant density mode m+1=2k-1. Thus (8),(9) give (3). At k=2, the s=-5 term is sin(-3 theta), which also contributes to that mode. Therefore b_3 uses A_(3,1)(2)-A_(3,-5)(2), giving the second value in (2). This low-order reflection is the reason (3) starts at k=3.

Every factor in the denominator of R(k) is positive for k>=3. The quartic numerator is positive there because its first two terms are k^3(8478k-13599)>0 and its remaining three terms are positive in total. Hence no later b_k vanishes.

## 3. Asymptotic growth and convergence of this part

Taking the leading coefficients in (3) gives

\[
 \lim_{k\to\infty} kR(k)
 =\frac{4\cdot8478}{9600\cdot3^4\cdot6^2}
 =\frac{157}{129600}=\lambda>0.
\]

The positive sequence B_k=(k-1)!b_k has successive ratio kR(k), so the logarithmic Cesaro mean of these ratios proves (4).

All coefficients A_(r,s)(k) and the corresponding normalized stream coefficients are rational functions with numerator degree at most denominator degree and with no integer poles for k>=3. They are bounded as k tends to infinity. At least one coefficient for each r has a nonzero limit, as the three explicitly displayed outer coefficients show. The same statement for h_1,h_2 follows directly from (7); for example their highest-frequency coefficients are (k-1)/(12k) and -(k-1)/(480k). Frequencies are distinct and positive once k>=4, so the sine-coefficient norm of each normalized profile is bounded above and bounded away from zero. Combining this with (4) proves (5).

For any lambda'>lambda, (4) bounds the unweighted coefficients by C(lambda')^k/(k-1)!. The extracted density subseries at each r has norm bounded by

\[
 C|z|^r\sum_{k\ge2}
 \frac{(\lambda'|z|^3)^k|t|^{k-1}}{(k-1)!},
\]

which converges for all finite z,t. The same proof applies to the three stream subsequences. This is a statement about the extracted top-degree part only. It does not control the number or sizes of the lower-degree columns.

## Verification and scope

The independent Cartesian implementation in code/maximal_log_cartesian_check.py constructs the full polynomial-log recursion through45 using only Cartesian derivative products and triangular Poisson inversion. Every stationary and Poisson identity is exact. All resonant b_k through k=15 and all highest-degree angular profiles through45 agree with (2),(3),(6). The complete verification took24.438055481761694 seconds. The exact output is retained in verification/cartesian_checks.json.

An early check exposed the k=2 reflected-frequency exception. Equation (3) was then restricted to k>=3 and b_3 was computed separately before the successful complete check. No conclusion about the full factorial norm, the observed intermediate-degree bump, or convergence of the complete rational-log expansion follows from this result.
