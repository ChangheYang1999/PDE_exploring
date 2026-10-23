"""Summarize completed second-inverse witnesses; no new field evaluations."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import mpmath as mp
V=Path('research/hydrostatic_axis_primitive/verification');B=Path('research/hydrostatic_state_audit/verification')
tags=['hsA_c3.0_N48','hsA_c3.0_N64','hsA_c3.0_N96','hsA_c3.0_N128'];rows=[];sources=[]
mp.mp.dps=130
for tag in tags:
 d=json.loads((V/(tag+'.json')).read_text());base=json.loads((B/(tag+'.json')).read_text());assert d['status']=='DONE';sources.extend([V/(tag+'.json'),V/(tag+'.polynomial.json'),B/(tag+'.json')])
 for p in d['points']:
  val=p['refinements'][-1]['values'];r=dict(tag=tag,region=p['source_region'],x=0,y=p['y'],exact_center_defect=base['exact']['delta_float'],values=val,differences=p['refinement_differences'],primary_differences=p['primary_differences']);rows.append(r)
maxdiff={key:{which:str(max(mp.mpf(r['differences'][key][which])for r in rows))for which in ['order24_40','order40_56']}for key in ['V2','R','R_Nf','R_Nv']}
maxprimary={key:str(max(mp.mpf(r['primary_differences'][key])for r in rows))for key in ['g','gy','V2','R','R_Nf','R_Nv']}
now=datetime.now(timezone.utc).isoformat();out=dict(utc=now,status='CONFIRMED finite axis witnesses',count=len(rows),rows=rows,max_refinement_differences=maxdiff,max_primary_differences=maxprimary,scope='Hydrostatic trial densities only. Finite sampled witnesses, not uniform maxima or interval enclosures. Original IPM endpoint remains UNRESOLVED.')
(V/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
s=['# Independent hydrostatic axis witnesses','',f'Completed {now}. CONFIRMED for the frozen finite inputs below; original Setting III remains UNRESOLVED.','', 'The second inverse uses an exact rational polynomial for V2_y, including its full-tail endpoint, and a finite physical integral from0 to y. It does not use the producer inverse or its numerical second derivatives. The first inverse uses analytic Cartesian derivatives and independent full-line quadrature. These samples were chosen from the first evaluator’s regional maxima; they are witnesses, not newly established uniform maxima.','', '| State | Region | y | R | Nf | Nv | abs(R)/Nf | abs(R)/Nv |','|---|---|---:|---:|---:|---:|---:|---:|']
for r in rows:
 v=r['values'];s.append('| '+r['tag']+' | '+r['region']+' | '+format(r['y'],'.12g')+' | '+' | '.join(mp.nstr(mp.mpf(v[k]),12)for k in ['R','Nf','Nv','R_Nf','R_Nv'])+' |')
s.extend(['','All four states have ell=3. Their exact first-order center defects ell+cH-1 are, in increasing N: +0.0003395003567235288, -0.00029093223108537456, -0.00001778572829210397 and +0.00001026138567754309. The N128 core peak is off axis, so this table makes no second-inverse claim for that peak.','',f'The maximum difference between the40 and56 point multiprecision rules is {mp.nstr(mp.mpf(maxdiff["R_Nf"]["order40_56"]),7)} in abs(R)/Nf and {mp.nstr(mp.mpf(maxdiff["V2"]["order40_56"]),7)} in V2. The largest difference from the original full-line rule is {mp.nstr(mp.mpf(maxprimary["R_Nf"]),7)} in abs(R)/Nf and {mp.nstr(mp.mpf(maxprimary["V2"]),7)} in V2. These are observed differences, not rigorous error bounds. Every numerator and denominator, precision, quadrature order, comparison and source hash is in SUMMARY.json and the per-state JSON.','', 'The manufactured gate has108 passing checks. Its two earlier failures were retained: the initial full-line comparator converged slowly for the P=3 tail. Moving the split while continuing to integrate the entire exterior resolved those tests. The exact polynomial primitive itself was unchanged. This makes explicit why a short-tail comparison alone was inadequate.','', 'Reconstruction metadata for these four states is confirmed against the producer’s later explicit-node export by result187/METADATA_RECHECK.json. All coefficients and nodes are unchanged. A nonzero residual here concerns a finite hydrostatic trial only; it excludes neither hydrostatic nor original profiles.'])
(V/'SUMMARY.md').write_text('\n'.join(s)+'\n')
manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),V.parent/'PROOF.md',V/'GATE.json',V/'SUMMARY.json',V/'SUMMARY.md',*sources]};(V/'SUMMARY_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('COMPLETE',len(rows),'axis witnesses',now);print('max refinements',maxdiff);print('max first-inverse difference',maxprimary)
