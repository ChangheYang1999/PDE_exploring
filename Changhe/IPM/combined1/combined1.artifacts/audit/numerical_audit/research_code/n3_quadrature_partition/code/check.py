from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/n3_quadrature_partition';start=time.monotonic();sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();prep=json.loads((B/'verification/PREPARE.json').read_text());assert sha(B/'PROOF.md')==prep['proof_sha256'];inputs={str((B/'PROOF.md').relative_to(R)):sha(B/'PROOF.md'),str((B/'verification/PREPARE.json').relative_to(R)):sha(B/'verification/PREPARE.json'),str(Path(__file__).relative_to(R)):sha(__file__)}
for row in prep['sources']:assert sha(R/row['copy'])==row['sha256'];inputs[row['copy']]=row['sha256']
s=(B/'source/legqs_quadcheck.py').read_text()
for line in ['panels = [(Q(0), Q(1, 2))]','range(1, 46)','range(1, 12)','1 - Q(1, 2 ** (k + 1))','Q(1, 2 ** (k + 1)), Q(1, 2 ** k)']:assert line in s,line
panels=[(Q(0),Q(1,2))]+[(1-Q(1,2**k),1-Q(1,2**(k+1))) for k in range(1,46)]+[(Q(1,2**(k+1)),Q(1,2**k)) for k in range(1,12)];repaired=[(Q(0),Q(1,2**12))]+panels[1:];assert len(panels)==len(repaired)==57
endpoints=sorted({q for row in panels+repaired for q in row});cells=[]
for a,b in zip(endpoints,endpoints[1:]):
 m=(a+b)/2;old=sum(x<m<y for x,y in panels);new=sum(x<m<y for x,y in repaired);expected=1+int(Q(1,2**12)<m<Q(1,2));assert old==expected and new==1
 cells.append({'a':str(a),'b':str(b),'original_multiplicity':old,'repaired_multiplicity':new})
covered=1-Q(1,2**46);extra=Q(1,2)-Q(1,2**12);mass=sum(b-a for a,b in panels);assert mass==covered+extra and sum(b-a for a,b in repaired)==covered
rec={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'REFUTED original partition; CONFIRMED exact corrected partition only','panel_count':57,'constant_integral_original':str(mass),'covered_interval_length':str(covered),'extra_mass':str(extra),'duplicated_interval':['1/4096','1/2'],'omitted_t_interval':[str(covered),'1'],'original_panels':[[str(a),str(b)] for a,b in panels],'repaired_panels':[[str(a),str(b)] for a,b in repaired],'all_endpoint_cells':cells,'inputs':inputs,'elapsed_seconds':time.monotonic()-start,'no_candidate_norm_claim':True,'foreign_code_executed':False}
p=B/'verification/result.json'
with p.open('x') as f:json.dump(rec,f,indent=2);f.write('\n')
print('PARTITION_DONE',rec['utc'],'mass',mass,'extra',extra,'cells',len(cells),sha(p),flush=True)
