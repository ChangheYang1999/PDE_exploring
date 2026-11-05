"""Exact-source cubic-free angular Gaussian residual coordinates.

psi_m=sqrt(2/(pi*m!))*a^(-m-1)*r^m*sin(mtheta)*exp(-r²/(2a²)).
For H=J^2.1(WF), <RH,RJ^-.1psi>=<WF,(1-Delta)psi>. All omitted
radial tails are bounded by inherited ||F||₂ times exact test-tail norms.
"""
import argparse,json,math,time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from flint import arb,arb_series,fmpq as Q,fmpq_poly as Poly,ctx
from fields013 import Evaluator,C,SOURCE_HASHES,rational_arb
from source_projections013 import residual_mode,sine_product

HERE=Path(__file__).resolve().parent
E=None;CONF=None


def setup(config):
    global E,CONF
    CONF=config;E=Evaluator(config['bits'],1,0)


def panel(index):
    m=CONF['m'];a=rational_arb(Q(CONF['width']));ratio=rational_arb(Q(CONF['ratio']))
    left=rational_arb(Q(CONF['rmin']))*ratio**index;right=left*ratio
    if right>rational_arb(Q(CONF['rmax'])):right=rational_arb(Q(CONF['rmax']))
    r=(left+right)/2;h=(right-left)/2;majorants,R=E.mode_majorants(r)
    rx,ry=majorants['rho',1,0],majorants['rho',0,1]
    mf=arb(C)*(r+R)*(sine_product({('c',1):arb(1)},rx,m,True)+sine_product({('s',1):arb(1)},ry,m,True))
    mf+=sine_product(majorants['u1',0,0],rx,m,True)+sine_product(majorants['u2',0,0],ry,m,True)+majorants['rho',0,0].get(('s',m),arb(0))
    N=(arb(2)/(arb.pi()*math.factorial(m))).sqrt()*a**(-m-1)
    upperr=r+R;mh=arb.pi()*N*(1+4*upperr**2).sqrt()*mf*upperr**(m+1)
    mh*=(-3*r*r/(8*a*a)).exp()*(1+2*(m+1)/a**2+upperr**2/a**4)
    z=h/R;degree=12
    while 2*h*mh*z**(degree+1)/(1-z)>arb(CONF['panel_target']):degree+=4
    assert degree<=CONF['max_degree']
    modes=E.modes_taylor(r,degree);rr=arb_series([r,1],prec=degree+1)
    f=residual_mode(modes,rr,m);s=rr*rr/(a*a)
    integrand=arb.pi()*N*(1+4*rr*rr)**arb('0.5')*f*rr**(m+1)*(-s/2).exp()*(1+(2*(m+1)-s)/(a*a))
    assert integrand.prec>=degree+1
    value=sum((2*integrand[k]*h**(k+1)/(k+1)for k in range(0,degree+1,2)),arb(0))
    error=(2*h*mh*z**(degree+1)/(1-z)).abs_upper()
    return {'index':index,'degree':degree,'integral':value.str(80),'error':error.str(70),'center':r.str(25),'halfwidth':h.str(25)}


def tail_norms(config):
    m=config['m'];a=Q(config['width']);s=Poly([0,1])
    polynomial=s**m*(1+4*a*a*s)*(1+(2*(m+1)-s)/(a*a))**2/math.factorial(m)
    def upper_gamma(n,z):
        return math.factorial(n)*(-z).exp()*sum((z**k/math.factorial(k)for k in range(n+1)),arb(0))
    slo=rational_arb((Q(config['rmin'])/a)**2);shi=rational_arb((Q(config['rmax'])/a)**2)
    near=sum((arb(c)*(math.factorial(k)-upper_gamma(k,slo))for k,c in enumerate(polynomial)if c),arb(0))
    far=sum((arb(c)*upper_gamma(k,shi)for k,c in enumerate(polynomial)if c),arb(0))
    assert near>0 and far>0;return near.sqrt(),far.sqrt()


def hashes():
    return {p.name:sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),HERE/'fields013.py',HERE/'source_projections013.py']}


def assemble(out):
    config=json.loads((out/'configuration.json').read_text());assert config['code_hashes']==hashes();ctx.prec=config['bits'];rows={}
    for file in out.glob('chunk_*.json'):
        record=json.loads(file.read_text());assert record['configuration']==config
        for row in record['rows']:assert row['index']not in rows;rows[row['index']]=row
    assert sorted(rows)==list(range(config['panels']))
    value=sum((arb(row['integral'])for row in rows.values()),arb(0));error=sum((arb(row['error'])for row in rows.values()),arb(0))
    near,far=tail_norms(config);tail=arb('0.0000007961207')*(near+far)
    interval=value+arb(0,(error+tail).abs_upper())
    result={'status':'CERTIFIED_ANGULAR_SOURCE_PROJECTION','configuration':config,'c_interval':interval.str(80),
        'core_integral':value.str(80),'core_error':error.str(70),'origin_test_L2_norm':near.str(70),
        'exterior_test_L2_norm':far.str(70),'tail_error':tail.str(70),'source_L2_bound':'0.0000007961207',
        'identity':'<R J^(21/10)(WF),R J^(-1/10)psi>=<WF,(1-Delta)psi>',
        'finished_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'One exact-source angular residual coordinate; actual full-matrix inverse Gram and theorem closure remain separate.'}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--m',type=int,default=115)
    ap.add_argument('--width',default='1471/10000');ap.add_argument('--rmin',default='7/10');ap.add_argument('--rmax',default='3')
    ap.add_argument('--workers',type=int,default=4);ap.add_argument('--chunk',type=int,default=8);ap.add_argument('--assemble',action='store_true');ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    ratio=Q(101,99);lo,hi=Q(args.rmin),Q(args.rmax);count=math.ceil(math.log(float(hi/lo))/math.log(float(ratio)))
    assert lo*ratio**count>=hi>lo*ratio**(count-1)
    config={'source_hashes':SOURCE_HASHES,'code_hashes':hashes(),'bits':384,'m':args.m,'width':str(Q(args.width)),
        'rmin':str(lo),'rmax':str(hi),'ratio':str(ratio),'panels':count,'max_degree':192,'panel_target':'1e-14'}
    if args.pilot:
        setup(config);print(json.dumps(panel(count//2),indent=2),flush=True);return
    if args.assemble:assemble(args.out);return
    args.out.mkdir(parents=True,exist_ok=True);cf=args.out/'configuration.json'
    if cf.exists():assert json.loads(cf.read_text())==config
    else:cf.write_text(json.dumps(config,indent=2)+'\n')
    tick=time.monotonic()
    for first in range(0,count,args.chunk):
        indices=list(range(first,min(first+args.chunk,count)));dest=args.out/f'chunk_{indices[0]:05d}_{indices[-1]:05d}.json'
        if dest.exists():continue
        with ProcessPoolExecutor(args.workers,initializer=setup,initargs=(config,))as pool:rows=list(pool.map(panel,indices,chunksize=1))
        dest.write_text(json.dumps({'configuration':config,'rows':rows},indent=2)+'\n');print('completed',indices[-1]+1,'/',count,'seconds',time.monotonic()-tick,flush=True)
    assemble(args.out)

if __name__=='__main__':main()
