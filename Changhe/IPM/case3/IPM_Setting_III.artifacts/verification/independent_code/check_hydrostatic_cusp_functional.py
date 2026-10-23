"""Manufactured verification for the own exact cusp functional, before state use."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
from hydrostatic_cusp_functional import kernel,rational_data,cusp,monomial_cusp,tail,cutoff_quadrature,exactmp
ROOT=Path('research/hydrostatic_cusp_row_audit');V=ROOT/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
mp.mp.dps=160
ps=[F(1,5),F(1,3),F(1,2),F(3,4),1-1/F(float(1.5-2**-52))]
rows=[]
for p in ps:
    w=kernel(p,9);check(str(p)+' first kernels',w[0]==1 and w[1]==-(p+5)/(1-p))
    zero=[(p+5)/(2*(p+2)),(1-p)/(2*(p+2))];zd=rational_data(p,zero)
    check(str(p)+' exact zero and normalized K',zd['Cp_rational']==0 and zd['K']==1)
    check(str(p)+' zero by monomial integration',abs(monomial_cusp(p,zero)[0])<mp.mpf('1e-140'))
    for k in range(9):
        b=[F(0)]*k+[F(1)];d=rational_data(p,b);cp=cusp(p,b);direct,abssum=monomial_cusp(p,b)
        er=abs(cp-direct)/max(1,abs(cp));check(str(p)+' k'+str(k)+' direct monomial',er<mp.mpf('1e-130'),float(er))
        check(str(p)+' k'+str(k)+' exact Q',d['Q']==(-1)**k*(p-1-4*k*k))
        rec=dict(p=str(p),k=k,Cp=mp.nstr(cp,65),monomial_error=mp.nstr(er,10),quadrature=[])
        for S in [8,32,128]:
            tv,bd=tail(p,b,S,20,d);v64=cutoff_quadrature(p,b,S,64);v96=cutoff_quadrature(p,b,S,96)
            errs=[abs(exactmp(v)+tv-cp)/max(1,abs(cp))for v in [v64,v96]]
            check(str(p)+' k'+str(k)+' cutoff'+str(S),max(errs)<mp.mpf('3e-10'),[float(e)for e in errs])
            check(str(p)+' k'+str(k)+' refinement'+str(S),abs(v64-v96)<3e-10*max(1,float(abs(cp))),abs(v64-v96))
            rec['quadrature'].append(dict(S=S,order64=v64,order96=v96,tail=mp.nstr(tv,65),tail_remainder_bound=mp.nstr(bd,10),normalized_errors=list(map(float,errs))))
        for S in [5,11]:
            v20,b20=tail(p,b,S,20,d)
            for L in [4,8,12]:
                value,bound=tail(p,b,S,L,d);err=abs(v20-value)
                check(str(p)+' k'+str(k)+' tailbound'+str(S)+' L'+str(L),err<=bound+b20,dict(error=float(err),bound=float(bound)))
        rows.append(rec)
# Symbolic counterexample checks, separate from the cusp kernel implementation.
import sympy as sp
s,p,x,y=sp.symbols('s p x y',positive=True)
Ffun=s*(1+s)**(p-2);eta=y*(x*x+y*y)*(1+x*x+y*y)**(p-2)
check('perturbation first derivative at zero',sp.diff(eta,y).subs({x:0,y:0})==0)
check('axis second derivative primitive',sp.simplify(sp.diff(eta,x,2).subs(x,0)-2*y*sp.diff(Ffun,s).subs(s,y*y))==0)
check('r2 shift -(c-1)',sp.simplify((2*p-1)/p-1+(1/p-1))==0)
for pp in [F(1,5),F(1,3),F(3,4)]:
    v=exactmp(pp)
    # x=y/(1-y) is only an integration substitution, no endpoint or map code reused.
    def integrand(t):
        if t==1:return mp.mpf(0)
        z=t/(1-t);return 2*z*(1+z*z)**(v-3)*(1+(v-1)*z*z)/(1-t)**2
    moment=mp.quad(integrand,[0,mp.mpf('.5'),mp.mpf('.9'),1])
    check(str(pp)+' perturbation preserves center strain',abs(moment)<mp.mpf('1e-60'),mp.nstr(moment,15))
result=dict(status='PASS'if all(a['passed']for a in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,module_sha256=sha('independent_code/hydrostatic_cusp_functional.py'),driver_sha256=sha(__file__),proof_sha256=sha(ROOT/'PROOF.md'))
(V/'CUSP_GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count'],flush=True);print([a for a in checks if not a['passed']],flush=True)
if result['status']!='PASS':raise SystemExit(1)
