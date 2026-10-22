# Accompanying artifacts: 2D inviscid Boussinesq, Setting A2 (Bsnsq_Setting_II)

These files accompany the report `../Bsnsq_Setting_II.report.md`. The final status of the study is
UNRESOLVED - 48h elapsed; active research duration unverified: no nonexistence theorem for the whole class
and no validated numerical candidate. Every stored coefficient state in `numerics/states/` is a rejected numerical state
(Section 6 of the report), not a solution and not numerical existence evidence. There is therefore no
candidate to regenerate; the commands below regenerate the rejected states and recompute the residuals,
checks and certificates quoted in the report.

All paths are relative. Each subfolder has its own README.md with the full file list and commands; run
the commands of a subfolder from inside that subfolder.

| folder | contents |
|---|---|
| `analysis/` | symbolic and exact-fraction checks of identities used in the analysis (Sections 1, 4, Theorems 10, 68, 88 and others) |
| `numerics/` | fitting code (parity-compatible smooth bases, xi-map and t-map coordinates, both signs of a0, beta free or fixed), validation tests, 72 stored coefficient states (`.npz`), diagnostics, dynamic-rescaling and forward/Picard codes |
| `verification/` | the independent verifier's code, written separately from the fitting code: whole-plane Biot-Savart inverses (target-centred polar quadrature, exact fourfold kernel cancellation with Duffy-type quadrature, adaptive radial modal inverse), residual evaluators, manufactured tests, exact rational origin and tail coefficients of stored states, integer-interval certificates of axis zeros and a python-flint certificate of one interior zero |
| `SHA256SUMS` | SHA-256 digests of every file in this folder |

## Software

Python 3.9 (tested with numpy 2.0.2, scipy 1.13.1, sympy 1.14.0, mpmath 1.3.0, torch 2.8.0 in float64,
python-flint 0.9.0). The least-squares fits were run on one NVIDIA A100 GPU; torch falls back to the CPU
(slower). All other scripts are CPU only.

## Quick start

Symbolic checks of the analysis:

    cd analysis
    python3 check88.py              # energy flux identity of Theorem 88
    python3 check_thm10_labels.py   # single angular mode, Theorem 10
    python3 check68_later.py        # exact check of (68.16), Theorem 68
    cd ..

Validation tests of the fitting code and regeneration of a rejected state (here the beta = 2, a0 < 0
state at N = 240, called N240 in Section 6 of the report; it starts from the stored N = 208 state):

    cd numerics
    mkdir -p runs
    python3 tests/check_reduction_sympy.py
    python3 tests/test_inverse_t.py
    python3 code/lm_solve.py --map t --N 240 --M 60 --L 1 --fixed_beta 2.0 --a0 -1 --Rw 30 --maxit 200 --tail 1.0 --t1 1e-5 --init states/TL_B2m_N208.npz --name TL_B2m_N240
    python3 code/table_states.py states/TL_B2m_N240.npz runs/TL_B2m_N240.npz
    python3 code/zero_jac.py states/TL_B2m_N240.npz > runs/zjac_TL_B2m_N240.log
    python3 code/local_res_Q.py states/TL_B2m_N240.npz
    cd ..

Independent inverse and residual evaluation of a stored state, and the manufactured tests:

    cd verification
    mkdir -p runs data/control_snapshots
    python3 test_inverse.py
    python3 test_duffy_inverse.py
    python3 test_residuals.py
    python3 audit_coefficients.py ../numerics/states/TL_B2m_N240.npz TL_B2m_N240
    python3 audit_coefficients.py ../numerics/states/TL_B2m_N240.npz TL_B2m_N240_polar --method polar --orders 64,128
    cd ..

The exact tail and origin certificates and the interval certificates of axis zeros are run as listed in
`verification/README.md`.

## Stored states

Each state archive records its own parameters: `beta`, the radial and angular resolutions `N` and `M`, the
coordinate map `mapname`, the target `a0_target`, the full solver options (key `extra`, JSON) and, where
recorded, the iteration history (key `hist`). For example

    python3 -c "import numpy as np; d=np.load('numerics/states/TL_B2m_N240.npz', allow_pickle=True); print(float(d['beta']), int(d['N']), int(d['M']), float(d['a0_target'])); print(d['extra'])"

File names encode the family, the branch and the resolution: `TL_B2m_N240` is the t-map family with
first-tail matching rows at beta = 2, a0 < 0 and N = 240; `B2p` denotes beta = 2 with a0 > 0;
`fix3` denotes beta fixed at 3. The first rows of the table in Section 6 of the report are
`A1_N48M12L6_b1` (the excluded control with beta = 0.9331), `B1_fix3_N40M10L15` (B1) and
`T4_fix3_N48M12L1` (T4); these three files, the four fit-domain variants `DM_B2m_N112_*` (map scale L and
weight radius Rw changed at N = 112) and `Nn3_fix3_a0m1_N64` are the solver's original uncompressed
output files, byte-identical to the files evaluated during the investigation; the other 64 files are
lossless compressed re-archives (see `numerics/README.md`). Regenerated states may differ from the stored
ones in the last digits (float64 reductions on a GPU); this was not tested after the artifacts were
assembled.

## Not included

The run logs, the solver output logs, the run launch scripts, the dated work logs, the written
verification records and proofs of the independent verifier, the reports of the external referee (a
second model), and the provenance manifest compiled during the run with its errata file (these index
files by their locations on the machine on which the investigation ran). The verification events are
dated in Section 8 of the report. No listed command was re-run after the artifacts were assembled.
