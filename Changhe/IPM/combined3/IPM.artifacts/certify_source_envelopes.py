#!/usr/bin/env python3
"""Whole-plane radial gradient envelopes for Gaussian near-source prices."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
import json,math,sys,time
from pathlib import Path
from flint import arb,arb_poly,fmpq as Q,ctx
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'coercivity_residual'))
from fields013 import Evaluator,rational_arb,SOURCE_HASHES
from asymptotics013 import Expansion
E=CFG=None

def setup(cfg):
    global E,CFG
    CFG=cfg
    E=Evaluator(cfg['precision'],max_density_order=1,max_velocity_order=0)

def panel(index):
    ratio=rational_arb(Q(CFG['ratio']))
    left=rational_arb(Q(CFG['rmin']))*ratio**index
    right=rational_arb(Q(CFG['rmin']))*ratio**(index+1)
    if right>arb(CFG['rmax']):right=arb(CFG['rmax'])
    r=(left+right)/2;h=(right-left)/2
    majorants,R=E.mode_majorants(r);z=h/R
    keys=[('rho',1,0),('rho',0,1)]
    magnitude=sum((a for k in keys for a in majorants[k].values()),arb(0))
    degree=16
    while magnitude*z**(degree+1)/(1-z)>arb('1e-7'):
        degree+=8
    assert degree<=CFG['max_degree']
    modes=E.modes_taylor(r,degree)
    argument=arb(0,h.abs_upper());tail=z**(degree+1)/(1-z)
    bounds=[]
    for key in keys:
        total=arb(0)
        for harmonic,series in modes[key].items():
            value=arb_poly(series.coeffs()[:degree+1])(argument)
            remainder=majorants[key].get(harmonic,arb(0))*tail
            total+=value.abs_upper()+remainder.abs_upper()
        bounds.append(total)
    B=(bounds[0]**2+bounds[1]**2).sqrt()
    return {'index':index,'degree':degree,
            'B_upper':B.str(70),'rB_upper':(right*B).str(70)}

def bindings():
    files=[Path(__file__),HERE/'coercivity_residual/fields013.py',
           HERE/'coercivity_residual/asymptotics013.py']
    return {str(p.relative_to(HERE)):sha256(p.read_bytes()).hexdigest()
            for p in files}

def maximum(values):
    return max((v.abs_upper() for v in values))

def assemble(folder):
    cfg=json.loads((folder/'configuration.json').read_text())
    assert cfg['bindings']==bindings();ctx.prec=cfg['precision']
    rows={}
    for p in sorted(folder.glob('chunk_*.json')):
        d=json.loads(p.read_text());assert d['configuration']==cfg
        for r in d['rows']:
            assert r['index'] not in rows;rows[r['index']]=r
    assert sorted(rows)==list(range(cfg['panels']))
    e=Evaluator(cfg['precision'],max_density_order=1,max_velocity_order=0)
    origin=Expansion(e,'origin',12);far=Expansion(e,'far',12)
    r0=rational_arb(Q(cfg['rmin']));r1=arb(cfg['rmax'])
    Bo=(origin.point_bound('rho',1,0,r0)**2+
        origin.point_bound('rho',0,1,r0)**2).sqrt()
    Bf=(far.point_bound('rho',1,0,r1)**2+
        far.point_bound('rho',0,1,r1)**2).sqrt()
    a0=maximum([Bo,Bf]+[arb(r['B_upper']) for r in rows.values()])
    core_rB=maximum([r0*Bo]+[arb(r['rB_upper']) for r in rows.values()])
    outrows=[]
    for Rint in [10000,30000,100000]:
        endpoint=arb(2*Rint);vs=[]
        for i,j in [(1,0),(0,1)]:
            total=arb(0)
            for (kind,n,power),a in far.field('rho',i,j).items():
                exponent=power+1
                radius=endpoint if exponent>=0 else r1
                total+=arb(abs(a))*radius**rational_arb(exponent)
            for a,power in far.remainder_terms('rho',i,j,r1):
                exponent=power+1
                radius=endpoint if exponent>=0 else r1
                total+=a*radius**rational_arb(exponent)
            vs.append(total)
        a1=maximum([core_rB,(vs[0]**2+vs[1]**2).sqrt()])
        outrows.append({'cut_R':Rint,'a0':a0.str(75),'a1':a1.str(75)})
    result={'status':'CERTIFIED_RADIAL_NEAR_SOURCE_ENVELOPES',
            'configuration':cfg,'a0_global_gradient':a0.str(75),
            'core_r_gradient':core_rB.str(75),
            'origin_gradient_bound':Bo.str(75),
            'far_gradient_bound':Bf.str(75),'rows':outrows,
            'meaning':'For b_near=(1-eta_R)*grad rho, exists radial '
                      'a>=|b_near| with sup a<=a0, sup r*a<=a1; '
                      'eta=1 for r>=2R. No complete energy claim.',
            'finished_utc':datetime.now(timezone.utc).isoformat()}
    (folder/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=3)
    ap.add_argument('--chunk',type=int,default=12)
    ap.add_argument('--assemble',action='store_true')
    args=ap.parse_args()
    if args.assemble:return assemble(args.output)
    ratio=Q(33,32);lo=Q(1,100000);hi=Q(1000)
    count=math.ceil(math.log(float(hi/lo))/math.log(float(ratio)))
    assert lo*ratio**(count-1)<hi<=lo*ratio**count
    cfg={'precision':384,'max_degree':144,'ratio':str(ratio),
         'rmin':str(lo),'rmax':str(hi),'panels':count,
         'bindings':bindings(),'source_hashes':SOURCE_HASHES}
    args.output.mkdir(parents=True,exist_ok=True)
    cp=args.output/'configuration.json'
    if cp.exists():assert json.loads(cp.read_text())==cfg
    else:cp.write_text(json.dumps(cfg,indent=2)+'\n')
    start=time.monotonic()
    with ProcessPoolExecutor(args.workers,initializer=setup,initargs=(cfg,)) as pool:
        for first in range(0,count,args.chunk):
            indices=list(range(first,min(first+args.chunk,count)))
            path=args.output/f'chunk_{indices[0]:05}_{indices[-1]:05}.json'
            if path.exists():
                old=json.loads(path.read_text());assert old['configuration']==cfg
                assert [r['index'] for r in old['rows']]==indices
                continue
            rows=list(pool.map(panel,indices,chunksize=1))
            path.write_text(json.dumps({'configuration':cfg,'rows':rows},
                                      indent=2)+'\n')
            print('source envelopes',indices[-1]+1,'/',count,
                  'seconds',time.monotonic()-start,flush=True)
    assemble(args.output)

if __name__=='__main__':main()
