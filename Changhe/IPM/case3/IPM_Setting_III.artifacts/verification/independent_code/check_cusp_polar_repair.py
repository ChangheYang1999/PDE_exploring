"""Result236: corrected producer cutoffs versus independent exact-data records."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import json,hashlib
R=Path('research/cusp_polar_repair_audit');V=R/'verification';checks=[];rows=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
inputs=json.loads((V/'INPUTS.json').read_text())
for x in inputs['files']:ck('frozen '+x['frozen'],sha(x['frozen'])==x['sha256'])
text=(V/'NUM_REPORT.frozen.md').read_text();table=(V/'hs_cp_form3.txt').read_text()
ck('tail wording observed','tail O(S^(p-2)), about 1e-10'in text)
ck('Kminus1 wording observed','stored K - 1 is of order 1e-16'in text)
ck('full finite-cutoff label observed','complete C_p/K (form 3, S = 1e6)'in text)
with localcontext()as ctx:
 ctx.prec=100;D=Decimal
 for root in ['hydrostatic_cusp_row_audit','hydrostatic_cusp_128_audit']:
  d=json.loads((Path('research')/root/'verification/CUSP_AXIS_CHECKS.json').read_text());ck(root+' independent gate',d['status']=='PASS'and all(t['passed']for t in d['checks']))
  for a in d['states']:
   tag=a['tag'];line=next(t for t in table.splitlines()if t.split()and t.split()[0]==tag)
   nums=[D(x.strip())for x in line.split('||')[1].replace('/',' ').split()];ck(tag+' form3 five columns',len(nums)==5)
   run=a['precision_runs'][-1];K=D(run['K']);full=D(run['Cp_K']);cuts={t['S']:t for t in a['cutoffs']};t=cuts[10**6];tail=D(t['tail_K']);cut=D(t['exact_cutoff_K']);reported=nums[-1]
   ck(tag+' complete additive identity',abs(cut+tail-full)<D('1e-75'))
   ck(tag+' raw Cp over K',abs(D(run['Cp'])/K-full)<D('1e-75'))
   ck(tag+' actual tail exceeds1e-10',abs(tail)>D('1e-9'),str(tail))
   ck(tag+' actual K defect exceeds1e-16',abs(K-1)>D('1e-12'),str(K-1))
   errors=[]
   for j,S in enumerate([1000,10000,100000,1000000]):
    if S not in cuts:continue
    exact=D(cuts[S]['exact_cutoff_K']);got=nums[j]/K;err=got-exact;errors.append(dict(S=S,producer_cutoff_K=str(got),exact_cutoff_K=str(exact),difference=str(err)))
    ck(tag+' corrected cutoff '+str(S),abs(err)<D('4e-10'),str(err))
   ck(tag+' reported normalized cutoff consistency',abs(nums[3]/K-reported)<D('1e-12'))
   cpdef=D(a['axis_runs'][-1]['cp_minus1']);r2=D(a['axis_runs'][-1]['r2']);ck(tag+' nonzero actual cp defect',cpdef!=0);ck(tag+' nonzero actual r2',r2!=0)
   linear=cpdef/(abs(1+cpdef)+1)
   rows.append(dict(tag=tag,K_minus1=str(K-1),cp_minus1=str(cpdef),linear_axis_coefficient=str(linear),r2=str(r2),full_Cp_K=str(full),tail_at_1e6_K=str(tail),exact_cutoff_at_1e6_K=str(cut),producer_reported_Cp_K=str(reported),producer_error_at_cutoff=str(reported-cut),producer_error_against_full=str(reported-full),relative_error_against_full=str(abs((reported-full)/full)),cutoff_comparisons=errors))
ck('three states',len(rows)==3)
result=dict(status='PASS'if all(t['passed']for t in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,states=rows,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),inputs_sha256=sha(V/'INPUTS.json'))
(V/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(result['status'],result['count']);print([t for t in checks if not t['passed']])
if result['status']!='PASS':raise SystemExit(1)
