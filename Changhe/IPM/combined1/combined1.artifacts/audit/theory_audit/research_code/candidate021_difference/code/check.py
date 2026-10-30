"""Independent polar density difference and direct hypergeometric norm."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('t4_diff_polar', B/'code/polar.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def integral(A, exponent, ell):
    start = time.monotonic()
    N = f.V * A.numerator_v()
    assert N
    order = 0
    while N[order] == 0:
        order += 1
    N = f.Poly(list(N)[order:])
    b = exponent + order
    assert b > -1, (ell, exponent, order)
    D, rows = f.crt_data(A.powers)
    P, remainder = divmod(N, D)
    result = sum((f.ar(a/(b+j+1)) for j, a in enumerate(P)), arb(0))
    replay = P*D
    count = 0
    for a, k, Di, Ei, inverse in rows:
        Ri = divmod(remainder*inverse, Di)[1]
        local = Ri(f.Poly([-1/a, 1/a]))
        for j, coefficient in enumerate(local):
            if coefficient:
                assert k-j > 0
                result += f.ar(coefficient)*f.pole(str(b), str(a), k-j)
                count += 1
        replay += Ri*Ei
    assert replay == N
    assert result.is_finite() and result.rel_accuracy_bits() > 150
    row = {'ell_sum': ell, 'endpoint_v_order': order, 'b': str(b),
           'denominator_powers': list(A.powers), 'principal_parts': count,
           'polynomial_degree': P.degree(), 'exact_CRT_replay': True,
           'numerator_after_stripping': [str(q) for q in N],
           'value': result.str(110), 'accuracy_bits': result.rel_accuracy_bits(),
           'elapsed_seconds': time.monotonic()-start}
    print('GROUP', ell, 'order', order, 'bits', result.rel_accuracy_bits(), flush=True)
    return result, row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, default=2048)
    args = parser.parse_args()
    ctx.prec = args.bits
    start = time.monotonic()
    began = datetime.now(timezone.utc).isoformat()
    paths = [B/'data/candidate020.json', B/'data/candidate021.json',
             B/'source/N4_result.json', B/'source/N4_PROOF.md',
             B/'source/T4_parent_distance.json', B/'PROOF.md',
             Path(__file__), B/'code/polar.py', B/'code/rational.py']
    old, new, peer = [json.loads(p.read_text()) for p in paths[:3]]
    assert sha(paths[0]) == peer['parent_raw_sha256'] == 'bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf'
    assert sha(paths[1]) == peer['successor_raw_sha256'] == 'c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8'
    c = Q(old['cl_exact'])
    assert Q(new['cl_exact']) == c == Q(4076476460239181,2251799813685248)
    delta = 1-1/c
    assert Q(2,5) < delta < Q(1,2)
    entries = {}
    for data, sign in [(new, 1), (old, -1)]:
        for g in data['generators']:
            j, m, gs = g['j'], g['m'], tuple(g['spec'])
            assert isinstance(j,int) and isinstance(m,int) and min(j,m)>=0
            assert gs[0] in {'mono','leg','legq','legqs'}
            assert all(isinstance(x,int) and x>=0 for x in gs[1:])
            if gs[0] == 'legqs': assert gs[4] in [25,50]
            key=(j,m,gs)
            entries[key]=entries.get(key,Q(0))+sign*Q(g['coef'])
    entries={k:v for k,v in entries.items() if v}
    prefix={}
    for (j,m,gs), v in entries.items():
        endpoint_order=gs[3] if gs[0] in {'legq','legqs'} else 0
        if j<4 and endpoint_order==0:
            prefix[j,m]=prefix.get((j,m),Q(0))+v
    assert all(v==0 for v in prefix.values())
    assert len(entries)==peer['difference_nonzero_generator_count']
    data={'cl_exact':str(c),'generators':[{'j':j,'m':m,'spec':list(gs),'coef':str(v)} for (j,m,gs),v in sorted(entries.items())]}
    with (B/'data/exact_difference.json').open('x') as stream:
        json.dump(data,stream,indent=2); stream.write('\n')
    c1,d1,rho,psi=f.fields(data)
    assert c1==c and d1==delta
    endpoints=[]
    for name, fields in [('rho',rho),('psi',psi)]:
        for (j,n),A in fields.items():
            if j<4:
                assert A.exact_value(Q(1))==0
                endpoints.append([name,j+1,n,'0'])
    checks=[]
    for row in peer['point_checks']['points']:
        values=f.evaluation(c,delta,rho,psi,row['x'],row['y'])
        for field in ['rho','u1','u2']:
            expected=arb(row['fields'][field]['Cartesian'])
            assert values[field].overlaps(expected)
            checks.append({'x':row['x'],'y':row['y'],'field':field,'value':values[field].str(110),'overlap':True})
    print('FIELDS',len(rho),len(psi),'POINTS',len(checks),'seconds',time.monotonic()-start,flush=True)
    by_mode={}
    for (j,n),A in rho.items():by_mode.setdefault(n,[]).append((j+1,A))
    groups={};ordered=0
    for rows in by_mode.values():
        for i,(ell,A) in enumerate(rows):
            for k,(ell2,C) in enumerate(rows[i:],i):
                multiplicity=1 if i==k else 2
                f.add(groups,ell+ell2,multiplicity*A*C)
                ordered+=multiplicity
    groups={k:v for k,v in groups.items() if v}
    assert ordered==peer['norm']['ordered_pairs']
    assert len(groups)==peer['norm']['group_count']
    reference={row['ell_sum']:row for row in peer['norm']['groups']}
    total=arb(0);records=[]
    for ell,A in sorted(groups.items()):
        value,row=integral(A,ell*delta/2-3,ell)
        assert Q(row['b'])==Q(reference[ell]['b'])
        assert row['endpoint_v_order']==reference[ell]['endpoint_v_order']
        assert value.overlaps(arb(reference[ell]['integral_ball']))
        row['peer_overlap']=True
        total+=value;records.append(row)
    square=arb.pi()/2*total
    assert square>0
    norm=square.sqrt()
    assert norm.rel_accuracy_bits()>150
    assert total.overlaps(arb(peer['norm']['sum_ball']))
    assert square.overlaps(arb(peer['norm']['square_ball']))
    assert norm.overlaps(arb(peer['norm']['norm_ball']))
    tau=Q(peer['norm']['tau_upper_exact'])
    assert norm<f.ar(tau)
    parent=json.loads((B/'source/T4_parent_distance.json').read_text())
    floor=Q(parent['strict_lower_exact'])
    screens=[]
    for row in peer['screens']:
        assert floor==Q(row['strict_parent_distance_floor'])
        b=Q(row['b']);margin=floor-b
        assert margin>=0 and Q(row['d_minus_b'])==margin
        failed=bool(square>f.ar(margin**2))
        passed=bool(square<=f.ar(margin**2))
        assert failed and not passed
        screens.append({'ceiling_id':row['ceiling_id'],'b':str(b),'parent_floor':str(floor),'margin':str(margin),'certified_square_above_margin_squared':failed,'screen_passed':passed})
    output={'utc_start':began,'utc':datetime.now(timezone.utc).isoformat(),
        'inputs':{str(p):sha(p) for p in paths},'precision_bits':ctx.prec,
        'prefix_P_verified':True,'prefix_checks':[[j,m,str(v)] for (j,m),v in sorted(prefix.items())],
        'nonzero_generator_differences':len(entries),'endpoint_checks':endpoints,
        'exact_difference_sha256':sha(B/'data/exact_difference.json'),
        'point_checks':checks,'density_terms':len(rho),'stream_terms':len(psi),
        'ordered_pairs':ordered,'groups':records,'group_count':len(records),
        'sum':total.str(110),'square':square.str(110),'norm':norm.str(110),
        'norm_accuracy_bits':norm.rel_accuracy_bits(),'tau_upper_exact':str(tau),
        'screens':screens,'elapsed_seconds':time.monotonic()-start,
        'verdict':'CONFIRMED compatibility and independent whole-plane norm; all three sufficient screens fail'}
    with (B/'verification/result.json').open('x') as out:
        json.dump(output,out,indent=2);out.write('\n')
    print('DONE',output['utc'],norm.str(45),'seconds',output['elapsed_seconds'],flush=True)

if __name__=='__main__':main()
