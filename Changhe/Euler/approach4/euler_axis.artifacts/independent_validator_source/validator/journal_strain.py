from pathlib import Path
from datetime import datetime,timezone
import json
ROOT=Path(__file__).resolve().parent;lane=ROOT.parent;now=datetime.now(timezone.utc).isoformat()
collection=ROOT/'results/strain_collection_20261029T020059.456111Z/collection.json';d=json.loads(collection.read_text())
lines=['| Field | Angular nodes | Max log step | Start radius | Induced strain with estimated tail |','|---|---:|---:|---:|---:|']
for r in d['runs']:lines.append(f"| {r['level']} | {r['angular']} | {r['dx']} | {r['start']} | {r['strain']:.12f} |")
text=f'''# Independent transported-strain validation

Recorded {now}. Candidate runs completed between 2026-10-29T01:49:07.866345+00:00 and 2026-10-29T02:00:21.990901+00:00. All runs used one assigned CPU core at a time; the existing CPU48 pressure worker was paused and resumed by recorded wrappers. No GPU or remote computation was used.

## Method

The standalone proof in PROOF.md derives the source-centred radial transport equations, source values, the explicit Gaussian repair and the five-dimensional strain kernel. The implementation starts from the saved phi coefficients and does not use the primary q or eta as transport input. It independently evaluates phi and its first two derivatives, transports log(q/K), its angular derivative and eta by fourth-order characteristic steps, and remaps on a quintic angular spline. The angular moment of that spline is integrated exactly on each polynomial piece; radial integration uses Simpson quadrature in log radius.

For both fields c_l=0.749, K=3.5 and the repair is

    phi_repaired = phi + epsilon (z-z_*) exp(-(r^2+(z-z_*)^2)/0.09).

L1 has z_*=0.007901586329666777 and epsilon=2.9613073537770873e-7. L2 has z_*=0.03937253277827264 and epsilon=1.937215708402995e-7. The repair changes the prescribed field, preserves the source point and second derivatives there, and makes phi_z exactly1/2. These are piecewise-classical numerical fields, not smooth exact profiles.

The independent evaluator passed48 tests against this lane's original Taylor evaluator, with a maximum absolute discrepancy of1.68e-14 on500 points through second derivatives. The transport method passed25 manufactured checks, including fourth-order convergence of fixed-angle and moving-angle examples. The initial failed spherical evaluation near R=0 and a subsequent initial-logging failure are preserved, with their source versions. The successful evaluator uses an exact-polynomial origin patch.

## Results

{chr(10).join(lines)}

At fixed129 angular nodes, halving the log step from0.02 to0.01 changes the strain by1.77385e-7 forL1 and7.31936e-8 forL2. At fixed step0.01, increasing129 to257 nodes changes it by1.13082e-8 and1.05797e-8. Reducing the starting radius from1e-4 to2.5e-5 at257 nodes changes it by3.70708e-8 and2.63539e-8.

The finest L1 value is-0.8118805553642826, comprising the integral to1000 of-0.8113694034108107 and estimated tail-0.0005111519534719042. The finest L2 value is-0.5136183944589859, comprising-0.5133572657587148 and estimated tail-0.0002611287002712034. Tail-extrapolated values at cutoffs250/500/1000 differ by at most4.99e-6 forL1 and2.06e-6 forL2. The numerical radial speed F remains positive on all evaluated stages, with minimum approximately0.249; this is not a continuum certificate.

For L2 the consecutive radial bands ending at0.3,3,30,250,500,1000 contribute approximately+0.03011344,-0.13305989,-0.38306518,-0.02594610,-0.00100197,-0.00039757. The negative strain is therefore not a tail-only effect. L1 has the same sign pattern.

The lead referee's separately stored stable results use321 angular nodes, step0.025 and cutoff2980.957987. Their values are-0.8118813840576037 and-0.5136192539073501, differing from this calculation by8.29e-7 and8.60e-7. These files were copied and hashed in the collection; no primary evaluator was imported.

## Verdict and limits

CONFIRMED: the reported rounded wrong-sign induced strains, approximately-0.812 and-0.514, for the explicitly Gaussian-repaired L1 and L2 potentials. Their numerical defects from the required+0.5 strain are about-1.312 and-1.014. A source-amplitude change multiplies the transported vorticity and strain by a nonnegative square and does not repair a negative sign in this prescribed-field calculation.

OPEN: a rigorous quadrature or tail enclosure, a global backward-basin certificate, and a quantitative distance bound to every exact profile. The output supplies numerical convergence of an integrated moment, not those theorems. The piecewise interfaces are not exactly matched. Pointwise angular-gradient convergence is also not established: the largest remapping-gradient discrepancy is not monotone across the grid sequence, and the fine start-radius comparison changes q/eta sup profiles at band radii by up to1.15e-4/2.78e-4 relatively. These facts are retained rather than hidden by the stable integrated strain. A comparison with time-parametrized event-resolved transport is a useful further check.

The saved raw potentials already fail independent interface, source-jet and full residual tests. This new result does not change the outcome label or imply nonexistence in the general smooth class.

## Evidence

- Immutable collection: axisymmetric_euler_24h/results/strain_collection_20261029T020059.456111Z, including every candidate and source hash, run CSV, pointwise comparisons and copied referee results.
- Code: source_radial_transport.py, radial_transport_solver.py and transported_strain_audit.py at the project root; every run stores their hashes and the proof hash.
- Tests: this topic's verification/check_evaluator.py and check_solver.py, with results and failed-attempt archives.
- Pause records: strain_batch_one_pause.json, strain_batch_two_pause.json, strain_crosscheck_pause.json and strain_collection_pause.json in project results.

The ten successful candidate runs used {sum(r['wall_seconds'] for r in d['runs']):.6f} measured process-wall seconds and {sum(r['cpu_seconds'] for r in d['runs']):.6f} CPU seconds. This excludes evaluator development/tests and the time the other worker was paused; pause durations are recorded separately and must not be added to CPU time.
'''
(lane/'research/source_centered_vorticity_transport/RESULTS.md').write_text(text)
(lane/'research/source_centered_vorticity_transport/verification/collection_path.txt').write_text(str(collection.relative_to(lane))+'\n')
short=f'''\n## {now}: Gaussian-repaired transported strain independently confirmed

Method: independent coefficient evaluation, source-centred characteristic transport and the five-dimensional Newton strain moment, with separate angular, radial-step, starting-radius and cutoff checks. The source repair is exactly the one disclosed in the report, epsilon(z-z_*)exp(-(r^2+(z-z_*)^2)/0.09); K=3.5 and c_l=.749. This changes the prescribed potential.

Result: finest induced strains are-0.8118805553642826 forL1 and-0.5136183944589859 forL2, against required+0.5. Fixed-step angular changes are1.13e-8/1.06e-8; start-radius changes3.71e-8/2.64e-8; tail-extrapolated cutoff250-to1000 changes4.99e-6/2.06e-6. Agreement with the separately stored referee stable values is better than8.60e-7. Ten successful runs used {sum(r['wall_seconds'] for r in d['runs']):.6f} measured wall seconds.48 evaluator tests and25 analytic transport tests passed.

Verdict: CONFIRMED the rounded numerical wrong-sign strains (-0.812/-0.514) of the stated repaired fields. OPEN a rigorous tail enclosure, global basin, pointwise derivative convergence and distance-to-solution bound. Fine q/eta sup profiles change by up to1.15e-4/2.78e-4, and remapping-gradient discrepancies are not monotone, although the integrated moment is stable. Do not upgrade this to a general nonexistence theorem. Full method, limits, failed attempts and table: research/source_centered_vorticity_transport/RESULTS.md; immutable collection results/strain_collection_20261029T020059.456111Z. The lead's 7.2 strain values may now be tagged as independently reproduced with these qualifications.
'''
for name in ['INDEPENDENT_VALIDATION.md','WORKLOG.md','NOTES_FOR_TEAM.md']:
 with (lane/name).open('a') as f:f.write(short)
p=lane/'research/INDEX.md';s=p.read_text().replace('An independent fast evaluator and manufactured transport tests pass; candidate strain refinement is in progress.','Independent evaluator and transport tests pass; ten candidate runs reproduce negative source strains for the Gaussian-repaired L1/L2 fields. Integrated-moment convergence is supported; global and pointwise derivative certificates remain open.');p.write_text(s)
print(now)
