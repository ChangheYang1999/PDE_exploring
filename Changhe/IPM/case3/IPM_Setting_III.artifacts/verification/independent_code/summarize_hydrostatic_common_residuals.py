"""Result287: independent scalar recomputation, masks, rounding and witnesses."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import json,hashlib,math,re,traceback
import numpy as np
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];rows=[];comparisons=[];selected={};refinements=[];headers={};start=datetime.now(timezone.utc).isoformat();eps=np.finfo(float).eps
regions=[(0.,.1),(.1,1.),(1.,100.),(100.,1e4),(1e4,1e6+1)]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def finitefloat(x):return None if not np.isfinite(x)else float(x)
def save(status):
 out=dict(status=status,started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,refinements=refinements,comparisons=comparisons,disagreements=[a for a in comparisons if not a['agrees']],witnesses=[dict(tag=k,indices=sorted(v))for k,v in selected.items()],source_sha256={str(p):sha(p)for p in [V/'RUN.json',V/'INPUTS.json',V/'POINTS.npz']},proof_sha256=sha(R/'SUMMARY_PROOF.md'),corrected_base_proof_sha256=sha(R/'PROOF.md'),proof_correction_sha256=sha(V/'PROOF_CORRECTION.json'),driver_sha256=sha(__file__),review_proof_sha256=sha(R/'REVIEW_RESOLUTION_PROOF.md'),source_headers=headers,longdouble_epsilon=str(np.finfo(np.longdouble).eps),zero_record_scope='Off-axis zero counts recompute the finite-sample positivity property already required by the base gate; no positivity theorem.',scope='Sampled auxiliary residuals; printed disagreements require adaptive followup. Fullplane UNRESOLVED.')
 (V/'SUMMARY.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
try:
 correction=json.loads((V/'PROOF_CORRECTION.json').read_text());ck('executed protocol hash',sha(correction['old_path'])==correction['old_sha256']);ck('corrected proof hash',sha(correction['new_path'])==correction['new_sha256']);ck('only corrected minus sign',Path(correction['old_path']).read_text().replace('Phi_yy=g_x and V=','-Phi_yy=g_x and V=')==Path(correction['new_path']).read_text())
 ck('extended precision is wider',np.finfo(np.longdouble).eps<eps)
 inp=json.loads((V/'INPUTS.json').read_text())
 for entry in inp['files']+[b[k]for b in inp['states']for k in ['state','export']]:ck('frozen source '+entry['path'],sha(entry['path'])==entry['sha256'])
 source=(V/'producer_definition_static.py').read_text();ck('source reporting radii',"r = np.logspace(-3, 6, 37)"in source and "Rr = Rg.reshape(-1)"in source);ck('source region endpoints','regs = [(0, 0.1), (0.1, 1), (1, 100), (100, 1e4), (1e4, 1e6 + 1)]'in source);ck('source region comparisons','m = (Rr >= lo) & (Rr < hi)'in source);ck('source pointwise ratio',"(np.abs(R[mm]) / Nf[mm]).max()"in source);ck('source denominator',"Nf = np.abs((c * X + V1) * gx) + np.abs((c * Y + V2) * gy) + np.abs(g)"in source)
 run=json.loads((V/'RUN.json').read_text());ck('pipeline complete',run['status']=='PASS'and all(z['passed']for z in run['checks']));ck('pipeline proof',run['proof_sha256']==sha(V/'EXECUTED_BASE_PROTOCOL.md'));ck('pipeline driver',run['driver_sha256']==sha('independent_code/audit_hydrostatic_common_residuals.py'));ck('pipeline inputs',run['input_sha256']==sha(V/'INPUTS.json'));ck('points hash',run['points_sha256']==sha(V/'POINTS.npz'))
 for k,h in run['modules'].items():ck('current module '+k,sha(Path('independent_code')/k)==h)
 for m in run['manufactures']:
  ck('manufacture hash '+m['path'],sha(m['path'])==m['sha256']);a=json.loads(Path(m['path']).read_text());ck('manufacture allpassed '+m['path'],a['status']=='PASS'and all(c['passed']for c in a['checks'])and len(a['checks'])==m['count'])
 pts=np.load(V/'POINTS.npz')['points'];x,y,r,j=pts.T;ck('radial-major exact radii',np.array_equal(r,np.repeat(np.logspace(-3,6,37),9)));ck('angular index order',np.array_equal(j,np.tile(np.arange(9),37)));ck('333points',len(pts)==333);ck('exact axes counts',sum(x==0)==37 and sum(y==0)==37);masks=[(r>=lo)&(r<hi)for lo,hi in regions];ck('regional partition',np.all(np.sum(masks,axis=0)==1));radial_indices=np.repeat(np.arange(37),9);integer_masks=[(radial_indices>=a)&(radial_indices<b)for a,b in [(0,8),(8,12),(12,20),(20,28),(28,37)]];ck('all regional masks match integer boundaries',all(np.array_equal(a,b)for a,b in zip(masks,integer_masks)))
 tokens={}
 for c,file in [(2,'producer_hs_common_res_c2.txt'),(3,'producer_hs_common_res_c3_hsG.txt')]:
  lines=(V/file).read_text().splitlines();headers[file]=lines[:2];ck('source header metrics '+file,'per region: max |R_h| / max |R_h|/N_f'in lines[0])
  for line in lines:
   m=re.match(r'^(\d+)x(\d+)\s+(.+)$',line)
   if not m:continue
   N,M=int(m[1]),int(m[2]);v=m[3].split();ck('finite scientific decimal tokens '+str((c,N)),all(re.fullmatch(r'[+-]?\d+\.\d{2}e[+-]\d+',t)for t in v));ck('10tokens '+str((c,N)),len(v)==10);ck('unique source row '+str((c,N)),(c,N)not in tokens);ck('source grid N M '+str((c,N)),sum(t['c']==c and t['N']==N and t['M']==M for t in run['states'])==1);tokens[c,N]=[v[i:i+2]for i in range(0,10,2)]
 ck('seven source states',len(tokens)==7)
 for state in run['states']:
  tag=state['tag'];c=state['c'];N=state['N'];selected[tag]=set();data=[];summary=dict(tag=tag,c=c,N=N,p=state['p'],levels=[]);rows.append(summary)
  for level in state['levels']:
   p=Path(level['path']);ck(tag+' raw hash '+str(level['order']),sha(p)==level['sha256']);a=dict(np.load(p));g=a['jets'][:,0];grad=a['jets'][:,1:3];vel=a['velocity'];z=[];scales=[];transport_scales=[];bound_scales=[]
   for pt,g0,d,v in zip(pts,g,grad,vel):
    xx,yy=map(np.longdouble,pt[:2]);gx,gy=map(np.longdouble,d);u,w=map(np.longdouble,v);gg=np.longdouble(g0);C=np.longdouble(c);aa=(C*xx+u)*gx;bb=(C*yy+w)*gy
    rh=aa+bb-gg;nf=abs(aa)+abs(bb)+abs(gg);nv=abs(gg)+abs(xx*gx+yy*gy)+abs(u*gx+w*gy);nb=np.sqrt((C*xx+u)**2+(C*yy+w)**2)*np.sqrt(gx**2+gy**2)+abs(gg);z.append([rh,nf,nv,nb]);scales.append(abs(gg)+abs(xx*gx)+abs(yy*gy)+abs(u*gx)+abs(w*gy));transport_scales.append(abs(gg)+abs(C*xx*gx)+abs(C*yy*gy)+abs(u*gx)+abs(w*gy));bound_scales.append((abs(C*xx)+abs(u)+abs(C*yy)+abs(w))*np.sqrt(gx*gx+gy*gy)+abs(gg))
   z=np.array(z,dtype=np.longdouble);ar={key:np.asarray(z[:,k],dtype=float)for k,key in enumerate(['Rh','Nf','Nv','Nbound'])}
   arithmetic_scales={'Rh':np.maximum(np.asarray(transport_scales,dtype=float),np.finfo(float).tiny),'Nf':np.maximum(np.asarray(transport_scales,dtype=float),np.finfo(float).tiny),'Nv':np.maximum(np.asarray(scales,dtype=float),np.finfo(float).tiny),'Nbound':np.maximum(np.asarray(bound_scales,dtype=float),np.finfo(float).tiny)}
   for key in ar:
    delta=abs(ar[key]-a[key]);ck(tag+' independent scalar '+key+' '+str(level['order']),np.all(delta<=128*eps*arithmetic_scales[key]),dict(max_abs_difference=float(max(delta))))
   ck(tag+' signed axis '+str(level['order']),np.all(ar['Rh'][y==0]==0)and np.all(ar['Nf'][y==0]==0)and np.all(ar['Nv'][y==0]==0))
   for ratio,denom in [('Rf','Nf'),('Rv','Nv'),('Rbound','Nbound')]:
    ar[ratio]=np.divide(abs(ar['Rh']),ar[denom],out=np.full(len(pts),np.nan),where=ar[denom]>0);ck(tag+' ratio mask '+ratio+str(level['order']),np.array_equal(np.isnan(ar[ratio]),np.isnan(a[ratio])));positive=ar[denom]>0;tol=512*eps*(arithmetic_scales['Rh'][positive]+ar[ratio][positive]*arithmetic_scales[denom][positive])/ar[denom][positive];ck(tag+' ratio arithmetic '+ratio+str(level['order']),np.all(abs(ar[ratio][positive]-a[ratio][positive])<=tol),dict(max_abs_difference=float(max(abs(ar[ratio][positive]-a[ratio][positive])))))
   lev=dict(order=level['order'],regions=[],raw_path=str(p),raw_sha256=sha(p));summary['levels'].append(lev);data.append((ar,vel))
   for k,mask in enumerate(masks):
    row=dict(region=k,interval=regions[k],point_count=int(sum(mask)),zero_nf=int(sum(mask&(ar['Nf']==0))),zero_nv=int(sum(mask&(ar['Nv']==0))),offaxis_zero_nf=int(sum(mask&(y>0)&(ar['Nf']==0))),offaxis_zero_nv=int(sum(mask&(y>0)&(ar['Nv']==0))),maxima={})
    for key in ['Rh','Rf','Rv','Rbound']:
     values=abs(ar[key])if key=='Rh'else ar[key];idx=np.where(mask&np.isfinite(values))[0];ck(tag+f' nonempty {level["order"]}/{k}/{key}',len(idx)>0);order=idx[np.lexsort((idx,-values[idx]))];i=int(order[0]);second=int(order[1]);maxi=dict(value=float(values[i]),index=i,x=float(x[i]),y=float(y[i]),radius=float(r[i]),angle_index=int(j[i]),signed_Rh=float(ar['Rh'][i]),Nf=float(ar['Nf'][i]),Nv=float(ar['Nv'][i]),Nbound=float(ar['Nbound'][i]),g=float(g[i]),gradient=list(map(float,grad[i])),velocity=list(map(float,vel[i])),second_index=second,second_value=float(values[second]),gap=float(values[i]-values[second]),tie_indices=list(map(int,idx[values[idx]==values[i]])));row['maxima'][key]=maxi
     if key in ['Rh','Rf']or(key=='Rv'and N==max(s['N']for s in run['states']if s['c']==c)):selected[tag].add(i)
    lev['regions'].append(row)
  ck(tag+' three levels',[a['order']for a in summary['levels']]==[32,48,64]);fine=summary['levels'][-1];final=data[-1][0]
  for k in range(5):
   for q,key in enumerate(['Rh','Rf']):
    token=tokens[c,N][k][q];val=fine['regions'][k]['maxima'][key]['value'];half=F(10)**Decimal(token).as_tuple().exponent/2;diff=F.from_float(val)-F(token);agree=abs(diff)<=half;row=dict(tag=tag,c=c,N=N,region=k,metric=key,printed=token,value=val,agrees=agree,rounding_half_width=str(half),signed_difference=str(diff),gap_outside_interval=str(abs(diff)-half),corrected=format(val,'.'+str(len(token.split('e')[0].split('.')[1]))+'e'),index=fine['regions'][k]['maxima'][key]['index']);comparisons.append(row)
    if not agree:
     values=abs(final[key])if key=='Rh'else final[key];idx=np.where(masks[k]&np.isfinite(values))[0];selected[tag].update(map(int,idx[np.argsort(values[idx])[-3:]]))
  for a,b in [(0,1),(1,2)]:
   da,va=data[a];db,vb=data[b];row=dict(tag=tag,orders=[summary['levels'][a]['order'],summary['levels'][b]['order']],regions=[])
   for k,mask in enumerate(masks):
    diffs=dict(region=k,weighted_velocity=float(np.max(np.hypot(*(va-vb).T)[mask]/(1+r[mask])**state['p'])),absolute_Rh=float(np.max(abs(da['Rh']-db['Rh'])[mask])))
    for key in ['Rf','Rv','Rbound']:diffs[key]=float(np.nanmax(abs(da[key]-db[key])[mask]))
    row['regions'].append(diffs)
   refinements.append(row)
 # Physical grid neighbors are additional sampled witnesses, not a continuum bound.
 for tag,base in selected.items():
  expanded=set(base)
  for i in base:
   k,jj=divmod(i,9)
   for kk,ll in [(k-1,jj),(k+1,jj),(k,jj-1),(k,jj+1)]:
    if 0<=kk<37 and 0<=ll<9:expanded.add(9*kk+ll)
  selected[tag]=expanded
 ck('70source comparisons',len(comparisons)==70);ck('7states',len(rows)==7);save('PASS');print('PASS',len(checks),'printed disagreements',sum(not a['agrees']for a in comparisons),'witnesses',sum(map(len,selected.values())),datetime.now(timezone.utc).isoformat())
 for a in comparisons:
  if not a['agrees']:print('DISAGREE',a['tag'],a['region'],a['metric'],a['printed'],a['value'],a['corrected'])
except Exception:
 save('FAIL');(V/'summary_traceback.txt').write_text(traceback.format_exc());raise
