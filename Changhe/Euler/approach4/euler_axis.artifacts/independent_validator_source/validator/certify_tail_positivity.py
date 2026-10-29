#!/usr/bin/env python3
"""Exact Bernstein subdivision certificate for a frozen Legendre polynomial."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime, timezone
import argparse, hashlib, json, time


def legendre_to_power(coeff):
    n=len(coeff)-1
    total=[F(0)]*(n+1)
    previous=[F(1)]
    for i,a in enumerate(previous):total[i]+=coeff[0]*a
    if n==0:return total
    current=[F(0),F(1)]
    for i,a in enumerate(current):total[i]+=coeff[1]*a
    for degree in range(2,n+1):
        nxt=[F(0)]*(degree+1)
        for i,a in enumerate(current):nxt[i+1]+=(2*degree-1)*a/degree
        for i,a in enumerate(previous):nxt[i]-=(degree-1)*a/degree
        for i,a in enumerate(nxt):total[i]+=coeff[degree]*a
        previous,current=current,nxt
    return total


def to_bernstein(power):
    """Power coefficients in mu -> Bernstein on mu=2t-1, 0<=t<=1."""
    n=len(power)-1
    shifted=[sum(power[k]*comb(k,j)*2**j*(-1)**(k-j) for k in range(j,n+1)) for j in range(n+1)]
    return [sum(shifted[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]


def split_half(coeff):
    triangle=[list(coeff)]
    while len(triangle[-1])>1:
        row=triangle[-1]
        triangle.append([(row[i]+row[i+1])/2 for i in range(len(row)-1)])
    return [row[0] for row in triangle],[row[-1] for row in reversed(triangle)]


def certify(coeff, max_depth=16):
    leaves=[]
    pending=[(F(-1),F(1),to_bernstein(legendre_to_power(coeff)),0)]
    while pending:
        lo,hi,bern,depth=pending.pop()
        lower=min(bern);upper=max(bern)
        if lower>0:status='POSITIVE'
        elif upper<0:status='NEGATIVE'
        elif depth>=max_depth:status='UNRESOLVED'
        else:
            left,right=split_half(bern);mid=(lo+hi)/2
            pending.append((mid,hi,right,depth+1));pending.append((lo,mid,left,depth+1));continue
        leaves.append({'lower_mu':str(lo),'upper_mu':str(hi),'bernstein_lower':str(lower),'bernstein_upper':str(upper),'depth':depth,'status':status})
    leaves.sort(key=lambda row:F(row['lower_mu']))
    assert F(leaves[0]['lower_mu'])==-1 and F(leaves[-1]['upper_mu'])==1
    assert all(F(a['upper_mu'])==F(b['lower_mu']) for a,b in zip(leaves,leaves[1:]))
    return leaves


def run(source,output,max_depth=16):
    start=time.perf_counter();raw=Path(source).read_bytes();doc=json.loads(raw)
    coeff=[F(int(c['numerator']),int(c['denominator'])) for c in doc['coefficients_exact_binary']]
    leaves=certify(coeff,max_depth)
    result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'coefficient_sha256':doc['coefficient_sha256'],
            'source_certificate':str(Path(source).resolve()),'source_certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'max_depth':max_depth,
            'degree':len(coeff)-1,'leaves':leaves,'strictly_positive_certified':all(x['status']=='POSITIVE' for x in leaves),
            'negative_interval_certified':any(x['status']=='NEGATIVE' for x in leaves),
            'unresolved_intervals':sum(x['status']=='UNRESOLVED' for x in leaves),
            'elapsed_seconds':time.perf_counter()-start,
            'scope':'Exact polynomial sign on the complete interval, conditional on audited frozen coefficient extraction. No Euler existence or global source-basin claim.'}
    Path(output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['recorded_utc','strictly_positive_certified','negative_interval_certified','unresolved_intervals','elapsed_seconds']}))
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('--output',type=Path,required=True);p.add_argument('--max-depth',type=int,default=16)
    args=p.parse_args();run(args.source,args.output,args.max_depth)
