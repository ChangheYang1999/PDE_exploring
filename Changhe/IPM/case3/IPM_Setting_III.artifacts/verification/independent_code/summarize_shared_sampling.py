"""Collect hash-matched shared-grid and independent MP evidence, without recomputing fields."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import json
import hashlib
import math


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def point_key(point):
    return float(point['x']), float(point['y'])


def main():
    producer_path = Path('evidence/producer_regions_20261021T033024Z/INDEPENDENT_COMPARISON.json')
    producer = read(producer_path)
    assert producer['producer_table_sha256'] == sha(producer_path.parent / 'region_maxima.txt')
    blocks = {b['tag']: b for b in producer['blocks']}
    rows = []
    for n in [64, 96, 128, 160, 192]:
        tag = f'R1C_CL3P0_N{n}'
        folder = Path('evidence/q_shared_sampling') / tag
        dp, gp = folder / 'diagnostic.json', folder / 'grid.json'
        mp = Path('evidence/q_mp_inverse') / (tag + '_SHARED') / 'diagnostic.json'
        diag, grid, multi = read(dp), read(gp), read(mp)
        block = blocks[tag]
        assert diag['status'] == multi['status'] == 'COMPUTED'
        source = diag['source_sha256']
        assert source == grid['source_sha256'] == multi['source_sha256'] == block['matched_source_sha256']
        assert source == sha(grid['snapshot'])
        assert grid['export_sha256'] == sha(grid['export']) and diag['grid_sha256'] == sha(gp)
        assert diag['points_sha256'] == multi['points_sha256'] == sha(diag['points_file'])
        assert grid['points'] == block['points'] == 2 * grid['N'] * (2 * grid['M'] + 4)
        assert grid['radial_guard_removed'] == 0
        assert [r['inverse_order'] for r in diag['rows']] == [128, 192, 256]
        high = max(multi['rows'], key=lambda x: x['target_digits'])
        assert high['target_digits'] == 110
        points = high['points']
        lookup = {point_key(p): p for p in points}
        assert len(lookup) == len(points)
        assert all(Decimal(p['Nf']) > 0 and Decimal(p['Nv']) > 0 for p in points)
        assert set(lookup) == {tuple(p) for p in read(diag['points_file'])}
        finest = diag['rows'][-1]
        assert finest['nonpositive_denominators'] == 0
        selected = {k: max(points, key=lambda p: Decimal(p[k])) for k in ['R_Nf', 'R_Nv']}
        regions = []
        for label, region in finest['regions'].items():
            checked = {}
            for key, peak in region['maxima'].items():
                p = lookup[point_key(peak)]
                discrepancy = abs(Decimal(str(peak['R'])) - Decimal(p['R'])) / Decimal(p['Nf'])
                checked[key] = dict(double_peak=peak, multiprecision_at_double_peak=p,
                                    absolute_R_difference_over_MP_Nf=str(discrepancy))
            regions.append(dict(region=label, points=region['points'], maxima=checked))
        precision = max(Decimal(v) for r in multi['precision_comparisons']
                        for v in r['scaled_absolute_differences'].values())
        assert precision < Decimal('1e-50')
        max_at_recorded = max(Decimal(p['absolute_R_difference_over_MP_Nf'])
                              for r in regions for p in r['maxima'].values())
        producer_maxima = {key: max(block['regions'], key=lambda r: r[key]['maximum'])[key]
                          for key in ['abs_R', 'R_Nf', 'R_Nv']}
        old_mp = read(block['own_MP_diagnostic'])
        assert sha(block['own_MP_diagnostic']) == block['own_MP_diagnostic_sha256']
        old_high = max(old_mp['rows'], key=lambda r: r['target_digits'])
        independent = {key: max((p for p in old_high['points'] if p[key] is not None),
                                key=lambda p: Decimal(p[key])) for key in ['R_Nf', 'R_Nv']}
        rows.append(dict(tag=tag, source_sha256=source, diagnostic=str(dp), diagnostic_sha256=sha(dp),
                         grid=str(gp), grid_sha256=sha(gp), MP=str(mp), MP_sha256=sha(mp),
                         N=n, M=grid['M'], points=grid['points'],
                         radius_range=[grid['radius'][0], grid['radius'][-1]],
                         theta_range=[grid['theta'][0], grid['theta'][-1]],
                         minimum_Nf=finest['minimum_Nf'], minimum_Nv=finest['minimum_Nv'],
                         inverse_orders=diag['order_comparisons'], MP_selected_count=len(points),
                         MP_target_digits=high['target_digits'], MP_working_digits=high['working_digits'],
                         MP_largest_precision_difference=str(precision),
                         max_R_difference_over_MP_Nf_at_recorded_finest_peaks=str(max_at_recorded),
                         regions=regions, selected_MP_maxima=selected, producer_printed_maxima=producer_maxima,
                         independent_offset_grid_selected_MP_maxima=independent,
                         all_MP_selected_points=points))
    now = datetime.now(timezone.utc).isoformat()
    scope = ('The producer sampling definition alone is shared. The evaluator, density derivatives, '
             'canonical full-plane inverse and MP source-primitives inverse are independently implemented. '
             'Floating-point operation order may change coordinates by rounding. MP values cover selected '
             'points, not the full grid, and all grid maxima are sampled numerical estimates. Differences '
             'between producer and canonical maxima are not pointwise inverse-error estimates. '
             'All source and data hashes are checked. No uniform residual or existence certificate.')
    result = dict(utc=now, code_sha256=sha(__file__), producer_comparison=str(producer_path),
                  producer_comparison_sha256=sha(producer_path), rows=rows, scope=scope,
                  verdict='CONFIRMED finite evaluation and comparison; primary endpoint OPEN')
    root = Path('evidence/q_shared_sampling')
    (root / 'SUMMARY.json').write_text(json.dumps(result, indent=2) + '\n')
    lines = ['# Independent canonical inverse on the producer sampling definition', '', now, '', scope, '',
             '| State | points | producer printed max R/Nf | canonical selected MP R/Nf | canonical selected MP R/Nv | independent offset selected MP R/Nf |',
             '|---|---:|---:|---:|---:|---:|']
    for r in rows:
        p, v, old = r['producer_printed_maxima'], r['selected_MP_maxima'], r['independent_offset_grid_selected_MP_maxima']
        lines.append(f"| {r['tag']} | {r['points']} | {p['R_Nf']['maximum']:.9g} | "
                     f"{float(v['R_Nf']['R_Nf']):.12g} | {float(v['R_Nv']['R_Nv']):.12g} | {float(old['R_Nf']['R_Nf']):.12g} |")
    lines += ['', 'The shared-grid canonical selected R/Nf values decrease through N160 and increase at N192. '
              'N128, N160 and N192 each have a selected value above1e-6. The discrepancy with the producer '
              'table therefore remains after sharing its sampling definition. It is not explained solely '
              'by using the independent offset grid. This is a statement about the two evaluated quantities, '
              'not a rigorously enclosed error of either inverse.', '',
              'The192/256-order maximum changes in R, divided by the finer Nf on the full shared grids, '
              'are between1.01e-8 and8.81e-8. The separate75/110targetdigit inverse checks the selected '
              'maxima; precise per-state errors and locations are below and in JSON.', '']
    for r in rows:
        lines += ['## ' + r['tag'], '', 'Source SHA-256 `' + r['source_sha256'] + '`.', '',
                  f"The grid has {r['points']} points, r in [{r['radius_range'][0]:.12g}, {r['radius_range'][1]:.12g}] "
                  f"and theta in [{r['theta_range'][0]:.12g}, pi/2]. Minimum sampled Nf={r['minimum_Nf']:.12g}, "
                  f"Nv={r['minimum_Nv']:.12g}. No threshold filter or radial overflow exclusion was used.", '',
                  f"MP checks: {r['MP_selected_count']} points,110 targetdigits,{r['MP_working_digits']} workingdigits; "
                  f"largest scaled75/110difference {r['MP_largest_precision_difference']}. The largest absolute "
                  f"R difference divided by MP Nf at the recorded finest-grid peaks is "
                  f"{r['max_R_difference_over_MP_Nf_at_recorded_finest_peaks']}. Neither statistic controls untested points.", '']
        for key, p in r['selected_MP_maxima'].items():
            lines.append(f"Selected {key}={float(p[key]):.14g} at ({float(p['x']):.17g},{float(p['y']):.17g}), "
                         f"R={float(p['R']):.14g}, Nf={float(p['Nf']):.14g}, Nv={float(p['Nv']):.14g}.")
        lines += ['', '| Region | double max absolute R | canonical MP at that point | max double R/Nf | MP at that point |',
                  '|---|---:|---:|---:|---:|']
        for region in r['regions']:
            a, f = region['maxima']['abs_R'], region['maxima']['R_Nf']
            lines.append(f"| {region['region']} | {a['double_peak']['maximum']:.11g} | "
                         f"{abs(float(a['multiprecision_at_double_peak']['R'])):.11g} | "
                         f"{f['double_peak']['maximum']:.11g} | {float(f['multiprecision_at_double_peak']['R_Nf']):.11g} |")
        lines += ['', 'All maximizing coordinates, signed R and both denominators are in the JSON. '
                  'The corresponding N_v maxima and the producer regional table are retained there. '
                  'The exact origin, x-axis, nearby wedges, gaps and radii beyond the last point remain outside this finite comparison.', '']
    (root / 'SUMMARY.md').write_text('\n'.join(lines))
    print('\n'.join(lines[:15]))


if __name__ == '__main__':
    main()
