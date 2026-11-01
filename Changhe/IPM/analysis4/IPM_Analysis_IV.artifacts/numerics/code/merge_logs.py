"""Merge two per-order jsonl logs of the same run: rows with n <= n_split from LOG_OLD and rows with n >= n_split + 1 from LOG_NEW
(later rows override earlier ones for the same order within each file). Header/done rows are dropped. usage: merge_logs.py LOG_OLD LOG_NEW n_split OUT"""
import json, sys
old, new, n_split, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
rows = {}
for path, keep in ((old, lambda n: n <= n_split), (new, lambda n: n > n_split)):
    for l in open(path):
        if not l.strip(): continue
        d = json.loads(l)
        if 'n' in d and 'log10_col_l1' in d and keep(d['n']): rows[d['n']] = d
with open(out, 'w') as f:
    for n in sorted(rows): print(json.dumps(rows[n]), file=f)
print(f'{len(rows)} orders written to {out} (min {min(rows)}, max {max(rows)})')
