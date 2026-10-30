"""Cartesian origin projection; Leibniz density norm with all cross terms."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from math import comb, factorial
import importlib.util, json, sys, time
from flint import fmpq as Q, arb, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/taylor_repair_audit'
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('taylor_cartesian',ROOT/'research/constraint_rank/code/check.py');J=importlib.util.module_from_spec(spec);spec.loader.exec_module(J)
add,scale,mul,spow=J.add,J.scale,J.mul,J.spow
PAIRS=[(2,1),(0,3),(3,1),(1,3),(0,4)]
KEYS=[(0,0),(2,0),(0,2),(4,0),(2,2),(0,4)]
def qball(q):return arb(int(q.numerator))/arb(int(q.denominator))
def fall(q,n):
 v=Q(1)
 for i in range(n):v*=q-i
 return v
def monodiff(i,j,a,b):
 if a>i or b>j:return {}
 return {(i-a,j-b):Q(factorial(i)*factorial(j),factorial(i-a)*factorial(j-b))}
def monoshift(poly,i,j):return {(a+i,b+j):v for (a,b),v in poly.items()}
def derivative_numerator(i,j,q,ax,ay):
 out={}
 for a in range(ax+1):
  for b in range(ay+1):
   dm=monodiff(i,j,ax-a,ay-b)
   if not dm:continue
   for h in range(a//2+1):
    for k in range(b//2+1):
     factor=Q(comb(ax,a)*comb(ay,b)*factorial(a)*factorial(b)*2**(a+b-2*h-2*k),factorial(h)*factorial(k)*factorial(a-2*h)*factorial(b-2*k))*fall(q,a+b-h-k)
     ss=3-a-b+h+k;assert ss>=0
     power=add(*(scale(spow(z),Q(comb(ss,z))) for z in range(ss+1)))
     term=mul(monoshift(dm,a-2*h,b-2*k),power,20)
     out=add(out,scale(term,factor))
 return out

def density_numerator(pair,p):
 i,j=pair;l=i+j;q=p-l-2
 return scale(add(derivative_numerator(2*i,2*j,q,2,1),derivative_numerator(2*i,2*j,q,0,3)),-1)
def moment_over_pi(u,v,A):
 out=Q(1)
 for n in range(1,u+1):out*=Q(2*n-1,2)
 for n in range(1,v+1):out*=Q(2*n-1,2)
 for n in range(1,u+v+2):assert A-n>0;out/=A-n
 return out
def norm_over_pi(poly,A):
 out=Q(0)
 for (i,j),cf in mul(poly,poly,22).items():
  assert i%2==j%2==0
  out+=cf*moment_over_pi(i//2,j//2,A)
 assert out>0
 return out

def main():
 start=time.monotonic();ctx.prec=768
 files=[BASE/'PROOF.md',Path(__file__),ROOT/'research/constraint_rank/code/check.py',ROOT/'research/constraint_rank/verification/candidate007.json',ROOT/'research/basis_redundancy/source/canonical007.json']+list(sorted((BASE/'source').glob('T4_*')))
 hashes={str(p.relative_to(ROOT)):H(p) for p in files}
 peer=json.loads((BASE/'source/T4_result.json').read_text());pars=json.loads((BASE/'source/T4_parameters.json').read_text())
 assert peer['parameters_file_sha256']==H(BASE/'source/T4_parameters.json') and peer['proof_sha256']==H(BASE/'source/T4_PROOF.md') and peer['code_sha256']==H(BASE/'source/T4_check.py') and peer['jets_sha256']==H(BASE/'source/T4_jets.py')
 raw=json.loads((ROOT/'research/basis_redundancy/source/canonical007.json').read_text());old=json.loads((ROOT/'research/constraint_rank/verification/candidate007.json').read_text())
 assert pars['source_canonical_sha256']==H(ROOT/'research/basis_redundancy/source/canonical007.json')
 c=Q(raw['cl']);p=(3+1/c)/2;assert c==Q(4076476460239181,2251799813685248)>1
 coeff={tuple(map(int,k)):Q(v) for k,v in zip(raw['order'],raw['coefficients'])}
 chi=add(*(scale(J.monojet(*key,c),v) for key,v in coeff.items() if key[2]<=4))
 a=J.fields(chi)[0].get((0,1),Q(0));assert a==Q(old['a0_exact']) and 4*chi.get((2,2),Q(0))==1-c
 def values(ch):
  f=J.quotient(J.residual(ch,c));return [f.get(k,Q(0)) for k in KEYS]
 assert values(chi)==list(map(Q,old['Taylor_residual_exact']))
 eta=[]
 for i,j in PAIRS:
  l=i+j;M={(2*i,2*j):Q(1)}
  eta.append(add(*(scale(mul(M,spow(n)),J.binomial(p-l-2,n)) for n in range(5-l))))
 def project(ch):
  f=values(ch);alpha=-f[1]/(24*(a-4*c+2));beta=f[2]/240
  first=add(ch,scale(eta[0],alpha),scale(eta[1],beta));g=values(first);assert g[:3]==[0,0,0]
  gg=-g[3]/(60*(a-8*c+4));dd=g[4]/(480*c);ee=(g[5]+12*(a-4)*dd)/1344
  pars=[alpha,beta,gg,dd,ee];patched=add(ch,*(scale(e,t) for e,t in zip(eta,pars)))
  assert values(patched)==[0]*6
  return pars,patched,g
 ts,patched,mid=project(chi)
 assert project(patched)[0]==[0]*5
 assert J.fields(patched)[0].get((0,1),Q(0))==a and 4*patched.get((2,2),Q(0))==1-c
 assert [Q(x['coefficient']) for x in pars['parameters']]==ts and [tuple(x['pair']) for x in pars['parameters']]==PAIRS
 changes={}
 for t,pair in zip(ts,PAIRS):
  row=next(x for x in old['directions'] if (x['a'],x['b'])==pair)
  for entry in row['tail_polynomials']:
   m=int(entry['m']);poly=list(map(Q,entry['polynomial_coefficients']))
   assert sum(poly,Q(0))==0 and sum((w*z for w,z in enumerate(poly)),Q(0))==0
   for w,z in enumerate(poly):
    if z:key=(0,m,m+w);changes[key]=changes.get(key,Q(0))+t*z
 changes={k:v for k,v in changes.items() if v};assert set(changes)<=set(coeff)
 peerchanges={tuple(x['index']):Q(x['coefficient']) for x in pars['canonical_changes']};assert changes==peerchanges
 rebuilt=add(*(scale(J.monojet(*key,c),v+changes.get(key,Q(0))) for key,v in coeff.items() if key[2]<=4));assert rebuilt==patched
 # All individual H values use a Leibniz formula, not recursive D operators.
 hs=[density_numerator(pair,p) for pair in PAIRS];A=15-1/c
 assert all(all(i%2==0 and j%2==1 for i,j in hh) for hh in hs)
 norms=[];triangle=arb(0)
 for pair,t,hh,pr in zip(PAIRS,ts,hs,peer['direction_norms']):
  Ai=2*sum(pair)+7-1/c;val=norm_over_pi(hh,Ai);bb=(arb.pi()*qball(val)).sqrt();triangle+=qball(abs(t))*bb
  assert tuple(pr['pair'])==pair and val==Q(pr['squared_L2_over_pi']) and bb.overlaps(arb(pr['L2_ball']))
  norms.append({'pair':list(pair),'squared_L2_over_pi':str(val),'L2':bb.str(70)})
 big=add(*(scale(mul(hh,{(0,0):Q(1),(2,0):Q(1),(0,2):Q(1)},20) if sum(pair)==3 else hh,t) for pair,t,hh in zip(PAIRS,ts,hs)))
 exact=norm_over_pi(big,A);norm=(arb.pi()*qball(exact)).sqrt()
 assert norm<=triangle and triangle.overlaps(arb(peer['density_L2_upper_bound_ball']))
 e=Q(3423716897,10**21);assert norm<qball(e) and triangle<qball(e)
 d=Q(4769166867,10**12);transfer=d-e;assert transfer>Q(4769166863,10**12)
 small={'candidate_reference':'C1-N1-007-d2w-j7-e2bal','c':str(c),'parameters':[{'pair':list(pair),'coefficient':str(t)} for pair,t in zip(PAIRS,ts)],'canonical_changes':[{'index':list(k),'coefficient':str(v)} for k,v in sorted(changes.items())],'combined_density_squared_L2_over_pi':str(exact)}
 target=BASE/'verification/exact.json'
 with target.open('x') as f:json.dump(small,f,indent=2);f.write('\n')
 out={'utc':datetime.now(timezone.utc).isoformat(),'method':'Cartesian exact Taylor jets and direct Leibniz density numerators; all combined cross moments','inputs':hashes,'c':str(c),'checks':{'initial_Taylor_equal_N4_164':True,'five_parameters_equal_T4_211':True,'six_final_coefficients_zero':True,'a0_and_strain_preserved':True,'idempotence':True,'all_changed_tail_moments_zero':True,'canonical_changes_equal_T4':True,'canonical_reconstruction':True,'five_individual_norms_equal_T4':True,'triangle_enclosures_overlap':True,'combined_norm_below_triangle':True,'strict_upper_bound_verified':True},'parameter_balls':[qball(t).str(60) for t in ts],'intermediate_balls':[qball(x).str(60) for x in mid],'direction_norms':norms,'combined_density_L2':norm.str(85),'triangle_bound':triangle.str(85),'strict_density_L2_upper_exact':str(e),'inherited_reference_distance_lower_exact':str(d),'transferred_distance_lower_exact':str(transfer),'transferred_simple_lower_exact':str(Q(4769166863,10**12)),'exact_result_sha256':H(target),'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED independent T4-211 arithmetic; general theorem Opus review separate; combined sharper norm OPEN peer'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:out[k] for k in ['utc','checks','parameter_balls','combined_density_L2','triangle_bound','strict_density_L2_upper_exact','transferred_simple_lower_exact','elapsed_seconds','status']},indent=2),flush=True)
if __name__=='__main__':main()
