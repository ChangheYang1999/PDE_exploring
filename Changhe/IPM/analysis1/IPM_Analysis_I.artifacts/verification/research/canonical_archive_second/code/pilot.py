"""Fixed six-span endpoint diagnostic and cost measurement, never a full claim."""
from engine import *
start=now();tick=time.monotonic();src=source();setup_seconds=time.monotonic()-tick;selected=[0,1,2,1555,1556,1557];records={};read_tick=time.monotonic();need(sha(ARCHIVE)==ARCHIVE_SHA,'fixed archive');count=0
with gzip.open(ARCHIVE,'rt') as f:
 head=json.loads(next(f));need(head['spans']==1558 and head['cells']==7809 and head['hashes']['input']==SOURCE_SHA and head['hashes']['normalization']==sha(ZPATH),'actual archive source binding')
 for si,line in enumerate(f):
  if si==1558:
   footer=json.loads(line);need(footer['type']=='complete' and footer['spans']==1558 and not f.read(),'actual complete footer');break
  need(line.endswith('\n'),'complete input line')
  if si in selected:
   r=json.loads(line);need(r['type']=='span' and r['span']==si and q(r['a_exact'])==src['knots'][si] and q(r['b_exact'])==src['knots'][si+1] and q(r['polynomial_mid_exact'])==(src['knots'][si]+src['knots'][si+1])/2,'exact selected geometry');records[si]=r
  count+=1
need(count==1558 and sorted(records)==selected,'all selected source records');read_seconds=time.monotonic()-read_tick;P={};hchecks=0;h_tick=time.monotonic()
for si in selected:
 P[si]=polynomials(src,si);c,w=exact_H_check(P[si],src['knots'][si+1]-src['knots'][si],records[si]['density_polynomials']);hchecks+=c
h_seconds=time.monotonic()-h_tick;I=list(map(ii,src['I0']));J=list(map(ii,src['U0']));C=list(map(ii,src['V0']));out=[];comparisons=0;steps=0;step_tick=time.monotonic()
def compare(si,label,values):
 global comparisons
 target=records[si]['i_left' if label=='I' else 'j_right'];need(len(target)==261,'all moment targets');worst=None
 for n,(v,t) in enumerate(zip(values,target,strict=True),1):
  lo,hi=ends(v);a,b=decode(t)
  if not a<=lo<=hi<=b:raise ValueError(json.dumps({'label':label,'span':si,'mode':n,'candidate':list(map(str,[lo,hi])),'target':list(map(str,[a,b])),'disjoint':hi<a or lo>b}))
  comparisons+=1;margin=min(lo-a,b-hi);relative=margin/(b-a) if b>a else fmpq(0)
  if b>a and (worst is None or relative<worst[0]):worst=(relative,n,v,t)
 need(worst is not None,'nontrivial target');relative,n,v,t=worst;out.append({'span':si,'family':label,'worst_relative_margin':str(relative),'mode':n,'candidate':box(v),'target':list(map(str,decode(t)))})
for si in [0,1,2]:
 compare(si,'I',I);h=src['knots'][si+1]-src['knots'][si]
 for n in range(1,262):I[n-1]=step(I[n-1],P[si][n-1],h,-(2*n+4));steps+=1
for si in [1557,1556,1555]:
 compare(si,'J',[a+b*src['Z'] for a,b in zip(J,C,strict=True)]);h=src['knots'][si+1]-src['knots'][si]
 for n in range(1,262):J[n-1]=step(J[n-1],reverse_poly(P[si][n]),h,4-2*n);C[n-1]*=iv.exp(ii((4-2*n)*h));steps+=1
step_seconds=time.monotonic()-step_tick;need(hchecks==12576 and comparisons==1566 and steps==1566,'all pilot counts');pins={str(p.relative_to(B)):sha(p) for p in [Path(__file__),D/'code/engine.py',D/'PROOF.md',D/'ADDENDUM.md',SOURCE,ARCHIVE,ZPATH,B/'research/modal_repair/PROOF.md',B/'research/modal_repair/evidence/audit_verdict.json']};x={'start_utc':start,'utc':now(),'status':'PASS_SIX_SPAN_ENDPOINT_DIAGNOSTIC_ONLY','iv_dps':iv.dps,'selected_spans':selected,'exact_H_containments':hchecks,'moment_containments':comparisons,'moment_steps':steps,'exact_anchor_checks':src['anchor_checks'],'timing_seconds':{'source':setup_seconds,'archive_read':read_seconds,'exact_polynomials_and_H_checks':h_seconds,'propagation_and_containment':step_seconds,'total':time.monotonic()-tick},'extrapolated_full_poly_and_step_seconds':(h_seconds+step_seconds)*1558/3,'witnesses':out,'files':pins,'scope':'First3 forward and last3 reverse spans only. Timing extrapolation is not guaranteed full cost or full containment. Full813276 moments and3265568H remain unverified.'}
with (D/'evidence/pilot.json').open('x') as f:json.dump(x,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in x.items() if k not in ['files','witnesses']},indent=2))
