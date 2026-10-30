"""Independent analytic-fixture, directed-composition, and review provenance audit."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
from math import factorial
import importlib.util,json,sys,time,os
from flint import arb,ctx,fmpq
R=Path(__file__).resolve().parents[3];B=R/'research/partial_hardy_opus_reciprocal';S=B/'source'
sys.set_int_max_str_digits(0)
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};external={};checks={};ctx.prec=1024
 def ck(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 def bind(p,h=None):
  p=Path(p).resolve();v=sha(p);assert h is None or v==h,(str(p),h,v)
  try:k=str(p.relative_to(R));d=inputs
  except ValueError:k=str(p);d=external
  assert k not in d or d[k]==v;d[k]=v;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 def accepted(p,h):
  d=read(p,h);ck('accepted:'+str(p.relative_to(R)),all(d['checks'].values()) and d['check_count']==len(d['checks']))
  for k,v in d.get('inputs',{}).items():bind(R/k,v)
  return d
 mf=read(S/'MANIFEST.json');ck('proof_first',not mf['checker_exists']);bind(B/'PROOF.md',mf['proof_sha256']);bind(Path(__file__))
 for row in mf['files'].values():bind(R/row['path'],row['sha256']);bind(row['source'],row['sha256'])
 for name,topic in [('T4_accept_manifest.json','partial_hardy_review_acceptance'),('T4_prefix31_manifest.json','candidate016_prefix31_hardy_audit')]:
  for row in read(S/name):bind(R.parent/'c1-t4/research'/topic/row['local'],row['sha256'])
 peer=read(S/'T4_accept_result.json','a5b3659c90eaf13bbe068e64a72c056a21f2307446d7ea9c2639e598a9d8ca78');t2=read(S/'T2_result.json');p=read(S/'parameters.json');general=read(S/'T4_general_result.json');fx=read(S/'T4_general_parameters.json')
 ck('263peer_checks',peer['check_count']==len(peer['checks'])==263 and all(isinstance(x,str) and x for x in peer['checks']))
 revision=read(B/'verification/PROOF_FIRST_v02.json');ck('revision_proof_first',not revision['checker_v02_exists']);bind(B/'PROOF_v02.md',revision['proof_sha256']);bind(B/'verification/FAILED_v01.json',revision['failed_record_sha256'])
 ck('35T2checks',t2['checks']==35 and not t2['fails'])
 ck('T1primary_log',"checks passed 4783 ; elapsed 7.1 s" in (S/'T1_log.txt').read_text() and (S/'T1_log.txt').read_text().rstrip().endswith('RESULT PASS'))
 ck('both_review_counts',peer['peer_counts']==[4783,35])
 for key,fn in [('proof_sha256','T4_accept_PROOF.md'),('checker_sha256','T4_accept_check.py'),('manifest_sha256','T4_accept_manifest.json')]:ck('acceptance_root_'+key,peer[key]==sha(S/fn))
 for block in ['A','G']:
  for k,v in t2[block]['inputs'].items():bind(R.parent/k,v)
 # Independently coded coefficient comparisons and outward-interval identity.
 def coef(N,n):return max(Q(1,N*N),Q(1,n*n))
 for N in p['odd_cuts']:
  for n in range(1,4*N+8,2):
   c=coef(N,n);ck(f'coefficient:{N}:{n}',0<=c-Q(1,n*n)<=Q(1,N*N) and coef(N+2,n)-c==(Q(1,(N+2)**2)-Q(1,N*N) if n>N else 0))
 for row in fx['fixtures']:
  E={int(n):Q(v) for n,v in row['energies'].items()};total=sum(E.values(),Q(0));M=sum((v/n**2 for n,v in E.items()),Q(0));prior=None
  found=next(q for q in general['fixtures'] if q['name']==row['name']);ck('fixture_total:'+row['name'],Q(found['S'])==total and Q(found['M2'])==M)
  for rec in found['prefixes']:
   N=rec['N'];C=sum((coef(N,n)*v for n,v in E.items()),Q(0));U=total+Q(1,97);lo={n:max(v-Q(1,83),Q(0)) for n,v in E.items()};up={n:v+Q(1,89) for n,v in E.items()}
   P=U/N**2+sum(((Q(1,n*n)-Q(1,N*N))*up[n] for n in E if n<N),Q(0));T=sum((up[n]/n**2 for n in E if n<N),Q(0))+(U-sum((lo[n] for n in E if n<N),Q(0)))/N**2
   ck(f'fixture_bound:{row["name"]}:{N}',M<=C==Q(rec['B_N']) and 0<=C-M==Q(rec['loss'])<=total/N**2 and (prior is None or C<=prior) and C<=P<=T and T-P==sum((up[n]-lo[n] for n in E if n<N),Q(0))/N**2);prior=C
 E={1:Q(1),3:Q(2),5:Q(3)};U=sum(E.values())+1;N=5
 P=U/N**2+sum(((Q(1,n*n)-Q(1,N*N))*v for n,v in E.items() if n<N),Q(0));T=sum((v/n**2 for n,v in E.items() if n<N),Q(0))+(U-sum((v for n,v in E.items() if n<N),Q(0)))/N**2
 ck('equality_does_not_need_exact_total',P==T and U>sum(E.values()))
 ck('tail_cannot_be_zero',Q(1,25)>0)
 # Own half-integer Gamma arithmetic: value = rational * pi^(power/2).
 def gammahalf(k):
  assert k>0
  if k%2==0:return Q(factorial(k//2-1)),0
  m=(k-1)//2;return Q(factorial(2*m),4**m*factorial(m)),1
 def beta2(a,b):
  x,i=gammahalf(a);y,j=gammahalf(b);z,k=gammahalf(a+b);return x*y/z,i+j-k
 pairs=[]
 for idx,terms in enumerate(p['polynomials']):
  val=Q(0)
  for i,j,c in terms:
   if i%2 or j%2==0:continue
   A,e=beta2(j+1,i+1);C,f=beta2(i+j+2,12-i-j);ck(f'beta_power:{idx}:{i}:{j}',e+f==2);val-=Q(c)*A*C
  ck('infinite_pairing:'+str(idx),val==Q(p['pairings_over_pi'][idx]));pairs.append(str(val))
 helper=bind(R/'research/candidate016_upper_opus_primary/code/check_v02.py','ae63d919f60b458b074df764cf7f94e35109a13e9828fe8949c0ccbb29b30eeb')
 spec=importlib.util.spec_from_file_location('own_fixture474',helper);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
 fixtures={}
 for n,b,A in [(1,h.Q(3,2),h.P([1])),(3,h.Q(2),h.T)]:
  e,F=h.source(n,b,A);vals={'S':n*n*h.mass(n,e,F),'d':h.energy(n,b,A,b,A),'a':h.energy(n,b,A,b,A,'a'),'b':h.pair(n,e,F,b,A)}
  for k,v in vals.items():ck(f'known_source:{n}:{k}',Q(str(v))==Q(t2['E'][str(n)][k]))
  ck('source_equality:'+str(n),vals['b']==-vals['a'] and vals['S']/n**2-vals['a']==vals['d']);fixtures[str(n)]={k:str(v) for k,v in vals.items()}
 # Euler derivative gives 1-12t+15t^2. Integrate t^(1/2)(1-t)^2 polynomial exactly.
 poly=h.D(h.Q(3,2),h.D(h.Q(3,2),h.P([1])));ck('D2profile',list(poly)==[1,-12,15]);cross=2*sum((Q(str(c))/Q(2*j+3,2) for j,c in enumerate(poly*h.W**2)),Q(0))
 ck('infinite_cross',cross==Q(-256,1155)==Q(peer['infinite_source_exact_cross']))
 pi=arb.pi();prev=None
 for N in p['odd_cuts']:
  p2=sum((Q(1,n*n) for n in range(1,N,2)),Q(0));p4=sum((Q(1,n**4) for n in range(1,N,2)),Q(0));a=lambda v:arb(fmpq(v.numerator,v.denominator));Sinf=pi/20;Minf=pi**3/240;BN=Sinf/N**2+2/(5*pi)*(a(p4)-a(p2)/N**2)
  ck('infinite_prefix:'+str(N),(BN-Minf)>0 and (Sinf/N**2-(BN-Minf))>0 and (prev is None or prev>BN));prev=BN
 norm=accepted(R/'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json','a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc')
 own7=accepted(R/'research/candidate016_angular_tail_bound/verification/result_v01.json','8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1')
 own31=accepted(R/'research/candidate016_angular_tail_bound/verification/result_v02.json','01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41')
 upper=accepted(R/'research/candidate016_reviewed_upper/verification/result.json','d50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0')
 crossr=accepted(R/'research/candidate016_solenoidal_upper/verification/result.json','e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603')
 # This path is source-bound through own reviewed upper; no imported peer module executes.
 tp=read(S/'T4_prefix31_result.json','ab005a62f3e3c27385ac50a1d1148879b5f9e8eccd0bcab0ec0b6f390b746cd1')
 ck('prefix31_peer_count',tp['check_count']==len(tp['checks'])==4463 and tp['group_count']==484)
 U={k:Q(v['accepted_upper_exact']) for k,v in norm['norms'].items()};L={k:Q(v['accepted_lower_exact']) for k,v in norm['norms'].items()};J=Q(crossr['improvement_sum_strict_lower_exact']);computed={}
 for label,d,N in [('own7',own7,9),('own31',own31,33),('peer31',tp,33)]:
  ck(label+':complete_prefix',[v['n'] for v in d['modes']]==list(range(1,N,2)) and d['raw_sha256']==norm['raw_sha256'])
  ql=sum((Q(v['q_lower_exact']) for v in d['modes']),Q(0));qu=sum((Q(v['q_upper_exact']) for v in d['modes']),Q(0));P=U['rF']**2/N**2+sum(((Q(1,v['n']**2)-Q(1,N*N))*Q(v['q_upper_exact']) for v in d['modes']),Q(0));T=sum((Q(v['q_upper_exact'])/v['n']**2 for v in d['modes']),Q(0))+(U['rF']**2-ql)/N**2
  ck(label+':positive_formula',P==Q(d['M2_upper_exact']) and T-P==(qu-ql)/N**2>0 and U['rF']**2-ql==Q(d['tail_rF_square_upper_exact'])>0)
  I=P-J;EU=U['P2']**2+2**14*U['G1']**2+2**18*U['G0']**2+Q(20,21)*2**18*I
  ck(label+':cross_and_energy',I==Q(d['improved_H_square_upper_exact']) and EU==Q(d['E2_upper_square_exact' if label=='peer31' else 'conditional_E2_upper_square_exact']))
  ck(label+':coarse_bounds',I<Q('.944107' if N==9 else '.619652')**2 and P<Q('1.063013' if N==9 else '.789068')**2 and EU<Q('722.968760' if N==9 else '629.296113')**2)
  computed[label]={'M2':str(P),'H_square_upper':str(I),'E2_square_upper':str(EU)}
 for a,b in zip(own31['modes'],tp['modes']):ck('peer31_contained:'+str(a['n']),Q(a['q_lower_exact'])<=Q(b['q_lower_exact'])<=Q(b['q_upper_exact'])<=Q(a['q_upper_exact']))
 ck('reviewed_upper_unchanged',Q(upper['H_upper_square_exact'])==Q(computed['own31']['H_square_upper']) and Q(upper['E2_upper_square_exact'])==Q(computed['own31']['E2_square_upper']))
 repairs=[]
 for row in p['display_attributions']:
  actual=Q(own7[row['source_key']]);display=Q(row['display']);shown=display if row['kind']=='direct' else display**2;k={'M2':'M2_upper','plain_H':'plain_H_upper','improved_H':'improved_H_upper'}[row['name']];safe=Q(p['directed_repairs'][k]);safevalue=safe if row['kind']=='direct' else safe**2
  ck('rounding_attribution:'+row['name'],shown<actual<safevalue);repairs.append({'name':row['name'],'inward_deficit_exact':str(actual-shown),'safe_display':str(safe)})
 ck('total_square_display',Q('51.061045287604983')<L['rF']**2<U['rF']**2 and Q(p['directed_repairs']['S_lower'])<L['rF']**2<U['rF']**2<Q(p['directed_repairs']['S_upper']))
 for rel,v in inputs.items():assert sha(R/rel)==v
 for rel,v in external.items():assert sha(rel)==v
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'inputs':inputs,'external_inputs':external,'own_exact_fixtures':fixtures,'infinite_pairings_over_pi':pairs,'infinite_source_cross_exact':str(cross),'computed_uppers':computed,'rounding_repairs':repairs,'source_integrals_recomputed_here':False,'peer_code_executed':False,'full_source_omitted_modes_retained':True,'configured_peer_model':'us.anthropic.claude-opus-5-5','actual_provider_response_observed':False,'verdict':'CONFIRMED both Opus general474 reviews and T4-481/T4-480 reciprocal exact compositions. REFUTED inward rounding attribution in original R1-050 V7, with coarse bounds preserved. No new candidate norm, inverse, existence or correction-distance ordering.'}
 target=B/'verification/result.json'
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],len(checks),'checks',len(inputs),'local',len(external),'external bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
