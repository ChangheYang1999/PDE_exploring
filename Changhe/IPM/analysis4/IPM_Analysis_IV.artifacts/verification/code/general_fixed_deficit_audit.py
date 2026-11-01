"""Exact Cartesian cycles and an independent finite limiting-offset map."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from laurent_log_audit import L,Q,parse
from maximal_log_cartesian_check import poisson,rational_function

def pair(G,F):return G.X()*F.Y()-G.Y()*F.X()
def amplitude(A,q,m):return 2*A.a[q][A.M+m] if q<len(A.a) and m<=A.M else Q(0)
def sine(A):return {m:amplitude(A,0,m) for m in range(1,A.M+1) if amplitude(A,0,m)}
def solve(non,n,c):
    den=(n-1)*(c-1);term=non.scale(1/den);out=term
    while term.a:
        term=term.dt().scale(c/den);out=out+term
    return out

def low(period,initial):
    d=Q(2,period);c=1/(1-d);F={};G={}
    for n in range(1,period+1):
        if n==1:F[n]=parse(1-d,{m:[v] for m,v in initial.items()})
        else:
            non=L(1-n*d,0,[])
            for i in range(1,n):non=non+pair(G[i],F[n-i])
            F[n]=solve(non,n,c)
        G[n]=poisson(F[n]);assert len(F[n].a)==1 and len(G[n].a)<=1
    return F,G

def limiting(period,F,G):
    d=Q(2,period);c=1/(1-d);f={};g={0:{0:Q(1)}}
    lf={n:sine(a) for n,a in F.items()};lg={n:sine(a) for n,a in G.items()}
    def add(out,s,v):out[s]=out.get(s,Q(0))+v
    for r in range(1,period+1):
        out={}
        for i in range(r):
            for shift,b in g[i].items():
                for ell,a in lf[r-i].items():
                    p=1-d*(r-i)
                    add(out,shift+ell,-b*a*(ell+p)/(2*c));add(out,shift-ell,b*a*(p-ell)/(2*c))
        for i in range(1,r):
            for ell,b in lg[i].items():
                for shift,a in f[r-i].items():
                    P=2-d*i
                    add(out,shift+ell,b*a*(P+ell)/(2*c));add(out,shift-ell,b*a*(ell-P)/(2*c))
        f[r]={s:v for s,v in out.items() if v}
        if r<period:g[r]={s+1:-v/(2*(s+1-d*r)) for s,v in f[r].items()}
    return -f[period].get(1,Q(0))/2, f,g

def cycle(period,F,G,k,degree):
    d=Q(2,period);c=1/(1-d);hf={};hg={0:parse(2-2*k,{2*k-2:[Q(0)]*degree+[Q(1)]})}
    for r in range(1,period+1):
        n=period*k+r;non=L(1-d*n,0,[])
        for i in range(r):non=non+pair(hg[i],F[r-i])
        for i in range(1,r):non=non+pair(G[i],hf[r-i])
        hf[r]=solve(non,n,c);hg[r]=poisson(hf[r])
    return amplitude(hg[period],degree+1,2*k)

def main():
    start=time.monotonic();root=Path('research/67_general_fixed_deficits');rows=[]
    cases=[(3,{1:Q(1)}),(3,{1:Q(1),3:Q(1,10)}),(4,{1:Q(1)}),(4,{3:Q(1)}),(5,{1:Q(1)}),(6,{1:Q(1),3:Q(-1,5),5:Q(1,11)})]
    for period,initial in cases:
        F,G=low(period,initial);lam,lf,lg=limiting(period,F,G)
        if period==3 and initial=={1:Q(1)}:assert lam==Q(157,129600)
        transfers=[]
        for k in [16,32,64,128]:
            kr=cycle(period,F,G,k,0)
            if period==3 and initial=={1:Q(1)}:assert kr==k*rational_function('',k)
            transfers.append(dict(k=k,kR_exact=str(kr),kR_approx=float(kr),difference_from_limit=float(kr-lam)))
        checks=[]
        for k in [5,8]:
            base=cycle(period,F,G,k,0)
            for q in [1,2,3]:
                value=cycle(period,F,G,k,q)
                assert (q+1)*value==base,(period,initial,k,q)
                checks.append(dict(k=k,input_log_degree=q,normalized_transfer_match=True))
        row=dict(period=period,delta=str(Q(2,period)),input={str(m):str(a) for m,a in initial.items()},limit_exact=str(lam),limit_approx=float(lam),
            finite_transfers=transfers,log_degree_checks=checks,limiting_density_offsets={str(r):{str(s):str(v) for s,v in a.items()} for r,a in lf.items()})
        rows.append(row);print(json.dumps(dict(period=period,input=row['input'],limit=row['limit_exact'],elapsed_s=time.monotonic()-start)),flush=True)
        result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),cases=rows,all_completed=len(rows)==len(cases),actual_elapsed_s=time.monotonic()-start)
        (root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['general_fixed_deficit_audit.py','laurent_log_audit.py','maximal_log_cartesian_check.py']:
        raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw)
    print('All checks passed',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
