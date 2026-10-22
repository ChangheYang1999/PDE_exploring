"""Bounded single-thread regeneration, preserving exact operands and outputs.

This is a contemporary replay, not authentication of absent historic arrays.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,resource,time,json,hashlib,ast,math
assert not sys.flags.optimize
resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/localized_forcing/source/src'
sys.path.insert(0,str(S))
import numpy as np
from cert_resid import Certifier,mag
from midrad import MR,U,succ
from flint import arb,ctx
ctx.prec=128

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
t=time.monotonic();started=now()
manifest=json.loads((B/'research/localized_forcing/evidence/snapshot_manifest.json').read_text())
pins={}
for name in ['src/cert_forcing.py','src/cert_resid.py','src/midrad.py']:
 x=manifest['sources'][name];p=B/x['snapshot'];assert sha(p)==x['sha256'];pins[str(p.relative_to(B))]=x['sha256']
G=Path('numerics/data/cert_green.npz')
T=G.with_name('trial_v2_h0.008.npz')
for p,h in [(G,'c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1'),(T,'a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874')]:assert sha(p)==h;pins[str(p)]=h
C=Certifier(G,T,12);assert C.M==260 and C.Nmax==522 and C.Nf==261
source=ast.parse((S/'cert_forcing.py').read_text());cl=next(n for n in source.body if isinstance(n,ast.ClassDef) and n.name=='Cell')
ns={'np':np,'succ':succ,'U':U};exec(compile(ast.Module(body=[cl],type_ignores=[]),'frozen_Cell','exec'),ns);Cell=ns['Cell']
geo=json.loads((B/'research/localized_forcing/evidence/geometry_arb.json').read_text());w=geo['w_up']
Nmax=C.Nmax;Qp=8;NDER=4;twoN1=2.0*np.arange(Nmax+1)+1.0
fpow=[MR.exact(np.ones(Nmax+1))]
for m in range(1,NDER+Qp+2):fpow.append(fpow[-1]*MR.exact(twoN1))
wq=succ(w**(Qp+1)*(1+2*(Qp+1)*U)/math.factorial(Qp+1))
remfac=[succ(mag(fpow[j+Qp+1])*wq*(1+2*U)) for j in range(NDER+1)]
fac=np.stack(remfac);pairs=[(i,j) for i in range(5) for j in range(5-i)]
fp=D/'evidence/factors.npz';np.savez(fp,w=np.array(w),wq=np.array(wq),nu=twoN1,remfac=fac,fpow_mid=np.stack([p.m for p in fpow]),fpow_rad=np.stack([p.r for p in fpow]));pins[str(fp.relative_to(B))]=sha(fp)
np.seterr(over='raise',invalid='raise',divide='raise');items=[]
print(started,'loaded',round(time.monotonic()-t,3),'seconds',flush=True)
for ci in range(4096,4109):
 h_up=float((C.tb[ci+1]-C.tb[ci]).mag());assert h_up==geo['cells'][ci-4096]['h_up'] and succ(2*C.Nf*h_up)<=1
 C.cell_core_deriv(h_up,C.e_ta[ci],[(0.0,C.T[ci])],C.A[ci],C.B[ci],C.m_ta[ci],C.wfar_ta[ci],NDER)
 eps=C._last_eps;cell=Cell(h_up,w,C.Q,Qp);epsSup=[e.sup(cell.hpow) for e in eps]
 cm=np.stack([e.c.m for e in eps]);cr=np.stack([e.c.r for e in eps]);er=np.stack([e.r for e in eps]);es=np.stack(epsSup)
 assert cm.shape==cr.shape==(5,523,13) and er.shape==es.shape==(5,523)
 sh=[];r2=[]
 for i,j in pairs:
  shat=(epsSup[i]*remfac[j]).sum();rr=succ(shat*succ(1+(Nmax+2)*U));sh.append(shat);r2.append(rr)
 for x in [cm,cr,er,es,fac,np.asarray(sh),np.asarray(r2)]:assert np.isfinite(x).all()
 for x in [cr,er,es,fac,np.asarray(sh),np.asarray(r2)]:assert (x>=0).all()
 p=D/'evidence'/f'cell_{ci}.npz';np.savez(p,ci=np.array(ci),h=np.array(h_up),hpow=cell.hpow,coef_mid=cm,coef_rad=cr,rem=er,epsSup=es,pairs=np.array(pairs,dtype=np.int64),sum_native=np.array(sh),r2_native=np.array(r2))
 hsh=sha(p);pins[str(p.relative_to(B))]=hsh
 item={'ci':ci,'file':str(p.relative_to(B)),'sha256':hsh,'seconds':time.monotonic()-t,'native_sum_min':min(sh),'native_sum_max':max(sh),'h_up':h_up}
 items.append(item);print(now(),'cell',ci,'sum_min',min(sh),'elapsed',round(time.monotonic()-t,3),flush=True)
for f,h in pins.items():assert sha(B/f)==h,f
out={'start_utc':started,'end_utc':now(),'seconds':time.monotonic()-t,'status':'REGENERATED_INPUTS_REQUIRING_TWO_ENGINE_AUDIT','cell_count':13,'radial_models':65,'per_mode_sups':33995,'reductions':195,'n':523,'Qp':8,'Qs':12,'numpy_version':np.__version__,'python_version':sys.version,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source':str(S.relative_to(B)),'cells':items,'pins':pins,'scope':'Contemporary frozen-source replay. Historical arrays absent; no inherited radial model accepted.'}
(D/'evidence/regeneration.json').write_text(json.dumps(out,indent=2)+'\n');print(out['end_utc'],out['status'],out['seconds'],'seconds',flush=True)
