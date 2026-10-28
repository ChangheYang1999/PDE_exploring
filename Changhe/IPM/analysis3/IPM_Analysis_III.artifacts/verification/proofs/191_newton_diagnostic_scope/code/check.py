from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
A=[[F(1),F(1,20)],[F(0),F(1,1000)]]
Ai=[[F(1),F(-50)],[F(0),F(1000)]]
assert [[sum(A[i][k]*Ai[k][j] for k in range(2)) for j in range(2)] for i in range(2)]==[[1,0],[0,1]]
ratio=81*(A[0][1]**2+A[1][1]**2);assert ratio==F(202581,1000000)<1
step=[-Ai[i][0] for i in range(2)];assert step==[-1,0]
lead=(LANE.parent/'s2-lead/NOTES_FOR_TEAM.md').read_text();start=lead.index('## 2026-10-28 13:01Z');end=lead.index('\n## ',start+3);snap=ROOT/'evidence/lead_note42.md';snap.write_text(lead[start:end]+'\n')
files=(ROOT/'PROOF.md',Path(__file__),snap);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED_COUNTEREXAMPLE','squared_test_ratio':str(ratio),'exact_step':[str(x) for x in step],'scalar_step':'0','scope':'general inference only; actual IPM heuristic remains open','hashes':{str(p.relative_to(LANE)):sha(p) for p in files}}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
