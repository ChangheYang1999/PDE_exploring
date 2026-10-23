"""Result285 final dependency and scope gate, no replacement of arithmetic checks."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,traceback
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(a,key,path):
 ck(str(path)+' '+key,a[key]==sha(path));bindings.append(dict(path=str(path),sha256=sha(path)))
specs=[('UNIVERSAL_NEWTON.json',320,'NEWTON_UNIVERSAL_PROOF.md','check_degree21_universal_newton.py'),('RECONSTRUCTION.json',1058,'PROOF.md','check_degree21_reconstruction.py'),('OUTER_CHECKS.json',None,'OUTER_DETERMINANT_PROOF.md','check_degree21_outer.py'),('BRANCH_CHECKS.json',282,'ZERO_BRANCH_PROOF.md','check_degree21_branches.py'),('PARTITION_CHECKS.json',335,'PARTITION_PROOF.md','check_degree21_partitions.py'),('NORMALIZED_CHECKS.json',16,'NORMALIZED_VALUES_PROOF.md','check_degree21_normalized_values.py'),('GCD_MANUFACTURED.json',15,'GCD_MANUFACTURED_PROOF.md','check_degree21_modular_manufacture.py'),('DENOMINATOR_LEDGER.json',None,'REVIEW_RESOLUTION_PROOF.md','check_degree21_denominator_ledger.py')];gates={};start=datetime.now(timezone.utc).isoformat()
def save(status):
 (V/'FINAL_CHECKS.json').write_text(json.dumps(dict(status=status,started_utc=start,finished_utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,gates={k:dict(count=a['count'],sha256=sha(V/k))for k,a in gates.items()},proof_sha256=sha(R/'FINAL_AUDIT_PROOF.md'),driver_sha256=sha(__file__),scope='Degree21 finite auxiliary moment exclusion only. Alternative lead eliminants288 and primary full-plane existence/nonexistence remain separate.'),indent=2)+'\n')
try:
 for f,count,proof,driver in specs:
  a=json.loads((V/f).read_text());gates[f]=a;ck(f+' PASS',a['status']=='PASS'and all(c['passed']for c in a['checks']));ck(f+' count',a['count']==len(a['checks'])and(count is None or a['count']==count));bind(a,'proof_sha256',R/proof);bind(a,'driver_sha256',Path('independent_code')/driver)
  if 'library_sha256'in a:bind(a,'library_sha256','independent_code/exact_degree21.py')
  if 'inputs_sha256'in a:bind(a,'inputs_sha256',V/'INPUTS.json')
  if 'universal_sha256'in a:bind(a,'universal_sha256',V/'UNIVERSAL_NEWTON.json')
  if 'reconstruction_sha256'in a:bind(a,'reconstruction_sha256',V/'RECONSTRUCTION.json')
  if 'gcd_proof_sha256'in a:bind(a,'gcd_proof_sha256',R/'GCD_CERTIFICATE_PROOF.md')
  if 'gcd_driver_sha256'in a:bind(a,'gcd_driver_sha256','independent_code/modular_gcd_certificate_285.py')
 bind(gates['UNIVERSAL_NEWTON.json'],'other_library_sha256','independent_code/exact_polynomial_275.py');bind(gates['RECONSTRUCTION.json'],'types56_proof_sha256',R/'TYPES56_PROOF.md');bind(gates['PARTITION_CHECKS.json'],'source_sha256',V/'external/enumeration.json');bind(gates['NORMALIZED_CHECKS.json'],'source_sha256',V/'external/certificate_13.json')
 inp=json.loads((V/'INPUTS.json').read_text())
 for f in inp['files']:ck('frozen '+f['frozen'],sha(f['frozen'])==f['sha256']);bindings.append(dict(path=f['frozen'],sha256=f['sha256']))
 rec=gates['RECONSTRUCTION.json'];out=gates['OUTER_CHECKS.json'];part=gates['PARTITION_CHECKS.json'];branches=gates['BRANCH_CHECKS.json'];den=gates['DENOMINATOR_LEDGER.json']
 ck('29 pattern certificates',len(rec['cases'])==29 and sorted(x['index']for x in rec['cases'])==list(range(1,30)));ck('29outer identities',len(rec['jobs'])==29 and len(out['cases'])==29 and [j['name']for j in rec['jobs']]==[j['name']for j in out['cases']]);ck('103 enumeration29survivors',part['partition_count']==103 and len(part['survivors'])==29);ck('8zero branches',len(branches['branches'])==8);ck('29denominator cases',len(den['rows'])==29)
 for row in out['cases']:
  ck(row['name']+' complete polynomial identity',row['samples']==row['bound']+1 and row['target_degree']<=row['bound'] and Fraction(row['constant'])!=0 and bool(row['finished_utc']));m,n,a,b=row['degrees'];ck(row['name']+' bound',row['bound']==n*a+m*b)
 norm=gates['NORMALIZED_CHECKS.json'];ck('91positive typeV core coefficients',len(norm['core_shifted_coefficients'])==91 and all(int(c)>0 for c in norm['core_shifted_coefficients']))
 proof='\n'.join((R/f).read_text()for f in ['PROOF.md','TYPES56_PROOF.md','REVIEW_RESOLUTION_PROOF.md','FINAL_AUDIT_PROOF.md']);ck('scope and branches explicit',all(t in proof for t in ['eta>=23','1322','degree1222','eta-x','T^12','G160','six typeIV','two typeVI','full-plane']))
 ck('interrupted attempts retained',(V/'before_modular_gcd_repair/INTERRUPTION_BEFORE_GCD_REPAIR.json').exists()and(V/'before_universal_substitution/TIMEOUT.json').exists())
 save('PASS');print('PASS',len(checks),datetime.now(timezone.utc).isoformat())
except Exception:
 save('FAIL');(V/'final_traceback.txt').write_text(traceback.format_exc());raise
