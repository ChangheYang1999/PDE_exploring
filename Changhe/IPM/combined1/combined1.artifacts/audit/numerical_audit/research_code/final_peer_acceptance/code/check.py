"""Finite reciprocal comparisons. No foreign program or source integral executes."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json,re,sys,time,os
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/final_peer_acceptance'
assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
start=time.monotonic();inputs={};external={};checks={}
def sha(p):return sha256(p.read_bytes()).hexdigest()
def need(k,v):
 assert k not in checks,k
 assert v,k
 checks[k]=True
def bind(p,expected=None):
 p=p.resolve();h=sha(p);key=str(p.relative_to(R)) if p.is_relative_to(R) else str(p)
 mapping=inputs if p.is_relative_to(R) else external
 if key in mapping:
  assert mapping[key]==h and (expected is None or expected==h),(key,'binding changed')
  return
 need('hash '+key,expected is None or h==expected);mapping[key]=h
def load(p):
 p=R/p if isinstance(p,str) else p;bind(p);return json.loads(p.read_text())
mf=load(B/'source/MANIFEST.json')
need('proof first',not mf['checker_exists'] and not mf['result_exists'] and sha(B/'PROOF.md')==mf['proof_sha256'])
for p,h in mf['files'].items():bind(R/p,h)
for p in [B/'PROOF.md',Path(__file__)]:bind(p)
t=load(B/'source/T4_result.json');m=load(B/'source/T4_manifest.json')
need('T4 all57declared manifest bindings',len(m)==57)
for row in m:bind(Path(mf['T4_base'])/row['local'],row['sha256'])
p=load('research/candidate016_angular_tail_bound/verification/result_v05.json')
c=load('research/candidate016_multimode_complete_bounds/verification/result_v03.json')
o=load('research/candidate017_opus_residual_review/verification/result.json')
b=load('research/negative_norm_forcing_assembly/verification/result.json')
x=load(B/'source/T4_external.json')
xm={z['source']:z['sha256'] for z in x['rows']}
need('361peer producer bindings',len(xm)==len(c['inputs'])==361)
for rel,h in c['inputs'].items():
 bind(R/rel,h);need('T4 same producer '+rel,xm[str(R/rel)]==h)
for rel,h in p['inputs'].items():bind(R/rel,h)
for rel,h in o['inputs'].items():bind(R/rel,h)
for name,d,n in [('T4',t,7564),('430',p,3921),('431',c,4446),('432',o,2290)]:
 need(name+' count',d['check_count']==len(d['checks'])==n)
 if isinstance(d['checks'],dict):need(name+' all passed',all(d['checks'].values()))
for key,value in [('candidate','C1-N1-016-legqs25-quot013'),('raw_sha256','a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')]:
 need('identity '+key,t[key]==p[key]==c[key]==value)
need('full160source support',t['complete_field_mode_count']==p['complete_field_mode_count']==160 and t['complete_field_component_count']==p['complete_field_component_count']==1360)
need('128tail retained',t['prefix']==p['prefix']==c['prefix']==63 and t['individually_integrated_modes']==c['individually_integrated_Hardy_modes']==32 and t['omitted_modes_retained']==160-32==128 and p['smallest_omitted_mode']==65 and p['complete_uncomputed_tail_retained'] and c['all160_source_modes_covered'])
need('all32distinct modes',[r['n'] for r in t['modes']]==[r['n'] for r in p['modes']]==list(range(1,64,2)))
S=Q(p['full_rF_square_upper_exact']);V=S/65**2;V0=V;delta=Q(0);groups=0
for a,z in zip(p['modes'],t['modes']):
 n=a['n'];lo,up=[Q(a[k]) for k in ['q_lower_exact','q_upper_exact']];v,w=[Q(z[k]) for k in ['q_lower_exact','q_upper_exact']]
 need(f'n{n} containing rational intervals',0<lo<=v<=w<=up)
 need(f'n{n} same groups',a['group_count']==z['group_count']>0)
 weight=Q(1,n*n)-Q(1,65**2);need(f'n{n} positive weight',weight>0)
 V+=weight*up;V0+=weight*w;delta+=weight*(up-w);groups+=a['group_count']
need('all920groups',groups==t['group_count']==920)
need('same complete upper',V==Q(p['M2_upper_exact'])==Q(c['complete_M2_upper_exact'])==Q(t['M2_producer_upper_exact']))
need('same tighter peer upper',V0==Q(t['M2_independent_upper_exact']))
need('exact tiny nonnegative difference',V-V0==delta==Q(t['producer_minus_independent_upper_exact']) and 0<=delta<Q(1,10**500))
L=sum((Q(r['selected_lower'])**2 for r in c['selected_modes']),Q(0));J=sum((Q(r['selected_improvement']) for r in c['selected_modes']),Q(0))
need('16distinct trials',[r['n'] for r in c['selected_modes']]==list(range(1,32,2)))
need('source trial coverage',c['pairing_group_count']==2130 and c['general_and_tail_reviews_completed'])
need('same dual lower',L==Q(c['H_lower_square_exact'])==Q(t['H_lower_square_exact'])==Q(p['H_lower_square_exact']))
need('same improvement',J==Q(c['selected_improvement_sum_lower_exact'])==Q(p['selected_improvement_sum_lower_exact']))
need('same producer upper square',V-J==Q(c['H_upper_square_exact'])==Q(t['H_upper_square_exact']))
need('same peer upper square',V0-J==Q(t['H_independent_upper_square_exact']) and L<V0-J<=V-J)
need('E2 lower identity',Q(c['E2_lower_square_exact'])==Q(t['E2_lower_square_exact']))
need('E2 exact upper difference',Q(c['E2_upper_square_exact'])==Q(t['E2_upper_square_exact']) and Q(t['E2_upper_square_exact'])-Q(t['E2_independent_upper_square_exact'])==Q(20,21)*2**18*delta)
for norm in ['H','E2']:
 for side in ['lower','upper']:
  k=norm+'_strict_'+side+'_exact';need('same '+k,Q(c[k])==Q(t[k]))
 lo,up=[Q(c[norm+'_strict_'+s+'_exact']) for s in ['lower','upper']]
 need(norm+' strict positive squares',0<lo*lo<Q(c[norm+'_lower_square_exact'])<Q(c[norm+'_upper_square_exact'])<up*up)
match=re.fullmatch(r'\[([^ ]+) \+/- ([^ ]+)\]',b['H_input_lower_ball']);need('007 containing H ball',match is not None)
hgap=Q(match[1])-Q(match[2])-Q(c['H_strict_upper_exact']);egap=Q(c['E2_strict_lower_exact'])-Q(b['E_upper']['strict_upper_exact'])
need('H gap',hgap==Q(t['strict_H_gap_lower'])==Q(c['H007_minus_H016_strict_lower_exact'])>Q('.017627007636152781'))
need('E2 gap',egap==Q(t['strict_E2_gap_lower'])==Q(c['E2016_minus_E2007_strict_lower_exact'])==Q('21.759869526341'))
need('outward complete016 displays',Q('.6167335007')<Q(c['H_strict_lower_exact'])<Q(c['H_strict_upper_exact'])<Q('.617897369') and Q('628.580088526341')==Q(c['E2_strict_lower_exact'])<Q(c['E2_strict_upper_exact'])<Q('628.865389'))
err=(B/'source/T4_erratum.md').read_text();need('T4 count erratum explicit','136 omitted modes' in err and '128 omitted modes' in err)
u=load(B/'source/T2_erratum_result.json');need('T2 eight successful checks',u['checks']==8 and u['fails']==[])
review=(B/'source/T2_review_revision1.md').read_text()
need('literal corrected Cauchy bound','||r F_n|| ||r Delta psi|| = n sqrt(Qn (a + d))' in review and 'Revision 1, 2026-10-29T18:14Z' in review)
for name,n,own in [('t4_n3',3,'counterexample'),('n1_k-1',1,'n1_k-1'),('n1_k0',1,'n1_k0'),('n3_k0',3,'n3_k0')]:
 P={k:Q(v) for k,v in u['examples'][name].items()};O=o['fixtures'][own]
 for k in ['d','p','a','b','Q']:need(name+' same '+k,P[k]==Q(O[k]))
 need(name+' exact cross',P['cross']==n*n*(P['b']-P['p']))
 need(name+' exact Laplacian energy',P['L']==n*n*(P['a']+P['d']))
 need(name+' three corrected Cauchy bounds',P['cross']**2<=n*n*P['Q']*(P['a']+P['d']) and n*n*P['b']**2<=P['Q']*P['a'] and n*n*P['p']**2<=P['Q']*P['d'])
 need(name+' unchanged residual identity',Q(O['R2'])==P['Q']+2*P['cross']+P['L'])
P={k:Q(v) for k,v in u['examples']['t4_n3'].items()}
need('factor3 exact counterexample',P['cross']==Q(64,35)==3*Q(64,105) and Q(64,105)**2==P['Q']*(P['a']+P['d']))
need('017 origin supplied',o['source_generator_count']==2174 and 'CONFIRMED' in o['source_local_integrability'])
need('no new field integration',t['foreign_code_executed'] is False and t['new_candidate_integrals'] is False and c['new_source_integrals'] is False and o['peer_code_executed'] is False)
for rel,h in inputs.items():assert sha(R/rel)==h,rel
for p,h in external.items():assert sha(Path(p))==h,p
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'external_readonly_bindings':external,'checks':checks,'check_count':len(checks),'prefix':63,'individually_integrated_modes':32,'omitted_modes_retained':128,'accepted_T4_group_count':920,'strict_H_gap_lower':str(hgap),'strict_E2_gap_lower':str(egap),'T2_literal_repair':'CONFIRMED missing factor n repaired; all four exact fixtures agree','full_017_upper_E2':'OPEN','new_candidate_integrals':False,'peer_code_executed':False,'verdict':'CONFIRMED finite reciprocal T4-502 acceptance of N4-430/431 and corrected T2 residual review; existing source-specific and analytic premises retained.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],len(checks),'checks',len(inputs),'local',len(external),'external',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
