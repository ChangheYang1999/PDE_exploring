"""Actual028 prescribed continuation space and full67-row source history."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
from decimal import Decimal
import ast,json,re,shlex,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate028_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2);f.write('\n')
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or h==got,(str(p),h,got)
  rel=str(p.relative_to(R));assert rel not in inputs or inputs[rel]==got;inputs[rel]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST_v01.json',prep['source_manifest_sha256'])
 for name,e in man['files'].items():bind(B/'source'/name,e['sha256'])
 accepted=read(R/'research/candidate022_shape_peer/verification/result.json','81f34093ebb36d8e4386696e2f53d2768d96a391f1530903988e3cc197d5f6bd')
 assert accepted['verdict'].startswith('CONFIRMED') and all(accepted['checks'].values())
 for path,h in accepted['own_inputs'].items():bind(R/path,h)
 for path,e in accepted['frozen_or_retained_sources'].items():bind(R/path,e['stored_sha256'])
 assert accepted['potential_dimension']==accepted['density_dimension']==2414
 checks['independent022_rank_acceptance_rebound']=True
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1
  d=ds[0];m=read(d/'MANIFEST.json');assert len(m['coefficient_files'])==1
  e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d,p,read(p),m
 d,rawp,actual,manifest=raw('028');pd,parentp,parent,pm=raw('022')
 assert d.name==manifest['id'] and d.name.startswith('C1-N1-028-')
 assert sha(parentp)==accepted['raw_sha256']=='85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f'
 snap=read(B/'verification/SNAPSHOT.json');assert snap['candidate']==d.name and snap['raw_sha256']==sha(rawp)
 sumrecords=[]
 for line in bind(d/'SHA256SUMS').read_text().splitlines():
  h,name=line.split(maxsplit=1);name=name.strip().lstrip('*');assert Path(name).name==name
  bind(d/name,h);sumrecords.append({'file':name,'sha256':h})
 checks['all_snapshot_SHA256SUMS']=True
 assert actual['cl_exact']==parent['cl_exact']=='4076476460239181/2251799813685248'
 checks['same_exact_c']=True
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 shapes=list(map(shape,actual['generators']));parent_shapes=list(map(shape,parent['generators']))
 new_shapes=[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,16) for N in range(12,24)]
 assert len(new_shapes)==252 and shapes==parent_shapes+new_shapes and len(shapes)==len(set(shapes))==2666
 assert actual['n_free']==manifest['basis']['generator_count']==2666 and actual['n_fixed']==0
 assert sum(s[0]=='legqs' for j,m,s in shapes)==744
 checks['all2666_actual_shapes_equal022_plus252_radial_terms']=True
 for g in actual['generators']:Fraction(g['coef'])
 checks['all_coefficients_exact_rational']=True
 meta=actual['meta'];assert meta['parent_json']==parentp.name and meta.get('added_legqs')=='1,2,3:9:15:25:24'
 checks['immediate022_input_with252_new_radial_shapes']=True
 c=Fraction(actual['cl_exact']);gamma=1/c;delta=1-gamma
 ps=[(3+gamma-j*delta)/2 for j in range(8)];diffs=[ps[j]-ps[k] for j in range(8) for k in range(j+1,8)]
 assert all(z.denominator!=1 for z in ps+diffs) and 3+gamma<4
 checks['all36_noninteger_branches_and_growth']=True
 from flint import fmpq as Q
 from math import comb
 import importlib.util
 backend=bind(R/'research/joint_scaled_factored_weak/code/fields_joint.py')
 spec=importlib.util.spec_from_file_location('n4_028_pole_witness',backend);F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
 witnesses=[];a=Q(624);v0=-1/a
 for m,N in sorted({(m,z[2]) for j,m,z in new_shapes}):
  A=F.generator(m,['legqs',0,N,4,25]);assert A.powers==tuple(4+N if q==a else 0 for q in F.SCALES)
  actual_laurent=A.numerator_v()(v0)/a**(4+N)
  expected_laurent=Q(25)**8*v0**4*comb(2*N,N)*(1-v0)**(m+N)/a**(4+N)
  assert actual_laurent==expected_laurent and actual_laurent!=0
  witnesses.append({'m':m,'N':N,'pole_order':4+N,'leading_Laurent_coefficient':str(actual_laurent)})
 assert len(witnesses)==84;checks['all84_new_nonzero_Laurent_witnesses']=True
 rows=lambda x:[(1,k) if isinstance(k,int) else tuple(k) for k in x['meta']['pair_k']]
 first=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 base=[(1,k) for k in first]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 heldin=[];expected=base
 assert rows(parent)==base and len(base)==67 and len(expected)==len(set(expected))==67 and rows(actual)==expected
 checks['all67_analytic_rows']=True
 script=bind(B/'source/N1_chain028.sh').read_text();tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1);calls=[]
 for line in script.splitlines():
  if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
   tokens=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));args=tokens[tokens.index('run_quot.py')+1:]
   assert args[-3]=='>' and args[-1]=='2>&1';calls.append(args[:-3])
 assert len(calls)==1;call=calls[0];assert len(call)==11
 assert Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag']
 assert int(call[1])==meta['angular_midpoint']==180 and int(call[2])==meta['steps']==60 and int(call[5])==meta['middle_order']==16
 assert Fraction(call[4])==Fraction(str(meta['hw'])) and meta['hw']==parent['meta']['hw']
 assert Fraction(call[6])==meta['wlog']==26214400 and Fraction(call[7])==meta['wkap']==3000000 and Fraction(call[8])==meta['wpair']==10**12
 parsed=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')]
 assert parsed==expected and call[10]==meta['pair_mode']=='penalty'
 assert meta['n_heldin_rows']==0 and meta['wpair_heldin'] is None and meta['desc_zero']==[0,1,2]
 for text in ['IPM_DEVICE=cuda','IPM_STEPNORM=1']:assert text in script
 assert 'IPM_ADD_LEGQS="1,2,3:9:15:25:24"' in script
 assert 'IPM_NHELDIN' not in script and 'IPM_WPAIR_HELDIN' not in script
 checks['all_recorded_parameters_and_single_row_weight']=True
 source=bind(B/'source/N1_run_quot.py').read_text();ast.parse(source)
 for literal in ["PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))",'pair_k=PAIRK','wpair=WLIST','[WPAIR]*(len(PAIRK)-NHELD) + [WHELD]*NHELD','a_start = prob.taylor_project(a0, iters=8)']:
  assert literal in source,literal
 implementation=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(implementation)
 assert 'for q, w in zip(self.pair_k, ws)' in implementation and 'phi_(n,K)' in implementation and 'dRho2' in implementation
 assert implementation.index('taylor_project')<implementation.index('dRho2')
 checks['literal_row_weights_projection_and_step_logging']=True
 log=bind(B/'source/N1_028.out').read_text()
 for text in ['generators 2666','added legqs functions 252','pair rows 67 weight 1000000000000.0','constraint rows 421','midpoint 180, middle 16',sha(rawp)]:assert text in log,text
 pattern=r'^it\s+(\d+) obj (\S+) -> (\S+) (ACC|rej) pred (\S+) lam (\S+) dRho2 (\S+) dCoef (\S+) '
 iterations=[dict(zip(['i','objective_before','objective_proposal','flag','pred','lambda','dRho2','dCoef'],z)) for z in re.findall(pattern,log,re.M)]
 for z in iterations:
  z['i']=int(z['i']);assert Decimal(z['dRho2'])>=0 and Decimal(z['dCoef'])>=0
 assert [z['i'] for z in iterations]==list(range(1,61));acceptedsteps=[z for z in iterations if z['flag']=='ACC']
 checks['all60_attempts_with_flags_and_FLOAT_steps']=True
 public=read(R/'research/heldout_probe_register/verification/register.json')
 extra=[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32,128,512]]
 heldp=bind(B/'source/N1_HELDOUT_028.md','caf3517ad1961fa1587a976bb14f879a81ab54d05c1c65d68b7c9c5b58187835')
 held=heldp.read_text();lines=[s for s in held.splitlines() if s.startswith('- the ')]
 observed=[[list(map(int,p)) for p in re.findall(r'(\d+):(\d+)',s)] for s in lines];assert observed==[public['pairs'],extra]
 probes=[]
 for n,K in sum(observed,[]):
  powers=[k for j,k in expected if j==n]
  assert not powers and n>=19 and K>=(n-1)//2 and n%2
  probes.append({'n':n,'K':K,'outside_span':True,'objective_powers_at_this_mode':powers,
                 'independence_reason':'Probe frequency at least19; every objective frequency at most17',
                 'member_of_25_register':[n,K] in public['pairs']})
 assert len(probes)==60 and len({(z['n'],z['K']) for z in probes})==60
 checks['all60_outside_analytic_span']=True
 worklog=bind(B/'source/N1_WORKLOG.md').read_text();assert '028' in worklog
 assert '12:51' in worklog
 assert '2028-10-29T12:51:53Z' in held
 launch='2028-10-29T12:51:00+00:00'
 assert datetime.fromisoformat(public['utc'])<datetime.fromisoformat(launch)<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 checks['public_register_predates_recorded_launch_minute']=True
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d.name,'raw_sha256':sha(rawp),
      'parent022_sha256':sha(parentp),'generator_count':2666,'potential_dimension':2666,'density_dimension':2666,
      'dimension_scope':'Before421 recorded constraints; not tangent dimension','actual_shapes_equal_accepted022_plus252_verified_pole_terms':True,
      'branch_exponents':list(map(str,ps)),'noninteger_differences':list(map(str,diffs)),
      'exact_objective_rows':[list(p) for p in expected],
      'objective_weights_exact':['1000000000000']*67,
      'new_heldin_rows':[],'new_Laurent_witnesses':witnesses,'iterations':iterations,
      'attempted':60,'accepted':len(acceptedsteps),'rejected':60-len(acceptedsteps),
      'FLOAT_sum_accepted_rounded_mesh_steps':str(sum((Decimal(z['dRho2']) for z in acceptedsteps),Decimal(0))),
      'step_norm_scope':'Rounded mesh values include per-step Taylor projection; exclude initial projection and final exact conversion; no rigorous total correction bound',
      'probe_rows':probes,'registration_utc':public['utc'],'publisher_recorded_launch_minute':launch,
      'heldout_document_claimed_creation_utc':'2028-10-29T12:51:53Z','heldout_current_sha256':sha(heldp),
      'heldout_before_launch_independently_observed':False,
      'historical_scope':'Accepted022 and its recorded earlier analytic rows ->028; current source inspection only; no new independent historical timestamp observation',
      'objective_scope':'All67 analytic weak rows; no statistical or sampled-objective independence',
      'checks':checks,'inputs':inputs,'SHA256SUMS':sumrecords,'foreign_code_executed':False,
      'elapsed_seconds':time.monotonic()-start,
      'status':'CONFIRMED own exact028 prescribed shapes and recorded span; OPEN independent actual028 structure and history review'}
 save(B/'verification/result.json',out)
 print(out['utc'],'028_SHAPES',len(shapes),'checks',len(checks),'inputs',len(inputs),
       'seconds',out['elapsed_seconds'],'sha',sha(B/'verification/result.json'),flush=True)
if __name__=='__main__':main()
