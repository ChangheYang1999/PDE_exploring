"""Manufactured tests for result96; intended for the sole serial CPU worker."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
import mpmath as mp
from q_canonical_high_jets import solve,product,scale,add,angular_poly
from q_exact_jets import jets
from q_high_precision_density import MPQDensity
mp.mp.dps=85
checks=[]
def check(name,ok,**values):
    assert ok,(name,values)
    checks.append(dict(name=name,**values))
def mf(v):return mp.mpf(v.numerator)/v.denominator
for kap in [F(3,2),F(5,3),F(2)]:
 for coeff in [[[F(3),F(-1,5),F(2,7)]],[[F(3),F(1,7)],[F(-2,3),F(1,11)],[F(1,9)],[F(-2,7)],[F(3,8)],[F(1,13)]]]:
    ell=F(5,2);z=solve(coeff,kap,ell,3);old=jets(coeff,kap,ell)
    for name,a,b in [('a',z['a'],old['a']),('c',z['c'],old['c']),('b',z['rho'].get((2,1),F(0)),old['b_core']),('e',z['rho'].get((0,3),F(0)),old['e_core']),('q1',z['psi'].get((3,1),F(0)),old['q1_core']),('q2',z['psi'].get((1,3),F(0)),old['q2_core']),('R21',z['R'].get((2,1),F(0)),old['actual_R_x2y_core']),('R03',z['R'].get((0,3),F(0)),old['actual_R_y3_core'])]:
        check('independent cubic '+name,a==b,kappa=str(kap),modes=len(coeff))
    check('full polynomial Poisson',not z['poisson'])
    model=MPQDensity([[float(v)for v in row]for row in coeff],1,float(kap),2.5)
    # Restore exact manufactured rational inputs after the generic loader.
    model.coeff=[[mf(v)for v in row]for row in coeff];model.kappa=mf(kap);model.ell=mf(ell)
    m0=mp.power(2,-model.kappa)
    errors=[]
    for rr in ['.001','.0001','.00001']:
      r=mp.mpf(rr)
      for cs,sn in [(mp.mpf(3)/5,mp.mpf(4)/5),(mp.mpf(5)/13,mp.mpf(12)/13)]:
        X=r*cs;Y=r*sn
        actual=r*model.at(m0*r,mp.atan2(Y,X))[0]
        poly=mp.fsum(mf(v)*X**i*Y**j for(i,j),v in z['rho'].items())
        scaled=abs(actual-poly)/r**9
        check('density series remainder degree9',scaled<mp.mpf('1e6'),kappa=str(kap),radius=rr,scaled_error=mp.nstr(scaled,12))
    if len(coeff)==1:
        radial={}
        for k in range(4):
            fk=z['beta'].get((0,k),F(0))
            for j in range(k+1):
                from math import comb
                radial[(2*j+1,2*(k-j)+1)]=-fk*comb(k,j)/(2*k+4)
        check('radial directly integrated stream',add(z['psi'],scale(radial,-1))=={})
    else:
        def Bj(j,s):return model.clenshaw(model.coeff[j],2*s-1)[0]if j<len(model.coeff)else mp.mpf(0)
        for h in z['harmonic']:
            n=h['n'];q=2*model.kappa*(n-1)
            value=mp.quad(lambda s:(1-s)**q*(Bj(n,s)-s*Bj(n+1,s))*(1+(2*model.kappa-1)*s)/4,[0,mp.mpf('.5'),1])
            error=abs(value-mf(h['density_exterior_moment_core']))
            check('adaptive original Chebyshev canonical moment',error<mp.mpf('1e-70'),n=n,kappa=str(kap),absolute_error=mp.nstr(error,15))
now=datetime.now(timezone.utc).isoformat();dest=Path('research/q_canonical_high_jets/verification');dest.mkdir(parents=True,exist_ok=True)
files=['research/q_canonical_high_jets/PROOF.md','independent_code/q_canonical_high_jets.py',__file__]
record=dict(utc=now,status='PASS',count=len(checks),checks=checks,hashes={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in files},scope='Exact algebraic and finite manufactured high-precision checks, not interval certification of candidates.')
(dest/'checks.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:record[k]for k in ['utc','status','count']}))
