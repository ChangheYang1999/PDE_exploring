from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from collections import defaultdict
import hashlib,json,time,sys
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
B=Path(__file__).resolve().parents[1];S=B.parent/'weighted_tail_candidate_audit'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rat(v):
 x=Fraction(str(v));return Q(x.numerator,x.denominator)
def ar(v):return arb(v.numerator)/v.denominator
def decode(d):return {int(n):rat(v) for n,v in d.items()}
def put(d,n,v):
 if n==0 or v==0:return
 if n<0:n,v=-n,-v
 d[n]=d.get(n,Q(0))+v
 if not d[n]:del d[n]
def product(out,P,T,ep,et):
 for m,A in P.items():
  for n,V in T.items():
   av=A*V/2
   put(out,n+m,av*(-et*m+(ep+1)*n));put(out,n-m,av*(-et*m-(ep+1)*n))
start=time.monotonic();inputs=json.loads((S/'data/inputs.json').read_text());rows=[]
for name in ['007','013','014']:
 inp=next(i for i in inputs if i['candidate']==name);src=Path(inp['path']);assert sha(src)==inp['sha256']
 state=json.loads(src.read_text());oldp=S/f'data/{name}_sectors.json';old=json.loads(oldp.read_text())
 c=rat(state['cl']);gamma=1/c;delta=1-gamma;p=2*gamma;q=1-4*delta-2
 assert -3<q<0 and 0<delta<1
 amp=defaultdict(lambda:[Q(0),Q(0)])
 for (j,m,k),v in zip(state['order'],state['coefficients']):
  if j==3:amp[m][0]+=rat(v);amp[m][1]+=k*rat(v)
 correction=[];Tr={};Pr={};moments=[]
 for m,(P0,P1) in sorted(amp.items()):
  A1=p*P0-P1
  if not A1:continue
  correction.extend([{'order':[3,m,m+4],'coefficient':str(-A1)},{'order':[3,m,m+5],'coefficient':str(A1)}])
  dP0=-A1+A1;dP1=-(m+4)*A1+(m+5)*A1;dA1=p*dP0-dP1
  assert dP0==0 and dA1==-A1
  moments.append({'m':m,'A1':str(A1),'delta_P1':str(dP1),'origin_vanishing_order':2*m+8})
  d=q+3;n=2*m;A=-A1
  put(Tr,n+1,-A*(d*d-n*n)*(d-2-n)/2);put(Tr,n-1,A*(d*d-n*n)*(d-2+n)/2)
  put(Pr,n+2,A*(d-n)*(d-n-2)/4);put(Pr,n-2,-A*(d+n)*(d+n-2)/4)
 oldTh={(r['K'],r['L']):decode(r['density']) for r in old['sectors']};oldPs={(r['K'],r['L']):decode(r['stream']) for r in old['sectors']}
 assert Tr=={n:-v for n,v in oldTh[4,1].items()};assert Pr=={n:-v for n,v in oldPs[4,1].items()}
 assert all(not oldTh[k,1] and not oldPs[k,1] for k in [1,2,3])
 oldF=decode(next(r for r in old['sectors'] if (r['K'],r['L'])==(4,1))['residual'])
 assert oldF=={n:(c*q-1)*v for n,v in oldTh[4,1].items()}
 Th=dict(oldTh);Ps=dict(oldPs);Th[4,1]={};Ps[4,1]={};records=[]
 expo=lambda k:1-k[0]*delta-2*k[1]
 for K in range(1,10):
  for L in range(2):
   key=K,L;e=expo(key);F={n:(c*e-1)*v for n,v in Th.get(key,{}).items() if (c*e-1)*v}
   for K1 in range(1,K):
    for L1 in range(L+1):product(F,Ps.get((K1,L1),{}),Th.get((K-K1,L-L1),{}),expo((K1,L1)),expo((K-K1,L-L1)))
   if e>=-3:assert not F,(name,key)
   records.append({'K':K,'L':L,'exponent_exact':str(e),'residual_zero':not F,'nonzero_angular_modes':len(F)})
 nz=[x for x in records if not x['residual_zero']];first=max(nz,key=lambda x:rat(x['exponent_exact']))
 assert (first['K'],first['L'])==(9,0)
 firstexp=expo((9,0));epsilon1=-3-firstexp;assert epsilon1>0
 assert gamma-4<firstexp and 1-10*delta<firstexp
 Cq=arb(1)/2+arb(2)**(-ar(q))+arb(2)**(1-ar(q))/ar(q+3)+arb(2)**(3-ar(q))+arb(2)**(ar(q)+2)/ar(-q)
 outdata={'candidate':name,'canonical':inp,'source_sector_sha256':sha(oldp),'formula':'-(1+r^2)^(2gamma) sum A1_m t^(m+4)(1-t) cos(2m theta)','potential_correction':correction,'moment_checks':moments,'after_residual_sectors':records}
 dst=B/f'data/{name}_tail_repair.json'
 with dst.open('x') as f:json.dump(outdata,f,indent=2);f.write('\n')
 row={'candidate':name,'q_exact':str(q),'q_float':float(q),'Cq_arb':Cq.str(80),'first_repaired_residual_sector':[9,0],'first_repaired_residual_exponent_exact':str(firstexp),'epsilon1_exact':str(epsilon1),'epsilon1_float':float(epsilon1),'repaired_residual_threshold_exact':str(firstexp+1),'correction_density_modes':len(Tr),'correction_potential_modes':len(moments),'minimum_potential_origin_order':min(x['origin_vanishing_order'] for x in moments),'all_sector_checks_above_minus3_zero':True,'data_sha256':sha(dst)}
 rows.append(row);print(name,'first repaired sector9,0 exponent',float(firstexp),'epsilon1',float(epsilon1),'Cq',Cq.str(20),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in [B/'PROOF.md',Path(__file__),S/'data/inputs.json',S/'verification/result.json']},'rows':rows,'elapsed_seconds':time.monotonic()-start,'status':'Exact checks passed; conditional asymptotic theorem and reference-design operation OPEN independent Opus review'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('DONE',out['utc'],out['elapsed_seconds'],flush=True)
