"""Bind the conditional transport proof to two arithmetic paths and actual review."""
import json,hashlib,math,sys,os
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/box_transport/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 fixed={'research/box_transport/PROOF.md':'d3ed4ff6d5ecc4a1cea368f5f673440ac46ac4a3224e80a03f58424733842dd0','research/box_transport/code/check_constants.py':'70a7e2cd20af14b2bb2f0ed482564192576c8a5714f88a6a84b559f4febe8803','research/box_transport/code/audit_output.py':'dbbd39fbcebf8d57476ab46e6467c637a141ffadffdcf53ec8ee1988fbb27aad','research/box_transport/evidence/checks.json':'51f90436d89db82df8df4204d6e3cb611451fb3fc1c1d98b2b8f1feec482edc4','research/box_transport/evidence/output_audit.json':'c7bda7b2f34ce11c47cc485cbc878c297592c15444a9f198d815178462f63593','research/box_transport/evidence/lead_global_flow_v2.md':'ed3a6f7638bbf323fad0124d395e9fc483d552d1832c24c33223fd34ec9406ea'}
 for p,h in fixed.items():assert sha(B/p)==h
 r=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());run=json.loads((E/'final_serialized_run.json').read_text())
 assert r['status']=='PASS_CONDITIONAL_CONSTANTS' and a['status']=='PASS' and a['two_sided_checks']==4
 assert r['source_sha256']==fixed['research/box_transport/code/check_constants.py'] and a['source_sha256']==fixed['research/box_transport/code/audit_output.py']
 assert r['proof_sha256']==a['proof_sha256']==fixed['research/box_transport/PROOF.md'] and a['checks_sha256']==fixed['research/box_transport/evidence/checks.json']
 assert r['lead_snapshot_sha256']==fixed['research/box_transport/evidence/lead_global_flow_v2.md']
 assert run['returncodes']==[0,0] and run['primary_pid']==4116796
 for p,h in run['source_hashes'].items():assert sha(B/p)==h
 for p,h in run['output_hashes'].items():assert sha(E/p)==h
 assert datetime.fromisoformat(run['utc_start'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(a['utc'])<datetime.fromisoformat(run['utc_resume'])
 logs=[json.loads(x) for x in (E/'final_check_run.log').read_text().splitlines()]
 assert len(logs)==2 and logs[0]['status']==r['status'] and logs[0]['checks']==r['checks'] and logs[1]==a
 exact=[]
 for row,lo,hi in zip(r['rows'],[F('6.244'),F('5.694')],[F('6.245'),F('5.695')]):
  kap=F(row['kappa_exact']);z=(F(123,100)+kap)*F(101,650);assert z==F(row['K_exact'])
  n=row['series']['degree'];assert n==128
  partial=sum(z**j/F(math.factorial(j)) for j in range(n+1));tail=z**(n+1)/F(math.factorial(n+1))/(1-z/(n+2))
  assert partial==F(row['series']['sum_exact']) and tail==F(row['series']['tail_majorant_exact'])
  assert lo<partial/kap<(partial+tail)/kap<hi
  for method in ['arb','iv']:
   x=row[method];assert lo<F(x['lower_exact'])<=partial/kap<(partial+tail)/kap<=F(x['upper_exact'])<hi
  exact.append({'kappa':str(kap),'strict_lower':str(lo),'strict_upper':str(hi)})
 assert F(101,650)-F(50,11)==F(r['log_bound_derivative_upper_exact'])<0
 paths={B/p for p in fixed}|{Path(__file__),E/'final_serialized_run.json',E/'final_check_run.log'};reviews={}
 for tag in ['box_transport_review','box_transport_closure','box_transport_final']:
  m=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());req=(B/f'notes/reviews/{tag}_request.txt').read_text();res=json.loads((B/f'notes/reviews/{tag}_response.json').read_text());answer=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert m['actual_response_model']==res['model']=='claude-opus-5-5' and sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256']
  assert res['stop_reason']==m['stop_reason']
  assert answer=='\n\n'.join(c['text'] for c in res['content'] if c['type']=='text')+'\n'
  if tag=='box_transport_closure':assert m['stop_reason']=='max_tokens'
  else:assert m['stop_reason']=='end_turn' and 'ACCEPT' in answer
  if tag in ['box_transport_closure','box_transport_final']:
   for p in m['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
   assert datetime.fromisoformat(run['utc_resume'])<datetime.fromisoformat(m['start_utc'])
  reviews[tag]={'actual_model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc'],'accepted_closure':tag=='box_transport_final'}
  for suff in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suff}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL','claims':['Monotone-y box visits form one interval, with explicit residence and positive-history cost','Pure transport maximal-domain inverse norm at most exp(K)/kappa from complete C1 quadrant flow and box/complement margins','Separate NT-prime alpha-limit argument under its additional strict-y and axis hypotheses','Under the enlarged-box inequalities the inverse norm is strictly below5.695 at kappa11/50'], 'refuted':'The enlarged-box upper-bound expression at kappa1/5 is not <=6.2; it lies strictly between6.244and6.245. This is not a lower bound on the actual inverse.', 'methods':'Independent analytic reconstruction; Arb512 exponential versus iv180 positive Taylor series with geometric tail; independent exact factorial rational certificate and local source/run/review rehashing. Actual Opus5.5 end_turn closure follows a truncated review and the repaired Volterra-domain explanation.', 'exact_public_bounds':exact,'checks':r['checks'],'runtime':r['runtime'],'reviews':reviews,'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Conditional theorem only. Actual trial box speed, margins, global V2 sign and all bounded-region geometry remain OPEN. No Garding estimate, nonlocal coupling control, coupled inverse, nonlinear closure or decisive endpoint. The smaller floating-box6.1example is a different uncertified calculation.'}
 tmp=E/'verdict.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
if __name__=='__main__':main()
