"""Conservative active-time enclosure for the numerics campaign ledger (read-only).

Method: the verifier's ledger-bounds proof. Records with explicit credited chunks ("chunks" or
"active_intervals", endpoints serialized to 0.001 s) are enclosed by [s-q, e+q], q = 0.000502 s, with lower length
e-s-2q; legacy records (whole-second displayed endpoints) are enclosed by [start-30, end+1] with active length
a-0.0005001. Both are grouped by (host, pid). lower = max(|shrunk chunks|, max a_g, |U| - sum(|I_g| - a_g)),
upper = |U|, U = union of all enclosing intervals.
Scope: these bound the union of the elapsed pieces that the trainer CREDITED. Credited chunks run between accepted
step ends and can include checkpoint I/O and short pauses; unrecorded first steps are omitted. This is not a
measurement or certificate of eligible numerical activity.
"""
import datetime, hashlib, json, math, sys
from collections import defaultdict

def stamp(x):
    if isinstance(x, (int, float)): return float(x)
    return datetime.datetime.fromisoformat(x.replace('Z', '+00:00')).timestamp()

def merged(iv):
    out = []
    for a, b in sorted(iv):
        if b <= a: continue
        if not out or a > out[-1][1]: out.append([a, b])
        else: out[-1][1] = max(out[-1][1], b)
    return out

def length(iv): return sum(b - a for a, b in merged(iv))

path = sys.argv[1] if len(sys.argv) > 1 else 'CAMPAIGN_LEDGER.jsonl'
# optional second argument: the verifier's VALIDATION_LEDGER.jsonl; its closed intervals (stop events with
# start_utc, end_utc) are added as exact intervals, giving the union over training and independent validation.
vpath = sys.argv[2] if len(sys.argv) > 2 else None
data = open(path, 'rb').read()
rows = [json.loads(l) for l in data.decode().splitlines() if l.strip()]
Q = 0.000502
exact, groups, nlegacy, nexact = [], defaultdict(lambda: [[], 0.0]), 0, 0
for r in rows:
    ch = r.get('chunks', r.get('active_intervals'))
    if ch is not None:
        nexact += 1
        g = groups[(r.get('host'), r.get('pid'))]
        for a, b in ch:
            a, b = stamp(a), stamp(b)
            g[0].append((a - Q, b + Q)); g[1] += max(0.0, b - a - 2 * Q)
            exact.append((a + Q, b - Q))
        continue
    nlegacy += 1
    s, e, a = stamp(r['interval_start']), stamp(r['interval_end']), float(r['active_seconds'])
    g = groups[(r['host'], r['pid'])]
    g[0].append((s - 30.0, e + 1.0)); g[1] += max(0.0, a - 0.0005001)
vexact = []
if vpath:
    for l in open(vpath):
        r = json.loads(l)
        if r.get('event') == 'stop' and r.get('end_utc'):
            vexact.append((stamp(r['start_utc']), stamp(r['end_utc'])))
num_only = dict(upper=None)
exact_num = list(exact)
exact = exact + vexact
U = list(exact) + [p for g in groups.values() for p in g[0]]
upper = length(U)
missing = sum(length(g[0]) - g[1] for g in groups.values())
lower = max([0.0, length(exact), upper - missing] + [g[1] for g in groups.values()])
times = [b for a, b in U]
print(json.dumps(dict(ledger_sha256=hashlib.sha256(data).hexdigest(), records=len(rows), legacy_records=nlegacy,
    chunk_records=nexact, shrunk_chunk_union_hours_numerics=length(exact_num) / 3600,
    validation_intervals=len(vexact), validation_union_hours=length(vexact) / 3600,
    credited_union_lower_hours=lower / 3600, credited_union_upper_hours=upper / 3600,
    scope='union of credited elapsed pieces (training chunks; plus verifier validation-task wall intervals if given); '
          'includes checkpoint I/O and short pauses; not a certificate of eligible numerical activity',
    last_end_utc=datetime.datetime.fromtimestamp(max(times), datetime.timezone.utc).isoformat() if times else None), indent=1))
