# T2_PART7_v02: the second theory agent's Part VII entry (THEORY_NEW_RESULTS: O2, O3 and the far section), second version: it carries AT-1759 to AT-1762, refreshes the status labels and the regional strain coverage at ledger v09, records the A_E^+ implementation, and gives the second theory agent's answers on the CS-B numerical application (AT-1540) and on s^+ (AT-1599)

Agent the second theory agent, written 2026-11-04 from 01:15Z; frozen 2026-11-04T01:20:23Z. Recipients: the first theory agent (publisher of THEORY_NEW_RESULTS
and of theory_vNN), the coordinator (X8 item 5(d); input for X9, freeze 04:15Z), the theory auditor (audit). Paths: notes/ relative to
the agent directory; code/, runs/, data/ and inputs013/ relative to research/h4/far009/ of agent the second theory agent. Status labels:
CONFIRMED (the theory auditor verdict cited), CLAIMED (proved by the second theory agent, audit requested), FLOAT (sampled value or code test, not a
bound), HEURISTIC, OPEN. Inputs read to about 01:15Z: ledger v09 (the coordinator, 00:37:46Z), the theory audit exchange through
audit_v535, the coordinator's notes through 01:08Z.

This version supersedes notes/T2_PART7_v01.md (frozen 2026-11-03T23:29:19Z, SHA256
7e9fb6b08a98fdebd8967e90a1e6fcbc96854404a1c71b33c101788e10aae182), which stays unchanged as a historical record. It
indexes results and restates no proof. The final Part VII far section is due by 2026-11-04T15:35Z (X8); it will be a
later version of this note. The changes against v01 are listed in section 6.

## 0. Answer

No complete existence theorem follows from the second theory agent's results, and none is claimed. The first unresolved condition is
O3. At the chain center C2-N1-013 the explicit route needs a certified weak-energy constant C^opt(b0) (ledger item G3:
near and far charges), a certified background rate (item B) and the actual-generator hypotheses (item G2). On the far
side neither far route is closed: Proposition F needs row C2, which stays OPEN (no C2 code, no NL6 rerun; X8), and
route F-a needs a certified A_E^+(a_W) (implementation running, section 2.2), the CS-B numerical application
(AT-1540, OPEN) and a certified global strain bound s^+ (item B, OPEN; section 2.3).

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

### 1.2 the theory auditor's scope verdicts

On notes/T2_O2O3_FINAL_v01.md and v02:

| id | audit | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|---|
| AT-1576 | audit_v480 | the consolidated qualitative O2/O3 statements remain valid with their cited proof restrictions; numerical constants and candidate closure remain open | CONFIRMED |
| AT-1577 | audit_v480 | the fixed 53/100 scalar proof justifies the explicit route for all 2 < q < 3 (counterexample q = 5/2, t = 2) | REFUTED; only q = 21/10 is admitted |
| AT-1578 | audit_v480 | the new N = 0.006 fractions are below 8.4 and 7.1 percent of b'M in the two specified cells | CONFIRMED |
| AT-1579 | audit_v480 | the full explicit energy theorem extends to arbitrary q, or these results give actual source013 closure | OPEN |
| AT-1592 | audit_v485 | v02 correctly restricts the explicit results to q = 21/10; the original hypotheses remain mandatory | CONFIRMED |
| AT-1593 | audit_v485 | the corrected scope or the newly appended far route closes O3 at source013 | OPEN; both far routes remain conditional |

On notes/T2_PART7_v01.md (the theory auditor research/o2o3_partvii_scope_audit, audit_v534, 00:28:29Z):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT-1759 | the Part VII index preserves the audited O2/O3 and pricing scope | CONFIRMED; "historical labels and coverage should be refreshed in a new version" (done here, sections 1.3 and 2.2) |
| AT-1760 | the C2 allowance and the rounded A_E sufficient threshold have the claimed exact arithmetic | CONFIRMED (14 exact checks); 1.3263305 is sufficient, not necessary |
| AT-1761 | q(c - 137/125) equals the decimal 1.5000703414199960 | REFUTED: the difference is -2769660487/137438953472000000000000000, below 1e-16 in absolute value; corrected in section 2.2 |
| AT-1762 | the Part VII index closes AT-1540, either band row or O3 | OPEN |

Reading for Part VII: Theorems A and B and the results of the v02 status table hold as stated there, with the
explicit formulas at q = 21/10 only; no closure of O3 at 013 or at any other center follows (AT-1579, AT-1593,
AT-1762).

### 1.3 Status changes since T2_O2O3_FINAL_v02 was frozen (v02 is not edited)

- Corollary CS-W and Proposition DW (the S input of route F-a): CONFIRMED conditionally (AT-1594 to AT-1596),
  notes/T2_FAR_CSW_v02.md; an unconditional numerical Schur, far or existence certificate is not supplied (AT-1599,
  OPEN).
- Lemma SC-W (the Hessian input of route F-a for the window Rw = Ww = 200): CONFIRMED (AT-1366, AT-1367; its
  application to this window AT-1598).
- Theorem CS-B: analytic parts CONFIRMED (AT-1536 to AT-1538); the rounding repair of the stored kernel uppers
  CONFIRMED as conditional finite arithmetic (AT-1731, AT-1732; audit_v525); the numerical application OPEN pending
  the complete replays (AT-1540, AT-1733, AT-1762). The second theory agent's answer: section 3.2.
- Lemma QID and Proposition ZO (notes/T2_QIDZO_v01.md, frozen 2026-11-03T23:24:25Z, SHA256
  cc67aa515de67fcc04496bcd1ed1f5529816a43bb957208c6a0cb5e2e7130c9e): CONFIRMED (AT-1754 to AT-1757; audit_v533,
  00:25:55Z), with the moment and energy scaling and the zeroth-order oscillation bound; they exclude only a
  universal vanishing bound of the band constant in SC, positive moments and energies of order above 1 (D1 is
  invariant and not excluded), and they give no candidate-specific band upper and no impossibility of the remaining
  C2 approaches (AT-1758, OPEN). v01 listed them as CLAIMED.
- The A_E^+ plan: notes/T2_FAR_AE_PLAN_v02.md (frozen 2026-11-03T23:45:01Z, SHA256
  d0eab8bf394a5f6b23f7c98c2ba9f829168f306fa425ecf9252704280fcfea9b) supersedes T2_FAR_AE_PLAN_v01 (frozen 23:17:11Z).
  Audits of v01 (audit_v517): Lemma SYM CONFIRMED (AT-1697); Proposition AE-CS CONFIRMED conditionally, "finiteness
  and the continuum essential supremum remain explicit premises" (AT-1698); support, radiality and factor 4
  CONFIRMED (AT-1699); the cancellation identity and its sign CONFIRMED (AT-1700); reuse of the r_B zero shortcut
  REFUTED (AT-1701); the count of about 130 cells REFUTED, 202 cells (AT-1702); no certified A_E (AT-1703, OPEN).
  Audits of v02 (audit_v524): Lemma ENC CONFIRMED as an analytic containing estimate (AT-1726 to AT-1728); the
  same-configuration FLOAT comparison CONFIRMED as provenance and sampled arithmetic only (AT-1729); no numerical
  A_E certificate (AT-1730, OPEN).
- New: the implementation, notes/T2_FAR_AE_v01.md (frozen 2026-11-04T01:19:42Z, SHA256 c36f571937a15bd98f4b5be2d93cc44d7222d7cb914737bb1fff7c337d67d7f3; CLAIMED, the theory auditor's reading requested). Its run is in
  progress (section 2.2).
- Row C2: still OPEN.

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
| C3, C4 | S^+ = 0.059699233948103884 >= S_h^B(a_f; 2 pi, 8 pi, h), h = <min(abs(xi), 63/10)>^-1 (route B, Theorem CS-B); SC^+ + S^+ <= Gbar exactly | analytic parts CONFIRMED (AT-1536 to AT-1538); rounding repair CONFIRMED conditionally (AT-1731, AT-1732); numerical application OPEN (AT-1540, AT-1733) | T2_FAR_CS_v02; notes 20:19Z |
| C2 | A_low^+(8 pi) >= A_low(8 pi) with A_low^+(8 pi) <= Gbar - S^+ = 426560137443922093/720575940379279360 (> 0.591971; exact, AT-1760) | OPEN: no priced route fits before the stop (HEURISTIC; qualifications below); FLOAT band value 0.3848 (the second numerics agent); QID/ZO exclude only a universal vanishing bound (AT-1754 to AT-1758) | T2_FAR_C2_PLAN_v01; T2_QIDZO_v01 |

Row C2 stays OPEN unless an auditor confirms a certified A_low^+; X8 keeps it OPEN with no C2 code and no NL6 rerun.
T2_FAR_C2_PLAN_v01 prices the routes it considers (HEURISTIC): a certified eigenproblem on the window support would
need an order of 1.6e6 or more in the parity class, against a dense capacity of about 5e4 on one core in 32 GB.
The numerical auditor's audit of that plan (exchange v370; CONFIRMED for the exact conditional budget and the values of the assumed
pricing formulas) adds two qualifications, kept here: (i) the parity count is a planning estimate, not a proved
minimum dimension of every possible certificate, so the evidence supports leaving C2 OPEN and not launching the dense
routes but does not prove that every route is impossible before the stop, and the FLOAT radius-100 tail and window
charges do not prove a mathematical exclusion of that radius; (ii) one 65000 by 65000 binary64 matrix alone needs
33800000000 bytes (above 32 decimal GB, below 32 GiB) and order 50000 needs 20 decimal GB for one matrix, before
factors, copies or interval storage, so a practical capacity needs a full allocation plan. Proposition ZO (CONFIRMED,
AT-1755 to AT-1757) shows that no bound of A_low by SC, Fourier moments M_s (s > 0) and energies D_s (s > 1) alone,
vanishing with them, can hold, so the tail cannot be charged through its derivatives only; the theory auditor's notes that this
excludes no use of D1 or of other information (AT-1757) and is not a general computational impossibility (AT-1758).

### 2.2 Route F-a (strain s^+ = 137/125, window Rw = Ww = 200)

AT-911 (CONFIRMED): A_*(a_W + a_t) <= max(SC^+, A_E^+) + S^+ + OMF(a_t), with a_W = a_f (1 - Sinf((r - Rw)/Ww)) and
a_t = a_f - a_W. The target is q (c - s^+). At s^+ = 137/125 it is exactly 4222322644155391629/2814749767106560000,
approximately 1.5000703414199960 (AT-1761; v01 wrote "equal to").

| input | value | status | where |
|---|---|---|---|
| SC^+(a_W) | 4194197216881219/9007199254740992 = 0.46564943200002806 | CONFIRMED (AT-1366, AT-1367, AT-1598) | Lemma SC-W, notes 17:15Z; T2_FAR_CSW_v02 E1 |
| S_W^+ >= S_h^B(a_W) | 0.05970055144902641 | CONFIRMED conditionally (AT-1594 to AT-1596), on AT-1540 and the B1 records D_s^+; AT-1599 OPEN | T2_FAR_CSW_v02 |
| OMF^+(a_t) | 0.11403919054571054 | CONFIRMED (AT-1336 to AT-1338) | notes 16:19Z |
| A_E^+(a_W) | needed: A_E^+ <= 1.3263305 (sufficient, not necessary, AT-1760); exact threshold for the rounded budget 0.17373975: 93332218082643491781/70368744177664000000, about 1.32633059142 | implementation CLAIMED, run in progress: chunk 0:40 (abs(xi) in [0, 2]) complete with 75 sub-cell bounds, max 1.3135985491329587; chunks 40:80, 80:126, 126:202 running, end about 02:00Z to 03:30Z (HEURISTIC); every accepted cell bound is about 1.3136 by the stop rule, not by the size of the bracket (T2_FAR_AE_v01 sections 5 and 7); Lemma SYM, AE-CS, ENC CONFIRMED (conditionally for AE-CS) as in section 1.3; FLOAT band value 1.1342736; FLOAT Cauchy-Schwarz value 1.18672 (AT-1729) | T2_FAR_AE_PLAN_v02; T2_FAR_AE_v01 |
| s^+ | 137/125 | OPEN (item B; AT-1599). At ledger v09, ||Sym Du||_op <= 137/125 is certified by both auditors only regionally: roots 0 to 31 (r^2 <= 1/3), root 34 (17/47 <= r^2 <= 35/93), root 98 (49/15 <= r^2 <= 99/29; AT-1674 to AT-1676, and the original replay AT-1659, AT-1660) and root 102 (51/13 <= r^2 <= 103/25; AT-1763 to AT-1765); root 100 (25/7 <= r^2 <= 101/27) passes in the numerical auditor's recount conditional on the stored intervals, the theory auditor's review pending; nineteen owner roots from 98 to 122 ended at the 64-leaf cap with all joint flags false (failed sufficient tests, not counterexamples) | ledger v09 row B; section 2.3 |

Since S_W^+ + OMF^+ < 0.17373975 and SC^+ < 1.3263305 < q (c - 137/125) - 0.17373975 (AT-1760), the far condition of
route F-a at s^+ = 137/125 is implied by the single inequality A_E^+ <= 1.3263305, with AT-1540 and s^+ as further
conditions. Route F-a gives nothing at strain 3/2: its FLOAT far value 1.308 exceeds Gbar.

### 2.3 Answer on s^+ (AT-1599; X8 item 5(d))

1. What route F-a needs. A certified number s^+ with ||Sym Du(x)||_op <= s^+ for the background u at every x of the
   plane (ledger item B; T2_FAR_v02 C6: for a far upper A, the admissibility A <= G needs a certified global strain
   bound at most c - A/q), and the far inequality max(SC^+, A_E^+) + S_W^+ + OMF^+ <= q (c - s^+). For a certified
   A_E^+ this is
       s^+ <= s_max(A_E^+) := c - (max(SC^+, A_E^+) + S_W^+ + OMF^+)/q,
   an exact rational once A_E^+ is a binary64 number. Values (exact rationals, rounded down here; the inputs SC^+,
   S_W^+, OMF^+ as in section 2.2):
   - at A = 1.3263305: s_max >= 1.096000047345 > 137/125 (this is AT-1760 read for s^+);
   - at A = 1.3163305 (the TARGET of the A_E^+ run; every sub-cell bound at or below it gives A_E^+ <= TARGET):
     s_max = 1665683415424191637/1513209474796486656 >= 1.100761952107.
   So if the run ends with A_E^+ <= 1.3163305, route F-a tolerates any certified global strain bound up to about
   1.10076, not only 137/125 = 1.096. For the change from 3/2 to 137/125, the theory auditor CONFIRMS that the strain enters the
   source013 conditions 3 to 8 only through G = q (c - s) and the strain predicate itself, with beta_* >= 3/5,
   g_* <= 1/4, the near inputs, the transfer theorem, the KB test and the C0 allowance D unchanged (AT-935, AT-936;
   ledger v09, row "strain target dependence"). The second theory agent reads the same dependence for every s in [137/125, s_max]; that
   reading is not audited, and a certified cover at a value other than 137/125 would need its own review.
2. What the second theory agent supplies and does not. The strain bound is a property of the background (item B), certified root by
   root by the numerical auditor and the theory auditor; it is not a the second theory agent computation, and no far result of the second theory agent bounds it. The regional
   certificates of section 2.2 do not suffice: route F-a needs the bound on the whole plane, including the
   exterior beyond the last root, with the containing exterior estimate.
3. What closes the s^+ row of route F-a: a certified s_* <= 137/125 (or <= s_max(A_E^+)) on all 128 roots and the
   exterior, with both auditors' reviews, plus the containment of the stored intervals that root 100's recount still
   assumes.

### 2.4 What the far section does not give

- No certified band upper yet: neither A_low^+(8 pi) (row C2, OPEN) nor A_E^+(a_W) (run in progress; its record is
  CLAIMED and unread).
- No far closure at strain 3/2 by route F-a.
- No inverse, near, invariant-ball or existence statement: every far row is an input of O3, not a part of it.

## 3. Answers to the theory auditor on Theorem CS-B

### 3.1 AT-1539 (REFUTED: nearest conversion of an arbitrary arb upper is outward)

the second theory agent agrees with the verdict and does not use that claim. Its correction (notes 20:19Z; T2_PART7_v01 section 3.1) is
CONFIRMED as conditional finite arithmetic (AT-1731, AT-1732): 90 one-step cell corrections, maximum
8603566328415511/144115188075855872 < 3/50, directed tail 0.024397461684268512. The certified per-cell uppers are
those of runs/cs_round_check_2018.json. The A_E^+ code (code/c1/ae_cells.py) converts every stored upper outward
(T2_FAR_AE_v01 section 4).

### 3.2 AT-1540 (OPEN: numerical application of CS-B; AT-1733: "pending the complete replays")

the second theory agent's answer on the CS-B numerical application:
1. Where the second theory agent's records meet each obligation of the theory auditor's list (research/far_cs_b_analytic_audit/PROOF.md, "Numerical
   implementation obligations and scope"): T2_PART7_v01 section 3.2, items 1 to 7, unchanged; all CLAIMED. AT-1762
   records that these owner descriptions do not close AT-1540. The second theory agent agrees: what is missing is the theory auditor's independent
   replay, not a further owner statement.
2. The replay. From research/h4/far009/ of agent the second theory agent, after copying (the agent is read-only for other agents), on one
   core, with the recorded run times (T2_FAR_CS_v02 item 7):
   - B1: python3 code/c1/tail_deriv.py -4 3.75 0.015625 34 8 5 256 runs/tail_deriv_1905.jsonl (1163.5 s), then
     python3 code/c1/ds_upper.py -4 256 runs/ds_upper_1926.json runs/tail_deriv_1905.jsonl runs/tail_deriv_1557.jsonl
     (4.4 s); runs/tail_deriv_1557.jsonl is the earlier record whose code is CONFIRMED (AT1336 to AT1342);
   - B2: EPS=0.3 NMAX=30000 TARGET=0.06 python3 code/c1/k_cells.py runs/ds_upper_1926.json
     0:30:120,30:60:60,60:120:60,120:200:40 runs/k_cells_1941.json (1129 s);
   - python3 code/c1/k_tail.py runs/ds_upper_1926.json 200 runs/k_tail_2000.json (1.6 s);
   - python3 code/c1/cs_assembly.py runs/k_cells_1941.json runs/k_tail_2000.json runs/cs_assembly_2001.json (< 1 s);
   - the rounding check: python3 code/c1/cs_round_check.py runs/k_cells_1941.json runs/k_tail_2000.json
     runs/ds_upper_1926.json <out.json> (< 1 s);
   - for route F-a also the window record: python3 code/c1/ds_window_v2.py 200 200 runs/ds_upper_1926.json
     <out.json> runs/tail_deriv_1905.jsonl runs/tail_deriv_1557.jsonl (0.4 s; its scalar output is CONFIRMED,
     AT-1596).
   About 38 minutes of computation in all. A partial replay is also possible: k_cells.py on a cell range (the
   7-second partial replay of notes 20:12Z reproduced the stored boxes bit for bit).
3. Core 41. X8 item 4(a) lets the CS-B replay use core 41 only when the second theory agent has no job there. The second theory agent's A_E^+ run holds
   core 41 from 01:05:20Z; it ends about 02:00Z to 03:30Z (HEURISTIC; T2_FAR_AE_v01 section 7), and core 41 is
   free for the theory auditor's replay from then. The second theory agent will start no further long core 41 job before the X9 freeze (only the
   assembly and record checks of the A_E^+ run, seconds each) and will post the end of the run in notes.

## 4. Other X8 item 5(d) entries

- The A_E^+ implementation: notes/T2_FAR_AE_v01.md, the first frozen piece for the theory auditor's reading, with the measured
  price; the cell table, the assembly and A_E^+ follow in T2_FAR_AE_v02 when the run ends.
- Row C2: OPEN, no C2 code, no NL6 rerun.

## 5. Files (SHA256)

- notes/T2_PART7_v01.md 7e9fb6b08a98fdebd8967e90a1e6fcbc96854404a1c71b33c101788e10aae182 (superseded, unchanged)
- notes/T2_FAR_AE_v01.md c36f571937a15bd98f4b5be2d93cc44d7222d7cb914737bb1fff7c337d67d7f3
- notes/T2_FAR_AE_PLAN_v02.md d0eab8bf394a5f6b23f7c98c2ba9f829168f306fa425ecf9252704280fcfea9b
- notes/T2_FAR_AE_PLAN_v01.md b1268b6343a31d76033fae1401146b91b6602d0951c659d098b8e6179f69673f
- notes/T2_O2O3_FINAL_v02.md 19c9bdfc9ca6ba062cb669029ea45a940a1476f4b4fb47b386bc53cefb08bf6e
- notes/T2_O2O3_FINAL_v01.md 7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1
- notes/T2_QIDZO_v01.md cc67aa515de67fcc04496bcd1ed1f5529816a43bb957208c6a0cb5e2e7130c9e
- notes/T2_FAR_CSW_v02.md 45542a92c4fa2f845a11466ae1a981de6ba579b39aecae5f816659f650aae8e1
- notes/T2_FAR_CS_v02.md aa1f9eda052ae1479dd5dc4f0325bc49110d080d20a55422a19e2cfde11dcaa6
- notes/T2_FAR_C2_PLAN_v01.md d9604af8f6abb707745cf37e42328a2403d919b6c08a7443b3703237c874ec9e
- notes/T2_FAR_v02.md 9cdc9c6850e306e931aa86e998d0fd6f588553d287a853956534a4882c36c671
- code/c1/cs_round_check.py 391dc3d05e36004a55fe21e50d1b982dbd16fd4d0f4302777acf5ca1cb01a733
- runs/cs_round_check_2018.json 73782ae75b5151270b0f42acd9f251c7e9892cafd58d2af2b03b36627174fefa
- runs/k_cells_1941.json 38735c097f0367c0e287be0eb015ece869056c8487d7bedb964490567cc93d8b
- runs/k_tail_2000.json 9d17f52c5f98afffa2d46092b8561a78d035df021b90ce0fc1978c3e6c54bda6
- runs/ds_upper_1926.json 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5

## 6. Changes against T2_PART7_v01

- Section 1.2: the verdicts AT-1759 to AT-1762 on v01.
- Section 1.3: Lemma QID and Proposition ZO now CONFIRMED (AT-1754 to AT-1757; AT-1758 OPEN); the AE plan v02 and
  its audits (AT-1697 to AT-1703, AT-1726 to AT-1730) replace the v01 entry for plan v01; the CS-B rounding repair
  CONFIRMED conditionally (AT-1731, AT-1732; AT-1733 OPEN); the implementation T2_FAR_AE_v01.
- Section 2.2: "approximately" and the exact rational for q (c - 137/125) (AT-1761); the A_E^+ row with the
  implementation; the s^+ row with the regional coverage at ledger v09 (roots 0 to 31, 34, 98 and 102).
- Sections 2.3 and 3.2: new answers on s^+ (AT-1599) and on AT-1540 (X8 item 5(d)).
