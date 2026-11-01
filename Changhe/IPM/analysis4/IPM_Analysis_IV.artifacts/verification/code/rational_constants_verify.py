"""Independent Arb certificate for the finite rational-parameter theorem."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
from flint import arb, ctx
from brjuno_constants_verify import ball, continued_fraction, convergents


def main():
    ctx.prec=512
    target=Path('research/22_rational_finite_bound')
    source=Path('research/02_candidate007/data/leading_exact.json')
    raw=source.read_bytes(); leading=json.loads(raw)
    deltaq=Fraction(leading['delta']); delta=ball(deltaq)
    aa=continued_fraction(deltaq/2); cv=convergents(aa)
    qs=[x[1] for x in cv]
    assert Fraction(*cv[-1])==deltaq/2
    B=sum((arb(qs[k+1]).log()/qs[k] for k in range(len(qs)-1)),arb(0))
    lam=ball(Fraction(3,2))+delta/2+1/delta
    c=1/(1-delta); N=qs[-1]-1
    amp=sum((abs(Fraction(v)) for v in leading['density'].values()),Fraction())
    rows=[]
    for name,F,L in [('sin1',Fraction(1),1),('candidate007_raw',amp,19)]:
        K=2*lam*(L+2)/(c-1)
        A=8*K*(2*B).exp()*ball(F)/delta
        pref=lam*(L+2)*A/(64*K*K)
        log2res=(2*pref*N).log()/arb(2).log()-N
        Aupper=int(A.upper().floor().unique_fmpz())+1
        log10R=(2*A).log()/(delta*arb(10).log())
        E=int((-log2res).lower().floor().unique_fmpz())
        assert A < Aupper
        assert log2res < -E
        assert log2res < -8150000000000000
        rows.append(dict(profile=name,F_exact=str(F),L=L,K=str(K),A=str(A),A_strict_integer_upper=Aupper,
                         half_ratio_radius_log10=str(log10R),residual_prefactor=str(pref),N=N,
                         log2_residual_upper_bound=str(log2res),residual_strict_binary_exponent=E))
        print(name,'A <',Aupper,'log10 radius',log10R.str(18),'residual < 2^-'+str(E),flush=True)
    theory=Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md')
    tbytes=theory.read_bytes(); (target/'sources/lead_theory_at_audit.md').write_bytes(tbytes)
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),profile_source=str(source),
             profile_sha256=sha256(raw).hexdigest(),lead_theory_sha256=sha256(tbytes).hexdigest(),
             arithmetic='Arb 512-bit with exact rational input and exact continued fractions',
             delta_exact=str(deltaq),continued_fraction=aa,convergent_denominators=qs,
             finite_Brjuno_sum=str(B),lambda_delta=str(lam),rows=rows)
    (target/'verification/rational_constants.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
