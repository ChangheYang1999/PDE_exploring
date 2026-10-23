"""Own finite grids, exact center identities and diagnostics for result320."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os,sys,json,hashlib,math
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
sys.set_int_max_str_digits(1000000)
import numpy as np
from independent_hydrostatic import CartesianQJet,exact_hydrostatic_center,quadrature_hydrostatic_center
from node_export_inverse_stage import RULES,evaluate
from larger_node_stage import NodeStore,rounded_fields,pair_spreads
from larger_node_independent_arithmetic import residual as exact_residual,summaries as independent_summaries
R=Path('research/accurate_map_final_audit');V=R/'verification'
STATES=[('B','hsQ_c2.0_N128_acc.pt'),('C','hsQ_c2.0_N96_acc_fromG.pt'),('A','hsQ_c2.0_N96_acc.pt'),('E','hsQ_c2.0_N96_acc_fine.pt'),('G80','hsQ_c2.0_N80_acc6_fine.pt'),('G96','hsQ_c2.0_N96_acc6_fine.pt'),('G112','hsQ_c2.0_N112_acc6_fine.pt'),('G128','hsQ_c2.0_N128_acc6_fine.pt')]
REGIONS=[('core',0.,.1),('sub',.1,1.),('annulus',1.,100.),('far',100.,float('inf'))]
EXTENTS=[100.,10000.,10000000.]
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def put(p,d):
 p=Path(p);tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n');tmp.replace(p)
def save_array(p,d):
 p=Path(p);tmp=p.with_suffix('.tmp')
 with tmp.open('wb')as f:np.savez_compressed(f,**d)
 tmp.replace(p)
def read_array(p):
 with np.load(p,allow_pickle=False)as a:return {k:a[k]for k in a.files}
def probe_grid():
 rad=np.unique(np.r_[np.logspace(-6,7,51),.1,1.,100.,10000.,10000000.]);angles=np.r_[0.,.017,.053,.147,.31,.59,.83,1.07,1.31,1.49,1.553,1.566,np.pi/2]
 rr,tt=np.meshgrid(rad,angles,indexing='ij');x=rr*np.cos(tt);y=rr*np.sin(tt);x[:,-1]=0.;y[:,0]=0.
 i=np.arange(111);ri=10.**(-6+13*(i+.37)/111);ti=np.pi/2*np.mod((i+1)*(np.sqrt(5)-1)/2,1.)
 return np.r_[np.column_stack([x.ravel(),y.ravel()]),np.column_stack([ri*np.cos(ti),ri*np.sin(ti)])]
def common_grid(shift=False):
 if shift:rad=10.**(-3+10*(np.arange(397)+.37)/397);theta=np.pi*(np.arange(47)+.23)/(2*47)
 else:rad=np.logspace(-3,7,401);theta=np.linspace(0,np.pi/2,49)
 rr,tt=np.meshgrid(rad,theta,indexing='ij');return np.column_stack([(rr*np.cos(tt)).ravel(),(rr*np.sin(tt)).ravel()]),rr.ravel()
def angular_grid(M):
 dense=np.linspace(0,np.pi/2,8*M+1)[1:-1];coll=(np.arange(M)+.5)*np.pi/(2*M);angles=np.r_[dense,coll];xy=[];records=[]
 for radius in [3.,30.,300.,3000.]:
  start=len(xy);xy.extend(np.column_stack([radius*np.cos(angles),radius*np.sin(angles)]));records.append(dict(radius=radius,start=start,dense_count=len(dense),coll_count=M,total=len(angles)))
 return np.array(xy),dense,coll,records

def regional(xy,rows,extent=float('inf')):
 radius=np.hypot(xy[:,0],xy[:,1]);out=[]
 for name,lo,hi in REGIONS:
  ids=np.flatnonzero((radius>=lo)&(radius<hi)&(radius<=extent));row=dict(region=name,count=len(ids),metrics={})
  for key,col in [('absR',0),('Rf',3),('Rv',4)]:
   val=abs(rows[:,col]);good=ids[np.isfinite(val[ids])];ind=int(good[np.argmax(val[good])])if len(good)else None
   row['metrics'][key]=dict(index=ind,value=float(val[ind])if ind is not None else None,defined_count=len(good),undefined_count=len(ids)-len(good),x=float(xy[ind,0])if ind is not None else None,y=float(xy[ind,1])if ind is not None else None,R=float(rows[ind,0])if ind is not None else None,Nf=float(rows[ind,1])if ind is not None else None,Nv=float(rows[ind,2])if ind is not None else None)
  out.append(row)
 return out

def select(xy,jets,B):
 reasons={}
 def add(i,name):
  if i is not None:reasons.setdefault(int(i),[]).append(name)
 for extent in [float('inf')]+EXTENTS:
  for row in regional(xy,B['residual'],extent):
   for key,z in row['metrics'].items():add(z['index'],str(extent)+' '+row['region']+' '+key)
 for k in [0,1]:add(np.argmax(abs(B['velocity'][:,k])),'absV'+str(k+1))
 add(np.argmax(abs(jets[:,3])),'absgxx')
 for i in [0,len(xy)//2,len(xy)-1]:add(i,'first/middle/last')
 return dict(indices=sorted(reasons),reasons={str(i):reasons[i]for i in sorted(reasons)})

def phase(path,tag,label,ids,xy,jets,jet,p,bindings):
 def compute(i):
  z=evaluate(jet,*xy[i],p,RULES[label]);return dict(velocity=z['V'],Phi=z['Phi'],dV2dy=z['dV2_dy'],tail_velocity=z['tail_V'],metadata=z['meta'],residual=rounded_fields(*xy[i],jets[i],z['V']))
 return NodeStore(path,tag+'_'+label,ids,xy,jets,RULES[label],bindings).run(compute,lambda n,i:print(tag,label,n,'/',len(ids),now(),flush=True))

def audit_rows(xy,jets,snapshot,ids):
 count=0
 for pos,i in enumerate(ids):
  vals=exact_residual(F(float(xy[i,0])),F(float(xy[i,1])),[F(float(t))for t in jets[i]],[F(float(t))for t in snapshot['velocity'][pos]])
  for k,(a,b)in enumerate(zip(vals,snapshot['residual'][pos])):
   if a is None:
    if not np.isnan(b):raise ArithmeticError(('expected undefined',i,k,b))
   elif not np.isfinite(b)or float(a)!=b:raise ArithmeticError(('independent row',i,k,a,b))
   if k in [1,2]and a is not None and a>0 and b<=0:raise ArithmeticError('denominator underflow')
   count+=1
 return count

def exact_center(q):
 coeff=q.exact_coefficients();a=sum(((-1)**j*v for j,v in enumerate(coeff[0])),F(0));d=sum(((-1)**(j+1)*j*j*v for j,v in enumerate(coeff[0])),F(0));u=sum(((-1)**j*v for j,v in enumerate(coeff[1])),F(0))if len(coeff)>1 else F(0)
 b=16*(2*d-a+u);e=16*(2*d-a-u);c=exact_hydrostatic_center(coeff,2);D=1+c
 if a==0:raise ArithmeticError('nondegenerate auxiliary trial required')
 K=sum(((-1)**k*sum(row,F(0))for k,row in enumerate(coeff)),F(0))/2
 exact=dict(a=a,b=b,e=e,E=e/a,K=K,cH=c,delta=D,B_minus_6E=b-6*e/a,cubic_residual=e*(2+3*D)-a*b/3,axis_limit=abs(D)/(abs(1+D)+1))
 out=dict(exact={k:str(x)for k,x in exact.items()},rounded={k:float(x)for k,x in exact.items()},center_formula_gauss={str(n):quadrature_hydrostatic_center(q,n)for n in [q.N+q.M+8,2*(q.N+q.M+8)]},source_sha256=sha(q.path),scope='Exact rational identities for this dyadic finite trial; Gaussian values are descriptive.')
 q._exact.clear();return out

def local_mp(q,xy,jets,indices):
 import mpmath as mp
 from scalar_mp_hydrostatic_density import ScalarMPDensity
 out=[]
 for i in indices:
  vals={}
  for dg in [72,108]:
   with mp.workdps(dg):
    f=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);vals[str(dg)]=[mp.nstr(x,dg,strip_zeros=False)for x in f.jet(*xy[i])]
  low=list(map(F,vals['72']));high=list(map(F,vals['108']));double=list(map(lambda x:F(float(x)),jets[i]));sens=[]
  for a,b,c in zip(low,high,double):
   scale=max(abs(a),abs(b));delta=abs(a-b);den=max(abs(c),abs(b));sens.append(dict(precision_abs=float(delta),precision_scaled=float(delta/max(scale,F(1,10**80))),precision_pass=bool(delta<=max(scale,F(1,10**80))*F(1,10**48)),double_abs=float(abs(c-b)),double_pure_relative=float(abs(c-b)/den)if den else None,both_zero=not bool(den)))
  out.append(dict(index=int(i),x=float(xy[i,0]),y=float(xy[i,1]),decimal=vals,double=list(map(float,jets[i])),diagnostics=sens))
 return out

def angular_summary(dense,coll,records,rows,M):
 out=[]
 for block in records:
  start=block['start'];n=block['dense_count'];a=rows[start:start+n];b=rows[start+n:start+block['total']];q=a[:,0]/a[:,1];qc=b[:,0]/b[:,1]
  if not np.isfinite(q).all()or not np.isfinite(qc).all():raise ArithmeticError('undefined angular normalization')
  modes=np.arange(3*M);mat=np.cos(2*dense[:,None]*modes);fit,_,rank,sing=np.linalg.lstsq(mat,q,rcond=None);k=int(np.argmax(abs(fit[1:]))+1)
  out.append(dict(radius=block['radius'],dense_max=float(max(abs(q))),dense_argmax=start+int(np.argmax(abs(q))),collocation_direct_max=float(max(abs(qc))),collocation_argmax=start+n+int(np.argmax(abs(qc))),collocation_interpolated_max=float(max(abs(np.interp(coll,dense,q)))),sign_changes=int(np.count_nonzero(q[1:]*q[:-1]<0)),dominant_k=k,dominant_coefficient=float(fit[k]),least_squares_rank=int(rank),condition_number=float(sing[0]/sing[-1]),fit_coefficients=list(map(float,fit)),quantity='signed R/Nf; direct collocation values and interpolated values kept separate'))
 return out

def function_difference(a,b,r):
 dg=abs(a[:,0]-b[:,0]);dgrad=np.hypot(a[:,1]-b[:,1],a[:,2]-b[:,2]);den=np.maximum(abs(a[:,0]),abs(b[:,0]));pure=np.divide(dg,den,out=np.zeros_like(dg),where=den!=0)
 quantities=dict(weighted_density=dg/np.sqrt(1+r),weighted_gradient=dgrad*np.sqrt(1+r),legacy_new_denominator_relative=dg/(abs(b[:,0])+1e-300),pure_relative=pure)
 out=[]
 for name,lo,hi in [('core',0,.1),('sub',.1,1),('annulus',1,100),('far_low',100,1e4),('far_high',1e4,1e7)]:
  ids=np.flatnonzero((r>=lo)&(r<hi));metrics={}
  for k,z in quantities.items():
   ind=int(ids[np.argmax(z[ids])])if len(ids)else None;metrics[k]=dict(index=ind,value=float(z[ind])if ind is not None else None)
  out.append(dict(region=name,count=len(ids),both_zero_count=int(np.count_nonzero(den[ids]==0)),metrics=metrics))
 return out
