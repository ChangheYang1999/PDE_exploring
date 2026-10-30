"""Combine already independently verified union and signed certificates."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sys
import time
from flint import arb, ctx, fmpq as Q
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/overlap_compression_audit'
NAME = 'C1-N1-008-d2w-j7-x3bal'

def H(p): return sha256(p.read_bytes()).hexdigest()
def ar(q): return arb(q.numerator)/q.denominator

def main():
    start=time.monotonic(); ctx.prec=2048
    union_path=BASE/'verification/candidate008_n8_m6_d32.json'
    signed_path=ROOT/'research/signed_compression_audit/verification/candidate008_n8_m7.json'
    signed_source=ROOT/'research/signed_compression_audit/source/T4_008_n8_m7_ball.json'
    peer_path=BASE/'source/T4_008_n8_m6_d32_signed.json'
    energy_path=ROOT/f'research/background_sobolev/verification/{NAME}.json'
    u,s,ss,p,e=[json.loads(x.read_text()) for x in [union_path,signed_path,signed_source,peer_path,energy_path]]
    assert all(d['candidate']==NAME for d in [u,s,ss,p])
    assert s['inputs'][str(signed_source.relative_to(ROOT))]==H(signed_source)
    assert s['exact_trace_equal'] and s['all_direct_LDL_pivots_positive']
    for path, expected in s['inputs'].items(): assert H(ROOT/path)==expected,path
    for path, expected in u['inputs'].items(): assert H(ROOT/path)==expected,path
    mapping={
        f'parity_hs_angular/verification/{NAME}_n8_m6.json':ROOT/'research/parity_angular_audit/source/T4_008_n8_m6.json',
        f'parity_hs_budget/verification/{NAME}_d32.json':ROOT/'research/parity_budget_audit/source/T4_008_d32.json',
        'nested_compression_union/code/combine.py':BASE/'source/T4_combine.py',
        'nested_compression_union/PROOF.md':BASE/'source/T4_PROOF.md',
        f'signed_compression_budget/verification/{NAME}_n8_m7_ball.json':signed_source,
    }
    for path, expected in p['inputs'].items(): assert H(mapping[path])==expected,path
    union=Q(u['union_energy_exact']);target=Q(ss['target_HS_exact']);q=Q(s['certified_q'])
    assert union==Q(p['union_energy_exact']) and q==Q(p['signed_q'])
    ex=Q(e['norms']['D_rho_x']['unweighted_rational_sum'])
    ey=Q(e['norms']['D_rho_y']['unweighted_rational_sum'])
    full=((arb(2).log()-Q(1,2))*ar(ex)+(3*arb(2).log()-2)*ar(ey))/32
    radicand=full-ar(union+target-q*q);assert radicand>0
    bound=radicand.sqrt();c=Q(4076476460239181,2251799813685248)
    vals={'signed_target_energy':ar(target),'S1_signed_upper':bound,'signed_theta_budget_for_beta2':ar(c-1)-bound}
    assert all(x.overlaps(arb(p[k])) for k,x in vals.items())
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':NAME,'precision_bits':ctx.prec,
         'union_energy_exact':str(union),'target_energy_exact':str(target),'signed_q':str(q),
         **{k:x.str(85) for k,x in vals.items()},'all_peer_balls_overlap':True,
         'inputs':{str(x.relative_to(ROOT)):H(x) for x in [union_path,signed_path,signed_source,peer_path,energy_path,BASE/'PROOF.md',ROOT/'research/signed_compression_audit/PROOF.md',Path(__file__)]},
         'elapsed_seconds':time.monotonic()-start,
         'status':'CONFIRMED combined finite compression bound; theta, low-generator and high-space hypotheses are separate.'}
    dest=BASE/'verification/candidate008_n8_m6_d32_signed.json';assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n');print('DONE',bound.str(40),flush=True)
if __name__=='__main__':main()
