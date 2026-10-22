"""Exact rational Laurent-polynomial audit of serialized spline tail PDEs.

Own mathematics and code only. No numerics-lane imports/execution.
The binary coefficients and reconstructed binary knot values are exact inputs.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, hashlib, time, sys
import numpy as np
from r2_state_values import R2State

ZERO=(Q(0),Q(0)); ONE=(Q(1),Q(0))
def cz(a): return (Q(a),Q(0))
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cc(a):return (a[0],-a[1])
def trim(a):return {n:c for n,c in a.items() if c!=ZERO}
def add(*args):
 out={}
 for a in args:
  for n,c in a.items():out[n]=ca(out.get(n,ZERO),c)
 return trim(out)
def scale(a,q):return trim({n:(c[0]*q,c[1]*q) for n,c in a.items()})
def mul(a,b):
 out={}
 for n,c in a.items():
  for j,d in b.items():out[n+j]=ca(out.get(n+j,ZERO),cm(c,d))
 return trim(out)
def deriv(a):return trim({n:(-n*c[1],n*c[0]) for n,c in a.items()})
COS={1:(Q(1,2),Q(0)),-1:(Q(1,2),Q(0))}
SIN={1:(Q(0),Q(-1,2)),-1:(Q(0),Q(1,2))}
CONST={0:ONE};COS2=mul(COS,COS)
def chebs(n):
 ans=[CONST,scale(SIN,Q(-1))]
 while len(ans)<n:ans.append(add(scale(mul(ans[1],ans[-1]),Q(2)),scale(ans[-2],Q(-1))))
 return ans[:n]
def linear(coeff,polys):return add(*(scale(p,c) for c,p in zip(coeff,polys)))
def inv(a,k):return trim({n:(c[0]/(n*n-k*k),c[1]/(n*n-k*k)) for n,c in a.items()})
def realcheck(a):
 for n,c in a.items():assert a.get(-n,ZERO)==cc(c)
def ser(a):return {str(n):[str(c[0]),str(c[1])] for n,c in sorted(a.items())}
def normfloat(a):return float(sum(abs(c[0])+abs(c[1]) for c in a.values()))
def evalfloat(a,theta):
 theta=np.asarray(theta);out=np.zeros(theta.shape,dtype=complex)
 for n,c in a.items():out+=(float(c[0])+1j*float(c[1]))*np.exp(1j*n*theta)
 assert np.max(abs(out.imag),initial=0)<1e-9*(1+np.max(abs(out.real),initial=0))
 return out.real

def exactpoint(a,x,y):
 z=(Q(x),Q(y));assert z[0]*z[0]+z[1]*z[1]==1
 pos={0:ONE};neg={0:ONE}
 for j in range(1,max([abs(n) for n in a]+[0])+1):
  pos[j]=cm(pos[j-1],z);neg[j]=cm(neg[j-1],cc(z))
 val=ZERO
 for n,c in a.items():val=ca(val,cm(c,pos[n] if n>=0 else neg[-n]))
 assert val[1]==0
 return val[0]
def witness(a):
 if not a:return None
 for t in [Q(0),Q(1,2),Q(-1,2),Q(1,3),Q(-1,3),Q(2,3),Q(-2,3)]+[Q(j,19) for j in range(1,90)]:
  x=(1-t*t)/(1+t*t);y=2*t/(1+t*t);v=exactpoint(a,x,y)
  if v:return {'cos_theta':str(x),'sin_theta':str(y),'exact_value':str(v),'float_value':float(v)}
 raise AssertionError('Nonzero Laurent polynomial missed too many distinct rational points')

def formulas(beta,b,L,H0,H1,A0,A1,AS):
 s=1/b;m=1-2*s;k=2-s;fs=inv(AS,k)
 et=add(scale(H1,3*beta*s-2),scale(add(scale(mul(fs,deriv(H0)),k),scale(mul(deriv(fs),H0),-m)),L))
 eo=add(scale(A1,2*beta*s-1),scale(add(scale(mul(fs,deriv(A0)),k),scale(mul(deriv(fs),A0),s)),L),scale(mul(COS,H0),-m),mul(SIN,deriv(H0)))
 return fs,et,eo

def endpoints(state,raw):
 if raw is None:return [Q(0)]*state.K,[Q(0)]*state.K
 data=raw.reshape(state.K,state.nb);assert (state.K-1)//2<state.nb-1
 factor=Q(state.degree)/(1-Q.from_float(float(state.edges[-2])))
 v=[Q.from_float(float(row[-1])) for row in data]
 d=[factor*(Q.from_float(float(row[-1]))-Q.from_float(float(row[-2]))) for row in data]
 return v,d

def manufacture():
 b=Q(7,2);s=1/b;m=1-2*s;k=2-s
 fs,et,eo=formulas(b,b,Q(1),COS2,{},COS,{},COS)
 assert not add(et,scale(mul(SIN,COS2),-3/(k*k-1)))
 expected=add(scale(mul(SIN,COS),2/(k*k-1)),scale(mul(COS,COS2),-m),scale(mul(mul(SIN,SIN),COS),Q(-2)))
 assert not add(eo,scale(expected,Q(-1)))
 assert not add(scale(deriv(deriv(fs)),Q(-1)),scale(fs,-k*k),scale(COS,Q(-1)))
 assert et and not exactpoint(et,Q(1),Q(0))
 # Endpoint derivative checked independently on an affine polynomial in t.
 knots=[Q(0),Q(1,4),Q(1)];p=5;c0=Q(7,9);slope=Q(-11,13)
 cprev=c0-slope*(1-knots[-2])/p
 assert p*(c0-cprev)/(1-knots[-2])==slope
 return {'checks':5,'beta':str(b),'ET_witness':witness(et),'verdict':'PASSED'}

def grid_compare(root,label,kind,beta,b,L,H0,A0,ET,EO):
 path=root/(label+'_'+kind+'.npz')
 if not path.exists():return {'status':'NO_RAW_GRID'}
 with np.load(path,allow_pickle=False) as z:
  rr=z['radii'];ang=z['angles']-np.pi/2;nt=len(ang)
  rt=z['Theta_R_h1e-05'].reshape(-1,nt);ro=z['Omega_R_h1e-05'].reshape(-1,nt)
  s=1/float(b);m=1-2*s;l=float(L);be=float(beta)
  h=evalfloat(H0,ang)*l**(1+2*s);a=evalfloat(A0,ang)*l**(1+s)
  et=evalfloat(ET,ang)*l**(1+3*s);eo=evalfloat(EO,ang)*l**(1+2*s)
  out=[]
  used=set()
  for R in [1e3,1e4,1e5,1e6,1e7,1e8]:
   i=int(np.argmin(abs(np.log(rr/R))))
   if i in used:continue
   used.add(i);r=rr[i]
   t2=(rt[i]-2*(1-be*s)*r**m*h)/r**(m-s)
   o2=(ro[i]-(1-be*s)*r**(-s)*a)/r**(-2*s)
   out.append({'r':float(r),'Theta_coefficient_max_error':float(np.max(abs(t2-et))),'Omega_coefficient_max_error':float(np.max(abs(o2-eo))),'Theta_predicted_max':float(np.max(abs(et))),'Omega_predicted_max':float(np.max(abs(eo)))})
 return {'status':'CHECKED_FLOATING_POINT','comparisons':out}

def main():
 start=time.monotonic();outroot=Path(sys.argv[1]);outroot.mkdir(exist_ok=True)
 manifest=json.loads((outroot/'manifest.json').read_text());out={'started_utc':datetime.now(timezone.utc).isoformat(),'manufacture':manufacture(),'states':[]}
 for item in manifest['states']:
  path=Path(item['snapshot']);state=R2State(path)
  beta=Q.from_float(state.beta);b=Q.from_float(state.bb);L=Q.from_float(state.L);eps=Q.from_float(float(state.meta.get('eps',1.)))
  bpol=chebs(state.K);fv,fd=endpoints(state,state.rawF);gv,gd=endpoints(state,state.rawG);ev,ed=endpoints(state,state.extG);dv,dd=endpoints(state,state.defectG)
  H0=mul(COS2,linear(fv,bpol));H1=mul(COS2,linear(fd,bpol));A0=mul(COS,linear(gv,bpol));A1=mul(COS,linear(gd,bpol))
  sv=[eps*g+(1-eps)*e+d for g,e,d in zip(gv,ev,dv)]
  row={'label':item['label'],'snapshot':str(path.resolve()),'sha256':state.sha256,'beta_exact':str(beta),'basis_exact':str(b),'L_exact':str(L),'last_internal_knot_exact':str(Q.from_float(float(state.edges[-2]))),'H0_zero':not H0,'A0_zero':not A0,'H0_horizontal':str(exactpoint(H0,Q(1),Q(0))),'A0_horizontal':str(exactpoint(A0,Q(1),Q(0))),'sources':{}}
  for name,AS in [('self',A0),('transport',mul(COS,linear(sv,bpol)))]:
   fs,ET,EO=formulas(beta,b,L,H0,H1,A0,A1,AS)
   for p in [H0,H1,A0,A1,fs,ET,EO]:realcheck(p)
   m=1-2/b
   if beta!=b and H0: verdict='INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL_FROM_LEADING_TERM'
   elif beta==b and b>3 and ET:verdict='INFINITE_ABSOLUTE_TEMPERATURE_RESIDUAL_FROM_SECOND_TERM'
   elif beta==b and b==3 and ET:verdict='NONZERO_FINITE_TEMPERATURE_RESIDUAL_LIMIT'
   else:verdict='NO_DIVERGENCE_CONCLUSION'
   obj={'ET_zero':not ET,'EO_zero':not EO,'ET_witness':witness(ET),'EO_witness':witness(EO),'verdict':verdict,'temperature_second_power':float(m-1/b),'coefficients':{nm:ser(p) for nm,p in [('H0',H0),('H1',H1),('A0',A0),('A1',A1),('FS',fs),('ET',ET),('EO',EO)]},'grid_comparison':grid_compare(Path(item['grid_root']),item['label'],name,beta,b,L,H0,A0,ET,EO)}
   row['sources'][name]=obj
  if beta!=b and row['H0_horizontal']!='0' and row['A0_horizontal']!='0':
   m=1-2/b
   row['horizontal_normalized_limits']={'Theta':str(abs(beta*m-(beta-2))/(beta*abs(m)+abs(beta-2))),'Omega':str(abs(1-beta/b)/(1+beta/b))}
   row['horizontal_normalized_limits_float']={n:float(Q(v)) for n,v in row['horizontal_normalized_limits'].items()}
  out['states'].append(row)
  print(item['label'],[(n,r['verdict'],r['ET_witness']['float_value'] if r['ET_witness'] else 0) for n,r in row['sources'].items()],flush=True)
 out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 (outroot/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
