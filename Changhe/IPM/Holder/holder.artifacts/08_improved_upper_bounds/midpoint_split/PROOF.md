# A midpoint split with a convergent harmonic tail

## Explicit theorem

Use the real homogeneous Hölder seminorm and operators in `../../01_setup/PROOF.md`, with $0<\alpha<1$. Write $x=1/2$, $y=-1/2$ in complex coordinates, let $B_r(z)$ denote the open Euclidean disk, and put

$$G(w)=\frac{w}{\pi(w^2-1/4)^2},\qquad
E=B_1(0)\setminus(B_{1/2}(x)\cup B_{1/2}(y)).$$

For $0\le\phi\le\pi/2$, define the finite positive integral

$$M_\alpha(\phi)=\frac12\int_E|\operatorname{Re}(e^{i\phi}G(w))|(2|w|)^\alpha\,dA(w)
+\int_{B_{1/2}(x)}\left|\operatorname{Re}\frac{e^{i\phi}}{2\pi(w+1/2)^2}\right|(2|w|)^\alpha\,dA(w).$$

Let $a_n(\alpha)$ be the exact angular constants proved in `../../02_upper_bounds/PROOF.md`, and set

$$H_\alpha=\frac{2a_3(\alpha)}{1-\alpha}
+\frac2\pi\sum_{n=1}^\infty\frac{(n+1)4^{-n}}{2n+1-\alpha}
\left[\frac{2(2n+3)\cos(\pi/(4n+6))}{(2n+3)^2-1}\right]^\alpha.$$

For any integer $m\ge1$, define

$$U_m(\alpha)=\frac{2a_2(\alpha)2^{-\alpha}}\alpha+H_\alpha
+\sec\left(\frac\pi{4m}\right)\max_{0\le j\le m}M_\alpha\left(\frac{j\pi}{2m}\right).$$

Then

$$\boxed{C_\alpha\le \min\{F(\alpha),U_m(\alpha)\}.}$$

With $A_\alpha$ and $G_{\rm proj}$ from `../local_projection/PROOF.md`, also

$$\boxed{D_\alpha\le\min\left\{G_{\rm proj}(\alpha),
\frac{2A_\alpha2^{-\alpha}}\alpha+\frac12+H_\alpha
+\sec\left(\frac\pi{4m}\right)\max_{0\le j\le m}M_\alpha\left(\frac{j\pi}{2m}\right)\right\}.}$$

These are explicit, rigorously computable upper bounds. The positive integrals have no singularities in their domains. They do not assert optimality of the chosen split or phase grid. The same scalar bounds hold for complex inputs by phase projection.

## Decomposition and the regular part

For the phase kernel $K_\phi(w)=\operatorname{Re}(e^{i\phi}/(2\pi w^2))$, subtract the two local convolutions of radius $1/2$ at $x,y$ from the increment density. The remaining density $m_\phi$ equals

$$m_\phi(w)=\begin{cases}
-K_\phi(w-y),&w\in B_{1/2}(x),\\
 K_\phi(w-x),&w\in B_{1/2}(y),\\
\operatorname{Re}(e^{i\phi}G(w)),&\text{elsewhere}.
\end{cases}$$

It is odd under $w\mapsto-w$. On $B_1(0)$, pair $w$ and $-w$. The Hölder constraint gives

$$\left|\int_{B_1}m_\phi(w)f(w)\,dA(w)\right|
\le\frac{[f]_\alpha}2\int_{B_1}|m_\phi(w)|(2|w|)^\alpha\,dA(w)
=[f]_\alpha M_\alpha(\phi).$$

The exact angular bound controls each local convolution by $a_2(\alpha)2^{-\alpha}[f]_\alpha/\alpha$. This gives the first local term of $U_m$.

For $R_1^2$, use instead the local projection identity from the other proof. The two paired local terms cost $2A_\alpha2^{-\alpha}[f]_\alpha/\alpha$. The negative convolution remainder, including the uncancelled identity part, has mass $1/2$, hence increment cost at most $[f]_\alpha/2$. The regular density above is unchanged.

## The harmonic tail

For $|w|=r\ge1$, the absolutely convergent expansion is

$$G(re^{i\theta})=\frac1\pi\sum_{n=0}^\infty(n+1)4^{-n}r^{-2n-3}e^{-i(2n+3)\theta}.$$

The exact angular lemma bounds the contribution of its $n$th term outside the unit disk by

$$\frac{2(n+1)4^{-n}a_{2n+3}(\alpha)}{2n+1-\alpha}[f]_\alpha.$$

Termwise integration is justified by the convergent positive majorant; constants in $f$ have zero angular integral. Keep the exact $n=0$ term. For $k>1$, the measure $k\sin(kt)dt$ on $[0,\pi/(2k)]$ has total mass one. Concavity of $s^\alpha$ gives

$$a_k(\alpha)\le\frac1\pi\left(k\int_0^{\pi/(2k)}\sin(kt)\,2\sin t\,dt\right)^\alpha
=\frac1\pi\left(\frac{2k\cos(\pi/(2k))}{k^2-1}\right)^\alpha.$$

This proves the stated $H_\alpha$. If its sum is truncated before $n=N\ge1$, the omitted positive sum is at most

$$\frac{1+1/N}{\pi}\frac{4^{-N}}{1-1/4}.$$

Indeed, the bracket is at most one for $k=2n+3\ge5$, and $2(n+1)/(2n+1-\alpha)\le1+1/N$ for $n\ge N$. This tail bound is uniform over $0<\alpha<1$.

## A finite phase grid suffices

The function $M_\alpha$ is the restriction to the unit circle of a seminorm on the two real coefficients of $K_\phi$. Conjugation of the domains and kernels makes it even in $\phi$, and changing sign gives period $\pi$. Therefore it suffices to consider $[0,\pi/2]$.

Between neighboring grid angles $\phi_j,\phi_{j+1}$ of spacing $\delta=\pi/(2m)$, the unit vector at $\phi$ is

$$v_\phi=\frac{\sin(\phi_{j+1}-\phi)}{\sin\delta}v_{\phi_j}
+\frac{\sin(\phi-\phi_j)}{\sin\delta}v_{\phi_{j+1}}.$$

Both coefficients are nonnegative, and their sum is at most $\sec(\delta/2)$. The seminorm triangle inequality gives the phase-grid bound in the theorem. This bounds every phase, not only the sampled phases.

## Compact parameter domains for interval verification

The first integral in $M_\alpha$ can be restricted to the first quadrant using the conjugation and central symmetries. Put $r=\sin v$, $\theta=\pi/2-v+v\tau$, with $0\le v\le\pi/2$, $0\le\tau\le1$, and $w=re^{i\theta}$. It becomes

$$2\int_0^{\pi/2}\int_0^1\max\{|\operatorname{Re}G(w)|\cos\phi,|\operatorname{Im}G(w)|\sin\phi\}
(2r)^\alpha r\cos v\,v\,d\tau\,dv.$$

For the second integral put $w=1/2+se^{i\theta}$, $0\le s\le1/2$, $0\le\theta\le\pi$, and $Q(w)=1/[2\pi(w+1/2)^2]$. It becomes

$$2\int_0^{1/2}\int_0^\pi\max\{|\operatorname{Re}Q(w)|\cos\phi,|\operatorname{Im}Q(w)|\sin\phi\}
(2|w|)^\alpha s\,d\theta\,ds.$$

The factor-two identities use $|a+b|+|a-b|=2\max(|a|,|b|)$. Both changes of variables cover exactly the stated domains up to boundaries of area zero. All kernel denominators remain separated from zero. Positive real powers at a zero endpoint are evaluated using their known nonnegative range. Rectangle interval quadrature therefore gives rigorous enclosures without a geometric-cell approximation.
