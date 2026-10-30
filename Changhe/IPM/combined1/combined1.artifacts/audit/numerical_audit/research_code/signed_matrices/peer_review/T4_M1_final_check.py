from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
from flint import arb,ctx
import json,time
B=Path(__file__).resolve().parents[1]
start=time.monotonic();ctx.prec=768;p=B/'verification/d2_M1_cover.json';d=json.loads(p.read_text())
assert d['all_pass'] and not d['pending']
def box(path):
    a,b,c,e=Q(0),Q(1),Q(-1),Q(1)
    for letter in path:
        if letter=='t':b=(a+b)/2
        elif letter=='T':a=(a+b)/2
        elif letter=='z':e=(c+e)/2
        elif letter=='Z':c=(c+e)/2
        else:raise ValueError(letter)
    return a,b,c,e
rects=[box(v['path']) for v in d['accepted']]
assert sum(((b-a)*(e-c) for a,b,c,e in rects),Q(0))==2
pairs=0
for i,(a,b,c,e) in enumerate(rects):
    for f,g,h,k in rects[i+1:]:
        assert b<=f or g<=a or e<=h or k<=c
        pairs+=1
keys=['diag1_lower','diag2_lower','det_lower']
mins={key:min(arb(v[key]).lower() for v in d['accepted']) for key in keys}
assert all(v>0 for v in mins.values())
assert all(v['pass'] for v in d['accepted'])
assert d['proof_sha256']==sha256((B/'PROOF.md').read_bytes()).hexdigest()
assert d['code_sha256']==sha256((B/'code/certify.py').read_bytes()).hexdigest()
assert d['reconstruction_sha256']==sha256((B/'verification/reconstruction.json').read_bytes()).hexdigest()
recon=json.loads((B/'verification/reconstruction.json').read_text());assert recon['all_matrix_coefficients_match']
out={'utc':datetime.now(timezone.utc).isoformat(),'cover_sha256':sha256(p.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'accepted':len(rects),'refinements':len(d['refined']),'area_exact':'2','disjoint_pairs_checked':pairs,'positive_minimum_bounds':{k:v.str(60) for k,v in mins.items()},'source_hashes_match':True,'coefficient_reconstruction_matches':True,'cover_elapsed_seconds':d['elapsed_seconds'],'final_check_elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED: M1 >= (9/10)I on the full plane'}
(B/'verification/final_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
