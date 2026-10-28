"""Sequential bounded chunks of the projection-cusp lower sums for cert_v7.py, driven by a JSON plan.
Plan: {"prefix", "alpha", "b", "shift", "K", "pieces": [{"sign", "left", "right" (null = default), "nx", "ny", "vleft",
"vright", "chunk"}]}. Chunk k of piece p is written to verification/{prefix}_s{sign}_p{p}_r{start}_{stop}.json."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,json
HERE=Path(__file__).resolve().parent;PY=sys.executable
plan=json.loads(Path(sys.argv[1]).read_text());BASE=HERE/'verification';BASE.mkdir(exist_ok=True)
for k,q in enumerate(plan['pieces']):
 for start in range(0,q['nx'],q['chunk']):
  stop=min(q['nx'],start+q['chunk']);name=f"{plan['prefix']}_s{q['sign']}_p{k}_r{start}_{stop}";out=BASE/(name+'.json');log=BASE/(name+'.log')
  if out.exists():print(datetime.now(timezone.utc).isoformat(),'SKIP',name,flush=True);continue
  cmd=[PY,str(HERE/'cert_v7.py'),'--alpha',plan['alpha'],'--b',plan['b'],f"--shift={plan['shift']}",'--K',plan['K'],'--sign',str(q['sign']),'--nx',str(q['nx']),'--ny',str(q['ny']),'--start',str(start),'--stop',str(stop),f"--left={q['left']}",f"--vleft={q['vleft']}",f"--vright={q['vright']}",'--out',str(out)]
  if q['right'] is not None:cmd.append(f"--right={q['right']}")
  print(datetime.now(timezone.utc).isoformat(),'START',name,flush=True)
  with log.open('w') as f:
   r=subprocess.run(cmd,cwd=HERE,stdout=f,stderr=subprocess.STDOUT,timeout=590)
  assert r.returncode==0,(name,r.returncode)
  print(datetime.now(timezone.utc).isoformat(),'DONE',name,flush=True)
print(datetime.now(timezone.utc).isoformat(),'COMPLETE',flush=True)
