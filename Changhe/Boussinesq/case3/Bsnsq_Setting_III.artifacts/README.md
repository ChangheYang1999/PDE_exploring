# Accompanying artifacts: Setting B2 (x-reflection symmetry only, moving material center)

These files accompany the report Bsnsq_Setting_III.report.md. The verdict is UNRESOLVED: no candidate profile was
found, so there is no candidate to regenerate. The files below reproduce the numerical states that the report
discusses (approximate solutions of forced problems), the independent residual tables, and the exact and symbolic
checks. All command blocks start from this folder; paths are relative to it unless a command changes directory.
The directory changes below run in subshells, so each block returns to this folder. Use a fresh working directory
for the regeneration commands. Set OMP_NUM_THREADS=1 and PYTHONDONTWRITEBYTECODE=1 before running the CPU checks.

## Contents

| folder or file | contents |
|---|---|
| specification/specification.md | admissible class, canonical whole-plane inverse, normalization, identities to check and numerical diagnostics, with the change log (version 94) |
| numerics/ | solver and evaluation code of the numerical work (flat layout), seed states, evaluation summaries (JSON and tables), the consolidated residual table |
| numerics/runs/ | the 59 stored coefficient files (NPZ) that, together with those under numerics/verifier/, are the inputs of the consolidated residual table |
| numerics/verifier/ | the independent regional residual evaluations (REGIONAL_RESIDUALS.json) and the coefficient snapshots they evaluated, packaged for the table |
| numerics/consolidated_residuals.csv, .md | absolute and normalized residuals of 123 independently evaluated states (121 forced-problem states, 2 manufactured controls) in six radial bands, 5904 rows |
| numerics/README_numerics.md | the command list of the numerical work (solver runs, continuation paths, diagnostics) |
| verification/code_independent/ | independent verification code: value reconstruction from stored coefficients, adaptive full-plane modal Green inverse, Cartesian inverse with Duffy quadrature and compactified exterior, finite differences, residual and regional-grid evaluators, exact rational-arithmetic certificates, symbolic checks of section 4, tests on manufactured solutions |
| verification/packets/287_quadrature_resolved_fields/ | one independent evaluation packet with the inputs needed below: the six quadrature-resolved states (rows q48 of Table 6.1e) and their comparison states, the manifest, and the recorded regional residuals, center certificates and inverse-constant certificates |
| verification/proofs/ | written proofs (PROOF.md) for the proof or check packets P n of the independent verification, with summaries (SUMMARY.md) where provided, in folders whose names begin with n; INDEX.md (reading order) and CATALOG.md (chronological) |
| verification/VERIFIER_SUMMARY.md | final synthesis of the independent verification |
| verification_timeline_full.md | the complete verification timeline (section 7 of the report gives its dated milestones) |

The proof notes and the timeline are working documents. They mention working file names, packet numbers and the
records of the analytic consultations with an external referee; those records, the work logs, the run logs and the
intermediate states belong to the working archives (about 1.2 GB), which are not published because of their size.
The packet manifest also records historical supporting inputs that are not bundled; the states and comparison
states required by the reproduction commands below are included.

## Software

Numerical work: Python 3.9 with NumPy 2.0, SciPy 1.13, PyTorch 2.8 with CUDA (the solvers and numerics/evalstate.py
run on one GPU), SymPy for tests. Independent verification: Python 3.12 with NumPy 2.5, SciPy 1.18, mpmath 1.3, SymPy
1.14, CPU only. All runs used one CPU thread (OMP_NUM_THREADS=1).

## 1. Regenerate the consolidated residual table (CPU, under a minute)

The numerics scripts expect a working directory with code/, runs/ and artifacts/ side by side. From this folder:

    export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
    mkdir -p wk/code wk/artifacts wk/runs
    cp numerics/*.py wk/code/
    cp numerics/runs/*.npz wk/runs/
    ln -s ../../numerics/verifier wk/artifacts/verifier
    (cd wk && python3 code/consolidate_audits.py)
    sha256sum wk/artifacts/consolidated_residuals.csv numerics/consolidated_residuals.csv
    cmp wk/artifacts/consolidated_residuals.md numerics/consolidated_residuals.md

Both CSV files have SHA-256 9367a7e40633d1c26b8d62469090983ca9612dad388eb9fd1826c24061f6c60d, and the Markdown tables
are identical (checked when this folder was assembled). The table reads the independent regional evaluations; it does
not rerun them.

## 2. Recompute an independent regional residual evaluation (CPU)

The verification scripts are run from verification/ and read the states named in the packet manifest. To keep the
recorded results for comparison, work on a copy:

    (
    set -e
    cd verification
    cp -r packets/287_quadrature_resolved_fields packets/rerun287
    P=packets/rerun287
    python3 code_independent/certify_center_ratios.py --output $P/center_certificates $P/quadB32_beta3.062.npz $P/quadB40_3076_beta3.076.npz $P/quadB40_3092_beta3.092.npz $P/quadB48_3062_beta3.062.npz $P/quadB48_3092_beta3.092.npz $P/quadL2B40_3085_beta3.085.npz
    python3 code_independent/check_general_center_ratio_certificate.py --output $P/center_certificates/checks.json $P/center_certificates/*.certificate.json
    python3 code_independent/farfield_grid_audit.py $P
    python3 code_independent/regional_grid_summary.py $P
    python3 code_independent/audit_native_tail_archive.py $P
    python3 code_independent/certify_native_inverse_constants.py $P
    )

Compare verification/packets/rerun287/REGIONAL_RESIDUALS.json, its center_certificates/ and its
inverse_constant_certificates/ with the recorded files in verification/packets/287_quadrature_resolved_fields/. The wide-grid evaluation uses 161 radii from 1e-5 to 1e8 and 96
angles per state; run times were not re-measured when this folder was assembled. The center certificates use exact
rational arithmetic (the limit of the normalized temperature residual at the center and the forced center-strain
mismatch). The packet's PROOF.md and SUMMARY.md in verification/proofs/287_quadrature_resolved_fields/ state what each
output certifies and its scope. The same scripts apply to the
other states: write a manifest.json of the same form listing the snapshot files of numerics/runs/ or
numerics/verifier/.

## 3. Tests of the independent inverses and evaluators (CPU)

    (
    set -e
    cd verification
    mkdir -p verification/manufactured_20261020T1915/snapshots
    cp ../numerics/verifier/verification/farfield_grid_20261020T1930/snapshots/manufactured_picard.npz verification/manufactured_20261020T1915/snapshots/man_pic1.npz
    python3 code_independent/test_adaptive_modal_inverse.py
    python3 code_independent/test_cartesian_inverse.py
    python3 code_independent/test_elliptic_cartesian_audit.py verification/elliptic_cartesian_audit.json
    )

The copy supplies the bundled manufactured Picard control at the historical relative path expected by the test.
Its SHA-256 is 87b2fc65c398e53e3a21319955ee686c7d32e498278e86cc4f70405f105d1ffa.
The other test_*.py and check_*.py files of code_independent/ are the controls of individual proof or check packets;
each packet's PROOF.md or SUMMARY.md in verification/proofs/ names the scripts it used and their arguments.

## 4. Regenerate the numerical states (GPU)

Using the working directory wk/ of section 1 (scripts in code/, states written to runs/):

    (
    set -e
    cd wk
    python3 code/test_inverse3.py
    python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 40 --K 12 --Nphi 24 --Nphi_res 24 --beta_basis 3.0 --beta_fixed 3.0 --ext_gauss 2.5,2.87,1.0 --eps_schedule 0.0 --iters 0 --tag fb30g
    python3 code/homotopy.py --rmap r2 --grade 1.5 --Nt 56 --K 16 --Nphi 32 --Nphi_res 32 --beta_basis 3.0 --beta_fixed 3.0 --ext_gauss 2.5,2.87,1.0 --eps_schedule 0.0 --iters 0 --tag fb30g16
    python3 code/picard_beta.py --state runs/fb30g16_eps0.npz --ext_gauss 2.87,1.0 --a0 1.011258 --lam_schedule 0.99,0.98,0.97,0.965,0.96,0.955,0.95,0.945,0.94,0.93,0.92,0.91,0.9,0.88,0.86,0.84,0.82,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0 --tag blam16v --Nphi_res 32 --fixed_source 1
    python3 code/evalstate.py runs/blam16v_lambda0.99.npz
    python3 code/diagnostics.py runs/blam16v_lambda0.99.npz
    )

The seeds fb30g_eps0.npz and fb30g16_eps0.npz are also stored in numerics/. The last command line of the
continuation is the lambda path of the first path with 16 angular modes; the angular refinements (24, 32, 40, 48
modes), the beta-prescribed continuations, the second path and the diagnostics are listed with their exact arguments
in numerics/README_numerics.md, whose commands are written for this code/, runs/, artifacts/ layout. The last two
commands evaluate the first state saved by the continuation. The continuation stops (forced residuals growing, lambda not decreasing) at the
values reported in section 6.1 of the report; none of these states is a candidate profile.
