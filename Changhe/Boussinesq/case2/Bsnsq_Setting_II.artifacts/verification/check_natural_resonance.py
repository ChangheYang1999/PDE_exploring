"""Exact finite angular recurrence, independently implemented in Q[e^(i phi)].
Odd functions are i times rational Laurent series. Their derivatives are real.
No imported fitting code. Outputs are written to runs/ next to this script.
"""
from fractions import Fraction as Q
from pathlib import Path
import datetime, hashlib, json, time
ROOT=Path(__file__).resolve().parent

def add(*series):
    out={}
    for s in series:
        for n,a in s.items(): out[n]=out.get(n,Q(0))+a
    return {n:a for n,a in out.items() if a}

def scale(s,a): return {n:a*b for n,b in s.items() if a*b}

def mul(a,b):
    out={}
    for n,x in a.items():
        for m,y in b.items(): out[n+m]=out.get(n+m,Q(0))+x*y
    return {n:c for n,c in out.items() if c}

def sin(n): return {n:Q(-1,2),-n:Q(1,2)}  # imaginary Laurent coefficients

def derivative(odd): return {n:-n*a for n,a in odd.items() if n*a} # real

def poisson(g,alpha):
    out={}
    for n,a in g.items():
        den=n*n-alpha*alpha
        if not den: raise ValueError(f'resonance {n=} {alpha=}')
        out[n]=a/den
    return out

def encode(a): return {'numerator':str(a.numerator),'denominator':str(a.denominator)}

def encoded_series(a): return {str(n):encode(c) for n,c in sorted(a.items())}

def main():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.monotonic()
    h=[scale(add(sin(1),sin(3)),Q(1,4))]
    g=[add(scale(sin(2),Q(1,4)),scale(sin(4),Q(-3,8)))]
    p=[poisson(g[0],Q(3,2))]
    cos1={1:Q(1,2),-1:Q(1,2)};sin1=sin(1)
    rows=[]
    for j in range(1,8):
        thermal={};vort={}
        for k in range(j):
            ell=j-1-k;alpha=Q(3-k,2)
            thermal=add(thermal,scale(mul(derivative(p[k]),h[ell]),Q(ell,2)),scale(mul(p[k],derivative(h[ell])),alpha))
            vort=add(vort,scale(mul(derivative(p[k]),g[ell]),Q(ell+1,2)),scale(mul(p[k],derivative(g[ell])),alpha))
        vort=add(vort,scale(mul(cos1,h[j-1]),Q(j-1,2)),mul(sin1,derivative(h[j-1])))
        h.append(scale(thermal,Q(1,j)));g.append(scale(vort,Q(1,j)))
        # Check the required reality/parity and Fourier support independently of later inversion.
        for label,a in [('H',h[-1]),('G',g[-1])]:
            assert all(a.get(-n,Q(0))==-c for n,c in a.items()), (j,label,'not real odd')
            required=1 if label=='H' else 0
            assert all(n%2==required for n in a), (j,label,'wrong parity')
        if j<7: p.append(poisson(g[j],Q(3-j,2)))
        rows.append({'j':j,'H':encoded_series(h[j]),'G':encoded_series(g[j]),'P':encoded_series(p[j]) if j<7 else None})
    b=-2*g[7].get(2,Q(0))
    target=Q(-248652665830143836372937708761809789,5600812026228230278370435051520000000000)
    out={'time_start':started,'time_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Independent rational Laurent recurrence; stored imaginary coefficients of real sine functions; not lead code','input_H0':encoded_series(h[0]),'input_G0':encoded_series(g[0]),'input_P0':encoded_series(p[0]),'orders':rows,'sin2_G7':encode(b),'frozen_source_target':encode(target),'target_equal':b==target,'nonzero':bool(b),'scope':'Finite exact algebra for this leading pair only; no convergence, global profile, or universal resonance obstruction'}
    path=ROOT/'runs/natural_resonance_independent.json';path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['orders','input_H0','input_G0','input_P0']},indent=2))
    assert b==target
if __name__=='__main__': main()
