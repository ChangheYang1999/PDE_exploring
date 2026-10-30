from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip,sys,time
from flint import arb,ctx,fmpq as Q
R=Path(__file__).resolve().parents[3];B=R/'research/dyadic010_and_01523_review';T=R.parent/'c1-t4/research'
sys.set_int_max_str_digits(0);ctx.prec=2048
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=Q(q);return arb(q.numerator)/q.denominator
known={};frozen={};bindings={}
previous=json.loads((R/'research/candidate015_peer_review/verification/result.json').read_text())
for local,v in previous['frozen_or_retained_sources'].items():
 p=R/local;assert sha(p)==v['stored_sha256'];known[v['sha256']]=(p,v['gzip'])
for p in [R/'research/candidate_audits/data/C1-N1-010-d2w-j7-x3bal-legqs/d2w_j7_n4_X3bal_legqs_mid180_exact.json',*list((R/'research/scaled_dyadic_probes/verification/C1-N1-010-d2w-j7-x3bal-legqs').glob('*.json')),R/'research/scaled_factored_weak/verification/C1-N1-015-pairQ-quot013_n023_K00600.json']:
 known[sha(p)]=(p,False)
def freeze(p,h=None):
 p=Path(p);data=p.read_bytes();digest=sha256(data).hexdigest();assert h is None or h==digest,(str(p),digest,h)
 if digest in known:
  dest,compressed=known[digest];localdata=gzip.decompress(dest.read_bytes()) if compressed else dest.read_bytes();assert localdata==data
 else:
  dest=B/'source'/p.relative_to(T);compressed=len(data)>1000000
  if compressed:dest=dest.with_name(dest.name+'.gz')
  dest.parent.mkdir(parents=True,exist_ok=True);encoded=gzip.compress(data,compresslevel=6,mtime=0) if compressed else data
  if dest.exists():assert dest.read_bytes()==encoded
  else:
   with dest.open('xb') as f:f.write(encoded)
  known[digest]=(dest,compressed)
 frozen[str(dest.relative_to(R))]={'original':str(p),'sha256':digest,'stored_sha256':sha(dest),'gzip':compressed};bindings[str(p)]=digest
 return json.loads(data) if p.suffix=='.json' else None

def save(name,data,start,inputs):
 data.update({'utc':datetime.now(timezone.utc).isoformat(),'frozen_or_retained_sources':frozen.copy(),'peer_bindings':bindings.copy(),'own_inputs':{str(p.relative_to(R)):sha(p) for p in [Path(__file__),B/'PROOF.md',*inputs]},'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start})
 p=B/'verification'/name
 with p.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
 print(name,sha(p),data['elapsed_seconds'],flush=True)

def dyadic():
 start=time.monotonic();P=T/'scaled_dyadic_reproduction';ownbase=R/'research/scaled_dyadic_probes/verification/C1-N1-010-d2w-j7-x3bal-legqs';op=ownbase/'result_modes_001_003.json';own=json.loads(op.read_text());peer=freeze(P/'verification/result.json')
 for p,h in peer['inputs'].items():freeze(p,h)
 fd=freeze(P/'source/FROZEN.json')
 for rel,item in fd['files'].items():freeze(P/rel,item['sha256'])
 checks={'candidate':own['candidate']==peer['candidate'],'origin':peer['origin_identities_exact'],'point_checks':all(peer['point_checks'].values()),'all_cells_flag':peer['all_seven_excluded']};energies={};inputs=[op,R/'research/scaled_dyadic_probes/PROOF.md']
 for n in [1,3]:
  pp=P/f'verification/mode_{n:03}.json';z=freeze(pp,peer['mode_hashes'][str(n)]);ref=ownbase/f'mode_{n:03}.json';o=json.loads(ref.read_text());assert sha(ref)==own['mode_result_sha256'][str(n)]==z['peer_sha256'];inputs.append(ref)
  for p,h in z['inputs'].items():freeze(p,h)
  checks[f'{n}_endpoints']=all(Q(row['margin'])>0 for row in z['endpoint'])
  checks[f'{n}_crt']=all(row['exact_CRT_replay'] for row in z['CRT_records'])
  checks[f'{n}_precision']=z['minimum_bits']>150
  assert len(z['weights'])==len(o['weights'])==8;energies[n]={}
  for k,(r,s) in enumerate(zip(z['weights'],o['weights'],strict=True)):
   a=Q(k,4);checks[f'{n}_{k}_a']=Q(r['a'])==Q(s['a'])==a
   for key in ['energy','norm']:checks[f'{n}_{k}_{key}']=arb(r[key]).overlaps(arb(s[key]))
   checks[f'{n}_{k}_sqrt']=arb(r['energy']).sqrt().overlaps(arb(r['norm']))
   energies[n][a]=arb(r['energy'])
 c=Q(4076476460239181,2251799813685248);d=c-1;s=(ar(2*d-3)+ar((2*d-3)**2+16*d).sqrt())/8;H=(ar(d)-s)*(4*arb.pi()*s*(1+s)).sqrt()
 checks['maximizer']=0<s and s<ar(d) and s.overlaps(arb(own['s_maximizer'])) and s.overlaps(arb(peer['s_maximizer']))
 checks['H']=H.overlaps(arb(peer['H_max'])) and H.overlaps(arb(own['H_max']))
 edges=[Q(k,4) for k in range(7)]+[1+1/c];cells=[]
 for k,(o,p) in enumerate(zip(own['seven_cells'],peer['seven_cells'],strict=True)):
  l,h=edges[k:k+2];e=Q(k+1,4);checks[f'cell{k}_exact']=Q(o['left'])==Q(p['left'])==l and Q(o['right'])==Q(p['right'])==h and Q(o['norm_evaluation_at'])==Q(p['norm_evaluation_at'])==e and e>=h
  J=(energies[1][e]+energies[3][e]).sqrt();lower=arb(5)**ar((l-2)/2)*J;upper=H*ar((1+c-c*l)/(1+l));vals={'projected_norm':J,'lower':lower,'upper':upper,'gap':lower-upper,'ratio':lower/upper}
  for key,v in vals.items():checks[f'cell{k}_{key}']=v.overlaps(arb(o[key])) and v.overlaps(arb(p[key]))
  checks[f'cell{k}_strict']=vals['gap']>0 and vals['ratio']>ar(o['strict_ratio_floor']) and Q(o['strict_ratio_floor'])==Q(p['strict_ratio_floor'])
  cells.append({**{key:v.str(100) for key,v in vals.items()},'strict_ratio_floor':o['strict_ratio_floor']})
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 save('dyadic010.json',{'candidate':own['candidate'],'checks':checks,'seven_cells':cells,'precision_bits':ctx.prec,'claim':'CONFIRMED N4-231 through T4-303; conditional scheme exclusion under complete proof hypotheses','minimum_strict_ratio_floor':str(min(Q(p['strict_ratio_floor']) for p in own['seven_cells']))},start,inputs)

def weak():
 start=time.monotonic();P=T/'candidate015_heldout23';pp=P/'verification/015_n23_k600.json';p=freeze(pp);a=freeze(P/'verification/ACCEPTANCE.json');op=R/'research/scaled_factored_weak/verification/C1-N1-015-pairQ-quot013_n023_K00600.json';o=json.loads(op.read_text())
 for path,h in a['inputs'].items():freeze(path,h)
 paths={'source_sha256':T/'new_successor_weak/data/015/canonical.json','build_sha256':T/'new_successor_weak/verification/015_build.json','proof_sha256':P/'PROOF.md','code_sha256':P/'code/check.py','helper_sha256':T/'localized_probe_audit/code/reproduce.py','probe_sha256':P/'data/probe_23_600.json'}
 for key,path in paths.items():freeze(path,p[key])
 checks={'n_K':p['angular_mode']==o['n']==23 and p['radial_power']==o['K']==600,'raw_canonical_identity':previous['checks']['exact_canonical_maps'] and previous['checks']['canonical_raw_identity'],'same_canonical_source':p['source_sha256'] in known,'direct_parts':p['direct_parts_overlap'] and o['direct_parts_overlap'],'endpoints':Q(p['minimum_endpoint_exponent'])>-1,'peer_flags':all(a['checks'].values())}
 for key in ['pairing','pairing_by_parts','M','C','D']:checks[key]=arb(p[key]).overlaps(arb(o[key]))
 for key,old in [('normM2','M2'),('normC2','C2')]:checks[key]=arb(p[key]).overlaps(arb(o[old]))
 H=Q(o['H_upper_exact']);checks['H_caps']=all(arb(cap)<ar(H) for cap in p['sup_certificate']['amplitude_caps'])
 I=abs(arb(p['pairing']));D=arb(p['D']);root=2*I/(D+(D*D+4*ar(H)*I).sqrt());floor=Q(o['strict_lower_exact'])
 checks['root']=root.overlaps(arb(o['radius'])) and root.overlaps(arb(a['radius_with_peer_H']))
 checks['strict_floor']=root>ar(floor) and floor==Q(a['peer_strict_floor_independently_verified'])==Q(1232449584356253,10**18)
 checks['exceeds_graded']=floor>Q(25,54684)
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 save('weak015_n23_K600.json',{'candidate':o['candidate'],'n':23,'K':600,'checks':checks,'root':root.str(100),'strict_lower_exact':str(floor),'precision_bits':ctx.prec,'claim':'CONFIRMED n23K600 part of N4-237 through T4-304; necessary distance only'},start,[op,R/'research/candidate015_peer_review/verification/result.json',R/'research/candidate015_holdout/verification/result.json'])

if __name__=='__main__':dyadic();weak()
