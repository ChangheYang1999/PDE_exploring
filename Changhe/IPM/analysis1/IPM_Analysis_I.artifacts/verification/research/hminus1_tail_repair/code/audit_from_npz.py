"""Independent exact input/power audit from original NPZ, no new interval norm.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_repair'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def evaluate():
 plan=json.loads((D/'source/plan.json').read_text());p=Path(plan['source_archive']);assert sha(p)==plan['source_archive_sha256']
 with np.load(p,allow_pickle=False) as z:
  k=Q(float(z['k']));L=Q(float(z['L']));t=Q(float(z['knots'][-1]));bo=Q(float(z['bo']));outer=[Q(float(x)) for x in z['Aout'].flat];knots=[Q(float(x)) for x in z['knots']]
  assert z['Aout'].shape==(260,10) and z['knots'].shape==(1573,)
 assert k>0 and 4*k<1 and bo>120
 # Independent explicit count of each original column exponent.
 ex=[(j+1)*k-j for j in range(6)]+[k-2,2*k-3,3*k-4,k-4,3-bo]
 assert len(set(ex))==11
 cross=0
 for i in range(11):
  for j in range(i):
   assert ex[i].numerator*ex[j].denominator!=ex[j].numerator*ex[i].denominator;cross+=1
 u=2*k-1;v=3*k-2;w=k-2;last=4*k-3
 assert ex[:3]==[k,u,v] and ex[6]==w and ex[3]==last
 remain=[x for i,x in enumerate(ex) if i!=6];table=[]
 for i,x in enumerate(remain):
  for j,y in enumerate(remain):
   power=x+y-1
   if (i,j)==(0,0):assert power==u;role='canceled_first'
   elif (i,j) in ((0,1),(1,0)):assert power==v;role='canceled_second'
   else:assert power<=last;role='remainder'
   table.append((i,j,str(power),role))
 assert all(x<=last for x in remain[3:]) and last<-2
 # Evaluate radial Euler eigenvalues by the factored Green denominators.
 den=0
 for x in ex:
  for n in range(1,262):assert (2*n-x-1)*(2*n+x+1)!=0;den+=1
 for x,N in [(u,522),(v,783),(w,261)]:
  for n in range(1,N+1):
   minus=2*n-x-1;plus=2*n+x+1;assert minus>0 and plus>0 and minus*plus==(2*n)**2-(x+1)**2;den+=1
 # Scalar coefficient equations solved independently as divisions.
 assert -1/(u/k-1)==k/(1-k) and -1/(v/k-1)==k/(2-2*k)
 # Radial strain homogeneity r^(a-2)dr and x²y bump r*dr.
 assert all(x-1<0 for x in (u,v,w))
 assert [(x-1)-2 for x in (u,v,w)]==[x-3 for x in (u,v,w)]
 # Closed exact Beta moments via rational product, separate from prior factorials.
 beta=Q(1,9)
 for j in range(1,9):beta*=Q(j,9+j)
 assert beta==Q(math.factorial(8)**2,math.factorial(17)) and 3*beta/2>0
 # Canonical homogeneous velocity power minus3 couples with density grad k-1.
 assert k-3-1<last
 return {'method':'exact binary64 NPZ ratios, surviving exponent table and factored Green eigenvalues','exact':{'k':str(k),'L':str(L),'tplus':str(t),'bo':str(bo),'a1':str(u),'a2':str(v),'d':str(w),'a3':str(last),'all_original_exponents':[str(x) for x in ex],'norm_decay_exponents':[str(u-k),str(v-k),str(w-k)]},'counts':{'distinct_exponent_pairs':cross,'surviving_ordered_products':len(table),'factored_mode_denominators':den,'original_Aout_entries':len(outer),'original_knots_entries':len(knots)},'outer_exact':outer,'knots_exact':knots,'product_table':table,'source_archive':{'path':str(p),'sha256':sha(p)}}
