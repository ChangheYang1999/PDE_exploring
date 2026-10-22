"""Exact mixed-source tail witnesses for one native fixed-source archive."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys,time
import numpy as np
from r2_state_values import R2State
from exact_tail_residuals import COS,SIN,COS2,add,mul,scale,deriv,inv,chebs,linear,endpoints,ser,exactpoint,witness
start=time.monotonic();root=Path(sys.argv[1]);manifest=json.loads((root/'manifest.json').read_text());out={'utc':datetime.now(timezone.utc).isoformat(),'states':[]}
for item in manifest['states']:
 state=R2State(root/item['snapshot']);assert state.native_source and state.bb==state.beta and float(state.meta['eps'])==1
 beta=Q.from_float(state.beta);s=1/beta;m=1-2*s;L=Q.from_float(state.L);lam=Q.from_float(float(state.meta['lam']));sf=state.seed_field
 assert 3<beta<4 and sf.bb==3 and lam!=0
 fv,fd=endpoints(state,state.rawF);gv,gd=endpoints(state,state.rawG);sv,sd=endpoints(sf,sf.rawG)
 H0=mul(COS2,linear(fv,chebs(state.K)));H1=mul(COS2,linear(fd,chebs(state.K)));A0=mul(COS,linear(gv,chebs(state.K)));A1=mul(COS,linear(gd,chebs(state.K)));AS0=mul(COS,linear(sv,chebs(sf.K)))
 P=inv(A0,2-s);PS=inv(AS0,Q(5,3))
 cross=lambda p,k,h,m:add(scale(mul(p,deriv(h)),k),scale(mul(deriv(p),h),-m))
 ET=add(H1,scale(cross(P,2-s,H0,m),L));DT=cross(PS,Q(5,3),H0,m)
 EO=add(A1,scale(cross(P,2-s,A0,-s),L),scale(mul(COS,H0),-m),mul(SIN,deriv(H0)));DO=cross(PS,Q(5,3),A0,-s)
 assert H0 and DT
 axes=[]
 for sy in [Q(-1),Q(1)]:
  val=exactpoint(PS,Q(0),sy);dval=exactpoint(deriv(PS),Q(0),sy);assert val==0 and dval!=0
  axes.append({'sin_theta':str(sy),'PS_value':str(val),'PS_derivative':str(dval),'PS_derivative_float':float(dval)})
 row={'archive_sha256':state.sha256,'beta_exact':str(beta),'L_exact':str(L),'lambda_exact':str(lam),'seed_L_exact':str(Q.from_float(sf.L)),'seed_basis':3,'seed_geometry':{'K':sf.K,'Nt':sf.Nt,'degree':sf.degree,'grade':sf.grade},'source_coefficients_sha256':hashlib.sha256(sf.rawG.tobytes()).hexdigest(),'coefficient_scales':{'ET':'L^(1+3/beta)','DT':'seed_L^(4/3)*L^(1+2/beta), multiplied by lambda','EO':'L^(1+2/beta)','DO':'seed_L^(4/3)*L^(1+1/beta), multiplied by lambda'},'coefficients':{key:ser(val) for key,val in [('H0',H0),('A0',A0),('PS0',PS),('ET',ET),('DT',DT),('EO',EO),('DO',DO)]},'exact_witnesses':{key:witness(val) for key,val in [('H0',H0),('ET',ET),('DT',DT),('EO',EO),('DO',DO)]},'source_axes':axes,'temperature_powers':{'self':str(m-s),'source':str(m-Q(1,3))},'temperature_powers_float':{'self':float(m-s),'source':float(m-Q(1,3))},'forced_verdict':'INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL','self_verdict':'INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL' if ET else 'NO_CONCLUSION','scope':'exact property of this finite represented field; not an exclusion of nearby profiles or zero-forcing endpoint'}
 out['states'].append(row)
 print(item['label'],row['temperature_powers_float'],row['forced_verdict'],row['self_verdict'],flush=True)
out.update(status='COMPLETE',elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(root/'exact_native_tail.json').write_text(json.dumps(out,indent=2)+'\n')
