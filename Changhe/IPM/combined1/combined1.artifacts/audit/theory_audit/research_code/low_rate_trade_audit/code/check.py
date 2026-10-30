from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(v):return arb(v.numerator)/v.denominator
def gram(mu,bl,w1,w0,m2=Q(1,2),m1=Q(9,10)):
 return [[m2-mu,Q(-347,10),Q(-5)],[Q(-347,10),w1*(m1-mu)-40,Q(-3*w1)],[Q(-5),Q(-3*w1),w0*(bl-mu)]]
def pivots(mat):
 a=[list(row) for row in mat];out=[]
 for k in range(3):
  p=a[k][k];out.append(p)
  if p<=0:return out
  for i in range(k+1,3):
   for j in range(k+1,3):a[i][j]-=a[i][k]*a[k][j]/p
 return out
def pd(mat):
 p=pivots(mat);return len(p)==3 and all(v>0 for v in p)
def bracket(bl,w1,w0,m2=Q(1,2),m1=Q(9,10)):
 lo=Q(0);hi=min(m2,m1,bl)
 if not pd(gram(lo,bl,w1,w0,m2,m1)):return None
 for _ in range(90):
  mid=(lo+hi)/2
  if pd(gram(mid,bl,w1,w0,m2,m1)):lo=mid
  else:hi=mid
 assert pd(gram(lo,bl,w1,w0,m2,m1)) and not pd(gram(hi,bl,w1,w0,m2,m1))
 return {'positive_lower':str(lo),'nonpositive_upper':str(hi),'lower_ball':ar(lo).str(60),'upper_ball':ar(hi).str(60)}
start=time.monotonic();ctx.prec=512
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(__file__),'peer_code_sha256':sha(ROOT/'source/T1_bl2_trade.py'),'peer_output_sha256':sha(ROOT/'source/T1_bl2_trade.out'),'critical_rates':[],'parameter_instances':[],'rate_brackets':[],'floor_sensitivity':[]}
for name,w1,w0,Cp,rounded,safe in [('sharp',2**14,2**18,401,Q(7602,10000),Q(76024,100000)),('sharpw',2**15,2**20,397,Q(3432,10000),Q(34325,100000))]:
 a=Q(1,2);b=Q(9,10)*w1-40;d=Q(-347,10);p=Q(-5);q=Q(-3*w1)
 assert a>0 and b-d*d/a>0
 critical=(p*p/a+(q-d*p/a)**2/(b-d*d/a))/w0
 assert critical==(25*b+1041*w1+Q(9,2)*w1*w1)/(w0*(b/2-Q(347,10)**2))
 assert rounded<critical<safe
 assert not pd(gram(Q(0),rounded,w1,w0)) and pd(gram(Q(0),safe,w1,w0))
 out['critical_rates'].append({'name':name,'exact':str(critical),'enclosure':ar(critical).str(90),'inadmissible_rounded_value':str(rounded),'safe_strictly_larger_value':str(safe)})
 for bl in [Q(2),Q(19,10),Q(9,5),Q(8,5),Q(7,5),Q(6,5),Q(1),Q(4,5),Q(3,5),Q(1,2),Q(2,5)]:
  out['rate_brackets'].append({'name':name,'beta_L':str(bl),'certificate':bracket(bl,w1,w0)})
 for floor,m2,m1 in [('A2',Q(1,2),Q(9,10)),('P96 quoted',Q(293619,500000),Q(972875,1000000)),('packet caps quoted',Q(61151,100000),Q(99116,100000))]:
  out['floor_sensitivity'].append({'name':name,'floor':floor,'scope':'Arithmetic only, conditional on the displayed matrix bounds. Packet caps are upper limits, not sufficient global bounds.','certificate':bracket(Q(2),w1,w0,m2,m1)})
for bl,mu,n,r,rate,eta,ratio in [(Q(7,5),Q(359,1000),74,Q(1213,10**6),Q(279,2000),Q(423,2500000),Q(49,2500)),(Q(1),Q(151,500),81,Q(459,500000),Q(581,5000),Q(533,5000000),Q(229,10000))]:
 s=Q(1,n*n);ps=pivots(gram(mu,bl,2**15,2**20));assert len(ps)==3 and all(v>0 for v in ps)
 beta=mu-397*s-Q(8,5)*r*n
 grad2=r*r/(4*Q(333,106)*s*(1+s))
 checks={'s_range':0<s<=Q(1,1024),'rate':beta>=rate,'residual':eta<=rate*r,'contraction_ratio':grad2<=(ratio*bl)**2,'strict_contraction':ratio<1,'positive_slope':grad2<Q(7,10)**2}
 assert all(checks.values())
 out['parameter_instances'].append({'beta_L':str(bl),'mu':str(mu),'s':str(s),'r':str(r),'certified_rate':str(rate),'actual_rate_expression':str(beta),'eta':str(eta),'G0_necessary_upper':str(eta/1024),'contraction_ratio_upper':str(ratio),'positive_LDL_pivots':list(map(str,ps)),'checks':checks})
out['elapsed_seconds']=time.monotonic()-start
(ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out['critical_rates']:print(row['name'],row['exact'],row['enclosure'],flush=True)
print('All checks pass; seconds',out['elapsed_seconds'],flush=True)
