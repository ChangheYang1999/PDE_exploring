"""Exact constants and independent interval checks for the r2 input condition."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from flint import arb,ctx
from mpmath import iv
D=Path(__file__).resolve().parents[1];ctx.prec=256;iv.dps=100;start=time.monotonic()
u=F(1,2**53);eta=F(1,2**1074)
def ff(x):return F.from_float(float(x))
def ar(x):return arb(x.numerator)/x.denominator
def ir(x):return iv.mpf(x.numerator)/x.denominator
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
counts=0;minimum=None
for n in range(1,4097):
 A=ff(np.nextafter(1+(n+1)*float(u),np.inf))
 assert A>=1+(n+1)*u
 assert n*(n+1)*u<F(1,2) and 1-n*u>0
 threshold=n*eta/u;assert ff(float(threshold))==threshold and threshold>=F(2)**-1022
 slack=(A*(1-n*u)-1)*threshold-n*eta/2;assert slack>=0
 # Independently enclose the crucial exact surplus in two interval engines.
 aa=(ar(A)*(1-ar(n*u))-1)*ar(threshold)-ar(n*eta/2)
 ii=(ir(A)*(1-ir(n*u))-1)*ir(threshold)-ir(n*eta/2)
 assert aa.lower()>0 and ii.a>0
 minimum=slack/eta if minimum is None else min(minimum,slack/eta);counts+=6
cases=[]
for n in [1,2,3,13,117,523,4096]:
 # One exactly represented normal leaf at the criterion and n-1 underflow ties.
 x=np.full(n,float(eta));y=np.full(n,0.5);x[0]=float(n*eta/u);y[0]=1
 product=x*y;s=float(product.sum());A=float(np.nextafter(1+(n+1)*float(u),np.inf));out=float(np.nextafter(s*A,np.inf))
 exact=sum((ff(a)*ff(b) for a,b in zip(x,y)),F(0));threshold=n*eta/u
 assert ff(s)>=threshold and ff(out)>=exact
 aa=sum((ar(ff(a))*ar(ff(b)) for a,b in zip(x,y)),arb(0));ii=sum((ir(ff(a))*ir(ff(b)) for a,b in zip(x,y)),iv.mpf(0))
 assert ar(ff(out)).lower()>=aa.upper() and ir(ff(out)).a>=ii.b
 cases.append({'n':n,'kind':'normal_leaf_at_threshold_plus_underflow_ties','computed_sum_exact':str(ff(s)),'criterion_exact':str(threshold),'exact_sum':str(exact),'rounded_result_exact':str(ff(out)),'margin_over_eta':str((ff(out)-exact)/eta)})
# Preserve the failed generic case, without calling it a failure of the criterion.
n=523;x=np.full(n,float(eta));y=np.full(n,0.5);s=float((x*y).sum());out=float(np.nextafter(s*np.nextafter(1+(n+1)*float(u),np.inf),np.inf))
assert s==0 and ff(out)==eta and ff(out)<n*eta/2 and ff(s)<n*eta/u
p=D/'R2_CERTIFICATE_CONDITION.md';pf=D/'evidence/r2_certificate_condition_proof_first.json';assert json.loads(pf.read_text())['sha256']==sha(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_r2_SUFFICIENT_INPUT_TEST','seconds':time.monotonic()-start,'n_values':4096,'exact_and_interval_constant_checks':counts,'minimum_exact_surplus_over_eta':str(minimum),'actual_n':523,'actual_n_threshold_exact':str(523*eta/u),'actual_n_threshold_float':float(523*eta/u),'native_boundary_cases':cases,'generic_counterexample_still_fails':True,'proof_sha256':sha(p),'scope':'Universal scalar lemma with explicit tree assumptions. No actual forcing r2 inputs or sums have been checked.'}
(D/'evidence/r2_condition.json').write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['status'],'checks',counts,'threshold',result['actual_n_threshold_float'],'seconds',result['seconds'])
