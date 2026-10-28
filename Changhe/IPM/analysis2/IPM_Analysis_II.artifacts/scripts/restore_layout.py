"""Recreate the directory layout expected by the certificate programs.

The programs in certificates/ locate their inputs relative to a common base directory BASE:
exact source data in BASE/source_audit/, every other proof part in BASE/<topic>/verification/,
the two original case 4 checkpoints in BASE/case4/IPM_case4.artifacts/checkpoints/, and the files of
the numerical work in BASE/numerics/code and BASE/numerics/data. This script copies certificates/<folder>
into that layout.

Usage: python3 restore_layout.py CERTIFICATES_DIR BASE_DIR [CASE4_ARTIFACTS_DIR] [--relocate]
Files are verified against certificates/MANIFEST.txt (SHA-256) before copying. A third argument copies
a complete case 4 artifacts folder into BASE/case4/IPM_case4.artifacts; the original checkpoints are
not shipped in this subset. Programs use relative input paths from BASE_DIR. Option --relocate prepares
additional relative inputs by copying the exact candidates of P10_refit_inputs that
P23_axis_constraints/axis_audit.py reads into BASE/numerics/data.
Then run the programs from BASE_DIR as described in S1_RESTART.md. The inputs of the independent recomputations
scripts/check_*.py are among the restored files; scripts/run_recomputations.py reruns those programs in BASE_DIR
(--relocate is not needed for them).
"""
import hashlib, shutil, sys
from pathlib import Path

LAYOUT = {
    "P1_source": "source_audit",
    "P2_singular": "04_singular/verification",
    "P3_tails": "05_tails/verification",
    "P4_energy": "02_energy/verification",
    "P5_frozen": "03_frozen/verification",
    "P6_P7_weighted": "07_weighted/verification",
    "P8_quasilinear": "09_quasilinear/verification",
    "P9_closure": "06_closure/verification",
    "P10_refits": "08_refits/verification",
    "P10_tail_splice": "10_tail_splice/verification",
    "P11_audit": "numerics_audit",
    "P10_refit_inputs": "08_refits/inputs",
    "P12_residual_norms": "11_residual_norms/verification",
    "P13_affine_obstruction": "12_affine_obstruction/verification",
    "P14_algebraic_repair": "13_algebraic_repair/verification",
    "P15_homogeneous_weight": "14_homogeneous_weight/verification",
    "P16_angular_sampling": "15_angular_sampling/verification",
    "P17_weighted_fractional": "16_weighted_fractional/verification",
    "P18_weight_radius": "17_weight_radius/verification",
    "P19_fractional_constants": "18_fractional_constants/verification",
    "P20_nb_candidates": "19_nb_candidates/verification",
    "P21_real_velocity": "20_real_velocity/verification",
    "P22_frozen_optimality": "21_frozen_optimality/verification",
    "P23_axis_constraints": "22_axis_constraints/verification",
    "P24_weaker_matrix": "24_weaker_matrix/verification",
    "P25_admissible_tail_gap": "23_admissible_tail_gap/verification",
    "P26_candidate_contract": "25_candidate_contract/verification",
    "P27_uniform_family_gap": "26_uniform_family_gap/verification",
    "P28_candidate_point_audit": "27_candidate_point_audit/verification",
    "P29_limits_of_tail_invariants": "28_limits_of_tail_invariants/verification",
    "P30_residual_targets": "29_residual_targets/verification",
    "P31_radial_degree_obstruction": "30_radial_degree_obstruction/verification",
    "P31_logarithmic_derivative": "31_logarithmic_derivative/verification",
    "P32_stationary_order_seven": "32_stationary_order_seven/verification",
    "P33_recursive_dilation": "33_recursive_dilation/verification",
    "P34_affine_scope": "34_affine_scope/verification",
    "P35_seven_branch_gap": "35_seven_branch_gap/verification",
    "P36_b6_candidates": "36_b6_candidates/verification",
    "P37_strain_trace": "37_strain_trace/verification",
    "P38_local_distance": "38_local_distance/verification",
    "P39_annular_distance": "39_annular_distance/verification",
    "P40_fixed_tail_distance": "40_fixed_tail_distance/verification",
    "P45_improved_distances": "45_improved_distances/verification",
    "P48_negative_energy_amplitudes": "48_negative_energy_amplitudes/verification",
    "P49_negative_annular_distance": "49_negative_annular_distance/verification",
    "P51_exterior_weight_transfer": "51_exterior_weight_transfer/verification",
    "P52_refit_annular_distance": "52_refit_annular_distance/verification",
    "P62_weighted_cauchy": "62_weighted_cauchy/verification",
    "P66_gaussian_holder": "66_gaussian_holder/verification",
    "P67_fractional_gaussian": "67_fractional_gaussian/verification",
    "P71_logarithmic_low_transfer": "71_logarithmic_low_transfer/verification",
    "P91_algebraic_derivative_caps": "91_algebraic_derivative_caps/verification",
    "P93_polar_covering_audit": "93_polar_covering_audit/verification",
    "P94_sharp_original_matrix": "94_sharp_original_matrix/verification",
    "P96_original_auxiliary_recomputation": "96_original_auxiliary_recomputation/verification",
    "P95_refit_global_hypotheses": "95_refit_global_hypotheses/verification",
    "P98_original_origin_recomputation": "98_original_origin_recomputation/verification",
    "P99_original_global_signs": "99_original_global_signs/verification",
    "P101_directed_far_residual": "101_directed_far_residual/verification",
    "P104_original_decay_recomputation": "104_original_decay_recomputation/verification",
    "P105_refit_reference_contract": "105_refit_reference_contract/verification",
    "P90_parameter_uniform_exclusions": "90_parameter_uniform_exclusions/verification",
    "P106_logarithmic_residual_membership": "106_logarithmic_residual_membership/verification",
    # files of the numerical work (with the independent recomputation of the annular residual bounds), in its layout
    "numerics_code": "numerics/code",
    "numerics_data": "numerics/data",
    "P1_checkpoint_state088": "case4/IPM_case4.artifacts/checkpoints/state088_handoff",
    "P1_checkpoint_state131": "case4/IPM_case4.artifacts/checkpoints/state131_last_unverified",
    "P0_proof_texts": "",  # files named <topic>__<file>.md go to <topic>/<file>.md
}

def relocate(base):
    inputs = base / LAYOUT["P10_refit_inputs"]
    for audit in sorted((base / LAYOUT["P20_nb_candidates"]).glob("*.audit.json")):
        name = audit.name[:-len(".audit.json")] + ".json"
        if (inputs / name).exists():
            (base / "numerics" / "data").mkdir(parents=True, exist_ok=True)
            shutil.copy2(inputs / name, base / "numerics" / "data" / name)
    print("prepared relative input layout")


def main():
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    sys.argv = [sys.argv[0]] + [a for a in sys.argv[1:] if not a.startswith("--")]
    cert, base = Path(sys.argv[1]), Path(sys.argv[2])
    manifest = {}
    for line in (cert / "MANIFEST.txt").read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        folder, name, size, digest = line.split("\t")
        manifest[(folder, name)] = (int(size), digest)
    bad = 0
    for (folder, name), (size, digest) in sorted(manifest.items()):
        src = cert / folder / name
        data = src.read_bytes()
        if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
            print("HASH MISMATCH", folder, name)
            bad += 1
            continue
        if folder == "P0_proof_texts":
            topic, _, fname = name.partition("__")
            dst = base / topic / fname
        else:
            dst = base / LAYOUT[folder] / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    if len(sys.argv) > 3:
        shutil.copytree(sys.argv[3], base / "case4" / "IPM_case4.artifacts", dirs_exist_ok=True)
    if "--relocate" in flags and not bad:
        relocate(base)
    print(f"{len(manifest) - bad} files restored under {base}; {bad} hash mismatches")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
