"""Full-matrix Riesz-source enclosure through one smooth vector coordinate.

The actual matrix inverse is interval-integrated on a core annulus.  The exact
Fourier Gram minus a certified core L² lower controls the entire complement.
This is a rigorous enclosure of the full-plane dual norm, not a plane FFT.
"""
import argparse,json,math,sys,time
from concurrent.futures import ProcessPoolExecutor
from hashlib import sha256
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,arb_poly,ctx,fmpq as Q
from fields013 import Evaluator,C,rational_arb,SOURCE_HASHES
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'finite_rank'))
from cubic_heat_certificate import CubicHeat

E=None;HEAT=None;TRIG=None;CONF=None;DER11=None
NEG=-np.inf;POS=np.inf
def down(x):return np.nextafter(x,NEG)
def up(x):return np.nextafter(x,POS)
def iv(value):return down(float(value.lower())),up(float(value.upper()))
def add(a,b):return down(a[0]+b[0]),up(a[1]+b[1])
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    pp=np.array([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
    return down(np.min(pp,axis=0)),up(np.max(pp,axis=0))
def square(a):
    lo=np.minimum(a[0]*a[0],a[1]*a[1]);lo=np.where((a[0]<=0)&(a[1]>=0),0,down(lo))
    return lo,up(np.maximum(a[0]*a[0],a[1]*a[1]))

def initialize(config):
    global E,HEAT,TRIG,CONF,DER11
    CONF=config;E=Evaluator(config['profile_bits'],1,1)
    HEAT=CubicHeat(width=config['width'],rmax='31/100',nodes=config['heat_nodes'],bits=config['heat_bits'])
    nt=config['nt'];TRIG={}
    for kind in ['s','c']:
        for n in range(164):
            vals=[]
            for j in range(nt):
                angle=arb.pi()*(2*j+1)/(4*nt)+arb(0,arb.pi()/(4*nt))
                value=(n*angle).sin()if kind=='s'else(n*angle).cos();vals.append(iv(value))
            TRIG[kind,n]=np.array([v[0]for v in vals]),np.array([v[1]for v in vals])
    # Each vector component has inverse-Fourier derivative bound C_j.
    # Extracting a radial Fourier coefficient costs at most a factor two.
    a=rational_arb(Q(config['width']));j=11
    def moment(p):return (2/a**2)**(arb(p+1)/2)*(arb(p+1)/2).gamma()/2
    DER11=2*a*a/arb.pi().sqrt()*(2*moment(j+2)+a*a*moment(j+4))

def synth(modes):
    lo=np.zeros(CONF['nt']);hi=np.zeros(CONF['nt'])
    for key,value in modes.items():
        a,b=mul(iv(value),TRIG[key]);lo=down(lo+a);hi=up(hi+b)
    return lo,hi

def phi_cover(r,h):
    count=11;values=[[],[]]
    for j in range(count):
        t=(arb.pi()*(2*j+1)/(2*count)).cos();point=r+h*t
        modes=HEAT.modes(point)
        values[0].append(modes['r2','c',0]);values[1].append(modes['r1','s',2])
    answer=[];polynomials=[];error=DER11*h**11/(2**10*math.factorial(11))
    T=[arb_poly([1]),arb_poly([0,1])]
    for k in range(1,count-1):T.append(arb_poly([0,2])*T[-1]-T[-2])
    for row in values:
        center=sum(row,arb(0))/count;variation=arb(0)
        poly=arb_poly([center])
        for k in range(1,count):
            ck=arb(2)/count*sum((row[j]*(arb.pi()*k*(2*j+1)/(2*count)).cos()for j in range(count)),arb(0))
            variation+=ck.abs_upper()
            poly+=ck*T[k]
        answer.append(center+arb(0,(variation+error).abs_upper()))
        polynomials.append(poly)
    return answer,error,polynomials

def panel(index):
    ratio=rational_arb(Q(CONF['ratio']));left=rational_arb(Q(CONF['rmin']))*ratio**index;right=left*ratio;end=rational_arb(Q(CONF['rmax']))
    if right>end:right=end
    r=(left+right)/2;h=(right-left)/2;majorants,R=E.mode_majorants(r);z=h/R
    mag=sum((b for mm in majorants.values()for b in mm.values()),arb(0));degree=12
    while mag*z**(degree+1)/(1-z)>arb('1e-10'):degree+=4
    assert degree<=160
    modes,meta=E.modes_cover(r,h,degree)
    (c0,c2),interpolation_error,polynomials=phi_cover(r,h);px=mul(iv(c2),TRIG['s',2]);py=sub(iv(c0),mul(iv(c2),TRIG['c',2]))
    profile={key:synth(value)for key,value in modes.items()}
    rball=r+arb(0,h.abs_upper());r2=rball*rball
    dilation=add(iv(arb(C)*r2/(arb(1)/4+r2)),mul(iv(rball/(arb(1)/4+r2)),add(mul(profile['u1',0,0],TRIG['c',1]),mul(profile['u2',0,0],TRIG['s',1]))))
    q=arb(21)/10
    aa0=add(sub(add(iv(arb(C)+1),dilation),mul(iv(q),add(iv(arb(C)),profile['u1',1,0]))),profile['rho',0,1])
    dd0=sub(add(iv(arb(C)+1),dilation),mul(iv(q),add(iv(arb(C)),profile['u2',0,1])))
    bb=sub(mul(iv(-q/2),add(profile['u1',0,1],profile['u2',1,0])),mul(iv(arb(1)/2),profile['rho',1,0]))
    mass=2*r*h;v1sq=square(px);v2sq=square(py);gamma_by_beta={};fallback={}
    for text in CONF['betas']:
        beta=rational_arb(Q(text));aa=sub(aa0,iv(beta));dd=sub(dd0,iv(beta))
        det=sub(mul(aa,dd),square(bb));numerator=add(sub(mul(dd,v1sq),mul(iv(arb(2)),mul(bb,mul(px,py)))),mul(aa,v2sq))
        delta=rational_arb(Q('704955805507/1000000000000')-Q(text))
        global_upper=mul(add(v1sq,v2sq),iv(1/delta))[1]
        valid=(det[0]>0)&(numerator[1]>=0);denominator=np.where(valid,det[0],1.)
        local_upper=up(numerator[1]/denominator);upper=np.where(valid,np.minimum(local_upper,global_upper),global_upper)
        assert np.all(np.isfinite(upper))and np.all(upper>=0)
        gam=mass*(2*arb.pi()/CONF['nt'])*sum((arb(float(v))for v in upper),arb(0))
        gamma_by_beta[text]=gam.upper().str(70);fallback[text]=int(np.sum(~valid))
    # Lower the true core norm using exact polynomial square integrals and
    # a uniform interpolation remainder, not a pointwise minimum.
    Qlower=arb(0)
    for polynomial in polynomials:
        integrand=(polynomial**2*arb_poly([r,h])).coeffs()
        energy=h*sum((2*integrand[k]/(k+1)for k in range(0,len(integrand),2)),arb(0))
        assert energy.upper()>0
        norm_lower=arb(0)if energy.lower()<=0 else energy.lower().sqrt()-interpolation_error*mass.sqrt()
        if norm_lower<0:norm_lower=arb(0)
        Qlower+=2*arb.pi()*norm_lower**2
    return {'index':index,'degree':degree,'center':r.str(30),'halfwidth':h.str(30),'Gamma_core_upper_by_beta':gamma_by_beta,'Q_core_lower':Qlower.lower().str(70),'fallback_angles':fallback,'Phi0':c0.str(50),'Phi2':c2.str(50),'interpolation_error':interpolation_error.str(50)}

def hashes():
    paths=[Path(__file__),HERE/'fields013.py',HERE.parent/'finite_rank/cubic_heat_certificate.py']
    return {str(p.relative_to(HERE.parent)):sha256(p.read_bytes()).hexdigest()for p in paths}

def assemble(out):
    config=json.loads((out/'configuration.json').read_text());assert config['code_hashes']==hashes();ctx.prec=384;rows={}
    for p in out.glob('chunk_*.json'):
        rec=json.loads(p.read_text());assert rec['configuration']==config
        for r in rec['rows']:assert r['index']not in rows;rows[r['index']]=r
    assert sorted(rows)==list(range(config['panels']))
    Qcore=sum((arb(r['Q_core_lower'])for r in rows.values()),arb(0))
    a=rational_arb(Q(config['width']));s=a*a
    B=a**4/2*(4*s.hypgeom_u(2,arb(29)/10)-8*s*s.hypgeom_u(3,arb(39)/10)+6*s*s*s.hypgeom_u(4,arb(49)/10))
    missing=(B.upper()-Qcore.lower()).upper();assert missing>0
    by_beta={}
    for text in config['betas']:
        core=sum((arb(r['Gamma_core_upper_by_beta'][text])for r in rows.values()),arb(0));delta=rational_arb(Q('704955805507/1000000000000')-Q(text));gamma=(core+missing/delta).upper()
        by_beta[text]={'Gamma_core_upper':core.str(70),'global_N_gap':str(Q('704955805507/1000000000000')-Q(text)),'Gamma_full_upper':gamma.str(70)}
    result={'status':'CERTIFIED_FULL_MATRIX_TEST_DUAL','configuration':config,'B_interval':B.str(80),'Q_core_lower':Qcore.str(70),'test_L2_complement_upper':missing.str(70),'by_beta':by_beta,'scope':'One actual full-matrix inverse Gram upper and complete smooth Riesz-vector tail enclosure. Combine with the independently certified source coordinate via Woodbury; this alone is not an existence theorem.','finished_utc':datetime.now(timezone.utc).isoformat()}
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--workers',type=int,default=4);ap.add_argument('--chunk',type=int,default=8);ap.add_argument('--assemble',action='store_true');ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    ratio=Q(101,99);lo=Q(1,1000000);hi=Q(3,10);panels=math.ceil(math.log(float(hi/lo))/math.log(float(ratio)))
    assert lo*ratio**panels>=hi>lo*ratio**(panels-1)
    config={'source_hashes':SOURCE_HASHES,'code_hashes':hashes(),'profile_bits':384,'heat_bits':256,'heat_nodes':768,'nt':256,'betas':['7/10','176/250','7049/10000','14099/20000','704954/1000000'],'width':'3/200','rmin':str(lo),'rmax':str(hi),'ratio':str(ratio),'panels':panels}
    if args.pilot:
        initialize(config)
        for value in [.001,.015,.03,.1,.29]:
            i=int(math.log(value/float(lo))/math.log(float(ratio)));print(json.dumps(panel(i),indent=2),flush=True)
        return
    if args.assemble:assemble(args.out);return
    args.out.mkdir(parents=True,exist_ok=True);cf=args.out/'configuration.json'
    if cf.exists():assert json.loads(cf.read_text())==config
    else:cf.write_text(json.dumps(config,indent=2)+'\n')
    start=time.monotonic()
    for first in range(0,panels,args.chunk):
        indices=list(range(first,min(first+args.chunk,panels)));dest=args.out/f'chunk_{indices[0]:05d}_{indices[-1]:05d}.json'
        if dest.exists():continue
        with ProcessPoolExecutor(args.workers,initializer=initialize,initargs=(config,))as pool:rows=list(pool.map(panel,indices,chunksize=1))
        dest.write_text(json.dumps({'configuration':config,'rows':rows},indent=2)+'\n');print('completed',indices[-1]+1,'/',panels,'seconds',time.monotonic()-start,flush=True)
    assemble(args.out)
if __name__=='__main__':main()
