# Reproducing the independent checks

Start with [VERIFY_SUMMARY.md](VERIFY_SUMMARY.md) for the conclusions and their limits, then [FINAL_CLAIM_MAP.md](FINAL_CLAIM_MAP.md) for the corresponding standalone proofs. The chronological record is the verification ledger, which is not included in the published folder. A proof label applies to its exact hypotheses; finite fitted growth is not an infinite convergence result.

All commands below are run from this `verification/` directory of the published artifacts. Labels of the form V<number> refer to entries of the chronological verification ledger (not included), and topic numbers refer to the folders `proofs/NN_topic/`; only the standalone `PROOF.md` of each topic is published, not its `sources/` and `verification/` receipt subfolders. The Candidate 007 replay needs the read-only source project `Changhe/IPM/combined1/` of the original repository, located at `../../../combined1/` relative to this directory; adjust that relative prefix if your checkout differs. Use a working copy when replaying scripts that write results. The recorded Python and arithmetic-library versions are in [runtime_versions.json](runtime_versions.json). No installation, JavaScript, server, cluster, GPU or Lean build is needed. The recorded commands pin one CPU, lower the priority and use one library thread; `taskset` and `nice` may be omitted elsewhere. Run commands sequentially.

## Independent Cartesian recurrence

The implementation in `code/cartesian_verify.py` represents homogeneous fields by exact Gaussian-rational Fourier coefficients. It constructs the nonlinear term with Cartesian differentiation and reconstructs a common potential. It imports no producer recurrence. Its basis checks also compare the polar Laplacian, incompressibility and mixed Cartesian derivatives.

The following small replay uses `c=5/3`, `f_1=sin(theta)+sin(3 theta)` and four nonexceptional orders. It writes a new result, leaving the original certificate untouched.

```sh
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 taskset -c 18 nice -n 19 python3 code/cartesian_verify.py --c 5/3 --initial 1:1,3:1 --order 4 --out replay/two_mode_replay.json
```

The `recursion` and `self_checks` objects should agree exactly with `two_mode_c5_3_N4.json` (copied here from the topic 01 receipt); timestamps differ. The replay recorded during final preparation is compared in `smoke_comparison.json`. Read [the recurrence proof](proofs/01_recurrence/PROOF.md) for signs, the ordered convolution, exceptional potential exponents and resonant harmonic freedoms. Four successful orders alone do not prove the infinite recurrence converges.

## Candidate 007 input

The exact extracted parameter and ten leading harmonics are in [leading_exact.json](../candidate_data/candidate007_leading_exact.json) (topic 02 data). The source coefficient, manifest and sector table are read-only. Their hashes are part of the extraction. A separate Cartesian extraction can be requested with:

```sh
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 taskset -c 18 nice -n 19 python3 code/cartesian_verify.py --candidate ../../../combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json --order 2 --out replay/candidate_replay.json
```

This checks input extraction and two recursion orders. It does not verify Candidate 007 as an exact stationary solution. The final independent table audit is [topic 295](proofs/295_candidate_publication_audit/PROOF.md); positivity and the unique first-quadrant maximum are proved in [topic 02](proofs/02_candidate007/PROOF.md).

## Infinite claims and numerical certificates

Read the complete informal proof before running its arithmetic. [CERTIFIED_RADII.md](CERTIFIED_RADII.md) identifies every admitted sufficient radius and its exact input. The corresponding JSON files contain exact rationals, algebraic-root intervals or directed numerical enclosures. The radii come from majorant inequalities with controlled infinite tails, not from fits to a finite prefix.

In the full verification record, the source and verification subdirectories beside each proof retain the producer snapshot, independent arithmetic and receipt; these subdirectories are not part of the published folder. A Python script beginning `admit_` records a particular chronological verdict. Such scripts are intentionally tied to a ledger position and should not be rerun against the completed ledger. Reproduce the mathematical check itself in a working copy; do not manufacture a second historical admission.

In the full verification record some completed JSON inputs are stored as `.json.gz` with storage manifests recording both original and compressed hashes, and binary checkpoint archives have separate recipes and manifests; `code/read_evidence_bytes.py` resolves such stored evidence. The storage manifests and checkpoint archives are not part of the published folder. A hash verifies identity, not a mathematical claim.

## Final document and provenance checks

`code/final_evidence_audit.py` writes a dated check of references embedded in admission receipts. It recognizes documented historical snapshots and exact text deltas. `code/final_local_reference_inventory.py` checks local links and explicitly named ledger artifacts. `code/publication_text_audit.py` and `code/compressed_evidence_text_audit.py` check the stated text scopes. These checks do not reprove convergence or replay all old coefficient arithmetic.

The publication index of the independent verification (not included) records the latest completed checks and the exact publication exclusions. Two raw floating transcripts of the theory part, `theory_code/tuned/hhf_Q7h1_root1_N301_f64.out` and `theory_code/tuned/hhf_Q8h1_root1_N304_f64.out`, are published as projected copies: only environment paths in runtime diagnostics are replaced by `[local runtime path]`, every numerical line is unchanged, and their hashes therefore differ from the original hashes cited in the ledger.

## Numerical limitations to preserve

The canonical `delta=2/3` continuation after order329 starts from stored midpoints. Later small arithmetic radii certify that chosen continuation, not the discarded uncertainty in the canonical sequence. The high-order tuned Q7 to Q10 extensions use rounded roots and floating arithmetic. Exact comparisons of their printed values and exact least-squares fits remain finite-data statements. No fitted radius is a rigorous boundary for the full series.
