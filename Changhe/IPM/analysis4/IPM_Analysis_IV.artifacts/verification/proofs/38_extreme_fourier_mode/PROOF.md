# The extreme Fourier mode has an explicit finite convergence radius

Status: CONFIRMED after independent adversarial review, 2026-10-31T03:52:43Z. See V049 and topic43 for the exact scope and evidence.

## Statement and notation

Fix 0<delta<1 and c=1/(1-delta). Let the nonzero leading density be a finite S1 sine polynomial with largest positive frequency L, where L is odd, and let alpha be its nonzero coefficient of sin(L theta). Set

\[
 B=L+1,\qquad d=c-1,\qquad \eta=B-\delta,\qquad
 a=\frac2\eta,\qquad b=\frac{2(B-1)}\eta.
\]

Thus B>=2 and 1<b<2. Define the positive beta integral

\[
 {\cal B}(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt,
 \qquad R_{\rm top}=\frac{4d}{|\alpha|}
       [a{\cal B}(a,b)]^{1/a}.
 \tag{1}
\]

For the pure recurrence wherever it exists, the coefficient A_n of sin((Bn-1)theta) in f_n is independent of every lower leading harmonic. It is

\[
 A_n=(-1)^{n-1}\alpha^n h_n,\qquad h_n>0,\qquad h_1=1.
 \tag{2}
\]

The power series H(z)=sum_(n>=1) h_n z^n has exact radius

\[
 R_H=4d[a{\cal B}(a,b)]^{1/a}.
 \tag{3}
\]

In particular, limsup |A_n|^(1/n)=1/R_top. If the full pure density recursion exists at all orders, its radius in C^0 of the circle is at most R_top. Its radius in the angular Wiener norm with strip sigma is at most exp(-B sigma) R_top. These are upper bounds on the full series radius, not convergence theorems for that series.

The same A_n is the entire top-frequency coefficient of every order-n polynomial in log r in the standard logarithmic recurrence, provided the only added homogeneous stream terms occur at resonances in the prescribed radial lattice. This coefficient is constant in log r. Consequently a generalized logarithmic density expansion cannot converge uniformly in angle at a fixed radius r with r^(-delta)>R_top. No claim is made about convergence at larger radii or about additional off-lattice channels.

## 1. A closed scalar recurrence at the highest frequency

The angular support induction gives density frequencies at most Bn-1 and stream frequencies at most Bn. The highest stream coefficient, at frequency Bi, is generated only by A_i and is

\[
 T_i=-\frac{A_i}{2[(B-\delta)i+2]}
     =-\frac{A_i}{2(\eta i+2)}.
 \tag{4}
\]

Its denominator is positive, so this particular mode never resonates. The highest output frequency Bn-1 in a product with i+j=n can only come from frequencies Bi and Bj-1. Its coefficient in the nonlinear expression is

\[
 \frac{T_iA_j}{2}\big[(2-i\delta)(Bj-1)
                    -(1-j\delta)Bi\big]
 =\frac{A_iA_j}{4}
       \left[1-\frac{2Bj}{\eta i+2}\right].
\]

Therefore

\[
 (n-1)d A_n=\frac14\sum_{i+j=n}
   \left[1-\frac{2Bj}{\eta i+2}\right]A_iA_j.
 \tag{5}
\]

This determines the top coefficients without any lower Fourier coefficient. After the sign and amplitude normalization in (2), it becomes

\[
 (n-1)d h_n=\frac14\sum_{i+j=n}
   \left[\frac{2Bj}{\eta i+2}-1\right]h_i h_j.
 \tag{6}
\]

Although an individual ordered summand need not be positive, pairing i,j gives the equivalent symmetric kernel

\[
 B\left[\frac{j}{\eta i+2}+\frac{i}{\eta j+2}\right]-1.
\]

For n=i+j>=2,

\[
 \frac{j}{\eta i+2}+\frac{i}{\eta j+2}
 \ge\frac{2n}{\eta n+4}.
\]

For example, subtracting the right side and putting over the positive common denominator leaves the numerator eta(eta n+2)(i-j)^2. The symmetric kernel is strictly positive because (B+delta)n>4. Induction proves h_n>0 for every n.

In the polynomial-log recurrence the same support argument holds. Resonant homogeneous stream modes have frequency n delta-2<Bn. If the top density coefficient is constant in log r, the top nonresonant Poisson inverse is also constant. Only top inputs can reach the top output, and their radial log derivatives vanish. Starting from f_1, induction proves that the top coefficient is exactly (5), with no positive log power. Free resonant stream amplitudes have strictly lower frequency and cannot change this conclusion.

## 2. Solving the scalar generating equation

Work first with formal power series, and put

\[
 H(z)=\sum_{n\ge1}h_nz^n,\qquad
 J(z)=\sum_{n\ge1}\frac{h_n}{\eta n+2}z^n,
 \qquad E=z\partial_z.
\]

Then eta E J+2J=H. Summing (6) gives

\[
 (d-BJ/2)E H=dH-H^2/4.
 \tag{7}
\]

Set x=H/(4d) and v=BJ/(2d). The system is

\[
 E x=\frac{x(1-x)}{1-v},\qquad
 E v=\frac2\eta(Bx-v).
 \tag{8}
\]

Near zero, x=z/(4d)+O(z^2) and v=2Bx/(eta+2)+O(x^2). Eliminating z and setting w=1/(1-v) gives the linear equation

\[
 \frac{dw}{dx}
  -a\frac{Bx-1}{x(1-x)}w
  =\frac{a}{x(1-x)}.
 \tag{9}
\]

An integrating factor is I(x)=x^a(1-x)^b, because b=a(B-1). The solution compatible with w(0)=1 satisfies

\[
 I(x)w(x)=a{\cal B}_x(a,b),\qquad
 {\cal B}_x(a,b)=\int_0^x t^{a-1}(1-t)^{b-1}\,dt.
 \tag{10}
\]

For real 0<x<1 this formula is positive. Also a B_x-I is strictly positive: it vanishes at zero and its derivative is (a+b)x^a(1-x)^(b-1). Thus 0<v<1 on this interval.

Using the first equation of (8),

\[
 \frac{d\log z}{dx}
 =\frac{1-v}{x(1-x)}
 =\frac1a\frac{d\log {\cal B}_x(a,b)}{dx}.
\]

The initial coefficient fixes the integration constant. The exact implicit solution is

\[
 \boxed{z=4d\,[a{\cal B}_x(a,b)]^{1/a},\qquad H(z)=4dx.}
 \tag{11}
\]

This formula defines an analytic inverse near zero. Indeed a B_x=x^a Phi(x), where Phi is analytic near zero and Phi(0)=1; the right side is 4d x Phi(x)^(1/a) with nonzero derivative. It satisfies the formal system and therefore has exactly the recursively specified coefficients.

## 3. Exact radius and a real boundary singularity

The map on the right side of (11) is strictly increasing and has nonzero derivative for 0<x<1. It is locally complex analytic with a locally analytic inverse at every such point, using the branch fixed by positive real values. It maps (0,1) onto (0,R_H), where R_H is (3).

Because every coefficient of H is positive, its first singularity in modulus must be on the positive real axis. The elementary fact needed here can be proved without a singularity theorem: if a power series with nonnegative coefficients has finite radius R but its real branch is analytic in a neighborhood of R, all derivative sums have finite limits at R. Taylor's formula at R and the binomial identity, with nonnegative summands, then make the original series converge at R+epsilon for sufficiently small positive epsilon, a contradiction. Applied to the analytic inverse along (0,R_H), this shows that the radius is at least R_H.

At x=1 the derivative of the map in (11) tends to zero, because b>1. The inverse derivative tends to positive infinity. Thus H is not analytic at z=R_H, and its radius is exactly R_H. More precisely, as z increases to R_H,

\[
 1-\frac{H(z)}{4d}
 \sim [ab{\cal B}(a,b)]^{1/b}
             (1-z/R_H)^{1/b}.
 \tag{12}
\]

This follows by integrating the beta integrand near one: B(a,b)-B_x(a,b) is asymptotic to (1-x)^b/b. Since 1/2<1/b<1, H has a finite boundary value 4d but an unbounded first derivative. Positivity also gives sum h_n R_H^n=4d by monotone convergence. No coefficient-by-coefficient asymptotic is inferred here from the real boundary law alone.

## 4. Consequences for the angular series

A sine coefficient A of a continuous real function f satisfies |A|<=4||f||_infinity/pi, by its Fourier integral. Hence the full density coefficient norm is at least pi|A_n|/4. The Wiener norm is at least |A_n| exp(sigma(Bn-1)). Cauchy-Hadamard therefore gives the radius upper bounds in the statement. The same Fourier coefficient extraction applies at every fixed log r to the polynomial-log density coefficients, because A_n is independent of that variable.

The result proves exact nontermination of this extreme Fourier sector and rules out an infinite radius in z for every finite nonzero leading sine polynomial. It is consistent with the Brjuno theorem, which supplies a positive radius for the full pure series under its arithmetic hypothesis. Other Fourier modes may have a smaller radius. In particular, the positive singularity of H describes the alternating, selected top-mode amplitudes; it does not locate a singularity of the original full angular function at a fixed angle.

## Dependencies and verification plan

Dependencies are the independently derived recurrence and Poisson inverse, finite Fourier support, elementary trigonometric products, a scalar analytic inverse, and the positive beta integral defined above. The exact top coefficients were compared with the independent Cartesian recurrence in five rational examples, for 41 density and 41 stream coefficients. Every comparison passed. The top density and stream coefficients in the independently verified delta=4/9 logarithmic data also match through order73, and every positive log-power coefficient in those modes is exactly zero. These checks are separate from the all-order proof.

The retained Arb512 enclosures give R_top=2.56653299384422569... and 1/R_top=0.389630681701142568... for sin(theta) at delta=1/sqrt(5). At delta=4/9 they give R_top=2.54171788408756549... and 1/R_top=0.393434694802481351... . The decimal displays here are approximations; the enclosing balls are in verification/checks.json. The actual combined check took 0.32232888974249363 seconds. Beta values were evaluated both as Gamma(a)Gamma(b)/Gamma(a+b) and as the incomplete beta at one; the enclosures overlap. The beta-gamma identity follows by substituting u=x+y and t=x/(x+y) in the positive double integral defining Gamma(a)Gamma(b).
