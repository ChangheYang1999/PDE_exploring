"""Exact independent algebra checks; no ODE or global proof certificate."""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
checks=0

def eq(x,y):
 global checks
 assert x==y,(x,y)
 checks+=1

for ell in [Q(6,5),Q(3,2),Q(2),Q(3),Q(9,2)]:
 D=ell-1
 for n in range(8):
  alpha=2*n+Q(3,2); a=4*(ell+1)*alpha; M=a/4-D; L0=(ell+1)/2
  eq(M-L0,2+2*n*(ell+1))
  eq(4*(alpha+2)-4*(ell+1)+2*D*alpha,a/2-4*D)
  eq(4*alpha*(ell+1),a)
  eq(-(4*(alpha+2))/alpha+6*(ell+1)-2*D-4*(ell+1),-8/alpha)
  for g2 in [Q(1,13),Q(2,7)]:
   A=2*ell-1; den=4*(ell+1)-a
   b=24*g2/den; e=4*g2*(a-2*A)/den
   eq(b-e,4*g2); eq(6*e,(a-2*A)*b)
   q1=(3*e-11*b)/48; q2=-(5*b+3*e)/48
   r21=2*A*b+3*a*q1; r03=2*e+a*q2
   eq(r21+3*r03,0)
   eq((r21-r03)/4,g2*(a*a-(4*ell+20)*a+64*(2*ell-1))/(4*den))
  eq((14*(ell+1))**2-(4*ell+20)*14*(ell+1)+64*(2*ell-1),140*ell*ell+184*ell-148)
  if n>=1:
   assert a*a-(4*ell+20)*a+64*(2*ell-1)>0; checks+=1
  for j in range(1,5):
   f=Q(j,3); fd=Q(j-2,5); g=Q(2*j,7); gd=Q(j-1,11); T=Q(j+2,3); J=Q(j,13); K=Q(j,17)
   Z2=(T-J)/2; Z4=-K/2; Z2d=(-g-f+4*J)/2; Z4d=(-g+6*K)/2
   direct=D*f+ell*fd+Z2*(f+fd)+(2*Z2+Z2d)*f/2-Z2*(g+gd)-3*(2*Z2+Z2d)*g/2+2*Z4*(g+gd)+3*(2*Z4+Z4d)*g/2
   L=ell+(T-J)/2
   N=f*f/4-(D+T)*f-f*g/2+(2*T+J-2*K)*g+((T-J)/2+K)*gd
   eq(direct,L*fd-N)
for beta in [Q(j,100) for j in range(1,26)]:
 eq(2-beta-(2+2*beta)*beta/(3-beta),(6-7*beta-beta*beta)/(3-beta))
 assert (6-7*beta-beta*beta)/(3-beta)>0; checks+=1
 eq(Q(1,6)/(1-beta/3),1/(6-2*beta))
p=Path('research/projected_unbounded_slopes_audit/PROOF.md')
out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'verdict':'PASS','proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Exact supporting Fourier, first-variation and cubic identities; global ODE construction checked in informal proof, not certified by this code.'}
Path('research/projected_unbounded_slopes_audit/verification/exact_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
