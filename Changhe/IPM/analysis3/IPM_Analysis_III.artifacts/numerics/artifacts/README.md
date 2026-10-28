# numerics team artifacts (numerics team of the S2 team; 2026-10-28)

In the published folder: link numerics/artifacts/research_copy/analysis1 to a copy of the original Analysis I
directory (see the README at the top of the folder) and run the commands below from numerics/artifacts/code with Python 3.12
and python-flint 0.9; outputs go to runs/ there. The run logs named below are not included.

Everything here reproduces the certified numbers of ../S2_NUMERICAL_CERTIFICATES.md (C1 to C7 with addenda), the numerical sections N1 to N3 and the pipeline tests. Paths are relative
to this directory; the code expects the team layout `../research_copy/analysis1/...` (the research copy of the Analysis I artifacts, byte-identical to
source/analysis1) two levels up from `code/`, i.e. run the commands from `../work/` (the live copy of `code/`)
or copy `code/` to a directory `X/work/` with `X/research_copy/analysis1` present.

Interpreter: python3 (numpy, scipy, mpmath, python-flint 0.9.0 = Arb). Always `export OMP_NUM_THREADS=1`.

## Inputs
- Exact modal trial rho~: research_copy/analysis1/IPM_Analysis_I.artifacts/verification/data_exact/modal_v2.json.xz
  (SHA-256 57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6) with the exact scalar repair z of modal_repair/PROOF.md
  (enclosure hard-coded in code/exact_trial.py).
- Fixture for tests: research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_small_M20.npz.

## Commands (times on one core unless stated)
```
cd ../work            # or your copy of code/
python3 exact_trial.py                                   # C1: strain of the exact trial, three formulas, 320 bits (3 min)
python3 test_identity.py                                 # C2: identity test on the fixture (10 min)  -> compare logs/test_identity3.log
python3 test_minf.py                                     # guard test on the exact trial (5 min)       -> logs/test_minf_exact.log
python3 run_section.py S0_M4_s60_o12 exact 4 60 12 30 4 256     # S0 section assembly (4 workers ~45 min; checkpoints ckpt_*.json)
python3 certify.py runs/S0_M4_s60_o12                    # C3  -> certificate.json        (data/S0_M4_s60_o12/certificate.json)
CERTIFY_NO_TAU=1 python3 certify.py runs/S0_M4_s60_o12   # C3b -> certificate_noTAU.json
python3 margin.py MARGIN_A 64 160 0:785 ; python3 margin.py MARGIN_B 64 160 785:1569   # (run in parallel; ~12 and ~19 min)
python3 merge_margin.py MARGIN MARGIN_A MARGIN_B         # C4  -> runs/MARGIN/margin.json, margin.npz (data/MARGIN/)
python3 hypA.py HYPA_A 64 160 0:785 ; python3 hypA.py HYPA_B 64 160 785:1569           # (~17 and ~19 min)
python3 merge_hypA.py HYPA HYPA_A HYPA_B                 # C5  -> runs/HYPA/hypA.json, hypA.npz, hypA_dropped.json (data/HYPA/)
python3 dbg_encl.py 4,1,1563,1566,800,1300               # containment test of the enclosure method (logs/dbg_encl3.log, dbg_encl4.log)
python3 zrefine.py ZREF                                  # (Zb): refinement of the source neighbourhood (needs runs/MARGIN/margin.npz)
python3 run_section_l2.py L2fix_M4_s60_o12 exact 4 60 12 30 4 256 ; python3 certify_l2.py runs/L2fix_M4_s60_o12   # C6
python3 fsec.py FSEC 4 60 4 192 19 ; python3 fsec_assemble.py runs/FSEC    # FLOATING estimate (jet realization), not a certificate
```
## Later additions (05:00Z-08:40Z)
- zrefine.py (hypothesis (Zb): refinement of the source neighbourhood against the verifier's rectangle Q or the theory author's disc B_P; outputs
  data/ZREF/zrefine_rect.json, zrefine_disc.json with every terminal leaf), merge_override.py (refinement rounds merged into the production
  margin arrays: data/MARGIN/margin_refined2.json/.npz, margin_map.csv.gz = per-box lower bounds of m_a and m), margin.py options
  MARGIN_REF_THR_M/MARGIN_REF_THR_MA/MARGIN_REF_DEPTH (refinement), MARGIN_FAMILY="a_ang,Delta" (decoupled weight family; data/MARGIN/
  margin_family.json holds the FLOATING boxwise minima of team message 21).
- fsec.py, fsec_ang.py, fsec_assemble.py: FLOATING sections of L_red (jet realization) and of the core S_1 = T_R + C_R on L^2(w_a)
  (FSEC_MODE=S1), complete angular mode set ('all'), checkpoints; dbg_div.py (truncation study), dbg_far.py, dbg_eta.py (diagnostics).
- eta.py, eta2.py: withdrawn attempts at eta = ||F(rho~)||_Y (truncated angular maps are not controlled approximations; see NUMERICS_REPORT 10(a)).
- certify_l2.py with two-sided exact whitening (C6); certify.py whitening variant and CERTIFY_NO_TAU (C3b).
Status words as above; everything under 'FLOATING' is numerical evidence, never a bound.

## Files
- code/: the exact pipeline (exact_trial, opimage, basis, section, run_section, certify; section_l2, run_section_l2, certify_l2; margin, hypA,
  encl, merge_*, zrefine, outward, tailbound, run_norms, run_tailbound2, offbasis, test_*, dbg_*; fsec, fsec_ang, fsec_assemble) and the
  chain scripts actually used (run_S0.sh, run_phase2e.sh, repro_M16.sh).
- data/S0_M4_s60_o12/: meta.json (section parameters), certificate.json (C3), certificate_noTAU.json (C3b), matrices_float.npz (float
  mid/rad of the exact matrices; the exact dyadic balls matrices_dyadic.json.gz (40 MB) stay in ../work/runs/S0_M4_s60_o12/).
- data/MARGIN/: margin.json (C4 summary), margin.npz (per-box arrays: M_lo, M_ref, MA_lo, MA_ref, Q, BP_up, GR_up, DU_up, VLO, DV, NREF, MU),
  Z0.json ((Z0) table). data/HYPA/: hypA.json (C5), hypA.npz (per-cell/per-box arrays), hypA_dropped.json.
- logs/: the production and test logs named in the certificates; the second-model referee answers (opcheck: operator formulas; hypA_ids: identities).
Status words: CERTIFIED = ball arithmetic with every error enclosed and inputs identified (verifier confirmation noted in the certificate file);
FLOATING = numerical evidence only.

## Later additions (09:32Z-)
- INTERPRETER WARNING: `python3` on PATH may be the system Python 3.9 (python-flint 0.6, which breaks exact_trial.py); use
  python3 explicitly for every command.
- S_1 core section, complete modes: `FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 fsec.py S1 2 60 4 256 all ; python3 fsec_assemble.py runs/S1 ;
  python3 s1_robust.py runs/S1` (4817 s on 4 workers; data/S1/S1_Mh2_grams.npz = the accumulated double Grams G_Z, B_Y, S1_Mh2_meta.json,
  S1_Mh2_fsec_result.json; logs/s1_assemble.log). s1_robust.py: 50-digit generalized singular values of the stored pair, near-dependence of the
  columns, Rayleigh quotients against a rounding estimate (NUMERICS_REPORT 10(b), S2_BASIS_CERTIFICATION.md 7.3-7.5). Mh = 3 run: tag S1M3 (same
  command with Mh 3); junction test: `BASIS_OUT_SHIFT=1 FSEC_DROP=+out ...` (outer power columns attached at t_+ + 1, sp+out columns dropped).
- Decoupled weight family, near-axis refinement (C7): `MARGIN_FAMILY=4,0.3 MARGIN_REF_BOXES=56:64 MARGIN_REF_THR_MA=1.5 MARGIN_REF_THR_M=-99
  MARGIN_REF_DEPTH=6 python3 margin.py FAM_4_03_A 64 160 runs/MARGIN_REF2/family_cells_A.json` (cell lists A-F in data/MARGIN/family_refined/),
  then `python3 family_combine.py 4 0.3 out.json runs/FAM_4_03_A ...` (needs runs/MARGIN_REF2/margin.npz = data/MARGIN/margin_refined2.npz);
  results data/MARGIN/family_refined/family_4_03.json, family_36_03.json.
- 15:10Z additions: fsec_assemble.py v3 (blocks = parts/bases/latest checkpoint, union of done sets == recorded expected cell set, legacy
  assignment reconstruction; v1 kept as fsec_assemble_v1.py), s1_robust.py (50-digit whitening + double eigen-solve, accumulation-rounding
  intervals), s1_blocks.py (pure-spline and per-mode sub-blocks, incl. the sp7..sp26 block of V210), s1_vectors.py (weakest-vector export;
  data/S1/S1M3_pure_spline_block.json), outer_merge.py + margin.py MARGIN_OUTER_EXTRA (finer outer cover; data/MARGIN/family_refined/
  outer_merge_*.json), fsec.py: FSEC_DROP, BASIS_OUT_SHIFT (basis.py), exact cos^4 input quotient templates (V189), done sets in parts,
  cells_expected and settings in meta.json, resume refusal without a settings record. data/S1/: S1 (Mh 2), S1M3 Grams/meta/results/expected
  cell sets. Logs: s1_assemble_v2.log, s1m3_assemble_v2.log, s1m3_robust.log, s1m3_bulk.log, outer_merge_*.log, second-model referee.md.
  Error model of the floating sections: accumulation rounding only (the cos^4 image division is not covered; verifier V187/V189).

## Later additions (15:33Z-18:20Z)
- S1M4P (N3; S2_BASIS_CERTIFICATION.md 7.7): `FSEC_MODE=S1 FSEC_DROP=+in,+out,in5,in6,in7,out FSEC_CKPT_SEC=600 python3 fsec.py S1M4P 4 60 4 256 all`
  (78 pure spline columns, m = 1, 2, 3; 10758 s on 4 workers), then `./s1m4p_chain.sh` (fsec_assemble.py v3, gram_compare.py, s1_blocks.py,
  s1_vectors.py, s1_robust.py; logs/s1m4p_chain.log). Data: data/S1/S1M4P_grams.npz (summed double Grams G_Z, B_Y of the four parts),
  S1M4P_meta.json, S1M4P_cells_expected.json, S1M4P_fsec_result.json (values), S1M4P_vectors.json (weakest vectors), S1M4P_gram_compare.json
  (input Gram against the verifier's exact V202 export: 7.41e-7 entrywise, 2.69e-6 quadratic-form relative), S1M4P_PRODUCER_PROVENANCE.md
  (the launched fsec.py used pinv input quotients and was not frozen). The S1M4P parts themselves (4 x 100 KB) stay in ../work/runs/S1M4P/.
- gram_compare.py needs the verifier's export verification/proofs/198_pure_spline_input_gram/evidence/gram_512_640.json
  (path hard-coded; SHA bc7512502550c11fd5ba859d7b4630ae70b7d643ff2de6d6af5e329e9261d606).
- Finer outer cover OUTER_F8 (t_+ + 1/2 .. t_+ + 8; 16 cells): `python3 outer_cells_f8.py` (writes runs/outer_cells_f8.json), then the margin.py
  command of ../S2_RESTART.md and `outer_merge2.py runs/OUTER_F403 runs/OUTER_F8 -- 4 0.3 runs/FAMILY_REF/family_4_03.json`; results (15:54Z, hardened 16:08Z): data/MARGIN/family_refined/OUTER_F8_margin.json (run summary),
  outer_merge2_f403_f8.json (combined plane infima: m_a >= 3.000000, m_fam(4, 0.3) >= 1.250190, m unchanged), outer_cells_f8.json; the per-box
  arrays margin.npz (18 MB) stay in ../work/runs/OUTER_F8/. Logs: outer_f8.log, outer_merge2_f403_f8.log.
- New code this shift: gram_compare.py, outer_merge2.py (multi-run outer-cover merge; replaces outer_merge.py for combined values), outer_cells_f8.py,
  s1m4p_chain.sh, s1j1_chain.sh (post-processing chains; exact commands inside).
- Junction test S1J1 (7.8): `BASIS_OUT_SHIFT=1 FSEC_DROP=+out FSEC_MODE=S1 FSEC_CKPT_SEC=600 python3 fsec.py S1J1 2 60 4 256 all`; conformity of
  the shifted basis: logs/basis_shift_test.log (`BASIS_OUT_SHIFT=1 python3 basis.py`). Results (16:52Z, N4): data/S1/S1J1_fsec_result.json, S1J1_meta.json, S1J1_grams.npz (summed double Grams), S1J1_PRODUCER_SHA256.txt; logs
  s1j1_prod.log, s1j1_chain.log. Far value 4.7481 (weakly resolved, outer power-law columns), bulk 50.32 unchanged. Input Gram against the verifier's
  exact V267 export: `python3 gram_compare_s1j1.py runs/S1J1` (needs ../../verifier/proofs/239_s1j1_full_input/evidence/check.json; 6.0e-7 entrywise,
  4.3e-4 quadratic form; data/S1/S1J1_gram_compare.json, logs/s1j1_gram_compare.log).
- family_recheck.py (directed re-derivation of the C7 whole-plane family combination): `python3 family_recheck.py 4 0.3 runs/FAMILY_REF/family_4_03.json`
  (1.129601) and `... 3.6 0.3 runs/FAMILY_REF/family_36_03.json` (0.959670); logs/family_recheck_*.log.

## Final state (2026-10-28T17:55Z)
No computation of this team ran after 16:53Z. Certified numbers: ../S2_NUMERICAL_CERTIFICATES.md C1 to C7 with the addenda of 15:54Z (inf m_a >= 3.000000,
m_fam(4, 0.3) >= 1.250190, team-certified; the verifier's V259 confirms 3.000000 independently). Numerical sections N1 to N4 are floating evidence only.
Every command above was run from ../work/ with the pyenv interpreter and OMP_NUM_THREADS=1; the run directories referenced (runs/...) live in ../work/runs/.
