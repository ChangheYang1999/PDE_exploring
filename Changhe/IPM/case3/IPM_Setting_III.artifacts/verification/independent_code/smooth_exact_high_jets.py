"""Exact full-plane Taylor auditor; standalone derivation is result83.

No producer code or derivative/inverse matrices are imported. Rational inputs
come from a registered exact JSON extraction of the saved density formula.
"""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, math, sys
sys.set_int_max_str_digits(1000000)


def frac(v):
    if isinstance(v, dict):return F(int(v['numerator']), int(v['denominator']))
    return F(v)


def enc(v):
    v=F(v)
    return dict(numerator=str(v.numerator),denominator=str(v.denominator))


def polyadd(a,b):
    ans=[F(0)]*max(len(a),len(b))
    for j,v in enumerate(a):ans[j]+=v
    for j,v in enumerate(b):ans[j]+=v
    return ans


def cheb_to_w(co):
    co=list(map(frac,co));out=[F(0)]*len(co);t0=[F(1)];t1=[F(1),F(-2)]
    for n,c in enumerate(co):
        if n==0:t=t0
        elif n==1:t=t1
        else:
            t=polyadd([2*v for v in t1],[F(0)]+[-4*v for v in t1])
            t=polyadd(t,[-v for v in t0]);t0,t1=t1,t
        for j,v in enumerate(t):out[j]+=c*v
    return out


def clean(p):return {k:v for k,v in p.items() if v}


def derivative(p,axis):
    q=defaultdict(F)
    for powers,v in p.items():
        if powers[axis]:
            target=list(powers);target[axis]-=1
            q[tuple(target)]+=powers[axis]*v
    return clean(q)


def add(*polys):
    q=defaultdict(F)
    for p in polys:
        for k,v in p.items():q[k]+=v
    return clean(q)


def scale(p,c):return clean({k:v*c for k,v in p.items()})


def product(p,q,max_degree):
    z=defaultdict(F)
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            if i+j+k+l<=max_degree:z[(i+k,j+l)]+=v*w
    return clean(z)


def solve(inputs,J=5):
    L=frac(inputs['length']);alpha=frac(inputs['alpha']);ell=frac(inputs['cl'])
    assert L>0 and 0<alpha<F(1,2) and ell>1
    supplied=inputs['chebyshev_coefficients'];M=len(supplied)
    converted=[cheb_to_w(c) for c in supplied[:J+3]]
    def P(k):return converted[k] if k<len(converted) else [F(0)]
    rho=defaultdict(F)
    for k in range(min(M,J+1)):
        radial=[]
        for h in range(J-k+1):
            val=F(0)
            for l,C in enumerate(P(k)):
                b=alpha*(l+1)+k;term=F(1)
                for z in range(h):term*=-F(b+z,z+1)
                val+=C*term
            radial.append(val/L**(2*k+2*h))
        for h,v in enumerate(radial):
            for z in range(k+1):
                vc=v*((-1)**z)*math.comb(2*k,2*z)
                for t in range(h+1):
                    rho[(2*k-2*z+2*t,2*z+1+2*h-2*t)]+=vc*math.comb(h,t)
    rho=clean(rho);a=rho.get((0,1),F(0));moments=[]
    for j in range(1,J+2):
        v=F(0);pj=P(j);pk=P(j+1)
        for l in range(max(len(pj),len(pk))):
            c=pj[l] if l<len(pj) else F(0);d=pk[l] if l<len(pk) else F(0)
            v+=(c-d)/(l+1+F(j-1)/alpha)+d/(l+1+F(j)/alpha)
        I=L**(2-2*j)*v/(4*alpha)
        d=a if j==1 else sum(P(j-1),F(0))/(2*L**(2*j-2))
        moments.append(dict(n=2*j,I=I,d=d,h=-d/(8*j)+I/2))
    rx=derivative(rho,0);psi={}
    for m in range(1,J+2):
        aa=[F(1)];bb=[F(0)]
        for j in range(m-1):
            fx=(2*j+3)*(2*j+2);fy=(2*m-2*j-1)*(2*m-2*j-2)
            source=rx.get((2*j+1,2*m-2*j-3),F(0))
            aa.append(-F(fy,fx)*aa[-1]);bb.append((-source-fy*bb[-1])/fx)
        weights=[F((-1)**(m-j+1),2**(2*m-1))for j in range(m)]
        denominator=sum((w*v for w,v in zip(weights,aa)),F(0));assert denominator
        q0=(moments[m-1]['h']-sum((w*v for w,v in zip(weights,bb)),F(0)))/denominator
        coeffs=[v*q0+b for v,b in zip(aa,bb)]
        assert sum((w*v for w,v in zip(weights,coeffs)),F(0))==moments[m-1]['h']
        for j,q in enumerate(coeffs):psi[(2*j+1,2*m-2*j-1)]=q
    psi=clean(psi)
    poisson=add(derivative(derivative(psi,0),0),derivative(derivative(psi,1),1),rx)
    assert not poisson,poisson
    u1=scale(derivative(psi,1),F(-1));u2=derivative(psi,0)
    w1=add(u1,{(1,0):ell});w2=add(u2,{(0,1):ell})
    R=add(product(w1,rx,2*J+1),product(w2,derivative(rho,1),2*J+1),scale(rho,F(-1)))
    c=psi.get((1,1),F(0));delta=ell+c-1
    assert R.get((0,1),F(0))==a*delta
    return dict(rho=rho,psi=psi,U1=u1,U2=u2,R=R,a=a,c=c,delta=delta,moments=moments,poisson=poisson)


def serial_poly(p):
    return [dict(x_power=i,y_power=j,value=enc(v),approx=float(v))for (i,j),v in sorted(p.items(),key=lambda z:(sum(z[0]),z[0]))]


def norms(p,d):
    terms={(i,j):v for (i,j),v in p.items() if i+j==d}
    l1=sum(map(abs,terms.values()),F(0))
    square=sum((math.factorial(d)*math.factorial(i)*math.factorial(j)*v*v for (i,j),v in terms.items()),F(0))
    return dict(coefficient_l1=float(l1),derivative_frobenius=math.sqrt(float(square)),derivative_frobenius_squared_exact=enc(square))


def extract(path,dest):
    import numpy as np
    path=Path(path);z=np.load(path,allow_pickle=False)
    N=int(z['radial']);M=int(z['angular']);p=float(z['exponent']);alpha=(1-p)/2
    inputs=dict(utc=datetime.now(timezone.utc).isoformat(),source=str(path),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),radial=N,angular=M,length=enc(float(z['length'])),exponent_stored=enc(p),alpha=enc(alpha),cl=enc(float(z['cl'])),mu=enc(float(z['mu'])if 'mu'in z.files else 0),chebyshev_coefficients=[[enc(float(v))for v in row]for row in z['coefficients'].reshape(M,N+1)],scope='Exact rational values of saved binary formula parameters. Alpha is the value computed by the scalar reconstructor, not silently replaced with a different rational.')
    dest.write_text(json.dumps(inputs,indent=2)+'\n');return inputs


def main():
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--tag',required=True);ap.add_argument('--degree',type=int,default=11);args=ap.parse_args()
    assert args.degree>=3 and args.degree%2==1
    gate=Path('research/smooth_canonical_high_jets/verification/manufactured.json')
    assert json.loads(gate.read_text())['status']=='PASS'
    dest=Path('evidence/smooth_exact_jets')/args.tag;dest.mkdir(parents=True,exist_ok=True)
    input_path=dest/'exact_input.json';extract(args.source,input_path)
    # Deliberately read the registered certificate input back, rather than
    # computing from the unregistered extraction in memory.
    inputs=json.loads(input_path.read_text());sol=solve(inputs,(args.degree-1)//2)
    output=dict(utc=datetime.now(timezone.utc).isoformat(),source=args.source,source_sha256=inputs['source_sha256'],input_file=str(input_path),input_sha256=hashlib.sha256(input_path.read_bytes()).hexdigest(),proof_file='research/smooth_canonical_high_jets/PROOF.md',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),degree=args.degree,a=enc(sol['a']),c=enc(sol['c']),delta=enc(sol['delta']),a_float=float(sol['a']),c_float=float(sol['c']),delta_float=float(sol['delta']),poisson_exact_zero=not sol['poisson'],polynomials={k:serial_poly(sol[k])for k in ['rho','psi','U1','U2','R']},canonical_moments=[{k:(enc(v)if isinstance(v,F)else v)for k,v in row.items()}for row in sol['moments']],by_degree=[dict(degree=d,rho=norms(sol['rho'],d),R=norms(sol['R'],d))for d in range(1,args.degree+1,2)],scope='Exact center coefficients of the saved smooth density and its canonical full-plane inverse. Necessary compatibility tests only; no uniform residual or smooth-limit certificate.')
    (dest/'jets.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items()if k in ['utc','source_sha256','a_float','c_float','delta_float','poisson_exact_zero']}),flush=True)
    for row in output['by_degree']:print(json.dumps(dict(degree=row['degree'],rho_l1=row['rho']['coefficient_l1'],R_l1=row['R']['coefficient_l1'],R_derivative_frobenius=row['R']['derivative_frobenius'])),flush=True)

if __name__=='__main__':main()
