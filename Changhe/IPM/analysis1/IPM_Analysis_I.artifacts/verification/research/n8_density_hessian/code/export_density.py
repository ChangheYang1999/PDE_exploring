"""Extract complete density polynomials and exact span/cell geometry to JSON."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sys,json,gzip,hashlib
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_density_hessian';E=D/'evidence';P=B/'research/middle_residual/evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
archive=P/'original_knots.jsonl.gz';audit=json.loads((P/'knot_audit.json').read_text());part=json.loads((P/'partition_exact.json').read_text())
assert audit['status']=='PASS' and audit['footer_read'] and sha(archive)==audit['archive_sha256']=='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
assert sha(P/'partition_exact.json')==audit['partition_sha256'] and sha(P/'knot_manifest.json')==audit['manifest_sha256']
need=set(range(4096,4109));spans=[];cells=[]
with gzip.open(archive,'rt') as f:
 header=json.loads(next(f));assert header['type']=='header' and header['degree']==7 and header['cells']==7809
 for line in f:
  row=json.loads(line)
  if row['type']=='complete':break
  assert row['type']=='span'
  hits=sorted(need.intersection(range(row['first_cell'],row['first_cell']+row['count'])))
  if not hits:continue
  si=row['span'];sp=part['spans'][si]
  assert all(row[k]==sp[k] for k in ['first_cell','count','a_exact','b_exact'])
  assert len(row['density_polynomials'])==262 and all(len(p)==8 for p in row['density_polynomials'])
  assert all(int(v['mid_m'])==int(v['rad_m'])==0 for v in row['density_polynomials'][-1])
  a,b=F(row['a_exact']),F(row['b_exact']);center=F(row['polynomial_mid_exact']);assert center==(a+b)/2
  spans.append({k:row[k] for k in ['span','first_cell','count','a_exact','b_exact','polynomial_mid_exact','density_polynomials']})
  for ci in hits:
   i=ci-row['first_cell'];left=a+(b-a)*i/row['count'];right=a+(b-a)*(i+1)/row['count'];assert a<=left<right<=b
   cells.append({'ci':ci,'span':si,'a_exact':str(left),'b_exact':str(right)})
  need.difference_update(hits)
  if not need:break
assert not need and len(cells)==13 and all(F(x['b_exact'])==F(y['a_exact']) for x,y in zip(cells,cells[1:]))
source=B/'research/n8_source_bounds/evidence/cert_n8_fine0165.json';num=json.loads(source.read_text())
files={str(p.relative_to(B)):sha(p) for p in [archive,P/'knot_audit.json',P/'knot_manifest.json',P/'partition_exact.json',Path(__file__),D/'PROOF.md',E/'proof_first.json',source]}
out={'utc':datetime.now(timezone.utc).isoformat(),'source_header':header,'source_center_bracket_exact':[str(F(v)) for v in num['x_star_bracket']],'delta_exact':'33/2000','theta_max_exact':'3/500','ntheta':160,'radial_subdivisions':4,'spans':spans,'cells':cells,'files':files}
(E/'density_inputs.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({'utc':out['utc'],'status':'EXTRACTED_FULL_POLYNOMIALS','spans':len(spans),'cells':len(cells),'coefficients':len(spans)*262*8,'sha256':sha(E/'density_inputs.json')}),flush=True)
