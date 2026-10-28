from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
p=BASE/'22_axis_constraints/verification/axis_audit.json';ax=json.loads(p.read_text())
for rel,h in ax['dependency_hashes'].items():assert hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==h,rel
rows=[]
for name in ['nb_stableA2_exact','nb_stableA3_exact']:
 d=next(a for a in ax['candidates'] if a['name']==name)
 source=Path('numerics/data')/(name+'.json')
 assert hashlib.sha256(source.read_bytes()).hexdigest()==d['source_json_sha256']
 z=next(z for z in d['points'] if z['point']==['0','1/10'])
 q=arb(z['cartesian']['q_second']);q2=arb(z['axis_series']['q_second'])
 assert q.overlaps(q2) and q>3
 rounded=arb('4.71760' if name=='nb_stableA2_exact' else '10.89908')
 assert q>rounded
 rows.append({'name':name,'point':['0','1/10'],'rho_yy':q.str(65),'strict_lower':rounded.str(12),'D2rho_bound_3_refuted':True,'source_sha256':d['source_json_sha256'],'canonical_sha256':d['canonical_sha256']})
p4=BASE/'19_nb_candidates/verification/nb_stableA4_exact.points.json';d=json.loads(p4.read_text())
for rel,h in d['dependencies'].items():assert hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==h,rel
raw=(BASE/'19_nb_candidates/verification/nb_stableA4_exact.audit.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()==d['input_sha256']
z=next(z for z in d['points'] if z['point']==['3','4'])
f=arb(z['cartesian']['F']);assert f.overlaps(arb(z['polar']['F']))
n=abs(f)/(16*arb(5)**(arb(1)/5));assert n>arb(9)/100
assert n*arb(2)**35>arb(2)**31
files=[HERE.parent/'PROOF.md',p,p4,BASE/'19_nb_candidates/verification/nb_stableA4_exact.audit.json',BASE/'18_fractional_constants/PROOF.md',BASE/'16_weighted_fractional/REFERENCE_AUDIT.md',BASE/'24_weaker_matrix/PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED necessary point tests; full contract remains uncertified','A2_A3_hessian_failures':rows,'A4':{'F_3_4':f.str(65),'N_point_witness_lower':n.str(65),'strict_N_lower':'9/100','strict_gap_power_over_eta_2^-35':31},'dependencies':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
