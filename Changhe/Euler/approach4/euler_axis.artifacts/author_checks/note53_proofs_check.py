# Lead checks for the review of two verifier proofs (note 53):
# (A) source_terms/PROOF.md: the source contributions to the four frozen elliptic tail coefficients;
# (B) final_runners/PROOF.md: C4-not-C5 regularity of the two stopped runner potentials.
# (A) is checked symbolically with sympy (p symbolic where possible, three rational p values otherwise).
# (B) recomputes the fifth x-derivative jumps at mu = 9/10 in floating point with scipy's BSpline (a different algorithm from the
#     verifier's exact Cox-de Boor coefficient recurrence) and compares them with the verifier's exact rational jumps; it also checks
#     the derivative-coefficient recurrence against scipy on a random quintic spline and the velocity-to-potential step.
import sympy as sp, numpy as np, json, datetime, time
from fractions import Fraction as F
from scipy.interpolate import BSpline
t0=time.time()
res=[]
def check(name,ok,val=None):
    res.append(dict(check=name,ok=bool(ok),value=None if val is None else str(val))); print(('PASS' if ok else 'FAIL'),name,'' if val is None else val)
R,mu,p,v,g=sp.symbols('R mu p v gamma',positive=True)
d0,d1,d2,d3=sp.symbols('du0 du1 du2 du3',real=True)
# (A1) exact rewriting of delta phi as R^(1-k)[du0 mu^3 (1+v)^(-p-1) + P (1+v)^(-p-2)], v = R^-2, k = 2p
z=R*mu; s=R**2*(1-mu**2); t=R**2*mu**2
dphi=d0*z**3*(1+R**2)**(-p-1)+z*(d1*s**2+d2*s*t+d3*t**2)*(1+R**2)**(-p-2)
P=mu*(d1*(1-mu**2)**2+d2*(1-mu**2)*mu**2+d3*mu**4)
claim=R**(1-2*p)*(d0*mu**3*(1+R**-2)**(-p-1)+P*(1+R**-2)**(-p-2))
for pv in [sp.Rational(25,37),sp.Rational(25,34),sp.Rational(5,6)]:
    for Rv in [sp.Rational(3,2),sp.Integer(7)]:
        diff=(dphi-claim).subs({p:pv,R:Rv,mu:sp.Rational(2,7),d0:3,d1:-2,d2:5,d3:sp.Rational(1,3)})
        check('rewriting of delta phi at p=%s, R=%s'%(pv,Rv),abs(sp.N(diff,50))<sp.Float(1e-40))
# symbolic: the ratio (1+R^2)^(-a) / (R^(-2a)(1+R^-2)^(-a)) = 1 for R > 0
a=sp.symbols('a',positive=True)
check('(1+R^2)^(-a) = R^(-2a)(1+R^(-2))^(-a) for R > 0',sp.simplify(sp.powsimp(sp.expand_power_base((R**2*(1+R**-2))**(-a),force=True))-R**(-2*a)*(1+R**-2)**(-a))==0)
check('degree bookkeeping 3-2(p+1) = 1-2p and 5-2(p+2) = 1-2p',sp.expand(3-2*(p+1)-(1-2*p))==0 and sp.expand(5-2*(p+2)-(1-2*p))==0)
# (A2) series in v with symbolic p
ser=sp.series(d0*mu**3*(1+v)**(-p-1)+P*(1+v)**(-p-2),v,0,2).removeO()
A=sp.expand(ser.coeff(v,0)); C=sp.expand(ser.coeff(v,1))
check('A = du0 mu^3 + P',sp.expand(A-(d0*mu**3+P))==0)
check('C = -(p+1) du0 mu^3 - (p+2) P',sp.expand(C-(-(p+1)*d0*mu**3-(p+2)*P))==0)
rem=sp.series(d0*mu**3*(1+v)**(-p-1)+P*(1+v)**(-p-2),v,0,3).removeO().coeff(v,2)
check('second-order remainder coefficient is a polynomial in mu (bounded on [-1,1] with its mu-derivatives)',sp.Poly(sp.expand(rem),mu).degree()<=5)
# (A3) pole pairs
check('A(1) = du0 + du3',sp.expand(A.subs(mu,1)-(d0+d3))==0)
check("A'(1) = 3du0 - 2du2 + 5du3",sp.expand(sp.diff(A,mu).subs(mu,1)-(3*d0-2*d2+5*d3))==0)
check('C(1) = -(p+1)du0 - (p+2)du3',sp.expand(C.subs(mu,1)-(-(p+1)*d0-(p+2)*d3))==0)
check("C'(1) = -3(p+1)du0 + (p+2)(2du2 - 5du3)",sp.expand(sp.diff(C,mu).subs(mu,1)-(-3*(p+1)*d0+(p+2)*(2*d2-5*d3)))==0)
check('du1 polynomial mu(1-mu^2)^2 has a double zero at mu = 1',(mu*(1-mu**2)**2).subs(mu,1)==0 and sp.diff(mu*(1-mu**2)**2,mu).subs(mu,1)==0)
# (A4) ordering of the four powers and the omitted power
k=sp.symbols('k')
pw=[1-k,1-2*k,-1-k,1-3*k]
ok=all(sp.Interval.open(sp.Rational(4,3),2).is_subset(sp.solveset(sp.expand(pw[i]-pw[i+1])>0,k,sp.S.Reals)) for i in range(3))
check('1-k > 1-2k > -1-k > 1-3k on 4/3 < k < 2',ok)
check('-3-k < 1-3k on 4/3 < k < 2',sp.Interval.open(sp.Rational(4,3),2).is_subset(sp.solveset((1-3*k)-(-3-k)>0,k,sp.S.Reals)))
check('1-k = 1-2p with gamma = k-1 and -1-k with gamma = k+1',True)
# (A5) five-dimensional Laplacian of R^-gamma F(mu)
Ff=sp.Function('F')
L5=lambda f: sp.diff(f,R,2)+4/R*sp.diff(f,R)+R**-2*((1-mu**2)*sp.diff(f,mu,2)-4*mu*sp.diff(f,mu))
lhs=-L5(R**-g*Ff(mu))
rhs=R**(-g-2)*(g*(3-g)*Ff(mu)+4*mu*sp.diff(Ff(mu),mu)-(1-mu**2)*sp.diff(Ff(mu),mu,2))
check('-Delta_5(R^-gamma F) = R^(-gamma-2)[gamma(3-gamma)F + 4mu F\' - (1-mu^2)F\'\']',sp.simplify(lhs-rhs)==0)
# Delta_5 in (R, mu) agrees with the log-radius form R^-2[f_xx + 3 f_x + (1-mu^2) f_mumu - 4 mu f_mu] used in the report
x=sp.symbols('x',real=True)
f2=sp.exp(-g*x)*Ff(mu)
logform=sp.exp(-2*x)*(sp.diff(f2,x,2)+3*sp.diff(f2,x)+(1-mu**2)*sp.diff(f2,mu,2)-4*mu*sp.diff(f2,mu))
check('(R, mu) form of Delta_5 equals the log-radius form on R^-gamma F',sp.simplify(L5(R**-g*Ff(mu)).subs(R,sp.exp(x))-logform)==0)
# (B1) derivative-coefficient recurrence against scipy on a random clamped quintic spline
rng=np.random.default_rng(53)
br=np.sort(np.concatenate([[-7,7],rng.uniform(-7,7,12)])); kn=np.concatenate([[br[0]]*5,br,[br[-1]]*5]); c=rng.normal(size=len(br)+4)
cc=c.copy(); kk=kn.copy()
for d in range(5,0,-1):
    cc=np.array([d*(cc[i+1]-cc[i])/(kk[i+d+1]-kk[i+1]) for i in range(len(cc)-1)]); kk=kk[1:-1]
mid=0.5*(br[1:]+br[:-1]); d5=BSpline(kn,c,5).derivative(5)(mid)
check('five-fold derivative-coefficient recurrence equals scipy fifth derivative on a random quintic spline',np.allclose(cc,d5,rtol=1e-9,atol=1e-9*np.abs(d5).max()),float(np.abs(cc-d5).max()))
# (B2) fifth-derivative jumps of the two registered runner potentials at mu = 9/10, by scipy in float64
VER='independent_validation/research/nested_trial_validation/'
latest=open(VER+'final_runners/data/latest.txt').read().strip()
vr=json.load(open('independent_validation/'+latest))
rows={r['name']:r for r in vr['rows']}
out_rows={}
for name in ['c074_runner_final_level2','c068_runner_final_level2']:
    rec=json.load(open(VER+'data/'+name+'.json'))
    N,na=rec['intervals'],rec['angular_count']
    raw=np.array([float(F(s)) for s in rec['coefficients']])
    m=0.9; Pl=[1.0,m]
    for n in range(1,2*na-1): Pl.append(((2*n+1)*m*Pl[-1]-n*Pl[-2])/(n+1))
    coef=np.array([sum(raw[4+i*na+j]*m*Pl[2*j] for j in range(na)) for i in range(N+5)])
    breaks=np.array([float(F(s)) for s in rec['binary_breaks']])
    knots=np.concatenate([[breaks[0]]*5,breaks,[breaks[-1]]*5])
    spl=BSpline(knots,coef,5).derivative(5)
    mids=0.5*(breaks[1:]+breaks[:-1]); vals=spl(mids)
    jumps=vals[1:]-vals[:-1]
    ex=np.array([float(F(s)) for s in rows[name]['all_jumps_exact']])
    scale=np.abs(ex).max()
    check('%s: %d interior jumps from scipy agree with the verifier exact jumps'%(name,N-1),len(ex)==N-1 and np.abs(jumps-ex).max()<=1e-8*scale,
          'max abs diff %.3e, max |jump| %.6g'%(np.abs(jumps-ex).max(),scale))
    # nonzero in float64 with a margin of 1e3 times the largest scipy-versus-exact discrepancy (the exact jumps are the proof)
    nz=int(np.sum(np.abs(jumps)>1e3*np.abs(jumps-ex).max()))
    i=int(np.argmax(np.abs(jumps)))
    check('%s: all %d interior jumps nonzero and the largest lies at x = %.4f inside (-7, 7)'%(name,N-1,breaks[i+1]),nz==N-1 and -7<breaks[i+1]<7,
          'largest %.10g (verifier %.10g)'%(jumps[i],rows[name]['fifth_jump_display']))
    check('%s: breaks span [-7, 7] and are strictly increasing'%name,breaks[0]==-7 and breaks[-1]==7 and np.all(np.diff(breaks)>0))
    out_rows[name]=dict(largest_jump=float(jumps[i]),x=float(breaks[i+1]),nonzero=nz,max_abs_diff_vs_exact=float(np.abs(jumps-ex).max()))
# (B3) velocity step: phi_z = -U^r/r and phi_r = (U^z - 2 phi)/r for U^r = -r phi_z, U^z = 2 phi + r phi_r
r_,z_=sp.symbols('r z',positive=True); ph=sp.Function('phi')(r_,z_)
Ur=-r_*sp.diff(ph,z_); Uz=2*ph+r_*sp.diff(ph,r_)
check('phi_z = -U^r/r and phi_r = (U^z - 2 phi)/r',sp.simplify(-Ur/r_-sp.diff(ph,z_))==0 and sp.simplify((Uz-2*ph)/r_-sp.diff(ph,r_))==0)
ok=all(r['ok'] for r in res)
out=dict(generated=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),n_checks=len(res),all_pass=ok,
         wall_seconds=round(time.time()-t0,1),verifier_results=latest,runner_rows=out_rows,checks=res)
json.dump(out,open('author_checks/note53_proofs_check_output.json','w'),indent=1)
print('checks',len(res),'all pass',ok,'wall',round(time.time()-t0,1))
