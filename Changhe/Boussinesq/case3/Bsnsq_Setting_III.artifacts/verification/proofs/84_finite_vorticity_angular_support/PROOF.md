# Finite angular vorticity implies the excluded finite-mode system

Status: CONFIRMED by independent derivation and the written actual Opus5.5 audit87 of the Fourier step. Its application depends on the separately checked packet83; lead review pending. This is a restricted exclusion, not a full B2 endpoint.

## Statement

There is no smooth B2 profile in class A whose vorticity has finite angular Fourier support, with a fixed maximal angular degree independent of radius. Here class A is the class already reduced from the prompt's polynomial-tail, sublinear-velocity target in packet40. The proof uses its automatic derivative estimates from packet36:

$$
|D^\alpha\Theta(X)|\le C_\alpha(1+|X|)^{m-|\alpha|},
\qquad m=1-\frac2\beta\in[0,1),
\tag{1}
$$

and the stream and vorticity estimates of packet83. For $\beta<2$ the independent exclusion in packet01 already applies. Thus the new argument concerns $\beta\ge2$.

More generally, the conclusion holds for any smooth profile with the parity, nonzero center jets, canonical sublinear relative inverse, and the estimates used in packets83 and (1). It does not exclude profiles with infinitely many angular modes, or finite-mode approximations with nonzero residuals.

## 1. A Fourier division lemma

Let $f$ be a smooth function on $\mathbb R^2$ such that, for a real $m<1$ and every multi-index $\alpha$,

$$
|D^\alpha f(X)|\le C_\alpha(1+|X|)^{m-|\alpha|}.
\tag{2}
$$

Suppose $\partial_x f$ has angular Fourier degrees at most $L$, where $L\ge1$. Then $f$ has angular Fourier degrees at most $L-1$, meaning $P_nf=0$ for every $|n|\ge L$.

For a smooth function, angular degree at most $L$ means that its Fourier coefficients on every circle vanish for $|n|>L$. Equivalently, the rotation projections $P_n$ defined below vanish for these indices. On tempered distributions the projections are defined by $\langle P_n T,\phi\rangle=\langle T,P_{-n}\phi\rangle$, with bilinear distributional pairing. This defines the same notion of finite angular degree.

The Fourier transform is used in the tempered-distribution sense, with

$$
\widehat{\partial_x f}(k)=ik_x\widehat f(k).
$$

First, $\widehat f$ is smooth for $k\ne0$. Fix a desired differentiability order $j$. Choose an integer $K$ with $2K>m+j+2$. Then $X^\gamma\Delta^K f$ is integrable for every $|\gamma|\le j$, by (2). Therefore $\widehat{\Delta^K f}$ is $C^j$. The distributional identity

$$
\widehat f(k)=(-|k|^2)^{-K}\widehat{\Delta^K f}(k)
\qquad(k\ne0)
$$

proves $C^j$ regularity there. Since $j$ was arbitrary, the claim follows.

The Fourier transform commutes with rotations. Consequently it preserves each angular eigenspace and every finite sum of such eigenspaces, also for tempered distributions. This can be seen directly by applying the angular projection

$$
P_n f(X)=\frac1{2\pi}\int_0^{2\pi}
 e^{-in\varphi}f(R_\varphi X)\,d\varphi
$$

to the Fourier integral and changing variables by $R_\varphi$. Thus $\widehat{\partial_x f}$ also has degrees at most $L$. On a fixed circle $k=\rho(\cos\theta,\sin\theta)$, $\rho>0$, write it as a Laurent polynomial

$$
A_\rho(z)=\sum_{n=-L}^L a_n(\rho)z^n,\qquad z=e^{i\theta}.
$$

The smooth function $\widehat f$ and the identity $A_\rho=i\rho\cos\theta\,\widehat f$ show that $A_\rho(i)=A_\rho(-i)=0$. Hence the ordinary polynomial $z^L A_\rho(z)$ is divisible by $z^2+1$. It follows that

$$
\frac{A_\rho(z)}{\cos\theta}
=2z^{1-L}\frac{z^L A_\rho(z)}{z^2+1}
$$

has Laurent degrees between $1-L$ and $L-1$. On the circle, the quotient equals $i\rho\,\widehat f$, including at the two apparent singularities by continuity. Therefore $\widehat f$ has angular degree at most $L-1$ away from zero.

Let $P_{\le L-1}=\sum_{|n|\le L-1}P_n$, and put $g=f-P_{\le L-1}f$. The preceding conclusion means $\widehat g$ is supported at the single point $0$. A distribution with point support is a finite linear combination of derivatives of the Dirac distribution; the elementary argument is given below. Its inverse Fourier transform is a polynomial. On the other hand, rotations preserve the bound (2), so

$$
|g(X)|\le C(1+|X|)^m,\qquad m<1.
$$

Any such polynomial is constant, or zero if $m<0$. Since $P_{\le L-1}g=0$ and that projection includes constants, $g=0$. This proves the lemma.

For completeness, the distribution fact used here needs no regularity assumption on $\widehat g$. A distribution supported at $0$ has finite order $J$ on a fixed compact neighborhood of $0$. If a test function has all derivatives through order $J$ zero at $0$, multiply it by a cutoff supported in the ball of radius $\varepsilon$ and equal to one closer to $0$. Its derivatives through order $J$ are $O(\varepsilon)$ by Taylor's theorem and the product rule. The distribution gives the same value on this product as on the original test function, by its support, and the finite-order estimate makes this value tend to zero. Thus the distribution depends only on the finite jet through order $J$. The dual of that finite-dimensional jet space is exactly the span of the derivatives of the Dirac distribution.

## 2. Applying the lemma to B2

Throughout this application, reflection means $\Psi(-x,y)=-\Psi(x,y)$ and $\Theta(-x,y)=\Theta(x,y)$. In particular $U_1(0)=0$. It does not mean oddness under $X\mapsto-X$. We retain exactly $-\Delta\Psi=\Omega$ and $V=(-\Psi_y,\Psi_x)$.

Suppose first that the centered stream $\Psi$ has angular degree $N<\infty$. The nonzero strain $\Psi_{xy}(0)=1+\beta/2$ gives $N\ge2$. Its Laplacian $\Omega$ has degree at most $N$. Polar differentiation shows

$$
V\cdot\nabla\Omega
=\frac1r(\Psi_r\Omega_\theta-\Psi_\theta\Omega_r),
$$

which has angular degree at most $2N$. The other terms of

$$
\Theta_x=\beta r\Omega_r+V\cdot\nabla\Omega+\Omega
$$

have degree at most $N$. Hence $\Theta_x$ has degree at most $2N$. Estimate (1) and the Fourier division lemma imply that $\Theta$ has degree at most $2N-1$.

Now both $\Psi$ and $\Theta$ have finite angular support. Their tails and center data satisfy packet83, including the first two derivative bounds of vorticity. Subtracting a linear stream changes neither its strain nor vorticity, and preserves $\Psi=O(r^{2-\nu})$ and $\nabla\Psi=O(r^{1-\nu})$ since $0<\nu\le1/2$. Thus the centered pair satisfies all hypotheses of packet83, which excludes this possibility. Therefore the centered stream of a class-A profile cannot have finite angular support.

Finally suppose that $\Omega$ has finite angular support, of degree $N_0$. The canonical full-plane relative inverse preserves finite angular support up to the permitted centering linear term. Here is also a direct argument that does not presume the conclusion from a modal formula. For any angular index $|n|>N_0$, the stream coefficient obeys the radial harmonic equation

$$
\psi_n''+r^{-1}\psi_n'-|n|^2r^{-2}\psi_n=0.
$$

Smoothness at the origin removes $r^{-|n|}$ and leaves $\psi_n=A_n r^{|n|}$. The stream bound $\Psi=O(r^{2-\nu})$, $0<\nu\le1/2$, removes every such term with $|n|\ge2$. Degree one is the only possible remaining harmonic term; it is finite angular support and is fixed by centering the velocity. Reflection oddness in $x$ removes degree zero. The growth estimate also explicitly forbids adding any harmonic polynomial of degree at least two to the inverse. Thus $\Psi$ has degree at most $\max(N_0,1)$, and the preceding argument gives a contradiction.

The use of a centered stream means replacing the canonical uncentered stream by $\Psi-U_2(0)x$ when that observer representative is defined. This changes only degree one and produces precisely $V=U-U(0)$. It adds no independent strain or fitted drift.

## 3. Why the derivative hypothesis matters

The Fourier division lemma would be false if only smoothness and boundedness of $f$ were assumed. For example,

$$
f(x,y)=e^{-y^2}-e^{-(x^2+y^2)}
$$

is smooth, even in $x$, vanishes on $x=0$, and has $f=x^2+O(|X|^4)$ at the origin. Its derivative

$$
f_x=2x e^{-(x^2+y^2)}
$$

has angular degree one, while $f$ has infinitely many angular modes on every circle of positive radius. Indeed $e^{-r^2\sin^2\theta}$ is a nonconstant exponential of $\cos2\theta$ and cannot be a finite Laurent polynomial: as a function of the complex variable $z=e^{i\theta}$ it has an essential singularity at zero.

This example violates (2): at any fixed $y\ne0$, $f_y(x,y)$ tends to $-2y e^{-y^2}\ne0$ as $|x|\to\infty$. Its Fourier transform has a contribution supported on the line $k_x=0$, precisely the possibility excluded by smoothness of the Fourier transform away from the origin. No B2 equation is claimed for this example.

## Scope and dependencies

Dependencies are the independently proved class-A reductions and derivative estimates, the complete restricted theorem83, elementary Fourier transforms of tempered distributions, rotation projections, polynomial division, and the displayed point-support argument. The ordinary differential inequalities and radial-zero matching remain in packet83 and are not replaced by this Fourier lemma.

The conclusion forbids an exact finite angular expansion for vorticity within the smooth target. It provides no uniform positive lower bound on the residual of finite expansions and no obstruction to convergence as angular degree tends to infinity. It therefore does not justify early termination of the research run.
