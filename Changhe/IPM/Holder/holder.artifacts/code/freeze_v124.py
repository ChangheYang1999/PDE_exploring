"""Freeze completed V124 evidence and apply exact prose clarifications."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'05_team_audit/closed_form37_lead'
p=ROOT/'07_diagonal_identity_term/linear_remainder/PROOF.md'
s=p.read_text();old='''Here the bases are v=r|t_r| and w=r|q|, which are below one for the
fixed small delta; the factors of r cancel in log(v/w).
and (13) bound the angular correction divided by a by C r^3.'''
new='''together with (13) bounds the angular correction divided by a by C r^3.
The bases are v=r|t_r| and w=r|q|, which are below one for the fixed
small delta; the factors of r cancel in log(v/w).'''
assert old in s;p.write_text(s.replace(old,new))
p=BASE/'PROOF.md';s=p.read_text();old='''The analytic argument below is complete. Acceptance of (1) additionally
requires successful numerical records in verification/independent_audit.json
and verification/alpha0_replay.json. Before those records exist, the
numerical inequality is OPEN. The source snapshot is immutable and its
hashes are in source/snapshot_manifest.json.'''
new='''Status: CONFIRMED in V124. The complete analytic argument and both
independent numerical checks passed. Their records are in
verification/independent_audit.json and verification/alpha0_replay.json.
The source snapshot is immutable; its hashes are in
source/snapshot_manifest.json. The corrected lead proof is saved
separately in verification/lead_PROOF_corrected.md.'''
assert old in s;p.write_text(s.replace(old,new))
for name in ['independent_audit.json','alpha0_replay.json']:
    d=json.loads((BASE/'verification'/name).read_text());assert d['verdict'].startswith('CONFIRMED')
paths=[BASE/'PROOF.md',BASE/'source/snapshot_manifest.json',*[BASE/'verification'/n for n in
 ['independent_audit.json','alpha0_replay.json','closed_form_values.json','lead_PROOF_corrected.md']],
 *[ROOT/'code'/n for n in ['audit_closed_form37_lead.py','replay_closed_form37_alpha0.py','check_closed_form37_values.py']]]
d=dict(time_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',ledger='V124',
       sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(BASE/'verification/accepted.json').write_text(json.dumps(d,indent=2)+'\n')
print(d['time_utc'],'V124 frozen')
