"""Summarize immutable outputs of this lane's independent grid evaluator."""
import json
import sys
from pathlib import Path
for arg in sys.argv[1:]:
    root = Path(arg)
    d = json.loads((root / 'results.json').read_text())
    lines = ['# Independent differential residual audit', '',
             f"Actual interval: {d['started_utc']} to {d['ended_utc']}; {d['elapsed_seconds']:.6f} seconds.", '',
             'Own stored-field evaluator, adaptive full-plane physical-radius modal inverse, and seven-point Cartesian finite differences. No numerics-lane code executed or imported. Radial grid includes 105 logarithmic radii from 1e-5 to 1e8 and finite spline-cell midpoint radii, with 96 angles. Grouped normalizers have no added floor. The finer derivative step is 1e-5 max(1,r), checked against twice that step.', '',
             '| State | beta | a0 | eps | lambda | transport RF/NF | transport RG/NG | self RF/NF | self RG/NG |',
             '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    details = []
    max_change = 0.
    for s in d['states']:
        fine = {r['kind']: r['summary'] for r in s['runs'] if r['relative_step'] == 1e-5}
        coarse = {r['kind']: r['summary'] for r in s['runs'] if r['relative_step'] == 2e-5}
        m = s['metadata']
        f, u = fine['transport'], fine['self']
        lines.append(f"| {s['label']} | {m['beta']:.9g} | {m['a0']:.9g} | {m['eps']:.12g} | {m.get('lam','not used')} | {f['F']['max_ratio']:.10g} | {f['G']['max_ratio']:.10g} | {u['F']['max_ratio']:.10g} | {u['G']['max_ratio']:.10g} |")
        change = max(abs(fine[k][field]['max_ratio'] - coarse[k][field]['max_ratio']) for k in fine for field in ['F','G','Theta','Omega'])
        max_change = max(max_change, change)
        failures = sum(len(q['failed']) for q in s['quadrature'].values())
        details += ['', f"## {s['label']}", '', f"SHA256: `{s['sha256']}`. {s['points']} points, {s['radii']} radii. K={m['K']}, Nt={m['Nt']}, L={m['L']}, Nphi_res={m.get('Nphi_res','not saved')}. Objective={m['obj']:.12g}. Inverse quadrature failure flags: {failures}. Maximum change of any listed field maximum under step halving: {change:.6g}.", '', '| Inverse | max abs RF | max abs RG | max abs RTheta | max abs ROmega |', '|---|---:|---:|---:|---:|']
        for k in fine:
            details.append('| '+k+' | '+' | '.join(f"{fine[k][field]['max_abs']:.12g}" for field in ['F','G','Theta','Omega'])+' |')
        details += ['', '| Radius interval | forced RF/NF | forced RG/NG |', '|---|---:|---:|']
        for a,b in zip(f['F']['regions'],f['G']['regions']):
            details.append(f"| {a['r_min']} to {a['r_max']} | {a['max_ratio']:.10g} | {b['max_ratio']:.10g} |")
        details += ['', 'Transport source: '+s.get('forcing_description','see saved state metadata')+'.']
        if all('max_abs' in r for k in fine for field in ['F','G','Theta','Omega'] for r in fine[k][field]['regions']):
            details += ['', '| Inverse | Field | Radius interval | max absolute | max pointwise normalized |',
                        '|---|---|---|---:|---:|']
            for k in fine:
                for field in ['F','G','Theta','Omega']:
                    for r in fine[k][field]['regions']:
                        details.append(f"| {k} | {field} | {r['r_min']} to {r['r_max'] if r['r_max'] is not None else '1e8'} | {r['max_abs']:.12g} | {r['max_ratio']:.12g} |")
        details += ['', f"Independent c_self={s['center']['c_self']:.12g}; mixed strain={s['center']['c_mixed']:.12g}. The amplitude a0 is a continuation parameter; a0 different from 1 is not itself a failed center compatibility condition."]
    lines += ['', f'Maximum change of field maxima over this run: {max_change:.6g}. All inverse failure flags are listed per state below.', '',
              'The transport columns use the source explicitly described for each state. An intended fixed-source reconstruction does not certify the different projected source used at runtime when those effective coefficients were not saved. Cartesian normalized maxima omit points exactly on the symmetry axis, where both numerator and denominator vanish; the divided equations include exact axis limits and the center is checked separately. Ratios are zero for R=N=0 and infinite for N=0,R!=0; no positive floor is used.',
              '', 'Verdict: CONFIRMED as numerical measurements on the archived representations. REFUTED as small-residual solutions of unforced B2 for these snapshots. The sampled maxima are not certified global norms. Quadrature estimates and step comparisons are numerical checks, not interval bounds. Empirical parameter agreement across resolutions does not supply a continuum parameter error bound or prove a saddle-node bifurcation.']
    (root/'SUMMARY.md').write_text('\n'.join(lines+details)+'\n')
    print(root, 'states',len(d['states']),'max_step_change',max_change)
