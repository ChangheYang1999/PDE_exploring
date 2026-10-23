"""Direct Cartesian-kernel parity interpolation for the N36 cancellation witness."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from dataclasses import asdict
from evaluate_smooth_state import ReconstructedSmooth
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from parity_axis_inverse import interpolate_vertical

assert json.loads(Path('research/parity_inverse_verification/verification/checks.json').read_text())['status']=='PASS'
tag='common1000_moments_cl2.5_N36M32';source=Path('evidence/smooth_solver')/tag/'final.npz'
model=ReconstructedSmooth(source);sha=hashlib.sha256(source.read_bytes()).hexdigest()
fd=json.loads((Path('evidence/smooth_evaluations')/(tag+'_dense_peaks')/'q2.json').read_text());assert fd['sha256']==sha
# The chosen raw Cartesian cancellation witness is fixed before this run.
x,y=.008009861376660828,3.717848312496212e-8
assert any(p['x']==x and p['y']==y for p in fd['points'])
out=Path('evidence/parity_axis_inverse')/(tag+'_smooth');out.mkdir(parents=True,exist_ok=True)
result={'started_utc':datetime.now(timezone.utc).isoformat(),'source':str(source),'sha256':sha,'proof_sha256':hashlib.sha256(Path('research/smooth_N36_refinement_audit/PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'gate_sha256':hashlib.sha256(Path('research/parity_inverse_verification/verification/checks.json').read_bytes()).hexdigest(),'rows':[]}
for level,(nr,nt,ne,of) in [(1,(40,256,144,4.)),(2,(64,512,224,8.))]:
 q=Quadrature(nr,nt,ne,of,model.L,model.p,16*model.L,1/(1-model.p));inv=DirectInverse(model.rho,q)
 raw=inv.velocity(x,y);rho=float(model.rho(x,y));gx,gy=map(float,cartesian_gradient(model.rho,x,y,.00075,0.))
 for h in [.008,.004,.002]:
  est=interpolate_vertical(inv,x,y,h);ux,uy=float(raw[0]),est['u2']
  tx=(model.cl*x+ux)*gx;ty=(model.cl*y+uy)*gy;R=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(ux*gx+uy*gy)
  row={'level':level,'quadrature':asdict(q),'x':x,'y':y,'interpolation':est,'U':[ux,uy],'raw_U':raw.tolist(),'rho':rho,'gradient':[gx,gy],'R':R,'Nf':nf,'Nv':nv,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv}
  result['rows'].append(row);result['updated_utc']=datetime.now(timezone.utc).isoformat()
  (out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps({'utc':result['updated_utc'],'level':level,'h':h,'R':R,'R_Nf':row['R_Nf'],'U2':uy}),flush=True)
result.update(finished_utc=datetime.now(timezone.utc).isoformat(),status='COMPUTED',scope='One fixed cancellation witness, two independent Cartesian inverse quadratures and three parity-interpolation scales. MP values do not enter construction. No interval or uniform bound.')
(out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n')
