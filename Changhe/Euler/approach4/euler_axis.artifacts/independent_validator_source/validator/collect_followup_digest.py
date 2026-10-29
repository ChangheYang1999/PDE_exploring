#!/usr/bin/env python3
"""Summarize completed independent follow-up collectors, without rerunning numerics."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'axisymmetric_euler_24h/results'
p=argparse.ArgumentParser();p.add_argument('--stem',required=True);p.add_argument('--driver',required=True);a=p.parse_args()
now=datetime.now(timezone.utc);inputs={}
def load(path):
 b=path.read_bytes();inputs[str(path.relative_to(ROOT))]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)};return json.loads(b)
pressure=load(R/(a.stem+'_pressure_collection.json'));balance=load(R/(a.stem+'_balances_cartesian_collection.json'));adv=load(R/(a.stem+'_adversarial_collection.json'));origin=load(R/(a.stem+'_origin_pressure.json'));reg=load(R/a.driver/'registered/summary.json')
for d in [pressure,balance,adv]:
 assert d['all_passed'] and len(d['checks'])==d['check_count'] and all(x['passed']for x in d['checks'])
for key,h in adv['input_sha256'].items():
 path=Path(key)
 if not path.is_absolute():path=ROOT/path
 assert path.resolve().is_relative_to(ROOT)
 assert hashlib.sha256(path.read_bytes()).hexdigest()==h,(path,h)
assert origin['phase']=='complete'
assert pressure['candidate_sha256']==reg['candidate_sha256']
origin_coefficients=[(Path(k),v)for k,v in origin['source_sha256'].items()if Path(k).name=='coeffs.npz']
assert len(origin_coefficients)==1 and origin_coefficients[0][1]==reg['candidate_sha256']
for path,h in [(Path(k),v)for k,v in origin['source_sha256'].items()]:
 assert path.resolve().is_relative_to(ROOT) and hashlib.sha256(path.read_bytes()).hexdigest()==h
fine=[x for x in balance['balance_rows']if x['label']=='fine'];assert [x['radius_over_a_eff']for x in fine]==[1,4,16]
direct=pressure['direct_rows'][-1];moments=origin['moments'];assert len(moments)==3
out=R/(a.stem+'_digest_'+now.strftime('%Y%m%dT%H%M%S.%fZ')+'.json')
record=dict(completed_utc=now.isoformat(),candidate_sha256=pressure['candidate_sha256'],check_counts={n:d['check_count']for n,d in [('pressure',pressure),('balance_cartesian',balance),('adversarial',adv)]},inputs=inputs,green_refinement=pressure['green_refinement_max_abs'],direct_refinement=pressure['direct_refinement_max_abs'],direct_final_pressure_error=direct['max_abs_pressure_difference'],direct_final_worst_point=direct['worst_point'],saved_sample_comparison=pressure['saved_sample_comparison'],pressure_parameters=balance['pressure_parameters'],energy_fine=[x['energy']for x in fine],helicity_fine=[x['helicity']for x in fine],cartesian_finest=balance['cartesian_steps'][-1],origin_Mz=moments[-1]['M_z'],origin_Mz_spread=max(x['M_z']for x in moments)-min(x['M_z']for x in moments),vorticity_maximum=adv['vorticity_maximum'],swirl_maximum=adv['swirl_maximum'],peaks=adv['peaks'],precision=adv['precision'],finite_root_count=len(adv['detected_roots']),fresh_point_count=adv['fresh_point_count'],registered_aggregate=reg['aggregate'],verdict='CONFIRMED',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Digest of completed retained checks and rechecked hashes. Not a new PDE evaluation, uniform pressure certificate, global maximum proof or accepted Euler profile.')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(ROOT)),'P':record['green_refinement'],'direct':record['direct_final_pressure_error'],'energy':[x['relative_raw_defect']for x in record['energy_fine']],'energy_corrected':max(x['relative_corrected_error']for x in record['energy_fine']),'origin':record['origin_Mz'],'origin_spread':record['origin_Mz_spread'],'cartesian':record['cartesian_finest']['M_max_error'],'vort':adv['vorticity_maximum']['relative_maximum_identity_defect'],'q':adv['swirl_maximum']['absolute_swirl_maximum_defect']}))
