# Independent verification code

This folder contains the evaluation code written by the independent verifier of the 2D inviscid
Boussinesq self-similar profile study (Setting A2). It was written separately from the fitting code
and does not import it. It reads the stored coefficient states only as data. Nothing here is an
existence proof: the numerical scripts are diagnostics, and the exact and interval scripts certify
only the stated finite inputs.

Layout assumed: `artifacts/numerics/states/<name>.npz` and `artifacts/verification/` side by side.
Run every command below from inside `artifacts/verification/`. Before the first run create the output
folders:

    mkdir -p runs data/control_snapshots

## Dependencies

Python 3.9 or newer, with:

- numpy, scipy: all numerical evaluators.
- mpmath: high-precision checks (`test_far_coefficients.py`, the exact inverse and certificate scripts).
- sympy: symbolic checks (`derive_a2red.py`, `check_single_mode.py`, `test_far_coefficients.py`, `test_vbs*.py`).
- python-flint: real-ball interval certificate in `certificates/numerical_diagnostics/interior_zero_certificate/`.
- torch (PyTorch): only `vbs_direct.py` and `test_vbs_direct.py`.

The exact-rational scripts (`check_tail_laurent.py`, `check_critical_tail.py`, `check_natural_resonance.py`,
`certified_axis_zeros/intervals.py`) use only the Python standard library.

## Files in this folder

Biot-Savart inverse (velocity from vorticity on the whole plane) and residual evaluators:

- `inverse.py`: whole-plane Biot-Savart quadrature with target-centred polar panels and the center strain.
- `duffy_inverse.py`: second physical-space quadrature with exact fourfold kernel cancellation and Duffy-type splitting of the singular cell; also gives the stream function.
- `exterior_inverse.py`: exact full-plane contribution of the source outside a radius R, using fourfold parity.
- `modal_quad.py`: adaptive radial modal (canonical) inverse, a third method independent of the other two.
- `modal_tail.py`: exterior-source contribution through adaptive radial Green integrals for a snapshot tag.
- `vbs.py`: modal Biot-Savart evaluator for odd-odd vorticity and the origin strain.
- `vbs_direct.py`: physical-space Biot-Savart quadrature on a log-polar grid, independent of `vbs.py`.
- `residuals.py`: Cartesian, divided (axis-factored) and normalized PDE residuals with explicit axis limits.
- `profile_data.py`: independent decoder of the stored coefficient states (both radial maps) and a snapshot helper.
- `manufactured.py`: analytic manufactured Poisson pairs used by the tests.

Manufactured tests:

- `test_inverse.py`: polar-panel inverse against analytic Poisson pairs.
- `test_duffy_inverse.py`: Duffy inverse against analytic Poisson pairs.
- `test_far_inverse.py`: far-field targets of the panel inverse.
- `test_residuals.py`: residual evaluators on manufactured exact states.
- `test_exact_inadmissible.py`: an exact PDE state that must fail global admissibility.
- `test_profile_data.py`: analytic tests of both radial coefficient maps.
- `test_stream.py`: Poisson and stream-gradient tests; with `--source` also a study of one stored state.
- `test_modal_quad.py`: adaptive modal inverse on manufactured data, plus one stored state (`../numerics/states/R4_fix3_N112M28.npz`).
- `test_modal_tail.py`: exterior modal tail on manufactured data.
- `test_far_coefficients.py`: analytic and high-precision checks of the far coefficients (uses `data/control_snapshots/tmap_T4_beta3.npz`).
- `test_vbs.py`, `test_vbs_direct.py`: manufactured tests of `vbs.py` and of `vbs_direct.py` against `vbs.py`.
- `study_exterior.py`: manufactured exterior check and far-tail omissions.

Evaluation of stored states:

- `audit_coefficients.py`: velocities (Duffy or polar inverse), center strain and residuals of one stored state at several quadrature orders.
- `probe_modal_axis.py`: adaptive modal cross-check of an axis zero found by `audit_coefficients.py`.
- `audit_axis_chains.py`: axis roots and trace residuals using the adaptive inverse.
- `far_coefficients.py`: finite-basis far coefficients and compatibility with the original PDE.
- `tail_onset.py`: exact tail coefficients against finite-radius samples for four stored states.

Exact rational and symbolic checks:

- `certify_tail_coefficients.py`: exact rational first-correction polynomial of the stored L=1 states, reading binary coefficients as exact rationals.
- `check_tail_laurent.py`: separate standard-library check of that certificate by exact Laurent convolution.
- `certify_critical_tail.py`: exact modular certificate of the beta=2 critical-temperature tail constraint for one stored state.
- `check_critical_tail.py`: separate standard-library decoder and checker of that certificate.
- `check_natural_resonance.py`: exact finite angular recurrence over rational Laurent series.
- `check_single_mode.py`: symbolic test of a stream function with only the sin(2 phi) mode.
- `derive_a2red.py`: symbolic derivation check of the reduced A2 system and the center relations.

`data/control_snapshots/tmap_T4_beta3.npz` (with its `.json` record) is a small coefficient snapshot of an
exploratory control run that is not among the published states. It is the fixed input of `test_far_coefficients.py`.

## Folder `certificates/`

Exact rational and interval certificates. Each script locates its inputs relative to its own folder, so
the commands can be run from `artifacts/verification/`.

- `inverse/beta2_closed_form/exact_inverse.py`: exact finite Green inverse for beta=2 (rational polynomial helper).
- `inverse/beta2_closed_form/manufactured.py`: manufactured tests of that inverse.
- `inverse/integer_beta_closed_form/exact_inverse.py`: exact finite Green inverse for integer beta; exact rational origin moments (a0, b0, c) and multiprecision samples of a stored state.
- `inverse/integer_beta_closed_form/manufactured.py`, `test_divided.py`: manufactured tests and divided-trace checks.
- `numerical_diagnostics/certified_axis_zeros/intervals.py`: outward fixed-denominator integer interval arithmetic and axis enclosures.
- `numerical_diagnostics/certified_axis_zeros/test_intervals.py`: manufactured tests of the interval arithmetic.
- `numerical_diagnostics/*/compile_inputs.py`: compile stored states into exact rational form and record the exact origin coefficients a0, b0, c (and c-6, 5 b0 - 2 a0) in `data/input_manifest.json`.
- `numerical_diagnostics/*/propose_roots.py`: floating-point proposals of axis zeros (stored in `data/root_proposals.json`).
- `numerical_diagnostics/*/certify.py`: integer interval certificates of the proposed axis zeros, written to `verification/certificates.json`.
  `certified_axis_zeros` covers TL_B2m_N176 and TL_Nn6_a0m1_N144, `resolution_axis_certificates` covers TL_B2p_N112, TL_B2p_N176 and TL_B2p_N208, and `negative_n208_axis_certificate` covers TL_B2m_N208.
- `numerical_diagnostics/interior_zero_certificate/certified_eval.py`: outward real-ball (python-flint) evaluator of the finite inverse.
- `numerical_diagnostics/interior_zero_certificate/certify.py`: interval certificate of an interior zero of TL_B2m_N208 with the rational parameters in `data/parameters.json`.
- `numerical_diagnostics/interior_zero_certificate/test_certified_eval.py`: manufactured tests of the real-ball evaluator.

The `data/*.json` and `verification/*.json` files are the stored inputs and results of the original runs.
File paths recorded inside the stored records are relative to `artifacts/`. The two input paths in
`interior_zero_certificate/data/parameters.json` are relative to that folder, because `certify.py` reads them.

## Commands

Manufactured tests (results go to `runs/`):

    python3 test_inverse.py
    python3 test_duffy_inverse.py
    python3 test_far_inverse.py
    python3 test_residuals.py
    python3 test_exact_inadmissible.py
    python3 test_profile_data.py
    python3 test_stream.py
    python3 test_modal_quad.py
    python3 test_modal_tail.py
    python3 test_far_coefficients.py
    python3 study_exterior.py
    python3 audit_axis_chains.py --manufactured-only
    python3 test_vbs.py
    python3 test_vbs_direct.py

Symbolic checks:

    python3 derive_a2red.py
    python3 check_single_mode.py
    python3 check_natural_resonance.py

Inverse and residuals of a stored state. `audit_coefficients.py` takes the state file and a short tag; it
writes a reduced copy to `data/control_snapshots/<tag>.npz` and the result to `runs/<tag>_audit.json`.
The later commands reuse the tag:

    python3 audit_coefficients.py ../numerics/states/TL_B2m_N208.npz TL_B2m_N208
    python3 audit_coefficients.py ../numerics/states/TL_B2m_N208.npz TL_B2m_N208_polar --method polar --orders 64,128
    python3 probe_modal_axis.py --tag TL_B2m_N208 --bracket R_LOW R_HIGH
    python3 modal_tail.py --tag TL_B2m_N208
    python3 audit_axis_chains.py ../numerics/states/TL_B2m_N208.npz TL_B2m_N208
    python3 far_coefficients.py ../numerics/states/TL_B2m_N208.npz --tag TL_B2m_N208
    python3 test_stream.py --source ../numerics/states/TL_B2m_N208.npz --tag TL_B2m_N208

Replace R_LOW and R_HIGH by two radii that enclose an axis zero of the chosen state (see `runs/<tag>_audit.json`). These runs can take a long time at
high quadrature orders.

Exact rational tail certificates (run in this order; `tail_onset.py` creates the snapshots that the
next two scripts read):

    python3 tail_onset.py
    python3 certify_tail_coefficients.py
    python3 check_tail_laurent.py
    python3 certify_critical_tail.py --source ../numerics/states/B2_p_gauss_N112.npz
    python3 check_critical_tail.py

Exact inverse tests and exact origin moments of one state:

    mkdir -p certificates/inverse/beta2_closed_form/{data,verification} certificates/inverse/integer_beta_closed_form/{data,verification}
    python3 certificates/inverse/beta2_closed_form/manufactured.py
    python3 certificates/inverse/integer_beta_closed_form/manufactured.py
    python3 certificates/inverse/integer_beta_closed_form/test_divided.py
    python3 certificates/inverse/integer_beta_closed_form/exact_inverse.py ../numerics/states/TL_B2p_N112.npz

Axis-zero interval certificates. `compile_inputs.py` writes compiled exact inputs of several MB into the
folder's `data/`; `certify.py` overwrites the stored `verification/certificates.json`. `certify.py`
checks the compiled file against the hash stored in `data/root_proposals.json`, so do not rerun
`propose_roots.py` unless new proposals are wanted.

    python3 certificates/numerical_diagnostics/certified_axis_zeros/test_intervals.py
    python3 certificates/numerical_diagnostics/certified_axis_zeros/compile_inputs.py
    python3 certificates/numerical_diagnostics/certified_axis_zeros/certify.py
    python3 certificates/numerical_diagnostics/resolution_axis_certificates/compile_inputs.py
    python3 certificates/numerical_diagnostics/resolution_axis_certificates/certify.py
    python3 certificates/numerical_diagnostics/negative_n208_axis_certificate/compile_inputs.py
    python3 certificates/numerical_diagnostics/negative_n208_axis_certificate/certify.py

Interior-zero certificate with python-flint (needs the compiled TL_B2m_N208 input from the previous block):

    python3 certificates/numerical_diagnostics/interior_zero_certificate/test_certified_eval.py
    python3 certificates/numerical_diagnostics/interior_zero_certificate/certify.py --bits 2048
    python3 certificates/numerical_diagnostics/interior_zero_certificate/certify.py --bits 2816 --output certificates/numerical_diagnostics/interior_zero_certificate/verification/certificate_2816.json

## About the published copies

- Paths were changed to the layout above and nothing else in the numerics was changed. The reduced
  copies and the published state files have identical coefficient arrays, but the published files are
  different bytes from the copies hashed when the certificates were first made. The certificate
  scripts therefore print a note instead of stopping when the raw state hash differs. The compiled
  exact coefficient file is still checked against its stored hash.
- The written proofs behind the certificates are not included. The scripts record a null proof hash
  when the proof file is absent.
