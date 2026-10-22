"""Link the completed two-method trace audit and actual Opus5.5 closure."""
import json,hashlib,sys,os
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3]; E=B/'research/annular_traces/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
 r=load(E/'checks.json');a=load(E/'algebra.json');o=load(E/'output_audit.json');run=load(E/'local_run.json')
 fixed={'research/annular_traces/PROOF.md':'c39e855c52a503ecdb6d26bd3360c10250cccf74509b32d70c0e8d7e1621fa93','research/annular_traces/code/check_constants.py':'964042674aecd1400224edb22152a8dea64295f2e99041c6b8bc86d0036e4ec4','research/annular_traces/code/check_algebra.py':'81cf8f1f1cac92812a29f8839e27740502397656c9b2ae16e33c4056dbccbca0','research/annular_traces/code/audit_output.py':'b91c1ce155b442e2fd38e4a0695a96b1526f26283e69294fa1b26cb058837de9','research/annular_traces/evidence/checks.json':'127538fab37f7fc3cf1b283cd563a9d4e509642a95c6f692f43fb6d7e64813b6','research/annular_traces/evidence/algebra.json':'d034ba924c4fc6b293c2fb08027f882754a8f866cdedbb2f0f94fa53785d32e9'}
 for rel,h in fixed.items():assert sha(B/rel)==h
 for item,src in [(r,'check_constants.py'),(a,'check_algebra.py'),(o,'audit_output.py')]:
  assert item['source_sha256']==sha(B/'research/annular_traces/code'/src) and item['proof_sha256']==sha(B/'research/annular_traces/PROOF.md')
 assert r['status']=='PASS_TWO_METHOD_CONSTANTS' and a['status']=='PASS_EXACT_ALGEBRA' and o['status']=='PASS'
 assert o['checks_sha256']==sha(E/'checks.json') and o['algebra_sha256']==sha(E/'algebra.json')
 assert r['checks']=={'endpoint_containments':10,'nonfinite_rejections':3,'special_function_containments':6,'constant_overlaps':216,'rows':18}
 assert o['constant_endpoint_containments']==432 and o['positive_integral_containments']==6 and len(r['rows'])==len(o['public_bounds'])==18
 assert [x['returncode'] for x in run['runs']]==[0,0,0]
 assert run['commands']==[x['command'] for x in run['runs']]==[['python3','research/annular_traces/code/'+x] for x in ['check_constants.py','check_algebra.py','audit_output.py']]
 stamps=[run['start_utc'],r['utc'],run['runs'][0]['end_utc'],a['utc'],run['runs'][1]['end_utc'],o['utc'],run['end_utc']]
 assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(stamps,stamps[1:]))
 for row,public in zip(r['rows'],o['public_bounds']):
  assert (row['trace'],row['original_a_exact'],row['original_b_exact'])==(public['trace'],public['a_exact'],public['b_exact']) and public['strict']
  upper=F(public['C_upper_exact'])
  for method in ['arb','iv']:assert F(row['constants']['C'][method]['upper_exact'])<upper
 paths={B/p for p in fixed}|{Path(__file__),E/'output_audit.json',E/'local_run.json',E/'review_repairs.json',E/'lead_corner_coupling.md',E/'proof_first.json',E/'integral_proof_first.json'}
 reviews={}
 for tag in ['annular_traces_repair','annular_traces_closure']:
  meta=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert meta['actual_response_model']==resp['model']=='claude-opus-5-5' and meta['stop_reason']==resp['stop_reason']=='end_turn'
  assert sha(B/f'notes/reviews/{tag}_request.txt')==meta['input_sha256'] and 'ACCEPT' in text
  assert text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
  if tag.endswith('closure'):
   assert datetime.fromisoformat(run['end_utc'])<datetime.fromisoformat(meta['start_utc'])
   for p in meta['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
  reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'end_utc':meta['end_utc'],'verdict':'ACCEPT_STATED_SCOPE'}
  for suff in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suff}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['All nine naturally subtracted annular traces bounded in the stated strict windows','Exact subtraction table and seven rectangular-subtraction failures','Explicit finite constants for every admitted a,b; rigorous numerical bounds at the two stated rational weight pairs'], 'methods':'Independent analytic near/far/comparable derivation; Arb512 special functions versus iv180 positive 4096-cell integral sums with rigorous tails; exact kernel and Fourier algebra; Arb768 saved-scalar recomputation. The last audit is not a third independent method.','public_bounds':o['public_bounds'],'scalar_checks':r['checks'],'algebra_checks':a['checks'],'output_checks':{'constant_endpoint_containments':432,'positive_integral_containments':6},'review_corrections':['Initial truncated answer was not accepted. Completed reviewer withdrew unexplained wrong-formula claim.','Reviewer omission of y-normal orders0,2,4 was corrected and acknowledged.','Closure phrase mu constant on the window is false: mu=A-j-1-max(Lset) varies with A. The accepted formulas and code use its actual value. Lset,P,s,K are constant for each trace.','The d>P branch of the near formula is vacuous for these nine traces but mathematically valid.'],'reviews':reviews,'runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Renormalized trace combinations on the completed parity space only. Does not establish continuity of individual canonical moments on global pure-weight data, variable coupling, conormal derivative constants, edge matching, a global inverse or a PDE endpoint.'}
 temp=E/'verdict.json.tmp';temp.write_text(json.dumps(result,indent=2)+'\n');os.replace(temp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
if __name__=='__main__':main()
