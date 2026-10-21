"""Summarize independent finite-point domain audits without relabeling errors."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sys,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1];V=ROOT/'verification';tag=sys.argv[1]
paths={name:V/(tag+'_'+suffix+'.json') for name,suffix in [('physical','physical'),('broad','broad4096'),('balls','balls'),('strain','strain'),('reconstruction','reconstruction')]}
items={key:json.loads(path.read_text()) for key,path in paths.items()}
p=items['physical'];b=items['broad'];assert p['complete'] and b['complete']
assert p['source_md5']==b['source_md5']==items['balls']['md5']==items['strain']['source_md5']==items['reconstruction']['md5']
a,z=p['passes'];assert len(a['transport'])==len(z['transport'])==8 and len(b['rows'])==58
rows=[]
for i,(coarse,fine) in enumerate(zip(a['transport'][:6],z['transport'][:6])):
 assert coarse['point']==fine['point'] and coarse['gradient']==fine['gradient']
 du=np.array(fine['U'])-coarse['U'];g=np.array(fine['gradient']);rows.append({'index':i,'point':fine['point'],'signed_U_fine_minus_coarse':du.tolist(),'signed_R_change_fixed_fine_Nf':float(du@g/fine['N_report_f'])})
rootdelta=z['root']['xstar']-a['root']['xstar']
maxrow=max(b['rows'],key=lambda r:r['absR_report_f']);maxnv=max(b['rows'],key=lambda r:r['absR_report_v'])
minr=min(b['rows'],key=lambda r:r['rho']);maxr=max(b['rows'],key=lambda r:r['rho'])
s={'date':datetime.now(timezone.utc).isoformat(),'source_md5':p['source_md5'],'input_hashes':{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in paths.items()},'state':{k:p[k] for k in ['N','M','L','cl','beta','first_row_unit','node_range']},'origin_c':items['strain']['c'],'origin_identity_defect':items['strain']['identity_defect_3cl_1_c'],'root':z['root'],'root_fine_minus_coarse':rootdelta,'source_jacobians':z['source_jacobian'],'elliptic':z['elliptic'],'parity':z['parity'],'transport8':[{k:r[k] for k in ['point','R','N_report_f','N_report_v','absR_report_f','absR_report_v']} for r in z['transport']],'inverse_comparison6':rows,'broad':{'max_R_report_f':maxrow['absR_report_f'],'max_R_report_f_point':maxrow['point'],'max_R_report_v':maxnv['absR_report_v'],'max_R_report_v_point':maxnv['point'],'max_absolute_R':max(abs(r['R']) for r in b['rows']),'rho_sample_range':[minr['rho'],maxr['rho']],'max_gradient_step_effect_fixed_Nf':max(abs(x) for r in b['rows'] for x in r['gradient_step_R_changes_fixed_Nf']),'max_chainrule_effect_fixed_Nf':max(abs(r['chainrule_R_change_fixed_Nf']) for r in b['rows']),'max_tail_R_bound_using_numerical_gradient':max(r['tail_R_bound_using_numerical_gradient'] for r in b['rows']),'max_U_exterior_bound':max(float(Fraction(r['exact_U_tail_bound'])) for r in b['rows'])},'exact_tail_C':p['exact_tail_C'],'exact_strain_exterior_bound':p['exact_strain_tail_bound'],'center':{k:items['balls'][k] for k in ['interpretation','values','contains_zero']},'reconstruction':items['reconstruction'],'scope':'L is a compactification scale, not a finite physical boundary. Maxima are over finite prescribed samples. Refinement differences are not certified numerical-error bounds. Exact center exclusions concern each fixed ideal-node binary interpolant, not limits or another profile. No endpoint.'}
assert s['state']['first_row_unit'] and not s['center']['contains_zero']['rho5_sine7_coefficient'] and not s['center']['contains_zero']['transport_balance_determinant']
(V/(tag+'_summary.json')).write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps({k:s[k] for k in ['date','source_md5','state','origin_c','origin_identity_defect','root','root_fine_minus_coarse','broad','exact_tail_C','exact_strain_exterior_bound','parity']},indent=2))
print('inverse signed_R changes',[r['signed_R_change_fixed_fine_Nf'] for r in rows])
print('source hP-1',[r['hP']-1 for r in s['source_jacobians']])
print('near-P E/rho_x',[[r['E_over_rho_x'] for r in e['checks']] for e in s['elliptic']])
print('COMPLETE')
