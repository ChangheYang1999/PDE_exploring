# Accompanying artifacts of the S2 theory report

These files accompany the S2 theory report on the full-plane IPM self-similar profile with leading term x^2 y
(case 1, candidate X3), published beside this folder. The report and the documents here cite verification records by
number (V001, V002, ...). Every record is an entry of verification/VERIFICATION_RECORD.md, with its proof directory
under verification/proofs/. A record whose verdict is CONFIRMED was checked by the independent verifier; where an
independent audit or an external referee (a second model) was also used, the record says so.

Final status of the work: PARTIAL, NOT SOLVED. A conditional existence theorem (Theorem E, V178) and the linear
theory it rests on are proved and confirmed; its hypotheses (I) base low injectivity and (S) smallness are open.

## Layout

- S2_L2_THEORY.md, S2_CALPHA_THEORY.md, S2_C_FUNCTIONAL.md, S2_BASIS_CERTIFICATION.md, S2_NUMERICAL_CERTIFICATES.md,
  S2_CLOSURE.md, S2_RESTART.md: the companion documents required by the task, in their final versions.
- CONVENTIONS.md: the conventions (equation, normalization, linearization, the trial and its parameters).
- verification/: VERIFICATION_RECORD.md (every record with claim, method, result, verdict and evidence),
  FINAL_VERIFICATION.md and THEOREM_MAP.md (the verifier's concise final summary, grouped by question), proofs/ (one
  directory per proof with PROOF.md, code/ and evidence/), certificates/ and code/ (short identity checkers).
  Evidence files larger than 2 MB are not copied; LARGE_EVIDENCE_NOT_COPIED.sizes and .sha256 list them (paths
  relative to verification/proofs/).
- numerics/: NUMERICS_REPORT.md, the numerics team's detailed basis-certification, numerical-certificate and restart
  documents, and numerics/artifacts/ with the exact finite-basis pipeline (code/ and data/; see its README.md).
- theory_notes/: the theory author's working notes on the high-norm theory and the conditional existence argument;
  theory_notes/audit/ holds the theory author's independent audits of verifier proofs (each names the audited proof
  and its checksum).
- code/ and data/: the theory author's scripts and outputs (farres/: residual point evaluations, the strong-residual
  study, the axis-trace and knot-scale checks; lyapunov/ and hinorm/: margin and weight studies; injrank/: floating
  estimates of the finite-rank part). These are NUMERICAL unless a verification record says otherwise.
- NOT_INCLUDED.txt: SHA-256, size and path of files left out of this folder (two regenerable data arrays, three
  machine-specific file-identity receipts of the final packaging check, two machine-specific source manifests, and
  three third-party reference texts).
- MANIFEST.sha256: SHA-256 of every file in this folder except itself.

## Setup

Run commands from the root of this folder. Check the published files without running any research computation:

```sh
sha256sum -c MANIFEST.sha256
```

Numerical commands use one thread:

```
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
python3 --version          # 3.12; packages: numpy, scipy, mpmath, python-flint 0.9 (Arb ball arithmetic)
```

The read-only original data are not included. In the published repository, `../..` is the directory `Changhe/IPM`.
If the originals are elsewhere, change `ORIG` to their relative location. The following setup creates relative
symlinks and leaves the original directories unchanged:

```sh
export ORIG=../..
python3 - <<'PYLINKS'
import os
from pathlib import Path

original = Path(os.environ["ORIG"]).resolve()
links = [
    ("source/case1", "case1"),
    ("source/analysis1", "analysis1"),
    ("verification/research_copy/case1", "case1"),
    ("verification/research_copy/analysis1", "analysis1"),
    ("numerics/artifacts/research_copy/analysis1", "analysis1"),
]
for destination, name in links:
    source = original / name
    if not source.is_dir():
        raise FileNotFoundError(source)
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() and target.resolve() == source:
        continue
    target.symlink_to(os.path.relpath(source, target.parent), target_is_directory=True)
PYLINKS
sha256sum source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz
# expected a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874
```

Input identities and stored results are named in the verification records. The commands below are explicit
calculation and audit entry points, not a complete dependency schedule for a clean replay. They require the
originals and the predecessor evidence named in each proof; some prerequisite files were omitted for size and
must first be regenerated. Some producers refuse to overwrite an existing journal. Use a separate working copy
for recomputation, preserving the published evidence. Some productions take hours on one core.

Publication changed text-file hashes. Auditors that compare those files against historical hashes will reject the
published text unless the dependent producer evidence is also regenerated. A current manifest check establishes
file integrity only; it does not rerun or validate the mathematical certificates.

## Certified numbers and calculation entry points

| Number (report) | Record | Commands (from this folder, in listed order) |
|---|---|---|
| 15.726087821623500282 < c[X3] < 15.726087821623500289 | V018 | `python3 verification/proofs/10_raw_x3_strain/code/certify.py`<br>`python3 verification/proofs/10_raw_x3_strain/code/certify.py --bits 256 --nq 28 --nt 44 --qcap 76 --tcap 25 --tag raw_x3_28_44`<br>`python3 verification/proofs/10_raw_x3_strain/code/audit.py`<br>`python3 verification/proofs/10_raw_x3_strain/code/audit_bounds.py`<br>`python3 verification/proofs/10_raw_x3_strain/code/consequences.py` |
| axis rate >= 5.5752, global coefficient margins | V077 | `python3 verification/proofs/68_independent_global_coefficients/code/global_check.py prepare`<br>`python3 verification/proofs/68_independent_global_coefficients/code/global_check.py finite --tag full`<br>`python3 verification/proofs/68_independent_global_coefficients/code/global_check.py ends`<br>`python3 verification/proofs/68_independent_global_coefficients/code/audit.py` |
| radial margin >= 5/2 | V086 | `python3 verification/proofs/82_margin_refinement/code/refine.py`<br>`python3 verification/proofs/82_margin_refinement/code/audit.py` |
| anisotropic margin m_a >= 3 | V259 | `python3 verification/proofs/233_margin_three/code/certify.py`<br>`python3 verification/proofs/233_margin_three/code/audit.py` |
| decoupled family (4, 0.3) margin >= 1.2501 | V191 | `python3 verification/proofs/186_family_margin_refinement/code/certify.py`<br>`python3 verification/proofs/186_family_margin_refinement/code/audit.py` |
| 6049.11 < norm of F in Y < 8601.42 | V164 | `python3 verification/proofs/154_residual_final_audit/code/audit.py`<br>`python3 verification/proofs/154_residual_final_audit/code/inner_replay.py`<br>`python3 verification/proofs/154_residual_final_audit/code/finalize.py` |
| norm of F in Y_a < 485.632 | V174 | `python3 verification/proofs/170_decoupled_residual_bound/code/check.py` |
| norm of F in Y_a > 3.270 | V179 | `python3 verification/proofs/175_decoupled_residual_lower/code/check.py --count 8 --fresh-variation --bits 384 --degree 28 --tag fresh`<br>`python3 verification/proofs/175_decoupled_residual_lower/code/check.py --count 8 --fresh-variation --bits 640 --degree 32 --tag replay`<br>`python3 verification/proofs/175_decoupled_residual_lower/code/audit.py` |
| eta_* < 6.321e129 (fixed high norm) | V182 | `python3 verification/proofs/177_high_residual_majorant/code/check.py --inner-method ep --bits 512 --tag production_512`<br>`python3 verification/proofs/177_high_residual_majorant/code/check.py --inner-method ep --bits 768 --tag replay_768`<br>`python3 verification/proofs/177_high_residual_majorant/code/check.py --inner-method green --bits 512 --tag green_512`<br>`python3 verification/proofs/177_high_residual_majorant/code/check.py --inner-method green --bits 768 --tag green_768`<br>`python3 verification/proofs/177_high_residual_majorant/code/audit.py` |
| eta_* > 38666592266 (fixed high norm) | V192 | `python3 verification/proofs/187_fractional_difference_constant/code/certify.py` |
| S0 section sigma_min >= 4.3337e-7 (conditional on exported entries) | V066 | `python3 verification/proofs/62_finite_section_matrix_certificate/code/check.py` |
| S0 without TAU sigma_min >= 0.020685 (conditional) | V200 | `python3 verification/proofs/196_s0_without_tau_matrix/code/check.py` |
| complement-realization section sigma_min >= 0.510914 (conditional) | V081 | `python3 verification/proofs/80_radial_finite_matrix/code/check.py` |

The finite-section matrices themselves, the margin and hypothesis certificates of the numerics team (C1 to C7) and
their production commands are in numerics/artifacts/README.md; run those commands from numerics/artifacts/code.
The theory author's grid and residual studies (NUMERICAL) are listed with their commands in S2_RESTART.md; the
farres/ scripts are run from this folder, for example `python3 code/farres/far_points.py --points 2,4,8`, and write into
data/farres/. data/lyapunov/field.npz is regenerated by
`cd data/lyapunov && ANALYSIS1_SRC=../../source/analysis1/IPM_Analysis_I.artifacts/numerics/src python3 ../../code/lyapunov/field.py 700 181`
(floating point; its SHA-256 at production is in NOT_INCLUDED.txt).

## Retained files over 1 MB

These files contain numerical data or certificate evidence, rather than console logs or scratch output:

| File | Purpose |
|---|---|
| `data/lyapunov/aniso_margin.npz` | Floating anisotropic-weight margin study produced by `code/lyapunov/aniso_margin.py`. |
| `numerics/artifacts/data/MARGIN/margin_map.csv.gz` | Exported cell margin map for the numerical margin study. |
| `numerics/artifacts/data/MARGIN/margin_refined2.npz` | Refined margin arrays retained with that study. |
| `numerics/artifacts/data/S0_M4_s60_o12/matrices_float.npz` | Floating finite-section matrices; their presence does not certify continuum invertibility. |
| `verification/proofs/82_margin_refinement/evidence/margin_map.json.gz` | Exported refined margin enclosures from V086. |
| `verification/proofs/186_family_margin_refinement/evidence/replacements.jsonl.gz` | Directed replacement-cell evidence read by the V191 audit. |
| `verification/proofs/239_s1j1_full_input/evidence/check.json` | Full finite-section input Gram and strain checks; input evidence only. |

## Publication edits

For publication, machine-specific absolute paths in text files were rewritten relative to this folder (source/ for
the original data, verification/ and numerics/ for the two teams' files; a path under theory-working-files/ names a
working file that is not included), and internal file and team names in Markdown files were replaced by
descriptions. Run-log dumps and selected caches were omitted; small production and diagnostic records remain with the evidence. Binary data files are unchanged. SHA-256 values that
the verification records and certificates quote for edited text files refer to their pre-publication versions;
MANIFEST.sha256 gives the published checksums.
