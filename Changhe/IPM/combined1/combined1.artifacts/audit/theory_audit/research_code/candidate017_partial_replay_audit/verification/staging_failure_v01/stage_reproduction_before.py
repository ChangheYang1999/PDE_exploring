"""Stage a fresh, non-executing reproduction inside this lane.

All generated outputs go into the new directory. Other research topics are
read-only dependencies by convention; only the chosen topic is copied.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import shlex
import shutil

LANE = Path(__file__).resolve().parents[1]
PYTHON = 'python3'
TOPICS = {
    'candidate017_partial_replay_audit': ['manifest.json', 'initial_sources.json', 'PROOF_FIRST.json'],
    'numerical_repair_successor_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'theory_final_draft58_audit': ['manifest.json', 'initial_sources.json', 'README_bindings.json', 'parameters.json', 'changes.json', 'PROOF_FIRST.json'],
    'numerical_literal_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    't2_final_summary_audit': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'candidate007_taylor_tolerance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'review_repairs_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json', 'changes.json'],
    'candidate016_complete_bounds_reciprocal': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json', 'PROOF_REVISION.json'],
    'theory_final_draft55_audit': ['manifest.json', 'initial_sources.json', 'additional_sources.json', 'README_bindings.json', 'parameters.json', 'changes.json', 'PROOF_FIRST.json'],
    'candidate016_multimode_replay_audit': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'sharpw_maximum_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'candidate017_conditional_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'PROOF_FIRST.json'],
    'prefix31_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'peer_data_mapping.json', 'PROOF_FIRST.json'],
    'theory_final_draft53_audit': ['manifest.json', 'initial_sources.json', 'parameters.json', 'changes.json', 'PROOF_FIRST.json'],
    'partial_hardy_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'peer_data_mapping.json', 'PROOF_FIRST.json'],
    'candidate016_prefix31_hardy_audit': ['manifest.json', 'initial_sources.json', 'external_bindings.json', 'parameters.json', 'PROOF_FIRST.json'],
    'frozen_report_1630_audit': ['manifest.json', 'initial_sources.json', 'PROOF_FIRST.json'],
    'prefix_endpoint_order_audit': ['manifest.json', 'initial_sources.json', 'parameters.json'],
    'reciprocal_hardy_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json', 'peer_data_mapping.json'],
    'candidate016_prefix_hardy_audit': ['manifest.json', 'initial_sources.json', 'external_bindings.json', 'parameters.json'],
    'divergence_free_upper_review_acceptance': ['manifest.json', 'initial_sources.json', 'parameters.json'],
    'partial_mode_hardy_certificate': ['manifest.json', 'initial_sources.json', 'parameters.json'],
    'constant_display_successors_audit': ['manifest.json', 'initial_sources.json', 'parameters.json'],
    'candidate016_cross_archive_audit': ['manifest.json', 'initial_sources.json', 'external_bindings.json', 'parameters.json'],
    'theory_v08_published_audit': ['manifest.json', 'initial_sources.json', 'accepted_sources.json', 'appendix_bindings.json', 'historical_bindings.json', 'changes.json', 'factor_parameters.json', 'table_parameters.json', 'bracket_parameters.json'],
    'candidate016_dual_replay_audit': ['manifest.json', 'parameters.json', 'external_bindings.json'],
    'divergence_free_negative_norm_upper': ['manifest.json', 'parameters.json'],
    'weight_uniform_review_acceptance': ['manifest.json', 'parameters.json', 'rounding.json', 'T1_bindings.json'],
    'candidate016_complete_forcing_audit': ['manifest.json', 'parameters.json', 'components.json', 'targets.json', 'external_bindings.json'],
    'candidate001_affine_review': ['manifest.json', 'external_bindings.json'],
    'tb_rebal_endpoint_audit': ['manifest.json', 'parameters.json', 'external_bindings.json', 'endpoint_parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'candidate017_dyadic_audit': ['manifest.json', 'parameters.json', 'external_bindings.json', 'candidate017.json.gz'],
    'weight_uniform_gram_audit': ['manifest.json', 'parameters.json'],
    'late_weak_supplement_audit': ['manifest.json', 'rows.json', 'external_bindings.json'],
    'candidate015_dyadic_audit': ['manifest.json', 'parameters.json', 'external_bindings.json'],
    'h18_coverage_audit': ['manifest.json', 'families.json', 'coverage.json', 'registry.json'],
    'candidate001_affine_exclusion': ['input_sources.json'],
    'historical_ratio_floor_audit': ['manifest.json', 'parameters.json', 'input_sources.json'],
    'theory_final_draft43_audit': ['manifest.json', 'parameters.json', 'bracket_parameters.json', 'input_sources.json', 'additional_sources.json', 'changes.json'],
    'family_ceiling_brackets': ['manifest.json', 'parameters.json', 'input_sources.json'],
    'theory_v08_preview2_audit': ['manifest.json', 'parameters.json', 'input_sources.json', 'additional_sources.json', 'appendix_bindings.json', 'reach_parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'candidate016_low_order_forcing_audit': ['manifest.json', 'input_sources.json', 'components.json', 'parameters.json'],
    'endpoint_falsification_repairs': ['manifest.json', 'input_sources.json'],
    'theory_final_draft39_audit': ['manifest.json', 'input_sources.json', 'additional_sources.json', 'parameters.json'],
    'theory_v08_preview1_audit': ['manifest.json', 'initial_sources.json', 'input_sources.json', 'appendix_observations.json'],
    'candidate026_shapes': ['manifest.json', 'candidate026.json', 'parent022.json', 'old_basis.json', 'quotient013.json'],
    'candidate026_point': ['candidate026.json'],
    'candidate026_origin': ['candidate026.json'],
    'candidate026_sectors': ['candidate026.json'],
    'candidate026_weak': ['candidate026.json', 'probe_n19_K1800.json'],
    'candidate025_shapes': ['manifest.json', 'candidate025.json', 'old_basis.json', 'quotient013.json'],
    'theory_v08_factors_audit': ['manifest.json', 'proposed_rows.json'],
    'candidate025_point': ['candidate025.json'],
    'candidate025_origin': ['candidate025.json'],
    'candidate025_sectors': ['candidate025.json'],
    'candidate025_weak': ['candidate025.json', 'probe_n19_K1800.json'],
    'theory_final_draft38_audit': ['manifest.json', 'parameters.json'],
    'finite_radius_reach_audit': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'candidate025_peer_acceptance': ['manifest.json'],
    'numerics_v12_audit': ['manifest.json', 'parameters.json'],
    'pointwise_profile_review_acceptance': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'theory_final_draft34_audit': ['manifest.json', 'parameters.json'],
    'radial_average_review_acceptance': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'outer_remainder_campaign_audit': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'candidate024_shapes': ['manifest.json', 'candidate024.json', 'old_basis.json', 'quotient013.json'],
    'candidate024_point': ['candidate024.json'],
    'candidate024_origin': ['candidate024.json'],
    'candidate024_sectors': ['candidate024.json'],
    'candidate024_weak': ['candidate024.json', 'probe_n19_K1800.json'],
    'candidate023_shapes': ['manifest.json', 'candidate023.json', 'phase1.json', 'old_basis.json'],
    'candidate023_point': ['candidate023.json'],
    'candidate023_origin': ['candidate023.json'],
    'candidate023_sectors': ['candidate023.json'],
    'candidate023_weak': ['candidate023.json', 'probe_n19_K1800.json'],
    'two_weight_campaign_audit': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'pointwise_profile_radial_cap': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'profile_shape_review_acceptance': ['manifest.json'],
    'two_weight_review_acceptance': ['manifest.json'],
    'radial_averaged_remainder_obstruction': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'folded_velocity_upper_audit': ['manifest.json', 'parameters.json', 'mesh.json'],
    'published_v07_audit': ['manifest.json'],
    'profile_velocity_review_acceptance': ['manifest.json'],
    'profile_velocity_shape_cap': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'pointwise_profile_velocity': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'profile_specific_velocity': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'candidate022_shapes': ['manifest.json', 'candidate022.json', 'phase1.json'],
    'candidate022_point': ['candidate022.json'],
    'candidate022_origin': ['candidate022.json'],
    'candidate022_sectors': ['candidate022.json'],
    'candidate022_weak': ['candidate022.json', 'probe_n19_K1800.json'],
    'endpoint_display_repairs': [],
    'fractional_velocity_review_acceptance': [],
    'two_weight_velocity_remainder': ['manifest.json', 'parameters.json'],
    'normalized_velocity_review_acceptance': [],
    'fractional_ball_velocity_lower': ['manifest.json', 'parameters.json'],
    'endpoint_review_repairs': [],
    'normalized_review_repairs': [],
    'theory_v07_audit': ['manifest.json', 'parameters.json'],
    'scaled_complete_cover_audit': ['manifest.json', 'parameters.json'],
    'endpoint_review_acceptance': [],
    'velocity_lower_review_acceptance': [],
    'numerics_final_repair_acceptance': [],
    'candidate021_point': ['candidate021.json'],
    'candidate021_origin': ['candidate021.json'],
    'candidate021_sectors': ['candidate021.json'],
    'candidate021_weak': ['candidate021.json', 'probe_n19_K1800.json'],
    'candidate021_difference': ['candidate020.json', 'candidate021.json'],
    'candidate021_shapes': ['candidate020.json', 'candidate021.json'],
    'normalized_velocity_lower': ['manifest.json', 'parameters.json'],
    'endpoint_pointwise_budget': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'universal_velocity_lower': ['manifest.json', 'parameters.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'sharp_moment_review_acceptance': [],
    'endpoint_gradient_budget': ['manifest.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'angular_tensor_review_acceptance': [],
    'rational_bernstein_audit': ['manifest.json'],
    'scaled_background_reconstruction': ['manifest.json', '017.json', 'N4_polynomials.json.gz'],
    'reference_screening_audit': ['manifest.json', 'parameters.json'],
    'higher_mode_rank_audit': ['manifest.json', 'old_basis.json', 'parent016.json'],
    'annular_moment_review_acceptance': [],
    'moment_interpolation_audit': ['manifest.json', '007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'sharp_amplitude_moment': [],
    'published_v06_audit': ['parameters.json'],
    'numerics_final_v06_audit': ['parameters.json'],
    's1_hessian_refinement': [],
    'candidate015_heldout': ['probe_19_600.json'],
    'candidate015_heldout23': ['probe_23_600.json'],
    'compact_endpoint_audit': [],
    'scaled_dyadic_reproduction': [],
    'candidate016_weak': ['candidate016.json', 'probe_n23_K2400.json', 'probe_n19_K1800.json'],
    'candidate017_weak': ['candidate017.json', 'probe_n23_K2400.json', 'probe_n19_K1800.json'],
    'candidate016_sectors': ['candidate016.json'],
    'candidate017_sectors': ['candidate017.json'],
    'candidate020_point': ['candidate020.json'],
    'candidate020_origin': ['candidate020.json'],
    'candidate020_sectors': ['candidate020.json'],
    'candidate020_weak': ['candidate020.json', 'probe_n19_K1800.json'],
    'candidate020_shapes': ['candidate020.json', 'parent016.json'],
    'scaled_hessian_audit': ['007.json', '016.json', '017.json', 'manifest.json'],
    'hessian_partition_audit': ['manifest.json'],
    'annular_moment_adjustment': [],
    'endpoint_reference_audit': ['manifest.json'],
    'candidate019_point': ['candidate019.json'],
    'candidate019_origin': ['candidate019.json'],
    'candidate019_sectors': ['candidate019.json'],
    'candidate019_weak': ['candidate019.json', 'probe_n19_K1800.json'],
    'endpoint_closure_inequality': ['007_endpoint.json', '013_endpoint.json', '014_endpoint.json'],
    'theory_v06_draft_audit': [],
    'candidate018_point': ['candidate018.json'],
    'candidate018_origin': ['candidate018.json'],
    'candidate018_weak': ['candidate018.json', 'probe_n19_K1800.json', 'probe_n23_K2400.json'],
    'candidate018_sectors': ['candidate018.json'],
    'homogeneous_tail_surgery': [],
    'cutoff_norm_extensions': [],
    'moment_resolved_tail': [
        '007_endpoint.json', '013_endpoint.json', '014_endpoint.json',
    ],
    'finite_tail_surgery': [],
    'tail_cutoff_weighted_cost': [],
    'mode_hardy_mellin': [],
    'joint_scaled_rank_audit': ['old_basis.json'],
    'scaled_rank_audit': ['candidate016.json', 'candidate017.json', 'old_basis.json'],
    'theory_final_h12_audit': [],
    'theory_final_draft15_audit': [],
    'numerics_final_h12_audit': [],
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('topic', choices=sorted(TOPICS))
args = parser.parse_args()
if shutil.disk_usage(LANE).free < 20 * 1024**3:
    raise SystemExit('Below 20 GiB free: do not stage or launch new work.')
source = LANE / 'research' / args.topic
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
run_root = LANE / 'reproductions' / (stamp + '_' + args.topic)
run = run_root / 'c1-t4' if args.topic == 'candidate026_shapes' else run_root
research = run / 'research'
research.mkdir(parents=True, exist_ok=False)
topic = research / args.topic
topic.mkdir()
for sibling in (LANE / 'research').iterdir():
    if sibling.is_dir() and sibling.name != args.topic:
        (research / sibling.name).symlink_to(sibling, target_is_directory=True)
for dirname in ['code', 'source', 'sources']:
    if (source / dirname).exists():
        shutil.copytree(source / dirname, topic / dirname)
shutil.copy2(source / 'PROOF.md', topic / 'PROOF.md')
for supplement in ['COVERAGE.md', 'PROSE_COROLLARY.md', 'ERRATA.md', 'ERRATA_v01.md', 'DEVELOPMENT.md', 'DRAFT17_ADDENDUM.md', 'DRAFT21_ADDENDUM.md',
                   'ACCEPTANCE.md', 'VERIFICATION.md', 'DOMAIN_ADDENDUM.md', 'REVIEW_STATUS.md', 'N23_ADDENDUM.md', 'REPAIRS_REVIEW.md', 'REPAIRS_ACCEPTANCE.md', 'DRAFT24_ADDENDUM.md', 'REPAIRS.md']:
    if (source / supplement).exists():
        shutil.copy2(source / supplement, topic / supplement)
(topic / 'data').mkdir()
(topic / 'verification').mkdir()
if args.topic in {'angular_tensor_review_acceptance', 'sharp_moment_review_acceptance',
                  'endpoint_review_acceptance', 'velocity_lower_review_acceptance',
                  'numerics_final_repair_acceptance', 'normalized_velocity_review_acceptance',
                  'endpoint_review_repairs', 'normalized_review_repairs',
                  'endpoint_display_repairs', 'fractional_velocity_review_acceptance'}:
    shutil.copy2(source / 'verification' / 'manifest.json', topic / 'verification' / 'manifest.json')
if args.topic == 'sharp_amplitude_moment':
    shutil.copy2(source / 'verification' / 'PREPARE.json', topic / 'verification' / 'PREPARE.json')
if args.topic == 'candidate016_low_order_forcing_audit':
    shutil.copy2(source / 'verification/PEER_SOURCE_ATTESTATION.json', topic / 'verification/PEER_SOURCE_ATTESTATION.json')
for filename in TOPICS[args.topic]:
    shutil.copy2(source / 'data' / filename, topic / 'data' / filename)
snapshot_copies = []
if args.topic == 'candidate026_shapes':
    candidate_id = 'C1-N1-026-heldin1e16-legqs25-m16to23'
    original_snapshot = LANE.parent / 'c1-shared/candidate_snapshots' / candidate_id
    private_snapshot = run_root / 'c1-shared/candidate_snapshots' / candidate_id
    private_snapshot.mkdir(parents=True)
    for entry in (source / 'source/SHA256SUMS').read_text().splitlines():
        expected, name = entry.split(maxsplit=1)
        name = name.lstrip('*')
        assert Path(name).name == name
        shutil.copy2(original_snapshot / name, private_snapshot / name)
        digest = hashlib.sha256((private_snapshot / name).read_bytes()).hexdigest()
        assert digest == expected, name
        snapshot_copies.append({'name': name, 'sha256': digest})
    shutil.copy2(source / 'source/SHA256SUMS', private_snapshot / 'SHA256SUMS')
    snapshot_copies.append({
        'name': 'SHA256SUMS',
        'sha256': hashlib.sha256((private_snapshot / 'SHA256SUMS').read_bytes()).hexdigest(),
    })
commands = []
for script in ['check.py', 'check17.py', 'check21.py', 'check_draft23.py', 'check_draft24.py', 'accept.py']:
    if (topic / 'code' / script).exists():
        commands.append(shlex.join([
            'env', 'OMP_NUM_THREADS=1', 'OPENBLAS_NUM_THREADS=1',
            'MKL_NUM_THREADS=1', 'PYTHONDONTWRITEBYTECODE=1',
            'TMPDIR=' + str(LANE / 'tmp'),
            'taskset', '-c', '50,51', 'nice', '-n', '19',
            PYTHON, '-B', str(topic / 'code' / script),
        ]))
if args.topic in {'candidate016_weak', 'candidate017_weak'}:
    commands.append(commands[0] + ' --mode 19 --power 1800')
if args.topic in {'candidate020_weak', 'candidate021_weak', 'candidate022_weak', 'candidate023_weak', 'candidate024_weak', 'candidate025_weak', 'candidate026_weak'}:
    commands[0] += ' --mode 19 --power 1800'
if args.topic == 'candidate019_weak':
    commands[0] += ' --mode 19 --power 1800 --skip-fixtures'
if args.topic == 'candidate018_weak':
    commands.append(commands[0] + ' --mode 23 --power 2400 --skip-fixtures')
manifest = {
    'staged_utc': datetime.now(timezone.utc).isoformat(),
    'topic': args.topic,
    'original': str(source),
    'proof_sha256': hashlib.sha256((topic / 'PROOF.md').read_bytes()).hexdigest(),
    'commands_in_order': commands,
    'calculation_started': False,
    'dependencies': 'Other topic directories are symlinks to frozen lane inputs.',
    'private_snapshot_copies': snapshot_copies,
}
(run / 'STAGING.json').write_text(json.dumps(manifest, indent=2) + '\n')
(run / 'COMMANDS.txt').write_text('\n'.join(commands) + '\n')
print(run)
print('\n'.join(commands))
