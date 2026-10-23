from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import json,hashlib
R=Path('research/report_hydrostatic_same_node_text');V=R/'verification';P=Path('research/hydrostatic_same_node_inverse_audit');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);s=sha(p);ck('binding '+str(p),h is None or s==h);bindings[str(p)]=s;return p
G=json.loads(bind(P/'verification/FINAL_BINDINGS.json').read_text());ck('completed304',G['status']=='PASS_SCOPED_FINITE_RULE_AUDIT' and G['count']==154==len(G['checks']) and all(z['passed']for z in G['checks']))
for p,h in G['bindings'].items():bind(p,h)
I=json.loads(bind(V/'INPUTS.json').read_text());bind(I['frozen'],I['sha256']);ck('lead stable input',I['two_reads_equal'])
B=json.loads((P/'verification/CHECKS.json').read_text());C=json.loads((P/'verification/COMPONENTS.json').read_text());b=B['rows'][0];rounded=B['rows'][1];phys=b['physical'][-1];diag=b['diagnostic_rule']['analytic'];text=(R/'REPLACEMENT.txt').read_text()
for token,value in [('1997.5179832081947',b['x']),('65.39196800919338',b['y']),('-0.774132',diag['V'][1]),('1.44e-9',diag['Rf']),('+0.541982',phys['V'][1]),('0.0250308',phys['R']),('5.00469',phys['Nf']),('0.00500146',phys['Rf']),('6.07e-6',rounded['diagnostic_rule']['analytic']['Rf']),('3.93e-8',B['producer_nodes_Fmax_absolute'])]:
 ck('displayed token '+token,token in text)
 with localcontext()as ctx:
  ctx.prec=60;d=Decimal(token);tol=Decimal(5).scaleb(d.as_tuple().exponent-1);ck('rounding token '+token,abs(Decimal.from_float(value)-d)<=tol)
ck('32commonpanels',B['node_recipe']['npan']==32 and '32 common logarithmic panels' in text);ck('three probes',len(B['rows'])==3 and [z['label']for z in B['rows']]==['reconstructed_node','rounded_node','annulus_probe']);ck('actual rounded point',rounded['x']==1998 and rounded['y']==65.4);ck('annulus probe',B['rows'][2]['x']==30 and B['rows'][2]['y']==1)
ck('finite-inner observed bound',max(abs(t['delta_J'])for row in C['rows']for t in row['tail_orders'])<=3.50e-17);ck('640differences nonzero',all(any(z!=0 for z in row['tail_orders'][-1]['delta_V']) and row['tail_orders'][-1]['ntail']==640 for row in C['rows']))
s=(P/'verification/producer_solver_static.py').read_text();ck('declared source default parameters',all(x in s for x in ['n_in=24, n_tail=80, q=3','n0=24, per_decade=4, ngl=8','np.polynomial.legendre.leggauss(n0)','np.polynomial.legendre.leggauss(n_tail)']))
ck('all finite scope caveats',all(x in text for x in ['actual matrices remains open','not inverse-error bounds or regional maxima','tail scale was not varied separately','not been reproduced','including normalization rows','three points']))
p=V/'opus_review';m=json.loads(bind(p/'metadata.json').read_text());resp=json.loads(bind(p/'response.json').read_text());a=bind(p/'answer.md').read_text();bind(p/'request.txt',m['request_sha256']);bind(V/'OPUS_REVIEW_REQUEST.txt',m['request_sha256']);ck('actualOpus5.5',m['requested_model']=='us.anthropic.claude-opus-5-5' and m['returned_model']==resp['model']=='claude-opus-5-5');ck('modelcomplete',m['stop_reason']=='end_turn'and m['answer_nonempty']);ck('modeltext',a.strip()=='\n\n'.join(z['text']for z in resp['content']if z['type']=='text').strip())
for p in [Path(__file__),R/'PROOF.md',R/'REVIEW_RESOLUTION.md',R/'RESULTS.md',R/'REPLACEMENT.txt',V/'replacement_before_model_review.txt']:bind(p)
o=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_REPLACEMENT_FINITE_SCOPE',count=len(checks),checks=checks,bindings=bindings,replacement_sha256=sha(R/'REPLACEMENT.txt'),original_proposal_sha256=I['sha256'],actual_model=dict(model=m['returned_model'],request_id=m['request_id'],started_utc=m['started_utc'],finished_utc=m['finished_utc']),scope='Replacement CONFIRMED for finite304observations only. Original full2304node maxima OPEN; no actual producer-map matrix reproduction. Whole-report insertion requires separate audit. PrimaryUNRESOLVED.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(o,indent=2)+'\n');print(o['status'],o['count'],o['utc'])
