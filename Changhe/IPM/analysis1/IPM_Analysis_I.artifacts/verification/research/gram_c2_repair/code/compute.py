from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,io,json,pickle,sys
import numpy as np
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/gram_c2_repair'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
def enc(q):return str(q.numerator)+'/'+str(q.denominator)
def horner(c,t):
 z=F(0)
 for a in reversed(c):z=z*t+a
 return z
def derivative(c):return [j*c[j] for j in range(1,len(c))] or [F(0)]
def jet(c,t):
 out=[]
 for _ in range(3):out.append(horner(c,t));c=derivative(c)
 return out
def solve(A,b):
 A=[list(row)+[val] for row,val in zip(A,b)]
 for j in range(len(b)):
  k=next(k for k in range(j,len(b)) if A[k][j]);A[j],A[k]=A[k],A[j];v=A[j][j];A[j]=[q/v for q in A[j]]
  for k in range(len(b)):
   if k==j:continue
   v=A[k][j];A[k]=[u-v*t for u,t in zip(A[k],A[j])]
 return [row[-1] for row in A]
def square(c):return [sum((c[j]*c[n-j] for j in range(len(c)) if 0<=n-j<len(c)),F(0)) for n in range(2*len(c)-1)]
def integral(c,w):return sum((v*w**(j+1)/F(j+1) for j,v in enumerate(c)),F(0))
def A(q):q=F(q);return arb(q.numerator)/q.denominator
def qarf(q):m,e=q.man_exp();return F(int(m))*F(2)**int(e)
def box(z):check(z.is_finite(),'finite ball');return [qarf(z.lower()),qarf(z.upper())]
def ceiling(q,places=18):return F(q.numerator*10**places//q.denominator+1,10**places)
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  allow={('numpy._core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy.core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,('numpy._core.multiarray','scalar'):np._core.multiarray.scalar,('numpy.core.multiarray','scalar'):np._core.multiarray.scalar}
  check((m,n) in allow,'pickle global');return allow[m,n]
prior=B/'research/gram_conforming_repair/evidence/verdict.json';pins={}
for n,h in json.loads(prior.read_text())['files'].items():check(sha(B/n)==h,'prior pin '+n);pins[n]=h
oldpath=B/'research/gram_conforming_repair/evidence/compute.json';old=json.loads(oldpath.read_text());L=F(old['L_exact']);k=F(old['k_exact']);check(L>0 and k<F(3,2),'weight parameters')
def weight(t):z=(2*A(t)).exp();return z*(1+z/A(L)**2)**A(F(3,2)-k)
records=[];total={'columns':0,'pieces':0,'value_traces':0,'first_derivative_traces':0,'second_derivative_traces':0,'rational_interpolation_equations':0}
for rec in old['records']:
 meta=Reader(io.BytesIO((B/rec['source']).read_bytes())).load();new=[];cache={};maxratio=F(0);which=None;starts=[]
 for col in rec['columns']:
  mode,pcs,label=meta['cols'][col['column_index']];check(mode==0 and label==col['label'],'source column');p=[]
  for aa,bb,alpha,coeff in pcs:
   aa,bb=F(float(aa)),F(float(bb));cc=[F(float(q)) for q in coeff];check(alpha==0 and bb>aa,'polynomial interval');p.append((aa,bb,cc,jet(cc,F(0)),jet(cc,bb-aa)))
  check(all(p[j-1][1]==p[j][0] for j in range(1,len(p))),'partition');check(len(p[0][2])-1>=6 and p[0][2][-1]!=0,'unchanged leading first-piece coefficient');starts.append(p[0][0]);targets=[[F(0)]*3]+[[(x+y)/2 for x,y in zip(p[j-1][4],p[j][3])] for j in range(1,len(p))]+[[F(0)]*3]
  U=arb(0);V=arb(0);outpcs=[]
  for j,(aa,bb,cc,jl,jr) in enumerate(p):
   w=bb-aa;el=[x-y for x,y in zip(targets[j],jl)];er=[x-y for x,y in zip(targets[j+1],jr)];left=[el[0],el[1],el[2]/2];right=jet(left,w);rhs=[x-y for x,y in zip(er,right)]
   mat=[[w**3,w**4,w**5],[3*w**2,4*w**3,5*w**4],[6*w,12*w**2,20*w**3]];d=left+solve(mat,rhs)
   check(jet(d,F(0))==el and jet(d,w)==er,'six exact Hermite equations');total['rational_interpolation_equations']+=6
   repaired=cc.copy()
   for q,z in enumerate(d):repaired[q]+=z
   check(jet(repaired,F(0))==targets[j] and jet(repaired,w)==targets[j+1],'exact repaired three jets')
   dd=derivative(d)+[F(0)];comb=[3*x+y for x,y in zip(d,dd)];ei=integral(square(d),w)+integral(square(comb),w);vi=integral(square(cc),w);check(ei>=0 and vi>0,'exact integral positivity')
   for t in (aa,bb):
    if t not in cache:cache[t]=weight(t)
   U+=cache[bb]*A(ei);V+=cache[aa]*A(vi)
   outpcs.append({'a_exact':enc(aa),'b_exact':enc(bb),'target_left_jet':list(map(enc,targets[j])),'target_right_jet':list(map(enc,targets[j+1])),'correction_coefficients':list(map(enc,d)),'exact_error_integral':enc(ei),'exact_original_square_integral':enc(vi)})
   total['pieces']+=1
   for name in ('value_traces','first_derivative_traces','second_derivative_traces'):total[name]+=2
  check(V>0 and U>0,'positive quotient');rb=box((U/V).sqrt())
  if rb[1]>maxratio:maxratio=rb[1];which=col['column_index']
  total['columns']+=1;new.append({'column_index':col['column_index'],'label':label,'first_piece_degree':len(p[0][2])-1,'pieces':outpcs,'U_arb512':list(map(enc,box(U))),'V_arb512':list(map(enc,box(V))),'sqrt_ratio_arb512':list(map(enc,rb))})
 check(starts==sorted(starts) and len(starts)==len(set(starts)),'independent support starts');delta2=ceiling(maxratio);delta0=F(rec['public']['uniform_single_column_relative_broken_energy_upper']);check(0<delta0<1,'C0 bound');xdist=ceiling((delta0+delta2)/(1-delta0))
 records.append({'source':rec['source'],'M':rec['M'],'N':len(new),'independent_repaired_functions':rec['M']*len(new),'columns':new,'public':{'single_column_relative_broken_norm_error_upper':enc(delta2),'single_column_relative_X_distance_from_C0_upper':enc(xdist)},'largest_ratio_column':which,'max_ratio_float_orientation_only':float(maxratio),'endpoint_weight_count':len(cache)})
for p in (prior,oldpath,D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__)):pins[str(p.relative_to(B))]=sha(p)
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof first')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_C2_HERMITE_LINEAR_SYSTEM_AND_ARB512_BROKEN_NORM_BOUNDS','L_exact':enc(L),'k_exact':enc(k),'totals':total,'records':records,'files':dict(sorted(pins.items())),'scope':'New C2,1 compact perturbations with zero central factor and local H1 images under explicit background assumptions. Only single-column norm comparisons; no matrix transfer, inverse or endpoint.'};p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'totals':total,'records':[{k:r[k] for k in ('M','N','public','largest_ratio_column','max_ratio_float_orientation_only')} for r in records]}))
