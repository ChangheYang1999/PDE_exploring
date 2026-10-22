from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,pickle,io,ast,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conforming_repair'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
class Reader(pickle.Unpickler):
 globals=[]
 def find_class(self,m,n):
  self.globals.append([m,n])
  allow={('numpy._core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy.core.multiarray','_reconstruct'):np._core.multiarray._reconstruct,('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype,('numpy._core.multiarray','scalar'):np._core.multiarray.scalar,('numpy.core.multiarray','scalar'):np._core.multiarray.scalar}
  check((m,n) in allow,'unapproved pickle global');return allow[m,n]
def q(x):return x if isinstance(x,F) else F(float(x))
def enc(x):return str(x.numerator)+'/'+str(x.denominator)
def horner(c,x):
 v=F(0)
 for z in reversed(c):v=v*x+q(z)
 return v
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
R=B/'research/gram_jump_rank';pr=json.loads((R/'evidence/verdict.json').read_text());pins={}
for n,h in pr['files'].items():check(sha(B/n)==h,'prior pin');pins[n]=h
src=B/'research/global_residual_assembly/evidence/primary_assembly_v2.json';para=json.loads(src.read_text());L=F(8614738245908811,1125899906842624);k=F(1615536043799051,9007199254740992);check(F(para['L_exact'])==L and F(para['k_exact'])==k and L>0 and k<F(3,2),'parameter linkage')
def A(x):x=F(x);return arb(x.numerator)/x.denominator
def qarf(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):check(x.is_finite(),'finite');return [qarf(x.lower()),qarf(x.upper())]
def weight(t):e=(2*A(t)).exp();return e*(1+e/A(L)**2)**A(F(3,2)-k)
def square(c):return [sum((c[j]*c[n-j] for j in range(len(c)) if 0<=n-j<len(c)),F(0)) for n in range(2*len(c)-1)]
def integ(c,w):return sum((v*w**(j+1)/F(j+1) for j,v in enumerate(c)),F(0))
def floorceil(x,places=18):n=x.numerator*10**places//x.denominator+1;return F(n,10**places)
rank=json.loads((R/'evidence/compute.json').read_text());records=[];alltraces=0
for rr in rank['records']:
 meta=Reader(io.BytesIO((B/rr['source']).read_bytes())).load();cols=meta['cols'];newcols=[];starts=[];maxD=F(0);maxE=F(0);maxratio=F(0);imax=None;cache={}
 for row in rr['pivots']:
  ci=row['column_indices'][0];m,pcs,lab=cols[ci];check(m==0 and lab==row['label'],'selected column');check(all(pcs[i][1]==pcs[i+1][0] for i in range(len(pcs)-1)),'consecutive pieces');check(len(pcs[0][3])>=3 and q(pcs[0][3][-1])!=0,'nonzero leading coefficient');starts.append(q(pcs[0][0]));beta=[F(0)]
  for j in range(1,len(pcs)):beta.append((horner(pcs[j-1][3],q(pcs[j-1][1])-q(pcs[j-1][0]))+q(pcs[j][3][0]))/2)
  beta.append(F(0));U=arb(0);V=arb(0);pieces=[]
  for j,(a,b,al,cc) in enumerate(pcs):
   check(al==0,'polynomial');a,b=q(a),q(b);w=b-a;c=list(map(q,cc));d0=beta[j]-c[0];dw=beta[j+1]-horner(cc,w);d1=(dw-d0)/w;d=[d0,d1];new=c.copy();new[0]+=d0;new[1]+=d1;check(new[0]==beta[j] and horner(new,w)==beta[j+1],'repaired exact traces');alltraces+=2
   ei=integ(square(d),w)+integ(square([3*d0+d1,3*d1]),w);vi=integ(square(c),w);check(ei>=0 and vi>0,'positive integrals')
   for t in [a,b]:
    if t not in cache:cache[t]=weight(t)
   U+=cache[b]*A(ei);V+=cache[a]*A(vi);maxD=max(maxD,abs(d0),abs(dw));maxE=max(maxE,abs(d1))
   pieces.append({'a_exact':enc(a),'b_exact':enc(b),'beta_left':enc(beta[j]),'beta_right':enc(beta[j+1]),'correction_constant':enc(d0),'correction_linear':enc(d1),'exact_error_integral':enc(ei),'exact_original_square_integral':enc(vi)})
  check(V>0 and U>0,'positive weighted ratio');rat=(U/V).sqrt();rb=box(rat)
  if rb[1]>maxratio:maxratio=rb[1];imax=ci
  newcols.append({'column_index':ci,'label':lab,'pieces':pieces,'U_arb512':list(map(enc,box(U))),'V_arb512':list(map(enc,box(V))),'sqrt_ratio_arb512':list(map(enc,rb))})
 check(len(starts)==len(set(starts)) and starts==sorted(starts),'distinct increasing support starts');public={'uniform_single_column_relative_broken_energy_upper':enc(floorceil(maxratio)),'uniform_coefficient_sup_error_upper':enc(floorceil(maxD)),'uniform_t_derivative_sup_error_upper':enc(floorceil(maxE))}
 records.append({'source':rr['source'],'M':rr['M'],'N':rr['N'],'independent_repaired_functions':rr['M']*rr['N'],'columns':newcols,'public':public,'largest_ratio_column':imax,'upper_ratio_float_for_orientation':float(maxratio),'max_coefficient_error_exact':enc(maxD),'max_t_derivative_error_exact':enc(maxE),'endpoint_weight_count':len(cache)})
for p in [D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),src,R/'evidence/verdict.json',R/'evidence/compute.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_AFFINE_CONTINUOUS_REPAIR_AND_ARB_BROKEN_ENERGY_BOUNDS','k_exact':enc(k),'L_exact':enc(L),'exact_repaired_trace_checks':alltraces,'records':records,'files':pins,'scope':'Single-column broken-energy comparison, uniform angular mode; no X distance from raw functions, no arbitrary-combination relative bound, operator or matrix transfer.'};p=D/'evidence/compute.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'traces':alltraces,'records':[{k:r[k] for k in ['M','N','public','largest_ratio_column','upper_ratio_float_for_orientation']} for r in records]}))
