# A sharper closed-form upper bound for $C_\alpha$ on the whole interval

## Statement

Use the operator constant $C_\alpha$ of the report (homogeneous Hölder space modulo constants, Euclidean seminorm, centred
circular principal values). Put $\kappa=\frac{209}{500}=0.418$, $c^{**}=\frac{1353}{2500}=0.5412$, $a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}$ and

$$F^{**}(\alpha)=\frac{2^{1-\alpha}a_2(\alpha)}{\alpha}+\frac{\kappa}{1-\alpha}+c^{**}
=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{0.418}{1-\alpha}+0.5412 .$$

Then $C_\alpha\le F^{**}(\alpha)$ for every $0<\alpha<1$.

This is $F^*-0.0348$, with $F^*$ the closed form of Theorem 9.3 of the report. As $\alpha\to0$,
$F^{**}(\alpha)-\frac2{\pi\alpha}\to0.9592-\frac{1+\log2}\pi=0.4202545\ldots$ (Theorem 9.3: $0.4550545\ldots$; sharp value
$C_0=0.4023257\ldots$). As $\alpha\to1$, $(1-\alpha)F^{**}\to0.418$, as before (sharp value $\frac{3\sqrt3}{4\pi}=0.4134967\ldots$).
For $D_\alpha$ the bound $G^*$ of Theorem 9.3 is kept: $F^{**}+\frac12>G^*$ for every $\alpha$, because $A_\alpha<a_2(\alpha)$.

## Proof

The proof follows the proof of Theorem 9.3 (`../lead_closed_form/PROOF.md` in the accompanying artifacts), with the
remainder of Theorem 3.5 replaced by the remainder of Theorem 3.7 on the whole interval $[0,\frac{199}{200}]$.

**Step 1 (decomposition).** Theorem 3.7 of the report, with $\delta=\frac1{64}$ and $m=16$, states
$C_\alpha\le S_\alpha(\delta)+R_{37}(\alpha)$, where

$$S_\alpha(\delta)=\frac{2a_2(\alpha)\delta^\alpha}\alpha+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2},\qquad
R_{37}(\alpha)=\sec\frac\pi{64}\max_{0\le j\le16}\big(L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)\big)$$

(paired local circles, middle circles of Theorem 3.6, exterior circles of Theorem 3.5). Write $L_C=2^{1-\alpha}a_2/\alpha$ and
$g=S_\alpha(\delta)-L_C$. Since $\int_\delta^{1/2}u^{\alpha-1}du=\frac{2^{-\alpha}-\delta^\alpha}\alpha$,

$$g(\alpha)=-2a_2(\alpha)\int_\delta^{1/2}u^{\alpha-1}\,du+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2},$$

which extends continuously to $\alpha=0$. So $C_\alpha\le L_C(\alpha)+g(\alpha)+R_{37}(\alpha)$, and it suffices to prove

$$g(\alpha)+R_{37}(\alpha)\le\frac\kappa{1-\alpha}+c^{**}\qquad(0<\alpha\le\tfrac{199}{200}).\tag{1}$$

**Step 2 (fixed plans and log-convexity).** The groups $0,\dots,7$ and their nodes are those of the uniform comparison
(Theorem 9.2; `data/nodes2.json`). In each group all plans are fixed: the local flows are the greedy flows (the greedy
order uses only floating Euclidean distances between cell midpoints at the mid radius of each bin, so the flows do not
depend on $\alpha$); the middle plans are chosen at the group's reference exponent ($\frac1{20}$ for group $0$, $\frac{27}{100}$ for group $1$,
$\frac{17}{40},\frac{11}{20},\frac{13}{20},\frac34,\frac{17}{20}$ for groups $2$ to $6$, $\frac{24}{25}$ for group $7$); the exterior plans are those of
the second pass of the uniform comparison (`far2_g*`, same references). With the plans fixed, $R_{37}=R_{37,g}$ is one explicit
function of $\alpha$ on the interval of group $g$, and $\log R_{37,g}$ is convex there. This is proved in section 1(e) of the
third pass of the uniform comparison (`09_uniform_comparison/pass3/source/PROOF3.md`): each local, middle and exterior bin
cost is a nonnegative combination of functions $c^\alpha$, of moments $\int r^\alpha d\mu(r)$ and of log-linear functions, with
bases and coefficients independent of $\alpha$; sums, positive multiples and finite maxima preserve log-convexity.

**Step 3 (nodes).** For groups $2$ to $6$ the nodal values $R_i\ge R_{37}(\alpha_i)$ are the certified upper values of
$S_{\alpha_i}(\delta)+R_{37}(\alpha_i)$ of the third pass (`data/uniform_result_thm37_pass3.json`) minus the exact lower endpoint
of $S_{\alpha_i}(\delta)$. For groups $0$, $1$ and $7$, new certificates of $R_{37}$ were computed at all nodes, with the
same grids as the third pass (local circles: $512$ cells per circle, $256$ radial bins of $[\delta,\frac12]$; middle circles:
$512$ cells per half, $512$ bins of $[0,\frac\pi2]$; exterior circles: $512$ cells, $128$ bins). The chunks are in `local/`,
`mid/` (groups $0$, $1$) and `local7/`, `mid7/` (group $7$); `code/nodes37.py` merges them, checks that every radial row and
phase is covered exactly once and that the script hashes match, and writes the upper values, rounded up to $10$
decimals, to `data/remainders37.json`. Every node of every group is of this kind.

**Step 4 (the node $\alpha=0$).** Every term of $R_{37,0}$ has a finite limit as $\alpha\to0^+$, and the limit is given by the
same formulas at $\alpha=0$: powers of positive numbers become $1$, and the local radial factor $\frac{b^\alpha-a^\alpha}\alpha$ becomes
$\log\frac ba$. The middle part is a finite sum of continuous functions. The exterior part is continuous at $0$ by Step 4
of the proof of Theorem 9.3, and its value at $0$ is the one computed there (`data/far_a0.json`, plans of group $0$; the
row $\alpha=\frac1{200}$ of that file coincides with the stored node certificate, which `code/nodes37.py` checks). The local and
middle scripts accept the exponent $0$ (`code/local_nodes.py`, `code/mid_nodes.py`; the only changes against the third
pass are this case and a docstring line). Hence $R_{37,0}$ is continuous on $[0,\frac1{200}]$ and log-convex on $(0,\frac1{200}]$, so
the chord bound below also holds on $[0,\frac1{200}]$. The value at $0$ is $R_{37,0}(0)\le3.16526$.

**Step 5 (chords against the closed form on $[0,\frac{199}{200}]$).** On each of the $59$ segments $[a,b]$ of consecutive nodes
of one group, $\log R_{37}\le E$, the chord through $(a,\log R_a)$ and $(b,\log R_b)$. Each segment is split into $4000$
equal rational pieces $[p,q]$. On a piece, $e^E\le\max(e^{E(p)},e^{E(q)})$ and $\frac\kappa{1-t}+c^{**}\ge\frac\kappa{1-p}+c^{**}$.
For $g$:

- if $q\le\frac78$, then $g(t)\le g(q)$ for $t\le q$. Indeed $(\log a_2)'=\frac{\log2}2-\frac1{\alpha+2}<0$ for $\alpha<\frac2{\log2}-2=0.885\ldots$,
  so $a_2$ is positive and decreasing on $[0,\frac78]$; $\int_\delta^{1/2}u^{\alpha-1}du$ is positive and decreasing because $u<1$;
  their product is decreasing, and $(1+2\delta)^\alpha$ is increasing. So $g$ is increasing on $[0,\frac78]$.
- if $q>\frac78$, $g$ is enclosed by ball evaluation with the interval argument $[p,q]$.

Every piece is verified in $256$-bit ball arithmetic at exact rational points (`code/check_closed_form37.py`, part 1). The
smallest margins per group (lower endpoints) are
$1.63\cdot10^{-4}$ (group $0$, at $\alpha=0$), $0.0183$, $0.0297$, $0.0362$, $0.0389$, $0.0411$, $0.0324$, $0.0278$ (groups $1$ to $7$).
This proves (1) on $(0,\frac{199}{200}]$.

**Step 6 ($\frac{199}{200}\le\alpha<1$).** Exactly as in Step 6 of the proof of Theorem 9.3, with $c^{**}$ in place of $c$: Theorem 3.1
gives $C_\alpha\le F_b(\alpha)$, and with $\delta'=1-\alpha$ and $s=\frac{2a_3+\delta'b}{2a_2}$, $b=\frac{2^{\alpha+1}}{3\pi}$, part 2 of
`code/check_closed_form37.py` proves $\frac{2a_2s^\alpha}\alpha<\delta'L_C+\kappa+c^{**}\delta'$ on $200$ closed subintervals of $[\frac{199}{200},1]$ with
interval exponent arguments. The smallest margin is $0.00297$. Dividing by $\delta'$ gives $F_b<F^{**}$. $\square$

## Comparison

At the exponents of Table 1 (floating evaluation, rounded up in the sixth place):

| $\alpha$ | 0.001 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 0.9 | 0.99 |
|---|---|---|---|---|---|---|---|---|---|---|
| $F^{**}$ | 637.040753 | 64.089516 | 13.189650 | 6.862161 | 3.763643 | 2.801398 | 2.233731 | 2.689226 | 5.078314 | 42.646407 |
| $F^*$ | 637.075553 | 64.124316 | 13.224450 | 6.896961 | 3.798443 | 2.836198 | 2.268531 | 2.724026 | 5.113114 | 42.681207 |

Direct certificates at a single exponent are smaller. The loss comes from the chord interpolation, from the single
constant $c^{**}$, which is forced by the node $\alpha=0$ ($\kappa+c^{**}\ge g(0)+R_{37,0}(0)=0.9590\ldots$), and near $\alpha=1$ from
$\kappa>\frac{3\sqrt3}{4\pi}$. A smaller $\kappa$ with a larger $c$ fails near $\alpha\in[0.9,0.99]$.

## Reproduction

```
bash code/run37.sh                                       # groups 0 and 1 and the exponent 0 (about 16 minutes)
bash code/run37_g7.sh                                    # group 7 (about 12 minutes)
python3 code/nodes37.py                                  # writes data/remainders37.json
python3 code/check_closed_form37.py 209/500 1353/2500 4000 200   # a few minutes; writes results/closed_form37_check_*.json
```

Inputs copied unchanged from
the uniform comparison and the proof of Theorem 9.3: `data/nodes2.json`, `data/far2_g0.json`, `data/far2_g1.json`,
`data/far2_g7.json` (exterior node certificates of the second pass), `data/far_a0.json` (exterior part at $\alpha=0$),
`data/uniform_result_thm37_pass3.json`, `data/uniform_result_thm35_pass3.json` (third pass nodal results; the second is used
only for a comparison column). The scripts `certify_far_circles.py`, `certify_local_circles_greedy.py`,
`local_circle_greedy.py`, `middle_circle_plan.py` and `circle_transport_plan.py` are identical to the copies in the third
pass sources; `check_explicit_bounds.py` is identical to the copy in the proof of Theorem 9.3.
