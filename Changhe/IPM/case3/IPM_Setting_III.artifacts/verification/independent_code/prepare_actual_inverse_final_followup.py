from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';now=datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
z=json.loads((V/'FINAL_COMPONENT_CHECKS.json').read_text());assert z['status']=='PASS_FINITE_COMPONENTS_AND_MAP_DECOMPOSITION' and z['count']==3258 and all(q['passed']for q in z['checks']);o=z['outputs']
for p,h in z['bindings'].items():assert sha(p)==h,p
s=(R/'RESULTS_DRAFT.md').read_text();s=s.replace('final inverse audit, draft for review','final inverse audit, repaired draft for review').replace('Written UTC 2026-10-22T04:02:24.259998+00:00.',f'Written UTC {now}.')
s=s.replace('undefined ratio is omitted. The three maxima need not occur at the same point.','undefined ratio is omitted. Regions use binary64 hypot and the stated half-open\nintervals. The three maxima need not occur at the same point.')
s=s.replace('The largest S/Nf_B is 2.8668589107e-14 at index23. These compare three rules','The largest S/Nf_B is 2.8668589107e-14 at index23, using the exact pre-rounding\nrational Nf_B. These compare three rules of one independent implementation')
s=s.replace('All selected local precision diagnostics pass;', 'None of the 13 new witnesses exceeds the previously reported 17-point jet\nmaxima. All selected local precision diagnostics pass;')
s=s.replace('error bound. At that far witness,','error bound. The signed component ledgers use disjoint phase node sets and\nfixed-sign coefficients for positive y; no negative-y extension is assumed.\nAt that far witness,')
start=s.index('Finite nonzero residuals and sensitivity to exported map velocities are')
end=s.index('Reading order:',start)
rows=[]
for q in o['all_node_component_maxima']:
 rows.append(f"| {q['rule']} | {q['reference']} | V{q['component']} | {q['absolute']['value']:.10g} ({q['absolute']['index']}) | {q['pure_relative']['value']:.10g} ({q['pure_relative']['index']}) |")
pairs=[]
for q in o['witness_component_maxima']:
 pairs.append(f"| V{q['component']} | {q['metric']} | {q[q['metric']]['value']:.10g} | {q['index']} | {' versus '.join(q['pair'])} |")
assert all(q['both_zero_count']==0 for q in o['all_node_component_maxima'])and all(not q['both_zero'] for q in o['witness_component_pairs'])
frac=max(q['map_residual_over_B_abs']['value']for q in o['headline_decompositions']);assert frac<.0046
new=f'''The supplemental independent checker passed 3258 finite checks at
{z['utc']}. With the same own jet J at every node, it verifies exactly
R_B = R(J,Vm) + (V_B-Vm).grad(J).
The maximum abs(R(J,Vm)) is {o['fixed_map_max_absolute']['value']:.12g}, less than
4e-8. At the twelve regional maximizing entries above, the largest ratio
abs(R(J,Vm))/abs(R_B) is {frac:.10g}. At those entries the observed residual
is therefore predominantly the velocity discrepancy projected onto this
fixed gradient. The exact three terms, fractions and coordinates are in
FINAL_COMPONENT_CHECKS.json. This assertion concerns those finite entries,
not every point of the plane. Which velocity is closer to the exact integral
remains OPEN. Neither these identities nor the reconstructed map export
authenticate historical matrices or establish a cause for a solver stall.

Velocity errors orthogonal to the local gradient can be invisible to a
residual comparison. The component differences below are independently
recomputed from all 2304 stored A/B velocities against Vm and Vp. Pure
relative means abs(a-b)/max(abs(a),abs(b)), with no artificial floor; the
both-zero case is undefined. There are no both-zero pairs in this table.
Absolute and relative maxima have their own indices and may differ.

| Rule | Reference | Component | max absolute difference (index) | max pure relative difference (index) |
| --- | --- | --- | ---: | ---: |
{chr(10).join(rows)}

At each of the 30 C witnesses, every pair C-B, C-A, A-B is computed for
both components, for 180 records. Their four maxima follow. All pairwise
records, their exact values and coordinates are retained in
FINAL_COMPONENT_CHECKS.json; none has a both-zero denominator.

| Component | Metric | Maximum | Index | Pair |
| --- | --- | ---: | ---: | --- |
{chr(10).join(pairs)}

These are three rules of one independent inverse implementation, with C
checked at the selected 30 points only. Their agreement in both components
and residual projections is empirical. It gives no error enclosure against
the exact integral, and no uniform statement over all integration paths.

The smallest recorded finite-panel widths are {o['metadata']['A']['minimum_panel_width']['min']:.10g}
for A and B (index385), and {o['metadata']['C']['minimum_panel_width']['min']:.10g} for C
(index0). Inner/outer panel-count ranges are 1..36/7..16 for A,
1..36/8..17 for B, and 1..61/16..32 for C. Finite inner/outer nodes range
48..1728/336..768, 64..2304/512..1088, and 88..5368/1408..2816,
respectively; the tail-node counts are fixed at160,192,256. All recorded
rounded-endpoint-node and imposed-axis counts are zero. These are quadrature
metadata, not accuracy estimates. Bitwise B replays of non-arithmetic
fields are confined to the five MP targets; integrity checks do not supply
historical authentication.

The component check's initial TypeError arose while adding a duplicate
component key to a summary dictionary. Its source and recovered failure
description are preserved. The correction was proved before editing and
all checks rerun; no candidate arrays changed.

The measured residuals refer to finite quadrature outputs. This comparison
alone proves neither that Vm is inaccurate nor that the represented trial
fails the exact hydrostatic equation. Any exclusion based on independently
proved center conditions is a separate result. Accuracy of the exact
hydrostatic inverse remains OPEN: no derivative enclosure, quadrature error
bound, or uniform global residual estimate has been proved. No infinite
sequence or continuum limit is controlled. No full-plane candidate,
existence theorem, or nonexistence theorem follows. The principal verdict
remains UNRESOLVED.

'''
s=s[:start]+new+s[end:];s=s.replace('both final correction proofs; this draft.','both final correction proofs; FINAL_COMPONENT_AND_INTERPRETATION_PROOF.md;\nFINAL_COMPONENT_DICTIONARY_CORRECTION_PROOF.md; this repaired draft.')
(R/'RESULTS_REPAIRED_DRAFT.md').write_text(s)
files=[R/'RESULTS_REPAIRED_DRAFT.md',R/'FINAL_COMPONENT_AND_INTERPRETATION_PROOF.md',R/'FINAL_COMPONENT_DICTIONARY_CORRECTION_PROOF.md',Path('independent_code/check_actual_inverse_components.py'),V/'opus_final/answer.md',V/'opus_final/metadata.json']
head='''Follow-up to your actual final desk review request8909e38f-be19-4a58-b718-2db62657a945 of verifier result309. Requested actual model Claude Opus5.5. No independent execution by you is asserted. Audit the exact R1/R2 repair text and supplemental independent code/output against your objections. Are any blocking mathematical or interpretive issues left? Correct your literal <=3.9e-8 to <4e-8 (true maximum3.93085333002e-8). We do not adopt the phrase three independent quadratures: one independent implementation, three rules, C only30. We quantify the map fraction at12regionalmax entries, not all2304. We omit your optional304 consistency comparison to avoid an unbound claim. Your prior review scope remains limited to the text/code supplied; exact integral accuracy and main PDE remain OPEN. We will verify your response before publication.

Restrictions: no JavaScript/TypeScript/Node or related tooling; no servers/listeners/tunnels; no RLScience cluster access or use; no Lean/Lake; no commits/push/posts/human contact; no writes outside verification. Text-only desk review; do not execute or request prohibited activity. Primary endpoint UNRESOLVED; no early stop.
'''
parts=[head]
for p in files:parts.append('\nFILE '+str(p)+' SHA256 '+sha(p)+'\n'+p.read_text())
parts.append('\nCOMPONENT OUTPUTS with source SHA256 '+sha(V/'FINAL_COMPONENT_CHECKS.json')+'\n'+json.dumps({k:v for k,v in z.items()if k not in ['checks','bindings']},indent=2))
# Supply the previous complete context so the final follow-up can examine dependencies.
parts.append('\nPREVIOUS COMPLETE FINAL REQUEST\n'+(V/'OPUS_FINAL_REQUEST.txt').read_text())
req='\n'.join(parts);(V/'OPUS_FINAL_FOLLOWUP_REQUEST.txt').write_text(req)
(V/'FINAL_FOLLOWUP_INPUTS.json').write_text(json.dumps(dict(utc=now,files={str(p):sha(p)for p in files},component_checks_sha256=sha(V/'FINAL_COMPONENT_CHECKS.json'),request_sha256=sha(V/'OPUS_FINAL_FOLLOWUP_REQUEST.txt')),indent=2)+'\n')
print('prepared',len(req.encode()),now)
