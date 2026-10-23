"""Frozen Q coefficients -> multiprecision full-plane inverse and residuals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,json,hashlib,time,sys
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_mp_primitives import MPQPrimitives,guard_digits

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);ap.add_argument('--points-file');ap.add_argument('--extra-points');ap.add_argument('--digits',nargs='+',type=int,default=[75,110]);args=ap.parse_args()
gate=Path('research/q_full_inverse_primitives/verification/manufactured.json');assert json.loads(gate.read_text())['status']=='PASS'
source=Path(args.snapshot);q=QCheckpoint(source);dest=Path('evidence/q_mp_inverse')/args.tag;dest.mkdir(parents=True,exist_ok=True)
if args.points_file:pts=json.loads(Path(args.points_file).read_text())
else:
    dense=Path('evidence/q_residual_grid')/args.tag/'diagnostic.json';saved=json.loads(dense.read_text());assert saved['sha256']==q.meta['sha256']
    rows=[row for row in saved['rows']if row['inverse_order']==256];pts=[]
    for key in ['R_Nf','R_Nv']:
        row=max((v['summary']['all'][key]for v in rows),key=lambda v:v['maximum']);pts.append([row['x'],row['y']])
    pts.extend([[0,0],[1,0],[0,1],[60,80],[6e249,8e249]])
if args.extra_points:pts.extend(json.loads(Path(args.extra_points).read_text()))
pts=list(dict.fromkeys(tuple(p)for p in pts));pointpath=dest/'points.json';pointpath.write_text(json.dumps(pts,indent=2)+'\n')
inputs=dict(source=str(source),source_sha256=q.meta['sha256'],L=str(F(float(q.L))),kappa=str(F(float(q.kappa))),ell=str(F(float(q.cl))),coefficients=[[str(F(float(v)))for v in row]for row in q.coeff],scope='Exact rational values of the saved binary scalars and Chebyshev coefficients. No normalization repair or producer inverse is included.')
inputpath=dest/'exact_input.json';inputpath.write_text(json.dumps(inputs,indent=2)+'\n')
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',command=[sys.executable,*sys.argv],source=str(source),source_sha256=q.meta['sha256'],metadata=q.meta,exact_input=str(inputpath),exact_input_sha256=hashlib.sha256(inputpath.read_bytes()).hexdigest(),points_file=str(pointpath),points_sha256=hashlib.sha256(pointpath.read_bytes()).hexdigest(),gate_sha256=hashlib.sha256(gate.read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/q_mp_primitives.py').read_bytes()).hexdigest(),density_sha256=hashlib.sha256(Path('independent_code/q_high_precision_density.py').read_bytes()).hexdigest(),auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),mpmath_version=mp.__version__,rows=[],scope='Finite selected-point canonical full-plane inverse and density derivatives evaluated together in multiprecision. Primitive formulas include the complete exterior tail. Comparison of precision is empirical, not an interval certificate or global residual bound. No nearby-profile claim.')
def save():result['updated_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
def pack(v,digits):
    if isinstance(v,dict):return {k:pack(x,digits)for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [pack(x,digits)for x in v]
    if v is None:return None
    return mp.nstr(v,digits)
save()
for target in args.digits:
    work=target+guard_digits(q.N,q.M,q.kappa)
    with mp.workdps(work):
        model=MPQPrimitives(inputs['coefficients'],inputs['L'],inputs['kappa'],inputs['ell'])
        exponent=1-1/model.kappa;defect=model.ell*exponent-1
        vertical_sum=sum(((-1)**j*sum(row,F(0)) for j,row in enumerate(model.raw_coeff)),F(0))
        vertical_amplitude=mp.power(model.L,1/model.kappa)*mp.mpf(vertical_sum.numerator)/(2*vertical_sum.denominator)
        row=dict(target_digits=target,working_digits=work,a=mp.nstr(model.a,target),c=mp.nstr(model.c,target),delta=mp.nstr(model.delta,target),actual_exponent=mp.nstr(exponent,target),far_linear_defect=mp.nstr(defect,target),far_vertical_angular_sum_exact=str(vertical_sum),far_vertical_leading_amplitude=mp.nstr(vertical_amplitude,target),far_axis_limit_R_Nf=mp.nstr(abs(defect)/(1+model.ell*exponent),target)if vertical_sum else None,far_axis_limit_R_Nv=mp.nstr(abs(defect)/(1+exponent),target)if vertical_sum else None,points=[]);result['rows'].append(row);save()
        for x,y in pts:
            started=time.monotonic();v=model.at(x,y);point=pack(v,target);point['elapsed_seconds']=time.monotonic()-started;row['points'].append(point);save()
            print(json.dumps(dict(utc=result['updated_utc'],tag=args.tag,digits=target,point=[x,y],seconds=point['elapsed_seconds'],R_Nf=point['R_Nf'],R_Nv=point['R_Nv'])),flush=True)
if len(result['rows'])>=2:
    with mp.workdps(max(args.digits)+20):
        aa=result['rows'][0];bb=result['rows'][-1];differences=[]
        for a,b in zip(aa['points'],bb['points']):
            errors={}
            for key in ['rho','psi','R','Nf','Nv','R_Nf','R_Nv']:
                if a.get(key)is None or b.get(key)is None:continue
                x=mp.mpf(a[key]);y=mp.mpf(b[key]);errors[key]=mp.nstr(abs(x-y)/(1+abs(y)),30)
            for key in ['U','gradient']:
                errors[key]=mp.nstr(max(abs(mp.mpf(x)-mp.mpf(y))/(1+abs(mp.mpf(y)))for x,y in zip(a[key],b[key])),30)
            differences.append(dict(x=b['x'],y=b['y'],scaled_absolute_differences=errors))
        result['precision_comparisons']=differences
result['status']='COMPUTED';result['finished_utc']=datetime.now(timezone.utc).isoformat();save()
