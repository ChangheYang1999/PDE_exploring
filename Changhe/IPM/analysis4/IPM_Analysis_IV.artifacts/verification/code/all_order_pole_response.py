"""Exact Cartesian response and all-index nonvanishing at delta=2/5, f1=sin(theta)."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq,fmpq_poly
import sympy as sp
import tuned_cartesian_exact as ce
from generic_response_identity import Rat
ROOT=Path('research/218_all_order_near_resonant_poles')

def coeffs(p):return [str(x) for x in p.coeffs()]
def evaluate(f,n):return f.n(n)/f.d(n)
def response(k,ff,gg):
    n=5*k
    generic=isinstance(k,Rat)
    e=ce.sine(ce.p(n)+1,(2,-2) if generic else 2*k-2)
    U={};V={}
    for r in range(1,6):
        total=ce.adv(e,ff[r])
        for s in range(1,r):total=total+ce.adv(V[s],ff[r-s])+ce.adv(gg[r-s],U[s])
        U[r]=total.scale(Rat(3)/(2*(n+r-1)));U[r].check_sine()
        if r<5:V[r]=ce.poisson(U[r])
    return 2*U[5].v.get((2,-1) if generic else (0,2*k-1),Rat.zero)

def main():
    start=time.monotonic()
    ce.K=ce.R=Rat;ce.k=Rat(fmpq_poly([0,1]));ce.MOD=None
    ce.p=lambda n:1-Rat(2)*n/5
    ff={1:ce.sine(ce.p(1),1)};gg={1:ce.poisson(ff[1])}
    for n in range(2,11):
        total=ce.F(ce.p(n),{})
        for i in range(1,n):total=total+ce.adv(gg[i],ff[n-i])
        ff[n]=total.scale(Rat(3)/(2*(n-1)));ff[n].check_sine()
        if n<10:gg[n]=ce.poisson(ff[n])
    R=ff[10].sine(1);assert R and R.n.degree()==R.d.degree()==0
    reference_R=fmpq('-8749424340298743474786211/74774522543657493340241516298240')
    assert evaluate(R,0)==reference_R
    print(json.dumps(dict(stage='low_fields',actual_elapsed_s=time.monotonic()-start)),flush=True)
    sig=response(ce.k,ff,gg)
    k,b=sp.symbols('k b')
    source=Path('research/130_period_five_tuning/verification/symbolic_responses.json')
    raw=source.read_bytes();expected=sp.cancel(sp.sympify(json.loads(raw)['sigma']).subs(b,0))
    an,ad=sp.fraction(expected)
    conv=lambda p:fmpq_poly([fmpq(str(x)) for x in reversed(sp.Poly(p,k).all_coeffs())])
    assert sig==Rat(conv(an),conv(ad))
    small_source=Path('research/130_period_five_tuning/verification/small_responses.json')
    smallraw=small_source.read_bytes();small={x['k']:sp.sympify(x['sigma']).subs(b,0) for x in json.loads(smallraw)['rows']}
    rows=[]
    for t in range(2,13):
        actual=response(t,ff,gg);assert actual.n.degree()==actual.d.degree()==0
        value=evaluate(actual,0);assert value
        assert value==fmpq(str(small[t]))
        generic_same=value==evaluate(sig,t)
        if t>=11:assert generic_same
        rows.append(dict(k=t,sigma=str(value),generic_same=generic_same,nonzero=True))
        print(json.dumps(dict(stage='finite',k=t,actual_elapsed_s=time.monotonic()-start)),flush=True)
    assert sig.n.degree()==sig.d.degree()
    sigma_infinity=sig.n[sig.n.degree()]/sig.d[sig.d.degree()]
    assert sigma_infinity==fmpq('-22057171011707398/16814963483136000000')
    shift=11
    x=fmpq_poly([shift,1]);pn=sig.n(x);pd=sig.d(x)
    nsign=1 if pn[0]>0 else -1;dsign=1 if pd[0]>0 else -1
    assert pn[0] and pd[0] and all(nsign*c>=0 for c in pn.coeffs()) and all(dsign*c>=0 for c in pd.coeffs())
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),status='PASS',R=str(reference_R),
        numerator=coeffs(sig.n),denominator=coeffs(sig.d),reference_formula_agreement=True,sigma_infinity=str(sigma_infinity),
        factorial_root_limit=str(abs(sigma_infinity)/10),
        finite_rows=rows,tail_from=shift,shifted_numerator=coeffs(pn),shifted_denominator=coeffs(pd),
        tail_numerator_sign=nsign,tail_denominator_sign=dsign,all_shifted_coefficients_have_stated_weak_sign=True,
        shifted_constant_terms_have_strict_sign=True,
        sources=[dict(path=str(source),sha256=sha256(raw).hexdigest()),dict(path=str(small_source),sha256=sha256(smallraw).hexdigest())],
        actual_elapsed_s=time.monotonic()-start,
        scope='All sigma_k are nonzero for integer k>=2. Generic formula used on k>=11; finite values checked separately.')
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    src=Path(__file__).read_bytes();(ROOT/'sources/all_order_pole_response.py').write_bytes(src)
    print(json.dumps(dict(status='PASS',actual_elapsed_s=result['actual_elapsed_s'],degrees=[sig.n.degree(),sig.d.degree()])),flush=True)

if __name__=='__main__':main()
