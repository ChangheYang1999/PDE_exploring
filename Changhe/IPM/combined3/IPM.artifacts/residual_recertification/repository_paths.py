#!/usr/bin/env python3
"""Locate the prompt/report repository without a machine-specific path.

Pass an explicit repository/IPM directory, set IPM_REPOSITORY_ROOT, or place
the certificate directory anywhere below the repository.  Source integrity
is checked separately by verify_manifest.py and the numerical producers.
"""
import argparse
import json
import os
from pathlib import Path
import sys

BASE007_RELATIVE = Path(
    'combined1/combined1.artifacts/candidates/'
    'C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json')
PHI013_RELATIVE = Path(
    'combined2/IPM.artifacts/exchange/candidate_snapshots/'
    'C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/phi_007_b18s2_phi_exact.json')


def _is_ipm_directory(path):
    return (path/BASE007_RELATIVE).is_file() and (path/PHI013_RELATIVE).is_file()


def _explicit_ipm_directory(path):
    path = Path(path).expanduser().resolve()
    if _is_ipm_directory(path):
        return path
    if _is_ipm_directory(path/'Changhe/IPM'):
        return path/'Changhe/IPM'
    raise FileNotFoundError('Exact Candidate 007/013 sources were not found below ' + str(path))


def find_ipm_root(explicit=None):
    """Return Changhe/IPM; explicit may name that directory or the repo."""
    if explicit is not None:
        return _explicit_ipm_directory(explicit)
    configured = os.environ.get('IPM_REPOSITORY_ROOT')
    if configured:
        return _explicit_ipm_directory(configured)
    searched = set()
    for start in [Path(__file__).resolve().parent, Path.cwd().resolve()]:
        for parent in [start] + list(start.parents):
            if parent in searched:
                continue
            searched.add(parent)
            candidate = parent/'Changhe/IPM'
            if _is_ipm_directory(candidate):
                return candidate
            if parent.name == 'IPM' and _is_ipm_directory(parent):
                return parent
    raise FileNotFoundError(
        'Could not locate the exact Candidate 007/013 inputs. '
        'Pass --repo-root/--ipm-root or set IPM_REPOSITORY_ROOT.')


def find_repository_root(explicit=None):
    ipm = find_ipm_root(explicit)
    if ipm.name != 'IPM' or ipm.parent.name != 'Changhe':
        raise ValueError('The located IPM directory is outside the established Changhe/IPM tree')
    return ipm.parent.parent


def coefficient_module_directory(explicit=None):
    path = find_ipm_root(explicit)/'combined3/IPM.artifacts/coercivity_residual'
    for filename in ['fields013.py', 'asymptotics013.py']:
        if not (path/filename).is_file():
            raise FileNotFoundError('Required source evaluator is missing: ' + str(path/filename))
    return path


def add_source_modules(explicit=None):
    """Prepend the existing exact-source evaluator directory to sys.path."""
    path = coefficient_module_directory(explicit)
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path)
    args = parser.parse_args()
    ipm = find_ipm_root(args.repo_root)
    print(json.dumps({'repository_root': str(find_repository_root(args.repo_root)),
                      'ipm_root': str(ipm),
                      'coefficient_module_directory': str(coefficient_module_directory(args.repo_root))},
                     indent=2))


if __name__ == '__main__':
    main()
