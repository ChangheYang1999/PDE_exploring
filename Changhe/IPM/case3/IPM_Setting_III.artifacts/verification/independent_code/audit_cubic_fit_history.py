"""Result247: independent Chebyshev reconstruction and MP least-squares fit."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,sys,time
import numpy as np
import mpmath as mp
from candidate_reader import Candidate
ROOT=Path('research/cubic_fit_history_audit');V=ROOT/'verification';SN=V/'snapshots';SN.mkdir(exist_ok=True)
checks=[];states=[];start=time.monotonic();mp.mp.dps=65
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
stamp=lambda:datetime.now(timezone.utc).isoformat()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def ser(v):
 if isinstance(v,mp.mpf):return mp.nstr(v,55)
 if isinstance(v,dict):return {k:ser(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [ser(x)for x in v]
 return v
def dump(p,z):p.write_text(json.dumps(ser(z),indent=2)+'\n')
def M(v):return mp.mpf(float(v))
def coordinate(r,L,P):
 target=r/L;q=(2**P)*target
 for j in range(50):
  f=q/(2-q)**P-target;der=(2+(P-1)*q)/(2-q)**(P+1);new=q-f/der
  if not 0<new<2:raise ValueError('local coordinate left branch')
  if abs(new-q)<16*mp.eps*abs(q):q=new;break
  q=new
 else:raise ValueError('coordinate convergence failed')
 return -1+q,q/(2-q)**P-target

def poly(a,t):
 b1=mp.mpf(0);b2=mp.mpf(0)
 for v in reversed(a[1:]):b1,b2=v+2*t*b1-b2,b1
 return a[0]+t*b1-b2

def fit_coeff(r,val):
 scale=r[-1]**2;u=[x*x/scale for x in r]
 H=mp.matrix([[mp.fsum(x**(i+j)for x in u)for j in range(4)]for i in range(4)])
 rhs=mp.matrix([mp.fsum(x**i*y for x,y in zip(u,val))for i in range(4)])
 fit=mp.lu_solve(H,rhs)
 return fit[1]/scale,fit

def radii(e,window):
 lo=mp.mpf('-3.5')if window=='A'else mp.mpf(-3);hi=mp.mpf('-1.5')if window=='A'else mp.log10(mp.mpf('.03'))
 return [min(mp.mpf(1),e)*10**(lo+(hi-lo)*i/29)for i in range(30)]

def evaluate(c,window):
 L,P,gam,e=map(M,[c.meta['L'],c.meta['p'],c.meta['gamma'],c.meta['Lf']]);co=[[M(v)for v in c.coefficients[:,k]]for k in range(3)]
 rr=radii(e,window);vals=[[],[]];err=[]
 for r in rr:
  t,res=coordinate(r,L,P);err.append(abs(res)/(r/L));B=[poly(a,t)for a in co];W=(1+(r/L)**2)**((gam-1)/2)
  vals[0].append(W*(B[0]-B[1]/2));vals[1].append(W*(B[1]-B[2])/2)
 f1,a1=fit_coeff(rr,vals[0]);f3,a3=fit_coeff(rr,vals[1])
 return dict(b_fit=f1+3*f3,sine1_r2=f1,sine3_r2=f3,rmin=rr[0],rmax=rr[-1],coordinate_relative_error=max(err))

def main():
 for z in json.loads((V/'RECORD_INPUTS.json').read_text())['files']:ck('record '+z['frozen'],sha(z['frozen'])==z['sha256'])
 # Separate polynomial manufactures use analytic injected coefficients.
 for e in [mp.mpf(1),mp.mpf('.001'),mp.mpf('1e-8')]:
  for win in ['A','B']:
   r=radii(e,win);b,ev=mp.mpf(7)/3,-mp.mpf(5)/7;s1=(b+3*ev)/4;s3=(b-ev)/4
   v1=[2+s1*x*x+3*x**4-7*x**6 for x in r];v3=[s3*x*x-2*x**4+5*x**6 for x in r]
   a1,_=fit_coeff(r,v1);a3,_=fit_coeff(r,v3);error=abs(a1+3*a3-b)
   ck('manufactured cubic '+str(e)+win,error<mp.mpf('1e-39'),mp.nstr(error,12))
 for P in [mp.mpf(1),mp.mpf(2),mp.mpf(3),mp.mpf('1.7')]:
  for ratio in [mp.mpf('1e-12'),mp.mpf('.001'),mp.mpf('.04')]:
   t,res=coordinate(ratio,mp.mpf(1),P);ck('coordinate manufacture '+str(P)+str(ratio),abs(res)/ratio<mp.mpf('1e-58')and -1<t<1)
 gate=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',count=len(checks),checks=checks.copy(),utc=stamp());dump(V/'MANUFACTURE_GATE.json',gate)
 if gate['status']!='PASS':raise RuntimeError('manufacture failed')
 tags=['eps_cl2','eps_cl3','eps_cl2_hi','eps_cl1.5','eps_cl1.5_far','eps_cl1.5_hi','eps_cl1.5_L01b'];provenance=[]
 for tag in tags:
  logged={}
  for line in (V/'records'/(tag+'.log')).read_text().splitlines():
   m=re.search(r'eps=\s*([0-9.]+):.*?a0=([+0-9.e-]+).*?K=([+0-9.e-]+).*?Lcan=([+0-9.e-]+).*?b_cub=([+0-9.e-]+) b_cub\*Lcan\^2=([+0-9.e-]+)',line)
   if m:logged[m[1]]=dict(zip(['a0','Kraw','Lraw','b_fit','b_fit_Lraw2'],m.groups()[1:]))
  files=sorted(Path('../numerics/runs').glob(tag+'_eps*.pt'),key=lambda p:-float(p.stem.split('_eps')[-1]));ck(tag+' states match logged rows',len(files)==len(logged),[len(files),len(logged)])
  for path in files:
   print(stamp(),path.stem,flush=True);c=Candidate(path);e=c.meta['Lf'];key=f'{e:.4f}';lg=logged[key]
   snapshot=SN/(path.stem+'.npz');c.save_snapshot(snapshot);provenance.append(dict(source=str(path),source_sha256=c.meta['sha256'],snapshot=str(snapshot),snapshot_sha256=sha(snapshot)))
   a0=M(c.values[0,0]);end=[mp.fsum(M(v)for v in c.coefficients[:,k])for k in range(c.meta['M'])];Kraw=mp.fsum((-1)**k*v for k,v in enumerate(end));L=M(c.meta['L']);gam=M(c.meta['gamma']);Kphys=Kraw*L**(1-gam);Lraw=(Kraw/a0)**(1/(1-gam));Lphys=(Kphys/a0)**(1/(1-gam))
   fitA=evaluate(c,'A');fitB=evaluate(c,'B');center=np.polynomial.chebyshev.chebval(-1,c.coefficients);leak=float(max(abs(center[1:])));ck(path.stem+' center angular consistency',leak<1e-9,leak)
   ck(path.stem+' coordinate A',fitA['coordinate_relative_error']<mp.mpf('1e-58'));ck(path.stem+' coordinate B',fitB['coordinate_relative_error']<mp.mpf('1e-58'))
   ck(path.stem+' physical L relation',abs(Lphys-L*Lraw)/(1+Lphys)<mp.mpf('1e-58'))
   ck(path.stem+' printed slope',abs(a0-mp.mpf(lg['a0']))<=mp.mpf('5.1e-9'))
   ck(path.stem+' printed raw K',abs(Kraw-mp.mpf(lg['Kraw']))<=mp.mpf('5.1e-7'))
   ck(path.stem+' printed raw L',abs(Lraw-mp.mpf(lg['Lraw']))/(1+abs(Lraw))<mp.mpf('5e-6'))
   errorA=(fitA['b_fit']-mp.mpf(lg['b_fit']))/abs(mp.mpf(lg['b_fit']));errorB=(fitB['b_fit']-mp.mpf(lg['b_fit']))/abs(mp.mpf(lg['b_fit']));errorL=(fitA['b_fit']*Lraw**2-mp.mpf(lg['b_fit_Lraw2']))/abs(mp.mpf(lg['b_fit_Lraw2']))
   # A priori reporting tolerance; do not silently increase if a state fails.
   ck(path.stem+' logged cubic A',abs(errorA)<mp.mpf('1e-5'),mp.nstr(errorA,14));ck(path.stem+' logged cubic raw-L square',abs(errorL)<mp.mpf('1e-5'),mp.nstr(errorL,14))
   physamp=M(c.meta['beta'])*L**(1-gam);ck(path.stem+' physical amplitude gauge',abs(physamp-4)<mp.mpf('4e-6'),mp.nstr(physamp,15))
   high=None
   if tag=='eps_cl1.5_far'and e<.003:
    mp.mp.dps=95;hh=evaluate(c,'A');high=abs(hh['b_fit']-fitA['b_fit'])/(1+abs(hh['b_fit']));ck(path.stem+' precision repeat',high<mp.mpf('1e-40'),mp.nstr(high,12));mp.mp.dps=65
   states.append(dict(tag=tag,state=path.stem,source_sha256=c.meta['sha256'],snapshot_sha256=sha(snapshot),metadata=c.meta,logged=lg,fitA=fitA,fitB=fitB,a0=a0,Kraw=Kraw,Kphys=Kphys,Lraw=Lraw,Lphys=Lphys,physical_mean_far_amplitude=physamp,center_angular_leak=leak,relative_log_error_A=errorA,relative_log_error_B=errorB,relative_log_error_A_Lraw2=errorL,precision_error=high))
   dump(V/'PIPELINE.json',dict(status='RUNNING',utc=stamp(),pid=os.getpid(),completed=len(states),last=path.stem))
 ck('64 original states',len(states)==64,len(states));dump(V/'STATE_INPUTS.json',dict(utc=stamp(),states=provenance))
 out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=stamp(),count=len(checks),checks=checks,states=states,seconds=time.monotonic()-start,source_sha256=sha(__file__),reader_sha256=sha('independent_code/candidate_reader.py'),proof_sha256=sha(ROOT/'PROOF.md'),state_inputs_sha256=sha(V/'STATE_INPUTS.json'),record_inputs_sha256=sha(V/'RECORD_INPUTS.json'))
 dump(V/'CHECKS.json',out);dump(V/'PIPELINE.json',dict(status='DONE',utc=stamp(),gate=out['status'],count=len(checks),states=len(states)));print(out['status'],len(checks),flush=True)
 for c in checks:
  if not c['passed']:print(c,flush=True)
 if out['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
