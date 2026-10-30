"""Finite reciprocal fixtures, literal repair and exact source-origin inspection."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,time,sys,difflib
B=Path(__file__).resolve().parents[1];start=time.monotonic();sys.set_int_max_str_digits(0)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
checks=[]
def ck(k,v):assert v,k;checks.append(k)
for row in read('data/manifest.json'):ck('binding '+row['local'],sha(B/row['local'])==row['sha256'])
first=read('data/PROOF_FIRST.json');ck('proof first',first['proof_sha256']==sha(B/'PROOF.md') and first['checker_exists'] is False)
for row in read('data/initial_sources.json')['rows']:ck('frozen source '+row['local'],sha(B/row['local'])==row['sha256'])
peer=read('source/N4_result.json');prior=read('../candidate017_residual_review_acceptance/verification/result.json');t2=read('source/T2_erratum_result.json');external={row['source']:row['sha256'] for row in read('data/external_bindings.json')['rows']}
ck('N4 documented finite checks',peer['check_count']==len(peer['checks'])==2290 and all(peer['checks'].values()))
ck('all257 external source bindings',len(external)==len(peer['inputs'])==257)
peerroot=Path('RUN_ROOT/numerics_audit_N4')
for rel,h in peer['inputs'].items():ck('producer source '+rel,external[str(peerroot/rel)]==h)
ck('own501 accepted exact fixtures',prior['check_count']==len(prior['checks'])==398)
ck('T2 erratum8checks',t2['checks']==8 and t2['fails']==[] and '8 checks, 0 FAIL' in (B/'source/T2_erratum_log.txt').read_text())
old=(B/'../candidate017_residual_review_acceptance/source/T2_review.md').read_text().splitlines();new=(B/'source/T2_review_revision1.md').read_text().splitlines();changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
 if tag!='equal':changes.append({'tag':tag,'old_lines':[a+1,b],'new_lines':[c+1,d],'old':old[a:b],'new':new[c:d]})
ck('every changed block frozen',changes==read('data/review_changes.json') and len(changes)==3)
ck('exact bound repaired',changes[1]['old']==['- the cross term is bounded by ||r F_n|| ||r Delta psi|| = sqrt(Qn (a + d)) (using Step 2).'] and changes[1]['new']==['- the cross term is bounded by ||r F_n|| ||r Delta psi|| = n sqrt(Qn (a + d)), since ||r Delta psi|| = n sqrt(a + d)','  by Step 2 (revision 1: the 18:07Z text omitted the factor n).'])
ck('other edits only provenance',all(c['tag']=='insert' and not c['old'] for c in [changes[0],changes[2]]))
fixtures={}
for name,n in [('n1_k-1',1),('n1_k0',1),('n3_k0',3),('t4_n3',3)]:
 own=prior['counterexample'] if name=='t4_n3' else prior['examples'][name];row=t2['examples'][name];foreign=peer['fixtures']['counterexample' if name=='t4_n3' else name]
 for k,v in row.items():ck(name+' T2 exact '+k,Q(v)==Q(own['lap2' if k=='L' else k]))
 for k in ['d','a','p','b','Q','R2']:ck(name+' N4 exact '+k,Q(foreign[k])==Q(own[k]))
 d,a,p,b,q,c,l=[Q(row[k]) for k in ['d','a','p','b','Q','cross','L']]
 ck(name+' corrected squared bounds',q>0 and d>0 and a>=0 and l==n*n*(a+d) and c==n*n*(b-p) and c*c<=n*n*q*(a+d) and n*n*b*b<=q*a and n*n*p*p<=q*d)
 fixtures[name]={k:str(Q(v)) for k,v in row.items()}
x=prior['counterexample'];q,a,d,c=[Q(x[k]) for k in ['Q','a','d','cross']]
ck('counterexample factor3 exact',c==q==Q(64,35) and q*(a+d)==Q(64,105)**2 and c*c==9*q*(a+d)>q*(a+d))
for k in ['d','a','p','b','Q','R2']:ck('Riesz same '+k,Q(peer['fixtures']['riesz'][k])==Q(prior['known_riesz'][k]))
ck('known Riesz H squares',Q(peer['fixtures']['riesz']['H2'])==Q(prior['known_riesz']['H2_over_pi'])==Q(4,15) and Q(peer['fixtures']['riesz']['residual_H2'])==Q(prior['known_riesz']['residual_H2_over_pi'])==Q(9,280))
rawpath=B/'../candidate017_point/data/candidate017.json';raw=read('../candidate017_point/data/candidate017.json');ck('exact candidate raw hash',sha(rawpath)=='7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114');ck('exact c',Q(raw['cl_exact'])==Q(4076476460239181,2251799813685248))
counts=Counter();radii=set();arity={'mono':2,'leg':3,'legq':4,'legqs':5}
for i,g in enumerate(raw['generators']):
 spec=g['spec'];kind=spec[0];ck(f'generator{i} complete type',kind in arity and len(spec)==arity[kind]);m,j,w=g['m'],g['j'],spec[1];deg=0 if kind=='mono' else spec[2];q=spec[3] if kind in ('legq','legqs') else 0;rad=Q(spec[4]) if kind=='legqs' else Q(1)
 ck(f'generator{i} smooth factors',all(type(v) is int and v>=0 for v in (m,j,w,deg,q)) and rad>0 and not isinstance(g['coef'],float) and Q(g['coef']).denominator>0)
 counts[kind]+=1;radii.add(rad)
ck('complete2174source generators',len(raw['generators'])==peer['source_generator_count']==2174 and dict(counts)==peer['source_kinds']=={'mono':262,'leg':1660,'legqs':252})
ck('positive exact radii',sorted(radii)==[Q(v) for v in peer['positive_source_radii']]==[1,50])
ck('origin source premise explicit','CONFIRMED from smooth finite potential' in peer['source_local_integrability'])
ck('full017 upperE2 remainsOPEN',peer['full_017_upper_E2']=='OPEN')
ck('no peer execution or integration',peer['peer_code_executed'] is False and peer['peer_quadratures_repeated'] is False and peer['new_candidate_integrals'] is False)
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'changed_review_blocks':len(changes),'external_source_binding_count':len(external),'source_generator_count':len(raw['generators']),'source_kinds':dict(counts),'positive_source_radii':[str(x) for x in sorted(radii)],'fixtures':fixtures,'T2_revision1_sha256':sha(B/'source/T2_review_revision1.md'),'N4_result_sha256':sha(B/'source/N4_result.json'),'source_local_integrability':'CONFIRMED, smooth finite canonical potential and F odd in y imply F_n=O(r) at zero','foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED T2 revision1 missing-n literal repair and N4-432 analytic/source-origin acceptance. All2174 raw generators inspected. Full017 H upper,E2 and017<007 remain OPEN.'}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(result['utc'],len(checks),'checks',result['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
