import gzip, hashlib, json, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import mpmath as mp
from flint import arb, arb_mat, fmpz, ctx

root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parents[1]/'evidence'
run=root.parent/'s2-num/work/runs/S0_M4_s60_o12'
ctx.prec=384
mp.mp.dps=100
start=time.time()
meta=json.loads((run/'meta.json').read_text())
with gzip.open(run/'matrices_dyadic.json.gz','rt') as f:data=json.load(f)

def ball(q):
    m,e,r,re=map(int,q)
    mid=arb(fmpz(m))*arb(2)**e
    rad=arb(fmpz(r))*arb(2)**re
    return mid+arb(0,rad)

def mp_mid(x):
    m,e=x.mid().man_exp()
    return mp.mpf(int(m))*mp.power(2,int(e))

n=int(meta['ncol'])+1
G=arb_mat(n,n)
for key,q in data['GX'].items():
    i,j=map(int,key.split('|'))
    value=ball(q)*(1+4*meta['columns'][i]['m']**2)**meta['weights']['sX']
    G[i,j]=value
    G[j,i]=value
labels=[c['label'] for c in meta['columns']]
G[labels.index('J'),labels.index('J')]=1
G[n-1,n-1]=1
kn,kd=map(int,meta['k'].split('/'))
k=arb(kn)/kd
c=[ball(x['c']) for x in meta['columns']]+[ball(meta['cTAU'])]
den=3/k+k*ball(meta['cKP'])
d=[-x*k/den for x in c]
for i in range(n):
    for j in range(n):G[i,j]+=d[i]*d[j]
print('decoded',n,'at',time.time()-start,flush=True)
Gf=np.array([[float(G[i,j].mid()) for j in range(n)] for i in range(n)])
res={'date':datetime.now(timezone.utc).isoformat(),'n':n,'prec_bits':ctx.prec,'mp_decimal_digits':mp.mp.dps,
     'input_sha256':hashlib.sha256((run/'matrices_dyadic.json.gz').read_bytes()).hexdigest(),
     'meta_sha256':hashlib.sha256((run/'meta.json').read_bytes()).hexdigest()}
try:
    np.linalg.cholesky(Gf)
    res['float_cholesky']='success'
except np.linalg.LinAlgError as e:res['float_cholesky']=str(e)
print(res['float_cholesky'],flush=True)
Gmp=mp.matrix([[mp_mid(G[i,j]) for j in range(n)] for i in range(n)])
try:
    L=mp.cholesky(Gmp)
    res['exact_midpoint_mp_cholesky']='success'
    print('mp Cholesky passed',time.time()-start,flush=True)
    T=mp.inverse(L).T
    Tb=arb_mat(n,n,[arb(mp.nstr(T[i,j],95)) for i in range(n) for j in range(n)])
    res['all_diagonal_intervals_exclude_zero']=all(not Tb[i,i].contains(0) for i in range(n))
    M=Tb.transpose()*G*Tb
    for i in range(n):M[i,i]-=1
    rows=[sum((abs(M[i,j]) for j in range(n)),arb(0)) for i in range(n)]
    upper=max((x.upper() for x in rows),key=mp_mid)
    res['congruence_error_infinity_upper']=str(upper)
    res['input_ball_G_positive_definite']=bool(upper<1 and res['all_diagonal_intervals_exclude_zero'])
    print('ball PD',res['input_ball_G_positive_definite'],str(upper),time.time()-start,flush=True)
except Exception as e:
    res['exact_midpoint_mp_cholesky']=repr(e)
    print('mp failed',repr(e),flush=True)
eps=mp.power(2,-80)
res['counterexample_exact_determinant']=mp.nstr(eps,50)
res['counterexample_float_last_entry']=float(1+eps)
res['seconds']=time.time()-start
(out/'check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2),flush=True)
