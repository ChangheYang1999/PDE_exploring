"""Result277: reproducible sampled statistics, literal printed precision and witnesses."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import json,hashlib,re,math
import numpy as np
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification'
assert V.resolve().is_relative_to(Path('verification'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];compares=[]
def ck(name,b,e=None):checks.append(dict(name=name,passed=bool(b),evidence=e))
def load(name):return json.loads((V/name).read_text())
def check_gate(name,expected_count):
    g=load(name)
    ck(name+' complete',g['status']=='PASS' and g['count']==expected_count and all(q['passed'] for q in g['checks']))
    return g
raw=check_gate('RUN.json',52)
ref=check_gate('REFINEMENT.json',35)
adapt=check_gate('ADAPTIVE.json',20)
gauss=check_gate('ADAPTIVE_MANUFACTURE.json',54)
power=check_gate('ADAPTIVE_POWER_MANUFACTURE.json',243)
for data,proof,driver in [(raw,'PROOF.md','audit_hydrostatic_velocity_sequence.py'),(ref,'WITNESS_PROOF.md','refine_hydrostatic_velocity_witnesses.py'),(adapt,'WITNESS_PROOF.md','audit_adaptive_velocity_witnesses.py'),(gauss,'WITNESS_PROOF.md','check_adaptive_hydrostatic_velocity.py'),(power,'ADAPTIVE_REVIEW_PROOF.md','check_adaptive_velocity_power_tails.py')]:
    ck(driver+' proof binding',data['proof_sha256']==sha(R/proof))
    ck(driver+' code binding',data['driver_sha256']==sha(Path('independent_code')/driver))
    for name,value in data.get('code_sha256',{}).items():ck(driver+' module '+name,value==sha(Path('independent_code')/name))
for data in [adapt,gauss,power]:ck('adaptive module binding '+str(data['count']),data['module_sha256']==sha('independent_code/adaptive_hydrostatic_velocity.py'))
ck('adaptive refinement binding',adapt['refinement_sha256']==sha(V/'REFINEMENT.json'))
ck('adaptive Gaussian binding',adapt['gate_sha256']==sha(V/'ADAPTIVE_MANUFACTURE.json'))
ck('refinement raw binding',ref['raw_sha256']==sha(V/'RUN.json'))
ck('adaptive raw binding',adapt['raw_sha256']==sha(V/'RUN.json'))
inp=load('INPUTS.json')
ck('raw input binding',raw['input_sha256']==sha(V/'INPUTS.json'))
ck('ref input binding',ref['input_sha256']==sha(V/'INPUTS.json'))
for row in inp['files']:ck('frozen text '+row['path'],sha(row['path'])==row['sha256'])
for row in inp['states']:ck('frozen coefficients '+row['tag'],sha(row['state']['path'])==row['state']['sha256'])
initial=load('SUMMARY_initial.json')
ck('initial two failures retained',initial['status']=='FAIL' and initial['count']==119 and sum(not q['passed'] for q in initial['checks'])==2)
ck('initial driver retained',initial['driver_sha256']==sha(V/'summary_checker_initial.py'))
items={s['tag']:s for s in raw['states']}
xy=np.array([[q['x'],q['y'],q['r']] for q in raw['states'][0]['levels'][-1]['points']])
arrays={tag:np.array([q['V'] for q in s['levels'][-1]['points']]) for tag,s in items.items()}
refined={s['tag']:{q['index']:q for q in s['levels'][-1]['points']} for s in ref['states']}
ref88={s['tag']:{q['index']:q for q in s['levels'][0]['points']} for s in ref['states']}
adaptive={s['tag']:{q['index']:q for q in s['points']} for s in adapt['states']}
ck('225 coordinates',xy.shape==(225,3))
ck('seven complete raw states',len(items)==7 and all(s['status']=='DONE' for s in items.values()))
ck('185 refined state points',sum(map(len,refined.values()))==185)
ck('7 adaptive state points',sum(map(len,adaptive.values()))==7)
sensitivity=[]
for tag,s in items.items():
    for level in s['levels']:
        ck('coordinates '+tag+str(level['order']),np.array_equal(xy,np.array([[q['x'],q['y'],q['r']] for q in level['points']])))
    p=s['p'];ar48=np.array([q['V'] for q in s['levels'][1]['points']])
    err48=float(np.max(abs(ar48-arrays[tag])/(1+xy[:,2,None])**p))
    err64=err88=0.
    for i,q in refined[tag].items():
        ck('ref point '+tag+str(i),[q['x'],q['y'],q['r']]==list(xy[i]))
        err64=max(err64,float(np.max(abs(np.array(q['V'])-arrays[tag][i]))/(1+q['r'])**p))
        err88=max(err88,float(np.max(abs(np.array(q['V'])-ref88[tag][i]['V']))/(1+q['r'])**p))
    ck('refined empirical sensitivity '+tag,max(err48,err64,err88)<1e-9,[err48,err64,err88])
    sensitivity.append(dict(tag=tag,weighted48to64=err48,weighted64to128=err64,weighted88to128=err88))
regions=[('inner',0,.1),('subunit',.1,1),('annulus',1,100),('far',100,10001)]
statistics=[];runner_gaps=[]
def observation(value,token,kind,**where):
    with localcontext() as context:
        context.prec=60
        literal=Decimal(token)
        unit=Decimal(10)**literal.as_tuple().exponent
        half=unit/2
        delta=Decimal(str(value))-literal
        agrees=abs(delta)<=half
        gap=max(Decimal(0),abs(delta)-half)
    row=dict(kind=kind,value=float(value),printed=token,agrees=bool(agrees),half_unit=str(half),difference_from_printed=str(delta),outside_interval_by=str(gap),**where)
    compares.append(row)
    return row
for c,suffix in [(2,'c2'),(3,'c3_hsG')]:
    text=(V/f'producer_hs_vel_cauchy_{suffix}.txt').read_text()
    tags=sorted([tag for tag,s in items.items() if s['c']==c],key=lambda tag:int(re.search(r'_N(\d+)',tag)[1]))
    printed=[]
    for line in text.split('scale of',1)[0].splitlines():
        match=re.match(r'^(\d+)x(\d+)\s*->\s*(\d+)x(\d+)\s+(.*)$',line)
        if match:printed.append((tuple(map(int,match.groups()[:4])),re.findall(r'[+-]?\d+\.\d+e[+-]\d+',match[5])))
    ck('pair row count '+str(c),len(printed)==len(tags)-1)
    for old,new,(dims,tokens) in zip(tags,tags[1:],printed):
        ck('pair labels '+old+new,[dims[0],dims[2]]==[int(re.search(r'_N(\d+)',tag)[1]) for tag in [old,new]])
        ck('pair printed columns '+old+new,len(tokens)==12)
        A=arrays[old];B=arrays[new];D=A-B
        for mask,rd in [('nominal',xy[:,2]),('hypot',np.hypot(xy[:,0],xy[:,1]))]:
            weight=(1+rd)**(1/c)
            values=[abs(D[:,0])/weight,abs(D[:,1])/weight,np.linalg.norm(D,axis=1),np.linalg.norm(B,axis=1)]
            out_regions={}
            for j,(name,lo,hi) in enumerate(regions):
                ii=np.flatnonzero((rd>=lo)&(rd<hi))
                ck('region nonempty '+old+new+mask+name,len(ii)>0)
                maxima=[]
                for k,value in enumerate(values):
                    pos=int(ii[np.argmax(value[ii])]);order=ii[np.argsort(value[ii],kind='stable')];runner=int(order[-2]);gap=float((value[pos]-value[runner])/value[pos])
                    ck('positive max '+old+new+mask+name+str(k),value[pos]>0)
                    ck('max refined '+old+new+mask+name+str(k),all(pos in refined[tag] for tag in [old,new]))
                    if gap<=1e-6:ck('close runner refined '+old+new+mask+name+str(k),all(runner in refined[tag] for tag in [old,new]))
                    runner_gaps.append(dict(old=old,new=new,mask=mask,region=name,metric=k,top=pos,runner=runner,relative_gap=gap))
                    maxima.append(dict(index=pos,value=float(value[pos]),x=float(xy[pos,0]),y=float(xy[pos,1]),r=float(xy[pos,2]),actual_radius=float(math.hypot(xy[pos,0],xy[pos,1]))))
                ratio=maxima[2]['value']/maxima[3]['value']
                out_regions[name]=dict(count=len(ii),maxima=maxima,euclidean_regional_ratio=ratio)
                if mask=='nominal':
                    for k in [0,1]:observation(maxima[k]['value'],tokens[3*j+k],'pair_component',c=c,old=old,new=new,region=name,component=k,index=maxima[k]['index'])
                    observation(ratio,tokens[3*j+2],'pair_ratio',c=c,old=old,new=new,region=name,difference_index=maxima[2]['index'],scale_index=maxima[3]['index'])
            statistics.append(dict(c=c,old=old,new=new,mask=mask,regions=out_regions))
    # Last-state scales, same regional weighted component definitions.
    line=next(line for line in text.splitlines() if line.startswith('scale of last:'))
    tokens=re.findall(r'[+-]?\d+\.\d+e[+-]\d+',line)
    ck('last scale token count '+str(c),len(tokens)==8)
    B=arrays[tags[-1]];rd=xy[:,2]
    for k,(name,lo,hi) in enumerate(regions):
        ii=np.flatnonzero((rd>=lo)&(rd<hi))
        for component in [0,1]:
            value=float(np.max(abs(B[ii,component])/(1+rd[ii])**(1/c)))
            observation(value,tokens[2*k+component],'last_scale',c=c,tag=tags[-1],region=name,component=component)
    for component,chunk in [(1,text.split('V_2(0, y)',1)[1].split('V_1(',1)[0]),(0,text.split('V_1(xi, 0)',1)[1])]:
        rows=[(int(re.match(r'^\s*(\d+)x',line)[1]),re.findall(r'[+-]\d+\.\d+',line)) for line in chunk.splitlines() if re.match(r'^\s*\d+x\d+:',line)]
        ck('axis row count '+str((c,component)),len(rows)==len(tags))
        for tag,(N,tokens) in zip(tags,rows):
            ck('axis labels '+tag+str(component),N==int(re.search(r'_N(\d+)',tag)[1]) and len(tokens)==7)
            for k,token in enumerate(tokens):
                index=36*k+(8 if component==1 else 0);q=refined[tag][index];p=items[tag]['p']
                denominator=(q['r'] if component==1 else 1+q['r'])**p
                ck('axis exact coordinate '+tag+str(component)+str(k),(q['x']==0 if component==1 else q['y']==0) and abs(q['r']/10**(k-2)-1)<2e-15)
                observation(q['V'][component]/denominator,token,'axis',c=c,tag=tag,component=component,index=index,r=q['r'])
failures=[q for q in compares if not q['agrees']]
ck('174 literal printed comparisons',len(compares)==174)
expected={('pair_component',2,'hsG_c2.0_N96_log','inner',0),('pair_ratio',2,'hsG_c2.0_N96_log','inner',None),('axis',2,'hsG_c2.0_N96_log',216,0),('axis',2,'hsG_c2.0_N192_log',180,0)}
actual={(q['kind'],q['c'],q.get('old',q.get('tag')),q.get('region',q.get('index')),q.get('component')) for q in failures}
ck('four identified disagreements and no hidden ones',actual==expected,failures)
adaptive_comparisons=[]
for tag,points in adaptive.items():
    for i,q in points.items():
        ck('adaptive coordinate '+tag+str(i),[q['x'],q['y'],q['r']]==list(xy[i]))
        weight=(1+q['r'])**items[tag]['p']
        delta=np.array(q['V'])-refined[tag][i]['V']
        error=float(np.max(abs(delta))/weight)
        estimate=float(max(q['estimated_error'])/weight)
        ck('adaptive empirical agreement '+tag+str(i),error<1e-9,error)
        ck('adaptive estimated error '+tag+str(i),estimate<1e-9,estimate)
        ck('adaptive no warnings '+tag+str(i),not q['messages'])
        adaptive_comparisons.append(dict(tag=tag,index=i,weighted_difference=error,weighted_estimated_error=estimate,V=q['V'],refinedV=refined[tag][i]['V']))
a='hsG_c2.0_N96_log';b='hsG_c2.0_N128_log_cont'
ad=np.array(adaptive[a][30]['V'])-adaptive[b][30]['V']
br=np.array(adaptive[b][35]['V'])
ratio=float(np.linalg.norm(ad)/np.linalg.norm(br))
coarse=next(s for s in statistics if s['old']==a and s['new']==b and s['mask']=='nominal')['regions']['inner']['euclidean_regional_ratio']
ck('adaptive ratio agreement',abs(ratio-coarse)<1e-8,dict(adaptive=ratio,coarse=coarse))
ck('ratio scale positive',np.linalg.norm(br)>0)
with localcontext() as context:
    context.prec=60
    ratio_gap=Decimal('0.004745')-Decimal(str(coarse))
    ck('reviewer ratio gap correction',Decimal('3e-7')<ratio_gap<Decimal('3.1e-7'),str(ratio_gap))
inner=[s['regions']['inner'] for s in statistics if s['old']==a and s['new']==b]
ck('same inner masks and witnesses',inner[0]==inner[1])
ck('no near ties omitted',min(q['relative_gap'] for q in runner_gaps)>1e-6,min(q['relative_gap'] for q in runner_gaps))
out=dict(status='PASS' if all(q['passed'] for q in checks) else 'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,comparisons=compares,failures=failures,statistics=statistics,runner_gaps=runner_gaps,sensitivity=sensitivity,adaptive_comparisons=adaptive_comparisons,adaptive_disputed_ratio=ratio,proof_sha256=sha(R/'FINAL_STATISTICS_PROOF.md'),driver_sha256=sha(__file__),sources={name:sha(V/name) for name in ['INPUTS.json','RUN.json','REFINEMENT.json','ADAPTIVE.json','ADAPTIVE_MANUFACTURE.json','ADAPTIVE_POWER_MANUFACTURE.json','SUMMARY_initial.json']},scope='Finite auxiliary state samples; four producer printed entries not reproduced; empirical precision only, no fullplane endpoint')
(V/'FINAL_STATISTICS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(checks),'printed',len(compares),'disagreements',len(failures));print([q for q in checks if not q['passed']]);print('adaptive ratio',ratio)
raise SystemExit(out['status']!='PASS')
