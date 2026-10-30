"""Exact specialization of the analytic dipole forced-tail theorem."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
from flint import fmpq as Q, arb, ctx
ctx.prec=512
B=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ar(q):
    q=Q(q)
    return arb(q.p)/arb(q.q)
def tw(q):
    return arb(2)**ar(q)
def main():
    tick=time.monotonic()
    c=Q(4076476460239181,2251799813685248);g=1/c;d=1-g
    q1=-1-4*d;q2=1-9*d;eps=2-4*d
    assert -3<q1<-1 and g-4<q2<-3 and eps>0
    assert 1-c*(g-4)==4*c
    assert q2-eps==-1-5*d
    D=tw(q2+3)*(ar(Q(1,2))+tw(-q2)+tw(3-q2)+tw(q2+2)/ar(-q2))+ar(32/((-q2-1)*(-q2-2)*(-q2-3)))
    peer=json.loads((B/'source/opus_result.json').read_text())
    assert D.overlaps(arb(peer['B']['Cprime_q2']))
    assert D>arb('610.805532899') and D<arb('610.805532900')
    rows=[]; old=None; files=[B/'PROOF.md',Path(__file__),B/'source/opus_result.json',B/'source/OPUS_REVIEW.md']
    for label in ['007','013','014']:
        path=B/f'data/{label}_sectors.json';files.append(path)
        s=json.loads(path.read_text())['sectors'];r=next(t for t in s if (t['K'],t['L'])==(9,0))
        assert Q(r['exponent_exact'])==q2
        F={int(k):Q(v) for k,v in r['residual'].items() if Q(v)}
        assert F and all(k>0 and k%2 for k in F)
        if old is not None:assert F==old
        old=F
        square=sum((v*v for v in F.values()),Q(0))/(1-c*q2)**2
        norm=(arb.pi()*ar(square)).sqrt()
        assert norm>arb('5428.78') and norm<arb('5428.80')
        rows.append({'candidate':label,'sector':[9,0],'nonzero_modes':len(F),'forced_angular_norm':norm.str(85),'source_sha256':sha(path)})
    out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in files},'q1':str(q1),'q2':str(q2),'epsilon':str(eps),'Dq2':D.str(90),'peer_overlap':True,'rows':rows,'elapsed_seconds':time.monotonic()-tick,'verdict':'CONFIRMED exact application and directed constants; proof in PROOF.md'}
    (B/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='inputs'},indent=2))
if __name__=='__main__':main()
