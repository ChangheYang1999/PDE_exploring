"""Audit report v26 against independently accepted inputs, using exact rationals."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'05_team_audit/report_v26'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(text):
 result={}
 for line in text.splitlines():
  if not line.startswith('| 0.'):continue
  c=[v.strip().strip('*') for v in line.split('|')[1:-1]]
  if len(c)==12:result[Q(c[0])]=c
 return result
text=(B/'FINAL_REPORT.md').read_text()
assert sha(B/'FINAL_REPORT.md')=='109a3c81e0ce369d49957fac3222a475d31b50a1d7d19350a6e28eb573a8e2bb'
prev=table((ROOT/'05_team_audit/report_v25/FINAL_REPORT.md').read_text());now=table(text)
assert len(now)==10 and set(now)==set(prev)
hashes={};checks=[];inputs={}
for rel,ledger in [('05_team_audit/report_v25/accepted.json','V170'),
 ('08_improved_upper_bounds/middle_circle_transport/balanced_residual/verification/accepted.json','V168'),
 ('05_team_audit/complex_approximation_reread/accepted.json','V169')]:
 p=ROOT/rel;d=load(p);assert d['verdict']=='CONFIRMED' and d['ledger']==ledger
 hashes[rel]=sha(p);inputs[ledger]=d
 for name,h in d['sha256'].items():assert sha(ROOT/name)==h,name;hashes[name]=h
new={Q(r['alpha']):r for r in inputs['V168']['rows']}
assert [(r['worst_C_phase'],r['worst_D_phase']) for r in new.values()]==[(14,11),(12,11),(11,11),(11,11)]
for a,row in now.items():
 changed=[j for j,(u,v) in enumerate(zip(prev[a],row)) if u!=v]
 assert set(changed)==({4,5,9,10} if a in new else set()),(a,changed)
 for j in changed:assert Q(row[j])<Q(prev[a][j]),(a,j)
 assert Q(row[9])>=Q(row[4])/Q(row[6]) and Q(row[10])>=Q(row[5])/Q(row[8])
 if a in new:
  for j,k in [(4,'safe_upper_C'),(5,'safe_upper_D')]:
   val=new[a][k];assert val in text and Q(val)<=Q(row[j])<Q(val)+Q(1,10**6)
 checks.append(dict(alpha=str(a),changed_columns=changed,ratios_outward=True))
assert max(Q(r[9]) for r in now.values())==Q('1.0564') and Q(now[Q(3,4)][9])==Q('1.0564')
assert max(Q(r[10]) for r in now.values())==Q('1.0787') and Q(now[Q(1,2)][10])==Q('1.0787')
gaps=[('3.0161919859','2.7729133174','0.2432'),('2.9418686222','2.7729133174','0.1689'),
 ('2.8051718212','2.7729133174','0.0322'),('2.4531232777','2.1934924293','0.2596'),
 ('2.8870680072','2.6387739538','0.2482'),('5.2413008171','5.0071216363','0.2341'),
 ('42.380088','42.2225497071','0.1575')]
for lo,up,gap in gaps:assert Q(lo)-Q(up)>=Q(gap) and gap in text
udiffs=[Q(r[5])-Q(r[4]) for r in now.values()]
assert min(udiffs)>=Q('.40') and max(udiffs)<=Q('.49')
for s in ['2.77292','2.19350','2.63878','5.00713','0.40$ to $0.49','worst phases $j=14,12,11,11$','worst phase $j=11$']:
 assert s in text,s
for s in ['2.772914','3.217505','2.193493','2.646007','2.638774','3.098411','5.007122','5.469860']:
 assert s in text,s
for p in (B/'FINAL_REPORT.md',B/'PROOF.md',B/'diff.txt',ROOT/'05_team_audit/phase_identity_reread/PROOF.md',Path(__file__)):
 hashes[str(p.relative_to(ROOT))]=sha(p)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V172',verdict='CONFIRMED',checks=checks,sha256=hashes,
 scope='Full v26 diff: middle-arc coupling, signed mass primitive, compact complex approximation, identity/phase separation, and numerical integration into report',
 limitation='H=0 is the trivial normalized zero function; radius M/H is used only for H>0. V171 later improves five unchanged C entries.')
(B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['ledger'],out['verdict'],checks)
