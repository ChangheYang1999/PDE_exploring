"""Exact-sector lower bound for the full-plane weighted Hessian residual norm.
Reads only this lane's reconstruction of the read-only original. No sibling code.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import sys,json,time,argparse
from flint import arb,ctx
from check_tail import density_stream,advection,add_sine
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from farfield_matrix_certificate import A,add,differentiate,binomial
ctx.prec=384
sys.set_int_max_str_digits(0)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--state',type=int,default=131);ap.add_argument('--cut',type=int,default=6);ap.add_argument('--radius',type=int,default=300);args=ap.parse_args()
 started=time.monotonic();state=args.state;cut=args.cut;R0=args.radius
 d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
 c=Q(d['exact_parameters']['cl']);gamma=1/c;delta=1-gamma
 coeff=list(map(Q,d['canonical_coefficients']));params=[(3+gamma-j*delta)/2 for j in range(4)]
 assert all(abs(params[j]-k)<26 for j,m,k in d['canonical_order'])
 absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,d['canonical_order']) if jj==j),Q(0)) for j in range(4)]
 dens={};stream={};powers={};field={k:[] for k in range(3,7)}
 for j in range(4):
  for q in range(cut+1):
   C={}
   for v,(jj,m,k) in zip(coeff,d['canonical_order']):
    if jj==j:C[2*m]=C.get(2*m,Q(0))+v*binomial(params[j]-k,q)
   p=gamma-j*delta-2*q;powers[j,q]=p
   dens[j,q],stream[j,q]=density_stream(C,p+3)
   T={('c',n):v for n,v in C.items() if v}
   deriv={(0,0):T}
   for order in range(1,7):
    for nx in range(order+1):
     ny=order-nx
     if nx:prev=deriv[nx-1,ny];axis='x'
     else:prev=deriv[nx,ny-1];axis='y'
     deriv[nx,ny]=differentiate(prev,p+4-order,axis)
    if order>=3:
     bound=max(sum(map(abs,deriv[nx,order-nx].values()),Q(0)) for nx in range(order+1))
     field[order].append((j,q,bound))
 print('exact potential sectors and derivative bounds',len(dens),'seconds',time.monotonic()-started,flush=True)
 E={}
 for (j,q),f in dens.items():
  E[j,q]={n:(c*powers[j,q]-1)*v for n,v in f.items() if (c*powers[j,q]-1)*v}
 for (i,q1),P in stream.items():
  for (j,q2),F in dens.items():
   key=(i+j+1,q1+q2);out=E.setdefault(key,{})
   term=advection(P,F,powers[i,q1]+1,powers[j,q2])
   for n,v in term.items():add_sine(out,n,v)
 E={k:{n:v for n,v in f.items() if v} for k,f in E.items() if any(f.values())}
 assert (0,0) not in E
 prior=json.loads(Path(__file__).with_name(f'state{state:03d}_tail.json').read_text())
 assert E[1,0]=={int(n):Q(v) for n,v in prior['E_coefficients']['1'].items()}
 ep={k:gamma-k[0]*delta-2*k[1] for k in E}
 print('exact residual sectors',len(E),'seconds',time.monotonic()-started,flush=True)
 # Each field tail is bounded by Td*r^(gamma+3-order) for r>=R0.
 r=A(R0);q0=cut+1;M={};T={}
 for order in range(3,7):
  M[order]=sum((A(v)*r**A(-j*delta-2*q) for j,q,v in field[order]),arb(0))
  ratio=A(Q(q0+26,q0+1)*Q(2*q0+34,2*q0+32)**order)/r**2
  assert ratio<1
  T[order]=A(comb(q0+25,q0)*(2*q0+32)**order)*r**(-2*q0)/(1-ratio)*sum((A(absj[j])*r**A(-j*delta) for j in range(4)),arb(0))
 # Full tensor coefficient bounds, normalized by the appropriate r power.
 U={i:arb(2)**(arb(i+1)/2)*M[3+i] for i in range(3)}
 EU={i:arb(2)**(arb(i+1)/2)*T[3+i] for i in range(3)}
 D={k:arb(2)**(1+arb(k)/2)*M[3+k] for k in range(1,4)}
 ED={k:arb(2)**(1+arb(k)/2)*T[3+k] for k in range(1,4)}
 NL=arb(0)
 for i,bino in [(0,1),(1,2),(2,1)]:
  k=3-i
  NL+=bino*(EU[i]*D[k]+U[i]*ED[k]+EU[i]*ED[k])
 # Linear tail keeps its additional r^(-2q0), to remain integrable.
 LIN=(A(c)*ED[3]+abs(A(2*c-1))*ED[2])*r**(2*q0)
 rows=[]
 for sig in [Q(3,20),Q(1,5),Q(3,10),Q(7,20),Q(2,5)]:
  assert gamma-delta<sig
  s=A(sig);weight_radius=Q(1,2);b=1-s;pref=A(weight_radius)**(-b)
  items=list(E);expo=[A(ep[k]) for k in items]
  values=[{n:A(v) for n,v in E[k].items()} for k in items]
  radial=[r**(p-s) for p in expo]
  total=arb(0)
  for i,ki in enumerate(items):
   p=expo[i]
   for j in range(i+1):
    t=expo[j]
    common=values[i].keys() & values[j].keys()
    angular=arb(0)
    for n in common:
     inner=p*(p-1)*t*(t-1)+2*(p-1)*(t-1)*n*n+(p-n*n)*(t-n*n)
     angular+=values[i][n]*values[j][n]*inner
    total+=(1 if i==j else 2)*angular*radial[i]*radial[j]/(2*s-p-t)
  norm=(arb.pi()*total).sqrt()*pref
  lpower=gamma-2*q0
  elin=(2*arb.pi()).sqrt()*LIN*r**A(lpower-sig)/(2*A(sig-lpower)).sqrt()*pref
  p2=2*gamma-1
  enl=(2*arb.pi()).sqrt()*NL*r**A(p2-sig)/(2*A(sig-p2)).sqrt()*pref
  lower=norm-elin-enl
  rows.append({'sigma':str(sig),'weight_radius':'1/2','truncated_residual_exact_power_weight_norm':norm.str(60),'linear_tail_error_upper':elin.str(50),'nonlinear_tail_error_upper':enl.str(50),'full_actual_weight_norm_lower':lower.str(60)})
  print('sigma',sig,'truncated',norm.str(12),'error',(elin+enl).str(12),'lower',lower.str(15),'seconds',round(time.monotonic()-started,2),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'input_sha256':d['canonical_serialization_sha256'],'precision_bits':ctx.prec,'Q':cut,'R0':R0,'residual_sectors':len(E),'tensor_norm':'Frobenius D2 on full R2','weight':'(1+4r^2)^((1-sigma)/2)','method':'Exact finite angular sectors, exact radial monomial integration, independent binomial field tails and reverse triangle inequality.','potential_component_bounds':{str(k):v.str(50) for k,v in M.items()},'potential_tail_bounds':{str(k):v.str(50) for k,v in T.items()},'nonlinear_error_coefficient':NL.str(60),'linear_error_coefficient':LIN.str(60),'rows':rows,'elapsed_seconds':time.monotonic()-started}
 Path(__file__).with_name(f'state{state:03d}_residual_hessian_lower.json').write_text(json.dumps(out,indent=2)+'\n')
 # Save the exact sector algebra so a later audit need not trust a displayed norm.
 sector={'state':state,'input_sha256':d['canonical_serialization_sha256'],'Q':cut,'powers':{str(k):str(ep[k]) for k in E},'coefficients':{str(k):{str(n):str(v) for n,v in es.items()} for k,es in E.items()}}
 Path(__file__).with_name(f'state{state:03d}_residual_truncated_sectors.json').write_text(json.dumps(sector,indent=2)+'\n')
if __name__=='__main__':main()
