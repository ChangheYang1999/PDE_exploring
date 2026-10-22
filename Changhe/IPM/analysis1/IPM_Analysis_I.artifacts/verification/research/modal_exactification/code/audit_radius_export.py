"""Execute frozen actual ball exporter and loader on exact outward Arb balls."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import ast,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/modal_exactification/evidence';src=BASE.parent/'ipmA-num/src/cert_green.py';text=src.read_text();tree=ast.parse(text)
ball=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='ball')
load=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='load_ball')
code=ast.fix_missing_locations(ast.Module(body=[ball,load],type_ignores=[]));scope={'arb':arb};exec(compile(code,str(src),'exec'),scope)
def dyad(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def bounds(v):
 m,r=dyad(v.mid()),dyad(v.rad());return m-r,m+r
def save(v):
 lo,hi=bounds(v);return {'display':v.str(35),'lower_exact':str(lo),'upper_exact':str(hi)}
ctx.prec=256
cases=[]
for radius in ('1.23451','1.23451e-70','3.14159e-76'):
 x=arb(1,radius);entry=scope['ball'](x);back=scope['load_ball'](entry);lo,hi=bounds(x);bl,bh=bounds(back);okay=bl<=lo and hi<=bh
 cases.append({'radius_input':radius,'initial_ball':save(x),'exported_entry':entry,'reimported_ball':save(back),'encloses_original_ball':okay,'upper_endpoint_loss_exact':str(hi-bh)})
assert not cases[0]['encloses_original_ball'] and not cases[1]['encloses_original_ball']
sha=hashlib.sha256(text.encode()).hexdigest();(E/'radius_export_source_snapshot.py').write_text(text)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'REFUTED universal enclosing-ball claim of current exporter','actual_source_sha256':sha,'actual_source_read_only':str(src),'method':'AST extraction executes exact current nested ball and load_ball; input and output endpoints compared as exact rational dyadics','cases':cases,'cause':'Radius printed to five significant decimal digits can round down by about 1e-5 relatively, whereas multiplier 1+1e-9 cannot cover that loss. The loader outward Arb radius rounding is also too small to restore the missing part.','scope':'Refutes this exporter as a general enclosure operation. Does not by itself show failure of a particular dependent coefficient or final residual enclosure.'}
(E/'radius_export_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
