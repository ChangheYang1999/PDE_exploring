"""Apply the established uniform graded and sharp point bounds."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sys
import time
from flint import arb, ctx, fmpq as Q

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/candidate_audits'
def H(p):return sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
def run(name):
    ctx.prec=1024;start=time.monotonic()
    source=BASE/f'verification/{name}_point.json'
    target=BASE/f'verification/{name}_uniform_point.json'
    assert not target.exists()
    data=json.loads(source.read_text());f={k:arb(v) for k,v in data['fields'].items()}
    canonical=BASE/f'data/{name}/canonical.json';c=Q(json.loads(canonical.read_text())['cl'])
    assert data['canonical_sha256']==H(canonical)
    F,V,D=abs(f['residual']),f['velocity_norm'],f['gradient_norm']
    b0=ar(Q(50,651))/(arb(28248)*4*arb.pi()).sqrt()
    b1=ar(Q(25,217))/(8*arb.pi()).sqrt()
    upper=b1*V+b0*(1+D)+b0*b1
    theta=(D-f['rho_y'])/2
    rows=[]
    for framework,s,r in [('FW-T-T4L2-sharp-v1',Q(1,7744),Q(147,200000)),
                          ('FW-T-T4L2-sharpw-v1',Q(1,5184),Q(1351,1000000))]:
        C0=1/(4*arb.pi()*ar(1+s)).sqrt()
        C1=1/(8*arb.pi()*ar(s*(1+s))).sqrt()
        bound=ar(r)*(C1*V+C0*(1+D))+ar(r*r)*C0*C1
        rows.append({'framework':framework,'s':str(s),'radius':str(r),
                     'point_upper':bound.str(90),'gap':(F-bound).str(90),
                     'strict_positive_gap':bool(F>bound)})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
         'candidate':name,'point':data['point'],'point_record_sha256':H(source),
         'canonical_sha256':H(canonical),'code_sha256':H(Path(__file__)),
         'proof_sha256':H(ROOT/'research/point_witness/PROOF_UNIFORM_GRADED.md'),
         'precision_bits':ctx.prec,'uniform_graded_upper':upper.str(90),
         'uniform_graded_gap':(F-upper).str(90),'uniform_graded_excluded':bool(F>upper),
         'sharp_boxes':rows,'point_theta':theta.str(90),
         'point_theta_minus_c_minus_one':(theta-ar(c-1)).str(90),
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Fixed-c point obstructions under the original graded top-margin constants and the two stated sharp balls. Negative gaps are inconclusive.'}
    target.write_text(json.dumps(out,indent=2)+'\n')
    print('uniform graded gap',out['uniform_graded_gap'])
    for row in rows:print(row['framework'],row['gap'])
if __name__=='__main__':run(sys.argv[1])
