"""Compare actual025 own expanded witnesses to independent T4-436 recurrence."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from decimal import Decimal
from math import comb
from hashlib import sha256
import ast,gzip,json,re,shlex,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate025_shape_peer';P=R.parent/'c1-t4/research'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();paths=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',R/'research/candidate025_holdout/verification/result.json',R/'research/candidate024_shape_peer/verification/result.json']
 own=json.loads(paths[3].read_text());prior=json.loads(paths[4].read_text());prep=json.loads(paths[2].read_text());known={};frozen={};bindings={}
 for p in paths:known[sha(p)]=(p,False)
 for rel,h in own['inputs'].items():
  p=R/rel;assert sha(p)==h;paths.append(p);known[h]=(p,False)
 for rel,e in prior['frozen_or_retained_sources'].items():
  p=R/rel;assert sha(p)==e['stored_sha256'];known[e['sha256']]=(p,e['gzip'])
 for rel,h in prior['own_inputs'].items():
  p=R/rel;assert sha(p)==h;paths.append(p);known[h]=(p,False)
 ownbindings={str(p.relative_to(R)):sha(p) for p in paths}
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
 peer=freeze(P/'candidate025_shapes/verification/result.json',prep['peer_result_sha256']);data={p:freeze(p,h) for p,h in peer['inputs'].items()};get=lambda rel:data[str(P/rel)]
 # Bind every input before any candidate-specific rational arithmetic.
 before={'utc':datetime.now(timezone.utc).isoformat(),'own_inputs':ownbindings,'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen}
 with (B/'verification/source_start_v01.json').open('x')as f:json.dump(before,f,indent=2);f.write('\n')
 raw=get('candidate025_shapes/data/candidate025.json');parent=get('higher_mode_rank_audit/data/parent016.json');old=get('candidate025_shapes/data/old_basis.json');quot=get('candidate025_shapes/data/quotient013.json')
 shape=lambda g:(int(g['j']),int(g['m']),tuple(g['spec']));low=lambda s:[(j,m,('legqs',0,n,4,s))for j in (1,2,3)for m in range(9,16)for n in range(12)]
 high=[(j,m,('legqs',0,n,4,25))for j in (1,2,3)for m in range(16,20 if j==1 else24)for n in range(12)]
 ss=list(map(shape,raw['generators']));ps=list(map(shape,parent['generators']));os=list(map(shape,old['generators']));checks={}
 checks['proof_bindings']=sha(B/'PROOF.md')==prep['proof_sha256'] and bindings[str(P/'candidate025_shapes/PROOF.md')]==prep['peer_proof_sha256']
 checks['actual_raw_bindings']=own['raw_sha256']==peer['raw_sha256']==bindings[str(P/'candidate025_shapes/data/candidate025.json')]=='3b1c9f7199b56fc892815eefac8696e811a72d729ead5b955491e20961221f17'
 checks['parent016_binding']=own['parent016_sha256']==bindings[str(P/'higher_mode_rank_audit/data/parent016.json')]=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
 checks['all2918_ordered_shapes']=ss==ps+low(50)+low(100)+high and ps==ps[:1922]+low(25) and len(ss)==len(set(ss))==2918 and len(high)==240
 checks['old_quotient_independent_sets']=set(ps[:1922])==set(os)==set(map(shape,quot['generators'])) and len(os)==len(set(os))==1922
 checks['dimensions']=own['potential_dimension']==own['density_dimension']==peer['potential_dimension']==peer['density_dimension']==2918
 c=Q(raw['cl_exact']);delta=1-1/c;branches=[(3+1/c-j*delta)/2 for j in range(8)];diffs=[branches[j]-branches[k] for j in range(8)for k in range(j+1,8)]
 checks['all36_noninteger_branches']=c==Q(parent['cl_exact'])==Q(quot['cl_exact'])==Q(4076476460239181,2251799813685248) and list(map(str,branches))==own['branch_exponents']==peer['branch_exponents'] and list(map(str,diffs))==own['noninteger_differences']==peer['noninteger_differences'] and all(q.denominator!=1 for q in branches+diffs) and 3+1/c<4
 ow={(w['scale'],w['m'],w['N']):Q(w['Laurent_coefficient'])for w in own['Laurent_witnesses']};tw={(w['scale'],w['m'],w['N']):Q(w['coefficient'])for w in peer['Laurent_witnesses']};records=[];crossrecords=[]
 for scale in (25,50,100):
  a=scale*scale-1;v=Q(-1,a)
  for other in (25,50,100):
   if other==scale:continue
   cross=1-Q(other*other-1,a);prow=[w for w in peer['cross_poles']if w['scale']==scale and w['other_scale']==other]
   assert cross!=0 and len(prow)==1 and Q(prow[0]['other_denominator'])==cross;crossrecords.append(prow[0])
  for m in range(9,24 if scale==25 else16):
   for n in range(12):
    value=scale**8*v**4*comb(2*n,n)*(1-v)**(m+n)/a**(4+n);assert value!=0 and value==ow[scale,m,n]==tw[scale,m,n]
    records.append({'scale':scale,'m':m,'N':n,'order':4+n,'coefficient':str(value)})
 checks['all348_expanded_witnesses']=len(records)==len(ow)==len(tw)==348 and all(w['recurrence_equals_formula']and w['pole_order']==4+w['N']for w in peer['Laurent_witnesses'])
 checks['all_six_cross_poles']=len(crossrecords)==6
 n1=list(range(9))+[12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]
 base=[(1,k)for k in n1]+[(n,(n-1)//2+s)for n in range(3,18,2)for s in (0,8,32,128,512)]
 rows=base+[(n,(n-1)//2+s)for s in (128,512)for n in range(19,32,2)];weights=['1000000000000']*67+['10000000000000000']*14
 normalized=lambda d:[(1,k)if isinstance(k,int)else tuple(k)for k in d['meta']['pair_k']]
 checks['all81_rows_and_split_weights']=normalized(raw)==rows==list(map(tuple,own['exact_objective_rows']))==list(map(tuple,peer['exact_objective_rows'])) and normalized(parent)==base and len(set(rows))==81 and own['objective_weights_exact']==peer['objective_weights_exact']==weights
 text=lambda name:get('candidate025_shapes/source/'+name)
 script=text('N1_chain025.sh');tag=re.search(r'^TAG=([^\s]+)$',script,re.M).group(1);calls=[]
 for line in script.splitlines():
  if line.startswith('taskset ')and 'run_quot.py'in shlex.split(line):
   words=shlex.split(line.replace('${TAG}',tag).replace('$TAG',tag));calls.append(words[words.index('run_quot.py')+1:])
 assert len(calls)==1;call=calls[0];meta=raw['meta'];rr=[tuple(map(int,z.split(':')))if ':'in z else(1,int(z))for z in call[9].split(',')]
 checks['launch_parameters']=rr==rows and Path(call[0]).name==meta['parent_json'] and call[3]==meta['tag'] and all(int(call[i])==meta[k]==v for i,k,v in [(1,'angular_midpoint',180),(2,'steps',60),(5,'middle_order',16)])and all(Q(call[i])==Q(str(meta[k]))==v for i,k,v in [(6,'wlog',26214400),(7,'wkap',3000000),(8,'wpair',10**12)])and meta['n_heldin_rows']==14 and meta['wpair_heldin']==10**16 and call[10]==meta['pair_mode']=='penalty'
 for literal in ['IPM_DEVICE=cuda','IPM_STEPNORM=1','IPM_NHELDIN=14','IPM_WPAIR_HELDIN=1e16']:assert literal in script,literal
 log=text('N1_025.out');iterations=[(int(i),flag)for i,flag in re.findall(r'^it\s+(\d+) obj .*? (ACC|rej) pred ',log,re.M)]
 checks['all60_attempts']=iterations==[(w['i'],w['flag'])for w in own['iterations']]==list(map(tuple,peer['iterations'])) and [i for i,f in iterations]==list(range(1,61))
 checks['39accepted21rejected']=own['attempted']==peer['attempted']==60 and own['accepted']==peer['accepted']==39 and own['rejected']==peer['rejected']==21 and sum(f=='ACC'for i,f in iterations)==39
 vals=[Decimal(x)for flag,x in re.findall(r'^it\s+\d+ obj .*? (ACC|rej) pred .*? dRho2 (\S+) ',log,re.M)if flag=='ACC']
 checks['displayed_mesh_sum']=str(sum(vals,Decimal(0)))==own['FLOAT_sum_accepted_rounded_mesh_steps']==peer['FLOAT_sum_accepted_rounded_mesh_steps']=='0.08387595'
 checks['logged_snapshot_and_structure']=own['raw_sha256']in log and all(x in log for x in ['generators 2918','pair rows 81 weight','constraint rows 421','midpoint 180, middle 16'])
 source=text('N1_run_quot.py');impl=text('N1_ipm_opt3.py');ast.parse(source);ast.parse(impl)
 checks['source_row_propagation']=all(x in source for x in ['pair_k=PAIRK','wpair=WLIST','[WPAIR]*(len(PAIRK)-NHELD) + [WHELD]*NHELD'])and 'for q, w in zip(self.pair_k, ws)'in impl and 'phi_(n,K)'in impl
 public={(n,k)for n in (19,23,25,29,31)for k in (600,900,1200,1800,2400)};probes=public|{(n,(n-1)//2+s)for n in range(19,32,2)for s in (0,8,32)}
 checks['all46_same_mode_span_separations']=len(probes)==46 and probes==set(map(tuple,peer['outside_analytic_span']))=={(w['n'],w['K'])for w in own['probe_rows']}and all(n%2 and 2*k+1>=n and k not in [q for j,q in rows if j==n]for n,k in probes)
 checks['public25_register']=public==set(map(tuple,text('register.json')['pairs']))
 manifest=text('snapshot_manifest.json');checks['two_manifest_descriptions_truncated']=manifest['basis']['description'].endswith('at weight ')and manifest['loss']['definition'].endswith('at weight ')
 checks['heldout_current_hash']=sha256(text('N1_HELDOUT_025.md').encode()).hexdigest()==own['heldout_current_sha256']==peer['heldout_sha256']
 checks['public_registration_earlier']=datetime.fromisoformat(text('register.json')['utc'])<datetime.fromisoformat(own['publisher_recorded_launch_utc'])<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 checks['peer_complete_check_count']=len(peer['checks'])==peer['check_count']==554
 checks['no_foreign_code_execution']=not peer['publisher_code_executed']and not own['foreign_code_executed']
 assert all(checks.values()),{k:v for k,v in checks.items()if not v}
 for rel,h in ownbindings.items():assert sha(R/rel)==h
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'own_inputs':ownbindings,'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'raw_sha256':own['raw_sha256'],'potential_dimension':2918,'density_dimension':2918,'current_rows':rows,'objective_weights_exact':weights,'outside_current_analytic_span':sorted(probes),'Laurent_witnesses':records,'cross_poles':crossrecords,'recorded_iterations':iterations,'historical_scope':'Current actual025 and recorded016-to025 stage; accepted earlier rank dependencies; no new independent historical observation','literal_step_scope_qualification':'Peer JSON says projection excluded; only initial projection is excluded, per-step Taylor projection is included as the bound own/peer proofs state; rounded mesh sum is not a density bound','foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED independent actual025 shape dimension,348 Laurent witnesses,81 rows and46 outside probes; two manifest descriptions incomplete; projection wording requires initial-only qualification'}
 with (B/'verification/result.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],'CONFIRMED025shape',len(checks),len(bindings),sha(B/'verification/result.json'),out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
