from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
L=Path.cwd();B=L/'research/t2_final_summary_audit';T=L.parent/'c1-t2';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'T2_FINAL_SUMMARY.md':T/'notes/T2_FINAL_SUMMARY.md','T2_BS_check.py':T/'artifacts/arith/bs_draft55_errata_check.py','T2_BS_result.json':T/'artifacts/data/bs_draft55_errata_check_results.json','T2_draft55_excerpt.txt':T/'artifacts/data/inputs/theory_final_d55_aa2d3063_excerpt.txt','T2_ledger_excerpt.txt':T/'artifacts/data/inputs/c1t4_verify_report_excerpt_1708.txt','T2_v01_excerpt.txt':T/'artifacts/data/inputs/theory_v01_47ba2ee7_excerpt.txt','T2_sharp.md':T/'notes/T2_T4L2_sharp.md','T2_handoff.md':T/'handoff/T2_to_T1_v01.md','theory_v01.md':L.parent/'c1-t1/drafts/theory_v01.md'}
rows=[]
for name,p in files.items():raw=p.read_bytes();(B/'source'/name).write_bytes(raw);rows.append({'source':str(p),'local':'source/'+name,'sha256':hashlib.sha256(raw).hexdigest()})
assert sha(B/'source/T2_FINAL_SUMMARY.md')=='c614ca8751ac132530fd8e5824a5d82abd08b1f92936348d137785a86a8cfd9a'
lines=(L/'VERIFY_REPORT.md').read_text().splitlines();ids=[int(x.split('\t',1)[0]) for x in (B/'source/T2_ledger_excerpt.txt').read_text().splitlines()];(B/'source/own_ledger_excerpt.txt').write_text(''.join(f'{i}\t{lines[i-1]}\n' for i in ids))
(B/'data/initial_sources.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'sources':rows},indent=2)+'\n')
(B/'data/parameters.json').write_text(json.dumps({'mu':'297/1000','C':402,'cU':'8/5','sqrtW2':512,'s':'1/4096','b':'3791/1000000000','eta':'1/10000000','factor_lower':'0.99998312568','factor_upper':'0.99998312569','factor_display':'0.99998313','accepted_counts':{'family_ceiling_brackets':35,'constant_display_successors_audit':290},'boxes':[{'s':'1/262144','m':'1/131072','B':'1/100','eps_display':'1.8938e-7'},{'s':'1/262144','m':'1/65536','B':'1/200','eps_display':'6.1967e-8'}]},indent=2)+'\n')
(B/'data/PROOF_FIRST.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha(B/'PROOF.md'),'checker_exists':(B/'code/check.py').exists()},indent=2)+'\n')
print('frozen',len(rows),sha(B/'PROOF.md'))
