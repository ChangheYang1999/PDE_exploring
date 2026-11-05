#!/usr/bin/env python3
"""Universal interval certificate for the gradient-source Cvs3 highpass kernel.

Only dimensionless elementary functions occur. Candidate-specific derivative
norms remain a separate input to the Hilbert-Schmidt bound.
"""
import argparse,json,math,time,hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from flint import arb,fmpq as Q,ctx
HERE=Path(__file__).resolve().parent
CONFIG=None;RADII=None;TRIG=None
def aq(q):
    q=Q(q);return arb(q.numerator)/q.denominator
def ball(lo,hi):return (aq(lo)+aq(hi))/2+arb(0,((aq(hi)-aq(lo))/2).abs_upper())
def arb_interval(lo,hi):return (lo+hi)/2+arb(0,((hi-lo)/2).abs_upper())
def positive_square(x):
    hi=x.abs_upper();hi=hi*hi
    if x.contains(0):lo=arb(0)
    else:
        l=x.lower();h=x.upper();lo=min(l*l,h*h)
    return arb_interval(lo,hi)
def positive_part_interval(x):
    lo=max(arb(0),x.lower());hi=max(arb(0),x.upper())
    return arb_interval(lo,hi)
def clipped_abs(x,limit):
    if not x.is_finite():return arb(limit)
    v=x.abs_upper()
    return arb(limit) if v>limit else v

def init(config):
    global CONFIG,RADII,TRIG
    CONFIG=config;ctx.prec=config['bits']
    ratio=Q(config['radial_ratio']);lo=Q(config['rmin']);end=Q(config['rmax']);RADII=[]
    while lo<end:
        hi=min(lo*ratio,end);RADII.append((lo,hi));lo=hi
    nt=config['nt'];TRIG=[]
    for j in range(nt):
        theta=arb.pi()*arb(2*j+1)/(2*nt)+arb(0,arb.pi()/(2*nt))
        TRIG.append((theta.cos(),theta.sin()))

def integrate(item):
    index,alo,ahi=item;A=ball(alo,ahi);al=aq(alo);sumpar=arb(0);sumperp=arb(0)
    nt=CONFIG['nt'];dtheta=arb.pi()/nt
    # Tiny-origin omitted disk: |da_x|<=2, |da_y|<=1 and H(r)<=r²/2.
    origin=arb.pi()/3*aq(CONFIG['rmin'])**6/al**4
    for rl,rh in RADII:
        R=ball(rl,rh);u=A/R
        mass=(aq(rh)**2-aq(rl)**2)/2
        hp=1-(-aq(rh)**2/2).exp();common=2*dtheta*mass*hp*hp/al**4
        p=arb(0);q=arb(0)
        for ct,st in TRIG:
            den2=positive_square(1-u)+2*u*positive_part_interval(1+ct)
            if den2.lower()<=0:
                dx=arb(2);dy=arb(1)
            else:
                den=den2.sqrt()
                # Stable formulas retain a factor u when displacement is small.
                dx=clipped_abs(u*(1-(u+2*ct)*ct/(1+den))/den,2)
                dy=clipped_abs(u*(u+2*ct)*st/(den*(1+den)),1)
            p+=dx*dx*dy*dy;q+=dy*dy*dy*dy
        sumpar+=common*p;sumperp+=common*q
    # At r>=rmax, |da|<=2a/r, H<=1 gives 16pi/rmax².
    tail=16*arb.pi()/aq(CONFIG['rmax'])**2
    sumpar+=origin+tail;sumperp+=origin+tail
    assert sumpar.is_finite() and sumperp.is_finite()
    target=aq(CONFIG['target'])
    return {'index':index,'a_lower':str(alo),'a_upper':str(ahi),'parallel_uniform_upper':sumpar.str(70),'perpendicular_uniform_upper':sumperp.str(70),'passes':bool(sumpar<target and sumperp<target)}

def analytic_cases(config):
    ctx.prec=config['bits'];amin=aq(config['amin']);amax=aq(config['amax'])
    c=100/(81*arb(3).sqrt());error=c/5+c*c/100
    angular=(5*arb.pi()/64).sqrt()+(2*arb.pi()).sqrt()*error
    small=angular*angular*arb(2).log()/2+arb.pi()/3*10**6*amin*amin
    large=32*arb.pi()/(amax*amax)
    target=aq(config['target']);assert small<target and large<target
    return {'small_a_uniform_upper':small.str(70),'large_a_uniform_upper':large.str(70)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--workers',type=int,default=4);ap.add_argument('--nt',type=int,default=64)
    ap.add_argument('--radial-ratio',default='11/10');ap.add_argument('--parameter-ratio',default='11/10')
    ap.add_argument('--amin',default='1/10000');ap.add_argument('--amax',default='20')
    ap.add_argument('--rmin',default='1/100000000');ap.add_argument('--rmax',default='100')
    ap.add_argument('--target',default='1/2');ap.add_argument('--pilot',action='store_true')
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    config={k:v for k,v in vars(args).items() if k not in ['out','workers','pilot']}
    config['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    fp=args.out/'configuration.json'
    if fp.exists():assert json.loads(fp.read_text())==config
    else:fp.write_text(json.dumps(config,indent=2)+'\n')
    analytical=analytic_cases(config);items=[];lo=Q(args.amin);end=Q(args.amax);ratio=Q(args.parameter_ratio)
    while lo<end:
        hi=min(lo*ratio,end);items.append((len(items),lo,hi));lo=hi
    if args.pilot:items=[(0,Q(9,10),Q(1))]
    st=time.time();rows=[];pending=[]
    for item in items:
        dest=args.out/f'parameter_{item[0]:04d}.json'
        if dest.exists() and not args.pilot:
            old=json.loads(dest.read_text())
            assert old['index']==item[0] and old['a_lower']==str(item[1]) and old['a_upper']==str(item[2])
            rows.append(old)
        else:pending.append(item)
    with ProcessPoolExecutor(args.workers,initializer=init,initargs=(config,)) as pool:
        for row in pool.map(integrate,pending,chunksize=1):
            dest=args.out/f'parameter_{row["index"]:04d}.json';dest.write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
            print('parameter',row['index'],'passes',row['passes'],'par',row['parallel_uniform_upper'],'perp',row['perpendicular_uniform_upper'],'seconds',round(time.time()-st,2),flush=True)
    rows.sort(key=lambda r:r['index']);assert len(rows)==len(items)
    result={'status':'CERTIFIED_UNIVERSAL_GRADIENT_CVS3_HS_KERNEL_CONSTANT' if not args.pilot and all(r['passes'] for r in rows) else 'PILOT_OR_NOT_CERTIFIED','configuration':config,'analytic_cases':analytical,'rows':rows,'elapsed_seconds':time.time()-st,'warning':'Universal dimensionless kernel bound only. Multiply by a separately certified actual derivative norm; no full IPM closure asserted.'}
    (args.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
