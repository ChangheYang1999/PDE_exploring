"""Seal retained ancestry of the two-round selector without rewriting its run."""
from datetime import datetime,timezone
from pathlib import Path
import gzip,hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');A=E/'analysis/two_round_wall_selector'
def main():
    inputs={};compressed={};edges=0
    def data(path,expected=None):
        p=Path(path)
        if p.is_file():value=p.read_bytes()
        else:
            q=Path(str(p)+'.gz');packed=q.read_bytes();value=gzip.decompress(packed)
            compressed[str(p)]=dict(archive=str(q),archive_sha256=hashlib.sha256(packed).hexdigest())
        h=hashlib.sha256(value).hexdigest()
        assert expected is None or expected==h,str(p)
        assert str(p) not in inputs or inputs[str(p)]==h,str(p)
        inputs[str(p)]=h;return value
    def checked(path):
        nonlocal edges
        d=json.loads(data(path))
        for p,h in d.get('input_sha256',{}).items():data(p,h);edges+=1
        return d
    declarations={}
    for stem in ('wall-prefix-selector','delayed-wall-counter','reserved-wall-counter','two-round-wall-selector'):
        declarations[stem]=checked(E/(stem+'-001.json'))
    parents={}
    for area in ('wall_prefix_selector','delayed_wall_counter','reserved_wall_counter','two_round_wall_selector'):
        parents[area]=checked(E/'analysis'/area/'verification/full_games.json')
        assert parents[area]['all_passed']
    supplements=[E/'wall-prefix-selector-checker-amendment-001.json',
        E/'analysis/wall_prefix_selector/verification/provenance_supplement.json',
        E/'analysis/wall_prefix_selector/verification/value_fixtures.json',
        E/'analysis/delayed_wall_counter/verification/context_supplement.json',
        E/'analysis/reserved_wall_counter/verification/PQ_controls.json']
    for p in supplements:checked(p)
    for name in ('two-round-wall-selector-review-001.md','two-round-wall-selector-implementation-review-001.md'):
        data(E/'reviews'/name)
    recovery=checked(A/'verification/publication-directory-recovery-001.json')
    data(recovery['preserved_report'],recovery['preserved_report_sha256'])
    data(Path(__file__).relative_to(Path.cwd()))
    r=parents['two_round_wall_selector'];assert r['new_games']==28
    prior_data={p:h for p,h in declarations['wall-prefix-selector']['input_sha256'].items() if '/data/' in p and p.endswith('.json')}
    for p,h in prior_data.items():
        assert declarations['two-round-wall-selector']['input_sha256'][p]==h
        data(p,h)
    stamp=datetime.now(timezone.utc).isoformat()
    report=A/'CONTEXT.md'
    with report.open('x') as f:f.write(f'''# Retained ancestry of the two-round selector

Checked {stamp}. The new R declaration and successful run directly pinned its sources, five counter data files, exact selected result/replay controls and the O/P/Q parent receipt bytes. They did not at declaration time traverse every parent receipt's input map or directly include O's checker amendment.

This separate post-run supplement verifies those retained direct edges for all four declarations and final receipts, the O amendment and provenance supplement, the logical-value fixtures, P's context supplement and the P/Q matched controls. It also pins both R source reviews. Original inputs, declarations and results are unchanged. Losslessly compressed earlier replays, if any, are checked against their original hashes, with compressed hashes recorded separately.

The first publication attempt failed because the verification directory was absent, after writing its result narrative. Its unchanged bytes and failure receipt are retained. The missing directory was created and the unchanged publisher rerun, adding no game or policy call. This recovery is included in the input map.

This closes the documented retained-byte ancestry gap. It does not reconstruct the past process or claim that the later supplement ran before the game. There are zero new policy decisions or games. R's H1-H4 verdicts remain those of its original receipt; a successful ancestry check does not turn a failed strategic hypothesis into a success. The source proof's environmental coupling and finite support-row scope remain in force.
''')
    data(report)
    for p,h in list(inputs.items()):data(p,h)
    result=dict(time_utc=stamp,all_passed=True,checked_input_edges=edges,data_inputs=prior_data,
        input_sha256=inputs,compressed_inputs=compressed,new_games=0,policy_decisions=0,
        strategic_hypotheses={k:r[k] for k in ('h1','h2','h3','h4')})
    atomic_json(A/'verification/context_supplement.json',result,exclusive=True)
    print(json.dumps(dict(time_utc=stamp,all_passed=True,checked_input_edges=edges,unique_inputs=len(inputs))),flush=True)
if __name__=='__main__':main()
