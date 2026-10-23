from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
import hashlib,json
r=Path('research/hydrostatic_axis_core_moment');v=r/'verification'
d=json.loads((v/'CHECKS.json').read_text());q=json.loads((v/'DIRECT_INTEGRAL.json').read_text());ins=json.loads((v/'INPUTS.json').read_text())
checks=[]
def ck(name,test,evidence=None):checks.append({'name':name,'passed':bool(test),'evidence':evidence})
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
ck('main333 allpass',d['status']=='DONE' and len(d['checks'])==333 and all(a['passed'] for a in d['checks']))
ck('direct3manufactures allpass',q['status']=='DONE' and len(q['checks'])==3 and all(a['passed'] for a in q['checks']))
ck('16unique states',len(d['states'])==len({a['tag'] for a in d['states']})==16)
ck('12direct states',len(q['states'])==12)
ck('maincodehash',sha(Path('independent_code/audit_hydrostatic_core_moment.py'))==d['driver_sha256'])
ck('libraryhash',sha(Path('independent_code/hydrostatic_core_moment.py'))==d['library_sha256'])
repair=json.loads((v/'K_SCOPE_REPAIR.json').read_text())
ck('originalproofretained',sha(v/'PROOF.before_K_scope.md')==repair['tested_proof_sha256']==d['proof_sha256'])
ck('currentproofhash',sha(r/'PROOF.md')==repair['current_proof_sha256'])
ck('directproofhash',sha(r/'INTEGRAL_PROOF.md')==q['proof_sha256'])
direct={a['tag']:a for a in q['states']};inputs={a['tag']:a for a in ins['states']};rows=[]
for a in d['states']:
 tag=a['tag'];b=a['values'][-1];x=inputs[tag]
 ck('statehash '+tag,sha(Path(x['frozen']))==x['sha256']==a['source_sha256'])
 ck('polynomialhash '+tag,sha(v/(tag+'.polynomials.json'))==a['polynomial_sha256'])
 ck('positiveK '+tag,Decimal(b['K'])>0)
 ck('precisionretained '+tag,abs(Decimal(a['constant_precision_difference']))<Decimal('1e-55'))
 ck('nonzeror2 '+tag,abs(Decimal(b['r2']))>Decimal('0.001'))
 ck('smallmapmismatch '+tag,abs(Decimal(b['cp_minus1']))<Decimal('1e-14'))
 if a.get('finite_integral_check'):ck('finiteintegral '+tag,abs(Decimal(a['finite_integral_check']['difference']))<Decimal('1e-45'))
 key='m0' if 'm0' in b else 'B_log';constant=float(b[key]);fit=a['producer_fits'].get(key+'_fit')
 row={'tag':tag,'kind':key,'constant':b[key],'r2':b['r2'],'K':b['K'],'cp_minus1':b['cp_minus1'],'source_sha256':a['source_sha256'],'producer_headline_fit':fit,'constant_minus_headline_fit':constant-fit,'max_physical_delta_R_Nf':max(abs(z['delta_R_Nf']) for z in a['physical_refinement'])}
 if tag in direct:
  u=direct[tag];ck('directsourcehash '+tag,u['source_sha256']==a['source_sha256']);row['direct_finest_difference']=u['empirical_finest_difference'];row['direct_level_values']=[z['value'] for z in u['levels']]
 rows.append(row)
summary={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS' if all(a['passed'] for a in checks) else 'FAIL','count':len(checks),'checks':checks,'states':rows,'scope':'Exact algebraic identities; finite multiprecision and quadrature evidence, not interval certification or profile convergence.'}
(v/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Axis core constants: independent results','',f"Summary checked {summary['utc']}. {len(checks)} summary checks pass; the main run has 333 passing checks and the separate direct integral has three passing manufactures.",'','Values below are evaluations for frozen finite trial densities. They are not physical parameter enclosures. The beta finite-part formula was derived independently, with exact rational polynomial reconstruction and two cancellation-aware multiprecision evaluations. Selected states were also checked by an absolutely convergent finite integral. All twelve c=3 states have a separate four-level direct density-curvature integral.','', '| Frozen trial | Constant type | Constant | r2 | Direct integral minus constant |', '|---|---|---:|---:|---:|']
for a in rows:lines.append(f"| {a['tag']} | {a['kind']} | {float(a['constant']):.12g} | {float(a['r2']):.9g} | {format(a['direct_finest_difference'],'.5g') if 'direct_finest_difference' in a else 'not applicable'} |")
lines.extend(['','For 0<p<1/2, m0 is the absolutely convergent moment integral of s*g_xx(0,s)-Q*s^(p-1). For p=1/2, B_log is the exact rational endpoint expression C*(k2-k1/4); a nonzero B_log precludes a finite m0. The coefficient r2 is computed directly from the axis density expansion, not fitted.','', 'The rule lim y*R_h/N_f=m0/6 at c=3 requires K>0, c*p=1 and r2=0. None of the twelve frozen c=3 states has r2=0, including the oversampled states. With the intended exact exponent p=1/3, their uncancelled term contributes [r2/(2K)]y^(1/3). The stored maps also have a nonzero binary discrepancy c*p-1 of about 3e-16; at sufficiently enormous radius that earlier term changes the exact asymptotic again. The proof and output keep the exact map exponent and do not silently assert an infinite-radius law for the rounded map.','', 'The physical curvature comparison uses separately differentiated density jets, composite finite physical intervals and a Gauss-Jacobi integral over the complete tail. Finest absolute discrepancies range from %.3g to %.3g. They are empirical agreement levels, not rigorous bounds. In particular the smallest m0 is not resolved to many relative digits by this double-precision comparison.'%(min(abs(a['direct_finest_difference']) for a in rows if 'direct_finest_difference' in a),max(abs(a['direct_finest_difference']) for a in rows if 'direct_finest_difference' in a)),'', 'The producer headline fits are recorded beside the precise formula evaluations in SUMMARY.json. They are fits on a finite window and can differ from fits on other windows. For c=2 N160 the formula gives B_log=-2816.80743077002, compared with the frozen headline fit -2800.29924711. This is evidence of fit-window error, not a claim that every producer diagnostic used that fit.','', 'The two older linear-reciprocal inverse levels give normalized-axis changes up to %.6g, with the largest changes in c=2 cores. These particular core digits remain unresolved by those levels; result 219 compares another tail variable. The constants above use exact axis polynomials and do not inherit that core-quadrature uncertainty.'%max(a['max_physical_delta_R_Nf'] for a in rows),'', 'Reproduce from this lane with python3 independent_code/audit_hydrostatic_core_moment.py --resume, python3 independent_code/check_hydrostatic_direct_core_integral.py, and python3 independent_code/summarize_hydrostatic_core_moment.py. The first command is substantial and should run alone at nice 19. Original timeout evidence, resume event, inputs, logs and proof-scope repair are retained. The K>0 qualification was made explicit after the original proof was frozen; all sixteen inputs pass the explicit positivity check.','', 'Verdict: CONFIRMED formulas and finite numerical comparisons; REFUTED unconditional m0/6 rule; OPEN profile convergence and the full Setting III endpoint.'])
(v/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print(summary['status'],summary['count']);print('directmax',max(abs(a['direct_finest_difference']) for a in rows if 'direct_finest_difference' in a));print([a for a in checks if not a['passed']])
if summary['status']!='PASS':raise SystemExit(1)
