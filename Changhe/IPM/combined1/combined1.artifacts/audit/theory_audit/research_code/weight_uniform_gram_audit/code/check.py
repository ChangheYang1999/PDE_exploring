"""Independent exact AM-GM elimination and Bernstein certificates for WU3."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as Q
from math import comb
import json, time
from flint import arb, ctx
import sympy as sp
B=Path(__file__).resolve().parents[1]
ctx.prec=1024
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
read=lambda rel:json.loads((B/rel).read_text())
def A(x):
 x=Q(x);return arb(x.numerator)/arb(x.denominator)
def add(*polys):
 out=[Q(0)]*max(map(len,polys))
 for p in polys:
  for i,v in enumerate(p):out[i]+=v
 return out
def mul(p,q):
 out=[Q(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out
def scale(p,c):return [v*c for v in p]
def affine(poly,a,b):
 out=[Q(0)]*len(poly)
 for j,x in enumerate(poly):
  for i in range(j+1):out[i]+=x*comb(j,i)*a**(j-i)*b**i
 return out
def bernstein(power):
 n=len(power)-1
 return [sum((power[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)),Q(0)) for i in range(n+1)]
def split(coeff):
 triangle=[coeff]
 while len(triangle[-1])>1:
  row=triangle[-1];triangle.append([(a+b)/2 for a,b in zip(row,row[1:])])
 return [r[0] for r in triangle],[r[-1] for r in triangle[::-1]]
def main():
 start=time.monotonic();started=now();checks={}
 def check(label,truth):
  assert label not in checks,label
  assert bool(truth),label
  checks[label]=True
 manifest=read('data/manifest.json')
 for z in manifest:check('binding:'+z['local'],sha(B/z['local'])==z['sha256'])
 params=read('data/parameters.json');O,k,u,sigma=[Q(params[x]) for x in ['O','K_lower','cU_lower','sigma']]
 check('seven_rows',len(params['rows'])==7)
 # Verify the full determinant and square completion symbolically.
 p,a,c,x,y,o,z=sp.symbols('p a c x y o z')
 E=40*p+o**2;zz=p*a*x-E
 mat=sp.Matrix([[p,-o,-5],[-o,a*x-40,-3*x],[-5,-3*x,c*y]])
 numer=9*p*x*x+(30*o+25*a)*x-1000
 check('symbolic_determinant_identity',sp.expand(mat.det()-c*y*zz+numer)==0)
 after=sp.expand((numer*p*a*a).subs(x,(z+E)/(p*a)))
 desired=9*z*z+(18*E+30*o*a+25*a*a)*z+(3*E+5*o*a)**2
 check('symbolic_square_completion',sp.cancel(after-desired)==0)
 minnum=18*E+30*o*a+25*a*a+6*(3*E+5*o*a)
 check('symbolic_AMGM_minimum',sp.expand(minnum-1440*p-(6*o+5*a)**2)==0)
 check('cross_coefficient_1041',30*O==1041)
 # Rebuild the unchanged uniform kernel and rough constants.
 pi=arb.pi();ss=A(sigma);M=pi.sqrt()*((1-ss)/2).gamma()/2
 W=8*arb(5).sqrt()*arb(6)**(-arb(3)/5)/5
 k1=M+arb(8)/5;cr=3*M/2+arb(32)/15
 c8=1+3*pi*W/4;dtop=1+pi*W/2
 K=2*dtop+6*c8+24*(cr+2*k1)+32*k1
 q0=1/(2*pi.sqrt());ps=arb(2)**ss*(1+ss).sqrt()/(2*pi.sqrt())
 P0=ps*(1+W*M*ss)+W*M*ss/(2*pi.sqrt())
 v=arb(4)/5*q0+q0*(1+4*W*M*ss)+arb(19)/5*P0
 check('K_lower_outward',K>A(k));check('rough_lower_outward',v>A(u))
 check('positive_kappa_coefficients',arb(2).log()>arb(1)/2 and 3*arb(2).log()>2)
 c0=Q(params['c0']);check('snapshot_c0_in_A',Q(9,5)<c0<Q(37,20))
 fam={r['name']:r for r in read('source/T4_family_parameters.json')['rows']}
 peer=read('source/T2_WU3_result.json');bl=read('source/T2_betacap_result.json')
 d007=Q(params['d007']);oldmin=Q(params['old_H18_minimum']);common=Q(params['common_H18_floor'])
 own7=read('source/T4_007_n7.json')
 check('d007_exact_source',d007==Q(own7['strict_lower_exact']))
 check('d007_strict_root',0<A(d007)<arb(own7['radius']))
 outputs=[]
 for row_index,row in enumerate(params['rows']):
  label=row['label'];pre=label+':'
  m2,m1,beta,bnd,gain,factor=[Q(row[x]) for x in ['m2','m1','beta','bound','gain','factor']]
  check(pre+'positive_ordered_parameters',0<m2<m1 and beta>m2 and bnd>0)
  pp=[m2,-Q(1)];aa=[m1,-Q(1)];cc=[beta,-Q(1)]
  den=add(scale(pp,1440),mul(add([6*O],scale(aa,5)),add([6*O],scale(aa,5))))
  numer=scale(mul([0,0,0,1],mul(cc,mul(pp,mul(aa,aa)))),4)
  poly=add(scale(den,27*k*u*u*bnd*bnd),scale(numer,-1))
  check(pre+'degree_seven',len(poly)==8 and poly[-1]!=0)
  initial=bernstein(affine(poly,Q(0),m2))
  stack=[(Q(0),Q(1),initial,0)];leaves=[];maxdepth=0
  while stack:
   l,r,coeff,depth=stack.pop();maxdepth=max(maxdepth,depth)
   if min(coeff)>0:
    leaves.append((l,r,coeff,depth));continue
   assert depth<params['max_bernstein_depth'],(label,'no Bernstein proof at depth',depth,l,r)
   left,right=split(coeff);mid=(l+r)/2
   stack.append((mid,r,right,depth+1));stack.append((l,mid,left,depth+1))
  check(pre+'partition_endpoints',leaves[0][0]==0 and leaves[-1][1]==1)
  for j,(l,r,coeff,depth) in enumerate(leaves):
   check(pre+f'leaf_{j}_strict_positive',l<r and all(vv>0 for vv in coeff))
   check(pre+f'leaf_{j}_independent_affine_recomposition',coeff==bernstein(affine(poly,m2*l,m2*(r-l))))
   if j:check(pre+f'leaf_{j}_contiguous',leaves[j-1][1]==l)
  ff=fam[row['family']]
  fsquared=4*Q(ff['mu'])**3/(27*Q(ff['C'])*Q(ff['cU'])**2*Q(ff['sqrtW2'])**2)
  check(pre+'gain_upper_exact',bnd*bnd<gain*gain*fsquared)
  check(pre+'007_factor_lower_exact',d007>factor*bnd)
  if 'old_bound' in row:check(pre+'implies_old_WU_bound',bnd<Q(row['old_bound']))
  if 'old_H18_factor' in row:
   check(pre+'old_H18_factor_exact',oldmin>Q(row['old_H18_factor'])*bnd)
   check(pre+'common_H18_factor_exceeds_243',common>243*bnd)
  pr=peer['rows'][row_index] if row_index<5 else bl['rows'][row_index-5]
  check(pre+'T2_claim_bound',bnd==Q(pr['Bstar3_upper']))
  check(pre+'T2_claim_factor',factor==Q(pr['factor_007_lower']))
  gainkey='over_registered_'+row['family']+'_upper'
  check(pre+'T2_claim_gain',gain==Q(pr[gainkey]))
  if row_index>=5:check(pre+'T2_claim_beta',beta==Q(pr['beta']))
  outputs.append({'label':label,'m2':str(m2),'m1':str(m1),'beta':str(beta),'strict_L2_upper':str(bnd),'polynomial_power_mu':[str(q) for q in poly],
                  'leaf_count':len(leaves),'max_depth':maxdepth,'minimum_Bernstein_coefficient':str(min(vv for _,_,coeff,_ in leaves for vv in coeff)),
                  'leaves':[{'t_interval':[str(l),str(r)],'Bernstein_coefficients':[str(q) for q in coeff],'depth':depth} for l,r,coeff,depth in leaves],
                  'registered_family_squared':str(fsquared),'gain_upper':str(gain),'007_distance_factor_lower':str(factor)})
 check('bL_c0_beta_identity',Q(params['rows'][5]['beta'])==1+c0)
 check('bL_A_cap_identity',Q(params['rows'][6]['beta'])==Q(57,20))
 # Bind and recheck the accepted H18 finite inequalities exactly.
 h18=read('source/T4_H18_result.json');review=read('source/T2_review_459_result.json')
 check('H18_review_proof_target',review['inputs']['c1-t4/research/h18_coverage_audit/PROOF.md']==sha(B/'source/T4_H18_PROOF.md'))
 check('H18_review_result_target',review['inputs']['c1-t4/research/h18_coverage_audit/verification/result.json']==sha(B/'source/T4_H18_result.json'))
 check('H18_review_checks',review['checks']==189 and review['fails']==[])
 hr=h18['weak_candidates'];check('H18_exact_24_ids',[r['number'] for r in hr]==[i for i in range(2,27) if i!=11])
 for rr in hr:
  pre='H18_'+str(rr['number'])+':'
  I,D,H=[Q(rr[x]) for x in ['I_lower_exact','D_upper_exact','H_upper_exact']]
  gap=I-D*common-H*common*common
  check(pre+'strict_common_floor',I>0 and D>0 and H>0 and gap>0)
  check(pre+'gap_identity',gap==Q(rr['positive_gap_exact']))
  check(pre+'old_H18_minimum_valid',I-D*oldmin-H*oldmin*oldmin>0)
 for z in manifest:check('unchanged:'+z['local'],sha(B/z['local'])==z['sha256'])
 result={'started_utc':started,'finished_utc':now(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,
         'K':K.str(100),'v':v.str(100),'rows':outputs,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),
         'foreign_code_executed':False,'new_field_integrals':False,'verdict':'CONFIRMED all seven necessary ceilings under stated fixed floors and uniform constants; exact weight elimination and bL extension. Actual full-scheme sharpness remains OPEN.'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['finished_utc'],'checks',len(checks),'seconds',result['elapsed_seconds'],'sha',sha(B/'verification/result.json'))
 for r in outputs:print(r['label'],r['strict_L2_upper'],'leaves',r['leaf_count'],'depth',r['max_depth'])
if __name__=='__main__':main()
