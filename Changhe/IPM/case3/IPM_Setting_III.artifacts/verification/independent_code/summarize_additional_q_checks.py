"""Aggregate independently generated, hash-matched exact and canonical MP audits.
This script reads results only. It runs neither the producer code nor an inverse.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from decimal import Decimal
import json, hashlib, argparse, re


def load(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(entry):
    return Fraction(entry['exact'])


def point_key(p):
    return float(p['x']), float(p['y'])


def dense_winner(rows, region, metric):
    candidates = [dict(r['summary'][region][metric], grid=r['grid']) for r in rows
                  if region in r['summary'] and metric in r['summary'][region]]
    return max(candidates, key=lambda p: p['maximum']) if candidates else None


def collect(exact_path):
    results = []
    for raw in load(exact_path)['rows']:
        m, e = raw['metadata'], raw['exact']
        name = Path(m['source']).name
        match = re.fullmatch(r'r1([CS])_cl([0-9.]+)_N([0-9]+)_(.+)\.pt', name)
        aniso = re.fullmatch(r'r1A_cl([0-9.]+)_N([0-9]+)x([0-9]+)\.pt', name)
        assert match or aniso, name
        if aniso:
            ell, n, angular = aniso.groups()
            tag = f'R1A_CL{ell.replace(".", "P")}_N{n}X{angular}'
        else:
            branch, ell, n, suffix = match.groups()
            tag = f'R1{branch}_CL{ell.replace(".", "P")}_N{n}_{suffix.upper() if branch == "S" else suffix}'
        assert sha(m['source']) == m['sha256']
        a, c, delta = (exact(e[k]) for k in ['a', 'c', 'delta'])
        A = 2 * exact(e['ell']) - 1
        assert delta == exact(e['ell']) + c - 1
        assert exact(e['poisson']) == 0
        b, ee, q1, q2 = (exact(e[k + '_core']) for k in ['b', 'e', 'q1', 'q2'])
        t1 = 6 * ee - (a - 2 * A) * b
        assert t1 == exact(e['jet_elimination_core'])
        scale = 2 ** (2 * m['map_kappa']) / m['L'] ** 2
        t2 = q1 - q2 - (a - 4 * A) * b / (3 * a)
        dense_path = Path('evidence/q_residual_grid') / tag / 'diagnostic.json'
        mp_path = Path('evidence/q_mp_inverse') / tag / 'diagnostic.json'
        d, mp = load(dense_path), load(mp_path)
        assert d['status'] == mp['status'] == 'COMPUTED'
        assert d['sha256'] == mp['source_sha256'] == m['sha256']
        assert d['metadata']['map_kappa'] == m['map_kappa']
        assert mp['finished_utc'] and d['finished_utc']
        finest_order = max(r['inverse_order'] for r in d['rows'])
        finest = [r for r in d['rows'] if r['inverse_order'] == finest_order]
        high_mp = max(mp['rows'], key=lambda r: r['target_digits'])
        pts = high_mp['points']
        precision_diffs = [Decimal(v) for r in mp['precision_comparisons']
                           for v in r['scaled_absolute_differences'].values()]
        maxima = {k: max((pt for pt in pts if pt[k] is not None), key=lambda p: Decimal(p[k])) for k in ['R_Nf', 'R_Nv']}
        at_dense = {}
        for k in maxima:
            p = dense_winner(finest, 'all', k)
            matches = [q for q in pts if point_key(q) == point_key(p)]
            assert len(matches) == 1, (tag, k)
            at_dense[k] = matches[0]
        results.append(dict(
            tag=tag, metadata=m, exact_source=str(exact_path), exact_source_sha256=sha(exact_path),
            exact=dict(a=str(a), c=str(c), delta=str(delta), T1_core=str(t1),
                       T2_core=str(t2), T1_relative=str(t1/(6*ee)) if ee else None),
            physical_cubics={k: float(exact(e[k+'_core']))*scale for k in ['b','e','q1','q2']},
            T2_physical=float(t2)*scale, core_to_physical_scale_rounded=scale,
            gradient_witness=raw['largest_witness'],
            origin_excluded=bool(delta),
            dense=dict(path=str(dense_path),sha256=sha(dense_path),finest_order=finest_order,
                       grids=[{k:r[k] for k in ['grid','inverse_order','radii','angles','log10_radius','theta']}
                              for r in d['rows']],
                       regions={region:{k:dense_winner(finest,region,k)for k in ['abs_R','R_Nf','R_Nv']}
                                for region in sorted(set(k for r in finest for k in r['summary']))},
                       order_maxima={str(order):{k:dense_winner([r for r in d['rows']if r['inverse_order']==order],'all',k)
                                                 for k in ['R_Nf','R_Nv']}
                                     for order in sorted(set(r['inverse_order']for r in d['rows']))}),
            MP=dict(path=str(mp_path),sha256=sha(mp_path),target_digits=high_mp['target_digits'],
                    working_digits=high_mp['working_digits'],point_count=len(pts),
                    undefined_ratios={k:sum(p[k] is None for p in pts) for k in ['R_Nf','R_Nv']},
                    largest_scaled_precision_difference=str(max(precision_diffs)),
                    max_over_MP_selected_points=maxima,at_double_dense_maximizers=at_dense,
                    points=pts,far_axis_limit_R_Nf=high_mp['far_axis_limit_R_Nf'],
                    far_axis_limit_R_Nv=high_mp['far_axis_limit_R_Nv'],
                    far_axis_amplitude=high_mp['far_vertical_leading_amplitude'])))
    return results


def main():
    p=argparse.ArgumentParser();p.add_argument('exact_path',nargs='+');p.add_argument('--out',required=True);args=p.parse_args()
    rows=[r for source in args.exact_path for r in collect(source)];out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    data=dict(utc=datetime.now(timezone.utc).isoformat(),code_sha256=sha(__file__),rows=rows,
              scope='Exact finite saved density formula and independently computed canonical inverse. Dense maxima are finite samples. MP maxima below are over selected points only, not optimized or uniform bounds. Printed physical cubic coefficients are rounded conversions of exact core coefficients. No exact or nearby profile is asserted.')
    out.with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    lines=['# Additional independent Q-state checks','',data['utc'],'',data['scope'],'',
           'T1rel = [6e-(a-2A)b]/(6e), A=2ell-1. T2 = q1-q2-(a-4A)b/(3a).',
           'The gauge amplitude K is computed from the saved far field. Comparing different K requires scaling cubic coefficients; a and ell already are invariant.','',
           '| State | a | Delta | b | e | T1rel | T2 | max selected MP R/Nf | max selected MP R/Nv | K |',
           '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        E=r['exact'];m=r['MP']['max_over_MP_selected_points'];b=r['physical_cubics']
        lines.append(f"| {r['tag']} | {float(Fraction(E['a'])):.12g} | {float(Fraction(E['delta'])):.8g} | {b['b']:.10g} | {b['e']:.10g} | {float(Fraction(E['T1_relative'])):.9g} | {r['T2_physical']:.9g} | {float(m['R_Nf']['R_Nf']):.12g} | {float(m['R_Nv']['R_Nv']):.12g} | {float(r['MP']['far_axis_amplitude']):.10g} |")
    lines += ['', 'All source files were rehashed, and source identities agree across exact, dense and MP computations. Each exact Poisson combination vanishes and each exact centre defect is nonzero. Density formulas are smooth; the separate interpolated stream used by the producer is not used here. Absence of a returned gradient witness does not establish a gradient bound.','']
    for r in rows:
        lines += ['## '+r['tag'],'',f"Source SHA-256 `{r['metadata']['sha256']}`.",
                  f"MP selected points: {r['MP']['point_count']}; {r['MP']['target_digits']} target digits with {r['MP']['working_digits']} working digits. Largest scaled difference between precision levels: {r['MP']['largest_scaled_precision_difference']}.",'']
        for k,pt in r['MP']['max_over_MP_selected_points'].items():
            lines.append(f"Selected {k} peak {float(pt[k]):.14g} at ({float(pt['x']):.17g}, {float(pt['y']):.17g}): |R|={abs(float(pt['R'])):.14g}, Nf={float(pt['Nf']):.14g}, Nv={float(pt['Nv']):.14g}.")
        lines += ['', '| Dense region | max absolute R | location | max R/Nf | max R/Nv |', '|---|---:|---|---:|---:|']
        for region in ['origin','core','middle','far']:
            rr=r['dense']['regions'].get(region)
            if not rr:continue
            ab=rr['abs_R']
            lines.append(f"| {region} | {ab['maximum']:.9g} | ({ab['x']:.8g}, {ab['y']:.8g}) | {rr['R_Nf']['maximum']:.10g} | {rr['R_Nv']['maximum']:.10g} |")
        lines += ['', 'The far absolute double-precision peak includes radii up to 1e250. It is sensitive to cancellation and the stored exponent; it is not a verified leading asymptotic coefficient or a global finite bound. Full region coordinates and denominators, per-order maxima, and all selected MP values are in JSON.','']
    out.with_suffix('.md').write_text('\n'.join(lines))
    print('\n'.join(lines[:18]))

if __name__=='__main__':main()
