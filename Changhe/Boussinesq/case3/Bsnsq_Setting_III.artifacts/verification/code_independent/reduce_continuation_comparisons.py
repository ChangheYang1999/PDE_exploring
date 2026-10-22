from pathlib import Path
import json
r=Path('verification/L2_physical_continuity_20261021T1239Z');d=json.loads((r/'results.json').read_text());fine=d['runs'][-1];coarse=d['runs'][0]
accepted=[p for p in fine['pairs'] if p['category']=='successive_accepted'];sec=[p for p in fine['pairs'] if p['category']=='successive_secant'];last=[p for p in fine['pairs'] if p['category']=='last_secant_to_accepted'];first=next(p for p in fine['pairs'] if p['category']=='reported_first_last');i6=fine['radii'].index(1e6);out={}
for k in ['F','G','Theta','Omega']:
 out[k]={'accepted_at1':[p['fields'][k]['at_r1.0']['old_relative'] for p in accepted],'accepted_at1e8':[p['fields'][k]['at_r100000000.0']['old_relative'] for p in accepted],'accepted_global_relative':[p['fields'][k]['old_relative_max'] for p in accepted],'accepted_global_max_r':[p['fields'][k]['radius_at_old_relative_max'] for p in accepted],'max_secant_relative':max(p['fields'][k]['old_relative_max'] for p in sec),'max_lastsecant_accepted':max(p['fields'][k]['old_relative_max'] for p in last),'first_to_beta312':first['fields'][k]['old_relative_by_radius'][i6],'sum_first7':sum(p['fields'][k]['old_relative_by_radius'][i6] for p in accepted[:7]),'zero_counts':sum(p['fields'][k]['zero_denominators'] for p in fine['pairs']),'positive_zero':sum(p['fields'][k]['positive_over_zero'] for p in fine['pairs']),'subnormal_counts':sum(p['fields'][k]['subnormal_denominators'] for p in fine['pairs']),'max_abs_grid_difference':max(abs(p['fields'][k]['old_relative_max']-q['fields'][k]['old_relative_max']) for p,q in zip(coarse['pairs'],fine['pairs']))}
 if k in ['F','G']:out[k]['max_abs_report_difference']=max(abs(p['fields'][k]['difference']) for p in fine['reported_value_comparison'])
old=json.loads((r/'compact_results.json').read_text()) if (r/'compact_results.json').exists() else None
print('Reduced tables agree with previous:',old==out)
(r/'compact_results.json').write_text(json.dumps(out,indent=2)+'\n')
