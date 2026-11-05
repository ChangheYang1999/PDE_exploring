# Reproducing the fixed-parameter certificates

The primary workspace is `Changhe/IPM/combined3`. Candidate007, Candidate013,
and all inherited files remain in their original locations. Every primary
configuration records the exact two source hashes and its producer/evaluator
hashes. Run from the repository root and use Python's `-B` option.

## Environment

```bash
python3 -B Changhe/IPM/combined3/IPM.artifacts/bootstrap_research_env.py
```

The bootstrap installs the pinned dependencies outside the repository at
`/tmp/ipm-combined3-venv`. Its Python executable is used below. No environment,
download, or import cache belongs in either inherited workspace.

## Verify the supplied certificates and reconstruct the scalar join

After the primary certificate set is complete, these commands verify its
source/code bindings and complete raw covers, then independently rebuild the
source moments, nonlinear formula, background rates, self-map margin, and
contraction. They write new output files without changing the published
certificates.

```bash
mkdir -p /tmp/ipm-combined3-independent-replay
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/operator_theory/assemble_fixed_parameter_closure_v01.py --selected-M 3/10 --selected-Rb 30000 --output /tmp/ipm-combined3-independent-replay/join.json
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/verify_final_local_Q_closure.py --consumer /tmp/ipm-combined3-independent-replay/join.json --out /tmp/ipm-combined3-independent-replay/independent.json
```

The first command must report `FINAL_NUMERICAL_CLOSURE_PASS`; the second
must report `ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS`. Missing data,
wrong hashes, incomplete covers, failed endpoints, or failed strict
inequalities cannot produce those statuses. These are numerical checks;
the analytic proofs and their independent audit remain part of the theorem.

The main consumer may select the longer full matrix certificate if that
optional computation subsequently finishes. The published join records
the precise matrix path and every input path/hash it used. Both matrix
routes target the identical actual bound `M >= 7/10 I` and the same scalar
parameters.

## Recompute primary whole-plane enclosures

Fresh output directories avoid changing the published hash-bound results.
These runs can take hours; the producer configurations and mathematical
enclosure methods are the same as the saved computations.

```bash
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/certify_actual_matrix.py --output /tmp/ipm-combined3-independent-replay/matrix --workers 3
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/certify_local_energy_coefficients.py --output /tmp/ipm-combined3-independent-replay/local --workers 6
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/finite_rank/certify_Q_source_constants.py --out /tmp/ipm-combined3-independent-replay/source --workers 6 --chunk 16
/tmp/ipm-combined3-venv/bin/python -B Changhe/IPM/combined3/IPM.artifacts/certify_source_envelopes.py --output /tmp/ipm-combined3-independent-replay/envelopes --workers 3
```

The exact direct-L2 construction, signed far integration and full-matrix
residual commands are documented in
[the completed A/B handoff](coercivity_residual/A_B_HANDOFF.md). The saved
exact far cache is a bound certificate, with source/builder hashes; it is
not a floating-point approximation. The original direct-L2 prototype
directories marked invalid are not theorem inputs.

The source end-prefetch manifest records a performance optimization only:
it called the unchanged panel function with the identical configuration
and installed disjoint completed chunks atomically. It supplies no new
mathematical assumption and is unnecessary for a fresh serial/chunked run.

## Independent subsidiary checks

`ROOT_DIRECT_L2_REPLAY.json`, `ROOT_SOURCE_ENVELOPE_REPLAY.json`,
`ROOT_LOCAL_COEFFICIENT_ASSEMBLY.json`, `ROOT_NONLINEAR_CORE_REPLAY.json`,
`ROOT_SIGNED_MATRIX_FAR_REPLAY.json`, and the independent auditor's receipts
record the subsidiary reassemblies. Their producers remain beside them.
Re-running a producer with its default destination can change a receipt's
timestamp and hash; use a separate checkout when regenerating those exact
canonical destinations.

The isolated numerical residual-pairing experiment has its own
[report and reproduction commands](residual_pairing_experiment/residual_pairing_experiment.report.md).
Its FFT/FFTLog norm estimates are not inputs to the primary certificates.
