"""Pin the actual exterior run, source, saved endpoints and adversarial closure."""
import hashlib,json,os,sys
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/exterior_flow/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1<<20),b''):h.update(x)
 return h.hexdigest()
def main():
 fixed={'research/exterior_flow/PROOF.md':'a803ef973cfb25999173c10b0bf566794b42a4fd9ec5dea9a63ceb8b670e1a5e','research/exterior_flow/code/check_tail.py':'74b42d975dc0409418444d6eb199c668a26013dc01a428d442f75bae75cab427','research/exterior_flow/code/audit_output.py':'db198d6abef1f20c8463f60c0d690bd3204974b0868644d18d9ae74b250cd5ab','research/exterior_flow/evidence/checks.json':'3742c1d9f5d7fc76f058fa2f4f8bff340acc253e0d6bc3e2e86f7a3855683a83','research/exterior_flow/evidence/output_audit.json':'dbb955bbf5dd9e5d4ba96bbd6ff5b4f0d1a500d2ce43719afa7ec924b1d91a3f'}
 for p,h in fixed.items():assert sha(B/p)==h
 r=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());run=json.loads((E/'final_serialized_run.json').read_text())
 assert a['status']=='PASS' and a['comparison_count']==13 and a['checks_sha256']==sha(E/'checks.json')
 assert r['source_sha256']==fixed['research/exterior_flow/code/check_tail.py'] and r['proof_sha256']==fixed['research/exterior_flow/PROOF.md']
 assert a['source_sha256']==fixed['research/exterior_flow/code/audit_output.py'] and a['proof_sha256']==r['proof_sha256']
 for p,h in r['dependencies_sha256'].items():assert sha(B/p)==h;fixed[p]=h
 assert run['returncodes']==[0,0] and run['primary_pid']==4116796
 for p,h in run['source_hashes'].items():assert sha(B/p)==h
 for p,h in run['output_hashes'].items():assert sha(E/p)==h
 assert datetime.fromisoformat(run['utc_start'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(a['utc'])<datetime.fromisoformat(run['utc_resume'])
 logs=[json.loads(x) for x in (E/'final_check_run.log').read_text().splitlines()];assert len(logs)==8
 assert [x['T'] for x in logs[:6]]==['0','1/16','1/8','1/4','1','9'];assert logs[6]['status']==r['status'] and logs[6]['checks']==r['checks'];assert logs[7]=={k:v for k,v in a.items() if k!='comparisons'}
 # Recheck public endpoints without mutating the accepted audit file.
 from fractions import Fraction as F
 for row in a['comparisons']:
  if 'strict_public_upper_exact' in row:assert F(row['upper_exact'])<F(row['strict_public_upper_exact'])
  else:assert F(row['joint_lower_exact'])>F(row['strict_public_lower_exact'])
 paths={B/p for p in fixed}|{Path(__file__),E/'final_serialized_run.json',E/'final_check_run.log'};review={}
 for tag in ['exterior_flow_review','exterior_flow_closure']:
  m=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());req=(B/f'notes/reviews/{tag}_request.txt').read_text();assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
  if tag.endswith('closure'):
   for p in m['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
   assert datetime.fromisoformat(run['utc_resume'])<datetime.fromisoformat(m['start_utc'])
  review[tag]={'actual_model':m['actual_response_model'],'end_utc':m['end_utc'],'verdict':'ACCEPT_CONDITIONAL_ON_UPSTREAM_EXTERIOR_SCOPE'}
  for suff in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suff}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['Entire exterior modal velocity with every261mode and11exponent family retained','Uniform Cartesian quotients through both axes with decay r^(k-1)','Outward drift X.V>3.83r^2 for r>=3634','For r>=4000: |Ur/r|<.104(4000/r)^(1-k), |Ui/Xi|<.313(4000/r)^(1-k), X.V>5.47r^2 and Vi/Xi>5.26'], 'methods':'Arb512 canonical Green forcing and original-basis exact monomial maxima; independent iv180 density-moment polynomial recurrence and shifted positive-series factorial bounds. Exact affine identities, previously audited shared canonical boundary data, exact public rounding, actual completed source-pinned run and independent file rehashing. Actual Opus5.5 closure corrected its first review homogeneous-mode error.','public_conclusions':a['public_conclusions'],'checks':r['checks'],'runtime':r['runtime'],'reviews':review,'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Exact normalized modal trial only, with all upstream canonical input/enclosure pins reverified. The two new methods share the audited normalization and boundary moments; no fresh independent integration of those moments. No bounded-region no-zero/sign proof, global flow assembly, coupled inverse, nonlinear closure or decisive endpoint.'}
 tmp=E/'verdict.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths),'checks':r['checks']}))
if __name__=='__main__':main()
