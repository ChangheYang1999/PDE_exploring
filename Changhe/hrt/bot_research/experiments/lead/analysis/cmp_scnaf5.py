"""Pair af5's scnaf5 games with V29's games in hs3 and hs4 by (opponent, scenario, seat)."""
import json
AF = '&attack_from=5'
def rows(p):
    return [json.loads(l) for l in open(p)]
af = rows('runs/economy/scnaf5/results.jsonl')
base = rows('runs/economy/hs3/results.jsonl') + rows('runs/economy/hs4/results.jsonl')
def key(r, me):
    seat = 0 if r['spec_a'] == me else 1
    opp = r['spec_b'] if seat == 0 else r['spec_a']
    return (opp, r['scenario'], seat)
def res(r, seat):
    w = r['winner']
    o = 'D' if w is None else ('W' if w == seat else 'L')
    d = r['hp_diff_a'] if seat == 0 else -r['hp_diff_a']
    return (o, d, r['rounds'])
afspec = {r['spec_a'] for r in af if AF in r['spec_a']} | {r['spec_b'] for r in af if AF in r['spec_b']}
assert len(afspec) == 1
afspec = afspec.pop()
v29 = afspec.replace(AF, '')
idx = {}
for r in base:
    if v29 in (r['spec_a'], r['spec_b']) and r['spec_a'] != r['spec_b']:
        idx.setdefault(key(r, v29), []).append(r)
same = diff = miss = 0
w = {'W': 0, 'D': 0, 'L': 0}
for r in af:
    k = key(r, afspec)
    a = res(r, k[2])
    w[a[0]] += 1
    m = idx.get(k)
    if not m:
        miss += 1
        continue
    bs = {res(x, k[2]) for x in m}
    if bs == {a}:
        same += 1
    else:
        diff += 1
        print('differs', k[0][-40:], k[1], k[2], a, bs)
print('af5', w, 'paired same', same, 'differ', diff, 'unpaired', miss)
