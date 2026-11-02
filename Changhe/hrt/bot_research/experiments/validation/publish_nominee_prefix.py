"""Publish the checked equal-label source-prefix argument."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
A=Path('bot_research/experiments/validation/analysis/nominee_prefix_equivalence')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    receipt=A/'verification/prefix.json';d=json.loads(receipt.read_text())
    assert d['all_passed'] and d['source_specialization_ast_equal'] and d['shared_parameters_equal']
    assert len(d['cases'])==12 and all(x['equal_next_observation'] and len(x['rounds'])==4 for x in d['cases'])
    for p,h in d['input_sha256'].items():assert digest(p)==h,p
    now=datetime.now(timezone.utc).isoformat()
    text=f'''# Equal gameplay prefixes do not prove a strategic impossibility

Checked {now}.

CONFIRMED under the exact hypotheses in PROOF.md: P4TNUB and P5TNUBM have identical gameplay histories through round 4 and identical observations before round-5 submissions, when their public labels are equal. The proof is a source specialization and induction on engine transitions. The verifier confirms that removing the inactive v30 additions yields the v28 syntax tree, checks the shared parameter relation, and reproduces twelve equal four-round prefixes on the original engine, covering six other policies in both assignments. These finite samples support the implementation check; they do not replace the induction argument.

This rules out identifying which nominee is present from those gameplay observations alone before the round-5 action. It does not prove that no one policy can beat both. The same legal action might be effective against both, and later decisions may adapt to their divergent histories. Any claim that insurance or an attack has an unavoidable loss tradeoff needs a separate payoff argument over the relevant legal choices.

The equal-label hypothesis is necessary for this information claim. Engine.snapshot exposes each player's name, and the development runner normally uses its full specification as that name. A policy allowed to read those names can identify a specification before gameplay diverges. The current counter does not use that shortcut. Final evaluation should distinguish gameplay adaptation from identity-based selection, and no benchmark secrecy claim follows from the interface.

The formal source hashes, exact parameters, all twelve prefixes and checker source hash are in verification/prefix.json. Run check_nominee_prefix_equivalence with a fresh output path using .venv/bin/python -B from the project root, bytecode disabled, temporary files under bot_research/tmp, one thread, low priority and assigned affinity. No held-out conditions were used.
'''
    result=A/'RESULTS.md'
    with result.open('x') as f:f.write(text)
    inputs=[receipt,result,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())]
    atomic_json(A/'verification/publication.json',dict(time_utc=now,all_passed=True,input_sha256={str(p):digest(p) for p in inputs},paired_prefixes=12,scope='Equal-label gameplay prefix equivalence, not a no-common-winning-policy theorem.'),exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Equal-prefix proof and limits of indistinguishability\n\nClaim and verdict: CONFIRMED under equal public labels, P4TNUB and P5TNUBM have identical gameplay prefixes through round4 and the same opponent observation before round5 submission. Source specialization produces equal syntax trees; twelve paired prefixes (six opponents, both seats) pass. Full proof and receipt: experiments/validation/analysis/nominee_prefix_equivalence/.\n\nFor lead and defense: this does not establish that one policy cannot beat both nominees. Equal information forces equal decisions only before divergence; it does not prove that every common decision loses one game. The same qualification applies to defense.md 15:32Z claim that no trigger can handle growth6 and growth7: the prefix observation alone does not establish an unavoidable strategic price. A separate exhaustive or analytic payoff argument is needed. Also, engine observations expose names and the runner normally gives full specs as names; our theorem explicitly requires equal labels. Pool C remains unused.\n')
    print(json.dumps(dict(time_utc=now,published=str(result))))
if __name__=='__main__':main()
