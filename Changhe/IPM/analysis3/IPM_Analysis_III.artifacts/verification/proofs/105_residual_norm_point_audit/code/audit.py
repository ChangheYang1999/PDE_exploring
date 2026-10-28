from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[1]
r=json.loads((ROOT/'evidence/points_384.json').read_text())
assert r['status']=='PASS_POINT_CHECKS_ONLY' and r['bits']==384
assert r['code_sha256']==hashlib.sha256((ROOT/'code/check_points.py').read_bytes()).hexdigest()
table=[('-40','5.8561103632e-72','5.8561103633e-72','2.0285703509e-70','2.0285703510e-70'),('-10','2.3286357062e-26','2.3286357063e-26','8.0836830870e-25','8.0836830871e-25'),('0','1.0638622903e-15','1.0638622904e-15','1.4354108071e-8','1.4354108072e-8'),('4','.00010352357242','.00010352357243','171275.298892','171275.298893'),('10','8.1268733611','8.1268733612','11779542.042748','11779542.042750'),('30','.0034358320362','.0034358320363','527.2295047104','527.2295047105')]
for x,row in zip(r['results'],table):
 assert x['t']==row[0]
 for key,lo,hi in [('axis_energy_density',row[1],row[2]),('remainder_energy_density',row[3],row[4])]:
  v=x[key];assert F(lo)<=F(v['lower_exact'])<=F(v['upper_exact'])<=F(hi)
 for key in ['raw_sine_axis_defect','axis_formula_difference','reconstruction_difference']:
  v=x[key];assert F(v['lower_exact'])<=0<=F(v['upper_exact'])
# Reconstruct the exact original basis-to-sine support, independently.
support=set()
for m in range(260):
 terms={}
 for f in [1+2*m,1-2*m,3+2*m,3-2*m]:
  n=(abs(f)-1)//2;terms[n]=terms.get(n,F(0))+F(1 if f>0 else -1,8)
 support.update(n for n,v in terms.items() if v)
assert max(support)==260 and 261 not in support
assert 2*261+(2*max(support)+1)==1043
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','point_count':len(table),'outward_table':table,'maximum_density_sine_index':260,'maximum_residual_sine_index':521,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
