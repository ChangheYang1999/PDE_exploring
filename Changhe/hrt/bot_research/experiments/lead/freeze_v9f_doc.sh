#!/bin/bash
# Docstring-only correction of frozen best_v9f (written 2026-10-31T18:13Z; run with bash, one process). The known-cost
# sentence of rule 3 was inexact; tmp/drafts/best_v9f_V33C_r1.py is the file checked by freeze_v9f.sh (sha256 36d861fc...),
# tmp/drafts/best_v9f_V33C.py the corrected copy. Checks: the frozen file equals the corrected copy, SHA256SUMS, the
# module ASTs without the module docstring are equal (so every function and constant is the same) and no code reads
# __doc__, then the bot tests, the harness tests and a smoke game (unique output name).
cd "$(dirname "$0")/../../.."
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 TMPDIR="$PWD/bot_research/tmp"
PY="taskset -c 20,21 nice -n 19 .venv/bin/python -B"
OUT=bot_research/runs/lead/freeze_v9f_doc
mkdir -p $OUT
echo "start $(date -u +%FT%TZ)"
cmp bot_research/experiments/lead/frozen/best_v9f.py bot_research/tmp/drafts/best_v9f_V33C.py; echo "cmp exit $?"
(cd bot_research/experiments/lead/frozen && sha256sum -c SHA256SUMS) > $OUT/sha256.out 2>&1
echo "sha256 exit $? $(date -u +%FT%TZ)"
$PY - bot_research/tmp/drafts/best_v9f_V33C_r1.py bot_research/experiments/lead/frozen/best_v9f.py > $OUT/ast.out 2>&1 <<'PYEOF'
import ast, sys
def body(path):
    t = ast.parse(open(path).read())
    if t.body and isinstance(t.body[0], ast.Expr) and isinstance(t.body[0].value, ast.Constant):
        t.body = t.body[1:]
    return ast.dump(t)
src = open(sys.argv[2]).read()
same = body(sys.argv[1]) == body(sys.argv[2])
print("AST equal without module docstring:", same, "| __doc__ in source:", "__doc__" in src)
sys.exit(0 if same and "__doc__" not in src else 1)
PYEOF
echo "ast exit $? $(date -u +%FT%TZ)"
BEST_MODULE=bot_research.experiments.lead.frozen.best_v9f PYTHONPATH=. $PY bot_research/tmp/test_best_v9f_V33C.py > $OUT/tests.out 2>&1
echo "tests exit $? $(date -u +%FT%TZ)"
$PY -m unittest bot_research.tests.test_harness bot_research.tests.test_gamekit > $OUT/tests_harness.out 2>&1
echo "harness tests exit $? $(date -u +%FT%TZ)"
$PY -m td_game.runner --balanced --bot-a bot_research.experiments.lead.frozen.best_v9f:decide --bot-b td_bots.protocol:idle \
  --output bot_research/runs/best-vs-idle-v9f-000002.jsonl > $OUT/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
