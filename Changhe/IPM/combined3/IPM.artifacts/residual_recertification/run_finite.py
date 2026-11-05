"""Whole annulus rigorous L2 and integer-energy residual enclosure."""
import sys,json,gzip,time,math,argparse,os
from pathlib import Path
from fractions import Fraction
from concurrent.futures import ProcessPoolExecutor,as_completed
from finite import *
from high_order import panel_energy
from finite_fast import residual_taylor_fast as residual_taylor
E=None

def initialize(precision):
    global E
    E=Evaluator(precision,max_density_order=1,max_velocity_order=0)

def exact(x):return str(arb(x).fmpq())
def pair(x):return [exact(x.lower()),exact(x.upper())]

def l2_energy(f,c,h,H,R,K):
    powers=[h**k for k in range(K+1)]
    P=arb_poly();Pmax=arb(0)
    for n,p in f.items():
        a=[p[k]*powers[k] for k in range(K+1)]
        pp=arb_poly(a);P+=pp*pp
        Pmax+=sum((v.abs_upper()for v in a),arb(0))
    P*=arb_poly([c,h]);polynomial=2*h*arb.pi()*sum((P[k]/(k+1)for k in range(0,P.degree()+1,2)),arb(0))
    q=h/R;tail=(H*q**(K+1)/(1-q)).abs_upper()
    err=(2*h*arb.pi()*(c+h)*(2*Pmax*tail+tail*tail)).abs_upper()
    lower=max(arb(0),polynomial.lower()-err);upper=polynomial.upper()+err
    return {'energy_lower':exact(lower.lower()),'energy_upper':exact(upper.upper()),'polynomial_integral':pair(polynomial),'analytic_error_upper':exact(err.upper()),'residual_remainder_l1_upper':exact(tail.upper()),'polynomial_l1_upper':exact(Pmax.upper()),'integrand_coefficients':[pair(P[k])for k in range(P.degree()+1)]}

def panel(task):
    index,left,right,outdir,precision=task;t=time.monotonic()
    target=Path(outdir)/('panel_%05d.json.gz'%index)
    if target.exists():
        with gzip.open(target,'rt')as fp:return json.load(fp)
    ctx.prec=precision
    leftq,rightq=Fraction(left),Fraction(right)
    cq=(leftq+rightq)/2;hq=(rightq-leftq)/2
    a,b=arb(left),arb(right);c=arb(str(cq));h=arb(str(hq))
    H,R=improved_majorant(E,c);H=H.upper();R=R.lower()
    q=h/R;assert 0<q<arb(1)/2
    desired=arb('1e-26')*min(arb(1),c**3)/max(arb(1),c**4)
    K=max(24,math.ceil((math.log(float(desired))-math.log(float(H.upper())))/math.log(float(q.upper()))))
    while not H*q**(K+1)/(1-q)<desired:K+=1
    f=residual_taylor(E,c,K,scale=h)
    data={'convolution_layout':'parity_compressed','status':'CERTIFIED_FINITE_RESIDUAL_PANEL','index':index,'left':left,'right':right,'center':str(cq),'halfwidth':str(hq),'degree':K,'precision':precision,'residual_majorant_upper':exact(H.upper()),'cauchy_radius':exact(R),'L2':l2_energy(f,c,h,H,R,K),'high_order':panel_energy(f,c,h,H,R,K,raw=True),'elapsed_seconds':time.monotonic()-t}
    temporary=Path(str(target)+'.tmp')
    with gzip.open(temporary,'wt')as fp:json.dump(data,fp,separators=(',',':'))
    os.replace(temporary,target)
    return {k:v for k,v in data.items()if k not in ['L2','high_order']}|{'L2':{k:v for k,v in data['L2'].items()if k!='integrand_coefficients'},'high_order':{k:v for k,v in data['high_order'].items()if k!='modal_rows'}}

def run(args):
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    left=Fraction(args.rmin);stop=Fraction(args.rmax);ratio=Fraction(args.ratio)
    tasks=[]
    while left<stop:
        right=min(stop,left*ratio);tasks.append((len(tasks),str(left),str(right),str(out),args.precision));left=right
    (out/'configuration.json').write_text(json.dumps({'rmin':args.rmin,'rmax':args.rmax,'ratio':args.ratio,'precision':args.precision,'panels':len(tasks),'source_hashes':SOURCE_HASHES,'code_files':['finite.py','finite_fast.py','run_finite.py','run_finite_legacy.py','high_order.py']},indent=2))
    print('PANELS',len(tasks),flush=True);start=time.monotonic()
    if args.only is not None:
        initialize(args.precision);print(json.dumps(panel(tasks[args.only]),indent=2));return
    finished=0
    with ProcessPoolExecutor(max_workers=args.workers,initializer=initialize,initargs=(args.precision,))as pool:
        futures={pool.submit(panel,t):t[0]for t in tasks}
        for future in as_completed(futures):
            row=future.result();finished+=1
            print(json.dumps({'done':finished,'total':len(tasks),'index':row['index'],'degree':row['degree'],'panel_s':row['elapsed_seconds'],'elapsed_s':time.monotonic()-start,'L2upper':float(Fraction(row['L2']['energy_upper'])),'E2upper':float(Fraction(row['high_order']['E2_upper'])),'E3upper':float(Fraction(row['high_order']['E3_upper']))}),flush=True)
    print('COMPLETE',flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--rmin',default='1/100000000');p.add_argument('--rmax',default='100000000000000000000');p.add_argument('--ratio',default='17/16');p.add_argument('--precision',type=int,default=640);p.add_argument('--workers',type=int,default=16);p.add_argument('--outdir',default='/tmp/residual_recertification/finite_data');p.add_argument('--only',type=int);run(p.parse_args())
