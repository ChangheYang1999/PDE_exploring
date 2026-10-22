from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,ast,time
V=Path('research/316_portable_residual_package/verification'); start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();C=[]
def ck(n,v,d=None):C.append(dict(name=n,passed=bool(v),detail=d))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
j=json.loads((V/'checks.json').read_text());m=j['manifest'];missing=[x['file']for x in m if x['artifact']is None]
ck('66_valid_code_records',len(m)==66 and all(x['declared']==x['code']for x in m))
ck('55_valid_artifact_copies',sum(x['artifact']==x['declared']for x in m)==55)
ck('11_absent_copies',len(missing)==11)
ck('33_failures_only_copy_assumption',len(j['failures'])==33 and all(x['category']in {'manifest_artifact_present','artifact_checksum_current','code_artifact_same'} and x['detail']in missing for x in j['failures']))
ck('every_missing_has_three',all(sum(f['detail']==s for f in j['failures'])==3 for s in missing))
ck('CSV_bytes_identical',sha(V/'target.csv')==sha(V/'independently_reconstructed.csv')==j['reconstructed_csv_sha256'])
choices=j['archive_choices'];pkg=sum(any(s.startswith('artifacts/verifier/')for s in paths)for paths in choices.values());runs=sum(not any(s.startswith('artifacts/verifier/')for s in paths)for paths in choices.values())
ck('all119_hashes',len(choices)==119);ck('all_paths_portable',all(all(s.startswith(('artifacts/verifier/','runs/')) and '..'not in Path(s).parts for s in paths)for paths in choices.values()))
ck('complete_source_split',pkg+runs==119)
# Parse source syntax, never import or execute it.
tree=ast.parse((V/'generator_readonly.py').read_text());imports=set()
for n in ast.walk(tree):
 if isinstance(n,ast.Import):imports.update(z.name for z in n.names)
 if isinstance(n,ast.ImportFrom):imports.add(n.module)
ck('generator_imports_only_stdlib_numpy',imports=={'json','glob','os','re','csv','numpy'},sorted(imports))
ck('generator_copy_exists_and_matches',next(x for x in m if x['file']=='consolidate_audits.py')['artifact']==sha(V/'generator_readonly.py'))
rd=(V/'README.md').read_text();changes=[
('No candidate data: no unforced B2-P candidate was obtained; every state is a forced-problem state.', 'No unforced B2-P candidate was obtained. The consolidated table contains 121 forced-problem audit entries and two manufactured-control entries; repeated archive hashes occur across comparisons.'),
('../code. Every command below runs on one GPU in minutes unless stated.', '../code. Hardware requirements and runtimes depend on the script. Consolidation reads saved JSON and NPZ data using Python and NumPy.'),
('the eight 48-point\n  quadrature restarts / roots)', 'six 48-point quadrature restarts and the two tighter secant states computed at 12 and 48 points)'),
('are those in runs/. Regenerating from the lane directory:', 'are stored under artifacts/verifier/ and runs/. Both directories are inputs to the reconstruction. Regenerating from the lane directory:'),
('- code_sha256.txt refreshed 07:58Z.', '- code_sha256.txt refreshed 07:58Z; its paths are relative to code/. At the verifier\'s 08:20Z read, all 66 records matched that directory, 55 also had matching copies in artifacts/, and 11 did not have artifact copies. This is a code-directory inventory, not a complete artifact-file manifest.')]
new=rd
for i,(a,b)in enumerate(changes):ck('replacement_anchor_'+str(i),new.count(a)==1,new.count(a));new=new.replace(a,b)
ck('README_no_all_forced', 'every state is a forced-problem state'not in new)
ck('README_no_all_GPU', 'Every command below runs on one GPU in minutes'not in new)
ck('README_mixed_Q_orders','two tighter secant states computed at 12 and 48 points'in new)
ck('README_both_archive_roots','Both directories are inputs to the reconstruction'in new)
ck('README_manifest_scope','code-directory inventory, not a complete artifact-file manifest'in new)
# Preserve all exact command lines, solely prose repairs.
cmd=lambda s:[x.strip()for x in s.splitlines()if x.lstrip().startswith('python3 ')]
ck('all_command_lines_unchanged',cmd(new)==cmd(rd))
(V/'approved_README.md').write_text(new)
(V/'required_README_replacements.json').write_text(json.dumps([dict(old=a,new=b)for a,b in changes],indent=2)+'\n')
out=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in C),total=len(C),checks=C,missing_artifact_copies=missing,required_hashes_in_package=pkg,required_hashes_supplied_only_by_runs=runs,imports=sorted(imports),code_sha256=sha(Path(__file__)),approved_README_sha256=sha(V/'approved_README.md'),scope='Documented manifest root and finite table portability; no teammate code run and no assertion all README commands audited.')
(V/'scope_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ('checks','missing_artifact_copies')},indent=2));print('FAILURES',[x for x in C if not x['passed']])
