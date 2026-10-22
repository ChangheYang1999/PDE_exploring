"""Exact contracts and independent Arb/iv arithmetic for conditional flow lemmas.
No trajectory computation and no numerical non-trapping claim.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,itertools
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=384;ctx.threads=1;iv.dps=160
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/global_flow/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ex(x):
 assert x.is_finite() and x.rad()==0;m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return ex(x.lower()),ex(x.upper())
def ie(x):
 out=[]
 for s,m,e,bc in x._mpi_:assert bc>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return tuple(out)
def pack(x,method):
 lo,hi=ae(x) if method=='arb' else ie(x);return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}

def main():
 trp=BASE/'data_exact/modal_v2.json';assert sha(trp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 tr=json.loads(trp.read_text());k=F.from_float(float.fromhex(tr['scalars_hex']['k']));assert k==F(1615536043799051,9007199254740992)
 a,b,gamma=F(129,20),F(307,100),F(1129,1000);S=a+b;cl=1/k;A0=2/k-1;D0=4/k-1
 values={'k':k,'cl':cl,'A0':A0,'D0':D0,'T_corner':-(1+cl)-a*A0+b*D0,'T_source_frozen_mu1':-(1+cl)+b,'T_far':-(1+cl)+gamma*cl,'kappa_inf':(1+k-gamma)/k,'inverse_lower_bound_conditional':k/(1+k-gamma),'quarter_margin':(1+k-gamma)/k-F(1,4),'unweighted_inverse_upper':1/(1+cl)}
 ka=aa(k);ki=iq(k);av={
 'k':ka,'cl':1/ka,'A0':2/ka-1,'D0':4/ka-1,
 'T_corner':-(1+1/ka)-aa(a)*(2/ka-1)+aa(b)*(4/ka-1),
 'T_source_frozen_mu1':-(1+1/ka)+aa(b),'T_far':-(1+1/ka)+aa(gamma)/ka,
 'kappa_inf':(1+ka-aa(gamma))/ka,'inverse_lower_bound_conditional':ka/(1+ka-aa(gamma)),
 'quarter_margin':(1+ka-aa(gamma))/ka-aa(F(1,4)),'unweighted_inverse_upper':1/(1+1/ka)}
 bv={
 'k':ki,'cl':iv.power(ki,-1),'A0':(2-ki)/ki,'D0':(4-ki)/ki,
 'T_corner':iq(a-b-1)+iq(-1-2*a+4*b)/ki,
 'T_source_frozen_mu1':iq(b-1)-1/ki,'T_far':iq(gamma-1)/ki-1,
 'kappa_inf':1-iq(gamma-1)/ki,'inverse_lower_bound_conditional':1/(1-iq(gamma-1)/ki),
 'quarter_margin':iq(F(3,4))-iq(gamma-1)/ki,'unweighted_inverse_upper':ki/(ki+1)}
 arithmetic=[]
 for name,q in values.items():
  x,y=ae(av[name]),ie(bv[name]);assert x[0]<=q<=x[1] and y[0]<=q<=y[1]
  arithmetic.append({'name':name,'exact':str(q),'arb':pack(av[name],'arb'),'iv':pack(bv[name],'iv')})
 assert values['T_corner']<0 and values['T_source_frozen_mu1']<0 and values['T_far']<0 and values['quarter_margin']>0
 # The previously independently certified actual local source enclosure.
 sp=BASE/'research/modal_source/evidence/source_result.json';ap=sp.with_name('output_audit.json');src=json.loads(sp.read_text());audit=json.loads(ap.read_text())
 assert sha(ap)=='1ac210fb952eb83594ab9975bb0fafd4c56759ddbd654a4443c58190f83e2e6e'
 assert sha(sp)==audit['source_result_sha256']=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691' and audit['verdict']=='PASS'
 assert src['input_sha256']==sha(trp)
 m=src['final_values']['mu_minus_1'];ml,mh=1+F(m['lower_exact']),1+F(m['upper_exact']);assert 0<ml<mh<1
 source_interval=[-(1+cl)+b*ml,-(1+cl)+b*mh];assert source_interval[1]<0
 ma=aa((ml+mh)/2)+arb(0,aa((mh-ml)/2));mi=iv.mpf([iq(ml).a,iq(mh).b])
 actual_a=-(1+1/ka)+aa(b)*ma;actual_i=iq(b-1)-1/ki+iq(b)*(mi-1)
 for bound in [ae(actual_a),ie(actual_i)]:assert bound[0]<=source_interval[0]<=source_interval[1]<=bound[1]
 # p=4 conic logarithmic differentiation, two algebraic forms of margin.
 conic=0
 for x,y,q1,q2,R in itertools.product([F(1,10),F(1),F(7)],[F(1,11),F(2),F(8)],[F(-9),F(0),F(6)],[F(-2),F(1),F(20)],[F(1),F(6)]):
  r2=x*x+y*y;z=r2*r2/R**4;s=(x*x*q1+y*y*q2)/r2;mu=gamma+(S-gamma)/(1+z)
  direct_log_derivative=-2*a*q1-2*b*q2+2*(S-gamma)*z*s/(1+z)
  margin1=-(1+cl)-direct_log_derivative/2
  margin2=-(1+cl)+a*(q1-s)+b*(q2-s)+mu*s
  assert margin1==margin2;conic+=1
 # Exact finite history contracts for the orbit correction. These cannot
 # establish any actual orbit cost. Negative constant past makes psi(t0)=0.
 orbit=0;maxima=[];kap=F(1,4)
 for coeffs in [list(map(F,[-2,3,-1,0,4,-5])),list(map(F,[-7,1,1,-3,8,-2,0])),[F(1,3),F(-1,2),F(7,4),F(-2,3)]]:
  times=[F(0)];prefix=[F(0)]
  for n,z in enumerate(coeffs):dt=F(n%3+1,3);times.append(times[-1]+dt);prefix.append(prefix[-1]+z*dt)
  psi=[v-min(prefix[:i+1]) for i,v in enumerate(prefix)];C=max(psi)
  for i in range(len(prefix)):
   for j in range(i,len(prefix)):
    assert 0<=psi[i]<=C and psi[j]-psi[i]>=prefix[j]-prefix[i]
    log0i=-prefix[i]+2*(kap-1-cl)*times[i];log0j=-prefix[j]+2*(kap-1-cl)*times[j]
    assert log0i+psi[i]-log0j-psi[j]<=2*(1+cl-kap)*(times[j]-times[i]);orbit+=1
  maxima.append(str(C))
 symbol=0
 for p,q,r in [(F(0),F(0),F(0)),(F(3),F(4),F(5)),(F(-3),F(4),F(5)),(F(3),F(-4),F(5)),(F(5),F(12),F(13)),(F(-8),F(-15),F(17))]:
  assert p*p+q*q==r*r;lam=(r-q)/2
  assert lam>=0 and lam+q>=0 and lam*(lam+q)-(p/2)**2==0
  for xi,eta in [(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(-3,5),F(4,5)),(F(5,13),F(-12,13))]:
   assert xi*xi+eta*eta==1 and p*xi*eta-q*xi*xi<=lam;symbol+=1
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_CONTRACTS_AND_INTERVAL_SCALARS','source_sha256':sha(Path(__file__)),'proof_sha256':sha(BASE/'research/global_flow/PROOF.md'),'input_sha256':sha(trp),'parameters_exact':{'k':str(k),'a':str(a),'b':str(b),'gamma':str(gamma)},'rational_values':arithmetic,'actual_source_margin':{'exact_enclosure':[str(z) for z in source_interval],'arb':pack(actual_a,'arb'),'iv':pack(actual_i,'iv'),'input_result_sha256':sha(sp),'input_audit_sha256':sha(ap)},'contracts':{'rational_scalar_arb_iv_containments':2*len(values),'actual_source_margin_containments':2,'conic_margin_identities':conic,'finite_history_orbit_inequalities':orbit,'symbol_psd_direction_checks':symbol},'finite_history_costs_exact':maxima,'scope':'Exact algebra and conditional endpoint scalar values only. No numerical flow, uniform axis-tail quotient, orbit transit/cost, smooth weight, coupled inverse or decisive endpoint.'}
 tmp=E/'checks.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'checks.json');print(json.dumps({k:v for k,v in result.items() if k not in ['rational_values','actual_source_margin']}),flush=True)
if __name__=='__main__':main()
