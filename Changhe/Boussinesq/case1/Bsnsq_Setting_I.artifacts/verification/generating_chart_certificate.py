"""Exact rational compact Bernstein certificate of A/E^(1/3)>0.

No sampled minimum is used as a proof. Reads exact binary inputs and records
an optional exact completion of c[2,0]. Integer subdivision denominators are
retained. A failed budget is OPEN. No coupled PDE conclusion follows.
"""
from fractions import Fraction as F
from math import comb,lcm
from pathlib import Path
import argparse,datetime,hashlib,json,time,platform
import numpy as np


def polyadd(*polys):
    out={}
    for p in polys:
        for key,v in p.items():out[key]=out.get(key,F(0))+v
    return {k:v for k,v in out.items() if v}

def polyscale(p,c):return {k:c*v for k,v in p.items() if c*v}

def polymul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in out.items() if v}


def exact_polynomial(coeff,a0):
    c=coeff;q=[F(2-j,6) for j in range(len(c))]
    p=sum(c[j][0]*q[j] for j in range(len(c)));d=p*(a0-70)/14
    one={(0,0):F(1)};u={(0,0):F(1),(6,0):F(-1),(0,3):F(-1)};v={(0,3):F(1)}
    uv=polymul(u,v);B={}
    for j in range(len(c)):
        for k in range(len(c[0])):
            h=q[j]-k
            P=polyadd(polyscale(one,F(6*k+1)),polyscale(u,2*h*(6*k+1)),polyscale(v,6*h),polyscale(uv,12*h*(h-1)))
            B=polyadd(B,polymul({(j,3*k):c[j][k]},P))
    Q=polyadd(one,polyscale(u,-2),polyscale(v,-2),polyscale(uv,8))
    return polyadd(B,polymul({(6,1):3*d},Q)),p,d


def bernstein_root(poly):
    n=max(i for i,j in poly);m=max(j for i,j in poly)
    b=[[F(0) for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            b[i][j]=sum(a*F(comb(i,p),comb(n,p))*F(comb(j,q),comb(m,q)) for (p,q),a in poly.items() if p<=i and q<=j)
    den=1
    for row in b:
        for x in row:den=lcm(den,x.denominator)
    return [[int(x*den) for x in row] for row in b],den


def split_curve(values):
    n=len(values)-1;left=[];right=[]
    for i in range(n+1):
        left.append(sum(comb(i,j)*values[j] for j in range(i+1))*(2**(n-i)))
        right.append(sum(comb(n-i,j)*values[i+j] for j in range(n-i+1))*(2**i))
    return left,right


def split_tensor(b,den,axis):
    n=len(b)-1;m=len(b[0])-1
    if axis==0:
        cols=[split_curve([b[i][j] for i in range(n+1)]) for j in range(m+1)]
        return [[cols[j][0][i] for j in range(m+1)] for i in range(n+1)],[[cols[j][1][i] for j in range(m+1)] for i in range(n+1)],den*2**n
    rows=[split_curve(row) for row in b]
    return [row[0] for row in rows],[row[1] for row in rows],den*2**m


def power_value(poly,t,w):return sum(a*t**i*w**j for (i,j),a in poly.items())

def bernstein_value(b,den,s,z):
    n=len(b)-1;m=len(b[0])-1
    return sum(F(b[i][j],den)*comb(n,i)*s**i*(1-s)**(n-i)*comb(m,j)*z**j*(1-z)**(m-j) for i in range(n+1) for j in range(m+1))


def self_check(poly,b,den):
    checks=[]
    points=[(F(0),F(0)),(F(1),F(1)),(F(1,3),F(2,7)),(F(5,8),F(4,9))]
    for t,w in points:checks.append(power_value(poly,t,w)==bernstein_value(b,den,t,w))
    for axis in [0,1]:
        l,r,d=split_tensor(b,den,axis)
        for side,ch in enumerate([l,r]):
            for s,z in points:
                t=(s+side)/2 if axis==0 else s;w=(z+side)/2 if axis==1 else z
                checks.append(power_value(poly,t,w)==bernstein_value(ch,d,s,z))
    if not all(checks):raise AssertionError('Exact Bernstein manufactured identity failed')
    return dict(exact_equalities=len(checks),passed=True)


def certify(poly,max_nodes=20000,max_seconds=240):
    start=time.monotonic();b,den=bernstein_root(poly);check=self_check(poly,b,den)
    stack=[('',F(0),F(1),F(0),F(1),b,den)];leaves=[];lower=None;visited=0;negative_sample=None
    while stack and visited<max_nodes and time.monotonic()-start<max_seconds:
        path,tl,th,wl,wh,b,d=stack.pop();visited+=1
        if tl**6+wl**3>1:
            leaves.append(dict(path=path,kind='outside'));continue
        minimum=min(min(row) for row in b)
        if minimum>0:
            bound=F(minimum,d);lower=bound if lower is None else min(lower,bound)
            leaves.append(dict(path=path,kind='positive',minimum_numerator=str(minimum),denominator=str(d)));continue
        # An exact negative sample is conclusive for failure of strict positivity.
        # Sampling success is never used as a certificate.
        t=(tl+th)/2;w=(wl+wh)/2
        if t**6+w**3<=1:
            value=power_value(poly,t,w)
            if value<=0:
                negative_sample=dict(t=str(t),w=str(w),value=str(value));break
        axis=0 if len(path)%2==0 else 1
        left,right,dd=split_tensor(b,d,axis)
        if axis==0:
            mid=(tl+th)/2
            stack.append((path+'1',mid,th,wl,wh,right,dd));stack.append((path+'0',tl,mid,wl,wh,left,dd))
        else:
            mid=(wl+wh)/2
            stack.append((path+'3',tl,th,mid,wh,right,dd));stack.append((path+'2',tl,th,wl,mid,left,dd))
    success=not stack and negative_sample is None
    return dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),verdict='CONFIRMED_CHART' if success else ('REFUTED_CHART' if negative_sample else 'OPEN'),visited=visited,remaining=len(stack),leaves=leaves,negative_sample=negative_sample,lower_bound=str(lower) if success else None,lower_bound_float=float(lower) if success else None,seconds=time.monotonic()-start,degree=[len(b)-1,len(b[0])-1],self_check=check,scope='Exact rational chart only, not the remaining vorticity PDE. Positive leaves cover D only when the finite tree is complete.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--out',required=True);ap.add_argument('--complete-center',action='store_true');ap.add_argument('--max-seconds',type=float,default=240);ap.add_argument('--max-nodes',type=int,default=20000);args=ap.parse_args()
    source=Path(args.source);dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    if source.suffix=='.npz':
        with np.load(source) as raw:c=np.asarray(raw['coeff']);a0=float(raw['a0'])
    else:
        raw=json.loads(source.read_text());c=np.asarray(raw['coeff']);a0=raw['a0']
    if c.ndim==1:c=c[:,None]
    exact=[[F.from_float(float(v)) for v in row] for row in c];a0=F.from_float(float(a0));original=exact[2][0]
    if args.complete_center:exact[2][0]=1-sum(exact[j][0] for j in range(len(exact)) if j!=2)
    if not a0:raise ValueError("a0 must be nonzero for the A1 family certificate")
    poly,p,d=exact_polynomial(exact,a0)
    inputs=dict(a0_nonzero=bool(a0),software=dict(python=platform.python_version(),numpy=np.__version__),input_conversion='Numeric JSON and npz values first converted to binary64, then exact rationals.',source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),coeff=[[str(v) for v in row] for row in exact],a0=str(a0),p=str(p),d=str(d),center_sum=str(sum(row[0] for row in exact)),exact_center_completion=args.complete_center,c20_change=str(exact[2][0]-original),polynomial=[dict(t_power=i,w_power=j,coefficient=str(v)) for (i,j),v in sorted(poly.items())],code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (dest/'input.json').write_text(json.dumps(inputs,indent=2)+'\n')
    result=certify(poly,args.max_nodes,args.max_seconds)
    result['input_sha256']=hashlib.sha256((dest/'input.json').read_bytes()).hexdigest()
    (dest/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='leaves'}),flush=True)
if __name__=='__main__':main()
