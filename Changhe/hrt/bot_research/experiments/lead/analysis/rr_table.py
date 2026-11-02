"""Round-robin tables (development, descriptive).
Usage: python3 tmp/rr_table.py RESULTS.jsonl NAME=SUFFIX ...  (a spec gets the first NAME whose SUFFIX ends it)
Prints a markdown matrix (row bot's W-D-L over both seats and the seat-0/seat-1 HP differences of the row bot)
and per-bot totals with worst HP difference, slowest decide call, rejected actions and bot errors."""
import json, sys
from collections import defaultdict
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
names = [a.split('=', 1) for a in sys.argv[2:]]
def nm(spec):
    for n, suf in names:
        if spec.endswith(suf):
            return n
    return spec[-25:]
order = [n for n, _ in names]
cell = defaultdict(list)            # (row, col) -> [(scenario, row seat, result, hp diff of row, rounds)]
tot = defaultdict(lambda: [0, 0, 0, 10**9, 0.0, 0, 0])
errs = []
for r in rows:
    if r.get('error'):
        errs.append(r['error']); continue
    a, b = nm(r['spec_a']), nm(r['spec_b'])
    w = r['winner']; d = r['hp_diff_a']
    for me, other, seat, sign in ((a, b, 0, 1), (b, a, 1, -1)):
        res = 'W' if w == seat else ('D' if w is None else 'L')
        cell[(me, other)].append((r.get('scenario') or 'std', seat, res, sign * d, r['rounds']))
        t = tot[me]; t['WDL'.index(res)] += 1; t[3] = min(t[3], sign * d)
        t[4] = max(t[4], (r.get('decide_max_seconds') or [0, 0])[seat])
        p = (r.get('players') or [{}, {}])[seat]
        t[5] += p.get('n_rejected', 0); t[6] += len(p.get('bot_errors', []))
scens = sorted({c[0] for v in cell.values() for c in v})
for sc in scens:
    print(f"\nStart {sc}: row bot's result, seat 0 / seat 1 HP difference of the row bot\n")
    print('| | ' + ' | '.join(order) + ' |')
    print('| --- ' * (len(order) + 1) + '|')
    for me in order:
        out = []
        for o in order:
            if o == me:
                out.append('-'); continue
            v = sorted(x for x in cell[(me, o)] if x[0] == sc)
            if not v:
                out.append(''); continue
            out.append(''.join(x[2] for x in v) + ' ' + '/'.join(f"{x[3]:+d}" for x in v))
        print(f"| {me} | " + ' | '.join(out) + ' |')
print('\n| bot | W-D-L | worst HP diff | slowest call (s) | rejected | bot errors |')
print('| --- | ---: | ---: | ---: | ---: | ---: |')
for me in sorted(order, key=lambda n: (-(tot[n][0] + tot[n][1] / 2), n)):
    t = tot[me]
    print(f"| {me} | {t[0]}-{t[1]}-{t[2]} | {t[3]:+d} | {t[4]:.2f} | {t[5]} | {t[6]} |")
if errs:
    print('\nharness errors:', len(errs), errs[:3])
