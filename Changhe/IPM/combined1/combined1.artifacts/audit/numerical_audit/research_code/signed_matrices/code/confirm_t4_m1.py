"""Validate the independent first-matrix certificate and its exact partition."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
PEER=BASE/'peer_review'
def sha(p):return sha256(p.read_bytes()).hexdigest()
def box(path):
    a,b,c,d=Q(0),Q(1),Q(-1),Q(1)
    for v in path:
        if v=='t':b=(a+b)/2
        elif v=='T':a=(a+b)/2
        elif v=='z':d=(c+d)/2
        elif v=='Z':c=(c+d)/2
        else:raise ValueError(v)
    return a,b,c,d
start=time.monotonic();ctx.prec=512
cover=json.loads((PEER/'T4_M1_cover.json').read_text())
summary=json.loads((PEER/'T4_M1_final_check.json').read_text())
recon=json.loads((PEER/'T4_M1_reconstruction.json').read_text())
checks={
    'proof':cover['proof_sha256']==sha(PEER/'T4_M1_PROOF.md'),
    'code':cover['code_sha256']==sha(PEER/'T4_M1_certify.py'),
    'helper':cover['helper_sha256']==sha(PEER/'T4_global_certify.py'),
    'reconstruction':cover['reconstruction_sha256']==sha(PEER/'T4_M1_reconstruction.json'),
    'source_cover':cover['source_cover_sha256']==sha(BASE/'verification/d2_M1_relative_768.json'),
    'summary_cover':summary['cover_sha256']==sha(PEER/'T4_M1_cover.json'),
    'summary_code':summary['code_sha256']==sha(PEER/'T4_M1_final_check.py'),
    'reconstruction_code':recon['code_sha256']==sha(PEER/'T4_M1_certify.py'),
    'gradient':recon['density_gradient_sha256']==sha(PEER/'T4_global_gradient.json'),
    'N4_polynomials':recon['N4_polynomials_sha256']==sha(ROOT/'research/global_matrices/data/independent_d2_polynomials.json.gz'),
    'canonical':recon['canonical_sha256']==sha(ROOT/'research/refit_audit/data/d2_canonical.json'),
    'all_matrix_coefficients_match':recon['all_matrix_coefficients_match'],
}
assert all(checks.values()),checks
assert not cover['pending'] and cover['all_pass'] and cover['complete_partition']
rects=[box(row['path']) for row in cover['accepted']]
assert len(set(rects))==len(rects)==summary['accepted']
keys=['diag1_lower','diag2_lower','det_lower']
assert all(row['pass'] and all(arb(row[k])>0 for k in keys) for row in cover['accepted'])
area=sum(((b-a)*(d-c) for a,b,c,d in rects),Q(0));assert area==2
pairs=0
for i,(a,b,c,d) in enumerate(rects):
    for aa,bb,cc,dd in rects[i+1:]:
        assert min(b,bb)<=max(a,aa) or min(d,dd)<=max(c,cc)
        pairs+=1
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'target':'N4-056: d2 M1 >= (9/10) I globally','peer_audit':'T4-061',
     'hash_and_identity_checks':checks,'cells':len(rects),'area_exact':str(area),
     'disjoint_interior_pairs_checked':pairs,'all_diagonal_and_determinant_margins_positive':True,
     'positive_minimum_bounds':summary['positive_minimum_bounds'],
     'peer_cover_sha256':sha(PEER/'T4_M1_cover.json'),'peer_summary_sha256':sha(PEER/'T4_M1_final_check.json'),
     'review_sha256':sha(BASE/'REVIEW_T4_M1.md'),'code_sha256':sha(Path(__file__)),
     'elapsed_seconds':time.monotonic()-start}
dest=BASE/'verification/T4_M1_confirmation.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
