"""Independent exact and interval checks for component-resolved constants."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import json
from flint import arb, ctx
ctx.prec=384

def A(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator

C,U1,U2,U3,R1,R2,R3,R4=map(Q,(2,6,24,160,22,32,80,2048))
K=[[Q(0) for _ in range(4)] for _ in range(4)]
K[0][0]=6*C+28*U1+166*U2+17*R2
K[0][1]=(17*U3+34*R3)/128
K[0][2]=17*R4/512
K[1][1]=C+28*U1+149*U2+17*R2
K[1][2]=17*R3/4
K[2][2]=C+28*U1+132*U2+17*R2
K[3][2]=17*(U1+R1)
K[3][3]=C
S=[[(K[i][j]+K[j][i])/2 for j in range(4)] for i in range(4)]
rows=[sum(row) for row in S]
assert rows==[Q(19053,4),Q(17925,4),Q(4324),Q(240)]
assert max(rows)<4800
s=Q(1,2**18); r=Q(1,2**16); eta=r/24
As=Q(4,5)*Q(3,10)+Q(3,10)*(1+142*s)+2*(1+44*s)
Bs=Q(9,5)*(1+44*s)
assert As==Q(127,50)+Q(653,5)*s
assert As+Bs==Q(217,50)+Q(1049,5)*s
assert Q(217,50)+Q(1049,5)/1024<5
assert s<Q(1,1024)
rate=Q(1,10)-4800*s-5*r*512
assert rate==Q(873,20480) and rate>Q(1,24)
assert 24*eta==r
pi=arb.pi(); cs=1/(2*(pi*A(s)*(1+A(s))).sqrt())
d=cs*A(r); KL=1/(A(Q(19,5))-d); q=KL*d
assert d<A(Q(1,400)) and q<A(Q(1,1000))
assert A(Q(7,10))-d>0
p=2**21; delta=s/2; kappa=p+4
assert p*delta==4 and p*(1+delta)+2-kappa==2
assert 2+3*512<2**11
optimal={}
for Cbg in [4800,Q(19053,4)]:
    so=Q(1,50)/Cbg; root=A(so).sqrt(); ro=root/125; eo=root/3125
    assert so<Q(1,1024)
    mu=Q(1,10)-Cbg*so; assert mu==Q(2,25)
    assert (A(mu)-5*ro/root).contains(A(Q(1,25)))
    do=ro/(2*(pi*A(so)*(1+A(so))).sqrt())
    qo=do/(A(Q(19,5))-do)
    assert do<A(Q(1,400)) and qo<A(Q(1,1000))
    optimal[str(Cbg)]={'s':str(so),'r':ro.str(60),'eta':eo.str(60),
                       'd':do.str(60),'contraction':qo.str(60)}
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'verdict':'CONFIRMED','precision_bits':ctx.prec,
     'upper_matrix':[[str(a) for a in row] for row in K],
     'symmetric_row_sums':[str(a) for a in rows],
     'Cbg':4800,'rough_constant':5,'rough_s_upper':'1/1024',
     's':str(s),'r':str(r),'eta':str(eta),'eta_decimal':A(eta).str(60),
     'rate_lower':str(rate),'inverse_upper':24,'gradient_upper':d.str(60),
     'contraction_upper':q.str(60),'moment_p':p,'moment_kappa':kappa,
     'combined_constant':24*2**11,'optimal':optimal,
     'scope':'Analytic constants only; actual residual smallness is not asserted.'}
path=Path(__file__).with_name('sharp_constants.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
