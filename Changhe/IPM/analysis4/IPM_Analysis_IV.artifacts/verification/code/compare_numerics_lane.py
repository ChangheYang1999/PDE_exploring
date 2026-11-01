"""Compare the independent Cartesian certificates with the numerics lane.

Run with PYTHONDONTWRITEBYTECODE=1 so reading their module writes no cache.
No external module is imported by the independent Cartesian implementation.
"""
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
from pathlib import Path
import json
import sys
from gmpy2 import mpq


def main():
    sys.dont_write_bytecode=True
    module_path=Path('../a4-num/code/ffcore.py')
    source_data=module_path.read_bytes()
    source_hash=sha256(source_data).hexdigest()
    snapshot=Path('research/01_recurrence/verification/source_snapshots')/('ffcore_'+source_hash+'.py')
    snapshot.parent.mkdir(parents=True,exist_ok=True)
    if not snapshot.exists(): snapshot.write_bytes(source_data)
    spec=importlib.util.spec_from_file_location('numerics_ffcore',module_path)
    module=importlib.util.module_from_spec(spec)
    exec(compile(source_data,snapshot.as_posix(),'exec'),module.__dict__)
    paths=[
        'research/01_recurrence/verification/single_mode_c9_5_N8.json',
        'research/01_recurrence/verification/three_mode_c31_17_N6.json',
        'research/01_recurrence/verification/single_mode_c5_3_N4.json',
        'research/01_recurrence/verification/two_mode_c5_3_N4.json',
        'research/02_candidate007/verification/candidate007_N5.json',
    ]
    cases=[]
    for name in paths:
        path=Path(name)
        data=json.loads(path.read_text())['recursion']
        f0=data['rows'][0]['density']
        highest=max(map(int,f0))
        initial=[f0.get(str(k),'0') for k in range(1,highest+1,2)]
        engine=module.FarField(module.make_ring('fmpq'),data['c'],initial)
        entries=0
        for row in data['rows']:
            n=row['n']
            if n>1: assert engine.step()==n
            generated={
                'density':{str(2*k+1):mpq(str(x)) for k,x in enumerate(engine.f[n]) if x},
                'stream':{str(2*k):mpq(str(x)) for k,x in enumerate(engine.g[n]) if x},
                'potential':{str(2*k):mpq(str(x)) for k,x in enumerate(engine.chi_coeffs(n)) if x},
            }
            for kind in generated:
                expected={k:mpq(v) for k,v in row[kind].items() if mpq(v)}
                assert generated[kind]==expected,(name,n,kind)
                entries+=len(expected)
        cases.append({'input':name,'input_sha256':sha256(path.read_bytes()).hexdigest(),
                      'through_order':len(data['rows']),'coefficients_exactly_equal':entries,
                      'density_stream_potential_all_equal':True})
    own=json.loads(Path('research/02_candidate007/data/leading_exact.json').read_text())
    other_path=Path('../a4-num/notes/cand007_f1.json')
    other=json.loads(other_path.read_text())
    assert mpq(own['c'])==mpq(other['c_l_exact'])
    assert [mpq(own['density'][str(k)]) for k in range(1,20,2)]==list(map(mpq,other['f1_sine_coefficients_exact']))
    assert [mpq(own['potential'][str(k)]) for k in range(0,20,2)]==list(map(mpq,other['C1_cos_coefficients_exact']))
    output={
        'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'comparator_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'numerics_module':module_path.as_posix(),
        'numerics_module_sha256':source_hash,
        'numerics_source_snapshot':snapshot.as_posix(),
        'comparisons':cases,
        'candidate_leading_extraction_exactly_equal':True,
        'numerics_extraction_sha256':sha256(other_path.read_bytes()).hexdigest(),
    }
    target=Path('research/01_recurrence/verification/independent_lane_comparison.json')
    target.write_text(json.dumps(output,indent=2)+'\n')
    print('All five exact coefficient comparisons and both Candidate 007 leading extractions agree.')


if __name__=='__main__':
    main()
