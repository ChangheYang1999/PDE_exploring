# Accompanying artifacts of the combined2 IPM campaign

These files accompany the final report IPM.report.md (a copy is COORDINATOR_FINAL_REPORT.md here). The campaign did
not reach a complete fixed-parameter existence theorem; the report states what was proved, what was certified and the
exact remaining gap. All paths below are relative to this folder.

## Layout

Top level:

- COORDINATOR_FINAL_REPORT.md: the final report (identical to IPM.report.md).
- EXISTING_PROOFS_REFERENCE.md, THEORY_NEW_RESULTS.md, NUMERICAL_OPTIMIZATION.md, JOINT_CLOSURE_LEDGER.md: the other
  four reports required by Part VII of the prompt.
- MIDCAMPAIGN_REPORT.md: the mid-campaign report. WORKSPACE_CONTRACTS.md: the workspace contracts set at the start.
- REPRODUCE.md: exact commands for every certified number. REPRODUCE_FILES.tsv: the files each number needs, and
  whether each is published here.
- SHA256SUMS: SHA256 of every other file in this folder (check from this folder with `sha256sum -c SHA256SUMS`). These publication checksums are distinct from the original audit bindings embedded in the records.

One directory per role, each keeping a selection of that agent's files in their original relative layout:

| Directory | Role |
| --- | --- |
| theory_agent_1 | The first theory agent (near and closure check programs, research/closure_check and research/h4rest) |
| theory_agent_2 | The second theory agent (proof notes in notes/, the closure program in research/closure_check) |
| numerics_agent_1 | The first numerics agent (the correction fitter and evaluators in numerics/optimization) |
| theory_audit | The theory auditor (AUDIT_LEDGER.md, final reports in reports/, the last exchange files, the tools that produce the P-S1 endpoints) |
| numerical_audit | The numerical auditor (AUDIT_LEDGER.md, reports/, the last exchange files, the certification programs and their summary records in research/ and scripts/) |
| exchange | the shared exchange (latest theory and numerics exchange versions, the candidate index and snapshots) |

The audit ledgers record every entry of the two auditors (AT-n, ATnnnn for the theory auditor; ANnnn and the exchange
versions vNNN for the numerical auditor); the report cites them by these numbers. The reports and ledgers also cite
many working files that are not published here (see "What was left out").

## Candidates

- Accepted center C2-N1-013: exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/. The exact
  coefficient file is phi_007_b18s2_phi_exact.json (exact rational atom coefficients of the odd-potential correction,
  the constraint A + 3B = 0 imposed exactly; SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a).
  MANIFEST.json records the base, the constraints, the evaluator code and the FLOAT evaluation.
- Alternatives: C2-N1-009-phi-007-sector-leg24-lat/ (certified L2 interval, larger residual) and
  C2-N1-012-phi-007-sector-d8-leg24-lat-nf/ in the same folder. exchange/candidate_snapshots/INDEX.md lists all
  snapshots of the campaign, most of which are not republished.
- FLOAT research state b28s (not certified, used by no theorem): numerics_agent_1/numerics/optimization/phi_runs/
  phi_007_b28s/ holds its coefficient vector phi_007_b28s_coefs.npy, its summary and its FLOAT evaluation; its config
  is numerics_agent_1/numerics/optimization/phi_cfg/phi_007_b28s.json. Its frozen exact file (8.6 MB, SHA256
  0a77881a1c2e67777a0bfcab7808ac1ca8ac5b11fbf4aa184e817dfe4ab039e4) is left out for size.

Check a snapshot with:

```
cd exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2
sha256sum -c SHA256SUMS
```

## Setup

1. Python 3.12 (the campaign used 3.12.13, which one script asserts) with numpy, scipy, mpmath, gmpy2 and
   python-flint 0.9.0; the fitter also needs torch and a GPU. Use `python3` and set all four thread limits:

   ```
   export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
   ```
2. Several scripts read the read-only source data of the campaign through a link named `source` at the top of this
   folder. Provide the source checkout beside this folder as `../source-checkout` (the folder with IPM/ and the
   extracted previous-campaign archive c1_full/), then create the relative link:

   ```
   ln -s ../source-checkout source
   ```

3. Restore the Candidate 007 input of the numerical auditor (a byte copy of the source file, not republished):

   ```
   mkdir -p numerical_audit/data
   cp "$(find -L source -name C1-N1-007-d2w-j7-e2bal.json | head -n 1)" numerical_audit/data/candidate007_exact.json
   sha256sum numerical_audit/data/candidate007_exact.json   # ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21
   ```

4. The scripts of the numerical auditor assert CPU affinity {50} and the theory auditor's tools CPU {40}; run them
   with `taskset -c 50 nice -n 19` and `taskset -c 40 nice -n 19`, or edit the asserts in a copy. Most outputs are
   written once and a rerun refuses to overwrite them, so replay in a copy of this folder.

## Arithmetic replay and archived checks

Run each block from the root of the accompanying artifacts, in a disposable copy. The subshells return to that root after each block.

Closure arithmetic of the current tuple (rates, prices, allowances and the rooms 9941475955 and 47277952671/5):

```
(
  cp -r theory_agent_2/research/closure_check closure_replay
  cd closure_replay
  python3 -B closure_check_v08.py inputs_v08.json > closure_check_v08.out
)
```

This replay reproduces the retained case arithmetic and returns `CLOSURE OPEN`. Its N1 binding row reports mismatches for the edited near-check note, program and runner. It is an arithmetic replay, not a new certificate.

Archived command for the numerical auditor's independent check (463 checks in the original audit):

```
(
  cd numerical_audit
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
    taskset -c 50 nice -n 19 python3 -B research/closure_current_tuple_audit/code/check_v01.py
)
```

That independent checker cannot complete on these publication copies: its initial bindings expect the original versions of three closure programs. Missing transitive records and write-once outputs also prevent a complete certificate replay. The original successful check is retained as evidence; its hashes have not been rewritten.

Near arithmetic replay of the first theory agent (it recreates scratch/nc09 inside theory_agent_1):

```
(
  cd theory_agent_1
  PYTHON=python3 bash research/closure_check/run_nc09.sh
)
```

The other archived certification commands (the Candidate 007 residual norm, the source norms of 013, the whole-plane background,
the near derivative norms and the exact identity of correction 013) are listed with their inputs and
size exceptions in REPRODUCE.md. The omitted inputs and original hash bindings must be restored for full recertification; this subset alone does not provide it.

## Restart

The restart procedure is NUMERICAL_OPTIMIZATION.md section 15; its paths are relative to numerics_agent_1, and paths
beginning with exchange/ are relative to this folder.

- From the accepted center: start from exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/
  phi_007_b18s2_phi_exact.json. The open obligations at 013 are listed in COORDINATOR_FINAL_REPORT.md section A,
  and the smallest gap (H4-REST: certified bounds for eps_rest and C_rest) in section B. The closure arithmetic above
  recomputes the required rooms for any new certified bound.
- From the research line: continue from b28s (coefficients and config above) with the next dictionary step. Any new
  center needs its own certified chain (the 013 chain took about 6.5 hours of wall time).
- The fitter needs the fixed background meshes (numerics_agent_1/numerics/optimization/phi_bg/*.pt, 12 to 23 MB
  each), the sector rows (phi_rows/*.npz, about 119 MB) and the h_0 target modes; these are not published and are
  rebuilt with the build mode of phi_fit.py and with fix_bg_far.py and phi_sector_rows.py (section 15 gives the
  arguments).

## What was left out

- Run logs, scratch directories, caches and backup copies of scripts; internal status files and work logs.
- The read-only source data (Candidate 007 and the previous campaign's files), including the numerical auditor's byte
  copy of Candidate 007.
- The exact far-sector supplements of the snapshots (109 to 118 MB each; the SHA256 of the 013 table is in
  OMITTED_FILES_SHA256.txt in its supplement folder) and the snapshots other than 013, 009 and 012.
- The large intermediate records of the certification chains (for example a 238 MB table archive, about 395 MB of
  regional records for the source norms and about 900 MB of background records); REPRODUCE.md names them.
- Earlier versions of the reports, ledgers and exchange files; the background meshes and sector rows of the fitter;
  the frozen exact file of b28s.

## Retained files larger than 1 MB

These files are needed to interpret or reproduce the reported results:

- `theory_audit/AUDIT_LEDGER.md`: the claim-specific verdicts cited throughout the report, including refutations and scope restrictions.
- `exchange/theory_requirements/theory_v26.md`: the final theoretical requirements and their retained hypotheses.
- The three exact coefficient JSON files in the candidate snapshots for 009, 012 and 013: the candidate definitions.
- `numerical_audit/research/source013_near_norms/verification/wholeplane_v02/result.json`: the near-derivative assembly used by the current tuple.
- `numerical_audit/research/source013_norms/verification/weighted_publication_v01/actual_review_v01.json`: the independent review of the weighted source norm.

No retained file larger than 1 MB is an unused scratch file or execution log.

## How the published copies differ from the working files

Markdown files were edited only to replace internal agent names, local paths and internal file names by role
directory names and words; the audit ledgers are published as AUDIT_LEDGER.md. Scripts had local paths and agent
directory names replaced by the role directory names, so the SHA256 of a script can differ from the value recorded
in the records that bind it. Data records (JSON, CSV, NPY and text outputs) retain their original bytes. Editorial review also qualified the report's conditional claims and removed internal references. The current root SHA256SUMS authenticates the publication copies only; it does not repair or replace the original audit bindings.
