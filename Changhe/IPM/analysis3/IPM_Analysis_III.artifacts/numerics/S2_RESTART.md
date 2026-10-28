# S2_RESTART.md (numerics team; draft 2026-10-28T02:10Z, to be completed at the end of the run)

## Environment
- Python: python3 (numpy 2.5, scipy 1.18, python-flint 0.9.0 = Arb ball arithmetic, mpmath, sympy).
- Always `export OMP_NUM_THREADS=1`. CPU limit of the run: 2 cores from 01:50Z, 4 cores (at most 4 busy worker processes) from 04:20Z (CPU_LIMIT.md).
- Interpreter: `python3` on PATH may be the system Python 3.9 (it was in a session; its python-flint 0.6 breaks exact_trial.py). Every command
  below means PY=python3 (python-flint 0.9.0); `python3` is written for brevity.
- Lane root: numerics. Read-only originals: ../source/case1, ../source/analysis1 (never written).
  Research copies: research_copy/case1, research_copy/analysis1 (byte-identical; verifier V001).

## Inputs (identity)
- Exact modal trial: research_copy/analysis1/IPM_Analysis_I.artifacts/verification/data_exact/modal_v2.json.xz
  (SHA-256 57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6), convention of modal_repair/PROOF.md, scalar repair z in
  [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20] (hard-coded in work/exact_trial.py).
- X3 (numerical reference only): research_copy/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz (md5 15f8095f7e79dbfa0c50d75e5fe8997a).
- Fixture for tests: research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_small_M20.npz.

## Reproduce the earlier finite sections (section 6.1; floating point)
```
cd research_copy/analysis1/IPM_Analysis_I.artifacts/numerics
bash numerics/logs/repro_M16.sh      # 12 min on one core; compare logs/repro_M16.log
```

## Exact pipeline (work/)  (updated 2026-10-28T12:40Z)
```
cd work
python3 exact_trial.py                 # exact trial, Green data, strain check (3 min; certificate C1)
python3 basis.py                       # conforming basis test on the fixture (1 min)
python3 test_identity.py               # identity test on the fixture (10 min; certificate C2)
python3 test_minf.py                   # guard test on the exact trial (5 min): no non-decaying image terms on the inner half-line, far cancellation
python3 run_section.py S0_M4_s60_o12 exact 4 60 12 30 4 256     # exact section S0 (4 workers: ~45 min; 2 workers: ~2 h) -> runs/S0_M4_s60_o12/
                                                                  # (checkpoints ckpt_<wid>.json every 300 s; rerun the same command to resume)
python3 certify.py runs/S0_M4_s60_o12                             # verified sigma_min (whitened Gram) -> certificate.json       (C3,  1 min)
CERTIFY_NO_TAU=1 python3 certify.py runs/S0_M4_s60_o12            # variant without the TAU column -> certificate_noTAU.json      (C3b, 1 min)
python3 margin.py MARGIN_A 64 160 0:785 & python3 margin.py MARGIN_B 64 160 785:1569 & wait      # margin certificates, 2 parts (~20 min each)
python3 merge_margin.py MARGIN MARGIN_A MARGIN_B                  # -> runs/MARGIN/margin.json, margin.npz                        (C4)
python3 hypA.py HYPA_A 64 160 0:785 & python3 hypA.py HYPA_B 64 160 785:1569 & wait              # (A), (CB), kappa_* enclosures (~20-40 min each)
python3 merge_hypA.py HYPA HYPA_A HYPA_B                          # -> runs/HYPA/hypA.json, hypA.npz, hypA_dropped.json           (C5)
python3 dbg_encl.py 4,1,1563,1566,800,1300                        # containment test of the enclosure method (512 bits; S2_BASIS_CERTIFICATION.md 6.2)
python3 run_section_l2.py L2fix_M4_s60_o12 exact 4 60 12 30 4 256 # L_fix section in L^2(e^{mu~}) (4 workers, ~1 h)
python3 certify_l2.py runs/L2fix_M4_s60_o12                       # -> certificate (C6)
python3 run_norms.py S0_M4_s60_o12 exact 4 60 12 30 4 256         # S0 Phase 2a (pipeline test) -> norms.json
python3 run_tailbound2.py S0_M4_s60_o12 exact 4 60 12 30 4 256    # S0 Phase 2b -> tailbound2.json
python3 offbasis.py runs/S0_M4_s60_o12                            # S0 off-basis bound -> offbasis.json
FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 fsec.py S1 2 60 4 256 all ; python3 fsec_assemble.py runs/S1    # FLOATING: core section S_1 = T_R + C_R on L^2(w_a),
                                                                  # Mh 2 (42 remainder columns, m = 1 only), stride 60, COMPLETE mode set ('all'), 4 workers (4817 s);
                                                                  # checkpoints ckpt_*.npz every 600 s, a relaunch of the same command resumes (any worker count)
python3 s1_robust.py runs/S1                                      # 50-digit generalized singular values of the stored pair, near-dependence, Rayleigh quotients vs rounding
# fsec_assemble.py is v2 (12:35Z): parts / bases / latest checkpoint per worker with a coverage check (v1 double-counted checkpointed cells; kept as fsec_assemble_v1.py)
FSEC_MODE=S1 FSEC_DROP=+in,+out,in5,in6,in7,out FSEC_CKPT_SEC=600 python3 fsec.py S1M4P 4 60 4 256 all   # pure splines, m = 1..3 (78 columns; 10758 s on 4 workers, DONE 15:41Z); unused S0 columns' images are skipped
./s1m4p_chain.sh    # = fsec_assemble.py runs/S1M4P ; gram_compare.py runs/S1M4P S1M4P (input Gram vs the verifier's exact V202 export) ; s1_blocks.py ; s1_vectors.py ; s1_robust.py
python3 outer_cells_f8.py   # -> runs/outer_cells_f8.json (indices 1571..1586 of the 24-offset outer cover), then:
MARGIN_OUTER_EXTRA=1/16,1/8,3/16,1/4,5/16,3/8,7/16,1/2,5/8,3/4,7/8,1,5/4,3/2,7/4,2,5/2,3,7/2,4,5,6,7,8 MARGIN_FAMILY=4,0.3 MARGIN_REF_THR=99 MARGIN_REF_DEPTH=6 python3 margin.py OUTER_F8 64 160 runs/outer_cells_f8.json ; python3 outer_merge2.py runs/OUTER_F403 runs/OUTER_F8 -- 4 0.3 runs/FAMILY_REF/family_4_03.json   # (DONE 15:54Z, hardened 16:08Z: inf m_a >= 3.000000, m_fam(4,0.3) >= 1.250190; C4 addendum 2, C7 addendum)
BASIS_OUT_SHIFT=1 FSEC_DROP=+out FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 fsec.py S1J1 2 60 4 256 all        # junction test (theory author message 32): outer power columns attached at t_+ + 1
FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 fsec.py S1M3 3 60 4 256 all ; python3 fsec_assemble.py runs/S1M3 ; python3 s1_robust.py runs/S1M3   # Mh 3 (adds m = 2), ~2 h
# decoupled weight family (theory author team message 26-28): refined near-axis lower bounds of m_fam = m_a + (a_ang - 17/4) tan(theta) V.grad(theta) - Delta q 1_{t>=0}
MARGIN_FAMILY=4,0.3 MARGIN_REF_BOXES=56:64 MARGIN_REF_THR_MA=1.5 MARGIN_REF_THR_M=-99 MARGIN_REF_DEPTH=6 python3 margin.py FAM_4_03_A 64 160 runs/MARGIN_REF2/family_cells_A.json
#   (same for _B, _C, _D cell lists: t_a in [4.5, 6] split in two, t_a >= 6 split in two; and MARGIN_FAMILY=3.6,0.3 -> FAM_36_03_*; ~4-5 min each)
python3 family_combine.py 4 0.3 runs/FAMILY_REF/family_4_03.json runs/FAM_4_03_A runs/FAM_4_03_B runs/FAM_4_03_C runs/FAM_4_03_D   # whole-plane minimum after refinement
python3 family_combine.py 3.6 0.3 runs/FAMILY_REF/family_36_03.json runs/FAM_36_03_A runs/FAM_36_03_B runs/FAM_36_03_C runs/FAM_36_03_D runs/FAM_36_03_E runs/FAM_36_03_F
# finer radial cover of the first outer sub-cell: MARGIN_OUTER_EXTRA=1/16,...,8 python3 margin.py OUTER_MA 64 160 1563,...,1570 ; python3 outer_merge.py runs/OUTER_MA (see status file)
python3 fsec.py FSEC 4 60 4 256 all ; python3 fsec_assemble.py runs/FSEC   # FLOATING: sigma_min of L_red in the w_a jet realization (complete modes; ~1 min/cell)
python3 eta.py ETA 3 256 40                                       # FLOATING eta = ||F(rho~)||_Y and ||F||_{L^2(e^mu~)} (exact residual modes, N <= 40; ~2 h on 3 workers)
# eta.py / eta2.py: WITHDRAWN (theory author message 25, verifier V111/V113): not controlled approximations of ||F||_Y; do not use. dbg_div.py: truncation study of the cos^4 quotient
```
Always `export OMP_NUM_THREADS=1`. The chain scripts logs/run_phase2e.sh (production order of 04:50Z) and logs/run_S0.sh record the exact
invocations used. Parameters of the S0 norms are in run_section.py (Weights(...)); margin.py and hypA.py take (tag, ntheta, prec, cell range).

## Inputs of the box certificates (C4, C5)
- The exact modal trial as in C1 (modal_v2.json.xz + the exact scalar repair z; hard-coded enclosure in exact_trial.py).
- Weights: mu~ knots and values (margin.py MU_KNOTS, MU_VALS; theory author message 5); w_a: a = 17/4, mu_a' = -17/2 / -5/4 (margin.py, hypA.py; theory author message 7).
- Cover: Cells(T, inner_extra=[1/2, 1, 2, 4], outer_extra=[1/2, 1, 2, 4, 8]); ntheta = 64 boxes of [0, pi/2].
- Enclosures: encl.py (MERGE_PREC 512, J_MERGE 20, MERGE_WIDTH 1.0, SPLIT 6, K_TAYLOR 8, TOL_ABS 1e-14); HI_PREC = 512 on the non-mid cells.
- Angular identities: hypA.py docstring (N0 = 12 exact modes); margin.py N0_EXACT = 8.

## Continuation (what to do next if the run is restarted)
1. Read status file (RESUME_HERE) and work log. Check `ps -eo pid,stat,args | grep "python3 -u"` for running or guard-paused (state T) jobs
   of this team (fsec.py, margin.py); use the pyenv interpreter explicitly.
2. Certified: C1 (strain), C2 (identity test), C3/C3b (S0 section), C4 (+ addendum: inf m_a >= 2.9270, V197; + addendum 2 of 15:54Z: inf m_a >= 3.000000, team-certified only), C5 ((A), (CB), kappa_*), C6 (L_fix
   section), C7 (family margins (4, 0.3) >= 1.2501, (3.6, 0.3) >= 0.9596). NUMERICAL: N1 (S1, m = 1), N2 (S1M3, m = 1, 2: pure-spline
   coupling value 3.4557), N3 (S1M4P, m = 1, 2, 3 pure splines: 2.7655; the value against the cutoff 50.32 / 3.456 / 2.766 is not converged),
   N4 (S1J1 junction test: far value 4.75 weakly resolved, concentrated in the outer power-law coordinates, not shown spurious (V279); bulk 50.32 unchanged), C4 addendum 2 and C7
   addendum (OUTER_F8 + OUTER_F403 merged with outer_merge2.py: inf m_a >= 3.000000, m_fam(4, 0.3) >= 1.250190).
3. Open numerical items in order: (a) a better-conditioned far basis (the outer power-law columns are near-dependent to 1e-11 and carry the
   ill-resolved far values of N1 and N4); (b) the m <= 4 run on the pure splines (Mh 5, FSEC_DROP as for S1M4P; about 3.5 h on 4 cores) is the next convergence test of the
   bulk value; (c) a better-conditioned far basis before any certified section (7.5 of S2_BASIS_CERTIFICATION.md).
4. Open analytic items this team cannot settle: the quantitative split (S) of Lemma IV.1, the blocks Q_M L (I - P_N) and D_{M,N} (prompt 6.6),
   injectivity of S_1 / L_red (the sections are numerical evidence only; a certified section needs the rigorous quadrature of 7.5 of
   S2_BASIS_CERTIFICATION.md), control of the cos^4 image division error (verifier V187/V189), a certified eta (the verifier's topic).
