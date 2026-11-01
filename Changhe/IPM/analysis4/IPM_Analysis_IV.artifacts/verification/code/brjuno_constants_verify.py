"""Certify continued-fraction constants using exact recurrences and Arb.

The tail estimate is proved in research/13_lead_theory_audit/PROOF.md.
No numerical continued-fraction extraction from rounded real numbers is used.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
from flint import arb, fmpq, ctx


def ball(q):
    q = Fraction(q)
    return arb(fmpq(q.numerator, q.denominator))


def continued_fraction(q):
    values = []
    while q.denominator != 1:
        a = q.numerator // q.denominator
        values.append(a)
        q = 1 / (q-a)
    values.append(q.numerator)
    return values


def convergents(aa):
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    result = []
    for a in aa:
        p, q = a*pm1+pm2, a*qm1+qm2
        result.append((p,q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    return result


def brjuno_bounds(aa, terms, tail_max):
    cv = convergents(aa)
    assert len(cv) >= terms+1
    q = [v[1] for v in cv]
    lower = sum((arb(q[k+1]).log()/q[k] for k in range(terms)), arb(0))
    tail = (4*arb(q[terms]).log()+14*arb(tail_max+1).log())/q[terms]
    return lower, lower+tail, q


def str_interval(lo, hi):
    return {'lower_ball': str(lo), 'upper_ball': str(hi)}


def main():
    ctx.prec = 512
    exact = Path('research/02_candidate007/data/leading_exact.json')
    data = json.loads(exact.read_text())
    a1 = sum((abs(Fraction(a)) for a in data['density'].values()), Fraction())
    delta_ref = Fraction(data['delta'])
    ref_cf = continued_fraction(delta_ref/2)
    expected = [0,4,2,7,2,1,5,8,3,1,3,3,2,4,2,1,1,1,43,17,1,2,3,7,8,1,3,1,1,3,5,2]
    assert ref_cf == expected
    ref_cv = convergents(ref_cf)
    pm, qm = ref_cv[-1]
    pp, qp = ref_cv[-2]
    assert Fraction(pm,qm) == delta_ref/2
    sd = arb(5).sqrt()
    phi = (1+sd)/2
    alpha_star = (pm*phi+pp)/(qm*phi+qp)
    distance = 1/(arb(qm)*(qm*phi+qp))
    assert abs(alpha_star-ball(delta_ref/2)).overlaps(distance)
    assert distance < ball(Fraction(1,10**32))
    periodic = [0,4]+[2,8]*45
    lo, hi, q = brjuno_bounds(periodic,80,8)
    p25, _, _ = brjuno_bounds(periodic,25,8)
    assert hi-p25 < ball(Fraction(4,10**14))
    star_seq = ref_cf+[1]*90
    slo, shi, sq = brjuno_bounds(star_seq,100,1)
    s31, _, _ = brjuno_bounds(star_seq,31,1)
    rows = []
    delta = 1/sd
    c = 1/(1-delta)
    lam = ball(Fraction(3,2))+delta/2+1/delta
    for name, amp, L in [('sin1',Fraction(1),1),('sin1_plus_half_sin3',Fraction(3,2),3),('candidate007_raw',a1,19),('candidate007_l1_normalized',Fraction(1),19)]:
        K = 2*lam*(L+2)/(c-1)
        Alo = 8*K*(2*lo).exp()*ball(amp)/delta
        Ahi = 8*K*(2*hi).exp()*ball(amp)/delta
        Rlo = Alo.log()/(delta*arb(10).log())
        Rhi = Ahi.log()/(delta*arb(10).log())
        rows.append({'name':name,'amplitude_l1_exact':str(amp),'L':L,'K':str(K),'A':str_interval(Alo,Ahi),'log10_R0':str_interval(Rlo,Rhi)})
    out = {
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'profile_input':exact.as_posix(),'profile_input_sha256':sha256(exact.read_bytes()).hexdigest(),
        'arithmetic':'exact rational continued fractions; Arb 512-bit logarithms and exponentials',
        'tail_bound':'sum from k=N <= (4 log q_N + 14 log(M+1))/q_N when all later partial quotients <= M',
        'sqrt5':{'alpha':'1/(2*sqrt(5))','partial_quotients':'[0;4,2,8,2,8,...]','first_denominators':q[:8], 'terms':80,'B':str_interval(lo,hi),'tail_after_25_terms':str_interval(lo-p25,hi-p25),'tail_after_25_lt_4e_minus14':True,'lambda_delta':str(lam)},
        'near_reference':{'reference_cf':ref_cf,'p31':pm,'q31':qm,'p30':pp,'q30':qp,'new_alpha':'(p31*phi+p30)/(q31*phi+q30), phi=(1+sqrt(5))/2','absolute_alpha_difference':str(distance),'delta_difference_lt_2e_minus32':True,'terms':100,'B':str_interval(slo,shi),'tail_after_31_terms':str_interval(slo-s31,shi-s31),'tail_after_31_lt_1e_minus14':bool(shi-s31 < ball(Fraction(1,10**14)))},
        'sqrt5_constant_table':rows,
    }
    target = Path('research/13_lead_theory_audit/verification/brjuno_constants.json')
    target.write_text(json.dumps(out,indent=2)+'\n')
    print('B(sqrt5) =',lo.str(25))
    print('Tail after 25 =',(hi-p25).str(12))
    print('B(near reference) =',slo.str(25))
    print('Tail after 31 =',(shi-s31).str(12))
    for row in rows:
        print(row['name'],row['K'][:25],row['A']['lower_ball'][:25],row['log10_R0']['lower_ball'][:25])

if __name__ == '__main__':
    main()
