from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
import gzip,json,re,time,sys
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate024_shape_peer';P=R.parent/'c1-t4/research'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();paths=[B/'PROOF.md',Path(__file__),B/'verification/PREPARE.json',R/'research/candidate024_holdout/verification/result.json',R/'research/candidate024_hash_reconstruction/verification/result.json',R/'research/candidate023_shape_peer/verification/result.json']
 own=json.loads(paths[3].read_text());repair=json.loads(paths[4].read_text());rank=json.loads(paths[5].read_text());prep=json.loads(paths[2].read_text());known={};bindings={};frozen={}
 for p in paths:known[sha(p)]=(p,False)
 for source in [own,repair]:
  for rel,h in source['inputs'].items():
   p=R/rel;assert sha(p)==h;paths.append(p);known[h]=(p,False)
 for rel,e in rank['frozen_or_retained_sources'].items():
  p=R/rel;assert sha(p)==e['stored_sha256'];known[e['sha256']]=(p,e['gzip'])
 for rel,h in rank['own_inputs'].items():p=R/rel;assert sha(p)==h;paths.append(p);known[h]=(p,False)
 def freeze(p,h=None):
  p=Path(p);blob=p.read_bytes();actual=sha256(blob).hexdigest();assert h is None or h==actual
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
 peer=freeze(P/'candidate024_shapes/verification/result.json',prep['peer_result_sha256']);d={p:freeze(p,h) for p,h in peer['inputs'].items()};get=lambda s:d[str(P/s)]
 raw=get('candidate024_shapes/data/candidate024.json');parent=get('higher_mode_rank_audit/data/parent016.json');old=get('candidate024_shapes/data/old_basis.json');quot=get('candidate024_shapes/data/quotient013.json')
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']));ss=list(map(shape,raw['generators']));ps=list(map(shape,parent['generators']));scaled=[(j,m,('legqs',0,n,4,25)) for j in (1,2,3) for m in range(9,16) for n in range(12)]
 n1=list(range(9))+[12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096];rows=[(1,k) for k in n1]+[(n,(n-1)//2+s)for n in range(3,18,2)for s in (0,8,32,128,512)]
 normalized=lambda q:[(1,k)if isinstance(k,int)else tuple(k)for k in q['meta']['pair_k']]
 public={(n,k)for n in (19,23,25,29,31)for k in (600,900,1200,1800,2400)};probes=public|{(n,(n-1)//2+s)for n in range(19,32,2)for s in (0,8,32,128,512)}
 held=get('candidate024_shapes/source/N1_HELDOUT_024.md');restored=held.replace('Objective rows (67):','Objective rows (81? no: 67):');iterations=[(int(i),flag)for i,flag in re.findall(r'^it\s+(\d+) obj .*? (ACC|rej) pred ',get('candidate024_shapes/source/N1_024.out'),re.M)]
 checks={'proof':sha(B/'PROOF.md')==prep['proof_sha256'],'raw':own['raw_sha256']==peer['raw_sha256']==bindings[str(P/'candidate024_shapes/data/candidate024.json')]=='3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d','ordered_shapes':ss==ps==ss[:1922]+scaled,'old_quotient_sets':set(ss[:1922])==set(map(shape,old['generators']))==set(map(shape,quot['generators'])),'distinct2174':len(ss)==len(set(ss))==2174,'subset_of_accepted_independent023':set(ss)<=set(map(shape,get('candidate023_shapes/data/candidate023.json')['generators'])),'accepted_rank':rank['potential_dimension']==rank['density_dimension']==2426 and all(rank['checks'].values()),'dimensions':own['potential_dimension']==own['density_dimension']==peer['potential_dimension']==peer['density_dimension']==2174,'exact_c':Q(raw['cl_exact'])==Q(parent['cl_exact'])==Q(quot['cl_exact'])==Q(4076476460239181,2251799813685248),'all67rows':normalized(raw)==normalized(parent)==rows==[tuple(x)for x in own['objective_rows']]==[tuple(x)for x in peer['exact_objective_rows']] and len(set(rows))==67,'all60probes':len(probes)==60 and probes==set(map(tuple,peer['outside_analytic_span']))=={(p['n'],p['K'])for p in own['probe_rows']},'outside_span':all(n>17 and 2*k+1>=n for n,k in probes),'iterations':iterations==[(p['i'],p['flag'])for p in own['iterations']]==list(map(tuple,peer['iterations'])) and [i for i,f in iterations]==list(range(1,13)),'attempts':own['attempted']==peer['attempted']==12 and own['accepted']==peer['accepted']==5 and own['rejected']==peer['rejected']==7,'radial_and_backend':own['comparison_parameters']['middle_order016']==16 and own['comparison_parameters']['middle_order024']==32 and own['comparison_parameters']['backend016']=='cpu' and own['comparison_parameters']['backend024']=='cuda','unique_heading':held.count('Objective rows (67):')==1 and 'Objective rows (81? no: 67):' not in held,'current_hash':sha256(held.encode()).hexdigest()==own['current_heldout_sha256']==peer['current_heldout_sha256'],'former_hash_reconstructed':sha256(restored.encode()).hexdigest()==peer['reconstructed_sha256']=='58586004ad6ae0d0bf1545de2afbaa2f4643170e9d86334b59eda032eb02f4f5','peer_scope':'no earlier optimizer history or independently witnessed09:13 save times' in peer['scope'],'peer_full_check_count':len(peer['checks'])==peer['check_count']==87,'no_foreign_execution':not own['foreign_code_executed'] and not peer['publisher_code_executed']}
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'raw_sha256':own['raw_sha256'],'potential_dimension':2174,'density_dimension':2174,'current_rows':rows,'outside_current_analytic_span':sorted(probes),'recorded_iterations':iterations,'frozen_or_retained_sources':frozen,'peer_input_bindings':bindings,'own_inputs':{str(p.relative_to(R)):sha(p)for p in paths},'historical_scope':peer['scope'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED current024 shape, objective and byte reconstruction through independent T4-427; historical save times remain unobserved'}
 with (B/'verification/result.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED024shape',len(checks),len(bindings),sha(B/'verification/result.json'))
if __name__=='__main__':main()
