"""Finite identities for the fractional-ball universal velocity obstruction."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib, json, time
import sympy as S
from flint import arb, ctx
B=Path(__file__).resolve().parents[1]
start=time.monotonic();ctx.prec=512
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==manifest['proof_sha256']
assert sha(B/'data/parameters.json')==manifest['parameters_sha256']
for name,row in manifest['inputs'].items():assert sha(B/'source'/name)==row['sha256']
p=json.loads((B/'data/parameters.json').read_text())
checks=[]
def identity(name,expr):
    assert S.simplify(expr)==0,(name,expr)
    checks.append(name)
y1,y2,z1,z2=S.symbols('y1 y2 z1 z2',real=True)
y2n=y1*y1+y2*y2;z2n=z1*z1+z2*z2
identity('weight moderate inequality sum of squares',
  2*(1+4*y2n)*(1+4*z2n)-(1+4*((y1+z1)**2+(y2+z2)**2))
  -(1+4*((y1-z1)**2+(y2-z2)**2)+32*y2n*z2n))
t11,t12,t21,t22=S.symbols('t11 t12 t21 t22',real=True)
identity('trace contraction squared gap',
  2*(t11*t11+t12*t12+t21*t21+t22*t22)-(t11+t22)**2
  -((t11-t22)**2+2*(t12*t12+t21*t21)))
t,u=S.symbols('t u',positive=True)
r=2*S.sqrt(t*u)
identity('Gaussian radial moment substitution',
 r**S.Rational(4,5)*r/(2*t)*S.exp(-r*r/(4*t))*S.diff(r,u)
 -(4*t)**S.Rational(2,5)*u**S.Rational(2,5)*S.exp(-u))
identity('weight and Gaussian moment factors',
 4**S.Rational(2,5)*4**S.Rational(2,5)-16**S.Rational(2,5))
a,k=S.symbols('a k',real=True)
identity('weighted derivative relative exponent',
 (1-a-k+S.Rational(4,5))-(1-a)-(S.Rational(4,5)-k))
identity('second derivative decay gain',S.Rational(4,5)-2+S.Rational(6,5))
identity('fourth derivative decay gain',S.Rational(4,5)-4+S.Rational(16,5))
ss=S.symbols('s',real=True);lam=S.symbols('lambda',positive=True)
identity('Bessel multiplier factorization',S.powsimp(lam**(-(2-ss)/2)*lam-lam**(ss/2)))
c=Fraction(p['c']);q=1/c-4;av=-q;sv=Fraction(p['s']);al=2-sv
assert 3<av<5 and 0<sv<2
assert 1-av<0 and -av-1<0
checks.extend(['campaign q and fractional domain','strict decay of both sequence terms'])
def ar(v):
 v=Fraction(v);return arb(v.numerator)/v.denominator
alA=ar(al);aa=ar(av)
Cs=arb(2)**ar('2/5')*(1+arb(16)**ar('2/5')*ar('7/5').gamma()*(alA/2+ar('2/5')).gamma()/(alA/2).gamma())
E=(aa-1)/(2*aa*(aa-3))
assert Cs>0 and Cs.is_finite() and E>ar('785064/1000000')
checks.extend(['weighted Bessel constant finite and positive','universal E exceeds fixed sharpw critical bound'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,
 'proof_sha256':manifest['proof_sha256'],'manifest_sha256':sha(B/'data/manifest.json'),
 'checker_sha256':sha(Path(__file__)),'checks':checks,'check_count':len(checks),'alpha':str(al),'a':str(av),
 'C_s_upper_formula_value':Cs.str(80),'Etest':E.str(80),
 'finite_radius_witness_computed':False,'foreign_code_executed':False,
 'status':'PASS finite identities; full analytic theorem OPEN independent review'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
