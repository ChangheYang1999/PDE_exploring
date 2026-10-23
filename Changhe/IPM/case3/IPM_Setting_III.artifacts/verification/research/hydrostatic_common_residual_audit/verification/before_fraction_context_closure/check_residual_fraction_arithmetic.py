"""Read-only reconstruction of result287 arrays. Never evaluates an inverse."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,math,traceback
import numpy as np
from rational_residual_arithmetic import exact,inspect,frac,json_safe,point_matches
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];groups=[];bindings={};current_context={}
def ck(name,b,evidence=None):
    checks.append(dict(name=name,passed=bool(b),evidence=evidence))
    if not b:raise AssertionError((name,evidence))
def bind(p,h=None):
    p=Path(p);got=sha(p)
    if h is not None:ck('hash '+str(p),got==h)
    bindings[str(p)]=got

def manufactures():
    # Expected values below were derived in FRACTION_REVIEW_RESOLUTION_PROOF.
    nb=math.sqrt(2249/512)+5/16
    generic=dict(W=[13/8,1/4],parts=[13/32,5/16],Rh=13/32,Nf=33/32,Nv=43/32,Nbound=nb,Rf=13/33,Rv=13/43,Rbound=(13/32)/nb)
    horizontal=dict(W=[9/4,0],parts=[0,0],Rh=0,Nf=0,Nv=0,Nbound=9/4,Rf=None,Rv=None,Rbound=0)
    origin=dict(W=[0,0],parts=[0,0],Rh=0,Nf=0,Nv=0,Nbound=0,Rf=None,Rv=None,Rbound=None)
    vertical=dict(W=[0,5/4],parts=[0,15/8],Rh=9/8,Nf=21/8,Nv=15/8,Nbound=21/8,Rf=3/7,Rv=3/5,Rbound=3/7)
    cases=[('generic',.5,.25,3,[5/16,1/4,5/4,0],[1/8,-1/2],generic),('horizontal',1,0,2,[0,0,1,0],[1/4,0],horizontal),('origin',0,0,2,[0,0,1,0],[0,0],origin),('vertical',0,.5,3,[3/4,0,3/2,0],[0,-1/4],vertical)]
    for label,x,y,c,j,v,st in cases:
        d=inspect(x,y,c,j,v,st);ck('hand-derived manufacture '+label,d['passed'],d['conditions'])
    z=exact(.5,.25,2,[5/16,1/4,5/4,0],[1/8,-1/2]);ck('earlier dyadic Rh',z['Rh']==frac(-1)/32);ck('earlier dyadic Nf',z['Nf']==frac(19)/32);ck('earlier dyadic Nv',z['Nv']==frac(43)/32)
    x,y,c,j,v=.5,.25,3,[5/16,1/4,5/4,0],[1/8,-1/2]
    for name,key,value in [('wrong Nv','Nv',71/32),('wrong Rf','Rf',generic['Rf']+1e-6),('wrong Nbound','Nbound',nb+1e-6),('missing-ratio encoding','Rf',None),('NaN ratio','Rf',math.nan),('negative ratio','Rv',-1),('wrong W','W',[13/8+1e-6,1/4]),('wrong parts','parts',[13/32,5/16+1e-6])]:
        bad=dict(generic);bad[key]=value;ck('reject '+name,not inspect(x,y,c,j,v,bad)['passed'])
    for key in ['W','parts']:
        bad=dict(generic);del bad[key]
        try:inspect(x,y,c,j,v,bad);rejected=False
        except ValueError:rejected=True
        ck('reject missing fixed '+key,rejected)
    ad={k:v for k,v in generic.items()if k not in ['W','parts']};ck('adaptive explicit schema',inspect(x,y,c,j,v,ad,require_wp=False)['passed'])
    for key,value in [('Rf',0.),('Rh',1e-6),('Nf',1e-6)]:
        bad=dict(horizontal);bad[key]=value;ck('reject horizontal '+key,not inspect(1,0,2,[0,0,1,0],[1/4,0],bad)['passed'])
    bad=dict(origin);bad['Rh']=1.;failed=inspect(0,0,2,[0,0,1,0],[0,0],bad)
    ck('zero-budget failed arithmetic',not failed['passed'] and math.isinf(failed['scores']['Rh']))
    serialized=json.dumps(json_safe(failed),allow_nan=False);ck('zero-budget diagnostic serialization',json.loads(serialized)['scores']['Rh']=='inf')
    for val in [math.inf,math.nan]:
        try:inspect(val,y,c,j,v,generic);rejected=False
        except ValueError:rejected=True
        ck('reject nonfinite input '+repr(val),rejected)
    first=[1e-3,0,1e-3,0];ck('reporting coordinate origin-ring',point_matches(0,first));ck('reject permuted coordinate',not point_matches(1,first));ck('reject changed radius',not point_matches(0,[1e-3,0,1.01e-3,0]));ck('reject relabelled index',not point_matches(0,[1e-3,0,1e-3,1]))
    ck('reject residual row permutation',not inspect(0,.5,3,[3/4,0,3/2,0],[0,-1/4],generic)['passed'])

def audit_group(label,records,count,require_wp=True):
    categories={k:0 for k in ['stored_data','identity','domain','parity']}
    n=0;condition_count=0;zeros={k:0 for k in ['Nf','Nv','Nbound']};maxima={}
    for i,x,y,c,j,v,stored in records:
        current_context.clear();current_context.update(group=label,index=int(i),x=float(x),y=float(y))
        z=inspect(x,y,c,j,v,stored,require_wp=require_wp)
        if not z['passed']:ck(label+' point '+str(i),False,z)
        n+=1;condition_count+=len(z['conditions'])
        for category in z['categories'].values():categories[category]+=1
        for k,vv in z['zero_denominators'].items():zeros[k]+=int(vv)
        for k,vv in z['scores'].items():
            if k not in maxima or vv>maxima[k]['score']:maxima[k]=dict(score=vv,index=i)
    ck(label+' complete',n==count)
    ck(label+' all point conditions',condition_count>0)
    groups.append(dict(label=label,points=n,point_conditions_passed=condition_count,conditions_by_category=categories,zero_denominators=zeros,maximum_budget_fractions=maxima))

def main(mode):
    manufactures();bind(__file__);bind('independent_code/rational_residual_arithmetic.py');bind(R/'FRACTION_ARITHMETIC_PROOF.md');bind(R/'FRACTION_REVIEW_RESOLUTION_PROOF.md');bind(R/'FRACTION_OUTPUT_PROOF.md')
    if mode=='manufactures':return
    manifest=json.loads((V/'FRACTION_INPUT_BINDINGS.json').read_text());bind(V/'FRACTION_INPUT_BINDINGS.json','614137e0948c5c5ee3aa770d4411756cceb9467417812359f25721b19faefde8')
    for item in manifest['files']:bind(item['path'],item['sha256'])
    p=V/'RUN.json';d=json.loads(p.read_text());bind(p,'69b33cd7f0248f43b168fcd10f35cf322159eb243707a457229022321233fa32');ck('run complete',d['status']=='PASS' and all(x['passed']for x in d['checks']))
    bind(V/'POINTS.npz',d['points_sha256']);pts=np.load(V/'POINTS.npz')['points'];ck('333 point schema',pts.shape==(333,4) and pts.dtype==np.dtype('float64'))
    ck('all independent reporting coordinates',all(point_matches(i,p)for i,p in enumerate(pts)))
    for name,h in d['modules'].items():bind(Path('independent_code')/name,h)
    bind('independent_code/audit_hydrostatic_common_residuals.py',d['driver_sha256']);bind(R/'verification/EXECUTED_BASE_PROTOCOL.md',d['proof_sha256']);bind(V/'INPUTS.json',d['input_sha256'])
    inp=json.loads((V/'INPUTS.json').read_text())
    for item in inp['files']+[s[k]for s in inp['states']for k in ['state','export']]:bind(item['path'],item['sha256'])
    expected={'hsG_c2.0_N96_log':(2,96,24),'hsG_c2.0_N128_log_cont':(2,128,32),'hsG_c2.0_N160_log':(2,160,40),'hsG_c2.0_N192_log':(2,192,48),'hsG_c3.0_N64_log':(3,64,16),'hsG_c3.0_N96_log':(3,96,24),'hsG_c3.0_N128_log':(3,128,32)}
    ck('exact unique state set',len(d['states'])==len(expected) and {s['tag']for s in d['states']}==set(expected))
    for state in d['states']:ck(state['tag']+' parameter metadata',(state['c'],state['N'],state['M'])==expected[state['tag']])
    if mode=='fixed':
        ck('seven states',len(d['states'])==7)
        for s in d['states']:
            ck(s['tag']+' complete',s['status']=='DONE');ck(s['tag']+' three exact configurations',[(a['order'],a['tail_order'],a['split'])for a in s['levels']]==[(32,96,16),(48,160,64),(64,192,128)])
            for a in s['levels']:
                bind(a['path'],a['sha256']);data=dict(np.load(a['path']));shapes={'jets':(333,4),'velocity':(333,2),'auxiliary':(333,5),'W':(333,2),'parts':(333,2),**{k:(333,)for k in ['Rh','Nf','Nv','Nbound','Rf','Rv','Rbound']}};ck(s['tag']+str(a['order'])+' exact schema',set(data)==set(shapes) and all(data[k].shape==shape and data[k].dtype==np.dtype('float64')for k,shape in shapes.items()))
                records=((i,*pts[i,:2],s['c'],data['jets'][i],data['velocity'][i],{k:v[i]for k,v in data.items() if k not in ['jets','velocity','auxiliary']})for i in range(333))
                audit_group(s['tag']+'_order'+str(a['order']),records,333)
        ck('6993 fixed points',sum(g['points']for g in groups)==6993)
    else:
        p=V/'ADAPTIVE.json';a=json.loads(p.read_text());bind(p);ck('adaptive complete',a['status']=='PASS'and all(x['passed']for x in a['checks']));bind(V/'SUMMARY.json',a['summary_sha256']);bind(V/'RUN.json',a['run_sha256']);bind(V/'POINTS.npz',a['points_sha256'])
        ck('adaptive same immutable inputs',a['input_sha256']==d['input_sha256']);fixed={t['tag']:t for t in d['states']}
        ck('adaptive exact state set',len(a['states'])==7 and {s['tag']for s in a['states']}==set(expected));selection={s['tag']:s['indices']for s in a['selection']}
        for s in a['states']:
            ck(s['tag']+' complete',s['status']=='DONE');ck(s['tag']+' adaptive c',s['c']==expected[s['tag']][0]);ck(s['tag']+' adaptive same source parameters',s['p']==fixed[s['tag']]['p'] and (fixed[s['tag']]['N'],fixed[s['tag']]['M'])==expected[s['tag']][1:]);ids=[r['index']for r in s['points']];ck(s['tag']+' exact selection',ids==selection[s['tag']])
            for r in s['points']:ck(s['tag']+' point coordinate '+str(r['index']),[r['x'],r['y'],r['radius'],r['angle_index']]==list(pts[r['index']]))
            records=((r['index'],r['x'],r['y'],s['c'],r['jet'],r['V'],r)for r in s['points'])
            audit_group(s['tag']+'_adaptive',records,len(ids),require_wp=False)
        ck('295 adaptive points',sum(g['points']for g in groups)==295)


def write_gate(path,out):
    text=json.dumps(json_safe(out),indent=2,allow_nan=False)+'\n'
    if path.exists():
        old=path.read_bytes();archive=path.with_name(path.stem+'.previous.'+hashlib.sha256(old).hexdigest()+'.json')
        if archive.exists():assert archive.read_bytes()==old
        else:
            with archive.open('xb') as f:f.write(old)
    if out['status']!='PASS':
        failed=path.with_name(path.stem+'.failed.'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
        with failed.open('x') as f:f.write(text)
    path.write_text(text)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['manufactures','fixed','adaptive']);args=parser.parse_args();started=datetime.now(timezone.utc).isoformat();status='FAIL';exception=None
    try:main(args.mode);status='PASS'
    except Exception as exc:
        exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc(),context=dict(current_context));traceback.print_exc()
    out=dict(status=status,exception=exception,started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,groups=groups,bindings=bindings,scope='Exact arithmetic on represented finite inputs; no error bound on inverse, jets or continuum residual.')
    path=V/('FRACTION_'+args.mode.upper()+'.json');write_gate(path,out);print(out['status'],out['count'],sum(g['points']for g in groups),sum(g['point_conditions_passed']for g in groups),out['finished_utc']);raise SystemExit(0 if status=='PASS' else 1)
