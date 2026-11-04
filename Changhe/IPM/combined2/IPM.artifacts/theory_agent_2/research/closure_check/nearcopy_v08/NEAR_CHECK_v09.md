# NEAR_CHECK_v09: the near check at C2-N1-013 with the direct NR-25 moment bound for a_n (the first theory agent; program near_check_v04.py, CLAIMED)

Written 2026-11-04 in a work session. NEAR_CHECK_v08 stays the record of the reviewed program near_check_v03.py at the
certified inputs; this version changes one term of the program and keeps every input. The new program and its
output are CLAIMED (the first theory agent) and not yet reviewed. The run is a dry run: eps_rest is an OPEN stand-in (value 0).

## 0. The change and why it is valid

near_check_v03.py bounds the absolute Fourier moment M4(a_n) = (2 pi)^-2 int |zeta|^4 |a_n^| only through the core
split a_n = a_r - a_c, a_c = c/(1 + 4|x|^2): M4(a_n) <= M4(a_c) + M4(a_r) <= 1024 c + M4^+(a_r), with
M4^+(a) = ((D4(a) D6(a) + D5(a)^2)/(2 pi))^(1/2) (NR-25 (iii)) at the D_m(a_r) uppers of the radial identity. The
split is what makes the tail term small (D6(a_r) <= 4.59579169e4 against D6(a_n) <= 63050.39273), but for the
moment it is worse: NR-25 (iii) applies to a_n itself (a real, measurable Fourier transform, finite D4 to D6; its
hypotheses are the ones under which the certified D_m(a_n) uppers are stated), and gives
M4(a_n) <= M4^+(a_n) <= 2.69196367334e3 at the certified uppers, against 1024 c + M4^+(a_r) <= 3.29387563990e3.
The direct value is the M4 upper 2691.963673338907009954203108 that the theory auditor's actual review checks (AT2871,
audit_v872) and the numerical auditor adopts (numerical audit exchange v917).

near_check_v04.py therefore uses M4(a_n) <= min(1024 c + M4^+(a_r), M4^+(a_n)) in the M4 term of e_up. The minimum
of two uppers is an upper, and the minimum of two functions that are nondecreasing in each D_m(a_n) upper and
nonincreasing in each K_m has the same monotonicity, so the threshold searches (c), (c') and the statement of
NEAR_CHECK_v03 section 6 keep their form. Every other formula, every input and every interface rule is unchanged;
the program prints both M4 uppers. The diff against near_check_v03.py is the docstring paragraph "Changes against
near_check_v03.py", the M4 lines of the formula list, the term label, the helper m4, the program name, the result
file name and one print line (the diff replaces 8 lines of near_check_v03.py by 26 lines).

## 1. Files

All paths are relative to the first theory agent agent. Run with Python 3.12.13 and python-flint 0.9.0. The SHA256 of every file
is in SHA256SUMS_v09.

| file | role |
|---|---|
| research/closure_check/near_check_v04.py | the program (new; one term changed against near_check_v03.py) |
| research/closure_check/near_params_v06.json | every input; the file of NEAR_CHECK_v08, unchanged (SHA256 96f06388...) |
| research/closure_check/run_nc09.sh | the run script |
| research/closure_check/near_check_v09.out | the dry run: `python3 -B near_check_v04.py near_params_v06.json > near_check_v09.out` |
| research/closure_check/near_check_v09.result.json | the result file that this run writes as near_check_v04.result.json, renamed |
| research/h4rest/hi_kq_v06.py, research/h4rest/hi_kq_v06.out | the HI' cuts of section 3 (in research/h4rest/SHA256SUMS_v06) |

The run was made by run_nc09.sh in a scratch copy of the program (cmp-identical), on core 41 at nice 19 with one
thread, from 2026-11-04T14:13:11.99Z to 14:13:12.16Z (0.17 s); hi_kq_v06.py ran from 14:13:12.16Z to 14:13:12.26Z.
An earlier manual run of the same commands (14:10:46.61Z to 14:10:46.84Z) gave byte-identical outputs. Against
near_check_v08.out the output differs only in the docstring, the new M4 line, the M4 term label and value, e_up,
the (a) and (a') margins and the (c), (c') and (d) targets; the price (b) is unchanged.

## 2. Dry run (near_check_v09.out; it proves nothing)

All entries are printed interface values. The Lambda, tail_B(a_c), tail_B(a_r) and e_nu terms, the D_m(a_r) uppers
and the price (b) equal those of NEAR_CHECK_v08 section 5.

| quantity | (11/20, 72), plan of record | (103/200, 68), registered fallback |
|---|---:|---:|
| M4 uppers: split, direct | 3.29387563990e3, 2.69196367334e3 | the same |
| M4 term A4c min(...)/mu^4 | 6.27517100611e-3 (v08: 7.67827334295e-3) | 7.88714636483e-3 (v08: 9.65067973862e-3) |
| e_up | 152627111489/10^12 | 180101237602/10^12 |
| e_up decrease against NEAR_CHECK_v08 | 1403102337/10^12 | 881766687/(5 10^11) |
| (a) cap-level margin, lower | 7.69209871099e-3 PASS | 1.52179725979e-2 PASS |
| (a') H4 rate margin at beta_* = 704955805507/10^12, eps_rest = 0, exact | 1164347009/(5 10^11) = 2.328694018e-3 PASS | 1970913581/(2 10^11) = 9.854567905e-3 PASS |
| (b) C_N_upper/D_lower, upper | 9.29740297910e-1 PASS | 9.14343229857e-1 PASS |
| (c) D6(a_n) target of (a) (sufficient) | 64981.4 | 66304.7 |
| (c') D6(a_n) target of (a') (sufficient) | 63629.8 | 65142.9 |
| (d) U targets of (a), (a') | 35.706, 25.427 | 46.979, 37.810 |
| required beta_* = b0 + e_up + eps_rest | 702627111489/10^12 + eps_rest | 347550618801/(5 10^11) + eps_rest |

Reading. If near_check_v04.py is confirmed, the rest room of the H4 join at the plan of record grows from
925591681/10^12 (NEAR_CHECK_v08) to 1164347009/(5 10^11) = 2.328694018e-3, a factor of about 2.52, and at the
fallback from 8091034531/10^12 to 1970913581/(2 10^11) = 9.854567905e-3. The ceiling rooms c + 1 - q - b0 - e_up
become 7.69209871099e-3 and 1.52179725979e-2 (their use needs the additional estimate of audit_v760). At the plan
of record the only input that is not certified is still eps_rest; at the fallback the mu 68 kernel uppers and
D_allow stay UNAUDITED.

## 3. Consequence for the Lemma HI' route of H4-REST (not part of the near check)

hi_kq_v06.py is hi_kq_v05.py with one addition: it prints the least integer cut at u for each coefficient (after
checking that the enclosure contains no integer) and adds these integers to the tested cuts. On
near_check_v08.result.json it reproduces hi_kq_v05.out (asserted), and on near_check_v07.result.json the cuts of
NR-34 (d), AT2774 and AT2775 (asserted). At the R of section 2 (NR-34; L2 = 3799152003154/10^12, AT2564;
u = 5123210549166463/10^15, AT2752, AT2753, conditional on the Fourier hypotheses):

| case | coefficient | least cut at L2 | least cut at u | least integer cut at u (v08) |
|---|---|---:|---:|---:|
| plan, R = 1164347009/(5 10^11) | K = c_tr' + 5q/2 | [167.890729992411, 167.890729992412] | [194.964026128795, 194.964026128796] | 195 (310) |
| plan | K_q = c_tr' + q | [140.968444179213, 140.968444179214] | [163.700374854132, 163.700374854133] | 164 (260) |
| plan | K_half = c_tr' + q/2 | [130.768385322863, 130.768385322864] | [151.855500860944, 151.855500860945] | 152 (241) |
| fallback, R = 1970913581/(2 10^11) | K | [81.613901212275, 81.613901212276] | [94.774588026046, 94.774588026047] | 95 (105) |
| fallback | K_q | [68.526622511025, 68.526622511026] | [79.576914236786, 79.576914236787] | 80 (88) |
| fallback | K_half | [63.568239186948, 63.568239186949] | [73.818964551323, 73.818964551324] | 74 (82) |

Decisions against the point lower u at the tested cuts (K_half necessary u_3 upper R mu_r^2/(phi K_half) in
brackets):

| case | mu_r | K | K_q | K_half |
|---|---:|---|---|---|
| plan | 152 [5.132965, 5.132966] | excluded | excluded | not excluded |
| plan | 164 [5.975425, 5.975426] | excluded | not excluded | not excluded |
| plan | 195 [8.447931, 8.447932] | not excluded | not excluded | not excluded |
| plan | 208 [9.611868, 9.611869] | not excluded (v08: excluded) | not excluded (v08: excluded) | not excluded (v08: excluded) |
| plan | 224 [11.147492, 11.147493] | not excluded (v08: excluded) | not excluded (v08: excluded) | not excluded (v08: excluded) |
| plan | 241 [12.903728, 12.903729] | not excluded (v08: excluded) | not excluded (v08: excluded) | not excluded |
| fallback | 72 [4.873840, 4.873841] | excluded | excluded | excluded |
| fallback | 74 [5.148369, 5.148370] | excluded | excluded | not excluded |
| fallback | 76 [5.430420, 5.430421] | excluded | excluded | not excluded (v08: excluded) |
| fallback | 80 [6.017086, 6.017087] | excluded | not excluded | not excluded |
| fallback | 82 [6.321701, 6.321702] | excluded | not excluded (v08: excluded) | not excluded |
| fallback | 88 [7.280675, 7.280676] | excluded | not excluded | not excluded |
| fallback | 95 [8.485032, 8.485033] | not excluded | not excluded | not excluded |

"Not excluded" means only that the necessary condition of NR-34 does not exclude the sufficient HI' estimate at that
cut; it is not an estimate. Exclusions apply to that sufficient estimate at that cut only, not to H4-REST, a larger
cut, a better rate or a different estimate. If near_check_v04.py is confirmed, the exclusions of the plan cuts 208,
224 and 241 (all three coefficients except K_half at 241) and of the fallback cuts 76 (K_half) and 82 (K_q) made at
the NEAR_CHECK_v07 and v08 rates no longer hold at the plan-of-record rate; they keep their v07 and v08 scope.

## 4. What is missing

- A review of near_check_v04.py and of this output.
- H4-REST: a certified eps_rest <= 1164347009/(5 10^11) at the plan of record with this program.
- For the fallback only: an audit of the mu 68 kernel uppers and of D at b0 0.515.
- H1 to H4 of NEAR_CHECK_v03 section 3 for the actual 013 near coefficient and the actual join.
