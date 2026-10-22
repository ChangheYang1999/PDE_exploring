"""Independent exact pointwise de Boor / polynomial identity checker, packet183.

Does not import the generator or its Cox polynomial/Bernstein conversion code.
"""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from bisect import bisect_right
from math import comb
import hashlib,json,sys,time
import exact_inverse_constant as power


def prepared(data):
    ts=[Q(z)for z in data['knots']];c=[Q(z)for z in data['coefficients']];d=data['degree']
    assert d==5 and len(c)==len(ts)-d-1 and ts.count(0)==6 and ts.count(1)==6
    assert ts[0]==0 and ts[-1]==1 and all(a<=b for a,b in zip(ts,ts[1:]))
    assert all(ts.count(t)<=3 for t in set(ts)if 0<t<1)
    ans=[(ts,c,d)]
    for _ in range(2):
        c=[Q(0)if ts[i+d+1]==ts[i+1]else d*(c[i+1]-c[i])/(ts[i+d+1]-ts[i+1])for i in range(len(c)-1)]
        ts=ts[1:-1];d-=1;ans.append((ts,c,d))
    return ans

def deboor(state,t):
    ts,c,d=state
    j=min(len(c)-1,bisect_right(ts,t)-1)
    assert d<=j<len(c)
    q=[c[j-d+i]for i in range(d+1)]
    for r in range(1,d+1):
        for i in range(d,r-1,-1):
            den=ts[i+1+j-r]-ts[i+j-d]
            a=Q(0)if den==0 else(t-ts[i+j-d])/den
            q[i]=(1-a)*q[i-1]+a*q[i]
    return q[d]

def bernvalue(net,t):
    n=len(net)-1
    return sum(v*comb(n,i)*t**i*(1-t)**(n-i)for i,v in enumerate(net))

def check(cert,xs,archives=True):
    assert cert['schema']=='rational-spline-difference-v1'
    if archives:
        for x in xs:power.archive_check(x)
    ps=[prepared(x)for x in xs];union=sorted(set(ps[0][0][0]+ps[1][0][0]));b=Q(xs[0]['basis_beta']);L=Q(xs[0]['L'])
    assert 3<b<4 and L>0
    assert Q(xs[1]['basis_beta'])==b and Q(xs[1]['L'])==L
    assert all(Q(x['beta'])==b for x in xs)
    assert cert['beta']==str(b) and cert['L']==str(L)
    assert cert['union_knots']==[str(q)for q in union]
    lows=[Q(0)]*3;highs=[Q(0)]*3;last=Q(0);identities=0
    for leaf in cert['leaves']:
        a,z=map(Q,leaf['interval']);assert a==last and a<z<=1
        j=bisect_right(union,a)-1;assert z<=union[j+1]
        assert len(leaf['nets'])==3
        for k,strings in enumerate(leaf['nets']):
            n=5-k;net=list(map(Q,strings));assert len(net)==n+1
            for i in range(n+1):
                t=Q(i,n);where=a+(z-a)*t
                actual=deboor(ps[0][k],where)-deboor(ps[1][k],where)
                assert bernvalue(net,t)==actual,(a,z,k,i)
                identities+=1
            lows[k]=max(lows[k],*[abs(bernvalue(net,t))for t in (Q(0),Q(1,2),Q(1))]);highs[k]=max(highs[k],*[abs(x)for x in net])
        last=z
    assert last==1
    assert cert['norm_enclosures']==[[str(a),str(b)]for a,b in zip(lows,highs)]
    ep=[(-1)**k*(deboor(ps[0][k],Q(1))-deboor(ps[1][k],Q(1)))for k in range(3)]
    assert cert['endpoint_P_derivatives']==list(map(str,ep))
    delta=1-union[-2];assert cert['first_z_cell']==str(delta);gamma=b-3
    a=power.powerbound(delta,1-gamma);deltapair=[a[0]/delta,a[1]/delta]
    assert cert['delta_negative_gamma']==list(map(str,deltapair))
    bound=b*L*L/2*(abs(ep[0])/(b-1)+abs(ep[1])/(b-2)+abs(ep[2])/(2*(b-3))+highs[2]*(17*deltapair[1]/(3*(1-gamma))+(deltapair[1]-1)/gamma))
    assert Q(cert['inverse_difference_upper'])>=bound
    return {'verdict':'CONFIRMED','polynomial_node_identities':identities,'leaf_count':len(cert['leaves']),'norm_float':[[float(a),float(b)]for a,b in zip(lows,highs)],'inverse_bound_float':float(Q(cert['inverse_difference_upper']))}

def main():
    path=Path(sys.argv[1]);start=time.monotonic();cert=json.loads(path.read_text());xs=[]
    for item in cert['inputs']:
        p=Path(item['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'];xs.append(json.loads(p.read_text()))
    result=check(cert,xs);result.update(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    path.with_suffix('.check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
