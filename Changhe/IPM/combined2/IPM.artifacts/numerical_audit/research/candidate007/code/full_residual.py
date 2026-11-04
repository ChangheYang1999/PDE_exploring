"""Independent complete radial Fourier residual and Arb moment enclosure.

Uses only canonical.json reconstructed from exact candidate strings by this lane.
One process, no omitted angular modes, no numerical integration.
"""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
from pathlib import Path
import gzip
import json
import os
import time
from flint import fmpq as Q, fmpq_poly as Poly, arb, arb_poly, ctx

ROOT=Path(__file__).resolve().parents[3]
INPUT=ROOT/'research/candidate007/verification/canonical.json'
OUTPUT=ROOT/'research/candidate007/verification'
ZERO=Poly([])
T=Poly([0,1])
U=Poly([1,-1])
EXPECTED='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')


def digest(p):
    return sha256(Path(p).read_bytes()).hexdigest()


def clean(a):
    return {n:p for n,p in a.items() if p}


def add(a,b,factor=Q(1)):
    out=dict(a)
    for n,p in b.items():
        out[n]=out.get(n,ZERO)+factor*p
    return clean(out)


def radial(p,e,a):
    return e*p-2*a*T*p+2*T*U*p.derivative()


def derivative(f,e,a,axis):
    out={}
    for n,p in f.items():
        d=radial(p,e,a)
        out[n-1]=out.get(n-1,ZERO)+(d+n*p)/2
        out[n+1]=out.get(n+1,ZERO)+(d-n*p)/2*(1 if axis=='x' else -1)
    return clean(out)


def many(f,e,a,axes):
    for axis in axes:
        f=derivative(f,e,a,axis)
        e-=1
    return f


def normalize(f):
    out={}
    for n,p in f.items():
        assert p[0]==0 and p[1]==0
        out[n]=Poly(list(p)[2:])
    return clean(out)


def pack(f,B):
    shift=max(map(abs,f),default=0)
    if not f:
        return ZERO,shift
    size=(2*shift)*B+max(p.degree() for p in f.values())+1
    coeff=[Q(0)]*size
    for n,p in f.items():
        offset=(n+shift)*B
        for k,v in enumerate(p):
            coeff[offset+k]=v
    return Poly(coeff),shift


def packed_convolve(f,g):
    if not f or not g:
        return {}
    B=max(p.degree() for p in f.values())+max(p.degree() for p in g.values())+1
    ff,sf=pack(f,B);gg,sg=pack(g,B)
    product=ff*gg
    out={}
    for block in range(product.degree()//B+1):
        vals=[product[block*B+k] for k in range(B)]
        p=Poly(vals)
        if p:
            out[block-sf-sg]=p
    return out


def direct_convolve(f,g):
    out={}
    for n,p in f.items():
        for m,q in g.items():
            out[n+m]=out.get(n+m,ZERO)+p*q
    return clean(out)


def serial_field(f):
    return {str(n):list(map(str,p)) for n,p in sorted(f.items())}


def calibration():
    f={-2:Poly([1,3]),0:Poly([-2,0,1]),4:Poly([Q(1,3)])}
    g={-3:Poly([2,-1,2]),2:Poly([1,0,Q(1,7)])}
    assert packed_convolve(f,g)==direct_convolve(f,g)
    # chi=x^2*y^2 corresponds to e=0,a=-2 and t^2 times its harmonics.
    fixture={0:T*T/8,4:-T*T/16,-4:-T*T/16}
    xxy=normalize(many(fixture,0,Q(-2),'xxy'))
    yyy=normalize(many(fixture,0,Q(-2),'yyy'))
    xyy=normalize(many(fixture,0,Q(-2),'xyy'))
    rho=add(yyy,xxy,-Q(1))
    assert rho=={-1:Poly([-2]),1:Poly([2])}
    assert xyy=={-1:Poly([-2]),1:Poly([-2])}
    assert xxy=={-1:Poly([2]),1:Poly([-2])}
    # F for chi=x^2*y^2 has rho=-4y, u=(-4x,4y), F=-(4c+12)y.
    c=Q(7,4)
    rx=derivative(rho,1,Q(0),'x')
    ry={n:-p for n,p in derivative(rho,1,Q(0),'y').items()}
    linear={n:c*radial(p,1,Q(0))-p for n,p in rho.items()}
    nonlinear=add(packed_convolve(xyy,rx),packed_convolve(xxy,ry))
    assert add(linear,nonlinear)=={-1:Poly([-Q(19,2)]),1:Poly([Q(19,2)])}


def assemble():
    start=stamp();tick=time.monotonic()
    data=json.loads(INPUT.read_text())
    assert data['source_sha256']==EXPECTED
    c=Q(data['cl_exact']);lam=1-1/c
    raw=defaultdict(lambda:defaultdict(dict))
    for j,m,k,a in data['coefficients']:
        aa=Q(a)
        if m:
            raw[j][2*m][k]=aa/2;raw[j][-2*m][k]=aa/2
        else:
            raw[j][0][k]=aa
    chi={}
    for j,modes in raw.items():
        chi[j]={n:Poly([d.get(k,Q(0)) for k in range(max(d)+1)]) for n,d in modes.items()}
    fields={}
    for j in sorted(chi):
        p=(4-(j+1)*lam)/2
        a=(j+1)*lam/2
        xxy=normalize(many(chi[j],0,-p,'xxy'))
        yyy=normalize(many(chi[j],0,-p,'yyy'))
        xyy=normalize(many(chi[j],0,-p,'xyy'))
        rho=add(yyy,xxy,-Q(1))
        fields[j]={'rho':rho,'ux':xyy,'uy':xxy,
                   'rx':derivative(rho,1,a,'x'),
                   'ry':{n:-v for n,v in derivative(rho,1,a,'y').items()}}
        print(stamp(),'fields branch',j,'modes',len(rho),flush=True)
    residual={}
    for j,f in fields.items():
        a=(j+1)*lam/2
        residual[j]=clean({n:c*radial(p,1,a)-p for n,p in f['rho'].items()})
    for i,f in fields.items():
        for j,g in fields.items():
            J=i+j+1
            v=add(packed_convolve(f['ux'],g['rx']),packed_convolve(f['uy'],g['ry']))
            residual[J]=add(residual.get(J,{}),v)
        print(stamp(),'nonlinear source branch',i,'complete',flush=True)
    sine={}
    endpoints=[]
    for J,f in sorted(residual.items()):
        for n,p in f.items():
            assert n%2 and f.get(-n,ZERO)==-p
        sine[J]={n:-2*p for n,p in f.items() if n>0}
        for n,p in sine[J].items():
            pu=p(U)
            order=next(k for k,v in enumerate(pu) if v)
            diagonal=(J+1)*lam+2*order-3
            assert diagonal>-1
            endpoints.append({'J':J,'n':n,'degree':p.degree(),'endpoint_order':order,
                              'integral_exponent_exact':str(diagonal)})
    # Compare every finite far-sector coefficient with independent homogeneous algebra.
    structure=json.loads((OUTPUT/'structure.json').read_text())
    for row in structure['sectors']:
        J,N=row['J'],row['N']
        got={str(n):str(p(U)[N]) for n,p in sine.get(J,{}).items() if p(U)[N]}
        assert got==row['sine_coefficients'],(J,N)
    result={'source_sha256':EXPECTED,'canonical_sha256':digest(INPUT),
            'code_sha256':digest(__file__),'cl_exact':str(c),'lambda_exact':str(lam),
            'rho_phase':'i times the complex Fourier polynomial',
            'fields':{str(j):{name:serial_field(f) for name,f in ff.items()} for j,ff in sorted(fields.items())},
            'residual_sine':{str(j):serial_field(f) for j,f in sorted(sine.items())}}
    dest=OUTPUT/'full_residual.json.gz'
    with dest.open('xb') as raw_file:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw_file,mtime=0) as f:
            f.write((json.dumps(result,separators=(',',':'))+'\n').encode())
    summary={'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,
             'source_sha256':EXPECTED,'canonical_sha256':digest(INPUT),'code_sha256':digest(__file__),
             'residual_sha256':digest(dest),'residual_file':'research/candidate007/verification/full_residual.json.gz',
             'fourier_positive_modes':sorted({n for f in sine.values() for n in f}),
             'branch_count':len(sine),'nonzero_polynomials':sum(map(len,sine.values())),
             'exact_far_field_comparison':True,'origin_divisibility':True,'endpoints':endpoints}
    (OUTPUT/'full_assembly.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(stamp(),'assembly completed',summary['elapsed_seconds'],'seconds',flush=True)
    return result


def load_residual():
    with gzip.open(OUTPUT/'full_residual.json.gz','rt') as f:
        return json.load(f)


def ball_record(x,digits=80):
    assert x.is_finite()
    return {'ball':x.str(digits),'lower_exact':str(x.lower().fmpq()),
            'upper_exact':str(x.upper().fmpq()),'relative_accuracy_bits':int(x.rel_accuracy_bits())}


def moments(data,bits):
    start=stamp();tick=time.monotonic();ctx.prec=bits
    lam=Q(data['lambda_exact'])
    by_mode=defaultdict(list)
    for j,modes in data['residual_sine'].items():
        J=int(j)
        for n,coef in modes.items():
            p=Poly(list(map(Q,coef)))(U)
            order=next(k for k,v in enumerate(p) if v)
            pp=Poly(list(p)[order:])
            a=(J+1)*lam/2+order
            assert 2*a-3>-1
            by_mode[int(n)].append((J,a,arb_poly([arb(v) for v in pp])))
    total=arb(0);rweighted=arb(0);hardy=arb(0);mode_rows=[]
    for n,terms in sorted(by_mode.items()):
        integral=arb(0);rintegral=arb(0);groups=0
        for j,(J,a,p) in enumerate(terms):
            for K,b,q in terms[j:]:
                product=p*q*arb_poly([1,-1])
                expo=a+b-3
                assert expo>-1
                base=arb(expo+1)
                v=arb(0)
                for degree,coefficient in enumerate(product):
                    v+=coefficient/(base+degree)
                multiplicity=1 if J==K else 2
                integral+=multiplicity*v
                # Complete rF moment: one further (1-u)/u.
                assert expo-1>-1
                rproduct=product*arb_poly([1,-1])
                vv=arb(0)
                for degree,coefficient in enumerate(rproduct):
                    vv+=coefficient/(base-1+degree)
                rintegral+=multiplicity*vv
                groups+=1
        assert integral>0 and rintegral>0,(n,integral,rintegral)
        sq=arb.pi()*integral/2;rsq=arb.pi()*rintegral/2
        total+=sq;rweighted+=rsq;hardy+=rsq/(n*n)
        mode_rows.append({'n':n,'groups':groups,'L2_squared':ball_record(sq),
                          'rF_squared':ball_record(rsq)})
        if n%20==1:
            print(stamp(),'moment mode',n,'L2',total.sqrt().str(20),flush=True)
    final={'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,
           'source_sha256':EXPECTED,'code_sha256':digest(__file__),
           'residual_sha256':digest(OUTPUT/'full_residual.json.gz'),'precision_bits':bits,
           'angular_modes':len(by_mode),'max_angular_mode':max(by_mode),'complete_whole_plane':True,
           'L2_squared':ball_record(total),'L2':ball_record(total.sqrt()),
           'rF_squared':ball_record(rweighted),'rF':ball_record(rweighted.sqrt()),
           'angular_Hardy_upper_proxy':ball_record(hardy.sqrt()),'modes':mode_rows,
           'scope':'Full analytic moment enclosure; Hardy proxy is only an upper bound for the negative norm.'}
    dest=OUTPUT/f'moments_{bits}.json'
    with dest.open('x') as f:f.write(json.dumps(final,indent=2)+'\n')
    print(stamp(),'L2=',total.sqrt().str(60),'seconds',final['elapsed_seconds'],flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--resume-moments',action='store_true')
    parser.add_argument('--bits',type=int,default=2048)
    args=parser.parse_args()
    calibration()
    data=load_residual() if args.resume_moments else assemble()
    moments(data,args.bits)
