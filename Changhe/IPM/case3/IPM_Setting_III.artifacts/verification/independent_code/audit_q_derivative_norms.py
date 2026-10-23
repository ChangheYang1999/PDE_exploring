"""Independent full-plane derivative norm quadrature from exact frozen input."""
import argparse,json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import mpmath as mp
import numpy as np
from polar_derivative_norms import QNormEvaluator
sys.set_int_max_str_digits(1000000)
ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--tag',required=True);ap.add_argument('--dps',type=int,default=80);ap.add_argument('--order',type=int,default=6);ap.add_argument('--kmax',type=int,default=6);ap.add_argument('--edges',nargs='+',default=['-20','-12','-8','-6','-4','-2','0','2','4','8','12','20']);args=ap.parse_args()
gate=Path('research/polar_derivative_norms/verification/manufactured.json');gd=json.loads(gate.read_text());assert gd['status']=='PASS';assert gd['code_sha256']==hashlib.sha256(Path('independent_code/polar_derivative_norms.py').read_bytes()).hexdigest()
p=Path(args.input);raw=json.loads(p.read_text());inputsha=hashlib.sha256(p.read_bytes()).hexdigest()
dest=Path('evidence/q_derivative_norms')/args.tag;dest.mkdir(parents=True,exist_ok=True)
out=dest/f'quad{args.order}_dps{args.dps}.json'
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',input=str(p),input_sha256=inputsha,source_sha256=raw['source_sha256'],dps=args.dps,order=args.order,kmax=args.kmax,log_radius_edges=args.edges,command=[sys.executable,*sys.argv],gate_sha256=hashlib.sha256(gate.read_bytes()).hexdigest(),code_sha256=gd['code_sha256'],auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=[],shells=[],totals={},scope='Full-plane canonical inverse at every point. Positive exact angular tensor formula; numerical Gauss-Legendre quadrature in log radius on specified finite annuli. Exterior/inner contributions outside the listed radii are not integrated or certified. No uniform error enclosure or limiting regularity claim.')
def pack(v):return mp.nstr(v,min(args.dps-10,65))
def save():record['updated_utc']=datetime.now(timezone.utc).isoformat();out.write_text(json.dumps(record,indent=2)+'\n')
save();model=QNormEvaluator(raw['coefficients'],raw['L'],raw['kappa'],raw['ell'],dps=args.dps,kmax=args.kmax)
record['inverse_working_dps']=model.workdps;save()
# Nodes/weights are computed at working precision, not taken from the producer.
with mp.workdps(args.dps):
    gx,gw=mp.gauss_quadrature(args.order,'legendre');edges=list(map(mp.mpf,args.edges))
    totals={k:{field:mp.mpf(0) for field in ['rho','residual']} for k in range(2,args.kmax+1)}
    for panel,(lo,hi) in enumerate(zip(edges,edges[1:])):
        shell={k:{field:mp.mpf(0) for field in ['rho','residual']} for k in totals}
        for index,(node,weight) in enumerate(zip(gx,gw)):
            t=(lo+hi)/2+(hi-lo)*node/2;w=(hi-lo)*weight/2;r=mp.exp(t)
            start=time.monotonic();values=model.at_radius(r)
            row=dict(panel=panel,index=index,log_radius=pack(t),r=pack(r),weight=pack(w),elapsed_seconds=time.monotonic()-start,values={str(k):{field:pack(v) for field,v in values[k].items()} for k in values})
            record['rows'].append(row)
            for k in totals:
                for field in totals[k]:shell[k][field]+=w*values[k][field];totals[k][field]+=w*values[k][field]
            save();print(json.dumps(dict(utc=record['updated_utc'],tag=args.tag,order=args.order,panel=panel,index=index,seconds=row['elapsed_seconds'])),flush=True)
        record['shells'].append(dict(log_lo=pack(lo),log_hi=pack(hi),norm_squared={str(k):{field:pack(v) for field,v in row.items()} for k,row in shell.items()}))
        save()
    for k,row in totals.items():
        record['totals'][str(k)]=dict(rho_norm_squared=pack(row['rho']),residual_norm_squared=pack(row['residual']),rho_norm=pack(mp.sqrt(row['rho'])),residual_norm=pack(mp.sqrt(row['residual'])),eta=pack(mp.sqrt(row['residual']/row['rho'])))
record['status']='COMPUTED';record['finished_utc']=datetime.now(timezone.utc).isoformat();save();print(json.dumps(dict(tag=args.tag,status=record['status'],totals=record['totals'])),flush=True)
