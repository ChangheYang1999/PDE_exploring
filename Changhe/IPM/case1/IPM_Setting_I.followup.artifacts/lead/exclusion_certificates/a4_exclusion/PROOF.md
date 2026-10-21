# A quantitative Lipschitz estimate and an explicit exclusion

## 1. The fixed-parameter theorem

Fix \(A>2\), \(L>0\), \(\beta=2/A\), and
\[
0<r<\min(1,L),\qquad \beta<\sigma\le2,\qquad
0<\theta\le1,\quad \theta+\beta>1.
\]
An admissible trace has
\[
w(0)=w(L)=0,\quad w'(0)=-A,\quad w'(L)=A,\quad w<0\quad(0<x<L),
\]
and, on \(0<x\le r\),
\[
w=-Ax+d_3x^3+d_5x^5+d_7x^7+R_w,\qquad
|R_w^{(i)}(x)|\le Mx^{7+\sigma-i}\quad(0\le i\le2).
                                                               \tag{1}
\]
It is \(C^{2,\theta}\) on \([r,L]\). It may be nonsmooth at \(L\). Smoothness on the open segment can be assumed when identifying its functional with the classical third-axis obstruction.

Use the norm
\[
\|w\|_{\mathcal X}=
|d_1|+|d_3|+|d_5|+|d_7|
+\sum_{i=0}^2\sup_{0<x\le r}x^{i-7-\sigma}|R_w^{(i)}(x)|
+\sum_{i=0}^2\|w^{(i)}\|_{C^{0,\theta}([r,L])},                \tag{2}
\]
where \(d_1=-A\) and \(\|f\|_{C^{0,\theta}}=\|f\|_\infty+[f]_\theta\).
For differences, use the differences of coefficients and remainders. At fixed \(A\), the \(d_1\) difference is zero.

The theorem below is **CONFIRMED**:

> Given an admissible reference \(w_0\), choose \(r\) small enough to satisfy the explicit condition \(\eta_0<1/2\) below. The constants defined in §3 depend only on computable norms of \(w_0\), \(A,L,r,\sigma,\theta\), and the selected ball radius \(d\). For every two admissible traces in that ball,
> \[
> |B_3(A,w_1)-B_3(A,w_2)|\le C_B\|w_1-w_2\|_{\mathcal X}.
>                                                               \tag{3}
> \]
> The ball radius and \(C_B\) are specified explicitly, with no unknown profile-dependent constant.

Here and below \(B_3(A,w)\) abbreviates \(B_3((A+1)/2,w)\). The estimate is conservative, intended as a rigorous certificate rather than an efficient numerical conditioning estimate.

## 2. A norm for the origin subtraction

Put \(p=4+\sigma\in(4,6]\). For a function with a unique expansion
\[
f=f_0+f_2x^2+f_4x^4+R_f,\qquad R_f=O(x^p),
\]
define
\[
\|f\|_{\mathcal A}
=|f_0|+|f_2|r^2+|f_4|r^4
+\sup_{0<x\le r}\frac{|R_f(x)|}{(x/r)^p}.                     \tag{4}
\]
The expansion coefficients are unique because \(p>4\). This norm controls the supremum and is submultiplicative. To check the latter, multiply the two polynomials. Terms of degree at most 4 contribute to the polynomial norm; terms of degree at least 6 contribute to the remainder because \((x/r)^6\le(x/r)^p\). The other three remainder products are bounded by the corresponding products of polynomial and remainder norms. Summing proves
\(\|fg\|_{\mathcal A}\le\|f\|_{\mathcal A}\|g\|_{\mathcal A}\).
This also proves completeness by taking the three coefficients and the weighted remainder separately.

Consequently the geometric and exponential series converge in this norm, with
\[
\|(1+v)^{-1}\|_{\mathcal A}\le(1-\|v\|_{\mathcal A})^{-1}
\quad(\|v\|_{\mathcal A}<1),\qquad
\|\exp f\|_{\mathcal A}\le e^{\|f\|_{\mathcal A}}.             \tag{5}
\]
On functions with zero constant coefficient, the operator
\[
(\mathcal If)(x)=\int_0^x f(t)\,\frac{dt}{t}
\]
has norm at most \(1/2\), by integrating its two polynomial terms and its remainder explicitly.

For each trace set
\[
z=-\frac{w}{Ax},\quad D=xz',\quad J=2z'/x+z''=-\frac{w''}{Ax},
\quad E=\mathcal I(z^{-1}-1),\quad b=ze^E.                   \tag{6}
\]
Direct differentiation shows that
\[
g=x^2b,\qquad m=Ae^{-E}/x                                   \tag{7}
\]
solve the normalized compatibility equation on \((0,r]\).

Define
\[
T=\frac{z^{-4}}2
\{e^{-(\beta+1)E}(1+z+D)+Ae^{-(\beta+2)E}J\},\qquad
V=z^{-1}e^{(1-\beta)E}.                                    \tag{8}
\]
Starting from \(Q=(g'-w'')/(2g^3)\), substitution of (6)–(7) gives the exact identity
\[
(Q-Q_*)m^{\beta-2}g^{-1}
=A^{\beta-2}\{x^{-5-\beta}T-Q_*x^{-\beta}V\}.                \tag{9}
\]
For clarity, the numerator in this calculation is
\[
2b+xb'-w''/x=e^E(1+z+xz')+AJ.
\]
Thus no third derivative of \(w\) enters (8).

The finite-part operator in (9) is explicitly
\[
\mathfrak F_\beta(T)=
\sum_{j=0,2,4}\frac{T_jr^{j-4-\beta}}{j-4-\beta}
+\int_0^r x^{-5-\beta}(T-T_0-T_2x^2-T_4x^4)\,dx.            \tag{10}
\]
There is no vanishing denominator. Its operator norm is bounded by
\[
F=r^{-4-\beta}\max\{\beta^{-1},(\sigma-\beta)^{-1}\}.         \tag{11}
\]
Indeed each scaled polynomial coefficient has multiplier at most
\(r^{-4-\beta}/\beta\), and the remainder has multiplier
\(r^{-4-\beta}/(\sigma-\beta)\).
Also
\[
\left|\int_0^r x^{-\beta}V\,dx\right|
\le I\|V\|_{\mathcal A},\qquad
I=\frac{r^{1-\beta}}{1-\beta}.                               \tag{12}
\]

## 3. Fully specified constants

All norms of the reference appearing below are part of the input and can be bounded above by interval arithmetic or analytic estimates. All positive minima can instead be replaced by certified positive lower bounds. The formulas remain valid with such outward bounds.

### Origin bounds

Compute \(z_0,D_0,J_0\) from (6), and let
\[
\eta_0=\|z_0-1\|_{\mathcal A}<\tfrac12,\quad
D_0^*=\|D_0\|_{\mathcal A},\quad J_0^*=\|J_0\|_{\mathcal A}.
\]
Shrinking \(r\) makes \(\eta_0<1/2\) for every reference satisfying (1).
Put
\[
Z_1={r^2+r^4+r^6+r^{6+\sigma}\over A},
\quad
D_1={2r^2+4r^4+6r^6+2r^{6+\sigma}\over A},
\]
\[
J_1={6+20r^2+42r^4+r^{4+\sigma}\over A}.                     \tag{13}
\]
For traces with the same \(A\), (1)–(2) give
\[
\|\Delta z\|_{\mathcal A}\le Z_1\|\Delta w\|_{\mathcal X},
\quad
\|\Delta D\|_{\mathcal A}\le D_1\|\Delta w\|_{\mathcal X},
\quad
\|\Delta J\|_{\mathcal A}\le J_1\|\Delta w\|_{\mathcal X}.      \tag{14}
\]
For example \(J\) has coefficients \(-6d_3/A,-20d_5/A,-42d_7/A\), and remainder \(-R_w''/(Ax)\). For \(z,D\), the \(x^6\) term is included in the remainder of (4). The remainders of \(z,D\) have order \(6+\sigma\); their bounds in (13) follow by evaluating their weighted bounds at \(r\).

For the tail define
\[
a_0(x)=-\frac{w_0(x)}{L-x},\qquad a_0(L)=A,\qquad
a_*=\min_{[r,L]}a_0>0.
\]
Choose any
\[
0<d\le\min\left\{1,\frac{1/2-\eta_0}{2Z_1},\frac{a_*}{2}\right\}.
                                                               \tag{15}
\]
All following envelopes apply to the closed ball of radius \(d\) around \(w_0\), restricted to the endpoint conditions.
Set
\[
\eta=\eta_0+Z_1d,\quad Z=1+\eta,\quad
D_*=D_0^*+D_1d,\quad J_*=J_0^*+J_1d,\quad N=(1-\eta)^{-1},
\]
\[
E_*=\frac{\eta}{2(1-\eta)},\qquad L_E=\tfrac12N^2Z_1.
\]
By (5), \(\|E\|_{\mathcal A}\le E_*\), and
\(\|\Delta E\|_{\mathcal A}\le L_E\|\Delta w\|_{\mathcal X}\).
Let
\[
e_1=e^{(\beta+1)E_*},\quad e_2=e^{(\beta+2)E_*},\quad
S=e_1(1+Z+D_*)+Ae_2J_*.
\]
Valid bounds and Lipschitz constants for (8) are
\[
T_*=\tfrac12N^4S,\qquad V_*=Ne^{(1-\beta)E_*},               \tag{16}
\]
\[
\begin{split}
L_T=\tfrac12\bigl\{
4N^5Z_1S+N^4[&
e_1(Z_1+D_1)+(\beta+1)e_1L_E(1+Z+D_*)\\
&+Ae_2J_1+A(\beta+2)e_2L_EJ_*]\bigr\},                       \tag{17}\\
L_V=e^{(1-\beta)E_*}\{N^2Z_1+N(1-\beta)L_E\}.               \tag{18}
\end{split}
\]
These follow from the product inequality, the inverse identity, and the exponential identity
\(e^f-e^g=(f-g)\int_0^1e^{tf+(1-t)g}\,dt\). For inverse powers, the bound used is
\(\|\Delta(z^{-n})\|\le nN^{n+1}\|\Delta z\|\).

### Reconstruction and endpoint bounds on the whole tail

Let \(\ell=L-r\), and put
\[
C_a=1+\tfrac12\ell^{1-\theta},\quad
a_{\min}=a_*/2,\quad
A_\theta=\|a_0\|_{C^{0,\theta}}+C_ad,
\]
\[
N_a=a_{\min}^{-1}+A_\theta a_{\min}^{-2},\qquad
W_2=\|w_0''\|_{C^{0,\theta}([r,L])}+d.                       \tag{19}
\]
For any trace in the ball, write \(a=-w/(L-x)\) with \(a(L)=A\), and
\[
j(x)=\frac{A-w'(x)}{L-x}
=\int_0^1w''(L-t(L-x))\,dt,\qquad k=j/a.
\]
The identities
\[
a(x)=\int_0^1w'(L-t(L-x))\,dt,\qquad g'=kg                 \tag{20}
\]
show that
\[
\|\Delta a\|_{C^{0,\theta}}\le C_a\|\Delta w\|_{\mathcal X},
\quad a\ge a_{\min},\quad
\|j\|_{C^{0,\theta}}\le W_2,\quad
\|\Delta j\|_{C^{0,\theta}}\le\|\Delta w\|_{\mathcal X}.
\]
The factor \(1/2\) in \(C_a\) follows by differentiating the average for \(a\) and integrating \(t\). In particular the control is on all of \([r,L]\), not just near \(L\).

Since \(C^{0,\theta}\), with the norm used here, is a normed algebra, set
\[
K=W_2N_a,\qquad L_K=N_a+W_2N_a^2C_a.                        \tag{21}
\]
They bound respectively \(\|k\|_{C^{0,\theta}}\) and the Lipschitz constant of \(k\).
For the origin value \(g(r)\), define
\[
g_r^+=r^2Ze^{E_*},\quad g_r^-=r^2(1-\eta)e^{-E_*},
\quad L_r=r^2e^{E_*}(Z_1+ZL_E).
\]
Let
\[
H=\ell+\ell^{1-\theta},\quad
G=g_r^+e^{HK},\quad
g_{\min}=g_r^-e^{-\ell K},\quad
L_G=e^{HK}(L_r+g_r^+HL_K).                                  \tag{22}
\]
Solving (20) as
\(g(x)=g(r)\exp\int_r^xk\)
gives
\[
\|g\|_{C^{0,\theta}}\le G,\quad g\ge g_{\min},\quad
\|\Delta g\|_{C^{0,\theta}}\le L_G\|\Delta w\|_{\mathcal X}.
\]
Here \(\|\int_r^x k\|_{C^{0,\theta}}\le HK\), directly from its derivative and its interval length. Thus these bounds also prove existence and positivity of the rebuilt \(g\) through \(L\).

Put
\[
N_g=g_{\min}^{-1}+Gg_{\min}^{-2},
\]
\[
Q_\theta=\tfrac12(KN_g^2+W_2N_g^3),                         \tag{23}
\]
\[
L_Q=\tfrac12\{L_KN_g^2+2KN_g^3L_G+N_g^3+3W_2N_g^4L_G\}.
                                                               \tag{24}
\]
The identity
\[
Q=\tfrac12(kg^{-2}-w''g^{-3})
\]
proves \(\|Q\|_{C^{0,\theta}}\le Q_\theta\) and
\(\|\Delta Q\|_{C^{0,\theta}}\le L_Q\|\Delta w\|_{\mathcal X}\).
In particular
\[
|\Delta Q_*|\le L_Q\|\Delta w\|_{\mathcal X},\qquad
|\Delta(Q(x)-Q_*)|
\le L_Q(L-x)^\theta\|\Delta w\|_{\mathcal X}.                 \tag{25}
\]

### Tail weight and final constant

On the tail \(m=(L-x)a/g\). Set
\[
M=a_{\min}^{\beta-2}G^{1-\beta},
\]
\[
L_M=(2-\beta)a_{\min}^{\beta-3}G^{1-\beta}
+(1-\beta)a_{\min}^{\beta-2}g_{\min}^{-\beta}L_G.              \tag{26}
\]
The mean value theorem on positive real numbers proves that these bound the supremum and the Lipschitz constant of \(a^{\beta-2}g^{1-\beta}\). Only \(\|\Delta a\|_\infty\le\|\Delta w\|_{\mathcal X}\) is needed here.

The promised explicit constant is
\[
\boxed{\begin{split}
C_B={1-\beta\over3A}
\{F L_T+I(Q_\theta L_V+L_QV_*)\}\\
\quad+{(1-\beta)A^{1-\beta}\over3}
\frac{\ell^{\theta+\beta-1}}{\theta+\beta-1}
\{L_QM+Q_\theta L_M\}.
\end{split}}                                                \tag{27}
\]
Every symbol in (27) has been explicitly defined in (11)–(26).

## 4. Proof of the estimate

The convergent finite-part formula in §6.3.1(i), or direct integration by parts in the R10 formula, gives
\[
B_3=
\frac{\beta-1}{3A}
\left\{\mathfrak F_\beta(T)-Q_*\int_0^r x^{-\beta}V\,dx\right\}
\frac{(\beta-1)A^{1-\beta}}3
\int_r^L(Q-Q_*)m^{\beta-2}g^{-1}\,dx.                        \tag{28}
\]
Equation (9) proves the first term with exactly the finite-part convention (10). The last integral is ordinary. By (25), its integrand is bounded by a constant times
\((L-x)^{\theta+\beta-2}\), so it converges.

Subtract (28) for the two traces. Equations (11)–(12) and (16)–(18), (23)–(25) bound the first difference by
\[
\frac{1-\beta}{3A}
\{F L_T+I(Q_\theta L_V+L_QV_*)\}\|\Delta w\|_{\mathcal X}.
\]
In the last integral use
\[
m^{\beta-2}/g=(L-x)^{\beta-2}a^{\beta-2}g^{1-\beta},
\]
then (25)–(26), and integrate
\(\int_r^L(L-x)^{\theta+\beta-2}dx
=\ell^{\theta+\beta-1}/(\theta+\beta-1)\).
This yields precisely the second term of (27), proving (3).

The same proof establishes existence of the finite-part functional for these nonsmooth traces. To identify \(C_0=\ell_3+B_3\), the actual third-axis equation and its origin expansion are still required, exactly as in §6.3.1(i). The continuity theorem alone does not give \(\ell_3=0\).

## 5. Allowing \(A\) to vary: explicit additional constants

This subsection supplies a quantitative extension; a fixed-\(A\) slice is not being passed off as an open neighborhood in the \(A\) variable.

Choose \(0<h<A_0-2\), write
\[
A_-=A_0-h,\quad A_+=A_0+h,\quad
\beta_-={2\over A_+},\quad\beta_+={2\over A_-},
\]
and require \(\sigma>\beta_+\), \(\theta+\beta_->1\).
In the preceding construction use \(A_0\) and the radius \(d\). For a new trace put
\[
\widehat w={A_0\over A}w,\qquad f=\widehat w/A_0=w/A.
\]
Both \(\widehat w\) and \(w_0\) have parameter \(A_0\). The rebuilt \(g\), and \(z,E,D,J\), depend only on \(f\), because
\((w'-A)/w=(f'-1)/f\). If
\(\delta=\|w-w_0\|_{\mathcal X}\), where \(d_1=-A\), then
\[
|A-A_0|\le\delta,\qquad
\|\widehat w-w_0\|_{\mathcal X}\le N_0\delta,\qquad
N_0={A_0+\|w_0\|_{\mathcal X}\over A_-}.                     \tag{29}
\]
Use \(\delta\le\min(h,d/N_0)\).

Here are finite constants for differentiation in \(A\) while \(f\) is fixed. All the envelopes \(N,E_*,Z,D_*,J_*,K,N_g,G,g_{\min},W_2,a_{\min},A_\theta\) are the preceding fixed-\(A_0\) envelopes. Define
\[
\begin{split}
T^+&=\tfrac12N^4\{
e^{(\beta_++1)E_*}(1+Z+D_*)+
A_+e^{(\beta_++2)E_*}J_*\},\\
T_f^+&=\tfrac12N^4e^{(\beta_++2)E_*}J_*,
\qquad V^+=Ne^{(1-\beta_-)E_*},\\
Q^+&=\tfrac12\{KN_g^2+(A_+/A_0)W_2N_g^3\},
\qquad q_f^+=\tfrac{W_2}{2A_0}N_g^3 .
\end{split}                                                \tag{30}
\]
Here \(q_f=-f''/(2g^3)=\partial_AQ\) at fixed \(f,\beta\), and the last two bounds are in \(C^{0,\theta}\).

Put \(\widetilde a=-f/(L-x)\), and take
\[
\widetilde a_-={a_{\min}\over A_0},\quad
\widetilde a_+={A_\theta\over A_0},
\quad
M^+=\max_{b\in\{\beta_-,\beta_+\}}
(\widetilde a_-)^{b-2}G^{1-b},
\]
\[
\Lambda=
\max\left\{\left|\log{\widetilde a_-\over G}\right|,
             \left|\log{\widetilde a_+\over g_{\min}}\right|\right\}.
                                                               \tag{31}
\]
These bound the tail weight and \(|\log(\widetilde a/g)|\).

For the origin let
\[
d_o=\min(\beta_-,\sigma-\beta_+),\quad
F^+=r^{-4-\beta_+}/d_o,\quad
F_{\log}^+=r^{-4-\beta_+}
\left({|\log r|\over d_o}+{1\over d_o^2}\right),
\]
\[
I^+={r^{1-\beta_+}\over1-\beta_+},\quad
I_{\log}^+=r^{1-\beta_+}
\left({|\log r|\over1-\beta_+}+{1\over(1-\beta_+)^2}\right).
                                                               \tag{32}
\]
For the tail let
\[
p_-=\theta+\beta_--1,\quad p_+=\theta+\beta_+-1,\quad
H_0=\max(\ell^{p_-},\ell^{p_+}),
\]
\[
H^+=H_0/p_-,\qquad
H_{\log}^+=H_0\left({|\log\ell|\over p_-}+{1\over p_-^2}\right).
                                                               \tag{33}
\]
Direct integration shows that (32) bounds the operators in (10), (12) and their exponent derivatives, and (33) bounds
\(\int_0^\ell s^{\theta+\beta-2}ds\) and the same integral with \(|\log s|\).

Define
\[
\begin{split}
\mathcal J^+&=F^+T^++Q^+I^+V^++H^+Q^+M^+,\\
\mathcal J_A^+&=F^+T_f^++q_f^+I^+V^++H^+q_f^+M^+,\\
\mathcal J_\beta^+&=(F_{\log}^++F^+E_*)T^+
+Q^+(I_{\log}^++I^+E_*)V^+\\
&\hspace{12mm}+Q^+M^+(H_{\log}^++H^+\Lambda).
\end{split}                                                \tag{34}
\]
Finally put
\[
c^+={1-\beta_-\over3A_-},\quad
c_A^+={2\over3A_-^3}+{1-\beta_-\over3A_-^2},
\]
\[
C_A=c_A^+\mathcal J^+
+c^+\{\mathcal J_A^++2A_-^{-2}\mathcal J_\beta^+\}.            \tag{35}
\]

To verify these constants, rewrite (28), with \(w=Af\), as
\[
B_3(A,Af)=c(A)\mathcal J(A,\beta,f),\qquad
c(A)={\beta-1\over3A},
\]
where the tail part of \(\mathcal J\) is
\[
\int_r^L(L-x)^{\beta-2}
(Q-Q_*)\widetilde a^{\beta-2}g^{1-\beta}\,dx.
\]
There is no residual power of \(A\) in this integral. At fixed \(f,\beta\),
\(\partial_AT=T_f\), \(\partial_AQ=q_f\), and \(\partial_AV=0\).
At fixed \(f,A\), \(\partial_\beta T=-ET\),
\(\partial_\beta V=-EV\). The tail exponent derivative multiplies its integrand by
\(\log(L-x)+\log(\widetilde a/g)\).
The finite-part exponent derivative is obtained by differentiating the three explicit fractions in (10) and the absolutely convergent remainder integral. Equations (32)–(34) justify these differentiations uniformly by integrable bounds. Since \(\beta'=-2/A^2\), the product rule gives (35).

It follows, using the fixed-\(A_0\) constant (27), that
\[
\boxed{\displaystyle
|B_3(A,w)-B_3(A_0,w_0)|
\le C_{\rm all}\|w-w_0\|_{\mathcal X},\qquad
C_{\rm all}=N_0C_B+C_A.}                                   \tag{36}
\]
This includes variations of the 7-jet, the weighted remainder, the entire tail, and \(A\), with an aligned source. Moving-source estimates require an additional specified identification of intervals; they are not asserted here.

## 6. A certified positive reference

For any \(A>2,L>0\), consider the compatible rational trace
\[
w_0(x)=-Ax\,{1-(x/L)^2\over1+(x/L)^2},\qquad
g_0(x)={x^2\over1+(x/L)^2}.
\]
Direct differentiation gives
\[
w_0g_0'=(w_0'-A)g_0,\qquad
m={A\over L}{1-u^2\over u},\qquad u=x/L,
\]
and
\[
L^5(Q-\mathcal P(m)-Q_*)
=(1-6k)(u^5-1)+(1+2k)(u^3-1),\qquad k=A/L^2.                \tag{37}
\]
The latter also follows by computing
\[
Q=\frac{-6AL^2+2Ax^2+L^4+L^2x^2}{L^4x^5}
\]
and subtracting its divergent polynomial in \(m\).

To evaluate \(B_3\), substitute \(m=(A/L)(1-u^2)/u\) into the ordinary integral and integrate by parts. Both endpoint terms vanish: at 0, the remainder in (37) is bounded while \(m^{\beta-1}\to0\); at 1, the remainder is \(O(1-u)\), so its product with \(m^{\beta-1}\) is \(O((1-u)^\beta)\).
Using \(t=u^2\), the result is
\[
B_3=C_A^{\rm rat}L^{-4-\beta}(1-S_A/L^2),                   \tag{38}
\]
\[
C_A^{\rm rat}={16-\beta\over3A(4+\beta)}
\,\mathrm B(2-\beta/2,\beta)>0,\qquad
S_A={6A(4A-3)\over8A-1}.                                   \tag{39}
\]
For verification before simplification, the two beta integrals are
\[
{L^{-4-\beta}\over6A}
\{5(1-6k)\mathrm B(3-\beta/2,\beta)
 +3(1+2k)\mathrm B(2-\beta/2,\beta)\}.
\]
The ratio of the beta functions is \((4-\beta)/(4+\beta)\), as follows by one integration by parts in their defining integrals. This proves (38)–(39), not just its sign.

Choose now \(A_0=4,L=4\). Then
\[
B_3(4,w_0)={23\over110592}\,\mathrm B(7/4,1/2).
\]
The defining integral gives the exact lower bound
\[
\mathrm B(7/4,1/2)=\int_0^1t^{3/4}(1-t)^{-1/2}dt
>\int_0^1t^{3/4}dt=4/7.
\]
Therefore
\[
\boxed{B_3(4,w_0)>23/193536>10^{-4}.}                        \tag{40}
\]
This uses the normalization \(g/x^2\to1\); it is not the rescaled “natural units” used for some trial values in the report.

For a completely specified choice of norm, take \(r=1/4\), \(\sigma=1\), \(\theta=3/4\). The reference is analytic and has a finite norm (2). With \(q=(r/L)^2=1/256\), its origin function satisfies
\[
\eta_0\le2q+2q^2+2q^3<1/2.
\]
This bound follows by subtracting the \(x^2,x^4\) terms of
\(z_0-1=-2(x/L)^2/(1+(x/L)^2)\). Its tail quotient is explicitly
\[
a_0(x)=4\,\frac{(x/4)(1+x/4)}{1+(x/4)^2},
\]
so \(a_0>0\) on \([r,4]\) and every reference quantity in §3 is a norm or a minimum of an explicit rational function.

At fixed \(A=4,L=4\), let \(d,C_B\) be (15), (27), and set
\[
\varepsilon_{\rm fix}=\min\{d,(20000C_B)^{-1}\}.             \tag{41}
\]
Every compatible trace with distance less than \(\varepsilon_{\rm fix}\) has \(B_3>1/20000\).

For a neighborhood also allowing \(A\) to vary, take \(h=1/2\). Then \(A_-=7/2,A_+=9/2\), \(\beta_-=4/9,\beta_+=4/7\), and the stated \(\sigma,\theta\) have both required strict margins. Use (29)–(36), and set
\[
\varepsilon_{\rm all}
=\min\{1/2,d/N_0,(20000C_{\rm all})^{-1}\}.                  \tag{42}
\]
All quantities in (41)–(42) are explicit functions of the reference norms specified above. No claim of a numerically useful size is made.

### A numerical radius, deliberately conservative

It is possible to give a specific radius without leaving reference norms unevaluated:
\[
\boxed{\ \|w-w_0\|_{\mathcal X}<\exp(-10^7),\quad L=4\ }     \tag{43}
\]
is contained in the variable-\(A\) exclusion neighborhood. The norm here still includes \(d_1=-A\), and uses \(r=1/4,\sigma=1,\theta=3/4\). This is an extremely small radius, not a practical validation claim.

Here are analytic upper bounds verifying (43). Choose \(d=10^{-4}\) and \(h=1/2\). The rational reference has
\[
a_*\ge1/4,\quad \|a_0\|_{C^{0,3/4}}<13,\quad
\|w_0''\|_{C^{0,3/4}}<43.5,\quad \|w_0\|_{\mathcal X}<116.
\]
To check them, write \(t=x/4\), so
\[
a_0=4t(1+t)/(1+t^2)\ge x,\quad
\|a_0\|_\infty\le8,\quad\|a_0'\|_\infty\le3.
\]
Also
\[
w_0''=\frac{256x(48-x^2)}{(16+x^2)^3},
\quad \|w_0''\|_\infty\le12,\quad \|w_0'''\|_\infty\le21.
\]
The latter follows by differentiating the displayed fraction: its two terms are bounded in absolute value by 3 and 18 on \([0,4]\). Since \((L-r)^{1/4}<1.5\), these derivative bounds imply the stated Hölder bounds. The bounds \(\|w_0\|_\infty\le16\), \(\|w_0'\|_\infty\le12\) give tail contributions less than \(34,30,43.5\) to (2). The jet contribution is less than 5. Its exact origin remainder is
\[
R_{w_0}=-\frac{x^9}{8192(1+x^2/16)}.
\]
Each of its three weighted derivative suprema in (2) is less than 1, proving the bound 116.

For the origin algebra, with \(q=r^2/16=1/256\),
\[
\|D_0\|_{\mathcal A}\le\frac{4q}{(1-q)^2}<1,\qquad
\|J_0\|_{\mathcal A}\le\frac{3+q}{4(1-q)^3}<1.
\]
Indeed \(D_0=-4(x^2/16)(1+x^2/16)^{-2}\) and
\(J_0=-(3-x^2/16)/(4(1+x^2/16)^3)\); use the algebra estimate (5).
Consequently (13)–(22) give
\[
\eta<.01,\ N<2,\ E_*<.01,\ Z_1,D_1<1,\ J_1<3,\ D_*,J_*<2,
\]
\[
a_{\min}\ge1/8,\quad A_\theta<14,\quad N_a\le904,\quad
W_2<44,\quad K<40000,\quad L_K<10^8,\quad H<6,
\]
\[
g_r^+<1,\quad g_r^->1/32,\quad L_r<1,
\]
\[
G<e^{240000},\quad g_{\min}>e^{-150004},\quad
L_G<e^{240021},\quad N_g<e^{540009}.
\]
In turn,
\[
Q_\theta<e^{1620050},\quad L_Q<e^{2400100},\quad
M<e^{120004},\quad L_M<e^{315030}.
\]
The core factors \(F,I,L_T,L_V,V_*\) in (27) are less than \(e^{20}\): this follows by inserting \(r=1/4,\beta=1/2\) and the displayed algebra bounds into (11)–(18). Thus
\[
C_B<e^{2600000}.
\]
For the variable-\(A\) constants, (29) gives \(N_0<100\). In (30)–(34), one may use
\[
Q^+<e^{1620050},\quad q_f^+<e^{1620050},\quad
M^+<e^{133340},\quad \Lambda<250000.
\]
The other factors \(T^+,T_f^+,V^+,F^+,F_{\log}^+,I^+,
I_{\log}^+,H^+,H_{\log}^+\) are less than \(10^5\), directly from
\(\beta_-=4/9,\beta_+=4/7\) and the core bounds. Substitution in (34)–(35) gives \(C_A<e^{1800000}\), and hence
\[
C_{\rm all}<e^{3000000}.
\]
These deliberately rounded inequalities also show that \(d=10^{-4}\) satisfies (15). Finally \(\delta<e^{-10^7}\) implies both \(N_0\delta<d\) and
\[
C_{\rm all}\delta<e^{-7000000}<1/20000.
\]
Together with (40) this proves (43), and provides an explicit numerical radius in addition to the sharper norm-dependent formulas.

## 7. Exclusion of exact smooth-center profiles

Suppose an exact profile has aligned source \(L=4\), an axis trace in the ball (41) or (42), is in \(P_\infty\), and satisfies the source Hölder hypothesis \(\alpha>1-2/A\) (or the accepted cone version). Then §6.3.1(h) of the supplied report gives \(B_3=0\). Equations (40)–(42) give \(B_3>1/20000\), a contradiction.

Thus these explicit neighborhoods contain no such exact profiles. Closeness of the trace to a specified rational function in a specified norm is the added geometric/analytic hypothesis; a sign of the unknown profile's obstruction is not assumed.

This proves neither that an exact \(P_2\) profile lies near the reference nor that the numerical branch is contained in this neighborhood. No error estimate connecting trial data to exact profiles has been supplied. The result is a rigorous local exclusion, not a global nonexistence theorem.

## Dependencies

The functional identification and endpoint formula are §6.3.1(i) of the supplied report. The final exclusion uses §6.3.1(h), together with the stated open-segment regularity for \(P_\infty\). All constants, the stability proof, and the certified rational reference value have been derived in this file.
