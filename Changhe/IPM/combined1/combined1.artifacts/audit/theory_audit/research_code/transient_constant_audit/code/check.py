from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json,time
B=Path(__file__).resolve().parents[1]
ctx.prec=512;start=time.monotonic()
def ar(q):
    q=Q(q);return arb(q.numerator)/q.denominator

def matrix(s,R,KL):
    ss,rr,kk=ar(s),ar(R),ar(KL);nu=rr/ss.sqrt();bs=ar(Q(9,5))*(1+44*ss)
    alpha=ar(Q(9,10))-4290*ss-ar(Q(13,10))*nu-ss*(6+1360*ss)
    q=6+1360*ss;m2=ar(Q(1,2))-4708*ss-(ar(Q(127,50))+ar(Q(653,5))*ss+bs)*nu
    v1=10+34816*ss;k1=ar(Q(347,5))+5440*ss+bs*nu+ss*v1
    assert alpha>0 and m2>0
    D=k1/m2+(40/m2).sqrt()
    N=[[1/m2,D/(128*alpha),kk*(v1/m2+D*q/alpha)/512],
       [arb(0),1/alpha,kk*q/(4*alpha)],[arb(0),4*ss/alpha,kk*(1+ss*q/alpha)]]
    return N,{'nu':nu,'alpha':alpha,'m2':m2,'q':q,'k1':k1,'v1':v1}

def minors(N,K):
    M=[[ar(K*K if i==j else 0)-sum((N[t][i]*N[t][j] for t in range(3)),arb(0)) for j in range(3)] for i in range(3)]
    return [M[0][0],M[0][0]*M[1][1]-M[0][1]*M[1][0],
            M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])]

def certify(N):
    lo,hi=Q(0),Q(1024)
    assert all(x>0 for x in minors(N,hi))
    for _ in range(58):
        mid=(lo+hi)/2;mm=minors(N,mid)
        if all(x>0 for x in mm):hi=mid
        else:
            assert any(x<0 for x in mm)
            lo=mid
    n=(hi.numerator*10**8+hi.denominator-1)//hi.denominator;K=Q(n,10**8)
    mm=minors(N,K);assert all(x>0 for x in mm)
    return K,mm

params=[('baseline',Q(1,131072),Q(1,16384),Q(2),Q('0.0000079595')),
        ('KL_1_2',Q(1,225**2),Q(21,100000),Q(1,2),Q('0.0000303220')),
        ('KL_1',Q(1,227**2),Q(21,100000),Q(1),Q('0.0000241869')),
        ('KL_2',Q(1,228**2),Q(21,100000),Q(2),Q('0.0000153446')),
        ('KL_4',Q(1,229**2),Q(21,100000),Q(4),Q('0.00000831687')),
        ('KL_8',Q(1,229**2),Q(21,100000),Q(8),Q('0.00000425137')),
        ('KL_16',Q(1,229**2),Q(21,100000),Q(16),Q('0.00000213775'))]
rows=[]
for name,s,R,KL,printed in params:
    N,pp=matrix(s,R,KL);K,mm=certify(N);eta0=R/K;eta=Q(eta0.numerator*10**12//eta0.denominator,10**12)
    assert eta*K<=R
    cs=1/(4*arb.pi()*ar(s*(1+s))).sqrt();contraction=ar(KL*R)*cs
    assert contraction<1 and ar(R)*cs<ar(Q(7,10))
    check=minors(N,R/printed);passed=all(x>0 for x in check)
    assert passed or any(x<0 for x in check)
    row={'name':name,'s':str(s),'R':str(R),'K_L':str(KL),'parameters':{k:v.str(65) for k,v in pp.items()},'certified_K':str(K),'K_decimal':str(float(K)),'positive_minors':[v.str(65) for v in mm],
         'eta_rational':str(eta),'eta_decimal':str(float(eta)),'unrounded_R_over_K':ar(eta0).str(65),'contraction':contraction.str(65),'T1_printed_eta':str(printed),'printed_eta_matrix_test_pass':passed,'printed_eta_minors':[v.str(65) for v in check]}
    rows.append(row)
    print(name,'K',float(K),'eta',float(eta),'printed passes',passed,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':sha256((B/'PROOF.md').read_bytes()).hexdigest(),'precision_bits':ctx.prec,'rows':rows,'elapsed_seconds':time.monotonic()-start}
(B/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
