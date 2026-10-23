"""Audit repaired source/data package statically; do not execute producer code."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json
root=Path('research/reconstruction_package_audit/verification/repair_20261021T0852');root.mkdir(parents=True,exist_ok=True)
base=Path('../numerics/artifacts/reconstruction');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior=json.loads((root.parent/'CHECKS.json').read_text());checks=[]
for row in prior['states']:
 p=base/row['file'];checks.append(dict(item=row['file'],passed=sha(p)==row['sha256']))
manifest=[]
for line in (base/'SHA256SUMS_SRC.txt').read_text().splitlines():
 if not line.strip():continue
 h,n=line.split(maxsplit=1);p=base/n.lstrip('*');assert p.is_file(),str(p)
 manifest.append(dict(file=n,sha256=sha(p),matches=h==sha(p)))
checks.append(dict(item='all source manifest hashes match',passed=all(r['matches']for r in manifest)))
text=(base/'load_state.py').read_text();tree=ast.parse(text)
parnodes=[n for n in ast.walk(tree)if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='par'for t in n.targets)]
assert len(parnodes)==1
pnode=parnodes[0].value;assert isinstance(pnode,ast.Call)and isinstance(pnode.func,ast.Name)and pnode.func.id=='dict'
par={k.arg:ast.literal_eval(k.value)for k in pnode.keywords}
expected=dict(rho=(1,-1),rho_x=(-1,-1),rho_y=(1,1),U1=(-1,1),U2=(1,-1),psi=(-1,-1),R=(1,-1),Nf=(1,1),Nv=(1,1))
checks.append(dict(item='parity multipliers match mathematical derivatives',passed=par==expected))
checks.append(dict(item='absolute coordinates and unclipped atan2 quadrant angle',passed='ax, ay = np.abs(xs), np.abs(ys)'in text and 'th = np.arctan2(ay, ax)'in text and 'np.clip'not in text))
sources=[]
for p in sorted((base.parent/'src').glob('*.py')):
 s=p.read_text();ast.parse(s);sources.append(dict(name=p.name,sha256=sha(p),has_live_override='numerics/src'in s))
checks.append(dict(item='four loader dependencies omit live absolute override',passed=all(not s['has_live_override']for s in sources if s['name']in ['ipm3.py','ipm3s.py','ipm3q.py','ipm3ql.py'])))
archive_extra_overrides=[r['name']for r in sources if r['has_live_override']]
checks.append(dict(item='every archived Python source omits live absolute override',passed=not archive_extra_overrides))
checks.append(dict(item='forced point residual uses signed original y and unforced R',passed='row.append(row[6] - mu * y * phi(rr[i]))'in text))
checks.append(dict(item='forced origin residual is a0 times center defect minus mu',passed="out['a0'] * out['centre_defect'] - out['mu']"in text))
checks.append(dict(item='saved angular oversampling option passed to rebuilt model',passed="st.get('options', {}).get('M2', None)"in text and 'Lf=Lf, M2=M2)'in text))
checks.append(dict(item='effective frozen-map exponent reported',passed='gamma_eff=gam_eff'in text and 'effective far-field exponent'in text))
listed={str((base/r['file']).resolve())for r in manifest}
checks.append(dict(item='all archived Python sources are in manifest',passed=all(str(p.resolve())in listed for p in (base.parent/'src').glob('*.py'))))
checks.append(dict(item='loader and run script are in manifest',passed=all(str((base/n).resolve())in listed for n in ['load_state.py','run_all.sh'])))
for n in ['load_state.py','README.md','SHA256SUMS_SRC.txt','SHA256SUMS.txt','run_all.sh','RECONSTRUCTION_OUTPUT.txt']:(root/n).write_bytes((base/n).read_bytes())
for n in ['ipm3.py','ipm3s.py','ipm3q.py','ipm3ql.py','hs.py']:(root/('source_'+n)).write_bytes((base.parent/'src'/n).read_bytes())
(root/'PRECHECK.json').write_text(json.dumps(checks,indent=2)+'\n')
assert all(c['passed']for c in checks), [c for c in checks if not c['passed']]
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_LOCAL_REPAIRS',code_sha256=sha(__file__),prior_audit_sha256=sha(root.parent/'CHECKS.json'),loader_sha256=sha(base/'load_state.py'),checks=checks,manifest=manifest,sources=sources,archive_extra_overrides=archive_extra_overrides,scope='Static source and exact file checks only; producer evaluator not run. Current20 states unchanged. Correct coordinate parity and archive dependency resolution established for the inspected tree. Historical bitwise replay and continuum residual accuracy remain outside this check. The origin is skipped only after the polar evaluate call; no claim of a robust origin API is made.')
(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['manifest','sources','checks']}));print('checks',len(checks),'manifest',len(manifest),'source_count',len(sources))
