"""Formal-polynomial polar calculation and exact Cartesian gap checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq as Q, fmpq_poly as Poly
from general_fixed_deficit_audit import low,limiting,cycle


def add(out,m,v,signed=True):
    if signed and m<0:m,v=-m,-v
    if signed and m==0:return
    out[m]=out.get(m,Poly([]))+v
    if not out[m]:del out[m]


def polar_low(period,initial):
    d=Q(2,period);c=1/(1-d);f={};g={}
    for n in range(1,period+1):
        if n==1:f[n]=initial
        else:
            out={}
            for i in range(1,n):
                j=n-i;P=2-d*i;p=1-d*j;den=2*(n-1)*(c-1)
                for ell,b in g[i].items():
                    for m,a in f[j].items():
                        add(out,ell+m,b*a*((P*m-p*ell)/den))
                        add(out,ell-m,b*a*((P*m+p*ell)/den))
            f[n]=out
        out={};P=2-d*n
        for m,a in f[n].items():
            add(out,m+1,-a/(2*(m+1+P)))
            if m>1:add(out,m-1,a/(2*(m-1-P)))
        g[n]=out
    return f,g


def polar_limit(period,lf,lg):
    d=Q(2,period);c=1/(1-d);f={};g={0:{0:Poly([1])}}
    for r in range(1,period+1):
        out={}
        for i in range(r):
            p=1-d*(r-i)
            for s,b in g[i].items():
                for ell,a in lf[r-i].items():
                    add(out,s+ell,-b*a*((ell+p)/(2*c)),False)
                    add(out,s-ell,b*a*((p-ell)/(2*c)),False)
        for i in range(1,r):
            P=2-d*i
            for ell,b in lg[i].items():
                for s,a in f[r-i].items():
                    add(out,s+ell,b*a*((P+ell)/(2*c)),False)
                    add(out,s-ell,b*a*((ell-P)/(2*c)),False)
        f[r]=out
        if r<period:g[r]={s+1:-v/(2*(s+1-d*r)) for s,v in out.items()}
    return -f[period].get(1,Poly([]))/2


def main():
    start=time.monotonic();root=Path('research/68_transfer_cancellation');lf,lg=polar_low(3,{1:Poly([1]),3:Poly([0,1])})
    result=polar_limit(3,lf,lg);expected=Poly([Q(314,259200),Q(-2925,259200),Q(6735,259200),Q(75,259200)])
    assert result==expected,(result,expected)
    evaluation=[]
    for beta in [Q(-5,3),Q(-1),Q(0),Q(1,10),Q(1,5),Q(2,9),Q(1),Q(2),Q(15,7)]:
        F,G=low(3,{1:Q(1),3:beta});lam,_,_=limiting(3,F,G)
        assert lam==result(beta)
        for n in range(1,4):
            for field,polar,cart in [('f',lf,F),('g',lg,G)]:
                M=max(max(polar[n],default=0),cart[n].M)
                for m in range(1,M+1):
                    actual=2*cart[n].a[0][cart[n].M+m] if cart[n].a and m<=cart[n].M else Q(0)
                    assert polar[n].get(m,Poly([]))(beta)==actual,(beta,n,field,m)
        evaluation.append(dict(beta=str(beta),lambda_exact=str(lam),all_low_coefficients_match=True))
    P=Poly([314,-2925,6735,75]);intervals=[]
    for a,b in [(Q(-90233,1000),Q(-90232,1000)),(Q(19598,100000),Q(19599,100000)),(Q(23674,100000),Q(23675,100000))]:
        fa,fb=P(a),P(b);assert fa*fb<0
        intervals.append(dict(left=str(a),right=str(b),left_value=str(fa),right_value=str(fb),opposite_signs=True))
    gap=[]
    cases=[(3,5,{5:Q(1)}),(3,7,{7:Q(1)}),(3,9,{9:Q(1)}),(3,5,{5:Q(1),15:Q(-2,7)}),(5,7,{7:Q(1)}),(5,7,{7:Q(2,3),21:Q(1,9)}),(7,9,{9:Q(1)})]
    for period,M,initial in cases:
        F,G=low(period,initial);lam,_,_=limiting(period,F,G);assert lam==0
        L=max(initial);first=(period*(L+1)+2)//4+1
        rows=[]
        for k in sorted({2,3,4,8,first-1,first,first+1,first+2,2*first}):
            v=cycle(period,F,G,k,0)
            if k>=first:assert v==0,(period,M,initial,k,v)
            rows.append(dict(k=k,kR_exact=str(v),above_proved_threshold=k>=first))
        gap.append(dict(period=period,M=M,input={str(m):str(a) for m,a in initial.items()},maximum_frequency=L,
            first_guaranteed_zero_k=first,limit_exact=str(lam),cycles=rows))
        print(json.dumps(dict(period=period,M=M,L=L,first_zero_k=first,elapsed_s=time.monotonic()-start)),flush=True)
    output=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
        cubic_coefficients_ascending=[str(a) for a in result.coeffs()],exact_polynomial_identity=True,
        cartesian_evaluations=evaluation,isolating_intervals=intervals,gap_cycles=gap,all_passed=True,actual_elapsed_s=time.monotonic()-start)
    (root/'verification/checks.json').write_text(json.dumps(output,indent=2)+'\n')
    hashes={}
    for name in ['transfer_cancellation_audit.py','general_fixed_deficit_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py']:
        raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw);hashes[name]=sha256(raw).hexdigest()
    (root/'verification/source_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print('All checks passed',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
