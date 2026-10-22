"""A concrete exact-knot counterexample to numerics' Arb basis selection."""
import os,sys,importlib.util,json,hashlib
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3]
source=Path('numerics/src/x3_arb.py')
spec=importlib.util.spec_from_file_location('num_arb_read_only',source);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
a=mod.X3Arb(prec=180)
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from strain_arb import Data,aa
from fractions import Fraction as F
d=Data()
rows=[]
for idx in (30,100,200,300):
    q=a.knots[idx];vals=a.bspline_values(q)
    # B_0,7 support is [t0,t8], so it is exactly zero at these later knots.
    assert q>a.knots[8]
    got=vals.get(0,(arb(0),arb(0)))[0]
    assert not got.contains(0),(idx,got)
    # The defect also appears after mapping an enclosing radius back to q.
    r=a.L*((1-q)**(-2/(1-a.k))-1).sqrt()
    q_back=-(-(1-a.k)/2*((r/a.L)**2).log1p()).expm1()
    mapped=a.bspline_values(q_back).get(0,(arb(0),arb(0)))[0]
    theta=arb('0.4');badH=a.H(r,theta)[0]
    qexact=F.from_float(float(a.knots_f[idx]));mid,poly=d.poly(qexact,qexact);rr=d.radial(q,mid,poly)
    goodH=(3-d.k)/(1-d.k)*(1-q).log()+sum((rr[m]*(2*m*theta).cos() for m in range(d.nm)),arb(0))+rr[-1]*theta.cos()**(d.p-2)*theta.sin()**2
    assert not goodH.overlaps(badH),(idx,goodH,badH)
    rows.append({'independent_H':goodH.str(35),'numerics_H':badH.str(35),'H_enclosures_disjoint':True,'knot_index':idx,'q':q.str(35),'returned_indices':list(vals),'B0_computed':got.str(35),'B0_exact':0,'excludes_exact_value':True,'q_roundtrip_contains_original':q_back.contains(q),'roundtrip_B0':mapped.str(35),'roundtrip_excludes_exact_value':not mapped.contains(0)})
# Origin derivative formula divides chipow by chi=0.
origin=a.H(arb(0),arb('0.4'))
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source':str(source),'cases':rows,'origin_H_outputs':[v.str(20) for v in origin],'verdict':'REFUTED: exact interior knots fall through strict floating comparisons to first span; basis values exclude the true zero. Origin derivative handling is also nonfinite.'}
(BASE/'research/numerics_audit/evidence/arb_knot_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
