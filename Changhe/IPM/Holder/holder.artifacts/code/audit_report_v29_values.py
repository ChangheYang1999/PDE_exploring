"""Exact audit of the new values in frozen report v29; V192 scope caveat retained."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib, json
R = Path(__file__).resolve().parents[1]
B = R / '05_team_audit/report_v29'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def table(text):
    out = {}
    for line in text.splitlines():
        if line.startswith('| 0.'):
            cells = [s.strip().strip('*') for s in line.split('|')[1:-1]]
            if len(cells) == 12: out[Q(cells[0])] = cells
    return out
hashes = {}
def accepted(rel, ledger):
    p = R / rel; d = load(p)
    assert d['verdict'] == 'CONFIRMED' and d['ledger'] == ledger
    hashes[rel] = sha(p)
    for name, h in d['sha256'].items():
        assert sha(R/name) == h, name
        hashes[name] = h
    return d
prior = accepted('05_team_audit/report_v28/accepted.json', 'V181')
phases = accepted('08_improved_upper_bounds/phase_interpolation/verification/accepted.json', 'V177')
extra = accepted('05_team_audit/d36_recombination/verification/accepted.json', 'V179')
a10 = accepted('05_team_audit/stieltjes_v7/a10/accepted.json', 'V182')
text = (B/'FINAL_REPORT.md').read_text()
assert sha(B/'FINAL_REPORT.md') == 'f0618332f6532fecaa57d852834394b15d848c8df6407e61a4a2566efc672c48'
old = table((R/'05_team_audit/report_v28/FINAL_REPORT.md').read_text())
now = table(text); assert len(now) == 10 and set(now) == set(old)
C = {Q(1,1000): Q('637.0248486806')}
D = {}
for row in phases['rows']:
    assert row['safe_upper'] in text
    a = Q(row['alpha']); value = Q(row['safe_upper'])
    if row['operator'] == 'C': C[a] = min(C.get(a, value), value)
    else: D[a] = value
for row in extra['rows']:
    if Q(row['alpha']) in [Q(1,5), Q(99,100)]:
        D[Q(row['alpha'])] = Q(row['safe_upper_D'])
        assert row['safe_upper_D'] in text and row['secant_upper_D'] in text
checks = []
for a, row in now.items():
    changed = [j for j,(u,v) in enumerate(zip(old[a],row)) if u != v]
    allowed = {4,9}
    if a in D: allowed |= {5,10}
    if a == Q(1,10): allowed |= {8,10}
    assert set(changed) <= allowed, (a, changed)
    assert C[a] <= Q(row[4]) < C[a]+Q(1,10**6)
    if a in D: assert D[a] <= Q(row[5]) < D[a]+Q(1,10**6)
    else: assert row[5] == old[a][5]
    if a == Q(1,10): assert Q(row[8]) <= Q(a10['safe_D_lower']) < Q(row[8])+Q(1,10**6)
    else: assert row[8] == old[a][8]
    assert Q(row[9]) >= Q(row[4])/Q(row[6])
    assert Q(row[10]) >= Q(row[5])/Q(row[8])
    checks.append(dict(alpha=str(a), changed_columns=changed, outward=True))
assert max(Q(r[9]) for r in now.values()) == Q('1.0564')
assert max(Q(r[10]) for r in now.values()) == Q('1.0786')
assert all(Q('.40') <= Q(r[5])-Q(r[4]) <= Q('.47') for r in now.values())
# New decimal margins are deliberately computed from the exact certified C
# endpoints and the stated lower endpoints, not by subtracting rounded table cells.
projection = [('1/1000','637.3340501785','.3092'),('1/100','64.3702681064','.2821'),
              ('1/20','13.4165946841','.2326'),('1/10','7.0259799882','.1748'),
              ('1/5','3.8088065348','.0656'),('3/10','2.8051718212','.0325')]
# The final 3/10 projection value is extracted from the report, separately
# checked by the preceding accepted report audit. Do not infer a new bound.
for a, lo, gap in projection:
    assert Q(lo)-C[Q(a)] >= Q(gap)
    assert gap[1:] in text
best_lower = {Q(r['alpha']): Q(r['selected_lower_D']['exact_safe_endpoint'])
              for r in load(B/'table_snapshot_v190.json')['rows']}
gaps = ['.3092','.2821','.2326','.1934','.2147','.2435','.2597','.2483','.2346','.1625']
for a,gap in zip(sorted(now),gaps): assert best_lower[a]-C[a] >= Q(gap)
assert Q('2.9418686222')-C[Q(3,10)] >= Q('.1692')
# All introductory upper and lower boxes have valid directed rounding.
box_up = ['637.02485','64.08817','13.18396','6.85115','3.74317','2.77266','2.19341','2.63877','5.00662','42.21759']
box_lo = ['637.33405','64.37026','13.41659','7.04454','3.95786','3.01619','2.45312','2.88706','5.24130','42.38008']
for a,up,lo in zip(sorted(now),box_up,box_lo):
    assert C[a] <= Q(up) and Q(lo) <= best_lower[a]
    assert up in text and lo in text
# Conservative ratios of the rounded upper displays suffice for this prose.
fc = next(line for line in text.splitlines() if line.startswith('| $F^{**}$ |'))
gd = next(line for line in text.splitlines() if line.startswith('| $G^*$ |'))
F = list(map(Q,[s.strip() for s in fc.split('|')[2:-1]]))
G = list(map(Q,[s.strip() for s in gd.split('|')[2:-1]]))
for (a,row),f,g in zip(sorted(now.items()),F,G):
    assert f/Q(row[4])-1 <= Q('.02')
    assert g/Q(row[5])-1 <= Q('.022')
    if a <= Q(1,10):
        assert f/Q(row[4])-1 <= Q('.0017')
        assert g/Q(row[5])-1 <= Q('.003')
assert r'(\frac1{10},\frac{1000}{1003},-\frac1{40})' in text
assert '1.002471319750' in text and '4096' in text and '$20$ chunk sums' in text
assert 'For $\\alpha$ outside the listed values $C_\\alpha<D_\\alpha$ is not' in text
for p in [B/'FINAL_REPORT.md', B/'PROOF.md', B/'diff.txt', B/'table_snapshot_v190.json',
          R/'08_improved_upper_bounds/strict_separation_near_zero/PROOF.md', Path(__file__)]:
    hashes[str(p.relative_to(R))] = sha(p)
out = dict(time_utc=datetime.now(timezone.utc).isoformat(), ledger='V194', verdict='CONFIRMED',
           scope='V29 new theorems and numerical changes only; inherited Section8(4) scope sentence is REFUTED in V192 and must be corrected',
           checks=checks, sha256=hashes)
(B/'accepted_changes.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['time_utc'],out['ledger'],out['verdict'],out['scope'])
