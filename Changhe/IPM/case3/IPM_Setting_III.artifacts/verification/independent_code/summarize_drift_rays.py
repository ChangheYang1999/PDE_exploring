"""Summarize retained independent ray data, preserving its sampled scope."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv,math,hashlib,sys
for tag in sys.argv[1:]:
 base=Path('evidence/q_drift')/tag
 d=json.loads((base/'diagnostic.json').read_text())
 with (base/'samples.csv').open() as f:rows=list(csv.DictReader(f))
 q1={(float(r['x']),float(r['y'])):r for r in rows if r['source'].endswith('/q1.json')}
 q2=[r for r in rows if r['source'].endswith('/q2.json')]
 groups={}
 for r in q2:groups.setdefault(round(math.log10(float(r['r'])),8),[]).append(r)
 fields=['rho_over_a_y','U1_over_actual_minus_c_x','U2_over_actual_c_y','R_Nf_FD8','R_Nv_FD8']
 radial=[]
 for logr,rr in sorted(groups.items()):
  row={'log10r':logr,'points':len(rr)}
  for key in fields:
   vals=[float(v[key]) for v in rr];row[key+'_min']=min(vals);row[key+'_max']=max(vals)
  row['max_component_strain_deviation']=max(abs(float(v[k])-1) for v in rr for k in fields[1:3])
  row['max_affine_density_deviation']=max(abs(float(v[fields[0]])-1) for v in rr)
  radial.append(row)
 first={}
 for threshold in (.05,.1,.5):
  ss=[r for r in radial if r['max_component_strain_deviation']>threshold]
  first[str(threshold)]=ss[0]['log10r'] if ss else None
 changes={}
 for key in fields:
  changes[key]=max(abs(float(r[key])-float(q1[(float(r['x']),float(r['y']))][key])) for r in q2)
 mass=d['signed_mass_log_profile'];mm=[r['rho3_over_r'] for r in mass]
 payload={'utc':datetime.now(timezone.utc).isoformat(),'tag':tag,'diagnostic_sha256':hashlib.sha256((base/'diagnostic.json').read_bytes()).hexdigest(),'a0':d['a0'],'D':d['D'],'c_actual':d['canonical_c_polynomial_quadrature'],'density_snapshot_sha256':d['metadata']['sha256'],'quadrature_level_max_changes':changes,'first_sample_log10r_above_velocity_deviation':first,'signed_third_mass_total':d['required_total_c_plus_a_over4'],'signed_mass_density_min_on_window':min(mm),'signed_mass_density_max_on_window':max(mm),'absolute_mass_percentiles_on_log10_window_minus30_to300':d['absolute_mass_log10_percentiles_on_window'],'radial_ranges':radial,'scope':'Three rays at selected radii only. R uses independent FD8 density derivatives and two levels of the separate infinite-domain inverse. Ratios divide by actual canonical center strain, not by required D. Threshold crossings are first sampled observations and not continuous bounds; signs may change. No ring localization or law in D inferred. Far FD precision limitations remain.'}
 (base/'ray_summary.json').write_text(json.dumps(payload,indent=2)+'\n')
 with (base/'ray_summary.csv').open('w') as f:
  writer=csv.DictWriter(f,fieldnames=list(radial[0]));writer.writeheader();writer.writerows(radial)
 print(json.dumps({k:v for k,v in payload.items() if k not in ('radial_ranges','scope')}))
