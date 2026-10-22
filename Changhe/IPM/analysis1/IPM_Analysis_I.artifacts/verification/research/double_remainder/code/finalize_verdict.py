"""Freeze the nine-case proof, actual two-method run and Opus5.5 closure."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/double_remainder/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 run=json.loads((E/'revised_run.json').read_text());r=json.loads((E/'checks.json').read_text());a=json.loads((E/'algebra.json').read_text());o=json.loads((E/'output_audit.json').read_text());summary=json.loads((E/'review_summary.json').read_text())
 fixed={'research/double_remainder/PROOF.md':'0555234b3d4cbc116abca060b5eed8361fcec6a073c989883369ef04cecd1d06','research/double_remainder/code/check_constants.py':'cb02c37f696a48c6d2685f733a5c000918a6a8bb9e893a23bb7f1da8a975865a','research/double_remainder/code/check_algebra.py':'d0f8a7fc19d6055f4bc12f3597d720550ef895eade7cb563fcc59f120b6c244c','research/double_remainder/code/audit_output.py':'22bb03c9d6337fba85b7e80f9ad4818193409669c499077826d8feeb9ed5b997','research/double_remainder/evidence/checks.json':'9424c27434aa1c1e402d6287cf0dc164e3904f3306e70e57312cdd372f0ef635','research/double_remainder/evidence/algebra.json':'b449c0e2387bbd404648ec128ff3a99a91b208cec49344997c346a0ed023b686','research/double_remainder/evidence/output_audit.json':'9a32019e2e6ffd2681b7a63cbb42bab2d065a918a8b455661ebafbbf62da038b'}
 for p,h in fixed.items():assert sha(B/p)==h
 assert run['returncodes']==[0,0,0] and run['primary_pid']==4116796
 for p,h in run['source_hashes'].items():assert sha(B/p)==h
 for p,h in run['output_hashes'].items():assert sha(E/p)==h
 for p,h in summary['artifact_sha256'].items():assert sha(E/p)==h
 assert r['source_sha256']==fixed['research/double_remainder/code/check_constants.py'] and a['source_sha256']==fixed['research/double_remainder/code/check_algebra.py'] and o['source_sha256']==fixed['research/double_remainder/code/audit_output.py']
 assert r['proof_sha256']==a['proof_sha256']==o['proof_sha256']==fixed['research/double_remainder/PROOF.md']
 assert r['lead_snapshot_sha256']==sha(E/'lead_corner_coupling.md') and o['checks_sha256']==sha(E/'checks.json') and o['algebra_sha256']==sha(E/'algebra.json')
 assert r['status']=='PASS_SCALARS' and a['status']=='PASS_EXACT_ALGEBRA' and o['status']=='PASS' and o['block_endpoint_containments']==108 and o['global_endpoint_containments']==48
 stamps=[run['utc_start'],r['utc'],a['utc'],o['utc'],run['utc_resume']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(stamps,stamps[1:]))
 logs=[json.loads(x) for x in (E/'revised_run.log').read_text().splitlines()];assert len(logs)==9
 assert [(x['N'],x['M'],x['a'],x['b']) for x in logs[:6]]==[(x['N'],x['M'],x['a_exact'],x['b_exact']) for x in r['rows']]
 assert logs[6]=={k:v for k,v in r.items() if k!='rows'} and logs[7]=={k:v for k,v in a.items() if k not in ['multiplier_bounds','kernel_bounds']} and logs[8]=={k:v for k,v in o.items() if k not in ['machin_pi_interval','rational_case_forms']}
 for idx,public in enumerate(o['public_bounds']):
  row=r['rows'][idx];upper=F(public['C_upper_exact']);assert public['strict'] and (row['a_exact'],row['b_exact'])==(public['a_exact'],public['b_exact'])
  for method in ['arb','iv']:assert F(row['C'][method]['upper_exact'])<upper
  assert F(row['joint_C_upper_exact'])<upper
 assert summary['scalar_checks']==r['checks'] and summary['algebra_checks']==a['checks']
 assert summary['output_audit']=={k:v for k,v in o.items() if k not in ['machin_pi_interval','rational_case_forms']}
 paths={B/p for p in fixed}|{Path(__file__),E/'revised_run.json',E/'revised_run.log',E/'review_summary.json',E/'lead_corner_coupling.md',E/'proof_first.json'};reviews={}
 for tag in ['double_remainder_proof','double_remainder_closure']:
  m=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());req=(B/f'notes/reviews/{tag}_request.txt').read_text();resp=json.loads((B/f'notes/reviews/{tag}_response.json').read_text());text=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
  assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and 'ACCEPT' in text
  assert text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
  if tag.endswith('closure'):
   assert datetime.fromisoformat(run['utc_resume'])<datetime.fromisoformat(m['start_utc'])
   for p in m['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
  reviews[tag]={'actual_model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc'],'verdict':'ACCEPT_STATED_SCOPE'}
  for suff in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suff}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['All9dyadic scale configurations with explicit aspect-ratio uniform constants','Bounded double Taylor remainder on product weights in the stated strict windows, including zero orders','Vector IPM zeroth remainder constant below4.725e17 at(a,b)=(6.45,3.07), below1.114e18 at(6.495,3.403)','Conormal commutator identities and constructible finite derivative bounds, on the stated completion with distributions off axes'],'methods':'Independent nine-case analytic reconstruction. Arb512 finite vectors versus iv180 direct nine sums and128term geometric decomposition. Exact rational Machin block certificate plus Arb768 output audit. Integer polynomial kernel and multiplier verification. Actual Opus5.5 followed the uniform-majorant clarification and accepted current source; actual completed run and all pins independently rehashed.','public_bounds':o['public_bounds'],'scalar_checks':r['checks'],'algebra_checks':a['checks'],'output_checks':{'block_endpoint_containments':108,'global_endpoint_containments':48},'runtime':r['runtime'],'reviews':reviews,'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Renormalized double remainder only. Numerical derivative constants not instantiated; explicit finite formulas are given. No bounded individual canonical moments on completed global pure-weight data, annular face trace theorem, variable coupling estimate, global inverse or decisive endpoint.'}
 tmp=E/'verdict.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
if __name__=='__main__':main()
