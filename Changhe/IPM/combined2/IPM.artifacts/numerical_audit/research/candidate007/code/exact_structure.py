"""Independent exact conversion and homogeneous Fourier constraint audit."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import time
from flint import fmpq as Q, fmpq_poly, fmpq_mat

ROOT = Path(__file__).resolve().parents[3]
EXPECTED = 'ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def digest(p):
    return sha256(Path(p).read_bytes()).hexdigest()


def binom_q(q, n):
    a = Q(1)
    for k in range(n):
        a = a * (q-k) / (k+1)
    return a


def legendre_rodrigues(n):
    return [Q((-1)**(n-k)*comb(n,k)*comb(n+k,k)) for k in range(n+1)]


def legendre_recurrence(n):
    z = fmpq_poly([-1,2]); a = fmpq_poly([1]); b = z
    if n == 0:
        return list(a)
    for k in range(1,n):
        a,b = b, ((2*k+1)*z*b-k*a)/(k+1)
    return list(b)


def canonicalize(data):
    can = defaultdict(Q)
    blocks = defaultdict(list)
    checked = set()
    for g in data['generators']:
        kind,*args = g['spec']
        if kind == 'mono':
            h, = args
            poly = [Q(0)]*h + [Q(1)]
        elif kind == 'leg':
            w,n = args
            if n not in checked:
                assert legendre_rodrigues(n) == legendre_recurrence(n)
                checked.add(n)
            poly = [Q(0)]*w + legendre_rodrigues(n)
        else:
            raise ValueError('unsupported generator kind: '+kind)
        j,m,a = int(g['j']),int(g['m']),Q(g['coef'])
        blocks[j,m].append(poly)
        for h,v in enumerate(poly):
            if v:
                can[j,m,m+h] += a*v
    can = {k:v for k,v in can.items() if v}
    return can,blocks,sorted(checked)


def clean(a):
    return {n:v for n,v in a.items() if v}


def plus(a,b,scale=Q(1)):
    out=defaultdict(Q,a)
    for n,v in b.items():
        out[n]+=scale*v
    return clean(out)


def derivative(a,degree,axis):
    # y differentiation strips one factor i, x strips none.
    out=defaultdict(Q)
    for n,v in a.items():
        out[n-1] += v*(degree+n)/2
        out[n+1] += v*(degree-n)/2 * (1 if axis=='x' else -1)
    return clean(out)


def diff_many(a,degree,axes):
    for axis in axes:
        a=derivative(a,degree,axis)
        degree-=1
    return a


def convolve(a,b):
    out=defaultdict(Q)
    for n,v in a.items():
        for m,w in b.items():
            out[n+m]+=v*w
    return clean(out)


def homogeneous_fields(chi,q):
    xxy=diff_many(chi,q,'xxy')
    yyy=diff_many(chi,q,'yyy')
    xyy=diff_many(chi,q,'xyy')
    # rho = i*(-DxDxTy+TyTyTy); ux=DxTyTy; uy=i*DxDxTy.
    rho=plus(yyy,xxy,-Q(1))
    return {'rho':rho,'ux':xyy,'uy':xxy,
            'rx':derivative(rho,q-3,'x'),
            'ry':{n:-v for n,v in derivative(rho,q-3,'y').items()}}


def audit(input_path,output_dir):
    start=stamp(); tick=time.monotonic()
    data=json.loads(input_path.read_text())
    input_hash=digest(input_path)
    assert input_hash==EXPECTED
    c=Q(data['cl_exact']); gamma=1/c; lam=1-gamma
    p=lambda j:(3+gamma-j*lam)/2
    can,blocks,leg_checks=canonicalize(data)
    canonical_file=output_dir/'canonical.json'
    canonical_doc={'source_sha256':input_hash,'cl_exact':str(c),
        'coefficients':[[j,m,k,str(a)] for (j,m,k),a in sorted(can.items())]}
    canonical_file.write_text(json.dumps(canonical_doc,indent=2)+'\n')
    origin=[Q(0)]*3
    for (j,m,k),a in can.items():
        if k<=2:
            assert m<=2
            origin[m]+=a*binom_q(p(j)-k,2-k)
    ell=8*origin[0]-24*origin[2]
    a0=-32*origin[0]+24*origin[1]
    assert c+ell==1 and a0>0
    assert a0*(c+ell-1)==0
    ranks=[]
    for (j,m),polys in sorted(blocks.items()):
        degree=max(map(len,polys))-1
        mat=fmpq_mat([[col[row] if row<len(col) else Q(0) for col in polys]
                      for row in range(degree+1)])
        rank=mat.rank()
        ranks.append({'j':j,'m':m,'columns':len(polys),'rank':rank,'degree':degree})
    for j in range(8):
        for jj in range(j):
            assert ((j-jj)*lam/2).denominator!=1
    # Calibration: x^2+y^2, degree 2, has Dx=2x and Dy=2y.
    assert derivative({0:Q(1)},Q(2),'x')=={-1:Q(1),1:Q(1)}
    assert derivative({0:Q(1)},Q(2),'y')=={-1:Q(1),1:Q(-1)}
    # chi=x^2*y^2: cos(0)/8-cos(4theta)/8, degree 4.
    fixture={0:Q(1,8),4:Q(-1,16),-4:Q(-1,16)}
    fix=homogeneous_fields(fixture,Q(4))
    assert fix['rho']=={-1:Q(-2),1:Q(2)} # rho=-4y
    assert fix['ux']=={-1:Q(-2),1:Q(-2)} # ux=-4x
    assert fix['uy']=={-1:Q(2),1:Q(-2)}  # uy=4y
    raw=defaultdict(lambda:defaultdict(Q))
    for (j,m,k),a in can.items():
        for n in (0,1):
            z=a*binom_q(p(j)-k,n)
            if m:
                raw[j,n][2*m]+=z/2;raw[j,n][-2*m]+=z/2
            else:
                raw[j,n][0]+=z
    fields={key:homogeneous_fields(clean(v),2*p(key[0])-2*key[1]) for key,v in raw.items()}
    rows=[]
    for J,N in sorted([(j,0) for j in range(9)]+[(j,1) for j in range(4)],
                      key=lambda key: gamma-key[0]*lam-2*key[1],reverse=True):
        exponent=gamma-J*lam-2*N
        E={}
        if (J,N) in fields:
            E={n:(c*exponent-1)*v for n,v in fields[J,N]['rho'].items()}
        for j1 in range(8):
            j2=J-j1-1
            if not 0<=j2<8:
                continue
            for n1 in range(N+1):
                n2=N-n1
                f,g=fields[j1,n1],fields[j2,n2]
                E=plus(E,convolve(f['ux'],g['rx']))
                E=plus(E,convolve(f['uy'],g['ry']))
        E=clean(E)
        assert all(n%2 and E.get(-n,Q(0))==-v for n,v in E.items())
        # F=i sum E_n exp(in theta)=sum_{n>0} (-2E_n) sin(n theta).
        sine={n:-2*v for n,v in E.items() if n>0}
        expected_zero=(N==0 and J<=7) or (N==1 and J<=2)
        assert (not sine)==expected_zero
        row={'J':J,'N':N,'exponent_exact':str(exponent),'exponent_float':float(exponent),
             'exact_zero':not sine,'sine_coefficients':{str(n):str(v) for n,v in sorted(sine.items())},
             'sine_square_sum':str(sum((v*v for v in sine.values()),Q(0)))}
        rows.append(row)
        print('sector',J,N,'zero',not sine,'modes',len(sine),flush=True)
    out={'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,
         'input':'data/candidate007_exact.json','input_sha256':input_hash,
         'code_sha256':digest(__file__),'canonical_sha256':digest(canonical_file),
         'cl_exact':str(c),'generators':len(data['generators']),'nonzero_canonical':len(can),
         'legendre_degrees_crosschecked':leg_checks,'origin_quartic':list(map(str,origin)),
         'ell_exact':str(ell),'a0_exact':str(a0),'a0_float':float(a0),
         'origin_normalization_exact':str(c+ell-1),'Fy_origin_exact':'0',
         'generator_rank':sum(b['rank'] for b in ranks),
         'zero_potential_kernel_dimension':sum(b['columns']-b['rank'] for b in ranks),
         'blocks':ranks,'sectors':rows,'assertions_passed':True,
         'scope':'Exact finite structure only. No quantitative whole-plane norm bound.'}
    dest=output_dir/'structure.json'
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('complete',len(can),'a0',float(a0),'seconds',out['elapsed_seconds'],flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',type=Path,default=ROOT/'data/candidate007_exact.json')
    parser.add_argument('--output-dir',type=Path,default=ROOT/'research/candidate007/verification')
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    audit(args.input,args.output_dir)
