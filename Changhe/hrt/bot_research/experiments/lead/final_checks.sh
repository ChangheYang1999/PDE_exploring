#!/bin/bash
# Written 2026-10-31T23:21Z. End-of-run checks of the lead lane (report section 9). Waits for the lead's last queues (PGIDs given as
# arguments), then: keeps the first smoke game under a new name, regenerates the smoke game with the exact command,
# runs the integrity check, the bot_research tests and the project's own tests, and the integrity check again.
# Outputs in runs/lead/final/. Reads bots/best.py through the smoke game and test_best only; changes no file outside
# bot_research.
cd "$(dirname "$0")/../../.." || exit 1
export PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1
for p in "$@"; do while kill -0 -- "-$p" 2>/dev/null; do sleep 10; done; done
F=bot_research/runs/lead/final
mkdir -p $F
T="taskset -c 20,21 nice -n 19"
echo "start $(date -u +%FT%TZ)"
sha256sum bot_research/bots/best.py bot_research/tests/test_best.py | sed 's/  / /' > $F/hashes.txt
if [ -f bot_research/runs/best-vs-idle-000001.jsonl ] && [ ! -f bot_research/runs/best-vs-idle-000001-0226Z.jsonl ]; then
  mv bot_research/runs/best-vs-idle-000001.jsonl bot_research/runs/best-vs-idle-000001-0226Z.jsonl
fi
echo "smoke start $(date -u +%FT%TZ)"
$T .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle --output bot_research/runs/best-vs-idle-000001.jsonl > $F/smoke.out 2>&1
echo "smoke exit $? $(date -u +%FT%TZ)"
$T .venv/bin/python -B -m bot_research.harness.integrity --json $F/integrity_1.json > $F/integrity_1.out 2>&1
echo "integrity_1 exit $? $(date -u +%FT%TZ)"
$T .venv/bin/python -B -m unittest bot_research.tests.test_best bot_research.tests.test_harness bot_research.tests.test_gamekit > $F/tests_bot_research.out 2>&1
echo "tests_bot_research exit $? $(date -u +%FT%TZ)"
$T .venv/bin/python -B -m unittest discover -s tests > $F/tests_project.out 2>&1
echo "tests_project exit $? $(date -u +%FT%TZ)"
$T .venv/bin/python -B -m bot_research.harness.integrity --json $F/integrity_2.json > $F/integrity_2.out 2>&1
echo "integrity_2 exit $? $(date -u +%FT%TZ)"
sha256sum bot_research/bots/best.py bot_research/tests/test_best.py | sed 's/  / /' > $F/hashes_after.txt
echo "== final_checks done $(date -u +%FT%TZ)"
