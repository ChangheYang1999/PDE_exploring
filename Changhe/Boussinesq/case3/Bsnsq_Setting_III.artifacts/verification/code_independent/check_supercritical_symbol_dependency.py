"""Exact scaling controls for the P229 appendix, written after its proof."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import time,json,hashlib
start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();checks={}
root=Path(__file__).resolve().parents[1];v=root/'research/229_supercritical_neighbourhood_symbols/verification'
b,j=s.symbols('beta j',positive=True);ss=1/b;m=1-2/b
# The exponent of tau converts to the negative exponent divided by beta in r.
for name,timepow,wanted in [('velocity',b-1,ss-1+j),('vorticity',-1,ss+j),('temperature',b-2,-m+j)]:
 derived=-(timepow-b*j)/b
 checks[name+'_derivative_prefactor']=s.simplify(derived-wanted)==0
 checks[name+'_profile_symbol_inverse']=s.simplify(-derived+ wanted)==0
checks['Du_annular_tau_cancellation']=s.simplify(-1+b*ss)==0
checks['gradTheta_annular_tau_cancellation']=s.simplify(-2+2*b*ss)==0
checks['theta_annular_tau_cancellation']=s.simplify(b-2-b*m)==0
checks['u_annular_tau_cancellation']=s.simplify(b-1-b*(1-ss))==0
checks['omega_annular_tau_cancellation']=s.simplify(-1+b*ss)==0
# General amplitudes differentiated in physical coordinates.
tau,x,y=s.symbols('tau x y',positive=True);O=s.Function('O');T=s.Function('T');V1=s.Function('V1');V2=s.Function('V2')
X=x/tau**b;Y=y/tau**b;oo=O(X,Y);tt=T(X,Y);u=s.Matrix([tau**(b-1)*V1(X,Y),tau**(b-1)*V2(X,Y)])
omega=oo/tau;theta=tau**(b-2)*tt
physO=-s.diff(omega,tau)+u[0]*s.diff(omega,x)+u[1]*s.diff(omega,y)
expectedO=tau**-2*(oo+(b*X+V1(X,Y))*s.diff(oo,x)*tau**b+(b*Y+V2(X,Y))*s.diff(oo,y)*tau**b)
checks['exact_physical_vorticity_scaling']=s.simplify(physO-expectedO)==0
physT=-s.diff(theta,tau)+u[0]*s.diff(theta,x)+u[1]*s.diff(theta,y)
expectedT=tau**(b-3)*(-(b-2)*tt+(b*X+V1(X,Y))*s.diff(tt,x)*tau**b+(b*Y+V2(X,Y))*s.diff(tt,y)*tau**b)
checks['exact_physical_temperature_scaling']=s.simplify(physT-expectedT)==0
checks['exact_physical_buoyancy_scaling']=s.simplify(s.diff(theta,x)-tau**-2*s.diff(tt,x)*tau**b)==0
# The chain of hypotheses is reviewed in prose; hashes only bind its sources.
manifest=json.loads((v/'dependencies/manifest.json').read_text())
for key,row in manifest['dependencies'].items():
 p=v/'dependencies'/(key+'.md');checks['frozen_'+key]=hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
checks['appendix_precedes_checks']=json.loads((v/'dependency_appendix_before_checks.json').read_text())['utc']<start
proof=(v.parent/'PROOF.md').read_bytes();checks['appendix_source_unchanged']=hashlib.sha256(proof).hexdigest()==json.loads((v/'dependency_appendix_before_checks.json').read_text())['proof_sha256']
end=datetime.now(timezone.utc).isoformat();data={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'checks':checks,'all_passed':all(checks.values()),'proof_sha256':hashlib.sha256(proof).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact rescaling and immutable dependencies. Analytic class reduction and local regularity are justified by their complete proofs, not these finite controls.'}
(v/'dependency_checks.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
