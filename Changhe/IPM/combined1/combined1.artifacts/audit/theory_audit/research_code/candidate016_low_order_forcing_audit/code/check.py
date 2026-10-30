"""Finite independent audit; accepted moment integrals are not recomputed."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, time
from flint import arb, ctx
B=Path(__file__).resolve().parents[1]; ctx.prec=1024; start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads((B/p).read_text())
checks=[]
def require(name,test,value=None):
 assert bool(test),(name,str(value))
 checks.append({'claim':name,'value':None if value is None else str(value)})
def ar(x):
 x=Q(x);return arb(x.numerator)/x.denominator
m=read('data/manifest.json');require('proof first',m['proof_written_before_checker'])
for rel,h in m['inputs'].items():require('frozen '+rel,sha(B/rel)==h)
for z in read('data/input_sources.json')['inputs']:require('copied '+z['local'],sha(B/z['local'])==z['sha256'])
p=read('data/parameters.json');comp=read('data/components.json');peer=read('source/N4_result.json');acc=read('source/G1_acceptance.json');partial=read('source/N4_partial.json');assembly=read('source/assembly_result.json');att=read('verification/PEER_SOURCE_ATTESTATION.json')
require('59 peer sources attested',len(att['hashes'])==59 and att['all_59_hashes_match'] and att['hashes']==peer['inputs'] and att['peer_result_sha256']==sha(B/'source/N4_result.json'))
require('accepted component record',sha(B/'source/G1_acceptance.json')==comp['accepted_record_sha256'] and acc['verdict'].startswith('CONFIRMED') and all(acc['checks'].values()))
require('recorded c',Q(partial['cl_exact'])==Q(4076476460239181,2251799813685248))
for label,z in [('parameters',p),('components',comp),('peer',peer),('acceptance',acc),('partial',partial),('source formula',assembly)]:
 require(label+' candidate',z['candidate']=='C1-N1-016-legqs25-quot013')
 require(label+' raw',z['raw_sha256']=='a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
low={};norms={}
for key,pairs,minbits in [('G0',14960,1739),('G1',30176,1730)]:
 c=comp['components'][key];a=acc['norms'][key];n=partial['norms'][key];lo=Q(c['lower_exact']);hi=Q(c['upper_exact']);low[key]=lo
 require(key+' exact endpoints',0<lo==Q(a['accepted_lower_exact']) and hi==Q(a['accepted_upper_exact']) and lo<hi)
 balls=[arb(n['norm_lower_ball']),arb(n['norm_upper_ball']),arb(a['own_lower_ball']),arb(a['own_upper_ball'])]
 for i,b in enumerate(balls):
  require(key+' strict enclosure '+str(i),ar(lo)<b.lower() and ar(hi)>b.upper())
  require(key+' N3 lower containment '+str(i),arb(a['peer_lower_ball']).contains(b))
  require(key+' N3 upper containment '+str(i),arb(a['peer_upper_ball']).contains(b))
 require(key+' whole-plane record',a['whole_plane_no_quadrature'] and partial['no_spatial_quadrature'])
 require(key+' all groups',len(n['groups'])==n['complete_group_count']==a['own_groups']==31 and a['peer_groups']==142)
 require(key+' ordered pair count',n['ordered_pair_count']==a['ordered_pair_count']==pairs)
 require(key+' precision',min(g['integral_accuracy_bits'] for g in n['groups'])==a['minimum_integral_accuracy_bits']==minbits)
 for i,g in enumerate(n['groups']):
  require(key+' integrable group '+str(i),Q(g['b'])>-1)
  require(key+' group reconstruction '+str(i),g['decomposition']['exact_reconstruction'])
 summed=sum((arb(g['integral_ball']) for g in n['groups']),arb(0))
 require(key+' saved sum',summed.overlaps(arb(n['S_ball'])))
 square=arb.pi()*summed/2
 for kind in ['square_lower_ball','square_upper_ball']:require(key+' square '+kind,square.overlaps(arb(n[kind])))
 require(key+' positive square',square>0)
 require(key+' independent norm',square.sqrt().overlaps(balls[0]) and square.sqrt().overlaps(balls[1]))
 norms[key]={'from_saved_moments':square.sqrt().str(100),'accepted_lower':str(lo),'accepted_upper':str(hi),'groups':31,'minimum_recorded_accuracy_bits':minbits}
specs=[(name,'Ns',s,16384,262144,t) for name,s,t,_ in p['Ns']]
name,s,t,_=p['legacy_X3'];specs.append((name,'X3',s,16384,262144,t))
specs.extend((name,'XSW',s,w1,w2,t) for name,s,w1,w2,_,t in p['XSW'])
require('ten distinct rows',len(specs)==len({z[0] for z in specs})==10)
old={z['framework']:z for z in assembly['instances']};other={z['framework']:z for z in peer['instances']};rows=[]
for name,kind,s,w1,w2,t in specs:
 s,t=Q(s),Q(t);a=old[name];n=other[name]
 require(name+' positive inputs',s>=0 and t>0 and w1>0 and w2>0)
 require(name+' source instance',(a['kind'],Q(a['s_exact']),Q(a['threshold_exact']))==(kind,s,t))
 if kind=='XSW':require(name+' source weights',a['weights']==[w1,w2])
 require(name+' N4 instance',(n['kind'],Q(n['s_exact']),Q(n['sufficient_threshold_exact']),n['weights'])==(kind,s,t,[w1,w2]))
 square=w1*low['G1']**2+w2*low['G0']**2;energy=ar(square).sqrt();ratio=energy/ar(t)
 require(name+' rational square',square==Q(n['low_order_square_exact']))
 require(name+' independent square root overlap',energy.overlaps(arb(n['forcing_lower_comparison']['ball'])))
 require(name+' independent ratio overlap',ratio.overlaps(arb(n['threshold_ratio_lower_comparison']['ball'])))
 require(name+' strict forcing floor',energy>ar(n['forcing_lower_comparison']['strict_lower_exact']))
 require(name+' strict integer factor',ratio>ar(n['threshold_ratio_lower_comparison']['strict_lower_exact'])>1)
 require(name+' sufficient test fails',energy>ar(t) and n['sufficient_smallness_condition_fails'])
 rows.append({'framework':name,'kind':kind,'s_exact':str(s),'weights':[w1,w2],'threshold_exact':str(t),'square_exact':str(square),'forcing':energy.str(100),'factor':ratio.str(100),'strict_forcing_lower_exact':n['forcing_lower_comparison']['strict_lower_exact'],'strict_integer_factor':n['threshold_ratio_lower_comparison']['strict_lower_exact']})
require('exact rebalanced source threshold',Q(p['Ns'][2][2])==Q(3,327680))
require('exact legacy source threshold',Q(p['legacy_X3'][2])==Q(1,163840))
for rel,h in m['inputs'].items():require('unchanged '+rel,sha(B/rel)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'peer_sha256':sha(B/'source/N4_result.json'),'norm_consistency':norms,'instances':rows,'candidate_integrals_repeated':False,'foreign_code_executed':False,'verdict':'CONFIRMED inequality and all ten sufficient scalar forcing failures, using accepted N3/N4 H1 components; no correction-distance or dyadic implication'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['utc'],out['elapsed_seconds'])
for z in rows:print(z['framework'],'factor >',z['strict_integer_factor'])
