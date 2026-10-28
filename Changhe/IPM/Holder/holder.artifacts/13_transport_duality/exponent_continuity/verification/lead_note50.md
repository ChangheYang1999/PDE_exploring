## Note 50 (2026-10-28T13:12Z): report v30 written (audit requested); V199 cross-read: CONFIRMED

To the verification work.

1. FINAL_REPORT.md is now version 30 (stamp 13:09Z, sha256 13665052...; edit script scratch/edit_v30.py, which asserts
   CONFIRMED + ledger for V190, V195, V196, V198 and the exact V190/V198 decimals before writing). Changes:
   - Table 1 D column = your V198 safe_upper_D values (6-decimal ceilings; identical to data/verified_table.md); ratios for D
     1.0002, 1.0020, 1.0148, 1.0343, 1.0568, 1.0666, 1.0784, 1.0729, 1.0435, 1.0072; Section 0 maximum 1.0784 at 1/2.
   - Theorem 3.8 tail: the cross2048 paragraph (V190 values, with your stated scope: all-node Cartesian float diagnostic,
     not a second interval run; unchanged-program check; 102-endpoint recombination at 384/768 bits).
   - New Theorem 3.9 (strict saving in the identity term; V195 + V198): statement with p, q, J, K, eta(s) = pJs^2 + qKs^4,
     parts (a) Theorems 3.3-3.6 at s = 1/2, (b) D_alpha <= G - eta(s^D) < G for every alpha (s^D <= 2^(alpha-1)(3-alpha) < 2),
     (c) the retained-edge cutoff form for J_D with the rho^4/512 and rho^6/49152 corrections; a compact proof; the
     ten-row value table (previous bound, source, saving, new bound).
   - Section 8(4): your V192 wording (separation for all sufficiently small alpha, no explicit threshold; global case open);
     Section 0 and Section 10 item 2 likewise. Section 8(2): D_alpha < G(alpha) strictly.
   - Literature item 2: V196 (direct proof of the periodic Hilbert constants, without the announced theorem).
   - Notation: Theorem 1.4's local A, B, s, s_0 renamed calligraphic/tilde; kappa in Theorem 3.2 renamed kappa_Q.
   - Fixes: Theorem 3.3 "Table 1 uses m = 32" -> "the certified evaluations of U_m use"; 0.8684 -> 0.8680 (twice;
     42.2175842339 - 3sqrt3/(0.04 pi) = 0.86795); Theorem 4.6 proof and Theorem 5.7 numerical paragraph cite 3.8.
   - Section 10 item 7: the Q + atom LP (the numerics work 12:32Z, heuristic) and the conclusion that the remaining D excess comes
     from the decoupling. Section 11 and the artifacts README list cross2048, strict_increment, strict_separation_near_zero
     and hilbert_periodic_direct. New Section 12 "Time spent".
   Please audit v30 (text and decimals). Artifacts re-synced at 13:10Z; table1.md regenerated from the copied data agrees.

2. V199 (13_transport_duality/exponent_continuity/PROOF.md, sha c95ac9b0...): CONFIRMED on my cross-read. Checked:
   a_2 <= 1/pi (concavity of 2 + t - 2^(1+t/2) on [0,1]); the Jordan mass of each truncated signed measure is at most
   m = (2/pi) log((R + 1/2)/epsilon) (plus 1/2 for the identity atom of D); all supports lie in B(0, R); the mean-value
   bound |d^alpha - d^beta| <= L |alpha - beta| with L = max(1/(e a), (2R)^b log(2R)) on [a, b] for d in (0, 2R]; the three
   terms of Ebar (inner principal-value disk 2 eps^a/(pi a), pole-neighbourhood term, outer tail with 2^b R^(b-1)/(1-b)); and
   |sup A - sup B| <= sup |A - B| over the common unit ball and phases. Remark only: with practical cutoffs the
   neighbourhoods are tiny (my estimate about 5e-7 around alpha = 1/2 for the existing gap 0.2597), so v31 will state V199
   qualitatively (continuity of C and D; each certified gap persists on an open neighbourhood) and not quote widths.

3. Next on my side: cross-reads of V202 (sharp deficiency, J_C/J_D; this also moves the Section 0 constants 2.8310 and
   2.9572 if you evaluate it), V200 and V201, in that order. cross4096 is at 2400/4096 cells (13:06Z), due about 13:45Z;
   Note 51 will follow with its recombination, with and without the V198 saving.

