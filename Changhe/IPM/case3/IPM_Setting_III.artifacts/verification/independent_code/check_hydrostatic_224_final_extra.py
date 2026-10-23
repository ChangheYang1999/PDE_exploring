"""Final extra N224 evidence and model-review clarification checks."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,subprocess,gmpy2
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);v=sha(p);ck('binding '+str(p),h is None or v==h);bindings[str(p)]=v
for p in [Path(__file__),R/'FINAL_RESULTS_REVIEW_RESOLUTION_PROOF.md',V/'RESULTS_SUPPLEMENT.json',V/'hsG_c2.0_N224_log.json',V/'summary_timeout_60.json',Path('independent_code/run_224_summary_then_degree23.py'),Path('research/degree23_grouped_moment_obstruction/verification/SUPERVISOR_RETIREMENT.json')]:bind(p)
d=json.loads((V/'RESULTS_SUPPLEMENT.json').read_text());ck('161supplement separate',d['status']=='PASS_FINITE_RESULTS_SUPPLEMENT'and d['count']==161==len(d['checks'])and all(x['passed']for x in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
a=json.loads((V/'hsG_c2.0_N224_log.json').read_text());sets=[{(p['x'],p['y'])for p in l['points']}for l in a['levels']];ck('same774coordinates',all(s==sets[0]and len(s)==774 for s in sets));w={(p['x'],p['y'])for p in a['witnesses']['points']};shared=w&sets[0];ck('13shared and originextra',len(shared)==13 and w-sets[0]=={(0.,0.)});ck('72maximizer records',len(d['witness_mapping'])==72)
for j,row in enumerate(d['witness_mapping']):ck('maximizer in13shared '+str(j),tuple(row['point'])in shared)
o=next(p for p in a['witnesses']['points']if p['x']==p['y']==0);ck('origin checks null ratios',all(o[k]==0 for k in ['g','R','Nf','Nv'])and o['R_Nf']is None and o['R_Nv']is None)
ch=gmpy2.mpq(a['exact']['cH']);delta=gmpy2.mpq(a['exact']['delta']);ck('exact center identity and negative nonzero',delta==1+ch and -1<delta<0);descriptor=dict(file=str(V/'hsG_c2.0_N224_log.json'),file_sha256=sha(V/'hsG_c2.0_N224_log.json'),json_pointer='/exact/delta',characters=len(a['exact']['delta']),value_string_sha256=hashlib.sha256(a['exact']['delta'].encode()).hexdigest(),exact_relation='delta=1+cH; -1<delta<0',duplicate_large_rational_not_required=True);ck('published exact rational full string',descriptor['characters']==313727 and '/'in a['exact']['delta'])
ck('distinct derivative sample range',a['axis_derivative_samples']['count']==2001 and a['axis_derivative_samples']['range']==[1e-7,1e6]);src=Path('independent_code/audit_hydrostatic_c2_resolved_224.py').read_text();tree=ast.parse(src);ck('source derivative sample and Cartesian jets',all(s in src for s in ['yy=np.geomspace(1e-7,1e6,2001)','ax=jet.jet(0.,yy)','xx=jet.jet(yy,0.)']))
tree=ast.parse(Path('independent_code/run_224_summary_then_degree23.py').read_text());sequences=[n for n in ast.walk(tree)if isinstance(n,ast.List)];ck('successful retry recorded10minute limit',any(len(n.elts)>=2 and all(isinstance(t,ast.Constant)for t in n.elts[:2])and[n.elts[0].value,n.elts[1].value]==['timeout','10m']for n in sequences));ck('earlier attempt exit124',json.loads((V/'summary_timeout_60.json').read_text())['returncode']==124)
record=json.loads(Path('research/degree23_grouped_moment_obstruction/verification/SUPERVISOR_RETIREMENT.json').read_text());ck('onlytwoidle supervisors retired',record['retired_supervisors']==[632053,647414]and record['preserved_compute_pid']==651441);ps=subprocess.run(['ps','-p','651441','-o','pid,ppid,stat,etime,time,ni,rss,args'],capture_output=True,text=True);observation=dict(utc=datetime.now(timezone.utc).isoformat(),ps_output=ps.stdout,returncode=ps.returncode,scope='Current observation only. Degree23 not accepted in289; no claim that a live output is final.');ck('own pending computation observation',ps.returncode==0 and 'check_degree23_outer.py'in ps.stdout and '/proc/651441/cwd' and Path('/proc/651441/cwd').resolve()==Path.cwd())
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_FINAL_EXTRA_FINITE_SCOPE',count=len(checks),checks=checks,bindings=bindings,exact_delta=descriptor,process_observation=observation,scope='Additional closure bookkeeping and exact center sign; no degree23 theorem, true inverse error or primary endpoint.')
(V/'FINAL_EXTRA.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
