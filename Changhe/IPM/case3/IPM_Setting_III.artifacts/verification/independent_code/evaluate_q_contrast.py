"""Global compact-coordinate angular contrast, with an exact coarse upper bound."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,json,math
import numpy as np
from numpy.polynomial.legendre import leggauss
from q_checkpoint_reader import QCheckpoint
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);args=ap.parse_args()
c=QCheckpoint(args.snapshot);a=float(c.polynomial(0,-1.));kap=c.kappa
assert a!=0
# Compute the exact binary endpoint and coefficient upper bound as rationals.
af=sum((Fraction(float(v))*(-1)**j for j,v in enumerate(c.coeff[0])),Fraction(0));kf=Fraction(kap)
terms=[]
for k in range(1,c.M):
 Ak=sum((abs(Fraction(float(v))) for v in c.coeff[k]),Fraction(0));Ik=Fraction(1,2*k*(k+1))+kf/(k+1);terms.append((k,Ak,Ik))
upper=2*sum((Ak*Ik for k,Ak,Ik in terms),Fraction(0))/abs(af)
angcoef=2*sum((k*Ak*Ik for k,Ak,Ik in terms),Fraction(0))/abs(af)
rows=[]
for nr,nt in [(128,129),(256,257),(512,513),(1024,1025)]:
 node,weight=leggauss(nr);sig=(node+1)/2
 theta=np.linspace(0,np.pi/2,nt)
 modes=np.arange(1,c.M)
 coeff=np.stack([sig**k*c.polynomial(k,2*sig-1) for k in modes])
 values=coeff.T@np.cos(2*modes[:,None]*theta[None,:])
 oscillation=np.max(values,axis=1)-np.min(values,axis=1)
 contrast=float(np.dot(weight,(.5/sig+kap-.5)*oscillation)/(2*abs(a)))
 assert math.isfinite(contrast) and contrast>=0
 row={'radial_gauss_order':nr,'angular_nodes':nt,'global_compact_coordinate_contrast':contrast,'angular_error_bound_if_radial_integral_exact':float(angcoef)*math.pi/(2*(nt-1))}
 rows.append(row);print(json.dumps(row),flush=True)
# Independent exact manufactured finite-mode formulas.
for kk in [1,2,5]:
 rr=Fraction(1,2*kk*(kk+1))+kf/(kk+1)
 nodes,weights=leggauss(64);sg=(nodes+1)/2
 numerical=float(np.dot(weights,(.5/sg+kap-.5)*sg**kk)/2)
 assert abs(numerical-float(rr))<2e-12*max(1.,float(rr))
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','metadata':c.meta,'a0_exact_binary_endpoint':str(af),'a0_double_endpoint':a,'contrast_refinement':rows,'global_upper_bound_exact_rational':str(upper),'global_upper_bound_upward_float':float(np.nextafter(float(upper),np.inf)),'angular_error_coefficient_exact_rational':str(angcoef),'scope':'Full infinite-radius contrast integral in sigma coordinates. Angular/radial quadrature outputs are numerical estimates; the coarse coefficient bound is exact for the binary interpolant. No exact profile or near-profile exclusion follows from sampled contrast alone.'}
out=Path('evidence/q_contrast');out.mkdir(exist_ok=True);(out/(args.tag+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','tag':args.tag,'finest_contrast':rows[-1]['global_compact_coordinate_contrast'],'global_upper_bound':float(upper),'utc':result['utc']}),flush=True)
