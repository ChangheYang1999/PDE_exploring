"""Exact stored tail audit. Does not execute the source modules or an operator."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys
sys.dont_write_bytecode=True
import ast,json,hashlib,zipfile,struct,re,math,time
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import fmpq,arb,ctx
from mpmath import iv
import numpy as np
B=Path(__file__).resolve().parents[3];D=B/'research/scaling_tail_obstruction';E=D/'evidence'
V='research/saved_vector_external_constraints/sources/c2gram2_M16_s16_p4_H1m_NJ1_rowsH1q_vec.npz';VH='4fd4ff818efd62aa03cb4392d8d56dcaf8f948188962fc1133c38c561099ba2e'
S='data_exact/modal_v2.json';SH='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
def now():return datetime.now(timezone.utc).isoformat()
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def qf(x):return F(int(x.numerator),int(x.denominator))
def hx(s):
 m=re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]*)p([+-]?\d+)',s);need(m is not None,'hex')
 sg,a,b,e=m.groups();return F((-1 if sg=='-' else 1)*int(a+b,16))*F(2)**(int(e)-4*len(b))
def ieee(b):
 need(len(b)==8,'word size');u=int.from_bytes(b,'little');sg=-1 if u>>63 else 1;e=(u>>52)&2047;m=u&((1<<52)-1);need(e!=2047,'finite IEEE')
 return sg*F(m if e==0 else m+(1<<52))*F(2)**(-1074 if e==0 else e-1075)
def npy(b,shape):
 need(b[:8]==b'\x93NUMPY\x01\x00','NPY v1');l=int.from_bytes(b[8:10],'little');h=ast.literal_eval(b[10:10+l].decode());need(h=={'descr':'<f8','fortran_order':False,'shape':shape},'exact NPY shape/type/order');raw=b[10+l:];count=math.prod(shape);need(len(raw)==8*count,'complete bytes');return [ieee(raw[i:i+8]) for i in range(0,len(raw),8)]
def rn(q):
 q=F(q)
 if not q:return q
 sg=1 if q>0 else -1;q=abs(q);e=q.numerator.bit_length()-q.denominator.bit_length()
 if q<F(2)**e:e-=1
 need(e<=1023,'finite rounded normal range');step=F(2)**max(-1074,e-52);a=q/step;i,r=divmod(a.numerator,a.denominator)
 if 2*r>a.denominator or (2*r==a.denominator and i%2):i+=1
 return sg*i*step

def ai(q):return arb(q.numerator)/arb(q.denominator)
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ie(t):s,m,e,b=t;need(b>=0,'finite iv');return (-1)**s*F(int(m))*F(2)**int(e)
def enclose(A,C,exact):
 ar=ai(A[0])*ai(C[1])-ai(A[1])*ai(C[0]);ir=ii(A[0])*ii(C[1])-ii(A[1])*ii(C[0]);a=[qf(ar.lower().fmpq()),qf(ar.upper().fmpq())];b=list(map(ie,ir._mpi_));lo=F('5.859714460078e-15');hi=F('5.859714460080e-15')
 for z in [a,b]:need(lo<z[0]<=exact<=z[1]<hi,'two rigorous determinant bounds')
 return {'exact':str(exact),'arb256':list(map(str,a)),'iv100':list(map(str,b)),'strict_decimal_lower':str(lo),'strict_decimal_upper':str(hi)}
def main():
 start=now();tic=time.monotonic();pins={}
 for n,h in [(V,VH),(S,SH)]:need(sha(B/n)==h,'fixed input');pins[n]=h
 pr=load(E/'proof_first.json');need(pr['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pr['utc'])<datetime.fromisoformat(start),'proof first')
 with zipfile.ZipFile(B/V) as z:
  need(len(z.namelist())==len(set(z.namelist())),'no duplicate ZIP');A=npy(z.read('A0.npy'),(260,));C=npy(z.read('Bm.npy'),(261,));k=npy(z.read('k.npy'),())[0];t0=npy(z.read('t0.npy'),())[0]
 with np.load(B/V,allow_pickle=False) as z:
  for key,seq in [('A0',A),('Bm',C),('k',[k]),('t0',[t0])]:need([F(*float(x).as_integer_ratio()) for x in z[key].ravel()]==seq,'independent NumPy exact import')
 src=load(B/S);need(src['arrays']['Aout']['shape']==[260,10],'Aout shape');aout=list(map(hx,src['arrays']['Aout']['hex']));need(A==aout[::10] and k==hx(src['scalars_hex']['k']) and t0==hx(src['arrays']['knots']['hex'][-1]),'entire leading vector source identity');need(0<k<1 and A[0]!=0,'nonzero leading vector and nondegenerate k')
 copied_modal=(D/'sources/modal_fit.py').read_text();tree=ast.parse(copied_modal);assign=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='OUTER_JL' for t in n.targets));jl=ast.literal_eval(assign.value);need([list(x) for x in jl]==src['outer_jl'] and jl[0]==(0,0),'actual rate index list');need(all(j>=0 and l>=0 and (j,l)!=(0,0) for j,l in jl[1:]),'strict lower rate pairs')
 exact_rates=[k-3-j*(1-k)-2*l for j,l in jl];rounded_rates=[rn(rn(rn(k-3)-rn(j*rn(1-k)))-2*l) for j,l in jl];float_rates=[F((float(k)-3)-j*(1-float(k))-2*l) for j,l in jl];need(rounded_rates==float_rates,'independent nearest-even rate arithmetic');bo=hx(src['scalars_hex']['bo']);rates={}
 for name,seq in [('mathematical',exact_rates),('literal_binary64',rounded_rates)]:
  leading=seq[0];gaps=[leading-r for r in seq[1:]+[-bo]];need(all(g>0 for g in gaps) and -2-leading>0,'every lower exponent and scaling factor');rates[name]={'leading_exact':str(leading),'scaling_factor_exact':str(-2-leading),'minimum_gap_exact':str(min(gaps)),'all_gaps_exact':list(map(str,gaps))}
 expected=[F(0)]*261;expected[0]=rn(A[1]/2);expected[1]=rn(A[0]+rn(A[2]/2))
 for j in range(2,260):expected[j]=rn(rn(A[j-1]+A[j+1])/2) if j+1<260 else rn(A[j-1]/2)
 need(C==expected,'all literal Bm source operations');ideal=[F(0)]*261;ideal[0]=A[1]/2;ideal[1]=A[0]+A[2]/2
 for j in range(2,261):ideal[j]=((A[j-1] if j-1<260 else 0)+(A[j+1] if j+1<260 else 0))/2
 c={0:fmpq(str(A[0]))}
 for j in range(1,260):c[j]=c[-j]=fmpq(str(A[j]))/2
 prod={}
 for j,v in c.items():
  for d in [-1,1]:prod[j+d]=prod.get(j+d,fmpq(0))+v/2
 scatter=[qf(prod.get(0,fmpq(0)))]+[qf(prod.get(j,fmpq(0))+prod.get(-j,fmpq(0))) for j in range(1,261)]
 need(scatter==ideal,'independent Laurent scatter ideal product');need(C[260]==0 and ideal[260]==A[259]/2!=0,'literal omitted highest mode')
 det=A[0]*C[1]-A[1]*C[0];detq=qf(fmpq(str(A[0]))*fmpq(str(C[1]))-fmpq(str(A[1]))*fmpq(str(C[0])));need(det==detq>0,'two exact nonzero determinant calculations');ideal_det=A[0]*ideal[1]-A[1]*ideal[0];need(ideal_det==qf(fmpq(str(A[0]))*fmpq(str(ideal[1]))-fmpq(str(A[1]))*fmpq(str(ideal[0])))>0,'ideal exact second determinant')
 ctx.prec=256;ctx.threads=1;iv.dps=100;enclosures={'stored':enclose(A,C,det),'ideal_full_product':enclose(A,ideal,ideal_det)}
 # Guard tests matter because the claimed finite input is exact, not a lossy float import.
 rejected=0
 for bad in [struct.pack('<Q',2047<<52),struct.pack('<Q',(2047<<52)|1),b'123']:
  try:ieee(bad)
  except ValueError:rejected+=1
  else:raise ValueError('invalid IEEE accepted')
 for q in [F(1)+F(1,2**53),F(1)+F(3,2**53),-F(1)-F(1,2**53),F(1,2**1075),F(3,2**1075)]:need(rn(q)==F(float(q)),'nearest even tie cases')
 for n in ['PROOF.md','evidence/proof_first.json','sources/c2_fminus.py','sources/modal_fit.py','sources/prior_referee_PROOF.md','code/check.py']:pins[str((D/n).relative_to(B))]=sha(D/n)
 for n,h in pins.items():need(sha(B/n)==h,'final immutable input')
 result={'start_utc':start,'utc':now(),'status':'PASS_EXACT_STORED_AND_IDEAL_TAIL_OBSTRUCTION_REQUIRES_ACTUAL_REVIEW','counts':{'manual_and_numpy_scalars':523,'leading_coefficients_bound':260,'literal_Bm_operations':261,'ideal_product_two_routes':261,'strict_lower_rates_each_convention':10,'exact_determinants_two_routes':2,'directed_determinants_each_engine':2,'IEEE_rejections':rejected,'nearest_even_tie_cases':5},'first_A_exact':list(map(str,A[:3])),'first_B_exact':list(map(str,C[:2])),'rates':rates,'determinants':enclosures,'omitted_ideal_B260_exact':str(ideal[260]),'rounded_product_discrepancies':sum(x!=y for x,y in zip(C,ideal)),'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tic,'scope':'Exact explicitly frozen stored-tail trial and Fminus recipe, separately exact mathematical and literal binary64 rates; ideal cosine product a separate application. No canonical normalization/X3/runtime attestation/free-class nonmembership/norm distance/inverse/endpoint.'}
 with (E/'checks.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({k:result[k] for k in ['utc','status','counts','seconds','rounded_product_discrepancies','omitted_ideal_B260_exact']}))
if __name__=='__main__':main()
