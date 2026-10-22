"""Independent exact rational checks of saved trial joins and conversion rules."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import io,json,hashlib,sys,importlib.util
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/modal_exactification/evidence';ctx.prec=256;ctx.threads=1
p=E/'trial_v2_h0.008.npz';data=p.read_bytes();d=np.load(io.BytesIO(data));f=lambda v:F.from_float(float(v))
def aa(q):return arb(q.numerator)/q.denominator
def ball(a):return {'ball':a.str(35),'lower':a.lower().str(45),'upper':a.upper().str(45)}
def rational(q):return {'exact_fraction':str(q),'float_for_display':float(q)}
rows=[]
for side in ('inner','outer'):
 vals=[]
 for m in range(d['S'].shape[0]):
  q=(F(int(m==0))+sum(map(f,d['D'][m]),F(0))+f(d['Ei'][m,0])-f(d['S'][m,0])) if side=='inner' else sum(map(f,d['Aout'][m]),F(0))+f(d['Eo'][m,0])-f(d['S'][m,-1])
  vals.append(q)
 i=max(range(len(vals)),key=lambda i:abs(vals[i]));rows.append({'join':side,'nonzero_modes':sum(v!=0 for v in vals),'mode_with_largest_absolute_jump':i,'jump':rational(vals[i]),'mode0_jump':rational(vals[0]),'all_jumps_exact':[str(q) for q in vals]})
endpoints=[]
for name,j in (('rmin',0),('R0',-1)):
 radius=aa(f(d[name]));knot=aa(f(d['knots'][j]));shift=radius.log()-knot
 assert not shift.contains(0)
 endpoints.append({'radius_name':name,'radius_exact':str(f(d[name])),'stored_knot_exact':str(f(d['knots'][j])),'log_exact_radius_minus_stored_knot':ball(shift),'exp_stored_knot_minus_radius':ball(knot.exp()-radius)})
# The exact export used by cert_green.py is float(mid), float(rad).
# Exhibit a finite Arb enclosure whose exported pair misses its exact value.
z=arb(1)/3;m=float(z.mid());r=float(z.rad());miss=abs(F(1,3)-f(m))-f(r)
assert miss>0
conversion={'exact_value':'1/3','arb_before':ball(z),'export_mid_hex':m.hex(),'export_rad_hex':r.hex(),'distance_beyond_exported_radius':rational(miss),'verdict':'REFUTED: raw double midpoint/radius export is not enclosing'}
# Actual midrad.mig call with a directed-rounding counterexample.
spec=importlib.util.spec_from_file_location('snapshot_midrad',E/'midrad.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
m=1.;r=2.**-55;claimed=float(mod.MR(m,r).mig());exact=f(m)-f(r)
assert f(claimed)>exact
mig={'mid':m.hex(),'radius':r.hex(),'returned_lower_bound':claimed.hex(),'exact_inf_abs':str(exact),'overstatement_exact':str(f(claimed)-exact),'verdict':'REFUTED'}
out={'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256(data).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stored_literal_C0_joins':rows,'exact_log_boundary_mismatches':endpoints,'arb_export_counterexample':conversion,'actual_midrad_mig_counterexample':mig,'scope':'The stored dyadic trial and the snapshotted certificate/export code. Exactification is a different trial, still requiring consistent endpoints and outward conversion.'}
(E/'definition_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='stored_literal_C0_joins'},indent=2));print('join counts:',[(q['join'],q['nonzero_modes'],q['jump']) for q in rows])
