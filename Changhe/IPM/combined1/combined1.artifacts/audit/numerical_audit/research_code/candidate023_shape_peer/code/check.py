"""Accept the actual 023 list and recorded stages against independent T4-416."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb
from hashlib import sha256
import ast,gzip,json,re,shlex,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate023_shape_peer';P=R.parent/'c1-t4/research'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();paths=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',R/'research/candidate023_holdout/verification/result.json']
 own=json.loads(paths[-1].read_text());prep=json.loads(paths[-2].read_text())
 for rel,h in own['inputs'].items():
  p=R/rel;assert sha(p)==h;(paths.append(p))
 known={sha(p):(p,False) for p in paths};frozen={};bindings={}
 prior=json.loads((R/'research/candidate022_shape_peer/verification/result.json').read_text())
 for rel,e in prior['frozen_or_retained_sources'].items():
  p=R/rel;assert sha(p)==e['stored_sha256'];known[e['sha256']]=(p,e['gzip'])
 def freeze(p,h=None):
  p=Path(p);blob=p.read_bytes();actual=sha256(blob).hexdigest();assert h is None or actual==h,(p,actual,h)
  if actual in known:dest,zipped=known[actual]
  else:
   dest=B/'source'/p.relative_to(P);zipped=len(blob)>1000000
   if zipped:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,compresslevel=2,mtime=0) if zipped else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:dest.write_bytes(stored)
   known[actual]=(dest,zipped)
  assert sha256(gzip.decompress(dest.read_bytes()) if zipped else dest.read_bytes()).hexdigest()==actual
  frozen[str(dest.relative_to(R))]={'original':str(p),'sha256':actual,'stored_sha256':sha(dest),'gzip':zipped};bindings[str(p)]=actual
  return json.loads(blob) if p.suffix=='.json' else blob.decode()
 peer=freeze(P/'candidate023_shapes/verification/result.json',prep['peer_result_sha256'])
 data={p:freeze(p,h) for p,h in peer['inputs'].items()};get=lambda rel:data[str(P/rel)]
 raw=get('candidate023_shapes/data/candidate023.json');phase=get('candidate023_shapes/data/phase1.json');parent=get('higher_mode_rank_audit/data/parent016.json');old=get('candidate023_shapes/data/old_basis.json')
 checks={};shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']));scaled=lambda scale:[(j,m,('legqs',0,n,4,scale)) for j in (1,2,3) for m in range(9,16) for n in range(12)]
 ps=list(map(shape,parent['generators']));shapes=list(map(shape,raw['generators']));os=list(map(shape,old['generators']))
 checks['proof_binding']=sha(B/'PROOF.md')==prep['proof_sha256'] and bindings[str(P/'candidate023_shapes/PROOF.md')]==prep['peer_proof_sha256']
 checks['raw_bindings']=own['raw_sha256']==peer['raw_sha256']==bindings[str(P/'candidate023_shapes/data/candidate023.json')]=='d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df' and own['phase1_sha256']==bindings[str(P/'candidate023_shapes/data/phase1.json')]=='637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb' and own['parent016_sha256']==bindings[str(P/'higher_mode_rank_audit/data/parent016.json')]=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 checks['all_ordered_shapes']=shapes==list(map(shape,phase['generators']))==ps+scaled(100) and ps==ps[:1922]+scaled(25) and len(shapes)==len(set(shapes))==2426
 checks['old_basis_permutation']=set(ps[:1922])==set(os) and len(os)==len(set(os))==1922
 checks['dimensions']=own['potential_dimension']==own['density_dimension']==peer['potential_dimension']==peer['density_dimension']==2426
 c=Q(raw['cl_exact']);delta=1-1/c;branches=[(3+1/c-j*delta)/2 for j in range(8)];diffs=[branches[j]-branches[k] for j in range(8) for k in range(j+1,8)]
 checks['fixed_c_and_branches']=c==Q(phase['cl_exact'])==Q(parent['cl_exact'])==Q(4076476460239181,2251799813685248) and list(map(str,branches))==own['branch_exponents'] and list(map(str,diffs))==own['noninteger_differences'] and all(q.denominator!=1 for q in branches+diffs) and 3+1/c<4
 ow={(w['scale'],w['m'],w['N']):Q(w['Laurent_coefficient']) for w in own['Laurent_witnesses']};tw={(w['scale'],w['m'],w['N']):Q(w['coefficient']) for w in peer['Laurent_witnesses']};records=[]
 for scale,other in [(25,100),(100,25)]:
  a=scale*scale-1;v=Q(-1,a);cross=1-Q(other*other-1,a);assert cross!=0
  prow=[w for w in peer['cross_poles'] if w['scale']==scale and w['other_scale']==other];assert len(prow)==1 and Q(prow[0]['other_denominator'])==cross
  for m in range(9,16):
   for n in range(12):
    value=scale**8*v**4*comb(2*n,n)*(1-v)**(m+n)/a**(4+n);assert value!=0 and value==ow[scale,m,n]==tw[scale,m,n]
    records.append({'scale':scale,'m':m,'N':n,'order':4+n,'coefficient':str(value)})
 checks['all168_independent_Laurent_witnesses']=len(records)==len(ow)==len(tw)==168 and all(w['recurrence_equals_formula'] and w['pole_order']==4+w['N'] for w in peer['Laurent_witnesses'])
 n1=list(range(9))+[12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096];objective=[(1,k) for k in n1]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in (0,8,32,128,512)]
 rows=lambda d:[(1,k) if isinstance(k,int) else tuple(k) for k in d['meta']['pair_k']]
 checks['all67_rows']=rows(raw)==rows(phase)==rows(parent)==objective==[tuple(x) for x in own['exact_objective_rows']]==[tuple(x) for x in peer['exact_objective_rows']] and len(set(objective))==67
 text=lambda name:get('candidate023_shapes/source/'+name)
 script=text('N1_chain023.sh');tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1);calls=[]
 for line in script.splitlines():
  if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line):
   words=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));calls.append(words[words.index('run_quot.py')+1:])
 checks['two_launches']=len(calls)==2
 for call,d,steps,logname,rawkey in zip(calls,(phase,raw),(12,28),('N1_023_phase1.out','N1_023_phase2.out'),('phase1.json','candidate023.json'),strict=True):
  rr=[tuple(map(int,z.split(':'))) if ':' in z else (1,int(z)) for z in call[9].split(',')];meta=d['meta']
  checks[f'launch_{steps}']=rr==objective and Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag'] and all(int(call[i])==meta[k]==v for i,k,v in [(1,'angular_midpoint',180),(2,'steps',steps),(5,'middle_order',16)]) and all(Q(call[i])==Q(str(meta[k]))==v for i,k,v in [(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)]) and Q(call[4])==Q(str(meta['hw']))==Q('0.952380952380952') and call[10]==meta['pair_mode']=='penalty'
  log=text(logname);checks[f'log_{steps}']=[int(x) for x in re.findall(r'^it\s+(\d+) obj ',log,re.M)]==list(range(1,steps+1)) and bindings[str(P/'candidate023_shapes/data'/rawkey)] in log and 'generators 2426' in log and 'pair rows 67 weight 1000000000000.0' in log and 'per-row weights:' not in log
 checks['stage_lineage']=phase['meta']['parent_json']=='quot013_legqs25_m9to15_cpu_m16_exact.json' and raw['meta']['parent_json']=='legqs25p100_m9to15_gpu_m16_s12_exact.json' and phase['meta']['added_legqs']=='1,2,3:9:15:100:12' and raw['meta']['added_legqs'] is None and own['recorded_iterations']==peer['recorded_iterations']==[12,28]
 parsers=[]
 for source in [get('candidate021_shapes/source/N1_run_quot020.py'),text('N1_run_quot.py')]:
  tree=ast.parse(source);pp=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='_parse'];aa=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in n.targets)];assert len(pp)==len(aa)==1
  parsers.append((ast.dump(pp[0],include_attributes=False),ast.dump(aa[0],include_attributes=False)));assert any(isinstance(n,ast.Call) and any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in n.keywords) for n in ast.walk(tree))
 checks['row_parser_unchanged']=parsers[0]==parsers[1];impl=text('N1_ipm_opt3.py');ast.parse(impl);checks['objective_row_propagation']='for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl
 reg=text('register.json');snapshot=text('snapshot_manifest.json');public={(n,k) for n in (19,23,25,29,31) for k in (600,900,1200,1800,2400)};probes=public|{(n,(n-1)//2+s) for n in range(19,32,2) for s in (0,8,32,128,512)}
 checks['all60_outside_analytic_span']=len(probes)==60 and probes=={tuple(x) for x in peer['outside_analytic_span']}=={(w['n'],w['K']) for w in own['probe_rows']} and all(n%2 and k>=(n-1)//2 and all(n!=j for j,l in objective) for n,k in probes)
 checks['public25_register']=public=={tuple(x) for x in reg['pairs']}=={(w['n'],w['K']) for w in own['probe_rows'] if w['member_of_25_register']}
 checks['documentary_timing']=datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:46:00+00:00')<datetime.fromisoformat(snapshot['created_utc'].replace('Z','+00:00'))
 checks['scoped_history']=peer['scope']=='Parent016 and two recorded023 stages; earlier history not independently replayed; no statistical-independence claim' and not peer['publisher_code_executed'] and not own['foreign_code_executed']
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(R)):sha(p) for p in paths},'raw_sha256':own['raw_sha256'],'potential_dimension':2426,'density_dimension':2426,'current_rows':objective,'outside_current_analytic_span':sorted(probes),'Laurent_witnesses':records,'recorded_iterations':[12,28],'historical_scope':peer['scope'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED actual023 shapes,2426-dimensional potential and density spans,168 fresh25/100 witnesses,67 rows and60 outside probes; recorded parent016 and two023 stages only'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(B/'verification/result.json'),'seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
