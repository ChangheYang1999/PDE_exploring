"""Exact identities and independently evaluated sine-tail illustrations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
z=S.symbols('z',real=True); checks=[]
for n in range(8):
 T=sum((-1)**j*z**(2*j+1)/S.factorial(2*j+1)for j in range(n+1))
 Sn=S.sin(z)-T
 assert S.simplify(Sn.subs(z,0))==0 and S.simplify(S.diff(Sn,z).subs(z,0))==0
 if n:
  prev=S.sin(z)-sum((-1)**j*z**(2*j+1)/S.factorial(2*j+1)for j in range(n))
  assert S.simplify(S.diff(Sn,z,2)+prev)==0
 assert S.expand(S.series(Sn,z,0,2*n+5).removeO()).coeff(z,2*n+3)==(-1)**(n+1)/S.factorial(2*n+3)
 checks.append({'n':n,'recurrence_and_next_coefficient':'PASS'})
mp.mp.dps=50
pairs=[]
for mu in [mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4]:
 vals=[mp.quad(lambda t:mp.sin(t)*((t+2*n*mp.pi)**(-1-mu)-(t+(2*n+1)*mp.pi)**(-1-mu)),[0,mp.pi])for n in range(12)]
 assert all(v>0for v in vals)
 pairs.append({'mu':str(mu),'first_12_pair_sum':str(sum(vals)),'minimum_pair':str(min(vals)),'scope':'Finite quadrature illustration; full positivity proved in PROOF.md.'})
# Exact reversal identity in Laurent variable w=exp(i z).
w,ur,vi=S.symbols('w ur vi'); lhs=(ur+S.I*vi)*w+(-ur+S.I*vi)/w
rhs=2*S.I*(ur*(w-1/w)/(2*S.I)+vi*(w+1/w)/2)
assert S.expand(lhs-rhs)==0
for A in [S.Rational(3,2),S.Rational(2),S.Rational(7,3),S.Rational(11)]:
 for g in [S.Rational(1,3),S.Rational(2),S.Rational(7)]:
  q=2*(A-1); b=g/q; eta=q/A
  for n in range(6):assert S.simplify(eta*(b+n)-(g+n*q)/A)==0
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','sine_recurrences':checks,'positive_half_period_pairs':pairs,'exact_exponent_identities':72,'reality_pairing_identity':'PASS','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact symbolic checks and floating illustrative quadrature; theorem depends on complete informal proof.'}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
