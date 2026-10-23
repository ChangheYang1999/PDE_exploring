"""Registered candidate inputs -> exact angular convolution at selected radii."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,json,hashlib,time,sys
import mpmath as mp
from q_mp_primitives import MPQPrimitives,guard_digits
from smooth_mp_primitives import SmoothMP,number
from finite_angular_residual_projection import q_modes,smooth_modes,diagnostic

ap=argparse.ArgumentParser();ap.add_argument('kind',choices=['Q','smooth']);ap.add_argument('input_json');ap.add_argument('--tag',required=True);ap.add_argument('--radii-file');ap.add_argument('--digits',type=int,nargs='+',default=[75,110]);args=ap.parse_args()
gate=Path('research/finite_angular_residual_projection/verification/manufactured.json');assert json.loads(gate.read_text())['status']=='PASS'
source=Path(args.input_json);inp=json.loads(source.read_text());raw=Path(inp['source']);assert hashlib.sha256(raw.read_bytes()).hexdigest()==inp['source_sha256']
radii=json.loads(Path(args.radii_file).read_text())if args.radii_file else ['1e-12','1e-6','.001','.01','.1','.3','.7','1','2','5','10','100','1e4','1e8','1e12','1e50','1e250']
out=Path('evidence/finite_angular_projection')/args.tag;out.mkdir(parents=True,exist_ok=True)
report=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',command=[sys.executable,*sys.argv],kind=args.kind,input=str(source),input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source=str(raw),source_sha256=inp['source_sha256'],gate_sha256=hashlib.sha256(gate.read_bytes()).hexdigest(),implementation_sha256=hashlib.sha256(Path('independent_code/finite_angular_residual_projection.py').read_bytes()).hexdigest(),auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),radii=radii,rows=[],scope='Finite radial sample of direct finite Fourier residual coefficients under the full-plane inverse. Angular L2 identity and triangle envelope are exact algebraic formulas, but their computed coefficients have no interval enclosure. This does not replace the task pointwise normalizations or certify a nearby profile.')
def save():report['updated_utc']=datetime.now(timezone.utc).isoformat();(out/'diagnostic.json').write_text(json.dumps(report,indent=2)+'\n')
save()
for target in args.digits:
    if args.kind=='Q':work=target+guard_digits(max(map(len,inp['coefficients']))-1,len(inp['coefficients']),float(F(inp['kappa'])))
    else:work=target+50+len(inp['chebyshev_coefficients'])+max(map(len,inp['chebyshev_coefficients']))-1
    with mp.workdps(work):
        if args.kind=='Q':model=MPQPrimitives(inp['coefficients'],inp['L'],inp['kappa'],inp['ell']);method=q_modes
        else:model=SmoothMP(inp,target);method=smooth_modes
        row=dict(target_digits=target,working_digits=work,points=[]);report['rows'].append(row);save()
        for rt in radii:
            started=time.monotonic();r=mp.mpf(rt)
            point_work=max(work,model.field_working_digits(r,0))if args.kind=='smooth'else work
            with mp.workdps(point_work):
                r=mp.mpf(rt);v=diagnostic(number(model.ell),r,method(model,r),target)
            v['working_digits']=point_work;v['elapsed_seconds']=time.monotonic()-started;row['points'].append(v);save()
            print(json.dumps(dict(utc=report['updated_utc'],tag=args.tag,digits=target,radius=rt,R1=v['R1_projection'],R3=v['R3_projection'],relative_angular_L2=v['R_to_rho_angular_L2'],seconds=v['elapsed_seconds'])),flush=True)
if len(report['rows'])>=2:
    with mp.workdps(max(args.digits)+20):
        comparisons=[]
        for a,b in zip(report['rows'][0]['points'],report['rows'][-1]['points']):
            d={}
            for k in ['R1_projection','R3_projection','angular_R_L2','R_to_rho_angular_L2','estimated_angular_abs_envelope']:
                if a[k]is not None and b[k]is not None:d[k]=mp.nstr(abs(mp.mpf(a[k])-mp.mpf(b[k]))/(1+abs(mp.mpf(b[k]))),30)
            comparisons.append(dict(radius=b['radius'],scaled_absolute_differences=d))
        report['precision_comparisons']=comparisons
report['status']='COMPUTED';report['finished_utc']=datetime.now(timezone.utc).isoformat();save()
