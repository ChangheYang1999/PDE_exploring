# Uniform comparison of upper and lower bounds on $\frac1{200}\le\alpha\le\frac{199}{200}$

## Statement

Let $U_C(\alpha)$ and $U_D(\alpha)$ denote the right sides of Theorem 3.5 (exterior circles) for $C_\alpha$ and $D_\alpha$,
with $m=16$ phase intervals, and with the following fixed choices: the compact part $\widetilde M_\alpha$ is the exact
reflection-orbit integral of Theorem 3.4; the exterior part uses $n=512$ angular cells, $128$ radial intervals
$u_i=\frac14+\frac34\cdot\frac i{128}$ and the cell masses $m_j$, cell bounds $T_j$ described below; and the transport
matrices $\pi_{jk}$ depend on the radial interval, the phase node and the exponent group, but not on $\alpha$ inside a
group. Let $I(\alpha,a)$ be the polygonal witness of Theorem 4.5. Let the groups and shapes be

| group | exponent interval | shape $a_0$ | plan reference exponent |
|---|---|---|---|
| 0 | $[1/200,\,19/100]$ | $14/25$ | $1/20$ |
| 1 | $[19/100,\,7/20]$ | $53/100$ | $27/100$ |
| 2 | $[7/20,\,1/2]$ | $97/200$ | $17/40$ |
| 3 | $[1/2,\,3/5]$ | $89/200$ | $11/20$ |
| 4 | $[3/5,\,7/10]$ | $39/100$ | $13/20$ |
| 5 | $[7/10,\,4/5]$ | $33/100$ | $3/4$ |
| 6 | $[4/5,\,9/10]$ | $53/200$ | $17/20$ |
| 7 | $[9/10,\,199/200]$ | $1/5$ | $24/25$ |

Claim. For every $\alpha$ in a group interval, with that group's shape and plans,

$$I(\alpha,a_0)\le C_\alpha\le U_C(\alpha)\le\rho_C\,I(\alpha,a_0),\qquad C_\alpha\le D_\alpha\le U_D(\alpha)\le\rho_D\,I(\alpha,a_0),$$

with $\rho_C=1.0830$ and $\rho_D=1.2899$. More precisely `combine.py thm35` prints
$\log\rho_C\le0.0796872360278252$ (ratio $1.0829483075$, worst segment $[\frac{13}{20},\frac{27}{40}]$) and
$\log\rho_D\le0.2545298546442173$ (ratio $1.2898550590$, worst segment $[\frac{23}{40},\frac35]$); the per-group values are
in `RESULTS.md`. The same procedure with $U$ the right side of Theorem 3.4 (`combine.py thm34`) gives $1.1144$ and $1.3237$
and is recorded only as a cross-check.

Corollary (whole interval). For every $0<\alpha<1$ the certified bounds satisfy

$$\ell_C(\alpha)\le C_\alpha\le1.0830\,\ell_C(\alpha),\qquad \ell_C(\alpha)\le D_\alpha\le1.2899\,\ell_C(\alpha),$$

where $\ell_C=L_1$ (Theorem 4.1) on $(0,\frac1{200}]$, $\ell_C=I(\cdot,a_0)$ with the group shape on $[\frac1{200},\frac{199}{200}]$, and
$\ell_C=H$ (Theorem 4.4) on $[\frac{199}{200},1)$. The proof of the corollary is section 5.

## Proof

**1. Log-convexity of $U_C$ and $U_D$ in $\alpha$, for fixed plans.** A positive function is log-convex if its
logarithm is convex. Sums, products, positive multiples and finite maxima of log-convex functions are log-convex
(for sums: Hölder's inequality $x^\theta y^{1-\theta}+z^\theta w^{1-\theta}\le(x+z)^\theta(y+w)^{1-\theta}$). A function
$\int d(\omega)^\alpha\,d\mu(\omega)$ with $\mu\ge0$ and $d>0$ is log-convex by Hölder's inequality; in particular $c^\alpha$
($c>0$) is log-linear and constants are log-convex.

(a) Local terms. $\frac{2^{1-\alpha}a_2(\alpha)}\alpha=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}$ has
$(\log)''=\alpha^{-2}+(\alpha+2)^{-2}>0$. For $D$: $\log A_\alpha=\log\Gamma(\frac{\alpha+2}2)-\log\Gamma(\frac{\alpha+3}2)+\text{const}$
has second derivative $\frac14(\psi'(\frac{\alpha+2}2)-\psi'(\frac{\alpha+3}2))>0$ because the trigamma function decreases,
so $\frac{2^{1-\alpha}A_\alpha}\alpha+\frac12$ is a sum of log-convex functions.

(b) Compact part. For each phase node, $\widetilde M_\alpha(\phi_j)$ is the integral over the compact region of the
four-point reflection-orbit cost. At each point the cost equals $a\,h^\alpha+b\,(\delta^\alpha-h^\alpha)$ if $a\ge b$ and
$a\,(\delta^\alpha-v^\alpha)+b\,v^\alpha$ otherwise ($a,b\ge0$ the two pair masses, $h,v,\delta$ the horizontal, vertical and
diagonal distances). Indeed the difference of the two expressions is $(a-b)(h^\alpha+v^\alpha-\delta^\alpha)$ and
$h^\alpha+v^\alpha\ge(h+v)^\alpha\ge\delta^\alpha$, so the code's maximum of the two expressions is the cost of the plan
selected by the mass comparison, which does not depend on $\alpha$. Both expressions are nonnegative combinations of
$h^\alpha,v^\alpha,\delta^\alpha$ with $\alpha$-independent coefficients ($a h^\alpha+b(\delta^\alpha-h^\alpha)=(a-b)h^\alpha+b\delta^\alpha$ with $a-b\ge0$).
Hence $\widetilde M_\alpha(\phi_j)$ is a moment integral, log-convex. This is the argument of the verifier's
`09_uniform_comparison/PROOF.md`.

(c) Exterior part. For a fixed matrix $\pi_{jk}$ (Theorem 3.5 allows any matrix with the stated marginals),
$B_\alpha=\sum\pi_{jk}c_{jk}^{\,\alpha}+2^\alpha\sum(T_j-|m_j|)$ with $c_{jk}>0$, $\pi_{jk}\ge0$, $T_j-|m_j|\ge0$ independent of
$\alpha$: log-convex. The radial weight $\frac{u_i^{1-\alpha}-u_{i-1}^{1-\alpha}}{1-\alpha}=\int_{u_{i-1}}^{u_i}(1/u)^\alpha du$ is a moment.
The tail: $a_3(\alpha)=\frac3\pi\int_0^{\pi/6}\sin3t\,(2\sin t)^\alpha dt$ with $\sin3t\ge0$, $\frac{u_0^{1-\alpha}}{1-\alpha}=\int_0^{u_0}(1/u)^\alpha du$, and
$a_{2k+3}(\alpha)\frac{u_0^{2k+1-\alpha}}{2k+1-\alpha}=\frac1\pi\kappa_k^{\,\alpha}\int_0^{u_0}u^{2k}(1/u)^\alpha du$ with a fixed $\kappa_k>0$. The convergent
series of log-convex terms is log-convex.

(d) $U_C=\text{local}+\sec\frac\pi{4m}\max_j(\widetilde M_\alpha(\phi_j)+E_\alpha(\phi_j))$ is therefore log-convex on $(0,1)$ for fixed
plans, and so is $U_D$.

In the computation the plan for (radial interval, phase node) is the exact integer plan returned by the verifier's
`best_plan` (adjacent sign runs or antipodal; marginals checked exactly by `check_plan`) for the float costs at the
group's reference exponent, and that same plan is evaluated at every exponent of the group. The cell masses $m_j$ and
the bounds $T_j$ come from the verifier's `cell_measures`, copied verbatim (they do not depend on $\alpha$). The value
used for $T_j-|m_j|$ is the upper endpoint of an interval enclosure; any upper bound is admissible in Theorem 3.5.

**2. Log-convexity of the lower witness.** For fixed $a$, $I(\alpha,a)/\alpha=\frac12\int_0^\infty(2t)^\alpha J_a(t)\,\frac{dt}t$ with
$J_a>0$ (Theorem 4.5), a moment integral, so $g(\alpha)=\log(I(\alpha,a)/\alpha)$ is convex.

**3. Interpolation.** Let $a<b$ be consecutive upper nodes with certified $U(a)\le A$, $U(b)\le B$ (same plans).
Convexity of $\log U$ gives $\log U(t)\le E(t)=\frac{(b-t)\log A+(t-a)\log B}{b-a}$ on $[a,b]$. Let $x_0<x_1<x_2<x_3$ be
consecutive lower nodes of one group with $[x_1,x_2]\subset[a,b]$ and certified $0<\ell(x)\le I(x,a_0)/x\le u(x)$. Convexity of $g$
gives $g(t)\ge L_1(t)=\log\ell(x_1)+\frac{t-x_1}{x_1-x_0}(\log\ell(x_1)-\log u(x_0))$ for $t\ge x_1$ and
$g(t)\ge L_2(t)=\log\ell(x_2)+\frac{x_2-t}{x_3-x_2}(\log\ell(x_2)-\log u(x_3))$ for $t\le x_2$ (the secant slopes of a convex
function increase; lowering $g(x_1)$ and raising $g(x_0)$ lowers the line on $t\ge x_1$). For a rational $c\in[x_1,x_2]$,
$\varphi_i(t)=E(t)-\log t-L_i(t)$ is convex, so

$$\max_{[x_1,x_2]}\log\frac{U(t)}{I(t,a_0)}\le\max\{\varphi_1(x_1),\varphi_1(c),\varphi_2(c),\varphi_2(x_2)\}.$$

The four values are evaluated in 200-bit ball arithmetic with exact rational $t$, and the largest upper endpoint is
taken. $c$ is a rational approximation of the crossing point of $L_1$ and $L_2$ (any choice is valid).

**4. Nodal certificates.** Upper nodes: `refl_nodes.py` (the verifier's `certify_reflection_orbits.py`, version 2, with
an exponent list and inline $a_2,a_3$; core loop byte-identical; it reproduces the verifier's 128-cell certificate at
all ten exponents of Table 1 to $10^{-9}$ and the 384-cell values at $\frac1{10},\frac3{10},\frac12,\frac34,\frac9{10}$
exactly) on $384^2$ rectangles, and `far_nodes.py` (the verifier's `certify_far_circles.py` with one plan per
(radial interval, phase) and group; with reference exponent $\frac12$ it reproduces the verifier's coarse exterior
certificate exactly). Lower nodes: the verifier's `certify_structured_full.py`, unchanged, with the group's shape and
all lower nodes of the group in one run ($4000$, $15000$ or $8000$ logarithmic cells per unit), using the saved safe
decimal lower and upper endpoints. Node lists: `nodes2.py` (59 upper nodes, 235 lower nodes).

**5. The end intervals.** For $C$ this is Theorem 9.1 of the report: $C_\alpha\le F(\alpha)\le1.0172482934\,L_1(\alpha)$ on
$(0,0.005]$ and $C_\alpha\le F(\alpha)\le1.0262309397\,H(\alpha)$ on $[0.995,1)$. For $D$ use $D_\alpha\le C_\alpha+\frac12$ and
$D_\alpha\ge C_\alpha$.

(i) $0<\alpha\le0.005$. $L_1(\alpha)=q^\alpha\big(\frac4{\pi\alpha(\alpha+2)}-\frac14\big)$ with $q=\sqrt2-1<1$ is a product of two positive
decreasing functions, so $L_1(\alpha)\ge L_1(0.005)\ge126.199$ (Arb: $126.19906852\ldots$). Hence
$D_\alpha/L_1(\alpha)\le1.0172482934+\frac{0.5}{126.199}\le1.0213$.

(ii) $0.995\le\alpha<1$, $\delta=1-\alpha\le0.005$. The proof of Theorem 9.1 gives
$\delta H(\alpha)\ge\frac{(\alpha+1)(\alpha+2)\sqrt3}{8\pi}\ge\frac{1.995\cdot2.995\sqrt3}{8\pi}\ge0.411775$, so
$H(\alpha)\ge0.411775/0.005=82.355$ and $D_\alpha/H(\alpha)\le1.0262309397+\frac{0.5}{82.355}\le1.0324$.

Both end constants are below $\rho_C=1.0830\le\rho_D$, so the middle interval determines the constants on $(0,1)$.
The groups meet at $\frac1{200}$ and $\frac{199}{200}$, where both statements apply. $\square$

