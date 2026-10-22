"""Reduce existing independent packet117 artifacts; no solver or NUM code used."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
root=Path(sys.argv[1]);data=json.loads((root/'summary.json').read_text())
local=json.loads((root/'local_jet_certificates/summary.json').read_text())
by={r['state']:r for r in local};now=datetime.now(timezone.utc).isoformat()
rows=[]
for r in data['states']:
    assert r['status']=='COMPLETE'
    path=root/r['state_file'];assert hashlib.sha256(path.read_bytes()).hexdigest()==r['state_sha256']
    q=by[r['state_file']];assert q['source_sha256']==r['state_sha256']
    assert q['nonzero']=={'f0':False,'f1':True,'g0':False,'g1':True}
    t=json.loads((root/(r['label']+'_tail_certificate.json')).read_text())
    assert t['source_sha256']==r['state_sha256']
    for key in ['stream_nonzero','temperature_nonzero','first_ladder_stream_nonzero','first_ladder_temperature_nonzero']:assert not t[key]
    rows.append(dict(label=r['label'],beta=r['beta'],eta=r['eta'],nfev=r['nfev'],objective=r['objective'],
       F=r['heldout']['divided_F']['max_ratio'],G=r['heldout']['divided_G']['max_ratio'],
       absolute_F=r['heldout']['divided_F']['max_absolute'],absolute_G=r['heldout']['divided_G']['max_absolute'],
       absolute_RT=r['heldout']['Cartesian_Theta']['max_absolute'],absolute_RO=r['heldout']['Cartesian_Omega']['max_absolute'],
       f1=q['residual_coefficients_float']['f1'],g1=q['residual_coefficients_float']['g1'],
       sv_min=r['conditioning']['column_normalized_singular_values'][-1],
       rank=r['conditioning']['column_normalized_rank_at_rcond_1e_10'],columns=r['conditioning']['columns']))
text=f"""# Independent first-tail-correction search

Audited {now}. Verdict: REFUTED all twelve stored fields as exact B2 solutions, including locally. No branch exclusion or accepted numerical evidence.

Run: {data['started_utc']} to {data['ended_utc']}, {data['elapsed_seconds']:.9f} seconds. Own stream-function parameterization and Cartesian differential matrices; no NUM code imported or executed. Fixed beta2.2/2.5/2.8 and free beta in[2.02,2.98], initial eta -1/0/1, independent seeded core perturbations, two successive sizes(n,J)=(4,2),(5,3), at most160 function evaluations per fit. The second size starts from its own first-size solution, so these are six lineages, not twelve independent initializations. The budget is a function-evaluation cap, not equal wall time; the two sizes have different parameters and grids.

Exact ordinary rational coefficients are reconstructed from the binary-rational optimizer coordinates. Every file hash was matched to the run record and its separate local/tail certificates. The center values a0=1,c=1+beta/2,b0=4/beta and all four first-tail compatibility polynomials pass exactly. Every state nevertheless has nonzero exact rational x2y and xy coefficients below. That rejects each field without relying on an optimizer flag or a sampling threshold.

| State | beta | eta | evals | objective | max R_F ratio | max R_G ratio | [x2y]R_Theta | [xy]R_Omega |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
"""
for r in rows:text+='| '+r['label']+' | '+' | '.join(f"{r[k]:.12g}"for k in ['beta','eta','nfev','objective','F','G','f1','g1'])+' |\n'
text+='''
Finite-grid absolute maxima, in the order specified by the prompt:

| State | max abs R_Theta | max abs R_Omega | max abs R_F | max abs R_G |
| --- | ---: | ---: | ---: | ---: |
'''
for r in rows:text+='| '+r['label']+' | '+' | '.join(f"{r[k]:.12g}"for k in ['absolute_RT','absolute_RO','absolute_F','absolute_G'])+' |\n'
free=[r for r in data['states']if r['mode']=='free'];maxbd=max(r['beta_bound_distance'][0]for r in free)
text+=f"""
Each held-out grid has {data['states'][0]['heldout_points']} points including the origin, both symmetry-axis rays and off-axis points, with radii1e-5 through1e8. The fit grids differ from this grid. Axis limits use the divided equations. A zero normalizer with zero residual contributes ratio0; a nonzero residual at a zero normalizer contributes infinity. No positive reporting floor is used. Cartesian normalizers vanish identically on the axis, so their ratios do not replace the divided checks. Every divided normalizer in these held-out sets was nonzero. Region and axis tables, peak coordinates, rounded-exact field comparisons and singular values are in summary.json; point arrays are in each heldout.npz.

All six free-beta fits end within {maxbd:.12g} of the lower bound2.02. This does not determine an exponent. Column-normalized smallest singular values range from {min(r['sv_min']for r in rows):.12g} to {max(r['sv_min']for r in rows):.12g}; these are coordinate-dependent finite-grid diagnostics, not operator conditioning or a posteriori bounds. No singularity was inferred from them.

The family has positive local temperature coefficient1 and nonzero vorticity derivative4/beta; the trivial state is excluded exactly. No positivity of the whole fields or a lower bound on amplitudes away from the center is imposed. Measured absolute maxima are sampled values, not full-plane suprema. This experiment supplies only two angular/radial sizes and one fit-domain scheme, so it does not satisfy the prompt's minimum programme for a YES. The separately implemented full-plane inverse had already passed manufactured and real-chart tests on three square/exterior decompositions in packet117, but those controls are not a replacement for a candidate convergence study.

Reproduce search: python3 code_independent/run_first_ladder_search.py ROOT --max-nfev 160. Reproduce exact local certificates: python3 code_independent/stream_local_jet_certificate.py archive ROOT. Reduce: python3 code_independent/summarize_first_ladder_search.py ROOT.

Actual-model collaboration: the original packet117 Opus156 call returned no written audit and is not counted as endorsement. The rejected fields are certified by the independent exact center calculation of packet118. A follow-up with actual Opus5.5 reviews the new six-pivot chart in packet125, which was motivated by this failure; that review does not retroactively validate the fits.
"""
(root/'SUMMARY.md').write_text(text)
(root/'reduction.json').write_text(json.dumps({'utc':now,'verdict':'REFUTED_AS_EXACT_FIELDS','rows':rows,'scope':'no full-class exclusion'},indent=2)+'\n')
inputs=[root/'summary.json',root/'local_jet_certificates/summary.json',Path(__file__),Path('code_independent/stream_local_jet_certificate.py')]+list(root.glob('*_state.json'))+list(root.glob('*_tail_certificate.json'))+list((root/'local_jet_certificates').glob('*_certificate.json'))
(root/'build_inputs.json').write_text(json.dumps({'updated_utc':now,'inputs':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in inputs}},indent=2)+'\n')
print('CONFIRMED reduction',len(rows),'all local fields refuted',now)
