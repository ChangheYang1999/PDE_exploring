"""Own exact source, adaptive orbit and a second gradient state for sign witnesses."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,math
import numpy as np
from scipy.integrate import solve_ivp
from signed_gaussian_feedback import SignedGaussianFlow,cases,ROOT

def reduced(g,point,rin,rtol):
 X=np.array(point,dtype=float)
 def event(t,q):return np.linalg.norm(q)-rin
 event.terminal=True;event.direction=-1
 back=solve_ivp(lambda t,q:-g.field(q)[1],(0,220),X,method='DOP853',rtol=rtol,atol=max(1e-15,rin*rtol*.01),events=event,dense_output=True)
 if not back.success or not len(back.t_events[0]):return {'status':'UNFINISHED'}
 T=float(back.t[-1]);xe,ye=back.y[:,-1]
 def rhs(t,z):
  x,y=back.sol(T-t);_,W,_,D=g.field([x,y]);v=W[0]/x;P,Q,G=z
  return [(g.beta-2-D[0,0]-v)*P-x*D[1,0]*Q,(g.beta-2-D[1,1]-2*v)*Q-D[0,1]/x*P,-(1+v)*G+P]
 forward=solve_ivp(rhs,(0,T),[2*(1+g.f01*ye),g.f01,g.b0+g.g01*ye],method='DOP853',rtol=rtol,atol=rtol*.001)
 P,Q,G=forward.y[:,-1];x=X[0]
 return {'status':'COMPLETE' if forward.success else 'FORWARD_FAILED','Omega':float(x*G),'G':float(G),'gradient':[float(x*P),float(x*x*Q)],'T':T,'endpoint':[float(xe),float(ye)],'nfev':[back.nfev,forward.nfev]}

t0=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((ROOT.parent/'PROOF.md').read_bytes()).hexdigest(),'rows':[]}
for key,c in cases().items():
 r=c['data']
 if r['unfinished'] or r['G_min']>=0:continue
 radius,y=r['G_min_at'];x=math.sqrt(radius*radius-y*y);g=SignedGaussianFlow(r['c_in'],r['lobes']);row={'case':key,'point':[x,y],'reported_G':r['G_min'],'own':[]}
 for rin,rtol in [(1e-3,2e-10),(3e-4,2e-10),(1e-4,2e-10),(1e-5,2e-10),(1e-5,2e-11)]:
  a=g.evaluate([x,y],r_in=rin,rtol=rtol);b=reduced(g,[x,y],rin,rtol);row['own'].append({'rin':rin,'rtol':rtol,'standard':a,'standard_G':a['Omega']/x,'reduced':b,'relative_difference':abs(a['Omega']-b['Omega'])/(1+abs(a['Omega']))})
 out['rows'].append(row)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0)
out['all_paths_complete']=all(q['standard']['status']=='COMPLETE' and q['reduced']['status']=='COMPLETE' for r in out['rows'] for q in r['own'])
out['all_G_positive']=all(q['standard_G']>0 and q['reduced']['G']>0 for r in out['rows'] for q in r['own'])
out['max_state_relative_difference']=max(q['relative_difference'] for r in out['rows'] for q in r['own'])
out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
(ROOT/'negative_witness_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out['rows']: print(r['case'],r['reported_G'],[(q['rin'],q['rtol'],q['standard_G'],q['reduced']['G']) for q in r['own']],flush=True)
print(out['started_utc'],out['ended_utc'],out['elapsed_seconds'],out['max_state_relative_difference'],flush=True)
