"""Finite text/source arithmetic audit307. Producer code is never executed."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from decimal import Decimal
import ast,json,hashlib
import numpy as np,torch
from q_local_checkpoint import load_numeric
R=Path('research/spec62_and_n224_text_audit');V=R/'verification';checks=[];bindings={};tokens=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);v=sha(p);ck('binding '+str(p),h is None or h==v);bindings[str(p)]=v;return p
def rat(v):return F(float(v))if isinstance(v,(float,np.floating))else F(str(v))
def rounded(label,s,value,source):
 q=F(Decimal(s));u=F(10)**Decimal(s).as_tuple().exponent;v=rat(value);lo=q-u/2;hi=q+u/2;ck('rounding '+label,lo<=v<hi)
 tokens.append(dict(label=label,printed=s,value=float(v),exact_value=str(v),lower=str(lo),upper=str(hi),source=source))
for p in [Path(__file__),R/'PROOF.md',V/'INPUTS.json',V/'CHANGES.json','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
for row in json.loads((V/'INPUTS.json').read_text())['files']:bind(row['frozen'],row['sha256'])
ck('halfunit manufacture inclusive lower',F(Decimal('1.25e-7'))==F(Decimal('1.3e-7'))-F(Decimal('1e-8'))/2)
ck('negative halfunit interval',F('-0.465')<=F('-0.4565')<F('-0.455'))
ck('accepted59 exact',sha(V/'accepted59.md')=='1aae4d7b376dd505b8ea33663327faa02b591d6acc36a7912218ea5b2c6cea8b')
old=(V/'accepted59.md').read_text();new=(V/'SPEC62.md').read_text();changes=json.loads((V/'CHANGES.json').read_text());ck('four cumulative changed blocks',len(changes)==4);restored=new
for i,c in enumerate(changes):ck('unique new block '+str(i),restored.count(c['new'])==1);restored=restored.replace(c['new'],c['old'],1)
ck('whole SPEC reverse equality',restored==old);norm=lambda t:' '.join(t.split())
ck('version only',changes[0]['new'].replace('v62, 2026-10-22T01:07Z','v59, 2026-10-21T23:27Z')==changes[0]['old'])
ck('degree23 pending retained','checker 292 pending' in norm(new)and 'would give d >= 25, P >= 27/2'in new)
ck('new exact calculation is attributed',"All 49 excluded by the lead's own exact computations"in changes[1]['new'])
ck('degree23 moved to d85','for d85, code/ed85.py'in changes[1]['new']);ck('real n uncertified remains','interval existence argument for the two real non-integer solutions not certified'in norm(new))
ck('only new logentries',changes[3]['tag']=='insert'and changes[3]['new'].count('\n- v')==2 and changes[3]['new'].startswith('- v62 '))
ck('primary verdict not changed','neither convergence nor its absence established'in norm(changes[2]['new']))
repair_old='they test whether the non-convergence is quadrature-induced.'
repair_new='they compare finite-state differences obtained with changed inverse quadrature; neither convergence nor causation is established.'
ck('required overclaim located once',new.count(repair_old)==1)
for token in ['Not checked: all-node maxima','producer map matrices (unexported)','high-mode mechanism','share in the 160..224 sampled residuals']:
 ck('retained open scope '+token,token in norm(new))
parents={}
for label,path,status in [('299','research/hydrostatic_224_function_difference/verification/FINAL_BINDINGS.json','PASS'),('304','research/hydrostatic_same_node_inverse_audit/verification/FINAL_BINDINGS.json','PASS'),('289','research/hydrostatic_c2_resolved_224_audit/verification/FINAL_BINDINGS.json','PASS_SCOPED_N224_AUXILIARY_AUDIT'),('306','research/report83_installation_and84_prelim/verification/FINAL_BINDINGS.json','PASS_SCOPED_INSTALLATION_AND_PRELIM')]:
 p=bind(path);d=json.loads(p.read_text());parents[label]=d;ck('completed parent '+label,str(d['status']).startswith(status)and d['count']==len(d['checks'])and all(q['passed']for q in d['checks']))
p=Path('research/hydrostatic_224_function_difference/verification/RUN.json');run=json.loads(bind(p,parents['299']['bindings'][str(p)]).read_text());ck('nine finite increase factors',len(run['annulus_increase'])==3)
# The already audited source rows are rechecked at their recorded digests.
p=Path('research/hydrostatic_same_node_inverse_audit/verification/CHECKS.json');d304=json.loads(bind(p,parents['304']['bindings'][str(p)]).read_text());row=next(q for q in d304['rows']if q['label']=='reconstructed_node')
rounded('SPEC coordinate x','1997.518',row['x'],'304');rounded('SPEC coordinate y','65.392',row['y'],'304')
ck('node index2136','node index 2136'in new and d304['node_recipe']['index']==2136)
# Input states and summary values are independent prior results, not recomputed inverse values here.
p=Path('research/hydrostatic_c2_resolved_224_audit/verification/SUMMARY.json');s224=json.loads(bind(p,parents['289']['bindings'][str(p)]).read_text())['states'][0]
p=Path('research/hydrostatic_c2_resolved_192_audit/verification/SUMMARY.json');s192=json.loads(bind(p,'8525829a2f71d3ba61b0fbddfd2b01202c68044adfa840153f7292bd58340175').read_text())['states'][0]
ci=Path('research/hydrostatic_c2_resolved_192_audit/verification/COMPARISON_INPUTS.json');d=json.loads(bind(ci).read_text());ck('192summary recorded before review',next(q['sha256']for q in d['files']if q['path']==str(p))==bindings[str(p)])
for n in ['COMPARISON.json','REVIEW_CHECKS.json']:
 p=Path('research/hydrostatic_c2_resolved_192_audit/verification')/n;d=json.loads(bind(p).read_text());ck('192 prior gate '+n,d['status']=='PASS'and d['count']==len(d['checks'])and all(q['passed']for q in d['checks']))
p=Path('research/hydrostatic_c2_resolved_224_audit/verification/hsG_c2.0_N224_log.completed.pt');bind(p,'fd0bc052d8a5eb54d759cb4c29cbcaf2983d92c94e13eabc953503a131abc632')
with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):data=load_numeric(p)
producer=data['result'];ck('producer source identity',producer['N']==224 and producer['M']==56 and producer['c']==2 and producer['tag']=='hsG_c2.0_N224_log');ck('log mode source',producer['inner']=='log')
log=(V/'producer224.log').read_text();lines=[x.removeprefix('# RESULT ')for x in log.splitlines()if x.startswith('# RESULT ')];ck('unique completed resultline',len(lines)==1);logged=json.loads(lines[0]);ck('checkpoint/log node maximum equality',producer['nodes_Fmax']==logged['nodes_Fmax']);ck('checkpoint/log sampled rows equality',[[float(x)for x in row]for row in producer['sampled']]==logged['sampled'])
# Read proposed pairs as literal data, never execute the Python file.
tree=ast.parse((V/'reps224b.py.txt').read_text());ck('one literal augmented assignment',len(tree.body)==1 and isinstance(tree.body[0],ast.AugAssign)and ast.unparse(tree.body[0].target)=='body');pairs=ast.literal_eval(tree.body[0].value);ck('two literal replacements',len(pairs)==2 and all(len(q)==2 and all(isinstance(x,str)for x in q)for q in pairs));proposed=' '.join(q[1]for q in pairs)
ck('producer values attributed','(main computation, as above)'in proposed);ck('independent774 sample named',"checker's independent evaluation at the 774 points"in proposed);ck('far axis signed not absolute','R_h tends to the nonzero limit -0.2895'in proposed);ck('represented trial only','this state is not an exact solution either'in proposed)
for label,s,value,source in [('node Fmax','1.3e-7',producer['nodes_Fmax'],'producer metadata'),('producer annulus','4.8e-5',producer['sampled'][2][3],'producer metadata'),('producer far','4.5e-5',producer['sampled'][3][3],'producer metadata'),('E','-0.442',s224['E'],'independent289'),('B','-3.108',s224['b'],'independent289'),('B-6E','-0.46',rat(s224['b'])-6*rat(s224['E']),'independent289 arithmetic'),('delta','-4.56e-5',s224['delta'],'independent289'),('CpTheta','5.75',s224['cusp']['Cp_K'],'independent289'),('annulus774','4.95e-5',s224['final_regions']['annulus']['R_Nf']['R_Nf'],'independent289'),('far774','4.53e-5',s224['final_regions']['far']['R_Nf']['R_Nf'],'independent289'),('signed r2','-0.2895',s224['far']['values']['r2'],'independent289'),('E change','0.52',abs(rat(s224['E'])-rat(s192['E'])),'independent265/289 arithmetic'),('B change','1.13',abs(rat(s224['b'])-rat(s192['b'])),'independent265/289 arithmetic'),('Section1 E','-0.44',s224['E'],'independent289')]:
 ck('printed in literal proposal '+label,s in proposed);rounded(label,s,value,source)
tk=np.asarray(data['tk'],dtype=float);tm=(float(tk[-1])+float(tk[-2]))/2;rmax=float(data['L'])*((1+tm)/2)**.5/(1-tm)**float(data['p']);rounded('producer nominal outer midpoint','6.7e7',rmax,'own reconstruction of declared midpoint/map formula');ck('224 mapping exact parameters',float(data['L'])==1 and float(data['p'])==2 and len(tk)==225)
ck('signed r2 negative',F(s224['far']['values']['r2'])<0);ck('Echange increases',s224['E']>s192['E']);ck('Bchange increases',s224['b']>s192['b']);ck('289 far independent extent',s224['final_regions']['extent10000']['count']==774)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_WITH_REQUIRED_SPEC_REPAIR',count=len(checks),checks=checks,bindings=bindings,tokens=tokens,spec_sha256=sha(V/'SPEC62.md'),proposal_sha256=sha(V/'reps224b.py.txt'),repair=dict(old=repair_old,new=repair_new),producer_diagnostics=dict(tag=producer['tag'],nodes_Fmax_absolute=producer['nodes_Fmax'],sampled_rows=producer['sampled'],nominal_outer_midpoint=rmax),scope='Cumulative SPEC62 scope/content audit and literal N224 proposal only. No report installation. Producer maxima are source testimony; independent289 sample differs. Degree23 gate OPEN; primary UNRESOLVED.')
(V/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
