from fractions import Fraction as Q
from math import comb
from itertools import combinations
from pathlib import Path
from datetime import datetime,timezone
import json,time,copy
from native_spline_difference import make
from check_native_spline_difference import check
start=time.monotonic();began=datetime.now(timezone.utc).isoformat();tests=[];negative=[];nodecount=0

def data(breaks,powers):
    knots=[Q(0)]*5+list(map(Q,breaks))+[Q(1)]*5;c=[]
    for i in range(len(knots)-6):
        xs=knots[i+1:i+6]
        c.append(sum(v*sum((__import__('math').prod(a)for a in combinations(xs,k)),Q(0))/comb(5,k)for k,v in enumerate(powers)))
    return {'source':'self','beta':'13/4','basis_beta':'13/4','L':'3/2','degree':5,'knots':list(map(str,knots)),'coefficients':list(map(str,c))}

def record(name,a,b,exact):
    global nodecount
    cert=make(a,b,2);result=check(cert,[a,b],archives=False);nodecount+=result['polynomial_node_identities']
    assert all(Q(lo)<=Q(q)<=Q(hi) for (lo,hi),q in zip(cert['norm_enclosures'],exact)),(name,cert['norm_enclosures'])
    assert all(Q(hi)-Q(lo)<Q(1,1000) for lo,hi in cert['norm_enclosures'])
    tests.append({'name':name,'norms':cert['norm_enclosures'],'known_exact_norms':[str(Q(q))for q in exact],'identities':result['polynomial_node_identities']});return cert

base=[0,1];refined=[0,Q(1,3),Q(4,7),1]
a=data(base,[Q(0),Q(1),Q(-1)]);b=data(refined,[Q(0),Q(1),Q(-1)])
record('identical quadratic on different meshes',a,b,[0,0,0])
zero=data(refined,[Q(0)])
c=record('interior quadratic maximum and physical derivatives',a,zero,[Q(1,4),1,2])
record('constant shift on different meshes',data(base,[Q(3)]),zero,[3,0,0])
record('quintic physical derivatives on unequal cells',data(refined,[Q(0)]*5+[Q(1)]),zero,[1,5,20])
record('same nonconstant function reversed comparison',zero,data(refined,[Q(0)]*5+[Q(1)]),[1,5,20])
for name,edit in [
    ('wrong net length',lambda z:z['leaves'][0]['nets'][1].append('0')),
    ('derivative net changed',lambda z:z['leaves'][0]['nets'][1].__setitem__(0,str(Q(z['leaves'][0]['nets'][1][0])+1))),
    ('one leaf removed',lambda z:z['leaves'].pop(1)),
    ('leaf overlap',lambda z:z['leaves'][1]['interval'].__setitem__(0,'0')),
    ('false global upper bound',lambda z:z['norm_enclosures'][2].__setitem__(1,'0')),
    ('wrong endpoint derivative',lambda z:z['endpoint_P_derivatives'].__setitem__(1,'99')),
]:
    bad=copy.deepcopy(c);edit(bad)
    try:check(bad,[a,zero],archives=False)
    except AssertionError:negative.append({'name':name,'rejected':True})
    else:raise AssertionError('bad certificate accepted:'+name)
r=Path('research/183_certified_native_spline_differences/verification');r.joinpath('manufactured_inputs.json').write_text(json.dumps({'quadratic_one_cell':a,'quadratic_refined':b,'zero_refined':zero,'quintic_refined':data(refined,[Q(0)]*5+[Q(1)])},indent=2)+'\n')
out={'started_utc':began,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'verdict':'PASS','exact_controls':tests,'negative_controls':negative,'polynomial_node_identities':nodecount}
r.joinpath('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
