"""Audit only the independently supplied numerical inputs in report v25."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];B=ROOT/'05_team_audit/report_v25'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(text):
 result={}
 for line in text.splitlines():
  if not line.startswith('| 0.'):continue
  c=[v.strip().strip('*') for v in line.split('|')[1:-1]]
  if len(c)==12:result[Q(c[0])]=c
 return result
text=(B/'FINAL_REPORT.md').read_text();assert sha(B/'FINAL_REPORT.md')=='a4ef1c91227644a3f7f4ce2478bccc36cf5492b885ecae1330d2249a5bcfc844'
prev=table((ROOT/'05_team_audit/report_v24/FINAL_REPORT.md').read_text());now=table(text);assert set(prev)==set(now) and len(now)==10
hashes={};checks=[]
for rel,ledger in [('05_team_audit/note14_certificate/replay_fine_a50/full_quadratic/accepted.json','V164'),('05_team_audit/stieltjes_v7/a30/accepted.json','V167')]:
 p=ROOT/rel;d=load(p);assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;hashes[rel]=sha(p)
 for name,h in d['sha256'].items():assert sha(ROOT/name)==h;hashes[name]=h
 a=Q(d['alpha']);assert d['safe_D_lower'] in text
 assert Q(now[a][8])<=Q(d['safe_D_lower'])<Q(now[a][8])+Q(1,10**6)
 if ledger=='V164':
  assert d['task_count']==d['total_manifest_tasks']==1847 and d['cells']==13777550 and Q(d['radius'])==10**8
  audit=load(p.parent/'independent_audit.json');i=audit['selected']['I0']
  assert Q('1.9531232')<=Q(i['lower'])<=Q(i['upper'])<=Q('1.9597430')
  assert Q(audit['tail_error']['upper'])<=Q('0.000000018')
  assert Q(audit['tail_main']['lower'])>=Q('0.0001004')
for a,row in now.items():
 changed=[j for j,(u,v) in enumerate(zip(prev[a],row)) if u!=v]
 assert set(changed)==({8,10} if a in (Q(1,2),Q(3,10)) else set()),(a,changed)
 assert Q(row[9])>=Q(row[4])/Q(row[6]) and Q(row[10])>=Q(row[5])/Q(row[8])
 checks.append(dict(alpha=str(a),changed_columns=changed,ratios_outward=True))
assert max(Q(r[10]) for r in now.values())==Q('1.0796') and Q(now[Q(1,2)][10])==Q('1.0796')
assert Q('3.0161919859')-Q('2.7740910337')>=Q('0.2421')
assert Q('2.4531232777')-Q('2.1956570947')>=Q('0.2574')
for s in ['2.4531232777','3.0161919859','13777550','1847','1.9531232','1.9597430','three selected chunks at each exponent']:
 assert s in text,s
for p in (B/'FINAL_REPORT.md',B/'PROOF.md',B/'diff.txt',Path(__file__)):hashes[str(p.relative_to(ROOT))]=sha(p)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger='V170',verdict='CONFIRMED',checks=checks,sha256=hashes,
 scope='Every changed statement and displayed number in report v25; unchanged claims inherited from accepted v24',
 limitation='The still valid upper endpoints precede the separately accepted V168 improvements.')
(B/'accepted.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['ledger'],out['verdict'],checks)
