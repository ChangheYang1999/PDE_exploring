"""Independent exact audit. No lead/numerics code is imported or executed.
Coefficient arithmetic uses our own truncated convolution and reciprocal recurrence.
Physical curl is independently differentiated before comparing strip formulas.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/227_lead_separable_vorticity_audit/verification'
t0=time.monotonic(); start=datetime.now(timezone.utc).isoformat(); checks={}; differences={}
def check(name,lhs,rhs=0):
    d=s.factor(s.cancel(lhs-rhs)); checks[name]=(d==0); differences[name]=str(d)
def truth(name,value): checks[name]=bool(value)
# Formal truncated polynomials in y, separate from SymPy series/diff of lead scripts.
N=6
def vec(seq=()): return [s.sympify(x) for x in seq]+[s.S.Zero]*(N+1-len(seq))
def add(*ps): return [s.expand(sum(p[i] for p in ps)) for i in range(N+1)]
def scale(p,c): return [s.expand(c*x) for x in p]
def mul(p,q): return [s.expand(sum(p[j]*q[i-j] for j in range(i+1))) for i in range(N+1)]
def deriv(p): return [(i+1)*p[i+1] for i in range(N)]+[s.S.Zero]
def integ(p): return [s.S.Zero]+[p[i-1]/i for i in range(1,N+1)]
def inv(p):
    out=[1/p[0]]
    for i in range(1,N+1):out.append(s.expand(-sum(p[j]*out[i-j] for j in range(1,i+1))/p[0]))
    return out
r,c2,c4,A0,B0,z=s.symbols('r c2 c4 A0 B0 z')
def quantities(a):
    ap=deriv(a); app=deriv(ap); AA=integ(a); ai=inv(a); ai2=mul(ai,ai)
    B=add(mul(app,ai),scale(mul(mul(ap,ap),ai2),-2))
    o1=add(scale(ap,4),scale(mul(AA,B),4),scale(ai2,-2*c2))
    o3=add(scale(B,c2),scale(ai2,-4*c4),scale(mul(mul(ap,ap),ai2),-2*c2))
    E1=scale(add(scale(mul(AA,deriv(o1)),4),mul(a,o1),vec([-A0])),-1)
    E3=scale(add(scale(mul(AA,deriv(o3)),4),scale(deriv(o1),c2),mul(a,o3),vec([-B0])),-1)
    return E1,E3
known=[s.S.One,r]
check('E1_constant_A0_relation',quantities(vec(known))[0][0],A0-4*r+2*c2)
for m in range(2,6):
    e=quantities(vec(known+[z]))[0][m-1].subs(A0,4*r-2*c2)
    leading=-4*m*m*(4*m-3)
    check(f'E1_y{m-1}_highest_jet',s.diff(e,z),leading)
    val=s.factor(-e.subs(z,0)/leading)
    known.append(val)
    print('solved r',m,flush=True)
E1,E3=quantities(vec(known))
for n in range(5):check(f'E1_recursion_y{n}',E1[n].subs(A0,4*r-2*c2))
check('r2',known[2],9*r*(2*r-c2)/40)
check('r3',known[3],r*(128*r-51*c2)*(2*r-c2)/2160)
for m in range(2,6):truth(f'r{m}_divisible_r_times_2r_minus_c2',s.cancel(known[m]/(r*(2*r-c2))).is_polynomial(r,c2))
Bsol=s.factor(-E3[0].subs(B0,0))
check('E3_y0_B0_solution',E3[0].subs(B0,Bsol))
E31=s.factor(E3[1]); claim1=-r*(219*c2**3+6026*c2**2*r+32*c2*r**2+12960*c4)/360
check('E3_y1',E31,claim1)
c4sol=-(219*c2**3+6026*c2**2*r+32*c2*r**2)/12960
check('E3_y1_c4_solution',E31.subs(c4,c4sol))
t=s.symbols('t'); P=-130509*t**2+4496958*t+12320
Q=-405889875*t**3+30302578176*t**2+58633849676*t+1213256384
E32=s.factor(E3[2].subs(c4,c4sol)); E33=s.factor(E3[3].subs(c4,c4sol))
check('E3_y2',E32,-c2*r**3*(2*r-c2)*P.subs(t,c2/r)/1123200)
check('E3_y3',E33,c2*r**4*(2*r-c2)*Q.subs(t,c2/r)/15466464000)
resultant=s.resultant(P,Q,t); check('resultant_value',resultant,-50076093926441217209396936743211581440)
truth('resultant_nonzero',resultant!=0)
# Independently check Bezout identity over Q[t], not just resultant implementation.
bp,bq,gcd=s.gcdex(P,Q,t); check('bezout_identity',bp*P+bq*Q,1)
# General formula for recursive highest coefficient.
m=s.symbols('m',integer=True,positive=True)
check('highest_coefficient_all_n',-16*m*(m-1)*(m-2)-36*m*(m-1)-4*m,-4*m*m*(4*m-3))
truth('highest_coefficient_nonzero',(-4*m*m*(4*m-3)).is_negative)
# Physical derivatives first, then evaluation x=k*a(y).
x,y,k=s.symbols('x y k',real=True); af=s.Function('a')(y); AA=s.Function('A')(y); Cf=s.Function('C')
def norm(expr): return s.simplify(expr.doit().subs(s.diff(AA,y),af).doit())
kphys=x/af; Dphys=4*AA+Cf(kphys)
W2=Dphys/af; W1=kphys*s.diff(af,y)*W2
omega=norm(s.diff(W1,y)-s.diff(W2,x))
Dm=4*AA+Cf(k); Bf=s.diff(af,y,2)/af-2*s.diff(af,y)**2/af**2
om=4*k*s.diff(af,y)+k*Dm*Bf-(1+k*k*s.diff(af,y)**2)*s.diff(Cf(k),k)/af**2
check('physical_divergence',norm(s.diff(W1,x)+s.diff(W2,y)),4)
check('physical_negative_curl',norm(omega.subs(x,k*af)),om)
check('material_k',norm(W1*s.diff(kphys,x)+W2*s.diff(kphys,y)))
physV=norm((af*(W1*s.diff(omega,x)+W2*s.diff(omega,y)+omega)).subs(x,k*af))
stripV=norm(Dm*s.diff(om,y)+af*om)
check('physical_vorticity_operator',physV,stripV)
a1=af**-2;a2=s.diff(af,y)**2/af**2;a3=-4*AA*Bf-4*s.diff(af,y);a4=-Bf
L=lambda f:norm(4*AA*s.diff(f,y)+af*f)
struct=-(s.diff(Cf(k),k)*L(a1)+k*k*s.diff(Cf(k),k)*L(a2)+k*L(a3)+k*Cf(k)*(L(a4)+s.diff(a3,y))+Cf(k)*s.diff(Cf(k),k)*s.diff(a1,y)+k*k*Cf(k)*s.diff(Cf(k),k)*s.diff(a2,y)+k*Cf(k)**2*s.diff(a4,y))
check('lead_structural_formula',stripV,norm(struct))
ph=4*AA/af; q=-2*c2/af**3-norm(s.diff(ph,y,2))
check('a3_is_a_phi_second',a3,norm(af*s.diff(ph,y,2)))
ap=s.diff(af,y); o1=4*ap+4*AA*Bf-2*c2/af**2
e1=-norm(4*AA*s.diff(o1,y)+af*o1-A0)
expanded=-16*AA**2*s.diff(af,y,3)/af-36*AA*s.diff(af,y,2)+80*AA**2*ap*s.diff(af,y,2)/af**2+40*AA*ap**2/af-64*AA**2*ap**3/af**3-4*af*ap+2*c2/af-16*c2*AA*ap/af**3+A0
check('expanded_E1',e1,expanded)
check('E1_axis_equation',e1,-norm(af**2*(ph*s.diff(q,y)+(5-norm(s.diff(ph,y)))*q-A0/af**2)))
check('axis_integrating_factor_identity',norm(ph*s.diff(af*q,y)+af*q),norm(af*(ph*s.diff(q,y)+(5-norm(s.diff(ph,y)))*q)))
# Complete singular system, generic algebraic substitution.
z1,z2,z3,z4,h=s.symbols('z1 z2 z3 z4 h')
N=-36*z4*z3+80*z4**2*z2*z3/z1**2+40*z4*z2**2/z1-64*z4**2*z2**3/z1**3-4*z1*z2+y*(2*c2/z1-16*c2*z4*z2/z1**3+A0)
sube={af:z1,AA:y*z4,s.diff(af,y):z2/y,s.diff(af,y,2):z3/y**2,s.diff(af,y,3):h/y**3}
check('Fuchsian_highest_derivative',s.cancel(y*expanded.subs(sube,simultaneous=True)),-16*z4**2*h/z1+N)
F=s.Matrix([z2,z2+z3,2*z3+z1*N/(16*z4**2),z1-z4])
for i,f in enumerate(F):check(f'Fuchsian_equilibrium_for_all_y_{i}',f.subs({z1:1,z2:0,z3:0,z4:1,c2:-A0/2},simultaneous=True))
truth('Fuchsian_denominators_nonzero_at_equilibrium',all(s.denom(s.cancel(f)).subs({z1:1,z4:1})!=0 for f in F))
K=s.symbols('K',positive=True); n=s.symbols('n',integer=True,positive=True); yy=s.symbols('yy',positive=True)
check('Gronwall_log_integral',s.integrate(K/y,(y,yy,1)),-K*s.log(yy))
check('flat_power_contradiction',s.limit(yy**n,yy,0,dir='+'),0)
# Rescaling exact control and explicit refutation of lead's original direction.
aex=s.sqrt(1+y*y); rhoold=2*aex; Hex=lambda u:u*u
old=Hex(x/rhoold); corrected=Hex((x/aex)/2); wrong=Hex(2*x/aex)
check('corrected_rescaling',old,corrected)
truth('original_rescaling_refuted',s.simplify(old-wrong)!=0)
check('regularity_recovery',s.sqrt(2/s.diff(old,x,2)),rhoold)
check('quadratic_H_after_rescaling',s.diff(Hex(k/2),k,2),s.diff(old,x,2).subs(y,0))
# Constant-scale solution and formal flat jet controls.
for m in range(1,6):check(f'constant_scale_jet_r{m}',known[m].subs(r,0))
check('constant_scale_E1',expanded.subs({af:1,AA:y,ap:0,s.diff(af,y,2):0,s.diff(af,y,3):0,c2:-A0/2},simultaneous=True))
end=datetime.now(timezone.utc).isoformat()
report={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'all_passed':all(checks.values()),'checks':checks,'algebraic_differences':differences,'jets':{f'r{i}':str(known[i]) for i in range(1,6)},'B0':str(Bsol),'c4':str(c4sol),'E3_y2':str(E32),'E3_y3':str(E33),'resultant':str(resultant),'bezout_P':str(bp),'bezout_Q':str(bq),'method':'Own truncated convolution and reciprocal recurrence from physical negative curl, no lead/numerics code imports. Exact SymPy rational simplification and independent Bezout identity.','scope':'Finite exact controls plus standalone PROOF.md; no formal proof or unrestricted B2 endpoint.','proof_sha256':hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({key:report[key] for key in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[k for k,v in checks.items() if not v])
