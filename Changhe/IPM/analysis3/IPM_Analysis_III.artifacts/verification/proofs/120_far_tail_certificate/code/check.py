import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import importlib.util,json,hashlib,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('point',LANE/'proofs/105_residual_norm_point_audit/code/check_points.py');P=importlib.util.module_from_spec(sp);sp.loader.exec_module(P)
G=P.G;M=G.M;ANG=P.ANG;aa=P.aa

def lightweight():
 source=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
 raw=M.np.load(source,allow_pickle=False)
 d=type('OuterData',(),{})();d.sha=hashlib.sha256(source.read_bytes()).hexdigest();G.check_hash(d)
 assert raw['Aout'].shape==(260,10) and int(raw['p'])==7
 knots=[M.rat(x) for x in raw['knots']];d.tp=knots[-1];d.k=M.rat(raw['k']);d.bo=M.rat(raw['bo'])
 d.knots=knots;d.spans=[j for j in range(7,len(knots)-8) if knots[j]<knots[j+1]]
 pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)]
 d.alphas=[d.k-3-j*(1-d.k)-2*l for j,l in pairs]
 scalar=json.loads(M.SCALAR.read_text());assert scalar['input_sha256']==d.sha
 z=arb(scalar['normalization_correction_z']['ball']);A=[[M.rat(v) for v in row] for row in raw['Aout']];eo=[]
 for m in range(260):
  co=[M.rat(v) for v in raw['S'][m,-8:][::-1]]
  jp=[(-1)**j*v for j,v in enumerate(M.endpoint_jets([-x for x in knots[::-1]],co))]
  op=[sum((A[m][l]*d.alphas[l]**j for l in range(10)),F(0)) for j in range(7)]
  eo.append(M.match(jp,op,-d.bo))
 A=[[aa(x) for x in row] for row in A];eo=[[aa(x) for x in row] for row in eo]
 A[0][0]+=z
 for j in range(7):eo[0][j]-=z*aa((d.alphas[0]+d.bo)**j/F(factorial(j)))
 d.A=M.project_mode_rows(A);d.Eo=M.project_mode_rows(eo)
 assert all(x==0 for x in d.A[-1]+d.Eo[-1])
 return d

def remove(ep,e):return G.EP({q:p for q,p in ep.terms.items() if q!=e})
def majorant(ep,rate,shift):
 ans=arb(0)
 for e,poly in ep.shift(shift).terms.items():
  if all(x==0 for x in poly):continue
  assert e<=rate,(e,rate)
  if e==rate:
   assert all(x==0 for x in poly[1:]);ans+=arb(poly[0].abs_upper())
  else:
   ans+=sum((arb(v.abs_upper())*factorial(j)/aa(rate-e)**j for j,v in enumerate(poly)),arb(0))
 return arb(ans.upper())
def total(eps,rate,shift,angular=False):
 return sum(((2*j+1 if angular else 1)*majorant(ep,rate,shift) for j,ep in enumerate(eps)),arb(0))
def interval(x):return G.rec(x)
def tailpair(lead,error):
 lo=arb(0) if (lead-error).lower()<=0 else arb((lead-error).lower())**2
 hi=arb((lead+error).upper())**2
 return {'leading_norm':interval(lead),'error_norm_bound':interval(error),'relative_error_bound':interval(error/lead),'energy_lower':interval(lo),'energy_upper':interval(hi)}
def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();d=lightweight();cache=G.load_cache(d)
 k=d.k;ell=1/aa(k);a0=k-3;a1=2*k-4;a2=3*k-5;b0=k-1;b1=2*k-2
 assert -d.bo<a2 and -4<b1
 h=G.density_eps(d,'outer');pe,qe,_,_=G.outer_eps(d,cache)
 hs=[remove(x,a0) for x in h];ps=[remove(x,b0) for x in pe];qs=[remove(x,b0) for x in qe]
 dh=[x.scale(3)+x.deriv() for x in h];dhs=[x.scale(3)+x.deriv() for x in hs]
 ls=[]
 for x in h:
  y=G.EP()
  for e,pol in x.terms.items():
   if e in (a0,a1):assert len(pol)==1;continue
   y.addterm(e,[aa((3+e)/k-1)*v+(j+1)*pol[j+1]*ell if j+1<len(pol) else aa((3+e)/k-1)*v for j,v in enumerate(pol)])
  ls.append(y)
 p0=[x.terms[b0][0] for x in pe];q0=[x.terms[b0][0] for x in qe];A=[row[0] for row in d.A];B=[row[1] for row in d.A]
 sins=P.residual_sines(A,[aa(a0)*v for v in A],p0,q0,arb(0))
 for j in range(len(A)):sins[j]+=A[j]+(1-ell)*B[j]
 cof=P.cofactor(sins);gamma=ANG.axis(cof);qu=ANG.quotient(cof);mass=ANG.beta_mass();es=mass*ANG.normalized_square(qu,ANG.moments(1044))
 ref=json.loads((LANE/'proofs/117_far_residual_leading_term/evidence/check.json').read_text())
 assert es.overlaps(arb(ref['remainder_coefficient_tau']['ball'])) and gamma.overlaps(arb(ref['axis_coefficient_tau']['ball']))
 N=522;cn=aa(4*N**4*(2*N+1));rows=[];r0=4*k-F(5,4);r2=6*k-F(13,4)
 for T in [F(20),F(30),F(40),F(45),F(60)]:
  shift=T-d.tp;P0=sum((arb(v.abs_upper()) for v in p0),arb(0))*(aa(b0*shift)).exp();Q0=sum((arb(v.abs_upper()) for v in q0),arb(0))*(aa(b0*shift)).exp()
  BB=total(ls,a2,shift)+P0*total(dhs,a1,shift)+total(ps,b1,shift)*total(dh,a0,shift)+Q0*total(hs,a1,shift,True)+total(qs,b1,shift)*total(h,a0,shift,True)
  leadfactor=(aa(F(27,4)*T+2*a1*shift)).exp()/aa(-r0)
  dfactor=cn*BB*(aa(F(27,8)*T)).exp()/aa(-r2).sqrt()
  rr=tailpair((leadfactor*es).sqrt(),mass.sqrt()*dfactor)
  yy=tailpair((leadfactor*(es+gamma**2)).sqrt(),(1+mass).sqrt()*dfactor)
  row={'T':str(T),'raw_error_constant':interval(BB),'remainder':rr,'full_Y':yy};rows.append(row)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'T':str(T),'relative_rem_error':rr['relative_error_bound']['ball'],'rem_tail_upper':rr['energy_upper']['ball'],'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','precision_bits':512,'original_sha256':d.sha,'normalization_source_sha256':hashlib.sha256(M.SCALAR.read_bytes()).hexdigest(),'green_source_sha256':hashlib.sha256(G.CACHE.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'N':N,'angular_operator_bound':str(4*N**4*(2*N+1)),'rate_leading':str(r0),'rate_error':str(r2),'rows':rows,'seconds':time.monotonic()-start}
 (ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
