#!/usr/bin/env python3
"""Independent actual-source M>=beta certificate, adaptive polar cover."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
import json,math,sys,time
from pathlib import Path
import numpy as np
from flint import arb,arb_poly,fmpq as Q,ctx
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'coercivity_residual'))
from fields013 import Evaluator,rational_arb,C,SOURCE_HASHES
from asymptotics013 import Expansion
E=CFG=None;TRIG={}
def down(x):return np.nextafter(x,-np.inf)
def up(x):return np.nextafter(x,np.inf)
def iv(x):return down(float(x.lower())),up(float(x.upper()))
def add(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=np.array([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
    return down(p.min(axis=0)),up(p.max(axis=0))
def square_hi(a):return up(np.maximum(a[0]*a[0],a[1]*a[1]))
def setup(cfg):
    global E,CFG
    CFG=cfg;E=Evaluator(cfg['precision'],1,1)
def trig(nt):
    if nt in TRIG:return TRIG[nt]
    out={}
    for kind in ['s','c']:
        for n in range(164):
            v=[]
            for j in range(nt):
                angle=arb.pi()*(2*j+1)/(4*nt)+arb(0,arb.pi()/(4*nt))
                v.append(iv((n*angle).sin() if kind=='s' else (n*angle).cos()))
            out[kind,n]=(np.array([p[0] for p in v]),
                         np.array([p[1] for p in v]))
    TRIG[nt]=out
    return out
def synth(modes,table,nt):
    a=np.zeros(nt);b=np.zeros(nt)
    for harmonic,value in modes.items():
        lo,hi=mul(iv(value),table[harmonic]);a=down(a+lo);b=up(b+hi)
    return a,b
def cover(left,right,nt):
    r=(left+right)/2;h=(right-left)/2
    majorants,R=E.mode_majorants(r);z=h/R
    keys=[('rho',1,0),('rho',0,1),('u1',0,0),('u2',0,0),
          ('u1',1,0),('u1',0,1),('u2',1,0)]
    mag=sum((v for k in keys for v in majorants[k].values()),arb(0))
    degree=16
    while mag*z**(degree+1)/(1-z)>arb('1e-8'):
        degree+=8
    assert degree<=CFG['max_degree']
    modes=E.modes_taylor(r,degree);argument=arb(0,h.abs_upper())
    factor=z**(degree+1)/(1-z);table=trig(nt);values={}
    for key in keys:
        radial={}
        for harmonic,p in modes[key].items():
            rem=(majorants[key].get(harmonic,arb(0))*factor).abs_upper()
            radial[harmonic]=arb_poly(p.coeffs()[:degree+1])(argument)+arb(0,rem)
        values[key]=synth(radial,table,nt)
    rb=r+arb(0,h.abs_upper());r2=rb*rb;c=rational_arb(C);q=arb(21)/10
    aW=add(iv(c*r2/(arb(1)/4+r2)),
           mul(iv(rb/(arb(1)/4+r2)),
               add(mul(values['u1',0,0],table['c',1]),
                   mul(values['u2',0,0],table['s',1]))))
    base=add(iv(c+1-q*c-rational_arb(Q(CFG['beta']))),aW)
    aa=add(sub(base,mul(iv(q),values['u1',1,0])),values['rho',0,1])
    dd=add(base,mul(iv(q),values['u1',1,0]))
    bb=sub(mul(iv(-q/2),add(values['u1',0,1],values['u2',1,0])),
           mul(iv(arb(1)/2),values['rho',1,0]))
    determinant=down(mul(aa,dd)[0]-square_hi(bb))
    finite=all(np.all(np.isfinite(v)) for v in [aa[0],dd[0],determinant])
    assert finite
    ok=bool(np.all(aa[0]>=0) and np.all(dd[0]>=0) and
            np.all(determinant>=0))
    return {'pass':ok,'degree':degree,'angular_arcs':nt,
            'min_aa':float(aa[0].min()),'min_dd':float(dd[0].min()),
            'min_determinant':float(determinant.min())}
def panel(index):
    ratio=rational_arb(Q(CFG['ratio']))
    left=rational_arb(Q(CFG['rmin']))*ratio**index
    right=rational_arb(Q(CFG['rmin']))*ratio**(index+1)
    if right>arb(CFG['rmax']):right=arb(CFG['rmax'])
    leaves=[]
    def visit(lo,hi,path):
        nt=CFG['angles'];row=cover(lo,hi,nt)
        if not row['pass'] and len(path)>=2:
            nt*=2;row=cover(lo,hi,nt)
        if not row['pass'] and len(path)<CFG['max_depth']:
            mid=(lo+hi)/2
            visit(lo,mid,path+'0');visit(mid,hi,path+'1')
        else:
            leaves.append({'path':path,**row})
    visit(left,right,'')
    return {'index':index,'pass':all(r['pass'] for r in leaves),
            'leaves':leaves}
def bindings():
    files=[Path(__file__),HERE/'coercivity_residual/fields013.py',
           HERE/'coercivity_residual/asymptotics013.py']
    return {str(p.relative_to(HERE)):sha256(p.read_bytes()).hexdigest()
            for p in files}
def scaled_bound(exp,name,i,j,R,shift):
    total=arb(0)
    for (kind,n,p),a in exp.field(name,i,j).items():
        assert p+shift>=0 if exp.side=='origin' else p+shift<0
        total+=arb(abs(a))*R**rational_arb(p+shift)
    for a,p in exp.remainder_terms(name,i,j,R):
        assert p+shift>=0 if exp.side=='origin' else p+shift<0
        total+=a*R**rational_arb(p+shift)
    return total
def assemble(folder):
    cfg=json.loads((folder/'configuration.json').read_text())
    assert cfg['bindings']==bindings();ctx.prec=cfg['precision'];rows={}
    for file in sorted(folder.glob('chunk_*.json')):
        d=json.loads(file.read_text());assert d['configuration']==cfg
        for row in d['rows']:
            assert row['index'] not in rows;rows[row['index']]=row
            paths={leaf['path'] for leaf in row['leaves']}
            assert len(paths)==len(row['leaves'])
            def complete(prefix):
                if prefix in paths:
                    assert not any(p.startswith(prefix) and p!=prefix for p in paths)
                    return
                assert len(prefix)<cfg['max_depth']
                complete(prefix+'0');complete(prefix+'1')
            complete('')
    assert sorted(rows)==list(range(cfg['panels']))
    e=Evaluator(cfg['precision'],1,1)
    origin=Expansion(e,'origin',12);far=Expansion(e,'far',12)
    c=rational_arb(C);q=arb(21)/10;r0=arb(cfg['rmin']);rF=arb(cfg['rmax'])
    by0=sum((arb(a) for (kind,n,p),a in origin.field('rho',0,1).items()
             if p==0),arb(0))
    d0=c-1;base=c+1-q*c
    M0=min((base-q*d0+by0).lower(),(base+q*d0).lower())
    u0=(scaled_bound(origin,'u1',0,0,r0,-1)**2+
        scaled_bound(origin,'u2',0,0,r0,-1)**2).sqrt()
    error=4*r0*r0*(c+u0)
    error+=q*(origin.point_bound('u1',1,0,r0,True)+
              (origin.point_bound('u1',0,1,r0)+
               origin.point_bound('u2',1,0,r0))/2)
    error+=origin.point_bound('rho',1,0,r0)+origin.point_bound('rho',0,1,r0,True)
    inner=M0-error
    uf=(scaled_bound(far,'u1',0,0,rF,-1)**2+
        scaled_bound(far,'u2',0,0,rF,-1)**2).sqrt()
    sf=far.point_bound('u1',1,0,rF)+(
        far.point_bound('u1',0,1,rF)+far.point_bound('u2',1,0,rF))/2
    bf=(far.point_bound('rho',1,0,rF)**2+
        far.point_bound('rho',0,1,rF)**2).sqrt()
    outer=1+(2-q)*c-c/(1+4*rF*rF)-uf-q*sf-bf
    beta=rational_arb(Q(cfg['beta']))
    passed=bool(inner>=beta and outer>=beta and
                all(r['pass'] for r in rows.values()))
    result={'status':'CERTIFIED_ACTUAL_MATRIX' if passed else 'MATRIX_NOT_CERTIFIED',
            'configuration':cfg,'origin_lower':inner.str(80),
            'exterior_lower':outer.str(80),
            'failed_base_panels':[i for i,r in rows.items() if not r['pass']],
            'total_leaves':sum(len(r['leaves']) for r in rows.values()),
            'finished_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Actual fixed Candidate013 pointwise M only. '
                    'No inherited numerical containment or balanced-root '
                    'premise used; exact source identities remain explicit. '
                    'No full stationary existence claim.'}
    (folder/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=3);ap.add_argument('--chunk',type=int,default=9)
    ap.add_argument('--assemble',action='store_true')
    args=ap.parse_args()
    if args.assemble:return assemble(args.output)
    ratio=Q(33,32);lo=Q(1,100000);hi=Q(10000000)
    count=math.ceil(math.log(float(hi/lo))/math.log(float(ratio)))
    assert lo*ratio**(count-1)<hi<=lo*ratio**count
    cfg={'precision':384,'max_degree':144,'ratio':str(ratio),
         'rmin':str(lo),'rmax':str(hi),'beta':'7/10','panels':count,
         'angles':1024,'max_depth':8,'bindings':bindings(),
         'source_hashes':SOURCE_HASHES}
    args.output.mkdir(parents=True,exist_ok=True)
    cp=args.output/'configuration.json'
    if cp.exists():assert json.loads(cp.read_text())==cfg
    else:cp.write_text(json.dumps(cfg,indent=2)+'\n')
    start=time.monotonic()
    with ProcessPoolExecutor(args.workers,initializer=setup,initargs=(cfg,)) as pool:
        for first in range(0,count,args.chunk):
            indices=list(range(first,min(first+args.chunk,count)))
            p=args.output/f'chunk_{indices[0]:05}_{indices[-1]:05}.json'
            if p.exists():
                d=json.loads(p.read_text());assert d['configuration']==cfg
                assert [r['index'] for r in d['rows']]==indices
                continue
            rows=list(pool.map(panel,indices,chunksize=1))
            p.write_text(json.dumps({'configuration':cfg,'rows':rows},
                                   indent=2)+'\n')
            print('matrix',indices[-1]+1,'/',count,
                  'failed',sum(not r['pass'] for r in rows),
                  'leaves',sum(len(r['leaves']) for r in rows),
                  'seconds',time.monotonic()-start,flush=True)
    assemble(args.output)
if __name__=='__main__':main()
