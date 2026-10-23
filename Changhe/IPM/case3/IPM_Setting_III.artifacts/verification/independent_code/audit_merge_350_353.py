"""Freeze and record the verifier's line-by-line audit of supplied proof text."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb,factorial
import hashlib,json
root=Path(__file__).resolve().parent.parent
out=root/'evidence/lead_merge_audit'
source=root.parent/'analysis/questions'
files={}
for name in ['MAIN_350_353.frozen.md','APPENDIX_350_353.frozen.md']:
    data=(source/name).read_bytes()
    (out/name).write_bytes(data)
    files[name]=hashlib.sha256(data).hexdigest()
assert files['APPENDIX_350_353.frozen.md'].startswith('92591fd004db8a3a')
checks=[]
def ck(name,a,b):
    assert a==b,(name,a,b)
    checks.append(dict(name=name,value=str(a)))
ck('Gaussian base denominator',2*4097*9,73746)
ck('Gaussian scale constant',16*73746,1179936)
ck('strict cap denominator',4*73746,294984)
ck('remote strain constant',1458*974+F(1,2)*(29160*F(4,3)+729*4862),3211731)
ck('rectangle residual norm lower constant',F(1,25)*F(4,5)*F(8,125),F(32,15625))
ck('rectangle exponential rational bound',F(11,4)**3*F(16,15)**2,F(5324,225))
assert F(81,169)*F(32,62500)>F(1,10000)
checks.append(dict(name='uniform fixed m3 ratio >1/100 using pi<4',value='true'))
for k in range(1,11):
    n=2*k+1
    ck('coefficient product ratio K='+str(k),F(factorial(2*k),factorial(2*k+1)),F(1,2*k+1))
    def rising(a,m):
        v=F(1)
        for i in range(m):v*=a+i
        return v
    for j in range(k+1):
        ck('positive law binomial coefficient '+str((k,j)),
           comb(2*k+1,2*j)*rising(F(1,2),j)*rising(F(3,2),k-j)/rising(F(3,2),k),comb(k,j))
    for chi in [F(-7,3),F(0),F(1,3),F(2)]:
        ck('K-th difference '+str((k,chi)),sum((-1)**j*comb(k,j)*rising(chi+j,k-1)for j in range(k+1)),0)
refs=['capped_gaussian_nonprofiles','capped_local_and_ball_examples','capped_weighted_limits',
      'one_sided_jet_thresholds','local_flat_sign_and_trajectories','angular_monotone_exclusion',
      'sign_and_local_uniqueness','conditional_integer_fredholm']
proofs={}
for name in refs:
    p=root/'research'/name/'PROOF.md'
    proofs[str(p.relative_to(root))]=hashlib.sha256(p.read_bytes()).hexdigest()
rows=[
('3.50(a)','CONFIRMED','Independent Fourier strain normalization, global deficit constants, gradient contraction, class/gauge and negative transport at (0,1). Monotonicity is correctly identified as failing.'),
('3.50(b)','CONFIRMED','Positive binomial mixture of scale copies preserves the full global cap; flatness and the radial transport contradiction are complete.'),
('3.50(c)','CONFIRMED','Both Cartesian PDEs and the strain factorization hold. The stated disc suffices. Linear density growth explicitly excludes the primary class.'),
('3.50(d)','CONFIRMED','Smooth logarithmic radial base, remote compact Poisson pair, explicit constants and support separation give the global cap. Dilation preserves a. Exact transport holds only on the prescribed ball; the use of flat exclusion outside is scoped correctly.'),
('3.50(e), fixed gap','CONFIRMED','Rectangle signs and lower mass, upper defect norm, and rational constants give the asserted lower bound for every B>=9.'),
('3.50(e), Gaussian limit','CONFIRMED','The nonnegative Fourier diagonal multiplier gives velocity convergence; uniform cubic and linear endpoint bounds allow dominated convergence exactly on 2<m<4. The positive limit and R3 bound follow.'),
('3.50(e), remote limits and m->2','CONFIRMED','For each fixed m>2 the affine core removes the inner singularity. Fixed b and positive b proportional to L within the cap constraint both have positive limits. The m->2 statement changes the norm; the Gaussian tail is correctly treated as Schwartz.'),
('3.51(a)','CONFIRMED','The inner signed mass is positive and concentrates exponentially relative to the exterior. Both signs of a are handled. The lower moment bound grows linearly in m, while the upper stays bounded. An exactly affine core has positive radial flow.'),
('3.51(b)','CONFIRMED','The smooth quotient equation holds across the axis. Backward convergence plus local source expansion makes G integrable in time. The dynamical hypothesis is explicitly extra.'),
('3.51(c)','CONFIRMED','All leading coefficients, recurrence dimension, endpoint product and positive-law contradiction match the independent proof. The A=n law degenerates to S=1 correctly. The quintic classification and ell<=3/5 consequences are complete.'),
('3.51(d)','CONFIRMED','The explicit negative quintic jet and its stream satisfy the leading Poisson/transport equations. Extension to all a<=-76 is a jet claim, not a profile claim.'),
('3.52','CONFIRMED','Primary-class restriction now supplies far-field symbol bounds. E, P0, graph domain and augmented L are identical, thresholds and weights are compatible, and kernel dimension1 plus Fredholm index1 yields surjectivity. Equal-weight uniqueness uses the previously repaired exterior upgrade.'),
('3.53','CONFIRMED','Circular integration by parts keeps the required order. A3.43 supplies the uniform derivative bounds through A3.23. Positivity forces 0<a<=4D; the y-axis angular coefficient sign and exact recurrence then contradict a nonzero first Taylor term. Flatness is excluded only with exact transport and the one-sided sign.')]
now=datetime.now(timezone.utc).isoformat()
record=dict(utc=now,verdict='CONFIRMED',frozen_sha256=files,items=[dict(item=a,verdict=b,method_and_result=c)for a,b,c in rows],
            prior_independent_proof_sha256=proofs,supplemental_exact_checks=checks,count=len(checks),
            scope='Audit of complete supplied statements and proof text, independently compared with prior verifier proofs. No new numerical candidate test; no primary endpoint.')
(out/'AUDIT_SECTIONS_350_353.json').write_text(json.dumps(record,indent=2)+'\n')
text=['# Audit of merged Sections 3.50 through 3.53','',now,'',
      'Verdict: CONFIRMED for every mathematical item in the supplied frozen statements and appendix. No local mathematical repair is required. The results retain their stated subclass, nonprofile or conditional scope.','',
      'The appendix SHA256 is '+files['APPENDIX_350_353.frozen.md']+'. The statement SHA256 is '+files['MAIN_350_353.frozen.md']+'. Full proof dependencies and hashes are in the companion JSON.','',
      'Method: full line-by-line reading, independent rederivation of signs and endpoints, comparison against the verifier proofs already recorded, and '+str(len(checks))+' additional exact rational/product checks. This does not count the main lane symbolic checks as independent verifier evidence.','']
for item,verdict,reason in rows:text += [f'**{item}: {verdict}.** {reason}','']
text += ['No implication from these restricted conclusions to the complete primary NO endpoint is justified. The numerical YES conditions are also unmet.','']
(out/'AUDIT_SECTIONS_350_353.md').write_text('\n'.join(text))
print(json.dumps(dict(utc=now,verdict='CONFIRMED',count=len(checks),frozen=files)))
