"""best_v9e (bvf), af5 (afq56), g1 and V29 (fresh5a, fresh6) on hrt-w2's 43 fresh5/fresh6 opponents, both seats.
Families by module: lead (experiments.lead), W1 fortress (bots.defense), W3 counters (bots.counters). Run from bot_research."""
import json, collections
opp = list(json.load(open('experiments/economy/opp_fresh56_pools.json')))
def fam(s):
    return 'LEAD' if '.experiments.lead.' in s else 'W1_FORTRESS' if '.bots.defense.' in s else 'W3_COUNTERS' if '.bots.counters.' in s else '?'
def who(s):
    if s.endswith('fill_own=true'): return 'g1f'
    if 'best_v9e:@make' == s.split('.')[-1] or s.endswith('frozen.best_v9e:@make'): return 'best_v9e'
    if s.endswith('attack_from=5'): return 'af5'
    if s.endswith('attack_from=7'): return 'g1'
    if s.endswith('fill_threat=true'): return 'V29'
    return None
res = collections.defaultdict(dict)   # bot -> (opp, seat) -> (outcome, margin, rounds)
for run in ('fresh5a', 'fresh6', 'afq56', 'bvf'):
    for l in open(f'runs/economy/{run}/results.jsonl'):
        r = json.loads(l)
        for seat, (me, other) in enumerate(((r['spec_a'], r['spec_b']), (r['spec_b'], r['spec_a']))):
            b = who(me)
            if b is None or other not in opp: continue
            m = r['hp_diff_a'] if seat == 0 else -r['hp_diff_a']
            w = r['winner']
            o = 'D' if w is None else ('W' if w == seat else 'L')
            res[b][(other, seat)] = (o, m, r['rounds'])
bots = ['best_v9e', 'af5', 'g1', 'V29']
for b in bots: print(b, len(res[b]))
def wdl(b, keys):
    c = collections.Counter(res[b][k][0] for k in keys)
    return f"{c['W']}-{c['D']}-{c['L']}"
keys = sorted(res['best_v9e'])
for f in ('LEAD', 'W1_FORTRESS', 'W3_COUNTERS', None):
    ks = [k for k in keys if f is None or fam(k[0]) == f]
    print(f or 'all', len(ks), ' '.join(f"{b} {wdl(b, ks)}" for b in bots))
ks = [k for k in keys if fam(k[0]) != 'W3_COUNTERS']
print('NOT_BUILT_AGAINST', len(ks), ' '.join(f"{b} {wdl(b, ks)}" for b in bots))
rank = {'W': 2, 'D': 1, 'L': 0}
for b in ('af5', 'g1'):
    worse = [k for k in keys if rank[res[b][k][0]] < rank[res['best_v9e'][k][0]]]
    better = [k for k in keys if rank[res[b][k][0]] > rank[res['best_v9e'][k][0]]]
    print(f'{b} vs best_v9e: worse {len(worse)} better {len(better)}')
    for k in worse: print('   worse', k[1], k[0][-70:], res[b][k], res['best_v9e'][k])
print('best_v9e non-wins:')
for k in keys:
    if res['best_v9e'][k][0] != 'W': print('  ', k[1], k[0][-75:], res['best_v9e'][k], 'af5', res['af5'][k][:2], 'g1', res['g1'][k][:2])
