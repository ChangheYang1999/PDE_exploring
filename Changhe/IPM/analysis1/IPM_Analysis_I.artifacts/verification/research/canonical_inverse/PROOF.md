# Canonical central strain and exact compactification

Status: analytical identities proved below. Numerical validation of X3 is a separate item. Written 2026-10-20 by the active verifier lane. This note is not an a posteriori existence theorem.

## Statement and hypotheses

Let $\rho\in C^2_{\mathrm{loc}}(\mathbb R^2)$ be even in $x$, odd in $y$, with $\rho=O(r^3)$ and $\nabla\rho=O(r^{1+\alpha})$ near zero for some $\alpha>0$, and $|\rho|+r|\nabla\rho|=O(r^\gamma)$ as $r\to\infty$, where $\gamma<1$. Write the sine coefficients of $\rho_x$ as $f_n(r)\sin(2n\theta)$, with coefficient convention $(1/\pi)\int_0^{2\pi}$. The canonical Poisson solution has the mode formula

$$\psi_n(r)=\frac{r^{-2n}\int_0^r s^{2n+1}f_n(s)\,ds+r^{2n}\int_r^\infty s^{1-2n}f_n(s)\,ds}{4n}.$$

For its central strain, when the canonical solution is $C^2$ near zero,

$$c=\psi_{xy}(0)=\frac12\int_0^\infty \frac{f_1(r)}r\,dr=\frac1\pi\int_{\mathbb R^2}\rho(x,y)\frac{y(3x^2-y^2)}{(x^2+y^2)^3}\,dx\,dy.$$

Equivalently, with $a_3(r)=(1/\pi)\int_0^{2\pi}\rho(r,\theta)\sin(3\theta)\,d\theta$,

$$c=\int_0^\infty a_3(r)r^{-2}\,dr.$$

The gradient condition at zero follows, for example, from the prompt's $C^{2,\alpha}$ regularity and strong continuous center factorization: the latter makes all Taylor coefficients of order at most two vanish. These estimates suffice for the integrals above. No assertion about convergence of every differentiated angular series is needed for the strain identity.

## Green formula

Put $m=2n$, $A(r)=\int_0^r s^{m+1}f_n(s)\,ds$ and $B(r)=\int_r^\infty s^{1-m}f_n(s)\,ds$. The integrals converge because $f_n=O(r^{1+\alpha})$ at zero and $f_n=O(r^{\gamma-1})$ at infinity. The proposed function is $(r^{-m}A+r^mB)/(2m)$. Differentiation cancels the terms $r f_n$ and gives $\psi_n'=(-r^{-m-1}A+r^{m-1}B)/2$. Differentiating again proves $-(\psi_n''+\psi_n'/r-m^2\psi_n/r^2)=f_n$.

The omitted homogeneous terms are $r^{-m}$, singular at zero, and $r^m$, whose velocity is not sublinear for $m\ge2$. Thus regularity and the canonical sublinear condition select the displayed mode. For $m=2$, $r^{-2}\psi_1(r)\to\frac14\int_0^\infty f_1(s)s^{-1}ds$. Since $r^2\sin(2\theta)=2xy$, this gives the strain coefficient. Higher modes do not contribute to the quadratic Taylor polynomial. One can identify the quadratic coefficient by taking its angular projection before passing to zero, avoiding an exchange of an infinite differentiated series.

## Integration by parts

Since $\sin(2\theta)=2xy/r^2$, the first strain integral equals $(1/\pi)\int \rho_x xy/r^4\,dX$. Integrate by parts on $\epsilon<r<R$. The boundary terms have absolute bounds $C\epsilon^2$ and $C R^{\gamma-1}$ respectively. Both vanish. The negative $x$ derivative of $xy/r^4$ is $y(3x^2-y^2)/r^6$. This proves the density formula. Its integrand is absolutely integrable: it is $O(1)$ at zero before the area element, and $O(r^{\gamma-3})$ at infinity. The identity $\sin(3\theta)=\sin\theta(3\cos^2\theta-\sin^2\theta)$ gives the one-dimensional radial formula.

For a finite annulus the corresponding endpoint term is not zero. If $a_1,a_3$ are the first and third sine coefficients of $\rho$, direct differentiation gives

$$\frac12\int_a^b f_1(r)r^{-1}dr=\int_a^b a_3(r)r^{-2}dr+\frac14\left[\frac{a_1(r)+a_3(r)}r\right]_a^b.$$

This term must be included when comparing truncated derivative and density implementations.

## Exact X3 compactification

Take the trial formula from PROMPT.md with exact stored binary64 values $L,k,r_0$, spline knots and coefficients, and $p=6+2k/(2-k)$. Define $q=1-(1+u^2)^{-(1-k)/2}$, $u=r/L$, and separate the logarithmic radial base as

$$H=\frac{k-3}{2}\log(1+u^2)+S(q,\theta).$$

Then the exact strain of the trial density, including its entire formula-defined exterior, is

$$c=\frac{4L^2}{\pi(1-k)}\int_0^1\int_0^{\pi/2}\cos^2\theta\sin\theta\sin(3\theta)\exp(S(q,\theta))\,d\theta\,dq.$$

Indeed, inserting $\rho=L^3u^3\cos^2\theta\sin\theta\exp(H)$ in the density formula produces the radial weight $L^2u\,du$. With $v=1-q$ and $b=2/(1-k)$ one has $u^2=v^{-b}-1$ and $u\,du=v^{-b-1}dq/(1-k)$. The logarithmic base contributes $v^{(3-k)/(1-k)}$, and the exponents cancel exactly. Reflection across the axes accounts for the factor four.

For evaluation on the compact interval, put

$$s=1-v^b,\qquad \chi=\frac{s}{s+r_0^2(1-s)},$$

and use

$$S=\sum_{m=0}^{200}\chi^{\max(m-1,0)}b_m(q)\cos(2m\theta)+s^{p/2}|\cos\theta|^{p-2}\sin^2\theta\,T(2q-1).$$

The limits are $s=\chi=1$ at $q=1$, and $s=\chi=0$ at $q=0$; the two modes with exponent zero retain multiplier one there. Every $b_m(0)$ is exactly zero because its first clamped-spline coefficient is zero. The compact integrand is bounded and continuous, so ordinary interval rectangles already give valid enclosures. Gauss quadrature without an explicit remainder does not.

## Scope and dependencies

The Green ODE, elementary differentiation, and integration by parts are the analytical dependencies. The use of the strain for arbitrary admissible densities presupposes a canonical $C^2$ Poisson solution near zero. The compactification identity is unconditional for the explicit X3 trial, whose local regularity and sublinear tail ensure convergence. This note does not validate a full-plane residual, a linear inverse, or any closing inequality.

## Certified quadrature by complex derivative bounds

This subsection states the enclosure method to be implemented and checked separately. Its validity does not imply that a particular computation has passed its bounds.

For an interval $[a,b]$ of length $\ell$ and $n$-point Gauss-Legendre quadrature $Q_n$, suppose the real function $f$ extends holomorphically to every complex disk of radius $R$ centered on $[a,b]$, with $|f|\le M$ on their union. The Gaussian error formula and Cauchy's derivative bound give

$$\left|\int_a^b f-Q_nf\right|\le \ell M\,C_n(\ell/R)^{2n},\qquad C_n=\frac{(n!)^4}{(2n+1)((2n)!)^2}.$$

For completeness, the monic orthogonal polynomial on the interval is a scaled Legendre polynomial. Its squared integral is $\ell^{2n+1}(n!)^4/((2n+1)((2n)!)^2)$. The Hermite interpolation remainder at the Gaussian nodes, each counted twice, is bounded by $\|f^{(2n)}\|_\infty/(2n)!$ times that squared integral. Integration yields the claimed Gaussian bound after Cauchy's inequality $\|f^{(2n)}\|_\infty\le(2n)!M/R^{2n}$.

For tensor quadrature on a rectangle, decompose the error as $(I_q-Q_q)I_\theta f+Q_q(I_\theta-Q_\theta)f$. The Gaussian weights are positive and sum to the interval length. Therefore separate uniform bounds on the holomorphic extensions in $q$ and in $\theta$ suffice; a joint complex extension is unnecessary. The resulting global bound is

$$E\le \frac\pi2\sum_i\ell_i M_i^{(q)} C_{n_q}(\ell_i/R_i)^{2n_q}+\sum_j d_j M_j^{(\theta)}C_{n_\theta}(d_j/S_j)^{2n_\theta},$$

where the covered $q$ range has length at most one. The function being integrated is $f=\cos^2\theta\sin\theta\sin(3\theta)e^{S(q,\theta)}$. On a real $q$ knot span its spline has a unique degree-seven polynomial extension, which is the extension used for the Cauchy estimate. Crossing other knot positions in this polynomial extension does not invalidate the error bound on the original span.

A sufficient bound for a radial complex domain is

$$M_i^{(q)}=\exp\left(\sum_m|b_m(q)\chi(q)^{\max(m-1,0)}|+B_p|s(q)^{p/2}T(2q-1)|\right),$$

with all terms bounded over the domain and $B_p=\max_{0\le t\le1}t^{p-2}(1-t^2)$. Its exact expression is $B_p=((p-2)/p)^{(p-2)/2}(2/p)$, obtained by differentiating with respect to $t^2$. The real angular kernel has absolute value at most one. Branch choices for $(1-q)^b$ and $s^{p/2}$ must be verified on the entire complex enclosure, and the denominator defining $\chi$ must exclude zero.

For angular complex domains, real spline convexity gives $|b_m(q)|\le C_m=\max_i|c_{i,m}|$, $0\le\chi,s\le1$, and $|T(2q-1)|\le C_T=\sum_j|t_j|$. Thus

$$M_j^{(\theta)}\le |\cos^2\theta\sin\theta\sin(3\theta)|\exp\left(\sum_m C_m|\cos(2m\theta)|+C_T|\cos^{p-2}\theta\sin^2\theta|\right).$$

The angular complex boxes used must stay in a region where the chosen $\cos^{p-2}\theta$ is analytic. Real integration occurs on $[0,\pi/2)$, where this branch agrees with the absolute-power ansatz.

Endpoint strips can be enclosed without derivatives. Globally on the real rectangle, $|S|\le C_\Sigma+C_TB_p$, where $C_\Sigma=\sum_m C_m$. Two radial strips of combined width $w$ contribute at most $w(\pi/2)\exp(C_\Sigma+C_TB_p)$. For an angular strip $\pi/2-d\le\theta\le\pi/2$, $\cos\theta\le\pi/2-\theta$, so its integral is bounded by

$$\frac{d^3}{3}\exp(C_\Sigma+C_Td^{p-2}).$$

Adding both strip bounds is safe even when it counts their overlap twice. Every bound and final quadrature sum must use outward arithmetic. The prefactor $4L^2/(\pi(1-k))$ is applied only after the unscaled integral and all errors have been enclosed. No guessed integration tolerance replaces these explicit remainder bounds.
