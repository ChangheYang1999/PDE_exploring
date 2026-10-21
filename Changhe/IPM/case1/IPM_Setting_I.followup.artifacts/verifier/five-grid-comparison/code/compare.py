"""Aggregate own saved field components using exact binary-rational arithmetic."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import hashlib, json, math, statistics
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'verifier/five-grid-comparison/verification'
pins={}
def read(rel):
    p=ROOT/rel; raw=p.read_bytes(); pins[rel]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)
def state(rel):
    p=ROOT/rel; raw=p.read_bytes(); pins[rel]=hashlib.sha256(raw).hexdigest()
    with np.load(p,allow_pickle=False) as a:
        return {'N':int(a['N']),'M':int(a['M']),'cl':float(a['c_l']),'L':float(a['L']),'beta':float(a['beta']),'md5':hashlib.md5(raw).hexdigest()}
def check(ok,msg):
    if not ok: raise ValueError(msg)
def q(x):return Q(float(x))
pointfile='verifier/sampled-physical-actions/verification/points.json'
points=read(pointfile)['points']; ph=pins[pointfile]; check(len(points)==58,'point count')
raw=read('verifier/sampled-physical-actions/refinement_radial/actions.json')
fd=read('verifier/sampled-physical-actions/verification/gradients_refined.json')
chain=read('verifier/sampled-physical-actions/verification/gradients_chainrule.json')
base=read('verifier/sampled-physical-actions/verification/actions.json')
check(fd['base_actions_sha256']==pins['verifier/sampled-physical-actions/verification/actions.json'],'gradient source')
check(raw['point_sha256']==ph and raw['points']==points and fd['points']==points,'shared points')
check(raw['complete'] and fd['complete'] and chain['complete'] and base['complete'],'complete inputs')
registration=read('verifier/five-grid-comparison/verification/registration.json')
for rel,sha in registration['manually_inspected_source_sha256'].items():
    check(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==sha,'inspected source pin')
inputs=[]
for topic,tag in [('third-grid','dnB_n72m30S'),('fourth-grid','dnB_n84m35S'),('fifth-grid','dnB_n108m44S')]:
    meta=state(f'verifier/{topic}/data/{tag}.npz'); d=read(f'verifier/{topic}/verification/{tag}_broad4096.json')
    check(meta['md5']==d['source_md5'] and d['points_sha256']==ph and d['complete'],'broad source binding')
    inputs.append((meta,d['config'],d['rows'],[r['gradient'] for r in d['rows']],[r['analytic_gradient'] for r in d['rows']],'U'))
for tag,name in [('n96m40S','dnB_n96m40S.npz'),('n120m48_S','dnSB_n120m48.npz')]:
    meta=state('verifier/sampled-physical-actions/data/'+name)
    d=next(s for s in raw['states'] if s['tag']==tag)
    g=next(s for s in fd['states'] if s['tag']==tag)
    a=next(s for s in chain['states'] if s['tag']==tag)
    check(meta['md5']==d['state_md5']==g['state_md5']==a['state_md5'],'action source binding')
    check(meta['cl']==d['cl'],'cl binding')
    check(g['gradient_steps'][-1]['relative_step']==3.125e-5,'fine gradient')
    inputs.append((meta,raw['config'],d['rows'],g['gradient_steps'][-1]['base_gradient'],a['base_gradient'],'base_U'))
inputs.sort(key=lambda z:z[0]['N']); exact=[]; states=[];max_decimal_error=Decimal(0);decimal_rows=0;decimal_quantities=0
for meta,config,rows,grads,agrads,ukey in inputs:
    check(meta['md5']==registration['expected_state_md5'][str(meta['N'])],'previously audited state identity')
    want={'nang':4096,'order':28 if meta['N'] in (72,84,108) else 32,'panel':.08 if meta['N'] in (72,84,108) else .075,'rmax':'1e30'}
    check(all(config[k]==value for k,value in want.items()),'inverse configuration')
    check(meta['L']==8 and meta['beta']==.9,'common scale');check(len(rows)==len(grads)==len(agrads)==58,'row count')
    rr=[]; records=[]
    for i,(row,gg,ag) in enumerate(zip(rows,grads,agrads)):
        check(row['point']==points[i] and row['index']==i,'point order')
        x=list(map(q,row['point']));u=list(map(q,row[ukey]));g=list(map(q,gg));rho=q(row['rho']);cl=q(meta['cl'])
        w=[cl*x[k]+u[k] for k in range(2)]; prod=[w[k]*g[k] for k in range(2)]
        r=sum(prod)-rho;nf=abs(rho)+sum(map(abs,prod));nv=abs(rho)+abs(sum(x[k]*g[k]for k in range(2)))+abs(sum(u[k]*g[k]for k in range(2)))
        check(nf>0 and nv>0,'positive denominators')
        chainchange=sum(w[k]*(q(ag[k])-g[k])for k in range(2))/nf
        with localcontext() as c:
            c.prec=110
            dd=lambda z:Decimal.from_float(float(z))
            dr=(dd(meta['cl'])*dd(row['point'][0])+dd(row[ukey][0]))*dd(gg[0])+(dd(meta['cl'])*dd(row['point'][1])+dd(row[ukey][1]))*dd(gg[1])-dd(row['rho'])
            dx=[dd(z)for z in row['point']];du=[dd(z)for z in row[ukey]];dg=[dd(z)for z in gg];dp=[(dd(meta['cl'])*dx[k]+du[k])*dg[k]for k in range(2)]
            df=abs(dd(row['rho']))+sum(map(abs,dp));dv=abs(dd(row['rho']))+abs(sum(dx[k]*dg[k]for k in range(2)))+abs(sum(du[k]*dg[k]for k in range(2)))
            for dec,rat in [(dr,r),(df,nf),(dv,nv),(abs(dr)/df,abs(r)/nf),(abs(dr)/dv,abs(r)/nv)]:
                error=abs(dec-Decimal(rat.numerator)/Decimal(rat.denominator));max_decimal_error=max(max_decimal_error,error)
                check(error<Decimal('1e-90'),'decimal reconstruction');decimal_quantities+=1
            decimal_rows+=1
        rr.append({'R':r,'Nf':nf,'Nv':nv,'rho':rho,'U':u,'g':g})
        records.append({'index':i,'point':points[i],'R':str(r),'Nf':str(nf),'Nv':str(nv),'absR_Nf':float(abs(r)/nf),'absR_Nv':float(abs(r)/nv),'analytic_change_fixed_Nf':float(chainchange)})
    vals=[abs(a['R'])/a['Nf']for a in rr];vvals=[abs(a['R'])/a['Nv']for a in rr];mi=max(range(58),key=lambda i:vals[i])
    states.append({'state':meta,'inverse_config':config,'max_R_Nf':float(vals[mi]),'max_R_Nf_index':mi,'max_R_Nf_point':points[mi],'RMS_R_Nf':math.sqrt(float(sum(v*v for v in vals)/58)),'RMS_squared_rounded':float(sum(v*v for v in vals)/58), 'RMS_exact_reconstructible_from_saved_row_fractions':True,'max_R_Nv':float(max(vvals)),'median_R_Nf':float(statistics.median(vals)),'max_absolute_R':float(max(abs(a['R'])for a in rr)),'max_gradient_chainrule_effect':max(abs(r['analytic_change_fixed_Nf'])for r in records),'rows':records})
    exact.append(rr)
ref=exact[-1]
for si,rows in enumerate(exact):
    vals=[abs(a['R'])/b['Nf']for a,b in zip(rows,ref)]
    states[si]['max_R_fixed_Nf120']=float(max(vals));states[si]['RMS_R_fixed_Nf120']=math.sqrt(float(sum(v*v for v in vals)/58))
    for row,v in zip(states[si]['rows'],vals):row['absR_fixed_Nf120']=float(v)
pairs=[]
for si in range(4):
    a,b=exact[si:si+2]
    diff=[abs(x['R']-y['R'])/z['Nf']for x,y,z in zip(a,b,ref)]
    pairs.append({'from_N':states[si]['state']['N'],'to_N':states[si+1]['state']['N'],'own_normalized_increase_count':sum(abs(y['R'])/y['Nf']>abs(x['R'])/x['Nf']for x,y in zip(a,b)),'absolute_R_increase_count':sum(abs(y['R'])>abs(x['R'])for x,y in zip(a,b)),'max_R_difference_fixed_Nf120':float(max(diff)),'max_density_difference':float(max(abs(x['rho']-y['rho'])for x,y in zip(a,b))),'max_velocity_component_difference':float(max(abs(x['U'][k]-y['U'][k])for x,y in zip(a,b)for k in range(2)))})
# Independently audit the newly added numerical report's simple summaries.
fifth=next(s for s in states if s['state']['N']==108);xstar=8.576668173142153
near=[r for r in fifth['rows']if math.hypot(r['point'][0]-xstar,r['point'][1])<2]
far=[r for r in fifth['rows']if math.hypot(*r['point'])>15]
extra={'fifth_RMS':fifth['RMS_R_Nf'],'fifth_median':fifth['median_R_Nf'],'near_P_count':len(near),'near_P_max':max(r['absR_Nf']for r in near),'r_gt15_count':len(far),'r_gt15_max':max(r['absR_Nf']for r in far),'largest3':sorted(fifth['rows'],key=lambda r:r['absR_Nf'],reverse=True)[:3]}
pins['verifier/five-grid-comparison/PROOF.md']=hashlib.sha256((ROOT/'verifier/five-grid-comparison/PROOF.md').read_bytes()).hexdigest()
pins['verifier/five-grid-comparison/code/compare.py']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
for rel,sha in pins.items():check(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==sha,'input changed '+rel)
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','states':states,'adjacent':pairs,'num_report_summary_check':extra,'pins':pins,'decimal_crosscheck_rows':decimal_rows,'decimal_crosscheck_quantities':decimal_quantities,'decimal_scope':'Different arithmetic implementation on identical parsed binary components; checks R,Nf,Nv and both ratios, not independent physical data','max_decimal_quantity_difference':str(max_decimal_error),'scope':'Exact arithmetic on saved binary components; differing radial quadratures disclosed. Finite samples only. No continuum error, convergence, kernel, family or endpoint.'}
(OUT/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'utc':result['utc'],'verdict':'PASS','states':[{k:v for k,v in s.items()if k != 'rows'}for s in states],'adjacent':pairs,'num_report':{k:v for k,v in extra.items()if k!='largest3'},'max_decimal_error':str(max_decimal_error)},indent=2))
