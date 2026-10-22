"""Preparation acceptance after preserved missing-packet and marker rejections."""
from pathlib import Path
import sys
D=Path(__file__).resolve().parents[1];sys.path.insert(0,str(D/'code'));import preparation_supplement as S
C=S.C;P=C.u;E=C.E
def main():
 p,xp,oldrv,count=S.check();sc=P.load(E/'preparation_supplement_checks.json')
 assert sc['counts']==count and sc['original_review']==oldrv and sc['files']==p
 fail=P.load(E/'preparation_followup_marker_rejection.json');assert fail['status']=='REJECTED_BY_SINGLE_TERMINAL_MARKER_GATE' and fail['marker_count']==2
 req=P.load(E/'preparation_supplement_v2_review_request.json');assert req['tag']=='scaling_lower_preparation_complete_v2'
 rv=P.auth(p,req['tag'],'CONFIRM_THREE_SCALING_NORM_PREPARATION_WITH_SUPPLIED_PROVENANCE',req['files'],req['question'])
 assert P.when(sc['utc'])<P.when(fail['utc'])<P.when(rv['start_utc'])
 ad=C.post(p,req['tag'],rv,'PREFLIGHT_ADJUDICATION')
 for n,h in ad['supplemental_files'].items():P.pin(p,n,h)
 for n in ['preparation_supplement_checks.json','preparation_supplement_review_request.json','preparation_supplement_v2_review_request.json','preparation_followup_marker_rejection.json']:P.pin(p,E/n)
 P.pin(p,Path(__file__).resolve());P.rehash(p);s=xp['summary']
 v={'utc':P.now(),'status':'ACCEPTED_THREE_SCALING_NORM_PREPARATION_SPANS_ONLY','cells':3,'complete_middle':False,'spans':[7,620,1564],'strict_norm_lower_decimal':s['strict_norm_lower_decimal'],'norm':P.load(E/'constants.json')['norm'],'canonical_identity_files':P.load(E/'constants.json')['canonical_identity_files'],'engines':s['engines'],'density_coefficient_equalities':6264,'exact_square_integral_equalities':3,'source_freeze_sha256':P.sha(E/'source_freeze.json'),'preserved_rejected_review':oldrv,'preserved_marker_rejection':fail,'actual_review':rv,'own_postreview':ad,'files':dict(sorted(p.items())),'scope':'Exactly3 preparation spans. Original missing-packet REJECT and strict-marker follow-up rejection remain preserved. Separate clean actual review plus later own adjudication. No1558-span coverage, final selected-annulus consequence, inverse existence or endpoint.'}
 P.write(E/'preparation.json',v);print(v['utc'],v['status'],len(p))
if __name__=='__main__':main()
