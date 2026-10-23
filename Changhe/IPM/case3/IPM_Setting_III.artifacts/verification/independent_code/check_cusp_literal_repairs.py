"""Result236 follow-up: numeric repairs and observable mismatch, without producer code."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,localcontext
import hashlib,json
R=Path('research/cusp_polar_repair_audit');V=R/'verification/repaired';checks=[];D=Decimal
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
flat=lambda s:' '.join(s.split())
def ck(name,ok,evidence=None):checks.append(dict(name=name,passed=bool(ok),evidence=evidence))
for x in json.loads((V/'INPUTS.json').read_text())['files']:ck('frozen '+Path(x['frozen']).name,sha(x['frozen'])==x['sha256'])
a=json.loads((R/'verification/CHECKS.json').read_text());ck('236 parent44',a['status']=='PASS'and a['count']==44 and all(x['passed']for x in a['checks']))
ck('236 proof unchanged',a['proof_sha256']==sha(R/'PROOF.md'))
text=flat((V/'NUM_REPORT.md').read_text());notes=flat((V/'NUM_NOTES.md').read_text());readme=flat((V/'ARTIFACTS_README.md').read_text());src=flat((V/'hs_solve.txt').read_text())
for x in ['trace-dependent coefficient; the exact tails beyond 1e6 are -7.2e-9 / +3.6e-8 / +4.0e-7 K','C_p/K at S = 1e6 (form 3; finite-cutoff estimates of the complete values)','their complete C_p/K is -1.441028e-5 / +7.822256e-5 / +8.534005e-4','the stored K - 1 of these states is +1.7e-11 / +4.2e-11 / +2.1e-10','stored floating-point c p - 1 = -2.96e-16','crossovers 2.2e10 for hsH 64, 2.0e11 for hsH 96, 6.4e9 for hsH 128']:
 ck('repair wording '+x,x in text)
ck('old tail size removed','tail O(S^(p-2)), about 1e-10'not in text)
ck('finite cutoff complete label removed','complete C_p/K (form 3, S = 1e6)'not in text)
ck('remaining observable error explicitly present','adds a linear axis term -1.48e-16 y to R_h' in text)
ck('historical K size labelled withdrawn',"(the first version of this paragraph said 'of order 1e-16')"in text)
for label,t in [('report',text),('README',readme)]:
 ck(label+' panel count formula','n = ceil(4 log10(max_rows y))'in t)
 ck(label+' minimum rather than equality','at least 4'in t)
ck('producer code comment minimum','at least per_decade panels per decade, more for inner rows'in src)
ck('producer code fixed panel count','n_pan = int(math.ceil(per_decade * np.log10(max(y.max(), 10.0))))'in src)
records=[]
with localcontext()as ctx:
 ctx.prec=100
 for root in ['hydrostatic_cusp_row_audit','hydrostatic_cusp_128_audit']:
  g=json.loads((Path('research')/root/'verification/CUSP_AXIS_CHECKS.json').read_text());ck(root+' gate',g['status']=='PASS'and all(x['passed']for x in g['checks']))
  records+=g['states']
 expected=[['-1.441028e-5','-7.2e-9','1.7e-11','2.2e10'],['7.822256e-5','3.6e-8','4.2e-11','2.0e11'],['8.534005e-4','4.0e-7','2.1e-10','6.4e9']]
 maxrel=D(0)
 for old,rec,exp in zip(a['states'],records,expected):
  tag=old['tag'];ax=rec['axis_runs'][-1];ck(tag+' record identity',tag==rec['tag'])
  vals=[D(old['full_Cp_K']),D(old['tail_at_1e6_K']),D(old['K_minus1']),D(ax['asymptotic']['power_constant_crossover'])]
  for key,val,rounded in zip(['full','tail','K defect','crossover'],vals,exp):
   d=D(rounded);tol=D('0.5')*D(10)**d.as_tuple().exponent;ck(tag+' rounding '+key,abs(val-d)<=tol,dict(exact=str(val),reported=rounded,tolerance=str(tol)))
  cp=D(old['cp_minus1']);linear=cp/(abs(1+cp)+1)
  ck(tag+' leading normalized coefficient independently divided',abs(linear-D(ax['asymptotic']['linear']))<D('1e-75'))
  ck(tag+' cp rounding',abs(cp-D('-2.96e-16'))<D('0.005e-16'))
  ck(tag+' linear rounding',abs(linear-D('-1.48e-16'))<D('0.005e-16'))
  ck(tag+' finite cutoff error remains below4e-10',abs(D(old['producer_error_at_cutoff']))<D('4e-10'))
  ck(tag+' complete comparison definition',abs(abs(D(old['producer_error_against_full'])/D(old['full_Cp_K']))-D(old['relative_error_against_full']))<D('1e-90'))
  maxrel=max(maxrel,D(old['relative_error_against_full']))
 ck('literal 5e-4 bound in old verifier too small',maxrel>D('5e-4') and maxrel<D('5.2e-4'),str(maxrel))
r=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'REPAIR_PROOF.md'),driver_sha256=sha(__file__),inputs_sha256=sha(V/'INPUTS.json'),parent_sha256=sha(R/'verification/CHECKS.json'),max_relative_complete_error=str(maxrel),verdicts={'complete_cusp_tail_and_K_numbers':'CONFIRMED','minimum_panel_density':'CONFIRMED','linear_term_assigned_to_raw_Rh':'REFUTED','old_verifier_at_most_5e-4_bound':'REFUTED: actual maximum 5.147851153577e-4; use below5.2e-4 or about5e-4'})
(V/'CHECKS.json').write_text(json.dumps(r,indent=2)+'\n');print(r['status'],r['count']);print([x for x in checks if not x['passed']]);print(r['verdicts'])
if r['status']!='PASS':raise SystemExit(1)
