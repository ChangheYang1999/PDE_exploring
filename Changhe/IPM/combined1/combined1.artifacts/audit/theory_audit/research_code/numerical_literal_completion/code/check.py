from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,re,ast,time
B=Path(__file__).resolve().parents[1];tick=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
for row in read('data/manifest.json'):need('binding '+row['local'],sha(B/row['local'])==row['sha256'])
first=read('data/PROOF_FIRST.json');need('proof before code',not first['checker_exists'] and first['proof_sha256']==sha(B/'PROOF.md'))
peer=read('source/N4_result.json');old=read('../numerical_literal_review_acceptance/verification/result.json');prev=read('../numerical_repair_successor_acceptance/verification/result.json')
need('prior accepted checks',old['check_count']==1340 and prev['check_count']==294)
need('N4424 accepted checks',peer['check_count']==len(peer['checks'])==226 and all(peer['checks'].values()))
ast.parse((B/'source/N4_check.py').read_text())
before=(B/'../numerical_repair_successor_acceptance/source/report.md').read_text();after=(B/'source/report.md').read_text();a,b=before.splitlines(),after.splitlines();need('same length',len(a)==len(b));changed=[(i+1,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y];need('exact two lines',len(changed)==2)
need('peer exact changed lines',peer['changed_lines']==[dict(line=i,before=x,after=y) for i,x,y in changed])
phase=next(y for i,x,y in changed if '023 at its final endpoint' in y);reg=next(y for i,x,y in changed if y.startswith('- Held-out registration:'))
pat=r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)';aa=re.findall(pat,before);bb=re.findall(pat,after);need('200records',len(aa)==len(bb)==200)
for i,(x,y) in enumerate(zip(aa,bb)):need('600display transfer '+str(i),x==y)
rats={tuple(map(int,k.split(':'))):Q(v) for k,v in old['phase_final_over12_exact'].items()};raw=json.loads((B/'../numerical_literal_review_acceptance/source/023_weaktests3.json').read_text(),parse_float=Q);values={p:Q(raw['probes'][f'{p[0]}:{p[1]}']['m_lower_bound']) for p in rats};initial={p:values[p]/rats[p] for p in rats}
need('complete25register',set(initial)=={(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]})
selected=[(19,1800),(23,2400),(25,2400),(31,2400)]
for p in selected:
 for q in initial:
  if q[0]==p[0] and q!=p:need('unique mode maximum '+str((p,q)),initial[p]>initial[q])
rank=sorted(values,key=values.get,reverse=True);need('globalfour',rank[:4]==[(19,1800),(19,1200),(19,2400),(23,2400)])
for p,q in zip(rank,rank[1:]):need('complete descending '+str(p),values[p]>=values[q])
lo=min(rats[p] for p in selected);hi=max(rats[p] for p in selected);need('selected endpoints',peer['selected_range_exact']==[str(lo),str(hi)]==prev['selected_ratio_range_exact']);need('nearest low',2*abs(lo-Q('.9389'))<=Q('.0001'));need('nearest high',2*abs(hi-Q('1.0109'))<=Q('.0001'))
for p,q in initial.items():need('peer reconstructed initial '+str(p),Q(peer['initial_exact'][str(p)])==q)
for s in ['Reading (FLOAT comparison','the largest value within each of the modes 19, 23, 25 and 31 at the 12-iteration stage','change by factors 0.9389 to 1.0109','the four largest final values on the full register are (19,1800), (19,1200), (19,2400), (23,2400)']:need('phase repair '+s,s in phase)
for s in ['the saved file hashes e171c051..., which is what the 09:13Z note and the WORKLOG print','the hash 58586004... printed in the 024 snapshot INDEX line and in the 11:00Z note is the reconstructed hash',"the save times are this lane's testimony"]:need('registration repair '+s,s in reg)
need('literal findings removed','the four largest values change by 0.94 to 1.04' not in phase and 'sha256 in NOTES 09:13Z; the hash cited there, 58586004...' not in reg)
need('target pinned',sha(B/'source/report.md')==peer['revised_report_sha256']=='0b0b1e898c54648b792471298b6f6c50d90a30783a7e76fd4c1c80fc57eb9422')
for row in read('data/manifest.json'):need('unchanged '+row['local'],sha(B/row['local'])==row['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'target_sha256':sha(B/'source/report.md'),'display_count':600,'changed_lines':[dict(line=i,before=x,after=y) for i,x,y in changed],'selected_ratio_range_exact':[str(lo),str(hi)],'selected_probes':[list(x) for x in selected],'global_final_four':[list(x) for x in rank[:4]],'foreign_code_executed':False,'verdict':'CONFIRMED both literal repairs and600 unchanged displays. Historical save events, entire-report acceptance and full017 norms remain outside this finite audit.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
