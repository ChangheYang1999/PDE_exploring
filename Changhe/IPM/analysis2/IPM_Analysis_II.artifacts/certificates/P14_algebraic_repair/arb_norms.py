"""All residual norms for the exact eight-sector algebraic repairs.
Uses verified endpoint orders q_1=q_2=2, q_3=...=q_6=1, q_ell=0 thereafter.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import sys,time,json,hashlib
from flint import arb,arb_poly,ctx
import arb_hessian as ah
HERE=Path(__file__).resolve().parent

def group(D,d,delta,basis,weight,rproxy):
 groups={};facts=[]
 for nx in range(d+1):
  modes={}
  for (ell,kind,n),p in D[d,nx].items():
   q=2 if ell<=2 else (1 if ell<=6 else 0)
   pp=p
   for _ in range(q):pp=ah.drop_om(pp)
   if basis=='u':pp=ah.compose(pp,ah.OM)
   modes.setdefault((kind,n),[]).append((ell,q,pp));facts.append([nx,ell,kind,n,q])
  for (kind,n),rows in modes.items():
   for i,(ell,q,p) in enumerate(rows):
    for j,(ell2,q2,p2) in enumerate(rows if basis=='u' else rows[i:]):
     factor=comb(d,nx)*(2 if n==0 and kind=='c' else 1)*(1 if basis=='u' or j==0 else 2)
     b=Q(d-3)+(ell+ell2)*delta/2+q+q2-(Q(4,5) if weight else 0)-(1 if rproxy else 0)
     assert b>-1,(d,ell,ell2,q,q2,b)
     groups[b]=groups.get(b,arb_poly([]))+p*p2*factor
  print('grouped',d,basis,nx,flush=True)
 power=(1 if d%2==0 else 0)+(1 if rproxy else 0)
 factor=(ah.Z if basis=='t' else ah.OM)**power
 return {b:p*factor for b,p in groups.items()},facts

def integrate(groups,basis,weight):
 if weight:return ah.integrate_t(groups,56) if basis=='t' else ah.integrate_u(groups,56)
 S=arb(0)
 for b,p in groups.items():
  if basis=='t':
   bet=1/ah.aq(b+1)
   for n,a in enumerate(p.coeffs()):
    if n:bet*=n/ah.aq(b+n+1)
    S+=a*bet
  else:S+=sum((a/ah.aq(b+n+1) for n,a in enumerate(p.coeffs())),arb(0))
 return S,S,arb(0)

def bound(S,T,e,weight):
 assert S>0
 pref=arb.pi()/2
 if weight:pref*=ah.aq(Q(5,2))**ah.aq(Q(4,5))
 lo=T-e*S;hi=T+e*S
 assert lo>0
 return (pref*lo).sqrt(),(pref*hi).sqrt()

def run(name,prec):
 assert name.startswith('algebraic_')
 ctx.prec=prec;start=time.monotonic();c,A,sha,rawsha,D=ah.construct(name);delta=1-1/c
 for nx in range(4):D[3,nx]=ah.diff(D[2,0],2,'y',delta) if nx==0 else ah.diff(D[2,nx-1],2,'x',delta)
 # The analytic endpoint orders rely on the exact repair, independently audited
 # for this identical coefficient hash. Record that link and test every factor.
 audit_path=HERE/'repair_audit.json';audit=json.loads(audit_path.read_text())
 row=next(r for r in audit['variants'] if r['name']==name)
 assert row['canonical_sha256']==sha and row['exact_difference_checked'],('source not in exact repair audit',name,sha)
 assert audit['verdict']=='CONFIRMED'
 out={'utc_started':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'precision_bits':prec,'canonical_sha256':sha,'source_record_sha256':rawsha,'repair_audit_sha256':hashlib.sha256(audit_path.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'norms':{}}
 dest=HERE/(name+'_arb_norms.json')
 for label,d,weight,rproxy in [('rF',0,False,True),('F',0,False,False),('DF',1,False,False),('omega_D2F',2,True,False),('omega_D3F',3,True,False)]:
  gt,facts=group(D,d,delta,'t',weight,rproxy);s,t,e=integrate(gt,'t',weight);lo,hi=bound(s,t,e,weight)
  gu,_=group(D,d,delta,'u',weight,rproxy);ss,tt,ee=integrate(gu,'u',weight);l2,h2=bound(ss,tt,ee,weight)
  assert s.overlaps(ss) and t.overlaps(tt) and lo.overlaps(l2) and hi.overlaps(h2)
  out['norms'][label]={'lower_ball':lo.str(80),'upper_ball':hi.str(80),'lower_endpoint':str(lo.lower()),'upper_endpoint':str(hi.upper()),'u_lower_ball':l2.str(80),'u_upper_ball':h2.str(80),'base_integral':s.str(80),'weighted_integral':t.str(80),'structural_endpoint_factors':facts}
  out['utc_updated']=datetime.now(timezone.utc).isoformat(timespec='seconds');out['elapsed_seconds']=time.monotonic()-start;out['status']='PARTIAL'
  dest.write_text(json.dumps(out,indent=2)+'\n');print(label,lo.str(40),hi.str(40),'seconds',time.monotonic()-start,flush=True)
 checks=[]
 for xs,ys in [('0','1/10'),('1','0'),('1/2','1/2'),('1','2'),('3','1'),('60','80'),('0','1000')]:
  x,y=Q(xs),Q(ys);pv=ah.evaluate(D,delta,x,y);cv=ah.au.direct_F(A,c,ah.aq(x),ah.aq(y))
  ok={str(k):v.is_finite() and cv[k].is_finite() and v.overlaps(cv[k]) for k,v in pv.items()}
  assert all(ok.values()),(xs,ys,ok)
  checks.append({'point':[xs,ys],'components':ok});print('Cartesian',xs,ys,'PASS',flush=True)
 out.update({'utc_completed':datetime.now(timezone.utc).isoformat(timespec='seconds'),'cartesian_checks':checks,'elapsed_seconds':time.monotonic()-start,'status':'PENDING_PROOF_AUDIT'})
 dest.write_text(json.dumps(out,indent=2)+'\n');print('DONE',name,out['elapsed_seconds'],flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'algebraic_n12_m10_k8',int(sys.argv[2]) if len(sys.argv)>2 else 1280)
