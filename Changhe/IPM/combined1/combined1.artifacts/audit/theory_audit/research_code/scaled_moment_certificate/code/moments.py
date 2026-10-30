"""Finite geometric partition, exact Taylor coefficients, explicit Cauchy remainder."""
from flint import fmpq as Q,fmpq_poly as P,arb
from hashlib import sha256
RHO=Q(3,2)
def ar(q):return arb(q.numerator)/q.denominator
def power(q,e):
 assert q>0
 return ar(q)**ar(e)
def factor_series(q,e,N):
 result=[Q(1)]
 for k in range(N):result.append(result[-1]*(e-k)*q/(k+1))
 return P(result)
def integral(alpha,beta,factors,N):
 assert alpha>-1 and beta>-1 and N>=0
 assert all(0<=z<1 for z,nu in factors)
 J=2
 while any(Q(1,2**J)>1-z for z,nu in factors):J+=1
 nodes=[Q(0)]+[1-Q(1,2**k) for k in range(1,J+1)]+[Q(1)]
 total=arb(0);details=[]
 for index,(left,right) in enumerate(zip(nodes,nodes[1:])):
  h=right-left;first=index==0;last=index==len(nodes)-2
  a=alpha if first else Q(0);b=beta if last else Q(0)
  C=ar(h)*power(h if first else left,alpha)*power(h if last else 1-left,beta)
  analytic=[]
  if not first:analytic.append((h/left,alpha))
  if not last:analytic.append((-h/(1-left),beta))
  for z,nu in factors:
   base=1-z*left;C*=power(base,-nu);analytic.append((-z*h/base,-nu))
  analytic=[(q,e) for q,e in analytic if q and e]
  assert all(abs(q)<=Q(1,2) for q,e in analytic)
  poly=P([1]);M=arb(1)
  for q,e in analytic:
   poly=P(list(poly*factor_series(q,e,N))[:N+1]);M*=power(1-RHO*abs(q),-abs(e))
  center=Q(0);mu=1/(b+1)
  for k,coefficient in enumerate(poly):
   if b==0:mu=1/(a+k+1)
   elif k:mu*=Q(k)/(b+k+1)
   center+=coefficient*mu
  mu0=1/(a+1) if b==0 else 1/(b+1)
  E=C*M*ar(RHO**(-N-1)/(1-1/RHO)*mu0)
  exact_radius=E.upper().fmpq()
  enclosure=C*ar(center)+arb(0,str(exact_radius))
  total+=enclosure
  serialized='\n'.join(map(str,poly))+'\n'
  details.append({'interval':[str(left),str(right)],'analytic_factors':[[str(q),str(e)] for q,e in analytic],
                  'endpoint_exponents':[str(a),str(b)],'normalizer':C.str(60),'cauchy_M':M.str(60),
                  'exact_polynomial_integral':str(center),'polynomial_sha256':sha256(serialized.encode()).hexdigest(),
                  'error_upper_exact':str(exact_radius),'enclosure':enclosure.str(60)})
 return total,details
