"""Order audit of actual high-degree velocity matrices before solver use."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
from smooth_basis import SmoothBasis
from smooth_density_moment_inverse import DensityMomentInverse
ap=argparse.ArgumentParser();ap.add_argument('--radial',type=int,default=36);ap.add_argument('--angular',type=int,default=32);ap.add_argument('--orders',nargs='+',type=int,default=[128,256,512]);ap.add_argument('--full-grid',action='store_true');ap.add_argument('--composite',action='store_true');args=ap.parse_args()
b=SmoothBasis(args.radial,args.angular,.4,1.);nr=2*b.N+3
t=-np.cos(np.pi*(np.arange(nr)+.5)/nr);r=np.maximum(np.sqrt(np.expm1(-np.log((1-t)/2)/b.a)),.015)
if not args.full_grid:r=np.unique(np.r_[r[np.linspace(0,nr-1,9).astype(int)],[.3,3.,30.,300.,3000.]])
root=Path('research/smooth_density_moment_inverse/verification');path=root/('HIGH_N%d_M%d_%s%s.json'%(b.N,b.M,'full'if args.full_grid else 'sample','_composite' if args.composite else ''))
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),arguments=vars(args),basis=b.metadata(),radii=r.tolist(),rows=[],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inverse_sha256=hashlib.sha256(Path('independent_code/smooth_density_moment_inverse.py').read_bytes()).hexdigest(),status='RUNNING')
start=time.monotonic()
for radius in r:
 previous=None;previous_order=None;w=(1+radius*radius)**(-b.a)
 row=dict(radius=float(radius),changes=[])
 for order in args.orders:
  now=time.monotonic();P,Q=DensityMomentInverse(b,order,composite=args.composite).modal_rows(radius)
  if previous is not None:
   changes=[abs(P-previous[0])/w,abs(Q-previous[1])/w]
   peaks=[]
   for matrix in changes:
    loc=np.unravel_index(np.argmax(matrix),matrix.shape)
    peaks.append(dict(value=float(matrix[loc]),stream_mode=2*(int(loc[0])+1),angular_basis=int(loc[1]//(b.N+1)),chebyshev_degree=int(loc[1]%(b.N+1))))
   row['changes'].append(dict(orders=[previous_order,order],max_P=peaks[0],max_Q=peaks[1],seconds=time.monotonic()-now))
  previous=P,Q;previous_order=order
 result['rows'].append(row);result['updated_utc']=datetime.now(timezone.utc).isoformat();path.write_text(json.dumps(result,indent=2)+'\n')
result['status']='COMPLETE';result['elapsed_seconds']=time.monotonic()-start;result['max_last_change']=max(max(row['changes'][-1][k]['value']for k in ['max_P','max_Q'])for row in result['rows']);result['scope']='Empirical matrix differences divided by radial w, before coefficient contraction. No interval bound.';path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['updated_utc','status','elapsed_seconds','max_last_change']}))
