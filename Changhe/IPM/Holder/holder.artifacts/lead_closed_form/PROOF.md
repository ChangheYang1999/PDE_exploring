# Closed-form upper bounds for every exponent

## Statement

Use the operator constants $C_\alpha$, $D_\alpha$ of the report (homogeneous Hölder space modulo constants, Euclidean
seminorm, centred circular principal values). Put $\kappa=\frac{209}{500}=0.418$, $c=\frac{72}{125}=0.576$,

$$a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)},\qquad A_\alpha=\frac{\Gamma(\frac{\alpha+2}2)}{2\sqrt\pi\,\Gamma(\frac{\alpha+3}2)},$$

$$F^*(\alpha)=\frac{2^{1-\alpha}a_2(\alpha)}{\alpha}+\frac{\kappa}{1-\alpha}+c
=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{0.418}{1-\alpha}+0.576,$$

$$G^*(\alpha)=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac12+\frac{\kappa}{1-\alpha}+c=\frac{2^{1-\alpha}A_\alpha}{\alpha}+\frac{0.418}{1-\alpha}+1.076.$$

Then for every $0<\alpha<1$

$$C_\alpha\le F^*(\alpha),\qquad D_\alpha\le G^*(\alpha).$$

As $\alpha\to0$: $F^*(\alpha)-\frac2{\pi\alpha}\to0.994-\frac{1+\log2}\pi=0.4550545\ldots$ (sharp value $C_0=0.4023257\ldots$) and
$G^*(\alpha)-\frac2{\pi\alpha}\to1.494-\frac2\pi=0.8573802\ldots$ (sharp value $2C_0=0.8046514\ldots$). As $\alpha\to1$:
$(1-\alpha)F^*,(1-\alpha)G^*\to0.418$ (sharp value $\frac{3\sqrt3}{4\pi}=0.4134967\ldots$).

## Proof

**Step 1 (decomposition).** Theorem 3.5 of the report, with the compact part of Theorem 3.4 and $m=16$, states

$$C_\alpha\le L_C(\alpha)+R(\alpha),\qquad D_\alpha\le L_D(\alpha)+R(\alpha),\qquad
R(\alpha)=\sec\frac\pi{64}\max_{0\le j\le16}\big(\widetilde M_\alpha(\phi_j)+E_\alpha(\phi_j)\big),$$

with $L_C=2^{1-\alpha}a_2/\alpha$ and $L_D=2^{1-\alpha}A_\alpha/\alpha+\frac12$. The cell masses $m_j$, the variation bounds
$T_j$ and the integer transport plans $\pi_{jk}$ of $E_\alpha$ do not depend on $\alpha$. In the uniform comparison
(Theorem 9.2) they are fixed once per group, so for each group $g$ the function $R=R_g$ is one explicit function of
$\alpha$, and the two inequalities hold at every $\alpha\in(0,1)$.

**Step 2 (log-convexity).** By Theorem 9.2 (i), $\log R_g$ is convex on $(0,1)$. Concretely: where $a\ge b$ the orbit
cost of Theorem 3.4 is $2((a-b)h+bd)$, and where $b\ge a$ it is $2((b-a)v+ad)$, a nonnegative combination of powers
$c^\alpha$ with the case decided independently of $\alpha$. The circle bounds $B_i$ are nonnegative combinations of $c^\alpha$.
The radial weights $\frac{u_i^{1-\alpha}-u_{i-1}^{1-\alpha}}{1-\alpha}=\int_{u_{i-1}}^{u_i}u^{-\alpha}du$ and the tail factors are moments.
Sums, products and maxima of log-convex functions are log-convex.

**Step 3 (nodes).** At the $59$ upper nodes of Theorem 9.2, the certified upper values of $L_C+R_g$ minus the exact lower
endpoint of $L_C$ give upper values $R_i\ge R_g(\alpha_i)$ (`code/make_remainders.py`). The same subtraction for $D$
agrees to $10^{-8}$; the larger value is kept, rounded up to six decimals. At a node shared by two groups the larger
of the two values is kept. These values are listed in `data/remainders.json`.

**Step 4 (the node $\alpha=0$).** Every term of $R_0$ (group $0$, plans chosen at $\alpha=\frac1{20}$) has a finite limit as
$\alpha\to0^+$. The integrands of $\widetilde M_\alpha$ are bounded on a fixed compact set and converge pointwise off a null
set. $E_\alpha$ is a finite sum plus a series dominated uniformly for $\alpha\in[0,\frac12]$. Hence $R_0$ extends continuously
to $\alpha=0$. The limit is given by the same formulas evaluated at $\alpha=0$, where the powers of positive numbers equal $1$.
Evaluated with the same code and grids, it gives $\lim_{\alpha\to0^+}R_0(\alpha)\le0.993975$ (`code/run_alpha0.sh`). The same run
recomputes the node $\alpha=\frac1{200}$ and reproduces the stored certificate exactly, both the compact part and the
exterior part. Convexity on $(0,\frac1{200}]$ and continuity at $0$ give the chord bound also on $[0,\frac1{200}]$.

**Step 5 (chords against the closed form on $[0,\frac{199}{200}]$).** On each of the $59$ segments $[a,b]$ of consecutive
nodes of one group, $\log R_g\le E$, the chord through $(a,\log R_a)$ and $(b,\log R_b)$. The segment is split into
$4000$ equal rational pieces $[p,q]$. Since $e^E$ is monotone, $e^E\le\max(e^{E(p)},e^{E(q)})$ on $[p,q]$, and
$\frac\kappa{1-t}+c\ge\frac\kappa{1-p}+c$. Every piece is verified in 256-bit ball arithmetic at exact rational points
(`code/check_closed_form.py`, part 1). The smallest margin is $2.46\cdot10^{-5}$, at $\alpha=0$. Hence
$R(\alpha)\le\frac\kappa{1-\alpha}+c$, and so $C_\alpha\le F^*$ and $D_\alpha\le G^*$, for $0<\alpha\le\frac{199}{200}$.

**Step 6 ($\frac{199}{200}\le\alpha<1$).** Theorem 3.1 gives $C_\alpha\le F_b(\alpha)$, where $F_b$ is $F$ with $b_\alpha$ replaced by
$\frac{2^{\alpha+1}}{3\pi}$ (Theorem 9.1). Also $D_\alpha\le C_\alpha+\frac12$ because $R_1^2=T_{xx}-\frac12I$. With $\delta=1-\alpha$ and
$s=\frac{2a_3+\delta b}{2a_2}$, we have $\delta F_b=2a_2s^\alpha/\alpha$, which is continuous on $[\frac{199}{200},1]$. Part 2 of
`code/check_closed_form.py` proves

$$\frac{2a_2s^\alpha}\alpha<\delta L+\kappa+c\,\delta\qquad(L=2^{1-\alpha}a_2/\alpha\ \text{and}\ L=2^{1-\alpha}A_\alpha/\alpha)$$

on $200$ closed subintervals of $[\frac{199}{200},1]$, with interval exponent arguments. The coefficient $a_3$ is computed by
the positive series with proved tail of the original upper certificate. The smallest margins are $0.00315$ and $0.00290$.
Dividing by $\delta$ gives $F_b<F^*$ and $F_b+\frac12<G^*$ there. $\square$

## Comparison

$F^*<F$ for $\alpha\lesssim0.975$ and $G^*<G$ for $\alpha\lesssim0.975$ (floating evaluation; both $F$ and $F^*$ are valid
everywhere, so $\min(F,F^*)$ and $\min(G,G^*)$ are valid upper bounds). At the exponents of Table 1:

| $\alpha$ | 0.001 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|---|---|---|
| $F^*$ | 637.075553 | 64.124316 | 13.224450 | 6.896961 | 3.798443 | 2.836198 | 2.268531 | 2.724026 | 5.113114 | 42.681207 |
| $G^*$ | 637.477946 | 64.527310 | 13.630069 | 7.305753 | 4.213236 | 3.256565 | 2.698894 | 3.165019 | 5.559634 | 43.130775 |

(upper endpoints rounded up). The loss against the certified nodal values comes from the interpolation, from the
single constant $c$, and near $\alpha=1$ from $\kappa>\frac{3\sqrt3}{4\pi}$.

## Reproduction

```
bash code/run_alpha0.sh                                  # about one minute; writes data/refl_a0.json, data/far_a0.json, data/remainder_a0.json
python3 code/make_remainders.py                          # writes data/remainders.json
python3 code/check_closed_form.py 0.418 0.576 4000 200   # about ten seconds; writes results/closed_form_check.json
```

Inputs: `data/uniform_result_thm35_pass3.json` and `data/uniform_result_thm37_pass3.json` are the nodal results of the
uniform comparison (identical to the copies in `09_uniform_comparison/pass3/data`). `data/upper_n384.json` and
`data/far2_g0.json` are the node certificates of group 0 used for the cross-check at $\alpha=\frac1{200}$. The scripts
`code/refl_nodes_a0.py` and `code/far_nodes_a0.py` differ from the node scripts of the uniform comparison only in
accepting $\alpha=0$ (and, at $\alpha=0$, recording only the compact part) and in a relative import path.
