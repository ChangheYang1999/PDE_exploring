# Sanitization and path log

Every file in this package is a copy of a file of the research run, of a rerun made for this package, or new
(README.md, this log, `audit_rerun/sources.json` in its rewritten form). This log lists every difference between a copy
and its original. It was checked by a byte comparison of each copy with its original: 58 copies are byte-identical, and
the differences of the other 58 are all listed below. No computation was changed.

Placeholders used below for locations outside this package:

- `<lead>`: the lead researcher's working folder.
- `<first-run verifier>`: the working folder of the verifier of the first investigation.
- `<referee answers>/<answer k>`: the folder of an external referee answer inside the lead researcher's working folder;
  the answers are numbered 1 to 18 here in the order of the internal labels, which are not reproduced. In quoted
  original texts below, internal labels of referee answers are written `<answer k>`, internal labels of verifier
  results `<verifier result>` and internal labels of the lead researcher's notes and specification `<note>`.
- `<site-packages>`: the site-packages folder of the referee's Python 3.12.13 installation.

## 1. Origin of the folders

| Folder here | Original |
|---|---|
| `exclusion_certificates/raw_bounds/01-differential` to `04-exclusion` | `<referee answers>/<answer 5>/answer/01-differential` to `04-exclusion` (first part of 6.3.1 (o)) |
| `exclusion_certificates/reference_fit/` | `<referee answers>/<answer 5>/answer/05-reference-fit/` |
| `exclusion_certificates/reference_fit/data/c6g_traces.npz` | `<first-run verifier>/runs/gen4/c6g_traces.npz` (byte-identical, md5 e53abea1da447eb20638b116efecf153; not in the referee folder, added as the input of fit_reference.py) |
| `exclusion_certificates/raw_bounds/norm_repair/` | `<referee answers>/<answer 7>/answer/02-remainder/verification/` |
| `exclusion_certificates/exclusion_theorem/audited_estimate/01-differential` to `04-exclusion` | `<referee answers>/<answer 7>/answer/01-differential` to `04-exclusion` (`PROOF.md` of each) |
| `exclusion_certificates/obstruction_certificate/` | `<referee answers>/<answer 6>/answer/01-obstruction/` |
| `exclusion_certificates/radius_budget/` | `<referee answers>/<answer 6>/answer/02-radius/` |
| `exclusion_certificates/trace_uncertainty/` | `<referee answers>/<answer 6>/answer/03-trace-uncertainty/` |
| `exclusion_certificates/exclusion_theorem/fitted_reference_exclusion/` | `<referee answers>/<answer 6>/answer/04-exclusion/` |
| `exclusion_certificates/audit_rerun/` | `<referee answers>/<answer 8>/answer/verification/` (audit_checks.py, sources.json, expected/); `referee_run/` holds the referee's audit_checks.json and installed_rounding.json; `audit_checks.json` and `installed_rounding.json` at the top of `audit_rerun/` are the outputs of the rerun for this package |
| `exclusion_certificates/a4_exclusion/PROOF.md` | `<referee answers>/<answer 1>/answer/03-quantitative-exclusion/PROOF.md` (byte-identical) |
| `b3_functional/b3infl`, `b3exact`, `b3grad`, `hminus`, `xref`, `s4a` | `<lead>/src/` folders of the same names |
| `b3_functional/dcode/vb3ibp.py` | `<lead>/src/r1/dcode/vb3ibp.py` (the first-run verifier's estimator, as copied into the lead researcher's tree) |
| `b3_functional/s4a/s4a_all_output.txt` | `<lead>/runs/s4a_all_output.txt` (byte-identical) |
| `symbolic_checks/*.py` and their stored logs | scripts in `<lead>`, renamed (section 5) |
| `symbolic_checks/rerun_outputs/` | new: outputs of the reruns for this package |

Not copied: from <answer 6> `INDEX.md`, `INPUTS.json`, `VERIFICATION.md`, `verification.log`, `verify_artifacts.py`,
`collaboration/STATUS.md` and `02-radius/verification/reference_estimate.md` (byte-identical to
`raw_bounds/02-remainder/PROOF.md`, same SHA-256, so the links point there); from <answer 5> `INDEX.md`; from <answer 7>
`INDEX.md`, `05-report-edits/`, `verification/` (execution notes, artifact checks, report excerpt, sources); from <answer 8>
the referee's proofs and notes (`01-certificate/` to `05-report/`, `INDEX.md`, `VERIFICATION.md`,
`collaboration/STATUS.md`), its replay logs, `context_sources.json`, `document_checks.json` and its private copy
`<answer 6>-copy/` of the <answer 6> answer; from <answer 1> `verification/README.md`. No collaboration status file is included.

## 2. PROOF.md files

- `obstruction_certificate/PROOF.md`, line 14: "copied byte for byte from <answer 5>. [../INPUTS.json](../INPUTS.json)
  records the input paths and SHA-256 digests." became "copied byte for byte from the reference fit of an earlier
  referee answer ([../reference_fit/data/fitted_reference.json](../reference_fit/data/fitted_reference.json))." (the
  INPUTS.json file is not included).
- `obstruction_certificate/PROOF.md`, line 22: "in the displayed definition in <answer 5>/05-reference-fit/PROOF.md;"
  became "in the displayed definition in the earlier referee answer's [../reference_fit/PROOF.md](../reference_fit/PROOF.md);".
- `radius_budget/PROOF.md`, line 3: "In the norm of <answer 5>/02-remainder, equation (12)," became "In the norm of the
  earlier referee answer's remainder estimate ([../raw_bounds/02-remainder/PROOF.md](../raw_bounds/02-remainder/PROOF.md)),
  equation (12),".
- `radius_budget/PROOF.md`, line 39: "the reference-relative theorem in <answer 5>/02-remainder, copied in full to
  [verification/reference_estimate.md](verification/reference_estimate.md); its source digest is recorded." became
  "the reference-relative theorem in the earlier referee answer's remainder estimate,
  [../raw_bounds/02-remainder/PROOF.md](../raw_bounds/02-remainder/PROOF.md)."
- `radius_budget/PROOF.md`, line 62: "equations (19)–(23) of the copied proof and" became "equations (19)–(23) of the
  remainder estimate ([../raw_bounds/02-remainder/PROOF.md](../raw_bounds/02-remainder/PROOF.md)) and".
- `radius_budget/PROOF.md`, line 192: "the conservative radius formula (32) in <answer 5>" became "the conservative radius
  formula (32) of the earlier referee answer ([../raw_bounds/03-norm-and-radius/PROOF.md](../raw_bounds/03-norm-and-radius/PROOF.md))".
- `trace_uncertainty/PROOF.md`, line 19: "This is <answer 5>/02-remainder, equation (12)." became "This is the norm of the
  earlier referee answer's remainder estimate ([../raw_bounds/02-remainder/PROOF.md](../raw_bounds/02-remainder/PROOF.md)),
  equation (12)."
- `trace_uncertainty/PROOF.md`, line 35: the clause "; [../INPUTS.json](../INPUTS.json) records provenance" was
  removed (the sentence now ends after "copied under `verification/`").
- `trace_uncertainty/PROOF.md`, line 249: link `../02-radius/PROOF.md` became `../radius_budget/PROOF.md`.
- `exclusion_theorem/fitted_reference_exclusion/PROOF.md`, line 120: link `../02-radius/PROOF.md` became
  `../../radius_budget/PROOF.md`.
- `exclusion_theorem/audited_estimate/02-remainder/PROOF.md`, line 3: "for the norm in <answer 5>'s equation (12).**"
  became "for the norm in equation (12) of the original remainder estimate (`raw_bounds/02-remainder/PROOF.md`).**".
- `exclusion_theorem/audited_estimate/02-remainder/PROOF.md`, line 30: "in <answer 5>'s `02-remainder/PROOF.md`," became
  "in the original `raw_bounds/02-remainder/PROOF.md`,".
- `raw_bounds/04-exclusion/PROOF.md`, line 3: "The fitted reference in the next folder has certified" became "The
  fitted reference of [../../reference_fit/PROOF.md](../../reference_fit/PROOF.md) has certified".

All other PROOF.md files are byte-identical to their originals.

## 3. JSON files

- `reference_fit/data/fitted_reference.json`, `obstruction_certificate/data/fitted_reference.json`,
  `obstruction_certificate/data/obstruction_certificate.json` and
  `audit_rerun/expected/01-obstruction/data/obstruction_certificate.json`: the field `source_file`
  "`<first-run verifier>/runs/gen4/c6g_traces.npz`" (an absolute path) became "reference_fit/data/c6g_traces.npz".
  The two fitted_reference.json files remain byte-identical to each other.
- `raw_bounds/norm_repair/norm_repair.json`: the field `source`
  "`<referee answers>/<answer 5>/answer/03-norm-and-radius/verification/rational_certificate.py`" (absolute) became
  "../03-norm-and-radius/verification/rational_certificate.py". The field `source_sha256` is unchanged and matches the
  copy here.
- `audit_rerun/referee_run/audit_checks.json`: in the names of the 45 provenance checks, the absolute prefix
  "`<referee answers>/<answer 6>/answer/`" became "original/" (23 names) and "answer/verification/<answer 6>-copy/answer/" became
  "copy/" (22 names). Results and all other fields are unchanged; the names still refer to the referee's own layout
  (for example "original/collaboration/STATUS.md"), which is not part of this package.
- `audit_rerun/referee_run/installed_rounding.json`: the field `module`
  "`<site-packages>/mpmath/libmp/libmpi.py`" (absolute) became "mpmath/libmp/libmpi.py".
- `audit_rerun/sources.json`: rewritten for this package. Each of the 23 entries keeps the referee's SHA-256 and gives the
  original file name relative to the <answer 6> answer (`original`), and either the path of the byte-identical copy here
  (`copy`, 7 entries, checked by audit_checks.py), or the path of the edited copy (`artifact_file`, 10 entries, marked
  "hash not checked"), or the note "not part of these artifacts" (6 entries). The original entries held absolute paths
  of the <answer 6> answer and of the referee's private copy of it.
- `audit_rerun/audit_checks.json` and `audit_rerun/installed_rounding.json`: new outputs of the rerun (they differ from
  the referee's files in `referee_run/` only as described in README.md: 102 instead of 140 checks; the rounding file is
  byte-identical to the sanitized referee file).

All other JSON files are byte-identical to their originals.

## 4. Code

### exclusion_certificates

- `reference_fit/verification/fit_reference.py`: `DATA=Path("<first-run verifier>/runs/gen4/c6g_traces.npz")` became
  `DATA=ROOT/"c6g_traces.npz"`; the output field `"source_file":str(DATA),` became
  `"source_file":"reference_fit/data/c6g_traces.npz",`.
- `raw_bounds/norm_repair/norm_repair.py`: docstring "The scalar certificate is deliberately reused from <answer 5>. Its
  three origin perturbation constants are replaced by the bounds proved in ../PROOF.md." became "... reused from
  ../03-norm-and-radius. Its three origin perturbation constants are replaced by the bounds proved in section 7 of
  ../../exclusion_theorem/audited_estimate/02-remainder/PROOF.md."; `SOURCE = Path("<referee answers>/<answer 5>/"
  "answer/03-norm-and-radius/verification/rational_certificate.py")` became
  `SOURCE = (Path(__file__).resolve().parents[1] / "03-norm-and-radius/verification/rational_certificate.py")`; the
  output field `"source": str(SOURCE),` became `"source": "../03-norm-and-radius/verification/rational_certificate.py",`.
- `raw_bounds/03-norm-and-radius/verification/rational_certificate.py`: unchanged (its docstring still gives the run
  command of the referee's layout, `answer/03-norm-and-radius/verification/rational_certificate.py`), because
  norm_repair.py records its SHA-256 5967adac06b840d76f1bd3cf01946219818980084e9a53bd5f0ad8e431afa269.
- `obstruction_certificate/verification/certify.py`, docstring: "Run from <answer 6> with timeout 540" became "Run from
  exclusion_certificates with timeout 540".
- `radius_budget/verification/radius.py`: `parents[2]/"01-obstruction/verification"` became
  `parents[2]/"obstruction_certificate/verification"`, and `ROOT.parents[1]/"01-obstruction/data/obstruction_certificate.json"`
  became `ROOT.parents[1]/"obstruction_certificate/data/obstruction_certificate.json"`.
- `trace_uncertainty/verification/analytic_bounds.py`: `parents[2]/"01-obstruction/verification"` became
  `parents[2]/"obstruction_certificate/verification"`.
- `trace_uncertainty/verification/compare.py`: the unused line `LEAD=Path("<lead>")` was removed;
  `ROOT.parents[1]/"01-obstruction/data/fitted_reference.json"` became
  `ROOT.parents[1]/"obstruction_certificate/data/fitted_reference.json"`.
- `audit_rerun/audit_checks.py`:
  - docstring "Independent exact/interval checks for the <answer 8> referee report. No certificate-generating <answer 6> module
    is imported." became "Independent exact/interval checks for the audit referee report. No certificate-generating
    module of the obstruction certificate is imported.";
  - `WORKSPACE = HERE.parent.parent` and `COPY = HERE / "<answer 6>-copy" / "answer"` became `WORKSPACE = HERE.parent`,
    `COPY = WORKSPACE`, a dictionary `LAYOUT` mapping 01-obstruction, 02-radius and 03-trace-uncertainty to
    obstruction_certificate, radius_budget and trace_uncertainty, and a function `located(relative)` used in place of
    `COPY / relative` in the six places that read the certificate outputs;
  - the check "source unchanged: " + source path (SHA-256 of each original file of the referee's layout) was removed,
    and entries of sources.json without a byte-identical copy are skipped (`if entry["copy"] is None: continue`);
  - the recorded mpmath module path `str(Path(libmpi.__file__).resolve())` became the path relative to the
    site-packages folder, `str(Path(libmpi.__file__).resolve().relative_to(Path(mpmath.__file__).resolve().parents[1]))`.

### b3_functional

- `b3infl/b3core.py`: docstring "copied into ../r1/dcode)" became "copied into ../dcode)";
  `sys.path.insert(0, '<lead>/src/r1/dcode')` became a path relative to the file (`.../../dcode`).
- `b3infl/lamfit.py`: docstring "(lambda-mode of g, lead notes <note>)" became "(lambda-mode of g)"; the dcode path as in
  b3core.py.
- `b3exact/lin_r12.py` and `b3exact/exact_analytic.py`: `sys.path.insert(0, '<lead>/src/b3infl')` became a path
  relative to the file; `np.load('<first-run verifier>/runs/gen4/c6g_traces.npz', ...)` became a relative path to
  `../../exclusion_certificates/reference_fit/data/c6g_traces.npz`.
- `b3exact/check_lin.py`: `open('<lead>/src/b3exact/lin_r12.py')` became `lin_r12.py` beside the file.
- `b3grad/b3grad.py`: docstring "Caution (lead notes <note> (a)): " became "Caution: "; the b3infl path relative to the file.
- `hminus/hminus.py` and `hminus/split.py`: the dcode path relative to the file; `D = '<first-run verifier>/runs/gen4/'`
  became `D = os.environ.get('TRACE_DIR', <file folder>/../traces) + os.sep`; the output
  `'<lead>/src/hminus/out_%s.json'` (`split_%s.json`) became the same name beside the file.
- `xref/fitref.py`: `sys.path.insert(0, '<lead>/src/xref')` became the folder of the file; `D` as in hminus.py; the
  output `'<lead>/src/xref/ref_%s_K%d.json'` became the same name beside the file. The docstring ("Writes
  src/xref/ref_<name>_K<K>.json") was not changed.
- `s4a/s4a.py`: docstring `"""<note> (a): B_3` became `"""B_3`; the b3infl path relative to the file; `D` as in
  hminus.py.
- `dcode/vb3ibp.py`, line 1: "(lead analysis.md section 12)" became "(from the lead's analysis notes)".
- All other files of b3_functional (infl.py, infl2.py, bref.py, the stored outputs and logs) are byte-identical.

### symbolic_checks (comments, docstrings, paths and one printed label)

- `Q2_cone_recurrence_log_defect.py`: "of <answer 18> part 5" became "of a referee answer, part 5".
- `area_preserving_pullback_structure.py`: "the <answer 17> counterexample" became "the referee's counterexample".
- `compact_canonical_extension_identities.py`: "of <verifier result> (compact canonical extension)" became "of the verifier's
  result (compact canonical extension)".
- `finite_angular_modes_identities.py`: "of <verifier result> (finite physical angular support)" became "of the verifier's result
  (finite physical angular support)".
- `fourth_order_identity_density_bound.py`: "of <answer 16> identity (17)" became "of a referee's identity (17)".
- `fourth_order_transport_identity.py`: "of <answer 14> (18)-(20)" became "of the referee's identities (18)-(20)".
- `frozen_fifth_order_examples_traces.py`: "of <answer 10> section 3" became "of a referee answer, section 3"; "see <answer 11>
  for those.)" became "a separate referee answer covers those.)".
- `frozen_kernel_fourier_solution.py`: "# <note>: frozen kernel" became "# Frozen kernel".
- `frozen_packet_even_y3_trace_at_source.py`: "# <answer 2> formula check:" became "# Check of a referee formula:".
- `frozen_packet_odd_y3_trace.py`: "# <note> numerical check:" became "# Numerical check:".
- `higher_order_transport_identity.py`: "of <answer 9> (3.4)" became "of the referee's identity (3.4)".
- `local_exclusion_reference_values.py`: docstring "the <answer 5> numbers" became "the local-exclusion referee numbers";
  `import sys, json` became `import os, sys, json` with `HERE` the folder of the file; `'<lead>/src/xref'` became
  `HERE/../b3_functional/xref`; `'<referee answers>/<answer 5>/answer/05-reference-fit/data/fitted_reference.json'` became
  `HERE/../exclusion_certificates/reference_fit/data/fitted_reference.json`; `'<lead>/src/xref/ref_c6g_K%d.json'`
  became `HERE/../b3_functional/xref/ref_c6g_K%d.json`.
- `log_cutoff_transport_example.py`: "of <answer 15> (M)" became "of the referee's example (M)".
- `log_primitive_transport_example.py`: "of <verifier result> (log primitive" became "of the verifier's example (log primitive".
- `r12_fifth_coefficient_finite_part.py`: "of <answer 10> section 6" became "of a referee answer, section 6"; "from the <note>
  S2 hierarchy" became "from the axis hierarchy of 6.3.1 (a)"; "(same formulas as <internal script name>)" became "(same
  formulas as resonant_fifth_order_log_residue_A2.py)"; the comments "# <answer 10> (23)" and "# <answer 10> normalized H5"
  became "# referee (23)" and "# referee's normalized H5"; the printed label "<answer 10> (21) =" became "referee (21) =".
- `r12_fifth_coefficient_global_sign.py`: "the verifier's r12-global-sign proof" became "the verifier's global-sign
  proof for R12 data".
- `r12_seventh_coefficient_A2.py`: "(<verifier result>, r12-seventh-resonance)" became "(verifier's seventh-order resonance result)".
- `r12_third_coefficient_general_L.py`: "of <verifier result> corollary (r12-seventh-resonance PROOF, md5 96dea1d9):" became "of the
  corollary of the verifier's seventh-order resonance proof:".
- `r12_third_coefficient_zero_SA.py`: "of <answer 3> section 4" became "of a referee answer, section 4"; "(<note> (d))"
  became "(axis hierarchy of 6.3.1 (a))".
- `reference_taylor_separations.py`: "of <answer 6>'s Taylor separation" became "of the referee's Taylor separation";
  `import json, mpmath as mp` became `import os, json, mpmath as mp` with `HERE` the folder of the file; the paths
  `'src/xref/ref_c6g_K%d.json'` and `'<referee answers>/<answer 5>/answer/05-reference-fit/data/fitted_reference.json'`
  (relative to `<lead>`) became `HERE/../b3_functional/xref/ref_c6g_K%d.json` and
  `HERE/../exclusion_certificates/reference_fit/data/fitted_reference.json`.
- `resonant_fifth_order_log_residue_A2.py`: "of <answer 3> section 2" became "of a referee answer, section 2"; "from the
  <note> hierarchy (b)-(d)." became "from the axis hierarchy of 6.3.1 (a), parts (b)-(d)."; "# check <answer 3> (8):"
  became "# check the referee's (8):".
- `thin_packet_velocity_suppression.py`: "(<answer 13> (21))" became "(referee's (21))".
- `third_order_forcing_and_r12_fifth_coefficient_A2.py`: "of <answer 4> claims" became "of a referee's claims".
- `transport_example_cutoff_numerics.py`: "the <answer 12> transport example" became "the referee's transport example".
- Unchanged: `Q2_velocity_and_axis_drift.py`, `cone_family_G5_G7.py`, `euler_beta_finite_part.py`,
  `r12_fifth_coefficient_sign.py`, `source_cone_general_seed_recurrence.py`, `source_cone_seed3_recurrence.py`, and
  all nine stored logs.

### symbolic_checks/rerun_outputs

In `frozen_packet_odd_y3_trace.out` and `frozen_packet_even_y3_trace_at_source.out` the absolute folder prefix of the
script name in the scipy IntegrationWarning line (printed on standard error) was removed, so that the line starts with
the script file name. No other change to the rerun outputs.

## 5. Names of the symbolic checks

The symbolic checks and their stored logs (`.log`, `.out`) were renamed from internal working names, which are not
reproduced here, to the descriptive names used in `symbolic_checks/`. Not included from the same folders: superseded
versions of two scripts, scripts that edit report drafts, and draft texts.

## 6. Hygiene scan

After these changes, a search of all files of this package for absolute local paths, the internal labels of the run
(of referee answers, verifier results, and items of the lead researcher's notes and specification), product and model
names and the em dash character finds none; in this log the internal labels are replaced by the placeholders listed at
the top.
