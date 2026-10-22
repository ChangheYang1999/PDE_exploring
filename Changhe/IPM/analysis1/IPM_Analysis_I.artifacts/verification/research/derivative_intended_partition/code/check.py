"""Exact coherent geometry plus reproduction of source start/width calculations."""
import os,sys
sys.dont_write_bytecode=True
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,importlib.util,shutil,time
import numpy as np
from flint import arb,ctx,fmpq
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_intended_partition';N=B.parent/'ipmA-num';W=B/'research/weighted_derivative_scalar_norms';ctx.prec=128;ctx.threads=1

def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def dump(p,v):
 with p.open('x') as f:json.dump(v,f,indent=1);f.write('\n')
def utc():return datetime.now(timezone.utc).isoformat()
def fq(x):return F.from_float(float(x))
def pin(p):
 p=p.resolve();pins[str(p.relative_to(B)) if p.is_relative_to(B) else str(p)]=sha(p)
start=utc();tick=time.monotonic();pins={};arrays={};source_files=['cert_resid_deriv.py','cert_resid.py','cert_green_outer.py','cert_green.py','midrad.py','xnorm_cert.py']
for name in source_files:
 p=N/'src'/name;q=D/'sources'/name
 need(not q.exists(),'fresh source '+name);shutil.copyfile(p,q);pin(q);pin(p)
sp=importlib.util.spec_from_file_location('frozen_derivative_geometry_mr',D/'sources/midrad.py');mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
part=B/'research/middle_residual/evidence/partition_exact.json';pin(part);grid=json.loads(part.read_text());pts=[]
for j,s in enumerate(grid['spans']):
 a,b=F(s['a_exact']),F(s['b_exact']);n=s['count'];need(s['span']==j and s['first_cell']==len(pts) and b>a and n>0,'span structure')
 if j:need(a==oldb,'middle spans meet')
 pts.extend(a+(b-a)*i/n for i in range(n));oldb=b
pts.append(oldb);need(len(pts)==7810 and grid['cells']==7809,'middle all points')
bmin,bmax=pts[0],pts[-1]
params=json.loads((W/'data_exact/parameters.json').read_text());pin(W/'data_exact/parameters.json')
trial=N/'data/trial_v2_h0.008.npz';pin(trial)
with np.load(trial,allow_pickle=False) as a:
 need(fq(a['knots'][0])==bmin and fq(a['knots'][-1])==bmax,'actual trial endpoint binding')
 need(fq(a['k'])==F(params['params']['k']['exact']) and fq(a['L'])==F(params['params']['L']['exact']),'actual weight parameters')
regions={};data={'schema':'ipm-coherent-derivative-geometry-v1','regions':{},'params':params['params']};rowrecords=[];counts=0
for reg,expected in [('inner',2632),('middle',7809),('outer',8948)]:
 path=N/'data'/('cert_green.npz' if reg=='middle' else 'cert_'+reg+'_green.npz');pin(path)
 with np.load(path,allow_pickle=False) as z:
  names=['tb','tb_rad'] if reg=='middle' else ['tau','tau_rad',('tmin' if reg=='inner' else 't0'),('tmin_rad' if reg=='inner' else 't0_rad')]
  small={name:np.array(z[name],copy=True) for name in names}
 names2=['tb','tb_rad'] if reg=='middle' else ['tau','tau_rad'];mm,rr=(small[k] for k in names2)
 need(mm.shape==rr.shape==(expected+1,) and np.isfinite(mm).all() and np.isfinite(rr).all() and (rr>=0).all(),'geometry arrays')
 base=F(0) if reg=='middle' else fq(small['tmin' if reg=='inner' else 't0']);baserad=F(0) if reg=='middle' else fq(small['tmin_rad' if reg=='inner' else 't0_rad'])
 need(baserad==0,'this data has exact base')
 if reg!='middle':need(base==(bmin if reg=='inner' else bmax),'base equality')
 nodes=pts if reg=='middle' else [base+F(-5 if reg=='inner' else 0)+F(5 if reg=='inner' else 17)*i/expected for i in range(expected+1)]
 for i,x in enumerate(nodes):need(fq(mm[i])-fq(rr[i])<=x-base<=fq(mm[i])+fq(rr[i]),'true node inside exported box '+reg+str(i))
 rowpath=W/'sources'/('derivative_'+reg+'.json');pin(rowpath);rows=json.loads(rowpath.read_text())['rows'];need(len(rows)==expected,'source rows')
 raw=mod.MR(mm,rr);harr=(raw[1:]-raw[:-1]).mag();rmax=F(0);imin=0
 for i,row in enumerate(rows):
  need(row['ci']==i and float(harr[i]).hex()==float(row['h']).hex(),'actual MR width reproduction '+reg+str(i))
  x,y=nodes[i:i+2];h=fq(row['h']);ah=fq(row['t_a']);need(y>x and h>=y-x,'true cell length bound')
  if reg=='middle':actual=float(mm[i])
  else:actual=float((arb(float(base),float(baserad))+arb(float(mm[i]),float(rr[i]))).mid())
  need(actual.hex()==float(row['t_a']).hex(),'actual rounded start reproduction '+reg+str(i))
  err=abs(x-ah)
  if err>rmax:rmax=err;imin=i
  rowrecords.append({'region':reg,'ci':i,'a':str(x),'b':str(y),'offset':str(x-ah),'h_slack':str(h-(y-x))})
  counts+=1
 regions[reg]={'cells':expected,'hull':[str(nodes[0]),str(nodes[-1])],'max_start_error':str(rmax),'max_start_error_cell':imin,'positive_start_errors':sum(F(z['offset'])>0 for z in rowrecords[-expected:]),'negative_start_errors':sum(F(z['offset'])<0 for z in rowrecords[-expected:])}
 data['regions'][reg]={'npz':str(path.resolve()),'source_rows':str(rowpath.relative_to(B)),'members':{k:{'shape':list(v.shape),'hex':[float(x).hex() for x in v.flat],'payload_sha256':hashlib.sha256(v.tobytes()).hexdigest()} for k,v in small.items()}}
need(counts==19389 and regions['inner']['hull'][1]==regions['middle']['hull'][0] and regions['middle']['hull'][1]==regions['outer']['hull'][0],'complete coherent coverage')
delta=max(F(v['max_start_error']) for v in regions.values());need(delta<F(1,10**14),'provisional delta 1e-14 bound')
data['partition_source']=str(part.relative_to(B));data['rows']=rowrecords;dump(D/'data_exact/geometry.json',data);pin(D/'data_exact/geometry.json');pin(Path(__file__));pin(D/'PROOF.md')
# Direct weight loss bound, independent of all physical derivative majorants.
ctx.prec=320;d=arb(fmpq(delta.numerator,delta.denominator));q=(4*d).exp();need(q.upper()<arb('1.00000000000004'),'loss <1+4e-14')
result={'start_utc':start,'utc':utc(),'status':'PASS_COHERENT_PARTITION_SOURCE_ROUNDING_AND_WIDTHS','rows':counts,'node_inclusions':counts+3,'regions':regions,'delta':str(delta),'exp4delta_arb':str(q),'loss_ceiling':'1.00000000000004','files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Geometry and weight only. Physical derivative majorants and historical runtime remain hypotheses; tails absent.'};dump(D/'evidence/check.json',result);print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
