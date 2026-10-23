from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
ROOT=Path('verification');R=ROOT/'research/closing_endpoint_audit';V=R/'verification'
assert not sys.flags.optimize and Path.cwd().resolve()==ROOT and not(V/'FINAL_MATRIX_CHECKS.json').exists()
checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable binding '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
def accepted(path,num,digest=None):
 j=json.loads(bind(path,digest));ck('passing '+str(path),j['count']==len(j['checks'])==num and all(c['passed']for c in j['checks']))
 for p,h in j['bindings'].items():bind(p,h)
 return j
for p in [__file__,R/'ENDPOINT_MATRIX_FINAL_DRAFT.md',R/'CLOSING_REGULARITY_NOTE.md',ROOT/'PROMPT.md']:bind(p)
s=json.loads(bind(V/'STRUCTURAL_BINDINGS.json'));ck('accepted structural scope',s['status']=='CONFIRMED_BY_HAND_STRUCTURAL_SAFEGUARDS'and s['primary_endpoint']=='UNRESOLVED')
for p,h in s['bindings'].items():bind(p,h)
old=accepted(V/'PRIMARY_RECORD_CHECKS.json',807);precision=accepted(V/'PRIMARY_PRECISION_CHECKS.json',686)
common=ROOT/'research/primary_common_mp_sample/verification'
final=accepted(common/'FINAL_BINDINGS.json',352,'0750932980dcee8cd6b52aa57f053718f1e8143941a2d931e71358fd6e5f33db')
j=json.loads(bind(common/'CHECKS.json',final['bindings'][str(common/'CHECKS.json')]));ck('common arithmetic1910',j['count']==len(j['checks'])==1910 and all(x['passed']for x in j['checks']))
raw=json.loads(bind(ROOT/'research/smooth_N44_refinement_audit/verification/critical_points/AUDIT.json'));rows=[]
for c,o,p,crit in zip(j['rows'],old['values'],precision['critical'],raw['states']):
 n=c['N'];ck('state order '+str(n),n==o['N']==p['N']);ck('exact center data '+str(n),float(F(c['a_exact']))==o['a']and float(F(c['delta_exact']))==o['Delta']and F(c['delta_exact'])!=0)
 ck('common sample size/undefined '+str(n),c['all']['points']==51 and c['all']['undefined_Nf']==c['all']['undefined_Nv']==3)
 ck('five actual checking points '+str(n),len(crit['MP'])==p['witnesses']==5 and all(q['candidate_cell_counts']=={'equilibrium':0,'density_critical':0}for q in crit['grids'])and p['axis_sampled_brackets']==p['interior_attempts']==0)
 ck('origin is flow equilibrium but not density critical '+str(n),p['origin']['equilibrium']is True and p['origin']['density_critical']is False and p['origin']['W']==[0,0]and p['origin']['gradient']==[0,o['a']])
 ck('exact finite Jacobian '+str(n),p['origin']['DW_diagonal']==[float(F(4)-F(c['delta_exact'])),float(F(1)+F(c['delta_exact']))])
 ck('exact extent counts '+str(n),[e['points']for e in c['extents']]==[45,49,49,50,51])
 r=dict(N=n,a=o['a'],center_defect=o['Delta'],Rf=c['all']['maxima']['R_Nf']['value'],Rv=c['all']['maxima']['R_Nv']['value'],abs_R_r100=c['extents'][0]['maxima']['abs_R']['value'],old_Rv=o['Rv'],old_abs_R_r100=o['abs_R_r100'],R_degree11=o['R_degree11'],rho_degree11=o['rho_degree11'],maxima={k:{q:v[q]for q in ['index','x','y','value','displayed_fields']}for k,v in c['all']['maxima'].items()})
 ck('unchanged Rf '+str(n),r['Rf']==o['Rf']);rows.append(r)
ck('remaining common-sample N40-to44 increases',rows[1]['Rf']<rows[2]['Rf']and rows[1]['Rv']<rows[2]['Rv'])
ck('new N40 larger finite maxima',rows[1]['Rv']>rows[1]['old_Rv']and rows[1]['abs_R_r100']>rows[1]['old_abs_R_r100'])
ck('decreasing matched near absolute maxima',rows[0]['abs_R_r100']>rows[1]['abs_R_r100']>rows[2]['abs_R_r100'])
for name in ['inverse','origin','far_field','far_field_holder','physical_scaling','local_ipm_continuation','vanishing_approximate_family']:bind(ROOT/'research'/name/'PROOF.md')
for p,h in bindings.items():ck('final unchanged '+str(p),hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_CLOSING_MATRIX_FINITE_EVIDENCE_REVIEW_PENDING',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,primary_rows=rows,scope='Frozen accepted evidence and current finite table/critical-record transcriptions. Manual mathematical proof audit and actual closing model review are separate. No actual final report or end time is accepted by this check.')
(V/'FINAL_MATRIX_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
