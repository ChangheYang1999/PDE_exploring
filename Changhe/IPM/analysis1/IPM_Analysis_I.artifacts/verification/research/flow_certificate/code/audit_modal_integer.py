"""Integer-only exact box images for all alpha=0 middle modal maps."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,hashlib,argparse
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_certificate/evidence';sys.path.insert(0,str(E/'source'))
from cert_resid import Certifier
from midrad import MR
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def unit(x):
 n,d=float(x).as_integer_ratio();assert d&(d-1)==0;shift=1074-(d.bit_length()-1);assert shift>=0;return n<<shift

def make_rows(M):
 # Derive sine coefficients by four product-to-sum frequencies, combine repetitions.
 rows=[{} for j in range(M+1)]
 for m in range(M):
  for freq in [2*m+1,1-2*m,2*m+3,3-2*m]:
   sign=1 if freq>0 else -1;j=(abs(freq)-1)//2
   if j<=M:rows[j][m]=rows[j].get(m,0)+sign
 return [{k:v for k,v in row.items() if v} for row in rows]
def combine(a,b,ca,cb):
 z={k:ca*v for k,v in a.items()}
 for k,v in b.items():z[k]=z.get(k,0)+cb*v
 return [(k,v) for k,v in z.items() if v]
def dot(row,m,r):return sum(v*m[k] for k,v in row),sum(abs(v)*r[k] for k,v in row)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--first',type=int,default=0);ap.add_argument('--count',type=int,default=7809);ap.add_argument('--tag',default='modal_integer_full');a=ap.parse_args();start=time.monotonic();data=B.parent/'ipmA-num/data/cert_green.npz';pins={str(p):sha(p) for p in [Path(__file__),data,E/'source/cert_resid.py',E/'source/midrad.py']};z=np.load(data);tm=z['T_mid'];tr=z['T_rad'];assert tm.shape==tr.shape and tm.shape[0]==7809 and tm.shape[1]==8 and np.isfinite(tm).all() and np.isfinite(tr).all() and (tr>=0).all();M=tm.shape[2];C=Certifier.__new__(Certifier);C.M=M;C.Nf=M+1;rows=make_rows(M);R=[list(r.items()) for r in rows];F0=[];F1=[]
 for n in range(1,M+2):
  l=rows[n-1];r=rows[n] if n<=M else {};F0.append(combine(l,r,4-2*n,4+2*n));F1.append(combine(l,r,1,1))
 stop=min(a.first+a.count,len(tm));count=0;cells=0;digest=hashlib.sha256()
 for ci in range(a.first,stop):
  ft,rt=C.f_terms_from_a([(MR.exact(0.),MR(tm[ci],tr[ci]))]);out=[rt[0][1],rt[0][2],MR(ft[0][1].m.T,ft[0][1].r.T)];assert all(np.isfinite(o.m).all() and np.isfinite(o.r).all() for o in out)
  mid=[[unit(v) for v in row] for row in tm[ci]];rad=[[unit(v) for v in row] for row in tr[ci]];rc=[[dot(R[j],mid[q],rad[q]) for j in range(M+1)] for q in range(8)]
  for q in range(8):
   for j in range(M+1):
    rm,rr=rc[q][j];nm,nr=rc[q+1][j] if q<7 else (0,0)
    values=[(2*rm,2*rr),(6*rm+2*(q+1)*nm,6*rr+2*(q+1)*nr)]
    fm,fr=dot(F0[j],mid[q],rad[q]);dm,dr=dot(F1[j],mid[q+1],rad[q+1]) if q<7 else (0,0);values.append((fm+(q+1)*dm,fr+(q+1)*dr))
    for kind,(m,r) in enumerate(values):
     om=16*unit(out[kind].m[q,j]);orr=16*unit(out[kind].r[q,j]);assert om-orr<=m-r<=m+r<=om+orr,(ci,q,j,kind);count+=1
  cells+=1;digest.update(f'{ci}:{count}\n'.encode())
  if cells%100==0:
   progress={'utc':datetime.now(timezone.utc).isoformat(),'first':a.first,'last':ci,'cells':cells,'checks':count,'seconds':time.monotonic()-start};(E/f'{a.tag}_progress.json').write_text(json.dumps(progress)+'\n');print(json.dumps(progress),flush=True)
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_INTEGER_INPUT_BOX_IMAGES','first':a.first,'stop_exclusive':stop,'cells':cells,'checks':count,'expected_checks_per_cell':3*8*(M+1),'alpha_exact':'0','coverage_digest':digest.hexdigest(),'seconds':time.monotonic()-start,'files':pins,'method':'Product-to-sum sine map rebuilt; all finite binary64 inputs scaled to exact integers in units2^-1074; modal weights in units1/16; exact minimal image including repeated-input dependencies compared with source output boxes.','scope':'Only stated middle cells, R,dR,F coefficient enclosures. No full field, tail or inverse claim.'};(E/f'{a.tag}.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o),flush=True)
if __name__=='__main__':main()
