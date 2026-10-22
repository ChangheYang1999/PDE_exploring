from pathlib import Path
import json,gzip,hashlib,sys
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/derivative_scalar_aggregation'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
manifest=json.loads((D/'evidence/manifest.json').read_text());first=json.loads((D/'evidence/compute.json').read_text());second=json.loads((D/'evidence/independent.json').read_text());pins=dict(second['files'])
for n,h in pins.items():assert sha(B/n)==h
expected=[]
for region,file,n in [('middle','runs__cert_deriv_middle.json',7809),('inner','runs__cert_deriv_regions_inner.json',2632),('outer','runs__cert_deriv_regions_outer.json',8948)]:
 d=json.loads((D/'sources'/file).read_text());assert d['done'] is True and len(d['rows'])==n and [r['ci'] for r in d['rows']]==list(range(n));expected.extend((region,i) for i in range(n))
with gzip.open(D/'data_exact/rows.jsonl.gz','rt') as f:
 head=json.loads(next(f));assert head['source_files']=={n:a['sha256'] for n,a in manifest['files'].items()};count=0
 for line in f:
  r=json.loads(line)
  if r['type']=='complete':assert r=={'type':'complete','rows':19389,'regions':{'middle':7809,'inner':2632,'outer':8948}} and not f.read();break
  assert r['type']=='row' and count<len(expected) and (r['region'],r['cell'])==expected[count];count+=1
 else:raise AssertionError('missing complete footer')
assert count==19389 and second['rows']==19389 and second['exact_scalar_comparisons']==232668 and second['interval_enclosures']==465336
r5=F(second['saved_R5_middle_maximum_exact']);assert F(427,1000)<r5<F(106861,250000)
report=(D/'sources/NUM_REPORT.md').read_text();extract=(D/'SOURCE_CLAIMS.md').read_text();pieces=[]
for start,end in [('Cartesian derivatives follow from','Division by the certified cell minimum'),('R5: ||eps~ - X.grad eps~||_{R0 norm}','R3 (P-disc'),('With the middle (7809 cells)','Whole-plane status: chain6 complete')]:
 a=report.index(start);b=report.index(end,a)+len(end);part=report[a:b];assert part in extract;pieces.append({'start':start,'end':end,'sha256':hashlib.sha256(part.encode()).hexdigest()})
for p in [D/'SOURCE_CLAIMS.md',D/'ADDENDUM.md',D/'evidence/independent.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SOURCE_ROW_COVERAGE_AND_REPORT_BINDING','ordered_source_rows':count,'footer_read':True,'report_excerpts':pieces,'R5_strict_interval_exact':['427/1000','106861/250000'],'files':dict(sorted(pins.items())),'scope':'Exhaustive saved-source rows and printed claim binding only. Does not certify geometric coverage or physical derivative values.'}
with (D/'evidence/coverage.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','ordered_source_rows','footer_read']}))
