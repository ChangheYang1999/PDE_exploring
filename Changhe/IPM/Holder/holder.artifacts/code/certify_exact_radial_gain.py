"""Directed scalar endpoints from the exact radial minorant on fixed disks."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import comb
from flint import arb, ctx
import argparse, hashlib, json

ROOT = Path(__file__).resolve().parents[1]
RAD = ROOT / '08_improved_upper_bounds/local_projection/strict_increment/larger_disks/radial_density'
EXACT = RAD.parent / 'exact_radial_density'
OUT = EXACT / 'numerical_values'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def load(path): return json.loads(path.read_text())
def endpoint(value, upper=False):
    return Q(str((value.upper() if upper else value.lower()).fmpq()))
def ceil10(value):
    scaled = value * 10**10
    k = -((-scaled.numerator) // scaled.denominator)
    return f'{k // 10**10}.{k % 10**10:010d}'
def linear_interval(constant, coefficient, lo, hi):
    return (constant + coefficient * lo, constant + coefficient * hi) if coefficient >= 0 else (constant + coefficient * hi, constant + coefficient * lo)
def bn_coefficients(n):
    c = Q(3, 4)
    constant = (-c)**n * (1/c - 1)
    constant += sum((Q(comb(n, j)) * (-c)**(n-j) * (1-c**(j-1)) / (j-1) for j in range(2, n+1)), Q(0))
    return constant, n * (-c)**(n-1)
def bn_ball(n, logarithm):
    c = arb(3)/4
    return ((-c)**n * (1/c - 1) + n * (-c)**(n-1) * logarithm
            + sum((comb(n, j) * (-c)**(n-j) * (1-c**(j-1))/(j-1) for j in range(2, n+1)), arb(0)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', required=True)
    ap.add_argument('--analytic-ledger', required=True)
    ap.add_argument('--analytic-acceptance', default=str((EXACT/'verification/accepted.json').relative_to(ROOT)))
    ap.add_argument('--cross-acceptance', default='05_team_audit/cross2048/recombination/verification/accepted.json')
    ap.add_argument('--cross-ledger', default='V190')
    ap.add_argument('--out', default=str(OUT.relative_to(ROOT)))
    args = ap.parse_args()
    destination = ROOT / args.out
    assert destination.is_relative_to(ROOT) and (destination/'PROOF.md').is_file()
    hashes = {}
    def bind(path):
        path = path.resolve(); assert path.is_relative_to(ROOT)
        hashes[str(path.relative_to(ROOT))] = sha(path)
    def accepted(relative, ledger):
        path = ROOT / relative; record = load(path)
        assert record['ledger'] == ledger and record['verdict'] == 'CONFIRMED'
        bind(path)
        for name, digest in record['sha256'].items():
            assert sha(ROOT/name) == digest, name
            bind(ROOT/name)
        return record
    analytic = accepted(str((RAD/'verification/accepted.json').relative_to(ROOT)), 'V195')
    for path in [RAD/'PROOF.md', RAD/'cutoff_plan/PROOF.md', RAD/'symmetric_concavity/PROOF.md', RAD/'symmetric_concavity/fourth_moment/PROOF.md']:
        assert analytic['sha256'][str(path.relative_to(ROOT))] == sha(path)
    new_analytic = accepted(args.analytic_acceptance, args.analytic_ledger)
    assert new_analytic['sha256'][str((EXACT/'PROOF.md').relative_to(ROOT))] == sha(EXACT/'PROOF.md')
    cross = accepted(args.cross_acceptance, args.cross_ledger)
    accepted('08_improved_upper_bounds/explicit_second_term/verification/accepted.json', 'V118')
    sources = {}
    def add(a, upper, radius, kind, source):
        a = Q(a); assert a not in sources
        sources[a] = dict(upper=Q(upper), radius=Q(radius), kind=kind, source=source)
    relative = '08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json'
    bind(ROOT/relative)
    for row in load(ROOT/relative)['rows']:
        if Q(row['alpha']) in [Q(1, 1000), Q(1, 100)]:
            d = row['bounds']['J_D']; assert 0 < Q(d['rho']) <= Q(1, 3)
            add(row['alpha'], d['upper'], d['rho'], 'retained cutoff', relative)
    relative = 'data/circle_composite_upper_n768.json'
    circle = load(ROOT/relative); bind(ROOT/relative)
    assert circle['source_sha256'] == sha(ROOT/'code/combine_circle_upper.py')
    bind(ROOT/'code/combine_circle_upper.py')
    for name, digest in circle['input_sha256'].items():
        assert sha(ROOT/name) == digest; bind(ROOT/name)
    comparison = load(ROOT/'data/reflection_n768_comparison.json')
    assert comparison['all_inside'] and comparison['comparisons'] == 170
    bind(ROOT/'data/reflection_n768_comparison.json')
    for name, digest in comparison['input_sha256'].items():
        assert sha(ROOT/name) == digest; bind(ROOT/name)
    for row in circle['rows']:
        if Q(row['alpha']) in [Q(1, 20), Q(1, 10)]:
            add(row['alpha'], row['safe_upper_D'], '1/2', 'unperturbed local', relative)
    for row in cross['rows']:
        add(row['alpha'], row['safe_upper_D'], '1/2', 'unperturbed local', args.cross_acceptance)
    assert sorted(sources) == [Q(1,1000), Q(1,100), Q(1,20), Q(1,10), Q(1,5), Q(3,10), Q(1,2), Q(3,4), Q(9,10), Q(99,100)]
    b3, k3 = bn_coefficients(3); b5, k5 = bn_coefficients(5)
    jr, jlog = 2*b3, 2*k3
    kr, kl = b5/2, k5/2
    assert (jr,jlog,kr,kl) == (Q(-31,32),Q(27,8),Q(-233,1024),Q(405,512))
    t = Q(1,7); terms = 256
    log_lo = 2 * sum((t**(2*n+1)/(2*n+1) for n in range(terms)), Q(0))
    log_hi = log_lo + 2*t**(2*terms+1)/((2*terms+1)*(1-t*t))
    jl, jh = linear_interval(jr, jlog, log_lo, log_hi)
    klow, khigh = linear_interval(kr, kl, log_lo, log_hi)
    ctx.prec = 384
    log_ball = (arb(4)/3).log()
    J = arb(str(jr))+arb(str(jlog))*log_ball
    K = arb(str(kr))+arb(str(kl))*log_ball
    assert endpoint(log_ball) <= log_lo <= log_hi <= endpoint(log_ball, True)
    assert Q(1,512) < endpoint(J) <= jl <= jh <= endpoint(J, True)
    old_J = arb(653)/288-arb(63)/8*log_ball
    old_K = arb(56627)/138240-arb(729)/512*log_ball
    assert endpoint(old_J, True) < endpoint(J) and endpoint(old_K, True) < endpoint(K)
    assert 0 < endpoint(K) <= klow <= khigh <= endpoint(K, True)
    j_text, k_text = J.str(45), K.str(45)
    rows = []
    for a, source in sorted(sources.items()):
        ctx.prec = 384
        s = source['radius']; p = a*(1-a); q = p*(2-a)*(3-a)
        c2 = s**4/(512*(1-s)**2) if source['kind'] == 'retained cutoff' else Q(0)
        c4 = s**6/(49152*(1-s)**2) if source['kind'] == 'retained cutoff' else Q(0)
        eta2 = arb(str(p))*(J*arb(str(s*s))-arb(str(c2)))
        eta4 = arb(str(q))*(K*arb(str(s**4))-arb(str(c4)))
        gain = eta2+eta4
        lower, upper = endpoint(gain), endpoint(gain, True)
        qlower, qupper = endpoint(eta2), endpoint(eta2, True)
        exact2lo, exact2hi = p*(jl*s*s-c2), p*(jh*s*s-c2)
        exact4lo, exact4hi = q*(klow*s**4-c4), q*(khigh*s**4-c4)
        assert 0 < qlower <= exact2lo <= exact2hi <= qupper
        assert 0 < endpoint(eta4) <= exact4lo <= exact4hi <= endpoint(eta4, True)
        assert 0 < lower <= exact2lo+exact4lo <= exact2hi+exact4hi <= upper
        gain_text, fourth_text = gain.str(45), eta4.str(45)
        ctx.prec = 768
        log2 = arb(4).log()-arb(3).log()
        j2 = 2*bn_ball(3, log2)
        k2 = bn_ball(5, log2)/2
        fresh = arb(str(p))*(j2*arb(str(s*s))-arb(str(c2))) + arb(str(q))*(k2*arb(str(s**4))-arb(str(c4)))
        assert lower <= endpoint(fresh) <= endpoint(fresh, True) <= upper
        value = source['upper']-lower; safe = ceil10(value)
        quadratic = ceil10(source['upper']-qlower)
        assert value <= Q(safe) < value+Q(1,10**10)
        assert Q(safe) <= Q(quadratic) < source['upper']
        rows.append(dict(alpha=str(a), radius=str(s), kind=source['kind'], source=source['source'], previous_upper_D=str(source['upper']), safe_upper_D=safe, quadratic_upper_D=quadratic, gain_lower=str(lower), gain_upper=str(upper), gain_ball=gain_text, fourth_moment_gain_ball=fourth_text, exact_rational_gain_lower=str(exact2lo+exact4lo), exact_rational_gain_upper=str(exact2hi+exact4hi)))
    for path in [destination/'PROOF.md', Path(__file__)]: bind(path)
    record = dict(time_utc=datetime.now(timezone.utc).isoformat(), ledger=args.ledger, verdict='CONFIRMED', precision_bits=[384,768], logarithm_terms=terms, J=dict(ball=j_text,lower=str(jl),upper=str(jh)), K=dict(ball=k_text,rational_coefficient=str(kr),logarithm_coefficient=str(kl),lower=str(klow),upper=str(khigh)), rows=rows, sha256=hashes, method='Confirmed exact radial minorant and reflection theorem, exact positive atanh series, two independently grouped ball computations, exact upward decimal rounding', scope='Ten finite diagonal endpoints; no new quadrature, no numerical sharpness claim')
    (destination/'accepted.json').write_text(json.dumps(record,indent=2)+'\n')
    print(record['time_utc'], args.ledger, 'CONFIRMED')
    for row in rows: print(row['alpha'], row['safe_upper_D'], row['gain_ball'])

if __name__ == '__main__': main()
