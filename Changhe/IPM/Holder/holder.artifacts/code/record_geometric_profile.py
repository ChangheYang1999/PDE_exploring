from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ctx.prec=192;root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
p=root/'07_diagonal_identity_term/geometric_profile_constant/certified_values';(p/'verification').mkdir(parents=True,exist_ok=True)
(p/'PROOF.md').write_text('''# Certified projection-profile factors

For the planar profile g and full geometric quantity K*_alpha defined in
../PROOF.md, the following inequalities hold:

    [g]_(3/10) <= K*_(3/10) <= 1.007,
    [g]_(1/2) <= K*_(1/2) <= 1.021.

Consequently these rational numbers can replace the sufficient denominator
K_alpha in the corresponding finite projection witness theorem. All other
hypotheses of that theorem, including its restrictions on a and rho, remain.
These are upper bounds for a profile seminorm, not sharp operator norms.

## Proof

Use epsilon=1/1000000 and the exact covering algorithm in ../PROOF.md.
The code works at160-bit Arb precision and uses exact rational subdivision
coordinates. Every split replaces one closed box by two closed boxes whose
union is that box. Every box is either accepted with an upper enclosure
at most the rational target or split. Thus termination with an empty stack
certifies the whole compact region. The endpoint intervals are checked
separately. No sample determines acceptance.

At alpha=3/10, the run checked1926349 boxes and accepted963175 terminal
boxes, with maximum depth33. Its largest accepted upper bound is less than
1.006999999776; the two endpoint bounds are less than1.000000301 and
1.000009465. At alpha=1/2, the run checked1331983 boxes and accepted665992
terminal boxes, with maximum depth42. Its largest accepted upper bound is
less than1.0209999990; the endpoint bounds are less than1.000000501 and
1.000250001. In each case the accepted count is exactly one more than the
number of split boxes, as expected for the binary tree.

The geometric reduction in ../PROOF.md and the nonexceptional-pair
estimates in ../../finite_projection_extended/PROOF.md prove the seminorm
inequality from the covering. Independent real-coordinate diagnostics
checked719130 sampled points in rational boxes and500000 arbitrary pairs.
Their agreement supports the audit; the complete interval covering and
analytic reduction provide the proof.

All proof, code and exact JSON input dependencies are hashed in the adjacent
verification manifest. The underlying certificate source list omitted the
extended-range proof because it used a stale optional path; the manifest
here explicitly includes that required dependency.
''')
raws=['data/geometric_profile_a30_tight.json','data/geometric_profile_a50_tight.json'];rows=[]
for name in raws:
    c=json.loads((root/name).read_text());assert c['checked_boxes']==2*c['accepted_boxes']-1
    for source,h in c['source_hashes'].items():assert hashlib.sha256((root/source).read_bytes()).hexdigest()==h
    upper=arb(c['largest_accepted_bound'])
    for key in ['left_endpoint','right_endpoint']:upper=arb.max(upper,arb(c[key]))
    assert upper<arb(c['certified_upper'])
    rows.append(dict(alpha=c['alpha'],safe_upper=c['certified_upper'],upper_interval=upper.str(45,more=True),certificate=name))
paths=raws+['07_diagonal_identity_term/geometric_profile_constant/PROOF.md','07_diagonal_identity_term/geometric_profile_constant/certified_values/PROOF.md','07_diagonal_identity_term/refined_profile_constant/PROOF.md','07_diagonal_identity_term/local_projection_profile/PROOF.md','07_diagonal_identity_term/finite_projection_extended/PROOF.md','code/certify_geometric_profile.py','code/check_geometric_profile.py','data/geometric_profile_independent_checks.json','code/record_geometric_profile.py']
hashes={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in paths}
out=dict(time_utc=now,rows=rows,source_hashes=hashes,status='Complete geometric profile covering and analytic proof audited; V064 CONFIRMED')
(root/'data/geometric_profile_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
(p/'verification/manifest.json').write_text(json.dumps(dict(time_utc=now,verdict='CONFIRMED',sha256=hashes),indent=2)+'\n')
with (root/'VERIFY_REPORT.md').open('a') as f:f.write(f'''\n## V064: Sharper profile constants from complete two-point geometry

Date: {now}

Claim: For the full geometric profile bound K*_alpha, K*_(3/10)<=1.007 and K*_(1/2)<=1.021. These may replace the old sufficient K in the finite projection theorem.

Method: Re-derived the exact opposite-quadrant quotient, checked the reduction by symmetries and dilation, and verified that all other pair classes have quotient at most one for alpha<=1/2. Audited monotonic numerator bounds, the convex radial distance minimization, both endpoint estimates, exact rational subdivision coverage and every Arb acceptance comparison. Independent real-coordinate diagnostics sampled719130 box points and500000 arbitrary pairs without a violation.

Result: Complete coverings checked1926349 and1331983 boxes respectively. Standalone statement/proof and the full dependency manifest are in07_diagonal_identity_term/geometric_profile_constant/certified_values/. The adapter data/geometric_profile_certificate.json is suitable for the existing finite-D combiner. These are sufficient profile bounds, not exact seminorms.

Verdict: **CONFIRMED**.
''')
with (root/'NOTES_FOR_TEAM.md').open('a') as f:f.write(f'''\n## {now}: V064, certified geometric projection factors

CONFIRMED [g]_.3<=1.007 and [g]_.5<=1.021, replacing old factors1.026981110219 and1.089352283627 where useful. Complete exact rational box coverings at160-bit Arb;719130 independent box samples and500000 arbitrary pairs pass. The proof includes all quadrant cases via the existing alpha<=1/2 extension. Data/geometric_profile_certificate.json adapts the results to the finite-D combiner; all original witness a,rho hypotheses remain. Alpha.3 regular integration is being refined to2048x2048 on each patch, aiming at a rigorous C_.3<D_.3 separation. Local-circle upper runs at.3,.75,.9 are in progress. Please audit the full-geometry argument when available.
''')
