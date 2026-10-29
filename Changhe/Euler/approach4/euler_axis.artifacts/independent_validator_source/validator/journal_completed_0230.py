#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parent.parent;BASE=ROOT/'axisymmetric_euler_24h';RES=BASE/'results'
marker=RES/'journal_completed_0230.json'
if marker.exists():raise FileExistsError(marker)
now=datetime.now(timezone.utc).isoformat();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
summary=json.loads((RES/'transport_completed_summary_20261029T023019.423459Z.json').read_text())
blocks=[]
blocks.append(f'''## {now}: full registered L1 reproduction with native derivatives

Method: independently differentiated the documented ball Jacobi, shell Chebyshev and exterior power bases in native radius and angle, with exact rational coordinate recurrences and a Cartesian polynomial origin evaluator. Compared the entire frozen L1 registered grid with the earlier Taylor implementation. This keeps the same mathematical field and pressure algorithm.

Result: expanded evaluator fixtures 484 PASS at2026-10-29T02:05:23.497286Z. The full run completed at2026-10-29T02:22:29.785289Z. Comparison at2026-10-29T02:22:45.313607Z:11588 checks PASS,57 sets,684 arrays, maximum scaled array discrepancy4.18332035678759e-12 and maximum scaled scalar discrepancy1.739527314394223e-8. Native rho_max=1.9235713186098957 and m_max=21.040838192520635. Checkpointed active runtime lower bound534.0670524728484s, including the earlier partial run; the final invocation measured242.89534036582336s. Earlier cache-method collision and timeout were retained, not counted as successful full runs.

Verdict: CONFIRMED full-grid numerical reproduction and the same A1/A2 failures. This is a second derivative route, not an independent pressure formula or a new candidate. Earlier diagnostic Boolean fields absent from the new record are explicitly listed in native_l1_full_comparison.json. Evidence: results/native_l1_registered and results/native_l1_full_comparison.json; proof and fixtures: research/native_derivative_operators.
''')
blocks.append(f'''## {now}: physical-time check of repaired radial transport

Method: source-centred radial transport was checked at30 distinct points per level by a separate physical-time DOP853 integration and variational equations, including transverse interface event corrections. Radii are0.3,3,30,250,500,1000 in the working source-centred coordinates; angular cosines are-1,-0.8314696,0,0.8314696,1. Both routes use the disclosed localized Gaussian strain repair, with radius0.3 and K=3.5. Cutoffs32,48,64 and relative tolerances2e-10,2e-11 were tested.

Result: atT=64, maximum absolute q differences against the radial reference are5.704961191094204e-7(L1) and5.566932106959577e-7(L2); maximum q_z differences are2.345286542249081e-6 and3.979973323631203e-6. Relative q differences are below8.56e-6; q_z differences normalized by max(|q_z,time|,|q_z,radial|,1e-10) are below1.05e-4. Tightening the ODE tolerance changes q by at most5.09e-11 and q_z by1.03e-10; changingT=48 to64 changes q by at most3.38e-10 and q_z by3.56e-11. Terminal |a| is at most2.514e-12. The last successful run completed2026-10-29T02:27:21.956290Z in80.23041414096951s. The earlier L2 tight invocation was interrupted; its initialized-only JSON is preserved and excluded.

Verdict: CONFIRMED sampled agreement of these two transport parametrizations. The remaining discrepancy is larger than the observed ODE tolerance/cutoff changes, so it is not explained by those changes; the radial interpolation, angular derivative and remapping remain possible sources. This is not a uniform pointwise error bound or an infinite-cutoff proof. Evidence: transport_completed_summary_20261029T023019.423459Z.json and its four hashed repaired-time inputs. The normal successful runs took47.0284/65.5072s and the tight runs54.6203/80.2304s; these are actual invocation runtimes.
''')
blocks.append(f'''## {now}: original frozen L1 source transport completed

Method: transported K=3.5 by the original frozen phi, with312 diagnostic points, ten core/shell/interface/axis sets, cutoffs16,32,48, relative tolerances2e-8 and2e-10, and variational interface corrections. No Gaussian repair is used here. The actual source has a0=1-2phi_z=5.922614709774621e-7, so both raw q_T and exp(a0 T)q_T are reported. These are distinct from the repaired-field results.

Result: completed2026-10-29T02:21:57.299675Z in3364.857156189624s wall and3338.150436658s CPU. AtT=48 the finite-cutoff identity defect is2.504473955525747e-9 at the tighter tolerance, down from1.4218876366939435e-7. Changing tolerance changes q by5.0254e-10 and grad q by1.3559e-7. BetweenT=32 and48, raw q changes3.3629e-5 and compensated q changes9.7070e-7. AtT=48 the relative difference from saved q is0.08967 in shell-4,0.62720 in shell-1,0.77457 in shell0,0.83673 in shell1,0.86492 in shell3 and0.86703 in shell5, normalized by transported-q RMS. It is0.07811 to0.07998 on the two axis/collar sets. Replacing the saved q by q_T raises rho_eta in shell-1 from0.16004 to2.78863 and at interface0 from0.16841 to2.84660. The full table is retained in the immutable summary.

Verdict: CONFIRMED a large saved-versus-transported swirl discrepancy and failure of eta closure for this prescribed original phi on these diagnostic sets. They are not the registered ranking grid. Compensation converges toward a forced equation with residual a0 q, not toward the homogeneous Euler transport equation; the raw nonzero-source-strain field cannot support a continuous exact solution with q(source)=K. No conclusion about a neighbourhood of potentials or general nonexistence follows. L2 original-field transport is running separately.
''')
casepaths=sorted((ROOT/'research/two_series_global_portrait/verification').glob('*.json'))
cases=[json.loads(p.read_text())for p in casepaths if p.stem!='results']
assert len(cases)==7 and all(d['certified']for d in cases)
table='\n'.join(f"| {d['name']} | {d['c_l']} | {d['aspect']} | {d['lower_float']:.12g} | {d['leaf_count']} | {d['depth']} |"for d in cases)
portrait=f'''## {now}: exact global portrait certificates for all seven two-series fields

Method: independently derived the Euclidean radial-growth identity for phi=z sum_j u^(-j/(2c_l)) P_j(as/u,z^2/u), u=1+as+z^2. Exact rational tensor Bernstein bounds, integer rational-power enclosures and complete dyadic subdivision cover the compactified square. Every accepted leaf's polynomial net is separately reconstructed by affine substitution in the original power basis, and prefix/area checks verify coverage. The a=2 cases use the Euclidean radius formula, not the elliptical-radius formula.

Result:247 analytic/arithmetic fixtures PASS at2026-10-29T02:22:45.497752Z. All seven exact-decimal inputs have W dot grad log R >= gamma >0 globally:

| Field | c_l | Aspect a | gamma | Leaves | Maximum depth |
|---|---:|---:|---:|---:|---:|
{table}

The seven certificate computations completed between2026-10-29T02:29:23.237556Z and2026-10-29T02:29:30.848953Z, using{sum(d['wall_seconds']for d in cases):.9f}s measured computation. The wrapper paused pressure for7.802420808933675s and resumed it successfully.

Verdict: CONFIRMED exactly one meridional zero, the source at the origin with eigenvalues c_l-1/2 and c_l+1, and convergence of every backward meridional orbit to it for each of these seven prescribed exact-decimal fields. The free-c_l field lies outside the target interval. These certificates do not assert Euler closure or validate the separately transported vorticity. Proof, individual exact fractions, all leaves, code and hashes: research/two_series_global_portrait. No primary certificate implementation was imported or executed.
'''
blocks.append(portrait)
(ROOT/'research/two_series_global_portrait/RESULTS.md').write_text('# Independent global portrait results\n\n'+portrait)
with (ROOT/'research/native_derivative_operators/RESULTS.md').open('a')as f:f.write('\n'+blocks[0])
with (ROOT/'research/source_time_crosscheck/RESULTS.md').open('a')as f:f.write('\n'+blocks[1])
with (ROOT/'research/source_transport_cutoff/RESULTS.md').open('a')as f:f.write('\n'+blocks[2])
clarification=f'''## {now}: clarification of the failure-map filter

SPEC9.1 explicitly defines its per-run floor using s_core>=0.05 and s_far>=0.05 in the parenthetical. That pre-registered magnitude filter is retained exactly; no new cross-level stability condition is imposed on the floor. Full label-B acceptance under SPEC9 additionally requires stability to10percent. Thus the 02:27Z audit item4 concerns claims of a full B2 acceptance pass and ambiguity in captions, not validity of the pre-registered magnitude-filter floor. F1/F5 may say "SPEC9.1 floor, filtered by swirl magnitude; acceptance stability assessed separately." The blanket instruction to change every "B2-admissible" label should be read with this distinction. Other narrative audit items are unchanged.
'''
with (ROOT/'report_audits/failure_narrative_20261029T022726.262542Z/AUDIT.md').open('a')as f:f.write('\n'+clarification)
fig=f'''# Revised F1/F5 audit\n\nDate: {now}. Frozen revision: numerics 02:22Z.\n\nMethod: checked figure CSVs against the frozen failure map and their underlying validation records, including per-equation maxima over all point sets. Read the generating code and visually inspected both frozen PNGs.\n\nResult:489 scalar checks PASS, zero incorrect dominant-equation labels, and no missing referenced records. The F1 independent ladder now has a separate level axis and accurate basis counts. F5 shades the target interval, marks the outside-target c_l=0.80 point and explains the c_l=2/3 reference. Scalar content: CONFIRMED.\n\nRemaining visual items: F1's upper red D48 label touches the title/frame; the legend covers a purple D36 marker; orange and green D36 labels overlap; and the right-panel level2 annotation should move inside the panel. F5's outside-target annotation should move away from the dense endpoint group. These are legibility issues, not changes to the data. Final visual clearance remains OPEN pending revised images.\n\nThe pre-registered SPEC9.1 floor uses its explicit swirl-magnitude filter. It does not by itself establish the separate cross-level stability clause in full SPEC9 B2 acceptance. Captions should make this distinction without altering the registered floor.\n\nEvidence: audit.json, frozen sources, captions, CSVs, PNGs and validation records in this directory. Initial incorrect-label revision remains in F1_F5_initial.\n'''
(ROOT/'report_audits/F1_F5_revision_1/AUDIT.md').write_text(fig)
blocks.append(f'''## {now}: failure narrative and revised F1/F5 audited

Method: froze the 02:22Z Stage II narrative, failure-map CSV, code and selected primary validation records; checked claims against exact frozen states and the registered protocol. Independently audited revised figure data and viewed both PNGs.

Result: narrative audit identifies incorrect completed-validation status, a working/reporting-gauge radius mismatch, an incorrect small origin-collar residual range (L2 has rho_Mz=2.902), blanket Stage I swirl-collapse and reflection-shell claims, and GPU/CPU slot-hour conflation. The396-row snapshot has369 device=cuda rows summing23.643 rounded slot-hours and27 device=cpu rows summing4.230, not27.87 GPU hours. This is the completed-row snapshot, not an audit of every interrupted run or exclusive physical GPU utilization. The new rm5 state has primary rho1.5813988 but still needs independent export validation. Revised F1/F5 data:489 checks PASS, zero incorrect equation labels; remaining F1 overlaps need repair.

Verdict: corrections and qualifications are required as individually recorded in report_audits/failure_narrative_20261029T022726.262542Z/AUDIT.md; revised scalar figure data CONFIRMED, final figure legibility OPEN. The SPEC9.1 magnitude filter remains unchanged; only claims that it establishes full cross-level B2 acceptance are rejected. The current overall failure conclusion is unaffected. Collaboration is with the lead's actual model us.anthropic.claude-opus-5-5, through the local reports and notes, with no outside messages or compute.
''')
for file in ['INDEPENDENT_VALIDATION.md','WORKLOG.md']:
 with (ROOT/file).open('a')as f:f.write('\n'+'\n'.join(blocks))
with (ROOT/'NOTES_FOR_TEAM.md').open('a')as f:
 f.write('\n'+clarification+'\n'+portrait)
 f.write(f'''\n## {now}: completed L1 native and source checks\n\nFull L1 native derivative reproduction:11588 checks/684 arrays PASS, same rho1.9235713 and m21.0408382. All seven two-series global source portraits are now CONFIRMED for their exact-decimal prescribed phi; independent transported eta remains queued. Gaussian-repaired physical-time transport agrees with radial transport on30points/level: q discrepancies<=5.71e-7, q_z<=3.98e-6; tightening time integration changes these by<=1.03e-10. The original, unrepaired L1 source transport is also complete; its large saved-q differences and increased eta residual are documented separately. Nonzero a0=5.9226e-7 is retained, so raw, compensated and Gaussian-repaired results must not be conflated. Full tables and limits are in INDEPENDENT_VALIDATION.md and transport_completed_summary_20261029T023019.423459Z.json.\n\nFor Opus review, inspect the topic76 radial formula and positive numerator/divisor bound, especially a=2, plus the interpretation of the physical-time comparison. Local read-only collaboration only; no JavaScript/TypeScript, servers, RLScience/cluster, remote or paid compute.\n''')
idx=ROOT/'research/INDEX.md';s=idx.read_text().replace('All468 checks pass; the full registered-grid comparison is pending.','All484 expanded fixtures and11588 full L1 comparison checks pass;57 sets and684 arrays reproduce the Taylor evaluator.').replace('Forty analytic checks pass; candidate comparison pending.','Forty analytic checks pass; both repaired L1/L2 agree with a physical-time check at30points per level, with explicit cutoff and tolerance studies.')
s+='\n76. [Global two-series source portraits](two_series_global_portrait/PROOF.md). Independent Euclidean radial identity and exact rational Bernstein/power bounds certify one global meridional source for all seven prescribed exact-decimal fields;247 fixtures pass. [Results](two_series_global_portrait/RESULTS.md).\n';idx.write_text(s)
marker.write_text(json.dumps({'completed_utc':now,'block_count':len(blocks),'scope':'Journal of completed work; no new numerical solver run'},indent=2)+'\n')
print(now)
