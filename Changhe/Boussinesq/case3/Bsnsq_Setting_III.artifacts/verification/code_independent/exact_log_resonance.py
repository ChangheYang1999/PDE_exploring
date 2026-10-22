"""Exact binary-rational endpoint resonance witnesses; no fitting-lane code."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import json,time,sys,numpy as np
from r2_state_values import R2State

def derivative(c,knots,p):
 ans=[p*(c[i+1]-c[i])/(knots[i+p+1]-knots[i+1]) for i in range(len(c)-1)]
 return ans,knots[1:-1],p-1

def endpoint_second(c,knots,p):
 c,t,d=derivative(c,knots,p);c,t,d=derivative(c,t,d)
 return c[-1]

def manufacture():
 p=5;t=[Q(0)]*6+[Q(1,7),Q(3,5)]+[Q(1)]*6;nb=len(t)-p-1;cases=[];checks=0
 for j in range(6):
  co=[]
  for i in range(nb):
   elementary=[Q(1)]+[Q(0)]*p
   for v in t[i+1:i+p+1]:
    for k in range(p,0,-1):elementary[k]+=v*elementary[k-1]
   co.append(elementary[j]/comb(p,j))
  for left,right in [(Q(0),Q(1,7)),(Q(1,7),Q(3,5)),(Q(3,5),Q(1))]:
   for k in range(1,7):
    x=left+(right-left)*Q(k,7)
    @lru_cache(None)
    def basis(i,d):
     if d==0:return Q(int(t[i]<=x<t[i+1]))
     val=Q(0)
     if t[i+d]!=t[i]:val+=(x-t[i])/(t[i+d]-t[i])*basis(i,d-1)
     if t[i+d+1]!=t[i+1]:val+=(t[i+d+1]-x)/(t[i+d+1]-t[i+1])*basis(i+1,d-1)
     return val
    assert sum(co[i]*basis(i,p) for i in range(nb))==x**j;checks+=1
  d2=endpoint_second(co,t,p);assert d2==j*(j-1);checks+=1
  cases.append({'power':j,'second_endpoint_exact':str(d2)})
 return {'checks':checks,'cases':cases,'verdict':'PASSED'}

def scalar_raw(state,raw):
 if raw is None:return [Q(0)]*state.nb
 c=np.asarray(raw).reshape(state.K,state.nb)
 vals=[]
 for i in range(state.nb):
  a=Q.from_float(float(c[0,i]))
  b=Q.from_float(float(c[2,i])) if state.K>2 and i>=1 else Q(0)
  vals.append(a-b/2)
 return vals

def main():
 start=time.monotonic();root=Path('research/95_serialized_beta_three_log_constant/verification');manifest=json.loads((root/'manifest.json').read_text());floats=json.loads((root/'results.json').read_text())
 out={'started_utc':datetime.now(timezone.utc).isoformat(),'manufacture':manufacture(),'states':[],'scope':'Exact algebra on stored binary rational inputs. No PDE existence claim or interval bound on a continuum profile.'}
 for item,fr in zip(manifest['states'],floats['states']):
  s=R2State(item['snapshot']);assert s.bb==3
  knots=[Q.from_float(float(v)) for v in s.knots];L=Q.from_float(s.L);eps=Q.from_float(float(s.meta.get('eps',1.)))
  g=scalar_raw(s,s.rawG);e=scalar_raw(s,s.extG);d=scalar_raw(s,s.defectG);mix=[eps*a+(1-eps)*b+c for a,b,c in zip(g,e,d)]
  row={'label':item['label'],'archive_sha256':s.sha256,'L':str(L),'eps':str(eps),'sources':{}}
  for kind,c in [('self',g),('transport',mix)]:
   sec=endpoint_second(c,knots,s.degree);alpha=L*L*sec/2;ap=fr['sources'][kind]['evaluations'][-1]['alpha'];diff=abs(float(alpha)-ap)
   assert diff<1e-9*(1+abs(float(alpha)))
   row['sources'][kind]={'Ssecond_end':str(sec),'alpha_exact':str(alpha),'alpha_float':float(alpha),'nonzero':bool(alpha),'float_stable_formula_difference':diff,'scalar_coefficients_exact':[str(v) for v in c]}
  row['self_finite_beta3_profile_constraint_violated']=bool(s.beta==3 and Q(row['sources']['self']['alpha_exact']))
  print(item['label'],'exactselfalpha',row['sources']['self']['alpha_float'],'betathreeconstraint',row['self_finite_beta3_profile_constraint_violated'],flush=True)
  out['states'].append(row)
 out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
 (root/'exact_resonance.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
