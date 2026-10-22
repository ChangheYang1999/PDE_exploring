#!/usr/bin/env python3
"""Own finite beta2 Green inverse. No fitting-code imports or execution."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent

def utc():
    return datetime.now(timezone.utc).isoformat()

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b, scale=1):
    out = list(a) + [0] * max(0, len(b) - len(a))
    for j, x in enumerate(b):
        out[j] += scale * x
    return trim(out)

def cheb_shifted(n):
    pol = [[1]]
    if n > 1:
        pol.append([-1, 2])
    for k in range(1, n - 1):
        out = [0] * (len(pol[k]) + 1)
        for j, x in enumerate(pol[k]):
            out[j] -= 2 * x
            out[j + 1] += 4 * x
        pol.append(add(out, pol[k - 1], -1))
    return pol

def qpower_times(a, power):
    out = [0] * (len(a) + 4 * power)
    for j in range(power + 1):
        fac = (-1)**j * math.comb(power, j)
        for k, x in enumerate(a):
            out[k + 4*j] += fac * x
    return trim(out)

def compiler(ca, cg):
    if ca.shape != cg.shape or ca.ndim != 2:
        raise ValueError('Expected equal (M,N) coefficient arrays')
    if not (np.isfinite(ca).all() and np.isfinite(cg).all()):
        raise ValueError('Nonfinite coefficient')
    M, N = ca.shape
    denom = max(float(x).as_integer_ratio()[1] for ar in (ca,cg) for x in ar.flat)
    shifted = cheb_shifted(N)
    def rows(ar):
        res=[]
        for row in ar:
            p=[0]*N
            for x, basis in zip(row, shifted):
                u,v=float(x).as_integer_ratio()
                w=u*(denom//v)
                for j,y in enumerate(basis):
                    p[j]+=w*y
            res.append(trim(p))
        return res
    ap,cp=rows(ca),rows(cg)
    modes=[]
    for k in range(1,M+1):
        a=cp[k-1]
        b=cp[k+1] if k+1<M else [0]
        f=2 if k==1 else 1
        P=add([f*x for x in qpower_times(a,2*k)],qpower_times(b,2*k+2),-1)
        Q=add([f*x for x in a],qpower_times(b,2),-1)
        L=4*k+3
        moment=sum((Fraction(p,j-L) for j,p in enumerate(P) if j!=L),Fraction())
        modes.append({'k':k,'P':P,'Q':Q,'moment':[moment.numerator,moment.denominator]})
    return {'M':M,'N':N,'denominator':denom,'A':ap,'C':cp,'modes':modes}

def horner_pair(coef,t):
    value=mp.mpf(0); deriv=mp.mpf(0)
    for c in reversed(coef):
        deriv=deriv*t+value
        value=value*t+c
    return value,deriv

def radial(comp,t):
    t=mp.mpf(t);q=1-t**4;qp=-4*t**3
    D=comp['denominator']
    out={'t':t,'q':q,'qp':qp,'A':[],'At':[],'C':[],'Ct':[],'X':[],'Y':[]}
    for name in ('A','C'):
        for m,coefs in enumerate(comp[name]):
            a,at=horner_pair(coefs,t);a/=D;at/=D
            out[name].append(q**m*a)
            out[name+'t'].append(q**m*(at+m*qp/q*a))
    for mode in comp['modes']:
        k=mode['k'];L=4*k+3
        P,Q=mode['P'],mode['Q'];u,v=mode['moment']
        # All coefficients have denominator 2D. Sum the complete polynomials.
        icoef=[mp.mpf(-p)/(j-L) if j!=L else mp.mpf(0) for j,p in enumerate(P)]
        i=mp.polyval(list(reversed(icoef)),t)+t**L*mp.mpf(u)/v
        if L<len(P):i-=P[L]*t**L*mp.log(t)
        o=mp.polyval([mp.mpf(Q[j])/(j+4*k-3) for j in reversed(range(len(Q)))],t)
        out['X'].append(q**(-k)*i/(2*D))
        out['Y'].append(q**k*o/(2*D))
    return out

def angular_cheb(z,M):
    T=[mp.mpf(1)];dT=[mp.mpf(0)]
    if M>1:T.append(z);dT.append(mp.mpf(1))
    for j in range(1,M-1):
        T.append(2*z*T[j]-T[j-1])
        dT.append(2*T[j]+2*z*dT[j]-dT[j-1])
    return T,dT

def evaluate(rad,phi):
    phi=mp.mpf(phi);t=rad['t'];q=rad['q'];qp=rad['qp']
    s,c=mp.sin(phi),mp.cos(phi);z=c*c-s*s
    T,dT=angular_cheb(z,len(rad['A']))
    A,At,C,Ct=[mp.fsum(x*y for x,y in zip(rad[n],T)) for n in ('A','At','C','Ct')]
    Az=mp.fsum(x*y for x,y in zip(rad['A'],dT))
    Cz=mp.fsum(x*y for x,y in zip(rad['C'],dT))
    Vr=-mp.fsum((x+y)*mp.cos(2*(j+1)*phi) for j,(x,y) in enumerate(zip(rad['X'],rad['Y'])))/(2*mp.sqrt(q))
    Vp=mp.fsum((-x+y)*mp.sin(2*(j+1)*phi) for j,(x,y) in enumerate(zip(rad['X'],rad['Y'])))/(2*mp.sqrt(q))
    F=(3*z-1)*A-2*(1-z*z)*Az
    LC=z*C-(1-z*z)*Cz
    fA=-t*q*At+6*t**4*A-t*t*mp.sqrt(q)*Vr*(At+3*qp*A/(2*q))/2+t*Vp*F/(2*mp.sqrt(q)*s*c)
    fG=-t*q*Ct+5*t**4*C-t*t*mp.sqrt(q)*Vr*(Ct+(1/t+qp/q)*C)/2+t*Vp*LC/(mp.sqrt(q)*s*c)+t*F/2+t*t*q*(1+z)*At/4+3*t*t*qp*(1+z)*A/8
    psi=mp.fsum((x+y)*mp.sin(2*(j+1)*phi)/(4*(j+1)) for j,(x,y) in enumerate(zip(rad['X'],rad['Y'])))/t**3
    return {'fA':fA,'fG':fG,'Vr':Vr,'Vp':Vp,'A':A,'C':C,'Psi':psi}

def load(path):
    with np.load(path,allow_pickle=False) as d:
        required={'beta':2.0,'beta_map':2.0,'sigma_a':1.5,'sigma_G':1.25,'L':1.0,'mapname':'t'}
        for k,v in required.items():
            if d[k].item()!=v:raise ValueError((k,d[k].item(),v))
        ca,cg=d['ca'].copy(),d['cG'].copy()
        if ca.shape!=(int(d['M']),int(d['N'])):raise ValueError('Array orientation')
        history=json.loads(d['hist'].item()) if 'hist' in d else []
        last={k:history[-1].get(k) for k in ('it','R1a_max','R1G_max','t')} if history else None
    return ca,cg,required,last

def serialize(comp):
    # Store exact integers as decimal strings to avoid downstream binary64 coercion.
    def conv(v):
        if isinstance(v,int):return str(v)
        if isinstance(v,list):return [conv(x) for x in v]
        if isinstance(v,dict):return {k:conv(x) for k,x in v.items()}
        return v
    return conv(comp)

def run_state(path,precisions,epsilons,output,save_exact=False):
    started=utc();begin=time.monotonic();ca,cg,meta,last=load(path)
    comp=compiler(ca,cg);compiled=time.monotonic()-begin
    result={'timestamp_start':started,'source':str(path),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'metadata':meta,'M':comp['M'],'N':comp['N'],'compiler_seconds':compiled,'source_history_last_diagnostic':last,'evaluations':[]}
    if save_exact:
        target=ROOT/'data'/(path.stem+'_exact_inverse.json')
        target.write_text(json.dumps(serialize(comp),separators=(',',':'))+'\n')
        result['exact_coefficients']={'path':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'bytes':target.stat().st_size}
    for dps in precisions:
        with mp.workdps(dps):
            for es in epsilons:
                e=mp.mpf(es);r1=radial(comp,e);r2=radial(comp,2*e)
                samples=[]
                for j in range(2*comp['M']):
                    phi=mp.pi*(j+mp.mpf('.5'))/(4*comp['M'])
                    a,b=evaluate(r1,phi),evaluate(r2,phi)
                    vals={name:(4*a[name]-b[name])/(2*e) for name in ('fA','fG')}
                    samples.append({'j':j,'phi':mp.nstr(phi,55),**{k:mp.nstr(v,55) for k,v in vals.items()}})
                maxa=max(samples,key=lambda x:abs(mp.mpf(x['fA'])))
                maxg=max(samples,key=lambda x:abs(mp.mpf(x['fG'])))
                entry={'dps':dps,'epsilon':es,'max_abs_fA':mp.nstr(abs(mp.mpf(maxa['fA'])),55),'max_abs_fG':mp.nstr(abs(mp.mpf(maxg['fG'])),55),'argmax_fA':maxa['j'],'argmax_fG':maxg['j'],'samples':samples,'elapsed_seconds':time.monotonic()-begin}
                result['evaluations'].append(entry)
                output.write_text(json.dumps(result,indent=2)+'\n')
                print(json.dumps({k:v for k,v in entry.items() if k!='samples'}),flush=True)
    result['timestamp_end']=utc();result['elapsed_seconds']=time.monotonic()-begin
    result['scope']='Complete finite formulas at the specified samples and precision. No interval bound or full-angle maximum certificate.'
    output.write_text(json.dumps(result,indent=2)+'\n')
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('state',type=Path);ap.add_argument('--dps',default='100,150');ap.add_argument('--eps',default='1e-5,1e-6,1e-7');ap.add_argument('--save-exact',action='store_true');ap.add_argument('--output',type=Path)
    args=ap.parse_args();out=args.output or ROOT/'verification'/(args.state.stem+'_finite_epsilon.json')
    run_state(args.state,[int(x) for x in args.dps.split(',')],args.eps.split(','),out,args.save_exact)

if __name__=='__main__':main()
