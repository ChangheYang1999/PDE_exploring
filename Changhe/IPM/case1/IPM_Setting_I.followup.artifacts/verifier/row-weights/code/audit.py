"""Independent row geometry and finite matrix arithmetic, no numerics imports."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
import torch
ROOT=Path(__file__).resolve().parents[1];SOURCE=ROOT.parent/'spectral-diagnostics/data';NUM=ROOT.parents[1]/'numerics'
out={'date':datetime.now(timezone.utc).isoformat(),'states':[],'scope':'Finite saved-action matrix arithmetic only. Squared norm fractions. No canonical linearized PDE, continuum regularity or kernel identification.'}
for tag,fn in [('n120m48_S','dnSB_n120m48.npz'),('n96m40S','dnB_n96m40S.npz'),('n96m40SL4','dnB_n96m40SL4.npz')]:
 p=NUM/'runs'/('reweight_'+tag+'.json');raw=p.read_bytes();(ROOT/'data'/p.name).write_bytes(raw);claims=json.loads(raw)
 pt=SOURCE/('ritz_'+tag+'.pt');obj=torch.load(pt,map_location='cpu',weights_only=False);D=obj['D'].detach().cpu().numpy();D=np.asarray(D,dtype=float)
 with np.load(SOURCE/fn) as z:N=int(z['N']);M=int(z['M']);L=float(z['L']);cl=float(z['c_l']);beta=float(z['beta'])
 q=(1-np.cos(np.pi*np.arange(1,N)/N))/2;r=np.r_[L*np.sqrt(np.expm1(-2*np.log1p(-q)/(1-1/cl))),np.inf];s=np.pi*(np.arange(M)+.5)/(2*M);theta=s+beta*np.sin(2*s)/2
 X=r[:,None]*np.cos(theta);Y=r[:,None]*np.sin(theta);dist=np.hypot(X-claims['xstar'],Y).ravel();assert D.shape[0]==N*M+2
 u,sv,vt=np.linalg.svd(D,full_matrices=False);action=D@vt[-4:].T;den=np.sum(action*action,axis=0);sv0=sv[::-1];assert max(abs(sv0[:12]-claims['base_ritz']))<1e-12
 entry={'tag':tag,'claim_sha256':hashlib.sha256(raw).hexdigest(),'matrix_sha256':hashlib.sha256(pt.read_bytes()).hexdigest(),'tests':[]}
 for claim in claims['tests']:
  if 'R' in claim:
   mask=np.r_[dist<claim['R'],True,False];assert sum(mask)==claim['nrows'];frac=(np.sum(action[mask]**2,axis=0)/den)[::-1];assert max(abs(frac-claim['frac_near_P_softest4']))<1e-8
   lam=claim['lam'];DD=D.copy();DD[mask]*=lam;ss=np.linalg.svd(DD,compute_uv=False)[::-1];err=float(max(abs(ss[:12]-claim['ritz'])));assert err<1e-10
   assert np.all(ss>=sv0-1e-10) and np.all(ss<=lam*sv0+1e-8)
   entry['tests'].append({'R':claim['R'],'lambda':lam,'rows':int(sum(mask)),'squared_action_fractions':frac.tolist(),'complementary_norm_fractions':np.sqrt(1-frac).tolist(),'singular_value_max_discrepancy':err,'first_four_singular_values':ss[:4].tolist()})
  else:
   index=-2 if claim['row']=='h(P) row' else -1;frac=(action[index]**2/den)[::-1];assert max(abs(frac-claim['frac_softest4']))<1e-8
   for ls,quoted in claim['lifted'].items():
    DD=D.copy();DD[index]*=float(ls);ss=np.linalg.svd(DD,compute_uv=False)[::-1];assert max(abs(ss[:4]-quoted))<1e-10
 out['states'].append(entry)
for N in [8,16,32,64]:assert abs(np.linalg.svd(np.diag([N**-3,1.]),compute_uv=False)[-1]-N**-3)<1e-15
out['complete']=True;(ROOT/'verification/audit.json').write_text(json.dumps(out,indent=2)+'\n');print('ALL_ROW_ARITHMETIC_CHECKS_PASS')
for st in out['states']:
 print(st['tag'],[(a['R'],a['squared_action_fractions'],a['complementary_norm_fractions']) for a in st['tests'] if a['lambda']==1])
