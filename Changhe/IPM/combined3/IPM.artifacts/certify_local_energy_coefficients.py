#!/usr/bin/env python3
"""Actual whole-plane coefficient envelopes for the joint local Q identity."""
import argparse,json,math,sys,time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
import numpy as np
from flint import arb,arb_poly,ctx,fmpq as Q
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'coercivity_residual'))
from fields013 import Evaluator,rational_arb,SOURCE_HASHES,C
from asymptotics013 import Expansion
import certify_actual_matrix as MI
E=CFG=None
def setup(cfg):
    global E,CFG
    CFG=cfg;E=Evaluator(cfg['precision'],3,2)
def bindings():
    files=[Path(__file__),HERE/'certify_actual_matrix.py',
           HERE/'coercivity_residual/fields013.py',
           HERE/'coercivity_residual/asymptotics013.py']
    return {str(p.relative_to(HERE)):sha256(p.read_bytes()).hexdigest()
            for p in files}
def point_panel(left,right,path):
    r=(left+right)/2;h=(right-left)/2
    majorants,R=E.mode_majorants(r);z=h/R
    keys=[('rho',i,d-i) for d in [1,2,3] for i in range(d+1)]
    keys+=[('u1',1,0),('u1',0,1),('u2',1,0)]
    keys +=[(name,i,2-i) for name in ['u1','u2'] for i in range(3)]
    magnitude=sum((a for key in keys for a in majorants[key].values()),arb(0))
    degree=16
    while magnitude*z**(degree+1)/(1-z)>arb('1e-7'):
        degree+=8
    assert degree<=CFG['max_degree']
    models=E.modes_taylor(r,degree)
    argument=arb(0,h.abs_upper());tail=z**(degree+1)/(1-z)
    covers={};bounds={}
    for key in keys:
        modes={};total=arb(0)
        for harmonic,p in models[key].items():
            rem=(majorants[key].get(harmonic,arb(0))*tail).abs_upper()
            value=arb_poly(p.coeffs()[:degree+1])(argument)+arb(0,rem)
            assert value.is_finite()
            modes[harmonic]=value;total+=value.abs_upper()
        covers[key]=modes;bounds[key]=total
    def tensor(name,d):
        return sum((math.comb(d,i)*bounds[name,i,d-i]*
                    bounds[name,i,d-i] for i in range(d+1)),arb(0)).sqrt()
    W2=1+4*right*right
    B0=tensor('rho',1)
    H1=W2.sqrt()*tensor('rho',2)
    H2=W2*tensor('rho',3)
    Hu=right*(tensor('u1',2)**2+tensor('u2',2)**2).sqrt()
    nt=CFG['angles'];table=MI.trig(nt)
    sx=MI.synth(covers['u1',1,0],table,nt)
    sy=MI.mul(MI.iv(arb(1)/2),MI.add(
        MI.synth(covers['u1',0,1],table,nt),
        MI.synth(covers['u2',1,0],table,nt)))
    ss=MI.up(MI.square_hi(sx)+MI.square_hi(sy))
    assert np.all(np.isfinite(ss))
    target=MI.iv(arb(3)/2)[0]
    passed=bool(np.all(ss<=MI.down(target*target)))
    records={'path':path,'degree':degree,'strain_pass':passed,
             'strain_square_upper':float(ss.max()),
             'B0':B0.str(70),'H1':H1.str(70),
             'H2':H2.str(70),'Hu':Hu.str(70)}
    return records
def panel(index):
    ratio=rational_arb(Q(CFG['ratio']))
    left=rational_arb(Q(CFG['rmin']))*ratio**index
    right=rational_arb(Q(CFG['rmin']))*ratio**(index+1)
    if right>arb(CFG['rmax']):right=arb(CFG['rmax'])
    leaves=[]
    def visit(lo,hi,path):
        row=point_panel(lo,hi,path)
        loose=arb(row['H2'])>10000
        if (not row['strain_pass'] or loose) and len(path)<CFG['max_depth']:
            mid=(lo+hi)/2;visit(lo,mid,path+'0');visit(mid,hi,path+'1')
        else:leaves.append(row)
    visit(left,right,'')
    return {'index':index,'leaves':leaves,
            'pass':all(r['strain_pass'] for r in leaves)}
def maxupper(values):return max(v.abs_upper() for v in values)
def endpoint(exp,r):
    def tensor(name,d,shift=0):
        terms=[]
        for i in range(d+1):
            key=(name,i,d-i)
            if shift and exp.side=='far':
                assert all(power+shift<0
                           for kind,n,power in exp.field(*key))
                assert all(power+shift<0
                           for a,power in exp.remainder_terms(*key,r))
            terms.append(math.comb(d,i)*exp.point_bound(*key,r)**2)
        return sum(terms,arb(0)).sqrt()
    W2=1+4*r*r
    b=tensor('rho',1)
    h1=W2.sqrt()*tensor('rho',2,1)
    h2=W2*tensor('rho',3,2)
    hu=r*(tensor('u1',2,1)**2+tensor('u2',2,1)**2).sqrt()
    s=exp.point_bound('u1',1,0,r)+(
        exp.point_bound('u1',0,1,r)+exp.point_bound('u2',1,0,r))/2
    return {'B0':b,'H1':h1,'H2':h2,'Hu':hu,'S':s}
def assemble(folder):
    cfg=json.loads((folder/'configuration.json').read_text())
    assert cfg['bindings']==bindings();ctx.prec=cfg['precision'];rows={}
    for file in sorted(folder.glob('chunk_*.json')):
        d=json.loads(file.read_text());assert d['configuration']==cfg
        for row in d['rows']:
            assert row['index'] not in rows;rows[row['index']]=row
            paths={p['path'] for p in row['leaves']}
            assert len(paths)==len(row['leaves'])
            def complete(path):
                if path in paths:
                    assert not any(p.startswith(path) and p!=path for p in paths)
                    return
                assert len(path)<cfg['max_depth']
                complete(path+'0');complete(path+'1')
            complete('')
    assert sorted(rows)==list(range(cfg['panels']))
    e=Evaluator(cfg['precision'],3,2)
    origin=endpoint(Expansion(e,'origin',16),arb(cfg['rmin']))
    far=endpoint(Expansion(e,'far',16),arb(cfg['rmax']))
    envelopes={}
    leaves=[p for row in rows.values() for p in row['leaves']]
    for key in ['B0','H1','H2','Hu']:
        envelopes[key]=maxupper([origin[key],far[key]]+
                                [arb(p[key]) for p in leaves])
    strain_ok=bool(origin['S']<arb(3)/2 and far['S']<arb(3)/2
                   and all(p['strain_pass'] for p in leaves))
    c=rational_arb(C);q=arb(21)/10;omega=arb(4);s=arb(3)/2
    # Triangle bound for the local E1, retaining no favorable correction.
    B0,H1,H2,Hu=[envelopes[k] for k in ['B0','H1','H2','Hu']]
    Minf=1+(2-q)*c
    K1=(2*omega*arb(2).sqrt()*(Minf+s)+omega*Hu+
        omega*arb(2).sqrt()*B0+
        2*omega*H1/2+
        q*omega*(1+1/arb(2).sqrt())*H1/2+
        (1+q)/2*H2)
    # Direct scalar E0, before favorable -4 beta omega.
    K0=omega*((8-2*q)*c+4+B0+(2-q/2)*H1/2)
    out={'status':'CERTIFIED_LOCAL_Q_COEFFICIENTS' if strain_ok
                 else 'LOCAL_COEFFICIENT_STRAIN_NOT_CERTIFIED',
         'configuration':cfg,'strain_op_upper':'3/2',
         'origin':{k:v.str(80) for k,v in origin.items()},
         'exterior':{k:v.str(80) for k,v in far.items()},
         'global_envelopes':{k:v.str(80) for k,v in envelopes.items()},
         'E1_local_upper':K1.str(80),'E0_local_upper':K0.str(80),
         'failed_strain_panels':[i for i,r in rows.items() if not r['pass']],
         'total_leaves':len(leaves),
         'finished_utc':datetime.now(timezone.utc).isoformat(),
         'scope':'Global actual coefficient envelopes for the local Q '
                 'identity only. Matrix, fractional terms, forcing, '
                 'operator bridge and self-map remain separate.'}
    (folder/'result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--workers',type=int,default=6);ap.add_argument('--chunk',type=int,default=12)
    ap.add_argument('--assemble',action='store_true')
    args=ap.parse_args()
    if args.assemble:return assemble(args.output)
    ratio=Q(33,32);lo=Q(1,100000);hi=Q(1000)
    count=math.ceil(math.log(float(hi/lo))/math.log(float(ratio)))
    assert lo*ratio**(count-1)<hi<=lo*ratio**count
    cfg={'precision':512,'max_degree':176,'ratio':str(ratio),
         'rmin':str(lo),'rmax':str(hi),'panels':count,
         'angles':512,'max_depth':5,'bindings':bindings(),
         'source_hashes':SOURCE_HASHES}
    args.output.mkdir(parents=True,exist_ok=True)
    cp=args.output/'configuration.json'
    if cp.exists():assert json.loads(cp.read_text())==cfg
    else:cp.write_text(json.dumps(cfg,indent=2)+'\n')
    start=time.monotonic()
    with ProcessPoolExecutor(args.workers,initializer=setup,initargs=(cfg,)) as pool:
        for first in range(0,count,args.chunk):
            ids=list(range(first,min(first+args.chunk,count)))
            path=args.output/f'chunk_{ids[0]:05}_{ids[-1]:05}.json'
            if path.exists():
                d=json.loads(path.read_text());assert d['configuration']==cfg
                assert [r['index'] for r in d['rows']]==ids
                continue
            rows=list(pool.map(panel,ids,chunksize=1))
            path.write_text(json.dumps({'configuration':cfg,'rows':rows},
                                      indent=2)+'\n')
            print('local coefficients',ids[-1]+1,'/',count,
                  'failed',sum(not r['pass'] for r in rows),
                  'seconds',time.monotonic()-start,flush=True)
    assemble(args.output)
if __name__=='__main__':main()
