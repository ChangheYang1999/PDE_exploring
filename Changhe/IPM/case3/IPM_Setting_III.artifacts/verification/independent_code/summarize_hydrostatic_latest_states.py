"""Read completed result219; independently recompute its finite diagnostics."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import math,json,hashlib,sys
# Exact rational center strings have over 100000 decimal characters.
sys.set_int_max_str_digits(0)
root=Path('research/hydrostatic_latest_state_audit');v=root/'verification'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
pipe=json.loads((v/'PIPELINE.json').read_text())
if pipe['status']!='DONE':raise SystemExit('Result219 is incomplete. No summary written.')
checks=[]
def check(name,test,evidence=None):checks.append({'name':name,'passed':bool(test),'evidence':evidence})
for p,h in pipe['code_and_proof_sha256'].items():check('code/proof hash '+p,sha(p)==h)
check('inputmanifesthash',sha(v/'INPUTS.json')==pipe['input_sha256'])
inputs={x['tag']:x for x in json.loads((v/'INPUTS.json').read_text())['states']}
regions=[('tiny',0.,.01),('inner',.01,.1),('core',.1,1.),('annulus',1.,100.),('far',100.,float('inf')),('extent10',0.,10.),('extent100',0.,100.),('extent10000',0.,10000.000001)]
def table(rows):
 out={}
 for name,lo,hi in regions:
  chosen=[a for a in rows if lo<=math.hypot(a['x'],a['y'])<hi]
  if not chosen:continue
  b={'count':len(chosen),'undefined_Nf':sum(a['Nf']==0 for a in chosen),'undefined_Nv':sum(a['Nv']==0 for a in chosen)}
  for key in ['R','R_Nf','R_Nv']:
   good=[a for a in chosen if a[key] is not None]
   if good:b[key]=max(good,key=lambda a:abs(a[key]))
  out[name]=b
 return out

def examine(rows,c,label):
 errors=[];nulls=True;finite=True;bounds=True;horizontal=True
 for a in rows:
  x,y,g,gx,gy,u,w=(a[k] for k in ['x','y','g','gx','gy','V1','V2']);A=(c*x+u)*gx;B=(c*y+w)*gy
  vals={'R':A+B-g,'Nf':abs(A)+abs(B)+abs(g),'Nv':abs(g)+abs(x*gx+y*gy)+abs(u*gx+w*gy)}
  errors.extend(abs(a[k]-z)/(1+abs(z)) for k,z in vals.items());finite &= all(math.isfinite(z) for z in [x,y,g,gx,gy,u,w,*vals.values()])
  for key,N in [('R_Nf','Nf'),('R_Nv','Nv')]:
   if vals[N]==0:nulls &= a[key] is None
   else:
    nulls &= a[key] is not None
    if a[key] is not None:errors.append(abs(a[key]-abs(vals['R'])/vals[N]))
  bounds &= (a['R_Nf'] is None or a['R_Nf']<=1+1e-13) and (a['R_Nv'] is None or a['R_Nv']<=max(c,1)+1e-13)
  if y==0:horizontal &= vals['R']==vals['Nf']==vals['Nv']==0
 check(label+' finite',finite);check(label+' recomputed R/Nf/Nv',max(errors)<1e-12,max(errors));check(label+' undefineddenominators',nulls);check(label+' trianglebounds',bounds);check(label+' horizontalaxis',horizontal)

def differences(A,B):
 common=sorted(set(A)&set(B));out={}
 for key in ['V1','V2','R','R_Nf','R_Nv']:
  vals=[{'x':x,'y':y,'difference':B[x,y][key]-A[x,y][key]} for x,y in common if A[x,y][key] is not None and B[x,y][key] is not None]
  out[key]=max(vals,key=lambda z:abs(z['difference'])) if vals else None
 return {'common_points':len(common),'maximum_pointwise_changes':out}
rows=[]
for entry in pipe['states']:
 tag=entry['tag'];inp=inputs[tag];base=json.loads((v/(tag+'.json')).read_text());a=json.loads((v/(tag+'.refined.json')).read_text());c=base['metadata']['cl']
 check(tag+' complete',entry['status']==base['status']==a['status']=='DONE')
 check(tag+' sourcehash',sha(inp['frozen'])==inp['sha256']==base['source_sha256']==a['source_sha256'])
 check(tag+' basehash',sha(v/(tag+'.json'))==entry['base_sha256']==a['base_result_sha256'])
 check(tag+' refinedhash',sha(v/(tag+'.refined.json'))==entry['refined_sha256'])
 check(tag+' fourlevels',len(a['levels'])==4 and [z['method'] for z in a['levels']]==['linear','linear','power','power'])
 exact=base['exact'];aa=float(Fraction(exact['a']));ch=float(Fraction(exact['cH']));delta=float(Fraction(exact['delta']));b=float(exact['b']);e=float(exact['e'])
 check(tag+' exactcenterrelation',abs(delta-(c+ch-1))<1e-15)
 check(tag+' nondegenerate',aa!=0)
 out={'tag':tag,'source_sha256':a['source_sha256'],'c':c,'a':aa,'cH':ch,'delta':delta,'b':b,'e':e,'E':float(exact['E']),'K':float(exact['K']),'p':float(exact['p']),'tail_defect':float(exact['tail_defect']),'axis_cubic_R':(3*(c+ch)-1)*e-aa*b/3,'origin_flow_diagonal':[c-ch,c+ch],'origin_axis_R_Nf_limit':abs(delta)/(abs(c+ch)+1),'levels':[]}
 basepoints=base['samples'];examine(basepoints,c,tag+' baseline');coords=[(z['x'],z['y']) for z in basepoints]
 for lev in a['levels']:
  label=tag+' '+lev['method']+str(lev['order']);points=lev['points'];check(label+' 774samepoints',len(points)==774 and [(z['x'],z['y'])for z in points]==coords);examine(points,c,label)
  t=table(points);check(label+' recomputedregions',t==lev['regions'])
  out['levels'].append({'method':lev['method'],'order':lev['order'],'tail_order':lev['tail_order'],'split':lev['split'],'center':lev['center'],'center_error':abs(lev['center']-ch),'regions':t})
 check(tag+' twoMPlevels',set(z['target_digits'] for z in base['mp_jet_checks'])=={70,100})
 out['MP_max_absolute_derivative_difference']=max(z for r in base['mp_jet_checks'] for z in r['absolute_double_errors'])
 check(tag+' MPderivatives',out['MP_max_absolute_derivative_difference']<1e-8,out['MP_max_absolute_derivative_difference'])
 out['same_method_power_fullgrid_change']=differences({(z['x'],z['y']):z for z in a['levels'][2]['points']},{(z['x'],z['y']):z for z in a['levels'][3]['points']})
 witnesses={w['method']:w for w in a['witnesses']};check(tag+' twowitnessmethods',set(witnesses)=={'linear','power'})
 for method,w in witnesses.items():examine(w['points'],c,tag+' witness'+method)
 W={k:{(z['x'],z['y']):z for z in w['points']}for k,w in witnesses.items()};check(tag+' witnesssamepoints',set(W['linear'])==set(W['power']))
 F={(z['x'],z['y']):z for z in a['levels'][-1]['points']}
 out['power_witness_vs_fullgrid']=differences(F,W['power']);out['power_vs_linear_witness']=differences(W['linear'],W['power']);out['power_witness_center_error']=abs(witnesses['power']['center']-ch)
 needed=set()
 for lev in [base, *a['levels']]:
  for region in lev['regions'].values():
   for key in ['R','R_Nf','R_Nv']:
    if key in region:needed.add((region[key]['x'],region[key]['y']))
 check(tag+' allmaximizerswitnessed',needed<=set(W['power']))
 out['witness_count']=len(W['power']);out['final_regions']=out['levels'][-1]['regions'];rows.append(out)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS' if all(a['passed'] for a in checks)else'FAIL','count':len(checks),'checks':checks,'states':rows,'proof_sha256':sha(root/'SUMMARY_PROOF.md'),'driver_sha256':sha(__file__),'scope':'Finite hydrostatic trials and empirical quadrature comparisons, not full elliptic IPM candidates.'}
(v/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Two newer hydrostatic trial states','',result['utc']+'; '+result['status']+'; '+str(len(checks))+' summary checks.','', 'These are c=2 hydrostatic trial states. The following maxima use the final power-tail 64/192/128 rule on774 independent physical points, with zero denominators left undefined. Highest-order witnesses and full-grid changes are separate empirical comparisons. They are not uniform error bounds.']
for a in rows:
 lines.extend(['','## '+a['tag'],'',f"a={a['a']:.12g}, c_H={a['cH']:.12g}, center defect={a['delta']:.9g}, b={a['b']:.9g}, e/a={a['E']:.9g}. The actual axis cubic residual coefficient is {a['axis_cubic_R']:.9g}.",'','| Region | max abs R | max abs R/Nf | max abs R/Nv | Nf-max location (x,y) |','|---|---:|---:|---:|---|'])
 for name in ['tiny','inner','core','annulus','far','extent10','extent100','extent10000']:
  z=a['final_regions'][name];p=z['R_Nf'];lines.append(f"| {name} | {abs(z['R']['R']):.9g} | {p['R_Nf']:.9g} | {z['R_Nv']['R_Nv']:.9g} | ({p['x']:.9g},{p['y']:.9g}) |")
 lines.extend(['','| Method/order/tail/split | center error |','|---|---:|'])
 for z in a['levels']:lines.append(f"| {z['method']} {z['order']}/{z['tail_order']}/{z['split']:g} | {z['center_error']:.4g} |")
 lines.append(f"| power witness88/256/512 | {a['power_witness_center_error']:.4g} |")
 for key in ['same_method_power_fullgrid_change','power_witness_vs_fullgrid','power_vs_linear_witness']:
  z=a[key];lines.append('\n'+key+': '+str(z['common_points'])+' common points; max pointwise changes '+', '.join(k+'='+format(abs(w['difference']),'.5g')for k,w in z['maximum_pointwise_changes'].items()if w is not None)+'.')
lines.extend(['','All maximizing points retain absolute R, Nf, Nv and locations in SUMMARY.json and the raw *.refined.json. The grid spans1e-5..1e4, with the three nested extents10,100,10000. It includes axes, near-axis angles and selected parity probes. This is a two-state audit, not a three-resolution convergence study. Old linear-tail results remain visible; replacing them is an inverse-evaluation correction, not a solver improvement.','', 'No candidate satisfies a SettingIII endpoint on this evidence. The auxiliary hydrostatic problem and the principal elliptic problem remain OPEN. Run python3 independent_code/summarize_hydrostatic_latest_states.py only after PIPELINE.json says DONE.'])
(v/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(result['status'],len(checks));print([a for a in checks if not a['passed']])
if result['status']!='PASS':raise SystemExit(1)
