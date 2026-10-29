from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,time
import numpy as np
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parent
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ');out=ROOT/'results'/('strain_collection_'+stamp);out.mkdir()
paths=[ROOT/'results/strain_l1_n65_h04']
for batch in ['strain_refinement_batch_one.json','strain_refinement_batch_two.json','strain_crosscheck_batch.json']:
 d=json.loads((ROOT/'results'/batch).read_text())
 if d.get('status')!='complete':raise RuntimeError('Batch incomplete: '+batch)
 paths.extend(ROOT/'results'/r['name'] for r in d['completed'])
rows=[];data={};inputs=[]
for p in paths:
 d=json.loads((p/'progress.json').read_text())
 if d['phase']!='complete':raise RuntimeError('Run incomplete')
 if sha256(p/'checkpoint.npz')!=d['checkpoint_sha256']:raise RuntimeError('Checkpoint changed')
 name=p.name;data[name]=d;c=d['config'];last=d['bands'][-1]
 rows.append(dict(name=name,level='L1' if '_l1_' in name else 'L2',angular=c['angular'],dx=c['maximum_log_radius_step'],start=c['start_radius'],strain=last['strain_with_estimated_tail'],truncated=last['cumulative_strain_without_inner_ball'],tail=last['estimated_tail'],minimum_F=d['minimum_sampled_F'],endpoint_error=d['maximum_endpoint_mu_error'],gradient_remap=d['maximum_gradient_remap_difference'],wall_seconds=d['accumulated_wall_seconds'],cpu_seconds=d['accumulated_cpu_seconds']))
 inputs.append(dict(path=str(p.relative_to(ROOT)),progress_sha256=sha256(p/'progress.json'),checkpoint_sha256=sha256(p/'checkpoint.npz'),candidate_sha256=d['candidate_sha256'],source_sha256=d['source_sha256']))
comparisons=[];referees=[]
for level in ['l1','l2']:
 ref=ROOT/'results'/f'strain_{level}_n257_h010_s2.5e-05';d=data[ref.name]
 for p in [x for x in paths if f'_{level}_' in x.name]:
  field_diffs=[]
  for band in range(1,7):
   with np.load(ref/f'band_{band:02d}.npz') as a,np.load(p/f'band_{band:02d}.npz') as b:
    skip=(len(a['mu'])-1)//(len(b['mu'])-1)
    if not np.allclose(a['mu'][::skip],b['mu'],atol=1e-15,rtol=0):raise RuntimeError('Non-nested angle grid')
    qa=3.5*np.exp(a['h'][::skip]);qb=3.5*np.exp(b['h']);ea=a['eta'][::skip];eb=b['eta']
    field_diffs.append(dict(radius=float(a['radius']),q_relative_sup=float(np.max(abs(qa-qb))/np.max(abs(qa))),eta_relative_sup=float(np.max(abs(ea-eb))/np.max(abs(ea)))))
  comparisons.append(dict(name=p.name,reference=ref.name,strain_difference=data[p.name]['bands'][-1]['strain_with_estimated_tail']-d['bands'][-1]['strain_with_estimated_tail'],fields=field_diffs))
 source=ROOT.parent.parent/'e4-lead/astra/t1diag/results/transport'/f'{level.upper()}_stable.json'
 raw=source.read_bytes();(out/source.name).write_bytes(raw);r=json.loads(raw)
 referees.append(dict(level=level.upper(),path=str(source),sha256=hashlib.sha256(raw).hexdigest(),referee_strain=r['K2S'],independent_strain=d['bands'][-1]['strain_with_estimated_tail'],difference=d['bands'][-1]['strain_with_estimated_tail']-r['K2S'],referee_angular=r['nm'],referee_dx=r['dx'],referee_cutoff=r['rho_max']))
with (out/'runs.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
record=dict(created_utc=datetime.now(timezone.utc).isoformat(),runs=rows,inputs=inputs,comparisons=comparisons,referee_comparisons=referees,scope='Finite numerical convergence and separate-implementation comparison on the same explicitly Gaussian-repaired potential. Not an interval enclosure, global basin proof or exact Euler profile.')
atomic_json(out/'collection.json',record)
print(str(out));print(json.dumps(rows,indent=2));print(json.dumps(referees,indent=2))
