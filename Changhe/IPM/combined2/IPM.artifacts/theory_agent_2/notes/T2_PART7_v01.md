# T2_PART7_v01: the second theory agent's Part VII entry (THEORY_NEW_RESULTS: O2, O3 and the far section), with the theory auditor verdicts, the far ledger (row C2 OPEN) and the answers to the theory auditor on Theorem CS-B (AT-1539, AT-1540)

Agent the second theory agent, written 2026-11-03 from 23:27Z; frozen 2026-11-03T23:29:19Z. Recipients: the first theory agent (publisher of THEORY_NEW_RESULTS
and of theory_vNN), the coordinator (X7 item 5(d); input for X8, freeze about 00:35Z), the theory auditor (audit). Paths: notes/ relative
to the agent directory; code/, runs/, data/ and inputs013/ relative to research/h4/far009/ of agent the second theory agent. Status labels:
CONFIRMED (the theory auditor verdict cited), CLAIMED (proved by the second theory agent, audit requested), FLOAT (sampled value, not a bound),
HEURISTIC, OPEN.

This is version 1. It indexes results; it restates no proof. The final Part VII far section is due by
2026-11-04T15:35Z (X7 item 5(d)); it will be a later version of this note and will change only section 2 and the
status updates of section 1.3.

## 0. Answer

No complete existence theorem follows from the second theory agent's results, and none is claimed. The first unresolved condition is
O3. At the chain center C2-N1-013 the explicit route needs a certified weak-energy constant C^opt(b0) (ledger item G3:
near and far charges), a certified background rate (item B) and the actual-generator hypotheses (item G2). On the far
side neither far route is closed: Proposition F needs row C2, for which no priced route fits before the stop
(HEURISTIC, with the qualifications of numerical audit exchange v370, section 2.1), and route F-a needs a certified A_E^+(a_W) and a certified strain bound s^+.

## 1. O2 and O3: notes/T2_O2O3_FINAL_v02.md

### 1.1 The entry

notes/T2_O2O3_FINAL_v02.md, frozen 2026-11-03T21:23:48Z, SHA256
19c9bdfc9ca6ba062cb669029ea45a940a1476f4b4fb47b386bc53cefb08bf6e. It supersedes notes/T2_O2O3_FINAL_v01.md (frozen
21:08:46Z, SHA256 7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1; errata in v02 section 8). Contents:
- section 2 (O2): the uniform small-k lifting (T2-HS1r, Lemma KP-W, WG-K, UT-K, S-inv-K, THR-K);
- section 3 (O3): Theorem A (the preferred type, qualitative: N(F) = ||J^q (W F)||_2 finite and ||F||_2 small enough,
  admissible ||F||_2 of order N(F)^(-2/(q-2)), constants finite but not numerical) and Theorem B (route Q at
  q = 21/10, every k-dependent constant numerical, with the capacity ceiling N(F) < b0^2/(4 lambda_1) and the floor
  L_B(R, K) > lambda_1 K);
- section 4: Theorem B at the chain center C2-N1-013 (allowance D > 1.61e11 at b0 = 0.60, D > 1.22e11 at b0 = 0.55,
  at beta_0 = 7/4 stipulated; AT-831);
- section 5: the status table; section 6: what would close O3, in order of leverage.
The explicit results are stated for q = 21/10 only (AT-1577, AT-1592).

### 1.2 the theory auditor's scope verdicts on v01 and v02

| id | audit | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|---|
| AT-1576 | audit_v480 | the consolidated qualitative O2/O3 statements remain valid with their cited proof restrictions; numerical constants and candidate closure remain open | CONFIRMED |
| AT-1577 | audit_v480 | the fixed 53/100 scalar proof justifies the explicit route for all 2 < q < 3 (counterexample q = 5/2, t = 2) | REFUTED; only q = 21/10 is admitted |
| AT-1578 | audit_v480 | the new N = 0.006 fractions are below 8.4 and 7.1 percent of b'M in the two specified cells | CONFIRMED |
| AT-1579 | audit_v480 | the full explicit energy theorem extends to arbitrary q, or these results give actual source013 closure | OPEN |
| AT-1592 | audit_v485 | v02 correctly restricts the explicit results to q = 21/10; the original hypotheses remain mandatory | CONFIRMED |
| AT-1593 | audit_v485 | the corrected scope or the newly appended far route closes O3 at source013 | OPEN; both far routes remain conditional |

Reading for Part VII: Theorems A and B and the results of the v02 status table hold as stated there, with the
explicit formulas at q = 21/10 only; no closure of O3 at 013 or at any other center follows (AT-1579, AT-1593).

### 1.3 Status changes since v02 was frozen (v02 is not edited)

- Corollary CS-W and Proposition DW (the S input of route F-a): CLAIMED in the v02 table, now CONFIRMED conditionally
  (AT-1594 to AT-1596), notes/T2_FAR_CSW_v02.md.
- Lemma SC-W (the Hessian input of route F-a for the window Rw = Ww = 200): CONFIRMED (AT-1366, AT-1367; its
  application to this window AT-1598). The v02 table did not list it.
- Theorem CS-B: unchanged (analytic parts CONFIRMED, AT-1536 to AT-1538; numerical application OPEN, AT-1540). The theory auditor
  REFUTED the general claim that nearest conversion of an arb upper is outward (AT-1539); the second theory agent's correction of
  20:19Z is answered in section 3.1.
- Row C2: still OPEN. The proofs of Lemma QID and Proposition ZO are now in notes/T2_QIDZO_v01.md (frozen
  2026-11-03T23:24:25Z, SHA256 cc67aa515de67fcc04496bcd1ed1f5529816a43bb957208c6a0cb5e2e7130c9e; CLAIMED).
- New: notes/T2_FAR_AE_PLAN_v01.md (frozen 23:17:11Z), a priced plan for a certified A_E^+(a_W) with Lemma SYM and
  Proposition AE-CS (CLAIMED); its numbers are FLOAT.

## 2. Far section (draft)

Both far routes bound the far constant of the 013 far piece a_f (complete far piece at erflog 8, rho 1, every angular
mode; exact inputs data/C1-N1-007_exact.json, SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21,
and inputs013/phi_007_b18s2_phi_exact.json, SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a).
q = 21/10, c = 4076476460239181/2251799813685248.

### 2.1 Proposition F (strain 3/2, target Gbar = q (c - 3/2), about 0.65167)

Proposition F (T2_FAR_F_v01; CONFIRMED conditional, AT-1236) gives the far bound max(SC^+, A_low^+(8 pi)) + S^+ <= Gbar
from Lemma HSB (T2_FAR_v02 section 2.3) and the rows below.

| row | content | status | where |
|---|---|---|---|
| C5a, C5b | a_f real, bounded, even in x_1 and x_2; hypotheses of NR-21 case B, a_f in S^(-lambda) | CONFIRMED (AT-1147 to AT-1152) | T2_FAR_C5_v01 |
| C1 | SC^+ = 0.46564943200002806 >= SC(a_f) | CONFIRMED (AT-1230 to AT-1234) | T2_FAR_C1_v01 |
| C3, C4 | S^+ = 0.059699233948103884 >= S_h^B(a_f; 2 pi, 8 pi, h), h = <min(abs(xi), 63/10)>^-1 (route B, Theorem CS-B); SC^+ + S^+ <= Gbar exactly | analytic parts CONFIRMED (AT-1536 to AT-1538); numerical application OPEN (AT-1540); rounding: section 3.1 | T2_FAR_CS_v02; notes 20:19Z |
| C2 | A_low^+(8 pi) >= A_low(8 pi) with A_low^+(8 pi) <= Gbar - S^+ (= 426560137443922093/720575940379279360 > 0.591971) | OPEN: no priced route fits before the stop (HEURISTIC; qualifications below); FLOAT band value 0.3848 (the second numerics agent) | T2_FAR_C2_PLAN_v01; T2_QIDZO_v01 |

Row C2 stays OPEN unless an auditor confirms a certified A_low^+ (X7 item 5(d)). T2_FAR_C2_PLAN_v01 prices the
routes it considers (HEURISTIC): a certified eigenproblem on the window support would need an order of 1.6e6 or more
in the parity class, against a dense capacity of about 5e4 on one core in 32 GB. The numerical auditor's audit of that plan (exchange
v370; CONFIRMED for the exact conditional budget and the values of the assumed pricing formulas) adds two
qualifications, kept here: (i) the parity count is a planning estimate, not a proved minimum dimension of every
possible certificate, so the evidence supports leaving C2 OPEN and not launching the dense routes but does not prove
that every route is impossible before the stop, and the FLOAT radius-100 tail and window charges do not prove a
mathematical exclusion of that radius; (ii) one 65000 by 65000 binary64 matrix alone needs 33800000000 bytes (above
32 decimal GB, below 32 GiB) and order 50000 needs 20 decimal GB for one matrix, before factors, copies or interval
storage, so a practical capacity needs a full allocation plan. Proposition ZO (CLAIMED) shows that no bound of A_low
by SC, Fourier moments M_s (s > 0) and energies D_s (s > 1) alone, vanishing with them, can hold, so the tail cannot be
charged through its derivatives only.

### 2.2 Route F-a (strain s^+ = 137/125, window Rw = Ww = 200)

AT-911 (CONFIRMED): A_*(a_W + a_t) <= max(SC^+, A_E^+) + S^+ + OMF(a_t), with a_W = a_f (1 - Sinf((r - Rw)/Ww)) and
a_t = a_f - a_W. The target is q (c - s^+), equal to 1.5000703414199960 at s^+ = 137/125.

| input | value | status | where |
|---|---|---|---|
| SC^+(a_W) | 4194197216881219/9007199254740992 = 0.46564943200002806 | CONFIRMED (AT-1366, AT-1367, AT-1598) | Lemma SC-W, notes 17:15Z; T2_FAR_CSW_v02 E1 |
| S_W^+ >= S_h^B(a_W) | 0.05970055144902641 | CONFIRMED conditionally (AT-1594 to AT-1596), on AT-1540 and the B1 records D_s^+ | T2_FAR_CSW_v02 |
| OMF^+(a_t) | 0.11403919054571054 | CONFIRMED (AT-1336 to AT-1338) | notes 16:19Z |
| A_E^+(a_W) | needed: A_E^+ <= 1.3263305 | OPEN; FLOAT band value 1.1342736; FLOAT value 1.18700 of the Cauchy-Schwarz upper of Proposition AE-CS (margin 0.1396); priced plan for X8 | T2_FAR_AE_PLAN_v01 |
| s^+ | 137/125 | OPEN (AT-1599); the theory auditor confirms strain <= 137/125 only regionally so far (the contiguous inner region r^2 <= 7/25 and the root 98 annulus 49/15 <= r^2 <= 99/29; the theory auditor's notes 23:16Z, the coordinator's notes 23:14Z) | ledger item B |

Since S_W^+ + OMF^+ < 0.17373975 and SC^+ < 1.3263305 < q (c - 137/125) - 0.17373975, the far condition of route F-a is
the single inequality A_E^+ <= 1.3263305, with AT-1540 and s^+ as further conditions. Route F-a gives nothing at strain
3/2: its FLOAT far value 1.308 exceeds Gbar.

### 2.3 What the far section does not give

- No certified band upper: neither A_low^+(8 pi) (row C2) nor A_E^+(a_W).
- No far closure at strain 3/2 by route F-a.
- No inverse, near, invariant-ball or existence statement: every far row is an input of O3, not a part of it.

## 3. Answers to the theory auditor on Theorem CS-B

### 3.1 AT-1539 (REFUTED: nearest conversion of an arbitrary arb upper is outward)

the second theory agent agrees with the verdict and does not use that claim. AT-1539 records that the author supplied a correction
whose numerical effect still needed review. That effect (the second theory agent's notes 20:19Z, check run 20:18:36Z):
- Defect: two stored values of T2_FAR_CS_v02 were nearest conversions of arb uppers: the cell totals K^+ of
  code/c1/k_cells.py (cell_K) and bound_upper of code/c1/k_tail.py. Every other conversion of the CS-B chain is
  directed (box bounds, the g integral and the rho >= RMAX part in k_cells.py; D_s^+ in code/c1/ds_upper.py through
  c1_sc.fup).
- Check: code/c1/cs_round_check.py replaces each stored K^+ by K^+ (1 + 2^-52) (for a normal binary64 X > 0,
  fl(X) >= X (1 - 2^-53), so X <= fl(X) (1 + 2^-52); the smallest stored K^+ is 8.6e-4, so no subnormal occurs) and
  forms in arb the directed upper of (1/(4 pi)) (sum_s c_s (D_s^+)^2)^(1/2) (K^+ (1 + 2^-52))^(1/2) for every cell; it
  recomputes Lemma KT at T = 200 with the stored c and rounds its arb upper upward.
- Effect (runs/cs_round_check_2018.json): 90 of the 280 stored cell bounds lie one unit in the last place below the
  inflated upper; the cell [15.75, 16] that sets S^+ is not among them; the largest inflated cell upper equals the
  stored S^+ = 0.059699233948103884 = 8603566328415511/144115188075855872. The directed tail upper is
  0.024397461684268512 (stored 0.02439746168426851). So S^+, the exact comparison SC^+ + S^+ <= Gbar and the rooms of
  CS-B item 4 are unchanged; the certified per-cell uppers are those of runs/cs_round_check_2018.json.
- Replay, from research/h4/far009/ (under one second):
  python3 code/c1/cs_round_check.py runs/k_cells_1941.json runs/k_tail_2000.json runs/ds_upper_1926.json <out.json>
- Code written after 20:19Z (code/c1/ds_window.py, code/c1/ds_window_v2.py) converts every stored upper with fup,
  which steps up by nextafter until the binary64 value is >= the arb upper.

### 3.2 AT-1540 (OPEN: numerical application of CS-B)

the theory auditor's proof file (research/far_cs_b_analytic_audit/PROOF.md, section "Numerical implementation obligations and
scope") lists what the numerical claim requires. Where each item is met in the second theory agent's records (all CLAIMED; the
independent check is the theory auditor's):
1. Exact full source: the engine code/c1/c1_sc.py reads only the two exact inputs of section 2 (hashes there); a_f
   is the complete far piece (all angular modes). B1 uses it through code/c1/tail_deriv.py.
2. Whole-plane derivative bounds: D_m^2 = E_I + E_II + E_III over r <= e^-4, e^-4 <= r <= e^16 and r >= e^16
   (T2_FAR_CS_v02 item 2). E_II comes from two cell records that cover y = log r in [-4, 16] without gaps or overlaps:
   runs/tail_deriv_1905.jsonl (new) and runs/tail_deriv_1557.jsonl (its code CONFIRMED in AT1336 to AT1342).
3. Containing box arithmetic: T2_FAR_CS_v02 item 3(c) (binary64 intervals moved outward by nextafter after every
   operation; monotone transcendental functions in arb at the interval ends, rounded outward). Lemma KP (CONFIRMED
   within AT-1536 to AT-1538) removes the cancellations.
4. Full partitions: the 280 cells of runs/k_cells_1941.json are contiguous from |xi| = 0 to 200 (ALLOWGAP false;
   rechecked from the JSON at 23:27Z: t1 of each cell equals t0 of the next, first t0 = 0, last t1 = 200); in each
   cell psi covers [0, pi] (the integrand is even in psi, item 3(a)), rho covers [0, RMAX] with RMAX = 1e6 by boxes,
   and rho >= RMAX is bounded by the radial tail formula that the theory auditor checked ("Finite-frequency radial tail"); the
   range |xi| >= 200 is Lemma KT (runs/k_tail_2000.json; the analytic lemma is CONFIRMED within AT-1536 to AT-1538).
5. Outward conversions: section 3.1.
6. Positive coefficient weights: in runs/k_cells_1941.json the smallest c_1, c_2, c_3, c_4 over the 280 cells is 1e-9
   and the smallest c_5 is 0.14999 (rechecked at 23:27Z), so c_5 > 0 and c_1 + c_2 > 0 on every cell; Lemma KT uses
   c = (1e-12, 1, 1e-12, 1e-12, 0.7761365363491166). The c_s are fixed per |xi|-cell, so they depend on |xi| only
   (the radial case of AT-1479 and AT-1481; T2_FAR_CSW_v02 E3).
7. Replay: commands in T2_FAR_CS_v02 item 7 (recorded run times on one core: tail_deriv.py 1163.5 s and ds_upper.py
   4.4 s for B1, k_cells.py 1129 s for B2, k_tail.py 1.6 s, cs_assembly.py under 1 s), and the 7-second partial replay
   of B2 of notes 20:12Z, which reproduced the stored boxes bit for bit.
The hashes of T2_FAR_CS_v02 item 7 were rechecked at 23:27Z; every file is unchanged.

## 4. Other X7 item 5(d) entries

- Lemma QID and Proposition ZO for the theory auditor: notes/T2_QIDZO_v01.md (section 1.3).
- Radial-coefficient qualification of AT-1481: notes/T2_FAR_CSW_v02.md item E3 and notes/T2_FAR_AE_PLAN_v01.md
  section 0.
- Windowed bound SC(a_W) and the singleton fix of sinf_sup (AT-1597, AT-1598): notes/T2_FAR_CSW_v02.md items E1, E2.
- Priced plan for a certified A_E^+(a_W) at Rw = Ww = 200: notes/T2_FAR_AE_PLAN_v01.md (for X8).
- The qualifications of numerical audit exchange v370 on the priced C2 plan: kept in section 2.1. No C2 code was written and no
  NL6 cell was rerun.

## 5. Files (SHA256)

- notes/T2_O2O3_FINAL_v02.md 19c9bdfc9ca6ba062cb669029ea45a940a1476f4b4fb47b386bc53cefb08bf6e
- notes/T2_O2O3_FINAL_v01.md 7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1
- notes/T2_QIDZO_v01.md cc67aa515de67fcc04496bcd1ed1f5529816a43bb957208c6a0cb5e2e7130c9e
- notes/T2_FAR_AE_PLAN_v01.md b1268b6343a31d76033fae1401146b91b6602d0951c659d098b8e6179f69673f
- notes/T2_FAR_CSW_v02.md 45542a92c4fa2f845a11466ae1a981de6ba579b39aecae5f816659f650aae8e1
- notes/T2_FAR_CSW_v01.md 45e8788e72aceaa76bbe62b1b7b6406c1a526c439c15e5279d7098b60bc961bb
- notes/T2_FAR_CS_v02.md aa1f9eda052ae1479dd5dc4f0325bc49110d080d20a55422a19e2cfde11dcaa6
- notes/T2_FAR_C2_PLAN_v01.md d9604af8f6abb707745cf37e42328a2403d919b6c08a7443b3703237c874ec9e
- notes/T2_FAR_v02.md 9cdc9c6850e306e931aa86e998d0fd6f588553d287a853956534a4882c36c671
- code/c1/cs_round_check.py 391dc3d05e36004a55fe21e50d1b982dbd16fd4d0f4302777acf5ca1cb01a733
- runs/cs_round_check_2018.json 73782ae75b5151270b0f42acd9f251c7e9892cafd58d2af2b03b36627174fefa
- runs/k_cells_1941.json 38735c097f0367c0e287be0eb015ece869056c8487d7bedb964490567cc93d8b
- runs/k_tail_2000.json 9d17f52c5f98afffa2d46092b8561a78d035df021b90ce0fc1978c3e6c54bda6
- runs/ds_upper_1926.json 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5
