"""Exact supremum enclosure from rational points and Bernstein positivity."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import comb
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];ctx.prec=768;start=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
checks=[]
def need(label,value):
 assert bool(value),label
 checks.append(label)
def add(*polys):
 r=[Q(0)]*max(map(len,polys))
 for p in polys:
  for i,x in enumerate(p):r[i]+=x
 return r
def scale(p,a):return [Q(a)*x for x in p]
def mul(a,b):
 r=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return r
def affine(p,a,b):
 r=[Q(0)]*len(p)
 for j,c in enumerate(p):
  for i in range(j+1):r[i]+=c*comb(j,i)*a**(j-i)*b**i
 return r
def bern(p):
 n=len(p)-1
 return [sum((p[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)),Q(0)) for i in range(n+1)]
def halves(c):
 triangle=[c]
 while len(triangle[-1])>1:
  r=triangle[-1];triangle.append([(x+y)/2 for x,y in zip(r,r[1:])])
 return [r[0] for r in triangle],[r[-1] for r in triangle[::-1]]
def certify(poly,m2,maxdepth):
 pending=[(Q(0),Q(1),bern(affine(poly,Q(0),m2)),0)];leaves=[]
 while pending:
  l,r,c,d=pending.pop()
  if min(c)>0:leaves.append((l,r,c,d));continue
  assert d<maxdepth,(l,r,d)
  cl,cr=halves(c);mid=(l+r)/2
  pending.extend([(mid,r,cr,d+1),(l,mid,cl,d+1)])
 return leaves
def rational_endpoint(x,side,digits=20):
 endpoint=x.lower() if side=='lower' else x.upper();m,e=endpoint.man_exp();v=Q(int(m))*Q(2)**int(e)*10**digits
 i=v.numerator//v.denominator-1 if side=='lower' else -(-v.numerator//v.denominator)+1
 return Q(i,10**digits)
manifest=read('data/manifest.json')
for item in manifest:need('frozen '+item['local'],sha(B/item['local'])==item['sha256'])
pars=read('data/parameters.json');t2=read('source/T2_result.json');old=read('source/T4_462_result.json');rounding=read('data/rounding.json');review=(B/'source/T2_review.md').read_text()
need('review exact proof target',t2['inputs']['c1-t4/research/weight_uniform_gram_audit/PROOF.md']==sha(B/'source/T4_462_PROOF.md')=='3c871d7f9ef82ba6b6fb925cf73a31cda678805cadc2c8a91f9659b2e2f3030c')
need('review exact result target',t2['inputs']['c1-t4/research/weight_uniform_gram_audit/verification/result.json']==sha(B/'source/T4_462_result.json')=='61803920bea366913555ebb213ac40b466d370b1c92dd5cfe9cc9b67b9895450')
need('review exact parameters',t2['inputs']['c1-t4/research/weight_uniform_gram_audit/data/parameters.json']==sha(B/'data/parameters.json'))
need('review exact old checker',t2['inputs']['c1-t4/research/weight_uniform_gram_audit/code/check.py']==sha(B/'source/T4_462_check.py'))
need('review own WU3 binding',t2['inputs']['arith/h18_wu_sharp.py']==sha(B/'source/T2_WU3_check.py'))
need('review52 passed',t2['checks']==52 and t2['fails']==[] and 'checks: 52, failed: 0' in (B/'source/T2_check.log').read_text())
need('old320 passed',old['check_count']==320 and all(old['checks'].values()))
need('review COI and scope','Conflict of interest' in review and 'not independent evidence' in review and 'weight-dependent commutator' in review)
O,k,u=[Q(pars[key]) for key in ['O','K_lower','cU_lower']];eps=Q(rounding['epsilon']);half=Q(rounding['decimal_half_unit'])
need('exact relaxed constants',(O,k,u)==(Q(347,10),Q(39068,100),Q(15871,10000)))
need('lower constants remain lower',ar(k)<arb(old['K']).lower() and ar(u)<arb(old['v']).lower())
need('seven rows',len(pars['rows'])==len(t2['rows'])==len(old['rows'])==len(rounding['displays'])==7)
outputs=[]
for row,peer,original,display in zip(pars['rows'],t2['rows'],old['rows'],rounding['displays'],strict=True):
 name=row['label'];m2,m1,beta,bound=[Q(row[key]) for key in ['m2','m1','beta','bound']];mu=Q(peer['argmax_mu']);p=m2-mu;a=m1-mu;c=beta-mu
 need(name+' positive exact test point',0<mu<m2<m1 and beta>m2 and bound>0)
 need(name+' same row identities',name==peer['label']==original['label'] and bound==Q(peer['bound'])==Q(original['strict_L2_upper']))
 need(name+' global w1 side constraint inactive',2*O**2/(m2*m1)>2)
 need(name+' global w2 side constraint inactive',36*O**2/(beta*m2*m1*m1)>1)
 E=40*p+O**2;S=3*E+5*O*a;x=(2*E+5*O*a/3)/(p*a);y=(1440*p+(6*O+5*a)**2)/(c*p*a*a);z=p*a*x-E
 need(name+' equality point admissible',x>2 and y>1 and z==S/3 and z>0)
 need(name+' determinant exactly zero',y*c*z-(9*p*x*x+(30*O+25*a)*x-1000)==0)
 # Exact sample, with no numerical optimizer or peer runtime.
 q=4*mu**3*c*p*a*a/(27*k*u*u*(1440*p+(6*O+5*a)**2));ceiling=q*(1+2*eps)
 need(name+' positive sample lower bound',0<q<ceiling<bound**2)
 pp=[m2,-Q(1)];aa=[m1,-Q(1)];cc=[beta,-Q(1)]
 den=scale(add(scale(pp,1440),mul(add([6*O],scale(aa,5)),add([6*O],scale(aa,5)))),27*k*u*u)
 numerator=scale(mul([0,0,0,Q(1)],mul(cc,mul(pp,mul(aa,aa)))),4)
 poly=add(scale(den,ceiling),scale(numerator,-1));need(name+' exact degree7',len(poly)==8 and poly[-1]!=0)
 leaves=certify(poly,m2,rounding['max_depth']);need(name+' partition ends',leaves[0][0]==0 and leaves[-1][1]==1)
 for j,(left,right,coeff,depth) in enumerate(leaves):
  tag=name+' leaf'+str(j)
  need(tag+' positive',left<right and all(x>0 for x in coeff))
  need(tag+' independent affine recomposition',coeff==bern(affine(poly,m2*left,m2*(right-left))))
  if j:need(tag+' contiguous',leaves[j-1][1]==left)
 d=Q(display);need(name+' exact six digit rounding cell',0<d-half and (d-half)**2<q and ceiling<(d+half)**2)
 need(name+' original gain and distance factors unchanged',Q(row['gain'])==Q(original['gain_upper']) and Q(row['factor'])==Q(original['007_distance_factor_lower']))
 lower=ar(q).sqrt();upper=ar(ceiling).sqrt();lo=rational_endpoint(lower,'lower');hi=rational_endpoint(upper,'upper')
 need(name+' outward exact lower',ar(lo)<lower.lower());need(name+' outward exact upper',upper.upper()<ar(hi))
 need(name+' relative sqrt enclosure',1+2*eps<(1+eps)**2)
 # Source decimal witness is a display; record point comparison, never use as a premise.
 printed=Q(peer['sup_lower_witness']);cmp='above exact saved-decimal-point value' if printed**2>q else 'below or equal exact saved-decimal-point value'
 outputs.append({'label':name,'m2':str(m2),'m1':str(m1),'beta':str(beta),'exact_test_mu':str(mu),'exact_f_at_test_mu':str(q),'exact_supremum_square_upper':str(ceiling),'sqrt_supremum_strict_outer_lower':str(lo),'sqrt_supremum_strict_outer_upper':str(hi),'sqrt_lower_ball':lower.str(80),'sqrt_upper_ball':upper.str(80),'six_digit_rounded_display':display,'w1_at_test_mu':str(x),'w2_at_test_mu':str(y),'polynomial_power_mu':[str(v) for v in poly],'leaf_count':len(leaves),'max_depth':max(v[3] for v in leaves),'leaves':[{'t_interval':[str(l),str(r)],'coefficients':[str(v) for v in coeff],'depth':dep} for l,r,coeff,dep in leaves],'peer_printed_witness_comparison':cmp,'peer_display_is_used_as_bound':False})
for item in manifest:need('unchanged '+item['local'],sha(B/item['local'])==item['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'review_sha256':sha(B/'source/T2_review.md'),'rows':outputs,'foreign_code_executed':False,'optimizer_executed':False,'new_field_integrals':False,'verdict':'CONFIRMED reciprocal exact weight elimination, equality constraints and seven relaxed-budget supremum intervals; unchanged original necessary ceilings. No full analytic-scheme sharpness or new inverse/existence claim.'}
with (B/'verification/result.json').open('x') as stream:json.dump(out,stream,indent=2);stream.write('\n')
print('PASS',len(checks),'checks',out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'))
for row in outputs:print(row['label'],row['six_digit_rounded_display'],'leaves',row['leaf_count'],'depth',row['max_depth'],'interval',row['sqrt_supremum_strict_outer_lower'],row['sqrt_supremum_strict_outer_upper'])
