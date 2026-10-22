"""Bounded contemporary geometry-only replay; no residual evaluations."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,resource,time,json,hashlib,ast,copy,math
assert not sys.flags.optimize
resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3))
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/forcing_composed_cutoff/source/src';sys.path.insert(0,str(S))
import numpy as np
from flint import arb,ctx
from midrad import MR,U,succ
from cert_resid import tm_exp
from cert_forcing import Cell,BiTM,BernSup,XSTAR,XRAD
from cert_forcing2 import Recentre,add_const
ctx.prec=128;started=datetime.now(timezone.utc).isoformat();tic=time.monotonic();np.seterr(over='raise',divide='raise',invalid='raise')
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
manifest=json.loads((B/'research/forcing_composed_cutoff/evidence/snapshot_manifest.json').read_text());pins={}
for name in ['cert_forcing.py','cert_forcing2.py','cert_resid.py','midrad.py']:
 p=S/name;h=manifest['files']['src/'+name]['source_sha256'];assert sha(p)==h;pins[str(p.relative_to(B))]=h
p=D/'PROOF.md';assert sha(p)==json.loads((D/'evidence/proof_first.json').read_text())['sha256']
G=Path('numerics/data/cert_green.npz');gh='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1';assert sha(G)==gh;pins[str(G)]=gh
with np.load(G,allow_pickle=False) as z:tb=z['tb'][4096:4110].copy();tr=z['tb_rad'][4096:4110].copy()
tbs=MR(tb,tr);geo=json.loads((B/'research/localized_forcing/evidence/geometry_arb.json').read_text());raw=json.loads((B/'research/forcing_composed_cutoff/source/runs/forcing/v21_p9_merged.json').read_text());Qs=12;Qp=8;Kser=16
w_up=geo['w_up'];theta_max=arb(raw['theta_max']);dth=theta_max/16
assert float(np.nextafter(float((dth/2).upper()),np.inf))==w_up
inv_fact=[MR(1.0/math.factorial(p),succ(U/math.factorial(p))) for p in range(9)];wq=succ(w_up**9*(1+18*U)/math.factorial(9));XS_MR=MR(XSTAR,XRAD);REC=Recentre(12,8)
angles=[]
for q in range(16):
 theta_c=dth*(q+arb(1)/2);s1,c1=theta_c.sin_cos();S1=MR.from_arb([s1]);C1=MR.from_arb([c1]);trig1=[S1,C1,-S1,-C1]
 cc=[trig1[(p+1)%4]*inv_fact[p] for p in range(9)];ss=[trig1[p%4]*inv_fact[p] for p in range(9)]
 cb=MR(np.array([x.m[0] for x in cc]),np.array([x.r[0] for x in cc]));sb=MR(np.array([x.m[0] for x in ss]),np.array([x.r[0] for x in ss]));angles.append((cb,sb))
# Bind critical scalar expressions directly to frozen-source AST nodes.
tree=ast.parse((S/'cert_forcing2.py').read_text());main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');expr={}
for name in ['c0','Umax','xr','tail','coef']:
 nodes=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(ast.unparse(t)==name for t in n.targets)];assert len(nodes)==1,(name,len(nodes));expr[name]=nodes[0].value
compiled={k:compile(ast.Expression(body=copy.deepcopy(v)),'frozen_series_'+k,'eval') for k,v in expr.items()}
base={'float':float,'succ':succ,'U':U,'arb':arb,'MR':MR,'comb':math.comb,'Kser':16}
records=[];qm=[];qr=[];qe=[];um=[];ur=[];ue=[];bcm=[];bcr=[];rows=[]
for ix,ci in enumerate(range(4096,4109)):
 h_up=float((tbs[ix+1]-tbs[ix]).mag());assert h_up==geo['cells'][ix]['h_up'];cell=Cell(h_up,w_up,12,8)
 E1c,E1r=tm_exp(1.0,h_up,12);ta=arb(float(tb[ix]),float(tr[ix]));e_ta=MR.from_arb([ta.exp()]);E1=BiTM.from_sigma(E1c*MR(e_ta.m[0],e_ta.r[0]),succ(E1r*float(e_ta.mag()[0])*(1+2*U)),cell)
 bern_c=BernSup(cell,64,8);hk=bern_c.hk;wk=bern_c.wk;assert hk==geo['cells'][ix]['hk'] and wk==geo['wk'];hb=32*hk;wb=4*wk;blockcell=Cell(hb,0.5*wb,12,8)
 for q,(cb,sb) in enumerate(angles):
  cos_b=BiTM.from_phi(cb,wq,cell);sin_b=BiTM.from_phi(sb,wq,cell)
  Ucell=E1*cos_b+BiTM.zero(cell);Ucell=add_const(Ucell,-XS_MR);Vcell=E1*sin_b
  for bs in range(2):
   for bp in range(2):
    a_s=MR.exact(bs*hb);a_p=MR.exact(-w_up)+MR.exact(bp*wb)+MR.exact(0.5*wb)
    ub,vb=REC.many([Ucell,Vcell],a_s,a_p,blockcell);qb=ub*ub+vb*vb
    ns=dict(base,qb=qb);c0=eval(compiled['c0'],ns);assert c0>0;ns['c0']=c0
    uq=add_const(qb,MR.exact(-c0));ns['uq']=uq;Umax=eval(compiled['Umax'],ns);ns['Umax']=Umax;xr=eval(compiled['xr'],ns);ns['xr']=xr;active=bool(xr<0.6);tail=0.0;cms=np.zeros(17);crs=np.zeros(17)
    if active:
     c0a=arb(c0);ns['c0a']=c0a;tail=eval(compiled['tail'],ns);z=MR.from_arb([c0a**arb(-0.5)])[0];cms[0]=float(z.m);crs[0]=float(z.r)
     for k in range(1,17):
      ns['k']=k;z=eval(compiled['coef'],ns);cms[k]=float(z.m);crs[k]=float(z.r)
    rows.append([ci,q,bs,bp]);qm.append(qb.c.m.copy());qr.append(qb.c.r.copy());qe.append(qb.r);um.append(uq.c.m.copy());ur.append(uq.c.r.copy());ue.append(uq.r);bcm.append(cms);bcr.append(crs)
    records.append({'ci':ci,'q':q,'bs':bs,'bp':bp,'active':active,'c0':c0,'Umax':float(Umax),'xr':float(xr),'tail':float(tail),'h':h_up,'w':w_up,'hk':float(hk),'wk':float(wk),'H':float(hb),'W':float(wb/2),'tb':float(tb[ix]),'tb_rad':float(tr[ix])})
 print(now(),'cell',ci,'blocks',len(records),'elapsed',round(time.monotonic()-tic,3),flush=True)
assert len(records)==832 and len({tuple(v) for v in rows})==832
arr={'indices':np.array(rows,dtype=np.int64),'q_mid':np.array(qm),'q_rad':np.array(qr),'q_rem':np.array(qe),'uq_mid':np.array(um),'uq_rad':np.array(ur),'uq_rem':np.array(ue),'coef_mid':np.array(bcm),'coef_rad':np.array(bcr)}
for k,a in arr.items():assert np.isfinite(a).all(),k
for k in ['q_rad','q_rem','uq_rad','uq_rem','coef_rad']:assert (arr[k]>=0).all(),k
p=D/'evidence/operands.npz';np.savez(p,**arr);pins[str(p.relative_to(B))]=sha(p)
p=D/'evidence/blocks.json';p.write_text(json.dumps(records,indent=1)+'\n');pins[str(p.relative_to(B))]=sha(p)
for f,h in pins.items():assert sha(B/f)==h,f
active=[r for r in records if r['active']];maxx=max(r['xr'] for r in active);maxt=max(r['tail'] for r in active)
out={'start_utc':started,'end_utc':now(),'seconds':time.monotonic()-tic,'status':'REGENERATED_GEOMETRY_SERIES_OPERANDS_REQUIRING_AUDIT','blocks':832,'active':len(active),'fallback':832-len(active),'max_active_x':maxx,'max_tail':maxt,'historic_maxima_equal':{'x':maxx==raw['worst_series']['x_series'],'tail':maxt==raw['worst_series']['tail']},'source_expressions':{k:ast.unparse(v) for k,v in expr.items()},'numpy_version':np.__version__,'python_version':sys.version,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'pins':pins,'scope':'Contemporary geometry-only frozen-source replay. No residual evaluation, no historical-array authentication.'}
(D/'evidence/regeneration.json').write_text(json.dumps(out,indent=2)+'\n');print(out['end_utc'],out['status'],out['seconds'],out['active'],out['fallback'],out['historic_maxima_equal'],flush=True)
