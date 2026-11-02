"""Add explicit source-proof/data context links without rewriting old receipts."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');A=E/'analysis/delayed_wall_counter'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs={};edges=0
    def checked(p):
        nonlocal edges
        inputs[str(p)]=sha(p);d=json.loads(Path(p).read_text())
        for q,h in d.get('input_sha256',{}).items():
            assert sha(q)==h,q
            assert q not in inputs or inputs[q]==h,q
            inputs[q]=h;edges+=1
        return d
    odeclaration=checked(E/'wall-prefix-selector-001.json')
    o=checked(E/'analysis/wall_prefix_selector/verification/full_games.json')
    pdecl=checked(E/'delayed-wall-counter-001.json')
    p=checked(A/'verification/full_games.json')
    fixtures=checked(E/'analysis/wall_prefix_selector/verification/value_fixtures.json')
    assert o['all_passed'] and p['all_passed'] and fixtures['all_passed']
    assert fixtures['policy_decision_calls']==0 and len(fixtures['tests'])==13
    data={q:h for q,h in odeclaration['input_sha256'].items() if '/data/' in q and q.endswith('.json')}
    for q,h in data.items():assert sha(q)==h;inputs[q]=h
    for name in ('wall_prefix_selector','delayed_wall_counter','reserved_wall_counter'):
        q=E/'analysis'/name/'PROOF.md';inputs[str(q)]=sha(q)
    for name in ('wall-prefix-provenance-review-001.md','delayed-wall-counter-review-001.md'):
        q=E/'reviews'/name;inputs[str(q)]=sha(q)
    assert all(c['outcome']=='D' for c in o['cases'] if c['opponent']=='G')
    assert all(c['outcome']=='W' for c in p['cases'] if c['opponent']=='O')
    assert all(c['outcome']=='L' for c in p['cases'] if c['opponent']=='G')
    stamp=datetime.now(timezone.utc).isoformat()
    report=A/'CONTEXT.md'
    text=f'''# Additional source and data links

Checked {stamp}. This post-run context receipt leaves all pre-call declarations and completed results unchanged. It links P's result explicitly to O's original declaration, source proof and completed result. P's declaration pinned O's executable source and logical-state checker directly, but did not directly include O's earlier informal proof or declaration.

The thirteen constructor and logical-value fixtures have zero policy decision calls. Their original receipt directly pins the early-wall JSON and the Python source closure. Constructors also read other counter JSON inputs. This supplement directly pins all five JSON inputs from O's original declaration, checks their current bytes against that pre-call declaration, and links the original fixture receipt. It supplies omitted provenance edges; it does not retrospectively attest which bytes a past process opened.

The old O/G games draw in both seats. P beats O and loses to G in both seats. This supports the stated counterexample to O's public signal rule, with the established caveat that moving the walls changes early income as well as visible state. It is not a pure information intervention. No games or policy decisions are added.
'''
    with report.open('x') as f:f.write(text)
    inputs[str(report)]=sha(report);inputs[str(Path(__file__).relative_to(Path.cwd()))]=sha(__file__)
    assert all(sha(q)==h for q,h in inputs.items())
    result=dict(time_utc=stamp,all_passed=True,checked_input_edges=edges,data_inputs=data,
        input_sha256=inputs,new_games=0,policy_decisions=0,fixture_count=13)
    atomic_json(A/'verification/context_supplement.json',result,exclusive=True)
    print(json.dumps(dict(time_utc=stamp,all_passed=True,checked_input_edges=edges,data_inputs=len(data))))
if __name__=='__main__':main()
