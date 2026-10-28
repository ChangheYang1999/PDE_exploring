"""Rerun the independent recomputations scripts/check_*.py in a restored layout and compare their outputs with the
shipped records scripts/check_*.json.

Usage: python3 run_recomputations.py CERTIFICATES_DIR BASE_DIR [--only NAME,NAME,...] [--timeout SECONDS]

BASE_DIR must first be filled by restore_layout.py (S1_RESTART.md section 3). The recomputations read the verification
records of the later parts, the exact source records, the two original checkpoints and some files of the numerical work,
all of which restore_layout.py puts into BASE_DIR. This program copies the scripts folder it lives in to
BASE_DIR/recomputations/, so that programs which write their record next to themselves do not overwrite the shipped
record, and runs every program single-threaded from BASE_DIR with the verification tree BASE_DIR as its first argument.
Three programs (check_p63.py, check_p66.py, check_p67.py) locate the original checkpoints relative to the parent of
the verification tree; in the copies only, that path is rewritten to BASE_DIR/case4 (the records compare hashes, not
paths).

Each output is compared with the shipped record. Keys that only record elapsed time are ignored, and so is the SHA-256
of the program itself for the three relocated programs (for every other program it must equal the record). A record is
reported as "same", or as DIFFERS with the paths of the differing keys. The shipped record of every program must also
record all_pass true, or contain no false check, and its stored program hash must equal the hash of the shipped
program. A summary table is written to BASE_DIR/run_recomputations.log.

Use a fresh restore (or run this program before run_checks.py): run_checks.py rewrites some of the files read here with
new time stamps, and the records store the SHA-256 hashes of their inputs, which would then differ.
"""
import hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

PY = sys.executable
HERE = Path(__file__).resolve().parent
# {R}: verification tree (BASE_DIR), {N}: numerical data, {C}: original state 131 checkpoint, {A}: annular record of the
# refit nb_stableA2_exact (P25), {S}: exact state 131 record, {E}: seventh-order recurrence record (P32), {O}: output.
JOBS = [
    ('check_jet_distance', ['{R}', '{O}']),
    ('check_p31_constants', ['{A}']),
    ('check_p32_order7', ['{S}', '{E}', '{O}']),
    ('check_p33_p35_constants', ['{A}', '{E}', '{O}']),
    ('check_p39_p40', ['{R}', '{O}']),
    ('check_p43_p47_constants', ['{O}']),
    ('check_p48_p49', ['{R}', '{O}']),
    ('check_p51', ['{R}', '{O}']),
    ('check_p52', ['{R}', '{O}']),
    ('check_p54_p58', ['{R}', '{O}']),
    ('check_p60', ['{O}']),
    ('check_p62', ['{R}', '{O}']),
    ('check_p63', ['{R}', '{O}']),
    ('check_p66', ['{R}', '{O}']),
    ('check_p67', ['{R}', '{O}']),
    ('check_p69', ['{O}']),
    ('check_p70', ['{O}']),
    ('check_p71', ['{R}', '{O}']),
    ('check_p72', ['{O}']),
    ('check_p73', ['{R}', '{O}', '{N}', '{C}']),
    ('check_p74', ['{O}']),
    ('check_p75_p77', ['{O}']),
    ('check_p76', ['{O}']),
    ('check_p78_p79', ['{O}']),
    ('check_p80_p85', ['{O}']),
    ('check_p86_p87', ['{R}', '{O}']),
    ('check_p88_p92', ['{R}', '{O}']),
    ('check_p93_p94', ['{R}', '{N}', '{O}']),
    ('check_p95', ['{R}', '{N}', '{O}']),
    ('check_p96', ['{R}', '{O}']),
    ('check_p97', ['{O}']),
    ('check_p98', ['{R}', '{N}', '{O}']),
]
# programs that locate the original checkpoints relative to the parent of the verification tree: (old, new) text
RELOCATE = {'check_p63': ("ROOT.parents[1] / 'source/case4/IPM_case4.artifacts/checkpoints/",
                          "ROOT / 'case4/IPM_case4.artifacts/checkpoints/"),
            'check_p66': ("ROOT.parent.parent / f'source/case4/IPM_case4.artifacts/checkpoints/",
                          "ROOT / f'case4/IPM_case4.artifacts/checkpoints/"),
            'check_p67': ("ROOT.parent.parent / f'source/case4/IPM_case4.artifacts/checkpoints/",
                          "ROOT / f'case4/IPM_case4.artifacts/checkpoints/")}
TIME_KEYS = {'seconds', 'elapsed', 'elapsed_seconds', 'wall_seconds'}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def diff(a, b, path='', skip=()):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k in TIME_KEYS or k in skip:
                continue
            if k not in a or k not in b:
                out.append(f'{path}/{k} (only in {"shipped" if k in a else "rerun"})')
            else:
                out += diff(a[k], b[k], f'{path}/{k}', skip)
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [f'{path} (length {len(a)} vs {len(b)})']
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in diff(x, y, f'{path}[{i}]', skip)]
    return [] if a == b else [path or '/']


def false_checks(d):
    bad = []
    for k in ('checks', 'claims'):
        if isinstance(d.get(k), dict):
            bad += [n for n, v in d[k].items() if v is False]
    return bad


def main():
    args = sys.argv[1:]
    only = timeout = None
    if '--only' in args:
        i = args.index('--only'); only = set(args[i + 1].split(',')); del args[i:i + 2]
    if '--timeout' in args:
        i = args.index('--timeout'); timeout = float(args[i + 1]); del args[i:i + 2]
    cert, base = Path(args[0]).resolve(), Path(args[1]).resolve()
    if not (base / 'source_audit' / 'state131_exact.json').exists():
        sys.exit('BASE_DIR is not a restored layout: run restore_layout.py first')
    if (base / 'run_checks.log').exists():
        print('note: run_checks.py has already run in BASE_DIR and rewrote some inputs of the recomputations with new time '
              'stamps, so their recorded input hashes will differ; use a fresh restore', flush=True)
    work = base / 'recomputations'
    if work.exists():
        shutil.rmtree(work)
    shutil.copytree(HERE, work, ignore=shutil.ignore_patterns('*.json', '*.log', '__pycache__'))
    for name, (old, new) in RELOCATE.items():
        p = work / f'{name}.py'
        text = p.read_text()
        assert text.count(old) == 1, name
        p.write_text(text.replace(old, new))
    (work / 'out').mkdir()
    sub = {'{R}': str(base), '{N}': str(base / 'numerics' / 'data'),
           '{C}': str(base / 'case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json'),
           '{A}': str(base / '23_admissible_tail_gap/verification/nb_stableA2_exact.annular.json'),
           '{S}': str(base / 'source_audit/state131_exact.json'),
           '{E}': str(base / '32_stationary_order_seven/verification/recur_sine.json')}
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
    rows, failures = [], 0
    for name, template in JOBS:
        if only and name not in only:
            continue
        out = work / 'out' / f'{name}.json'
        if '{O}' not in template:
            out = work / f'{name}.json'
        cmd = [PY, str(work / f'{name}.py')] + [sub.get(x, str(out) if x == '{O}' else x) for x in template]
        t0 = time.monotonic()
        with open(work / 'out' / f'{name}.log', 'w') as lg:
            try:
                rc = subprocess.run(cmd, cwd=base, stdout=lg, stderr=subprocess.STDOUT, env=env,
                                    timeout=timeout or 1500).returncode
            except subprocess.TimeoutExpired:
                rc = 'timeout'
        sec = round(time.monotonic() - t0, 1)
        shipped = json.loads((HERE / f'{name}.json').read_text())
        notes = []
        if 'code_sha256' in shipped and shipped['code_sha256'] != sha(HERE / f'{name}.py'):
            notes.append('shipped record hash differs from the shipped program')
        if shipped.get('all_pass') is False or false_checks(shipped):
            notes.append('shipped record has a failing check')
        if rc != 0 or not out.exists():
            verdict = f'exit status {rc}'
        else:
            d = diff(shipped, json.loads(out.read_text()), skip=('code_sha256',) if name in RELOCATE else ())
            verdict = 'same' if not d else 'DIFFERS at ' + ', '.join(d[:12]) + (' ...' if len(d) > 12 else '')
        ok = verdict == 'same' and not notes
        failures += not ok
        rows.append(f'{name:28s} {sec:8.1f} s  {verdict}' + ('; ' + '; '.join(notes) if notes else ''))
        print(rows[-1], flush=True)
    summary = f'{len(rows)} programs, {failures} not reproduced'
    (base / 'run_recomputations.log').write_text('\n'.join(rows + [summary]) + '\n')
    print(summary)
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()
