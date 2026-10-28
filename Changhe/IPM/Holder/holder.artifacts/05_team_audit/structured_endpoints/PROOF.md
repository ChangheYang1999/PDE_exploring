# Endpoint regularization of the polygonal witness

## Statement and dependencies

Let $I(\alpha,a)$ be the admissible polygonal-witness increment in `../structured_layercake/PROOF.md`, with $a>0$, $0<\alpha<1$, and

$$I(\alpha,a)=2^{\alpha-1}\alpha\int_0^\infty t^{\alpha-1}J_a(t)\,dt.$$

All operators, spaces and normalizations are as in that proof and `../../01_setup/PROOF.md`. In particular $C_\alpha,D_\alpha\ge I(\alpha,a)$ for both homogeneous inputs and the supremum over real $C_c^\infty$ inputs. The exact line and circle primitives $\mathcal L$ and $\mathcal A$ below are those already proved in the layer-cake formula.

We prove analytic regularity of

$$K_a(t)=J_a(t)+\frac4\pi\log t\quad\hbox{at }t=0,
\qquad R_a(u)=\frac{J_a(1/u)}u\quad\hbox{at }u=0,$$

with

$$K_a(0)=j_0(a)=\frac{\sqrt3\arctan(1/a)-\tfrac12\log(1+1/a^2)-2\log2}{\pi},
\qquad R_a(0)=\frac{3\sqrt3}{4\pi}.$$

Consequently, for each fixed $a>0$,

$$I(\alpha,a)=\frac2{\pi\alpha}+\frac{2\log2}{\pi}+\frac{j_0(a)}2+O(\alpha)\quad(\alpha\downarrow0),$$

$$\lim_{\alpha\uparrow1}(1-\alpha)I(\alpha,a)=\frac{3\sqrt3}{4\pi}.$$

The small-exponent additive term is maximized over this family at $a=1/\sqrt3$ and equals $1/(2\sqrt3)+\log2/(2\pi)$. This is a lower-bound-family optimum, not an exact operator norm.

## Regularized expression at zero

If $0<t<\min\{a/(3-\sqrt3),a,1/2\}$, all small-$t$ branches in the layer-cake formula are fixed. Write $s=a+(\sqrt3-2)t$. The only singular terms are

$$\mathcal L_{0,1+t}(t)-\mathcal L_{0,t}(t)
=-\frac1\pi\log t+\frac{\log(1+4t^4)-2\log2}{4\pi}.$$

This follows by multiplying the two positive quadratic factors $1+2t+2t^2$ and $1-2t+2t^2$. Thus the following formula extends regularly to $t=0$:

$$K_a(t)=\frac{\log(1+4t^4)-2\log2}{\pi}
+4\left[-\mathcal L_{0,1+t}(s)+\mathcal L_{1/\sqrt3,1+(2t-a)/\sqrt3}(s)
+\mathcal L_{0,t}(a)+\mathcal A_{t,a}(\pi/6)-\mathcal A_{t,a}(0)
-\mathcal L_{-1/\sqrt3,(2t+a)/\sqrt3}(a+t/2)\right].$$

All logarithm arguments remain separated from zero in a neighborhood of $t=0$. Their branches are the continuous branches fixed in the earlier proof. At zero the circle difference vanishes. Reflection of the line primitive gives $\mathcal L_{-m,1-b}=-\mathcal L_{m,b}$. Evaluating at $s=a$ gives

$$j_0(a)=-\frac{2\log2}{\pi}+\frac2\pi\log\frac{a^2}{1+a^2}
+8\mathcal L_{1/\sqrt3,1-a/\sqrt3}(a),$$

which simplifies to the displayed formula. Analyticity implies $K_a(t)=j_0(a)+O(t)$.

## Regularized expression at infinity

For $t\ge\max\{2a,2\}$ the positive branch begins on its oblique line, the vertical and circular negative pieces vanish, and the negative ray begins where its two offsets meet at $x=1/2$. Set $u=1/t$ and

$$X=\sqrt3+(1-a/\sqrt3)u,
\quad A(u)=\frac{2\sqrt3+(1-2a/\sqrt3)u}{1+(\sqrt3-a u/\sqrt3)^2},$$

$$B(u)=\frac1{1+X(X-u)},\qquad E(u)=\frac1{4+(2a-\sqrt3)u}.$$

The line formula then gives exactly

$$R_a(u)=\frac3{4\pi}A(u)\,\frac{\log(1+uA(u))}{uA(u)}
+\frac{\sqrt3}{2\pi}B(u)\,\frac{\arctan(uB(u))}{uB(u)}
+\frac{\sqrt3}{\pi}E(u)\,\frac{\arctan(uE(u))}{uE(u)}.$$

The quotients are assigned their removable value one at zero. For sufficiently small nonnegative $u$, all denominators are positive and the principal argument in the line formula equals the arctangent used here. This proves analyticity and gives

$$R_a(0)=\frac3{4\pi}\frac{\sqrt3}2+\frac{\sqrt3}{2\pi}\frac14+\frac{\sqrt3}{\pi}\frac14
=\frac{3\sqrt3}{4\pi}.$$

In particular $J_a(t)=3\sqrt3/(4\pi t)+O(t^{-2})$.

## Endpoint limits

Split the integral at one. On $(0,1)$ write $J_a=-4\log t/\pi+K_a(t)$ and use

$$\int_0^1t^{\alpha-1}(-\log t)\,dt=\alpha^{-2},\qquad
\alpha\int_0^1t^{\alpha-1}K_a(t)\,dt=j_0(a)+O(\alpha).$$

The second statement follows because $K_a(t)-j_0(a)=O(t)$ near zero and is integrable with weight $1/t$ away from zero. The tail contributes $O(\alpha)$ at this endpoint. Expanding $2^{\alpha-1}$ proves the small-$\alpha$ formula. Its derivative with respect to $a$ has the sign of

$$j_0'(a)=\frac{1/a-\sqrt3}{\pi(1+a^2)},$$

so the unique maximizer is $a=1/\sqrt3$. Substitution proves the claimed maximum.

At the other endpoint, the tail decomposition $J_a(t)=R_a(0)/t+O(t^{-2})$ gives its pole $R_a(0)/(1-\alpha)$; all remainders stay bounded. Since $2^{\alpha-1}\alpha\to1$, the stated limit follows.

## Rigorous full-integral certification

Choose $t_0>0$ in the small-branch range and $u_0>0$ in the large-branch range, with $t_0<1/u_0$. Let $\mathcal K$ enclose $K_a([0,t_0])$ and $\mathcal R$ enclose $R_a([0,u_0])$. Then the two omitted pieces are enclosed by

$$\int_0^{t_0}t^{\alpha-1}J_a(t)\,dt
\in t_0^\alpha\left[\frac4\pi\left(\frac1{\alpha^2}-\frac{\log t_0}{\alpha}\right)+\frac{\mathcal K}{\alpha}\right],$$

$$\int_{1/u_0}^\infty t^{\alpha-1}J_a(t)\,dt
\in\mathcal R\frac{u_0^{1-\alpha}}{1-\alpha}.$$

These are interval inclusions, with all factors positive except the explicitly handled regularized interval. Combine them with interval cells in the middle and multiply by $2^{\alpha-1}\alpha$. The result encloses the full witness value on both sides.

For interval evaluation of the removable quotients, use the Taylor series of $\log(1+z)/z$ and $\arctan z/z$. After $N$ terms, for $|z|\le r<1$, absolute remainder bounds are respectively $r^N/((N+1)(1-r))$ and $r^{2N}/((2N+1)(1-r^2))$. These follow term by term from the geometric series and remain valid on interval arguments containing zero. No singular numerical division by zero is used.
