"""Export audited root-box lower bounds, rounded down to exact millionths."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import gzip,json,hashlib
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lo(r):return F(r['lower_exact'])
def down(x):return (x.numerator*1000000)//x.denominator
bp=LANE/'proofs/68_independent_global_coefficients/evidence/full.json'
rp=TOP/'evidence/refinement.json.gz';ap=TOP/'evidence/audit.json'
b=json.loads(bp.read_text());a=json.loads(ap.read_text())
assert a['status']=='PASS' and a['base_result_sha256']==sha(bp) and a['full_result_sha256']==sha(rp)
with gzip.open(rp,'rt') as f:r=json.load(f)
rows=[{'i':i,'t0':x['left_exact'],'t1':x['right_exact'],'ma':[None]*128,'mr':[None]*128} for i,x in enumerate(b['records'])]
minimum={};location={}
for i in r['preserved_radial_indices']:
 x=b['records'][i]
 for k,out in [('ma_lower','ma'),('mr_lower','mr')]:
  val=lo(x[k]);rows[i][out]=[down(val)]*128
  if out not in minimum or val<minimum[out]:
   minimum[out]=val;location[out]={'kind':'preserved_radial','i':i,'t0':x['left_exact'],'t1':x['right_exact'],'diagnostic_theta_index':x.get('ma_argmin') if out=='ma' else None}
for leaf in r['leaves']:
 i,j=leaf['root']
 for k,out in [('ma_lower','ma'),('mr_lower','mr')]:
  val=lo(leaf[k]);v=down(val);old=rows[i][out][j];rows[i][out][j]=v if old is None else min(v,old)
  if out not in minimum or val<minimum[out]:
   minimum[out]=val;location[out]={'kind':'refined_leaf','root':[i,j],**{q:leaf[q] for q in ('t0','t1','a0','a1','depth')}}
assert all(isinstance(v,int) and v>=2500000 for row in rows for k in ('ma','mr') for v in row[k])
for k,out in [('ma_lower','ma'),('mr_lower','mr')]:assert minimum[out]==F(a['global_lower_exact'][k])
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','scale':1000000,'angle_box':'theta/pi in [j/256,(j+1)/256], j=0..127','definition':'ma or mr integer divided by scale is a rigorous lower bound on the whole root box','note':'Preserved radial cells use their common all-angle bound; refined cells use the minimum of all terminal descendants. Infinite ends are in the accepted ends certificate.','source_sha256':a['source_sha256'],'base_sha256':sha(bp),'refinement_sha256':sha(rp),'audit_sha256':sha(ap),'rows':rows}
p=TOP/'evidence/margin_map.json.gz'
with gzip.open(p,'wt') as f:json.dump(out,f,separators=(',',':'))
s={'date':out['date'],'status':'PASS','radial_cells':len(rows),'root_boxes':len(rows)*128,'map_sha256':sha(p),'script_sha256':sha(Path(__file__)),'minimum':{k:{'exact':str(minimum[k]),'diagnostic':float(minimum[k]),'location':location[k]} for k in minimum}}
(TOP/'evidence/map_summary.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps(s,indent=2))
