from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shlex
R=Path(__file__).resolve().parents[3];B=R/'research/expanded_objective_span';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();inputs={}
def bind(p,h=None):
 p=Path(p);v=sha(p);assert h is None or h==v,(p,h,v);inputs[str(p.relative_to(R))]=v;return p
def read(p):return json.loads(bind(p).read_text())
def launch(name):
 text=bind(B/'data'/name).read_text();rows=[];args=[]
 for line in text.splitlines():
  if not line.startswith('taskset ') or 'run_quot.py' not in shlex.split(line):continue
  tok=shlex.split(line);a=tok[tok.index('run_quot.py')+1:];args.append(a);rows.append([tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in a[9].split(',')])
 return args,rows
prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
for name,d in read(B/'data/SOURCES.json')['files'].items():bind(B/'data'/name,d['sha256'])
prior=read(R/'research/candidate016_holdout/verification/result.json')
for p,h in prior['inputs'].items():bind(R/p,h)
p=R/'research/candidate_audits/data/C1-N1-016-legqs25-quot013';m=read(p/'MANIFEST.json');e=m['coefficient_files'][0];bind(p/e['name'],e['sha256']);raw=read(p/e['name']);old=[(1,k) if isinstance(k,int) else tuple(k) for k in raw['meta']['pair_k']]
a21,r21=launch('N1_chain021.sh');a22,r22=launch('N1_chain022.sh');new=[(n,(n-1)//2+s) for s in [128,512] for n in range(19,32,2)]
assert len(a21)==1 and len(a22)==2 and r21[0]==old+new and r22==[old,old]
assert len(old)==len(set(old))==67 and len(set(r21[0]))==81
assert int(a21[0][2])==40 and [int(a[2]) for a in a22]==[12,28]
reg=read(R/'research/heldout_probe_register/verification/register.json');assert len(reg['pairs'])==25
assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:32:00+00:00')
extra=[(n,(n-1)//2+s) for n in range(19,32,2) for s in [0,8,32]];checks=[]
for n,K in [tuple(x) for x in reg['pairs']]+extra:
 exps=sorted(k for m,k in r21[0] if m==n);assert n%2==1 and K>=(n-1)//2 and K not in exps
 checks.append({'n':n,'K':K,'objective_exponents_at_n':exps,'coefficient_at_K':0,'outside_span':True,'member_of_25_register':[n,K] in reg['pairs']})
assert (21,522) in r21[0] and len(checks)==46
checks22=[]
for n,K in [tuple(x) for x in reg['pairs']]+[(n,(n-1)//2+s) for n in range(19,32,2) for s in [0,8,32,128,512]]:
 assert n>max(m for m,k in old);checks22.append({'n':n,'K':K,'outside_span':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'registration_utc':reg['utc'],'proposed021_rows':[list(p) for p in r21[0]],'proposed022_rows':[list(p) for p in old],'proposed021_tests':checks,'proposed022_tests':checks22,'previous_diagnostic_21_522_now_objective_row':True,'actual_candidate_bound':False,'inputs':inputs,'foreign_code_executed':False,'status':'PASS exact proposed row lists and polynomial span criterion; actual snapshots and independent new-lemma review OPEN'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'021 probes',len(checks22),'022 probes',sha(B/'verification/result.json'))
