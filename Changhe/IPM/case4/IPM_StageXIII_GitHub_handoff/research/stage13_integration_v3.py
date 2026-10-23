"""V3 production arithmetic with the unchanged V2 independent integrator.

Only the production cache's private scalar-exp field namespace is new. Every
future trial still receives fresh independent V2 stateless whole-axis checks.
Original exact physical reference points may be reused for initial provider
qualification only with source/input/mesh hashes and fresh production values.
"""
import gc
from pathlib import Path
import time

from absolute_common import ROOT, BASE, A_REF, np, read, digest, array_hash
from absolute_model import FrozenLogMesh
import stage13_integration_v2 as old
from stage13_model_v3 import CachedAbsoluteProblem, original_namespace_identity_record

physical_identity = old.physical_identity
_evaluate = old._evaluate
independent_integral = old.independent_integral


def integration_sources():
    result = old.integration_sources()
    result.update({name: digest(ROOT / name) for name in
        ('stage13_integration_v3.py', 'stage13_model_v3.py', 'stage13_stable_exp.py')})
    return result


def independent_sources():
    result = old.integration_sources()
    manifest = ROOT / 'provenance/base_manifest.json'
    result['provenance/base_manifest.json'] = digest(manifest)
    for name, expected in read(manifest).items():
        if name.endswith('.py'):
            actual = digest(BASE / name)
            if actual != expected:
                raise ValueError('Frozen independent base source changed: ' + name)
            result['base/' + name] = actual
    return result


def require_original_namespace():
    value = original_namespace_identity_record()
    if not value['passed']:
        raise ValueError('The original independent field namespace was modified')
    return value


class EpochIntegrator(old.EpochIntegrator):
    def __init__(self, candidate_template, immutable_epoch_record_path):
        import json
        self.candidate = json.loads(json.dumps(candidate_template))
        self.path = Path(immutable_epoch_record_path).resolve(); self.record = read(self.path)
        if self.record.get('schema') != 'stage13_integration_epoch_v3':
            raise ValueError('An explicit V3 integration epoch is required')
        for name in ('training', 'refined'):
            row = self.record['meshes'][name]
            if digest(row['path']) != row['sha256']:
                raise ValueError('Immutable ' + name + ' mesh changed')
            mesh = FrozenLogMesh.load(row['path'])
            if mesh.fingerprint != row['fingerprint']:
                raise ValueError('Immutable mesh identity differs')
            with np.load(row['path'], allow_pickle=False) as arrays:
                blocks = arrays['block_ids'].copy()
            setattr(self, 'mesh' if name == 'training' else 'refined_mesh', mesh)
            setattr(self, 'training_blocks' if name == 'training' else 'refined_blocks', blocks)
        self.workers = int(self.record['workers']); self._fine_problem = None
        require_original_namespace()

    def require_qualified(self, candidate, workers=4):
        r = self.record
        if not (r.get('passed') and r.get('local_qualification_passed') and r.get('whole_axis_qualified')
                and r.get('neighborhood_validated') and r.get('representative_neighborhood_only')
                and not r.get('uniform_rigorous_certificate')
                and r.get('original_physical_trust_design_retained')
                and not r.get('old_points_relabelled_as_new_normalized_design')):
            raise ValueError('The explicit V3 empirical provider qualification is incomplete')
        if r.get('fresh_process_cached_proof_pending', True) or not r.get('fresh_process_cached_replay_released'):
            raise ValueError('Strict fresh-process V3 production release is mandatory')
        if r['physical_identity'] != physical_identity(candidate) or workers != self.workers:
            raise ValueError('V3 endpoint or thread policy differs from its qualification')
        if r['source_sha256'] != integration_sources() or r['independent_source_sha256'] != independent_sources():
            raise ValueError('Production or unchanged independent source closure changed')
        if r['qualification_source_sha256'] != digest(ROOT / 'stage13_qualification_v3.py'):
            raise ValueError('The V3 local qualification source changed')
        for key in ('recovery', 'original_reference_epoch', 'failed_v2_release', 'derivative_record',
                'supplemental_replay_review'):
            ref = r[key]
            if digest(ref['path']) != ref['sha256']:
                raise ValueError('Bound V3 qualification reference changed: ' + key)
        review = read(r['supplemental_replay_review']['path'])
        if review['reviewer_source_sha256'] != digest(ROOT / 'stage13_qualification_review_v3.py'):
            raise ValueError('The V3 replay-review source changed')
        if not (review.get('passed') and review.get('cached_selected_policy_original64epsilon_passed')
                and review.get('cached_selected_policy_vs_original_initial64epsilon_passed')):
            raise ValueError('V3 cached same-policy replay did not satisfy the original strict requirement')
        if review['physical_identity'] != r['physical_identity']:
            raise ValueError('V3 release review belongs to another physical endpoint')
        for ref in [review['policy'], review['original_pending_epoch']] + review['diagnostics']:
            if digest(ref['path']) != ref['sha256']:
                raise ValueError('Bound V3 release evidence changed')
        for proof in review['fresh_native_process_guard_proofs']:
            for ref in (proof['result'], proof['epoch_design']):
                if digest(ref['path']) != ref['sha256']:
                    raise ValueError('Fresh native-process guard/design evidence changed')
        if not r['endpoint_restore']['passed']:
            raise ValueError('Fresh V3 endpoint restoration is unresolved')
        require_original_namespace()
        return True

    def validate(self, p24, extraK, coarse_r=None, predicted_reduction=None, reference=None):
        """Fresh production plus unchanged fresh adaptive independent checks."""
        before = require_original_namespace()
        if coarse_r is None:
            model = CachedAbsoluteProblem(self.candidate, self.mesh, A_REF, block_size=1024, workers=self.workers)
            coarse_r = model.fun(p24, extraK); model.clear_cache(); del model; gc.collect()
        value = super().validate(p24, extraK, coarse_r, predicted_reduction, reference)
        value.update(schema='stage13_trial_whole_axis_validation_v3', source_sha256=integration_sources(),
            independent_source_sha256=independent_sources(),
            original_independent_namespace_before=before,
            original_independent_namespace_after=require_original_namespace(),
            independent_provider='Unchanged V2 stateless fields, origin20/24,85-digit overlap and tails',
            independent_reference_reused=False, production_provider_version=3)
        return value

    def validate_reference(self, p24, extraK, coarse_r, old_validation, proof):
        """Fresh V3 production against an exact, unchanged physical reference.

        This is initial provider qualification only, never a replacement for
        fresh independent validation at a new optimization trial.
        """
        began = time.time(); before = require_original_namespace()
        p = np.asarray(p24, float); extra = np.asarray(extraK, float)
        from absolute_chart import hp_report
        feasible = hp_report(p)
        if feasible['max_abs'] >= 1e-10 or not feasible['physical_bounds'] or abs(feasible['a0']) <= 1e-12:
            raise ValueError('Original physical reference is no longer C5 admissible')
        if old_validation['physical_identity'] != physical_identity(self.candidate, p, extra):
            raise ValueError('The original reference is a different physical point')
        if old_validation['source_sha256'] != old.integration_sources():
            raise ValueError('Original V2 reference source closure changed')
        if old_validation['mesh_sha256'] != self.mesh.fingerprint:
            raise ValueError('Original reference used a different training rule')
        if digest(proof['path']) != proof['sha256']:
            raise ValueError('Original independent reference record changed')
        coarse_r = np.asarray(coarse_r, float)
        if coarse_r.shape != (self.mesh.size,) or not np.all(np.isfinite(coarse_r)):
            raise ValueError('Complete finite fresh production residual required')
        blocks = {}; coarse_J = float(coarse_r @ coarse_r / 2)
        for index, name in enumerate(('origin', 'middle', 'infinity')):
            part = coarse_r[self.training_blocks == index]
            training = float(part @ part / 2)
            fine = float(old_validation['block_contributions'][name]['refined_J'])
            blocks[name] = {'training_J': training, 'refined_J': fine,
                'refinement_error_diagnostic': abs(training - fine),
                'refined_value_is_unchanged_original_stateless_reference': True}
        import math
        mesh_error = math.fsum(row['refinement_error_diagnostic'] for row in blocks.values())
        independent = old_validation['independent_integral']
        if not independent['accuracy_passed']:
            raise ValueError('Original independent reference failed its recorded accuracy criterion')
        fine_J = float(old_validation['refined_J_abs']); difference = abs(coarse_J - independent['J_abs'])
        roundoff = 256 * np.finfo(float).eps * max(coarse_J, fine_J, independent['J_abs'], 1e-300)
        error = max(difference, mesh_error) + independent['error_abs'] + roundoff
        tolerance = max(float(self.record['default_independent_error_abs']),
            float(self.record['relative_accuracy']) * abs(independent['J_abs']))
        accuracy = bool(error <= tolerance and independent['accuracy_passed'])
        return {'schema': 'stage13_trial_whole_axis_validation_v3',
            'physical_identity': physical_identity(self.candidate, p, extra), 'J_abs': independent['J_abs'],
            'error_abs': error, 'training_J_abs': coarse_J, 'refined_J_abs': fine_J,
            'training_difference_from_independent': difference, 'three_block_mesh_error_diagnostic': mesh_error,
            'block_contributions': blocks, 'independent_integral': independent,
            **{key: independent[key] for key in ('origin_tail_error_abs', 'infinity_tail_error_abs',
                'radial_quadrature_error_abs', 'angular_quadrature_error_abs')},
            'accuracy_tolerance': tolerance, 'five_Taylor_validation': feasible,
            'accuracy_passed': accuracy, 'requires_refinement': not accuracy,
            'prediction': None, 'reference_plus_trial_error_abs': error,
            'prediction_uncertainty_fraction_limit': .05,
            'mesh_sha256': self.mesh.fingerprint, 'epoch_path': str(self.path), 'epoch_sha256': digest(self.path),
            'a_ref': A_REF, 'source_sha256': integration_sources(), 'independent_source_sha256': independent_sources(),
            'independent_reference_reused': True, 'original_reference': proof,
            'original_independent_namespace_before': before,
            'original_independent_namespace_after': require_original_namespace(),
            'fresh_production_evaluated_at_exact_original_physical_point': True,
            'finite_quadrature_exact_invariance_claimed': False, 'rigorous_error_certificate': False,
            'seconds': time.time() - began}
