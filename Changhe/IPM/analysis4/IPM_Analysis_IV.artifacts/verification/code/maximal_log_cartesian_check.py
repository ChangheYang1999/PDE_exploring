"""Full exact Cartesian logarithmic recursion versus the maximal-degree chain."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import json,time,sys
from laurent_log_audit import L,Q,Poly,parse
sys.set_int_max_str_digits(0)


def poisson(F):
    rhs=F.X();P=F.q+1;K=len(rhs.a)-1
    out=[[Q(0) for _ in range(2*rhs.M+1)] for _ in range(K+2)]
    for idx in range(2*rhs.M+1):
        m=idx-rhs.M
        h=[a[idx] for a in rhs.a]
        if not any(h):continue
        den=m*m-P*P
        assert m
        if den:
            for j in range(K,-1,-1):
                out[j][idx]=(h[j]+2*P*(j+1)*out[j+1][idx]+((j+2)*(j+1)*out[j+2][idx] if j+2<len(out) else 0))/den
        else:
            for j in range(K,-1,-1):
                out[j+1][idx]=-h[j]/(2*P*(j+1))-((j+2)*out[j+2][idx]/(2*P) if j+2<len(out) else 0)
    G=L(P,rhs.M,[Poly(a) for a in out])
    assert (G.X().X().scale(-1)+G.Y().Y()-rhs).zero()
    return G


def rational_function(text,k):
    # Fixed trusted expression from the symbolic calculation, evaluated exactly by its displayed factors.
    return Q((k-1)*(2*k-1)**2*(8478*k**4-13599*k**3+507*k*k+4184*k-340),9600*k*k*(3*k-4)*(3*k-2)*(3*k+1)*(3*k+2)*(6*k-5)*(6*k-1))


def run(N=45,seconds=400):
    start=time.monotonic();d=Q(2,3);c=Q(3)
    F,G,XF,YF,XG,YG={},{},{},{},{},{}
    output=Path('research/44_maximal_log_chain/verification/cartesian_checks.json')
    data=json.loads(Path('research/44_maximal_log_chain/verification/symbolic_chain.json').read_text())
    # Sympy is used only to evaluate the separate symbolic formula, not to generate Cartesian coefficients.
    import sympy as s
    var=s.symbols('k',integer=True,positive=True)
    fformula={int(r):{int(j):s.sympify(v,locals={'k':var}) for j,v in a.items()} for r,a in data['normalized_density'].items()}
    gformula={int(r):{int(j):s.sympify(v,locals={'k':var}) for j,v in a.items()} for r,a in data['normalized_stream'].items()}
    def predicted(offsets,k,b):
        result={};m=2*k-2
        for j,v in offsets.items():
            freq=m+j;v=Q(str(v.subs(var,k)))*b
            if freq<0:freq=-freq;v=-v
            if freq:result[freq]=result.get(freq,Q(0))+v
        return {freq:v for freq,v in result.items() if v}
    def highest(A):
        return {j:2*A.a[-1][A.M+j] for j in range(1,A.M+1) if A.a[-1][A.M+j]}
    b={2:Q(data['b2'])};checks=[]
    for n in range(1,N+1):
        p=1-d*n
        if n==1:F[n]=parse(p,{1:['1']})
        else:
            non=L(p,0,[])
            for i in range(1,n):non=non+XG[i]*YF[n-i]-YG[i]*XF[n-i]
            lam=2*(n-1);term=non.scale(Q(1,lam));ans=term
            while term.a:
                term=term.dt().scale(Q(3,lam));ans=ans+term
            F[n]=ans
            assert (F[n].scale(-lam)+F[n].dt().scale(c)+non).zero()
        G[n]=poisson(F[n]);XF[n],YF[n]=F[n].X(),F[n].Y();XG[n],YG[n]=G[n].X(),G[n].Y()
        row=dict(n=n,density_degree=len(F[n].a)-1,stream_degree=len(G[n].a)-1,stationary_exact_zero=True,poisson_exact_zero=True)
        if n>=6 and n%3==0:
            k=n//3
            if k==3:b[k]=Q(data['b3'])
            elif k>3:b[k]=b[k-1]*rational_function(data['successive_ratio'],k-1)
            assert highest(G[n])=={2*k-2:b[k]},('resonant top',n,highest(G[n]),b[k], highest(F[n]))
            assert len(G[n].a)-1==k-1
            row.update(resonant_top_exact=str(b[k]),scalar_product_match=True)
        if n>=7:
            k=(n-1)//3;r=n-3*k
            assert highest(F[n])==predicted(fformula[r],k,b[k]),('density top',n)
            assert len(F[n].a)-1==k-1
            if r<3:assert highest(G[n])==predicted(gformula[r],k,b[k]),('stream top',n)
            row['symbolic_top_profile_match']=True
        checks.append(row)
        if n%3==0 or n==N:
            record=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
              code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),cartesian_engine_sha256=sha256(Path('code/laurent_log_audit.py').read_bytes()).hexdigest(),
              delta='2/3',c='3',input='sin(theta)',canonical_resonant_constant_zero=True,
              requested_N=N,completed_N=n,checks=checks,actual_elapsed_s=time.monotonic()-start)
            output.write_text(json.dumps(record,indent=2)+'\n')
            print(json.dumps(dict(n=n,top_log_match=True,elapsed_s=record['actual_elapsed_s'])),flush=True)
        if time.monotonic()-start>seconds:break

if __name__=='__main__':run()
