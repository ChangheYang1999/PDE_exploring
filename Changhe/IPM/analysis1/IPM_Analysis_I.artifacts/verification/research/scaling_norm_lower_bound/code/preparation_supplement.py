"""Supplemental acceptance after the preserved original preparation rejection."""
from pathlib import Path
import sys,argparse
D=Path(__file__).resolve().parents[1];sys.path.insert(0,str(D/'code'));import common as C,gate as G
P=C.u;E=D/'evidence';R=C.ROOT;TAG='scaling_lower_preparation_provenance_followup'
EXPECTED='CONFIRM_THREE_SCALING_NORM_PREPARATION_WITH_SUPPLIED_PROVENANCE'
def check():
 p=C.source();pp=C.parents();assert len(pp)==78 and len(p)==112 and all(p[n]==h for n,h in pp.items())
 freeze=P.load(E/'source_freeze.json');diag=P.load(E/'input_selfcheck.json')
 assert diag['source_sha256']==P.sha(D/'code/common.py')==freeze['files'][str((D/'code/common.py').relative_to(R))]
 assert diag['parent_pins']==78 and diag['actual_modal_spans_executed']==0
 xp=G.projection('smoke');old=P.load(E/'smoke_extract.json');assert {k:v for k,v in old.items() if k!='utc'}==xp
 rows=C.rows('smoke');assert rows==xp['selected_actual_rows'] and len(rows)==3
 for key in ['audit','replay']:
  n=D/'code'/(key+'.py');assert xp[key]['source_sha256']==P.sha(n)==freeze['files'][str(n.relative_to(R))]
 for n,h in P.load(E/'source_external_rehash.json')['files'].items():P.pin(p,n,h)
 fs=P.load(D/'review_files.json')['preparation'];rv=P.auth(p,'scaling_lower_preparation','REJECT',fs,(D/'preparation_question.txt').read_text())
 for n in ['smoke_rows.jsonl','smoke_summary.json','smoke_audit.json','smoke_replay.json','smoke_extract.json','source_external_rehash.json']:P.pin(p,E/n)
 for n in ['PREPARATION_PROVENANCE_SUPPLEMENT.md','code/preparation_supplement.py']:P.pin(p,D/n)
 return p,xp,rv,{'parent_pins':len(pp),'frozen_source_pins':112,'raw_projected_rows_equal':3,'diagnostic_is_not_a_numerical_premise':True,'original_rejection_preserved':True}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('stage',choices=['check','accept']);a=ap.parse_args();p,xp,oldrv,count=check()
 if a.stage=='check':
  P.write(E/'preparation_supplement_checks.json',{'utc':P.now(),'status':'PASS_PREPARATION_SOURCE_FREEZE_PROVENANCE_AND_ALL_RAW_ROW_PROJECTION_CHECKS','counts':count,'original_review':oldrv,'files':p});print(P.now(),count);return
 sc=P.load(E/'preparation_supplement_checks.json');assert sc['counts']==count and sc['original_review']==oldrv and sc['files']==p
 req=P.load(E/'preparation_supplement_review_request.json');assert req['tag']==TAG
 rv=P.auth(p,TAG,EXPECTED,req['files'],req['question']);assert P.when(sc['utc'])<P.when(rv['start_utc'])
 ad=C.post(p,TAG,rv,'PREFLIGHT_ADJUDICATION')
 for n,h in ad['supplemental_files'].items():P.pin(p,n,h)
 for n in ['preparation_supplement_checks.json','preparation_supplement_review_request.json']:P.pin(p,E/n)
 P.rehash(p);s=xp['summary'];v={'utc':P.now(),'status':'ACCEPTED_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY','cells':3,'complete_middle':False,'spans':[7,620,1564],'strict_norm_lower_decimal':s['strict_norm_lower_decimal'],'norm':P.load(E/'constants.json')['norm'],'canonical_identity_files':P.load(E/'constants.json')['canonical_identity_files'],'engines':s['engines'],'density_coefficient_equalities':6264,'exact_square_integral_equalities':3,'source_freeze_sha256':P.sha(E/'source_freeze.json'),'preserved_rejected_review':oldrv,'actual_review':rv,'own_postreview':ad,'files':dict(sorted(p.items())),'scope':'Exactly three preparation spans; full1558 coverage remains uncomputed. The raw original REJECT is preserved and its missing evidence is supplied to a separately authenticated follow-up. No final selected-annulus consequence, inverse existence or endpoint.'}
 P.write(E/'preparation.json',v);print(v['utc'],v['status'],len(p))
if __name__=='__main__':main()
