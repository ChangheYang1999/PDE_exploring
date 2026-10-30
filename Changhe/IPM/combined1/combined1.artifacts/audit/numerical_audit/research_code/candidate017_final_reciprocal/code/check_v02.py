"""Finite reciprocal endpoint and provenance check. Peer code remains inert."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,gzip,time
from flint import arb,ctx
ctx.prec=4096
ROOT=Path(__file__).resolve().parents[3];B=Path(__file__).resolve().parents[1]
start=time.monotonic();checks={};inputs={};external={}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def need(k,v):
 assert k not in checks,k
 checks[k]=bool(v)
 assert checks[k],k
def local(p,h=None):
 p=Path(p);p=p if p.is_absolute() else ROOT/p;assert p.resolve().is_relative_to(ROOT);key=str(p.relative_to(ROOT));actual=sha(p)
 need('local '+key, h is None or actual==h)
 if key in inputs:need('same local '+key,inputs[key]==actual)
 inputs[key]=actual;return p
def outside(p,h):
 p=Path(p).resolve();key=str(p);actual=sha(p)
 need('external '+key,actual==h)
 if key in external:need('same external '+key,external[key]==actual)
 external[key]=actual;return p
def read(p):return json.loads(Path(p).read_bytes())
m=read(local(B/'source/MANIFEST.json'));local(B/'PROOF.md',m['proof_sha256']);local(Path(__file__));local(B/'ALIAS_PROOF_v02.md')
need('proof before checker',not m['checker_exists'] and not m['result_exists'])
for name,row in m['files'].items():local(B/'source'/name,row['sha256'])
peer=read(B/'source/T4_result.json');pm=read(B/'source/T4_manifest.json');initial=read(B/'source/T4_initial_sources.json');pb=Path(m['peer_base'])
for row in pm:outside(pb/row['local'],row['sha256'])
for i,row in enumerate(initial['sources']):
 raw=(pb/row['local']).read_bytes();raw=gzip.decompress(raw) if row['local'].endswith('.gz') else raw
 need('decoded peer raw '+str(i),hashlib.sha256(raw).hexdigest()==row['raw_sha256'])
for row in initial['checked_peer_graph']:
 # All producer paths are this lane; bind them locally for the final index.
 local(row['source'],row['sha256'])
rp=local('research/candidate017_dual_residual_replay/verification/result.json','7e093982e733237262819ca3ad0486f85bdc4d31c69d73a99e382dbad5c3ab06');r=read(rp)
need('own5704checks',r['check_count']==len(r['checks'])==5704 and all(r['checks'].values()))
need('peer10450checks',peer['check_count']==len(peer['checks'])==10450 and len(set(peer['checks']))==10450)
need('exact raw candidate',r['raw_sha256']==peer['raw_sha256']=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114' and r['candidate']==peer['candidate']=='C1-N1-017-legqs50-quot013')
need('194producerbindings',len(r['inputs'])==len(initial['checked_peer_graph'])==peer['producer_bindings']==194)
for p,h in r['inputs'].items():
 need('producer map '+p,inputs[p]==h)
need('all16dual modes',[v['n'] for v in r['modes']]==[v['n'] for v in peer['rows']]==list(range(1,32,2)))
L=Q(0);coeff=0;energy=0;group_count=0;group_files=0;rows=[]
def group(rec,n,pr):
 global group_count,group_files
 g=read(local(rec['record'],rec['sha256']));need(f'n{n} {rec["kind"]}complete group',g['n']==n and g['kind']==rec['kind']==pr['kind'] and len(g['groups'])==rec['group_count']==pr['groups'] and g['inputs']==r['inputs'])
 need(f'n{n} {rec["kind"]}record overlap',arb(rec['value_ball']).overlaps(arb(pr['replayed_value'])))
 group_count+=len(g['groups']);group_files+=1
for rec,pr in zip(r['modes'],peer['rows'],strict=True):
 n=rec['n'];m0=read(local(rec['record'],rec['sha256']));lf=Q(rec['quotient_strict_lower_exact']);L+=lf*lf
 need(f'n{n} equal directed dual floor',lf>0 and lf==Q(pr['dual_floor_exact'])==Q(m0['dual_quotient_strict_lower_exact']))
 need(f'n{n}completebindings',m0['inputs']==r['inputs'])
 coeff+=m0['dual_exact_coefficient_count'];energy+=m0['dual_beta_count']**2
 need(f'n{n}dualbasiscount',m0['dual_beta_count']==9 and m0['dual_exact_coefficient_count']==pr['energy_coefficient_count']==9*(15-(n-3)//2))
 group(m0['dual_group_record'],n,pr['dual_replay'])
 need(f'n{n}residualscope',rec['independent_hres']==(n in [1,3]) and ('residual_trial' in m0)==('residual_trial' in pr)==(n in [1,3]))
 row={'n':n,'dual_floor_exact':str(lf)}
 if n in [1,3]:
  rr=m0['residual_trial'];pp=pr['residual_trial'];coeff+=rr['coefficient_count'];energy+=rr['beta_count']**2
  need(f'n{n}residualbasiscount',rr['beta_count']==8 and rr['coefficient_count']==8*(15-(n-3)//2))
  for key in ['H_mode_strict_lower_exact','H_mode_strict_upper_exact']:
   need(f'n{n}same '+key,Q(rr[key])==Q(pp[key]));row[key]=rr[key]
  need(f'n{n}residualintervalorder',0<Q(rr['H_mode_strict_lower_exact'])<Q(rr['H_mode_strict_upper_exact']))
  need(f'n{n}residualsquare consistency',arb(rr['residual_square_ball']).overlaps(arb(pp['residual_square'])))
  for key,gp in zip(['pairing','cross','rF_square'],pp['replays'],strict=True):group(rr[key],n,gp)
 rows.append(row)
need('1472coefficients',coeff==peer['coefficient_count']==1472)
need('1424orderedenergypairs',energy==peer['ordered_energy_pair_count']==1424)
need('1339groups22files',group_count==peer['saved_group_count']==1339 and group_files==22)
need('exact sum lower square',L==Q(r['H_lower_square_exact'])==Q(peer['H_lower_square_exact']))
hf=Q(r['H_strict_lower_exact']);need('exact strict whole H floor',hf==Q(peer['H_strict_lower_exact'])==Q(307209799380023711068567013529,5*10**29) and hf>0 and hf*hf<L)
hardy=read(ROOT/'research/candidate017_dual_residual_replay/source/N3_hardy.json');hm=[v['n'] for v in hardy['modes']]
need('160distinctoddHardyinputs',hm==list(range(1,320,2)))
need('onlytworesidualsreplayed',sum(v['independent_hres'] for v in r['modes'])==2)
need('full017upperandE2OPEN',r['complete_H_upper'].startswith('OPEN:') and r['complete_E2_and_017_less_than007'].startswith('OPEN:') and peer['complete_H_upper']==peer['complete_E2_and_017_less_than007']=='OPEN')
need('historicalcodeunobserved',not r['peer_hres_historical_code_matches_frozen_current'] and r['peer_hres_historical_code_sha256_claimed']!=r['peer_hres_frozen_current_code_sha256'])
need('nopeerexecution',not r['peer_code_executed'] and not r['peer_F_cache_read'] and not peer['foreign_code_executed'] and not peer['candidate_integrals_repeated'])
for p,h in inputs.items():need('unchangedlocal '+p,sha(ROOT/p)==h)
for p,h in external.items():need('unchangedexternal '+p,sha(p)==h)
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'inputs':inputs,'external_readonly_bindings':external,'check_count':len(checks),'checks':checks,'candidate':r['candidate'],'raw_sha256':r['raw_sha256'],'coefficient_count':coeff,'ordered_energy_pairs':energy,'groups':group_count,'group_files':group_files,'mode_files':16,'H_lower_square_exact':str(L),'H_strict_lower_exact':str(hf),'rows':rows,'remaining_residual_trials':14,'remaining_Hardy_modes':158,'full_H_upper':'OPEN','complete_E2_and_ordering':'OPEN','peer_programs_executed':False,'candidate_integrals_repeated':False,'scope':'CONFIRMED finite reciprocal agreement with T4-495 and N4-425; only16dual lower trials and2residual-mode enclosures. Source integral soundness remains the accepted N4-425 premise. General Opusreviews inN4-414; specific017identityreview pending separately.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',len(inputs),'local',len(external),'external',out['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
