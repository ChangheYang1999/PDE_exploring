"""Stable inverse constant from packet93, independently implemented.
Only verifier state reader and public SciPy primitives; no numerics-lane imports.
"""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.interpolate import BSpline
from scipy.special import roots_jacobi
from numpy.polynomial.legendre import leggauss
from fractions import Fraction
import json,time,hashlib,sys
from r2_state_values import R2State

def weighted_integral(second,edges,b,order):
 nodes,weights=leggauss(order);gamma=2-b;total=0.
 for left,right in zip(edges[:-2],edges[1:-1]):
  mid=(left+right)/2;half=(right-left)/2;t=mid+half*nodes
  total+=half*np.dot(weights,(1-t)**gamma*second(t))
 width=1-edges[-2];nodes,weights=roots_jacobi(order,0,gamma)
 t=1-width*(nodes+1)/2
 total+=width**(gamma+1)/2**(gamma+1)*np.dot(weights,second(t))
 return float(total)

def constant(value0,slope0,second,edges,b,L,order):
 integ=weighted_integral(second,edges,b,order)
 result=-b*L*L/(2*(b-1)*(b-2))*(slope0-(b-2)*value0+integ)
 return float(result),integ

def manufacture():
 out=[]
 edges=np.array([0.,.13,.47,.81,1.])
 for b in [2.125,2.5,2.875]:
  for j in range(7):
   second=(lambda t,j=j:j*(j-1)*(1-t)**(j-2)) if j>=2 else (lambda t:np.zeros_like(t))
   val,I=constant(1.,-j,second,edges,b,1.5,32);want=-b*1.5**2/(2*(j+1-b))
   err=abs(val-want);assert err<1e-10*(1+abs(want))
   out.append({'b':b,'j':j,'calculated':val,'exact_formula':want,'absolute_error':err})
 return out

def main():
 start=time.monotonic();root=Path(sys.argv[1]);manifest=json.loads((root/'manifest.json').read_text())
 out={'started_utc':datetime.now(timezone.utc).isoformat(),'manufacture':manufacture(),'states':[],'scope':'Source inverse constants only, not B2 residual or interval certificates.'}
 for item in manifest['states']:
  p=Path(item['snapshot']);state=R2State(p);b=state.bb;L=state.L
  if not 2<b<3:raise ValueError('constant formula requires2<b<3')
  raw=state.Gs.c.copy();eps=float(state.meta.get('eps',1.));source=eps*raw
  if eps!=1:source+=(1-eps)*state.Es.c
  if state.Ds is not None:source+=state.Ds.c
  row={'label':item['label'],'source_archive':str(p.resolve()),'sha256':state.sha256,'beta':state.beta,'basis_beta':b,'L':L,'sources':{}}
  exact={'basis_beta':str(Fraction.from_float(b)),'L':str(Fraction.from_float(L)),'knots':[str(Fraction.from_float(float(v))) for v in state.knots],'degree':state.degree,'source_rule':'self: stored masked cG; transport: eps*cG+(1-eps)*cG_ext+cG_f_effective; numerical combination is floating-point','eps':str(Fraction.from_float(eps)),'scalar_coefficients':{}}
  for kind,data in [('self',raw),('transport',source)]:
   Sdata=data[:,0]-.5*data[:,2] if state.K>2 else data[:,0]
   spl=BSpline(state.knots,Sdata,state.degree,extrapolate=False);second=spl.derivative(2)
   v0=float(spl(0));d0=float(spl.derivative()(0));ve=float(spl(1));de=float(spl.derivative()(1))
   checks=[]
   for order in [8,16,32,64]:
    C,I=constant(v0,d0,second,state.edges,b,L,order)
    checks.append({'order':order,'C2':C,'weighted_second_derivative_integral':I})
   row['sources'][kind]={'S0':v0,'Sprime0':d0,'Send':ve,'Sprime_end':de,'B0_first_cosine':L**(1+1/b)*ve,'B1_first_cosine':-L**(1+2/b)*de,'evaluations':checks,'order32_64_change':abs(checks[-1]['C2']-checks[-2]['C2'])}
   exact['scalar_coefficients'][kind]=[str(Fraction.from_float(float(v))) for v in Sdata]
   print(item['label'],kind,'C2',checks[-1]['C2'],'change',row['sources'][kind]['order32_64_change'],flush=True)
  out['states'].append(row);(root/(item['label']+'_exact_inputs.json')).write_text(json.dumps(exact,indent=2)+'\n')
 out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
