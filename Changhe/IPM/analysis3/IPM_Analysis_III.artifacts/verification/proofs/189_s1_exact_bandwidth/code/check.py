from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]

def index(f):
 assert f%2 and f
 return (abs(f)-1)//2

def support(J,M):
 out=set()
 for j in range(M+1):
  out.add(j)
  for n in range(1,J+1):
   out.update((index(2*j+1+2*n),index(2*j+1-2*n)))
 for j in range(J):
  for n in range(1,M+2):
   out.update((index(2*j+1+2*n),index(2*j+1-2*n)))
  out.update((j,index(2*j+3),index(2*j-1)))
 out.update((0,1));assert max(out)==J+M
 return out

cases=[]
for J,M in [(1,2),(2,3),(17,5),(261,2),(261,3),(261,4)]:
 s=support(J,M);cases.append({'J':J,'M':M,'maximum_raw_index':max(s),'raw_slots':J+M+1,'quotient_slots':J+M-1,'current_padded_slots':2*J+2*M+5})
files=[ROOT/'PROOF.md',Path(__file__)]+[LANE.parent/'s2-num/artifacts/code'/s for s in ['fsec.py','opimage.py','exact_trial.py']]
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','cases':cases,'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
