"""Exact constraint rank via six tail-free origin directions. No optimizer import."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
from collections import defaultdict
import importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, arb, ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/constraint_rank'
T=Poly([0,1]);KEYS=[(2,0),(0,2),(4,0),(2,2),(0,4)]
def H(p):return sha256(Path(p).read_bytes()).hexdigest()
def add(*rows):
 out={}
 for p in rows:
  for k,v in p.items():out[k]=out.get(k,Q(0))+v
 return {k:v for k,v in out.items() if v}
def scale(p,a):return {k:v*a for k,v in p.items() if v*a}
def mul(p,q,d=8):
 out={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():
   if i+j+k+l<=d:out[i+k,j+l]=out.get((i+k,j+l),Q(0))+a*b
 return {k:v for k,v in out.items() if v}
def diff(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   kk=list(k);kk[axis]-=1;out[tuple(kk)]=v*k[axis]
 return out
def dx(p):return diff(p,0)
def dy(p):return diff(p,1)
def spow(k):return {(2*i,2*(k-i)):Q(comb(k,i)) for i in range(k+1)}
def harmonic(m):return {(2*(m-j),2*j):Q((-1)**j*comb(2*m,2*j)) for j in range(m+1)}
def binomial(p,l):
 z=Q(1)
 for j in range(l):z=z*(p-j)/(j+1)
 return z
def monojet(j,m,k,c):
 if k>4:return {}
 p=(3+1/c-j*(1-1/c))/2
 return add(*(scale(mul(harmonic(m),spow(k-m+l)),binomial(p-k,l)) for l in range(5-k)))
def fields(p):
 rho=scale(dy(add(dx(dx(p)),dy(dy(p)))),-1)
 return rho,scale(dx(dy(dy(p))),-1),dx(dx(dy(p)))
def residual(p,c):
 rho,u,v=fields(p);wx=add({(1,0):c},u);wy=add({(0,1):c},v)
 return add(mul(wx,dx(rho),5),mul(wy,dy(rho),5),scale(rho,-1))
def linearized(base,pert,c):
 rho,u,v=fields(base);h,hu,hv=fields(pert)
 return add(mul(add({(1,0):c},u),dx(h),5),mul(add({(0,1):c},v),dy(h),5),mul(hu,dx(rho),5),mul(hv,dy(rho),5),scale(h,-1))
def quotient(p):
 assert all(j>=1 for i,j in p)
 return {(i,j-1):v for (i,j),v in p.items()}
def leg(n):
 a,b=Poly([1]),2*T-1
 if n==0:return a
 for k in range(1,n):a,b=b,((2*k+1)*(2*T-1)*b-k*a)/(k+1)
 return b
def gp(g):
 s=g['spec'];return T**int(s[1]) if s[0]=='mono' else T**int(s[1])*leg(int(s[2]))
def aq(q):return arb(int(q.numerator))/arb(int(q.denominator))
def frozen_peer():
 path=BASE/'source/N1_ipm_origin.py';spec=importlib.util.spec_from_file_location('constraint_rank_peer',path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def main():
 start=time.monotonic();ctx.prec=768
 mp=BASE/'source/MANIFEST.json';manifest=json.loads(mp.read_text())
 for p,h in manifest['files'].items():assert H(ROOT/p)==h
 src=ROOT/'research/basis_redundancy/source/candidate007.json';canpath=ROOT/'research/basis_redundancy/source/canonical007.json'
 raw=json.loads(src.read_text());can=json.loads(canpath.read_text());c=Q(can['cl']);p0=(3+1/c)/2
 assert c==Q(4076476460239181,2251799813685248) and c>0
 br=json.loads((ROOT/'research/basis_redundancy/verification/candidate007.json').read_text())
 assert br['potential_space_dimension']==1922 and br['exact_zero_potential_dimension']==1060
 gens=raw['generators'];groups=defaultdict(list)
 for i,g in enumerate(gens):groups[int(g['j']),int(g['m'])].append(i)
 assert len(groups)==360 and len([k for k in groups if k[0] in [0,1,2]])==60
 tail=[]
 for (j,m),ids in sorted(groups.items()):
  pj=(3+1/c-j*(1-1/c))/2;rows=[]
  for i in ids:
   p=gp(gens[i]);rows.append((i,p(1),(pj-m)*p(1)-p.derivative()(1)))
  first=next(r for r in rows if r[1]);assert all(r[1]==1 for r in rows)
  if j in [0,1,2]:
   second=next(r for r in rows if first[1]*r[2]-first[2]*r[1]);det=first[1]*second[2]-first[2]*second[1];indices=[first[0],second[0]]
  else:det=first[1];indices=[first[0]]
  tail.append({'j':j,'m':m,'rows':2 if j in [0,1,2] else 1,'witness_indices':indices,'imposed_moment_determinant':str(det)})
 assert sum(r['rows'] for r in tail)==420
 # Exact canonical Taylor polynomial, independent of the stored a0 and strain.
 chi={};terms=[];coefs=[]
 for key,cf in zip(can['order'],can['coefficients']):
  j,m,k=map(int,key)
  if k>4:continue
  q=Q(cf);chi=add(chi,scale(monojet(j,m,k,c),q));terms.append({'m':m,'k':k,'p':str((3+1/c-j*(1-1/c))/2)});coefs.append(str(q))
 rho,_,_=fields(chi);a0=rho.get((0,1),Q(0));strain=4*chi.get((2,2),Q(0))
 assert a0==Q(can['a0']) and strain==Q(can['strain'])==1-c
 factors=[a0-4*c+2,a0-8*c+4];assert all(z!=0 for z in factors)
 rf=quotient(residual(chi,c));taylor=[rf.get(k,Q(0)) for k in [(0,0)]+KEYS]
 # Independent copied origin-jet path only; no torch or floating optimizer.
 peer=frozen_peer();from gmpy2 import mpq
 peerterms=[dict(m=t['m'],k=t['k'],p=mpq(t['p'])) for t in terms]
 oj=peer.OriginJets(peerterms,degmax=4,exact=True);pc=[mpq(x) for x in coefs]
 assert Q(str(oj.a0(pc)))==a0
 assert sum((Q(str(v))*Q(q) for v,q in zip(oj.strains(),coefs)),Q(0))==strain
 assert [Q(str(x)) for x in oj.Rf_coeffs(mpq(str(c)),pc)]==taylor
 directions=[];columns=[]
 for a,b in [(1,1),(2,1),(0,3),(3,1),(1,3),(0,4)]:
  l=a+b;M={(2*a,2*b):Q(1)}
  eta=add(*(scale(mul(M,spow(q)),binomial(p0-l-2,q)) for q in range(5-l)))
  # Independent angular decomposition and exact membership in j=0 blocks.
  basis=[mul(harmonic(m),spow(l-m),2*l) for m in range(l+1)]
  mat=Mat([[basis[m].get((2*i,2*(l-i)),Q(0)) for m in range(l+1)] for i in range(l+1)])
  rhs=Mat([[Q(i==a)] for i in range(l+1)]);weights=mat.inv()*rhs
  assert add(*(scale(basis[m],weights[m,0]) for m in range(l+1)))==M
  eta2={};dterms=[];dcoefs=[];membership=[]
  for m in range(l+1):
   q=weights[m,0]
   if not q:continue
   pol=q*T**(l-m)*(1-T)**2
   assert pol(1)==0 and pol.derivative()(1)==0
   monodegrees={int(gens[i]['spec'][1]) for i in groups[0,m] if gens[i]['spec'][0]=='mono'}
   assert {i for i,z in enumerate(pol) if z}<=monodegrees
   membership.append({'m':m,'polynomial_coefficients':[str(z) for z in pol]})
   for w,z in enumerate(pol):
    if not z:continue
    k=m+w;eta2=add(eta2,scale(monojet(0,m,k,c),z));dterms.append({'m':m,'k':k,'p':mpq(str(p0))});dcoefs.append(mpq(str(z)))
  assert eta==eta2
  drf=quotient(linearized(chi,eta,c));column=[4*eta.get((2,2),Q(0))]+[drf.get(k,Q(0)) for k in KEYS];columns.append(column)
  # Centered exact differences of the quadratic residual give its differential.
  plus=quotient(residual(add(chi,eta),c));minus=quotient(residual(add(chi,scale(eta,-1)),c))
  assert all((plus.get(k,Q(0))-minus.get(k,Q(0)))/2==drf.get(k,Q(0)) for k in [(0,0)]+KEYS)
  aug=peer.OriginJets(peerterms+dterms,degmax=4,exact=True);values=aug.Rf_coeffs_jacobian(mpq(str(c)),pc+[mpq(0)]*len(dterms))
  peercol=[sum((Q(str(v[row]))*Q(str(cf)) for v,cf in zip(values[len(terms):],dcoefs)),Q(0)) for row in range(1,6)]
  assert peercol==column[1:]
  directions.append({'a':a,'b':b,'tail_polynomials':membership,'strain':str(column[0]),'Taylor_differential':[str(x) for x in column[1:]],'independent_peer_jacobian_agrees':True,'exact_centered_difference_agrees':True})
 matrix=Mat([[columns[j][i] for j in range(6)] for i in range(6)])
 determinant=matrix.det();formula=Q(4*24*(-240)*60*(-480)*(-1344))*c*factors[0]*factors[1]
 assert determinant==formula and determinant!=0
 assert [columns[j][0] for j in range(6)]==[Q(4),Q(0),Q(0),Q(0),Q(0),Q(0)]
 assert columns[1][1:3]==[24*factors[0],Q(0)] and columns[2][1:3]==[Q(0),Q(-240)]
 assert columns[3][1:]==[Q(0),Q(0),60*factors[1],Q(0),Q(0)]
 assert columns[4][1:]==[Q(0),Q(0),Q(0),-480*c,12*(a0-4)]
 assert columns[5][1:]==[Q(0),Q(0),Q(0),Q(0),Q(-1344)]
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007-d2w-j7-e2bal','tail_rank':420,'linear_constraint_rank':421,'Taylor_additional_rank':5,'full_constraint_rank':426,'potential_dimension':1922,'constrained_potential_tangent_dimension':1496,'generator_dimension':2982,'constrained_generator_tangent_dimension':2556,'zero_potential_dimension':1060,'a0_ball':aq(a0).str(80),'nonzero_factors':[aq(z).str(80) for z in factors],'determinant_ball':aq(determinant).str(80),'a0_exact':str(a0),'strain_exact':str(strain),'Taylor_residual_exact':[str(x) for x in taylor],'five_Taylor_equations_exact':all(x==0 for x in taylor[1:]),'all_six_Taylor_coefficients_exact_zero':all(x==0 for x in taylor),'linear_right_sides_scope':'Center checked. All prescribed tail targets not rechecked here; do not infer affine feasibility solely from rank.','tail_witnesses':tail,'directions':directions,'determinant_exact':str(determinant),'manifest_sha256':H(mp),'code_sha256':H(__file__),'proof_sha256':H(BASE/'PROOF.md'),'elapsed_seconds':time.monotonic()-start,'status':'OPEN peer: exact constraint rank, not residual Jacobian rank or conditioning'}
 with (BASE/'verification/candidate007.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:out[k] for k in ['utc','tail_rank','linear_constraint_rank','full_constraint_rank','constrained_potential_tangent_dimension','constrained_generator_tangent_dimension','a0_ball','nonzero_factors','determinant_ball','five_Taylor_equations_exact','elapsed_seconds','status']},indent=2),flush=True)
if __name__=='__main__':main()
