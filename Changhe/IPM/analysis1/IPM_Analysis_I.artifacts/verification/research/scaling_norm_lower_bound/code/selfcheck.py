"""Manufactured finite arithmetic checks only. No actual modal span is executed."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
sys.dont_write_bytecode=True
from flint import fmpq as Q,fmpq_poly as P
import cox_monomial as a, deboor_legendre as b, weights as w
D=Path(__file__).resolve().parents[1]

def run():
    counts={}
    hs=['0x0.0p+0','-0x0.0p+0','0x1.0000000000000p+0','-0x1.fffffffffffffp+1023','0x0.0000000000001p-1022','0x1.123456789abcdp-37']
    for h in hs:assert a.decode(h)==b.decode(h)
    counts['independent_hex_decoders']=len(hs)
    knots=[Q(0)]*8+[Q(1),Q(2),Q(3)]+[Q(4)]*8
    N=len(knots)-8;greville=[sum(knots[i+1:i+8],Q(0))/7 for i in range(N)]
    S=[[Q(1) for i in range(N)],greville]+[[Q((-1)**(i+m)*(i*i+3*m),i+m+1) for i in range(N)] for m in range(1,5)]
    for span in range(7,11):
        x=a.modal(knots,S,span);y=b.modal(knots,S,span);assert x==y
        assert x[0]==P([1]) and x[1]==P([knots[span],knots[span+1]-knots[span]])
        assert sum(a.basis(knots,span),P([]))==P([1])
        assert a.angular(x)==b.angular(y)
        assert a.compute(knots,S,span)==b.compute(knots,S,span)
    counts['manufactured_spline_span_pairs']=4;counts['partition_of_unity_and_linear_reproduction']=8
    for m in range(6):
        S=[P([int(i==m)]) for i in range(6)]
        assert a.angular(S)==b.angular(S)
    counts['single_angular_mode_pairs']=6
    for l in range(8):
        for j in range(8):
            p=b.LEG[l]*b.LEG[j]
            val=sum((p[i]/(i+1) for i in range(len(p))),Q(0))
            assert val==(Q(1,2*l+1) if l==j else Q(0))
    counts['exact_legendre_orthogonality_entries']=64
    for k in range(10):
        p=P([Q((-1)**(i+k)*(k+i+1),i+2) for i in range(8)])
        assert a.square_integral(p)==b.square_integral(p)>0
    counts['manufactured_polynomial_square_integral_pairs']=10
    for row in [{'a':'-3','b':'-2','Q':'7/11'},{'a':'1','b':'2','Q':'103/7'},{'a':'-1','b':'1','Q':'0'}]:
        x=w.cell_arb(row,'2/11','5/3');y=w.cell_iv(row,'2/11','5/3')
        for side in ['left','right']:
            xx=w.valid(x[side]);yy=w.valid(y[side]);assert max(xx[0],yy[0])<=min(xx[1],yy[1])
        if row['Q']!='0':
            for pair,fun in [(x['left'],w.root_arb),(y['left'],w.root_iv)]:
                lo,hi=w.valid(pair);rlo,rhi=w.valid(fun(pair));assert rlo*rlo<=lo<=hi<=rhi*rhi
                text=w.downward(rlo);assert 0<F(text)<rlo and F(text)**2<lo
    counts['manufactured_dual_weight_pairs']=6;counts['root_endpoint_containments_and_lower_decimal_checks']=4
    for val in ['1','1/3','1234567/100','1/10000000000000000','98765432101234567890123456789/13']:
        q=F(val);s=w.downward(q);assert 0<F(s)<q and '/' not in s
    counts['strict_downward_decimal_cases']=5
    return counts

if __name__=='__main__':
    out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_MANUFACTURED_SCALING_NORM_ARITHMETIC_ONLY','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'counts':run(),'actual_modal_spans_executed':0}
    p=D/'evidence/selfcheck.json'
    with p.open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
