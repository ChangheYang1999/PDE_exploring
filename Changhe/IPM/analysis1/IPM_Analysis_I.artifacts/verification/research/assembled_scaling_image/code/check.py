"""Exact saved-array summation and independent nodal/edge finite norms only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from flint import fmpq,arb,ctx
from mpmath import iv
import numpy as np
import zipfile,ast,struct,math,json,hashlib,time,re
B=Path(__file__).resolve().parents[3];D=B/'research/assembled_scaling_image';E=D/'evidence';S=E/'source'
ctx.prec=320;iv.dps=100;N=467;M=40;ROWS=['L2','L2q','H1','H1q']
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def fq(q):return fmpq(q.numerator,q.denominator)
def aa(q):return arb(q.numerator)/arb(q.denominator)
def ii(q):return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ab(v):
 need(v.is_finite(),'finite Arb output');return [F(str(v.lower().fmpq())),F(str(v.upper().fmpq()))]
def ib(v):
 out=[]
 for s,m,e,b in v._mpi_:
  need(b>=0,'finite iv output');out.append((-1)**s*F(m)*F(2)**e)
 return out
def ss(b):return [str(v) for v in b]
def envelope(a,b):
 need(max(a[0],b[0])<=min(a[1],b[1]),'independent interval overlap');return [min(a[0],b[0]),max(a[1],b[1])]
def manual(path,name):
 with zipfile.ZipFile(path) as z:
  names=z.namelist();need(len(names)==len(set(names)),'unique zip members');buf=z.read(name+'.npy')
 need(buf[:6]==b'\x93NUMPY','NPY magic');v=tuple(buf[6:8]);need(v in [(1,0),(2,0)],'NPY version');sz=2 if v==(1,0) else 4;ln=int.from_bytes(buf[8:8+sz],'little');h=ast.literal_eval(buf[8+sz:8+sz+ln].decode('latin1'));need(set(h)=={'descr','fortran_order','shape'} and h['fortran_order'] is False and type(h['shape']) is tuple,'NPY fixed schema');shape=h['shape'];need(all(type(x) is int and x>=0 for x in shape),'NPY dimensions');descr=h['descr'];need(descr in ['<f8','<i8'],'numeric64 NPY');data=buf[8+sz+ln:];count=math.prod(shape);need(len(data)==8*count,'NPY exact length');out=[]
 for (bits,) in struct.iter_unpack('<Q',data):
  if descr=='<i8':out.append(fmpq(bits-(1<<64) if bits>>63 else bits));continue
  exp=(bits>>52)&2047;mant=bits&((1<<52)-1);need(exp!=2047,'finite IEEE');power=exp-1075 if exp else -1074;sig=mant+(1<<52) if exp else mant;val=fmpq((-1 if bits>>63 else 1)*sig);out.append(val*(fmpq(2)**power))
 return shape,descr,out
checks={'manual_ieee_values':0,'summed_entries_twice':0,'shape_checks':0,'range_checks':0,'geometry_checks':0}
def read_numeric(path,name,shape):
 sh,descr,q=manual(path,name);need(sh==shape,'fixed numeric shape');checks['shape_checks']+=1
 with np.load(path,allow_pickle=False) as z:
  a=z[name];need(a.shape==shape and a.dtype==np.dtype('float64' if descr=='<f8' else 'int64'),'NumPy independent schema');f=[F.from_float(float(v)) if descr=='<f8' else F(int(v)) for v in a.flat]
 for u,v in zip(f,q,strict=True):need(fq(u)==v,'all independent exact imports');checks['manual_ieee_values']+=1
 return f,q

def arb_forms(values,t,w):
 t=list(map(aa,t));w=list(map(aa,w));dd=[t[i+1]-t[i] for i in range(N-1)];om=[dd[0]/2]+[(dd[i-1]+dd[i])/2 for i in range(1,N-1)]+[dd[-1]/2];wb=[(w[i]+w[i+1])/2 for i in range(N-1)];v=list(map(aa,values));s=[arb(0) for _ in ROWS]
 for i in range(N):
  for n in range(M):
   u=(w[i]*v[i*M+n])**2;fac=1+(2*n+1)**2;s[0]+=u;s[1]+=om[i]*u;s[2]+=fac*u;s[3]+=fac*om[i]*u
 for i in range(N-1):
  for n in range(M):
   u=(wb[i]*(v[(i+1)*M+n]-v[i*M+n])/dd[i])**2;s[2]+=u;s[3]+=dd[i]*u
 return s

def iv_forms(values,t,w):
 # Edge-trapezoid formula, descending mode/row order and exact rational weights.
 ds=[t[i+1]-t[i] for i in range(N-1)];wt=[ii(x*x) for x in w];dd=list(map(ii,ds));dc=[ii((w[i]+w[i+1])**2/(4*ds[i]**2)) for i in range(N-1)];qc=[ii((w[i]+w[i+1])**2/(4*ds[i])) for i in range(N-1)];s=[iv.mpf(0) for _ in ROWS]
 for n in reversed(range(M)):
  vals=[ii(values[i*M+n]) for i in range(N)];u=[wt[i]*vals[i]**2 for i in range(N)];fac=1+(2*n+1)**2
  for i in reversed(range(N)):s[0]+=u[i];s[2]+=fac*u[i]
  for i in reversed(range(N-1)):
   tr=dd[i]*(u[i]+u[i+1])/2;dif=(vals[i+1]-vals[i])**2;s[1]+=tr;s[2]+=dc[i]*dif;s[3]+=fac*tr+qc[i]*dif
 return s

def main():
 start=now();timer=time.monotonic();frozen=json.loads((E/'frozen_inputs.json').read_text());pins={n:v['sha256'] for n,v in frozen['files'].items()}
 for n,h in pins.items():need(sha(B/n)==h,'frozen input')
 zfile=S/'KC_assembled_image_all260.npz';tv,tq=read_numeric(zfile,'t_eval',(N,));wv,wq=read_numeric(zfile,'w_i',(N,));need(all(x>0 for x in wv) and all(b>a for a,b in zip(tv,tv[1:])),'positive exact geometry');need([fq(b-a) for a,b in zip(tv,tv[1:])]==[b-a for a,b in zip(tq,tq[1:])],'independent exact grid increments')
 Z,_=read_numeric(zfile,'img_assembled',(N,M));direct,_=read_numeric(zfile,'img_direct',(N,M));S1=[F(0) for _ in Z];S2=[fmpq(0) for _ in Z];sumabs=[F(0) for _ in Z];ranges=[];cs1=F(0);cs2=fmpq(0)
 paths=sorted(S.glob('KC_m*_*.npz'),key=lambda p:int(re.fullmatch(r'KC_m([0-9]+)_([0-9]+)\.npz',p.name)[1]));need(len(paths)==42,'all42 pieces')
 for path in paths:
  ll,lq=read_numeric(path,'m_lo',());rr,rq=read_numeric(path,'m_hi',());mm,mq=read_numeric(path,'Mout',());l=int(ll[0]);r=int(rr[0]);need(ll[0]==l and rr[0]==r and 0<=l<r<=260 and mm==[F(M)],'valid integer mode range');need(path.name==f'KC_m{l}_{r}.npz','label filenames');need(l==(ranges[-1][1] if ranges else 0),'contiguous disjoint range');ranges.append([l,r]);checks['range_checks']+=1
  t,_=read_numeric(path,'t_eval',(N,));w,_=read_numeric(path,'w_i',(N,));need(t==tv and w==wv,'every piece exact geometry');checks['geometry_checks']+=2*N
  p,q=read_numeric(path,'img',(N,M));c,cq=read_numeric(path,'c',());cs1+=c[0];cs2+=cq[0]
  for i,(a,b) in enumerate(zip(p,q,strict=True)):S1[i]+=a;S2[i]+=b;sumabs[i]+=abs(a)
 need(ranges[-1][1]==260 and fq(cs1)==cs2,'complete range and exact strain sum')
 for a,b in zip(S1,S2,strict=True):need(fq(a)==b,'every exact full sum independent');checks['summed_entries_twice']+=1
 original=S/'KprojB2_M16_s16_NJ1_img.npz'
 for name,target,shape in [('img_K',direct,(N,M)),('t_eval',tv,(N,)),('w_i',wv,(N,))]:p,_=read_numeric(original,name,shape);need(p==target,'direct image identity to explicit B2 file')
 summary=json.loads((S/'KC_merge_all.json').read_text());need(summary['modes']==ranges,'summary range list')
 vals={'D':direct,'Z':Z,'S':S1,'Z_minus_D':[a-b for a,b in zip(Z,direct)],'S_minus_D':[a-b for a,b in zip(S1,direct)],'Z_minus_S':[a-b for a,b in zip(Z,S1)]};energies={};outputs={};overlaps=0
 for name,v in vals.items():
  a=arb_forms(v,tv,wv);b=iv_forms(v,tv,wv);en={};norm={}
  for row,x,y in zip(ROWS,a,b,strict=True):en[row]={'arb':ss(ab(x)),'iv':ss(ib(y))};norm[row]=ss(envelope(ab(x.sqrt()),ib(iv.sqrt(y))));envelope(ab(x),ib(y));overlaps+=2
  energies[name]=(a,b);outputs[name]={'energy':en,'norm_enclosure':norm,'max_abs_exact':str(max(map(abs,v)))}
  print(json.dumps({'utc':now(),'stage':name,'seconds':time.monotonic()-timer}),flush=True)
 ratios={};literal_errors={};tolerance_results={};count=0
 for name in ['Z_minus_D','S_minus_D','Z_minus_S']:
  rat={}
  for j,row in enumerate(ROWS):
   a=energies[name][0][j];b=energies[name][1][j];da=energies['D'][0][j];db=energies['D'][1][j];need(ab(da)[0]>0 and ib(db)[0]>0,'nonzero reference');rat[row]=ss(envelope(ab((a/da).sqrt()),ib(iv.sqrt(b/db))));overlaps+=1
  ratios[name]=rat
 for field,key in [('functionals_LK_assembled','Z'),('functionals_LK_direct','D'),('functionals_difference','Z_minus_D')]:
  errs={}
  for row in ROWS:
   q=F.from_float(summary[field][row]);lo,hi=map(F,outputs[key]['norm_enclosure'][row]);err=max(abs(lo-q),abs(hi-q));tolerance_results[field+'/'+row]=err<F(1,10**10)*max(abs(q),F(1,10**20));errs[row]={'absolute_bound':str(err),'relative_bound':str(err/max(abs(q),F(1,10**20)))};count+=1
  literal_errors[field]=errs
 for row in ROWS:
  q=F.from_float(summary['rel_difference'][row]);lo,hi=map(F,ratios['Z_minus_D'][row]);err=max(abs(lo-q),abs(hi-q));tolerance_results['rel_difference/'+row]=err<F(1,10**10)*abs(q);literal_errors.setdefault('rel_difference',{})[row]={'absolute_bound':str(err),'relative_bound':str(err/abs(q))};count+=1
 for field,key in [('max_abs_img_diff','Z_minus_D'),('max_abs_img','D')]:
  q=F.from_float(summary[field]);v=F(outputs[key]['max_abs_exact']);err=abs(q-v);tolerance_results[field]=err<F(1,10**15)*max(abs(v),F(1,10**20));literal_errors[field]={'absolute_exact':str(err),'relative_exact':str(err/max(abs(v),F(1,10**20)))};count+=1
 norm_value_difference={}
 for j,row in enumerate(ROWS):
  aaZ=energies['Z'][0][j].sqrt();aaD=energies['D'][0][j].sqrt();iiZ=iv.sqrt(energies['Z'][1][j]);iiD=iv.sqrt(energies['D'][1][j]);norm_value_difference[row]=ss(envelope(ab(abs(aaZ-aaD)/aaD),ib(abs(iiZ-iiD)/iiD)));overlaps+=1
 max_round=max(abs(a-b) for a,b in zip(Z,S1));max_sumabs=max(sumabs);need(max_round>=0,'exact finite discrepancy');out={'start_utc':start,'utc':now(),'status':'PASS_EXACT_SAVED_ALL_MODE_IMAGE_SUM_AND_DISCRETE_NORMS_REQUIRES_REVIEW','checks':checks,'arb_bits':ctx.prec,'iv_digits':iv.dps,'ranges':ranges,'interval_overlaps':overlaps,'literal_scalar_checks':count,'exact_sum_strain':str(cs1),'saved_strain_absolute_discrepancy':str(abs(cs1-F.from_float(summary['c_K_assembled']))),'max_partial_absolute_sum':str(max_sumabs),'max_saved_Z_minus_exact_S':str(max_round),'results':outputs,'difference_norm_ratios':ratios,'relative_difference_of_norm_values':norm_value_difference,'literal_summary_absolute_errors':literal_errors,'original_diagnostic_tolerances_passed':tolerance_results,'seconds':time.monotonic()-timer,'scope':'Exact saved finite partial-image summation and four discrete row norms only. No constituent is physically reassembled, no continuous norm or projection/inverse/PDE conclusion.'}
 for p in [D/'PROOF.md',D/'REVIEW_RESOLUTION.md',D/'SAVED_SUMMARY_DISCREPANCY.md',D/'code/check_attempt1.py.txt',E/'check_attempt1.log',E/'proof_first.json',E/'frozen_inputs.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
 for n,h in pins.items():need(sha(B/n)==h,'unchanged input throughout')
 out['files']=dict(sorted(pins.items()))
 with (E/'checks.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['files','results','difference_norm_ratios','relative_difference_of_norm_values','literal_summary_absolute_errors','ranges']},indent=2))
if __name__=='__main__':main()
