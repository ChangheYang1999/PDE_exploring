"""One selected cell: weighted density-moment recurrences and exact dyadic integer products."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,time,math,argparse
import flint,mpmath
from flint import fmpz_poly,ctx
from mpmath import iv
assert not sys.flags.optimize and flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
iv.dps=180;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy';N0=64;RADIAL=129;PREC=640;DEN=1<<(2*PREC)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ie(x):
 z=[]
 for sign,m,e,bc in x._mpi_:
  assert bc>=0;z.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 assert z[0]<=z[1];return z

def be(x):
 assert x['schema']=='arb-dyadic-mid-radius-v1';m=F(int(x['mid_m']))*F(2)**int(x['mid_e']);r=F(int(x['rad_m']))*F(2)**int(x['rad_e']);assert r>=0;return m-r,m+r

def decode(x):a,b=be(x);return iv.mpf([iq(a).a,iq(b).b])
def quant(x,p):
 a,b=ie(x);a*=1<<p;b*=1<<p;lo=a.numerator//a.denominator;hi=-((-b.numerator)//b.denominator);m=(lo+hi)//2;return m,max(m-lo,hi-m)
def out(x):a,b=ie(x);return {'lower_exact':str(a),'upper_exact':str(b)}
def write(p,x):
 with p.open('x') as f:json.dump(x,f,separators=(',',':'));f.write('\n');f.flush();os.fsync(f.fileno())
start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,required=True);args=ap.parse_args();manifest=json.loads((D/'data_exact/manifest.json').read_text());record=next(x for x in manifest['cells'] if x['cell']==args.cell);pins=dict(manifest['files'])
for n,hh in pins.items():assert sha(B/n)==hh
for p in [D/'data_exact/manifest.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
sample=next(x for x in json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'] if x['cell']==args.cell);tc=F(record['center_exact']);h=F(record['h_exact']);ht=iq(h);rad=4*ht;assert sample['t_exact']==str(tc) and h>0
trial=json.loads((B/'data_exact/modal_v2.json').read_text());k=F.from_float(float.fromhex(trial['scalars_hex']['k']));cinv=iq(1/k)
H=[[decode(v) for v in p] for p in sample['density_polynomial_at_point']];I=list(map(decode,sample['i']));J=list(map(decode,sample['j']));assert len(H)==262 and len(I)==len(J)==261 and all(len(p)==8 for p in H) and all(ie(x)==[0,0] for x in H[-1])
HP=[[3*p[q]+((q+1)*p[q+1] if q<7 else 0) for q in range(8)] for p in H]
C=[sum((abs(v)*rad**q for q,v in enumerate(p)),iv.mpf(0)) for p in H];CP=[sum((abs(v)*rad**q for q,v in enumerate(p)),iv.mpf(0)) for p in HP];Ds=[iv.exp(3*iq(tc)+3*rad)*v for v in C[:261]];Es=[iv.exp(3*iq(tc)+3*rad)*v for v in CP[:261]]
Pb=[];Qb=[]
for n in range(1,262):
 m=2*n;IB=iv.exp((m+4)*rad)*(abs(I[n-1])+rad*C[n-1]);JB=iv.exp(abs(m-4)*rad)*(abs(J[n-1])+rad*C[n]);fac=iv.exp(2*iq(tc)+2*rad);Pb.append(n*fac*(IB+JB));Qb.append(fac*(m*(IB+JB)+C[n-1]+C[n])/2)
DS=[sum(((2*a+1)**j*v for a,v in enumerate(Ds)),iv.mpf(0)) for j in range(7)];ES=[sum(((2*a+1)**j*v for a,v in enumerate(Es)),iv.mpf(0)) for j in range(6)];PS=[sum(((2*n)**j*v for n,v in enumerate(Pb,1)),iv.mpf(0)) for j in range(6)];QS=[sum(((2*n)**j*v for n,v in enumerate(Qb,1)),iv.mpf(0)) for j in range(6)]
Bs=[abs(cinv)*ES[j]+DS[j]+sum((math.comb(j,l)*(PS[l]*ES[j-l]+QS[l]*DS[j-l+1]) for l in range(j+1)),iv.mpf(0)) for j in range(6)];tails={}
for i in range(6):
 for j in range(6-i):tails['W_%d_%d'%(i,j)]=out(Bs[j]*iq(h**(-i)*F(math.factorial(65)//math.factorial(65-i),4**65)/(1-F(66,4*(66-i)))))
pre={'utc':datetime.now(timezone.utc).isoformat(),'cell':args.cell,'status':'COMPUTED_DENSITY_DISK_MAJORANTS_BEFORE_PRODUCTS','B_j':[out(x) for x in Bs],'tail_upper_inputs':tails,'h_exact':str(h),'radius_exact':'4','degree':64,'files':dict(sorted(pins.items()))}
write(D/'evidence'/('iv_preflight_%d.json'%args.cell),pre)
print(json.dumps({'phase':'disk_preflight','cell':args.cell,'B0_display_only':float(F(pre['B_j'][0]['upper_exact'])),'tail_5_0_display_only':float(F(tails['W_5_0']['upper_exact'])),'seconds':time.monotonic()-start}),flush=True)
scaled=[[v*ht**q for q,v in enumerate(p)] for p in H];scaledP=[[v*ht**q for q,v in enumerate(p)] for p in HP];expcoefs={}
for beta in [2,3]:
 es=[iv.exp(beta*iq(tc))]
 for q in range(1,65):es.append(es[-1]*beta*ht/q)
 expcoefs[beta]=es

def expoly(p,beta):return [sum((p[s]*expcoefs[beta][q-s] for s in range(min(q+1,len(p)))),iv.mpf(0)) for q in range(65)]
EH=[expoly(p,2) for p in scaled];R=[expoly(p,3) for p in scaled[:261]];Rt=[expoly(p,3) for p in scaledP[:261]]
Pv=[];Qv=[]
for n in range(1,262):
 m=2*n;K=[expcoefs[2][0]*I[n-1]];M=[expcoefs[2][0]*J[n-1]]
 for q in range(64):K.append(ht*(-(m+2)*K[-1]+EH[n-1][q])/(q+1));M.append(ht*((m-2)*M[-1]-EH[n][q])/(q+1))
 Pv.append([-n*(mm-kk) for kk,mm in zip(K,M)]);Qv.append([(m*(K[q]+M[q])-EH[n-1][q]-EH[n][q])/2 for q in range(65)])

def pack(values,even,sine,angular_derivative=False):
 offset=522 if even else 521;center=[0]*(2*offset*RADIAL+65);radius=[0]*len(center)
 for n,row in enumerate(values):
  freq=2*(n+1) if even else 2*n+1
  for q,x in enumerate(row):
   val=x*freq if angular_derivative else x
   if not sine:val/=2
   m,r=quant(val,PREC);a=(offset+freq)*RADIAL+q;b=(offset-freq)*RADIAL+q;center[a]=m;center[b]=-m if sine else m;radius[a]=radius[b]=r
 return fmpz_poly(center),fmpz_poly(radius),fmpz_poly([abs(v) for v in center])
def mul(x,y):
 a,r,aa=x;b,s,bb=y;return a*b,aa*s+r*bb+r*s
m1,r1=mul(pack(Pv,True,False),pack(Rt,False,True));m2,r2=mul(pack(Qv,True,True),pack(R,False,False,True));mc=m1+m2;rc=r1+r2
assert mc.degree()<=2086*RADIAL+128 and rc.degree()<=2086*RADIAL+128
# Only now read the independently computed physical result for comparisons.
firstpath=D/'evidence'/('arb_%d.json'%args.cell);first=json.loads(firstpath.read_text());assert first['cell']==args.cell and first['status']=='COMPUTED_PHYSICAL_GREEN_CELL_TAYLOR_NEEDS_INDEPENDENT_AUDIT'
for n,hh in first['files'].items():assert sha(B/n)==hh
point=json.loads((B/'research/residual_point_jets/evidence'/('iv_%d.json'%args.cell)).read_text());coefs=[];checks=0;jetchecks=0
for N in range(522):
 row=[]
 for q in range(65):
  idx=(1043+2*N+1)*RADIAL+q;m,r=int(mc[idx]),int(rc[idx]);assert r>=0
  if N<261:lm,lr=quant(cinv*Rt[N][q]-R[N][q],2*PREC);m+=lm;r+=lr
  a,b=F(m-r,DEN),F(m+r,DEN);u,v=be(first['coefficient_boxes'][N][q]);assert max(a,u)<=min(b,v),('METHOD_DISJOINT',args.cell,N,q);checks+=1
  if q<=5:
   scale=F(math.factorial(q))*h**(-q);u,v=be(point['coefficient_boxes'][q][N]);assert max(a*scale,u)<=min(b*scale,v),('POINT_DISJOINT',args.cell,N,q);jetchecks+=1
  row.append({'schema':'arb-dyadic-mid-radius-v1','mid_m':str(m),'mid_e':-2*PREC,'rad_m':str(r),'rad_e':-2*PREC})
 coefs.append(row)
assert checks==33930 and jetchecks==3132
for p in [firstpath]:pins[str(p.relative_to(B))]=sha(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_CELL_TAYLOR_RECURRENCES_AND_POINT_COMPARISONS','cell':args.cell,'degree':64,'modes':522,'coefficient_boxes':coefs,'coefficient_comparisons':checks,'point_jet_comparisons':jetchecks,'integer_polynomial_products':8,'B_j':pre['B_j'],'iv_dps':iv.dps,'quantization_bits':PREC,'seconds':time.monotonic()-start,'files':dict(sorted(pins.items())),'scope':'Selected cell Taylor coefficients only; full scalar and Cauchy audit still required.'}
write(D/'evidence'/('iv_%d.json'%args.cell),result)
print(json.dumps({k:result[k] for k in ['utc','status','cell','coefficient_comparisons','point_jet_comparisons','seconds']}),flush=True)
