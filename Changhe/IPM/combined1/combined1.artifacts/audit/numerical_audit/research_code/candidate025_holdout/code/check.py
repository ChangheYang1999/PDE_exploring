"""Exact actual-025 shapes, three-pole rank witnesses and recorded row history."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
from decimal import Decimal
from math import comb
import ast,importlib.util,json,re,shlex,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate025_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or h==got,(str(p),h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST_v01.json',prep['source_manifest_sha256'])
 for path,e in man['files'].items():bind(R/path,e['sha256'])
 prior=read(R/'research/candidate016_holdout/verification/result.json','57a7fd0da9db3842f81de94fe3fc3a2d635a765bfd5a12769899b5799050db02');assert prior['status'].startswith('CONFIRMED')
 for path,h in prior['inputs'].items():bind(R/path,h)
 accepted=read(R/'research/candidate023_shape_peer/verification/result.json','b9f961dd801661a02048d092b6c13d029ef588be8f89aa51aad7034ccde78d96');assert accepted['verdict'].startswith('CONFIRMED')
 for path,h in accepted['own_inputs'].items():bind(R/path,h)
 for path,e in accepted['frozen_or_retained_sources'].items():bind(R/path,e['stored_sha256'])
 oldaudit=read(R/'research/optimizer_quotient_audit/verification/result.json')
 for path,h in oldaudit['inputs'].items():bind(R/path,h)
 row=next(x for x in oldaudit['rows'] if x['candidate']=='C1-N1-013-pairU-from007')
 assert row['selected_columns']==1922 and row['nonpivot_relations']==0 and sum(b['rank'] for b in row['blocks'])==1922 and row['all_canonical_coefficients_equal'] and row['selected_original_shapes_match'];checks['accepted_old1922_rank_rebound']=True
 old=read(R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json','c0d3536ea961908a8a4d251054192bad0b5b2534435e3c8224fe0424bda5f7fe')
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1
  d=ds[0];m=read(d/'MANIFEST.json');e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d,p,read(p),m
 d,rawp,actual,manifest=raw('025');pd,parentp,parent,pm=raw('016')
 assert d.name==manifest['id']=='C1-N1-025-combined-heldin1e16' and sha(parentp)==prior['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 snap=read(B/'verification/SNAPSHOT.json');assert snap['candidate']==d.name and snap['raw_sha256']==sha(rawp)
 sumrecords=[]
 for line in bind(d/'SHA256SUMS').read_text().splitlines():
  h,name=line.split(maxsplit=1);name=name.strip().lstrip('*');assert Path(name).name==name;bind(d/name,h);sumrecords.append({'file':name,'sha256':h})
 checks['all_snapshot_SHA256SUMS']=True
 assert actual['cl_exact']==parent['cl_exact']==old['cl_exact']=='4076476460239181/2251799813685248';checks['same_exact_c']=True
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 olds=list(map(shape,old['generators']));scaled=lambda scale:[(j,m,('legqs',0,N,4,scale)) for j in [1,2,3] for m in range(9,16) for N in range(12)]
 high=[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(16,20 if j==1 else 24) for N in range(12)]
 shapes=olds+scaled(25)+scaled(50)+scaled(100)+high
 assert len(olds)==len(set(olds))==1922 and len(high)==240 and len(shapes)==len(set(shapes))==2918
 assert list(map(shape,parent['generators']))==olds+scaled(25) and list(map(shape,actual['generators']))==shapes;checks['all2918_actual_ordered_shapes']=True
 assert actual['n_free']==manifest['basis']['generator_count']==2918 and actual['n_fixed']==0
 for g in actual['generators']:Fraction(g['coef'])
 checks['all_coefficients_exact_rational']=True
 assert actual['meta']['parent_json']==parentp.name and actual['meta']['added_legqs']=='1,2,3:9:15:50:12;1,2,3:9:15:100:12;1,2,3:16:23:25:12';checks['immediate016_input_and744_additions']=True
 c=Q(actual['cl_exact']);gamma=1/c;delta=1-gamma;ps=[(3+gamma-j*delta)/2 for j in range(8)];diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(z.denominator!=1 for z in ps+diffs) and 3+gamma<4;checks['all36_noninteger_branches_and_growth']=True
 backend=bind(R/'research/joint_scaled_factored_weak/code/fields_joint.py');spec=importlib.util.spec_from_file_location('n4_rank_three_scales',backend);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
 witnesses=[];cross=[]
 for scale in [25,50,100]:
  a=Q(scale*scale-1);v0=-1/a
  for other in [r for r in [25,50,100] if r!=scale]:
   aa=Q(other*other-1);value=1-aa/a;assert value!=0
   cross.append({'scale':scale,'other_scale':other,'pole_v_exact':str(v0),'other_denominator_at_pole_exact':str(value),'other_scale_analytic':True})
  for m,N in sorted({(m,s[2]) for j,m,s in shapes if s[0]=='legqs' and s[4]==scale}):
   A=F.generator(m,['legqs',0,N,4,scale]);assert A.powers==tuple(4+N if q==a else 0 for q in F.SCALES)
   expanded=A.numerator_v()(v0)/a**(4+N);formula=Q(scale)**8*v0**4*comb(2*N,N)*(1-v0)**(m+N)/a**(4+N)
   assert expanded==formula and expanded!=0
   witnesses.append({'scale':scale,'m':m,'N':N,'pole_order':4+N,'Laurent_coefficient':str(expanded),'expanded_formula_equal':True})
 assert len(witnesses)==348 and len(cross)==6;checks['all348_actual_Laurent_witnesses']=True;checks['six_cross_pole_analyticity_values']=True
 rows=lambda x:[(1,k) if isinstance(k,int) else tuple(k) for k in x['meta']['pair_k']]
 first=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 base=[(1,k) for k in first]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 heldin=[(n,(n-1)//2+s) for s in [128,512] for n in range(19,32,2)];expected=base+heldin
 assert rows(parent)==base and len(base)==67 and len(heldin)==14 and len(expected)==len(set(expected))==81 and rows(actual)==expected;checks['all81_analytic_rows']=True
 script=bind(B/'source/N1_chain025.sh').read_text();tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1);calls=[]
 for line in script.splitlines():
  if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
   tokens=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));args=tokens[tokens.index('run_quot.py')+1:];assert args[-3]=='>' and args[-1]=='2>&1';calls.append(args[:-3])
 assert len(calls)==1;call=calls[0];meta=actual['meta'];assert len(call)==11
 assert Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag']
 assert int(call[1])==meta['angular_midpoint']==180 and int(call[2])==meta['steps']==60 and int(call[5])==meta['middle_order']==16
 assert Fraction(call[4])==Fraction(str(meta['hw'])) and meta['hw']==parent['meta']['hw']
 assert Fraction(call[6])==meta['wlog']==26214400 and Fraction(call[7])==meta['wkap']==3000000 and Fraction(call[8])==meta['wpair']==10**12
 parsed=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')];assert parsed==expected and call[10]==meta['pair_mode']=='penalty'
 assert meta['n_heldin_rows']==14 and Fraction(str(meta['wpair_heldin']))==10**16 and meta['desc_zero']==[0,1,2]
 for text in ['IPM_DEVICE=cuda','IPM_STEPNORM=1','IPM_NHELDIN=14','IPM_WPAIR_HELDIN=1e16',meta['added_legqs']]:assert text in script
 checks['all_recorded_parameters_and_split_weights']=True
 source=bind(B/'source/N1_run_quot.py').read_text();ast.parse(source)
 for literal in ["PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))",'pair_k=PAIRK','wpair=WLIST','[WPAIR]*(len(PAIRK)-NHELD) + [WHELD]*NHELD','a0 = np.r_[a0, np.zeros(added)]',"sp = ['legqs', w, n, 4, R0]",'w = max(5-m, 0)','a_start = prob.taylor_project(a0, iters=8)']:
  assert literal in source,literal
 implementation=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(implementation);assert 'for q, w in zip(self.pair_k, ws)' in implementation and 'phi_(n,K)' in implementation and 'dRho2' in implementation
 checks['literal_row_weights_zero_addition_and_step_logging']=True
 log=bind(B/'source/N1_025.out').read_text()
 for text in ['generators 2918','pair rows 81 weight 1000000000000.0','per-row weights: first 67 rows 1000000000000.0 ; last 14 rows 1e+16','constraint rows 421','midpoint 180, middle 16',sha(rawp),'added legqs functions 240']:
  assert text in log,text
 pattern=r'^it\s+(\d+) obj (\S+) -> (\S+) (ACC|rej) pred (\S+) lam (\S+) dRho2 (\S+) dCoef (\S+) '
 iterations=[dict(zip(['i','objective_before','objective_proposal','flag','pred','lambda','dRho2','dCoef'],z)) for z in re.findall(pattern,log,re.M)]
 for z in iterations:
  z['i']=int(z['i']);assert Decimal(z['dRho2'])>=0 and Decimal(z['dCoef'])>=0
 assert [z['i'] for z in iterations]==list(range(1,61));acceptedsteps=[z for z in iterations if z['flag']=='ACC'];checks['all60_attempts_with_flags_and_FLOAT_steps']=True
 public=read(R/'research/heldout_probe_register/verification/register.json');extra=[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32]]
 heldp=bind(B/'source/N1_HELDOUT_025.md','6412b2627b390e88e31257cb7fd0788575c6c037aaeaaedc6343e5438a587ea0');held=heldp.read_text();lines=[s for s in held.splitlines() if s.startswith('- the ')]
 observed=[[list(map(int,p)) for p in re.findall(r'(\d+):(\d+)',s)] for s in lines];assert observed==[public['pairs'],extra]
 probes=[]
 for n,K in sum(observed,[]):
  powers=[k for j,k in expected if j==n];assert powers==[(n-1)//2+128,(n-1)//2+512] and K not in powers and K>=(n-1)//2 and n%2
  probes.append({'n':n,'K':K,'outside_span':True,'objective_powers_at_this_mode':powers,'independence_reason':'Distinct nonnegative integer monomials t^K after angular projection','member_of_25_register':[n,K] in public['pairs']})
 assert len(probes)==46 and len({(z['n'],z['K']) for z in probes})==46;checks['all46_outside_analytic_span']=True
 worklog=bind(B/'source/N1_WORKLOG.md').read_text();assert 'chain025 launched 10:05Z' in worklog
 launch='2026-10-29T10:05:00+00:00';assert datetime.fromisoformat(public['utc'])<datetime.fromisoformat(launch)<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 checks['public_register_predates_recorded_launch']=True
 shapep=B/'verification/abstract_shapes.json';save(shapep,{'c_exact':str(c),'generators':[{'j':j,'m':m,'spec':list(s)} for j,m,s in shapes]});bind(shapep)
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d.name,'raw_sha256':sha(rawp),'parent016_sha256':sha(parentp),'generator_count':2918,'potential_dimension':2918,'density_dimension':2918,'dimension_scope':'Before421 recorded constraints; not tangent dimension','old_accepted_rank':1922,'new_shapes_over016':744,'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),'growth_exponent':str(3+gamma),'fourth_derivative_exponent':str(gamma-1),'cross_pole_analyticity':cross,'Laurent_witnesses':witnesses,'exact_objective_rows':[list(p) for p in expected],'objective_weights_exact':['1000000000000']*67+['10000000000000000']*14,'new_heldin_rows':[list(p) for p in heldin],'iterations':iterations,'attempted':60,'accepted':len(acceptedsteps),'rejected':60-len(acceptedsteps),'FLOAT_sum_accepted_rounded_mesh_steps':str(sum((Decimal(z['dRho2']) for z in acceptedsteps),Decimal(0))),'step_norm_scope':'Reported rounded mesh values only; excludes initial Taylor projection and final exact conversion, no rigorous total correction bound','probe_rows':probes,'registration_utc':public['utc'],'publisher_recorded_launch_utc':launch,'heldout_document_claimed_creation_utc':'2026-10-29T09:13:13Z','heldout_document_claimed_addendum_utc':'2026-10-29T09:41:40Z','heldout_current_sha256':sha(heldp),'historical_scope':'007->013->exact quotient->016->025, recorded stages only; no new independent historical timestamp observation','objective_scope':'All81 analytic weak rows, no statistical or sampled-objective independence','checks':checks,'inputs':inputs,'SHA256SUMS':sumrecords,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED own exact finite shapes, three-pole witnesses and recorded span checks; OPEN independent actual025 rank and history review'}
 save(B/'verification/result.json',out);print(out['utc'],'025_SHAPES',len(shapes),'checks',len(checks),'inputs',len(inputs),'seconds',out['elapsed_seconds'],'sha',sha(B/'verification/result.json'),flush=True)
if __name__=='__main__':main()
