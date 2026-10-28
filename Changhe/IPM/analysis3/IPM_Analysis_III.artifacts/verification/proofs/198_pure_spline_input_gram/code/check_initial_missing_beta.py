"""Independent exact-rational input Gram from the archived original knots."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from datetime import datetime,timezone
import hashlib,json,importlib.util,time
import numpy as np
from flint import arb,arb_mat,ctx
ROOT=Path(__file__).resolve().parents[3];TOP=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
spec=importlib.util.spec_from_file_location('independent_deboor',ROOT/'proofs/04_modal_scalar/code/recompute.py');db=importlib.util.module_from_spec(spec);spec.loader.exec_module(db)
ctx.prec=512;ctx.threads=1

def stamp():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):
 if not isinstance(q,F):q=F(q)
 return arb(q.numerator)/q.denominator

def dyadic(x):
 n,e=x.mid().man_exp();return [str(n),int(e)]
def pack(x):return {'ball':x.str(42),'lo_binary':dyadic(x.lower()),'hi_binary':dyadic(x.upper())}
def unpack(d):
 def one(v):
  n,e=v;return F(int(n))*F(2)**e
 lo,hi=one(d['lo_binary']),one(d['hi_binary']);return aa((lo+hi)/2)+arb(0,aa((hi-lo)/2).upper())
def rat(x):return F.from_float(float(x))
def padd(a,b):
 z=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):z[i]+=v
 for i,v in enumerate(b):z[i]+=v
 return z

def plin(p,a,b):
 z=[F(0)]*(len(p)+1)
 for i,v in enumerate(p):z[i]+=a*v;z[i+1]+=b*v
 return z

def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z

def cox(knots,span):
 a,b=knots[span:span+2];h=b-a;cur={span:[F(1)]}
 for degree in range(1,8):
  nxt={}
  for i in range(span-degree,span+1):
   v=[F(0)]*(degree+1)
   den=knots[i+degree]-knots[i]
   if den and i in cur:v=padd(v,plin(cur[i],(a-knots[i])/den,h/den))
   den=knots[i+degree+1]-knots[i+1]
   if den and i+1 in cur:v=padd(v,plin(cur[i+1],(knots[i+degree+1]-a)/den,-h/den))
   nxt[i]=v
  cur=nxt
 return cur

def transform(p,a,b):
 z=[F(0)]*len(p)
 for j,v in enumerate(p):
  for k in range(j+1):z[k]+=v*comb(j,k)*a**(j-k)*b**k
 return z

def moments(z,degree,method):
 z=aa(z)
 if method=='taylor':
  N=160;out=[arb(0) for _ in range(degree+1)];power=arb(1)
  for n in range(N):
   for j in range(degree+1):out[j]+=power/(n+j+1)
   power*=z/(n+1)
  return [x+arb(0,(abs(z).exp()*abs(power)/(N+j+1)).upper()) for j,x in enumerate(out)]
 assert not z.contains(0)
 ez=z.exp();out=[(ez-1)/z]
 for j in range(1,degree+1):out.append(ez/z-j*out[-1]/z)
 return out

def compute(knots,pieces,method):
 R=[[arb(0) for _ in range(26)] for _ in range(26)];strain=[arb(0) for _ in range(26)];parts=0
 for ci,polys in enumerate(pieces):
  a,b=knots[ci+7:ci+9];h0=b-a;cuts=[a]+([F(0)] if a<0<b else [])+[b]
  for lo,hi in zip(cuts,cuts[1:]):
   parts+=1;h=hi-lo;ps={i:transform(v,(lo-a)/h0,h/h0) for i,v in polys.items() if 4<=i<=29}
   lam=F(-1,2) if hi<=0 else F(27,4)
   ms=moments(lam*h,14,method);pre=aa(h)*aa(lam*lo).exp()
   cs=moments(2*h,7,method);cpre=aa(h)*aa(2*lo).exp()
   for i,p in ps.items():
    strain[i-4]+=cpre*sum((aa(v)*cs[j] for j,v in enumerate(p)),arb(0))
    for j,q in ps.items():
     R[i-4][j-4]+=pre*sum((aa(v)*ms[k] for k,v in enumerate(mul(p,q))),arb(0))
 return R,strain,parts

def maxrow(M):
 return max(sum(abs(M[i,j]) for j in range(M.ncols())).upper() for i in range(M.nrows()))
def comparison(G,B):
 n=len(G);GM=arb_mat(G);mid=np.array([[float(x.mid()) for x in row] for row in G]);L=np.linalg.cholesky(mid)
 T=np.linalg.solve(L.T,np.eye(n));TM=arb_mat([[aa(rat(x)) for x in row] for row in T]);I=arb_mat(np.eye(n,dtype=int).tolist())
 e=maxrow(TM.transpose()*GM*TM-I)
 BM=arb_mat([[aa(rat(x)) for x in row] for row in B]);d=maxrow(TM.transpose()*(BM-GM)*TM)
 assert e<1
 return {'n':n,'whitening_identity_error':pack(e),'transformed_error':pack(d),'relative_quadratic_form_error':pack(d/(1-e)),'T_sha256':hashlib.sha256(T.tobytes()).hexdigest(),'midpoint_normalized_Gram_condition':float(np.linalg.cond(mid/np.sqrt(np.outer(np.diag(mid),np.diag(mid)))))}

def main():
 started=time.monotonic();assert sha(SRC)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 data=np.load(SRC,allow_pickle=False);assert int(data['p'])==7
 fine=list(map(rat,data['knots']));assert fine[:8]==[fine[0]]*8 and fine[-8:]==[fine[-1]]*8
 interior=fine[8:-8][::60];knots=[fine[0]]*8+interior+[fine[-1]]*8
 nb=len(knots)-8;assert nb==34;spans=list(range(7,len(knots)-8));assert len(spans)==27 and all(knots[s]<knots[s+1] for s in spans)
 pieces=[];replay=[];checks=0
 for span in spans:
  ps=cox(knots,span);ds={}
  total=[F(0)]*8
  for i,p in ps.items():
   co=[F(int(j==i)) for j in range(nb)];ds[i]=db.deboor_poly(knots,co,7,span);assert p==ds[i];checks+=1;total=padd(total,p)
  assert total==[F(1)]+[F(0)]*7;pieces.append(ps);replay.append(ds)
 for ci in range(26):
  w1=knots[ci+8]-knots[ci+7];w2=knots[ci+9]-knots[ci+8]
  for i in range(nb):assert db.jets(pieces[ci].get(i,[F(0)]*8),w1,True)==db.jets(pieces[ci+1].get(i,[F(0)]*8),w2,False)
 for i in range(4,30):
  assert db.jets(pieces[0].get(i,[F(0)]*8),knots[8]-knots[7],False)[:4]==[F(0)]*4
  assert db.jets(pieces[-1].get(i,[F(0)]*8),knots[-8]-knots[-9],True)[:4]==[F(0)]*4
 R,C,nparts=compute(knots,pieces,'taylor')
 print(json.dumps({'date':stamp(),'stage':'production','parts':nparts,'seconds':time.monotonic()-started}),flush=True)
 ctx.prec=640;RR,CC,nreplay=compute(knots,replay,'antiderivative');assert nparts==nreplay==28
 for i in range(26):
  assert C[i].overlaps(CC[i]) and C[i]>0
  for j in range(26):assert R[i][j].overlaps(RR[i][j])
 # Independent Beta evaluation by gamma products and the rising ratio recurrence.
 I0=2*(arb(1)/2).beta(arb(1)/4);I0b=2*(arb(1)/2).gamma()*(arb(1)/4).gamma()/(arb(3)/4).gamma();assert I0.overlaps(I0b)
 ratios=[F(1)]
 for j in range(5):ratios.append(ratios[-1]*F(4*j+2,4*j+3))
 Q=[[F(0),F(2)],[F(0),F(0),F(0),F(-8)],[F(0),F(2),F(0),F(-16),F(0),F(32)]]
 Arat=[[sum((v*ratios[k//2] for k,v in enumerate(mul(p,q)) if k%2==0),F(0)) for q in Q] for p in Q]
 A=[[I0*aa(v) for v in row] for row in Arat]
 # Different sine expansion and Beta calls check every angular entry.
 for m,p in enumerate(Q):
  for n,q in enumerate(Q):
   direct=sum((aa(v)*2*(arb(k+1)/2).beta(arb(1)/4) for k,v in enumerate(mul(p,q)) if k%2==0),arb(0));assert direct.overlaps(A[m][n])
 output={'date':stamp(),'verdict':'PENDING_OUTPUT_AUDIT','source_sha256':sha(SRC),'script_sha256':sha(__file__),'proof_sha256':sha(TOP/'PROOF.md'),'coarse_knots_exact':list(map(str,knots)),'radial_indices':list(range(4,30)),'coarse_span_count':27,'integration_part_count':nparts,'exact_unit_column_polynomial_checks':checks,'exact_C6_interior_joins':26*nb,'production_bits':512,'independent_replay_bits':640,'angular_rational_matrix':[[str(x) for x in row] for row in Arat],'angular_common_I0':pack(I0),'radial_Gram':[[pack(x) for x in row] for row in R],'radial_strain':list(map(pack,C)),'runs':{}}
 for tag in ('S1M3','S1M4P'):
  mp=TOP/'evidence/source'/f'{tag}_meta.json';meta=json.loads(mp.read_text());idx=[];decl=[];gram=[];strainerrors=[]
  for j,col in enumerate(meta['new']):
   typ,label,m=col
   if typ=='rem' and label in [f'sp{i}' for i in range(4,30)]:
    ri=int(label[2:])-4;orig=[j0 for j0,(lab,mm) in enumerate(zip(meta['labels'],meta['col_m'])) if lab==label and mm==0];assert len(orig)==1
    scale=rat(meta['column_scales'][orig[0]]);assert scale>0
    idx.append(j);decl.append((ri,m-1,scale));cv=aa((F(3,8),F(-3,8),F(1,8))[m-1])*C[ri]/aa(scale)
    strainerrors.append(abs(aa(rat(meta['cvec'][j]))/cv-1))
  for i,m,s in decl:gram.append([A[m][n]*R[i][j]/aa(s*t) for j,n,t in decl])
  record={'metadata_sha256':sha(mp),'selected_new_indices':idx,'basis_declaration':[[i+4,m+1,str(s)] for i,m,s in decl],'maximum_relative_stored_strain_error':pack(max(x.upper() for x in strainerrors)),'exact_scaled_input_Gram':[[pack(x) for x in row] for row in gram]}
  if tag=='S1M3':
   file=ROOT/'proofs/183_s1m3_floating_audit/evidence/parts_matrices.npz';mat=np.load(file,allow_pickle=False);Gf=mat['G'][np.ix_(idx,idx)];record['floating_matrix_sha256']=sha(file);record['comparison']=comparison(gram,Gf)
  output['runs'][tag]=record
  print(json.dumps({'date':stamp(),'stage':tag,'n':len(idx),'strain_error':record['maximum_relative_stored_strain_error']['ball'],'comparison':record.get('comparison'),'seconds':time.monotonic()-started}),flush=True)
 output['date']=stamp();output['seconds']=time.monotonic()-started
 (TOP/'evidence/gram_512_640.json').write_text(json.dumps(output,indent=2)+'\n')
 print(json.dumps({'date':stamp(),'stage':'finished','seconds':time.monotonic()-started,'output_sha256':sha(TOP/'evidence/gram_512_640.json')}),flush=True)
if __name__=='__main__':main()
