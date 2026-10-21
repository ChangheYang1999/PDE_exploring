from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast,hashlib,json
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
def exact(n):
 if isinstance(n,ast.Constant):return F(n.value)
 if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -exact(n.operand)
 if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Div):return exact(n.left)/exact(n.right)
 raise ValueError(ast.dump(n))
files=['verifier/inverse/code/density.py','verifier/sampled-physical-actions/code/gradients.py'];w=[F(4,5),F(-1,5),F(4,105),F(-1,280)];evidence=[]
for f in files:
 p=BASE/f;tree=ast.parse(p.read_text());matches=[]
 for n in ast.walk(tree):
  if isinstance(n,ast.List) and len(n.elts)==4:
   try:v=[exact(t) for t in n.elts]
   except ValueError:continue
   if v==w:matches.append(n.lineno)
 assert len(matches)==1,(f,matches)
 evidence.append({'file':f,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'exact_weight_list_line':matches[0]})
moments={str(k):str(sum(wj*(F(j)**k-F(-j)**k) for j,wj in enumerate(w,1))) for k in range(10)}
assert moments['1']=='1' and all(moments[str(k)]=='0' for k in range(9) if k!=1)
pts=json.loads((BASE/'verifier/gauss-sampled-actions/verification/points.json').read_text())['points'];margin=min(min(abs(x),abs(y))-4*max(1,abs(x),abs(y))/32000 for x,y in pts);assert margin>0
obj={'utc':datetime.now(timezone.utc).isoformat(),'input_implementations':evidence,'stencil_moments':moments,'gauss_minimum_axis_margin_at_primary_step':margin,'verdict':'PASS','scope':'Exact antisymmetric stencil weights imply derivative exactness on all polynomials of degree<=8 at fixed h. Source inspection establishes h=max(1,abs(x),abs(y))/32000; this is not an error bound for the trial derivatives.'};(ROOT/'verification/stencil_contract.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj))
