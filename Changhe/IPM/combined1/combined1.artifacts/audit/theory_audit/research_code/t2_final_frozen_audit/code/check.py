"""Final T2 text and exact rational examples, without peer execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import difflib,hashlib,json,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert v,k
 checks.append(k)
for r in read('data/manifest.json'):need('binding '+r['local'],sha(B/r['local'])==r['sha256'])
need('proof precedes checker',not read('data/PROOF_FIRST.json')['checker_exists'] and read('data/PROOF_FIRST.json')['proof_sha256']==sha(B/'PROOF.md'))
doc=(B/'source/T2_FINAL_SUMMARY.md').read_text();flat=' '.join(doc.split());old=(B/'../t2_summary_repair_acceptance/source/T2_FINAL_SUMMARY.md').read_text()
need('finaltarget',sha(B/'source/T2_FINAL_SUMMARY.md')=='13cd15cdadfcc1ac07e94dd08157d5740f66e8ee98ab54ecc658fdcfb6722a0f')
need('692lines',len(doc.splitlines())==692);changes=[]
for tag,a,b,c,d in difflib.SequenceMatcher(None,old.splitlines(),doc.splitlines()).get_opcodes():
 if tag!='equal':changes.append(dict(tag=tag,old_start=a+1,old_stop=b,new_start=c+1,new_stop=d))
need('4changedblocks',len(changes)==4 and changes==read('data/changes.json'))
for topic,n in [('t2_summary_repair_acceptance',80),('candidate017_residual_review_acceptance',398),('candidate017_review_repair_acceptance',4710)]:
 r=read('../'+topic+'/verification/result.json');need('accepted '+topic,r['check_count']==n==len(r['checks']))
need('currentreview accepted503',sha(B/'source/T2_review.md')==sha(B/'../candidate017_review_repair_acceptance/source/T2_review_revision1.md'))
need('oldreview preserved501',sha(B/'source/T2_review_1807.md')==sha(B/'../candidate017_residual_review_acceptance/source/T2_review.md'))
r=read('../candidate017_review_repair_acceptance/verification/result.json');need('2174originchecked',r['source_generator_count']==2174 and sum(r['source_kinds'].values())==2174)
f=r['fixtures']['t4_n3'];need('missing n fixture',Q(f['cross'])==Q(64,35) and Q(f['Q'])*(Q(f['a'])+Q(f['d']))==Q(64,105)**2 and 3*Q(64,105)==Q(64,35))
src=read('../candidate017_residual_review_acceptance/source/T2_result.json');examples=[]
for key,n,want in [('n1_k-1',1,Q(63,110)),('n1_k0',1,Q(667,945)),('n3_k0',3,Q(349,210))]:
 z=src['examples'][key];d,p,a,b,q=map(Q,[z[k] for k in ['d','p','a','b','Q']]);v=q+2*n*n*(b-p)+n*n*(a+d)
 need('fixture '+key,v==Q(z['R2'])==want);need('positive energies '+key,min(d,a,q,v)>0);examples.append(dict(name=key,R2_over_pi=str(v)))
z=src['riesz_example'];d,p,a,b,q=map(Q,[z[k] for k in ['d','p','a','b','Q']]);v=q+2*(b-p)+a+d;h=Q(z['H2_over_pi']);g=Q(z['residual_H2_over_pi'])
need('Riesz exactR',v==Q(z['R2'])==Q(1959,20020));need('Riesz H',h==Q(4,15));need('residualHdistinct',g==Q(9,280)<v);need('duality',p*p<=d*h);need('triangle sign',d+h-v>0);need('triangle squared',(d+h-v)**2<=4*d*h)
for phrase in ['Rn^2 = Qn + 2 n^2 (b - p) + n^2 (a + d)','n sqrt(Qn (a + d))','3 + 2 k_i - n even and >= 0','F_n integrable near the origin is a fact the 017 source must supply','from its 2174 exact generators','no 017 number reviewed','Rn^2/pi = 63/110, 667/945, 349/210','H(F)^2/pi = 4/15, Rn^2/pi = 1959/20020','T4-503','T4-499','The 18:07Z text is kept']:
 need('scope '+phrase,phrase in flat)
review=' '.join((B/'source/T2_review.md').read_text().split());need('critical exponent concrete fixture','At beta = 3/2 (n = 1, k = 0)' in review)
for r in read('data/manifest.json'):need('unchanged '+r['local'],sha(B/r['local'])==r['sha256'])
out=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,check_count=len(checks),checks=checks,proof_sha256=sha(B/'PROOF.md'),checker_sha256=sha(Path(__file__)),target_sha256=sha(B/'source/T2_FINAL_SUMMARY.md'),changed_blocks=4,examples=examples,Riesz_R2_over_pi=str(v),verdict='CONFIRMED all four final-summary additions under the accepted hypotheses. Critical beta divergence refers to the named single trial, not every finite sum. Full017 upper,E2 and actual correction-distance ordering remain OPEN. No new theorem or candidate verdict.',foreign_code_executed=False,new_candidate_integrals=False)
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('PASS',len(checks),'checks',out['elapsed_seconds'],'seconds')
