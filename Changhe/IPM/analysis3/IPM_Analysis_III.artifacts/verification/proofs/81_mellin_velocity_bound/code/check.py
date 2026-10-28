from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
la,n,si,xi,theta,r=s.symbols('lambda n sigma xi theta r',real=True)
ii=s.I
ap=(la-n)/(la+n+2);am=(la+n)/(la-n+2)
z=si+ii*xi
assert s.simplify(ap.subs(la,z)-(ii*xi-n)/(ii*xi+n)-2*((si+1)*n-ii*xi)/((z+n+2)*(ii*xi+n)))==0
assert s.simplify(am.subs(la,z)-(ii*xi+n)/(ii*xi-n)+2*((si+1)*n+ii*xi)/((z-n+2)*(ii*xi-n)))==0
# Store each angular coefficient rather than relying on exponential simplification.
psi={n+1:-1/(2*(la+n+2)),n-1:-1/(2*(la-n+2))}
ux={};uy={};rhs={}
for m,c in psi.items():
 rhs[m]=s.factor(-c*((la+1)**2-m*m))
 ux[m+1]=ux.get(m+1,0)-c*(la+1-m)/(2*ii)
 ux[m-1]=ux.get(m-1,0)+c*(la+1+m)/(2*ii)
 uy[m+1]=uy.get(m+1,0)+c*(la+1-m)/2
 uy[m-1]=uy.get(m-1,0)+c*(la+1+m)/2
assert s.simplify(rhs[n+1]-(la-n)/2)==0 and s.simplify(rhs[n-1]-(la+n)/2)==0
assert s.simplify(ux[n+2]-ap/(4*ii))==0 and s.simplify(ux[n])==0 and s.simplify(ux[n-2]+am/(4*ii))==0
assert s.simplify(uy[n+2]+ap/4)==0 and s.simplify(uy[n]+s.Rational(1,2))==0 and s.simplify(uy[n-2]+am/4)==0
assert -s.Rational(17,2)+2==-s.Rational(13,2)
assert -s.Rational(13,4)+s.Rational(29,8)==s.Rational(3,8)
TOP=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','identities':'two multiplier differences; stream equation; velocity signs; radial isometry exponents','proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest()}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
