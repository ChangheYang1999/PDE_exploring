"""Audit actual frozen exponent export and current angular/ODE sign paths."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,ast,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/residual_arithmetic/evidence/refreshed_1448';ctx.prec=256;ctx.threads=1
sys.path.insert(0,str(E))
from cert_resid import Certifier,TMArr,MR
# Compile only the actual nested export function; no Green calculation is run.
src=E/'cert_green_outer.py';tree=ast.parse(src.read_text());node=next(n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='exp_terms')
export_node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='export')
namespace={'np':np};exec(compile(ast.fix_missing_locations(ast.Module(body=[export_node,node],type_ignores=[])),str(src),'exec'),namespace)
d=json.loads((BASE/'data_exact/modal_v2.json').read_text());k=F.from_float(float.fromhex(d['scalars_hex']['k']));exact=k-3
alpha=arb(exact.numerator)/exact.denominator
am,ar,_,_=namespace['exp_terms']([[(alpha,[[arb(1)]])]])
m,r=F.from_float(float(am[0])),F.from_float(float(ar[0]));assert r==0 and m!=exact
reader=E/'cert_resid_regions.py';text=reader.read_text();assert 'alphas_rad' not in text
# Current calls have repaired both signs. Test the actual numerical methods with exact toy data.
C=Certifier.__new__(Certifier);C.Q=12;C.M=0;C.Nf=1;C.N1=np.array([[1]]);C.N2=np.array([[0]]);C.S2=np.array([[-1.]]);C.Nmax=2
coef=np.zeros((1,13));coef[0,0]=1;P=TMArr(MR.exact(coef),np.zeros(1));h=.01;hp=np.array([1.]+[h**i for i in range(1,27)])
v=C.conv_scatter(P,P,hp,h,flip2=True)
assert F.from_float(float(v.c.m[0,0]))-F.from_float(float(v.c.r[0,0]))<=1<=F.from_float(float(v.c.m[0,0]))+F.from_float(float(v.c.r[0,0]))
assert 'self.conv_scatter(Qn, Rhat, hpow, h_up, flip2=True)' in (E/'cert_resid.py').read_text()
gd=np.zeros((1,13));gd[0,0]=1;vB=C.ode_tm(MR.exact(np.ones(1)),P,gd,np.array([2.]),h,gsign=-1.0)
assert abs(float(vB.c.m[0,1])-1)<=float(vB.c.r[0,1])
assert 'h_up, gsign=-1.0)' in (E/'cert_resid.py').read_text()
# The product-coefficient invariant is still false in this new snapshot.
a=np.array([[1e16]+[1.]*6+[-1e16]+[0.]*5]);b=np.ones((1,8));p=TMArr(MR.exact(a),np.zeros(1)).mul_poly(MR.exact(b),hp)
pm,pr=F.from_float(float(p.c.m[0,7])),F.from_float(float(p.c.r[0,7]));assert pm+pr<6
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_hashes':{n:hashlib.sha256((E/n).read_bytes()).hexdigest() for n in ('cert_resid.py','cert_green_outer.py','cert_resid_regions.py','midrad.py')},'outer_exponent_export':{'exact_k_minus_3':str(exact),'exported_midpoint':str(m),'exported_radius':str(r),'midpoint_minus_exact':str(m-exact),'interval_contains_exact':False,'actual_reader_ignores_alphas_rad':True},'B_forcing_sign':'CONFIRMED repaired in source and toy ODE coefficient','tangential_sign':'CONFIRMED repaired in source and exact n=1,j=0 trigonometric coefficient','mul_poly_coefficient_invariant':{'verdict':'REFUTED remains','exact':6,'midpoint':str(pm),'radius':str(pr)},'scope':'Exponent export pair excludes the exact specified exponent. No claimed measured final-residual error; extra rounding margins are not a proof of propagation of discarded input uncertainty.'}
(BASE/'research/residual_arithmetic/evidence/current_export_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
