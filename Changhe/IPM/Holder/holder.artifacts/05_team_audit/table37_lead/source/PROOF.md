# Direct Theorem 3.7 upper bounds for $C_\alpha$ at six exponents of Table 1

## Statement

Use the operator constant $C_\alpha$ of the report (homogeneous Hölder space modulo constants, Euclidean seminorm, centred
circular principal values). Then

| $\alpha$ | $\frac1{1000}$ | $\frac1{100}$ | $\frac1{20}$ | $\frac1{10}$ | $\frac15$ | $\frac{99}{100}$ |
|---|---|---|---|---|---|---|
| $C_\alpha\le$ | 637.0404763100 | 64.0882805059 | 13.1843720067 | 6.8520467682 | 3.7444366045 | 42.2253356279 |

(upper interval endpoints rounded up at ten decimals; `results/table37.json`).

## Proof

Theorem 3.7 of the report, with $\delta=\frac1{64}$ and $m=16$ phases $\phi_j=j\pi/32$, states

$$C_\alpha\le S_\alpha(\delta)+\sec\frac\pi{64}\max_{0\le j\le16}\big(L_\alpha(\phi_j)+W_\alpha(\phi_j)+E_\alpha(\phi_j)\big),\qquad
S_\alpha(\delta)=\frac{2a_2(\alpha)\delta^\alpha}\alpha+(1+2\delta)^\alpha\frac{\delta^2}{2(1-\delta)^2},$$

for any admissible choice of the local flows (paired local circles, $L_\alpha$), of the middle-circle plans (Theorem 3.6,
$W_\alpha$) and of the exterior-circle plans (Theorem 3.5, $E_\alpha$). Each of the three terms is an upper bound for every
admissible plan, so the plans may be chosen in any way, in particular by floating optimization at the exponent itself;
only the evaluation of the chosen plans must be rigorous. The three terms are computed separately in ball arithmetic
(160 bits for the circle terms) with the programs used for the nodal certificates of the closed form of Theorem 9.3 (B)
and of the third pass of the uniform comparison of Theorem 9.2:

- `code/local_nodes.py`: paired local circles, $512$ cells per circle, $256$ radial bins of $[\delta,\frac12]$, greedy exact integer
  flows (the flows depend only on the cell masses and the distance order, not on the exponent), in four row chunks
  (`local/r*_*.json`). Each chunk also encloses $S_\alpha(\delta)$, which `code/table37.py` recomputes and compares.
- `code/mid_nodes.py`: middle circles, $512$ cells per half, $512$ radial bins of $[0,\frac\pi2]$, plans by `best_plan` ($17$ trials)
  chosen at the exponent itself, in $16$ row chunks of $32$ bins (`mid/n512_*.json`).
- `code/far_nodes.py`: exterior circles, $512$ cells, $128$ radial bins of $u\in[\frac14,1]$, plans by `best_plan` ($9$ trials) chosen at the
  exponent itself (`far/far_*.json`).

`code/table37.py` checks that the middle chunks cover the $512$ radial rows exactly once and that the local chunks cover all
$256$ radial rows and all $17$ phases exactly once, that the grid parameters agree between chunks, and that the hashes of the
programs recorded in the chunks equal the hashes of the files in `code/`. It then forms, at each phase, the sum of the
three upper enclosures, takes the maximum over the $17$ phases, multiplies by $\sec\frac\pi{64}$, adds $S_\alpha(\delta)$ and rounds the
upper endpoint up. The local and middle programs and their helpers (`local_nodes.py`, `mid_nodes.py`,
`certify_local_circles_greedy.py`, `local_circle_greedy.py`, `middle_circle_plan.py`, `circle_transport_plan.py`,
`certify_far_circles.py`) are byte-identical to the copies in `../lead_closed_form37/code/`. `far_nodes.py` is the exterior
program of the uniform comparison (`09_uniform_comparison/lead_certificate/source/far_nodes.py`) with one change, the
import path set to its own folder; it is run with `--ref` equal to the exponent, so the plans are selected at the
exponent itself. `refl_nodes.py` is identical to the copy in that folder; only its function `a3_of` (the series for $a_3$)
is imported. $\square$

## Values

| $\alpha$ | $S_\alpha(\delta)$ | remainder | $C_\alpha\le$ | worst phase $j$ | local | middle | exterior | previous best (source) |
|---|---|---|---|---|---|---|---|---|
| 1/1000 | 633.8805868640 | 3.1598894460 | 637.0404763100 | 16 | 2.23326143 | 0.27362702 | 0.64919479 | 637.024849 (Theorem 5.7(ii)) |
| 1/100 | 60.9759126072 | 3.1123678988 | 64.0882805059 | 16 | 2.18294156 | 0.27366909 | 0.65200828 | 64.089516 (Theorem 9.3) |
| 1/20 | 10.2661674077 | 2.9182045990 | 13.1843720067 | 15 | 1.97499331 | 0.27412772 | 0.66556848 | 13.189650 (Theorem 9.3) |
| 1/10 | 4.1413084470 | 2.7107383213 | 6.8520467682 | 15 | 1.74803816 | 0.27455756 | 0.68487741 | 6.862161 (Theorem 9.3) |
| 1/5 | 1.3500977783 | 2.3943388262 | 3.7444366045 | 14 | 1.38290506 | 0.27495076 | 0.73359894 | 3.763643 (Theorem 9.3) |
| 99/100 | 0.0100039251 | 42.2153317028 | 42.2253356279 | 11 | 0.34390002 | 0.29288287 | 41.52769862 | 42.262094 (Theorem 3.5) |

At the worst phase, the three parts are listed in `results/table37.json` (`parts_at_worst_phase`). Against the best
certified values of Table 1 before this computation, the new values are smaller at $\alpha=\frac1{100},\frac1{20},\frac1{10},\frac15,\frac{99}{100}$, by 0.001235, 0.005278, 0.010114, 0.019206, 0.036758 respectively. At $\alpha=\frac1{1000}$ the value 637.040477 is larger than the explicit bound $637.024849$ of Theorem 5.7(ii), which remains the best there; the row is kept as a cross-check.

## Reproduction

```
bash code/run_table37.sh      # about 40 minutes, sequential, single-threaded; every step is bounded by 590 s
python3 code/table37.py       # writes results/table37.json
```
