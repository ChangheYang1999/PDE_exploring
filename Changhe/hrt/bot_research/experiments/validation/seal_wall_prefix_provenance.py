"""Add the omitted amended-checker receipt edges without rewriting evidence."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.finite_table_certificate import verify

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/wall_prefix_selector'
def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs={};checked_edges=0
    def checked(p):
        nonlocal checked_edges
        inputs[str(p)]=sha(p);d=read(p)
        for q,h in d.get('input_sha256',{}).items():
            assert sha(q)==h,q
            assert q not in inputs or inputs[q]==h,q
            inputs[q]=h;checked_edges+=1
        return d
    declaration=checked(E/'wall-prefix-selector-001.json')
    amendment=checked(E/'wall-prefix-selector-checker-amendment-001.json')
    final=checked(A/'verification/full_games.json')
    assert amendment['constructor_fixtures_passed']
    assert amendment['policy_calls_before_amendment']==amendment['new_games_before_amendment']==0
    assert final['all_passed'] and final['new_games']==22
    assert final['h3'], 'Observed branch or self-result exception requires a separate interpretation.'
    campaigns=[]
    for campaign in declaration['campaigns']:
        name=campaign['name'];freeze=read(R/name/'freeze.json')
        assert datetime.fromisoformat(amendment['time_utc'])<datetime.fromisoformat(freeze['started_utc'])
        inputs[str(R/name/'freeze.json')]=sha(R/name/'freeze.json')
        branch=checked(R/(name+'-branches.json'))
        assert branch['all_passed'] and all(c['predicted_branch_agrees'] for c in branch['cases'])
        campaigns.append(dict(name=name,started_utc=freeze['started_utc'],branch_utc=branch['time_utc']))
    certificate=final['pure_O_certificate'];assert certificate and verify(final['payoff'],certificate['weights'])
    assert all(c['outcome']=='D' for c in final['cases'] if c['opponent']=='O')
    for p in [Path(__file__).relative_to(Path.cwd()),E/'reviews/wall-prefix-selector-review-001.md']:
        inputs[str(p)]=sha(p)
    stamp=datetime.now(timezone.utc).isoformat()
    text=f'''# Amended-checker provenance supplement

Recorded {stamp}, after the game and checker executions. This document supplements the existing final receipt; it does not replace or edit any declared input or prior result.

The version-two checker verified its four amendment pins at entry and exit, but its branch and final receipt builders initialized their input maps from the original declaration and campaign freezes. They consequently omitted direct edges to the amendment and the new checker/helper. The separate source review identified this receipt-closure gap before publication. `verification/provenance_supplement.json` adds those edges, checks every direct input edge of the declaration, amendment, three branch receipts and final receipt, and pins this sealer and the source review. The amendment time precedes each campaign's recorded start. These are checks of retained bytes and recorded timestamps, not a new independent attestation of past process state.

The review also identified two conditional reporting gaps. A changed actual branch would make the preselected baseline label inaccurate, and a non-draw self result would stop the publisher before its final falsification report. Neither was exercised here: every observed branch equals its predeclared branch, the full predicted row check passes, and both self games draw. The supplement explicitly checks these conditions before accepting the successful finite certificate. It rechecks that certificate with exact rational arithmetic.

Logical-state comparisons exclude shared module globals, alias identity and process time. The conditional common-prefix proof and measured execution scope remain unchanged. There are no new policy calls or strength games in this supplement.
'''
    proof=A/'PROVENANCE.md'
    with proof.open('x') as f:f.write(text)
    inputs[str(proof)]=sha(proof)
    assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=stamp,all_passed=True,checked_input_edges=checked_edges,input_sha256=inputs,
        declaration_utc=declaration['declared_utc'],amendment_utc=amendment['time_utc'],campaigns=campaigns,
        observed_branches_match=True,both_self_games_draw=True,exact_certificate_rechecked=True,
        policy_calls=0,new_games=0,scope='Retained-byte closure for the pre-call checker amendment; original receipts unchanged.')
    atomic_json(A/'verification/provenance_supplement.json',result,exclusive=True)
    print(json.dumps(dict(time_utc=stamp,all_passed=True,checked_input_edges=checked_edges,unique_inputs=len(inputs))),flush=True)
if __name__=='__main__':main()
