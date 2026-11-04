"""Bind the registered013 application and publish its limited structural verdict."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/reference_b18s2_audit'
def dig(p):return sha256(p.read_bytes()).hexdigest()
def put(p,x):
    with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def main():
    now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    freeze=json.loads((BASE/'verification/freeze_v01.json').read_text())
    for p,h in freeze['files'].items():assert dig(ROOT/p)==h
    names=['research/legendre_exact_bridge/verification/reference_b18s2_v01/result.json','research/fitted_center_constraints/verification/reference_b18s2_v01/result.json','research/fitted_center_constraints/verification/reference_b18s2_reduction_v01/result.json']
    bridge,primary,reduction=[json.loads((ROOT/n).read_text()) for n in names]
    codes=['research/legendre_exact_bridge/code/convert.py','research/fitted_center_constraints/code/check.py','research/fitted_center_constraints/code/reduce_v02.py']
    for x,c in zip([bridge,primary,reduction],codes,strict=True):assert x['code_sha256']==dig(ROOT/c)
    assert bridge['passed'] and primary['normalization_pass'] and primary['slope_positive'] and primary['cap_pass'] and primary['metadata_all_agree'] and reduction['passed']
    assert bridge['canonical_sha256']==primary['input_sha256']==dig(ROOT/bridge['canonical_path'])
    assert reduction['record']==names[1] and reduction['record_sha256']==dig(ROOT/names[1])
    assert bridge['input_sha256']=='a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'
    assert primary['base_sha256']=='0973c3659f5ad0b5a3b2087a9e91ea61408b4356cee11006773879c13f9bfe20'
    assert primary['ell_correction_exact']=='0' and bridge['raw_atom_count']==12273
    assert bridge['origin_normalized'] and bridge['producer_elementary_identity'] and bridge['independent_recurrence_identity'] and bridge['leading_metadata_identity']
    manifest=json.loads((BASE/'data/MANIFEST.json').read_text());meta=manifest['exact_identities']
    for name,key in [('A_cubic','A_exact'),('B_cubic','B_exact'),('ell_h_phi','ell_correction_exact'),('a_star_exact','a_star_exact'),('a_star_minus_q_times_2c_minus_2_at_q_21_10','cap_margin_exact')]:assert meta[name]==primary[key],name
    for p,h in primary['files'].items():assert dig(ROOT/p)==h
    pause=json.loads((BASE/'verification/serial_pause_v01.json').read_text());assert len(pause['stages'])==3 and all(r['exit_code']==0 for r in pause['stages'])
    def bracket(key):
        v=primary[key];return '('+v['strict_lower_decimal']+', '+v['strict_upper_decimal']+')'
    scalars='\n'.join('| '+label+' | '+bracket(key)+' |' for label,key in [('a_star','a_star'),('a_star - q(2c-2)','cap_margin'),('origin cap c+1-q','origin_margin'),('complete leading circle norm','leading_circle_norm'),('A absolute-sum cancellation factor','origin_A_cancellation'),('B absolute-sum cancellation factor','origin_B_cancellation')])
    nonzero=primary['leading_sector_nonzero'];assert nonzero
    proof=f'''# Checked structure of registered snapshot013

Recorded {now}. Read PROOF.md first for the exact statement, hypotheses, notation and full derivation. The arithmetic below verifies every finite premise of that argument for C2-N1-013-phi-007-sector-d8-leg24-lat-nf2 at the fixed c=4076476460239181/2251799813685248 and q=21/10.

The raw correction SHA256 is {bridge['input_sha256']}. The independent canonical elementary SHA256 is {bridge['canonical_sha256']}. The exact base quotient SHA256 is {primary['base_sha256']}; its equality with authoritative Candidate007 is the accepted full identity bound in the request. Neither base was changed.

The complete Legendre recurrence and binomial maps agree with the exported elementary potential ({bridge['checks']} checks). The complete exact structural check passes ({primary['checks']} checks, {primary['precision_bits']} bits). A separate Python-Fraction Cartesian cubic calculation and rational Machin pi bracket verify normalization and all displayed endpoint directions ({reduction['checks']} checks). All {primary['atom_count']} elementary atoms satisfy the exact positive-scale and tau<=mu restrictions. Thus A+3B=0 and ell(h)=0 exactly. The eleven forbidden sectors above e remain zero by the accepted correction-class theorem and checked base identities. The complete leading vector at e is nonzero.

| Quantity | Strict interval |
| --- | --- |
{scalars}

The leading norm uses integral dtheta on [0,2pi], so it equals sqrt(pi times the sum of squared sine coefficients). The two cancellation factors are ratios of absolute sums of cubic contributions to their nonzero exact sums; they diagnose cancellation in these finite rows, not the condition number of the optimization Hessian. Exact arithmetic, followed by containing high-precision intervals and independent endpoint checks, controls that cancellation here.

All three stages have actual timestamps in verification/serial_pause_v01.json. The ongoing long numerical child was held for those serial checks and then resumed. The immutable manifest's exact A, B, ell, a_star and cap-margin fields agree with this independent calculation. Its FLOAT quadrature and background fields are outside this verdict.

Verdict: CONFIRMED for exact representation, structural normalization, all eleven forbidden-sector zeros, positive slope, origin cap and the complete leading circle interval. Membership in the stated weighted Sobolev spaces follows from the accepted correction-class theorem and the checked atom hypotheses, without providing a norm constant. Complete residual norms, a specified-radius tail remainder, global background gap, inverse estimate, invariant-ball closure and stationary existence remain OPEN for this source. Earlier007+b7 residual bounds do not transfer.
'''
    with (BASE/'RESULT_PROOF.md').open('x') as f:f.write(proof)
    files={n:dig(ROOT/n) for n in names};files.update(freeze['files'])
    for p in [BASE/'verification/freeze_v01.json',BASE/'verification/bridge_request_v01.json',BASE/'verification/serial_pause_v01.json',BASE/'RESULT_PROOF.md',ROOT/bridge['canonical_path']]:files[str(p.relative_to(ROOT))]=dig(p)
    put(BASE/'verification/publication_v01.json',{'created_utc':now,'passed':True,'audit_id':'OBS-013-STRUCTURE-001','candidate_id':manifest['id'],'code_sha256':dig(Path(__file__)),'proof_sha256':dig(BASE/'PROOF.md'),'result_proof_sha256':dig(BASE/'RESULT_PROOF.md'),'files':files,'checks':[x['checks'] for x in [bridge,primary,reduction]],'scope':'Complete exact structure, origin and leading sector only; no full residual or global background certificate.'})
    entry=f'''## OBS-013-STRUCTURE-001 | {now}

Claim: Registered snapshot013 preserves the exact Candidate007 normalization and forbidden-sector constraints, satisfies the origin cap and has the stated complete leading residual sector.

Method: Frozen manifest and raw source; independent full Legendre conversion; exact cubic and Fourier sums; separate Fraction Cartesian reconstruction and Machin pi enclosure. Manifest exact scalars and every bound input are rechecked. See research/reference_b18s2_audit/RESULT_PROOF.md and its complete proof dependencies.

Result: {bridge['checks']} + {primary['checks']} + {reduction['checks']} checks pass. a_star in{bracket('a_star')}, cap margin in{bracket('cap_margin')}; full leading circle norm in{bracket('leading_circle_norm')} is NONZERO. Exact ell correction is zero and all eleven forbidden higher sectors remain zero. The raw source SHA256 is {bridge['input_sha256']}.

Verdict: CONFIRMED for these structural and leading-sector claims. Full residual, specified-radius tail, global background and closure are OPEN. FLOAT mesh values in the manifest are not certified by this check.

'''
    with (ROOT/'VERIFY_REPORT.md').open('a') as f:f.write(entry)
    p=ROOT/'NOTES_FOR_TEAM.md';p.write_text(f'''# Snapshot013 exact structure confirmed

Updated {now}. OBS-013-STRUCTURE-001 confirms exact normalization, all11 forbidden higher sectors, positive slope and origin cap. Independent leading circle interval: {bracket('leading_circle_norm')}, with the unnormalized dtheta convention. a_star interval: {bracket('a_star')}. Raw hash {bridge['input_sha256']}; canonical hash {bridge['canonical_sha256']}. Read research/reference_b18s2_audit/RESULT_PROOF.md. Checks {bridge['checks']} +{primary['checks']} +{reduction['checks']}; actual serial pause/resume is recorded. Whole-plane residual and global background remain OPEN; the earlier007+b7 lower bounds do not transfer.

The source009 annulus and global-cover queue remains first and is unchanged. These fast exact checks do not transfer any009 residual endpoint to013. For AT and the existing the main model-configured theory/coordinator lanes: review the immutable013 source bindings and complete structural application. Actual provider-response identity remains uninspected. No additional agent or remote client was launched.

## Earlier notes

'''+p.read_text())
    with (ROOT/'WORKLOG.md').open('a') as f:f.write(f'\n{now}: OBS-013-STRUCTURE-001 published; complete exact conversion, origin and leading sector independently checked, {bridge["checks"]}+{primary["checks"]}+{reduction["checks"]}. No complete residual claim.\n')
    with (ROOT/'research/README.md').open('a') as f:f.write('\n- `reference_b18s2_audit/PROOF.md` then `RESULT_PROOF.md`: registered013 exact structural and complete leading-sector audit; full residual and global background open.\n')
    print(now,'published OBS-013-STRUCTURE-001',bracket('leading_circle_norm'),flush=True)
if __name__=='__main__':main()
