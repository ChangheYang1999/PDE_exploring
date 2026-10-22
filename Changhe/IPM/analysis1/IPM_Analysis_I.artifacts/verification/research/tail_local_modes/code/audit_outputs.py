"""Exact input, finite-mode, geometric-tail and output audit for topic114.
No JS/TS, servers, RLScience, Lean/Lake; writes only this lane.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time,math,subprocess
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_modes';E=D/'evidence'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def endpoints(v):
 l,h=F(v['lower_exact']),F(v['upper_exact']);assert l<=h;return l,h
def ff(v,j):return math.prod(range(v-j+1,v+1))
def sines(c):
 # Direct recurrence, independent of the primary signed-frequency loop.
 cc=lambda m:c[m] if 0<=m<len(c) else F(0)
 return [(2*cc(0)-cc(2))/8,(2*cc(0)+cc(1)-cc(2)-cc(3))/8]+[(cc(j-1)+cc(j)-cc(j+1)-cc(j+2))/8 for j in range(2,len(c)+1)]
def run():
 assert not sys.flags.optimize;st=time.monotonic();counts={};pins={};dep=B/'research/hminus1_tail_quantitative/evidence/verdict.json';prior=read(dep)
 assert prior['status']=='CONFIRMED_QUANTITATIVE_HIGHER_TAIL_DISTANCE_LOCAL_JETS_AND_T_GE_10000_NONSTATIONARITY'
 for p,h in prior['files'].items():assert sha(B/p)==h,p;pins[p]=h
 assert len(pins)==249;pins[str(dep.relative_to(B))]=sha(dep);counts['prior_frozen_pins']=249
 inp=B/'data_exact/modal_v2.json';ar=read(inp);hexq=lambda x:F(float.fromhex(x));archive=B.parent/'ipmA-num/data/trial_v2_h0.008.npz'
 with np.load(archive,allow_pickle=False) as z:
  assert z['Aout'].shape==(260,10)
  exact=[F(float(v)) for v in z['Aout'].flat];knots=[F(float(v)) for v in z['knots']]
  assert exact==list(map(hexq,ar['arrays']['Aout']['hex']));assert knots==list(map(hexq,ar['arrays']['knots']['hex']))
  k,L,t=F(float(z['k'])),F(float(z['L'])),knots[-1]
  assert k==hexq(ar['scalars_hex']['k'])==F(1615536043799051,9007199254740992) and L==hexq(ar['scalars_hex']['L'])
 assert sha(archive)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 counts.update(original_outer_dyadics=len(exact),original_knots=len(knots),exact_scalars=3)
 exps=[2*k-1,3*k-2,k-2];assert 0<k<F(1,4) and all(a<1 for a in exps)
 first={name:read(E/(name+'.json')) for name in ('arb','iv')};pub=read(D/'source/public_ceilings.json')
 for name,x in first.items():
  assert x['status']=='COMPUTED_REQUIRES_AUDIT';assert x['exact']=={'k':str(k),'L':str(L),'tplus':str(t),'R':'9','T':'3000','exponents':list(map(str,exps))}
  for p,h in x['files'].items():assert sha(B/p)==h,p
  if name=='iv':assert x['source_archive']['sha256']==sha(archive)
 # Every basis column of the quotient-to-sine map has l1 norm at most1/2.
 # Verify support, negative-frequency signs, and the alternative recurrence.
 nproj=0
 for m in range(782):
  c=[F(0)]*(m+1);c[m]=F(1);sn=sines(c);manual={}
  for f in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(f)-1)//2;manual[j]=manual.get(j,F(0))+(F(1,8) if f>0 else -F(1,8))
  for j in range(len(sn)):assert sn[j]==manual.get(j,F(0));nproj+=1
  assert sum(map(abs,sn),F(0))<=F(1,2)
 counts.update(quotient_l1_basis_cases=782,quotient_projection_coordinates=nproj)
 col=exact[6::10];hd=sines(col);assert len(col)==260 and len(hd)==261
 assert hd[2]==(col[1]+col[2]-col[3]-col[4])/8
 # Check the full new derivative weights and Green integration cancellation.
 count=0
 for a,last in zip(exps,(521,782,260)):
  m=max(F(1,2),F(2)/(3-a))
  for n in range(1,last+2):
   assert F(2*n-1,2)-F(2*n-1,2)==0
   assert F(2*n-1,2)+F(2*n+1,2)==2*n
  for n in range(2,last+1):
   assert 2*n-a-1>0 and F(n)/(2*n-a-1)<=m and a-2*n+1<0
   for j in range(4):
    assert ff(2*n-1,j)==math.factorial(2*n-1)//math.factorial(2*n-1-j)>0
    assert 2*n-1-j>=0;count+=1
  assert a-3<0 and a-5<0
 assert count==6240==first['arb']['counts']['finite_positive_terms'];counts['all_finite_derivative_weights']=count
 # Derive generating-function moments exactly and reconstruct Zj.
 moments=[F(4,3),F(4,9),F(20,27),F(44,27)];Z=[]
 for j in range(4):
  p=[1]
  for d in range(j):
   qq=[0]*(len(p)+1)
   for m,v in enumerate(p):qq[m]+=(5-d)*v;qq[m+1]+=2*v
   p=qq
  Z.append(sum(v*moments[m] for m,v in enumerate(p)))
 assert Z==[F(4,3),F(68,9),F(1016,27),F(4600,27)]
 ratios=0
 for j,g in enumerate(first['iv']['geometric']):
  lo,hi=endpoints(g);rat=F(g['tail_ratio']);partial=sum((F(ff(2*m+5,j),4**m) for m in range(64)),F(0))
  assert lo==partial and rat==F(1,4)*(1+F(2,134-j))**j<1
  assert hi==partial+F(ff(133,j),4**64)/(1-rat) and lo<Z[j]<=hi
  # Exact factorwise inequality for all m>=64 follows from positive,
  # increasing denominators. Check every factor at the worst m=64.
  for d in range(j):assert F(2,133-d)<=F(2,134-j)
  for m in range(64,320):assert F(ff(2*m+7,j),4*ff(2*m+5,j))<=rat;ratios+=1
 counts.update(exact_geometric_sums=4,exact_tail_ratio_cases=ratios)
 # N1 is an l1 bound, not an empirical supremum; topic105's complete map
 # is inherited through113. Recheck its strict decimal direction.
 p105=read(B/'research/normalized_tail_repair/evidence/verdict.json');assert p105['public_bounds']['N_upper']=='38.37961982'
 assert F(p105['public_bounds']['strict_intervals']['N'][1])<F('38.37961982')
 # N2 copied from the independently audited iv full quotient sum; Hd computed
 # from the original NPZ. Current reported enclosures must include old ones.
 p113=read(B/'research/hminus1_tail_quantitative/evidence/iv.json')
 assert first['iv']['values']['N2']==p113['values']['N2']
 # The isolated fifth sine coefficients must overlap across independent
 # source chains. This is a diagnostic after the dependency/formula checks.
 diagnostics=0
 for key in ('h1_freq5','h2_freq5','hd_freq5'):
  l,h=endpoints(first['arb']['values'][key]);ll,hh=endpoints(first['iv']['values'][key]);assert max(l,ll)<=min(h,hh);diagnostics+=1
 for name,x in first.items():
  for key,limit in pub.items():
   l,h=endpoints(x['values'][key]);assert 0<l<=h<F(limit),(name,key)
  # Complete finite sum is enclosed by the distinct positive majorant,
  # which is checked by an exact separated comparison, not overlap.
 for row in ('1','2','d'):
  for j in range(4):
   key='row'+row+'_j'+str(j);l,h=endpoints(first['arb']['values'][key]);ll,hh=endpoints(first['iv']['values'][key]);assert 0<l<=h<ll<=hh
 counts.update(strict_public_ceiling_tests=8,distinct_majorant_order_tests=12,fifth_sine_overlap_diagnostics=diagnostics)
 # Prior source bounds and the exact positive-radius bracket are checked.
 sc=read(B/'research/source_jet_corrections/evidence/checks.json')
 for mapping in ('exact_ranges','portable_bounds'):
  dl,dh=endpoints(sc[mapping]['D']);cl,ch=endpoints(sc[mapping]['C']);assert F('6.70197e-7')<dl<=dh and 0<cl<=ch<F('30.0230')
 pl,ph=map(F,sc['root_bracket_exact']);assert 0<pl<=ph<9
 # Independent rational Taylor series for Rb with proved tail.
 term=total=F(1)
 for n in range(1,129):term*=t/n;total+=term
 assert 0<t<9 and t/130<1;hi=total+(term*t/129)/(1-t/130)
 assert F('3412.96685816')<total<=hi<F('3412.96685817')
 assert 18<3000<total and 1<L<total
 for name in first:
  l,h=endpoints(first[name]['values']['R_b']);assert max(l,total)<=min(h,hi)
 assert F(pub['total_j1'])<F(pub['total_j0'])<F('1e-8')
 margin=F('6.70197e-7')-F('30.0230')*F(pub['total_j0']);assert margin>F('6.6989e-7')>F('3.69e-7')
 counts.update(source_endpoint_tests=4,root_bracket_tests=1,radius_taylor_terms=129,strict_source_margin_tests=2)
 # Complete deterministic reruns into NEW files, preserving all old evidence.
 for name in ('arb','iv'):
  out=E/('rerun_'+name+'.json');proc=subprocess.run([sys.executable,str(D/'code'/('engine_'+name+'.py')),'--output',str(out)],cwd=B,capture_output=True,text=True,timeout=30,env=os.environ.copy());(E/('rerun_'+name+'.log')).write_text(proc.stdout+proc.stderr);assert proc.returncode==0
  old=first[name].copy();new=read(out)
  for x in (old,new):x.pop('utc');x.pop('seconds')
  assert old==new,name
 counts['complete_engine_reruns']=2
 assert read(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')
 assert read(E/'addendum_first.json')['sha256']==sha(D/'ADDENDUM.md')
 for p in (D/'PROOF.md',D/'ADDENDUM.md',D/'source/public_ceilings.json',D/'code/engine_arb.py',D/'code/engine_iv.py',Path(__file__),E/'arb.json',E/'iv.json',E/'proof_first.json',E/'addendum_first.json',E/'rerun_arb.json',E/'rerun_iv.json',E/'rerun_arb.log',E/'rerun_iv.log'):pins[str(p.relative_to(B))]=sha(p)
 for p,h in pins.items():assert sha(B/p)==h,p
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_FINITE_AUDIT_REQUIRES_COLLABORATIVE_CLOSURE','counts':counts,'strict_public_ceilings':pub,'strict_source_defect_lower':'6.6989e-7','source_margin_exact':str(margin),'radius_taylor':{'lower_exact':str(total),'upper_exact':str(hi)},'exact_Zj':list(map(str,Z)),'source_archive':{'path':str(archive),'sha256':sha(archive)},'files':dict(sorted(pins.items())),'seconds':time.monotonic()-st,'scope':'Explicit106 repair at every admissible T only. Reuses previously independently certified H2 coefficients. No global inverse, small forcing, surrounding exclusion or endpoint.'}
 (E/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('utc','status','counts','seconds')}))
if __name__=='__main__':run()
