"""Integer fixtures audit the copied finite-mesh pair-row implementation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from types import SimpleNamespace
import json,time,sys,math,os
os.environ['CUDA_VISIBLE_DEVICES']=''
R=Path(__file__).resolve().parents[3];D=R/'research/weak_optimizer_audit';sys.path.insert(0,str(D/'source/lib'))
import numpy as np
import torch
import ipm_opt3 as target
import ipm_opt2 as prior
torch.set_num_threads(1)
DER=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def splits(d):
 i,j=d
 return [(math.comb(i,a)*math.comb(j,b),(a,b),(i-a,j-b)) for a in range(i+1) for b in range(j+1)]
NL=[(-1,(0,1),(1,0)),(1,(1,0),(0,1))]
def H(p):return sha256(Path(p).read_bytes()).hexdigest()

def fixture(seed):
 rng=np.random.default_rng(seed);n=4;nr=5;nt=7
 keys={('T',d) for d in DER}
 for d in DER:
  for sign,dp,dr in NL:
   for cf,d1,d2 in splits(d):
    keys.add(('psi',(dp[0]+d1[0],dp[1]+d1[1])));keys.add(('rho',(dr[0]+d2[0],dr[1]+d2[1])))
 keys=sorted(keys);p=object.__new__(target.Problem3);p.n=n;p.mesh=SimpleNamespace(Nr=nr,Nt=nt,device=torch.device('cpu'));p.keys=keys
 angle=rng.integers(-1,2,size=(3,nt),dtype=np.int64);p.tabs=SimpleNamespace(tab={'q':[torch.tensor(v,dtype=torch.float64) for v in angle]});p.gslots=[{} for j in range(n)];p.tail={};mat={};offset={}
 for key in keys:
  mat[key]=np.zeros((nr,nt,n),dtype=np.int64)
  for j in range(n):
   p.gslots[j][key]=[]
   for slot in range(2):
    rad=rng.integers(-1,2,size=nr,dtype=np.int64);k=int(rng.integers(3));p.gslots[j][key].append(('q',k,torch.tensor(rad,dtype=torch.float64)));mat[key][:,:,j]+=rad[:,None]*angle[k][None,:]
  rad=rng.integers(-1,2,size=nr,dtype=np.int64);k=int(rng.integers(3));p.tail[key]={('q',k):torch.tensor(rad,dtype=torch.float64)};offset[key]=rad[:,None]*angle[k][None,:]
 a=np.array([-2,-1,1,2],dtype=np.int64);weights={d:np.full((nr,nt),4**(j%3),dtype=np.int64) for j,d in enumerate(DER)};p.wts={d:torch.tensor(w,dtype=torch.float64) for d,w in weights.items()}
 kp=[(('rho',(2,0)),np.full((nr,nt),4,dtype=np.int64)),(('rho',(1,1)),np.full((nr,nt),16,dtype=np.int64))];p.kap_rows=[(key,torch.tensor(w,dtype=torch.float64)) for key,w in kp]
 pairs=[(rng.integers(-1,2,size=(nr,nt),dtype=np.int64),w) for w in (1,4,9)];p.pair=[(torch.tensor(ph,dtype=torch.float64),w) for ph,w in pairs]
 def fields(av):return {key:offset[key]+np.einsum('rtj,j->rt',mat[key],av) for key in keys}
 def residual(av):
  field=fields(av);out={}
  for d in DER:
   v=field['T',d].copy()
   for sign,dp,dr in NL:
    for cf,d1,d2 in splits(d):v+=sign*cf*field['psi',(dp[0]+d1[0],dp[1]+d1[1])]*field['rho',(dr[0]+d2[0],dr[1]+d2[1])]
   out[d]=v
  return out
 F=residual(a);fd=fields(a);J={d:np.empty((nr,nt,n),dtype=np.int64) for d in DER}
 for j in range(n):
  unit=np.eye(n,dtype=np.int64)[j];plus=residual(a+unit);minus=residual(a-unit)
  for d in DER:
   diff=plus[d]-minus[d];assert np.all(diff%2==0);J[d][:,:,j]=diff//2
 baseG=np.zeros((n,n),dtype=np.int64);baseg=np.zeros(n,dtype=np.int64);basephi=0
 for d in DER:
  baseG+=np.einsum('rt,rtj,rtk->jk',weights[d],J[d],J[d]);baseg+=np.einsum('rt,rtj,rt->j',weights[d],J[d],F[d]);basephi+=int(np.sum(weights[d]*F[d]**2))
 for key,w in kp:
  baseG+=np.einsum('rt,rtj,rtk->jk',w,mat[key],mat[key]);baseg+=np.einsum('rt,rtj,rt->j',w,mat[key],fd[key]);basephi+=int(np.sum(w*fd[key]**2))
 pairG=np.zeros((n,n),dtype=np.int64);pairg=np.zeros(n,dtype=np.int64);pairphi=0
 for ph,w in pairs:
  I=int(np.sum(ph*F[0,0]));dI=np.einsum('rt,rtj->j',ph,J[0,0]);pairG+=w*np.outer(dI,dI);pairg+=w*I*dI;pairphi+=w*I*I
 assert max(int(np.max(np.abs(baseG))),int(np.max(np.abs(pairG))),basephi,pairphi)<2**45
 rows=[];saved=p.pair
 for usepair in (False,True):
  p.pair=saved if usepair else [];EG=baseG+(pairG if usepair else 0);Eg=baseg+(pairg if usepair else 0);Ephi=basephi+(pairphi if usepair else 0)
  for block,chunk in [(1,1),(2,3),(5,7)]:
   G,g,phi=p.normal_equations(a,block=block,rchunk=chunk);checks={'G_exact_integer_equality':np.array_equal(G.numpy(),EG),'g_exact_integer_equality':np.array_equal(g.numpy(),Eg),'Phi_exact_integer_equality':phi==Ephi};assert all(checks.values()),(seed,usepair,block,chunk,checks)
   rows.append({'seed':seed,'pair_rows':len(p.pair),'block':block,'radial_chunk':chunk,'checks':checks})
 return rows

def main():
 start=time.monotonic();manifest=json.loads((D/'source/MANIFEST.json').read_text());assert all(H(R/row['local'])==row['sha256'] for row in manifest['files'])
 rows=fixture(11)+fixture(29)
 out={'utc':datetime.now(timezone.utc).isoformat(),'target':'copied N1 Problem3.normal_equations on exact small affine-field fixtures','cases':rows,'scalar_comparisons':len(rows)*3,'integer_magnitude_bound':2**45,'precision':'binary64, integer fixture operations below2^53','source_manifest_sha256':H(D/'source/MANIFEST.json'),'code_sha256':H(Path(__file__)),'proof_sha256':H(D/'PROOF.md'),'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED finite algebra and chunk assembly only; continuum quadrature and candidate conditioning separate'}
 with (D/'verification/integer_fixtures.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
