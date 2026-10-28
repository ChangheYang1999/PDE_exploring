# The diagonal direction maximizes the circular finite part

Status: proved, with an independent audit requested. The argument gives an exact value for the second term of the full real Hölder operator norm.

## Statement

Use the notation and homogeneous Hölder spaces of `../general_direction/PROOF.md`. In particular, $C_\alpha$ is the common norm of $T_{xx}$ and $T_{xy}$, and $W(b)$ is the circular finite part of the increment density with poles $(\pm1/2,0)$. Then $W$ is strictly increasing on $0<b<\pi/4$. Consequently

$$\max_b W(b)=W(\pi/4)=\frac12,$$

and

$$\boxed{C_\alpha=\frac2{\pi\alpha}+\frac12+\frac{\log2-1}{\pi}+o(1)
\quad(\alpha\downarrow0).}$$

This does not identify the constant term for $D_\alpha=\|R_1^2\|$. It strengthens the general variational theorem by evaluating its one-parameter maximum exactly.

Dependencies: existence of the full second term from `../general_direction/PROOF.md`, and the exact diagonal finite part from `../diagonal/PROOF.md`. The direction maximization itself is proved below.

## Angular moments of the complex increment

Set $a=1/2$ and write the holomorphic version of the complex increment as

$$q(z)=\frac{z}{\pi(z^2-a^2)^2}.$$

The physical complex kernel is its complex conjugate. Reflection symmetry makes the real directional finite part even in its phase, so either convention gives the same cosine coefficients. For $n\ge1$, define the circularly regularized moment

$$M_n=\lim_{\varepsilon\downarrow0}\int_{\mathbb C\setminus(B(a,\varepsilon)\cup B(-a,\varepsilon))}
|q(z)|\cos(2n\arg q(z))\,dA(z).$$

The limit exists. Near each pole $q=\pm(2\pi h^2)^{-1}+O(1)$, so the leading angular moment integrates to zero on every circular annulus, while the error is locally integrable. The imaginary moment vanishes by conjugation symmetry.

We first integrate with a concentric annulus removed, $||z|-a|>\delta$. Put $u=r^2/a^2$. On the circle $|z|=r$, the complex moment has angular average obtained by taking the residue at zero of

$$-a^{-4}t^{-n}\frac{(u-t)^{2n-1}}{(1-ut)^{2n+1}},\qquad t=e^{2i\theta}.$$

The full circle traverses the $t$ circle twice, which leaves its average equal to the usual single-circle constant term. For $r<a$, the only enclosed pole is zero. Define

$$C_n(u)=[t^{n-1}]\frac{(u-t)^{2n-1}}{(1-ut)^{2n+1}}.$$

For $r>a$, both finite poles are enclosed and the sum of their residues is zero: the rational function decays as $t^{-n-2}$ at infinity. Including the radial factor $r^2/\pi$ and using $a=1/2$ therefore gives the annular-cutoff moment

$$M_n^{\mathrm{ann}}=-2\int_0^1 u^{1/2}C_n(u)\,du.$$

The polynomial coefficient can also be written

$$C_n(u)=\sum_{j=0}^{n-1}(-1)^j
\binom{2n-1}{j}\binom{3n-1-j}{n-1-j}u^{3n-2-2j}.$$

## Exact evaluation of the polynomial integral

Let $P_N^{(A,B)}$ denote the Jacobi polynomial with Rodrigues normalization

$$P_N^{(A,B)}(2v-1)=\frac{(-1)^N}{N!v^B(1-v)^A}
\frac{d^N}{dv^N}\bigl(v^{N+B}(1-v)^{N+A}\bigr).$$

Coefficient expansion gives

$$C_n(u)=u^nP_{n-1}^{(1,n)}(2u^2-1).$$

Thus, with $s=n/2-1/4>0$,

$$M_n^{\mathrm{ann}}=-\int_0^1v^sP_{n-1}^{(1,n)}(2v-1)\,dv.$$

The derivative identity, obtained directly from the polynomial coefficients or Rodrigues formula, is

$$\frac d{dv}P_n^{(0,n-1)}(2v-1)=2nP_{n-1}^{(1,n)}(2v-1).$$

Since $P_n^{(0,n-1)}(1)=1$, one integration by parts yields

$$M_n^{\mathrm{ann}}=-\frac1{2n}+\frac{s}{2n}
\int_0^1v^{s-1}P_n^{(0,n-1)}(2v-1)\,dv.$$

Apply Rodrigues again and integrate by parts $n$ times. All boundary terms vanish: at zero each has a positive power at least $v^s$, and at one a positive power of $1-v$. The remaining beta integral gives

$$s\int_0^1v^{s-1}P_n^{(0,n-1)}(2v-1)\,dv
=\prod_{k=0}^{n-1}\frac{s-n-k}{s+1+k}
=(-1)^nP_n,$$

where the scalar $P_n$ in this and subsequent formulas is

$$P_n=\frac{\Gamma(3n/2+1/4)\Gamma(n/2+3/4)}
{\Gamma(3n/2+3/4)\Gamma(n/2+1/4)}.$$

The distinction between the scalar $P_n$ and the earlier Jacobi polynomial with superscripts is explicit. Hence

$$M_n^{\mathrm{ann}}=\frac{(-1)^nP_n-1}{2n}.$$

## Converting the annular cutoff to circular pole cutoffs

Near either pole, the concentric annular cutoff is a smooth deformation of the strip $|\operatorname{Re}h|>\delta$. A local coordinate change with derivative the identity straightens it. The change in the leading homogeneous integrand is $O(|h|^{-1})$, hence integrable, and contributes zero to the difference of the two limiting cutoffs. Away from the poles the removed annulus has a vanishing integral by local boundedness and dominated convergence.

For the homogeneous local moment, replacing this strip by a circular hole adds, at each pole,

$$\frac1{2\pi}\int_0^{2\pi}\cos(4n\theta)
\log\frac1{|\cos\theta|}\,d\theta=\frac1{4n}.$$

This Fourier coefficient follows, for example, from the convergent Abel regularization of $-\log|1+re^{2i\theta}|$ followed by $r\uparrow1$; the logarithmic singularities are integrable. There are two poles. Therefore

$$\boxed{M_n=M_n^{\mathrm{ann}}+\frac1{2n}=\frac{(-1)^nP_n}{2n}.}$$

The cutoff correction is essential; omitting it gives a false sign pattern for the circular moments.

## Fourier coefficients of the directional finite part

Write $\phi=2b$ and denote the finite part as a function of phase by $\mathcal W(\phi)=W(\phi/2)$. The elementary Fourier expansion is

$$|\cos t|=\frac2\pi+\frac4\pi\sum_{n\ge1}
\frac{(-1)^{n+1}\cos(2nt)}{4n^2-1}.$$

For fixed circular cutoff, its insertion into the integral is justified by absolute uniform convergence. To pass to the finite part, subtract the two local leading homogeneous absolute kernels in fixed disks. The remaining integrand has an integrable bound uniform in $\phi$; equivalently, the finite parts of the cutoff functions converge uniformly in $\phi$. It follows that their Fourier coefficients converge to those of $\mathcal W$. The nonconstant coefficients are one half the displayed coefficients of $|\cos|$ multiplied by $M_n$. Thus

$$\mathcal W(\phi)=A-\frac1\pi\sum_{n\ge1}
\frac{P_n\cos(2n\phi)}{n(4n^2-1)}$$

for a constant $A$ independent of $\phi$. The series is uniformly absolutely convergent and determines the continuous function from its Fourier coefficients. Its derivative series is also uniformly absolutely convergent because $P_n$ is bounded:

$$\mathcal W'(\phi)=\frac2\pi\sum_{n\ge1}
\frac{P_n}{4n^2-1}\sin(2n\phi).$$

## Positivity of the sine series

Extend $P_n$ to a function $P(t)$ for $t>0$ by the same gamma quotient. Put $g(x)=\log\Gamma(x+3/4)-\log\Gamma(x+1/4)$. The standard digamma difference, which follows by termwise integration of its absolutely convergent reciprocal series, is

$$g'(x)=\int_0^\infty\frac{e^{-xu}}{2\cosh(u/4)}\,du.$$

As $\log P(t)=g(t/2)-g(3t/2)$, change variables in the two terms to obtain

$$\frac d{dt}\log P(t)=\int_0^\infty e^{-tu}
\left(\frac1{2\cosh(u/2)}-\frac1{2\cosh(u/6)}\right)du<0.$$

Its derivative is strictly positive. Therefore $P(t)>0$, $P'(t)<0$, and $P''(t)>0$. On $t\ge1$, the function $(4t^2-1)^{-1}$ is also positive, strictly decreasing, and strictly convex. Their product is strictly decreasing and strictly convex. Consequently

$$a_n=\frac{P_n}{4n^2-1}>0,\qquad
\Delta^2a_n=a_n-2a_{n+1}+a_{n+2}>0.$$

It tends to zero, and two summations of its second difference give

$$a_n=\sum_{m\ge n}(m-n+1)\Delta^2a_m.$$

For $0<x<\pi$, the finite triangular sine sum is

$$\sum_{n=1}^m(m-n+1)\sin(nx)
=\frac{(m+1)\sin x-\sin((m+1)x)}{2(1-\cos x)}\ge0.$$

The inequality $|\sin(kx)|\le k\sin x$ follows from the geometric-sum identity and the triangle inequality. The $m=1$ triangular sum is strictly positive. Absolute convergence justifies summing the preceding representation of $a_n$ in this order; it also follows by finite summation and a limit. Hence

$$\sum_{n\ge1}a_n\sin(nx)>0\qquad(0<x<\pi).$$

Taking $x=2\phi$ proves $\mathcal W'(\phi)>0$ for $0<\phi<\pi/2$, or equivalently $W'(b)>0$ for $0<b<\pi/4$. The symmetry reductions in the general theorem cover all other directions. The exact diagonal evaluation finishes the proof.
