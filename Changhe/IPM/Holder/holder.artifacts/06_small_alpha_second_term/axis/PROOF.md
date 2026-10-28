# Exact axis finite part

## Statement

With the normalized increment density

$$G(w)=\frac{w}{\pi(w^2-1/4)^2},\qquad \nu_0(w)=\operatorname{Re}G(w),$$

define the circular finite part

$$N(0)=\lim_{\rho\downarrow0}\left[\frac12\int_{\mathbb C\setminus(B_\rho(1/2)\cup B_\rho(-1/2))}|\nu_0(w)|\,dA(w)+\frac2\pi\log\rho\right].$$

Then

$$\boxed{N(0)=\frac13+\frac{\sqrt3-1+\log\bigl(2/(2+\sqrt3)\bigr)}{\pi}.}$$

This evaluates the axis finite part appearing in the general-direction Hölder asymptotic theorem. It is not a formula for a finite-exponent operator norm. The principal-value normalization and its relation to the second term are in `../general_direction/PROOF.md`.

## Exact horizontal variation

For the calculation keep $a>0$ in $G_a(w)=w/[\pi(w^2-a^2)^2]$, then specialize to $a=1/2$. For $w=x+iy$, $y>0$, an $x$-primitive of $\operatorname{Re}G_a$ is

$$F(x,y)=-\frac{x^2-y^2-a^2}{2\pi\bigl((x^2-y^2-a^2)^2+4x^2y^2\bigr)}.$$

Its derivative has the sign of $x$ times

$$x^4-2(y^2+a^2)x^2-3y^4-2a^2y^2+a^4.$$

Put $c=\sqrt{y^2+a^2}$. The positive critical abscissas have squares $b_\pm^2=y^2+a^2\pm2yc$. Both exist when $0<y<a/\sqrt3$; only $b_+$ exists for $y>a/\sqrt3$. Direct substitution gives

$$F(0,y)=\frac1{2\pi c^2},\quad F(b_-,y)=\frac{c+y}{8\pi a^2y},\quad
F(b_+,y)=-\frac{c-y}{8\pi a^2y},\quad F(\infty,y)=0.$$

For $y<a/\sqrt3$, the primitive first increases, then decreases, then increases to zero. For larger $y$, it decreases and then increases. Its total variation on $x>0$ is therefore

$$S_a(y)=\int_0^\infty|\operatorname{Re}G_a(x+iy)|\,dx
=\begin{cases}
\dfrac{c}{2\pi a^2y}-\dfrac1{2\pi c^2},&0<y<a/\sqrt3,\\[4pt]
\dfrac1{2\pi c^2}+\dfrac{c-y}{4\pi a^2y},&y\ge a/\sqrt3.
\end{cases}$$

The two formulas agree at the transition.

## Strip finite part

Primitives of the two pieces are

$$L_a(y)=\frac{c+a\log(y/(a+c))}{2\pi a^2}-\frac1{2\pi a}\arctan(y/a),$$

$$H_a(y)=\frac1{2\pi a}\arctan(y/a)+\frac{c-y+a\log(y/(a+c))}{4\pi a^2}.$$

These follow from $\int c/y\,dy=c+a\log(y/(a+c))$. Evaluating at $y=a/\sqrt3$ and infinity gives

$$2\int_\varepsilon^\infty S_a(y)\,dy
=\frac1{6a}+\frac{\sqrt3+\log(2-\sqrt3)}{2\pi a}-2L_a(\varepsilon).$$

Since $L_a(\varepsilon)=[1+\log\varepsilon-\log(2a)]/(2\pi a)+o(1)$, specializing to $a=1/2$ yields

$$N_{\mathrm{strip}}=\lim_{\varepsilon\downarrow0}\left[2\int_\varepsilon^\infty S_{1/2}(y)\,dy+\frac2\pi\log\varepsilon\right]
=\frac13+\frac{\sqrt3-2-\log(2+\sqrt3)}\pi.$$

The factor two is exactly half of the four quadrant contributions.

## Conversion to circular cutoffs

Near each pole, the own kernel is $\cos(2\theta)/(2\pi r^2)$ and the other-pole kernel is bounded. Replacing the strip cutoff $|y|>\varepsilon$ by the circular cutoff $r>\varepsilon$ adds, in the limit, the own-kernel integral over $\varepsilon<r<\varepsilon/|\sin\theta|$. The bounded remainder contributes zero in the limit. There are two poles and the finite part has prefactor one half, so

$$N(0)-N_{\mathrm{strip}}=-\frac1{2\pi}\int_0^{2\pi}|\cos2\theta|\log|\sin\theta|\,d\theta.$$

The logarithm is integrable at its zeros; this also justifies the cutoff limit after restricting to small fixed pole neighborhoods. On a quadrant, split at $\pi/4$ and use

$$\int\cos2\theta\log\sin\theta\,d\theta
=\frac12\sin2\theta\log\sin\theta-\frac\theta2-\frac14\sin2\theta.$$

The full angular integral is $-2(1+\log2)$. Thus the conversion adds $(1+\log2)/\pi$, giving the displayed exact formula.
