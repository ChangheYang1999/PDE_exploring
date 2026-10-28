# A strict second-term lower bound for the original diagonal transform

Status: proved lower bound. The exact second term of $D_\alpha$ remains open.

## Statement

Let $C_\alpha$ and $D_\alpha$ be the real homogeneous Hölder seminorm operator norms of $T_{xx}$ and $R_1^2=T_{xx}-I/2$, with the definitions and extension modulo constants in `../../01_setup/PROOF.md`. Then

$$\liminf_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)
\ge \frac12+\frac{\log2-1}{\pi}+\frac2\pi\log\cosh\frac\pi4.$$

In particular, the exact expansion for $C_\alpha$ proved in `../../06_small_alpha_second_term/direction_maximum/PROOF.md` implies

$$\liminf_{\alpha\downarrow0}(D_\alpha-C_\alpha)
\ge \frac2\pi\log\cosh\frac\pi4>0.$$

The result is a lower bound, not an exact formula for the gap. No numerical integration is needed. The proof constructs globally admissible functions whose values at the two evaluation points are nonzero and opposite.

## An asymmetric signed-power lemma

Fix $A,B>0$ with $A+B=1$, let $0<\alpha<1$, and put

$$p=\frac1{1-\alpha},\qquad
M_\alpha=(A^p+B^p)^{-1/p},\qquad c=\frac12-A.$$

For a real variable $v$, define

$$P_\alpha(v)=M_\alpha\bigl(A(v_+)^\alpha-B((-v)_+)^\alpha\bigr).$$

Its real-line Hölder seminorm is at most one. On one side of zero, the estimate follows from $M_\alpha A\le1$, $M_\alpha B\le1$, and $|s^\alpha-t^\alpha|\le|s-t|^\alpha$. Across zero, Hölder's inequality gives

$$A s^\alpha+B t^\alpha
\le(A^p+B^p)^{1/p}(s+t)^\alpha\qquad(s,t\ge0).$$

Thus composing $P_\alpha$ with a 1-Lipschitz real function gives a Hölder function with seminorm at most one. Also, writing $H(A)=-A\log A-B\log B$,

$$\log M_\alpha=\alpha H(A)+O_A(\alpha^2).$$

This follows by differentiating $-(1-\alpha)\log(A^{1/(1-\alpha)}+B^{1/(1-\alpha)})$ at zero.

## A global odd construction with prescribed pole values

Take $x=(1/2,0)$, $y=-x$, $b=\pi/4$, and let $\nu_b$ and its signed-distance function $v_b$ be as in `../../06_small_alpha_second_term/general_direction/PROOF.md`. Thus $v_b$ is 1-Lipschitz, has the sign of $\nu_b$, and vanishes at both poles. On $H=\{w_1>0\}$ set

$$h_\alpha(w)=\frac12(2w_1)^\alpha,\qquad
u_\alpha(w)=c+P_\alpha(v_b(w)),$$

$$f_\alpha(w)=\max\{-h_\alpha(w),\min\{h_\alpha(w),u_\alpha(w)\}\}.$$

Extend $f_\alpha$ oddly by $f_\alpha(-w)=-f_\alpha(w)$, and set it to zero on $w_1=0$.

The maximum and minimum of real Hölder functions with seminorm at most one still have seminorm at most one: this is the usual lattice property for 1-Lipschitz functions in the metric $|z-w|^\alpha$. Both $h_\alpha$ and $-h_\alpha$ have seminorm at most $2^{\alpha-1}\le1$ in $H$. Hence the restriction to either half-plane has seminorm at most one. For points $w\in H$ and $z\notin H$,

$$|f_\alpha(w)-f_\alpha(z)|
\le 2^{\alpha-1}(w_1^\alpha+(-z_1)^\alpha)
\le(w_1-z_1)^\alpha\le|w-z|^\alpha.$$

The middle inequality is concavity. Thus $[f_\alpha]_\alpha\le1$ globally. Since $h_\alpha(x)=1/2$ and $|c|<1/2$,

$$f_\alpha(x)=c,\qquad f_\alpha(y)=-c.$$

At every fixed point away from the zero set and the separating line, $M_\alpha\to1$, $h_\alpha\to1/2$, and

$$f_\alpha(w)\longrightarrow\frac12\operatorname{sign}\nu_b(w).$$

The construction has at most $O(1+|w|^\alpha)$ growth, so its output increments are well defined.

## Local contribution

For fixed $A,B$, choose a sufficiently small radius $\rho>0$. The clamp is inactive throughout $B(x,\rho)$ for all sufficiently small positive $\alpha$. Here is a uniform justification. Since $|v_b(w)|\le|w-x|\le\rho$ and $w_1\ge1/2-\rho$, it is enough that

$$M_\alpha A\rho^\alpha+c\le\tfrac12(1-2\rho)^\alpha,$$
$$M_\alpha B\rho^\alpha-c\le\tfrac12(1-2\rho)^\alpha.$$

At $\alpha=0$ both are equalities. Their first-order inequalities hold strictly if

$$H(A)+\log\rho<\frac{\log(1-2\rho)}{2A},\qquad
H(A)+\log\rho<\frac{\log(1-2\rho)}{2B}.$$

Such a radius exists because the left side tends to $-\infty$ and the right sides tend to zero as $\rho\downarrow0$. Continuity of the derivatives then proves the asserted inequalities for small $\alpha$.

The constant $c$ contributes zero to the own-kernel integral by circular cancellation. Replace $v_b$ near the pole by signed distance $v_0$ to the two perpendicular zero lines of the own kernel. The local geometric estimate from the general-direction proof is $|v_b-v_0|\le C r^3$. Applying its weighted signed-power argument separately to the two branches gives the same error $O_A(\alpha\rho^{\alpha+2}+\rho^{\alpha+4})$. The positive and negative angular integrals for $v_0$ have equal magnitude by a quarter-turn. Therefore the sum of the two pole contributions is

$$\frac{2a_2(\alpha)\rho^\alpha}{\alpha}\frac{M_\alpha}{2^\alpha}
+O_A(\alpha\rho^{\alpha+2}+\rho^{\alpha+4}+\rho^2),$$

where the last term includes the smooth other-pole contributions, including their products with the nonzero constant $c$. All own-kernel integrals here use circular principal values; their constant terms cancel exactly. Also,

$$a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

The exact leading expression expands as

$$\frac2{\pi\alpha}
+\frac{2H(A)-\log2-1}{\pi}
+\frac2\pi\log\rho+O_{A,\rho}(\alpha).$$

Outside the pole disks, dominated convergence gives half the total variation of the increment density. Domination at infinity follows from its cubic decay and $|f_\alpha(w)|\le C(1+|w|^{1/2})$ for $\alpha\le1/2$. Taking $\alpha\downarrow0$, then $\rho\downarrow0$, and using $W(\pi/4)=1/2$, gives

$$T_bf_\alpha(x)-T_bf_\alpha(y)
=\frac2{\pi\alpha}+\frac12+\frac{2H(A)-\log2-1}{\pi}+o(1).$$

For clarity, the sequential error argument establishes the displayed limit of the renormalized expression for the fixed globally defined family $f_\alpha$; $\rho$ is only an auxiliary proof cutoff.

## Identity contribution and optimization

The rotated operator $T_b-I/2$ has norm $D_\alpha$, because it is the square of a first-order Riesz transform in a rotated direction. Its increment on this function is the preceding expression minus $c$. Hence

$$\liminf_{\alpha\downarrow0}\left(D_\alpha-\frac2{\pi\alpha}\right)
\ge\frac12+\frac{\log2-1}{\pi}
+\frac2\pi(H(A)-\log2)+A-\frac12.$$

The right side is maximized at

$$A=\frac{e^{\pi/2}}{1+e^{\pi/2}},\qquad
B=\frac1{1+e^{\pi/2}}.$$

Indeed, its derivative is $1+(2/\pi)\log(B/A)$ and its second derivative is negative. Substitution gives the extra term $(2/\pi)\log\cosh(\pi/4)$. This proves the stated lower bound. The approximation lemma from the setup transfers the bound to the original supremum over real $C_c^\infty$ inputs without changing its value.
