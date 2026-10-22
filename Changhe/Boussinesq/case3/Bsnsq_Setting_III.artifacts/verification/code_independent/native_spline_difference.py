"""Exact common-cell derivative enclosures for packet183, generator only."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
from datetime import datetime,timezone
from bisect import bisect_right
import json,hashlib,time,argparse
from exact_temperature_certificate import spline_span,splitvec
import higher_inverse_constant as inverse
import exact_inverse_constant as interval


def restrict(a,offset,scale):
    n=len(a)-1
    return [sum(a[j]*comb(j,k)*offset**(j-k)*scale**k for j in range(k,n+1)) for k in range(n+1)]

def bernstein(a,n):
    return [sum(a[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]

def value(net,t):
    while len(net)>1:net=[(1-t)*a+t*b for a,b in zip(net,net[1:])]
    return net[0]

def bounds(leaves):
    ans=[]
    for k in range(3):
        nets=[[Q(q)for q in leaf['nets'][k]]for leaf in leaves]
        lo=max(abs(value(net,t))for net in nets for t in [Q(0),Q(1,2),Q(1)])
        hi=max(abs(q)for net in nets for q in net)
        ans.append([str(lo),str(hi)])
    return ans

def make(left,right,depth=3):
    assert 0<=depth<=6
    data=[left,right];knots=[];pieces=[]
    for x in data:
        _,_,_,ts,d,cs=inverse.validate(x)
        assert d==5 and all(ts.count(t)<=3 for t in set(ts)if 0<t<1)
        knots.append(ts);ps={}
        inp={'degree':5,'knots':x['knots'],'coefficients':[x['coefficients']]}
        for j in range(5,len(ts)-6):
            if ts[j]==ts[j+1]:continue
            a,b,poly=spline_span(inp,j)
            ps[j]=(a,b,[poly[0].get((k,0),Q(0))for k in range(6)])
        pieces.append(ps)
    assert left['basis_beta']==right['basis_beta'] and left['L']==right['L']
    union=sorted(set(knots[0]+knots[1]));leaves=[]
    def split(a,b,nets,d):
        if d==0:
            leaves.append({'interval':[str(a),str(b)],'nets':[[str(q)for q in net]for net in nets]});return
        parts=[splitvec(net)for net in nets];mid=(a+b)/2
        split(a,mid,[p[0]for p in parts],d-1);split(mid,b,[p[1]for p in parts],d-1)
    for a,b in zip(union,union[1:]):
        arrays=[]
        for ts,ps in zip(knots,pieces):
            j=bisect_right(ts,(a+b)/2)-1;aa,bb,poly=ps[j]
            arrays.append(restrict(poly,(a-aa)/(bb-aa),(b-a)/(bb-aa)))
        p=[x-y for x,y in zip(*arrays)];nets=[]
        for k in range(3):
            dp=[p[j+k]*Q(factorial(j+k),factorial(j))/(b-a)**k for j in range(6-k)]
            nets.append(bernstein(dp,5-k))
        split(a,b,nets,depth)
    enclosures=bounds(leaves);b=Q(left['basis_beta']);L=Q(left['L']);g=b-3
    assert 3<b<4
    delta=1-union[-2];powint=interval.scale(interval.powerbound(delta,1-g),1/delta)
    endpoint=[Q(leaves[-1]['nets'][k][-1])*(-1)**k for k in range(3)]
    jets=abs(endpoint[0])/(b-1)+abs(endpoint[1])/(b-2)+abs(endpoint[2])/(2*(b-3))
    M=Q(enclosures[2][1]);brace=17*powint[1]/(3*(1-g))+(powint[1]-1)/g
    bound=interval.up(b*L*L/2*(jets+M*brace))
    return {'schema':'rational-spline-difference-v1','depth':depth,'beta':str(b),'L':str(L),'union_knots':[str(q)for q in union], 'leaves':leaves,'norm_enclosures':enclosures,'endpoint_P_derivatives':[str(q)for q in endpoint],'first_z_cell':str(delta),'delta_negative_gamma':interval.ser(powint),'inverse_difference_upper':str(bound)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('left',type=Path);ap.add_argument('right',type=Path);ap.add_argument('output',type=Path);ap.add_argument('--depth',type=int,default=3);a=ap.parse_args();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
    xs=[json.loads(p.read_text())for p in [a.left,a.right]]
    for x in xs:inverse.base.archive_check(x)
    result=make(*xs,a.depth)
    result['inputs']=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in [a.left,a.right]]
    result['started_utc']=utc;result['ended_utc']=datetime.now(timezone.utc).isoformat();result['elapsed_seconds']=time.monotonic()-start
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'utc':result['ended_utc'],'elapsed_seconds':result['elapsed_seconds'],'leaf_count':len(result['leaves']),'norms':[[float(Q(q))for q in x]for x in result['norm_enclosures']],'C2_difference_bound':float(Q(result['inverse_difference_upper']))}),flush=True)
if __name__=='__main__':main()
