"""Certified finite plain-norm curvature and weighted angular mass partitions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from stream_precision_audit import unpack
ctx.prec=640;start=time.monotonic();now=datetime.now(timezone.utc)
base=Path('research/64_log_precision_updates/verification/log_sin1_c3_p512_N290_20261031T061856Z')
paths=[base/'checks.json',base/'selected_packed_coefficients.json']
raws=[p.read_bytes() for p in paths];data,packed=map(json.loads,raws)
root=Path('research/87_plain_distance_diagnostics');out=root/'verification'/now.strftime('%Y%m%dT%H%M%SZ');out.mkdir()
text=lambda x:x.str(30,radius=True)
L10=arb(10).log();lf={n:arb(factorial(n)).log()/L10 for n in range(291)}
res=dict(checked_at_utc=now.isoformat(timespec='seconds'),checkpoint_sha256=data['checkpoint_sha256'],precision_bits=640,inputs=[dict(path=str(p),sha256=sha256(raw).hexdigest()) for p,raw in zip(paths,raws)],plain={},distance=[])
allrows={}
for f in ['f','g']:
 rows={r['n']:r for r in data['fields'][f]['all_order_factorial_comparisons']};allrows[f]=rows
 L={n:arb(r['log10_plain_norm']) for n,r in rows.items()};curv=[];slopes=[];maxima=[]
 for n in range(100,291):
  h=30;den=lf[n]-2*lf[n-h]+lf[n-2*h];assert den>0
  curv.append(dict(n=n,h=h,finite_sigma=text((L[n]-2*L[n-h]+L[n-2*h])/den)))
  slopes.append(dict(n=n,h=h,per_order_increment=text((L[n]-L[n-h])/h)))
 for n in [200,230,260,290]:
  cols=list(map(arb,rows[n]['column_log10_norms']));q=max(range(len(cols)),key=lambda q:float(cols[q].mid()));assert all(cols[q]>v for j,v in enumerate(cols) if j!=q)
  maxima.append(dict(n=n,q=q,column_log10=text(cols[q]),plain_log10=text(L[n])))
 res['plain'][f]=dict(curvatures=curv,slopes=slopes,strict_plain_column_maxima=maxima)
res['plain']['stream_over_density']=[dict(n=n,log10_ratio=text(arb(allrows['g'][n]['log10_plain_norm'])-arb(allrows['f'][n]['log10_plain_norm'])),ratio=text(((arb(allrows['g'][n]['log10_plain_norm'])-arb(allrows['f'][n]['log10_plain_norm']))*L10).exp())) for n in range(230,291)]
n=290
for f in ['f','g']:
 cols=packed[f][str(n)]
 for center in ['common_P','factor_channel']:
  # The common center is |P|; factor_channel is |P+1| for density, |P| for stream.
  center3=abs(6-2*n) if center=='common_P' or f=='g' else abs(9-2*n)
  weights=[];rows=[];globalbands=[arb(0)]*3;highbands=[arb(0)]*3;distnorm={C:arb(0) for C in [1,4,12]}
  for q,col in enumerate(cols):
   norm=arb(0);bands=[arb(0)]*3;first=arb(0);absbands=[arb(0)]*2;modevalues=[]
   for j,v in enumerate(col):
    mass=abs(arb(*unpack(v)));m=2*j+(f=='f');d3=abs(3*m-center3);norm+=mass
    band=(0 if d3<=6 else 2) if q==0 else (0 if 4*d3<=3*q else 1 if d3<=3*q else 2)
    bands[band]+=mass;first+=mass*d3/3
    if d3<=6:absbands[0]+=mass
    if d3<=30:absbands[1]+=mass
    if mass>0:modevalues.append((mass,m,d3))
    for C in distnorm:distnorm[C]+=mass*factorial(q)*(arb(3*C)/(3+d3))**q
   assert norm>0
   fac=arb(factorial(q))*12**q;w=norm*fac;weights.append(w)
   for b in range(3):
    globalbands[b]+=bands[b]*fac
    if q>=40:highbands[b]+=bands[b]*fac
   vmax,mmax,dmax=max(modevalues,key=lambda x:float(x[0].log().mid()));assert all(vmax>v for v,m,d in modevalues if m!=mmax)
   rows.append(dict(q=q,column_norm=text(norm),weighted_log10=text(w.log()/L10),fractions=[text(v/norm) for v in bands],mean_distance=text(first/norm),mean_distance_over_q=None if q==0 else text(first/norm/q),distance_le_2=text(absbands[0]/norm),distance_le_10=text(absbands[1]/norm),largest_mode_frequency=mmax,largest_mode_distance=str(arb(dmax)/3)))
  total=sum(weights,arb(0));high=sum(highbands,arb(0));winner=max(range(len(weights)),key=lambda q:float(weights[q].log().mid()));assert all(weights[winner]>v for q,v in enumerate(weights) if q!=winner)
  for q,row in enumerate(rows):row['weighted_share_of_total']=text(weights[q]/total)
  res['distance'].append(dict(field=f,n=n,center=center,center_times_3=center3,weight_s=12,strict_maximum_weighted_column=winner,total_log10=text(total.log()/L10),global_weighted_band_fractions=[text(v/total) for v in globalbands],q_ge_40_weighted_share=text(high/total),q_ge_40_band_fractions=[text(v/high) for v in highbands],distance_norm_log10={str(C):text(v.log()/L10) for C,v in distnorm.items()},columns=rows))
res['actual_elapsed_s']=time.monotonic()-start
(out/'checks.json').write_text(json.dumps(res,indent=2)+'\n')
for name in ['plain_distance_diagnostics.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps(dict(output_directory=str(out),actual_elapsed_s=res['actual_elapsed_s'])))
for f in ['f','g']:
 print(json.dumps(dict(field=f,curvatures=[r for r in res['plain'][f]['curvatures'] if r['n'] in [120,150,180,210,240,270,290]],maxima=res['plain'][f]['strict_plain_column_maxima'])))
for row in res['distance']:
 print(json.dumps({k:v for k,v in row.items() if k!='columns'}))
 print(json.dumps(dict(field=row['field'],center=row['center'],selected_columns=[r for r in row['columns'] if r['q'] in [40,50,60,70,80,84,90,91,92,93,94,95]])))
