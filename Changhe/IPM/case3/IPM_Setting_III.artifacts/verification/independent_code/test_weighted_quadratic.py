"""Independent angular operator and rational Schur-complement certification."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
import sympy as sp
import numpy as np
out=Path('research/weighted_quadratic_sharp/verification');out.mkdir(parents=True,exist_ok=True)
def b(j):return F(4*j*j+9,4*abs(4*j*j-9))
def pivots(lam,sg,N,tail):
    tau=sg*F(1,2)+2*b(N+1)
    if tail:assert lam>tau
    pp=[]
    for j in range(1,N+1):
        value=lam-sg*(F(1,4) if j==1 else F(1,2))
        if tail and j==N:value-=b(N)**2/(lam-tau)
        if j>1:value-=b(j-1)**2/pp[-1]
        pp.append(value)
        if value<=0:break
    return tau,pp
cert=[]
for sg,lo,hi in [(1,F(16327,10000),F(1633,1000)),(-1,F(704,1000),F(71,100))]:
    tau,pp=pivots(hi,sg,8,True);assert len(pp)==8 and all(p>0 for p in pp)
    _,lower=pivots(lo,sg,8,False);assert all(p>0 for p in lower[:-1]) and lower[-1]<0
    cert.append({'diagonal_sign':sg,'N':8,'tail_upper_bound':str(tau),'upper_lambda':str(hi),'upper_pivots':list(map(str,pp)),'lower_lambda':str(lo),'lower_pivots_until_first_negative':list(map(str,lower))})
# Work directly with signed sine modes.  A radial monomial derivative raises
# or lowers a mode; solve the Poisson equation before applying d_x again.
z=sp.symbols('z');checks=[]
def add_mode(d,n,c):
    if n==0:return
    if n<0:n=-n;c=-c
    d[n]=d.get(n,0)+c

def dx(modes,power):
    result={}
    for n,c in modes.items():
        add_mode(result,n+1,c*(power-n)/2)
        add_mode(result,n-1,c*(power+n)/2)
    return {n:sp.factor(c) for n,c in result.items()}
for n in range(1,24,2):
    source=dx({n:sp.Integer(1)},z-1)
    potential={k:sp.cancel(c/(k*k-z*z)) for k,c in source.items()}
    actual=dx(potential,z)
    expected={n:-sp.Rational(1,4) if n==1 else -sp.Rational(1,2),n+2:(n+1-z)/(4*(n+1+z))}
    if n>1:expected[n-2]=(n-1+z)/(4*(n-1-z))
    for k in set(actual)|set(expected):assert sp.cancel(actual.get(k,0)-expected.get(k,0))==0
    checks.append('Poisson then vertical derivative at odd mode '+str(n))
m,xi,n=sp.symbols('m xi n',real=True);zz=m+sp.I*xi
herm=sp.Rational(1,8)*((n+zz)/(n-zz)+(n-sp.conjugate(zz))/(n+sp.conjugate(zz)))
# Depending on the displayed orientation this is the conjugate of the proof's entry.
expected=(n*n+m*m+xi*xi)/(4*(n-zz)*(n+sp.conjugate(zz)))
assert sp.cancel(herm-expected)==0
checks.append('Hermitian entry exact complex algebra')
# Dense samples support, but do not replace, the all-frequency analytic comparison.
samples=[]
for mv in [2.1,2.5,np.sqrt(8),3.,3.5,3.9]:
    size=60;js=np.arange(1,size);ns=2*js;dd=np.full(size,.5);dd[0]=.25
    bs=(mv*mv+ns*ns)/(4*abs(ns*ns-mv*mv))
    jm=np.diag(dd)+np.diag(bs,1)+np.diag(bs,-1)
    jp=np.diag(-dd)+np.diag(bs,1)+np.diag(bs,-1)
    qm=np.linalg.eigvalsh(jm)[-1];qp=np.linalg.eigvalsh(jp)[-1]
    for xv in [0.,.05,.2,.7,2.,10.,100.]:
        zv=mv+1j*xv
        tm=np.diag(-dd.astype(complex))+np.diag((ns+zv)/(4*(ns-zv)),1)+np.diag((ns-zv)/(4*(ns+zv)),-1)
        hh=(tm+tm.conj().T)/2;ev=np.linalg.eigvalsh(hh)
        assert ev[-1]<=qp+2e-12 and -ev[0]<=qm+2e-12
        samples.append({'m':float(mv),'xi':xv,'finite_min':float(ev[0]),'finite_max':float(ev[-1]),'finite_Qminus':float(qm),'finite_Qplus':float(qp)})
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_certificates':cert,'exact_operator_checks':checks,'finite_matrix_supporting_samples':samples,'scope':'Independent exact rational Schur certificate with a proved infinite-tail bound, and independent Poisson-first angular derivation. Finite floating spectra are supporting samples only. No copied positive supersolution vector, no producer code, no interval-certified candidate.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'utc':result['utc'],'status':'PASS','certificates':len(cert),'exact_checks':len(checks),'matrix_samples':len(samples)}),flush=True)
