# T2_FAR_AE_PILOT_v02: measured price of a lower-TARGET A_E^+ rerun (pilots at TARGET 1.25 on four base cells and at TARGET 1.30 on three), and a FLOAT check of the stored weights at five points per sub-cell; second version, with the stop-rule wording corrected after AT1975

Agent the second theory agent, version 1 written 2026-11-04 from 02:15Z and frozen 02:15:57Z (notes/T2_FAR_AE_PILOT_v01.md, SHA256
ced7084b313e65fc714c54de86d3628965cbef572ee70dbc9323909e5b4bb487, unchanged); this version written from 03:29Z, frozen
2026-11-04T03:31:33Z. It corrects the stop-rule wording that the theory auditor REFUTES (AT1975, audit v603) and records the theory auditor's verdicts
AT1975 to AT1978; the measured records and the numbers of sections 1, 2 and 4 are unchanged, and the theory auditor CONFIRMS that
the summaries of sections 1 and 2 match the frozen records (AT1976). Changes: section 7. Recipients: the coordinator (the
lower-TARGET option of notes/T2_FAR_AE_v02.md section 8), the theory auditor (audit), the first theory agent (publisher). Paths: notes/ and scratch/
are relative to the agent directory; code/ and runs/ are relative to research/h4/far009/ of agent the second theory agent. Status labels:
CONFIRMED and REFUTED (the theory auditor verdicts), CLAIMED, FLOAT (sampled value, not a bound), HEURISTIC (projection), OPEN.

Nothing here changes notes/T2_FAR_AE_v02.md (frozen 2026-11-04T01:47:14Z, SHA256
970868f088afe45d71da4aaf09ca15a50e18fbd61fbe043fe83c8fe11e4b921d) or its A_E^+ = 1.3135985491329587. The pilots
used the frozen code unchanged (code/c1/ae_cells.py, SHA256 5d784f20...; code/c1/k_cells.py, 68af822a...;
runs/ds_window_v2_2158.json, e26aeb71...; hashes printed at the head of the TARGET 1.25 log) with EPS = 0, NTRY =
60000, DMAX = 5, and only TARGET changed. They cover four base cells at TARGET 1.25 (4, 12, 72 partly, 150) and
three at TARGET 1.30 (4, 12, 72), not [0, U8], so they give no A_E^+ (AT1978). Their only use is the price.

The stop rule of the code (T2_FAR_AE_v01 section 4; code/c1/ae_cells.py line 342). A sub-cell is split while its bound
exceeds TARGET and its depth is below DMAX = 5; at depth DMAX it is accepted whatever its bound. So TARGET is not a
guaranteed upper for the accepted bounds: base cell 72 of section 1 has four accepted depth-5 rows above TARGET 1.25,
with maximum 1.2536446583143115 (AT1975). In the complete run of T2_FAR_AE_v02 (TARGET 1.3163305) every accepted bound
is below TARGET, the maximum being 1.3135985491329587 (AT1891).

## 1. Pilot at TARGET 1.25 (runs/ae_t125_pilot_0158.log, core 41, 01:58:17Z to 02:11:08Z)

| base cell | \|xi\| | accepted sub-cells | failed attempts | deepest level | box evaluations | seconds | max bound_upper | stored run (TARGET 1.3163305): seconds, max bound |
|---|---|---|---|---|---|---|---|---|
| 4 | [0.2, 0.25] | 2 | 1 | 1 | 115160 | 32.6 | 1.2475970657090092 | 4.1, 1.3135985491329587 |
| 12 | [0.6, 0.65] | 14 | 12 | 4 | 1482560 | 498.3 | 1.2498827665504211 | 26.2, 1.313480402367652 |
| 72 | [3.6, 3.65], stopped at 3.60625 | 4 (t-length 1/160) | 5 | 5 | 540000 | 190.2 | 1.2536446583143115 (above TARGET) | 18.4, 1.3120760903540205 |
| 150 | [12.3, 12.55] | 1 | 0 | 0 | 1680 | 1.2 | 1.2452520049304103 | 0.6, 1.3089224977485272 |

On base cell 72 every attempt used the full budget of 60000 box evaluations, and the bound of the leftmost sub-cell
(left end 3.6) went 1.29472, 1.27259, 1.26170, 1.25632, 1.25364 at levels 1 to 5 (widths 1/40 to 1/640): each halving
of the t-width removes about half of the remaining excess, so at this box budget the bound tends to about 1.2510, and
at DMAX = 5 the code accepts sub-cells with bound 1.2536 > TARGET. I stopped this cell at 02:11:05Z (its .partial file
is kept). Projected for the whole cell from the eighth done: about 1500 s (HEURISTIC). From about 02:02Z to 02:11Z
short jobs of other agents shared core 41 at times (one, terminal_prep.py, was seen there at 02:06Z); sub-cell times in
that window are 15 to 31 s against 14 to 16 s before, so the seconds of the second half of cell 12 and of cell 72
overstate the one-core time.

## 2. Pilot at TARGET 1.30 (runs/ae_t130_pilot_0211.log, core 41, 02:11:14Z to 02:12:53Z)

| base cell | accepted sub-cells | failed attempts | box evaluations | seconds | max bound_upper | factor in seconds against the stored run |
|---|---|---|---|---|---|---|
| 4 | 1 | 0 | 19640 | 9.6 | 1.2973489076285489 | 2.3 |
| 12 | 2 | 0 | 91024 | 37.3 | 1.2972344516237515 | 1.4 |
| 72 | 2 | 0 | 115440 (57944 and 57496) | 46.6 | 1.2958294721343018 | 2.5 |

No bisection was needed, but on cell 72 both halves came within 4 percent of NTRY (against 37000 each in the
stored run, a factor of about 1.6). In the stored run the 26 sub-cells with more than 45000 evaluations all lie in
[2, 3), the largest (53808) on [2.5, 2.525]; with a similar factor most of them would exceed NTRY at TARGET 1.30 and
bisect once, about 3 times their present cost.

## 3. Reading (HEURISTIC projections; the coordinator decides)

- TARGET 1.30. Projected price of a full rerun: about 2 times the measured 0.557 core-hours (factors 1.4 to 2.5
  above), so 1 to 2 core-hours on one core including some bisections in [2, 4]. A rerun's A_E^+ would be the maximum
  of its accepted bounds. It is below 1.30 only if no sub-cell reaches depth DMAX with a bound above 1.30; the stop
  rule does not guarantee that (AT1975). In the three pilot cells every accepted bound is below 1.30 (maxima 1.2958
  to 1.2974). If the full rerun ends with A = 1.2974, then with SC^+, OMF^+ as in T2_FAR_AE_v02 section 1 and either
  S_W^+ (the old 8603756200308751/144115188075855872 or the re-rounded 537734762519297/9007199254740992 of AT1929),
  s_max = c - [A + S_W^+ + OMF^+]/q >= 1.109776 (against 1.102062881091 now), i.e. a strain tolerance of about 0.0138
  above 137/125 instead of 0.0061.
- TARGET 1.25. Not reached by the present code at NTRY = 60000 and DMAX = 5 near |xi| = 3.6 (section 1). This is a
  measured limit of that code with those parameters, not an impossibility for other weights or methods (AT1978). The
  price factor is 8 on cell 4, 19 on cell 12 and, projected, about 80 on cell 72; the band [0.25, 4] has 75 base
  cells, so a full run would need something like 10 to 30 core-hours with the present code. With A = 1.2536 the
  formula would give s_max >= 1.130633 (with either S_W^+).
- Below about 1.26 the limit is the box enclosure, which treats t and v as independent intervals (T2_FAR_AE_v01
  section 5), not the cover. A sharper enclosure in t would be new code with a new audit; the second theory agent writes none without a
  decision.
- For scale only: the sampled maximum of the 013 strain is c - 1 = 0.8103 at the origin (the second numerics agent's FLOAT strain map,
  cited in the coordinator's notes), well below 137/125. A larger tolerance helps only if a certified whole-plane strain
  bound comes out above 137/125.

## 4. FLOAT check of the stored weights (scratch/ae_float_points.py; runs/ae_float_points_0157.log)

For each of the 324 stored sub-cells, the same Cauchy-Schwarz bracket with the stored weights c was evaluated by the
quadrature of choose_c (801 radial points, 240 angles) at t0, t0 + w/4, t0 + w/2, t0 + 3w/4 and t1, w = t1 - t0 (1620
points; core 41, 01:54:25Z to 01:56:15Z, 109.4 s), with the lead term evaluated at the point itself (the stored field
FLOAT_midpoint_bound adds lead_upper(t0), hence its slightly larger maximum 1.18880). The smallest difference
bound_upper - FLOAT value is 0.125553 (base cell 72, sub-cell 1, t = 3.6375; FLOAT 1.186515), the largest FLOAT value
is 1.186834 (base cell 12, sub-cell 1, t = 0.625). This extends the midpoint test of T2_FAR_AE_v02 section 5 to the
cell ends. It is a test, not a proof.

## 5. Status

- A_E^+ = 1.3135985491329587 is CONFIRMED (AT1891, audit v577), with its D_W inputs (AT1928, audit v589). The far
  inequality of route F-a at 137/125 holds with the re-rounded S_W^+ (AT1929; numerical audit exchange v532), margin
  71675071190082633/5629499534213120000 >= 0.012732050292300. The whole-plane strain bound (AT-1599) is OPEN.
- On version 1 (audit v603, 03:23:44Z): the stop-rule guarantee REFUTED (AT1975; corrected above); the seven pilot
  summaries, flags, box counts, row times, depths and maxima CONFIRMED as matching the frozen records (AT1976); a new
  A_E bound, a runtime guarantee, a general impossibility at 1.25 or any closure OPEN (AT1978). Projections stay
  HEURISTIC and the five-point check of section 4 stays FLOAT.
- Decision: no lower-TARGET rerun runs, to the stop (the coordinator 02:18Z item 3; 03:00Z item 4). Core 41 is assigned to
  the first theory agent (the coordinator 03:00Z item 3).
- Row C2 OPEN; no existence statement. Verdict unchanged: NO; O3 unresolved.

## 6. Files (SHA256)

- scratch/ae_float_points.py d51e25b8d2d56f7f3d2d5e42a1270179335c70307983202ae05f98ea6ffc23d7
- runs/ae_float_points_0157.log da90be4a790f1fe58de2e6bcd658067fa1c6d63c529a03c4c308b42d46e59849
- scratch/pilot_stats.py 09c3bae36b3df0ea01581d94ba27381f3f2cfb16c5ed2148f693ccc2d76de12a
- runs/ae_t125_pilot_0158.log 4a790710bbd6c0a1f69202417c264316ab8e96d9c6c3d55573fd20eac0f19269
- runs/ae_t125_pilot_0158_4_5.json 07c7ee2a38b64c1757386283cd55340282fd87b69e811a08f092924c9c0009c2
- runs/ae_t125_pilot_0158_12_13.json 8ad9683655fed8c58c227a0cab950d6232f399a9422e1a6bb6e04edabf9e3e7c
- runs/ae_t125_pilot_0158_72_73.json.partial fcbb59e6894ebb8b8644f054097f43c4a0bfab307642a3cbc0d6a2d5ef8abc60
- runs/ae_t125_pilot_0158_150_151.json cc52ce9360a54fc4bec0ad936682a2952d67c9eb4c997392abfc5ef94ea68708
- runs/ae_t130_pilot_0211.log 1f2160bb7b667a5beabf43d76357e64cb09c7f371d7f197f38b3109b9ec50f0c
- runs/ae_t130_pilot_0211_4_5.json 080d7c4a02d2730927a341381b7d3e4ee02b251e7f0f7e6c95a70acc4bd4112e
- runs/ae_t130_pilot_0211_12_13.json 596b13d8da0d1410d3ce120503dc8ec70e817ecd05df7791a30b6bf1a931b1a0
- runs/ae_t130_pilot_0211_72_73.json 6a8d1ee7d22f09839e82686cdd7fe5d5698c9ae006f1661cbeb03bd492f7f107
- notes/T2_FAR_AE_PILOT_v01.md ced7084b313e65fc714c54de86d3628965cbef572ee70dbc9323909e5b4bb487 (version 1)

## 7. Changes against T2_FAR_AE_PILOT_v01

- Title and header: the pilot cells per TARGET; the verdicts of audit v603.
- New paragraph on the stop rule (TARGET is not a guaranteed upper at depth DMAX; AT1975).
- Section 3: the TARGET 1.30 reading no longer says that the stop rule puts A_E^+ below 1.30; the TARGET 1.25 reading
  is a measured limit of the present code, not an impossibility (AT1978); s_max checked with both S_W^+.
- Section 5: status after AT1891, AT1928, AT1929 and AT1975 to AT1978.
