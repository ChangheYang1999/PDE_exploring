from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_direct_quadrature_spotcheck';V=R/'verification';dest=V/'FINAL_BINDINGS.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('bind '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'DESIGN_REPAIRS_PROOF.md',R/'DESIGN_REVIEW_RESOLUTION.md',R/'FINAL_ACCEPTANCE_PROOF.md',R/'RESULTS_REVIEWED_DRAFT.md',R/'RESULTS.md',R/'RESULTS_REVIEW_RESOLUTION.md',R/'FOLLOWUP_RESOLUTION.md',V/'INDICATOR_COMPARISON.json',V/'RUN_PROCESS.json',ROOT/'runs/primary_direct_quadrature.log']:bind(p)
for p,status,count in [(V/'CHECKS.json','PASS_DIRECT_PRIMARY_QUADRATURE_REVIEW_PENDING',174),(V/'MANUFACTURES.json','PASS_DIRECT_PRIMARY_MANUFACTURES',51)]:
 d=json.loads(bind(p));ck('accepted record '+p.name,d['status']==status and d['count']==count==len(d['checks'])and all(c['passed']for c in d['checks']))
 for q,h in d['bindings'].items():bind(q,h)
design=json.loads(bind(V/'DESIGN_ACCEPTANCE.json'));ck('accepted design',design['status']=='ACCEPTED_DIRECT_PRIMARY_DESIGN')
for p,h in design['bindings'].items():bind(p,h)
old=ROOT/'research/primary_fresh_sample/verification/FINAL_BINDINGS.json';d=json.loads(bind(old,'8647310f5bf4595c0e2073859ec663103c53ae9cefbc1f32313afc9a3878d5bd'));ck('accepted336',d['status']=='CONFIRMED_FINITE_PRIMARY_FRESH_SAMPLE'and d['count']==341==len(d['checks'])and all(c['passed']for c in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
r=json.loads(bind(V/'RESULTS.json'));ex=json.loads(bind(V/'JOB_EXIT.json'));ck('successful actual run',r['status']=='COMPLETE_DIRECT_PRIMARY_QUADRATURE'and ex['returncode']==0)
ck('resource records',r['nice']==19 and all(v=='1'for v in r['environment'].values())and r['memory_limits']==[14*1024**3]*2)
ck('chronology',datetime.fromisoformat(design['utc'])<=datetime.fromisoformat(r['started_utc'])<datetime.fromisoformat(r['finished_utc'])<=datetime.fromisoformat(ex['utc']))
ind=json.loads(bind(V/'INDICATOR_COMPARISON.json'));rows=r['rows'];ck('three orders',[x['order']for x in rows]==[96,192,384]);ratios=[abs(F(x['differences']['R']))/F(x['conditioning']['epsilon_R_indicator'])for x in rows];pd=[abs(F(a['values']['R'])-F(b['values']['R']))for i,a in enumerate(rows)for b in rows[i+1:]];maxind=max(F(x['conditioning']['epsilon_R_indicator'])for x in rows)
ck('all reference differences exceed indicator',min(ratios)>1 and ind['all_reference_differences_exceed_indicator']and ind['reference_error_indicator_ratios']==[float(x)for x in ratios]);ck('all pairwise differences exceed every indicator',min(pd)>maxind and ind['every_pairwise_difference_exceeds_every_indicator']and ind['minimum_pairwise_residual_difference']==float(min(pd))and ind['maximum_indicator']==float(maxind))
reviews=[]
for label in ['design','design_followup','results','results_followup']:
 a=V/('opus_'+label);m=json.loads(bind(a/'metadata.json'));raw=json.loads(bind(a/'response.json'));q=bind(a/'request.txt');ans=bind(a/'answer.md');ck('actual Opus5.5 '+label,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==raw['model']=='claude-opus-5-5'and m['stop_reason']==raw['stop_reason']=='end_turn'and m['answer_nonempty']and bool(ans.strip())and m['request_sha256']==hashlib.sha256(q).hexdigest())
 if label.startswith('results'):ck('actual check version in review '+label,hashlib.sha256((V/'CHECKS.json').read_bytes()).hexdigest().encode()in q)
 reviews.append(dict(label=label,request_id=m['request_id'],model=m['returned_model'],finished_utc=m['finished_utc']))
for p,h in bindings.items():ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINITE_DIRECT_PRIMARY_QUADRATURE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,primary_verdict='UNRESOLVED',scope='One actual N44 point. Separate full-plane Gaussian quadrature and analytic polar derivatives empirically agree with336. Exact recombination and recorded finite differences; no inverse error enclosure, uniform residual, error-cause attribution, continuum convergence or decisive endpoint.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print('sha256',hashlib.sha256(dest.read_bytes()).hexdigest())
