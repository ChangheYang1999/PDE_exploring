import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import gzip,hashlib,json,time,shutil
import numpy as np
import mpmath as mp
from flint import arb,arb_mat,fmpz,ctx
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
RUN=LANE.parent/'s2-num/work/runs/L2fix_M4_s60_o12'
ctx.prec=384;ctx.threads=1;mp.mp.dps=140;t0=time.monotonic()
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for fn in ('meta.json','matrices_dyadic.json.gz','certificate.json'):
 shutil.copyfile(RUN/fn,TOP/'inputs'/fn)
meta=json.loads((TOP/'inputs/meta.json').read_text())
with gzip.open(TOP/'inputs/matrices_dyadic.json.gz','rt') as f:raw=json.load(f)
source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
assert sha(source)==meta['sha']=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
assert meta['operator']=='L_fix (no strain term)'
assert meta['ncol']==169 and meta['Mout']==12 and meta['ntest']==71
active=meta['test_active'];assert active==list(range(1,70));pos={v:i for i,v in enumerate(active)}
n=meta['ncol'];nt=len(active);nm=meta['Mout']
def ball(q):
 m,e,r,re=map(int,q);assert r>=0
 z=arb(fmpz(m))*arb(2)**e+arb(0,arb(fmpz(r))*arb(2)**re)
 assert z.is_finite();return z
def mpv(x):
 m,e=x.mid().man_exp();return mp.mpf(int(m))*mp.power(2,int(e))
def exact(x):
 m,e=x.mid().man_exp();return F(int(m))*F(2)**int(e)
def upper_norm(M):
 rows=[sum((abs(M[i,j]) for j in range(M.ncols())),arb(0)).upper() for i in range(M.nrows())]
 return max(rows,key=exact)
def error(M):
 E=arb_mat(M)
 for i in range(M.nrows()):E[i,i]-=1
 return upper_norm(E)
def whiten(M):
 n=M.nrows();Lm=mp.cholesky(mp.matrix([[mpv(M[i,j]) for j in range(n)] for i in range(n)]));Tm=mp.inverse(Lm).T
 T=arb_mat(n,n,[arb(mp.nstr(Tm[i,j],100)).mid() if i<=j else arb(0) for i in range(n) for j in range(n)])
 assert all(not T[i,i].contains(0) for i in range(n))
 return T
G=arb_mat(n,n);H=arb_mat(nt,nt);B=[arb_mat(nt,n) for _ in range(nm)]
for key,q in raw['GX'].items():
 i,j=map(int,key.split('|'));assert 0<=i<=j<n
 G[i,j]=ball(q);G[j,i]=ball(q)
for key,q in raw['GY'].items():
 i,j=map(int,key.split('|'));assert 0<=i<=j<meta['ntest']
 if i in pos and j in pos:H[pos[i],pos[j]]=ball(q);H[pos[j],pos[i]]=ball(q)
for key,q in raw['rows'].items():
 N,it,j=map(int,key.split('|'));assert 0<=N<nm and 0<=it<meta['ntest'] and 0<=j<n
 if it in pos:B[N][pos[it],j]=ball(q)
print(now(),'decoded',n,nt,nm,flush=True)
T=whiten(G);S=whiten(H);G1=T.transpose()*G*T;H1=S.transpose()*H*S
ge=error(G1);he=error(H1);assert ge<1 and he<1
print(now(),'whitened',str(ge),str(he),flush=True)
Hi=H1.inv();K=arb_mat(n,n)
for N in range(nm):
 C=S.transpose()*B[N]*T;K+=C.transpose()*Hi*C
 print(now(),'mode',N,'seconds',time.monotonic()-t0,flush=True)
K=(K+K.transpose())/2;G1=(G1+G1.transpose())/2
s=F(255457,500000);sb=arb(s.numerator)/s.denominator;M=K-G1*sb*sb
Mf=np.array([[float(M[i,j].mid()) for j in range(n)] for i in range(n)])
Lf=np.linalg.cholesky(Mf);L=arb_mat(n,n,[arb(float(x)) for x in Lf.ravel()]);Li=L.inv();er=error(Li*M*Li.transpose())
assert er<1
result={'date':now(),'status':'PASS_CONDITIONAL_ON_EXPORTED_ENTRIES','source_sha256':sha(source),
 'precision_bits':ctx.prec,'midpoint_digits':mp.mp.dps,'columns':n,'active_tests_per_mode':nt,'output_modes':nm,
 's_exact':str(s),'s_decimal':'0.510914','domain_gram_error':str(ge),'test_gram_error':str(he),'positive_difference_error':str(er),
 'seconds':time.monotonic()-t0,'input_hashes':{f:sha(TOP/'inputs'/f) for f in ('meta.json','matrices_dyadic.json.gz','certificate.json')},
 'proof_sha256':sha(TOP/'PROOF.md'),'code_sha256':sha(Path(__file__)),
 'scope':'finite projected L_fix bound only; exact-pairing input enclosure is not proved by this matrix calculation; no complement bound'}
(TOP/'evidence/check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
