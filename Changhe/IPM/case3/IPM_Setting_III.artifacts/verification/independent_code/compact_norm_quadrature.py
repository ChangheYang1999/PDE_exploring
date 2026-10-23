"""Positive whole-plane radial quadrature nodes for result103."""
import json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp


def nodes(order,digits=50):
    p=Path(f'evidence/q_derivative_norms/gauss_nodes/order{order}_dps{digits}.json')
    if not p.exists():
        started=time.monotonic()
        with mp.workdps(digits):
            x,w=mp.gauss_quadrature(order,'legendre')
            data=[dict(s=mp.nstr((v+1)/2,digits),weight=mp.nstr(z/2,digits)) for v,z in zip(x,w)]
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),order=order,digits=digits,seconds=time.monotonic()-started,rows=data),indent=2)+'\n')
    rec=json.loads(p.read_text());assert rec['order']==order and rec['digits']==digits
    with mp.workdps(digits):
        rows=[(mp.mpf(v['s']),mp.mpf(v['weight'])) for v in rec['rows']]
        assert len(rows)==order and all(0<s<1 and w>0 for s,w in rows)
        errors=[]
        for k in sorted(set([0,1,2,3,order,2*order-2,2*order-1])):
            exact=1/mp.mpf(k+1);err=abs(mp.fsum(w*s**k for s,w in rows)-exact)
            assert err<mp.power(10,-digits+8),(order,k,err)
            errors.append(dict(degree=k,absolute_error=mp.nstr(err,15)))
        symmetry=max(max(abs(rows[i][0]+rows[-i-1][0]-1),abs(rows[i][1]-rows[-i-1][1])) for i in range(order))
        assert symmetry<mp.power(10,-digits+8)
    return rows,dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),moment_checks=errors,symmetry_error=mp.nstr(symmetry,15),generation_seconds=rec['seconds'])


def radius_and_jacobian(s,L,kappa):
    r=L*mp.sqrt(s)*mp.power(2*(1-s),-kappa)
    jac=(1+(2*kappa-1)*s)/(2*s*(1-s))
    return r,jac
