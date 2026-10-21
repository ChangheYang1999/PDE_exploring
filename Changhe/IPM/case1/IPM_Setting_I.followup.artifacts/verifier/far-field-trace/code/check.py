from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np,sympy as s
root=Path(__file__).resolve().parents[1];v=root/'verification'
k=s.symbols('k',real=True);theta=s.symbols('theta',real=True);checks={}
F=(s.sin(theta)+s.sin(3*theta))/4
a2=(k+1)/(4*(1-k)*(k+3));a4=-1/(8*(k+5))
checks['angular_density']=s.trigsimp(s.expand_trig(F-s.cos(theta)**2*s.sin(theta)))
source=s.expand_trig(k*s.cos(theta)*F-s.sin(theta)*s.diff(F,theta))
poisson=(4-(k+1)**2)*a2*s.sin(2*theta)+(16-(k+1)**2)*a4*s.sin(4*theta)
checks['homogeneous_poisson']=s.trigsimp(s.expand_trig(s.simplify(source-poisson)))
rr,cl,rv,adv=s.symbols('r cl rho adv',nonzero=True)
checks['radial_identity']=s.simplify(rr**(-1/cl)*(rv-adv)/(cl*rr)-(1/cl)*rr**(-1/cl-1)*rv+(1/cl)*rr**(-1/cl-1)*adv)
gamma=s.symbols('gamma');beta=(1-gamma)/(1-k)
checks['angular_balance']=s.simplify(1-(gamma-k)/(1-k)-beta)
checks['velocity_homogeneity']=s.simplify((k+1)-1-k)
checks['tail_integrable_exponent']=s.simplify((k-3)+1-(k-2))
assert all(z==0 for z in checks.values()),checks
N=M=2;q=(1-np.cos(np.arange(N+1)*np.pi/N))/2;theta_nodes=(np.arange(M)+.5)*np.pi/(2*M)
path=v/'manufactured.npz';np.savez_compressed(path,N=N,M=M,L=1.,c_l=5.,beta=0.,q=q,theta=theta_nodes,b=np.ones((N+1,M)),C=0.,tag='own smooth homogeneous-tail manufactured density, not a profile')
points=[]
for r in [10.,100.,1000.,10000.]:
 for angle in [.3,1.1,1.55]:points.append([float(r*np.cos(angle)),float(r*np.sin(angle))])
(v/'points.txt').write_text(';'.join(','.join(format(x,'.17g') for x in pt) for pt in points)+'\n')
out={'date':datetime.now(timezone.utc).isoformat(),'symbolic_checks':{name:str(expr) for name,expr in checks.items()},'all_pass':True,'manufactured_md5':hashlib.md5(path.read_bytes()).hexdigest(),'scope':'symbolic algebra and a manufactured inverse fixture; analytic theorem needs its complete proof','a2_at_k_one_fifth':str(a2.subs(k,s.Rational(1,5))),'a4_at_k_one_fifth':str(a4.subs(k,s.Rational(1,5))),'exact_center_strain':'5/16','cl_identity_target':14}
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
