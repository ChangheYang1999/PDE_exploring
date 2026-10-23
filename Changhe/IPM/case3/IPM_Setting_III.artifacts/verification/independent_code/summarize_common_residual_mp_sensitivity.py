"""Result287: controlled local jet/inverse comparisons, no additional quadrature."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,traceback,math
import mpmath as mp
import numpy as np
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];rows=[];tokens=[];start=utc();regions=[(0,.1),(.1,1),(1,100),(100,1e4),(1e4,1e6+1)]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def metric(jet,vel,x,y,c):
 g,gx,gy=jet[:3];u,v=vel;aa=(c*x+u)*gx;bb=(c*y+v)*gy;rr=mp.fsum([aa,bb,-g]);nf=abs(aa)+abs(bb)+abs(g);nv=abs(g)+abs(mp.fsum([x*gx,y*gy]))+abs(mp.fsum([u*gx,v*gy]));nb=mp.sqrt((c*x+u)**2+(c*y+v)**2)*mp.sqrt(gx*gx+gy*gy)+abs(g)
 d=dict(Rh=rr,Nf=nf,Nv=nv,Nbound=nb,T=abs(c*x*gx)+abs(u*gx)+abs(c*y*gy)+abs(v*gy)+abs(g))
 d.update({ratio:abs(rr)/den if den else None for ratio,den in [('Rf',nf),('Rv',nv),('Rbound',nb)]});return d
def serialize(d):return {k:mp.nstr(v,108)if v is not None else None for k,v in d.items()}
def ff(v):return F.from_float(float(v))
def fraction_record(d):return {k:F(v)if v is not None else None for k,v in d.items()if k in ['Rh','Rf','Rv','Rbound']}
def verdict(a,b,center,half,sensitivity):
 da=a-center;db=b-center;ina=abs(da)<=half;inb=abs(db)<=half;margin=min(abs(abs(da)-half),abs(abs(db)-half));stable=margin>10*sensitivity;same=(da>half and db>half)or(da< -half and db< -half)
 return ('CONFIRMED'if ina and inb and stable else'REFUTED'if not ina and not inb and same and stable else'OPEN'),margin,ina,inb
def save(status):
 out=dict(status=status,started_utc=start,finished_utc=utc(),count=len(checks),checks=checks,rows=rows,tokens=tokens,source_sha256={str(V/f):sha(V/f)for f in ['RUN.json','SUMMARY.json','ADAPTIVE.json','ADAPTIVE_SUMMARY.json','MP_JETS.json','INPUTS.json','POINTS.npz','MP_SELECTION.json','revision153/FIXED_COMPARISON.json']},proof_sha256=sha(R/'MP_SENSITIVITY_PROOF.md'),driver_sha256=sha(__file__),scope='Partially MP-corrected finite samples with empirical tenfold reporting margin; no rigorous error enclosure or full-plane endpoint.')
 (V/'MP_SENSITIVITY.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
try:
 with mp.workdps(108):
  d=metric(list(map(mp.mpf,['.3125','.25','1.25','.5'])),list(map(mp.mpf,['.125','-.5'])),mp.mpf('.5'),mp.mpf('.25'),mp.mpf(2));ck('manufactured exact residual',d['Rh']==-mp.mpf(1)/32);ck('manufactured Nf',d['Nf']==mp.mpf(19)/32);ck('manufactured Nv without c',d['Nv']==mp.mpf(43)/32);ck('manufactured ratios',d['Rf']==mp.mpf(1)/19 and d['Rv']==mp.mpf(1)/43)
  a=metric(list(map(mp.mpf,[0,0,1,0])),list(map(mp.mpf,[.2,0])),mp.mpf(1),mp.mpf(0),mp.mpf(2));ck('horizontal denominator policy',a['Rh']==a['Nf']==a['Nv']==0 and a['Rf']is None and a['Rv']is None and a['Rbound']==0)
  a=metric(list(map(mp.mpf,[0,0,1,0])),list(map(mp.mpf,[0,0])),mp.mpf(0),mp.mpf(0),mp.mpf(2));ck('origin denominator policy',all(a[k]is None for k in ['Rf','Rv','Rbound']))
 for name,a,b,e,want in [('inside','1.01','1.015','.001','CONFIRMED'),('outside','1.07','1.075','.001','REFUTED'),('boundary','1.05','1.05','0','OPEN')]:ck('reporting manufacture '+name,verdict(F(a),F(b),F(1),F('.05'),F(e))[0]==want)
 run=json.loads((V/'RUN.json').read_text());base=json.loads((V/'SUMMARY.json').read_text());ad=json.loads((V/'ADAPTIVE.json').read_text());ads=json.loads((V/'ADAPTIVE_SUMMARY.json').read_text());jets=json.loads((V/'MP_JETS.json').read_text());rev=json.loads((V/'revision153/FIXED_COMPARISON.json').read_text());selection=json.loads((V/'MP_SELECTION.json').read_text());points=np.load(V/'POINTS.npz')['points'];gates=[('base',base),('adaptive',ad),('adaptive summary',ads),('MP',jets),('revision',rev)]
 for name,g in gates:ck(name+' complete',g['status']=='PASS'and all(c['passed']for c in g['checks']))
 ck('MP driver',jets['driver_sha256']==sha('independent_code/audit_common_residual_mp_jets.py'));ck('MP scalar module',jets['module_sha256']==sha('independent_code/scalar_mp_hydrostatic_density.py'));ck('MP exact18selection',jets['selection_sha256']==sha(V/'MP_SELECTION.json')and sorted((t['tag'],t['index'])for t in jets['rows'])==[(t['tag'],t['index'])for t in selection['selection']]and len(jets['rows'])==18)
 for source in [ads,jets]:
  for p,h in source['source_sha256'].items():ck('parent source '+p,sha(p)==h)
 fixed={};adaptive={};partial_fixed={};partial_adaptive={};parameters={}
 for state in run['states']:
  level=state['levels'][-1];ck('raw fixed binding '+state['tag'],sha(level['path'])==level['sha256']);fixed[state['tag']]=dict(np.load(level['path']));arr=fixed[state['tag']];partial_fixed[state['tag']]={i:{key:ff(arr[key][i])if np.isfinite(arr[key][i])else None for key in ['Rh','Rf','Rv','Rbound']}for i in range(333)}
 for state in ad['states']:
  tag=state['tag'];parameters[tag]=state['c'];adaptive[tag]={q['index']:q for q in state['points']};partial_adaptive[tag]={q['index']:{key:ff(q[key])if q[key]is not None else None for key in ['Rh','Rf','Rv','Rbound']}for q in state['points']}
 for row in jets['rows']:
  tag=row['tag'];i=row['index'];ck('MP inside adaptive '+tag+str(i),i in adaptive[tag]);point=adaptive[tag][i];arr=fixed[tag];x,y,r,j=points[i];ck('MP exact coordinate '+tag+str(i),row['coordinate_hex']==[float(x).hex(),float(y).hex()]and row['x']==point['x']==x and row['y']==point['y']==y);ck('MP precisions '+tag+str(i),[a['dps']for a in row['precisions']]==[72,108])
  with mp.workdps(108):
   jm=list(map(mp.mpf,row['precisions'][-1]['jet']));jd=[mp.mpf(float(t))for t in arr['jets'][i]];vf=[mp.mpf(float(t))for t in arr['velocity'][i]];va=[mp.mpf(float(t))for t in point['V']];xx,yy,c=mp.mpf(float(x)),mp.mpf(float(y)),mp.mpf(float(parameters[tag]));dd=metric(jd,vf,xx,yy,c);mf=metric(jm,vf,xx,yy,c);da=metric(jd,va,xx,yy,c);ma=metric(jm,va,xx,yy,c);cross=mp.fsum([(va[k]-vf[k])*(jm[k+1]-jd[k+1])for k in range(2)]);decomp=ma['Rh']-mf['Rh']-da['Rh']+dd['Rh'];scale=sum(a['T']for a in [dd,mf,da,ma]);ck('bilinear residual decomposition '+tag+str(i),abs(cross-decomp)<=mp.mpf('1e-95')*max(mp.mpf('1e-300'),scale),mp.nstr(abs(cross-decomp),20))
   for k in ['Rh','Nf','Nv','Nbound','Rf','Rv','Rbound']:
    old=row['precisions'][-1][k];ck('same MP fixed '+tag+str(i)+k,(old is None and mf[k]is None)or(old is not None and mf[k]is not None and abs(mp.mpf(old)-mf[k])<=mp.mpf('1e-95')*max(mp.mpf('1e-300'),abs(mf[k]),scale)))
   item=dict(tag=tag,index=i,region=next(k for k,(lo,hi)in enumerate(regions)if lo<=r<hi),x=float(x),y=float(y),four_records={name:serialize(a)for name,a in [('doublejet_fixedV',dd),('MPjet_fixedV',mf),('doublejet_adaptiveV',da),('MPjet_adaptiveV',ma)]},Rh_decomposition={name:mp.nstr(value,100)for name,value in [('arithmetic_change',dd['Rh']-mp.mpf(float(arr['Rh'][i]))),('local_jet_change',mf['Rh']-dd['Rh']),('inverse_change',da['Rh']-dd['Rh']),('cross_term',cross)]});rows.append(item);partial_fixed[tag][i]=fraction_record(item['four_records']['MPjet_fixedV']);partial_adaptive[tag][i]=fraction_record(item['four_records']['MPjet_adaptiveV'])
 for version,comparisons in [('original_q3',base['comparisons']),('revision153',rev['comparisons'])]:
  for t in comparisons:
   tag=t['tag'];region=t['region'];key=t['metric'];printed=t.get('printed',t.get('token'));half=F(t.get('rounding_half_width',t.get('half_width')));lo,hi=regions[region];regional=lambda data:[(i,abs(z[key])if key=='Rh'else z[key])for i,z in data.items()if lo<=points[i,2]<hi and z[key]is not None];i,a=max(regional(partial_fixed[tag]),key=lambda t:t[1]);j,b=max(regional(partial_adaptive[tag]),key=lambda t:t[1]);parent=next(s for s in ads['tokens']if s['tag']==tag and s['region']==region and s['metric']==key);emp=F.from_float(parent['empirical_sensitivity']);chosen=[q for q in rows if q['tag']==tag and q['region']==region];local=F(0)
   for q in chosen:
    z=q['four_records']
    for lhs,rhs in [('MPjet_fixedV','doublejet_fixedV'),('MPjet_adaptiveV','doublejet_adaptiveV')]:
     if z[lhs][key]is not None and z[rhs][key]is not None:local=max(local,abs(F(z[lhs][key])-F(z[rhs][key])))
   sensitivity=max(emp,local,abs(a-b));label,margin,ina,inb=verdict(a,b,F(printed),half,sensitivity);tokens.append(dict(version=version,source=t.get('source','original artifact'),tag=tag,region=region,metric=key,printed=printed,half_width=str(half),partially_corrected_fixed_value=str(a),partially_corrected_adaptive_value=str(b),fixed_float=float(a),adaptive_float=float(b),fixed_index=i,adaptive_index=j,MP_point_count=len(chosen),fixed_agrees=ina,adaptive_agrees=inb,previous_sensitivity=str(emp),observed_local_jet_sensitivity=str(local),sensitivity=str(sensitivity),margin=str(margin),verdict=label,scope='Partially corrected finite samples and an empirical reporting margin, not an enclosure.'))
 ck('all187 tokens',len(tokens)==187 and sum(t['version']=='original_q3'for t in tokens)==70 and sum(t['version']=='revision153'for t in tokens)==117);ck('all18 local records',len(rows)==18);save('PASS');print('PASS',len(checks),utc());print({v:{k:sum(t['version']==v and t['verdict']==k for t in tokens)for k in ['CONFIRMED','REFUTED','OPEN']}for v in ['original_q3','revision153']})
except Exception:
 (V/'mp_sensitivity_traceback.txt').write_text(traceback.format_exc())
 if all((V/f).exists()for f in ['ADAPTIVE_SUMMARY.json','MP_JETS.json']):save('FAIL')
 raise
