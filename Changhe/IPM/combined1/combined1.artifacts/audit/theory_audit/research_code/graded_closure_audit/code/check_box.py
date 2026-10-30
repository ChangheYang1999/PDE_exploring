from fractions import Fraction as Q
from pathlib import Path
import json
from flint import arb, ctx
ctx.prec=256

def A(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator
s=Q(1,50000)
r=[Q(1,5000),Q(1,3000000),Q(1,50000000),Q(1,30000000)]
eta_old=Q(1,1572864)
phi=[25*eta_old,25*eta_old/128,25*eta_old/512,Q(41,40)*25*eta_old/512]
S=A(s); R=list(map(A,r)); F=list(map(A,phi))
nu=(R[0]**2+2*R[1]**2+R[2]**2).sqrt()/S.sqrt()
As=A(Q(127,50))+A(Q(653,5))*S
Bs=A(Q(9,5))*(1+44*S)
mH=A(Q(19,5))-2*S
m0=A(Q(11,4))-3882*S-A(Q(3,10))*nu
m1=A(Q(9,10))-4290*S-A(Q(13,10))*nu
m2=A(Q(1,2))-4708*S-(As+Bs)*nu
q0=476*S+nu
kappa=q0/mH
den=1-kappa/m0.sqrt()
assert all(x>0 for x in [mH,m0,m1,m2,den])
b=(F[2]/m0+F[3]/(mH*m0.sqrt()))/den
H=F[3]/mH+kappa*b
a=(F[1]+(6+1360*S)*b)/m1
alpha=A(Q(347,5))+5440*S+Bs*nu
beta=10+34816*S
P=(F[0]+alpha*a+beta*b)/m2+(40/m2).sqrt()*a
Gamma=[P,a,b,H]
slack=[x-y for x,y in zip(R,Gamma)]
assert all(x>0 for x in slack)
d=(R[0]**2+2*R[1]**2+R[2]**2).sqrt()/(2*(arb.pi()*S*(1+S)).sqrt())
contract=d/(A(Q(19,5))-d)
assert contract<1
# An explicit auxiliary dissipative energy for this particular box.
# t=1 suffices here; Gershgorin supplies a positive low matrix floor.
ell0=m0-q0/2; ellH=mH-1-q0/2
ell=A(Q(5,2))
assert ell0>ell and ellH>ell
M=(41+alpha**2/m2)/m1
L=(1+beta**2/m2+(M*(6+1360*S))**2/2)/ell
result={'s':str(s),'box':[str(x) for x in r], 'forcing_upper_bounds':[str(x) for x in phi],
 'gain_comparison':'25 times the exact old component bounds of J^s F, with a safe 41/40 upper rounding of sqrt(21/20) in the H direction; s differs.',
 'nu':str(nu),'margins':dict(zip(['mH','m0','m1','m2','feedback_denominator'],map(str,[mH,m0,m1,m2,den]))),
 'Gamma':list(map(str,Gamma)),'positive_slacks':list(map(str,slack)),
 'low_contraction':str(contract),'gradient_bound':str(d),
 'auxiliary_energy_weights_P_a_b_H':['1',str(M),str(L),str(L)],
 'scope':'Arb256 certificate for this exact rational box and forcing upper vector, conditional on the analytic graded theorem.'}
Path(__file__).resolve().parents[1].joinpath('verification/rational_box.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
