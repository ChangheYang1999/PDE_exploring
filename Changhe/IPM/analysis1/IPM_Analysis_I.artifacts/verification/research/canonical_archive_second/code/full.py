"""Complete fresh forward/reverse independent moment validation. Never resumes."""
from engine import *
import resource,traceback
E=D/'evidence'
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()+b'\n'
def put(p,v):
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def inputs():
 manifest=json.loads((E/'preflight_manifest.json').read_text());need(manifest['status']=='ACCEPTED_PREPARATION_ONLY','accepted preparation')
 for n,h in manifest['files'].items():need(sha(B/n)==h,'frozen input '+n)
 return manifest

def main():
 start=now();tick=time.monotonic();manifest=inputs();src=source();need(sha(ARCHIVE)==ARCHIVE_SHA,'fixed archive');stream=E/'full_spans.jsonl';counts={'H':0,'I':0,'J':0,'I_steps':0,'J_steps':0};digest=hashlib.sha256();Jtargets=[];context={'stage':'initialization'}
 def emit(f,v):
  raw=canonical(v);f.write(raw);f.flush();digest.update(raw)
 def compare(si,family,values,targets):
  need(len(values)==len(targets)==261,'all target modes');state=hashlib.sha256();worst=None;samples=[]
  for n,(value,target) in enumerate(zip(values,targets,strict=True),1):
   lo,hi=ends(value);a,b=target;record={'span':si,'family':family,'mode':n,'candidate':list(map(str,[lo,hi])),'target':list(map(str,[a,b]))};state.update(canonical(record))
   if not a<=lo<=hi<=b:put(E/'failure_witness.json',{'utc':now(),'failure':'MOMENT_CONTAINMENT','disjoint':hi<a or lo>b,**record});raise ValueError('full containment failed; witness requires independent review')
   counts[family]+=1;margin=min(lo-a,b-hi);relative=margin/(b-a) if a<b else fmpq(0)
   if a<b and (worst is None or relative<q(worst['relative_margin'])):worst={**record,'relative_margin':str(relative)}
   if n in [1,2,3,261]:samples.append(record)
  need(worst is not None,'nonzero radius witness');return {'worst':worst,'samples':samples,'state_sha256':state.hexdigest(),'comparisons':261}
 try:
  with stream.open('xb') as out:
   emit(out,{'type':'header','schema':'ipm-canonical-second-v1','utc':now(),'iv_dps':iv.dps,'source_sha256':SOURCE_SHA,'archive_sha256':ARCHIVE_SHA,'normalization_sha256':sha(ZPATH),'preflight_sha256':sha(E/'preflight_manifest.json'),'full_run':True,'spans':1558,'modes':261,'anchor_checks':src['anchor_checks'],'I0_exact':list(map(str,src['I0'])),'U0_exact':list(map(str,src['U0'])),'V0_exact':list(map(str,src['V0'])),'Z_exact':src['Z_exact']})
   I=list(map(ii,src['I0']))
   with gzip.open(ARCHIVE,'rt') as f:
    head=json.loads(next(f));need(head['type']=='header' and head['spans']==1558 and head['cells']==7809 and head['degree']==7 and head['stream_modes']==261 and head['hashes']['input']==SOURCE_SHA and head['hashes']['normalization']==sha(ZPATH),'complete archive header/source binding')
    for si in range(1558):
     context={'stage':'forward','span':si};line=next(f);need(line.endswith('\n'),'complete archive row');r=json.loads(line);a,b=src['knots'][si:si+2];h=b-a;need(r['type']=='span' and r['span']==si and q(r['a_exact'])==a and q(r['b_exact'])==b and q(r['polynomial_mid_exact'])==(a+b)/2,'all exact original geometry');need(len(r['i_left'])==len(r['j_right'])==261,'all archive moment shapes');P=polynomials(src,si);count,worstH=exact_H_check(P,h,r['density_polynomials']);counts['H']+=count;Itarget=list(map(decode,r['i_left']));Jtargets.append(list(map(decode,r['j_right'])));record=compare(si,'I',I,Itarget)
     # Save one predetermined nonzero-mode polynomial coefficient as an extra target audit.
     hj=int.from_bytes(hashlib.sha256((SOURCE_SHA+':H:'+str(si)).encode()).digest()[:4],'big')%261;power=si%8;he=sum((P[hj][k]*comb(k,power)/fmpq(2)**(k-power) for k in range(power,8)),fmpq(0))/h**power;hl,hr=decode(r['density_polynomials'][hj][power]);need(hl<=he<=hr,'selected exact H');selectedH={'mode':hj,'power':power,'exact':str(he),'target':list(map(str,[hl,hr]))}
     emit(out,{'type':'forward','utc':now(),'span':si,'a_exact':str(a),'b_exact':str(b),'archive_line_sha256':hashlib.sha256(line.encode()).hexdigest(),'H_count':count,'worst_H':worstH,'selected_H':selectedH,**record})
     for n in range(1,262):I[n-1]=step(I[n-1],P[n-1],h,-(2*n+4));counts['I_steps']+=1
     if si%50==0:print(json.dumps({'utc':now(),'stage':'forward','span':si,'counts':counts,'seconds':time.monotonic()-tick}),flush=True)
    footer=json.loads(next(f));need(footer['type']=='complete' and footer['spans']==1558 and footer['cells']==7809 and not f.read(),'complete archive footer and no trailing data')
   J=list(map(ii,src['U0']));C=list(map(ii,src['V0']))
   for si in reversed(range(1558)):
    context={'stage':'backward','span':si};a,b=src['knots'][si:si+2];h=b-a;record=compare(si,'J',[v+c*src['Z'] for v,c in zip(J,C,strict=True)],Jtargets[si]);emit(out,{'type':'backward','utc':now(),'span':si,'a_exact':str(a),'b_exact':str(b),**record});P=polynomials(src,si)
    for n in range(1,262):J[n-1]=step(J[n-1],reverse_poly(P[n]),h,4-2*n);C[n-1]*=iv.exp(ii((4-2*n)*h));counts['J_steps']+=1
    Jtargets[si]=None
    if si%50==0:print(json.dumps({'utc':now(),'stage':'backward','span':si,'counts':counts,'seconds':time.monotonic()-tick}),flush=True)
   need(counts=={'H':3265568,'I':406638,'J':406638,'I_steps':406638,'J_steps':406638},'all complete counters');prefix=digest.hexdigest();out.write(canonical({'type':'complete','utc':now(),'counts':counts,'prefix_sha256':prefix}));out.flush();os.fsync(out.fileno())
  inputs();need(sha(ARCHIVE)==ARCHIVE_SHA and sha(SOURCE)==SOURCE_SHA,'immutable source after full computation');result={'start_utc':start,'utc':now(),'status':'COMPUTED_FULL_REQUIRES_OUTPUT_AUDIT','counts':counts,'archive_footer_read':True,'exact_anchor_checks':3915,'iv_dps':iv.dps,'output_sha256':sha(stream),'preflight_sha256':sha(E/'preflight_manifest.json'),'producer_sha256':sha(Path(__file__)),'engine_sha256':sha(D/'code/engine.py'),'seconds':time.monotonic()-tick,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Complete directed containment by an independent propagation engine, pending separate output audit and actual-output model review. Shared exact trial and accepted normalization interval. No derivative or IPM endpoint.'};put(E/'full_summary.json',result);print(json.dumps(result),flush=True)
 except Exception as exc:
  put(E/'full_failure.json',{'utc':now(),'status':'OPEN_FAILED_SUFFICIENT_CHECK_REQUIRES_WITNESS_REVIEW','context':context,'error':str(exc),'counts':counts,'seconds':time.monotonic()-tick,'traceback':traceback.format_exc()});raise
if __name__=='__main__':main()
