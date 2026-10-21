"""Independent paired audit summary. --partial reports only finished grids."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification'
raw=(V/'withheld.json').read_bytes();data=json.loads(raw);partial='--partial' in sys.argv
if not partial:assert data.get('complete'), 'full withheld calculation incomplete'
fits=json.loads((V/'fits.json').read_text());assert fits['complete']
out={'date':datetime.now(timezone.utc).isoformat(),'withheld_sha256':hashlib.sha256(raw).hexdigest(),'entire_calculation_complete':bool(data.get('complete')),'states':[],'scope':'Independent paired whole-plane inverse at4fit and84withheld physical points; finite samples, not uniform residual bounds. Numerical differences are not interval error certificates. The exact fixed-field center exclusions remain.'}
for st in data['states']:
 if len(st['rows'])!=88:continue
 fs=next(x for x in fits['states'] if x['tag']==st['tag']);fit=next(x for x in fs['fits'] if x['filename']==fs['selected']);rr=st['rows'];wh=[r for r in rr if r['set']=='withheld'];ft=[r for r in rr if r['set']=='fit'];assert len(wh)==84 and len(ft)==4
 ent={'tag':st['tag'],'files':st['files'],'md5s':st['md5s'],'number_withheld':len(wh),'selected_fit_radius':fit['radius'],'fit_shape_RMS':fit['shape_norm'],'fit_baseline_max':fs['baseline_R_actualN_max'],'fit_selected_max':fit['fit_R_actualN_max'],'fields':[],'paired_decomposition':{}}
 for i,label in enumerate(['base','corrected']):
  rows=[r['fields'][i] for r in wh];nf=np.array([r['Nf'] for r in rows]);R=np.array([r['R'] for r in rows]);metrics={'label':label,'withheld_min_abs_rho':min(abs(r['rho']) for r in rows),'withheld_min_Nf':float(min(nf))}
  for name in ['absR_Nf','absR_Nv']:
   values=np.array([r[name] for r in rows]);j=int(np.argmax(values));metrics[name]={'max':float(values[j]),'RMS':float(np.linalg.norm(values)/np.sqrt(len(values))),'max_point':wh[j]['point'],'max_index':wh[j]['index']}
  for name in ['Cartesian_step_R_change_fixedNf','analytic_gradient_R_change_fixedNf','tail_R_using_numerical_gradient']:
   metrics[name+'_max']=max(abs(r[name]) for r in rows)
  metrics['R_RMS_over_fixed_base_Nf']=float(np.linalg.norm(R/np.array([r['fields'][0]['Nf'] for r in wh]))/np.sqrt(84));ent['fields'].append(metrics)
 nf0=np.array([r['fields'][0]['Nf'] for r in wh]);bR=np.array([r['fields'][0]['R'] for r in wh]);nR=np.array([r['fields'][1]['R'] for r in wh]);delta=[];quad=[];reconstruction=[]
 fpath=ROOT/'data'/st['files'][0]
 with np.load(fpath) as z:cl=float(z['cl']) if 'cl' in z else float(z['c_l'])
 for r in wh:
  a,b=r['fields'];g0=np.array(a['gradient']);g1=np.array(b['gradient']);u0=np.array(a['U']);u1=np.array(b['U']);W=cl*np.array(r['point'])+u0;dg=g1-g0;du=u1-u0;dh=b['rho']-a['rho'];lin=float(W@dg+du@g0-dh);q=float(du@dg);delta.append(lin);quad.append(q);reconstruction.append(abs((b['R']-a['R'])-lin-q)/a['Nf'])
 delta=np.array(delta);quad=np.array(quad);err=max(reconstruction);assert err<1e-12
 ent['paired_decomposition']={'linear_R_RMS_over_base_Nf':float(np.linalg.norm(delta/nf0)/np.sqrt(84)),'quadratic_R_RMS_over_base_Nf':float(np.linalg.norm(quad/nf0)/np.sqrt(84)),'quadratic_R_max_over_base_Nf':float(max(abs(quad/nf0))),'expansion_max_error_over_base_Nf':err,'samples_improved_actual_Nf':sum(r['fields'][1]['absR_Nf']<r['fields'][0]['absR_Nf'] for r in wh),'samples_worse_actual_Nf':sum(r['fields'][1]['absR_Nf']>r['fields'][0]['absR_Nf'] for r in wh),'max_signed_change_fixed_base_Nf':float(max(abs((nR-bR)/nf0)))}
 ent['fit_direct_quadratic_max_U_difference']=max(max(abs(z) for z in r['fields'][1]['direct_vs_quadratic_U']) for r in ft);ent['fit_direct_quadratic_max_R_difference_fixed_baseNf']=max(abs(r['fields'][1]['direct_vs_quadratic_R_fixed_base_Nf']) for r in ft)
 out['states'].append(ent)
name='withheld_summary_partial' if partial else 'withheld_summary';(V/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));print('COMPLETE_GRIDS',len(out['states']))
