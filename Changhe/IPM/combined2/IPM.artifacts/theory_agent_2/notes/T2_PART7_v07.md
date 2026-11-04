# T2_PART7_v07: the second theory agent's Part VII entry (THEORY_NEW_RESULTS: O2, O3 and the far section), seventh version: A_E^+ = 1.3135985491329587, the CS-B numerical application and the window stage CONFIRMED (AT1891, AT1921, AT1922, AT1928, AT1929) with the re-rounded S^+ and S_W^+, so that every far input of route F-a is certified and its far inequality at s^+ = 137/125 holds, conditional on a whole-plane strain bound at most s_max (zero far slack at equality; AT2043, AT2044), the rerun price and decision, and the regional strain coverage of ledger v11 with the exact 87-index union of both auditors (the numerical auditor AN637; the theory auditor AT2240, AT2241) read to 07:12Z, whose only gap for the strain target is 57/71 < r^2 < 49/15, with the premise of the progressive assembly restored (AT2260)

Agent the second theory agent, written 2026-11-04 from 07:11Z on the text of v06; frozen 2026-11-04T07:14:05Z. Recipients: the first theory agent (publisher of
THEORY_NEW_RESULTS and of theory_vNN), the coordinator (final report; X8 and X9 item 5(d)), the theory auditor (audit). Paths: notes/ and
scratch/ relative to the agent directory; code/, runs/, data/ and inputs013/ relative to research/h4/far009/ of agent the second theory agent.
Status labels: CONFIRMED and REFUTED (the theory auditor verdicts cited), CLAIMED (proved or computed by the second theory agent, audit requested),
FLOAT (sampled value or code test, not a bound), HEURISTIC, OPEN. Inputs read to about 07:12Z: ledger v11 (the coordinator,
06:17:33Z, SHA256 8059094197cb01e4997ba778727b2ec0d8177e492052388c4da93e64dc048891), the coordinator's notes through 07:08Z,
the theory audit exchange through audit_v693 (07:09:13Z), the numerical audit exchange through v646 (07:10:22Z), the first theory agent's notes through note 82
(07:08Z; THEORY_NEW_RESULTS version 20).

This version supersedes notes/T2_PART7_v06.md (frozen 2026-11-04T06:50:12Z, SHA256
ec4c737ce9fd7c6d9b24673e63a69959ef84ba164205a2d81d3e441baaa210d4), which stays unchanged as a historical record, as do
v01 to v05. It indexes results and restates no proof. It is the second theory agent's final Part VII far section (X8, X9 item 5(d): due
by 2026-11-04T15:35Z); a later version follows before that deadline only if a verdict changes this entry or both
auditors certify the three background bounds of section 2.2 on the whole plane. A narrower gap alone does not lead to
a new version. The changes against v06 are listed in section 6; those of v06 against v05 are in v06 section 6.

Decimal conventions. A decimal written after "<=" or ">=" is an outward rounding of the exact value. A decimal
written after "=" next to a dyadic rational, or in parentheses after one, is the shortest decimal name of that
binary64 number; it differs from the exact value by less than 1e-17 and is not itself a bound. So the decimals
0.059699233948103884 (old S^+) and 0.05970055144902641 (old S_W^+) of earlier the second theory agent's notes lie below their exact
values by less than 1e-18 and are not decimal upper bounds (notes 02:48Z item 3). For every bound this version gives
the exact rational.

## 0. Answer

No complete existence theorem follows from the second theory agent's results, and none is claimed. The first unresolved condition is
O3. At the chain center C2-N1-013 the explicit route needs a certified weak-energy constant C^opt(b0) (ledger item G3:
near and far charges), a certified background rate (item B) and the actual-generator hypotheses (item G2).

On the far side neither far route is closed:
- Proposition F needs row C2, which stays OPEN (no C2 code; X8).
- Route F-a: every far input is now certified by the theory auditor. These are SC^+ (AT-1366, AT-1367, AT-1598), OMF^+ (AT-1336 to
  AT-1338), the complete A_E^+(a_W) = 1.3135985491329587 (AT1891), the CS-B application for a_f with the re-rounded
  S^+ = 1075445791051939/18014398509481984 (AT1921, AT1922), and the window stage: the five D_W uppers (AT1928) and
  S_W^+ = 537734762519297/9007199254740992 (AT1929). The numerical auditor checks the CS-B assembly and the window transfer
  independently (numerical audit exchange v529, v532). The far inequality at s^+ = 137/125 holds in exact rationals with margin
  71675071190082633/5629499534213120000 >= 0.012732050292300 (AT1929; v532). The strain tolerance is s_max =
  4963249980622857/4503599627370496 >= 1.102062881091 (the theory auditor audit v589; numerical audit exchange v532; the second theory agent's transfer). The far
  absorption of Proposition FG holds for every certified strain upper s <= s_max, with zero far slack at s = s_max; a
  strictly positive far margin holds exactly when s < s_max (AT2044 CONFIRMED, AT2043 REFUTED, audit v625, which
  withdraws the strict reading of AT2038; section 2.3). The theory auditor states this conclusion as conditional on a matching
  whole-plane strain bound and the analytic source hypotheses (audit v589). Route F-a still needs a certified
  whole-plane strain bound of at most 1.102062881091 (item B, OPEN; one open r^2 gap, 57/71 < r^2 < 49/15, of the
  regional coverage remains at 07:12Z, section 2.2; section 2.3) and the near side; the far closure and everything
  after it are OPEN (AT1894, AT1924, AT1931).

## 1. O2 and O3: notes/T2_O2O3_FINAL_v02.md

### 1.1 The entry

notes/T2_O2O3_FINAL_v02.md, frozen 2026-11-03T21:23:48Z, SHA256
19c9bdfc9ca6ba062cb669029ea45a940a1476f4b4fb47b386bc53cefb08bf6e. It supersedes notes/T2_O2O3_FINAL_v01.md (frozen
21:08:46Z, SHA256 7130dcc8fdc3c5412305773e66efef1973c2ed7decf5246f0742e46fec8d88e1; errata in v02 section 8).
Contents:
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
| AT-1759 | the Part VII index preserves the audited O2/O3 and pricing scope | CONFIRMED; "historical labels and coverage should be refreshed in a new version" (done in v02) |
| AT-1760 | the C2 allowance and the rounded A_E sufficient threshold have the claimed exact arithmetic | CONFIRMED (14 exact checks); 1.3263305 is sufficient, not necessary |
| AT-1761 | q(c - 137/125) equals the decimal 1.5000703414199960 | REFUTED: the difference is -2769660487/137438953472000000000000000, below 1e-16 in absolute value; corrected in v02 section 2.2 |
| AT-1762 | the Part VII index closes AT-1540, either band row or O3 | OPEN |

On notes/T2_PART7_v02.md (the theory auditor research/strain_continuous_target_audit, audit_v562, 01:31:25Z):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT-1853 | the strain target can vary continuously in [137/125, s_max(A_E)] while the other fixed source013 dependency formulas remain unchanged | CONFIRMED as a conditional implication; every new strain premise needs a separate whole-plane certificate |
| AT-1854 | the two printed s_max lower bounds and the stated exact fraction have the claimed arithmetic | CONFIRMED (116 exact checks); the fraction holds for the binary64 literal 1.3163305 = 5928225549296419/4503599627370496 |
| AT-1855 | T2_PART7_v02 preserves the reviewed qualitative O2/O3 and conditional far scope | CONFIRMED; final coverage needs a fresh snapshot, and FLOAT diagnostics remain noncertifying |
| AT-1856 | the larger scalar strain allowance supplies actual far or invariant-ball closure | OPEN |

On notes/T2_PART7_v03.md and notes/T2_FAR_AE_PILOT_v01.md (the theory auditor research/t2_part7_v03_pilot_audit, audit_v603,
03:23:44Z; 280 finite checks):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT1973 | T2_PART7_v03 retains the reviewed O2/O3 scope as a historical index | CONFIRMED; the explicit formulas stay at q = 21/10 and no generator, background or near premise is removed |
| AT1974 | the refreshed far margin and strain tolerance have the claimed exact values | CONFIRMED: margin >= 0.012732050292300 and s_max >= 1.102062881091 with the re-rounded S_W^+; the older v03 fractions hold only with the historical S_W^+ |
| AT1975 | the bounded-depth stop rule guarantees that every accepted row lies below TARGET | REFUTED: at depth 5 the code accepts a row above TARGET (base cell 72 at TARGET 1.25, maximum 1.2536446583143115); corrected in section 2.2, section 2.3 item 4 and T2_FAR_AE_PILOT_v02; the complete A_E maximum and its cover are unaffected |
| AT1976 | the pilot summaries accurately describe their frozen finite records | CONFIRMED: all seven pilot summaries match, base cell 72 at TARGET 1.25 explicitly partial |
| AT1977 | the AT1842 exceptional-endpoint argument transfers to the unchanged 96-bit k_cells.box_R call | CONFIRMED; no monotonicity on a negative interval is asserted |
| AT1978 | the pilots supply a new global A_E bound, runtime guarantee, general 1.25 impossibility or O3 closure | OPEN |

On notes/T2_FAR_AE_PILOT_v02.md (the theory auditor research/t2_pilot_v02_wording_audit, audit_v610, 03:41:42Z; 73 checks):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT1999 | the revised pilot note correctly withdraws the TARGET upper-bound guarantee and preserves the finite observations | CONFIRMED; sections 1, 2 and 4 unchanged after whitespace normalization; exact depth-5 witness 2822956808019673/2251799813685248 > 5/4 |
| AT2000 | the two printed conditional strain allowances remain valid for either old or re-rounded S_W | CONFIRMED (four exact substitutions, A in {1.2974, 1.2536}); conditional on the assumed A values |
| AT2001 | the pilots or corrected wording establish a new continuum A bound, runtime guarantee or full closure | OPEN |

On notes/T2_PART7_v04.md (the theory auditor research/t2_part7_v04_audit, audit_v626, 04:20:00Z; 425 checks, all 28 listed file
references authenticated):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT2046 | T2_PART7_v04 preserves the reviewed O2/O3 scope and analytic assumptions | CONFIRMED; the explicit route stays at q = 21/10 and the numerical inputs remove no generator or near hypothesis |
| AT2047 | the refreshed exact far arithmetic and decimal conventions of T2_PART7_v04 are valid | CONFIRMED; absorption includes equality s = s_max, positive slack is strict |
| AT2048 | the numerical dependencies and both dated regional snapshots of T2_PART7_v04 match their accepted evidence | CONFIRMED; the five window uppers equal the A_E^+ inputs, the 48- and 51-index snapshots match, J_7 separate |
| AT2049 | the fourth entry correctly states the bounded-depth pilot rule and historical measured observations | CONFIRMED; depth 5 may accept above TARGET, the complete maximum is below its target |
| AT2050 | the refreshed Part VII entry completes the actual far, inverse or invariant-ball route for source013 | OPEN |

On notes/T2_PART7_v05.md (the theory auditor research/t2_part7_v05_audit, audit_v658, 05:37:07Z; 598 checks, all 29
listed file references authenticated):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT2143 | T2_PART7_v05 preserves the reviewed O2/O3 scope and analytic assumptions | CONFIRMED; explicit results stay at q = 21/10; source, generator and near hypotheses remain mandatory |
| AT2144 | the fifth entry states valid exact far arithmetic and the correct inclusive absorption endpoint | CONFIRMED; absorption includes equality, positive slack is strict, the distance below s_max is the stated fraction |
| AT2145 | the fifth entry correctly binds its numerical dependencies and its dated 58-root regional inventory | CONFIRMED; 58 distinct indices, six gradient-1/4 gaps and two gradient-71/500 gaps; historical snapshots dated |
| AT2146 | the refreshed Part VII entry establishes a full inverse or closes stationary existence | OPEN |

On notes/T2_PART7_v06.md (the theory auditor research/t2_part7_v06_audit, audit_v693, 07:09:13Z; 308 checks, all 30 listed
references authenticated, the complete diff from v05 read):

| id | claim (the theory auditor's wording, shortened) | verdict |
|---|---|---|
| AT2259 | T2_PART7_v06 preserves its conditional O2/O3 scope, exact far constants and selected 86-index inventory | CONFIRMED; the 86- and 82-index inventories agree with both actual unions; a dated inventory |
| AT2260 | the shortened progressive assembly follows from successful receipts, actual reviews and adopted same-source publications without requiring passing field inequalities | REFUTED (E-T2-v06-1): every added root must prove the three bounds M >= (3/5) I, gradient at most 1/4 and strain at most 137/125; corrected in section 2.2 |
| AT2261 | once every missing ordinary root proves the weaker conjunction, the route F-a far margin at 137/125 is positive under its analytic assumptions | CONFIRMED; margin 71675071190082633/5629499534213120000; whole-plane strain is a premise, not a present conclusion |
| AT2262 | the refreshed Part VII entry supplies a complete near bound, full inverse or stationary existence theorem | OPEN |

The second theory agent accepts AT2260. The omitted premise is a logical one: a successful computation can return an unresolved
sufficient test, and an adopted review can record that outcome correctly, so these records alone supply no pointwise
inequality (the theory auditor research/t2_part7_v06_audit/PROOF.md). No regional inequality is refuted (audit v693).

Reading for Part VII: Theorems A and B and the results of the v02 status table hold as stated there, with the
explicit formulas at q = 21/10 only; no closure of O3 at 013 or at any other center follows (AT-1579, AT-1593,
AT-1762, AT-1856, AT1894, AT1924, AT1931, AT1978, AT2001, AT2045, AT2050, AT2146, AT2262).

### 1.3 Status changes since T2_O2O3_FINAL_v02 was frozen (v02 is not edited)

- Corollary CS-W and Proposition DW (the S input of route F-a): CONFIRMED conditionally (AT-1594 to AT-1596),
  notes/T2_FAR_CSW_v02.md. New: the theory auditor's complete window stage (audit v589, 02:49:36Z) CONFIRMS the five D_W
  uppers of the R = W = 200 window on all 5120 radial cells (AT1928; they equal the inputs of
  runs/ds_window_v2_2158.json used by the A_E^+ run) and S_W^+ = fup(lambda^+ S^+) = 537734762519297/9007199254740992
  with the far margin of section 2.2 (AT1929). The numerical auditor CONFIRMS the window transfer independently (384-bit cutoff
  calculation and radial tensor integration on all 5120 cells; the same D_W, S_W^+, lhs, margin and s_max; exchange
  v532, 03:01:33Z). The comparison of the new S_W^+ with the old record
  8603756200308751/144115188075855872 is REFUTED (AT1930: one 2^-57 step above); the theory auditor's notes that this is no
  counterexample to the old bound. Background, inverse and existence are OPEN (AT1931).
- Lemma SC-W (the Hessian input of route F-a for the window Rw = Ww = 200): CONFIRMED (AT-1366, AT-1367; its
  application to this window AT-1598).
- Theorem CS-B (notes/T2_FAR_CS_v02.md): analytic parts CONFIRMED (AT-1536 to AT-1538); the rounding repair of the
  stored kernel uppers CONFIRMED as conditional finite arithmetic (AT-1731, AT-1732). New: the theory auditor's complete
  independent replay (audit v587, 02:45:45Z) CONFIRMS
  - the five whole-plane derivative energy uppers D_m^+ of a_f (AT1921: 248 panels, 1984 cells, 9920 comparisons at
    256 bits and a fresh 384-bit interior and exterior assembly; all five equal, as rationals, to the field D_upper
    of runs/ds_upper_1926.json, checked by the second theory agent);
  - S_h^B(a_f; 2 pi, 8 pi, h) <= S^+ = 1075445791051939/18014398509481984 <= 0.059699233948103892 < 3/50, and
    Gbar - SC^+ - S^+ = 11378045011678071/90071992547409920 > 0 (AT1922).
  The numerical auditor recomputes the final assembly at 512 bits on all 280 radial frequency cells of [0, 200] with the certified
  tail and CONFIRMS the same S^+ (exchange v529, 02:52:07Z; the derivative and kernel-box enclosures imported from
  the theory auditor's check).
  The theory auditor's S^+ exceeds the stored the second theory agent value S_old = 8603566328415511/144115188075855872 by 1/144115188075855872, so
  the comparison S^+ <= S_old is REFUTED (AT1923). The theory auditor states that this does not disprove the bound at S_old, but
  that the replay certifies only the new upper. The second theory agent uses the new rational everywhere (section 2.2). The window
  application and every closure are OPEN (AT1924). Earlier in the same replay: the 48 first-panel endpoints reproduce
  exactly at 256 bits (AT1898, CONFIRMED). The theory auditor's own working assumption that no endpoint grows from 256 to 384 bits
  is REFUTED (AT1899: seven grow). This is not a the second theory agent claim and not a counterexample to either bound. AT1900 (the
  original derivative norm neither disproved nor certified at that stage) is answered by AT1921.
  AT-1540, AT-1733 and AT-1762 asked for this numerical application. For a_f it is now given by AT1921 and AT1922.
- Lemma QID and Proposition ZO (notes/T2_QIDZO_v01.md, frozen 2026-11-03T23:24:25Z, SHA256
  cc67aa515de67fcc04496bcd1ed1f5529816a43bb957208c6a0cb5e2e7130c9e): CONFIRMED (AT-1754 to AT-1757; audit_v533,
  00:25:55Z), with the moment and energy scaling and the zeroth-order oscillation bound; they exclude only a
  universal vanishing bound of the band constant in SC, positive moments and energies of order above 1 (D1 is
  invariant and not excluded), and they give no candidate-specific band upper and no impossibility of the remaining
  C2 approaches (AT-1758, OPEN).
- The A_E^+ plan: notes/T2_FAR_AE_PLAN_v02.md (frozen 2026-11-03T23:45:01Z, SHA256
  d0eab8bf394a5f6b23f7c98c2ba9f829168f306fa425ecf9252704280fcfea9b) supersedes T2_FAR_AE_PLAN_v01 (frozen 23:17:11Z).
  Audits of v01 (audit_v517): Lemma SYM CONFIRMED (AT-1697); Proposition AE-CS CONFIRMED conditionally, "finiteness
  and the continuum essential supremum remain explicit premises" (AT-1698); support, radiality and factor 4
  CONFIRMED (AT-1699); the cancellation identity and its sign CONFIRMED (AT-1700); reuse of the r_B zero shortcut
  REFUTED (AT-1701); the count of about 130 cells REFUTED, 202 cells (AT-1702); no certified A_E (AT-1703, OPEN).
  Audits of v02 (audit_v524): Lemma ENC CONFIRMED as an analytic containing estimate (AT-1726 to AT-1728); the
  same-configuration FLOAT comparison CONFIRMED as provenance and sampled arithmetic only (AT-1729); no numerical
  A_E certificate (AT-1730, OPEN).
- The A_E^+ implementation, notes/T2_FAR_AE_v01.md (frozen 2026-11-04T01:19:42Z, SHA256
  c36f571937a15bd98f4b5be2d93cc44d7222d7cb914737bb1fff7c337d67d7f3). Audits (audit_v548, 00:59:18Z, on a pre-freeze
  copy of the code, SHA256 1b7f269c...; audit_v559, 01:26:14Z, on the frozen code): Lemma BOX CONFIRMED as an
  analytic identity with its endpoint bounds (AT-1808); the claim that the sinhc call of rE_box always has a
  nonnegative argument REFUTED, the only negative lower argument being -2^(-1074) (AT-1809); the clamp at zero
  CONFIRMED as a valid repair (AT-1810); the unchanged call CONFIRMED as containing at 96 bits, its lower end
  1 - 2^(-53) being below the minimum 1 of sinhc (AT-1842), so no restart was needed (the coordinator 01:32Z); the adaptive
  cover with piecewise positive weights CONFIRMED as preserving the conditional AE-CS implication (AT-1843); coverage
  and scalar assembly of chunk 0:40 CONFIRMED (AT-1844); no complete far closure and no full A_E constant at that
  stage (AT-1811, AT-1845, OPEN).
- The complete run, notes/T2_FAR_AE_v02.md (frozen 2026-11-04T01:47:14Z, SHA256
  970868f088afe45d71da4aaf09ca15a50e18fbd61fbe043fe83c8fe11e4b921d). The theory auditor recomputed all four chunks independently
  with complete partitions: 0:40 (AT1865, audit_v566), 40:80 (AT1873, audit_v569), 80:126 (AT1887, audit_v575) and
  126:202 (AT1889, audit_v576), all CONFIRMED; each chunk alone is no full constant (AT1866, AT1874, AT1888, AT1890,
  OPEN). The combined check (audit_v577, 02:18:48Z, 4052 assertions) CONFIRMS
  - the complete frequency cover and all accepted integral bounds, A_E = 5915921936389617/4503599627370496 =
    1.3135985491329587, on base cell 4, |xi| in [0.2, 0.25] (AT1891);
  - the route F-a scalar inequality at 137/125 for the fixed recorded inputs, margin
    1146801139041322753/90071992547409920000 >= 0.012732050292300 (AT1892);
  - the strain threshold 1667651993489279957/1513209474796486656 >= 1.102062881091 (AT1893).
  At that stage the theory auditor kept the D_s inputs as a condition; they are now supplied by AT1921 and AT1928. AT1892 and
  AT1893 use the old S_W^+ = 8603756200308751/144115188075855872; with the new one see AT1929 and section 2.2. The far
  closure is OPEN (AT1894). So Proposition AE-RUN and the exact arithmetic of Corollary F-a-far are CONFIRMED. Lemma
  SE (the AT-1842 argument written out) adds nothing to AT-1842.
- The rerun price, notes/T2_FAR_AE_PILOT_v01.md (frozen 2026-11-04T02:15:57Z, SHA256
  ced7084b313e65fc714c54de86d3628965cbef572ee70dbc9323909e5b4bb487), corrected by notes/T2_FAR_AE_PILOT_v02.md (frozen
  2026-11-04T03:31:33Z, SHA256 aa60587c95e69490074d511792c2dc4743ab6293391c12d0a55c0c547e162020): section 2.3 item 4.
  The theory auditor CONFIRMS the pilot summaries (AT1976), REFUTES the stop-rule prediction of v01 (AT1975), CONFIRMS v02's
  corrected wording and its two conditional strain allowances (AT1999, AT2000), and keeps any new A_E bound, runtime
  guarantee or impossibility at TARGET 1.25 OPEN (AT1978, AT2001).
- Row C2: still OPEN.

## 2. Far section

Both far routes bound the far constant of the 013 far piece a_f (complete far piece at erflog 8, rho 1, every angular
mode; exact inputs data/C1-N1-007_exact.json, SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21,
and inputs013/phi_007_b18s2_phi_exact.json, SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a).
q = 21/10, c = 4076476460239181/2251799813685248.

### 2.1 Proposition F (strain 3/2, target Gbar = q (c - 3/2), about 0.65167)

Proposition F (T2_FAR_F_v01; CONFIRMED conditional, AT-1236) gives the far bound max(SC^+, A_low^+(8 pi)) + S^+ <=
Gbar from Lemma HSB (T2_FAR_v02 section 2.3) and the rows below. Gbar = 14674311533937489/22517998136852480.

| row | content | status | where |
|---|---|---|---|
| C5a, C5b | a_f real, bounded, even in x_1 and x_2; hypotheses of NR-21 case B, a_f in S^(-lambda) | CONFIRMED (AT-1147 to AT-1152) | T2_FAR_C5_v01 |
| C1 | SC^+ = 4194197216881219/9007199254740992 (0.46564943200002806) >= SC(a_f) | CONFIRMED (AT-1230 to AT-1234) | T2_FAR_C1_v01 |
| C3, C4 | S^+ = 1075445791051939/18014398509481984 (<= 0.059699233948103892) >= S_h^B(a_f; 2 pi, 8 pi, h), h = <min(abs(xi), 63/10)>^-1 (route B, Theorem CS-B); SC^+ + S^+ <= Gbar exactly, room 11378045011678071/90071992547409920 (> 0.126321) | CONFIRMED: analytic parts AT-1536 to AT-1538; numerical application AT1921, AT1922, and numerical audit exchange v529 (the old S_old fails the comparison, AT1923) | T2_FAR_CS_v02; the theory auditor audit v587 |
| C2 | A_low^+(8 pi) >= A_low(8 pi) with A_low^+(8 pi) <= Gbar - S^+ = 53320017180490261/90071992547409920 (> 0.591971; with the new S^+, notes 02:48Z; the v03 value 426560137443922093/720575940379279360 belongs to S_old, AT-1760) | OPEN: no priced route fits before the stop (HEURISTIC; qualifications below); FLOAT band value 0.3848 (the second numerics agent); QID/ZO exclude only a universal vanishing bound (AT-1754 to AT-1758) | T2_FAR_C2_PLAN_v01; T2_QIDZO_v01 |

So rows C5, C1, C3 and C4 are CONFIRMED, and Proposition F at erflog 8, rho 1 now waits on row C2 alone (and, for
any use, on the strain bound 3/2 of item B and the near side). Row C2 stays OPEN unless an auditor confirms a
certified A_low^+; X8 keeps it OPEN with no C2 code and no NL6 rerun.
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
The A_E^+ run of section 2.2 bounds A_low(8 pi; a_W) for the windowed piece a_W with the definitions of route F-a
(Proposition AE-CS); it gives no C2 bound, since row C2 concerns a_f under Proposition F, and its budget 0.591971 is
below 1.3136 in any case.

### 2.2 Route F-a (strain s^+ = 137/125, window Rw = Ww = 200)

AT-911 (CONFIRMED): A_*(a_W + a_t) <= max(SC^+, A_E^+) + S^+ + OMF(a_t), with a_W = a_f (1 - Sinf((r - Rw)/Ww)) and
a_t = a_f - a_W. The target is q (c - s^+). At s^+ = 137/125 it is exactly 4222322644155391629/2814749767106560000,
at least 1.500070341419995 (AT-1761).

| input | value | status | where |
|---|---|---|---|
| SC^+(a_W) | 4194197216881219/9007199254740992 = 0.46564943200002806 | CONFIRMED (AT-1366, AT-1367, AT-1598) | Lemma SC-W, notes 17:15Z; T2_FAR_CSW_v02 E1 |
| S_W^+ >= S_h^B(a_W) | 537734762519297/9007199254740992 (<= 0.059700551449026418) = fup(lambda^+ S^+), lambda^+ = 4503699017199667/4503599627370496 | CONFIRMED (AT1929, with Corollary CS-W AT-1594, lambda^+ AT-1596, S^+ AT1922 and the D_W uppers AT1928; numerical audit exchange v529, v532; the second theory agent's transfer, notes 02:48Z, agrees); the old record fails the comparison (AT1930) | T2_FAR_CSW_v02; runs/splus_transfer_0246.json |
| OMF^+(a_t) | 513586856047295/4503599627370496 = 0.11403919054571054 | CONFIRMED (AT-1336 to AT-1338) | notes 16:19Z |
| A_E^+(a_W) | 5915921936389617/4503599627370496 = 1.3135985491329587 (needed: at most rhs - S_W^+ - OMF^+ = 7466577491677103883/5629499534213120000 >= 1.326330599425) | CONFIRMED (AT1891; chunks AT1865, AT1873, AT1887, AT1889; its D_W inputs AT1928): complete run of 202 base cells, 324 sub-cells, 5970416 box evaluations, maximum on base cell 4, abs(xi) in [0.2, 0.25]; the premises of AE-CS kept open in AT-1698 (finiteness, continuum supremum) are met by the complete cover (the theory auditor far_ae_complete_assembly_audit/PROOF.md), and Lemma BOX is CONFIRMED (AT-1808); every accepted bound of the complete run is below TARGET 1.3163305 (the stored maximum above). The stop rule does not guarantee this: the code splits a sub-cell while its bound exceeds TARGET and its depth is below DMAX = 5, and at depth DMAX it accepts the sub-cell whatever its bound (AT1975; code/c1/ae_cells.py line 342). The bounds sit near TARGET because refinement stops once a bound is below it, not because of the size of the bracket, whose FLOAT midpoint values are at most 1.18880 | T2_FAR_AE_v02 sections 0 to 3 |
| s^+ | 137/125 | OPEN (item B; AT-1599); regional coverage below | ledger v11 row B; section 2.3 |

Far condition with the new S^+ (CONFIRMED, AT1929, numerical audit exchange v532; the second theory agent's exact computation code/c1/splus_transfer.py,
output runs/splus_transfer_0246.json, SHA256 c28add462b059fd91e14064dc82a539d4770e561e9a9310e22b6002301ab1336,
agrees):
    lhs = max(SC^+, A_E^+) + S_W^+ + OMF^+ = 13396752347393121/9007199254740992 <= 1.487338291127696,
    rhs = q (c - 137/125) = 4222322644155391629/2814749767106560000 >= 1.500070341419995,
    rhs - lhs = 71675071190082633/5629499534213120000 >= 0.012732050292300.
The same computation with the old S_W^+ reproduces the exact values of AT1892 and AT1893. The new values are below
them by 1/144115188075855872 (lhs above, margin below), and every printed bound of T2_FAR_AE_v02 and T2_PART7_v03
still holds. The far absorption step of Proposition FG (T2_FAR_v01 section 3) needs lhs <= q (c - s), equality
included; a strictly positive margin is lhs < q (c - s) (AT2044, audit v625); at s = 137/125 the margin above is
positive. The theory auditor states the conclusion as conditional on a matching whole-plane strain bound and the analytic source
hypotheses (audit v589, v625); route F-a as a whole also needs the near side. Route F-a gives nothing at strain 3/2:
there the target q (c - 3/2) is about 0.65167, below A_E^+ alone.

Status of the premises of AE-CS and Corollary CS-W at this freeze (the coordinator X9, item 5(d)):
- Proposition AE-CS (T2_FAR_AE_PLAN_v02; CONFIRMED conditionally, AT-1698). (i) The uppers D_s of the derivative
  L2 norms of a_W, s = 1 to 5, which the theory auditor's assembly of A_E^+ takes as hypotheses
  (far_ae_complete_assembly_audit/PROOF.md): supplied, since the fresh window uppers of AT1928 equal the D_W inputs
  of the run. (ii) Finiteness and the continuum essential supremum (AT-1698): met by the complete cover, 324
  sub-cells tiling [0, U8] with U8 >= 8 pi (AT1891). (iii) The containing BOX residual and the exceptional sinhc
  endpoint: CONFIRMED (AT-1808, AT-1842; the k_cells.box_R call AT1977). (iv) The piecewise Cauchy-Schwarz bound
  with positive cell weights: CONFIRMED (AT-1698, AT-1843).
- Corollary CS-W and Proposition DW (T2_FAR_CSW_v02; CONFIRMED "under the complete stated kernel and derivative
  hypotheses", AT-1594 to AT-1596). The complete CS-B certificate for a_f is supplied by AT1921 and AT1922 (the numerical auditor
  v529); the derivative bounds and the containing cell data of DW by the window stage, AT1928 and AT1929 (numerical audit exchange v532).
- Kept as hypotheses in AT1891 and AT1929: the fixed source013 at C2-N1-013 with Candidate 007 unchanged and the
  admitted source calculus, the original tail-table certificate, the window Leibniz and Faa di Bruno estimates, the
  singleton repair and CS-W homogeneity, which the theory auditor cites by immutable hashes and does not reprove
  (far_window_complete_audit/PROOF.md), and the audited inputs SC^+ and OMF^+. The second theory agent claims nothing beyond these
  statements.
- Not met: the whole-plane strain bound (item B; coverage below) and, outside the far chain, the near step and the
  inverse step (AT1931, OPEN).

Regional strain coverage (ledger v11 and the exact unions of both auditors read to 07:12Z). Here t = r^2/(1 + r^2) and
root k is k/128 <= t <= (k + 1)/128; root 127 is the exterior r^2 >= 127. Each certified region carries M >= (3/5) I,
|grad h| <= 1/4 and ||Sym Du||_op <= 137/125 uniformly in angle; these are regional results.
- Ledger v11 (X10, the coordinator, 2026-11-04T06:17:33Z, SHA256
  8059094197cb01e4997ba778727b2ec0d8177e492052388c4da93e64dc048891), row B: both auditors certify 62 of the 128 roots,
  namely roots 0 to 55 (r^2 <= 7/9), the balanced roots 98, 100, 102, 104 and 106, and all of root 127 (J_7, J_8 to
  J_20 and Proposition TC; AT2098, AT2099; numerical audit exchange v588, v589); for |grad h| <= 1/4 six open r^2 gaps remain, all inside
  7/9 < r^2 < 127 (numerical audit exchange v620; AT2183, AT2184, audit v670). T2_PART7_v05 recorded the 58-index state of 05:28Z and
  T2_PART7_v06 the 86-index state of 06:49Z.
- After ledger v11: the 24 capped roots 99, 101, 103, 105 and 107 to 126, as closed slabs. The first theory agent's job 7 produced the
  record (the first theory agent's note 78; producer-record audit AT2179, AT2180); the numerical auditor reconstructed the source independently and
  recounted it exactly (numerical audit exchange v630, v631), and the theory auditor CONFIRMS that reconstruction (AT2219 to AT2221, audit v681,
  06:34:21Z; AT2222 OPEN).
- Base union of both auditors: the theory auditor AT2223, AT2224 (audit v682, 06:35:03Z; AT2225 OPEN) and the numerical auditor AN634 (06:41:20Z;
  research/background_slabs_union/verification/check_v01.json in the numerical auditor, SHA256
  acd9faf50026923c96203d180a86229e71443e06a1a0dc9477d6119ec705e8e5), in agreement (AT2231, AT2232, audit v685,
  06:46:49Z; AT2233 OPEN): 86 indices, 0 to 55 and 98 to 127, with components [0, 7/9] and [49/15, infinity) in r^2
  for the three bounds (the theory auditor CONFIRMS v06's statement of it, AT2259).
- Progressive assembly (the theory auditor AT2228, AT2229, audit v684, 06:37:05Z; AT2230 OPEN; premise restated after AT2260, audit
  v693). Let m be an integer with 55 <= m <= 97 such that every root 56 to m has a same-source regional theorem
  proving M >= (3/5) I, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125 uniformly in angle on that root, each resting on
  a complete successful ordinary computation, an independent actual review and an adopted same-source publication.
  Then, with the 86-index base union, the three bounds hold on the indices 0 to m and 98 to 127 (m + 31 indices), and
  the only gap is ((m + 1)/(127 - m), 49/15) for m < 97; at m = 97 no gap remains. The three bounds on every added
  root are a premise: a successful computation can return an unresolved sufficient test and an adopted review can
  record that outcome, so the records alone imply no bound (AT2260).
- Union at m = 56, the current exact union of both auditors: the numerical auditor AN637 (06:50:46Z;
  research/background_progressive_union/verification/check_v02.json in the numerical auditor, SHA256
  aaab1c7d475dd75b2ce5f2ba7a31f6a78b2c51d3630666eac3b29bce260b4027) and the theory auditor AT2240, AT2241 (audit v688, 06:52:27Z;
  AT2242 OPEN), with root 56 (7/9 <= r^2 <= 57/71; AT2234, AT2235, audit v686) passing all four joint flags. It covers
  87 indices, 0 to 56 and 98 to 127. For the three bounds the closed components in r^2 are [0, 57/71] and [49/15,
  infinity), and the only open gap is (57/71, 49/15), the interior of the union of roots 57 to 97. For the stronger
  |grad h| <= 71/500 with the same matrix and strain bounds the union has 83 indices and the open gaps (57/71, 99/29),
  (25/7, 101/27), (51/13, 103/25) and (13/3, 105/23). The global background and existence stay OPEN (AT2242; AN637).
  The ledger of X11 is the authority for the joint targets.
- Certified roots without a union at 07:12Z: root 57 (57/71 <= r^2 <= 29/35; the theory auditor AT2243, AT2244, audit v689; AT2245
  OPEN; numerical audit exchange v641) and root 58 (29/35 <= r^2 <= 59/69; AT2252, AT2253, audit v691; AT2254 OPEN; numerical audit exchange v645). Each
  actual review records all four flags true, so each proves the three bounds of the premise. No executed union
  containing them is published at the cutoff; after a reviewed one, the progressive assembly at m = 58 leaves the gap
  (59/69, 49/15).
- No certificate at 07:12Z: the ordinary roots 59 to 97. Root 59 has completed its physical run (numerical audit exchange v644; 07:02:48Z
  to 07:09:17Z); its actual review and adoption are pending. The first theory agent's job 8 (the producer record SLAB_REQUEST_v02 of
  roots 97 to 52, core 41, 06:35:55Z to at most 08:35:55Z) had finished roots 97 to 88 by 07:08Z with every flag true
  in its producer record (the first theory agent's note 82); a producer record certifies no root. The independent reconstruction of its
  42 ordinary roots on core 49 is allocated under conditions that are not yet met (the numerical auditor PLAN_v01, v638; the coordinator
  07:08Z item 2(a)). The open gap is missing evidence, not a counterexample.
- Consequence for route F-a (a restatement of section 2.3 item 1 with s^+ = 137/125; no new hypothesis; the theory auditor CONFIRMS
  it as a conditional statement, AT2261): if every root 57 to 97 has a regional theorem proving the three bounds,
  certified by both auditors, then the progressive assembly at m = 97 gives ||Sym Du||_op <= 137/125 < s_max on the
  whole plane, the far inequality of route F-a holds with the margin 71675071190082633/5629499534213120000 >=
  0.012732050292300, and far absorption follows under the analytic premises listed above. The whole-plane strain bound
  is a premise here, not a present conclusion. The near step and the inverse step stay OPEN (AT2262).
These are regional results; none of them is a whole-plane bound, and route F-a needs the whole plane (section 2.3).

### 2.3 Answer on s^+ (AT-1599; X8 item 5(d))

1. What route F-a needs. A certified number s^+ with ||Sym Du(x)||_op <= s^+ for the background u at every x of the
   plane (ledger item B; T2_FAR_v02 C6: for a far upper A, the admissibility A <= G needs a certified global strain
   bound at most c - A/q), and the far inequality max(SC^+, A_E^+) + S_W^+ + OMF^+ <= q (c - s^+). For a certified
   A_E^+ this is
       s^+ <= s_max(A_E^+) := c - (max(SC^+, A_E^+) + S_W^+ + OMF^+)/q.
   Since q > 0, q (c - s) - lhs = q (s_max - s). At s^+ = s_max the far absorption holds with zero far slack, since
   Proposition FG drops a nonpositive term; a strictly positive margin holds exactly when s^+ < s_max. The theory auditor CONFIRMS
   this (AT2044) and REFUTES the claim that Proposition FG requires strict slack (AT2043; audit v625,
   research/far_endpoint_scope_correction), withdrawing its strict reading AT2038 of audit v623; AT2039 stands only
   as the equivalence for a positive margin. The theory auditor reads this section of v04 as correct for absorption (audit v625).
   The theory auditor CONFIRMS this continuous dependence: at the fixed source, split and other inputs, only the strain premise and
   G(s) = q (c - s) change with s (AT-1853, building on AT-935, AT-936). With the old S_W^+: s_max =
   1667651993489279957/1513209474796486656 >= 1.102062881091 (AT1893). With the new S_W^+:
       s_max = c - lhs/q = 4963249980622857/4503599627370496 >= 1.102062881091
   (the theory auditor audit v589 with AT1929; numerical audit exchange v532; runs/splus_transfer_0246.json), above 137/125 = 1.096 by at least
   0.006062881091. The decimal 1.102062881091 = 1102062881091/10^12 lies strictly below s_max, by exactly
   628456482009/1099511627776000000000000 (> 5.7e-13). So route F-a tolerates any certified whole-plane strain target
   s with 137/125 <= s <= 1.102062881091, each with a positive far margin and each needing its own whole-plane
   certificate (AT-1853, AT1893, AT2044). The earlier values (s_max >=
   1.096000047345 at A = 1.3263305 and s_max = 1665683415424191637/1513209474796486656 >= 1.100761952107 at the
   binary64 TARGET 1.3163305) are CONFIRMED arithmetic (AT-1854) and are superseded.
2. What the second theory agent supplies and does not. The strain bound is a property of the background (item B), certified root by
   root by the numerical auditor and the theory auditor; it is not a the second theory agent computation, and no far result of the second theory agent bounds it. The regional
   certificates of section 2.2 do not suffice: route F-a needs the bound on the whole plane, including every annulus
   between the last certified inner root and the terminal region.
3. What closes the s^+ row of route F-a: a certified s_* <= 1.102062881091 (for instance 137/125) on all 128 roots
   and the exterior, with both auditors' reviews.
4. The lower-TARGET option (notes/T2_FAR_AE_PILOT_v02.md, which corrects v01 after AT1975 and is CONFIRMED as
   corrected, AT1999; HEURISTIC projections from measured pilots on four base cells at TARGET 1.25 and three at TARGET
   1.30, with the frozen code, only TARGET changed). A rerun at TARGET 1.30 would cost about 1 to 2 core-hours. Its
   A_E^+ would be the maximum of its accepted bounds, and the stop rule does not keep that below 1.30 (AT1975); in the
   three pilot cells every accepted bound is below 1.30 (maxima 1.2958 to 1.2974). At A = 1.2974, s_max >= 1.109776
   with either S_W^+ (AT2000). TARGET 1.25 was not reached by the present code at NTRY 60000 and DMAX 5: on base cell
   72 the bound tends to about 1.2510, and four depth-5 sub-cells were accepted with bounds up to 1.2536446583143115.
   This is a measured limit of that code, not an impossibility for other weights or methods (AT1978). The coordinator
   decided against a rerun before X9 (the coordinator 02:18Z), and that decision stands to the stop (the coordinator 03:00Z item 4;
   X9 item 4(d)). The theory side asks for none: a smaller A_E^+ improves no constant that O3 uses now, since it
   raises only s_max and every certified region has ||Sym Du||_op <= 137/125 (the first theory agent's note 63; theory_v17). Core 41 now
   serves the first theory agent's terminal-cell extension (the coordinator 03:00Z item 3).

### 2.4 What the far section does not give

- No certified A_low^+(8 pi) (row C2, OPEN), so Proposition F is not closed.
- No far closure at strain 3/2 by route F-a.
- No whole-plane strain bound, and so no unconditional far bound by route F-a (AT1894, AT1924, AT1931).
- No inverse, near, invariant-ball or existence statement: every far row is an input of O3, not a part of it.

## 3. Answers to the theory auditor on Theorem CS-B

### 3.1 AT-1539 (REFUTED: nearest conversion of an arbitrary arb upper is outward)

the second theory agent agrees with the verdict and does not use that claim. Its correction (notes 20:19Z; T2_PART7_v01 section 3.1) is
CONFIRMED as conditional finite arithmetic (AT-1731, AT-1732): 90 one-step cell corrections, maximum
8603566328415511/144115188075855872 < 3/50, directed tail 0.024397461684268512. The theory auditor's independent replay rounds one
cell one binary64 step higher (AT1922, AT1923); the second theory agent adopts the theory auditor's value. The A_E^+ code (code/c1/ae_cells.py)
converts every stored upper outward (T2_FAR_AE_v01 section 4).

### 3.2 AT-1540 (numerical application of CS-B)

For a_f it is CONFIRMED by the theory auditor's complete replay (AT1921, AT1922; section 1.3), which used the theory auditor's own copies of
the code. The owner descriptions of T2_PART7_v01 section 3.2 and the replay commands of T2_PART7_v03 section 3.2 stay
as recorded. The open question of v03 item 3 (the unclamped sinhc line in k_cells.box_R) does not arise for the
admitted value, since the theory auditor's replay uses its own clamped copy (the theory auditor's notes 01:29:42Z), and it is now closed:
the theory auditor CONFIRMS that the AT1842 exceptional-endpoint argument also covers the unchanged 96-bit call in k_cells.box_R
(AT1977), with no monotonicity claim on a negative interval. For a_W it is CONFIRMED by
the theory auditor's window stage (AT1928, AT1929). Core 41, reserved for these replays, was released by the theory auditor at 02:49:04Z
and assigned to the first theory agent (the coordinator 03:00Z item 3); the second theory agent runs no job there.

## 4. Other X8 item 5(d) entries

- The A_E^+ implementation: notes/T2_FAR_AE_v01.md and notes/T2_FAR_AE_v02.md (complete run, assembly, Lemma SE,
  checks, measured price and replay commands), now CONFIRMED with the source hypotheses (section 1.3).
- Measured price (T2_FAR_AE_v02 section 6): 01:05:20Z to 01:38:51Z wall time on core 41, 2005.4 s summed sub-cell
  time (0.557 core-hours, including about nine minutes of core sharing), 5970416 box evaluations, no failure-driven
  bisection; the plan priced 0.1 to 1.7 core-hours (HEURISTIC). The theory auditor's four chunk replays took 429.5, 967.1, 153.1
  and 34.6 measured seconds (audit_v577).
- Rerun price: section 2.3 item 4.
- Row C2: OPEN, no C2 code, no NL6 rerun.
- The final closure check that the coordinator requests in its 07:08Z note (item 3(a)) is a separate the second theory agent file, not part of
  this entry.

## 5. Files (SHA256)

- notes/T2_PART7_v06.md ec4c737ce9fd7c6d9b24673e63a69959ef84ba164205a2d81d3e441baaa210d4 (superseded, unchanged)
- notes/T2_PART7_v05.md 9155c45fa096b5cb550297d85d3d725b89c03e7f3c105f056c5c82ce3d5960a7 (superseded, unchanged)
- notes/T2_PART7_v04.md 7bb604246236d1f6a4f8eb9820b6fb2f17e0df5ecf15f5a44f78c4b8c0a1a714 (superseded, unchanged)
- notes/T2_PART7_v03.md 4b8afd144edff883c271ede4d6678d70229f95c1e7758bbaa01aa373c5d6fcc8 (superseded, unchanged)
- notes/T2_PART7_v02.md 6a106195732cad8e706edc74535ab43e0c91a8082c47ad132118a7df6c5b43bd (superseded, unchanged)
- notes/T2_PART7_v01.md 7e9fb6b08a98fdebd8967e90a1e6fcbc96854404a1c71b33c101788e10aae182 (superseded, unchanged)
- notes/T2_FAR_AE_PILOT_v02.md aa60587c95e69490074d511792c2dc4743ab6293391c12d0a55c0c547e162020
- notes/T2_FAR_AE_PILOT_v01.md ced7084b313e65fc714c54de86d3628965cbef572ee70dbc9323909e5b4bb487 (superseded,
  unchanged)
- notes/T2_FAR_AE_v02.md 970868f088afe45d71da4aaf09ca15a50e18fbd61fbe043fe83c8fe11e4b921d
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
- code/c1/ae_cells.py 5d784f2089fcff9d6220cf2bb0c52a410cec867337a8bb6c94825442827b080e
- code/c1/k_cells.py 68af822acae61a314befce6083de2de11a717deca79be89fb3db8a6a7843bf2c
- code/c1/splus_transfer.py 4ab2f6c20dfcf4052156b1f3efda5236ff1410067abb496854093da0f98b9708
- runs/splus_transfer_0246.json c28add462b059fd91e14064dc82a539d4770e561e9a9310e22b6002301ab1336
- runs/splus_transfer_0246.out 364ca0ead733735058777a6fa8f3ac47923ae4c975fada5303dec0c7228056a5
- runs/ae_cells_0105_final.json 37b85872cd235957c2c1bf9245783cf0cfeaaabe24be522b5f5a99305c24bf45
- code/c1/cs_round_check.py 391dc3d05e36004a55fe21e50d1b982dbd16fd4d0f4302777acf5ca1cb01a733
- runs/cs_round_check_2018.json 73782ae75b5151270b0f42acd9f251c7e9892cafd58d2af2b03b36627174fefa
- runs/k_cells_1941.json 38735c097f0367c0e287be0eb015ece869056c8487d7bedb964490567cc93d8b
- runs/k_tail_2000.json 9d17f52c5f98afffa2d46092b8561a78d035df021b90ce0fc1978c3e6c54bda6
- runs/ds_upper_1926.json 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5
- runs/ds_window_v2_2158.json e26aeb71eadadf209a0140d50d8e9339aa1c8a3985e96cb8862893c3377abf6a

## 6. Changes against T2_PART7_v06

- Title and header: inputs read to about 07:12Z (ledger v11; the coordinator 07:08Z; the theory auditor audit v693; numerical audit exchange v646; the first theory agent's note
  82). The rule for a later version names the whole-plane certificate.
- Section 1.2: the verdicts on T2_PART7_v06 (AT2259 to AT2262, audit v693) added, with the second theory agent's acceptance of AT2260.
- Section 2.2, progressive assembly (E-T2-v06-1, AT2260): the premise that every added root 56 to m has a regional
  theorem proving M >= (3/5) I, |grad h| <= 1/4 and ||Sym Du||_op <= 137/125 is restored; v06 listed only the
  computation, review and publication records. The consequence for route F-a now names the same premise and cites
  AT2261.
- Section 2.2, coverage: the exact 87-index union at m = 56 (AN637; AT2240, AT2241) replaces the 86-index union as the
  current one, which stays as the base union; the gap for the three bounds is (57/71, 49/15), and for 71/500 the union
  has 83 indices. Roots 57 and 58 are listed as certified without a union, root 59 and job 8 as uncertified. Section 0
  names the new gap.
- Section 5: T2_PART7_v06 added.
