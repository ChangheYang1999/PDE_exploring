#!/usr/bin/env python3
"""Plan a frozen worker; execution is explicit, guarded and never automatic."""
import argparse
import json
import os
from pathlib import Path
import platform
import runpy
import sys
from runtime import Runtime, HISTORICAL_ROOTS, digest

VERIFY = {'stage13_model_benchmark_v3.py', 'stage13_qualification_v3.py',
          'stage13_reproducibility_v3.py', 'stage13_qualification_review_v3.py',
          'stage13_gradient_refinement_v3.py',
          'verification/scripts/independent_residual_assessment.py',
          'verification/scripts/remote_cancellation_check.py',
          'verification/scripts/stationarity_assessment.py',
          'farfield_asymptotic_audit_20261022_0836/coefficients_audit.py'}
RESEARCH = {'stage13_campaign_v3.py'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--worker', required=True, choices=sorted(VERIFY|RESEARCH))
    parser.add_argument('--plan-output', type=Path)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--allow-research', action='store_true')
    parser.add_argument('--qualification', type=Path)
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    rt = Runtime(args.repo)
    work = args.workspace.expanduser().resolve()
    if work == rt.repo or rt.repo in work.parents or work in rt.repo.parents:
        parser.error('Use an independent writable workspace outside the repository')
    for prefix in HISTORICAL_ROOTS:
        p = Path(prefix)
        if work == p or p in work.parents:
            parser.error('Do not use an original research directory as the writable workspace')
    worker = work/args.worker
    if not worker.is_file() or digest(worker) != digest(rt.research/args.worker):
        parser.error('Working worker must be an exact byte copy of released source')
    state = rt.read(rt.research/'campaign/global181_v3/state.json')
    for name, sha in state['source_sha256'].items():
        if digest(work/name) != sha:
            parser.error('Frozen numerical source differs: '+name)
    rt = Runtime(args.repo, work)
    arguments = args.arguments[1:] if args.arguments[:1] == ['--'] else args.arguments
    arguments = [rt.translate(value) for value in arguments]
    plan = {'worker': str(worker), 'worker_sha256': digest(worker), 'arguments': arguments,
            'working_directory': str(work), 'execution_requested': args.execute,
            'optimization_requested': args.worker in RESEARCH,
            'new_host_qualification_checked': False,
            'outer_driver_launched': False, 'counters_or_radius_reset': False,
            'relocation': rt.record()}
    if args.execute:
        if not os.environ.get('IPM_RESOURCE_SESSION') or not os.environ.get('IPM_RESOURCE_RUN'):
            parser.error('Execution requires a fresh hardware/guard.py resource session')
        if args.worker in RESEARCH:
            if not args.allow_research or args.qualification is None:
                parser.error('Resume requires --allow-research and --qualification')
            q = json.loads(args.qualification.read_text())
            flags = ('fresh_native_provider_replay_passed', 'complete_derivative_check_passed',
                     'independent_J_abs_reproduced', 'resources_rebaselined')
            if not all(q.get(k) is True for k in flags):
                parser.error('Actual new-host qualification is incomplete')
            if q.get('host') != platform.node() or q.get('machine') != platform.machine() or q.get('python_executable') != sys.executable:
                parser.error('Qualification belongs to another host/interpreter')
            if q.get('source_sha256') != state['source_sha256'] or q.get('candidate_sha256') != state['candidate_sha256']:
                parser.error('Qualification does not bind this source/current checkpoint')
            if not q.get('evidence'):
                parser.error('Qualification must bind real test artifacts')
            for row in q['evidence']:
                if digest(row['path']) != row['sha256']:
                    parser.error('New-host evidence changed: '+row['path'])
            epoch = Runtime(args.repo).read(state['epoch_path'])
            if q.get('training_mesh_fingerprint') != epoch['meshes']['training']['fingerprint']:
                parser.error('Qualification uses another production training rule')
            # This branch is explicit guarded research execution only. Loading
            # the native numerical libraries here performs no PDE evaluation.
            from make_qualification import numerical_signature
            if q.get('numerical_signature') != numerical_signature():
                parser.error('Numerical packages or loaded BLAS changed since qualification')
            plan['new_host_qualification_checked'] = True
    if args.plan_output:
        if args.plan_output.exists():
            parser.error('Use a fresh plan output')
        args.plan_output.parent.mkdir(parents=True, exist_ok=True)
        with args.plan_output.open('x') as stream:
            json.dump(plan, stream, indent=2, allow_nan=False)
            stream.write('\n')
    print(json.dumps(plan, indent=2))
    if not args.execute:
        return
    rt.install()
    os.chdir(work)
    os.environ['IPM_WORK_DIR'] = str(work)
    sys.argv = [str(worker)]+arguments
    runpy.run_path(str(worker), run_name='__main__')


if __name__ == '__main__':
    main()
