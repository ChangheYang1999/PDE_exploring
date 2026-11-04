# T2_FAR_AE_PLAN_v02: corrected priced plan (HEURISTIC) for a certified windowed band upper A_E^+(a_W) at Rw = Ww = 200 on route F-a, after the theory auditor AT1697 to AT1703 (audit_v517) and numerical audit exchange v444, with Lemma ENC (CLAIMED) for the boxes at zeta = 0 and on the first |xi| cell

Agent the second theory agent, written 2026-11-03 from 23:42Z; frozen 2026-11-03T23:45:01Z. Supersedes notes/T2_FAR_AE_PLAN_v01.md (frozen
23:17:11Z, SHA256 b1268b6343a31d76033fae1401146b91b6602d0951c659d098b8e6179f69673f, unchanged). Recipients: the coordinator
(X8 input, inputs due 00:30Z, freeze 00:35Z), the theory auditor and the numerical auditor (audit), the first theory agent (route F-a). Code and run paths are
relative to research/h4/far009/ of agent the second theory agent, scratch/ and notes/ paths to the agent directory. Labels: Lemma SYM and
Proposition AE-CS are CONFIRMED (conditionally for AE-CS, AT1697, AT1698); Lemma ENC is CLAIMED; every number of
section 3 is FLOAT; every price of section 4 is HEURISTIC. No certification code was written.

## 0. Summary

- Target (unchanged): a certified A_E^+ >= the AT-707 band bound of A_low(8 pi) for a_W with A_E^+ <= 1.3263305
  (then max(SC^+, A_E^+) <= 1.3263305, since SC^+ = 4194197216881219/9007199254740992 is about 0.46565).
- Audits of v01. The theory auditor CONFIRMS Lemma SYM (AT1697) and, conditionally, Proposition AE-CS with the full AT-707
  hypotheses, derivative uppers for the same orders as the weight W, and a finite continuum essential supremum
  (AT1698); the radial reduction, the support in two disks and the first-quadrant factor 4 (AT1699); the cancellation
  identity and the sign of its bracket (AT1700). It REFUTES the reuse of the r_B zero region of code/c1/k_cells.py
  for r_E (AT1701) and the count of about 130 cells (AT1702: 202). AT1703 (a certified A_E and closure) is OPEN.
  The numerical auditor (exchange v444) CONFIRMS 202 cells, CONFIRMS the allowance 1.427 only as arithmetic on the 165 stored FLOAT
  rows, and REFUTES the claim that 1.45495 was obtained at the same configuration.
- Corrections (section 0a): the cell count, the comparison, the scope of 1.427, the X8 time, the zero region, the
  antipodal indicators and the quadrant factor.
- New (section 2): Lemma ENC, finite enclosures of r_E/|zeta|^2 on every box, including the boxes that touch
  zeta = 0 and the first |xi| cell [0, 1/20], uniformly as |xi| -> 0 and |eta| -> 0. It replaces the zero region and
  gives the finiteness of the kernel integral for every c_s >= 0 with c_1 + c_2 > 0.
- New FLOAT comparison on one grid (section 3): at the final configuration (tau 9/8, slopes 193/100 and 147/100,
  integer orders 1 to 5, grid 1201 x 240) on the same 166 sampled radii, the sampled sup is 1.18672 (at |xi| = 0.65)
  with Lemma SYM and 1.45973 (at |xi| = 3.65) without it.
- Price (HEURISTIC, section 4): the second theory agent theory done (this note), code 3 to 5 h, run 0.1 to 1.7 core-hours on core 41
  (202 cells, at most 10000 boxes per cell), note 1 h; the theory auditor 3 to 6 h of review plus a replay. From X8 (publication
  about 00:45Z) the second theory agent part ends at about 04:50Z to 08:30Z and the review at about 08:00Z to 16:10Z; the later end
  is after the final Part VII deadline (15:35Z).
- What it would give (unchanged from v01 section 0): route F-a's far inequality, still conditional on AT-1540 and on
  the strain bound s^+ = 137/125 (AT-1599); no row C2, nothing at strain 3/2, no near bound; the verdict stays NO,
  O3 unresolved.

## 0a. Errata to v01

- E1 (AT1702, v444). Section 4(C) "about 130 cells" is wrong. Width 1/20 on [0, 63/10] gives 126 cells and width 1/4
  on [63/10, 8 pi] gives 76 cells, the last one [501/20, 8 pi] (clipped). The mesh has 202 cells; section 4 reprices
  it.
- E2 (v444). Section 0 and the table of section 3 say "Without Lemma SYM the same configuration gives 1.45495". It
  does not: runs/ae_cs_v1_e.json (1.45495) has tau 1.1265, slopes 1.9312 and 1.4689, orders 1 to 5 by 1/2 and 20
  sampled radii, while runs/ae_cs_v1_d.json (1.18700) has the same parameters but 165 radii (18 in common), and the
  final configuration of runs/ae_cs_v2_h.json has tau 9/8, slopes 193/100 and 147/100 and orders 1, ..., 5. The
  comparison at one configuration on one grid is section 3 (1.18672 against 1.45973).
- E3 (v444). "Every row may be overestimated by a factor 1.427 in its kernel integral before the margin is lost" holds
  only for the 165 sampled FLOAT rows of runs/ae_cs_v2_h.json at their FLOAT coefficients c_s (the numerical auditor's
  reconstruction: minimum 1.4274500303843765 at |xi| = 73/20). It gives no margin on the continuum, no integration
  enclosure and no allowance for other c_s on a cell.
- E4 (AT1703 text, v444). The X8 time 02:05Z of v01 sections 0 and 4 is superseded: X8 inputs 00:30Z, freeze 00:35Z,
  publication about 00:45Z (the coordinator's notes 23:14Z item (e)). Section 4 redoes the timeline.
- E5 (AT1701). v01 section 4(B) says "adapted from code/c1/k_cells.py" without excluding its zero region: k_cells.py
  returns R = 0 on boxes with t1 <= 2 pi and rho1 + t1 <= 2 pi, because r_B vanishes when both ramp angles vanish.
  r_E does not vanish there. At xi = (1, 0), eta = (-1, 0), tau = 9/8: |w - w'|^2 = 4, Ktil = 8, P = -4 q^2 = -441/25,
  phi_E(1)^2 = 4096/10657, and r_E = 3281636/266425 > 0 (recomputed exactly with sympy, in agreement with AT1701).
  ae_cells.py has no zero region; Lemma ENC gives the enclosure on every box.
- E6 (AT1699). v01 section 4(B) says the angular range is a quarter turn but gives neither the factor nor the
  indicators. The kernel integral is 4 times its integral over the first quadrant psi in [0, pi/2] (xi = (t, 0)).
  G_xi(zeta) carries the indicator of |xi - zeta| <= 8 pi and G_xi(-zeta) that of |xi + zeta| <= 8 pi; both are kept,
  box by box, and the support of Gbar_xi is B(xi, 8 pi) union B(-xi, 8 pi), inside |zeta| <= |xi| + 8 pi <= 16 pi.
- E7 (AT1703 text, v444). The sampled radii of section 3 of v01 run from 1e-9 to 25, not over [0, 8 pi], and the
  FLOAT quadrature omits the disk |zeta| < RHOMIN = 1e-6. Both concern FLOAT values only; the certificate covers
  [0, 8 pi] by cells and every zeta by boxes (section 4).

## 1. Audit status of the plan (the theory auditor audit_v517, 23:27:01Z; numerical audit exchange v444, 23:33:14Z)

| id | claim | verdict |
|---|---|---|
| AT1697 | Lemma SYM | CONFIRMED (a vanishing energy factor is treated directly, an infinite kernel norm gives no bound) |
| AT1698 | Proposition AE-CS | CONFIRMED conditionally: full AT-707 hypotheses, same-order derivative uppers, finite continuum essential supremum; factor 1/(4 pi) correct |
| AT1699 | radial Kbar, support in two disks, factor 4 on the first quadrant | CONFIRMED (for xi != 0 and almost every zeta) |
| AT1700 | cancellation identity, bracket (1 - phi phi') <xi><eta> - theta theta' >= 0 | CONFIRMED (no small-frequency enclosure inferred from it alone) |
| AT1701 | reuse of the r_B zero region for r_E | REFUTED (prospective; erratum E5) |
| AT1702 | about 130 cells | REFUTED; 202 (erratum E1) |
| AT1703 | a certified A_E <= 1.3263305 and closure | OPEN |
| v444 | 202 cells; 1.427 as arithmetic on stored rows; same-configuration claim for 1.45495 | CONFIRMED; CONFIRMED (FLOAT rows only); REFUTED (erratum E2) |

The theory auditor's requirements for an implementation, and where this plan meets them: no zero region (E5, section 2); both
antipodal indicators and the factor 4 (E6, section 4(B)); an enclosure of the whole first |xi| cell and of all zeta
near 0, with integrability not taken from c_s != 0 alone (Lemma ENC, section 2); the literal 202-cell mesh repriced
(section 4(C)).

## 2. Lemma ENC (CLAIMED): box enclosures of r_E/|zeta|^2 that stay finite at zeta = 0 and at xi = 0

Setting. q = 21/10, tau = 9/8. xi = (t, 0) with t > 0; zeta = rho (cos psi, sin psi) with rho > 0; eta = xi - zeta
with v = |eta| > 0. a = <t>, b = <v>, w = (1, 0), w' = eta/v, c = w.w', om2 = |w - w'|^2 = 2 (1 - c),
s1c = (1 - c)/rho^2, tau' = log(a/b). M = max(t, v), m = min(t, v). alpha = arctan((t/tau)^2), beta = arctan((v/tau)^2),
so that phi_E(t) = sin alpha, theta_E(t) = cos alpha, phi_E(v) = sin beta, theta_E(v) = cos beta (phi_E(t) =
u/(u^2 + 1)^(1/2), u = (t/tau)^2, as in Proposition AE-CS). Write pp = phi_E(t) phi_E(v), tt = theta_E(t) theta_E(v),
    f(x) = sinh^2(q x/2) - q^2 sinh^2(x/2),
    Ng = q^2 ((t - v)/rho)^2 (1/(a + t) + 1/(b + v)) (a + b + t + v)/(a + b)^2,
    S1 = 2 (a b - t v) + (q^2 + 1) t v (1 - c) + q^2 (t - v)^2,
and r_E = Ktil - pp P - tt om2 with Ktil, P as in Lemma HS (T2_FAR_v02 section 2.3).

Statement.
(i) r_E/rho^2 = A1 + A2 + A3 with
      A1 = 4 a b (1 - pp) sinh^2(q tau'/2)/rho^2,
      A2 = (om2/rho^2) [ (1 - pp)(a b - 1) + 2 sin^2((alpha - beta)/2) ],
      A3 = pp [ s1c S1 + 4 a b f(tau')/rho^2 - Ng ],
    and A1 >= 0, A2 >= 0, S1 >= 0, f(tau') >= 0, Ng >= 0.
(ii) om2 <= 4 rho^2/M^2; |tau'| <= |t^2 - v^2|/(a + b); t^2 - v^2 = rho (2 t cos psi - rho) and |t^2 - v^2| <= 2 M rho;
    |t - v| <= rho; 0 <= pp <= t^2 v^2/tau^4.
(iii) Consequently
      -pp Ng <= r_E/rho^2 <= A1 + 4 (1 - pp)(2 + m^2)/(a b + 1) + 8 rho^2/tau^4 + (2 m^2/tau^4) S1 + 4 a b pp f(tau')/rho^2 - pp Ng,
    where A1 = a b (1 - pp) q^2 (tau'/rho)^2 (sinh(y)/y)^2 with y = q tau'/2, |tau'/rho| <= |2 t cos psi - rho|/(a + b),
    and 4 a b f(tau')/rho^2 = 4 a b (tau'/rho)^2 tau'^2 F(tau'^2) with F as in code/c1/k_cells.py (f(x) = x^4 F(x^2)).
    Every term on the right and the left is bounded on every bounded set of (t, rho, psi), uniformly as t -> 0 or
    v -> 0.
(iv) Hence, for every box T x [r0, r1] x [psi0, psi1] of [0, 8 pi] x [0, 16 pi] x [0, 2 pi] (r0 = 0 and t0 = 0
    allowed), sup |r_E|/rho^2 over the points with t > 0, v > 0 of the box is finite, and an interval enclosure of the
    right sides of (iii) bounds it. With h radial and positive and bounded ratios h(v)/h(t) on the band, Gbar_xi/rho^2
    is bounded on |zeta| <= 16 pi, and Kbar(xi) = int Gbar_xi^2/W_xi is finite for every c_s >= 0 with c_1 + c_2 > 0:
    in polar coordinates the integrand is (Gbar_xi/rho^2)^2 g(rho) with g(rho) = rho^5/W(rho) <= min(rho^3/c_1, rho/c_2),
    integrable at 0, and the domain is bounded. With c_1 = c_2 = 0, g behaves like 1/(c_3 rho) at 0 and no finiteness
    follows from (iii); ae_cells.py asserts c_1 + c_2 > 0 on every cell (the theory auditor, audit_v517: arbitrary nonzero c_s do
    not by themselves prove integrability).

Proof.
(i) With a^q - b^q = (a b)^(q/2) 2 sinh(q tau'/2), Ktil = a b om2 + 4 a b sinh^2(q tau'/2). Hence
    r_E = (1 - pp) Ktil + pp (Ktil - P) - tt om2 = 4 a b (1 - pp) sinh^2(q tau'/2) + om2 [(1 - pp) a b - tt] + pp (Ktil - P).
    (1 - pp) a b - tt = (1 - pp)(a b - 1) + (1 - pp - tt), and 1 - pp - tt = 1 - cos(alpha - beta) = 2 sin^2((alpha - beta)/2).
    Ktil - P = 2 (1 - c)(a b - t v) + (q^2 + 1) t v (1 - c)^2 + 4 a b f(tau') + q^2 (1 - c)(t - v)^2 - rho^2 Ng is the
    identity of code/c1/k_cells.py (T2_FAR_CS_v02 item 3; Lemma KP, CONFIRMED within AT-1536 to AT-1538), and divided
    by rho^2 it is s1c S1 + 4 a b f(tau')/rho^2 - Ng. Signs: pp, tt in [0, 1]; a b >= 1 and a b - t v >= 1; sinh(q y) >=
    q sinh(y) for y >= 0 and q >= 1 (the difference vanishes at 0 and has derivative q (cosh(q y) - cosh(y)) >= 0), so
    f >= 0 (f is even).
(ii) Let |xi| >= |eta| (the other case is symmetric). |w - w'| <= |xi/|xi| - eta/|xi|| + |eta/|xi| - eta/|eta|| =
    |xi - eta|/|xi| + (|xi| - |eta|)/|xi| <= 2 |xi - eta|/|xi| = 2 rho/M. log is 1-Lipschitz on [1, infinity), so
    |tau'| <= |a - b| = |a^2 - b^2|/(a + b) = |t^2 - v^2|/(a + b). t^2 - v^2 = |xi|^2 - |xi - zeta|^2 = 2 xi.zeta - rho^2 =
    rho (2 t cos psi - rho), and |t^2 - v^2| = (t + v)|t - v| <= 2 M rho since |t - v| <= |xi - eta| = rho. phi_E(t) =
    u/(u^2 + 1)^(1/2) <= u = t^2/tau^2, and the same at v.
(iii) The lower bound: drop A1, A2, pp s1c S1 and the f term, all >= 0. The upper bound: by (ii) om2/rho^2 <= 4/M^2, and
    a b - 1 = (a^2 b^2 - 1)/(a b + 1) = (t^2 + v^2 + t^2 v^2)/(a b + 1) <= M^2 (2 + m^2)/(a b + 1). arctan is 1-Lipschitz,
    so |alpha - beta| <= |t^2 - v^2|/tau^2 <= 2 M rho/tau^2, and 2 sin^2(x/2) <= x^2/2 gives
    (om2/rho^2) 2 sin^2((alpha - beta)/2) <= (4/M^2)(2 M^2 rho^2/tau^4) = 8 rho^2/tau^4. pp s1c = pp om2/(2 rho^2) <=
    (t^2 v^2/tau^4)(2/M^2) = 2 m^2/tau^4 since t v = M m. The two expressions for A1 and the f term are the definitions
    with tau'/rho bounded by (ii): |tau'/rho| <= |2 t cos psi - rho|/(a + b) <= 2 M/(a + b). Ng <= q^2 (1/(a + t) +
    1/(b + v))(a + b + t + v)/(a + b)^2 since |t - v| <= rho. All these are bounded on bounded sets.
(iv) From (iii); h(v)/h(t) is bounded on the band since h is positive, continuous and radial; the rest is stated.
QED.

Use. On each box, ae_cells.py encloses r_E/rho^2 by the interval form of (i), using the reduced forms of k_cells.py
for s1c where they apply (s1c = sin^2 psi/(v (v + eta_1)) when eta_1 > 0 on the box; s1c = (1 - eta_1/v)/rho^2 when
rho0 > 0), and intersects the result with the bounds of (iii). In k_cells.py the reduced form needs eta_1 > 0 when
rho0 = 0, which holds for every cell with t0 >= 1/20 (the first radial box is [0, 1/32]) but fails on the first cell
[0, 1/20]; there (iii) is the enclosure on the boxes with rho0 = 0. Such a box contributes 2 pi (sigma1 - sigma0) sup R
times an upper of int_0^rho1 g, where sup R is bounded by (iii) independently of rho1 and int_0^rho1 g <=
min(rho1^4/(4 c_1), rho1^2/(2 c_2)), so halving rho1 makes the contribution as small as needed.
Points with t = 0 or v = 0 form a null set and do not enter the essential supremum or the integrals (AT1699).

FLOAT check (not a proof): code/c1/enc_check.py evaluates (ii) and (iii) and compares (i) with the direct formula at
20000 random points in 50-digit mpmath (t from 1e-9 to 8 pi, rho from 1e-9 to 16 pi, one point in five with rho/t in
[1e-3, 10^0.5]; runs/enc_check_2340.log): max om2/(4 rho^2/M^2) = 0.99999661; identity error at most 2.71e-33
relative to 1 + |r_E/rho^2|; max (r_E/rho^2 - upper)/(1 + |r_E/rho^2|) = -0.666675 and max (lower - r_E/rho^2)/
(1 + |r_E/rho^2|) = -2.1383e-7, so every point satisfies both bounds.

## 3. FLOAT comparison on one grid (errata E2, E7)

code/c1/ae_cs_wopt_float.py (unchanged, SHA256 7003aabe...b7052) at tau 9/8, p 2, h slopes 193/100 (t <= 1/2) and
147/100, orders 1, ..., 5, grid 1201 radii x 240 angles, RHOMIN 1e-6, D_s^+ of runs/ds_window_v2_2158.json, c_s per
radius by L-BFGS-B, on 166 radii: the 165 of runs/ae_cs_v2_h.json (1e-9, 0.05 to 4 by 0.05, 4.25 to 25 by 0.25) and
25.13274122 (just below 8 pi). Script scratch/aewopt_verify3.sh, 23:34:19Z to 23:35:53Z on core 41, log
runs/ae_cs_v3.out.

| run | SYM | sup of lead + CS over the 166 radii | at \|xi\| | value at \|xi\| = 25.13274122 | margin to 1.3263305 |
|---|---|---|---|---|---|
| runs/ae_cs_v3_i.json | 1 (Lemma SYM) | 1.1867232199856157 | 0.65 | 0.71829 | 0.13961 |
| runs/ae_cs_v3_j.json | 0 | 1.4597266449643085 | 3.65 | 0.82294 | -0.13340 |

The SYM=1 row reproduces runs/ae_cs_v2_h.json exactly at all 165 common radii (checked from the JSON files). All values are FLOAT
samples of a quadrature, not bounds.

## 4. Certification plan and prices (HEURISTIC), replacing v01 section 4

A. Theory: Lemma SYM and Proposition AE-CS (CONFIRMED, AT1697, AT1698), Lemma ENC (section 2, CLAIMED). Data: tau = 9/8,
   p = 2, h(t) = <t>^(-193/100) for t <= 1/2 and h(t) = <1/2>^(-193/100) (<t>/<1/2>)^(-147/100) for t >= 1/2,
   Sigma = {1, ..., 5}, D_s^+(a_W) of runs/ds_window_v2_2158.json (same orders as W, AT1698). Done in this note
   except the theory auditor's review of Lemma ENC (about 0.5 h).
B. Code (the second theory agent, 3 to 5 h): code/c1/ae_cells.py, a new file that reuses the interval helpers of code/c1/k_cells.py
   (directed binary64 intervals moved outward after every operation, arb at monotone endpoints, Fint, Gint) and
   differs from it in:
   - no zero region (E5); no RMAX tail term (Gbar_xi = 0 for rho > t + 8 pi);
   - the box enclosure of r_E/rho^2 of Lemma ENC (identity (i), reduced forms where they apply, intersected with (iii));
   - alpha = arctan((t/tau)^2) as an increasing function at the interval ends; phi_E = sin alpha, theta_E = cos alpha;
     1 - pp - tt = 2 sin^2((alpha - beta)/2) from the interval of |alpha - beta|, clipped to [0, pi/2];
   - h(v)/h(t) from the piecewise power law (h decreasing) at the interval ends;
   - the two indicators separately, for the box and for its antipode: 0 if v > 8 pi on the whole box, 1 if v <= 8 pi on
     the whole box, the interval [0, 1] otherwise;
   - Lemma SYM on boxes: psi = (pi/2) sigma with sigma in [0, 1]; the antipode of the box [r0, r1] x [psi0, psi1] is,
     after the reflection psi -> -psi (G_xi is symmetric in it since xi = (t, 0)), the box [r0, r1] x [pi - psi1,
     pi - psi0]; the box upper of Gbar/rho^2 is the mean of the two box uppers of G/rho^2, and the box adds
     4 (pi/2)(sigma1 - sigma0) (sup Gbar/rho^2)^2 Gup(r0, r1) = 2 pi (sigma1 - sigma0) (sup Gbar/rho^2)^2 Gup(r0, r1)
     (factor 4 of AT1699);
   - radial grid 0, 1/32, then factor 1.25 up to t1 + 8 pi (31 to 35 radial intervals), 16 angular intervals;
   - c_s per cell from the FLOAT choice of ae_cs_wopt_float.py at the cell midpoint; c_1 + c_2 > 0 asserted;
   - cell bound: lead O^+ - (O^+ - SC^+) phi_E(t0)^2 at the left end (decreasing in t) plus
     (1/(4 pi)) (sum_s c_s (D_s^+)^2)^(1/2) (Kbar^+)^(1/2), in arb, with fup for every stored upper;
   - tests: identity (i) against the direct formula (FLOAT and arb points, including AT1701's point, where the code
     must return 3281636/266425 within its enclosure), the bounds of enc_check.py, cell bounds against
     ae_cs_wopt_float.py at the cell midpoints (each certified bound must lie above).
C. Run (the second theory agent, core 41, 0.1 to 1.7 core-hours). Mesh: the 202 cells of E1. Initial boxes per cell: at most 35 x 16 =
   560, each with two evaluations (box and antipode). Refinement as in k_cells.py (split into four, largest gap
   first) until the cell bound is at most 1.3263305 - 0.01, or Kbar^+ <= 1.3 Kbar^-, or 10000 boxes. Basis: run 1941
   of k_cells.py took 1129.1 s for 740180 box evaluations (1.53 ms each on average; 0.83 ms on its 74 cells in
   [6.3, 8 pi], 2.83 ms on [8 pi, 200]); at an assumed 3 ms per box (two evaluations, more terms) the initial pass
   costs 202 x 560 x 3 ms = 339 s, a refinement like that of k_cells.py on [6.3, 8 pi] (6377 boxes per cell) 3865 s,
   and the cap of 10000 boxes per cell 6060 s. The per-box time is measured first on a 3-cell timing run; the full
   run is detached (with its log polled) and split into chunks of about 50 cells. A cell that stops at the cap above
   1.3163305 is split in t and rerun alone.
D. Note (the second theory agent, 1 h): notes/T2_FAR_AE_v01.md with the statement, the code and run hashes, the cell table and A_E^+.
E. Review (the theory auditor, 3 to 6 h, plus a replay of 0.1 to 1.7 core-hours): Lemma ENC and its use (0.5 to 1 h); the
   enclosures and the rounding of ae_cells.py (2 to 4 h; the shared helpers are those of k_cells.py under AT-1540); the
   replay. The numerical auditor's numerical audit in parallel.
Timeline from X8 publication (about 00:45Z): code to 03:45Z - 05:45Z (the second theory agent a work session ends about 02:44Z; the next
the second theory agent shift continues), run to 03:50Z - 07:30Z, note to 04:50Z - 08:30Z, review with replay to 08:00Z - 16:10Z. The
later end is after 15:35Z. Risks: (1) Lemma ENC's bounds may be loose on the first cell, where the reduced forms do not apply
(the sampled FLOAT margin is 0.139 on [0, 1)); (2) the theory auditor core serves the root reviews and the CS-B replay first;
(3) the certificate inherits whatever AT-1540 finds in the derivative records.
Recommendation for X8 (unchanged in substance): code it only if it can start at X8 and the theory auditor can review it by 15:35Z;
otherwise record it in Part VII as a priced conditional step, with Lemma SYM and AE-CS CONFIRMED, Lemma ENC CLAIMED and
the sampled FLOAT margin 0.1396.

## 5. Dependencies and what this does not give

Unchanged from v01 section 5: A_E^+ rests on the D_s^+(a_W) of Proposition DW and hence on the B1 derivative records
under AT-1540 (OPEN); route F-a also needs s^+ = 137/125 (AT-1599, OPEN) and the near side; row C2 of Proposition F
(strain 3/2) stays OPEN; no existence certificate follows. Verdict: NO; O3 unresolved.

## 6. Files (SHA256)

- notes/T2_FAR_AE_PLAN_v01.md b1268b6343a31d76033fae1401146b91b6602d0951c659d098b8e6179f69673f (superseded, unchanged)
- code/c1/enc_check.py b9d3db168f41b6f69538afecb5638920408b09eded9c2da19648356e5cba30f7 (FLOAT check of Lemma ENC)
- runs/enc_check_2340.log 932eec182c6d0cd5bbec075eb1219449fefd268a2e2de25fa85b520e341a73cc
- code/c1/ae_cs_wopt_float.py 7003aabe1c0cadf4a3680091d5a4054e6512e390e8ba457d41bf7e7ce18b7052
- scratch/aewopt_verify3.sh 4a97a3c7e6f443003227d335385a99ca069bf6bf406111c0c91f149523540d45
- runs/ae_cs_v3_i.json 44c100865f92359bb7542e566c387b099198fc77b92dd733a1e7f9841c7f4bfe
- runs/ae_cs_v3_j.json 95d1e176726f03b1ec13561b0434ea96ae4b3f3e682c1534da6a8e95b1df64a6
- runs/ae_cs_v3.out 104b766ddae7183550cd643a18fccf02d92fa30d23b2a7a32bc48c6d1872d808
- runs/ae_cs_v2_h.json c3684dfb82af3bf7e50aa6893b45550f8046247f54c3c469168f83b39324f02d
- runs/ae_cs_v1_d.json a1221a334df970ab1e3ba4775a8112a25d8b83af14b2c4717b4422b4532fcd7f
- runs/ae_cs_v1_e.json 2d28ec22e64571a545ced221f69fbfe8b62bd764c479a226f6251d159f6a3024
- runs/ds_window_v2_2158.json e26aeb71eadadf209a0140d50d8e9339aa1c8a3985e96cb8862893c3377abf6a
- runs/k_cells_1941.json 38735c097f0367c0e287be0eb015ece869056c8487d7bedb964490567cc93d8b (timing basis of section 4(C))
