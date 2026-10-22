"""Extract canonical anchor moments, retaining complete density archive provenance."""
from pathlib import Path
from datetime import datetime,timezone
import json,gzip,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_velocity_hessian';E=D/'evidence';S=B/'research/n8_density_hessian/evidence/density_inputs.json'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
d=json.loads(S.read_text())
for p,h in d['files'].items():assert sha(B/p)==h,p
archive=B/'research/middle_residual/evidence/original_knots.jsonl.gz';need={r['span']:r for r in d['spans']};rows=[]
with gzip.open(archive,'rt') as f:
 header=json.loads(next(f));assert header==d['source_header']
 for line in f:
  row=json.loads(line)
  if row['type']=='complete':break
  if row['span'] not in need:continue
  assert all(row[k]==v for k,v in need[row['span']].items())
  assert len(row['i_left'])==len(row['j_right'])==261
  rows.append(row);del need[row['span']]
  if not need:break
assert not need and len(rows)==7
out={k:d[k] for k in ['source_header','source_center_bracket_exact','delta_exact','theta_max_exact','ntheta','radial_subdivisions','cells']};out.update(utc=datetime.now(timezone.utc).isoformat(),spans=rows,Q=16,series_degree=80,files={str(p.relative_to(B)):sha(p) for p in [S,archive,D/'PROOF.md',E/'proof_first.json',Path(__file__)]})
(E/'moment_inputs.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({'utc':out['utc'],'status':'EXTRACTED_CANONICAL_MOMENTS','spans':7,'moments':3654,'sha256':sha(E/'moment_inputs.json')}),flush=True)
