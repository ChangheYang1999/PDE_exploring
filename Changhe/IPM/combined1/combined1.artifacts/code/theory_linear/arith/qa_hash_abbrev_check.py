"""QA check of abbreviated sha256 values (8 hex digits, "...", and optionally 4 or more final hex digits) in the c1-t2
texts (reviews/, notes/, handoff, artifacts/README.md, RUN_STATUS.md, WORKLOG.md) and in the docstrings of
artifacts/arith/*.py.

Run from artifacts/:  python3 -B -u arith/qa_hash_abbrev_check.py
Reads only. Hashes every file below 400 MB in the c1-t2 lane and in R6/{c1-t4, c1-shared, c1-t1, c1-n1, c1-coord,
c1-n3/astra} (about 7700 files, about 10 s), and adds the uncompressed hashes listed in data/COMPRESSED_INPUTS.sha256.
For each abbreviation it prints NOMATCH when no hashed file has that prefix and suffix, with the full hash and file of
any file that has the prefix. A prefix match with a different suffix is a wrong suffix in the text (8 hex digits
identify the file). No prefix match means the file is elsewhere, was replaced, or the prefix is wrong.
Output: stdout only.
"""
import hashlib
import os
import re
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
R6 = LANE.parent
trees = [LANE, R6 / "c1-t4", R6 / "c1-shared", R6 / "c1-t1", R6 / "c1-n1", R6 / "c1-coord", R6 / "c1-n3" / "astra"]
H = {}
for tr in trees:
    for dp, dn, fn in os.walk(tr):
        for f in fn:
            fp = Path(dp) / f
            try:
                if fp.is_symlink() or fp.stat().st_size > 400_000_000:
                    continue
                h = hashlib.sha256()
                with open(fp, "rb") as fh:
                    for chunk in iter(lambda: fh.read(1 << 20), b""):
                        h.update(chunk)
                H.setdefault(h.hexdigest(), []).append(str(fp.relative_to(R6)))
            except OSError:
                pass
for line in (LANE / "artifacts/data/COMPRESSED_INPUTS.sha256").read_text().splitlines():
    h_, f_ = line.split()
    H.setdefault(h_, []).append("c1-t2/artifacts/" + f_ + " (uncompressed, from COMPRESSED_INPUTS.sha256)")
print("hashed files:", sum(len(v) for v in H.values()), flush=True)
hexes = list(H)
texts = sorted(list((LANE / "reviews").glob("*.md")) + list((LANE / "notes").glob("*.md")) +
               [LANE / "handoff/T2_to_T1_v01.md", LANE / "artifacts/README.md", LANE / "RUN_STATUS.md", LANE / "WORKLOG.md"] +
               sorted((LANE / "artifacts/arith").glob("*.py")))
pat = re.compile(r"(?<![0-9a-f])([0-9a-f]{8})\.\.\.([0-9a-f]{4,})?")
bad = 0
total = 0
for tf in texts:
    for ln, line in enumerate(tf.read_text().splitlines(), 1):
        for m in pat.finditer(line):
            total += 1
            a, b = m.group(1), m.group(2)
            hits = [h for h in hexes if h.startswith(a) and (b is None or h.endswith(b))]
            if not hits:
                pre = [h for h in hexes if h.startswith(a)]
                bad += 1
                print("NOMATCH %s:%d %s...%s prefix-only matches: %s" % (tf.relative_to(LANE), ln, a, b or "",
                      [(h, H[h][0]) for h in pre][:3]))
print("abbreviations checked: %d, unmatched: %d" % (total, bad))
