from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
R=Path(__file__).resolve().parents[3];B=R/'research/background_sobolev';P=B/'peer_review/T4_009'
def H(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ar(q): return arb(q.numerator)/q.denominator
start=time.monotonic();name='C1-N1-009-d2w-j7-x3balk'
source=R/f'research/candidate_audits/data/{name}/canonical.json'
target=B/f'verification/{name}.json';out=B/'verification/T4_009_confirmation.json'
assert not out.exists()
peer=json.loads((P/'result.json').read_text());own=json.loads(target.read_text())
checks={'candidate':peer['candidate']==name,
        'canonical':peer['source_sha256']==H(source),
        'target':peer['N4_target_sha256']==H(target),
        'proof':peer['proof_sha256']==H(P/'PROOF.md'),
        'code':peer['code_sha256']==H(P/'reproduce_new_candidate.py')}
assert all(checks.values()),checks
energies={};rows=[]
for k in ['D2rho','D3rho','D_rho_x','D_rho_y']:
    q=Q(own['norms'][k]['unweighted_rational_sum']);energies[k]=q
    p=peer['norms'][k];n=(arb.pi()*ar(q)/2).sqrt()
    eq=q==Q(p['rational_energy_over_pi_half'])
    nc={'exact_energy_equality':eq,'own_norm_overlap':n.overlaps(arb(own['norms'][k]['norm_upper_ball'])),
        'peer_norm_overlap':n.overlaps(arb(p['norm']))}
    assert all(nc.values()),(k,nc)
    rows.append({'name':k,'checks':nc,'norm':n.str(80)})
assert energies['D_rho_x']+energies['D_rho_y']==energies['D2rho']
kappa=(((arb(2).log()-arb(1)/2)*ar(energies['D_rho_x'])+(3*arb(2).log()-2)*ar(energies['D_rho_y']))/32).sqrt()
assert kappa.overlaps(arb(peer['gradient_HS_norm'])) and kappa.overlaps(arb(own['gradient_identity_conditional_HS_upper']))
inputs=[source,target,P/'result.json',P/'PROOF.md',P/'reproduce_new_candidate.py',B/'REVIEW_T4_009.md',Path(__file__)]
result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'precision_bits':ctx.prec,
        'source_checks':checks,'rows':rows,'column_energy_sum':True,'HS_overlaps_both':True,'kappa':kappa.str(80),
        'peer_elapsed_seconds':peer['elapsed_seconds'],'elapsed_seconds':time.monotonic()-start,
        'inputs':{str(p.relative_to(R)):H(p) for p in inputs},'status':'CONFIRMED seminorms and kappa; no global theta or existence claim'}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
