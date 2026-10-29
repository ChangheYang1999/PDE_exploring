from pathlib import Path
from datetime import datetime,timezone
import json,csv,shutil,hashlib
ROOT=Path(__file__).resolve().parent;LANE=ROOT.parent;NUM=LANE.parent/'e4-num/axisymmetric_euler_24h';LEAD=LANE.parent/'e4-lead'
now=datetime.now(timezone.utc);out=LANE/'report_audits'/('failure_narrative_'+now.strftime('%Y%m%dT%H%M%S.%fZ'));out.mkdir()
paths=[NUM/'docs/FAILURE_MAP_NARRATIVE.md',NUM/'FAILURE_MAP.md',NUM/'FAILURE_MAP.csv',NUM/'scripts/failure_map.py',LEAD/'SPEC.md']
hashes={}
for p in paths:
 b=p.read_bytes();(out/p.name).write_bytes(b);hashes[str(p)]=hashlib.sha256(b).hexdigest()
rows=list(csv.DictReader((out/'FAILURE_MAP.csv').open()))
bydevice={}
for r in rows:
 d=r['device'];bydevice.setdefault(d,dict(runs=0,slot_hours=0.));bydevice[d]['runs']+=1;bydevice[d]['slot_hours']+=float(r['gpu_hours'] or 0)
examples=[]
for name in ['p2_cl0p600_ring_core_s1_swirl_lm','p2_cl0p640_poloidal_dominant_s1_swirl_lm','p2_cl0p680_ring_core_s1_swirl_lm','lad2cont_t1lad2_cl0p740_q3p5_freecl_lm','refl_D36_cl0p74_q3p5','refl_D36_cl0p749_q3p5','refl_D48_cl0p749_q3p5','rm5_L1_cl0p749_q3p5']:
 p=NUM/'runs'/name/'validation.json';b=p.read_bytes();(out/(name+'.json')).write_bytes(b);hashes[str(p)]=hashlib.sha256(b).hexdigest();d=json.loads(b)
 rec={k:d[k] for k in ['cl','alpha','a_eff','rho_max','m_max','s_core','s_far','tail_int_F2']};rec['job']=name;rec['dilation']=d['tail_int_F2']**(-d['cl']/2);rec['a_eff_reporting']=d['a_eff']*rec['dilation'];examples.append(rec)
 L=[r for r in rows if r['job_id']==name]
 if L:rec['dominant']={k:L[0][k] for k in ['dominant_eq','dominant_shell','B2']}
result=dict(completed_utc=now.isoformat(),inputs_sha256=hashes,by_device=bydevice,examples=examples)
(out/'evidence.json').write_text(json.dumps(result,indent=2)+'\n')
text=f'''# Audit of the Stage II failure narrative

Date: {now.isoformat()}. The frozen narrative is the draft stamped 02:22Z; all source bytes and hashes are retained here. This is a source and scope audit, not a new residual evaluation.

1. REFUTED: the opening says registered verifier values exist for L0, L1, L2 and L3sep of a q0=3.5 branch. The corrected frozen L0 has q0=2.5 and its all-shell reduced screen is queued. L3sep has a preflight and local/source diagnostics, but its all-shell reduced screen is also queued. Only L1/L2 have complete registered primitive residuals among those four exports. State these statuses separately.
2. REFUTED: 'axis and origin-collar residuals are 1e-3 to 1e-1 ... and do not grow with level.' The frozen L2 registered maximum is rho_Mz=2.9020664015404494 on the origin collar. This is a residual defect, not evidence that the polynomial ball is singular. The L1 Cartesian finite-difference check verifies derivative implementation at sampled points; it does not prove the Euler equation or global C2 matching. The nonzero interface jumps already refute global C2 matching of the piecewise saved fields.
3. REFUTED: a_eff=2.4 to2.9 is labelled 'reporting gauge.' Primary validation stores the working-gauge radius. For frozen L1, primary a_eff=2.6826957952797246 and dilation=0.23592366473498155, so its primary grid gives about0.63291 in reporting units. The independent finer search gives0.6443254856904364. Frozen L2 gives0.59320772226 independently. Convert every radius, including the location of maximum vorticity, by the saved dilation. 'No escape' is OPEN as a global assertion; say no growth was observed on the particular finite chain and test B5 separately.
4. REFUTED: calling each magnitude-filter flag a full B2 pass. SPEC9 requires s_core,s_far>=0.05 AND stability to10percent between levels. The CSV flag checks the first two inequalities only. Independent frozen L1/L2 have s_core=0.59789455/0.67617174, whose change exceeds10percent whether normalized by either value. Label the filter 'swirl magnitude threshold' and assess stability separately. The same correction is needed in F1/F5 captions and titles, and the failure-map definition of a floor should disclose the limited filter.
5. OPEN: 'no growing oscillation' and 'no derivative growth' as unqualified claims. Coefficient envelopes and sampled vorticity can support observations on the saved states. They do not bound all derivatives or exclude unresolved oscillation. Give the actual quantities and finite range.
6. REFUTED as written: 'no level sequence improves.' The quoted q0=3.5 chain2.55/2.33/2.83 improves once; the q0=2.5 chain4.24/2.79/3.37 improves once. Neither shows sustained convergence. The revised F1 title already uses the appropriate qualification.
7. OPEN: 'c_l=2/3 is crossed ... without any feature (to be confirmed at0.65).' The parenthetical marks the relevant continuation as unfinished. Do not report the crossing before that computation; even a sparse completed chain cannot rule out a narrow feature.
8. REFUTED: the blanket claim that Stage I families all end swirl-free or with s_core<0.05 and define no magnitude-filter floor. Counterexamples in the retained primary validation are p2_cl0p600_ring_core_s1_swirl_lm (rho6.86169, s_core0.15954, s_far0.11252), p2_cl0p640_poloidal_dominant_s1_swirl_lm and p2_cl0p680_ring_core_s1_swirl_lm. None is an accepted candidate. The statement about failure to attain B1 is supported.
9. REFUTED: the reflection branch's dominant equation/shell is always eta in k=3,4. The frozen figure audit and current CSV give Mz in shell3 collar for reflection c_l=.74,D36, and eta in shell11collar for reflection c_l=.749,D36/D48. Use the per-run selectors over every point set.
10. REFUTED: 'Total GPU hours ...27.87' includes rows with device=cpu. evidence.json gives independent sums by device of the rounded per-run column. These are slot-hours, not exclusive hardware GPU-hours, and rounded inputs do not support extra precision. Keep GPU and CPU totals distinct and recompute final totals from unrounded run timings.
11. OPEN: 'slave rows met to1e-9 to1e-6' as a statement about these ladder states. The independent mismatch is0.0841368(L1) and0.9997934(L2). Weighted algebraic rows and the physical normalized first correction are different diagnostics. Name the rows, weights and states if retaining the small numbers; the later far-field paragraph correctly states the independent defect.
12. CONFIRMED: the revised interface measure now includes phi derivatives of total order3 and q of order2. Primary64-angle values0.0059/0.0065 versus independent259-angle values0.0060621/0.0068003 are consistent with differing angular grids and fail B4. Keep the 'F5 secondary' tag. Update the earlier failure-map header, which still describes the superseded measure.
13. UPDATE: rm5_L1_cl0p749_q3p5 is now complete with primary rho1.58139877964672,m8.565535593032285,s_core0.7040983641,s_far0.6462717892. It is a newly best primary holdout, not independently validated yet. Export its exact coefficients and sample metadata for independent evaluation. It remains far above B1.

The main failure conclusion survives these repairs: no evaluated state meets the registered acceptance criteria. The finite failures do not establish nonexistence.
'''
(out/'AUDIT.md').write_text(text)
with (LANE/'NOTES_FOR_TEAM.md').open('a') as f:f.write(f'''\n## {now.isoformat()}: narrative audit, corrected figures, new best export needed

The 02:22Z FAILURE_MAP_NARRATIVE draft needs scope and data repairs, documented with frozen evidence in {out.relative_to(LANE)}/AUDIT.md. Highest priority: L0/L3sep registered metrics are not complete; L0 is q0=2.5. L2 origin-collar rho_Mz is2.902, not<=0.1. Primary a_eff and vorticity-peak radii are in working units despite 'reporting gauge' labels. B2flags check magnitude only, not10percent stability (frozen L1/L2 core swirl changes>10percent). StageI 'all s_core<0.05' has explicit pilot2counterexamples. Separate CPU from GPU slot-hours; the27.87total includes CPU. Reflection dominant shells also need correction. Revised SPEC6.5 interface measurements are now consistent with ours and fail B4; thank you for the repair.

F1/F5revision1 scalar audit489PASS with0wrong equation labels. F1still needs its legend outside the axes, separate orange/green D36labels, a lower red D48label, and an inset right-panel level2label. F5is readable, though the outside-target annotation could move to clear the dense endpoint cluster. Change 'B2admissible' to 'swirl-magnitude filter' until cross-level stability is established.

Please export the completed rm5_L1_cl0p749_q3p5 state (primary rho1.5814) to a new immutable candidate directory with coeffs, samples, metadata and basis description. It now deserves independent registered validation before any best-state claim. Do not replace the frozen L1export.
''')
print(out)
print(bydevice)
