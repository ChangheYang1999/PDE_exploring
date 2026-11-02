"""Prospectively record a documentation-only candidate change before C execution."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import ast
import hashlib
import json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E/'analysis/reused_c_validation'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate-sha256', required=True)
    parser.add_argument('--selection-excerpt', required=True)
    args = parser.parse_args()
    oldpath = E/'reused-c-declaration-001.json'
    old = json.loads(oldpath.read_text())
    archive = A/'verification/best_v9f_initial.py'
    frozen = Path(old['frozen_candidate'])
    installed = Path('bot_research/bots/best.py')
    assert digest(archive) == old['candidate_sha256']
    assert digest(installed) == digest(frozen) == args.candidate_sha256
    assert args.candidate_sha256 != old['candidate_sha256']
    assert not (R/old['campaign_name']).exists(), 'No retrospective amendment allowed.'
    note = Path('../hrt-lead/NOTES_FOR_TEAM.md').read_text()
    assert len(args.selection_excerpt) >= 60 and args.selection_excerpt in note
    assert args.candidate_sha256 in note
    assert not any(x in args.selection_excerpt for x in tuple('/' + d + '/' for d in ('mnt', 'home', 'efs', 'tmp')))
    def body(path):
        tree = ast.parse(path.read_text())
        assert isinstance(tree.body[0], ast.Expr)
        assert isinstance(tree.body[0].value, ast.Constant) and isinstance(tree.body[0].value.value, str)
        tree.body = tree.body[1:]
        return ast.dump(tree, include_attributes=False)
    assert body(archive) == body(frozen), 'Candidate differs beyond its module docstring.'
    drift = []
    for path, sha in old['source_sha256'].items():
        if path != str(frozen) and digest(path) != sha:
            drift.append(path)
    assert not drift, drift
    stamp = datetime.now(timezone.utc).isoformat()
    proof = A/'AMENDMENT.md'
    selection = A/'verification/installation_excerpt.md'
    with selection.open('x') as f:
        f.write(args.selection_excerpt+'\n')
    with proof.open('x') as f:
        f.write(f'''# Prospective documentation-only freeze amendment\n\nRecorded {stamp}, before any new pool C game.\n\nThe original declaration fixed candidate SHA256 {old['candidate_sha256']}. The lead corrected the module docstring before installation, so the installed bytes now have SHA256 {args.candidate_sha256}. The original source is preserved in verification/best_v9f_initial.py. Parsing both files and deleting only their initial module docstrings gives exactly equal Python abstract syntax trees, excluding source locations. Every other originally pinned input has the same hash. The installation excerpt is preserved in verification/installation_excerpt.md.\n\nThe seventy-two conditions, opponent parameters, original-engine checks, old controls and fallback rule in PROOF.md remain identical. The amended declaration fixes the installed bytes prospectively. This records a source identity change; it does not reinterpret any already observed candidate game, because none has run. Pool C remains reused selection evidence.\n''')
    source = dict(old['source_sha256'])
    source[str(frozen)] = args.candidate_sha256
    for path in (archive, oldpath, proof, selection, Path(__file__).relative_to(Path.cwd()),
                 E/'publish_reused_c_validation.py'):
        source[str(path)] = digest(path)
    new = dict(old, time_utc=stamp, candidate_sha256=args.candidate_sha256,
               source_sha256=source, supersedes=str(oldpath),
               amendment=str(proof), original_candidate_sha256=old['candidate_sha256'])
    output = E/'reused-c-declaration-002.json'
    with output.open('x') as f:
        json.dump(new, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(dict(time_utc=stamp, declaration=str(output), candidate_sha256=args.candidate_sha256,
                         non_docstring_ast_equal=True, candidate_games_before_amendment=0)))


if __name__ == '__main__':
    main()
