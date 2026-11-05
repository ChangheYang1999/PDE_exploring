#!/usr/bin/env python3
"""Whole-plane interval certificate for the tame Q-source coefficient constants.

Only scalar density modes are differentiated. All radial polynomial integrals
and Cauchy tails use Arb. Origin/exterior tails use exact homogeneous expansions.
Chunk records are restartable and bound to all source hashes.
"""
import argparse,json,math,sys,time,hashlib
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
from flint import arb,arb_poly,arb_series,fmpq as Q,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import Evaluator,SOURCE_HASHES,rational_arb
from asymptotics013 import Expansion
E=None;CONF=None

def initialize(config):
    global E,CONF
    CONF=config;E=Evaluator(config['bits'],max_density_order=0,max_velocity_order=-1)

def apoly(pp,degree):return arb_poly(pp.coeffs()[:degree+1])
def sq(x):return x*x
def lap(f,rr,n):return f.derivative().derivative()+f.derivative()/rr-n*n*f/(rr*rr)

def field_majorants(M,r,n):
    # rho modes bounded by M on |z-r|<=r/8; at |z-r|<=r/16,
    # Cauchy bounds j! M/(r/16)^j and |z|>=15r/16 apply.
    R=r/16;lo=15*r/16
    j=[math.factorial(k)*M/R**k for k in range(6)]
    L=j[2]+j[1]/lo+n*n*j[0]/lo**2
    Lr=j[3]+j[2]/lo+(1+n*n)*j[1]/lo**2+2*n*n*j[0]/lo**3
    L2=j[4]+2*j[3]/lo+(1+2*n*n)*j[2]/lo**2+(1+2*n*n)*j[1]/lo**3+abs(n**4-4*n*n)*j[0]/lo**4
    L2r=j[5]+2*j[4]/lo+(3+2*n*n)*j[3]/lo**2+3*(1+2*n*n)*j[2]/lo**3+abs(n**4-10*n*n-3)*j[1]/lo**4+4*abs(n**4-4*n*n)*j[0]/lo**5
    return j[:3],[L,Lr,n*L/lo,L2,L2r,n*L2/lo]

def integral_square(p,r,h,weight):
    # Exact polynomial integral (r+z)^weight p(z)^2.
    rr=arb_poly([r,1]);power=arb_poly([1])
    for _ in range(weight):power*=rr
    coeff=(p*p*power).coeffs()
    value=sum((2*coeff[k]*h**(k+1)/(k+1) for k in range(0,len(coeff),2)),arb(0))
    assert value.is_finite() and value.upper()>=0
    return value.upper()

def panel(index):
    cc=CONF;ratio=Q(cc['ratio']);aa=rational_arb(Q(cc['rmin']))*rational_arb(ratio)**index
    bb=rational_arb(Q(cc['rmin']))*rational_arb(ratio)**(index+1)
    if bb>rational_arb(Q(cc['rmax'])):bb=rational_arb(Q(cc['rmax']))
    r=(aa+bb)/2;h=(bb-aa)/2;R=r/16
    assert h>0 and h<R/2
    majors,outer=E.mode_majorants(r)
    mm=majors['rho',0,0]
    bound={key:field_majorants(M,r,key[1]) for key,M in mm.items()}
    magnitude=sum((sum(js,arb(0))+sum(fs,arb(0)) for js,fs in bound.values()),arb(0))
    z=h/R;chosen=12;target=arb('1e-15')/(1+r)**6
    while magnitude*z**(chosen+1)/(1-z)>target and chosen<cc['max_degree']:chosen+=4
    assert chosen<=cc['max_degree'] and magnitude*z**(chosen+1)/(1-z)<target
    series=E.modes_taylor(r,degree=chosen+5)['rho',0,0]
    rr=arb_series([r,1],prec=chosen+6)
    tf=z**(chosen+1)/(1-z);vv=arb(0,h.abs_upper())
    # First four norm energies are ||Delta rho||², ||gradDelta rho||²,
    # ||Delta²rho||², ||gradDelta²rho||².
    energy=[arb(0) for _ in range(6)]
    hess_rad=arb(0);hess_mix=arb(0);hess_tan=arb(0);remmax=arb(0)
    mass1=2*r*h;mass3=2*r**3*h+2*r*h**3
    for key,f in series.items():
        kind,n=key;js,fs=bound[key]
        L=lap(f,rr,n);LL=lap(L,rr,n)
        fields=[L,L.derivative(),n*L/rr,LL,LL.derivative(),n*LL/rr]
        assert all(p.prec>=chosen+1 for p in fields)
        angular=2*arb.pi() if n==0 else arb.pi()
        for k,(pp,M) in enumerate(zip(fields,fs)):
            p=apoly(pp,chosen);rem=(M*tf).abs_upper()
            if rem>remmax:remmax=rem
            integ=integral_square(p,r,h,1)
            val=sq(integ.sqrt()+rem*mass1.sqrt())*angular
            slot=[0,1,1,2,3,3][k];energy[slot]+=val
            if k in [1,2,4,5]:
                integ3=integral_square(p,r,h,3)
                val3=sq(integ3.sqrt()+rem*mass3.sqrt())*angular
                energy[4 if k in [1,2] else 5]+=val3
        # Form polar Hessian components before enclosure. In particular the
        # linear n=1 origin mode cancels exactly from mixed/tangential terms.
        deriv=[f.derivative().derivative(),
               n*(f.derivative()/rr-f/(rr*rr)),
               f.derivative()/rr-n*n*f/(rr*rr)]
        lo=15*r/16
        hmaj=[js[2],n*(js[1]/lo+js[0]/lo**2),
              js[1]/lo+n*n*js[0]/lo**2]
        ranges=[]
        for pp,M in zip(deriv,hmaj):
            value=apoly(pp,chosen)(vv)+arb(0,(M*tf).abs_upper())
            assert value.is_finite();ranges.append(value.abs_upper())
        hess_rad+=ranges[0]
        hess_mix+=ranges[1]
        hess_tan+=ranges[2]
    H1=(1+4*bb*bb).sqrt()*(sq(hess_rad)+2*sq(hess_mix)+sq(hess_tan)).sqrt()
    assert H1.is_finite() and all(v.is_finite() for v in energy)
    return {'index':index,'degree':chosen,'r_center':r.str(32),'halfwidth':h.str(32),'energy_upper':{str(k):v.str(80) for k,v in enumerate(energy)},'H1_upper':H1.str(80),'max_remainder':remmax.str(30)}

def bindings():
    return {str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE.parent/'coercivity_residual'/'fields013.py',HERE.parent/'coercivity_residual'/'asymptotics013.py']}

def run(args):
    args.out.mkdir(parents=True,exist_ok=True);ratio=Q(args.ratio);rmin=Q(args.rmin);rmax=Q(args.rmax)
    panels=math.ceil(math.log(float(rmax/rmin))/math.log(float(ratio)))
    assert rmin*ratio**panels>=rmax>rmin*ratio**(panels-1)
    cc={'bits':args.bits,'max_degree':args.max_degree,'ratio':args.ratio,'rmin':args.rmin,'rmax':args.rmax,'panels':panels,'source_hashes':SOURCE_HASHES,'code_hashes':bindings()}
    fp=args.out/'configuration.json'
    if fp.exists():assert json.loads(fp.read_text())==cc
    else:fp.write_text(json.dumps(cc,indent=2)+'\n')
    N=min(args.max_panels,panels) if args.max_panels else panels;st=time.time();done=0
    with ProcessPoolExecutor(args.workers,initializer=initialize,initargs=(cc,)) as pool:
        for j in range(0,N,args.chunk):
            indices=list(range(j,min(j+args.chunk,N)));dest=args.out/f'chunk_{indices[0]:05d}_{indices[-1]:05d}.json'
            if dest.exists():
                old=json.loads(dest.read_text());assert old['configuration']==cc and [r['index'] for r in old['rows']]==indices
                done+=len(indices);continue
            rows=[]
            for row in pool.map(panel,indices,chunksize=1):
                rows.append(row)
                if len(rows)%4==0:print('completed',done+len(rows),'of',N,'seconds',round(time.time()-st,2),'degree',row['degree'],flush=True)
            dest.write_text(json.dumps({'configuration':cc,'rows':rows,'finished_utc':datetime.now(timezone.utc).isoformat()},indent=2)+'\n');done+=len(rows)
    if done==panels:assemble(args.out)

def tail_norm(exp,i,j,r,weight=0):
    rr=arb(r);v=arb(0)
    terms=[(arb(abs(a)),p) for (kind,n,p),a in exp.field('rho',i,j).items()]
    terms.extend(exp.remainder_terms('rho',i,j,rr))
    for a,p in terms:
        power=p+weight;den=2*power+2 if exp.side=='origin' else -2*power-2
        if a==0:continue
        assert den>0
        v+=a*rr**rational_arb(power+1)/rational_arb(den).sqrt()
    return (2*arb.pi()).sqrt()*v

def lap_tail_energy(exp,s,r,gradient=False,weight=0):
    # On a restricted origin/exterior region, global Parseval identities
    # cannot replace the actual Laplacian expression by tensor derivatives.
    # Bound its explicit Cartesian sum by Minkowski instead.
    out=arb(0)
    for axis in ([0,1] if gradient else [None]):
        val=arb(0)
        for k in range(s+1):
            i=2*k+(axis==0);j=2*(s-k)+(axis==1)
            val+=math.comb(s,k)*tail_norm(exp,i,j,r,weight)
        out+=sq(val)
    return out

def weighted_grad_lap_tail(exp,s,r):
    return lap_tail_energy(exp,s,r,gradient=True,weight=1)

def point_weighted(exp,i,j,r,weight):
    rr=arb(r);v=arb(0)
    terms=[(arb(abs(a)),p) for (kind,n,p),a in exp.field('rho',i,j).items()]
    terms.extend(exp.remainder_terms('rho',i,j,rr))
    for a,p in terms:
        if a==0:continue
        assert p+weight>=0 if exp.side=='origin' else p+weight<0
        v+=a*rr**rational_arb(p+weight)
    return v

def moment(D,m,sigma):
    s=arb(sigma);C=1/(2*(arb.pi()*s/2).cos().sqrt()*(1-s)**((1-s)/4)*(1+s)**((1+s)/4))
    return C*D[m]**((1-s)/2)*D[m+2]**((1+s)/2)

def assemble(outdir):
    cc=json.loads((outdir/'configuration.json').read_text());assert cc['code_hashes']==bindings();ctx.prec=cc['bits']
    rows={}
    for p in sorted(outdir.glob('chunk_*.json')):
        rec=json.loads(p.read_text());assert rec['configuration']==cc
        for r in rec['rows']:
            if r['index'] in rows:assert rows[r['index']]==r
            rows[r['index']]=r
    assert sorted(rows)==list(range(cc['panels']))
    core=[sum((arb(rows[i]['energy_upper'][str(k)]) for i in sorted(rows)),arb(0)) for k in range(6)]
    e=Evaluator(cc['bits'],max_density_order=0,max_velocity_order=-1)
    near=Expansion(e,'origin',degree=20);far=Expansion(e,'far',degree=20)
    totals=core.copy();tails={};Hmax=max((arb(r['H1_upper']).upper() for r in rows.values()))
    for name,exp,r in [('origin',near,cc['rmin']),('exterior',far,cc['rmax'])]:
        extra=[lap_tail_energy(exp,1,r),lap_tail_energy(exp,1,r,gradient=True),
               lap_tail_energy(exp,2,r),lap_tail_energy(exp,2,r,gradient=True)]
        extra.extend([weighted_grad_lap_tail(exp,s,r) for s in [1,2]])
        tails[name]=[v.str(80) for v in extra]
        totals=[a+b for a,b in zip(totals,extra)]
        wt=0 if name=='origin' else 1
        xx=point_weighted(exp,2,0,r,wt);xy=point_weighted(exp,1,1,r,wt);yy=point_weighted(exp,0,2,r,wt)
        factor=(1+4*arb(r)**2).sqrt() if name=='origin' else (4+arb(r)**-2).sqrt()
        Hbound=factor*(sq(xx)+2*sq(xy)+sq(yy)).sqrt();tails[name+'_H1_bound']=Hbound.str(80)
        if Hbound.upper()>Hmax:Hmax=Hbound.upper()
    Db={j+1:totals[j].sqrt() for j in range(4)}
    Dxb={2:(totals[4]+4*totals[0]).sqrt(),4:(totals[5]+16*totals[2]).sqrt()}
    A={}
    for sig in ['0','1/10']:
        key='2' if sig=='0' else '21/10'
        A[key]=moment(Db,2,sig)+2*moment(Dxb,2,sig)+4*moment(Db,1,sig)
    ratio=arb('3.813e-7')/arb('.387');q=arb(21)/10;cq=q*(q-1)/2
    parts=[q*Hmax*ratio**(1/q),cq*A['2']*ratio**(1-arb(1)/21),cq*A['21/10']*ratio]
    result={'status':'CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS','configuration':cc,'H1_upper':Hmax.str(80),'D_b_L2_upper':{str(k):v.str(80) for k,v in Db.items()},'D_xb_L2_upper':{str(k):v.str(80) for k,v in Dxb.items()},'A_s_upper':{k:v.str(80) for k,v in A.items()},'core_energies':[v.str(80) for v in core],'tail_energies':tails,'example_R_over_M':ratio.str(60),'example_tame_rate_parts':[v.str(70) for v in parts],'example_tame_rate_sum':sum(parts,arb(0)).str(70),'finished_utc':datetime.now(timezone.utc).isoformat(),'warning':'The coefficient constants and displayed source-commutator estimate are certified. Full IPM energy, inverse, nonlinear closure, and existence are separate obligations.'}
    (outdir/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--workers',type=int,default=4)
    ap.add_argument('--bits',type=int,default=512);ap.add_argument('--max-degree',type=int,default=160);ap.add_argument('--ratio',default='201/199')
    ap.add_argument('--rmin',default='1/100000');ap.add_argument('--rmax',default='100000');ap.add_argument('--chunk',type=int,default=16)
    ap.add_argument('--max-panels',type=int);ap.add_argument('--assemble',action='store_true')
    args=ap.parse_args()
    if args.assemble:assemble(args.out)
    else:run(args)

if __name__=='__main__':main()
