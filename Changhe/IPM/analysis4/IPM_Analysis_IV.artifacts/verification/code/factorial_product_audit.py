"""Independent Laurent-column audit of realized factorial product losses."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import factorial, lgamma, log10, log
import argparse, gzip, heapq, json, pickle, random, sys, time
sys.dont_write_bytecode = True
from flint import arb, arb_poly, fmpq, ctx
from stream_precision_audit import unpack
from laurent_log_audit import L, Q, parse

ROOT = Path('research/78_factorial_product_losses')
text = lambda x: x.str(30, radius=True)


def angular(col, M, even):
    a, c = [arb(0) for _ in range(2*M+1)], [arb(0) for _ in range(2*M+1)]
    for j, v in enumerate(col):
        m = 2*j if even else 2*j+1
        if not m or v == 0:
            continue
        assert m <= M
        a[M+m], a[M-m] = v/2, -v/2
        c[M+m] = c[M-m] = m*v/2
    return arb_poly(a), arb_poly(c)


def norm(A, M):
    return 2*sum((abs(A[M+m]) for m in range(1, M+1, 2)), arb(0))


def exact_contains(x, q):
    m, e = x.mid().man_exp()
    r, s = x.rad().man_exp()
    a, b = Q(int(m))*Q(2)**int(e), Q(int(r))*Q(2)**int(s)
    return a-b <= q <= a+b


def synthetic():
    rng = random.Random(781031)
    count = 0
    for trial in range(80):
        i, j = rng.randrange(1, 12), rng.randrange(1, 12)
        u, v = rng.randrange(5), rng.randrange(5)
        P, p = Q(2)-Q(2*i, 3), Q(1)-Q(2*j, 3)
        g = [Q(0)]+[Q(rng.randrange(-6, 7), rng.randrange(1, 8)) for _ in range(3)]
        f = [Q(rng.randrange(-6, 7), rng.randrange(1, 8)) for _ in range(4)]
        Ag, Cg = angular([arb(x) for x in g], 6, True)
        Af, Cf = angular([arb(x) for x in f], 7, False)
        x, y = Ag*Cf, Cg*Af
        out = [arb_poly([]) for _ in range(u+v+1)]
        out[u+v] += arb(P)*x-arb(p)*y
        if u+v:
            out[u+v-1] += u*x-v*y
        G = parse(P, {2*k: [Q(0)]*u+[z] for k, z in enumerate(g) if k})
        F = parse(p, {2*k+1: [Q(0)]*v+[z] for k, z in enumerate(f)})
        expected = G.X()*F.Y()-G.Y()*F.X()
        for q in range(len(out)):
            for m in range(1, 14, 2):
                z = 2*expected.a[q][expected.M+m] if q < len(expected.a) and m <= expected.M else Q(0)
                assert exact_contains(2*out[q][13+m], z), (trial, q, m)
                count += 1
    return dict(random_seed=781031, exact_cartesian_cases=80, coefficient_checks=count)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--positive-orders', default='120,180,220,250,260,270')
    ap.add_argument('--rank-orders', default='270')
    ap.add_argument('--rank-count', type=int, default=256)
    ap.add_argument('--rank-subsets', default='all,positive')
    ap.add_argument('--seconds', type=float, default=480)
    ap.add_argument('--input', default='../a4-num/ckpt/log_sin1_c3_p512.pkl')
    ap.add_argument('--resume-input', action='store_true')
    a = ap.parse_args()
    started = time.monotonic()
    ctx.prec = 640
    (ROOT/'verification').mkdir(parents=True, exist_ok=True)
    (ROOT/'sources').mkdir(exist_ok=True)
    syn = synthetic()
    print(json.dumps(dict(synthetic=syn, elapsed_s=time.monotonic()-started)), flush=True)
    snapshot = ROOT/'verification/input_checkpoint.pkl.gz'
    if a.resume_input:
        raw = gzip.decompress(snapshot.read_bytes())
    else:
        raw = Path(a.input).read_bytes()
        snapshot.write_bytes(gzip.compress(raw, compresslevel=1, mtime=0))
    digest, bytecount = sha256(raw).hexdigest(), len(raw)
    state = pickle.loads(raw)
    del raw
    assert state['ring'] == 'arb' and state['prec'] == 512
    assert (state['A'], state['B']) == ('2', '3')
    N = max(state['f'])
    fields, cnorms, dnorms, fnorms, pnorms = {}, {}, {}, {}, {}
    factors = [arb(factorial(q)) for q in range(N+1)]
    for field in ['f', 'g']:
        fields[field], cnorms[field], dnorms[field], fnorms[field], pnorms[field] = {}, {}, {}, {}, {}
        even = field == 'g'
        for n, cols in sorted(state[field].items()):
            decoded = [[arb(*unpack(z)) for z in col] for col in cols]
            fields[field][n] = decoded
            norms = [sum(map(abs, col), arb(0)) for col in decoded]
            derivs = [sum(((2*j if even else 2*j+1)*abs(z) for j, z in enumerate(col)), arb(0)) for col in decoded]
            cnorms[field][n], dnorms[field][n] = norms, derivs
            fnorms[field][n] = sum((factors[q]*v for q, v in enumerate(norms)), arb(0))
            pnorms[field][n] = sum((factors[q]*v for q, v in enumerate(norms) if q), arb(0))
    del state
    F, G = fields['f'], fields['g']
    exact = lambda x: arb(x)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        checkpoint_path=a.input, checkpoint_sha256=digest, checkpoint_bytes=bytecount,
        retained_checkpoint=str(snapshot), maximum_order=N, precision_bits=640, synthetic=syn,
        scope='finite interval computations conditional on the audited stored recurrence',
        source_sha256={}, full_ratios=[], positive_ratios=[], ranked_pairs=[])
    old_path = ROOT/'verification/checks.json'
    if a.resume_input and old_path.exists():
        old = json.loads(old_path.read_text())
        assert old['checkpoint_sha256'] == digest
        result['positive_ratios'] = old['positive_ratios']
        result['ranked_pairs'] = old['ranked_pairs']
        result['previous_audit_elapsed_s'] = old['actual_elapsed_s']
    result['factorial_norms'] = [dict(n=n, density=text(fnorms['f'][n]),
        stream=text(fnorms['g'][n]), stream_over_density=text(fnorms['g'][n]/fnorms['f'][n]))
        for n in sorted(F) if fnorms['f'][n] > 0]
    for name in ['factorial_product_audit.py', 'stream_precision_audit.py', 'laurent_log_audit.py']:
        raw = Path('code', name).read_bytes()
        (ROOT/'sources'/(name+'.txt')).write_bytes(raw)
        result['source_sha256'][name] = sha256(raw).hexdigest()

    def save():
        result['actual_elapsed_s'] = time.monotonic()-started
        (ROOT/'verification/checks.json').write_text(json.dumps(result, indent=2)+'\n')

    denominators, positive_denominators = {}, {}
    full_forcings = {}
    for n in range(2, N+1):
        M = 2*n-1
        S = []
        for q, col in enumerate(F[n]):
            nxt = F[n][q+1] if q+1 < len(F[n]) else []
            S.append([2*(n-1)*(col[j] if j < len(col) else arb(0))
                      -3*(q+1)*(nxt[j] if j < len(nxt) else arb(0))
                      for j in range(max(len(col), len(nxt)))])
        full_forcings[n] = S
        numer = sum((factors[q]*sum(map(abs, col), arb(0)) for q, col in enumerate(S)), arb(0))
        den, pden = arb(0), arb(0)
        for i in range(1, n):
            j = n-i
            w = exact(2*j*(abs(Q(2)-Q(2*i, 3))+1)+2*i*(abs(Q(1)-Q(2*j, 3))+1))
            den += w*fnorms['g'][i]*fnorms['f'][j]
            pden += w*pnorms['g'][i]*pnorms['f'][j]
        assert den > 0
        denominators[n], positive_denominators[n] = den, pden
        result['full_ratios'].append(dict(n=n, forcing_factorial_norm=text(numer),
            denominator=text(den), rho=text(numer/den), log10_rho=text((numer/den).log()/arb(10).log())))
    save()
    print(json.dumps(dict(all_full_ratios_through=N, elapsed_s=time.monotonic()-started)), flush=True)

    polys = {}
    def pc(field, n, q):
        key = (field, n, q)
        if key not in polys:
            polys[key] = angular(fields[field][n][q], 2*n if field == 'g' else 2*n-1, field == 'g')
        return polys[key]

    # Compute all terms with at least one constant log factor, then subtract.
    for n in [int(x) for x in a.positive_orders.split(',') if x]:
        if n > N:
            continue
        if any(r['n'] == n for r in result['positive_ratios']):
            continue
        if time.monotonic()-started > a.seconds:
            result['stopped_before_positive_order'] = n
            break
        t0 = time.monotonic()
        M, out = 2*n-1, [arb_poly([]) for _ in range(max(len(F[n]), n//3+1))]
        for i in range(1, n):
            j = n-i
            P, p = exact(Q(2)-Q(2*i, 3)), exact(Q(1)-Q(2*j, 3))
            Ag, Cg = pc('g', i, 0)
            for v in range(len(F[j])):
                Af, Cf = pc('f', j, v)
                X, Y = Ag*Cf, Cg*Af
                out[v] += P*X-p*Y
                if v:
                    out[v-1] -= v*Y
            Af, Cf = pc('f', j, 0)
            for u in range(1, len(G[i])):
                Ag, Cg = pc('g', i, u)
                X, Y = Ag*Cf, Cg*Af
                out[u] += P*X-p*Y
                out[u-1] += u*X
        pp = arb(0)
        by_degree = []
        for q in range(len(out)):
            sf = angular(full_forcings[n][q], M, False)[0] if q < len(full_forcings[n]) else arb_poly([])
            val = sf-out[q]
            if q == 0:
                assert all(val[M+m].contains(0) for m in range(1, M+1, 2)), ('constant', n)
            nr = factors[q]*norm(val, M)
            pp += nr
            by_degree.append(dict(q=q, weighted_norm=text(nr)))
        pd = positive_denominators[n]
        assert pd > 0
        row = dict(n=n, positive_forcing_norm=text(pp), denominator=text(pd),
            rho_positive=text(pp/pd), log10_rho_positive=text((pp/pd).log()/arb(10).log()),
            constant_coefficient_contains_zero=True, weighted_columns=by_degree,
            elapsed_s=time.monotonic()-t0)
        result['positive_ratios'].append(row)
        save()
        print(json.dumps({k:v for k,v in row.items() if k != 'weighted_columns'}), flush=True)

    # Upper-bound screening, retaining an enclosure for every omitted pair.
    rank_requests = [(int(x), subset) for x in a.rank_orders.split(',') if x
                     for subset in a.rank_subsets.split(',')]
    for n, subset in rank_requests:
        assert subset in ['all', 'positive']
        if n > N or time.monotonic()-started > a.seconds:
            continue
        t0 = time.monotonic()
        heap, total_bound, paircount, outside_bound = [], arb(0), 0, arb(0)
        def omit(bound):
            nonlocal outside_bound
            if bound > outside_bound:
                outside_bound = bound
            elif not outside_bound > bound:
                outside_bound = (outside_bound+bound+abs(outside_bound-bound))/2
        for i in range(1, n):
            j = n-i
            P, p = exact(abs(Q(2)-Q(2*i, 3))), exact(abs(Q(1)-Q(2*j, 3)))
            for u, an in enumerate(cnorms['g'][i]):
                if not an > 0 or (subset == 'positive' and not u):
                    continue
                ad = dnorms['g'][i][u]
                for v, bn in enumerate(cnorms['f'][j]):
                    if not bn > 0 or (subset == 'positive' and not v):
                        continue
                    bd, q = dnorms['f'][j][v], u+v
                    X, Y = an*bd, ad*bn
                    bound = factors[q]*(P*X+p*Y)
                    if q:
                        bound += factors[q-1]*(u*X+v*Y)
                    if not bound > 0:
                        continue
                    total_bound += bound
                    paircount += 1
                    item = (float(bound.log()), i, u, v, bound)
                    if len(heap) < a.rank_count:
                        heapq.heappush(heap, item)
                    elif item > heap[0]:
                        omit(heapq.heapreplace(heap, item)[4])
                    else:
                        omit(bound)
        checked = []
        for _, i, u, v, bound in sorted(heap, reverse=True):
            j, M, q = n-i, 2*n-1, u+v
            Ag, Cg = pc('g', i, u)
            Af, Cf = pc('f', j, v)
            X, Y = Ag*Cf, Cg*Af
            top = exact(Q(2)-Q(2*i, 3))*X-exact(Q(1)-Q(2*j, 3))*Y
            val = factors[q]*norm(top, M)
            if q:
                val += factors[q-1]*norm(u*X-v*Y, M)
            checked.append(dict(i=i, j=j, u=u, v=v, factorial_norm=text(val),
                log10_factorial_norm=text(val.log()/arb(10).log()) if val > 0 else None,
                _sort=float(val.log()) if val > 0 else float('-inf'), _value=val))
        checked.sort(key=lambda r:r['_sort'], reverse=True)
        global_rank_prefix = 0
        for idx, row in enumerate(checked):
            if row['_value'] > outside_bound and all(row['_value'] > r['_value'] for r in checked[idx+1:]):
                global_rank_prefix += 1
            else:
                break
        for row in checked:
            del row['_sort']
            del row['_value']
        result['ranked_pairs'] = [r for r in result['ranked_pairs'] if not
            (r['n'] == n and r.get('subset', 'all') == subset)]
        result['ranked_pairs'].append(dict(n=n, subset=subset, all_pairs_screened=paircount,
            directly_evaluated=len(checked), certified_global_rank_prefix=global_rank_prefix,
            largest_omitted_pair_upper_bound=text(outside_bound),
            ranking_scope='global ranks are certified only through certified_global_rank_prefix',
            sum_all_pair_upper_bounds=text(total_bound), pairs=checked, elapsed_s=time.monotonic()-t0))
        save()
        print(json.dumps(dict(rank_order=n, subset=subset, screened=paircount, evaluated=len(checked),
                              certified_global_rank_prefix=global_rank_prefix, top=checked[:3],
                              elapsed_s=time.monotonic()-t0)), flush=True)
    save()
    print(json.dumps(dict(complete=True, maximum_order=N, actual_elapsed_s=result['actual_elapsed_s'])), flush=True)


if __name__ == '__main__':
    main()
