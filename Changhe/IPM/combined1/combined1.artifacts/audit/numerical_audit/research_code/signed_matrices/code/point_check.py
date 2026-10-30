"""Check rational Cartesian points selected from inconclusive cover cells."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,math,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/point_witness/code'))
sys.path.insert(0,str(ROOT/'research/global_matrices/code'))
from cartesian import CartesianJet,ar,q
from cover import endpoints,digest
from radial import Radial
ctx.prec=1024;start=time.monotonic();cp=ROOT/'research/signed_matrices/verification/d2_M1_768.json'
data=json.loads(cp.read_text());paths=data['pending'][:12]
source=ROOT/'research/refit_audit/data/d2_canonical.json';model=Radial(source)
model.fields['chi13']=(model.deriv(1,3),4,'s');rows=[]
for path in paths:
 a,b,c,d=endpoints(path);t=float((a+b)/2);z=float((c+d)/2);r2=t/(1-t)
 x=format(math.sqrt(r2*(1+z)/2),'.8f');y=format(math.sqrt(r2*(1-z)/2),'.8f')
 jet=CartesianJet(source,x,y);v={'chi04':jet.chi(0,4),'chi22':jet.chi(2,2),'chi13':jet.chi(1,3)}
 other=model.evaluate(x,y);assert all(v[k].overlaps(other[k]) for k in v)
 eig=1-(v['chi04']+v['chi22'])/2-((v['chi04']-v['chi22'])**2+4*v['chi13']**2).sqrt()/2
 gap=eig-ar(q('9/10'))
 rows.append({'cover_path':path,'point':[x,y],'fields':{k:a.str(90) for k,a in v.items()},
              'least_eigenvalue':eig.str(90),'gap_above_target':gap.str(90),'target_refuted':bool(gap<0),'independent_field_overlaps':True})
 print('point',x,y,'M1',eig.str(18),'refutes',bool(gap<0),flush=True)
 if gap<0:break
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'candidate':'d2',
     'cover_sha256':digest(cp),'source_sha256':digest(source),'code_sha256':digest(__file__),'rows':rows,
     'elapsed_seconds':time.monotonic()-start,'scope':'Only a strictly negative point gap refutes the global condition; other results are inconclusive.'}
(ROOT/'research/signed_matrices/verification/d2_M1_points.json').write_text(json.dumps(out,indent=2)+'\n')
