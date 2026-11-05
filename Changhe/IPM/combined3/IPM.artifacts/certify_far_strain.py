#!/usr/bin/env python3
"""Actual Candidate013 far strain: (1-chi) Sym Du, whole-plane cover.

Arb radial Taylor models plus Cauchy tails; Arb angular intervals converted
outward to IEEE binary64 interval arrays. Inner region uses the explicitly
identified inherited global strain bound; exterior uses exact asymptotics.
No result is a certificate unless every panel and endpoint check succeeds.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
import time

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
CODE=HERE/'coercivity_residual'
sys.path.insert(0,str(CODE))
import numpy as np
from flint import arb, arb_poly, fmpq as Q, ctx
from fields013 import Evaluator, SOURCE_HASHES, rational_arb, linear_combination
from asymptotics013 import Expansion

E=TRIG=CFG=None

def low(a): return np.nextafter(float(a.lower()),-np.inf)
def high(a): return np.nextafter(float(a.upper()),np.inf)
def down(a): return np.nextafter(a,-np.inf)
def up(a): return np.nextafter(a,np.inf)

def chi(r):
    ell=arb(8).log()/(2*arb.pi().sqrt())
    return (((r/arb(8).sqrt()).log()/ell).erfc())/2

def init(config):
    global E,TRIG,CFG
    CFG=config
    E=Evaluator(config['precision'],max_density_order=0,max_velocity_order=1)
    nt=config['angles']
    TRIG={}
    for kind in ('s','c'):
        for n in range(164):
            vals=[]
            for j in range(nt):
                angle=arb.pi()*(2*j+1)/(4*nt)+arb(0,arb.pi()/(4*nt))
                v=(n*angle).sin() if kind=='s' else (n*angle).cos()
                vals.append((low(v),high(v)))
            TRIG[kind,n]=(np.array([v[0] for v in vals]),np.array([v[1] for v in vals]))

def synth(modes):
    lo=np.zeros(CFG['angles']);hi=np.zeros(CFG['angles'])
    for k,v in modes.items():
        vl,vh=low(v),high(v);tl,th=TRIG[k]
        products=np.array([vl*tl,vl*th,vh*tl,vh*th])
        lo=down(lo+down(products.min(axis=0)))
        hi=up(hi+up(products.max(axis=0)))
    return lo,hi

def panel(index):
    ratio=rational_arb(Q(CFG['ratio']))
    left=rational_arb(Q(CFG['rmin']))*ratio**index
    right=rational_arb(Q(CFG['rmin']))*ratio**(index+1)
    if right>rational_arb(Q(CFG['rmax'])):right=rational_arb(Q(CFG['rmax']))
    r=(left+right)/2;h=(right-left)/2
    assert r>0 and 0<h<r/8
    majors,R=E.mode_majorants(r);z=h/R
    relevant=[('u1',1,0),('u1',0,1),('u2',1,0)]
    magnitude=sum((a for k in relevant for a in majors[k].values()),arb(0))
    # A fixed absolute enclosure tolerance suffices for the supremum test.
    # Its contribution is included mode by mode in the actual cover below.
    degree=16;target=arb('1e-6')
    while magnitude*z**(degree+1)/(1-z)>target and degree<CFG['degree']:
        degree+=8
    assert magnitude*z**(degree+1)/(1-z)<target
    series=E.modes_taylor(r,degree)
    cover={};arg=arb(0,h.abs_upper());tail=z**(degree+1)/(1-z)
    for k in relevant:
        cover[k]={}
        for harmonic,p in series[k].items():
            polynomial=arb_poly(p.coeffs()[:degree+1])
            remainder=(majors[k].get(harmonic,arb(0))*tail).abs_upper()
            cover[k][harmonic]=polynomial(arg)+arb(0,remainder)
    sx=cover['u1',1,0]
    sy=linear_combination((arb(1)/2,cover['u1',0,1]),(arb(1)/2,cover['u2',1,0]))
    xl,xh=synth(sx);yl,yh=synth(sy)
    xa=np.maximum(np.abs(xl),np.abs(xh));ya=np.maximum(np.abs(yl),np.abs(yh))
    s_square=up(up(xa*xa)+up(ya*ya))
    # The cut 1-chi increases with radius; no interval dependency is needed.
    far_upper=high(1-chi(right))
    sf_square=up(up(far_upper*far_upper)*s_square)
    level=Q(CFG['bound']);level2=low(rational_arb(level*level))
    passing=bool(np.all(sf_square<=level2))
    return {'index':index,'degree':degree,'center':r.str(30),'halfwidth':h.str(30),
            'pass':passing,'upper_square_float':float(sf_square.max()),
            'worst_angle':int(np.argmax(sf_square))}

def bindings():
    return {p.name:sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),CODE/'fields013.py',CODE/'asymptotics013.py']}

def assemble(folder):
    cfg=json.loads((folder/'configuration.json').read_text())
    assert cfg['bindings']==bindings()
    ctx.prec=cfg['precision']
    rows={}
    for p in folder.glob('chunk_*.json'):
        rec=json.loads(p.read_text());assert rec['configuration']==cfg
        for r in rec['rows']:
            assert r['index'] not in rows
            rows[r['index']]=r
    assert sorted(rows)==list(range(cfg['panels']))
    level=rational_arb(Q(cfg['bound']))
    inner=rational_arb(Q(137,125))*(1-chi(rational_arb(Q(cfg['rmin']))))
    e=Evaluator(cfg['precision'],max_density_order=0,max_velocity_order=1)
    far=Expansion(e,'far',12)
    ext=far.point_bound('u1',1,0,cfg['rmax'])+(far.point_bound('u1',0,1,cfg['rmax'])+far.point_bound('u2',1,0,cfg['rmax']))/2
    ok=bool(inner<=level and ext<=level and all(r['pass'] for r in rows.values()))
    result={'status':'CERTIFIED_FAR_STRAIN' if ok else 'NOT_CERTIFIED',
            'bound':cfg['bound'],'cut':'1-erfc(log(r/sqrt8)/ell)/2, ell=log8/(2sqrtpi)',
            'configuration':cfg,'inner_upper_arb':str(inner),'exterior_upper_arb':str(ext),
            'failed_panels':[i for i,r in rows.items() if not r['pass']],
            'inherited_input':'||Sym Du_*||op<=137/125 on inner region; original certificate premises retained',
            'scope':'A bound on the actual far strain coefficient only; no complete TIS/closure assertion',
            'finished_utc':datetime.now(timezone.utc).isoformat()}
    (folder/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=4);ap.add_argument('--angles',type=int,default=512)
    ap.add_argument('--precision',type=int,default=384);ap.add_argument('--degree',type=int,default=120)
    ap.add_argument('--ratio',default='33/32');ap.add_argument('--rmin',default='5/2')
    ap.add_argument('--rmax',default='100000000');ap.add_argument('--bound',default='1/2')
    ap.add_argument('--chunk',type=int,default=16);ap.add_argument('--assemble',action='store_true')
    args=ap.parse_args()
    if args.assemble:return assemble(args.output)
    args.output.mkdir(parents=True,exist_ok=True)
    ratio,rmin,rmax=Q(args.ratio),Q(args.rmin),Q(args.rmax)
    count=math.ceil(math.log(float(rmax/rmin))/math.log(float(ratio)))
    assert rmin*ratio**(count-1)<rmax<=rmin*ratio**count
    cfg={'precision':args.precision,'degree':args.degree,'angles':args.angles,'ratio':args.ratio,
         'rmin':args.rmin,'rmax':args.rmax,'bound':args.bound,'panels':count,
         'bindings':bindings(),'source_hashes':SOURCE_HASHES}
    cp=args.output/'configuration.json'
    if cp.exists():assert json.loads(cp.read_text())==cfg
    else:cp.write_text(json.dumps(cfg,indent=2)+'\n')
    start=time.monotonic()
    with ProcessPoolExecutor(args.workers,initializer=init,initargs=(cfg,)) as pool:
        for first in range(0,count,args.chunk):
            indices=list(range(first,min(first+args.chunk,count)))
            path=args.output/f'chunk_{indices[0]:05}_{indices[-1]:05}.json'
            if path.exists():
                old=json.loads(path.read_text());assert old['configuration']==cfg
                assert [r['index'] for r in old['rows']]==indices
                continue
            rows=list(pool.map(panel,indices,chunksize=1))
            path.write_text(json.dumps({'configuration':cfg,'rows':rows,
                'finished_utc':datetime.now(timezone.utc).isoformat()},indent=2)+'\n')
            print('panels',indices[-1]+1,'of',count,'failed',sum(not r['pass'] for r in rows),
                  'seconds',time.monotonic()-start,flush=True)
    assemble(args.output)

if __name__=='__main__':main()
