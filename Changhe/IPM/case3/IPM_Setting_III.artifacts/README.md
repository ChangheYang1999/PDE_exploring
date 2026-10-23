# Accompanying artifacts: full-plane IPM, Setting III (nondegenerate y-leading branch)

These files accompany the report IPM_Setting_III.report.md. The verdict of the report is UNRESOLVED: there is no
candidate profile, so nothing here regenerates a candidate. The folder lets a reader re-evaluate the saved trial
states quoted in Section 4 of the report (canonical velocity, a0 = rho_y(0), psi_xy(0), centre defect, sampled
residual maxima |R|, |R|/N_f, |R|/N_v by region), rerun the manufactured tests of the inverse, and rerun selected exact
symbolic and interval checks cited in Section 3 and Appendix A. All paths are relative to this folder.

Software used in the run: Python 3.9 and 3.12, numpy, scipy, sympy, mpmath, torch (CUDA optional), python-flint (for
the ball-arithmetic checks). The reconstruction and manufactured-test commands below use the CPU. Historical solver
scripts may require CUDA or a change to their device selection.

## Layout

- `numerics/`: the main computation (solver, canonical modal inverse, off-grid evaluator, saved states).
  - `src/`: all solver and diagnostic sources (`ipm3.py` compactified Chebyshev-Radau x quadrant-trigonometric
    discretization with the canonical modal Green-function inverse; `ipm3q.py` and `q_free.py` the representation
    smooth at the origin by construction and the free-c_l and fixed-c_l least-squares solves of Section 4.7;
    `dr.py` the dynamic rescaling flow of Section 4.9; `hs_*.py` the hydrostatic trial states of Section 4.10;
    `qdiag.py`, `region_maxima.py`, `residual_table.py` the between-node residual tables). `numerics/README.md`
    is the detailed file-by-file index written during the run (its section headings refer to the producer's
    internal section numbers; the batch launch scripts and run logs it mentions are not included here).
  - `tests/`: manufactured tests of the inverse, the fields and the Jacobians.
  - `data/`: saved states (torch dictionaries; keys in `numerics/README.md`), including `data/early_states/` (the four
    early states of Section 3.8 and A.3.8, with `SHA256SUMS.txt`), `data/psic_export/` (exact discrete stream modes
    for independent audits of the inverse), and the hydrostatic trial states and node exports (`data/hs*`).
    `data/dr_spectra_export/` retains the spectral data for Section 4.9: `const64.npz`, `const96.npz` and
    `stall64.npz` contain basis maps, singular vectors, coefficients, eigenvectors and residual arrays, with
    parameters in `META.json`. These are the only files larger than 1 MB; they support the reported finite
    spectral diagnostics and are retained as data, not as solver logs.
  - `reconstruction/`: a standalone loader and evaluator for the states cited in Sections 4.3 and 4.7, with
    `SHA256SUMS.txt` (the first eight hex digits are the hash prefixes used in the report, for example e861227a) and
    `RECONSTRUCTION_OUTPUT.txt` (its recorded output).
  - `MANIFEST_STATES.md`: one line per saved state of Section 4 (SHA-256, representation, size, c_l, a0, gauge).
  - `results/`: text tables produced by the diagnostics (drift tables, regional maxima, comparisons modulo scaling,
    angular spectra, far-field checks).
- `verification/`: the independent checker, written separately from the main computation (it does not import the
  producer's modules to generate its fields).
  - `basic_code/`: independent canonical inverse (`vmodal.py`, angular-mode form; `vdirect.py`, direct real-space
    principal-value quadrature), closed-form manufactured canonical pairs (`manufactured.py`) and the symbolic checks
    of the origin relation and the scaling (`sym_checks.py`).
  - `independent_code/`: the checker's further independent implementations (residual campaigns, exact rational and
    multiprecision re-evaluations, hydrostatic inverse quadratures, exact degree eliminations for 3.80).
  - `research/<topic>/`: per-topic proofs as checked (`PROOF.md`), the check scripts and their small result records;
    `research/INDEX.md` is the reading order. Large intermediate arrays (more than about 8 KB per record) are not
    included because of the size limit of this folder.
- `analysis_checks/`: exact symbolic and numerical checks of the main analysis cited in Section 3 and Appendix A
  (for example `rep4_intervals.py` for the enclosures of A.3.8, `indicial*.py` and `jet_resonance.py` for the
  local jet and mode computations, `chk*.py` and `app*.py` for appendix identities), and `hydrostatic_axis/` (the computations behind 3.73-3.80:
  axis inverse, logarithmic constant, polynomial axis data).

## Commands

Start each block from this folder's root. Parentheses keep directory changes local to a block.
The commands below evaluate supplied data or run manufactured checks; the all-state loop can take substantially
longer than an individual reconstruction.

Re-evaluate the saved states quoted in the report (canonical velocity from the saved density, a0, psi_xy(0), centre
defect c_l + psi_xy(0) - 1, far-field amplitude K, cubic coefficients, between-node regional maxima of |R|, |R|/N_f,
|R|/N_v with their locations, and point values):

    (
      cd numerics/reconstruction || exit
      sha256sum -c SHA256SUMS.txt
      python3 load_state.py states/r1C_cl3.0_N128.pt --device cpu
      python3 load_state.py states/qfree_cl1.5_N64_Lf0.25.pt --points '1,2;0.1,0.3;30,40' --device cpu
    )

Optional evaluation of all 20 states, with output printed to the terminal:

    (
      cd numerics/reconstruction || exit
      for state in states/*.pt; do
        python3 load_state.py "$state" --device cpu || exit
      done
    )

Manufactured tests of the main computation's inverse and fields (run from this folder's root, as their imports require):

    python3 numerics/tests/test_basic.py
    python3 numerics/tests/test_poisson.py
    python3 numerics/tests/test_fields.py
    python3 numerics/tests/test_forced_jac.py
    python3 numerics/tests/test_dr_manufactured.py cpu

Diagnostics of a saved state (the scripts read the state path given on the command line; the first also writes a table):

    (
      cd numerics || exit
      mkdir -p runs
      python3 src/qdiag.py data/qfree_cl1.5_N64_Lf0.25.pt QFREE64      # between-node residual tables, Theta0, strain moment
      python3 src/region_maxima.py data/r1C_cl3.0_N128.pt              # regional maxima of |R|, |R|/N_f, |R|/N_v with locations
      python3 src/farfield_check.py reconstruction/states/rf_s1_cl3.0_N96M48.pt     # far-field two-term expansion
    )

The commands that produced every number of the main computation (solves, scans, releases) are listed in
`numerics/README.md` (section "Commands used for the numbers"); they are written to be run from `numerics/` with
`runs/` created first, and inputs named `runs/<name>.pt` there are the saved states in `data/` or
`reconstruction/states/` of the same name.

Independent checks:

    (
      cd verification/basic_code || exit
      python3 sym_checks.py           # origin relation, scaling, manufactured canonical pairs (exact symbolic)
      python3 test_inverse.py         # angular-mode canonical inverse against closed-form pairs
      python3 test_direct.py          # direct real-space velocity quadrature against the same pairs
    )

Interval enclosures of A.3.8 (from this folder's root; requires python-flint):

    python3 analysis_checks/rep4_intervals.py

Topic checks of the checker are retained in `verification/research/<topic>/verification/` and
`verification/independent_code/`. Their working directories vary, and some require omitted records described
below; they are archival supporting material, not a standalone test suite.
Snapshots explicitly named as syntax failures or as preceding syntax repairs are retained as provenance;
they are not runnable checks.

## Limitations

- No candidate profile was obtained; no file here is a candidate.
- Run logs, batch launch scripts, queue and handoff scripts, and process records of the run (launch, job, progress and
  process-id records) are not included, and the large intermediate arrays of the checker are not included because of
  the size limit; the scripts that produced them are included. The checker's binding and provenance scripts (names
  beginning with `check_*_bindings`, `check_*_provenance`, `bind_*`, `accept_*`, `close_*`, `finalize_*`) also verify
  hashes of review records and run records that are not in this folder, so they report those files as missing. The commands listed
  above do not read those records; after this folder was assembled, the hash checks, one reconstruction
  (`r1C_cl3.0_N128.pt`), `sym_checks.py` and `rep4_intervals.py` were rerun and ran to completion.
- Hashes of the source code at the time of the historical optimizer runs were not recorded, so the reproduction is of
  the evaluation of the saved coefficients, not a bitwise replay of the runs.
- Absolute paths of the run machine were replaced by paths relative to this folder in all text files. Some check
  records of the checker bind text files by SHA-256; for text files whose paths were rewritten those stored hashes no
  longer match. Hashes of the binary states (`SHA256SUMS.txt` files) are unaffected.
- The reconstruction loader uses the main computation's discrete inverse. Its values can differ from the
  independent canonical evaluations in Section 4.7(c), as the report explains.
- The manufactured scripts print diagnostics without enforcing acceptance tolerances. In `test_inverse.py`,
  the first line labels a near-origin floating-point evaluation as `exact psi_xy(0)`; that printed value is
  unreliable and must not be used as an exact reference. In `test_poisson.py`, the relative-error columns over
  all radii divide by zero at the origin and print `NaN`; those columns are not usable error estimates.
- Sampled maxima are maxima over finite point sets, not suprema; no file certifies a uniform residual bound.
