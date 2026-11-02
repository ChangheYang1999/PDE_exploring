"""Per-candidate W-D-L (engine winner), worst HP diff, slowest decide, and the non-wins per opponent and seat.
Usage: python3 tmp/wdl_short.py RESULTS.jsonl [SUFFIX=NAME ...]"""
import json, sys
from collections import defaultdict
rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
names = dict(a.split('=', 1)[::-1] for a in sys.argv[2:]) if False else [a.rsplit('=', 1) for a in sys.argv[2:]]
def cname(c):
    for suf, n in names:
        if c.endswith(suf):
            return n
    return c.split(':')[0].split('.')[-1] + c[-30:]
def short(o):
    for a, b in (("bot_research.", ""), ("bots.counters.", "K."), ("bots.economy.frozen.", "E."), ("bots.defense.frozen.", "D."),
                 ("experiments.lead.frozen.", "L."), ("harness.baselines:", "B:"), (":@make", "")):
        o = o.replace(a, b)
    return o[:90]
agg = defaultdict(lambda: [0, 0, 0, 10**9, 0.0, 0, 0, []])
for r in rows:
    cs = r['candidate_side']; c = r['spec_a'] if cs == 0 else r['spec_b']; o = r['spec_b'] if cs == 0 else r['spec_a']
    d = r['hp_diff_a'] * (1 if cs == 0 else -1)
    w = r['winner']; k = 0 if w == cs else (2 if w == 1 - cs else 1)
    a = agg[cname(c)]; a[k] += 1; a[3] = min(a[3], d)
    a[4] = max(a[4], r['decide_max_seconds'][cs] if r.get('decide_max_seconds') else 0)
    p = r['players'][cs] if r.get('players') else {}
    a[5] += p.get('n_rejected', 0); a[6] += len(p.get('bot_errors', [])) + (1 if r.get('error') else 0)
    if k:
        a[7].append(f"{'DL'[k-1]} {d:+d} r{r['rounds']} s{cs} {r.get('scenario') or 'std'} {short(o)}")
for n, a in agg.items():
    print(f"{n}: {a[0]}-{a[1]}-{a[2]} worst {a[3]:+d} max decide {a[4]:.2f}s rejected {a[5]} errors {a[6]}")
    for x in sorted(a[7]):
        print("   ", x)
