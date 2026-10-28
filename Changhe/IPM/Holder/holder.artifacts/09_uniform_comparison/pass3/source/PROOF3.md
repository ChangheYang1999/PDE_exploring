# Uniform comparison, third pass: Theorem 3.7 for $C_\alpha$ on $[\frac7{20},\frac9{10}]$

This supplements `../uniform/PROOF.md` (second pass), whose notation, groups, shapes, lower nodes, lower certificates and
interpolation (section 3) are used unchanged. Only the upper function for $C_\alpha$ in groups 2 to 6 changes.

## Statement

For groups $g=2,\dots,6$ (exponent intervals $[\frac7{20},\frac12],[\frac12,\frac35],[\frac35,\frac7{10}],[\frac7{10},\frac45],[\frac45,\frac9{10}]$) let

$$U^{(3.7)}_C(\alpha)=S_\alpha(\delta)+\sec\frac\pi{4m}\max_{0\le j\le m}\big(L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)\big)$$

be the right side of Theorem 3.7 with $\delta=\frac1{64}$, $m=16$, and the following fixed choices.

- Local circles $L_\alpha$: $N=512$ cells per circle, $256$ radial bins of $[\delta,\frac12]$, the cell masses $m_j$ and bounds $T_j$
  of the verifier's `angular_data`, and the integer flows of the verifier's `transport_greedy`. The greedy order uses only
  floating Euclidean distances between cell midpoints at the bin's mid radius, so these flows do not depend on $\alpha$ and
  are the same for all groups.
- Middle circles $W_\alpha$ (Theorem 3.6): $N=512$ cells per half, $512$ bins of $[0,\frac\pi2]$, the masses and bounds of the
  verifier's `cell_measures`, and for each (bin, phase node, group) the integer plan returned by the verifier's `best_plan`
  (17 trials) for the float costs at the group's reference exponent ($\frac{17}{40},\frac{11}{20},\frac{13}{20},\frac34,\frac{17}{20}$).
- Exterior $E_\alpha$ (Theorem 3.5): the second-pass exterior functions of the same group (`far2_g2` to `far2_g6`, reference
  exponents as above).

Claim. For every $\alpha$ in the interval of group $g\in\{2,\dots,6\}$, $C_\alpha\le\min\{U_C(\alpha),U^{(3.7)}_C(\alpha)\}$, where $U_C$ is
the second-pass upper function, and the resulting ratio to $I(\alpha,a_0)$ is bounded as stated in `RESULTS3.md`.

Result (`RESULTS3.md`). On $[\frac1{200},\frac{199}{200}]$, with the group shapes of the second pass,

$$I(\alpha,a_0)\le C_\alpha\le1.0625\,I(\alpha,a_0),\qquad I(\alpha,a_0)\le D_\alpha\le1.2894\,I(\alpha,a_0).$$

More precisely $\log\rho_C\le0.0606161506306427$ ($\rho_C\le1.0624909995$, segment $[\frac{27}{40},\frac7{10}]$, Theorem 3.7 family) and
$\log\rho_D\le0.2541485128253728$ ($\rho_D\le1.2893632771$, segment $[\frac{23}{40},\frac35]$). With the end intervals of
`../uniform/PROOF.md`, section 5 ($C$: $1.0263$; $D$: $1.0324$), the same two constants hold on all of $(0,1)$ with
$\ell_C$ as in the second-pass corollary. Per group (minimum of both families on each segment), the $C$ ratios are
$1.0259, 1.0502, 1.0519, 1.0599, 1.0625, 1.0622, 1.0554, 1.0470$ for groups $0$ to $7$.

The $D$ value differs from the second pass ($1.2898550590$) only through the split point; it agrees with the verifier's
independent recombination of the second-pass data ($1.2893632770$, rounded down there in the last place). The second-pass
$C$ value with the new split point is $1.0824118313$ (verifier: $1.0824118312$).

## Proof

**1(e). Log-convexity of $U^{(3.7)}_C$ for fixed plans.** We use the facts of `../uniform/PROOF.md`, section 1.

- $S_\alpha(\delta)=\frac4\pi\cdot\frac{2^{\alpha/2}\delta^\alpha}{\alpha(\alpha+2)}+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2}$. The first term has
  $(\log)''=\alpha^{-2}+(\alpha+2)^{-2}>0$; the second is log-linear. So $S_\alpha(\delta)$ is log-convex.
- Local bin cost. The masses $m_j$, the bounds $T_j$, the flow $\pi$, the chord bounds $c_k=2\sin(\pi\min\{k+1,N/2\}/N)$ and
  the opposite-circle bounds $e_{jk}$ do not depend on $\alpha$ (in the code `dist` is an upper decimal of
  $\max(|1+at|,|1+bt|)$, computed once per bin and phase). The same-circle term is
  $\pi_{jk}c_k^\alpha\frac{b^\alpha-a^\alpha}\alpha=\pi_{jk}\int_a^b(c_kr)^\alpha\frac{dr}r$, a moment. The opposite term
  $\pi_{jk}e_{jk}^\alpha\log\frac ba$ and the remainder $(1+2b)^\alpha\log\frac ba\sum_j(T_j-|m_j|)$ are log-linear with nonnegative
  coefficients. So $L_\alpha(\phi_j)$ is log-convex.
- Middle bin cost. $(b-a)\big(\sum\pi_{jk}c_{jk}+(2\sin b)^\alpha\sum_j(T_j-|m_j|)\big)$ with
  $c_{jk}=[2\sin b\,\sin(b(k+1)/N)]^\alpha$ or $[2\sin b\,\cos(a\max\{0,k-1\}/N)]^\alpha$ (code: `same`, `opposite`, with
  `rmax` the upper endpoint of an enclosure of $\sin[a,b]$, so $\ge\sin b$; $b(k+1)/N\le\frac\pi2$ because $b\le\frac\pi2$ and $k+1\le N$). All bases and coefficients are positive and
  independent of $\alpha$ inside a group, so $W_\alpha(\phi_j)$ is a nonnegative combination of log-linear functions, hence log-convex.
- $E_\alpha(\phi_j)$ is log-convex by `../uniform/PROOF.md`, section 1(c).

Sums, positive multiples and the finite maximum over $j$ preserve log-convexity. In all three parts, the value used for
$T_j-|m_j|$ is the upper endpoint of an interval enclosure that is computed once per (bin, phase) and does not depend on
$\alpha$; any upper bound is admissible in Theorems 3.5, 3.6 and 3.7.

**3'. Interpolation.** Section 3 of `../uniform/PROOF.md` applies verbatim to $U^{(3.7)}_C$, with the same upper and lower
nodes (the upper nodes of groups 2 to 6 are the multiples of $\frac1{40}$ in $[\frac7{20},\frac9{10}]$). The split point $c$ is
now a rational approximation of the crossing point of $L_1$ and $L_2$ (with $c=x_2$ if $L_1\ge L_2$ at $x_2$ and $c=x_1$ if
$L_1\le L_2$ at $x_1$); any $c\in[x_1,x_2]$ is valid. The maximum of the four values is formed with `arb.max` (the two values at $c$ can coincide to
double precision), and its upper endpoint is used.

**Minimum.** On each upper segment $[a,b]$ both $U_C$ and $U^{(3.7)}_C$ bound $C_\alpha$, and each is log-convex there with its
own fixed plans. Hence $\sup_{[a,b]}C_\alpha/I(\alpha,a_0)\le\min\{\rho^{(3.5)}_{[a,b]},\rho^{(3.7)}_{[a,b]}\}$, where each $\rho$ is the
segment bound of section 3 for that family. The uniform constant is the maximum over segments of this minimum.

**4'. Nodal certificates.** `local_nodes.py` is the verifier's `certify_local_circles_multi.py` with only the output
path and the list of hashed files changed; at $\alpha=\frac3{10}$ its rows $0$ to $128$ reproduce the verifier's
`multi_r0_128_3_10.json` exactly (all phase intervals and the small-disk value). `mid_nodes.py` is the verifier's
`certify_middle_chunks.py` with one `best_plan` per (bin, phase, group) at the group's reference exponent; with the single
group $\frac12:\frac12$ it reproduces the verifier's chunk `n512_320_384` exactly. `combine3.py` merges the chunks with exact
coverage checks (all $256$ local rows and $17$ phases, all $512$ middle rows) and common source hashes. Its nodal upper values (recorded as
`nodal_upper` in `uniform_result_thm37_pass3.json`) reproduce the single-exponent Theorem 3.7 certificates at $\frac12$, $\frac34$ and
$\frac9{10}$ to all printed digits (`RESULTS3.md`).
