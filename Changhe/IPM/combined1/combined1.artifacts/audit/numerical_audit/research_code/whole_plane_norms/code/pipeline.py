"""Bounded, restartable stages for independent whole-plane norm audits."""
from pathlib import Path
from datetime import datetime,timezone
from flint import fmpq,fmpq_poly,ctx
import sys,json,gzip,hashlib,time,argparse
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/exact_negative_norm/code'))
from radial import Radial
from norms import derivative,norm,evaluate_derivative
from packed_residual import residual_sine
from negative import negative_norm
DATA=ROOT/'research/whole_plane_norms/data'
OUT=ROOT/'research/whole_plane_norms/verification'

def source(name):
    if name.startswith('C1-N1-'):
        return ROOT/f'research/candidate_audits/data/{name}/canonical.json'
    return ROOT/(f'research/baseline/data/{name}_independent.json' if name.startswith('state') else f'research/refit_audit/data/{name}_canonical.json')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def save(name,order,D,path):
    rows=[]
    for (d,nx),A in sorted(D.items()):
        if d!=order:continue
        for (ell,kind,n),P in sorted(A.items()):
            rows.append({'d':d,'nx':nx,'ell':ell,'kind':kind,'n':n,'denominator':str(P.denom()),'numerator':[str(v) for v in P.numer()]})
    output={'schema':'N4-radial-polynomial-v1','candidate':name,'source_sha256':digest(source(name)),
            'utc':now(),'order':order,'rows':rows}
    temp=path.with_suffix('.tmp')
    with gzip.open(temp,'wt',compresslevel=2) as f:json.dump(output,f,separators=(',',':'))
    temp.replace(path)
    print('saved',path.name,'rows',len(rows),'bytes',path.stat().st_size,flush=True)
def load(name,order):
    path=DATA/f'{name}_D{order}.json.gz'
    with gzip.open(path,'rt') as f:obj=json.load(f)
    assert obj['schema']=='N4-radial-polynomial-v1' and obj['source_sha256']==digest(source(name))
    D={}
    for row in obj['rows']:
        d,nx,ell,kind,n=(row[k] for k in ('d','nx','ell','kind','n'))
        P=fmpq_poly([int(v) for v in row['numerator']])/fmpq(row['denominator'])
        D.setdefault((d,nx),{})[ell,kind,n]=P
    return D

def run(args):
    start=time.monotonic();ctx.prec=args.bits;name=args.candidate;path=source(name)
    raw=json.loads(path.read_text());delta=1-1/fmpq(raw['cl'])
    print(now(),args.stage,name,args.label,flush=True)
    if args.stage=='assemble':
        model=Radial(path);print('potential derivatives ready',time.monotonic()-start,flush=True)
        assemble=residual_sine
        if args.packing=='tight':
            from packed_tight import residual_sine as assemble
            certificate=json.loads((OUT/'tight_product_check.json').read_text())
            assert certificate['exact_coefficient_agreement']
            assert certificate['product_code_sha256']==digest(Path(__file__).with_name('packed_tight.py'))
        A=assemble(model,True)
        D={(0,0):{(h+1,'s',n):P for (h,n),P in A.items()}}
        checks=[]
        for x,y in [('1/2','1/2'),('0','1'),('3','4'),('6','8')]:
            a=evaluate_derivative(D[0,0],0,model,x,y);b=model.evaluate(x,y)['residual']
            assert a.overlaps(b),(x,y,a,b)
            checks.append({'x':x,'y':y,'residual':a.str(50),'direct_overlap':True})
        save(name,0,D,DATA/f'{name}_D0.json.gz')
        (OUT/f'{name}_assembly.json').write_text(json.dumps({'utc':now(),'source_sha256':digest(path),
            'polynomial_sha256':digest(DATA/f'{name}_D0.json.gz'),'fieldchecks':checks,
            'packing':args.packing,'code_sha256':digest(Path(__file__)),
            'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
    elif args.stage=='derivatives':
        for d in range(args.max_order):
            target=DATA/f'{name}_D{d+1}.json.gz'
            if target.exists():continue
            D=load(name,d);out={}
            for nx in range(d+2):
                out[d+1,nx]=derivative(D[d,0],d,'y',delta) if nx==0 else derivative(D[d,nx-1],d,'x',delta)
            for nx in range(1,d+1):assert out[d+1,nx]==derivative(D[d,nx],d,'y',delta)
            save(name,d+1,out,target)
            print('order',d+1,'seconds',time.monotonic()-start,flush=True)
    else:
        params={'G0':(0,False,False,False),'G1':(1,False,False,False),'P2':(2,True,False,False),
                'Q3':(3,True,False,False),'rF_proxy':(0,False,True,False),'angular_Hminus1_proxy':(0,False,True,True)}
        if args.stage=='negative':
            D=load(name,0);polynomial_hash=digest(DATA/f'{name}_D0.json.gz')
            result=negative_norm(D,delta,checkpoint=DATA/f'{name}_negative_{polynomial_hash[:16]}',max_seconds=500);label='Hminus1'
        else:
            d,w,r,h=params[args.label];D=load(name,d)
            result=norm(D,d,delta,w,r,args.degree,h);label=args.label
        result.update({'candidate':name,'component':label,'utc':now(),'source_sha256':digest(path),
                      'precision_bits':ctx.prec,'stage_elapsed_seconds':time.monotonic()-start})
        (OUT/f'{name}_{label}.json').write_text(json.dumps(result,indent=2)+'\n')
        print(label,result['status'],result.get('norm_lower_ball'),result.get('norm_upper_ball'),flush=True)
    print('completed seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('stage',choices=['assemble','derivatives','norm','negative']);p.add_argument('--packing',choices=['global','tight'],default='global')
    p.add_argument('--label',default='G0');p.add_argument('--bits',type=int,default=768);p.add_argument('--degree',type=int,default=112);p.add_argument('--max-order',type=int,choices=[1,2,3],default=3)
    run(p.parse_args())
