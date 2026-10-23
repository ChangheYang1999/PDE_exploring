"""Result206 summary of immutable independent outputs; no producer code."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
from decimal import Decimal,localcontext
r=Path('research/hydrostatic_extended_state_audit');v=r/'verification';pipeline=json.loads((v/'PIPELINE.json').read_text());assert pipeline['status']=='DONE'
rows=[];checks=[]
def ck(name,value):checks.append(dict(name=name,passed=bool(value)));assert value,name
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for phase in pipeline['phases']:
 path=Path(phase['result_path']);ck('raw identity '+phase['tag'],sha(path)==phase['result_sha256']);j=json.loads(path.read_text());ck('completed '+j['tag'],j['status']=='DONE')
 ck('state identity '+j['tag'],sha(v/'states'/(j['tag']+'.pt'))==j['source_sha256'])
 ck('common independent sample count '+j['tag'],len(j['samples'])==774)
 q=j['quadrature_comparisons'];ck('three inverse settings '+j['tag'],len(q)==3)
 maps=[{(z['x'],z['y']):z for z in level['points']}for level in q]
 ck('same refinement points '+j['tag'],set(maps[0])==set(maps[1])==set(maps[2]))
 selected={}
 for name,region in j['regions'].items():
  chosen={}
  for norm in ['R','R_Nf','R_Nv']:
   a=region[norm];key=(a['x'],a['y']);levels=[m[key]for m in maps]
   ck('base witness agrees '+j['tag']+name+norm,levels[1]==a)
   chosen[norm]=dict(base=a,levels=levels,last_change={k:abs(levels[-1][k]-levels[-2][k])if levels[-1][k]is not None else None for k in ['V1','V2','R','Nf','Nv','R_Nf','R_Nv']})
  selected[name]=chosen
 mpj=j['mp_jet_checks'];ck('ten MP derivative comparisons '+j['tag'],len(mpj)==10)
 with localcontext()as c:
  c.prec=110;md=max(abs(Decimal(a)-Decimal(b))/(1+abs(Decimal(b)))for a0,b0 in zip(mpj[:5],mpj[5:])for a,b in zip(a0['values'],b0['values']))
 ck('same MP coordinates '+j['tag'],all(a['point']==b['point']for a,b in zip(mpj[:5],mpj[5:])))
 ck('MP precisions agree '+j['tag'],md<Decimal('1e-68'))
 ex={k:z for k,z in j['exact'].items()if k not in ['cH','delta','a']}
 rows.append(dict(tag=j['tag'],source_sha256=j['source_sha256'],result_path=str(path),result_sha256=sha(path),cl=j['metadata']['cl'],N=j['metadata']['N'],M=j['metadata']['M'],exact=ex,node_reconstruction=j['node_reconstruction'],selected_witnesses=selected,inverse_center_errors=[x['center_error']for x in q],finite_radius_identity=[x['finite_R_identity']for x in q],mp_max_scaled_precision_change=str(md),mp_max_absolute_double_jet_error=max(max(x['absolute_double_errors'])for x in mpj),axis_derivative_samples=j['axis_derivative_samples'],sampled_region_counts={k:dict(count=z['count'],undefined_Nf=z['undefined_Nf'],undefined_Nv=z['undefined_Nv'])for k,z in j['regions'].items()}))
report=dict(utc=datetime.now(timezone.utc).isoformat(),status='DONE',verdict='CONFIRMED for exact center and recorded finite comparisons; OPEN for a converged residual evaluator at every displayed sample and for convergence of these trial states.',checks=checks,check_count=len(checks),states=rows,scope='The base grid uses (20,112,64). Fine values are re-evaluations of base maxima, not maxima on a fully refined grid. Last changes are observations, not rigorous bounds. Three extents:10,100,10000. Original IPM endpoint remains UNRESOLVED.',pipeline_sha256=sha(v/'PIPELINE.json'),code_sha256=sha(__file__))
(v/'SUMMARY.json').write_text(json.dumps(report,indent=2)+'\n')
text=['# Ten additional hydrostatic trial states',report['utc'],'','CONFIRMED: source identities, reconstruction, exact center functional and recorded finite comparisons. OPEN: a converged evaluator at every sample and convergence of these trial states. This is the hydrostatic limit, not an original IPM candidate.','', 'R=(c x+V1)g_x+(c y+V2)g_y-g. Nf is the sum of the absolute values of the two displayed transport terms and g. Nv=|g|+|xg_x+yg_y|+|V1g_x+V2g_y|. Undefined ratios at zero denominators are retained.','', '| state | exact c+cH-1 | B | E=e/a | annulus fine NF witness | change from base | far fine NF witness | change from base |', '|---|---:|---:|---:|---:|---:|---:|---:|']
for z in rows:
 a=z['selected_witnesses']['annulus']['R_Nf'];f=z['selected_witnesses']['far']['R_Nf'];e=z['exact'];text.append(f"|{z['tag']}|{e['delta_float']:+.5e}|{float(e['b']):.7g}|{float(e['E']):.7g}|{a['levels'][-1]['R_Nf']:.7g}|{a['last_change']['R_Nf']:.3g}|{f['levels'][-1]['R_Nf']:.7g}|{f['last_change']['R_Nf']:.3g}|")
text+=['','These are selected physical points from the unchanged 774-point grid, with extents 10,100,10000. Each witness was recomputed at (finite order,tail order,split factor)=(14,64,16),(20,112,64),(28,192,256). The last column changes are not error enclosures. Fine values are not claimed as full fine-grid maxima. Absolute residuals, both denominators and every coordinate are retained in SUMMARY.json and the raw outputs.','', 'The c=1.5,N96 annulus witness changes substantially under inverse refinement. All c=1.5 center quadratures remain poorly resolved, and several c=2 center/core values also need further inverse refinement. Thus their base core or annulus maxima must not be quoted as accurate canonical maxima. By contrast the displayed far witnesses and the c=3 annulus witnesses are much more stable. The exact center functional is independent of this vertical quadrature and remains valid.','', '|state| center inverse error, coarse / base / fine | max absolute double jet error versus MP |','|---|---:|---:|']
for z in rows:text.append('|'+z['tag']+'|'+' / '.join(f'{x:.3g}'for x in z['inverse_center_errors'])+f"|{z['mp_max_absolute_double_jet_error']:.3g}|")
text+=['','The two MP precision levels are70 and100 target digits, with extra guards for the exact polynomial conversion. The largest scaled discrepancy between those levels is '+str(max(Decimal(z['mp_max_scaled_precision_change'])for z in rows))+'. This checks density derivatives at the selected points; it does not certify the velocity quadrature.','', 'Every exact center defect is nonzero for the stored binary input. The exact-row states have defects about-7.70e-9 and-9.04e-10. These facts exclude exact transport for those specific finite files, not an exact solution near them. Their cubic coefficients and residuals still move under refinement. No convergence is established.','', 'The c=2,N128 input is the40-iteration capped checkpoint, SHA25653b3ea34341c42220f01b7b933164b8753dbf7674fa0e8825e09be1ef42e2554. It is neither the later continued state nor an established stall. Later N128 continuation and N160 states require separate input freezes and evaluations.','',str(len(checks))+' integrity/comparison checks pass. Reproduce with independent_code/run_hydrostatic_extended_state_audit.py after its gate, then independent_code/summarize_hydrostatic_extended_states.py. See PROOF.md for the complete operator and scope.']
(v/'SUMMARY.md').write_text('\n'.join(text)+'\n');print(report['utc'],len(checks),'PASS',len(rows),'states')
