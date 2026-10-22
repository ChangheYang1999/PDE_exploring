from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_c2_repair'
def check(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
pins={}
a=json.loads((D/'evidence/compute.json').read_text());b=json.loads((D/'evidence/independent.json').read_text());old=json.loads((B/'research/gram_conforming_repair/evidence/compute.json').read_text());image=B/'research/operator_image_joins/evidence/verdict.json';im=json.loads(image.read_text())
for evidence in (a,b,im):
 for n,h in evidence['files'].items():check(sha(B/n)==h,'pin '+n);check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(a['L_exact']==old['L_exact'] and a['k_exact']==old['k_exact'],'same norm parameters')
rows=[];matches=0
for x,y,z in zip(a['records'],b['records'],old['records'],strict=True):
 for key in ('source','M','N','independent_repaired_functions'):check(x[key]==y[key]==z[key],'same family '+key)
 starts=[];ends=[];degrees=set()
 for p,q,r in zip(x['columns'],y['columns'],z['columns'],strict=True):
  check(p['column_index']==q['column_index']==r['column_index'] and p['label']==q['label']==r['label'],'same raw column');degrees.add(p['first_piece_degree'])
  check(p['pieces']==q['pieces'],'both engines all exact records');starts.append(F(p['pieces'][0]['a_exact']));ends.append(F(p['pieces'][-1]['b_exact']))
  for pp,rr in zip(p['pieces'],r['pieces'],strict=True):
   check(pp['a_exact']==rr['a_exact'] and pp['b_exact']==rr['b_exact'],'same piece');check(pp['target_left_jet'][0]==rr['beta_left'] and pp['target_right_jet'][0]==rr['beta_right'],'same exact continuous value targets');check(pp['exact_original_square_integral']==rr['exact_original_square_integral'],'same denominator moments');matches+=1
   check(-5<F(pp['a_exact'])<F(pp['b_exact'])<9,'annular support bound')
  check(p['pieces'][0]['target_left_jet']==p['pieces'][-1]['target_right_jet']==['0/1']*3,'all exterior jets zero')
 check(len(starts)==len(set(starts)) and starts==sorted(starts),'independence order');check(degrees=={7},'all first pieces degree7')
 rows.append({'M':x['M'],'N':x['N'],'independent_repaired_functions':x['independent_repaired_functions'],'first_piece_degrees':sorted(degrees),'minimum_support_log_endpoint_exact':str(min(starts)),'maximum_support_log_endpoint_exact':str(max(ends)),'public':x['public'],'largest_ratio_column':x['largest_ratio_column']})
# Exact determinant of the factored endpoint matrix: det = 2*w^9, w>0.
mat=[[1,1,1],[3,4,5],[6,12,20]];det=sum((-1)**j*mat[0][j]*(mat[1][(j+1)%3]*mat[2][(j+2)%3]-mat[1][(j+2)%3]*mat[2][(j+1)%3])*(-1)**j for j in range(3));check(det==2,'factored Hermite system determinant')
for p in (D/'evidence/compute.json',D/'evidence/independent.json',B/'research/gram_conforming_repair/evidence/compute.json',image,Path(__file__)):pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SAME_RAW_FAMILY_COMMON_PARTITION_WEIGHT_AND_C0_BINDING','same_piece_records':matches,'totals':a['totals'],'independent_totals':b['totals'],'unit_Hermite_jet_checks':b['unit_Hermite_jet_checks'],'factored_endpoint_matrix_determinant':det,'records':rows,'files':dict(sorted(pins.items())),'scope':'Every same-family, support, degree and norm binding needed by the scoped repair theorem; full spectra and endpoints OPEN.'};p=D/'evidence/binding.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pieces':matches,'pins':len(pins),'records':rows}))
