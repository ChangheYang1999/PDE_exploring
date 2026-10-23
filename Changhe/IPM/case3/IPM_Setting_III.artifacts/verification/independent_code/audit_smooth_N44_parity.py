"""Independent raw Cartesian-kernel parity audit of two fixed N44 witnesses."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
from dataclasses import asdict
from evaluate_smooth_state import ReconstructedSmooth
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from parity_axis_inverse import interpolate_vertical
from smooth_mp_primitives import SmoothMP

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
gate=Path('research/parity_inverse_verification/verification/checks.json');assert json.loads(gate.read_text())['status']=='PASS'
tag='common1000_moments_cl2.5_N44M40';source=Path('evidence/smooth_solver')/tag/'final.npz';model=ReconstructedSmooth(source)
assert json.loads((out_manifest:=Path('research/smooth_N44_refinement_audit/verification/AUDIT_PIPELINE.json')).read_text())['source_sha256']==sha(source)
exact=Path('evidence/smooth_exact_jets')/tag/'exact_input.json';data=json.loads(exact.read_text());assert data['source_sha256']==sha(source)
points=[(.00800986137674711,1.7256723212410504e-10),(.00309218611001119,3.09218611001119e-11)]
out=Path('research/smooth_N44_refinement_audit/verification/parity');out.mkdir(exist_ok=True)
result={'started_utc':utc(),'source':str(source),'source_sha256':sha(source),'proof_sha256':sha(out.parent.parent/'PARITY_PROOF.md'),'code_sha256':sha(__file__),'gate_sha256':sha(gate),'points':[],'status':'RUNNING'}
def save():result['updated_utc']=utc();(out/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
for x,y in points:
 point={'x':x,'y':y,'MP':[],'rows':[]};result['points'].append(point)
 for digits in [75,110]:
  point['MP'].append(SmoothMP(data,digits=digits).fields(x,y));save()
 for level,(nr,nt,ne,of) in [(1,(40,256,144,4.)),(2,(64,512,224,8.))]:
  tick=time.monotonic();q=Quadrature(nr,nt,ne,of,model.L,model.p,16*model.L,1/(1-model.p));inv=DirectInverse(model.rho,q)
  raw=inv.velocity(x,y);rho=float(model.rho(x,y));gx,gy=map(float,cartesian_gradient(model.rho,x,y,.00075,0.))
  def calculate(ux,uy):
   tx=(model.cl*x+ux)*gx;ty=(model.cl*y+uy)*gy;R=tx+ty-rho;nf=abs(tx)+abs(ty)+abs(rho);nv=abs(rho)+abs(x*gx+y*gy)+abs(ux*gx+uy*gy)
   return {'U':[ux,uy],'rho':rho,'gradient':[gx,gy],'R':R,'Nf':nf,'Nv':nv,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv}
  raw_fields=calculate(float(raw[0]),float(raw[1]))
  for h in [.008,.004,.002]:
   est=interpolate_vertical(inv,x,y,h);row={'level':level,'quadrature':asdict(q),'interpolation':est,'raw':raw_fields,'corrected':calculate(float(raw[0]),est['u2']),'elapsed_since_level_start':time.monotonic()-tick}
   point['rows'].append(row);save();print(json.dumps({'utc':utc(),'x':x,'level':level,'h':h,'raw_NF':raw_fields['R_Nf'],'corrected_NF':row['corrected']['R_Nf'],'MP_NF':point['MP'][-1]['R_Nf']}),flush=True)
result['status']='COMPUTED';result['finished_utc']=utc();result['scope']='Two fixed points; raw and parity-corrected Cartesian inverse, two quadrature orders, three interpolation scales. MP does not enter construction. No interval or uniform certificate.';save()
