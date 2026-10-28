# An exact one-dimensional formula for the gated two-point witness

Status: independently proved audit and strengthening of the lead investigator's gated witness. Numerical evaluations are separate from the proof. Conventions, the canonical homogeneous extension, and equality of smooth compact and full-space suprema are in `../../01_setup/PROOF.md`.

## Statement

Let $0<\alpha<1$, $x=(1/2,0)$, $y=-x$, $k=1/\sqrt2$, and $q=\sqrt2-1$. For $t>0$, put $c=kt$ and $\ell=(t-1)/2$, and define

$$J(t)=\frac1\pi\int_\ell^\infty\sum_{\epsilon=\pm1}
\mathbf1_{|r|+\epsilon c>0}(|r|+\epsilon c)
\left[\frac1{r^2+(|r|+\epsilon c)^2}
-\frac1{(r+1)^2+(|r|+\epsilon c)^2}\right]dr.$$

This is a nonnegative elementary integral, finite for every $t>0$. Define

$$L_{\rm cap}(\alpha)=\alpha\int_0^1t^{\alpha-1}J(t)\,dt,
\qquad L_{\rm gate}(\alpha)=\alpha\int_0^\infty t^{\alpha-1}J(t)\,dt.$$

Then

$$C_\alpha\ge L_{\rm gate}(\alpha)>L_{\rm cap}(\alpha),
\qquad D_\alpha\ge L_{\rm gate}(\alpha).$$

The functions are explicit lower bounds for the real homogeneous Hölder seminorm, and for the supremum over real smooth compact inputs. Their endpoint behavior is

$$L_{\rm cap}(\alpha)=\frac2{\pi\alpha}+\frac{\log2}\pi+O(\alpha),
\qquad
L_{\rm gate}(\alpha)=\frac2{\pi\alpha}+\frac{\log2}\pi+O(\alpha)
\quad(\alpha\downarrow0),$$

and

$$L_{\rm gate}(\alpha)=\frac{1+\sqrt2}{2\pi(1-\alpha)}+O(1)
\quad(\alpha\uparrow1).$$

The last coefficient is below the sharp coefficient proved using the degree-three homogeneous witness. It is not claimed optimal.

## The input and its seminorm

Set

$$u(z)=\frac12\operatorname{sign}(|z_1|-|z_2|)
\big(\sqrt2\,\big||z_1|-|z_2|\big|\big)^\alpha.$$

This equals $2^{\alpha-1}\operatorname{sign}(s)|s|^\alpha$ for the 1-Lipschitz function $s=(|z_1|-|z_2|)/\sqrt2$. The signed-power inequality gives $[u]_\alpha\le1$.

For $w_1\ge0$, define

$$v(w)=\max\{-h(w),\min(u(w-x),h(w))\},\qquad
h(w)=2^{\alpha-1}w_1^\alpha.$$

For $w_1<0$, set $v(w)=0$, and let $f(w)=v(w)-v(-w)$. The capped witness replaces $h$ by $\min(1/2,h)$.

On the right half-plane, $u(\cdot-x)$, $h$, and $-h$ have Hölder seminorm at most one. The maximum or minimum of two functions with this property again has this property, because the functions are 1-Lipschitz for the metric $|p-q|^\alpha$. Thus $v$ has the required estimate within that half-plane. The left half-plane follows by symmetry. For $p_1\ge0\ge q_1$,

$$|f(p)-f(q)|\le h(p)+h(-q)
\le2^{\alpha-1}(p_1^\alpha+(-q_1)^\alpha)
\le(p_1-q_1)^\alpha\le|p-q|^\alpha.$$

Hence $[f]_\alpha\le1$. Also $f(x)=f(y)=0$, and $f$ is odd. The uncapped function has at most $|w|^\alpha$ growth. It is therefore an admissible homogeneous input.

For completeness, on $B(x,r_0)$ with $r_0=1/(2+\sqrt2)$, the uncapped and capped witnesses both equal $u(w-x)$. Indeed, $|u(w-x)|\le(\sqrt2r)^\alpha/2$, while $h(w)\ge(1-2r)^\alpha/2$ and $\sqrt2r\le1-2r$ for $r\le r_0$. The additional cap is inactive because $\sqrt2r_0<1$.

## Level sets and integration in the vertical coordinate

For $w=(a,b)$ with $a>0$, set $d=|a-1/2|-|b|$. Then

$$f(w)=\frac12\operatorname{sign}(d)
\min\{\sqrt2|d|,2a\}^\alpha.$$

Thus

$$f(w)=\frac\alpha2\int_0^\infty t^{\alpha-1}\sigma_t(w)dt,$$

where, on the right half-plane,

$$\sigma_t(a,b)=\mathbf1_{a>t/2}
\left(\mathbf1_{|b|<|a-1/2|-t/\sqrt2}
-\mathbf1_{|b|>|a-1/2|+t/\sqrt2}\right),$$

and $\sigma_t(-w)=-\sigma_t(w)$. An indicator with negative upper threshold in the first term is zero. The capped input uses exactly the same levels, restricted to $0<t<1$.

For each $t>0$, $\sigma_t$ vanishes near both $x$ and $y$. Its increment integral converges absolutely at infinity. For the integral over all $t$, absolute Fubini is valid: the $t$ integral of $t^{\alpha-1}|\sigma_t|$ is $2|f|/\alpha$; near the two centers $f$ vanishes with Hölder order $\alpha$, and at infinity the difference kernel is $O(|w|^{-3})$. These estimates are integrable in two dimensions when $0<\alpha<1$.

The elementary antiderivative

$$\int K_{xx}(s,b)\,db=\frac{b}{2\pi(s^2+b^2)}$$

shows that the integral of $K_{xx}(x-w)\sigma_t(w)$ over the right half-plane is

$$\frac1\pi\int_{t/2}^\infty\sum_{\epsilon=\pm1}
\mathbf1_{p_\epsilon>0}\frac{p_\epsilon}{(a-1/2)^2+p_\epsilon^2}\,da,
\qquad p_\epsilon=|a-1/2|+\epsilon c.$$

Subtract the contribution of the odd reflection in the left half-plane. This replaces the denominator by the difference between $(a-1/2)^2+p_\epsilon^2$ and $(a+1/2)^2+p_\epsilon^2$. Put $r=a-1/2$ to obtain precisely $J(t)$.

The separate right and left integrals above need not converge at infinity. Their displayed difference is the integrable quantity, and all uses of the preceding formulas are made after this subtraction or with a common symmetric cutoff. Since $a>0$, the difference of the two reciprocal denominators is positive. This proves $J(t)>0$.

Oddness and the even kernel give the increment $T_{xx}\sigma_t(x)-T_{xx}\sigma_t(y)=2J(t)$. Consequently

$$T_{xx}f(x)-T_{xx}f(y)=\alpha\int_0^\infty t^{\alpha-1}J(t)dt.$$

The two-point distance is one. The local term in $R_1^2=T_{xx}-I/2$ contributes zero since $f(x)=f(y)=0$. The seminorm bound proves both claimed lower bounds. The compact approximation theorem in the setup proof transfers them to smooth compact inputs.

## Elementary evaluation of J

For $s\in\{-1,1\}$ and the nonzero denominators occurring below, put

$$H_{s,b}(r)=\frac s4\log\frac{r^2+(sr+b)^2}{(r+1)^2+(sr+b)^2}
+\frac12\left[\arctan\frac{2r+sb}{b}
-\arctan\frac{2r+1+sb}{b-s}\right].$$

Direct differentiation gives the rational integrand with $|r|$ replaced by $sr$. For $0<t\le1$,

$$\pi J(t)=\frac12\log(1+c^2)-\frac32\log c+\frac12\log(1+c)
-H_{-1,c}(\ell)
+\mathbf1_{t<q}\left[-\frac12\log\frac c{1-c}-H_{-1,-c}(\ell)\right].$$

At $t=q$ the last bracket is zero. The formula follows by splitting the rational integral at $r=0,\pm c$, retaining only intervals with positive numerator. The branch change occurs when $\ell=-c$, namely $t=q$.

For $t\ge1$, both retained intervals have $r\ge0$. With $D_0=\ell^2+(\ell+c)^2$ and $D_1=(\ell+1)^2+(\ell+c)^2$,

$$\pi J(t)=\frac14\log\frac{D_1}{D_0}
+\frac12\left[\arctan\frac c{t-1+c}-\arctan\frac{c-1}{t+c}\right]
+\frac12\log\frac{1+c}c.$$

This expression remains valid at $c=1$ by continuity and avoids any arctangent branch change there.

## Endpoint expansions and a bounded integral representation

For $0<t<q$, define $A=(1-t)/2$ and

$$P_0=4A^4+c^4,\qquad
P_1=((1-A)^2+A^2+c^2)^2-4A^2c^2.$$

The regularized function $K(t)=J(t)+2\log(t)/\pi$ has the nonsingular expression

$$\begin{aligned}
\pi K(t)={}&\log2+\tfrac12\log(1-c^4)+\tfrac14\log(P_0/P_1)\\
&+\tfrac12\left[-\arctan\frac c{1-t+c}+\arctan\frac c{1-t-c}
+\arctan\frac{t-c}{1+c}+\arctan\frac{t+c}{1-c}\right].
\end{aligned}$$

It extends analytically to zero, where $K(0)=\log2/\pi$ and $K'(0)=0$. These statements follow by substitution and differentiation; the logarithmic ratio contributes derivative $-1$, and the last two arctangents together contribute derivative $1$. Thus $K(t)-K(0)=O(t^2)$. For $q\le t\le1$, use the preceding elementary formula plus $2\log t/\pi$.

For the tail, let $R(s)=J(1/s)/s$, $0<s\le1$, and set

$$d(s)=\frac{(1-s)^2}{4}+\left(\frac{1-s}{2}+k\right)^2,
\qquad A(s)=\frac{1+2k-s}{2+2k-(1+2k)s}.$$

With the continuous functions $\mathcal L(z)=\log(1+z)/z$ and $\mathcal A(z)=\arctan(z)/z$, both defined as one at zero,

$$R(s)=\frac1\pi\left[\frac1{4d(s)}\mathcal L\!\left(\frac{s}{d(s)}\right)
+\frac{A(s)}2\mathcal A(sA(s))
+\frac1{2k}\mathcal L\!\left(\frac{s}{k}\right)\right].$$

The identity follows by combining the difference of the two arctangents using the subtraction formula; all denominators are positive. It extends analytically to $s=0$, where

$$R(0)=\frac1\pi\left(\frac12+\frac1{\sqrt2}\right)=\frac{1+\sqrt2}{2\pi}=:Q.$$

Therefore the exact formula useful for certification is

$$L_{\rm gate}(\alpha)=\frac2{\pi\alpha}
+\alpha\int_0^1t^{\alpha-1}K(t)dt
+\alpha\int_0^1s^{-\alpha}R(s)ds.$$

The first integral equals $K(0)+O(\alpha)$ as $\alpha\downarrow0$; the second is $O(\alpha)$. At the other endpoint, the first integral stays bounded and the second equals $\alpha Q/(1-\alpha)+O(1)$, since $R(s)-Q=O(s)$. This proves the stated expansions.

## Certificate method

Partition $[0,q]$ and $[q,1]$ for $K$, and $[0,1]$ for $R$. Evaluate each displayed expression with outward Arb interval arithmetic on each entire cell, then multiply by the exact positive weight integral. The weights are $b^\alpha-a^\alpha$ for $K$ and $\alpha(b^{1-\alpha}-a^{1-\alpha})/(1-\alpha)$ for $R$. The functions $\mathcal L$ and $\mathcal A$ are decreasing on $[0,\infty)$, as follows from their integral representations $\int_0^1(1+uz)^{-1}du$ and $\int_0^1(1+u^2z^2)^{-1}du$. Endpoint evaluation thus gives rigorous bounds even on cells touching zero. No quadrature remainder estimate is needed: each summand encloses the full cell integral.
