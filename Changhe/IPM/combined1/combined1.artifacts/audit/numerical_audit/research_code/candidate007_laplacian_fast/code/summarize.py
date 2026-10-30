"""Check completeness and summarize exact weighted angular energies."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
import json,time
from flint import arb,fmpq,ctx
R=Path(__file__).resolve().parents[3];D=R/'research/candidate007_laplacian_fast';ctx.prec=512;t0=time.monotonic()
def H(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
f=D/'verification/full.json';full=json.loads(f.read_text());mp=D/'verification/manifest.json';manifest=json.loads(mp.read_text())
assert full['complete'] and not full['missing_modes'] and full['manifest_sha256']==H(mp)
assert full['completed_modes']==manifest['modes']==list(range(1,320,2))
assert all(H(R/p)==h for p,h in manifest['inputs'].items())
rows={};checks=0
for n in manifest['modes']:
 p=D/f'verification/modes/mode_{n:03d}.json';r=json.loads(p.read_text());assert H(p)==full['mode_record_sha256'][str(n)] and r['manifest_sha256']==H(mp)
 assert r['mode']==n and [w['a'] for w in r['weights']]==manifest['weights']
 assert all(w['relative_accuracy_bits']>150 and arb(w['energy'])>0 for w in r['weights'])
 if r['Cartesian_record_sha256']:
  q=R/f'research/candidate007_weighted_laplacian/verification/modes/mode_{n:03d}.json';assert H(q)==r['Cartesian_record_sha256']
  assert all(w['checks']['Cartesian_exact_product_energy_overlap'] for w in r['weights']);checks+=len(r['weights'])
 rows[n]=r
N1=R/'research/candidate007_weighted_laplacian/source/N1_007_weaktests_float.json';peer=json.loads(N1.read_text())['NORM-T-WLAP-v1'];weights=[]
for i,w in enumerate(full['weights']):
 a=fmpq(w['a']);energy=sum((arb(r['weights'][i]['energy']) for r in rows.values()),arb(0));assert energy.overlaps(arb(w['energy'])) and energy.sqrt().overlaps(arb(w['norm']))
 bands=[]
 for low,high in [(1,15),(17,31),(33,63),(65,127),(129,319)]:
  s=sum((arb(r['weights'][i]['energy']) for n,r in rows.items() if low<=n<=high),arb(0))
  bands.append({'modes':[low,high],'energy_fraction':(s/energy).str(45),'partial_norm':s.sqrt().str(45)})
 top=sorted(rows,key=lambda n:float(arb(rows[n]['weights'][i]['energy']).mid()),reverse=True)[:10]
 top=[{'n':n,'energy_fraction':(arb(rows[n]['weights'][i]['energy'])/energy).str(45)} for n in top]
 key=f'{float(a):.6f}';comparison=None
 if key in peer:
  x=Fraction(str(peer[key]['N_a']));val=arb(fmpq(x.numerator,x.denominator));comparison=((val-energy.sqrt())/energy.sqrt()).str(45)
 weights.append({'a':str(a),'norm':w['norm'],'N1_relative_error':comparison,'bands':bands,'largest_mode_fractions':top})
out={'utc':datetime.now(timezone.utc).isoformat(),'target':'N(a)^2=integral (1+r^2)^(2-a)|Delta F|^2','full_sha256':H(f),'manifest_sha256':H(mp),'summary_code_sha256':H(Path(__file__)),'N1_source_sha256':H(N1),'complete_modes':160,'Cartesian_energy_comparisons':checks,'weights':weights,'runtime_seconds':time.monotonic()-t0,'status':'N4-origin OPEN independent full-norm peer comparison'}
p=D/'verification/angular_summary.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('summary',H(p),'seconds',out['runtime_seconds'])
for w in weights:
 print('a',w['a'],'norm',w['norm'],'N1relative',w['N1_relative_error'])
 if w['a']=='0':print('a0 bands',json.dumps(w['bands']));print('a0 top',json.dumps(w['largest_mode_fractions']))
