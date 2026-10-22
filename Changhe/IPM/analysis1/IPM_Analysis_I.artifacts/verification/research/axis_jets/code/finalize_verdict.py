"""Source/output binding and completed text-review closure for topic58."""
import json,hashlib,sys,os
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/axis_jets/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
 r=load(E/'checks.json');run=load(E/'local_run.json')
 assert r['status']=='PASS' and run['returncode']==0
 assert r['source_sha256']==sha(B/'research/axis_jets/code/check_exact.py')=='1b06958def5949ea24742595fa8fd8376b77479bc71f1729c3d78955902d6a4e'
 assert r['proof_sha256']==sha(B/'research/axis_jets/PROOF.md')=='2bb1bf7c4af14900015593bcd384faa14a7b4e486c26f3127c2093788e633657'
 assert r['input_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
 k=F(r['model_constant']['k_exact']);A=F(r['model_constant']['A_exact']);M=F(r['model_constant']['M_exact']);assert A==2/k-1 and M==F(7,12)/A
 for row in r['model_constant']['enclosures']:assert F(row['lower_exact'])<=M<=F(row['upper_exact'])
 for ex in r['evaluation_examples']:
  e,m=F(ex['epsilon']),F(ex['m']);assert F(ex['inverse_norm'])==e/abs(m) and F(ex['evaluation_X_norm'])==1/e
 assert r['checks']=={'trace_equation':1,'coupled_P_row':1,'center_cancellations':2,'taylor_denominators':9,'homogeneous_exponent':1,'rational_model':4,'kernel_constant':5,'non_Dini_counterexample':2,'evaluation_scaling_examples':9,'block_norms':4,'exact_constant_containments':2}
 paths={Path(__file__),B/'research/axis_jets/PROOF.md',B/'research/axis_jets/code/check_exact.py',B/'data_exact/modal_v2.json'}|{E/p for p in ['checks.json','local_run.json','review_repairs.json','proof_first.json','lead_global_flow.md']};reviews={}
 for tag in ['axis_jets_proof','axis_jets_closure']:
  meta=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert meta['actual_response_model']==resp['model']=='claude-opus-5-5' and meta['stop_reason']==resp['stop_reason']=='end_turn'
  assert sha(B/f'notes/reviews/{tag}_request.txt')==meta['input_sha256']
  assert text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
  if tag.endswith('closure'):
   assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(run['end_utc'])<datetime.fromisoformat(meta['start_utc'])
   for p in meta['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
  reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'end_utc':meta['end_utc']}
  for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SCOPED_RESULTS_AND_REFUTATIONS','confirmed':['Axis transport equation, exact-profile P compatibility with nonzero G1(P), full coupled P-row','Evaluation-norm ratio lower bound','Center cubic cancellation','Local homogeneous exponents and Taylor denominators','Inner inverse formula on the open interval, with Dini sufficient for finite endpoint; C1 sufficient for C1 endpoint','Conditional triangular block inverse bound in specified domains and sum norms'], 'refuted':['Norm-independent transport inverse lower bound from merely bounded evaluations','Claim that zero center coefficient does not remove an inner homogeneous mode','Endpoint/bounded-inverse interpretation of J7 under only continuous f(P)=0'], 'open':['Compatible numerical-profile jet realization and quantitative inverse','Nonlocal P-row solvability','Jet extension commutator into the remainder norm','Full PDE endpoint'], 'checks':r['checks'],'model_constant':r['model_constant'],'illustrative_parameter_definition':'For the rational model only, c_l=1/k is assigned using the exact modal k and A=2/k-1. The arithmetic checks do not certify that the rational model is the trial field.','methods':'Independent analytic proof; exact symbolic jets and rational counterexamples; Arb512 arithmetic versus iv180 expanded-integral arithmetic, both also compared to an exact rational value; finalizer exact output/source binding.','reviews':reviews,'review_corrections':load(E/'review_repairs.json'),'runtime':r['runtime'],'scope':'Transport jets and conditional block algebra only. No numerical-profile inverse or PDE existence/exclusion.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
 t=E/'verdict.json.tmp';t.write_text(json.dumps(result,indent=2)+'\n');os.replace(t,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
if __name__=='__main__':main()
