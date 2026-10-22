"""Packet96: independent finite-difference evaluation of actual and divided residuals.
Proof preceded code. Only verifier's own FD stencil is imported. No numerical-lane code.
The tested r>=2 exterior belongs to the compactly center-corrected example in proof96.
"""
from pathlib import Path
from datetime import datetime, timezone
import time, json, hashlib
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from finite_difference import stencil

BETA=2.5
s=1/BETA
power=(1-s)/2

def bump(t):
 t=np.asarray(t);z=(t-1)*(2-t);out=np.zeros_like(t,dtype=float)
 good=z>0
 out[good]=np.exp(4-1/z[good])
 return out
I0=quad(lambda t:float(bump(t)),1,2,epsabs=1e-13,epsrel=1e-13)[0]
I2=quad(lambda t:t*t*float(bump(t)),1,2,epsabs=1e-13,epsrel=1e-13)[0]
qn,qw=leggauss(96)

def inverse_changes(x,y,R,D):
 r=np.hypot(x,y);z=r/R;J0=np.zeros_like(r);J2=np.zeros_like(r)
 J0[z>=2]=I0;J2[z>=2]=I2
 mask=(z>1)&(z<2)
 t=1+((z[mask]-1)/2)[:,None]*(qn+1)
 bv=bump(t)
 J0[mask]=(z[mask]-1)/2*(bv@qw)
 J2[mask]=(z[mask]-1)/2*((bv*t*t)@qw)
 factor=np.divide(D*J2,I0*z*z,out=np.zeros_like(r),where=z>0)
 dA=np.divide(-2*factor*y,r*r,out=np.zeros_like(r),where=r>0)
 dB=D*J0/I0+factor*np.divide(x*x-y*y,r*r,out=np.zeros_like(r),where=r>0)
 return dA,dB

def F(x,y):return (1+x*x+y*y)**(-.5-s)
def G(x,y):
 rr=x*x+y*y
 return 4*power*(1+rr)**(power-2)*(2+(power+1)*rr)
def deltaG(x,y,R,D):
 r=np.hypot(x,y)
 return np.divide(-2*D*bump(r/R),R*I0*r,out=np.zeros_like(r),where=r>0)

nodes,weights=stencil()
def grad(fun,p,step):
 h=step*np.maximum(1,np.linalg.norm(p,axis=1));ret=[]
 for axis in [0,1]:
  q=np.repeat(p[:,None,:],len(nodes),axis=1)
  q[:,:,axis]+=h[:,None]*nodes
  ret.append(fun(q[:,:,0],q[:,:,1])@weights/h)
 return np.column_stack(ret)

def ratios(terms):
 signed=np.sum(terms,axis=1);norm=np.sum(abs(terms),axis=1)
 quotient=np.divide(signed,norm,out=np.zeros_like(signed),where=norm>0)
 return quotient,norm,signed

def evaluate(p,R,D,step):
 x,y=p.T;rr=x*x+y*y
 f=F(x,y);g=G(x,y);dg=deltaG(x,y,R,D)
 gf=grad(F,p,step);gg=grad(G,p,step)
 ggnew=grad(lambda x,y:G(x,y)+deltaG(x,y,R,D),p,step)
 gt=grad(lambda x,y:x*x*F(x,y),p,step)
 go=grad(lambda x,y:x*G(x,y),p,step)
 gonew=grad(lambda x,y:x*(G(x,y)+deltaG(x,y,R,D)),p,step)
 A=BETA+2*power*y*(1+rr)**(power-1)
 B=BETA*y-np.expm1(power*np.log1p(rr))-2*power*x*x*(1+rr)**(power-1)
 da,db=inverse_changes(x,y,R,D)
 results=[]
 axis=(x==0)
 for anew,bnew,gnew,ggcur,gocur in [(A,B,g,gg,go),(A+da,B+db,g+dg,ggnew,gonew)]:
  cf=ratios(np.column_stack((x*anew*gt[:,0],bnew*gt[:,1],-(BETA-2)*x*x*f)))
  cg=ratios(np.column_stack((x*anew*gocur[:,0],bnew*gocur[:,1],x*gnew,-gt[:,0])))
  # Original Cartesian fields and parity derivatives vanish exactly on x=0.
  cf[0][axis]=0;cg[0][axis]=0
  df=ratios(np.column_stack((anew*(2*f+x*gf[:,0]),bnew*gf[:,1],-(BETA-2)*f)))
  dgg=ratios(np.column_stack((anew*(gnew+x*ggcur[:,0]),bnew*ggcur[:,1],gnew,-(2*f+x*gf[:,0]))))
  ef=ratios(np.column_stack((2*anew*f,x*anew*gf[:,0],bnew*gf[:,1],-(BETA-2)*f)))
  eg=ratios(np.column_stack((anew*gnew,x*anew*ggcur[:,0],bnew*ggcur[:,1],gnew,-2*f,-x*gf[:,0])))
  results.append(dict(cartesian_F=cf,cartesian_G=cg,divided_F=df,divided_G=dgg,expanded_F=ef,expanded_G=eg))
 metrics={}
 for key in results[0]:
  old=results[0][key][0];new=results[1][key][0]
  metrics[key]={'absolute_ratio_difference':float(np.max(abs(abs(new)-abs(old)))),
   'signed_ratio_difference':float(np.max(abs(new-old))),
   'axis_absolute_difference':float(np.max(abs(abs(new[axis])-abs(old[axis])))),
   'background_max':float(np.max(abs(old))),'perturbed_max':float(np.max(abs(new)))}
 off=~axis
 identities=[]
 for res in results:
  identities.append({key:float(np.max(abs(res['cartesian_'+key][0][off]-(np.sign(x[off]) if key=='G' else 1)*res['divided_'+key][0][off]))) for key in ['F','G']})
 return metrics,identities,float(np.min((g+dg)/g)),results

start=time.monotonic()
root=Path('research/96_normalized_residual_topology/verification');root.mkdir(exist_ok=True)
angles=2*np.pi*(np.arange(72)+.317)/72
vectors=[(np.cos(a),np.sin(a)) for a in angles]
for small in [1e-3,1e-6,1e-8,0.]:
 for sy in [-1.,1.]:
  for sx in [-1.,1.]:
   vectors.append((sx*small,sy*np.sqrt(1-small*small)))
vectors=np.unique(np.array(vectors),axis=0)
radial=np.r_[.7,np.linspace(1.01,1.99,39),np.geomspace(2,1e3,60)]
out={'started_utc':datetime.now(timezone.utc).isoformat(),'beta':BETA,
 'scope':'Supplementary sampled checks of proved changes of residual functions, not an exact profile or interval certificate.',
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'zero_policy':'Exact Cartesian axis ratios set to zero from exact parity. Divided ratios evaluated on the axis. All other ratios have their actual denominators, no floor.',
 'core_policy':'Compact center correction is analytically identically zero on every tested point and stencil. Its center relations are proved in PROOF.md, not inferred from these exterior samples.',
 'angles':len(vectors),'radius_factors':radial.tolist(),'bump_I0':I0,'bump_I2':I2,'rows':[]}
for D in [.35,-.35]:
 for R in [4.,16.,64.,256.,1024.,4096.,16384.,65536.,262144.]:
  p=(R*radial[:,None,None]*vectors[None,:,:]).reshape(-1,2)
  assert np.min(np.linalg.norm(p,axis=1))>2.1
  core=np.array([[0.,0.],[.1*R,.6*R],[-.3*R,-.4*R]])
  ca,cb=inverse_changes(core[:,0],core[:,1],R,D)
  assert np.max(abs(ca))+np.max(abs(cb))+np.max(abs(deltaG(core[:,0],core[:,1],R,D)))==0
  rows=[];values=[]
  for step in [2e-5,1e-5]:
   metrics,identities,minratio,raw=evaluate(p,R,D,step)
   rows.append({'step':step,'metrics':metrics,'cartesian_divided_signed_ratio_difference':identities})
   values.append(raw)
  step_errors={key:max(float(np.max(abs(values[0][j][key][0]-values[1][j][key][0]))) for j in [0,1]) for key in values[0][0]}
  record={'R':R,'D':D,'points':len(p),'min_Gnew_over_G':minratio,'FD':rows,'step_change':step_errors,'exact_core_change':0.,'constant_C2_background':1.,'constant_C2_new':1+D}
  out['rows'].append(record)
  print('R',R,'D',D,'min_G_ratio',minratio,'dF',metrics['divided_F']['absolute_ratio_difference'],'dG',metrics['divided_G']['absolute_ratio_difference'],'step',max(step_errors.values()),flush=True)
  assert minratio>0
  assert max(step_errors.values())<1e-7
  assert max(v for pair in identities for v in pair.values())<1e-7
# Supplementary asymptotic check. The theorem does NOT require monotonicity at small R.
for D in [.35,-.35]:
 rows=[q for q in out['rows'] if q['D']==D]
 for key in ['cartesian_F','cartesian_G','divided_F','divided_G','expanded_F','expanded_G']:
  vals=[q['FD'][-1]['metrics'][key]['absolute_ratio_difference'] for q in rows]
  assert all(vals[j+1]<vals[j] for j in range(len(vals)-4,len(vals)-1)),(D,key,vals)
  assert vals[-1]<.01,(D,key,vals[-1])
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'normalized_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
