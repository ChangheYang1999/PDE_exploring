# Realized factorial product losses

Status: identities and an audit protocol. Finite measurements do not imply an all-order bound.

## Setting and exact definitions

Use the canonical logarithmic recursion at delta=2/3, c=3 and F_1(t,theta)=sin(theta). Write p_j=1-2j/3, P_i=2-2i/3, lambda_n=2(n-1), and D=d/dt. Every resonant stream constant is zero. The forcing is

\[
 S_n=\sum_{i+j=n}J_{i,j}(G_i,F_j),\qquad
 J_{i,j}(G,F)=(P_iG+DG)\partial_\theta F
             -(\partial_\theta G)(p_jF+DF).
 \tag{1}
\]

The density equation gives the independent reconstruction

\[
 S_n=(\lambda_n-cD)F_n.
 \tag{2}
\]

For a real sine polynomial H=sum_q t^q h_q(theta), define

\[
 \|H\|_!=\sum_q q!\sum_m |h_{q,m}|,\quad
 H^+=H-H(0,\theta),\quad
 w_{i,j}=2j(|P_i|+1)+2i(|p_j|+1).
\]

The two requested ratios, when their denominators are nonzero, are

\[
 \rho_n=\frac{\|S_n\|_!}{\sum_{i+j=n}w_{i,j}\|G_i\|_!\|F_j\|_!},
\qquad
 \rho_n^{++}=
 \frac{\|\sum_{i+j=n}J_{i,j}(G_i^+,F_j^+)\|_!}
 {\sum_{i+j=n}w_{i,j}\|G_i^+\|_!\|F_j^+\|_!}.
 \tag{3}
\]

The factors 2i and 2j are the common Fourier bandwidth bounds for this initial profile. They are deliberately kept in (3), to match the proposed statistic; tighter actual derivative norms are used only when screening individual summands.

## Exact product decomposition

For G=t^u g(theta), F=t^v f(theta), bilinearity gives

\[
 J_{i,j}(G,F)
 =t^{u+v}(P_i g f'-p_jg'f)
  +t^{u+v-1}(u g f'-v g'f).
 \tag{4}
\]

The second term is absent when u=v=0. This formula remains valid when one input has degree zero. Consequently

\[
 S_n^{++}=S_n-\sum_{i+j=n}
 \left[J_{i,j}(G_i(0),F_j)+J_{i,j}(G_i^+,F_j(0))\right].
 \tag{5}
\]

There is no double counting: the first removed term contains all pairs with u=0, and the second contains precisely u>0,v=0. All pairs in S_n^{++} have u,v>=1, so its constant coefficient is exactly zero.

The angular products are implemented independently in real Laurent arithmetic. Let A_h be the antisymmetric Laurent polynomial with coefficients h_m/2 at +m and -h_m/2 at -m; it represents i h(theta). Let C_h have coefficients m h_m/2 at both signs; it represents h'(theta). Then A_g C_f and C_g A_f represent i g f' and i g'f. Twice the positive-frequency coefficients recover the real sine amplitudes in (4). This also fixes the difference-frequency signs.

For screening a single input-column pair, let a=||g||, b=||f||, a'=||g'||, b'=||f'|| in the sine coefficient norm. With q=u+v, the triangle inequality proves

\[
 \|J_{i,j}(t^u g,t^v f)\|_!
 \le q!(|P_i|ab'+|p_j|a'b)
    +\mathbf1_{q>0}(q-1)!(uab'+va'b).
 \tag{6}
\]

The sine/cosine products satisfy the required norm bound because each product of two basis elements has two coefficients of magnitude at most 1/2. A ranked list of individual norms measures the sizes of signed contributions before their mutual cancellation; it is not a decomposition of the norm of their sum. A claimed global rank must be separated from every uncomputed upper bound in (6).

## Verification and limitations

Write this derivation before running the arithmetic. Check (4) against exact Cartesian derivatives on rational synthetic data and against the independently generated low-order canonical sequence. At high orders decode the retained numerical checkpoint as exact dyadic balls, and compute all quantities using outward-rounded Arb arithmetic. Equation (2) uses the audited recurrence but is not a new independent recomputation of every high-order convolution. Equation (5), including the zero constant coefficient, supplies an additional independent boundary-product check.

Finite bounds for rho_n, even very small ones, do not prove a convergent infinite series. In particular, an order-dependent geometric loss cannot be absorbed without examining its products along trees. For C>1, the positive scalar recurrence

\[
 x_1=1,\qquad x_n=C^n\sum_{i=1}^{n-1}x_i x_{n-i}
\]

has loss C^n at each order, but

\[
 x_n\ge C^n x_{n-1}\ge C^{n(n+1)/2-1}.
\]

Thus its power series has radius zero. This exact counterexample refutes a general inference from a geometric per-order loss to an exponential coefficient bound. A valid all-order closure needs a uniform loss or a stronger tree-summability argument, and must also control the Poisson step.

## Completed finite audit, 2026-10-31T06:13:57Z

All279 full forcing ratios through280 are below1, with unique maximum .360721512928792 at280. Positive-degree ratios at120,180,220,250,260,270,280 are respectively .07704,.10597,1.05959,28.35559,42.35754,50.09268,58.04595. At280 the positive-degree forcing norm is1.33491313107 times the full norm. The exact outward intervals and frozen checkpoint are retained in verification/.

At270 the globally largest column pair has(i,u,v)=(1,0,46), and the largest positive-degree pair has(18,3,43). At280 these are(1,0,53) and(21,4,49). Every omitted pair has a rigorous upper bound below the stated winners. The certified rank prefixes contain122/128 and118/128 entries for the all/positive subsets. This is a ranking of individual norms before mutual cancellation. It does not partition the norm of the signed forcing. The final pass took491.3457557139918 seconds.
