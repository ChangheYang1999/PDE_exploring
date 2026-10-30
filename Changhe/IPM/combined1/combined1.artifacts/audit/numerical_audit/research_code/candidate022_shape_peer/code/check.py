"""Accept T4-403 for the actual022 basis and two recorded objective stages."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import ast, gzip, json, re, shlex, sys, time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate022_shape_peer';P=R.parent/'c1-t4/research'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 op=R/'research/candidate022_holdout/verification/result.json';own=json.loads(op.read_text());paths=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',op]
 for rel,h in own['inputs'].items():
  p=R/rel;assert sha(p)==h;paths.append(p)
 known={sha(p):(p,False) for p in paths};frozen={};bindings={}
 rp=R/'research/higher_mode_rank_peer/verification/result.json';rankown=json.loads(rp.read_text())
 for rel,e in rankown['frozen_or_retained_sources'].items():
  p=R/rel;assert sha(p)==e['stored_sha256'];known[e['sha256']]=(p,e['gzip'])
 def freeze(p,expected=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert expected is None or h==expected,(p,h,expected)
  if h in known:dest,compressed=known[h]
  else:
   dest=B/'source'/p.relative_to(P);compressed=len(blob)>1000000
   if compressed:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,mtime=0) if compressed else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:
    with dest.open('xb') as f:f.write(stored)
   known[h]=(dest,compressed)
  if compressed:assert sha256(gzip.decompress(dest.read_bytes())).hexdigest()==h
  else:assert sha(dest)==h
  frozen[str(dest.relative_to(R))]={'original':str(p),'sha256':h,'stored_sha256':sha(dest),'gzip':compressed};bindings[str(p)]=h
  return json.loads(blob) if p.suffix=='.json' else blob.decode()
 prep=json.loads((B/'verification/PREPARE.json').read_text())
 peer=freeze(P/'candidate022_shapes/verification/result.json',prep['peer_result_sha256'])
 data={p:freeze(p,h) for p,h in peer['inputs'].items()}
 get=lambda name:data[str(P/name)]
 new=get('candidate022_shapes/data/candidate022.json');phase=get('candidate022_shapes/data/phase1.json');old=get('higher_mode_rank_audit/data/parent016.json');abstract=get('higher_mode_rank_audit/source/N4_shapes.json');rank=get('higher_mode_rank_audit/verification/result.json')
 checks={};shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']));shapes=list(map(shape,new['generators']));base=list(map(shape,old['generators']))
 blocks=[(1,m) for m in range(16,20)]+[(j,m) for j in [2,3] for m in range(16,24)]
 extra=[(j,m,('legqs',0,k,4,25)) for j,m in blocks for k in range(12)]
 checks['proof_binding']=sha(B/'PROOF.md')==prep['proof_sha256'] and bindings[str(P/'candidate022_shapes/PROOF.md')]==prep['peer_proof_sha256']
 checks['raw_hashes']=own['raw_sha256']==peer['raw_sha256']==bindings[str(P/'candidate022_shapes/data/candidate022.json')]=='85c7e4e2c060f1124f2f1d77a2b7f07cd67b32849bd849c1e0a2ec8aa85ce75f' and own['phase1_sha256']==bindings[str(P/'candidate022_shapes/data/phase1.json')]=='2a13c07969eb37af27c68a0336fa7f28a9f1747119e1f7ad4623302f58d5fd4f' and own['parent016_sha256']==bindings[str(P/'higher_mode_rank_audit/data/parent016.json')]=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 checks['all_ordered_shapes']=shapes==list(map(shape,phase['generators']))==list(map(shape,abstract['generators']))==base+extra and len(shapes)==len(set(shapes))==2414 and len(base)==2174 and len(extra)==240 and own['actual_shapes_match_accepted_rank'] and peer['all_actual_shapes_equal_accepted_abstract']
 checks['dimensions']=own['potential_dimension']==own['density_dimension']==peer['potential_dimension']==peer['density_dimension']==rank['potential_dimension']==rank['density_dimension']==rankown['potential_dimension']==rankown['density_dimension']==2414
 c=Q(new['cl_exact']);checks['exact_c']=c==Q(phase['cl_exact'])==Q(old['cl_exact'])==Q(4076476460239181,2251799813685248)
 n1=list(range(9))+[12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 expected=[(1,k) for k in n1]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 rows=lambda d:[(1,x) if isinstance(x,int) else tuple(x) for x in d['meta']['pair_k']]
 checks['all_exact_67_rows']=rows(new)==rows(phase)==rows(old)==expected==[tuple(x) for x in own['exact_objective_rows']]==[tuple(x) for x in peer['exact_objective_rows']] and len(expected)==len(set(expected))==67
 register={(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]};diagnostics={(n,(n-1)//2+s) for n in range(19,32,2) for s in [0,8,32,128,512]};probes=register|diagnostics
 checks['all_60_absent_probes']=len(probes)==60 and not(register&diagnostics) and probes=={tuple(x) for x in peer['outside_analytic_span']}=={(x['n'],x['K']) for x in own['probe_rows'] if x['outside_span']} and all(n>17 and n%2 and k>=(n-1)//2 and (n,k) not in expected for n,k in probes)
 checks['register_25']=register=={tuple(x) for x in get('candidate022_shapes/source/register.json')['pairs']}=={(x['n'],x['K']) for x in own['probe_rows'] if x['member_of_25_register']}
 text=lambda name:get('candidate022_shapes/source/'+name)
 calls=[]
 for line in text('N1_chain022.sh').splitlines():
  if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
   words=shlex.split(line);calls.append(words[words.index('run_quot.py')+1:])
 checks['two_recorded_launches']=len(calls)==2
 tags=re.findall(r'^TAG=([a-zA-Z0-9_]+)$',text('N1_chain022.sh'),re.M);assert tags==['legqs25_m16to23_gpu_m16']
 expand=lambda value:value.replace('${TAG}',tags[0]).replace('$TAG',tags[0])
 for call,d,steps,logfile,rawkey in zip(calls,[phase,new],[12,28],['N1_022_phase1.out','N1_022_phase2.out'],['phase1.json','candidate022.json'],strict=True):
  rr=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in call[9].split(',')];m=d['meta']
  numeric=all(int(call[i])==m[k]==v for i,k,v in [(1,'angular_midpoint',180),(2,'steps',steps),(5,'middle_order',16)])
  weights=all(Q(call[i])==Q(str(m[k]))==v for i,k,v in [(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)])
  checks['launch_'+str(steps)]=rr==expected and numeric and weights and expand(call[0])=='candD2/'+m['parent_json'] and call[10]==m['pair_mode']=='penalty'
  log=text(logfile);it=[int(x) for x in re.findall(r'^it\s+(\d+) obj ',log,re.M)]
  checks['completed_log_'+str(steps)]=it==list(range(1,steps+1)) and bindings[str(P/'candidate022_shapes/data'/rawkey)] in log and 'generators 2414' in log and 'pair rows 67 weight 1000000000000.0' in log
 checks['two_stage_lineage']=phase['meta']['parent_json']=='quot013_legqs25_m9to15_cpu_m16_exact.json' and new['meta']['parent_json']=='legqs25_m16to23_gpu_m16_s12_exact.json' and phase['meta']['added_legqs']=='1,2,3:16:23:25:12' and new['meta']['added_legqs'] is None and own['recorded_iterations']==peer['recorded_iterations']==[12,28]
 asts=[]
 for source in [get('candidate021_shapes/source/N1_run_quot020.py'),text('N1_run_quot.py')]:
  tree=ast.parse(source);parsers=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='_parse'];pair=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in n.targets)];assert len(pair)==len(parsers)==1
  asts.append((ast.dump(parsers[0],include_attributes=False),ast.dump(pair[0],include_attributes=False)))
  app=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='Problem3'];assert len(app)==1 and any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in app[0].keywords)
 checks['current_parser_inspection']=asts[0]==asts[1]
 p1=(3+1/c-(1-1/c))/2;witness=4*33*32*(p1-16-Q(4,625));support=sorted({2*m+s for j,m in blocks for s in [-1,1]})
 checks['density31_witness']=witness!=0 and str(witness)==own['density31_origin_coefficient']==peer['density31_origin_coefficient']==rank['density31_origin_coefficient']==rankown['density31_origin_coefficient']
 checks['support_and_false_disjointness']=support==list(range(31,48,2))==own['density_new_mode_support']==peer['density_new_mode_support']==rankown['density_new_mode_support'] and 'outside the N4-160 n <= 31 sweep' in text('snapshot_manifest.json')['notes'] and own['checks']['manifest_outside31_claim_refuted']
 reg=text('register.json');manifest=text('snapshot_manifest.json')
 checks['documentary_registration_order']=datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:32:00+00:00')<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 checks['peer_binds_own_result']=get('candidate022_shapes/source/N4_result.json')==own
 checks['limited_historical_scope']=peer['scope']=='Parent016 and two recorded022 stages; earlier history not replayed; no statistical-independence claim' and not peer['publisher_code_executed'] and not own['publisher_code_executed']
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(R)):sha(p) for p in paths},'raw_sha256':own['raw_sha256'],'potential_dimension':2414,'density_dimension':2414,'current_rows':expected,'outside_current_analytic_span':sorted(probes),'density_new_mode_support':support,'density31_origin_coefficient':str(witness),'recorded_iterations':[12,28],'historical_scope':peer['scope'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-321 through T4-403 for all actual022 shapes and two recorded67-row stages,60 absent probes; REFUTED complete support outside through31 sweep; no new earlier-history or statistical-blindness audit'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
