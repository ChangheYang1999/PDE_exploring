"""Independent original-checkpoint audit for the 4/9 decay and R=2^32.
All output is confined to this verification directory; no archived code runs.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import sys, json, hashlib
from flint import arb, ctx
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'source_audit'))
import recover_state as rec
rec.HERE=HERE
rec.COPY=Path('case4/IPM_case4.artifacts')
c,coeff,record=rec.read_state(131)
ctx.prec=512
gam=1/c; delta=1-gam; d=Q(4,9); sigma=Q(11,5)
assert Q(9,5)<c<Q(37,20) and d<delta<Q(1,2)
A=lambda x: arb(Q(x).numerator)/Q(x).denominator
p=[(3+gam-j*delta)/2 for j in range(4)]
assert all(abs(p[j]-k)<26 for j,m,k in rec.CANON)
# Complex Laurent coefficients as exact real/imaginary pairs. This independently
# checks the sine/cosine differentiation in the older sector producer.
def plus(T,n,z):
    old=T.get(n,(Q(0),Q(0)))
    new=(old[0]+z[0],old[1]+z[1])
    if new==(0,0): T.pop(n,None)
    else: T[n]=new
def scale(z,a): return (z[0]*a,z[1]*a)
def times_i(z): return (-z[1],z[0])
def derivative(T,powr,axis):
    out={}
    for n,z in T.items():
        if axis=='x':
            plus(out,n+1,scale(z,(powr-n)/2))
            plus(out,n-1,scale(z,(powr+n)/2))
        else:
            plus(out,n+1,scale(times_i(z),-(powr-n)/2))
            plus(out,n-1,scale(times_i(z),(powr+n)/2))
    return out
def choose(x,n):
    out=Q(1)
    for k in range(n): out*= (x-k)/(k+1)
    return out
def l1(T):
    # Every coefficient here is pure real or pure imaginary.
    assert all(a==0 or b==0 for a,b in T.values())
    return sum((abs(a)+abs(b) for a,b in T.values()),Q(0))
axes={'chi12':'xyy','chi21':'xxy','chi13':'xyyy','chi22':'xxyy','chi31':'xxxy','chi04':'yyyy','chi41':'xxxxy','chi32':'xxxyy','chi23':'xxyyy','chi14':'xyyyy','chi05':'yyyyy'}
sectors={}
for j in range(4):
    for q in range(7):
        T={}
        for v,(jj,m,k) in zip(coeff,rec.CANON):
            if jj==j:
                a=v*choose(p[j]-k,q)
                plus(T,2*m,(a/2,Q(0)))
                plus(T,-2*m,(a/2,Q(0)))
        for label,aa in axes.items():
            V=T
            for z,axis in enumerate(aa): V=derivative(V,2*p[j]-2*q-z,axis)
            sectors[j,q,label]=l1(V)
            assert d-delta-j*delta-2*q<0
R0=arb(100); q0=7
absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,rec.CANON) if j==jj),Q(0)) for j in range(4)]
tails={}
for order in (3,4,5):
    ratio=A(Q(q0+26,q0+1)*Q(2*q0+34,2*q0+32)**order)/R0**2
    assert ratio<1
    tails[order]=A(comb(q0+25,q0)*(2*q0+32)**order)*R0**(-2*q0)/(1-ratio)*sum((A(absj[j])*R0**A(-j*delta) for j in range(4)),arb(0))
norm={label:sum((A(v)*R0**A(-j*delta-2*q) for (j,q,ll),v in sectors.items() if ll==label),arb(0))+tails[len(aa)] for label,aa in axes.items()}
old=json.loads((BASE/'07_weighted/verification/state131_weighted_bounds.json').read_text())
assert old['input_sha256']==record['canonical_serialization_sha256']
for k,v in norm.items(): assert v.overlaps(arb(old['field_sector_coefficients'][k])),k
G4=((norm['chi31']+norm['chi13'])**2+(norm['chi22']+norm['chi04'])**2).sqrt()
G5=((norm['chi41']+norm['chi23'])**2+2*(norm['chi32']+norm['chi14'])**2+(norm['chi23']+norm['chi05'])**2).sqrt()
U3=(norm['chi12']**2+norm['chi21']**2).sqrt()
U4=(2*norm['chi22']**2+norm['chi13']**2+norm['chi31']**2).sqrt()
U5=(norm['chi41']**2+3*norm['chi32']**2+3*norm['chi23']**2+norm['chi14']**2).sqrt()
fac=R0**A(d-delta)
far={'C_rho':fac*(G4+G5),'C_U':fac*U3,'C_DU':fac*U4,'C_D2U':fac*U5}
local={'C_rho':24*R0**A(d),'C_U':A(Q(14,5))*R0**A(d),'C_DU':A(Q(14,5))*R0**A(d),'C_D2U':3*R0**A(d)}
target={'C_rho':190,'C_U':23,'C_DU':23,'C_D2U':56}
for k,t in target.items(): assert local[k]<t and far[k]<t,(k,local[k],far[k])
M=A(d/2)*A((2-d)/d)**A(1-d/2)
Ccomm=4*A(sigma)*M/A(3-sigma-d)
assert Ccomm<15
R=arb(2)**32
Ctotal=23+16*190+A(sigma)*(9*23+2*23+56/arb(2).sqrt())
margin=A(Q(2,5))-Ctotal/R**A(d)
assert margin>A(Q(1,5))
# A rational-only margin check. R^(4/9)>2^14 and 1/sqrt(2)<5/7.
rational_margin=Q(2,5)-(23+16*190+sigma*(9*23+2*23+Q(56*5,7)))/2**14
# This coarser denominator does not prove 1/5: use a rational lower 19000.
assert 19000**9 < 2**128
rational_margin=Q(2,5)-(23+16*190+sigma*(9*23+2*23+Q(56*5,7)))/19000
assert rational_margin>Q(1,5)
deps=[HERE.parent/'PROOF.md',BASE/'source_audit/recover_state.py',BASE/'07_weighted/verification/sharp_coefficient_audit.json',BASE/'02_energy/verification/state131_coefficient_bounds.json',BASE/'07_weighted/LOW_INVERSE_PROOF.md',BASE/'07_weighted/RADIAL_COMMUTATOR_PROOF.md',BASE/'07_weighted/SHARP_WEIGHTED_H2_PROOF.md',BASE/'16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED V088','state':131,'source_json_sha256':record['source_json_sha256'],'canonical_sha256':record['canonical_serialization_sha256'],'precision_bits':ctx.prec,'decay_exponent':str(d),'actual_decay':str(delta),'physical_weight_exponent':str(sigma),'local_bounds':{k:v.str(70) for k,v in local.items()},'exterior_bounds':{k:v.str(70) for k,v in far.items()},'global_upper_bounds':target,'commutator_coefficient':Ccomm.str(70),'rounded_commutator_coefficient':15,'radius':'2^32','low_margin':margin.str(70),'rational_margin_lower':str(rational_margin),'inverse_upper':5,'independent_complex_sector_checks':len(norm),'dependency_hashes':{str(x.relative_to(BASE)):hashlib.sha256(x.read_bytes()).hexdigest() for x in deps},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
