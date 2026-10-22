"""Packet95 stable log constant. Own source reader and quadrature only."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import factorial,log
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import BSpline
import json,sys,time,hashlib
from r2_state_values import R2State

def log_integral(third,endpoint_derivatives,edges,order):
 nodes,weights=leggauss(order);total=0.
 for left,right in zip(edges[:-2],edges[1:-1]):
  mid=(left+right)/2;half=(right-left)/2;t=mid+half*nodes
  total+=half*np.dot(weights,np.log1p(-t)*third(t))
 width=1-edges[-2]
 for k,d in enumerate(endpoint_derivatives):
  total+=(-1)**k*d/factorial(k)*width**(k+1)*(log(width)/(k+1)-1/(k+1)**2)
 return float(total)

def calculate(v0,d0,d2end,third,endpoint_derivatives,edges,L,order):
 I=log_integral(third,endpoint_derivatives,edges,order)
 alpha=L*L*d2end/2
 C=3*L*L/4*(v0-d0-I)+alpha*(log(L)/2-2)
 return float(C),float(alpha),I

def manufacture():
 out=[];edges=np.array([0.,.13,.47,.81,1.])
 for L in [1.,1.5,2.]:
  for j in range(7):
   third=(lambda t,j=j:-j*(j-1)*(j-2)*(1-t)**(j-3)) if j>=3 else (lambda t:np.zeros_like(t))
   ed=[((-1)**j*factorial(j) if j==k else 0.) for k in range(3,max(j+1,4))]
   C,a,I=calculate(1.,-j,2. if j==2 else 0.,third,ed,edges,L,32)
   want=3*L*L/4 if j==0 else 3*L*L/2 if j==1 else L*L*(.25+log(L)/2) if j==2 else -3*L*L/(2*(j-2))
   err=abs(C-want);assert err<2e-10*(1+abs(want))
   out.append({'L':L,'j':j,'C':C,'alpha':a,'expected_C':want,'absolute_error':err})
 return out

def main():
 start=time.monotonic();root=Path(sys.argv[1]);manifest=json.loads((root/'manifest.json').read_text())
 out={'started_utc':datetime.now(timezone.utc).isoformat(),'manufacture':manufacture(),'states':[],'scope':'Source inverse only. No interval or coupled PDE certificate.'}
 for item in manifest['states']:
  state=R2State(item['snapshot']);assert state.bb==3
  eps=float(state.meta.get('eps',1.));raw=state.Gs.c.copy();source=eps*raw
  if eps!=1:source+=(1-eps)*state.Es.c
  if state.Ds is not None:source+=state.Ds.c
  row={'label':item['label'],'archive':str(state.path.resolve()),'sha256':state.sha256,'beta':state.beta,'basis_beta':state.bb,'L':state.L,'sources':{}}
  exact={'knots':[str(Fraction.from_float(float(v))) for v in state.knots],'degree':state.degree,'L':str(Fraction.from_float(state.L)),'source_rule':'self=stored masked cG; transport=eps*cG+(1-eps)*cG_ext+cG_f_effective, combined in floating point','scalar_coefficients':{}}
  for kind,data in [('self',raw),('transport',source)]:
   sd=data[:,0]-.5*data[:,2] if state.K>2 else data[:,0]
   spl=BSpline(state.knots,sd,state.degree,extrapolate=False);d0=float(spl.derivative()(0));v0=float(spl(0));d2end=float(spl.derivative(2)(1));third=spl.derivative(3)
   ed=[float(spl.derivative(k)(1.)) for k in range(3,state.degree+1)]
   checks=[]
   for order in [8,16,32,64]:
    C,a,I=calculate(v0,d0,d2end,third,ed,state.edges,state.L,order)
    checks.append({'order':order,'C':C,'alpha':a,'log_third_derivative_integral':I})
   row['sources'][kind]={'S0':v0,'Sprime0':d0,'Send':float(spl(1)),'Sprime_end':float(spl.derivative()(1)),'Ssecond_end':d2end,'B0_first_cosine':state.L**(4/3)*float(spl(1)),'B1_first_cosine':-state.L**(5/3)*float(spl.derivative()(1)),'B3_first_cosine':-state.L**(7/3)*float(third(1))/6,'evaluations':checks,'order32_64_change':abs(checks[-1]['C']-checks[-2]['C'])}
   exact['scalar_coefficients'][kind]=[str(Fraction.from_float(float(v))) for v in sd]
   print(item['label'],kind,'alpha',a,'C',C,'change',row['sources'][kind]['order32_64_change'],flush=True)
  out['states'].append(row);(root/(item['label']+'_exact_inputs.json')).write_text(json.dumps(exact,indent=2)+'\n')
 out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
