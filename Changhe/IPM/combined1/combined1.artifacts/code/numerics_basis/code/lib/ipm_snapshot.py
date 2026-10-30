"""Immutable candidate snapshots in the exchange directory (CONTRACTS v01 section 5)."""
import os, json, hashlib, shutil, datetime
SH = 'candidates'
LANE = 'RUN_ROOT/numerics_N1N2'

def sha256(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()

def write_snapshot(cid, parent, chart, c_l_exact, theta0, a0, b0n_status, basis_desc, coef_files, evaluator_code, sector_file, loss, notes, description, extra_files=()):
    d = os.path.join(SH, cid)
    assert not os.path.exists(d), 'snapshot exists: '+cid
    os.makedirs(d)
    cf = []
    for name, src, fmt, exactness in coef_files:
        shutil.copy(src, os.path.join(d, name)); cf.append({'name': name, 'sha256': sha256(os.path.join(d, name)), 'format': fmt, 'exactness': exactness})
    shutil.copy(sector_file, os.path.join(d, 'sector_table.json'))
    for src in extra_files: shutil.copy(src, d)
    man = {'id': cid, 'created_utc': datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'), 'created_by_lane': 'c1-n1', 'parent': parent, 'chart': chart,
           'c_l_exact': c_l_exact, 'theta0': theta0, 'a0': a0, 'B0n_status': b0n_status, 'basis': basis_desc, 'coefficient_files': cf,
           'evaluator_code': [{'path': p, 'sha256': sha256(p)} for p in evaluator_code],
           'sector_table': {'name': 'sector_table.json', 'sha256': sha256(os.path.join(d, 'sector_table.json'))}, 'loss': loss, 'notes': notes}
    json.dump(man, open(os.path.join(d, 'MANIFEST.json'), 'w'), indent=1)
    with open(os.path.join(d, 'SHA256SUMS'), 'w') as f:
        for fn in sorted(os.listdir(d)):
            if fn == 'SHA256SUMS': continue
            f.write(f'{sha256(os.path.join(d, fn))}  {fn}\n')
    msha = sha256(os.path.join(d, 'MANIFEST.json'))
    idx = os.path.join(SH, 'INDEX.md')
    if not os.path.exists(idx):
        open(idx, 'w').write('# candidate_snapshots INDEX (append-only): ID | UTC | lane | parent | chart | description | sha256(MANIFEST.json)\n')
    open(idx, 'a').write(f"{cid} | {man['created_utc']} | c1-n1 | {parent if isinstance(parent, str) else parent.get('id', parent.get('path'))} | {chart} | {description} | {msha}\n")
    return man


def basis_summary(gens_json_path):
    """basis description fields computed from the exact generator JSON: generator count, branches, angular max m, radial max k (= m + w + n for Legendre
    functions t^w P_n with monomial degree up to w+n; m + h for monomials; m + w + Q + n for legq; legqs are multi-scale functions whose radial
    degree in the canonical variable is not finite: listed separately)"""
    import json
    J = json.load(open(gens_json_path))
    ks = []; legqs = []; branches = set(); mmax = 0
    for g in J['generators']:
        m = int(g['m']); sp = g['spec']; mmax = max(mmax, m)
        if 'j' in g: branches.add(int(g['j']))
        if sp[0] == 'mono': ks.append(m+int(sp[1]))
        elif sp[0] == 'leg': ks.append(m+int(sp[1])+int(sp[2]))
        elif sp[0] == 'legq': ks.append(m+int(sp[1])+int(sp[2])+int(sp[3]))
        elif sp[0] == 'legqs': legqs.append((m, sp))
    return {'generator_count': len(J['generators']), 'n_free': J.get('n_free'), 'n_fixed': J.get('n_fixed'), 'branches': sorted(branches), 'angular_max_m': mmax,
            'radial_max_k_canonical': max(ks) if ks else None, 'legqs_multiscale_functions': len(legqs),
            'radial_max_k_note': 'k = largest monomial degree m+h in the canonical form r^(2k)(1+r^2)^(p-k); C1-N1-002..004 manifests wrote 25 (the T1 value) which was wrong for the new blocks (c1-n4 N4-044/N4-048): their correct values are 72 (002), 82 (003), 42 (004)'}
