"""Sequential local certificate sweep; diagnostic optimizer only chooses rationals."""
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, sys, time
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/structured_shape_exploration.json').read_text())
if isinstance(rows,dict): rows=rows['rows']
out=root/'data/structured_shape_certificates'
out.mkdir(exist_ok=True)
deadline=time.monotonic()+480
completed=0
for row in rows:
    if time.monotonic()>deadline-30 or completed>=3: break
    alpha=str(row['alpha']); shape=str(row['shape_a'])
    target=out/f'alpha_{alpha.replace(".","p")}.json'
    if target.exists():continue
    print(datetime.now(timezone.utc).isoformat(),alpha,shape,flush=True)
    subprocess.run([sys.executable,str(root/'code/certify_structured_full.py'),
        '--alphas',alpha,'--a',shape,'--step','15000','--out',str(target)],
        cwd=root,check=True,timeout=max(1,deadline-time.monotonic()))
    completed+=1
print('BATCH FINISHED',datetime.now(timezone.utc).isoformat(),flush=True)
