from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import gzip,hashlib,json,time,shutil
import numpy as np
import mpmath as mp
from flint import arb,arb_mat,fmpz,ctx
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parents[1]/'evidence'
run=root.parent/'s2-num/work/runs/S0_M4_s60_o12'
ctx.prec=384;mp.mp.dps=100;t0=time.time()
for fn in ('meta.json','matrices_dyadic.json.gz','certificate.json'):
 shutil.copyfile(run/fn,out/fn)
meta=json.loads((out/'meta.json').read_text())
with gzip.open(out/'matrices_dyadic.json.gz','rt') as f:raw=json.load(f)
reported=json.loads((out/'certificate.json').read_text())
source=root.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
source_sha=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_sha==meta['sha']
res={'start':datetime.now(timezone.utc).isoformat(),'source_sha256':source_sha,'precision':ctx.prec,'mp_digits':mp.mp.dps,'hashes':{f:hashlib.sha256((out/f).read_bytes()).hexdigest() for f in ('meta.json','matrices_dyadic.json.gz','certificate.json')},'input_condition':'exported entries enclose the exact finite-section pairings; not independently established by this matrix calculation'}
def ball(q):
 m,e,r,re=map(int,q)
 return arb(fmpz(m))*arb(2)**e+arb(0,arb(fmpz(r))*arb(2)**re)
def mpv(x):
 m,e=x.mid().man_exp();return mp.mpf(int(m))*mp.power(2,int(e))
def upper_norm(M):
 rows=[sum((abs(M[i,j]) for j in range(M.ncols())),arb(0)).upper() for i in range(M.nrows())]
 def exact_key(x):
  m,e=x.mid().man_exp();return Fraction(int(m))*Fraction(2)**int(e)
 return max(rows,key=exact_key)
def identity_error(M):
 E=arb_mat(M)
 for i in range(M.nrows()):E[i,i]-=1
 return upper_norm(E)
def whiten(M):
 n=M.nrows();L=mp.cholesky(mp.matrix([[mpv(M[i,j]) for j in range(n)] for i in range(n)]));T=mp.inverse(L).T
 Tb=arb_mat(n,n,[arb(mp.nstr(T[i,j],95)).mid() for i in range(n) for j in range(n)])
 assert all(not Tb[i,i].contains(0) for i in range(n))
 return Tb
nc=meta['ncol'];n=nc+1;nt=meta['ntest'];nm=meta['Mout']
assert meta['weights']['sX']==meta['weights']['sY']==1
G=arb_mat(n,n);H=arb_mat(nt,nt)
for key,q in raw['GX'].items():
 i,j=map(int,key.split('|'));x=ball(q)*(1+4*meta['columns'][i]['m']**2);G[i,j]=x;G[j,i]=x
for key,q in raw['GY'].items():
 i,j=map(int,key.split('|'));x=ball(q);H[i,j]=x;H[j,i]=x
labels=[q['label'] for q in meta['columns']];G[labels.index('J'),labels.index('J')]=1;G[n-1,n-1]=1
kq=Fraction(meta['k']);k=arb(kq.numerator)/kq.denominator
D=3/k+k*ball(meta['cKP']);assert not D.contains(0)
d=[-k*ball(c['c'])/D for c in meta['columns']]+[-k*ball(meta['cTAU'])/D]
for i in range(n):
 for j in range(n):G[i,j]+=d[i]*d[j]
B=[arb_mat(nt,n) for _ in range(nm)];BK=[arb_mat(nt,1) for _ in range(nm)]
for key,q in raw['rows'].items():
 N,it,j=map(int,key.split('|'));B[N][it,j]=ball(q)
for key,q in raw['rows_tau'].items():
 N,it=map(int,key.split('|')[:2]);B[N][it,n-1]=ball(q)
for key,q in raw['rows_kp'].items():
 N,it=map(int,key.split('|')[:2]);BK[N][it,0]=ball(q)
for it in (0,nt-1):
 for j in range(nt):H[it,j]=0;H[j,it]=0
 H[it,it]=1
for N in range(nm):
 for it in range(nt):
  for j in range(n):B[N][it,j]=0 if it in (0,nt-1) else B[N][it,j]+d[j]*BK[N][it,0]
print('decoded',n,nt,nm,'seconds',time.time()-t0,flush=True)
T=whiten(G);S=whiten(H)
G1=T.transpose()*G*T;H1=S.transpose()*H*S
ge=identity_error(G1);he=identity_error(H1)
res['domain_gram_error']=str(ge);res['test_gram_error']=str(he)
assert ge<1 and he<1
print('whitened',str(ge),str(he),'seconds',time.time()-t0,flush=True)
Hi=H1.inv();K=arb_mat(n,n)
for N in range(nm):
 C=S.transpose()*B[N]*T
 K+=C.transpose()*Hi*C/(1+(2*N+1)**2)
 print('output mode',N,'seconds',time.time()-t0,flush=True)
K=(K+K.transpose())/2;G1=(G1+G1.transpose())/2
sf=float(reported['verified_lower_bound']);sq=Fraction(sf);sb=arb(sq.numerator)/sq.denominator
M=K-G1*sb*sb
Mf=np.array([[float(M[i,j].mid()) for j in range(n)] for i in range(n)])
L=np.linalg.cholesky(Mf);Lb=arb_mat(n,n,[arb(float(x)) for x in L.ravel()]);Li=Lb.inv()
E=Li*M*Li.transpose()
for i in range(n):E[i,i]-=1
err=upper_norm(E)
res.update({'s_exact':str(sq),'s_float':sf,'positive_difference_error':str(err),'conditional_matrix_certificate':bool(err<1),'finish':datetime.now(timezone.utc).isoformat(),'seconds':time.time()-t0})
(out/'check.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2),flush=True)
