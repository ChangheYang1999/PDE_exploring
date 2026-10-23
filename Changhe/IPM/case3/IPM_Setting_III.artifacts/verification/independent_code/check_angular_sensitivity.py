import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,math
import numpy as np
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_evaluator_sensitivity';V=R/'verification';D=V/'candidate';checks=[];bindings={};scalar=0
EPS=[0.,1e-4,1e-5,1e-6]
def test(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p,h=None):
 p=Path(p).resolve();a=p.read_bytes();test('stable '+p.name,p.read_bytes()==a);got=hashlib.sha256(a).hexdigest()
 if h is not None:test('sha '+p.name,h==got)
 if str(p)in bindings:test('duplicate '+p.name,bindings[str(p)]==got)
 bindings[str(p)]=got;return a
def load(p):return json.loads(bind(p))
def Q(x):
 x=float(x)
 if not math.isfinite(x):raise ValueError('nonfinite operand')
 return F(x)
def algebra(j,v,x,y):
 g,gx,gy=map(Q,j[:3]);v1,v2=map(Q,v);x,y=map(Q,[x,y]);a=(2*x+v1)*gx;b=(2*y+v2)*gy;rr=a+b-g;nf=abs(a)+abs(b)+abs(g);nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy)
 if abs(rr)>nf or abs(rr)>2*nv:raise ArithmeticError('triangle bounds')
 return [rr,nf,nv,abs(rr)/nf if nf else None,abs(rr)/nv if nv else None]
def display(row):return [float(z)if z is not None else np.nan for z in row]
def signed(row):return row[0]/row[1]if row[1]else None
def count(q):return sum(a*b<0 for a,b in zip(q[:-1],q[1:]))
def fit(q,theta):
 a=np.asarray([float(z)for z in q]);C=np.cos(2*np.arange(96)[None,:]*theta[:,None]);coeff,res,rank,s=np.linalg.lstsq(C,a,rcond=None);k=int(np.argmax(abs(coeff[1:]))+1)
 return dict(strict_sign_changes=int(count(q)),zero_count=sum(z==0 for z in q),dominant_nonconstant_k=k,dominant_coefficient=float(coeff[k]),constant_coefficient=float(coeff[0]),largest_nonconstant_amplitude=float(abs(coeff[k])),max_abs_signed_ratio=float(max(map(abs,q))),argmax_abs_signed_ratio=int(max(range(len(q)),key=lambda i:abs(q[i]))),fit_max_abs_error=float(max(abs(C@coeff-a))),rank=int(rank),singular_condition=float(s[0]/s[-1]))
def maxrec(a):
 i=max(range(len(a)),key=lambda i:abs(a[i]));return dict(index=i,value=float(a[i]),absolute=float(abs(a[i])))
def close(row,stored,tol=256*np.finfo(float).eps):
 for k,(a,b)in enumerate(zip(row,stored)):
  if a is None:
   if not np.isnan(b):return False
  elif not math.isfinite(float(b)):return False
  else:
   scale=row[1] if k==0 else (abs(a)if k in [1,2]else F(1))
   if abs(Q(b)-a)>Q(tol)*max(scale,F(1,10**300)):return False
 return True
# Synthetic algebra and negative checks, before reading candidate fields.
manufactures=[]
def mt(n,b):test('manufacture '+n,b);manufactures.append(n)
mt('zero ratios undefined',algebra([0,0,0],[0,0],0,0)==[F(0),F(0),F(0),None,None])
mt('Rv reaches2',algebra([0,1,0],[0,0],1,0)[4]==2)
mt('zero skipping refused',count([F(1),F(0),F(-1),F(1)])==1)
for i,(j,v,x,y)in enumerate([([1,2,3],[4,5],6,7),([-1,0,3],[0,-4],2,-3),([0,1,1],[-2,-2],1,1),([1e-10,-1e4,1e-8],[1e2,-1e2],1e-6,1e4)]):
 a=algebra(j,v,x,y);mt('roundtrip'+str(i),close(a,display(a)))
 bad=display(a);bad[0]+=float(a[1])+1;mt('R corruption'+str(i),not close(a,bad))
 bad=display(a);bad[1]*=2;mt('Nf corruption'+str(i),not close(a,bad)if a[1]else True)
 v2=[v[0],v[1]+.125];b=algebra(j,v2,x,y);mt('fixed jet identity'+str(i),b[0]-a[0]==(Q(v2[1])-Q(v[1]))*Q(j[2]))
for bad in [float('nan'),float('inf')]:
 try:Q(bad);refused=False
 except ValueError:refused=True
 mt('nonfinite refused '+str(bad),refused)
manufacture_count=len(manufactures)
job=load(V/'JOB_EXIT.json');test('worker exit0',job['returncode']==0)
complete=load(D/'COMPLETE.json');test('worker completed',complete['status']=='COMPLETE_FINITE_CANDIDATE_DIAGNOSTIC_REQUIRES_CHECK')
for group in ['bindings','outputs']:
 for p,h in complete[group].items():bind(p,h)
inputs=load(V/'INPUTS.json')
for row in inputs['files']:bind(row.get('snapshot',row.get('reused_path')),row['sha256'])
prior=load(ROOT/'research/accurate_map_final_audit/verification/FINAL_BINDINGS.json');test('all prior320 bindings current',all(sha(p)==h for p,h in prior['bindings'].items()))
old=np.load(ROOT/'research/accurate_map_final_audit/verification/candidate/B_angular_B.npz',allow_pickle=False)
results=[];outputfiles={}
for rad,offset in [(3,0),(30,287)]:
 z=np.load(D/f'R{rad}_B.npz',allow_pickle=False);theta=z['theta'];x,y=z['x'],z['y'];j=z['jet'];vel=z['velocity'];tail=z['tail'];stored=z['residual'];n=len(x)
 test('epsilon order '+str(rad),z['eps'].tolist()==EPS);test('255 exact common coordinates '+str(rad),n==255 and np.array_equal(x,rad*np.cos(theta))and np.array_equal(y,rad*np.sin(theta))and np.array_equal(theta,np.linspace(0,np.pi/2,257)[1:-1]))
 test('all finite arrays '+str(rad),all(np.all(np.isfinite(z[k]))for k in z.files))
 test('V1 identical across epsilon '+str(rad),np.array_equal(vel[:,:,0],np.repeat(vel[:,0:1,0],4,axis=1)))
 test('no quadrature node endpoint '+str(rad),np.all(z['meta'][:,7:]==0))
 rows=[];rounderr=[]
 for i in range(n):
  a=[algebra(j[i],vel[i,k],x[i],y[i])for k in range(4)];rows.append(a)
  if not all(close(t,stored[i,k])for k,t in enumerate(a)):raise ArithmeticError('worker residual arithmetic '+str((rad,i)))
  scalar+=20
  for k in range(4):
   if k and a[k][0]-a[0][0]!=(Q(vel[i,k,1])-Q(vel[i,0,1]))*Q(j[i,2]):raise ArithmeticError('exact fixed-jet identity')
   rounderr.append(abs(Q(stored[i,k,0])-a[k][0])/a[k][1])
 test('all exact arithmetic rows '+str(rad),True)
 ar=np.array([[display(t)for t in a]for a in rows]);signedrows=[[signed(rows[i][k])for i in range(n)]for k in range(4)]
 test('all ratios defined '+str(rad),all(z is not None for a in signedrows for z in a))
 statistics=[dict(eps=EPS[k],**fit(signedrows[k],theta))for k in range(4)]
 fixed=[];div=[]
 for k in range(4):
  fixed.append([(rows[i][k][0]-rows[i][0][0])/rows[i][0][1]for i in range(n)])
  div.append([Q(tail[i,k])-Q(tail[i,0])for i in range(n)])
 selected=load(D/f'R{rad}_SELECTION.json');ids=selected['indices'];required={0,127,254}
 for k in range(4):
  required.add(max(range(n),key=lambda i:rows[i][k][3]))
  if k:
   required.add(max(range(n),key=lambda i:abs(fixed[k][i])));required.add(max(range(n),key=lambda i:abs(div[k][i])))
   required.update([i for i in range(n)if rows[i][k][0]*rows[i][0][0]<0][:3])
 test('selection covers exact predicates '+str(rad),set(ids)==required)
 comparisons=[]
 for lab in ['A','C']:
  zz=np.load(D/f'R{rad}_{lab}.npz',allow_pickle=False);test('selection identities '+str(rad)+lab,zz['indices'].tolist()==ids)
  labrows=[]
  for pos,i in enumerate(ids):
   rr=[algebra(j[i],zz['velocity'][pos,k],x[i],y[i])for k in range(4)]
   test('selected residual arithmetic '+str((rad,lab,i)),all(close(a,zz['residual'][pos,k])for k,a in enumerate(rr)));scalar+=20
   labrows.append(rr)
  comparisons.append((lab,zz,labrows))
 spreads=[]
 for pos,i in enumerate(ids):
  for k in range(4):
   rr=[comparisons[0][2][pos][k][0],rows[i][k][0],comparisons[1][2][pos][k][0]];s=max(rr)-min(rr);base=abs(rows[i][k][0])
   spreads.append(dict(index=i,eps=EPS[k],spread_over_Nf_B=float(s/rows[i][k][1]),spread_over_abs_R_B=float(s/base)if base else None,all_three_same_strict_sign=all(a>0 for a in rr)or all(a<0 for a in rr)))
 prod=np.load(V/f'hsQ_c2.0_N128_acc_scan_r{rad}.npz',allow_pickle=False)
 test('producer same grid '+str(rad),np.array_equal(prod['theta'],theta)and np.array_equal(prod['x'],x)and np.array_equal(prod['y'],y))
 pq=[];dr=[];dj=[];dv=[];pj=np.stack([prod['g'],prod['g_xi'],prod['g_y']],axis=-1);pv=np.stack([prod['V1'],prod['V2']],axis=-1);parith=[]
 for i in range(n):
  a=rows[i][0];b=algebra(pj[i],pv[i],x[i],y[i]);pq.append(signed(b));parith.append(display(b))
  # Producer Nv was not exported. Check its R,Nf and q separately against exact operands.
  if abs(Q(prod['R_h'][i])-b[0])>F(1,10**12)*b[1]or abs(Q(prod['N_f'][i])-b[1])>F(1,10**12)*b[1]or abs(Q(prod['q'][i])-signed(b))>F(1,10**12):raise ArithmeticError('producer arithmetic')
  scalar+=3
  jetterm=(2*Q(x[i])+Q(vel[i,0,0]))*(Q(pj[i,1])-Q(j[i,1]))+(2*Q(y[i])+Q(vel[i,0,1]))*(Q(pj[i,2])-Q(j[i,2]))-(Q(pj[i,0])-Q(j[i,0]))
  velterm=(Q(pv[i,0])-Q(vel[i,0,0]))*Q(pj[i,1])+(Q(pv[i,1])-Q(vel[i,0,1]))*Q(pj[i,2])
  if b[0]-a[0]!=jetterm+velterm:raise ArithmeticError('two-jet exact identity')
  dr.append((b[0]-a[0])/a[1]);dj.append(jetterm/a[1]);dv.append(velterm/a[1])
 test('producer finite arithmetic and decomposition '+str(rad),True)
 oo=slice(offset,offset+n);test('prior320 same coordinates/jets '+str(rad),np.array_equal(old['xy'][oo],np.stack([x,y],axis=-1))and np.array_equal(old['jets'][oo],j))
 olddelta=[]
 for i in range(n):olddelta.append((algebra(j[i],old['velocity'][offset+i],x[i],y[i])[0]-rows[i][0][0])/rows[i][0][1])
 test('fsum baseline within5e-12 normalized of320 '+str(rad),max(map(abs,olddelta))<=F(5,10**12))
 comparisons_to_producer=[]
 for k in range(4):
  diff=[pq[i]-signedrows[k][i]for i in range(n)]
  comparisons_to_producer.append(dict(eps=EPS[k],max_abs_signed_q_difference=maxrec(diff),pointwise_opposite_sign_count=sum(pq[i]*signedrows[k][i]<0 for i in range(n))))
 result=dict(radius=rad,points=n,statistics=statistics,selected_indices=ids,selected_quadrature_spreads=spreads,normalized_rounding_max=float(max(rounderr)),fixed_Nf0_residual_changes=[dict(eps=EPS[k],**maxrec(fixed[k]))for k in range(4)],finite_divergence_proxies=[dict(eps=EPS[k],**maxrec(div[k]))for k in range(4)],producer_statistics=fit(pq,theta),producer_minus_own_baseline=dict(total=maxrec(dr),jet_part=maxrec(dj),velocity_part=maxrec(dv)),producer_comparisons=comparisons_to_producer,baseline_minus320_normalized_max=float(max(map(abs,olddelta))))
 results.append(result)
 p=V/f'CHECKED_R{rad}.npz';np.savez_compressed(p,exact_residual_rounded=ar,producer_exact_residual_rounded=parith,fixed_Nf0_change=np.asarray([[float(z)for z in a]for a in fixed]).T,finite_divergence_proxy=np.asarray([[float(z)for z in a]for a in div]).T,producer_decomposition=np.asarray([[float(a),float(b),float(c)]for a,b,c in zip(dr,dj,dv)]));outputfiles[str(p.resolve())]=sha(p)
bind(__file__);bind(R/'ARITHMETIC_PROOF.md');bind(V/'JOB.json');bind(V/'INITIAL_JOB_EXIT.json')
for p,h in list(bindings.items()):test('end stable '+Path(p).name,sha(p)==h)
out=dict(status='PASS_FINITE_ANGULAR_SENSITIVITY_CHECKS_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),manufacture_count=manufacture_count,scalar_comparisons=scalar,checks=checks,bindings=bindings,outputs=outputfiles,results=results,scope='Exact algebra on finite operands, empirical quadrature/evaluator comparisons. Auxiliary only; no enclosure or historical causal attribution; primary UNRESOLVED.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','manufacture_count','scalar_comparisons']},indent=2))
for a in results:print('RADIUS',a['radius'],'COUNTS',[(b['eps'],b['strict_sign_changes'],b['dominant_nonconstant_k'],b['max_abs_signed_ratio'])for b in a['statistics']],'PRODUCER',a['producer_statistics']['strict_sign_changes'],'DECOMP',a['producer_minus_own_baseline'])
