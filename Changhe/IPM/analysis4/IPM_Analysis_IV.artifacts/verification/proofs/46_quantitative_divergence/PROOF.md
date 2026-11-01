# An explicit arithmetic condition for zero radius

Status: CONFIRMED after the theory part's independent adversarial review at2026-10-31T04:14Z and the retained exact finite checks. This is a sufficient divergence condition. It does not characterize the boundary of the Brjuno convergence theorem.

## Statement

Fix a nonzero finite rational odd-sine polynomial

\[
 f_1(\theta)=\sum_{\substack{1\le m\le L\\m\text{ odd}}}
 \alpha_m\sin(m\theta),\qquad \alpha_1\alpha_L\ne0,
 \qquad B=L+1.
\]

Let delta be irrational in (0,1), c=1/(1-delta), and construct its unique pure density and stream coefficients by the stationary recurrence in topic01. Suppose that, for some real tau satisfying

\[
 \tau>\frac{B\pi^2}{6},
 \tag{1}
\]

there are infinitely many distinct primes p and even integers a with 4<=a<p such that

\[
 0<\left|\delta-\frac ap\right|<p^{-\tau p^2}.
 \tag{2}
\]

Then

\[
 \limsup_{n\to\infty}\|f_n(\delta)\|_{\ell^1}^{1/n}=\infty.
 \tag{3}
\]

The density power series has radius zero in the angular Wiener norm and in the uniform angular norm. The same conclusion holds if all the rational coefficients are multiplied by one fixed nonzero real scalar. A simpler sufficient choice in (2) is tau=2B.

For example, tau=4 suffices for f_1=sin(theta), and tau=40 suffices for the ten-mode rational Candidate007 profile. These parameters are new exact irrational parameters, not Candidate007's stored rational exponent.

## 1. A common denominator at a prime center

Write delta_0=a/p. Let Q be a common positive integer denominator of the alpha_m. For large p, the prime obstruction theorem in topic31 gives

\[
 \kappa_p=[\sin((a-3)\theta)]f_p(\delta_0)\ne0.
 \tag{4}
\]

The notation [sin(k theta)] means its real sine amplitude. The excluded primes divide fixed input numerators or denominators, so they affect only finitely many centers.

Every coefficient of f_p(delta_0) has a common denominator dividing the positive integer

\[
\begin{split}
 D_p={}&Q^p(4a)^{p-1}
 \prod_{n=2}^{p}(n-1)^{\lfloor p/n\rfloor}\\
 &\times\prod_{i=1}^{p-1}\prod_{j=1}^{Bi/2}
 \left|v^+_{i,j}v^-_{i,j}\right|^{\lfloor p/i\rfloor},\\
 v^+_{i,j}={}&(2j+2)p-ia,\qquad
 v^-_{i,j}=(2j-2)p+ia.
\end{split}
\tag{5}
\]

Here Bi/2 is an integer since B is even. Every displayed v is nonzero: for v^+, a zero would imply p divides i, while 1<=i<p; v^- is positive.

To prove (5), expand the quadratic recurrence into ordered full binary trees with p leaves. Each leaf contributes one leading amplitude. At an internal node of total mass n, let the velocity child have mass i<n and stream frequency 2j. The stream inverse at delta_0 contributes plus or minus p/(2v^+_{i,j}) or p/(2v^-_{i,j}). The radial factors P_i=(2p-ia)/p or p_{n-i}=(p-(n-i)a)/p cancel that numerator p. The trigonometric product contributes a factor 1/2, and the stationary inverse contributes (p-a)/(a(n-1)). Thus this node's scalar denominator divides

\[
 4a(n-1)v^+_{i,j}\quad\hbox{or}\quad4a(n-1)v^-_{i,j}.
\]

There are p-1 internal nodes. Distinct nodes of the same mass n have disjoint leaf sets, because one cannot be a proper descendant of another of equal mass. There are at most floor(p/n) such nodes. The selected velocity subtrees of any fixed mass i likewise have disjoint leaf sets and number at most floor(p/i). The frequency support bound gives 1<=j<=Bi/2. These statements prove that every tree denominator divides D_p, so the denominator of their finite sum also divides D_p. No count of the number of trees is needed.

Since kappa_p is a nonzero rational number, (5) implies

\[
 |\kappa_p|\ge D_p^{-1}.
 \tag{6}
\]

## 2. Height estimate

For every factor in (5),

\[
 |v^\pm_{i,j}|\le(B+3)ip\le(B+3)p^2.
\]

The number of stream factors, with multiplicity, is

\[
 B S_p,\qquad S_p=\sum_{i=1}^{p-1}i\lfloor p/i\rfloor.
\]

Reversing the finite sums and using floor(p/k)<=p/k gives

\[
\begin{split}
 S_p&\le\frac12\sum_{k=1}^{p}
 \left((p/k)^2+p/k\right)\\
 &\le\frac{\pi^2}{12}p^2+\frac p2(1+\log p).
\end{split}
\tag{7}
\]

Consequently the logarithm of the stream product in (5) is at most

\[
 B S_p\big(2\log p+\log(B+3)\big)
 =\left(\frac{B\pi^2}{6}+o(1)\right)p^2\log p.
\]

The remaining factors satisfy

\[
 \log Q^p=p\log Q,\quad
 \log(4a)^{p-1}\le p\log(4p),\quad
 \sum_{n=2}^p\lfloor p/n\rfloor\log(n-1)
 \le p\log p(1+\log p).
\]

Their combined logarithm is o(p^2 log p). Hence, uniformly over the allowed a for this fixed input,

\[
 \boxed{\log D_p\le
 \left(\frac{B\pi^2}{6}+o(1)\right)p^2\log p.}
 \tag{8}
\]

All constants implicit here depend only on B and Q. In particular, if beta>B pi^2/6 is fixed, then

\[
 |\kappa_p|\ge p^{-\beta p^2}
 \tag{9}
\]

at all sufficiently large admissible prime centers.

## 3. A uniform analytic neighborhood and remainder bound

Fix epsilon>0. Restrict to centers delta_0 in [epsilon,1-epsilon] and take p sufficiently large depending on epsilon. Put

\[
 R_p=\frac1{4p^2}.
\]

For every i<p, every stream linear divisor at the center is a nonzero integer divided by p, with modulus at least 1/p. On the complex closed disk |z-delta_0|<=R_p its change is at most i R_p<1/(4p), so its modulus is at least 3/(4p). Thus f_n(z) is holomorphic on a neighborhood of this disk for n<=p. The factor c(z)-1=z/(1-z) has a uniformly bounded inverse there.

At i=p, the single vanishing stream divisor is 2j_0+2-pz, where j_0=a/2-1. On the boundary circle its modulus is p R_p=1/(4p). The other divisors remain nonzero throughout the disk. Therefore the uniform estimate

\[
 \|g_i(z)\|_{\ell^1}\le4p\|f_i(z)\|_{\ell^1}
 \tag{10}
\]

holds for i<p on the whole disk and for i=p on its boundary. The angular bandwidth is at most Bi, while |P_i(z)|<=4i and |p_j(z)|<=3j for sufficiently large p. The stationary inverse has modulus at most 2/(epsilon(n-1)). Writing X_n=n||f_n|| gives on the applicable disk or boundary

\[
 X_n\le \frac{112B}{\epsilon}p
 \sum_{i+j=n}X_iX_j.
 \tag{11}
\]

The Catalan recurrence now supplies a constant C depending only on epsilon, B and f_1, not on a or p, such that

\[
 \|f_n(z)\|_{\ell^1}\le(Cp)^n
 \quad(n\le p),\qquad
 \|f_{p+1}(z)\|_{\ell^1}\le(Cp)^{p+1}
 \quad(|z-\delta_0|=R_p).
 \tag{12}
\]

For completeness, the majorant of (11) is
X_n<=Cat_{n-1}(112Bp/epsilon)^{n-1}||f_1||^n, and Cat_{n-1}<=4^{n-1}. Choosing C at least max(1,448B/epsilon)max(1,||f_1||) proves (12).

Only g_p has a pole at delta_0 in the order p+1 recurrence. That pole is at most simple. Consequently

\[
 H(h)=h f_{p+1}(\delta_0+h)
\]

is holomorphic on a neighborhood of |h|<=R_p, and its boundary norm is at most R_p(Cp)^{p+1}. Cauchy's coefficient estimate, followed by a geometric sum, gives for |h|<=R_p/2

\[
 \left\|f_{p+1}(\delta_0+h)-\frac{\operatorname{Res}_p}{h}\right\|_{\ell^1}
 \le2(Cp)^{p+1}.
 \tag{13}
\]

Indeed, if H=sum H_k h^k, then ||H_k||<=R_p(Cp)^{p+1}R_p^{-k}, and summing k>=1 after division by h proves (13). This also bounds each individual sine amplitude of the remainder.

## 4. The nonzero pole cannot be canceled

The pole formula in topic15 gives a particularly useful component:

\[
 [\sin((L+2j_0)\theta)]\operatorname{Res}_p
 =-\frac{\kappa_p j_0(L+\gamma_0)\alpha_L}
 {2p^2(c_0-1)},\qquad
 \gamma_0=1-\delta_0.
 \tag{14}
\]

For p>=4/epsilon, j_0>=epsilon p/4, L+gamma_0>=1, and 1/(c_0-1)>epsilon. Therefore

\[
 |[\sin((L+2j_0)\theta)]\operatorname{Res}_p|
 \ge c_*\frac{|\kappa_p|}{p},\qquad
 c_*=\frac{\epsilon^2|\alpha_L|}{8}>0.
 \tag{15}
\]

Choose beta strictly between B pi^2/6 and tau and write eta=tau-beta>0. The centers in (2) eventually belong to some fixed [epsilon,1-epsilon], and their distances h from delta satisfy |h|<R_p/2. Combining (9), (13) and (15) yields

\[
 \left|[\sin((L+2j_0)\theta)]f_{p+1}(\delta)\right|
 \ge c_*p^{\eta p^2-1}-2(Cp)^{p+1}.
\]

The first term dominates because its logarithm has positive leading term eta p^2 log p, whereas the subtracted term has logarithm O(p log p). For all sufficiently large primes in this subsequence the right side is at least c_* p^{eta p^2-1}/2. Taking the (p+1)-st root tends to infinity. This proves (3). Each real sine amplitude is bounded by twice the uniform norm, so the same root conclusion holds for the uniform norm.

Amplitude homogeneity gives f_n(lambda f_1)=lambda^n f_n(f_1), proving the assertion for a fixed nonzero real multiple.

## 5. An explicit common arithmetic class

Let U be the irrational delta in (0,1) satisfying

\[
 0<|\delta-a/p|<p^{-p^3}
\]

for infinitely many admissible prime centers. Then U is a dense G_delta of Lebesgue measure zero, and every element is Liouville. Every delta in U gives radius zero simultaneously for every rational finite odd-sine profile with nonzero first harmonic, and for their nonzero real multiples.

To check the set statements directly, for each integer N take the union of the open punctured intervals of the displayed radii at all admissible prime centers p>N. Each union is open and dense in (0,1): any open interval contains an even-numerator center for every sufficiently large prime, and a punctured neighborhood of that center. Their countable intersection, intersected with the irrationals, is a dense G_delta by the Baire theorem. Its measure is zero since the total length of all intervals with p>N is at most sum_{p>N}2p p^{-p^3}, which tends to zero. For every fixed M the approximation is eventually stronger than p^{-M}, so its irrational elements are Liouville. The rational-profile conclusion follows from (1)-(2) for every finite B. These assertions do not say that all Liouville parameters diverge; topic18 gives convergent ones.

## Dependencies and open boundary

The proof uses the exact recurrence and support bound in topic01, the nonzero prime compatibility theorem in topic31, the pole formula in topic15, elementary binary-tree counting, the Catalan bound, and Cauchy's coefficient estimate. The fixed rational-coefficient hypothesis supplies the height lower bound. No such lower bound is claimed here for arbitrary real coefficients.

The Brjuno theorem allows convergent Liouville parameters. The present sufficient divergence condition is much stronger than failure of the Brjuno condition: its approximation exponent has order p^2 log p. Closing that arithmetic gap remains OPEN. No conclusion about the rational logarithmic continuation is implied.

## Finite verification

The independent exact audit checks51 admissible prime centers and inputs, comprising45 single-sine cases, two Candidate007 cases, and four newly generated rational three-mode cases. Every one of1591 density coefficient denominators divides the proposed D_p, every nonzero kappa obeys its lower bound, and every finite height inequality passes. Actual computation time was0.8589268811047077 seconds. The code is ../../code/quantitative_divergence_audit.py and records are in verification/checks.json. These finite checks corroborate the common-denominator formula; they do not replace the all-order argument.

## Independent review closure

At2026-10-31T04:16:52Z, the verifier checked the theory part's stepwise04:14Z review and confirmed the all-order argument. The review and its hash are retained in verification/. The asserted stream bound in topic46 is the coarse4p bound, which is valid also on the resonant boundary circle; the smaller4p/3 column estimate applies to the nonresonant disk case. Neither proof depends on a smaller boundary constant.
