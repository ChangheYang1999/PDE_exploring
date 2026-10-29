# Summarizes the verifier's published full-bandwidth pressure records (read only) for FULL_SPACE_PRESSURE.md and
# FINAL_REPORT.md section 6. The D64 state (t1_seed74_l3, bound 88) is reported separately.
import json,glob,collections
V='independent_validation/report_audits/'
rows={}
for f in sorted(glob.glob(V+'pressure_bandwidth_published_*.json')):
    d=json.load(open(f)); r=d['row']
    assert d['verdict'].startswith('CONFIRMED')
    rows[r['stem']]=dict(file=f.split('/')[-1],utc=d['recorded_utc'],D=r['bulk_source_degree_bound'],
        fine=[r['levels'][-1][k] for k in ('lmax','nangle','nradial')],coarse_lmax=r['levels'][0]['lmax'],
        last_dP=r['levels'][-1]['change_from_previous']['pressure'],last_dG=r['levels'][-1]['change_from_previous']['gradient'],
        direct=r['fine_direct_pressure_error'],saved=r['saved_sample_max_error'],finite=r['saved_sample_finite_count'],
        all_indep_finite=r['all_765_independent_pressures_and_gradients_finite'])
main={k:v for k,v in rows.items() if k!='t1_seed74_l3'}
out=dict(n_main=len(main),states=sorted(main),D_counts=dict(collections.Counter(v['D'] for v in main.values())),
 lmax_range=[min(v['coarse_lmax'] for v in main.values()),max(v['fine'][0] for v in main.values())],
 max_last_dP=max(v['last_dP'] for v in main.values()),max_last_dG=max(v['last_dG'] for v in main.values()),
 max_direct=max(v['direct'] for v in main.values()),max_saved=max(v['saved'] for v in main.values()),
 all_765_finite=all(v['finite']==765 for v in main.values()),all_indep_finite=all(v['all_indep_finite'] for v in rows.values()),
 latest_utc=max(v['utc'] for v in rows.values()),D64=rows.get('t1_seed74_l3'),rows=rows)
json.dump(out,open('author_checks/pressure_bandwidth_summary_output.json','w'),indent=1)
print({k:v for k,v in out.items() if k not in ('rows','D64')})
