"""Own frozen-report documentary and directed finite numerical audit."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import importlib.util,json,re,time,sys
R=Path(__file__).resolve().parents[3];B=R/'research/frozen_report_1630_numerical'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);v=sha(p);assert h is None or h==v,(str(p),h,v);key=str(p.relative_to(R));assert key not in inputs or inputs[key]==v;inputs[key]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def ck(k,b):assert k not in checks;checks[k]=bool(b);assert b,k
 first=read(B/'verification/PROOF_FIRST.json');bind(B/'PROOF.md',first['proof_sha256']);bind(Path(__file__))
 revision=read(B/'verification/PROOF_FIRST_v02.json');bind(B/'PROOF_v02.md',revision['proof_sha256']);bind(B/'verification/FAILED_v01.json',revision['failed_record_sha256'])
 manifest=read(B/'source/MANIFEST.json',first['manifest_sha256'])
 for name,rec in manifest['files'].items():bind(B/'source'/name,rec['sha256'])
 bind(B/'source/FINAL_REPORT.md','244c9c223dad0925c570d594cb4afdfcbbcb8196d5981a6c8cf024827813f838')
 bind(B/'source/closure_matrix.md','6a6c2bc0fac0460b0add7b2e6d139bd49eb30d6973e96180a8d8543c668c0982')
 helper=bind(R/'research/final_table_trace/code/check_documentary_v02.py')
 spec=importlib.util.spec_from_file_location('own_table_parser',helper);P=importlib.util.module_from_spec(spec);spec.loader.exec_module(P)
 report=(B/'source/FINAL_REPORT.md').read_text();matrix=(B/'source/closure_matrix.md').read_text();ledger=(B/'source/N4_VERIFY_REPORT.md').read_text()
 RR=P.rows(report,8,'| # | framework | candidate |');MM=P.rows(matrix,11)
 ck('all108_report_and_matrix_numbers',set(RR)==set(MM)==set(range(1,109)))
 ck('report106_physical_rows',len({r['line'] for r in RR.values()})==106)
 blocks=re.split(r'(?m)(?=^## )',ledger);cites={}
 for block in blocks:
  head=block.splitlines()[0] if block.splitlines() else '';ids=re.findall(r'N4-(\d{3})',head)
  if 'V001' in head:ids.append('001')
  if 'V002' in head:ids.append('002')
  bare=re.match(r'^## (333|334|335)\.',head)
  if bare:ids.append(bare.group(1))
  for id in ids:cites.setdefault(int(id),[]).append(head)
 def candidate(x):
  x=x.split('(',1)[0];x=re.sub(r'(?<![A-Za-z0-9-])(d2|Mpen2|b6)(?![A-Za-z0-9-])',lambda m:'C1-A2-'+m.group(1),x)
  return set(re.findall(r'C1-N1-\d{3}|C1-BASE-S131|C1-A2-(?:d2|Mpen2|b6)',x))
 trace=[]
 for n,r in RR.items():
  m=MM[n];a,b=candidate(r['cells'][2]),candidate(m['cells'][2]);same=b<=a if n in [12,13,14] else a==b
  ck(f'row{n}_candidate',same);ck(f'row{n}_status',P.lab(r['cells'][-1])==P.lab(m['cells'][-1]))
  ids=sorted({int(x) for x in re.findall(r'N4-(\d{3})',r['text']+' '+m['text'])});ck(f'row{n}_ledger',all(i in cites for i in ids))
  trace.append({'row':n,'report_line':r['line'],'matrix_line':m['line'],'candidate_ids':sorted(a),'status':P.lab(r['cells'][-1]),'N4_ids':ids,'scope':'documentary linkage only'})
 answer='\n'.join(report.splitlines()[:328]);answer_ids=sorted({int(i) for i in re.findall(r'N4-(\d{3})',answer)})
 ck('answer_N4_ids_in_ledger',all(i in cites for i in answer_ids))
 ck('no_pair_proved_or_conditional',all(P.lab(r['cells'][-1]) not in ['PROVED','CONDITIONAL'] for r in RR.values()))
 old=read(R/'research/final_table_trace/verification/distance_v02.json','9db8a391298b84c35edf5940c6cd4d0ac1d855248e0db661242bb752e4b38905')
 ck('accepted387',all(old['checks'].values()) and not old['errors'])
 for rel,h in old['inputs'].items():bind(R/rel,h)
 for edge in old['edges']:
  ck('edge:'+str(len(checks)),edge['pass'] and not edge['decoded_gzip']);bind(R/edge['path'],edge['expected_sha256'])
 ck('direct_edges2023',len(old['edges'])==2023)
 principal=[]
 for r in old['results']:
  n=r['report_row'];text=RR[n]['text']
  # Select the occurrence closest to the accepted principal distance.
  vals=[(m.group(0),Q(m.group(1))) for m in re.finditer(r'>\s*(0\.\d+)',text)]
  candidates=[x for x in vals if Q(r['floor'])/2<x[1]<Q(r['floor'])*2]
  ck(f'principal{n}_display_present',bool(candidates))
  # Explanatory parentheses may quote an explicitly refuted old display;
  # choose the first present principal lower, before those parentheses.
  literal,value=candidates[0];ck(f'principal{n}_strict_floor',value<=Q(r['floor'])<Q(r['root_interval'][0]))
  principal.append({'candidate':r['candidate'],'row':n,'line':RR[n]['line'],'literal':literal,'display_exact':str(value),'accepted_floor':r['floor'],'root_lower':r['root_interval'][0]})
 ratios=[]
 for i,r in enumerate(old['selected_ratios']):
  ck(f'ratio{i}_same_literal',r['literal'] in RR[r['report_row']]['text']);ck(f'ratio{i}_strict',Q(r['printed_factor'])<Q(r['exact_lower_ratio']))
  ratios.append(r)
 cover=read(R/'research/h18_coverage_peer/verification/result_v02.json')
 ck('accepted390',cover['verdict'].startswith('CONFIRMED') and all(cover['checks'].values()))
 for rel,h in cover['inputs'].items():bind(R/rel,h)
 bind(R/'research/h18_coverage_peer/PROOF.md')
 for r in cover['scalar_families']:ck('scalar:'+r['name'],Q(r['ceiling_squared_exact'])<Q(3793,10**9)**2)
 ck('eight_scalar_tuples',len(cover['scalar_families'])==8)
 tight2=Q(50,651)**2/Q(28248);ck('exact_graded_square',tight2==Q(625,2992882662))
 ck('line163_graded_display_valid',tight2<Q('4.57e-4')**2)
 ck('line988_graded_display_valid',tight2<Q('4.5717e-4')**2)
 ck('looser_rational_does_not_refute_tighter_bound',Q(25,54684)>Q('4.57e-4'))
 ck('scalar3_8e_minus6',Q(3793,10**9)<Q('3.8e-6'))
 ck('line163_literal','||h||_2 < 4.57e-4' in report.splitlines()[162])
 upper=read(R/'research/candidate016_reviewed_upper/verification/result.json','d50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0')
 ck('accepted410',all(upper['checks'].values()))
 for rel,h in upper['inputs'].items():bind(R/rel,h)
 ck('E2_strict_gap',Q('608.392385921614')-Q('606.820219')>Q('1.572166921613'))
 ck('017_order_label_claimed','CLAIMS E_2(017) < E_2(007)' in report)
 gate_lines=[i for i,l in enumerate(report.splitlines(),1) if 'R1-050' in l and (i<145 or i==1117)]
 ck('three_selected_gate_attributions',gate_lines==[48,139,1117])
 findings=[{'claim':'the frozen report contains105 physical comparison rows','verdict':'REFUTED coordinator16:28 count;106 physical rows cover108 numbered entries, only12-14 combined','report_repair_required':False},{'claim':'line163 needs4.572e-4 because25/54684 exceeds4.57e-4','verdict':'REFUTED preliminary audit inference; frozen line163 CONFIRMED by sharper accepted bound','line':163,'exact_sharper_ceiling_square':str(tight2),'actual_source':'research/h18_coverage_peer/PROOF.md equations7 and8','report_repair_required':False},
 {'claim':'N4 promotes the finite016 upper only after R1-050','verdict':'REFUTED as the current numerical acceptance gate; frozen text predates410','lines':gate_lines,'repair':'N4-408 accepts the R1-049 general upper review; N4-410 discharges the numerical gate using the accepted finite source-specific tail. R1-050 is an additional general tail review.','mathematical_upper_changed':False},
 {'claim':'all108 comparison rows match matrix candidate IDs and primary status; explicit N4 IDs resolve','verdict':'CONFIRMED documentary scope only'},
 {'claim':'nineteen selected principal floors and twenty-two ratio displays are supported','verdict':'CONFIRMED by refreshed exact comparisons and2023 bound source edges'},
 {'claim':'017 complete narrow H/E2 and017<007 independently accepted','verdict':'OPEN; frozen CLAIMED label correct'}]
 for rel,h in inputs.items():assert sha(R/rel)==h,rel
 out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'physical_report_rows':106,'numbered_rows':len(trace),'answer_N4_ids':answer_ids,'trace':trace,'principal_displays':principal,'selected_ratios':ratios,'rebound_direct_edges':len(old['edges']),'findings':findings,'integration_repeated':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED stated finite numerical and documentary checks; current review-gate attribution corrected; no new whole-plane certificate'}
 path=B/'verification/result.json'
 with path.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({'utc':out['utc'],'check_count':out['check_count'],'input_count':len(inputs),'sha256':sha(path),'elapsed_seconds':out['elapsed_seconds'],'findings':findings},indent=2))
if __name__=='__main__':main()
