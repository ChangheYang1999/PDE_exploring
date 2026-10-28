"""Exact endpoint recombination of the original producer remainder bounds."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
R=Path(__file__).resolve().parents[1];B=R/'05_team_audit/note14_certificate/producer_fine_a75'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ep(x,up=False):
    assert x.is_finite();return Q(str((x.upper() if up else x.lower()).fmpq()))
def rec(x):return dict(lower=str(ep(x)),upper=str(ep(x,True)),display=x.str(40))
def dec(x,n=10):
    k=(x*10**n).__floor__();return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
    audit=json.loads((B/'import_audit.json').read_text());d=json.loads((B/'n14_a34_c30_ff.json').read_text())
    for n,h in audit['sha256'].items():assert sha(R/n)==h
    ctx.prec=384;a=arb(d['alpha']);p=d['params'];rm=arb(str(p['rho_min']));eta=arb(str(p['rho_m']));radius=arb(str(p['rho_max']))
    inner=rm**a/a+rm*rm/(2*(1-rm)**2)*(arb(1)/2+rm**a)
    sliver=arb(2)**(a+3)*eta**(a+3)/(arb.pi()*(a+3)*(1-eta*eta).sqrt())
    tail=arb(2)**a*(radius/(radius-arb(1)/2))**3*radius**(a-1)/(1-a)
    n,m=audit['totals']['near'],audit['totals']['middle'];error=2*ep(inner,True)+ep(sliver,True)+ep(tail,True)
    lo=2*Q(n['lower'])+Q(m['lower'])-error;hi=2*Q(n['upper'])+Q(m['upper'])+error
    # The producer's presentation balls are used only as consistency checks.
    for key,tot in [('near',n),('rest',m)]:
        ball=arb(d[key]);assert ep(ball)<=Q(tot['lower'])<=Q(tot['upper'])<=ep(ball,True)
    pb=arb(d['I0']);assert ep(pb)<=lo<=hi<=ep(pb,True)
    producerlo=arb(d['I0_lower']);producerhi=arb(d['I0_upper'])
    # Exact summation of the serialized task intervals may be tighter than the
    # original 80-bit accumulation. Report both endpoints without narrowing either.
    exact=max(Q(0),lo,-hi)+Q(1,2)
    src={str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'PROOF.md',B/'import_audit.json',B/'n14_a34_c30_ff.json']}
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='EXACT_ORIGINAL_RECOMBINATION_PASSED',scope='All imported task balls summed exactly; original absolute pole, sliver and exterior bounds; not a new cell replay',inner=rec(inner),sliver=rec(sliver),tail=rec(tail),I0=dict(lower=str(lo),upper=str(hi),lower_display=dec(lo,16),upper_display=dec(hi+Q(1,10**16),16)),safe_D_lower=dec(exact),exact_D_lower=str(exact),producer_I0_lower=rec(producerlo),producer_I0_upper=rec(producerhi),lower_improvement_over_producer_upper_endpoint=str(lo-ep(producerlo,True)),sha256=src)
    (B/'original_recombination.json').write_text(json.dumps(out,indent=2)+'\n');print(out['time_utc'],out['verdict'],out['safe_D_lower'])
if __name__=='__main__':main()
