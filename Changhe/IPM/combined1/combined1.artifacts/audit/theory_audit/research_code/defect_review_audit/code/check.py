from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
from flint import arb,ctx
import json,time
B=Path(__file__).resolve().parents[1]
start=time.monotonic();ctx.prec=384
def a(q):
    q=Q(q);return arb(q.numerator)/q.denominator
def show(v):return v.str(80)
rows=[]
for name,mu0,C,kappa,rootw in [('baseline',Q(1,10),4800,Q(5),512),('rebalanced',Q(297,1000),4800,Q(5),512),('sharp_H',Q(297,1000),402,Q(8,5),512),('sharp_L2',Q(259,1000),401,Q(8,5),512),('sharpw_L2',Q(97,250),397,Q(8,5),1024)]:
    sstar=mu0/(3*C);rmax=a(2*mu0/(3*kappa))*a(sstar).sqrt();mmax=rmax/rootw
    rows.append({'name':name,'s_star':str(sstar),'r_sup':show(rmax),'L2_distance_sup':show(mmax)})
    if name=='baseline':assert rmax.overlaps(1/(9000*arb(10).sqrt()))
boxes=[]
for name,mu0,C,l in [('sharpw',Q(97,250),397,72),('sharp',Q(259,1000),401,88)]:
    s=Q(1,l*l);mu=mu0-C*s;A=Q(8,5)*l
    rs=[mu/(2*A),Q(143,100000),Q(449,250000)] if name=='sharpw' else [mu/(2*A),Q(411,500000)]
    ms=[Q(0),Q(1,4096),Q(1,1024)]
    for idx,r in enumerate(rs):
        m=ms[idx];bb=Q(0) if idx==0 else Q(1,100);beta=mu-A*r;eps=(r-m)*beta-bb*r
        assert beta>0 and eps>0
        maximum=((mu-A*m-bb)**2-4*A*bb*m)/(4*A)
        assert maximum>=eps
        q=a(r)/(2*(4*arb.pi()*a(s*(1+s))).sqrt())
        boxes.append({'name':name,'m':str(m),'B':str(bb),'r':str(r),'beta':str(beta),'epsilon_at_r':str(eps),'epsilon_at_r_decimal':show(a(eps)),'epsilon_optimum':str(maximum),'q_upper_ball':show(q)})
    if name=='sharp':assert ((mu-A*Q(1,1024)-Q(1,100))**2-4*A*Q(1,100)*Q(1,1024))/(4*A)<0
cs={}
for sm in (Q(1,2),Q(1,1024)):
    value=arb.pi().sqrt()/2*a((1-sm)/2).gamma()+a(Q(16,5))
    cs[str(sm)]=show(value)
    if sm==Q(1,1024):assert value<a(Q(24,5))
out={'utc':datetime.now(timezone.utc).isoformat(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':sha256((B/'PROOF.md').read_bytes()).hexdigest(),'source_sha256':sha256((B/'source/T2_REVIEW.md').read_bytes()).hexdigest(),'universal_budgets':rows,'boxes':boxes,'moment_constants':cs,'all_checks_pass':True,'elapsed_seconds':time.monotonic()-start}
(B/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
