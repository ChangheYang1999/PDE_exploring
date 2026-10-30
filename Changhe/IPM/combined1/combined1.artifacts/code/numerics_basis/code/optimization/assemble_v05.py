# Assemble numerics_v05 from the draft: header, corrections (theory_v02 R5, R10a, c1-n4 02:04Z wording), sections 5b/6/7 extended, section 8 and R3.
import re, subprocess, datetime, hashlib, json, os
root='RUN_ROOT/numerics_N1N2'
src=open(f'{root}/numerics/NUMERICS_v05_draft.md').read()
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
tables=subprocess.run(['python3','-B',f'{root}/numerics/optimization/v05_tables.py'],capture_output=True,text=True,cwd=f'{root}/numerics/optimization').stdout
blocks=tables.split('\n\n')
pt_table=blocks[0]; dy009=blocks[1]; dy010=blocks[2]; weak=blocks[3]
weak008=[l for l in weak.splitlines() if l.startswith('C1-N1-008')]
weak008=weak008[0] if weak008 else 'C1-N1-008: weak tests pending.'
# header
src=src.replace('# numerics_v05 (batch N publication; author c1-n1) -- DRAFT','# numerics_v05 (batch N publication; author c1-n1)')
src=re.sub(r'- version: numerics_v05 \(DRAFT\); supersedes numerics_v04 \(sha256 1aab468111951bce33f78f6f83c9ec00c5686cb0682b13b96ba2f93a1974ce9b\); supersedes numerics_v03 \(sha256 4d91a51db33f7f258fca54a48ec718e11a4ed26c78bb5eb3f41d8e2d688290a8\); UTC time: 2026-10-29T00:21:10Z;',
 f'- version: numerics_v05; UTC time: {now}; supersedes numerics_v04 (sha256 1aab468111951bce33f78f6f83c9ec00c5686cb0682b13b96ba2f93a1974ce9b), numerics_v03 (sha256 4d91a51db33f7f258fca54a48ec718e11a4ed26c78bb5eb3f41d8e2d688290a8);',src)
src=src.replace("""- consulted (v05): theory_v02.md (c1-t1, 2026-10-29T01:44Z; sections 0, 2, 5.2, 9, R read; ACK in c1-n1/RUN_STATUS.md 01:49Z); theory_v01.md;
  c1-coord NOTES_FOR_TEAM.md (through 01:06Z), CONTRACTS v01-v04, closure_matrix (latest); c1-n4 VERIFY_REPORT.md entries cited in theory_v02 (N4-091, N4-098,
  N4-102, N4-103, N4-106, N4-113 to N4-115) and NOTES_FOR_TEAM.md (through 23:45Z); c1-n3 NOTES_FOR_TEAM.md (22:35Z) and RUN_STATUS.md; astra/farfield-structure/answer.md.""",
"""- consulted (v05): theory_v02.md (c1-t1, 2026-10-29T01:44Z; sections 0, 2, 5.2, 8, 9 and R read; ACK in c1-n1/RUN_STATUS.md 01:49Z); theory_v01.md;
  c1-coord NOTES_FOR_TEAM.md through 02:23Z (closure matrix v31; requests of 01:47Z, 02:10Z, 02:19Z) and CONTRACTS; c1-n4 NOTES_FOR_TEAM.md through 02:27Z
  (N4-131 to N4-142: 007 G0 and theta CONFIRMED, FW-T-DYADIC-Y-v1 excluded at 007 for every 0 < a < 2, 009 kappa 0.71321 CONFIRMED, 010 point exclusions
  CONFIRMED, rounded-coefficient cutoff a > 2/c, multi-scale moment integrator N4-137) and RUN_STATUS.md; c1-n3 NOTES_FOR_TEAM.md through 02:28Z (007
  VALIDATED G0, rF, G1, P2; exact N_a(d2) validation of wlap_norms.py; exact N_a(007) running) and RUN_STATUS.md; astra/farfield-structure/answer.md.
  Batch N consultation for this version: c1-n3 and c1-n4 results above are cited with their IDs; no number of theirs is restated as mine.""")
# theory_v02 R5: fix the refuted sentence in 3b
old58="consequence (exact pure-exterior formula, FULL-CIRCLE norms): with onset T = 10 the tail cost ||F||_(L^2(r>T)) never decreases with the number of\nexact branches (143 to 164 for 7 to 8 branches, 590 at 12, 1008 at 13, 812 at 16: the growth of the amplitudes wins); with T = 100 it falls by a"
new58="consequence (exact pure-exterior formula, FULL-CIRCLE norms): with onset T = 10 the tail cost ||F||_(L^2(r>T)) does NOT decrease systematically with\nthe number of exact branches: it is 143 to 164 for 7 to 8 branches, 944 at 9, 449 at 10, 590 at 12, 1008 at 13, 812 at 16 (not monotone: order 9 exceeds\norder 10, N4-103; the growth of the amplitudes balances the decay); with T = 100 it falls by a"
assert old58 in src; src=src.replace(old58,new58)
# wording: finite asymptotic far correction (c1-n4 02:04Z)
src=src.replace("cell test are computed FLOAT by optimization/weak_tests.py (I_k with the exact-sector far part, A_k, B_k, C_k on the mesh region, exact H_k);",
 "cell test are computed FLOAT by optimization/weak_tests.py (I_k = mesh quadrature plus a finite asymptotic far correction beyond r = 8356.47 from the\nexact surviving sectors, not an exact far part; A_k, B_k, C_k on the mesh region; exact H_k);")
src=src.replace("## 5b. theory_v02 cheap tests (FLOAT; optimization/weak_tests.py; rule radial Gauss 32/panel x midpoint 180 on 0.02 <= r <= 8356.47; I_k far parts exact)",
 "## 5b. theory_v02 cheap tests (FLOAT; optimization/weak_tests.py; rule radial Gauss 32/panel x midpoint 180 on 0.02 <= r <= 8356.47; I_k with a finite asymptotic far correction from the exact surviving sectors beyond 8356.47)")
src=src.replace("The weak probe (N4-053, T2-R3 Proposition W) is reported as the pairing <F, y/(1+r^2)^2> (mesh part plus the exact far part from the sin(theta)",
 "The weak probe (N4-053, T2-R3 Proposition W) is reported as the pairing <F, y/(1+r^2)^2> (mesh part plus a finite asymptotic far correction from the sin(theta)")
# 5b: replace the pending line with the 008 row and the ordering
old="(008 and the d2 calibration row: at publication.)"
new=weak008+"""
Reading of 008: its weak distance is between those of 007 and 010; like 009 and 010 its k = 0 pairing is created in 0.5 <= r < 8 with one sign (no
cancellation between annuli), whereas 007's pairing changes sign at r = 2 and is 60x smaller in total: the E_2-balanced objective with the rF term is
the only one of our objectives that keeps the weak pairing small, and it does so by cancellation, not by a small pointwise residual.
The d2 calibration row of weak_tests.py (expected pairing -0.0288 and distance 0.2955 against N4-053 / T4-064) is running (core 54) and will be in
v06; until then the FLOAT distances above are calibrated only through 007 (3.79e-5 FLOAT against N4-091's certified 4.3987e-5, a 14 percent
difference that is consistent with the mesh quadrature of the A_k, B_k, C_k denominators and the finite far correction; the FLOAT value is NOT a bound)."""
assert old in src; src=src.replace(old,new)
# section 6: add dyadic 009/010 after the 007 reading line
anchor="Reading for 007: largest L^2 annulus [4, 8) with 43 percent of ||F||_2^2; the balanced objective removed the near-field peak of 005 (sup|F| 0.138 at r = 2-4)."
assert anchor in src
src=src.replace(anchor, anchor+"\n"+dy009+"\n"+dy010+"""
Reading across 007, 009, 010 (theory_v02 R10d): the L^2 mass of every balanced candidate sits in 2 <= r < 64 (mid field), the derivative energy in
0.5 <= r < 8, and the weak pairing is created in 0.5 <= r < 8 (section 5b). The far field beyond r = 64 contributes less than 1e-6 to the pairing and
less than 2 percent to G0^2 for 007 and 009; for 010 the legqs functions at scale R0 = 100 leave a visible bump in ||rF|| at 256 <= r < 2048
(46 to 124 against 3 to 4 for 007), which is why its rF is 187 against 7.8.""")
# section 7: replace the point-test table
i=src.index('## 7. Point tests'); j=src.index('## 7b.')
sec7=src[i:j]
k=sec7.index('| candidate |')
newsec7=sec7[:k]+pt_table.replace('| C1-N1-007-d2w-j7-e2bal |','| C1-N1-007-d2w-j7-e2bal |')+"\n"
# keep the old d2/005/006 rows
oldrows=[l for l in sec7.splitlines() if l.startswith('| C1-A2-d2') or l.startswith('| C1-N1-005') or l.startswith('| C1-N1-006')]
lines=newsec7.splitlines()
hdr_end=[n for n,l in enumerate(lines) if l.startswith('|---')][0]
lines=lines[:hdr_end+1]+oldrows+lines[hdr_end+1:]
newsec7='\n'.join(lines)+"\n"+"""The framework balls have radius 2^-14 (FW-T-T4L2-v1) to 2^-16 (FW-A2-Db): every candidate, d2 included, is excluded by these maxima by 2 to 4 orders
of magnitude (consistent with T4-007/T4-055; the CONFIRMED exact point exclusions are N4-106 (008), N4-115 (009), N4-123 (010)). 009 has the smallest
FLOAT R_nec (7.7e-4) but the largest weak distance of the three balanced candidates (section 5b): the point tests and the weak distance pull in
different directions under our objectives, and the weak distance is the one that excludes 007 (coordinator matrix v31: every snapshot 001 to 010 is
RULED OUT in every specified ball by its fixed-c L^2 distance).
"""
src=src[:i]+newsec7+src[j:]
# section 8: rewrite
i=src.index('## 8. Next steps')
src=src[:i]+f"""## 8. Status at publication, next steps (batch N) and what the theory should take from v05
Status (FLOAT unless stated). Best candidate: C1-N1-007 (certified: G0 0.37668932 (N3 VALIDATED, N4-139 CONFIRMED), theta <= 2/25 and (B-L2) with
kappa_HS 0.72816 (N4-111/T4-162 CONFIRMED), fixed-c L^2 distance LB 4.3987e-5 (N4-091 CONFIRMED)). It misses FW-T-T4L2-sharpw-v1 by a certified
factor above 1.83e6 in X_(s,w) (c1-coord v31) and is excluded from every registered ball by the weak distance (budget <= 3.8e-6 scalar, 4.6e-4 graded).
Every other snapshot is worse in the weak distance by a factor 60 (010) to 160 (009). FW-T-DYADIC-Y-v1 is RULED OUT at 007 for every 0 < a < 2
(N4-132, AUDITED conditional), so my FLOAT N_a values in section 5b are now calibration data only; c1-n3's exact N_a(007) (running, about 03:15Z)
decides the FLOAT disagreement with c1-t1's partial sums (N4's reading: the partial sum over modes 1 to 15 and my all-mode value need not agree).
Running (CPU, cores 52 and 53; each about 150 s per Gauss-Newton step on the reduced radial rule): (a) E_2-balanced + legqs multi-scale functions from
007, 20 steps (step 17 at 02:30Z, objective 1.707e7 against 1.711e7 at the start: a plateau); (b) E_2-balanced with kappa penalty 1e7 from 009, 30 steps
(step 22 at 02:30Z, objective 1.82e8, rejections dominate: plateau). Both will be snapshotted (011, 012) with weak tests first (theory_v02 order), then
point tests and the section 5 table; expected before 03:30Z. Neither is expected to beat 007 in the weak distance.
Next (in order):
1. Weak-pairing rows. The nine pairings I_k = <F, phi_k>, k = 0..8, of NORM-T-WEAK-v1 are linear in F (quadratic in the coefficients) and will enter the
   balanced objective as nine explicit residual rows with weight w_k such that w_k |I_k| of order 1e-5 competes with the other terms (w_k about
   2^18 x 1e2 / 1e-5); implementation as extra rows in ipm_opt2 (like the kappa row), run from 007 on CPU (reduced mesh, 20 steps). Target: weak
   distance below 3.8e-6 (factor 11.6) while (B-L2) (kappa margin), G0 and sup|F| stay within 20 percent of 007. This is a test of whether the
   exclusion by NC-T-DIST is a soft constraint of the objective or a structural obstruction of the basis. Note for the theory: driving I_k to zero
   removes the exclusion by these nine test functions, it does not make the candidate pass a sufficient condition; the smallness gap of 1.8e6 in
   X_(s,w) is untouched by it.
2. If 1 succeeds in FLOAT: exact snapshot 013 and the weak distance certified by c1-n4 (N4-091 method); if it fails (G0 or kappa blow up), report the
   trade-off curve (weak distance against G0 and kappa) as the quantitative answer to "can the fixed-c L^2 distance be optimized away".
3. Message to batch T (unchanged from v01, now quantified): the number of exact branches is cheap (eight exact branches, eleven EXACT-ZERO sectors in
   every balanced candidate); the mid-field accuracy out to r of order 100 to 1000 is the lever for every framework; (B-L2) is a real design
   constraint that the raw L^2-weighted objectives violate (008, 010) and the balanced objective satisfies with margins +0.072 (007) to +0.087 (009);
   the fixed-c L^2 distance is created in 0.5 <= r < 8 by all our objectives; a theory whose ball is not centered at the fixed c (or whose distance
   test allows the scaling direction) would remove the exclusion that now rules out every snapshot, and the quantitative evidence for that request
   is section 5b.
4. CPU-only consequences (honest statement): one Gauss-Newton step for 2982 generators takes 150 s on one core; 20-step runs take about one hour.
   No run with the full radial rule (416 panels) or with more than about 4000 generators is feasible before the freeze; the multi-scale (legqs)
   designs with R0 = 1000, which section 3b identifies as the lever for the mid field beyond r = 100, cannot be optimized within the budget on CPU.
   They are documented as the first item of the continuation plan (NUMERICS_FINAL.md section 7).
""" 
open(f'{root}/numerics/NUMERICS_v05_published.md','w').write(src)
h=hashlib.sha256(open(f'{root}/numerics/NUMERICS_v05_published.md','rb').read()).hexdigest()
print(now, h, len(src))
