"""Exact actual-023 shape, two-pole rank witnesses and recorded row history."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from math import comb
import ast,importlib.util,json,re,shlex,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate023_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or h==got,(str(p),h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST_v01.json',prep['manifest_sha256'])
 for name,e in man['files'].items():bind(B/'source'/name,e['sha256'])
 rank=read(R/'research/joint_scaled_rank_peer/verification/result.json');assert rank['verdict'].startswith('CONFIRMED')
 for path,h in rank['inputs'].items():bind(R/path,h)
 for e in rank['frozen_sources'].values():bind(R/e['local'],e['stored_sha256'])
 prior=read(R/'research/candidate016_holdout/verification/result.json','57a7fd0da9db3842f81de94fe3fc3a2d635a765bfd5a12769899b5799050db02');assert prior['status'].startswith('CONFIRMED')
 for path,h in prior['inputs'].items():bind(R/path,h)
 oldaudit=read(R/'research/optimizer_quotient_audit/verification/result.json')
 for path,h in oldaudit['inputs'].items():bind(R/path,h)
 row=next(x for x in oldaudit['rows'] if x['candidate']=='C1-N1-013-pairU-from007')
 assert row['selected_columns']==1922 and row['nonpivot_relations']==0 and sum(b['rank'] for b in row['blocks'])==1922 and row['all_canonical_coefficients_equal'] and row['selected_original_shapes_match'];checks['accepted_old1922_rank_rebound']=True
 old=read(R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json')
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1;d=ds[0];m=read(d/'MANIFEST.json');e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d.name,p,read(p),m
 name,rawp,actual,manifest=raw('023');pn,parentp,parent,pm=raw('016');phasep=bind(B/'source/N1_023_phase1.json','637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb');phase=read(phasep)
 assert sha(rawp)=='d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df' and sha(parentp)=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42' and prior['raw_sha256']==sha(parentp)
 assert actual['cl_exact']==phase['cl_exact']==parent['cl_exact']=='4076476460239181/2251799813685248';checks['same_exact_c']=True
 assert phase['meta']['parent_json']==parentp.name and actual['meta']['parent_json']=='legqs25p100_m9to15_gpu_m16_s12_exact.json';checks['actual_two_phase_lineage']=True
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 olds=list(map(shape,old['generators']));scaled=lambda scale:[(j,m,('legqs',0,N,4,scale)) for j in [1,2,3] for m in range(9,16) for N in range(12)]
 shapes=olds+scaled(25)+scaled(100)
 assert len(olds)==len(set(olds))==1922 and len(shapes)==len(set(shapes))==2426
 assert list(map(shape,parent['generators']))==olds+scaled(25) and list(map(shape,phase['generators']))==list(map(shape,actual['generators']))==shapes;checks['all2426_actual_ordered_shapes']=True
 c=Q(actual['cl_exact']);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)];diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(z.denominator!=1 for z in ps+diffs) and 3+gamma<4
 oldrank=read(R/'research/joint_scaled_density_rank/verification/result.json',rank['own_result_sha256'])
 assert list(map(str,ps))==oldrank['branch_exponents'] and list(map(str,diffs))==oldrank['noninteger_differences'];checks['all36_noninteger_branches_and_growth']=True
 backend=bind(R/'research/joint_scaled_factored_weak/code/fields_joint.py');spec=importlib.util.spec_from_file_location('n4_rank25100_fields',backend);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
 witnesses=[];cross=[]
 for scale,other in [(25,100),(100,25)]:
  a=Q(scale*scale-1);aa=Q(other*other-1);v0=-1/a;crossval=1-aa/a;assert crossval!=0
  cross.append({'scale':scale,'other_scale':other,'pole_v_exact':str(v0),'other_denominator_at_pole_exact':str(crossval),'other_scale_analytic':True})
  for m in range(9,16):
   for N in range(12):
    A=F.generator(m,['legqs',0,N,4,scale]);assert A.powers==tuple(4+N if q==a else 0 for q in F.SCALES)
    expanded=A.numerator_v()(v0)/a**(4+N);formula=Q(scale)**8*v0**4*comb(2*N,N)*(1-v0)**(m+N)/a**(4+N)
    assert expanded==formula and expanded!=0
    witnesses.append({'scale':scale,'m':m,'N':N,'pole_order':4+N,'Laurent_coefficient':str(expanded),'expanded_formula_equal':True})
 assert len(witnesses)==168;checks['all168_actual_Laurent_witnesses']=True;checks['both_other_scale_analytic']=True
 rows=lambda d:[(1,k) if isinstance(k,int) else tuple(k) for k in d['meta']['pair_k']]
 expected=rows(parent);assert len(expected)==len(set(expected))==67 and rows(phase)==rows(actual)==expected and max(n for n,k in expected)==17;checks['same67_rows_both_stages']=True
 script=bind(B/'source/N1_chain023.sh').read_text();tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1)
 def commands(text):
  out=[]
  for line in text.splitlines():
   if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
    tokens=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));out.append(tokens[tokens.index('run_quot.py')+1:])
  return out
 calls=commands(script);assert len(calls)==2
 for i,(call,d,steps,logname) in enumerate(zip(calls,[phase,actual],[12,28],['N1_023_phase1.out','N1_023_phase2.out'],strict=True)):
  callrows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')];assert callrows==expected
  meta=d['meta'];assert Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag']
  assert int(call[1])==meta['angular_midpoint']==180 and int(call[2])==meta['steps']==steps and int(call[5])==meta['middle_order']==16
  assert float(call[4])==meta['hw']==0.952380952380952 and float(call[6])==meta['wlog']==26214400 and float(call[7])==meta['wkap']==3000000 and float(call[8])==meta['wpair']==1e12 and call[10]==meta['pair_mode']=='penalty'
  log=bind(B/'source'/logname).read_text();assert sha(phasep if i==0 else rawp) in log and 'generators 2426' in log and 'pair rows 67 weight 1000000000000.0' in log and 'per-row weights:' not in log
  iterations=[int(v) for v in re.findall(r'^it\s+(\d+) obj ',log,re.M)];assert iterations==list(range(1,steps+1));checks[f'phase{i+1}_all_parameters_and_iterations']=True
 assert phase['meta']['added_legqs']=='1,2,3:9:15:100:12' and actual['meta']['added_legqs'] is None and 'unset IPM_ADD_LEGQS' in script;checks['252_R100_shapes_added_once']=True
 before=bind(R/'research/candidate016_holdout/source/N1_run_quot.py').read_text();after=bind(B/'source/N1_run_quot.py').read_text()
 for text in [before,after]:
  ast.parse(text);assert "PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))" in text and 'pair_k=PAIRK' in text
 impl=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(impl);assert 'for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl;checks['analytic_row_parser_text_only']=True
 reg=read(R/'research/heldout_probe_register/verification/register.json');assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:46:00+00:00')<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'));checks['public25_register_predates_recorded_launch']=True
 probes=[]
 for n,K in reg['pairs']+[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32,128,512]]:
  assert n>17 and n%2 and K>=(n-1)//2 and all(j!=n for j,k in expected)
  probes.append({'n':n,'K':K,'outside_span':True,'all_objective_coefficients_at_n':0,'member_of_25_register':[n,K] in reg['pairs']})
 assert len(probes)==60;checks['all60_outside_analytic_span']=True
 shapep=B/'verification/abstract_shapes.json';save(shapep,{'c_exact':str(c),'generators':[{'j':j,'m':m,'spec':list(s)} for j,m,s in shapes]});bind(shapep)
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'parent016_sha256':sha(parentp),'phase1_sha256':sha(phasep),'generator_count':2426,'potential_dimension':2426,'density_dimension':2426,'old_accepted_rank':1922,'new_shapes_over016':252,'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'cross_pole_analyticity':cross,'Laurent_witnesses':witnesses,'exact_objective_rows':[list(p) for p in expected],'recorded_iterations':[12,28],'accepted_update_count':'Not inferred from iteration count','probe_rows':probes,'registration_utc':reg['utc'],'historical_scope':'007->013->exact quotient->016->023 phase1->023 phase2, recorded stages only','objective_scope':'Complete analytic weak rows, no independence from sampled residual values or unrecorded history','checks':checks,'inputs':inputs,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED own exact finite shape, pole and recorded-span checks; OPEN independent actual25100 rank and history review'}
 save(B/'verification/result.json',out);print(out['utc'],'023_SHAPES',len(shapes),'checks',len(checks),'inputs',len(inputs),'seconds',out['elapsed_seconds'],'sha',sha(B/'verification/result.json'),flush=True)
if __name__=='__main__':main()
