from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from datetime import datetime,timezone
from math import comb
import json,hashlib,time
B=Path(__file__).resolve().parents[1];started=time.monotonic();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
def ck(s,t):
 assert t,s
 checks.append(s)
m=json.loads((B/'data/manifest.json').read_text());ck('proof hash',sha(B/'PROOF.md')==m['proof_sha256'])
for rel,h in m['inputs'].items():ck('input '+rel,sha(B/rel)==h)
p=json.loads((B/'source/peer_result.json').read_text());n=json.loads((B/'source/N4_result.json').read_text());t=json.loads((B/'source/436_result.json').read_text());a=json.loads((B/'source/source_attestation.json').read_text())
ck('attestation202',a['all_pass'] and len(a['bindings'])==202 and a['peer_result_sha256']==sha(B/'source/peer_result.json'))
ck('24 peer checks',len(p['checks'])==p['check_count']==24 and all(p['checks'].values()))
ck('15 independent N4 checks',len(n['checks'])==15 and all(n['checks'].values()))
ck('554 original checks',len(t['checks'])==t['check_count']==554)
for filename in ['peer_PROOF.md','peer_check.py','N4_result.json','N4_check.py']:ck('peer own binds '+filename,sha(B/'source'/filename) in p['own_inputs'].values())
for filename in ['436_PROOF.md','436_check.py','436_result.json']:ck('peer binds '+filename,sha(B/'source'/filename) in p['peer_input_bindings'].values())
ck('raw identity',p['raw_sha256']==n['raw_sha256']==t['raw_sha256']=='3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17')
ck('dimensions',p['potential_dimension']==p['density_dimension']==n['potential_dimension']==n['density_dimension']==t['potential_dimension']==t['density_dimension']==2918)
ck('36 conditions',n['branch_exponents']==t['branch_exponents'] and n['noninteger_differences']==t['noninteger_differences'] and len(n['branch_exponents'])+len(n['noninteger_differences'])==36 and all(Q(x).denominator!=1 for x in n['branch_exponents']+n['noninteger_differences']))
pw={(x['scale'],x['m'],x['N']):Q(x['coefficient']) for x in p['Laurent_witnesses']};nw={(x['scale'],x['m'],x['N']):Q(x['Laurent_coefficient']) for x in n['Laurent_witnesses']};tw={(x['scale'],x['m'],x['N']):Q(x['coefficient']) for x in t['Laurent_witnesses']}
ck('348 unique entries',len(pw)==len(nw)==len(tw)==348 and pw.keys()==nw.keys()==tw.keys())
for (R,mode,N),value in pw.items():
 v=Q(-1,R*R-1);z=R**8*v**4*comb(2*N,N)*(1-v)**(mode+N)/(R*R-1)**(4+N)
 ck('Laurent '+str((R,mode,N)),z==value==nw[R,mode,N]==tw[R,mode,N] and z!=0)
ck('same six poles',p['cross_poles']==t['cross_poles'] and len(p['cross_poles'])==6)
for w in p['cross_poles']:ck('cross '+str((w['scale'],w['other_scale'])),Q(w['other_denominator'])==1-Q(w['other_scale']**2-1,w['scale']**2-1)!=0)
ck('81 ordered rows',p['current_rows']==n['exact_objective_rows']==t['exact_objective_rows'] and len(p['current_rows'])==81)
ck('81 split weights',p['objective_weights_exact']==n['objective_weights_exact']==t['objective_weights_exact']==[str(10**12)]*67+[str(10**16)]*14)
ck('46 probes',p['outside_current_analytic_span']==sorted(t['outside_analytic_span'])==sorted([[w['n'],w['K']] for w in n['probe_rows']]) and len(p['outside_current_analytic_span'])==46)
ck('60 iteration flags',p['recorded_iterations']==[[w['i'],w['flag']] for w in t['iterations']] and len(p['recorded_iterations'])==60)
trans=[{('objective_before' if k=='before' else 'objective_proposal' if k=='proposal' else k):v for k,v in w.items()} for w in t['iterations']]
ck('60 complete iteration records',trans==n['iterations'])
steps=[Decimal(w['dRho2']) for w in t['iterations'] if w['flag']=='ACC']
ck('FLOAT sum',len(steps)==39 and str(sum(steps,Decimal(0)))==t['FLOAT_sum_accepted_rounded_mesh_steps']==n['FLOAT_sum_accepted_rounded_mesh_steps']=='0.08387595')
source=(B/'source/N1_ipm_opt3.py').read_text();launch=(B/'source/N1_run_quot.py').read_text()
ck('initial projection precedes optimization',launch.index('a_start = prob.taylor_project')<launch.index('a = prob.optimize2(a_start'))
ck('perstep projection precedes norm',source.index('if taylor: a_new = self.taylor_project(a_new)')<source.index("drho = self.fields(a_new - a)[('rho', (0, 0))]"))
ck('exact conversion follows optimization',launch.index('a_exact, piv = OPT.finalize_exact')>launch.index('a = prob.optimize2(a_start'))
ck('old scope needs qualifier','projection, exact conversion and integration error excluded' in t['step_scope'] and 'only initial projection' in p['literal_step_scope_qualification'])
res={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-started,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'raw_sha256':p['raw_sha256'],'witness_count':348,'attested_source_hashes':202,'foreign_code_executed':False,'verdict':'CONFIRMED reciprocal structural comparison; only initial projection is absent from recorded step sums; no certified density-distance bound'}
(B/'verification/result.json').write_text(json.dumps(res,indent=2)+'\n');print('PASS',len(checks),res['utc'],res['elapsed_s'])
