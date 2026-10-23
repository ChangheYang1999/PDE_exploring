"""Bind completed finite sensitivity audit304, without new integral computation."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
R=Path('research/hydrostatic_same_node_inverse_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);s=sha(p);ck('binding '+str(p),h is None or s==h);bindings[str(p)]=s;return p
B=json.loads(bind(V/'CHECKS.json').read_text());C=json.loads(bind(V/'COMPONENTS.json').read_text())
for d,n,s in [(B,52,'PASS_FINITE_PROBES'),(C,55,'PASS_FINITE_COMPONENT_SENSITIVITY')]:
 ck('completed '+s,d['status']==s and d['count']==n==len(d['checks']) and all(x['passed'] for x in d['checks']))
for p,h in [(Path('independent_code/check_hydrostatic_same_node.py'),B['driver_sha256']),(R/'PROOF.md',B['proof_sha256']),(V/'INPUTS.json',B['input_sha256']),(R/'DESIGN_REVIEW_RESOLUTION.md',B['review_resolution_sha256']),(Path('independent_code/check_hydrostatic_same_node_components.py'),C['driver_sha256']),(R/'TAIL_COMPONENT_PROOF.md',C['proof_sha256']),(R/'MANUFACTURE_RESOLUTION_CORRECTION.md',C['correction_proof_sha256']),(V/'CHECKS.json',C['base_sha256'])]:bind(p,h)
ck('component base driver unchanged',C['base_driver_sha256']==B['driver_sha256'])
for p,h in B['modules'].items():bind(Path('independent_code')/p,h)
for p,h in B['parents'].items():bind(p,h)
I=json.loads((V/'INPUTS.json').read_text())
for z in I['sources']:bind(z['frozen'],z['sha256'])
bind(I['state']['path'],I['state']['sha256']);ck('exact fixed state',I['state']['sha256']=='4ad484e6391001597ab57d501c8b3f644259af7b4c217b5032a28b00be609d01')
F=V/'component_manufacture_first_failure';fd=json.loads(bind(F/'COMPONENTS.json').read_text());bind(F/'check_hydrostatic_same_node_components.py',fd['driver_sha256']);ck('first failure retained',fd['status']=='FAIL' and any(not z['passed'] for z in fd['checks']) and not fd.get('rows',[]))
ck('three base and component probes',len(B['rows'])==len(C['rows'])==3)
ck('principal manufacture coverage',len(B['manufactures'])==6 and all(z['scaled_error']<1e-9 for z in B['manufactures']))
ck('final diagnostic manufacture coverage',len(C['manufactures'])==15 and len([z for z in C['manufactures'] if z['ntail']==5120])==3 and all(z['scaled_error']<1e-9 for z in C['manufactures'] if z['ntail']==5120))
text=(R/'RESULTS.md').read_text();tablelines=[line.split('|')[1:-1] for line in text.splitlines() if line.startswith('| ') and any(z['label'] in line for z in B['rows'])]
ck('all printed table rows present',len(tablelines)==15)
for z,w in zip(B['rows'],C['rows']):
 label=z['label'];ck('same probe '+label,label==w['label'] and z['x']==w['x'] and z['y']==w['y'])
 ck('principal reproduced '+label,z['physical'][-1]['V']==w['principal']['V'])
 ck('four tail orders '+label,[v['ntail'] for v in w['tail_orders']]==[80,160,320,640])
 line=next(p for p in tablelines if len(p)==7 and p[0].strip()==label)
 values=[z['x'],z['y'],z['physical'][-1]['R'],z['physical'][-1]['Nf'],z['physical'][-1]['Rf'],z['diagnostic_rule']['analytic']['Rf']]
 for token,value in zip(line[1:],values):ck('printed base '+label+' '+token.strip(),abs(float(token)-value)<=6e-11*max(abs(value),1e-100))
 for t in w['tail_orders']:
  line=next(p for p in tablelines if len(p)==4 and p[0].strip()==label and int(p[1])==t['ntail'])
  for token,value in zip(line[2:],t['delta_V']):ck('printed tail '+label+' '+token.strip(),abs(float(token)-value)<=6e-9*max(abs(value),1e-100))
  ck('fixed inner contribution '+label+str(t['ntail']),abs(t['delta_J'])<3.50e-17)
 ck('three held velocities '+label,[u['name'] for u in w['mp']]==['physical','diagnostic_analytic','diagnostic_fd'])
ann=next(x for x in C['rows'] if x['label']=='annulus_probe');e=[t['delta_V'][0] for t in ann['tail_orders']];ck('corrected V1 monotone decrease',all(e[k]>e[k+1]>0 for k in range(3)))
rf=max(abs(z['held_velocity_MP']['Rf_change']) for z in B['rows']);rv=max(abs(z['Rv_change']) for row in C['rows'] for z in row['mp']);dv=max(abs(a) for row in B['rows'] for d in row['changes'] for a in d['V']);dr=max(abs(d['Rf']) for row in B['rows'] for d in row['changes'])
ck('Rf physical-only observed bound',rf<=5.58e-15);ck('Rv all held velocities observed bound',rv<=1.47255e-14);ck('velocity observed sensitivity',dv<=9.53e-13);ck('Rf quadrature observed sensitivity',dr<=4.11e-15)
ck('explicit physical-only label','held-principal-velocity' in text);ck('no false monotonicity in resolution','non-monotone initial behavior' not in (R/'FINAL_REVIEW_RESOLUTION.md').read_text());ck('Nv normalized interpretation','normalized ratio' in (R/'FINAL_REVIEW_COMPLETION.md').read_text())
ck('absolute Fmax unchanged',B['producer_nodes_Fmax_absolute']==3.93085375083313e-8 and B['producer_result']['centre']=='drop' and B['producer_result']['extra']==[])
models=[]
for label in ['design','followup','results','closure']:
 p=V/('opus_'+label);m=json.loads(bind(p/'metadata.json').read_text());resp=json.loads(bind(p/'response.json').read_text());a=bind(p/'answer.md').read_text();bind(p/'request.txt',m['request_sha256']);bind(V/('OPUS_'+label.upper()+'_REQUEST.txt'),m['request_sha256'])
 ck('actual Opus5.5 '+label,m['requested_model']=='us.anthropic.claude-opus-5-5' and m['returned_model']==resp['model']=='claude-opus-5-5')
 ck('completed model '+label,m['answer_nonempty'] and m['stop_reason']=='end_turn')
 ck('response text matches '+label,a.strip()=='\n\n'.join(z['text'] for z in resp['content'] if z['type']=='text').strip())
 models.append(dict(label=label,model=m['returned_model'],request_id=m['request_id'],started_utc=m['started_utc'],finished_utc=m['finished_utc']))
for p in [V/'closure_first_failure.json',V/'closure_first_driver.py.txt',V/'results_before_explicit_scope_sentence.md',R/'CLOSURE_SCOPE_CLARIFICATION.md',Path(__file__),R/'CLOSURE_PROOF.md',R/'FINAL_REVIEW_RESOLUTION.md',R/'FINAL_REVIEW_COMPLETION.md',R/'RESULTS.md',V/'results_before_closure_minor_fixes.md',V/'final_review_resolution_before_closure_minor_fixes.md',V/'driver_before_design_resolution.py.txt']:bind(p)
ck('explicit open scopes',all(s in text for s in ['actual map matrices','true inverse error','UNRESOLVED','not bounds','no bound on the trial density']))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_SCOPED_FINITE_RULE_AUDIT',count=len(checks),checks=checks,bindings=bindings,observed_sensitivities=dict(physical_only_Rf_MP=rf,all_held_Rv_MP=rv,physical_V_quadrature=dv,physical_Rf_quadrature=dr),actual_reviews=models,scope='Finite computed rule discrepancy and denominator interpretation CONFIRMED. No producer-map matrix reproduction or global maximum accepted. True inverse accuracy, solver causality and primary existence/nonexistence OPEN; full-plane UNRESOLVED.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
