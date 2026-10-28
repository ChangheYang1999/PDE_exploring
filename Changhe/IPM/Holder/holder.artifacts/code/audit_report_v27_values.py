"""Audit the V171 integration into frozen report v27."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import hashlib,json
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/report_v27'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(text):
 out={}
 for line in text.splitlines():
  if not line.startswith('| 0.'):continue
  cells=[s.strip().strip('*') for s in line.split('|')[1:-1]]
  if len(cells)==12:out[Q(cells[0])]=cells
 return out
text=(B/'FINAL_REPORT.md').read_text();assert sha(B/'FINAL_REPORT.md')=='ee8257d63e11b35d5209dfbd49dab1128a6a9cc6e3b0a332e7cfdc95f2f4a4a5'
hashes={};inputs={}
for rel,ledger in [('05_team_audit/report_v26/accepted.json','V172'),('08_improved_upper_bounds/middle_circle_transport/balanced_residual/table37/verification/accepted.json','V171')]:
 p=R/rel;d=load(p);assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;hashes[rel]=sha(p);inputs[ledger]=d
 for name,h in d['sha256'].items():assert sha(R/name)==h,name;hashes[name]=h
prev=table((R/'05_team_audit/report_v26/FINAL_REPORT.md').read_text());now=table(text);assert len(now)==10 and set(now)==set(prev)
rows={Q(r['alpha']):r for r in inputs['V171']['rows']};improved=set(rows)-{Q(1,1000)};checks=[]
for a,row in now.items():
 changed=[j for j,(u,v) in enumerate(zip(prev[a],row)) if u!=v]
 if a in improved:
  assert 4 in changed and set(changed)<={4,9}
  assert Q(rows[a]['safe_upper_C'])<=Q(row[4])<Q(rows[a]['safe_upper_C'])+Q(1,10**6)
  assert all(Q(row[j])<Q(prev[a][j]) for j in changed)
 else:assert not changed
 assert Q(row[9])>=Q(row[4])/Q(row[6]) and Q(row[10])>=Q(row[5])/Q(row[8])
 checks.append(dict(alpha=str(a),changed_columns=changed,ratios_outward=True))
for a,r in rows.items():assert r['safe_upper_C'] in text
assert [rows[a]['worst_phase'] for a in sorted(improved)]==[16,15,15,15,11]
assert 'j=16,15,15,15,14,12,11,11,11' in text
for lo,up,gap in [('637.3340501785','637.0248486806','.3092'),('64.3702681064','64.0882119580','.2820'),
 ('13.4165946841','13.1840592665','.2325'),('7.0259799882','6.8514311158','.1745'),
 ('3.8088065348','3.7431835793','.0656'),('3.9578692464','3.7431835793','.2146'),
 ('42.380088','42.2180350354','.1620')]:assert Q(lo)-Q(up)>=Q(gap)
assert max(Q(r[9]) for r in now.values())==Q('1.0564') and max(Q(r[10]) for r in now.values())==Q('1.0787')
assert all(Q('.40')<=Q(r[5])-Q(r[4])<=Q('.50') for r in now.values())
ctx.prec=384;leading=3*arb(3).sqrt()/(4*arb.pi()*arb('1/100'))
assert arb('42.2180350354')-leading<arb('.8684')
assert arb(now[Q(99,100)][6])-leading>arb('.6532')
for s in ['64.08822','13.18406','6.85144','3.74319','42.21804','0.8684','0.1620','0.2146']:
 assert s in text,s
for p in [B/'FINAL_REPORT.md',B/'PROOF.md',B/'diff.txt',Path(__file__)]:hashes[str(p.relative_to(R))]=sha(p)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V174',verdict='CONFIRMED',checks=checks,
 leading_at_alpha_99_100=dict(lower=str(leading.lower().fmpq()),upper=str(leading.upper().fmpq())),sha256=hashes,
 scope='Full v27 diff, unchanged angular extraction with exponent-specific plans, all changed numerical displays, phase indices, and one-exponent renormalized remainder')
(B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['ledger'],out['verdict'],checks)
