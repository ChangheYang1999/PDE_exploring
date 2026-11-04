# T2_FAR_F_v01: row F of the 013 far owner table (assembly at erflog 8, rho 1: what is certified after C5a, C5b and C1, and which hypotheses remain)

Agent the second theory agent, written 2026-11-03T15:28Z for the coordinator 14:05Z item 4(b) ("the second theory agent takes, in order, C5a, C5b and C1, then the
assembly F, which states what is then certified and which hypotheses remain"). Row F is that of
notes/T2_013_FAR_OWNERS_v01.md section 2.1. Proposition F below is CLAIMED and submitted to the theory auditor; it is an assembly:
its proof combines Lemma HSB (T2_FAR_v02 section 2.3, CONFIRMED conditionally by the theory auditor, AT-695 to AT-698) with
Theorems C5a, C5b (notes/T2_FAR_C5_v01.md, CONFIRMED, AT-1147 to AT-1152) and Theorem C1 (notes/T2_FAR_C1_v01.md,
CLAIMED, submitted 15:21Z). Paths are relative to research/h4/far009/ of agent the second theory agent unless another agent is named.
Every number marked FLOAT is a sampled value, not a bound.

## 0. Summary

1. Certified now (conditional on the audit of Theorem C1 and on its tool hypotheses): for the complete 013 far piece
   a_f at erflog 8, rho 1 (unwindowed, every angular mode), SC(a_f) <= SC^+ = 0.46564943200002806, so the SC
   condition SC^+ <= Gbar - S^+ of the direct route holds for every S^+ <= Gbar - SC^+ =
   8377636983468883/45035996273704960 (> 0.186020). The hypotheses of Lemma HSB on a_f (real, bounded, a_f^ a
   function with int |a_f^| (1 + |zeta|^2) finite, finite S_h^B for h = 1 and for Perron weights) hold by C5a and
   C5b. In particular HS Step 2 with Theorem C1 gives M_phi(v) <= SC^+ ||Phi v||^2 for every radial multiplier phi
   with values in [0, 1].
2. Proposition F (conditional far statement): if a certified S^+ >= S_h^B (rows C3, C4) and a certified
   A_low^+ >= A_low(8 pi) (row C2) satisfy S^+ <= Gbar - SC^+ and A_low^+ <= Gbar - S^+ (exact comparison), then
   B_(a_f)(g) <= [max(SC^+, A_low^+) + S^+] ||J^-1 g||^2 <= Gbar ||J^-1 g||^2 for every g in the test class. With a
   certified strain bound s_* <= 3/2 (row C6) the far side of the split is admissible at the strain target 3/2.
3. Open: C2 (blocked; no construction of A_low^+(8 pi) is known that can finish before the stop), C3 and C4 (not
   started), C6 (the numerical auditor), C7 (near side, the first theory agent), and the binding D0 of the C1 manifest to the 013 identity (the theory auditor).
   So after C1 the far theorem at this split reduces to C2, C3 with C4, C6 and the binding D0.
4. By-products of C1 for other rows: sup_x lambda_max(D^2 a_f) <= 0.2134920580043215 (row T3 allows up to 0.229 at
   the FLOAT remainders), and osc(w a_f) <= 0.7719 for every measurable w with 0 <= w <= 1 (a_f itself, and the
   windowed piece a_W of route F-a for every Rw and Ww), an interval upper O^+ usable in route (a) (AT-882 to AT-885).
5. With the FLOAT inputs S_h^B 0.0227 and band value 0.3848 (not bounds), the exact comparison of code/c1/f_assembly.py
   gives the far constant 0.48835 and the rooms 0.16332 (SC condition) and 0.24417 (band condition)
   (runs/f_assembly_float_1523.json; this is an illustration of row F, not a certificate).

## 1. Status of the rows of section 2.1 of T2_013_FAR_OWNERS_v01

| row | content | status at 2026-11-03T15:28Z | where |
|---|---|---|---|
| D0 | identity binding and containing arithmetic | C1 and C5 read only data/C1-N1-007_exact.json (SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21) and inputs013/phi_007_b18s2_phi_exact.json (SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a, the raw correction hash a16e9d85... of D0); C1 uses arb ball arithmetic with upward rounding of every binary64 output, and no binary64 table enters it. The binding of the C1 manifest (T2_FAR_C1_v01 section 6) to the 013 identity is the theory auditor's: requested | T2_FAR_C1_v01 sections 4, 6 |
| C5a | a_f real, bounded, even in x_1 and x_2; quadrant reduction | CONFIRMED (AT-1147 to AT-1152) | T2_FAR_C5_v01 |
| C5b | hypotheses of NR-21 case B; a_f in S^(-lambda) | CONFIRMED (AT-1147 to AT-1152); qualitative: the constants A_beta are not enclosed | T2_FAR_C5_v01 |
| C0 | unwindowed, all angular modes | satisfied by C1 (no window; every angular mode, that is the 161 complex modes n = -160, ..., 160, n even, of a_f); C3 and C4 must satisfy it as well | T2_FAR_C1_v01 section 1 |
| C1 | SC^+ >= SC(a_f), SC^+ <= Gbar - S^+ | CLAIMED, submitted 15:21Z: SC^+ = 0.46564943200002806; the condition holds for S^+ <= 0.186020 | T2_FAR_C1_v01 |
| C3 | majorant m >= abs(a_f^) and signed enclosures | OPEN, not started (HEURISTIC cost 16 to 30 hours of code) | owner table |
| C4 | S^+ >= S_h^B from m | OPEN, needs C3 (FLOAT S_h^B 0.0227 Perron weight, 0.0262 h = 1, at Rw 50, Ww 10) | owner table |
| C2 | A_low^+ >= A_low(8 pi), A_low^+ <= Gbar - S^+ | OPEN, blocked (the second numerics agent 11:48Z; the theory auditor AT-873 to AT-875: a HEURISTIC implementation assessment, not an exclusion); FLOAT band value 0.3848 | owner table |
| C6 | certified strain bound s_* <= 3/2 | OPEN (the numerical auditor); FLOAT level c - HSB-R/q = 1.5834 | owner table |
| C7 | near side at the same split | The first theory agent (note 48 item 1: NR-27 PROVED conditionally, AT-1094, AT-1134; near windows HEURISTIC, AT-1122, AT-1137; near closure OPEN, AT-1097) | The first theory agent |

## 2. Proposition F

Setting. c, q = 21/10, Gbar = q (c - 3/2) = 14674311533937489/22517998136852480, and a_f = chi_E(|x|) atil_013(x) at the
erflog cut lam = 8, rho = 1, unwindowed and with all angular modes, as in notes/T2_FAR_C5_v01.md section 1 and
Theorem C1. K = 2 pi, K' = 8 pi, the ramp alpha, theta, phi, the kernels Ktil, P, r_B, the band constant A_low(K'),
the Schur supremum S_h^B, the form B_a and the test class are those of T2_FAR_v02 section 2.3 (Lemma HSB). SC^+ is
the binary64 number 0.46564943200002806 of Theorem C1.

Proposition F (CLAIMED). Let h : R^2 -> (0, infinity) be measurable, and assume
(F1) [rows C3, C4] S_h^B(a_f; K, K', h) <= S^+ for a number S^+;
(F2) [row C2] A_low(K') <= A_low^+ for a number A_low^+, A_low(K') the continuum band constant of a_f on the closed
     disk |xi| <= K';
(F3) S^+ <= Gbar - SC^+ = 8377636983468883/45035996273704960 and A_low^+ <= Gbar - S^+.
Then for every g in the test class
    B_(a_f)(g) <= A ||J^-1 g||^2,   A = max(SC^+, A_low^+) + S^+ <= Gbar.
If moreover (F4) [row C6] a certified global strain bound s_* <= 3/2 holds, the far constant A meets the gain
G = q (c - s_*) >= Gbar, so the far side of the split erflog 8, rho 1 is admissible at the strain target 3/2. The near
side (row C7) and the identity binding (row D0) are separate inputs of the split and are not part of this statement.

Proof. Lemma HSB needs a real and bounded with a^ a function and int |a^(zeta)| (1 + |zeta|^2) d zeta finite: a_f is
real and C-infinity (Theorem C5a), bounded (Theorem C1 (iii): -0.33547165257164097 <= a_f <= 0.436419343821821),
and its Fourier transform is a function with that moment finite (Theorem C5b with the AT-1021 lemma). S_h^B is
finite (Theorem C5b (iv) for the weights listed there, and in any case by (F1)). Lemma HSB then gives
B_(a_f)(g) <= [max(SC(a_f), A_low(K')) + S_h^B] ||J^-1 g||^2. By Theorem C1, SC(a_f) <= SC^+; with (F1), (F2) and
the monotonicity of max and of the sum, the bracket is at most A. Finally
max(SC^+, A_low^+) + S^+ <= Gbar holds exactly when SC^+ + S^+ <= Gbar and A_low^+ + S^+ <= Gbar, which is (F3). For
the last sentence, G = q (c - s_*) >= q (c - 3/2) = Gbar when s_* <= 3/2. QED.

Row-wise form. Under the same hypotheses, Corollary HSB-R (CONFIRMED conditionally, AT-706) gives the bound with the
constant ess sup_xi [SC(a_f) phi(|xi|)^2 + A_low(K') theta(|xi|)^2 + rho_h^B(xi)] in place of max(SC, A_low) + S_h^B.
Theorem C1 enters it in the same way (SC(a_f) phi^2 <= SC^+ phi^2 and A_low(K') theta^2 <= A_low^+ theta^2), so with
a certified row bound R^+(xi) >= rho_h^B(xi) the condition reads ess sup_xi [SC^+ phi^2 + A_low^+ theta^2 + R^+] <=
Gbar.

Exact comparison (code/c1/f_assembly.py). Given S^+ and A_low^+ as decimal strings or binary64 numbers, it reads
SC^+ as the largest of the three region bounds of Theorem C1 from runs/c1_r2_1508.jsonl and runs/c1_tails_1507.json,
checks Gbar = q (c - 3/2) from the exact c of the 013 input, and evaluates (F3) and A in exact rational arithmetic.
Whether its inputs are bounds is stated by its label argument; at present only SC^+ is certified.

## 3. What C1 adds to other rows

1. Row T3 (TS fallback, Lemma HB'). Theorem C1 (ii): sup_x lambda_max(D^2 a_f(x)) <= Lambda_+^+ = 0.2134920580043215,
   against the FLOAT value 0.2110 and the 0.2110 + 0.018 = 0.229 that T3 allows at the FLOAT remainders. The other
   inputs of T3 (the remainder integrals of Lemma HB' from m) need C3.
2. Oscillation uppers. Let AFL = -0.33547165257164097 and AFU = 0.436419343821821 be the bounds of Theorem C1 (iii).
   Since AFL < 0 < AFU, every measurable w with 0 <= w <= 1 gives AFL <= min(0, a_f(x)) <= w(x) a_f(x) <= max(0,
   a_f(x)) <= AFU, so osc(w a_f) <= AFU - AFL = 13905152014912945/18014398509481984 (0.771890996393462 rounded) <=
   0.7719. This covers a_f (sampled osc 0.7711), the windowed piece a_W = a_f (1 - Sinf((r - Rw)/Ww)) of route F-a
   for every Rw and Ww (row FA3), and the tail a_t of route F-a (row FA5), where it is far above the FLOAT tail
   oscillation (0.135 to 0.265) and so of no use. As O^+ in route (a) (AT-882 to AT-885: an interval upper of osc
   used consistently), it exceeds the sampled oscillation by about 0.0008.
3. Route F-a, row FA1. Theorem C1 is for the unwindowed a_f. On route F-a, Lemma HSB is applied to a_W, whose SC
   includes the window transition on Rw <= r <= Rw + Ww. The product rule of Lemma P (T2_FAR_C1_v01 section 3)
   holds for any smooth radial factor, but the engine has not been run with the window factor, so SC(a_W) is not
   bounded. On this route SC enters only through max(SC^+, A_E^+) with A_E far above SC (row FA1), so coarse panels
   would suffice.
4. Split log 16, rho 2, row L1. Not covered: the log cut is not analytic at its two ends (T2_FAR_C1_v01 section 5
   item 4).

## 4. Remaining hypotheses, in the order of the far inequality

1. C2: A_low^+(8 pi) <= Gbar - S^+, a certified upper of the continuum band constant. The FLOAT band value is 0.3848
   and the band budget Gbar - S at the FLOAT S = 0.0227 is 0.62897; no construction that can finish before the stop
   is known.
2. C3 and C4: a certified S^+, which by C1 may be as large as 0.186020 for the SC condition (FLOAT S_h^B 0.0227, so
   the majorant m may inflate the rows by a factor of about 8 before the SC condition fails; the band condition
   then needs A_low^+ <= Gbar - S^+).
3. C6: s_* <= 3/2 (the numerical auditor); C7: the near side (the first theory agent); D0: the binding of the manifests of C1 and of every later
   certified number to the 013 identity (the theory auditor).

## 5. Evidence

    python3 code/c1/f_assembly.py 0.0227 0.3848 "FLOAT inputs (S_h^B Perron weight, band value 8 pi): not bounds;
        illustration of the exact comparison only" runs/f_assembly_float_1523.json
(the label is one argument; it is broken here for the line length). For certified inputs, replace the two numbers
by S^+ and A_low^+ and the label accordingly.

| file | role | SHA256 |
|---|---|---|
| code/c1/f_assembly.py | exact comparison of row F (section 2) | 93327e77e4a498e8795e86225bd4733453a593ca997c90aec0d48a4ac2aa9c02 |
| runs/f_assembly_float_1523.json | FLOAT illustration (not a certificate) | 104698bc4301ded9135b0af881d4d60bb4e5f9538c99de17cd65ab24db12510c |
| runs/c1_r2_1508.jsonl | Region II of Theorem C1 (input of f_assembly.py) | c094d5ab2f924c00c97a5894ed3af0352a48cd515c460f7c3bf893d260869bd3 |
| runs/c1_tails_1507.json | Regions I and III of Theorem C1 (input of f_assembly.py) | 9c683ee8a79f3f1f597043242ffc951a75e3dc115e13d26b64a2a76656a9a8e8 |
| inputs013/phi_007_b18s2_phi_exact.json | exact c (input of f_assembly.py) | a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a |
| notes/T2_FAR_C1_v01.md (agent directory) | Theorem C1 | a00ee53fdcfc379b636c655e2316dc5440903568974cdffcfeea6a268a72b18b |
| notes/T2_FAR_C5_v01.md (agent directory) | Theorems C5a, C5b | ad85f093ec2ce587dbf18e3823236856fbabb4724012c593041e2fce54adf377 |
