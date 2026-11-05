"""Whole-plane direct Candidate013 L² coercivity certificate.

Local exact-source Taylor polynomials have rigorous Cauchy remainders.  Their
squared radial norms are integrated as polynomials.  Angular theta inequalities
use Arb trigonometric enclosures followed by outward-rounded IEEE interval
arithmetic.  Origin/exterior contributions use exact asymptotic expansions.
Restartable chunk files are self-contained records; final assembly checks every
panel index and input/code hash.  No successful certificate is declared unless
all checks pass.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor,as_completed
from datetime import datetime,timezone
from hashlib import sha256
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb,arb_poly,fmpq as Q,ctx
from fields013 import Evaluator,SOURCE_HASHES,C,rational_arb
from asymptotics013 import Expansion

HERE=Path(__file__).resolve().parent
E=None;TRIG=None;ARGS=None
INF=np.inf
def lower(x):return np.nextafter(float(x.lower()),-INF)
def upper(x):return np.nextafter(float(x.upper()),INF)
def up(x):return np.nextafter(x,INF)
def down(x):return np.nextafter(x,-INF)

def initialize(precision,degree,nt,theta,ratio_num,ratio_den,rmin,rmax):
    global E,TRIG,ARGS
    E=Evaluator(precision,max_density_order=2,max_velocity_order=-1)
    ARGS=(degree,nt,Q(theta),Q(ratio_num,ratio_den),Q(rmin),Q(rmax))
    harmonics=range(0,164)
    TRIG={}
    for kind in ['s','c']:
        for n in harmonics:
            vals=[]
            for i in range(nt):
                angle=arb.pi()*(2*i+1)/(4*nt)+arb(0,arb.pi()/(4*nt))
                val=(n*angle).sin()if kind=='s'else(n*angle).cos()
                vals.append((lower(val),upper(val)))
            TRIG[kind,n]=(np.array([v[0]for v in vals]),np.array([v[1]for v in vals]))

def interval_synthesis(modes):
    nt=ARGS[1];lo=np.zeros(nt);hi=np.zeros(nt)
    for key,val in modes.items():
        vl,vh=lower(val),upper(val);tl,th=TRIG[key]
        prods=np.array([vl*tl,vl*th,vh*tl,vh*th])
        lo=down(lo+down(np.min(prods,axis=0)))
        hi=up(hi+up(np.max(prods,axis=0)))
    return lo,hi

def radial_integral(p,r,h):
    """Exact polynomial integral of (r+t)*p(t)^2 on [-h,h]."""
    q=arb_poly(p.coeffs())**2
    co=(q*arb_poly([r,1])).coeffs()
    return sum((2*co[k]*h**(k+1)/(k+1) for k in range(0,len(co),2)),arb(0))

def panel(index):
    degree,nt,T,ratio,rmin,rmax=ARGS
    # Exact interval endpoints are rmin*ratio**index and min(next,rmax).
    # Arb operations contain those exact rationals without huge text transport.
    aa=rational_arb(rmin)*rational_arb(ratio)**index
    bb=rational_arb(rmin)*rational_arb(ratio)**(index+1)
    if bb>rational_arb(rmax):bb=rational_arb(rmax)
    r=(aa+bb)/2;h=(bb-aa)/2
    assert h>0 and h<r/8
    majorants,R=E.mode_majorants(r)
    z=h/R
    # Degree is the configured maximum.  Choose the least multiple of four
    # giving a summed field remainder below a fixed, scale-aware target.
    magnitude=sum((b for mm in majorants.values()for b in mm.values()),arb(0))
    target=arb('1e-14')/(1+r*r)
    chosen=12
    while magnitude*z**(chosen+1)/(1-z)>target and chosen<degree:chosen=min(chosen+4,degree)
    assert magnitude*z**(chosen+1)/(1-z)<target
    degree=chosen
    series=E.modes_taylor(r,degree)
    z=h/R;tailfactor=z**(degree+1)/(1-z);v=arb(0,h.abs_upper())
    cover={};remmax=arb(0);radints={}
    mass=2*r*h
    for key,modes in series.items():
        dd={};integer=arb(0)
        for harmonic,pp in modes.items():
            p=arb_poly(pp.coeffs()[:degree+1]);val=p(v)
            rem=(majorants[key].get(harmonic,arb(0))*tailfactor).abs_upper()
            dd[harmonic]=val+arb(0,rem)
            if rem>remmax:remmax=rem
            if key[1]+key[2]==2:
                integ=radial_integral(p,r,h)
                # Analytic integrand is nonnegative; tiny negative roundoff is
                # harmless when the containing ball's lower endpoint is used.
                assert integ.upper()>0
                # Only the certified upper endpoint is needed.  This also
                # handles a zero component whose roundoff ball crosses zero.
                sqr=integ.upper()
                norm=sqr.sqrt()+rem*mass.sqrt()
                weight=2 if harmonic[1]==0 else 1
                integer+=weight*norm**2*arb.pi()
        cover[key]=dd
        if key[1]+key[2]==2:radints[key]=integer
    axlo,axhi=interval_synthesis(cover['rho',1,0]);bylo,byhi=interval_synthesis(cover['rho',0,1])
    absx=np.maximum(np.abs(axlo),np.abs(axhi))
    tlo,thi=lower(rational_arb(T)),upper(rational_arb(T))
    rhs=down(down(4*tlo)*down(bylo+tlo))
    lhs=up(absx*absx)
    gaps=down(rhs-lhs);positive=down(bylo+2*tlo)
    passing=bool(np.all(gaps>=0)&np.all(positive>=0))
    return {'index':index,'degree':degree,'r_center':r.str(30),'halfwidth':h.str(30),'theta_pass':passing,
            'theta_min_gap':float(gaps.min()),'theta_min_positive':float(positive.min()),
            'worst_angular_index':int(np.argmin(gaps)),
            'radial_integrals':{str(k):v.str(70)for k,v in radints.items()},
            'max_cauchy_remainder':remmax.str(30)}

def bindings():
    return {p.name:sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),HERE/'fields013.py',HERE/'asymptotics013.py']}

def run(args):
    args.out.mkdir(parents=True,exist_ok=True)
    ratio=Q(args.ratio);rmin,rmax=Q(args.rmin),Q(args.rmax)
    panels=math.ceil(math.log(float(rmax/rmin))/math.log(float(ratio)))
    assert rmin*ratio**panels>=rmax and rmin*ratio**(panels-1)<rmax
    config={'source_hashes':SOURCE_HASHES,'code_hashes':bindings(),'precision':args.precision,'degree':args.degree,'nt':args.nt,'theta':args.theta,'ratio':args.ratio,'rmin':args.rmin,'rmax':args.rmax,'panels':panels}
    fp=args.out/'configuration.json'
    if fp.exists():assert json.loads(fp.read_text())==config
    else:fp.write_text(json.dumps(config,indent=2)+'\n')
    chunks=[list(range(i,min(i+args.chunk,panels)))for i in range(0,panels,args.chunk)]
    if args.max_panels:chunks=[list(range(min(args.max_panels,panels)))]
    completed=0;start=time.monotonic()
    for indices in chunks:
        dest=args.out/f'chunk_{indices[0]:05d}_{indices[-1]:05d}.json'
        if dest.exists():
            old=json.loads(dest.read_text());assert old['configuration']==config
            assert [r['index']for r in old['rows']]==indices
            completed+=len(indices);continue
        rows=[]
        with ProcessPoolExecutor(args.workers,initializer=initialize,
             initargs=(args.precision,args.degree,args.nt,args.theta,ratio.numerator,ratio.denominator,args.rmin,args.rmax))as pool:
            for rr in pool.map(panel,indices,chunksize=1):
                rows.append(rr)
                if len(rows)%16==0:print('completed',completed+len(rows),'/',panels,'seconds',time.monotonic()-start,'failedtheta',sum(not r['theta_pass']for r in rows),flush=True)
        record={'configuration':config,'rows':rows,'finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds_this_chunk':time.monotonic()-start}
        dest.write_text(json.dumps(record,indent=2)+'\n');completed+=len(rows)
    print('run_completed_rows',completed,flush=True)
    if completed==panels:assemble(args.out)

def assemble(outdir):
    config=json.loads((outdir/'configuration.json').read_text());assert config['code_hashes']==bindings()
    ctx.prec=config['precision'];rows={}
    for file in sorted(outdir.glob('chunk_*.json')):
        rec=json.loads(file.read_text());assert rec['configuration']==config
        for rr in rec['rows']:
            if rr['index']in rows:assert rows[rr['index']]==rr
            rows[rr['index']]=rr
    assert sorted(rows)==list(range(config['panels']))
    e=Evaluator(config['precision'],max_density_order=2,max_velocity_order=-1)
    near=Expansion(e,'origin',12);far=Expansion(e,'far',12)
    integrals={}
    for key in [('rho',2,0),('rho',1,1),('rho',0,2)]:
        s=sum((arb(row['radial_integrals'][str(key)])for row in rows.values()),arb(0))
        nl=near.tail_L2_bound(*key,config['rmin']);fl=far.tail_L2_bound(*key,config['rmax'])
        integrals[str(key)]={'core':s.str(70),'origin_L2_upper':nl.str(70),'far_L2_upper':fl.str(70),'total_squared_upper':(s+nl**2+fl**2).str(70)}
    xx=arb(integrals[str(('rho',2,0))]['total_squared_upper']);xy=arb(integrals[str(('rho',1,1))]['total_squared_upper']);yy=arb(integrals[str(('rho',0,2))]['total_squared_upper'])
    kap=(((arb(2).log()-arb(1)/2)*(xx+xy)+(3*arb(2).log()-2)*(xy+yy))/(16*arb.pi())).sqrt()
    T=rational_arb(Q(config['theta']));xnear=near.point_bound('rho',1,0,config['rmin']);yr=near.point_bound('rho',0,1,config['rmin'],exclude_constant=True)
    origin_constants=[(kind,n,a)for (kind,n,power),a in near.field('rho',0,1).items()if power==0]
    assert all(kind=='c'and n==0 for kind,n,a in origin_constants)
    assert not any(power==0 for (kind,n,power),a in near.field('rho',1,0).items())
    a0=sum((arb(a)for kind,n,a in origin_constants),arb(0))
    nearpass=bool(xnear**2<4*T*(a0-yr+T) and a0-yr+2*T>0)
    # Far gradient L1 bound controls theta <= |grad rho| <= |rho_x|+|rho_y|.
    fgrad=far.point_bound('rho',1,0,config['rmax'])+far.point_bound('rho',0,1,config['rmax'])
    farpass=bool(fgrad<T)
    corepass=all(r['theta_pass']for r in rows.values())
    beta=rational_arb(C)+1-T-kap
    result={'status':'CERTIFIED_DIRECT_L2'if nearpass and farpass and corepass else 'NOT_CERTIFIED_THETA_COVER_FAILED',
        'configuration':config,'integrals':integrals,'kappa_HS_upper':kap.str(70),'theta_upper':str(Q(config['theta'])),
        'beta_L2_lower':beta.str(70),'theta_origin_pass':nearpass,'theta_exterior_pass':farpass,'theta_core_pass':corepass,
        'theta_failed_panel_indices':[i for i,r in rows.items()if not r['theta_pass']],
        'origin_a0':a0.str(70),'origin_gradient_remainder':yr.str(70),'far_gradient_L1_upper':fgrad.str(70),
        'finished_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Exact-source whole-plane scalar coercivity via theta plus the full-space Hilbert-Schmidt bound. Does not certify inverse/generator or high-order closure.'}
    (outdir/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--workers',type=int,default=8);ap.add_argument('--precision',type=int,default=384);ap.add_argument('--degree',type=int,default=72);ap.add_argument('--nt',type=int,default=1024);ap.add_argument('--theta',default='1/80');ap.add_argument('--ratio',default='201/199');ap.add_argument('--rmin',default='1/100000');ap.add_argument('--rmax',default='100000000');ap.add_argument('--chunk',type=int,default=128);ap.add_argument('--max-panels',type=int);ap.add_argument('--assemble',action='store_true');args=ap.parse_args()
    if args.assemble:assemble(args.out)
    else:run(args)
if __name__=='__main__':main()
