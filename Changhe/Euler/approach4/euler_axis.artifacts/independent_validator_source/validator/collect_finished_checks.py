#!/usr/bin/env python3
"""Collect only completed, hash-stable balance, transport and field comparisons."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, math

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_complete(path):
    d = json.loads(path.read_text())
    if d.get('phase') != 'complete':
        raise ValueError('Incomplete input: ' + str(path))
    for name, wanted in d['source_sha256'].items():
        p = Path(name)
        if not p.is_absolute():
            p = (ROOT if name.startswith(('research/', 'axisymmetric_euler_24h/')) else BASE) / p
        if digest(p) != wanted:
            raise ValueError('Changed source: ' + str(p))
    return d

def balances(path):
    d = load_complete(path)
    cp = BASE / 'external_exports/T1_ladder_L2_20261028T235434Z'
    if digest(cp/'coeffs.npz') != d['candidate_sha256']:
        raise ValueError('Candidate changed')
    c = json.loads((cp/'candidate.json').read_text())['cl']
    rows = []
    for r in d['rows']:
        t = {k:r[k] for k in ['label', 'R', 'radius_over_a_eff', 'nradial', 'nangle']}
        for tag, factor in [('energy', 5*c-2), ('helicity', 4*c-2)]:
            scale = max(abs(r[tag+'_flux']), abs(factor*r[tag]))
            calculated = r[tag+'_flux'] - factor*r[tag]
            if abs(calculated-r[tag+'_defect']) > 1e-10*max(1.,scale):
                raise ValueError('Balance definition mismatch')
            t[tag] = dict(integral=r[tag], flux=r[tag+'_flux'], defect=r[tag+'_defect'],
                          scale=scale, relative_defect=abs(r[tag+'_defect'])/scale,
                          residual_work=r[tag+'_residual_work'], interface_jump=r[tag+'_interface_jump'],
                          corrected_error=r[tag+'_corrected_error'],
                          relative_corrected_error=abs(r[tag+'_corrected_error'])/scale)
        rows.append(t)
    return dict(input=str(path.relative_to(ROOT)), input_sha256=digest(path), c_l=c,
                completed_utc=d['updated_utc'], wall_seconds=d['elapsed_seconds'], cpu_seconds=d['cpu_seconds'],
                rows=rows, pressure_parameters=d['pressure_parameters'],
                scope='Finite-ball piecewise classical balances with bulk full-space pressure. Energy tests A9; helicity is diagnostic. Corrected errors test the identity implementation, not Euler closure.')

def transport(path):
    d = load_complete(path)
    if not d['all_data_comparisons_passed'] or len(d['rows']) != 7 or len(d['transport_rows']) != 4:
        raise ValueError('Missing or failed comparisons')
    rows = [{k:v for k,v in r.items() if k != 'points'} for r in d['transport_rows']]
    return dict(input=str(path.relative_to(ROOT)), input_sha256=digest(path), completed_utc=d['updated_utc'],
                wall_seconds=d['elapsed_seconds'], cpu_seconds=d['cpu_seconds'], data_rows=d['rows'], transport_rows=rows,
                scope='Seven saved elliptic fields and E values reproduced using saved transported arrays. Independent physical-time transport checked on 28 points at each of c_l=.68,.74 and two cutoffs/tolerances. This does not independently reproduce full-grid E or global strain S.')

def fields(path):
    path = path.resolve()
    d = load_complete(path)
    rows = d['rows']
    if len(rows) != 117 or len(d['tail']) != 6:
        raise ValueError('Missing field-comparison rows')
    results = []
    for pair in d['pairs']:
        medium = {r['band']:r for r in rows if r['pair']==pair and r['level']=='medium'}
        fine = {r['band']:r for r in rows if r['pair']==pair and r['level']=='fine'}
        if len(medium)!=19 or medium.keys()!=fine.keys():
            raise ValueError('Missing radial bands')
        changes = {}
        for key in next(iter(fine.values()))['fields']:
            vals = [(band, r['fields'][key]) for band,r in fine.items()]
            largest = max(vals, key=lambda p:p[1]['relative_difference_rms'])
            changes[key] = dict(largest_band_relative_difference=largest[1]['relative_difference_rms'],
                                band_at_largest=largest[0],
                                max_absolute_quadrature_change_in_relative_difference=max(abs(r['fields'][key]['relative_difference_rms']-medium[band]['fields'][key]['relative_difference_rms']) for band,r in fine.items()),
                                sampled_sup_a=max(v['sampled_sup_a'] for _,v in vals),
                                sampled_sup_b=max(v['sampled_sup_b'] for _,v in vals),
                                sampled_sup_difference=max(v['sampled_sup_difference'] for _,v in vals))
        results.append(dict(pair=pair, fields=changes,
                            selected_bands=[fine[n] for n in ['origin','shell_-3','shell_0','shell_2','shell_10']],
                            axis=next(r for r in rows if r['pair']==pair and r['level']=='axis'),
                            tail=[r for r in d['tail'] if r['pair']==pair]))
    return dict(input=str(path.relative_to(ROOT)),input_sha256=digest(path), completed_utc=d['updated_utc'],
                wall_seconds=d['wall_seconds'],cpu_seconds=d['cpu_seconds'], gauges=d['gauges'],
                reference_a_eff=d['reference_a_eff'],pairs=results,scope=d['scope'])

def main():
    p=argparse.ArgumentParser();p.add_argument('--fields',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists() or not a.output.resolve().is_relative_to(ROOT):raise ValueError('Fresh output in lane required')
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(), collector_sha256=digest(Path(__file__)),
             balances=balances(BASE/'results/ladder_l2_balances.json'),
             transport=transport(BASE/'results/two_series_transport.json'),fields=fields(a.fields))
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(a.output)
    for r in out['balances']['rows']:
        if r['label']=='fine':print('balance',r['radius_over_a_eff'],r['energy']['relative_defect'],r['helicity']['relative_defect'])
    for r in out['fields']['pairs']:
        print('fields',r['pair'])
        for key,v in r['fields'].items():print(key,v)
        print('tail',r['tail'][-1]['comparison']['relative_difference_rms'])

if __name__=='__main__':main()
