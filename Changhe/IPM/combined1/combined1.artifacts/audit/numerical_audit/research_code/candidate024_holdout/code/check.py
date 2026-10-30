"""Exact024 finite shapes and recorded history. Publisher code is text only."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from fractions import Fraction
import ast,json,re,shlex,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate024_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);got=sha(p);assert h is None or h==got,(str(p),h,got);inputs[str(p.relative_to(R))]=got;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'verification/PREPARE_v03.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 man=read(B/'source/MANIFEST_v01.json',prep['source_manifest_sha256'])
 for path,e in man['files'].items():bind(R/path,e['sha256'])
 rank=read(R/'research/joint_scaled_rank_peer/verification/result.json');assert rank['verdict'].startswith('CONFIRMED')
 for path,h in rank['inputs'].items():bind(R/path,h)
 for e in rank['frozen_sources'].values():bind(R/e['local'],e['stored_sha256'])
 assert rank['potential_dimension']==rank['density_dimension']==2426
 prior=read(R/'research/candidate016_holdout/verification/result.json','57a7fd0da9db3842f81de94fe3fc3a2d635a765bfd5a12769899b5799050db02');assert prior['status'].startswith('CONFIRMED')
 for path,h in prior['inputs'].items():bind(R/path,h)
 checks['accepted_rank_and_recorded016_history_rebound']=True
 old=read(R/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json','c0d3536ea961908a8a4d251054192bad0b5b2534435e3c8224fe0424bda5f7fe')
 def raw(ident):
  ds=list((R/'research/candidate_audits/data').glob('C1-N1-'+ident+'-*'));assert len(ds)==1
  d=ds[0];m=read(d/'MANIFEST.json');e=m['coefficient_files'][0];p=bind(d/e['name'],e['sha256']);return d,p,read(p),m
 d,rawp,actual,manifest=raw('024');pd,parentp,parent,pm=raw('016')
 assert sha(rawp)=='3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d'
 assert sha(parentp)==prior['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 sums=bind(d/'SHA256SUMS').read_text();sumrecords=[]
 for line in sums.splitlines():
  h,name=line.split(maxsplit=1);name=name.strip().lstrip('*');assert Path(name).name==name;bind(d/name,h);sumrecords.append({'file':name,'sha256':h})
 checks['all_snapshot_SHA256SUMS']=True
 assert actual['cl_exact']==parent['cl_exact']==old['cl_exact']=='4076476460239181/2251799813685248';checks['same_exact_c']=True
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']))
 olds=list(map(shape,old['generators']));added=[(j,m,('legqs',0,N,4,25)) for j in [1,2,3] for m in range(9,16) for N in range(12)]
 shapes=olds+added
 assert len(olds)==len(set(olds))==1922 and len(shapes)==len(set(shapes))==2174
 assert list(map(shape,actual['generators']))==list(map(shape,parent['generators']))==shapes
 abstract=read(R/'research/joint_scaled_density_rank/verification/abstract_shapes.json','e13d90dcaceae46e4584670d16fb8af80b26559f9a9f1caec985cfc808d408e0')
 subset=[shape(g) for g in abstract['generators'] if not (g['spec'][0]=='legqs' and g['spec'][4]==50)]
 assert subset==shapes;checks['all2174_ordered_shapes_equal016_and_accepted_subset']=True
 for g in actual['generators']:Fraction(g['coef'])
 assert manifest['basis']['generator_count']==actual['n_free']==2174 and actual['n_fixed']==0
 checks['exact_rational_coefficients_and_raw_counts']=True
 rows=lambda x:[(1,k) if isinstance(k,int) else tuple(k) for k in x['meta']['pair_k']]
 first=[0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 expected=[(1,k) for k in first]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 assert len(expected)==len(set(expected))==67 and rows(actual)==rows(parent)==expected;checks['all67_exact_rows_match016']=True
 script=bind(B/'source/N1_chain024.sh').read_text();script016=bind(R/'research/candidate016_holdout/source/N1_chain016_core54_cpu.sh').read_text()
 def command(text):
  tag=re.search(r'^TAG=([^\s]+)$',text,re.M).group(1);out=[]
  for line in text.splitlines():
   if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
    tokens=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));args=tokens[tokens.index('run_quot.py')+1:];assert args[-3]=='>' and args[-1]=='2>&1';out.append(args[:-3])
  assert len(out)==1;return out[0]
 call=command(script);call016=command(script016);meta=actual['meta']
 assert len(call)==len(call016)==11
 assert all(call[i]==call016[i] for i in range(11) if i not in [3,5])
 assert Path(call[0]).name==meta['parent_json']=='d2w_j7_n4_E2bal_pairU_cpu_m16_quot_exact.json'
 assert int(call[1])==meta['angular_midpoint']==180 and int(call[2])==meta['steps']==12 and call[3]==meta['tag']
 assert Fraction(call[4])==Fraction(str(meta['hw'])) and meta['hw']==parent['meta']['hw']
 assert int(call[5])==meta['middle_order']==32 and int(call016[5])==parent['meta']['middle_order']==16
 assert Fraction(call[6])==meta['wlog']==26214400 and Fraction(call[7])==meta['wkap']==3000000 and Fraction(call[8])==meta['wpair']==10**12
 parsed=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')]
 assert parsed==expected and call[10]==meta['pair_mode']=='penalty'
 assert meta['added_legqs']=='1,2,3:9:15:25:12' and meta['n_heldin_rows']==0 and meta['wpair_heldin'] is None and meta['desc_zero']==[0,1,2]
 checks['all_recorded_objective_parameters']=True
 assert 'IPM_DEVICE=cpu' in script016.split('while ')[0] and 'IPM_DEVICE=cuda' in script and 'IPM_STEPNORM=1' in script
 checks['backend_also_changed']=True
 source=bind(B/'source/N1_run_quot.py').read_text();ast.parse(source)
 for literal in ["PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))",'pair_k=PAIRK','a0 = np.r_[a0, np.zeros(added)]',"sp = ['legqs', w, n, 4, R0]",'w = max(5-m, 0)','a_start = prob.taylor_project(a0, iters=8)']:
  assert literal in source,literal
 implementation=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(implementation)
 assert 'for q, w in zip(self.pair_k, ws)' in implementation and 'phi_(n,K)' in implementation
 checks['literal_zero_addition_projection_and_row_parser_text_only']=True
 log=bind(B/'source/N1_024.out').read_text()
 for literal in ['added legqs functions 252','generators 2174','pair rows 67 weight 1000000000000.0','constraint rows 421','midpoint 180, middle 32',sha(rawp)]:assert literal in log,literal
 assert 'per-row weights:' not in log
 iterations=[{'i':int(i),'flag':flag} for i,flag in re.findall(r'^it\s+(\d+) obj \S+ -> \S+ (ACC|rej) ',log,re.M)]
 assert [r['i'] for r in iterations]==list(range(1,13)) and [r['flag'] for r in iterations]==['rej','rej','ACC','rej','rej','rej','ACC','ACC','rej','ACC','ACC','rej']
 accepted=sum(r['flag']=='ACC' for r in iterations);assert accepted==5;checks['12_attempts_5_accepted_7_rejected']=True
 public=read(R/'research/heldout_probe_register/verification/register.json')
 extra=[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32,128,512]]
 heldp=bind(B/'source/N1_HELDOUT_024.md');held=heldp.read_text();lines=[s for s in held.splitlines() if s.startswith('- the ')]
 observed=[[list(map(int,p)) for p in re.findall(r'(\d+):(\d+)',s)] for s in lines]
 assert observed==[public['pairs'],extra];probes=[]
 for n,K in sum(observed,[]):
  assert n>17 and n%2 and 2*K+1>=n and all(n!=j for j,k in expected)
  probes.append({'n':n,'K':K,'outside_analytic_span':True,'all_objective_coefficients_at_n':0})
 assert len(probes)==60;checks['all60_current_pairs_and_analytic_span']=True
 launch='2026-10-29T10:37:00+00:00'
 assert datetime.fromisoformat(public['utc'])<datetime.fromisoformat(launch)<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 checks['public_register_predates_publisher_recorded_launch']=True
 good='e171c051207448d35c53b44567b45c3699ed54de3349fb9e7402e06755fc0fab';bad='58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5'
 assert sha(heldp)==good and good!=bad
 records={'index':bind(B/'source/N1_INDEX.md').read_text(),'publisher_notes':bind(B/'source/N1_NOTES.md').read_text(),'immutable_manifest':bind(d/'MANIFEST.json').read_text()}
 locations={key:{'actual_hash':[i+1 for i,s in enumerate(text.splitlines()) if good in s],'claimed_other_hash':[i+1 for i,s in enumerate(text.splitlines()) if bad[:8] in s],'full_other_hash':[i+1 for i,s in enumerate(text.splitlines()) if bad in s]} for key,text in records.items()}
 assert locations['index']['claimed_other_hash'] and locations['publisher_notes']['claimed_other_hash'] and locations['publisher_notes']['actual_hash']
 assert not locations['immutable_manifest']['claimed_other_hash'] and not locations['immutable_manifest']['actual_hash'];checks['bad_hash_locations_and_manifest_absence']=True
 index024=[{'line':i+1,'text':s} for i,s in enumerate(records['index'].splitlines()) if 'C1-N1-024-rulem32-legqs25' in s]
 assert any('10:37Z launch' in z['text'] for z in index024) and any('LOSS (MID 16)' in z['text'] and 'Optimizer report (MID 16)' in z['text'] for z in index024) and all('middle 32' in s for s in log.splitlines() if s.startswith('FINAL (FLOAT') or s.startswith('start (FLOAT'))
 checks['index_MID16_label_refuted_by_actual_log']=True
 assert all(checks.values()) and all(sha(R/p)==h for p,h in inputs.items())
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':d.name,'raw_sha256':sha(rawp),'generator_count':2174,'potential_dimension':2174,'density_dimension':2174,'dimension_scope':'Potential and density span before the recorded421 constraint rows, not tangent dimension','same_ordered_shapes_as016':True,'recorded_initial_candidate':'013 exact quotient, before Taylor projection','new_shapes':252,'new_coefficients_before_projection':'zero by frozen source branch, no floating replay','objective_rows':[list(p) for p in expected],'iterations':iterations,'attempted':12,'accepted':accepted,'rejected':12-accepted,'comparison_parameters':{'same_input_and67_rows':True,'same_weights_angular_rule_steps':True,'middle_order016':16,'middle_order024':32,'backend016':'cpu','backend024':'cuda','024_stepnorm_logging':True},'probe_rows':probes,'current_heldout_sha256':good,'other_claimed_sha256':bad,'hash_locations':locations,'index024_records':index024,'registered_public_utc':public['utc'],'publisher_recorded_launch_utc':launch,'heldout_document_asserted_write_utc':'2026-10-29T09:13:13Z','snapshot_utc':manifest['created_utc'],'source_snapshot_utc':man['utc'],'source_mtimes':{k:e['source_mtime_utc'] for k,e in man['files'].items() if 'source_mtime_utc' in e},'SHA256SUMS':sumrecords,'checks':checks,'inputs':inputs,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdicts':{'exact_basis_and_recorded_rows':'CONFIRMED','current_heldout_list_and_outside_span':'CONFIRMED','index_and_later_notes_hash_byte_identity':'REFUTED','bad_hash_in_immutable_manifest':'REFUTED, absent from this frozen immutable manifest','index_MID16_optimizer_label':'REFUTED, actual middle32','isolated_one_parameter_control':'REFUTED by also changed backend','older_bad_hash_preimage':'OPEN, unavailable','optimizer_stopping_cause':'OPEN, finite trial history does not decide','numerical_norm_background_inverse_existence':'OPEN, outside this check'},'status':'CONFIRMED own exact finite shape and recorded history checks with explicit provenance refutations; no certified norm or independent actual024 replay'}
 p=B/'verification/result.json'
 with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'024_HISTORY',len(checks),'checks',len(inputs),'inputs',out['elapsed_seconds'],'seconds','sha',sha(p),flush=True)
if __name__=='__main__':main()
