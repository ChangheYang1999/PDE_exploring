# Accompanying artifacts of "Rigorous a posteriori error analysis of the full-plane IPM profile X3"

Final status of the case: UNRESOLVED (no rigorous YES, no properly scoped NO; see the report).

All paths below are relative to this folder (the artifacts root). Nothing here contains an absolute path of the
machine used for the run: such paths were rewritten at publication (see `PATH_REWRITES.tsv`).

## Layout
- `numerics/`: the numerical team's code and data.
  - `src/`: reconstruction of X3, canonical modal inverse, the explicit modal trial (fit, exact joins and
    normalization), the interval certificate pipeline (Arb ball arithmetic via python-flint, mid-rad arithmetic),
    X-norm ceilings, floating diagnostics (finite sections, Gram rows, jets, closure tests).
  - `data/trial_v2_h0.008.npz`: the stored floating-point representation of the modal trial (SHA-256
    `a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874`); exactified dependent coefficients
    (`cert_coeffs.json.gz` and those of the three variants); a 20-mode test fixture; cell boundaries. The exact trial
    rho~ uses the dependent coefficients determined by the join and normalization equations below.
  - `runs/`: certificate outputs (per-cell residual and derivative certificates, gzipped when above 400 KB), the
    floating residual tables of X3 at three resolutions, the variant comparisons, X-norm tables and summaries.
  - `numerical_report.md`: the numerical team's full report (section 7 describes each certificate, section 8 lists
    the replay commands, run times and a SHA-256 table of code, data and outputs).
  - `README_numerics.md`: the complete command list with run times.
- `verification/`: the independent verifier's work, with code written separately from the numerical team's.
  - `reading_guide.md`: the verifier's final verdict and reading order; `research/CURRENT_INDEX.md` (by subject) and
    `research/INDEX.md` (chronological) list the verification topics.
  - `research/<topic>/`: one folder per verified item: `PROOF.md`, adjudication and correction records, and `code/`.
  - `evidence.tar.xz`: the evidence outputs (`research/<topic>/evidence/`) of all topics, files up to 300 KB, and
    up to 2 MB for the five derivative-norm topics behind the whole-plane X bounds. Larger per-cell row files (up to
    58 MB each) are not included; the topic's `run.py` regenerates them.
  - `data_exact/*.json.xz`: exact rational exports (binary64 dyadics written exactly) of X3 and of the trial,
    with the exact scalar repair and the modal repair; `modal_v2.json` has SHA-256
    `57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6`.
  - `code/`: the verifier's own evaluators of X3 (density, velocity, central strain, symbolic identities).
  - `verification_record.md`: the chronological record of all verifier verdicts.
- `analysis/specification.md`: the specification followed by the team (targeted theorem, spaces and norms, operator
  splitting, list of bounds and who computes each), final version 3.44, with its revision history inside.
- `PATH_REWRITES.tsv`: the files in which absolute local paths were replaced by relative names, with the original and
  the published SHA-256. Hashes quoted inside the records refer to the original files; every file not listed there
  retains its original content, except for this publication README.

Not included: the X3 coefficient file itself (it is published in Changhe Yang's repository, see below); large
regenerable intermediates (the 320 MB mode file, the 291 MB Arb Green data, the variant trial files, per-cell row
files above the limits stated above); raw run logs, driver and launcher scripts; the transcripts of the referee
reviews by a second model (the evidence archive keeps only the short review records that the topics cite) and the
working notes of the team. Some verification records cite such notes by a relative path beginning `../notes/`;
those files are not part of this folder.

Renamed files: references inside the records to `NUM_REPORT.md` mean `numerics/numerical_report.md`, to
`VERIFY_REPORT.md` mean `verification/verification_record.md`, to `RESULT.md` mean `verification/reading_guide.md`,
and to `SPEC.md` mean `analysis/specification.md`. The working-directory names of the run that occur in some
records (`ipmA-num`, `ipmA-ver`, `ipmA-lead`) refer to `numerics/`, `verification/` and `analysis/`.

## Environment
Single-threaded CPU (`export OMP_NUM_THREADS=1`). Numerics: Python 3.9, numpy 2.0.2, scipy 1.13.1, python-flint
0.6.0 (Arb), mpmath 1.3.0. Verification: Python 3.12 (3.11 or later is required, the scripts use
`hashlib.file_digest`), numpy 2.5.0, python-flint 0.9.0, mpmath 1.3.0.

## Setup
```
git clone https://github.com/ChangheYang1999/PDE_exploring.git PDE_exploring
md5sum PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz   # 15f8095f7e79dbfa0c50d75e5fe8997a (X3)
export X3_COEFF_PATH=$PWD/PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/a_coefficients/c6g_shape.npz
export X3_EVALUATOR_DIR=$PWD/PDE_exploring/Changhe/IPM/case1/IPM_Setting_I.artifacts/d_evaluator/code
export OMP_NUM_THREADS=1
unxz -k verification/data_exact/*.json.xz
tar xJf verification/evidence.tar.xz -C verification
```

## Regenerate the candidate (the explicit modal trial rho~)
```
(
cd numerics
python3 src/x3.py                                                       # X3 reconstruction self-test (0.1 s)
python3 src/x3_modes.py 80000 4096 1e-4 1e5 260 data/x3_modes_N80000_q4096_M260.npz   # angular modes of X3 (34 s, 320 MB)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_regen.npz   # fit (55 s)
sha256sum data/trial_regen.npz data/trial_v2_h0.008.npz                # compare; the historical rerun was byte-identical
)
```
The exact joins and the exact normalization of the trial are computed by the verifier's exactification
(`verification/research/modal_exactification/`, `verification/research/modal_repair/`, code in their `code/`
folders, outputs in the evidence archive); the exact export is `verification/data_exact/modal_v2.json`.

## Recompute residuals, bounds and checks
Numerics (start at the artifacts root; per-cell inputs stored as `.json.gz` must be gunzipped first where a command
reads the plain file, see `README_numerics.md`):
```
(
cd numerics
python3 src/x3_resid.py 16875 512 1e-4 1e6 runs/resid_N16875_q512.json   # floating residual table of X3 (8 s)
python3 src/trial_resid.py data/trial_v2_h0.008.npz 1200 runs/trial_v2_resid.json   # floating residual of the trial (1 min)
python3 src/cert_green.py data/trial_v2_h0.008.npz 256 0.0019 data/cert      # Arb Green boundary values (16 min, 291 MB)
python3 src/cert_scalars2.py data/cert_green.npz data/trial_v2_h0.008.npz runs/scalars_full.json   # certified scalars (10 s)
python3 src/cert_resid.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_resid_middle.json 12   # middle region (35 min)
python3 src/cert_summary.py                                                 # summary of the saved certificates (seconds)
python3 src/xnorm_cert.py                                                   # X-norm ceilings from the saved cells (60 s)
python3 src/variants_summary.py                                             # comparison with the three variants
)
```
`README_numerics.md` lists every other command (outer and inner regions, tails, derivative certificates, flow,
finite sections, Gram rows, jets, closure tests) with its arguments and run time.

Verification (from this folder; each topic's `PROOF.md` states the result and the header of each script gives its
arguments). The topics behind the main items of the report:
- exact trial and its normalization: `modal_exactification`, `modal_repair`, `modal_green`, `modal_source`;
- X3 scalars, normalization defect and far-field repair: `canonical_inverse`, `local_geometry`,
  `far_field_normalization`;
- zeroth-order residual certificates: `inner_cells`, `outer_cells`, `middle_residual`, `residual_cells`;
- whole-plane X bounds `1.49546805188731021373656` and `2464.68293019825564964515`:
  `full_derivative_norm_bound_v2` (middle annulus), `outer_derivative_cells_v2` (exterior),
  `inner_derivative_cells_v2` (interior), `derivative_end_tails`, combined in
  `derivative_norm_regional_composition` (mode `both`); the historical commands are listed below, with their
  replay limitations. A separate portable command checks the saved scalar composition;
- centre quasimodes and inverse obstructions: `center_weighted_quasimodes`, `center_weighted_fredholm_obstruction`,
  `higher_center_weight_quasimodes`, `factor_supremum_quasimodes`;
- axis-weighted norms `Y_(a,s)`: the `logarithmic_*` topics, `axis_weighted_nonlocal_mapping`,
  `canonical_residual_weak_axis_membership`, `weak_axis_compact_mapping`, `weak_axis_compact_higher_orders`;
- source exclusions: `source_transport`, `moving_source`, `sobolev_source_box`, `pure_source`;
- conditional two-norm theorem: `two_norm_scheme`.

## Historical verification commands and replay limits

The regional computations used these exact commands from the artifacts root:

```bash
python3 verification/research/full_derivative_norm_bound_v2/code/run.py --tag full
python3 verification/research/outer_derivative_cells_v2/code/run.py --tag full
python3 verification/research/inner_derivative_cells_v2/code/run.py --tag full
python3 verification/research/derivative_end_tails/code/check.py
python3 verification/research/derivative_norm_regional_composition/code/evaluate.py both
```

These historical commands are not an executable end-to-end replay from this bundle alone. Both computation and
replay scripts can require omitted review transcripts, launcher files, large parent row files and original source
hashes (some published files were rewritten, see `PATH_REWRITES.tsv`). The three regional runners also enforce the
original 2026-10-22 12:35 UTC deadline and require unused output names. Supplying missing inputs and adapting the
historical workflow would require a separate verification effort. Do not disable assertions to bypass these checks.
The proof statements, saved results and their stated dependencies remain available for inspection.

## Check the published scalar aggregation

This read-only command needs only Python's standard library, starts at the artifacts root and does not extract or
modify the archive. It checks the trial hashes and the final rational aggregation and rounding against the saved
regional ceilings. It does not recompute the interval enclosures or establish their analytic hypotheses.

```bash
python3 - <<'PY'
from pathlib import Path
from fractions import Fraction
import hashlib, json, lzma, tarfile

root = Path('.')
inputs = [
    ('numerics/data/trial_v2_h0.008.npz',
     'a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'),
    ('verification/data_exact/modal_v2.json.xz',
     '57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'),
]
for name, expected in inputs:
    data = (root / name).read_bytes()
    if name.endswith('.xz'):
        data = lzma.decompress(data)
    assert hashlib.sha256(data).hexdigest() == expected, name
with tarfile.open(root / 'verification/evidence.tar.xz') as archive:
    prefix = 'research/derivative_norm_regional_composition/evidence/both/'
    checks = json.load(archive.extractfile(prefix + 'checks.json'))
    verdict = json.load(archive.extractfile(prefix + 'verdict.json'))
assert verdict['status'] == 'CONFIRMED_COMPLETE_CANONICAL_REGIONAL_DERIVATIVE_COMPOSITION'
expected = ['1.49546805188731021373656', '2464.68293019825564964515']
assert checks['published_whole_plane_norm_ceilings'] == expected
for index, ceiling in enumerate(expected):
    total = sum((Fraction(checks['regional_squared_ceilings'][region][index]['exact'])
                 for region in ('inner', 'middle', 'outer')), Fraction(0))
    assert total == Fraction(checks['displayed_region_reductions'][index]['sum_exact'])
    assert Fraction(ceiling) ** 2 > total
    print('Saved regional aggregation and strict rounding checked:', ceiling)
print('Trial hashes checked; underlying interval bounds were not regenerated.')
PY
```

The files above 1 MB are the trial and its exact export, compressed cell certificates and the evidence archive.
They supply the data and verification results described above; the larger entries inside the evidence archive are
coefficient bounds and analytic tail data needed by the derivative-norm checks. No large raw log or scratch dump is
needed for these commands.

Floating-point outputs are exploratory evidence and are never used as certified bounds.
