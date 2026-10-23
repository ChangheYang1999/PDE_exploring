"""Saved exact JSON -> independent multiprecision canonical point residuals."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,json,hashlib,time
import mpmath as mp
from smooth_mp_primitives import SmoothMP
from smooth_far_coefficients import at_point
ap=argparse.ArgumentParser();ap.add_argument('input_json');ap.add_argument('--tag',required=True);ap.add_argument('--points-file');ap.add_argument('--digits',nargs='+',type=int,default=[75,110]);args=ap.parse_args()
gate=json.loads(Path('research/smooth_full_inverse_primitives/verification/manufactured.json').read_text());assert gate['status']=='PASS'
assert json.loads(Path('research/smooth_far_residual_coefficient/verification/manufactured.json').read_text())['status']=='PASS'
p=Path(args.input_json);inputs=json.loads(p.read_text());dest=Path('evidence/smooth_mp_inverse')/args.tag;dest.mkdir(parents=True,exist_ok=True)
source=Path(inputs['source']);assert hashlib.sha256(source.read_bytes()).hexdigest()==inputs['source_sha256']
if args.points_file:
    pts=json.loads(Path(args.points_file).read_text())
else:
    d=json.loads((Path('evidence/smooth_residual_grid')/args.tag/'diagnostic.json').read_text())
    rows=[r for r in d['rows']if r['inverse_order']==256]
    pts=[]
    for key in ['R_Nf','R_Nv']:
        choices=[r['summary']['all'][key]for r in rows];b=max(choices,key=lambda r:r['maximum']);pts.append([b['x'],b['y']])
    pts.extend([[0,0],[1,0],[0,1],[.003,3e-13],[60,80],[6e11,8e11],[6e249,8e249]])
    coarse=json.loads((Path('evidence/complementary_charts')/args.tag/'diagnostic.json').read_text())
    for key in ['R_Nf','R_Nv']:
        b=coarse['rows'][-1]['summary']['all'][key];pts.append([b['x'],b['y']])
    pts=list(dict.fromkeys(tuple(p)for p in pts))
pointpath=dest/'points.json';pointpath.write_text(json.dumps(pts,indent=2)+'\n')
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=str(source),source_sha256=inputs['source_sha256'],input=str(p),input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),points_file=str(pointpath),points_sha256=hashlib.sha256(pointpath.read_bytes()).hexdigest(),gate_sha256=hashlib.sha256(Path('research/smooth_full_inverse_primitives/verification/manufactured.json').read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/smooth_mp_primitives.py').read_bytes()).hexdigest(),auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),far_code_sha256=hashlib.sha256(Path('independent_code/smooth_far_coefficients.py').read_bytes()).hexdigest(),mpmath_version=mp.__version__,rows=[],scope='Canonical full-plane velocity and Cartesian differentiation of the density both in multiprecision. Finite selected points, no interval certificate, uniform bound, or nearby-profile claim.')
def stamp():
    result['updated_utc']=datetime.now(timezone.utc).isoformat();(dest/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
for digits in args.digits:
    model=SmoothMP(inputs,digits)
    row=dict(digits=digits,working_digits=model.working_digits,a_exact=str(model.a0),c_exact=str(model.c),delta_exact=str(model.delta),effective_exponent_exact=str(model.p),far_leading_defect_exact=str(model.ell*model.p-1),points=[])
    result['rows'].append(row);stamp()
    for x,y in pts:
        started=time.monotonic();values=model.fields(x,y)
        with mp.workdps(model.working_digits):values['far_asymptotics']=at_point(model,x,y)
        values['elapsed_seconds']=time.monotonic()-started;row['points'].append(values);stamp()
        print(json.dumps(dict(utc=result['updated_utc'],digits=digits,point=[x,y],seconds=values['elapsed_seconds'],R_Nf=values['R_Nf'],R_Nv=values['R_Nv'],abs_R=values['abs_R'])),flush=True)
result['finished_utc']=datetime.now(timezone.utc).isoformat();stamp()
