from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import hashlib,json,numpy as np
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification';tag='dnB_n84m35S';read=lambda tail:json.loads((V/(tag+'_'+tail+'.json')).read_text());s=read('summary');b=read('broad4096');p=read('physical');c=read('center_certificate');checks=[]
assert p['complete'] and b['complete'] and c['complete'];assert s['source_md5']==p['source_md5']==b['source_md5']==c['source_md5']
for key,suffix in [('physical','physical'),('broad','broad4096'),('balls','balls'),('strain','strain'),('reconstruction','reconstruction')]:assert hashlib.sha256((V/(tag+'_'+suffix+'.json')).read_bytes()).hexdigest()==s['input_hashes'][key]
for row in c['dependencies']:assert hashlib.sha256(Path(row['file']).read_bytes()).hexdigest()==row['sha256']
assert s['state']['first_row_unit'] and c['certificates_overlap'] and not c['self_consistency_contains_zero']
assert s['frozen_field_smoothness_excluded']==(not s['center']['contains_zero']['rho5_sine7_coefficient'])
assert s['frozen_field_transport_excluded']==(not s['center']['contains_zero']['transport_balance_determinant'])
values=[]
for row in b['rows']:
 x=row['point'];u=row['U'];g=row['gradient'];rho=row['rho'];W=[s['state']['cl']*x[j]+u[j] for j in range(2)];res=sum(W[j]*g[j] for j in range(2))-rho;nf=abs(rho)+sum(abs(W[j]*g[j]) for j in range(2));assert abs(res-row['R'])<1e-10;assert abs(nf-row['N_report_f'])<1e-10;assert abs(abs(res)/nf-row['absR_report_f'])<1e-12;values.append(abs(res)/nf)
assert len(values)==58;ind=int(np.argmax(values));assert s['broad']['max_R_report_f_point']==b['rows'][ind]['point'];assert abs(s['broad']['max_R_report_f']-values[ind])<1e-12
assert s['broad']['max_U_exterior_bound']==max(float(Fraction(r['exact_U_tail_bound'])) for r in b['rows'])
for i,row in enumerate(s['inverse_comparison6']):
 lo,hi=[a['transport'][i] for a in p['passes']];diff=sum((hi['U'][j]-lo['U'][j])*hi['gradient'][j] for j in range(2))/hi['N_report_f'];assert abs(diff-row['signed_R_change_fixed_fine_Nf'])<1e-18
out={'utc':datetime.now(timezone.utc).isoformat(),'source_md5':s['source_md5'],'verdict':'PASS','scalar_rows_checked':len(values),'six_angular_differences_checked':6,'center_dependency_hashes_checked':len(c['dependencies']),'maximum_R_Nf':max(values),'canonical_identity_defect_exact_ball':c['first_self_consistency_ball'],'second_exact_ball':c['second_self_consistency_ball'],'summary_sha256':hashlib.sha256((V/(tag+'_summary.json')).read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Recorded finite arithmetic and provenance. No additional inverse or general certificate validation is asserted.'};(V/'summary_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
