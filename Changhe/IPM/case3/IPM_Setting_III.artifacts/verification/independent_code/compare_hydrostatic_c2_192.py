from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,math
from fractions import Fraction
import sys
sys.set_int_max_str_digits(0)
R=Path('research/hydrostatic_c2_resolved_192_audit');V=R/'verification';checks=[];rows=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
for row in json.loads((V/'COMPARISON_INPUTS.json').read_text())['files']:ck('frozen '+row['path'],sha(row['path'])==row['sha256'])
sources=[('hydrostatic_c2_resolved_audit','hsG_c2.0_N96_log','prior235_SUMMARY.json'),('hydrostatic_c2_resolved_audit','hsG_c2.0_N128_log','prior235_SUMMARY.json'),('hydrostatic_c2_continuation_audit','hsG_c2.0_N128_log_cont','prior238_SUMMARY.json'),('hydrostatic_c2_resolved_160_audit','hsG_c2.0_N160_log','prior242_SUMMARY.json'),('hydrostatic_c2_resolved_192_audit','hsG_c2.0_N192_log','SUMMARY.json')]
coord=None
for dirname,tag,sf in sources:
 base=Path('research')/dirname/'verification';summary=json.loads((V/sf).read_text());state=next(s for s in summary['states']if s['tag']==tag);raw=json.loads((base/(tag+'.json')).read_text())
 ck(tag+' summary gate',summary['status']=='PASS'and summary['count']==(246 if sf=='prior235_SUMMARY.json' else 134))
 ck(tag+' all summary checks',all(c['passed']for c in summary['checks']))
 p=raw['levels'][-1]['points'];here=[(a['x'],a['y'])for a in p]
 if coord is None:coord=here
 ck(tag+' identical774points',here==coord and len(here)==774)
 ck(tag+' same complete inverse rule',[(r['order'],r['tail_order'],r['split'])for r in raw['levels']]==[(32,96,16),(48,160,64),(64,192,128)])
 chosen=[a for a in p if math.hypot(a['x'],a['y'])<10000.000001]
 maxima={k:max((a for a in chosen if a[k] is not None),key=lambda a:abs(a[k]))for k in ['R','R_Nf','R_Nv']}
 for k in maxima:ck(tag+' recomputed maximum '+k,maxima[k]==state['levels'][-1]['regions']['extent10000'][k])
 ck(tag+' nonzero center defect',state['delta']!=0 and state['a']!=0)
 f=state['far']['values'];ck(tag+' exact intended exponent',float(f['cp_minus1'])==0)
 ck(tag+' nonzero raw axis limit',float(f['r2'])!=0)
 rows.append(dict(tag=tag,source_sha256=state['source_sha256'],summary_sha256=sha(V/sf),raw_sha256=sha(base/(tag+'.json')),delta=state['delta'],b=state['b'],E=state['E'],b_minus_6E=state['b']-6*state['E'],Q=f['Q'],B_log=f['B_log'],Cp_K=state['cusp']['Cp_K'],r2=f['r2'],maxima={k:abs(maxima[k][k])for k in maxima},locations={k:[maxima[k]['x'],maxima[k]['y']]for k in maxima}))
cert=json.loads((V/'hsG_c2.0_N192_log.polynomials.json').read_text());cf=lambda x:Fraction(int(x[0]),int(x[1]));C=cf(cert['L'])/4;h1,h2=map(cf,cert['H_w'][1:3]);k1=cf(cert['k_w'][1]);exact_r2=C*(-h2+h1/4+h1*k1);ck('exact rational axis residual limit nonzero',exact_r2!=0 and exact_r2<0);ck('exact axis limit value agrees summary',abs(float(exact_r2)-float(state['far']['values']['r2']))<1e-14)
latest=state;prior=rows[-2];ratios={r['tag']:{k:rows[-1]['maxima'][k]/r['maxima'][k]for k in ['R','R_Nf','R_Nv']}for r in rows[:-1]}
log=(V/'producer_hsG_c2.0_N192_log.log').read_text();results=re.findall(r'^# RESULT (.+)$',log,re.M);ck('one producer result',len(results)==1);result=json.loads(results[0])
steps=re.findall(r'^  it (\d+): \|F\|2 ([^ ]+) \|F\|max ([^ ]+) lam ([^ ]+)',log,re.M)
ck('accepted numbered lines0to68',[int(r[0])for r in steps]==list(range(69)));ck('positive accepted lambdas',all(float(r[3])>0 for r in steps));ck('failure at69','it 69: line search failed (lam 9.3e-10); stop'in log)
ck('F2 at62',float(steps[62][1])==1.999e-6);ck('F2 from63to68',all(float(r[1])==1.998e-6 for r in steps[63:]));ck('not iteration80cap','maxit' in log and "'maxit': '80'"in log and len(steps)<80)
ck('source fixed c2',result['c']==2 and result['cfree']is False);ck('source center dropped',result['centre']=='drop'and result['centre_row_defect']is None)
comparisons={}
for key,own in [('a0',latest['a']),('E',latest['E']),('B',latest['b']),('K',float(latest['far']['values']['K'])),('cH',latest['cH']),('centre_defect_single',latest['delta'])]:
 err=abs(result[key]-own);comparisons[key]=dict(source=result[key],independent=own,absolute_error=err);ck('source reconstructed '+key,err<1e-11,err)
fd_error=abs(result['cH_fd_row']-latest['cH']);ck('descriptive saved FD row error window',3.2e-8<fd_error<3.3e-8,fd_error)
ck('node loss below2e-7',result['nodes_Fmax']<2e-7);ck('independent residual exceeds1e-6',rows[-1]['maxima']['R_Nf']>1e-6);ck('center defect exceeds1e-6',abs(latest['delta'])>1e-6)
harvest=(V/'producer_harvest_N192.txt').read_text();exact_match=re.search(r'D_exact ([+-]?[\deE.+-]+)',harvest);ck('harvest exact center',abs(float(exact_match[1])-latest['delta'])<2e-14)
cptext=harvest.split('||',1)[1].split('\n',1)[0];cpcut=[float(z)for z in re.findall(r'[+-]\d+\.\d+e[+-]\d+',cptext)];ck('four cutoff values and repeatedlast',len(cpcut)==5 and cpcut[-1]==cpcut[-2]);cp=float(latest['cusp']['Cp_K']);errs=[abs(x-cp)for x in cpcut[:4]];ck('cutoff Cp errors decrease',all(x>y for x,y in zip(errs,errs[1:])),errs);ck('descriptive last-cutoff error window',1e-6<errs[-1]<2e-6,errs[-1])
blog=float(re.search(r'B_log ([+-]\d+\.\d+)',harvest)[1]);ck('descriptive rough-Blog error window',3<abs(blog-float(latest['far']['values']['B_log']))<4)
axisvals=[float(z)for z in re.search(r'meas ([^\n]+)',harvest)[1].split(' / ')];axown=[float(t['y_signed_R_Nf'])for t in latest['axis_points']if float(t['y'])in[1e4,1e6,1e8]];ck('three far-axis source measurements',len(axisvals)==len(axown)==3 and max(abs(a-b)for a,b in zip(axisvals,axown))<1e-7)
checkerrors=[abs(result['axis'][key]-latest['delta'])for key in ['centre_defect_R1','centre_defect_R10','centre_defect_R100']];ck('recorded producer finite-radius errors exceed1e-5',min(checkerrors)>1e-5,checkerrors)
ck('source regional maxima retained as separategrid',len(result['sampled'])==4 and result['sampled'][3][3]>rows[-1]['maxima']['R_Nf'])
z=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,N192_to_prior_ratios=ratios,axis_limit_exact_nonzero=dict(sign=-1,numerator_bits=abs(exact_r2.numerator).bit_length(),denominator_bits=exact_r2.denominator.bit_length()),producer_record=dict(accepted_line_indices=[0,68],accepted_line_count=69,failed_index=69,comparisons=comparisons,saved_FD_row_error=fd_error,recorded_nodes_Fmax=result['nodes_Fmax'],recorded_nodes_F2=result['nodes_F2'],regional_source_grid=result['sampled'],cutoff_Cp_K=cpcut[:4],cutoff_Cp_errors=errs,rough_Blog=blog,exact_Blog=float(latest['far']['values']['B_log']),finite_radius_center_errors=checkerrors,scope='optimizer history, source grid extrema and runtime are recorded claims; no optimizer rerun or shared-grid comparison is implied'),proof_sha256=sha(R/'COMPARISON_PROOF.md'),driver_sha256=sha(__file__))
(V/'COMPARISON.json').write_text(json.dumps(z,indent=2)+'\n');print(z['status'],z['count']);print('N192toN160',ratios[prior['tag']]);print([c for c in checks if not c['passed']]);raise SystemExit(z['status']!='PASS')
