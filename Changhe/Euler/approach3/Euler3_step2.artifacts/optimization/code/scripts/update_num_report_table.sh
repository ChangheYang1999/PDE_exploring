#!/bin/bash
# Regenerates the deliverable-A table (scripts/summary_table.py -> status/tmp_summary_table.md) and replaces the "## Deliverable A" section of ../NUM_REPORT.md (up to the next "## " header) with it. v1 (2026-10-30T09:0xZ).
cd "$(dirname "$0")/.."; P12=python3
nice -n 10 taskset -c 31-34 $P12 scripts/summary_table.py | grep -v "^written " > status/tmp_summary_table.md || exit 1
$P12 - <<'PYEOF'
import time, re
p = "../NUM_REPORT.md"; s = open(p).read(); tbl = open("status/tmp_summary_table.md").read().strip("\n")
ts = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
i = s.index("## Deliverable A:"); j = s.index("\n## ", i + 10)
head = "## Deliverable A: numerics summary table of every production run (%s; scripts/summary_table.py from the worker end records results.jsonl; machine-readable validation/summary_runs.json; this section is regenerated at each update)\n\n" % ts
intro = s[i:j].split("\n\n")[1] if len(s[i:j].split("\n\n")) > 2 else ""
new = head + (intro + "\n\n" if intro and not intro.startswith("|") else "") + tbl + "\n"
open(p, "w").write(s[:i] + new + s[j:]); print("NUM_REPORT deliverable-A section replaced at", ts, "rows", tbl.count("\n| "))
PYEOF
