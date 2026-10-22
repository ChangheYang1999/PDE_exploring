"""Actual three-annulus lower-bound application, separate from full1558 coverage."""
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q
from datetime import datetime,timezone
import sys,json,hashlib,subprocess,argparse,os,ast
R=Path(__file__).resolve().parents[3];D=R/'research/scaling_selected_application';E=D/'evidence';S=R/'research/scaling_norm_lower_bound'
sys.path.insert(0,str(S/'code'));import common as C
P=C.u
DEN='research/derivative_norm_regional_composition/evidence/both/verdict.json'
FIXED=['PROOF.md','evidence/proof_first.json','code/application.py']
QUESTION='Independently audit this actual three-WHOLE-annulus scaling norm lower bound and optional necessary inverse-constant quotient. Reconstruct both spline methods, rational monomial versus Legendre square integrals, monotone weight and global-lower-bound direction, directed roots and exact scalar reduction. Three selected full annuli suffice by nonnegativity; no full1558-span computation is claimed. The original smoke gate stays preparation only. This separate application has complete three-span replay and its own audit. Verify same canonical trial, norm, LK=epsilon-D epsilon, and graph-limit K_delta with J=Sigma=0 rather than false J(K)=0. Check all mandatory source/provenance addenda and actual source hashes, times, model reviews. No inverse existence, error to X3 or PDE endpoint is claimed. Reject unproved claims. End exactly VERDICT: CONFIRM_THREE_ANNULUS_SCALING_LOWER_BOUND_AND_NECESSARY_QUOTIENT or VERDICT: REJECT.'

def inherited(p,z):
 for n,h in z.get('files',{}).items():P.pin(p,n,h)
 for n,h in z.get('own_postreview',{}).get('supplemental_files',{}).items():P.pin(p,n,h)

def baseline():
 p=C.source();ext=P.load(S/'evidence/source_external_rehash.json')
 for n,h in ext['files'].items():P.pin(p,n,h)
 P.pin(p,S/'evidence/source_external_rehash.json')
 assert C.sha(S/'evidence/source_freeze.json')=='88ffd4f4ffc61268ac13e8e4eecd2d756d2d88d21574d8c5e265da1afc6cd4c9'
 assert C.selected('smoke')==[7,620,1564]
 pf=P.load(E/'proof_first.json');assert pf['proof_sha256']==P.sha(D/'PROOF.md') and pf['code_files']==[]
 for n in FIXED:P.pin(p,D/n)
 return p

def check():
 p=baseline();freeze=P.load(E/'source_freeze.json');assert freeze['status']=='FROZEN_SELECTED_APPLICATION_BEFORE_NUMERICAL_RUN' and freeze['files']==baseline()
 P.pin(p,E/'source_freeze.json');prep=P.load(S/'evidence/preparation.json');assert prep['status']=='ACCEPTED_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY' and prep['spans']==[7,620,1564] and prep['cells']==3 and prep['complete_middle'] is False
 inherited(p,prep);P.pin(p,S/'evidence/preparation.json')
 s=P.load(S/'evidence/smoke_summary.json');a=P.load(S/'evidence/smoke_audit.json');r=P.load(S/'evidence/smoke_replay.json');rows=C.rows('smoke');assert [x['span'] for x in rows]==[7,620,1564] and r['indices']==[7,620,1564]
 assert P.when(freeze['utc'])<P.when(s['start_utc'])<=P.when(s['utc'])<P.when(a['start_utc'])<=P.when(a['utc'])<P.when(r['start_utc'])<=P.when(r['utc'])<P.when(prep['utc'])
 assert s['strict_norm_lower_decimal']==prep['strict_norm_lower_decimal'] and s['rows_sha256']==a['rows_sha256']==r['rows_sha256']==P.sha(S/'evidence/smoke_rows.jsonl')
 assert a['status']=='PASS_COMPLETE_SCALING_NORM_ROWS_WEIGHTS_SUMS_AND_INTEGER_LOWER_ROUNDING' and r['status']=='PASS_EXACT_DUAL_SPLINE_AND_WEIGHT_REPLAY_FIXED_AND_ACTUAL_MAXIMA'
 assert s['density_coefficient_equalities']==r['density_coefficient_equalities']==6264 and s['exact_square_integral_equalities']==3
 intervals=[(Q(z['methods']['cox_monomial']['a']),Q(z['methods']['cox_monomial']['b'])) for z in rows]
 assert all(x<y for x,y in intervals) and all(intervals[i][1]<=intervals[i+1][0] for i in range(2))
 q=Q(str(F(s['strict_norm_lower_decimal'])));assert q>0;checks=[]
 for eng in ['iv220','arb512']:
  for side in ['right','left']:
   lo=sum((Q(z['weights'][eng][side]['lower_exact']) for z in reversed(rows)),Q(0));hi=sum((Q(z['weights'][eng][side]['upper_exact']) for z in reversed(rows)),Q(0));rec=s['engines'][eng]
   sl,sh=[Q(rec['endpoint_weighted_sum_squares'][side][k]) for k in ['lower_exact','upper_exact']];rl,rh=[Q(rec['endpoint_weighted_sum_roots'][side][k]) for k in ['lower_exact','upper_exact']]
   assert 0<=sl<=lo<=hi<=sh and 0<=rl<=rh and rl*rl<=sl<=sh<=rh*rh
   if side=='left':assert q<rl and q*q<sl
   checks.append({'engine':eng,'side':side,'raw_sum_lower':str(lo),'raw_sum_upper':str(hi),'sum_lower':str(sl),'sum_upper':str(sh),'root_lower':str(rl),'root_upper':str(rh),'strict_lower_square_margin':str(sl-q*q) if side=='left' else None})
 for n in ['smoke_rows.jsonl','smoke_summary.json','smoke_audit.json','smoke_replay.json']:P.pin(p,S/'evidence'/n)
 den=P.load(R/DEN);assert den['status']=='CONFIRMED_COMPLETE_CANONICAL_REGIONAL_DERIVATIVE_COMPOSITION' and den['mode']=='both';inherited(p,den);P.pin(p,DEN)
 b=F(den['published_whole_plane_norm_ceilings'][1]);assert b>0
 ratio=F(str(q))/b;scale=10**12;n=ratio.numerator*scale//ratio.denominator
 if F(n,scale)==ratio:n-=1
 down=F(n,scale);assert 0<down<ratio and Q(str(down))*Q(str(b))<q
 for npath in ['research/modal_graph_scaling/evidence/verdict.json','research/modal_repair/evidence/audit_verdict.json','data_exact/modal_v2.json']:assert npath in p
 # This reduction checks saved endpoints; full spline replay is separately retained.
 return p,{'status':'COMPLETE_SELECTED_ANNULI_ARITHMETIC_REQUIRES_ACTUAL_REVIEW','selected_spans':[7,620,1564],'complete_middle':False,'density_coefficient_equalities':6264,'exact_square_integral_equalities':3,'strict_global_K_norm_lower_decimal':s['strict_norm_lower_decimal'],'denominator_norm_upper_decimal':den['published_whole_plane_norm_ceilings'][1],'denominator_source':DEN,'denominator_sha256':P.sha(R/DEN),'strict_necessary_inverse_constant_lower_rational':str(down),'strict_necessary_inverse_constant_lower_decimal':str(n//scale)+'.'+str(n%scale).zfill(12),'checks':checks,'source_freeze_sha256':P.sha(E/'source_freeze.json'),'preparation_sha256':P.sha(S/'evidence/preparation.json'),'scope':'Three whole annuli give a global lower bound by nonnegativity. Right sums bound selected union only. Necessary inverse-constant quotient on stated graph domain only; no existence, full1558 coverage, X3 distance or endpoint.'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['freeze','extract','review','finalize']);a=ap.parse_args()
 if a.stage=='freeze':
  assert not (S/'evidence/smoke_rows.jsonl').exists();ast.parse(Path(__file__).read_text());p=baseline();P.write(E/'source_freeze.json',{'utc':P.now(),'status':'FROZEN_SELECTED_APPLICATION_BEFORE_NUMERICAL_RUN','files':p});print('FROZEN',len(p));return
 if a.stage=='review':
  req=P.load(E/'review_request.json');assert not (P.REV/(req['tag']+'_request.txt')).exists();cmd=[sys.executable,'-B',str(P.REV/'focused_review.py'),'--tag',req['tag'],'--question',req['question'],'--max-tokens','16000']
  for n in req['files']:cmd+=['--file',n]
  raise SystemExit(subprocess.run(cmd,cwd=R,timeout=555).returncode)
 p,x=check()
 if a.stage=='extract':
  P.write(E/'checks.json',{'utc':P.now(),**x,'files':p});fs=[str((D/n).relative_to(R)) for n in FIXED]+[str((E/'checks.json').relative_to(R))]+[str((S/n).relative_to(R)) for n in ['PROOF.md','THEOREM_ADJUDICATION.md','WORKFLOW_ADJUDICATION.md','SOURCE_PROVENANCE_CLARIFICATION.md','PREFLIGHT_ADJUDICATION.md','code/cox_monomial.py','code/deboor_legendre.py','code/weights.py','code/audit.py','code/replay.py','code/gate.py','code/common.py','evidence/smoke_extract.json']]+['research/modal_graph_scaling/PROOF.md','research/modal_graph_scaling/ADDENDUM.md','research/modal_graph_scaling/REVIEW_RESOLUTIONS.md','research/modal_graph_scaling/FINAL_ADJUDICATION.md','research/derivative_norm_regional_composition/PROOF.md','research/derivative_norm_regional_composition/evidence/both/POSTREVIEW_ADJUDICATION.md'];P.write(E/'review_request.json',{'utc':P.now(),'tag':'scaling_three_annulus_actual','files':fs,'question':QUESTION});print(P.now(),x['strict_global_K_norm_lower_decimal'],x['strict_necessary_inverse_constant_lower_decimal']);return
 old=P.load(E/'checks.json');assert {k:v for k,v in old.items() if k not in ['utc','files']}==x and old['files']==p
 req=P.load(E/'review_request.json');assert req['question']==QUESTION;rev=P.auth(p,req['tag'],'CONFIRM_THREE_ANNULUS_SCALING_LOWER_BOUND_AND_NECESSARY_QUOTIENT',req['files'],req['question']);assert P.when(old['utc'])<P.when(rev['start_utc'])
 po=P.load(E/'postreview.json');md=D/'POSTREVIEW_ADJUDICATION.md';assert po['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and po['request_id']==rev['request_id'] and po['input_sha256']==rev['input_sha256'] and po['response_sha256']==P.sha(P.REV/(req['tag']+'_response.json')) and po['adjudication_sha256']==P.sha(md) and po['all_substantive_objections_resolved'] is True
 assert P.when(rev['end_utc'])<P.when(po['utc'])<P.when(P.now()) and rev['request_id'] in md.read_text() and po['response_sha256'] in md.read_text()
 for n,h in po['supplemental_files'].items():P.pin(p,n,h)
 for n in ['checks.json','review_request.json','postreview.json']:P.pin(p,E/n)
 P.pin(p,md);P.rehash(p);P.write(E/'verdict.json',{'utc':P.now(),'status':'CONFIRMED_THREE_ANNULUS_SCALING_LOWER_BOUND_AND_NECESSARY_QUOTIENT','result':x,'actual_review':rev,'own_postreview':po,'files':dict(sorted(p.items()))});print(P.now(),'CONFIRMED')
if __name__=='__main__':main()
