# Sharp energy growth forced by bounded decaying velocity

## Exact theorem

Let `c>0`, let `omega` be any finite real number, and let `U,P in C^1(R^3)` solve

\[
 (1-c)U+((cI-\omega J)y+U)\cdot\nabla U+\omega JU+\nabla P=0,
 \qquad \operatorname{div}U=0.
\]

Assume `U(y)->0` uniformly as `|y|->infinity`. Define

\[
 E(R)=\int_{|y|<R}|U(y)|^2\,dy,\qquad \beta=5-\frac2c.
\]

Then:

1. If `0<c<2/5` or `c>=1`, `U=0` and pressure is constant.
2. If `2/5<=c<1`, there is `L>=0` such that

\[
 E(R)=LR^\beta+o(R^{\beta-1})\qquad(R\to\infty).
\]

Moreover `L=0` if and only if `U=0`. Thus every nonzero profile in this range has `L>0`.

For the target range `2/5<c<1/2`, one has `0<beta<1`. The theorem forces infinite energy and the exact positive leading coefficient; it does not contradict velocity decay or prove nonexistence in that interval.

No derivative decay, vorticity integrability, symmetry, outgoing condition, or pressure normalization is an additional hypothesis. The canonical-pressure theorem A031 supplies the needed pressure representation. The estimates below contain no explicit rotation parameter.

## Dependencies and notation

Write `M=||U||_infinity`, which is finite by decay and continuity. Let `K_ij` be the kernel of the double Riesz transform away from zero:

\[
 K_{ij}(z)=\frac{3z_i z_j-\delta_{ij}|z|^2}{4\pi|z|^5}.
\]

The distributional transform includes the local term `-delta_ij delta_0/3`. Its `L^2` operator norm is bounded, directly by its bounded Fourier multiplier and Plancherel. The kernel obeys `|K(z)|<=C|z|^-3` and `|grad K(z)|<=C|z|^-4`.

The proof uses the exact local energy identity, the divergence theorem, this `L^2` bound, a kernel difference estimate, and dyadic summation. It does not invoke an external Liouville or energy-growth theorem.

## 1. A pressure estimate on one annulus

Suppose for some `0<=a<=3` that

\[
 E(R)\le C_a R^a\qquad(R\ge1).                         \tag{1}
\]

This is initially available with `a=3` from bounded velocity. Fix `R>=1`. On `|y|<2R`, canonical pressure can be written

\[
 P(y)-C_R=P_{\rm near}(y)+P_{\rm far}(y),
\]

where

\[
 P_{\rm near}=\sum_{i,j}R_iR_j(U_iU_j\,1_{|z|<4R}),
\]

and

\[
 P_{\rm far}(y)=\sum_{i,j}\int_{|z|\ge4R}
                 [K_{ij}(y-z)-K_{ij}(-z)]U_i(z)U_j(z)\,dz.
                                                               \tag{2}
\]

The kernel difference is absolutely integrable against bounded `U_iU_j`. This representation follows either by testing the canonical distribution against zero-mean tests supported in the ball, or by comparing gradients there. The remaining term is a spatial constant `C_R`. It may depend on `R`.

The near term satisfies

\[
 \|P_{\rm near}\|_2
       \le C\|U\otimes U\|_{L^2(B_{4R})}
       \le CM E(4R)^{1/2}\le C R^{a/2}.                     \tag{3}
\]

For the far term, the mean-value theorem and dyadic shells give

\[
\begin{aligned}
 |P_{\rm far}(y)|
 &\le CR\int_{|z|\ge4R}|U(z)|^2|z|^{-4}\,dz\\
 &\le CR\sum_{k\ge2}(2^kR)^{-4}E(2^{k+1}R)
 \le C R^{a-3},\qquad |y|<2R.                              \tag{4}
\end{aligned}
\]

The series converges since `a<=3<4`. On `A_R={R<|y|<2R}`, Cauchy-Schwarz now gives

\[
\begin{aligned}
 \int_{A_R}|P-C_R|\,|U|
 &\le \|P_{\rm near}\|_2 E(2R)^{1/2}
       +C R^{a-3}|A_R|^{1/2}E(2R)^{1/2}\\
 &\le C(R^a+R^{3a/2-3/2})\le C R^a.                       \tag{5}
\end{aligned}
\]

The last inequality uses `a<=3` and `R>=1`. Also `integral_(A_R)|U|^3<=M E(2R)<=C R^a`. Therefore

\[
 \int_{A_R}\big(|U|^3+2|P-C_R||U|\big)\,dy\le C R^a.    \tag{6}
\]

Every constant used here is finite. No pointwise bound on the local singular-integral pressure has been assumed.

## 2. Exact radial energy equation

Set `B=(cI-omega J)y+U` and `q=|U|^2/2`. The local identity is

\[
 \operatorname{div}(qB+PU)=(5c-2)q.
\]

Since `Jy` is tangent to centered spheres, the divergence theorem yields

\[
 cR E'(R)-c\beta E(R)=-F(R),
 \qquad F(R)=\int_{|y|=R}(|U|^2+2P)U\cdot n\,dS.          \tag{7}
\]

The pressure constant can be changed separately on each annular estimate, because `integral_(|y|=r) U dot n=0` for every `r`. Define `Z(R)=R^-beta E(R)`. Then

\[
 Z'(R)=-\frac{F(R)}{c R^{\beta+1}}.                         \tag{8}
\]

Using (6), coarea, and the pressure constant `C_R` on `R<=r<=2R`, gives for any `R<=r_1<r_2<=2R`

\[
 |Z(r_2)-Z(r_1)|\le C R^{a-\beta-1}.                       \tag{9}
\]

In particular all steps below control intermediate radii as well as dyadic endpoints.

## 3. Bootstrap the energy upper bound

Summing (9) from radius 1 up to radius R shows that (1) implies

\[
 E(R)\le
 \begin{cases}
 C R^{a-1},&a-\beta-1>0,\\
 C R^\beta\log(2R),&a-\beta-1=0,\\
 C R^\beta,&a-\beta-1<0.
 \end{cases}                                                \tag{10}
\]

An additional term `C R^beta` in the first line is absorbed for `R>=1`. This estimate uses an upper bound for `|Z|`, so no sign of the boundary flux is needed.

If `beta<0`, apply (10) successively with `a=3,2,1`. This gives `E(R)<=C`, so one more application with `a=0` gives either `C R^beta`, `C R^-1 log(2R)`, or `C R^-1`. Each tends to zero. Since `E` is nonnegative and nondecreasing, `E=0`, and `U=0`.

If `0<=beta<3`, start with `a=3` and apply (10). Whenever the current exponent exceeds `beta+1`, it drops by one. Once it is less than `beta+1`, (10) gives `E(R)<=C R^beta`. In the equality case, absorb the logarithm into `R^delta` with `0<delta<min(1,3-beta)`, then apply (10) once more. Thus in finitely many steps

\[
 E(R)\le C R^\beta\qquad(R\ge1).                          \tag{11}
\]

## 4. The leading coefficient and its positivity

Under (11), (9) has right side `C/R`. Its dyadic tail is summable, so `Z(R)` converges to a finite `L>=0` and

\[
 |Z(R)-L|\le C/R.                                          \tag{12}
\]

If `L=0`, this first gives `E(R)<=C R^(beta-1)`. A negative exponent immediately gives `U=0`. Otherwise use this new exponent `a=beta-1>=0` in (9), now summing from R to infinity because the limit is known to be zero. The result is `E(R)<=C R^(a-1)=C R^(beta-2)`. Repetition reaches a negative exponent in finitely many steps. Thus `L=0` forces `U=0`; the converse is immediate.

## 5. Exclusion for c>=1

If `beta>=3`, boundedness gives `Z(R)->0` when `beta>3`. When `beta=3`, decay gives `E(R)=o(R^3)`, so the same limit is zero. Start with `a=3` in (9) and sum its dyadic tail to infinity. Since `a-beta-1<0`, this gives `E(R)<=C R^(a-1)=C R^2`. Repeating with `a=2,1,0` gives `E(R)<=C R^-1`, hence `U=0`.

This uses the boundary limit at infinity before the backward bootstrap; it is not an extension of the forward sum (10) to a regime where that sum would be insufficient.

## 6. Improve the error to little-o using actual decay

It remains to improve (12) for `0<=beta<3`. Put

\[
 m(R)=\sup_{|y|\ge R}|U(y)|\longrightarrow0.
\]

Split the near pressure in Section 1 further into sources `|z|<R/2` and `R/2<=|z|<4R`. On `A_R`, the inner-source pressure is bounded by

\[
 C R^{-3}E(R/2)\le C R^{\beta-3}.
\]

The middle-source pressure has `L^2` norm at most

\[
 C m(R/2)E(4R)^{1/2}\le C m(R/2)R^{\beta/2}.
\]

The far pressure in (4) is `O(R^(beta-3))`. Consequently

\[
 \int_{A_R}|P-C_R||U|
 \le C m(R/2)R^\beta+C R^{3\beta/2-3/2}=o(R^\beta),        \tag{13}
\]

because `beta<3`. The cubic integral is at most `m(R)E(2R)=o(R^beta)`. Thus (9) improves to `o(1/R)` uniformly for endpoints in `[R,2R]`. More precisely its bound is `epsilon(R)/R` with `epsilon(R)->0`. The dyadic tail is at most

\[
 \frac2R\sup_{s\ge R}\epsilon(s)=o(1/R).
\]

This proves `Z(R)=L+o(1/R)`, or the stated `E(R)=LR^beta+o(R^(beta-1))`.

## Consequences and limits

For `2/5<c<1/2`, a nonzero profile necessarily has `E(R)~LR^beta` with `0<beta<1`; in particular it is not in `L^2`. If an added hypothesis gives `E(R)=o(R^beta)`, the profile is zero. For example, uniform velocity decay strictly faster than `R^{1-1/c}` implies this energy condition, with the usual elementary treatment of the logarithmic and integrable cases.

The energy theorem does not prove pointwise velocity asymptotics, derivative decay, or pointwise pressure decay. It does not classify internal B dynamics. Its exact power law is compatible with the expected rotating far-field tails and leaves the primary conjecture open.

This proof was independently reconstructed to audit the energy theorem announced in Theory Agent A's run status. It is available for cross-agent challenge. No numerical calculation or formal verification is used.
