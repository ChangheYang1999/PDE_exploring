"""Independent exact sine/cosine recurrence near delta=2/5, through order20."""
from pathlib import Path
from flint import fmpq as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
ROOT=Path('research/216_repeated_near_resonant_poles')
start=time.monotonic()
constants=json.loads((ROOT/'verification/checks.json').read_text())

def add(d,m,x):
    if m<0:m,x=-m,-x
    if m and x:
        d[m]=d.get(m,Q(0))+x
        if not d[m]:del d[m]

def run(delta,N=20):
    f={1:{1:Q(1)}};g={}
    def p(n):return 1-n*delta
    for n in range(1,N+1):
        if n>1:
            out={}
            for i in range(1,n):
                j=n-i
                for ell,b in g[i].items():
                    for m,a in f[j].items():
                        add(out,ell+m,b*a*(-p(j)*ell+(p(i)+1)*m)/2)
                        add(out,m-ell,b*a*(-p(j)*ell-(p(i)+1)*m)/2)
            f[n]={m:a*(1-delta)/(delta*(n-1)) for m,a in out.items()}
        P=p(n)+1;g[n]={}
        for j in range(1,(max(f[n])+1)//2+1):
            den=2*(4*j*j-P*P)
            num=(P-2*j)*f[n].get(2*j-1,Q(0))+(P+2*j)*f[n].get(2*j+1,Q(0))
            if not den:
                assert n==N==10
                return f,g
            if num:g[n][2*j]=num/den
    return f,g

f,g=run(Q(2,5),10)
assert f[10][1]==Q(constants['R'])
rows=[]
for bits in [20,30,40]:
    eps=Q(1,2**bits);f,g=run(Q(2,5)+eps)
    row={'epsilon':'1/'+str(2**bits),'orders':{}}
    for n,d in [(10,1),(15,2),(20,3)]:
        predicted=Q(constants['leading_poles'][str(n)]['coefficient'])
        ratio=g[n][2*(n//5-1)]*eps**d/predicted
        err=abs(ratio-1)
        row['orders'][str(n)]={'scaled_coefficient_over_predicted':float(ratio),'relative_error':float(err)}
        if bits==40:assert err<Q(1,1000000)
    rows.append(row)
    print(json.dumps(row),flush=True)
for n in [10,15,20]:
    errs=[r['orders'][str(n)]['relative_error'] for r in rows]
    assert errs[1]<errs[0]/500 and errs[2]<errs[1]/500
out={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'all_checks_pass':True,'exact_arithmetic':'python-flint fmpq; displayed ratios only converted to binary64','rows':rows,'exact_R_recomputed':str(f[1][1]),'actual_elapsed_s':time.monotonic()-start}
out['exact_R_recomputed']=constants['R']
(ROOT/'verification/independent_fourier_check.json').write_text(json.dumps(out,indent=2)+'\n')
p=Path('code/repeated_near_resonant_numeric_check.py');(ROOT/'sources'/p.name).write_bytes(p.read_bytes())
print(json.dumps({'all_checks_pass':True,'actual_elapsed_s':out['actual_elapsed_s']}),flush=True)
