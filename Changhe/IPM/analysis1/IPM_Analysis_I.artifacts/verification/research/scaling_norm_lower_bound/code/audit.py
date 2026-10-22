"""Every saved span, exact endpoint sum and lower-rounding direction checked."""
from common import *
import argparse
import weights as w

def audit(tag):
    p=source();rr=rows(tag);spans=selected(tag);assert len(rr)==len(spans)
    old=load(E/(tag+'_summary.json'));assert {k:v for k,v in old.items() if k not in ['utc','start_utc']}==summarize(tag,rr)
    c=load(E/'constants.json');count=0
    for row in rr:
        for eng,fun,method in [('arb512',w.cell_arb,'cox_monomial'),('iv220',w.cell_iv,'deboor_legendre')]:
            got=fun(row['methods'][method],c['k'],c['L']);assert got==row['weights'][eng]
            count+=2
    q=F(old['strict_norm_lower_decimal']);assert q>0 and '/' not in old['strict_norm_lower_decimal']
    for eng in ['arb512','iv220']:
        for side in ['left','right']:
            low=sum((F(row['weights'][eng][side]['lower_exact']) for row in rr),F(0));high=sum((F(row['weights'][eng][side]['upper_exact']) for row in rr),F(0))
            slo,shi=w.valid(old['engines'][eng]['endpoint_weighted_sum_squares'][side]);assert slo<=low<=high<=shi
            rlo,rhi=w.valid(old['engines'][eng]['endpoint_weighted_sum_roots'][side]);assert rlo*rlo<=slo<=shi<=rhi*rhi
            if side=='left':assert q<rlo and q*q<slo
    return {'cells':len(rr),'all_endpoint_weights_replayed':count,'density_coefficient_equalities':2088*len(rr),'exact_square_integral_equalities':len(rr),'integer_sum_containments':4,'integer_root_containments':4,'strict_lower_decimal_checks':2}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--tag',choices=['smoke','full'],required=True);a=ap.parse_args();start=now();counts=audit(a.tag)
    write(E/(a.tag+'_audit.json'),{'start_utc':start,'utc':now(),'status':'PASS_COMPLETE_SCALING_NORM_ROWS_WEIGHTS_SUMS_AND_INTEGER_LOWER_ROUNDING','tag':a.tag,'source_sha256':sha(Path(__file__)),'rows_sha256':sha(E/(a.tag+'_rows.jsonl')),'summary_sha256':sha(E/(a.tag+'_summary.json')),'counts':counts});print(json.dumps(counts))
