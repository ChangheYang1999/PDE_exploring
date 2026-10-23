"""Independent algebra, connection, inverse manufacture and correction resonance."""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import mpmath as mp
import sympy as sy

r = Path("research/hydrostatic_inner_layer_audit/verification")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc = lambda: datetime.now(timezone.utc).isoformat()
out = dict(started_utc=utc(), status="RUNNING", pid=os.getpid(), checks=[], numeric=[],
           proof_sha256=sha(r.parent / "PROOF.md"), code_sha256=sha(__file__),
           lead_checks_read=False)


def save():
    (r / "CHECKS.json").write_text(json.dumps(out, indent=2)+"\n")


def check(name, ok, evidence=None):
    out["checks"].append(dict(name=name, passed=bool(ok), evidence=evidence))
    if not ok:
        out["status"] = "FAILED"
        save()
        raise AssertionError(name)


def zero(name, expr):
    check(name, sy.factor(expr) == 0)


p, beta, z, y, x, kk, L = sy.symbols("p beta z y x K L", positive=True)
alpha = (p+1)/2
c = 1/p
h = alpha*p
q = h+p-1
s = p-1/alpha
A = c*(1-alpha)
lam = p*kk/(2*alpha**2*A)
zero("density inverse balance", q-2*alpha-(h-2))
zero("transport constant", c*q-1+A*(p+2))
zero("lambda simplified", lam-4*p*p*kk/((p+1)**2*(1-p)))
zero("inverse second root", alpha*s-h+1)
zero("inner V1 scaling", q-alpha+1-(h+alpha-1))
zero("V1 inner base transport", h+alpha-1+alpha+p-2-(q+p-1))
zero("outer intermediate degree", q+(1-alpha)*s-(p+s))
zero("excluded fast degree", q+(1-alpha)*(p+2)-p)
zero("first odd zero polynomial", p/(p+1)-(1-p)/2-(p*p+2*p-1)/(2*(p+1)))
zero("primed odd denominator1", (1+1/(p+1))-((1-p)/2+1/(p+1))-(1+p)/2)
zero("primed odd denominator2", (2+1/(p+1))-((1-p)/2+1/(p+1))-(3+p)/2)
B = sy.Function("B")(z)
theta = lambda f: z*sy.diff(f, z)
triple = lambda f, roots: theta(theta(theta(f))) - sum(roots)*theta(theta(f)) + sum(roots[i]*roots[j] for i in range(3) for j in range(i+1,3))*theta(f) - sy.prod(roots)*f
v = -A*(theta(B)-(p+2)*B)/(p*kk)
zero("elimination including sign",
     sy.diff(B,z,2)+alpha**2*(theta(theta(v))-(p+s)*theta(v)+p*s*v)
     +alpha**2*A/(p*kk)*(triple(B,[p,s,p+2])-2*lam*sy.diff(B,z,2)))
m = p+beta/alpha
n = m-1/alpha
t = p+2-beta/(1-alpha)
zero("general correction transport root", c*(q+beta)-1+A*t)
zero("general correction b2", 1+(t-m)/2-(2-beta/(2*alpha*(1-alpha))))
ms = sy.factor(m.subs(beta,p-1))
zero("first correction resonance polynomial", ms+1-(p*p+4*p-1)/(p+1))
zero("resonance exact root", (ms+1).subs(p,sy.sqrt(5)-2))
zero("resonance c", 1/(sy.sqrt(5)-2)-(sy.sqrt(5)+2))
zero("Green tail weight", (h-1)/alpha-s)
zero("flat prefactor", 5+2*p+s-(3*p+2*p/(p+1)+3))
zero("compact outer correction moment", (2*p-1)*(2*p-2)+4*(2*p-2)+6-(2*p)*(2*p+1))
zero("outer completion relative order", alpha*(2*p-1)-h-alpha*(p-1))
zero("tail substitution weight removed", (2-h)/(1-h)-1/(1-h)-1)
check("stated total fixed-line exponent too small", float((p-h).subs(p,sy.Rational(1,2))) > 0)
save()

mp.mp.dps = 85


def params(p, beta=mp.mpf("0"), k=mp.mpf("1")):
    a = (p+1)/2
    m = p+beta/a
    n = m-1/a
    t = p+2-beta/(1-a)
    lam = 4*p*p*k/((p+1)**2*(1-p))
    return a,m,n,t,lam,[-m/2,(1-m)/2],[1-1/(2*a), 2-beta/(2*a*(1-a))]


def connection(aa, bb, lam, j):
    other = 1-j
    return (mp.gamma(bb[0])*mp.gamma(bb[1])*mp.gamma(aa[other]-aa[j])
            *mp.rgamma(aa[other])*mp.rgamma(bb[0]-aa[j])*mp.rgamma(bb[1]-aa[j])
            *lam**(-aa[j]))


ST = [[1], [0,1], [0,1,1], [0,1,3,1]]


def theta_jet(z, power, aa, bb, lam):
    arg = -lam/z**2
    ff = [mp.rf(aa[0],j)*mp.rf(aa[1],j)/(mp.rf(bb[0],j)*mp.rf(bb[1],j))
          *mp.hyper([a+j for a in aa],[b+j for b in bb],arg) for j in range(4)]
    d = [mp.fsum(ST[k][j]*arg**j*ff[j] for j in range(k+1)) for k in range(4)]
    return [z**power*mp.fsum(math.comb(k,j)*power**(k-j)*(-2)**j*d[j] for j in range(k+1)) for k in range(4)]


def direct_series(aa, bb, arg):
    term = total = mp.mpf(1)
    for j in range(1, 2000):
        term *= (aa[0]+j-1)*(aa[1]+j-1)*arg/((bb[0]+j-1)*(bb[1]+j-1)*j)
        total += term
        if abs(term) < mp.mpf("1e-82")*max(1,abs(total)):
            return total, j
    raise ArithmeticError("series did not settle")


def taylor_value(E, O, roots, lam, z, length=32):
    cc = [E,O]
    for j in range(length-2):
        cc.append(mp.fprod(j-a for a in roots)*cc[j]/(2*lam*(j+2)*(j+1)))
    return mp.fsum(a*z**j for j,a in enumerate(cc))


ps = [mp.mpf(1)/5, mp.mpf(1)/4, mp.mpf(1)/3, mp.sqrt(2)-1,
      mp.mpf(1)/2, mp.mpf(3)/4, mp.mpf(9)/10]
for pv in ps:
    a,m,n,t,lv,aa,bb = params(pv)
    shift = 1/(2*a)
    a2 = [v+shift for v in aa]
    b2 = [1+shift,bb[1]+shift]
    E1,O1 = [connection(aa,bb,lv,j) for j in (0,1)]
    E2,O2 = [connection(a2,b2,lv,j) for j in (0,1)]
    record = dict(p=str(pv),lambda_=str(lv),E1=str(E1),O1=str(O1),E2=str(E2),O2=str(O2),samples=[])
    check("leading O2 nonzero "+str(pv), O2 < 0)
    for power, avec, bvec, E, O, label in [(m,aa,bb,E1,O1,"B1"),(n,a2,b2,E2,O2,"B2")]:
        own, count = direct_series(avec,bvec,mp.mpf("-1.75"))
        exact = mp.hyper(avec,bvec,mp.mpf("-1.75"))
        err = abs(own-exact)/max(1,abs(exact))
        check("independent 2F2 coefficient sum "+label+str(pv), err < mp.mpf("1e-78"), str(err))
        for zv in [mp.mpf(".08"),mp.mpf(".4"),mp.mpf("1.3")]:
            J = theta_jet(zv,power,avec,bvec,lv)
            d2 = (J[2]-J[1])/zv**2
            roots = [m,n,t]
            terms = [J[3],-sum(roots)*J[2],
                     (m*n+m*t+n*t)*J[1],-m*n*t*J[0],-2*lv*d2]
            error = abs(mp.fsum(terms))/max(1,mp.fsum(abs(v) for v in terms))
            check("ODE "+label+str(pv)+str(zv), error < mp.mpf("1e-72"), str(error))
            if zv == mp.mpf(".4"):
                fun = lambda zz: zz**power*mp.hyper(avec,bvec,-lv/zz**2)
                dnum = mp.diff(fun,zv,2)
                error2 = abs(dnum-d2)/max(1,abs(dnum))
                check("derivative crosscheck "+label+str(pv), error2 < mp.mpf("1e-70"), str(error2))
        for zv in [mp.mpf(".003"),mp.mpf(".006")]:
            direct = zv**power*mp.hyper(avec,bvec,-lv/zv**2)
            predicted = taylor_value(E,O,[m,n,t],lv,zv)
            error = abs(direct-predicted)/max(1,abs(direct))
            check("residue Taylor asymptotic "+label+str(pv)+str(zv), error < mp.mpf("1e-36"), str(error))
            record["samples"].append(dict(branch=label,z=str(zv),value=str(direct),Taylor=str(predicted),error=str(error)))
    combo_odd = O1-(O1/O2)*O2
    check("smooth matching odd cancellation "+str(pv), abs(combo_odd) < mp.mpf("1e-80"))
    if pv == mp.mpf(".5"):
        b0 = pv/(1/pv-1)*(E1-(O1/O2)*E2)
        b_second = mp.fprod(-a for a in [m,n,t])*b0/(2*lv)
        check("nonzero inner curvature gives divergent subtracted moment", b_second > 0)
        record["Cp_one_b0"] = str(b0)
        record["Cp_one_b_second0"] = str(b_second)
    out["numeric"].append(record)
    save()
    print(utc(),"p",mp.nstr(pv,9),"PASS",flush=True)

pv = mp.sqrt(2)-1
a,m,n,t,lv,aa,bb = params(pv)
check("leading exceptional O1", abs(connection(aa,bb,lv,1)) < mp.mpf("1e-80"))
pv = mp.sqrt(5)-2
a,m,n,t,lv,aa,bb = params(pv,pv-1)
shift = 1/(2*a)
ap = [v+shift for v in aa]
bp = [1+shift,bb[1]+shift]
o_main, o_free = connection(aa,bb,lv,1), connection(ap,bp,lv,1)
check("first correction free odd zero", abs(o_free) < mp.mpf("1e-79"), str(o_free))
check("first correction main odd nonzero", abs(o_main) > mp.mpf(".01"), str(o_main))
check("resonant upper lower parameter cancellation", abs(ap[1]-bp[0]) < mp.mpf("1e-80"))
for zv in [mp.mpf(".05"),mp.mpf(".2"),mp.mpf("1")]:
    left = zv**n*mp.hyper(ap,bp,-lv/zv**2)
    right = zv**n*mp.hyp1f1(ap[0],bp[1],-lv/zv**2)
    check("resonant 1F1 reduction "+str(zv), abs(left-right) < mp.mpf("1e-72")*max(1,abs(right)))
out["first_correction"] = dict(p=str(pv),c=str(1/pv),m=str(m),n=str(n),t=str(t),
                               odd_main=str(o_main),odd_free=str(o_free),
                               verdict="HOMOGENEOUS_RESONANCE_CONFIRMED; ACTUAL_FORCING_COMPATIBILITY_OPEN")
save()

# Exact incomplete-gamma Green function and a separately parameterized t integral.
# This manufacture does not solve the inner ODE and tests the inverse independently.
mp.mp.dps = 55
out["inverse_manufactures"] = []
for pv in [mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(3)/4]:
    a,m,n,t,lv,aa,bb = params(pv)
    hv = a*pv
    for xv,yv in [(mp.mpf(".6"),mp.mpf(".8")),(mp.mpf("1.7"),mp.mpf(".4"))]:
        zv = xv/yv**a
        first = 2*mp.gammainc(1-pv/2,zv*zv,mp.inf)-mp.gammainc(-pv/2,zv*zv,mp.inf)
        second = 2*mp.gammainc(1-n/2,0,zv*zv)-mp.gammainc(-n/2,0,zv*zv)
        expected = yv**hv/a*(zv**pv*first+zv**n*second)
        def curvature(tt):
            zz = xv/tt**a
            return tt**(hv-2)*(4*zz**2-2)*mp.exp(-zz**2)
        finite = mp.quad(lambda tt:tt*curvature(tt),[0,yv/2,yv])
        # Direct physical tail with its leading algebraic weight removed.
        tail = yv**hv/(1-hv)*mp.quad(
            lambda uu:(4*zv*zv*uu**(2*a/(1-hv))-2)
            *mp.exp(-zv*zv*uu**(2*a/(1-hv))), [0,mp.mpf(".25"),1])
        error = abs(finite+tail-expected)/max(1,abs(expected))
        check("canonical inner inverse manufacture "+str(pv)+str(xv), error < mp.mpf("1e-36"), str(error))
        out["inverse_manufactures"].append(dict(p=str(pv),x=str(xv),y=str(yv),
            direct=str(finite+tail),gamma=str(expected),error=str(error)))
save()
out.update(status="DONE", finished_utc=utc(), check_count=len(out["checks"]))
save()
print(utc(),len(out["checks"]),"PASS",flush=True)
